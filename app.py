from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import boto3
from botocore.exceptions import NoCredentialsError
import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get AWS credentials and configuration from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Initialize the S3 client with the credentials
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

app = FastAPI()

# Upload file to S3 bucket
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Check if the file already exists in S3
        existing_files = s3.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=file.filename)

        if existing_files.get('KeyCount', 0) > 0:
            raise HTTPException(status_code=400, detail=f"File '{file.filename}' already exists.")

        # Upload the file to S3 with Server-Side Encryption (SSE-S3)
        s3.upload_fileobj(
            file.file, 
            S3_BUCKET_NAME, 
            file.filename,
            ExtraArgs={'ServerSideEncryption': 'AES256'}  # SSE-S3 encryption
        )
        return {"message": f"File '{file.filename}' uploaded successfully"}
    
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="AWS Credentials not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

# Download file from S3 bucket (generates a presigned URL)
@app.get("/download/{filename}")
async def download_file(filename: str):
    try:
        # Generate a presigned URL for the file download
        file_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': S3_BUCKET_NAME, 'Key': filename},
            ExpiresIn=3600  # URL expiration time in seconds
        )
        return JSONResponse(content={"url": file_url})
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found or download failed: {str(e)}")

# Share file (generates a presigned URL for sharing)
@app.post("/share/{filename}")
async def share_file(filename: str):
    try:
        # Generate a presigned URL for sharing
        share_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': S3_BUCKET_NAME, 'Key': filename},
            ExpiresIn=3600  # Link expires in 1 hour
        )
        return {"shareable_url": share_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not generate shareable URL: {str(e)}")

# Delete file from S3
@app.delete("/delete/{filename}")
async def delete_file(filename: str):
    try:
        # Delete the file from S3
        s3.delete_object(Bucket=S3_BUCKET_NAME, Key=filename)
        return {"message": f"File '{filename}' deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found or could not be deleted: {str(e)}")

# Start the FastAPI app with Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Cloud-Based Storage System

## Table of Contents
- [Overview](#overview)
- [Project Objectives](#project-objectives)
- [Target Audience](#target-audience)
- [Assessment Deliverables](#assessment-deliverables)
- [How to Run the Project](#how-to-run-the-project)
- [License](#license)
- [Conclusion](#conclusion)

## Overview
The **Cloud-Based Storage System** project is an online initiative designed to address real-world business challenges. Offered through Qureos, this project aims to evaluate the technical skills of prospective engineers for Accenture, a leading global IT services company. The assessment focuses on designing a robust system architecture, implementing backend services for file management, and ensuring data security.

## Project Objectives
The primary objective of this project is to assess applicants' technical competencies in key areas, including:
- Cloud computing skills
- Backend development capabilities
- Strong understanding of data security principles

## Target Audience
This project is intended for:
- Individuals aspiring to become **Cloud Engineers**
- Professionals seeking to enhance their technical skills in a practical environment
- Anyone looking to showcase their technical abilities to potential employers

## Assessment Deliverables
This assessment consists of three key deliverables:
1. **Designing a System Architecture**: Creating a scalable and secure architecture for the cloud-based storage service.
2. **Implementing Backend Services**: Developing backend functionalities necessary for efficient file management.
3. **Ensuring Data Security**: Implementing robust security measures to protect user data and comply with data privacy regulations.

## How to Run the Project
To run the **Cloud-Based Storage System** locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mado007/Cloud-Based-Storage-System
   cd Cloud-Based-Storage-System
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your AWS credentials:
   ```plaintext
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_REGION=your_region
   S3_BUCKET_NAME=your_bucket_name
   ```

6. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API**:
   Open your browser or use a tool like Postman to interact with the API:
   - Upload a file: `POST http://127.0.0.1:8000/upload/`
   - Download a file: `GET http://127.0.0.1:8000/download/{filename}`
   - Share a file: `POST http://127.0.0.1:8000/share/{filename}`
   - Delete a file: `DELETE http://127.0.0.1:8000/delete/{filename}`

## License
This project is licensed under the [MIT License](LICENSE). Feel free to explore, modify, and distribute the codebase. For any questions or feedback, please contact us at [Mahmoud Eid](mailto:eng.mahmod.eid.elsayed@gmail.com).

## Conclusion
The **Cloud-Based Storage System** project serves as a vital stepping stone for aspiring engineers to validate their technical skills and address real-world business problems. Through this initiative, we aim to identify and nurture talent for the IT industry, ensuring a pool of skilled professionals ready to meet the demands of the evolving tech landscape.

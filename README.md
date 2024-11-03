# Cloud-Based Storage System

## Table of Contents
- [Overview](#overview)
- [Project Objectives](#project-objectives)
- [Security Measures](#Security-Measures)
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

## Security Measures

This project includes multiple security features to ensure that all data stored and transmitted through the cloud-based storage system is protected.

### 1. File Encryption (SSE-S3)
We implemented **Server-Side Encryption (SSE-S3)** to encrypt all files at rest. Files uploaded to the S3 bucket are automatically encrypted using **AES-256**, ensuring that sensitive data remains secure while stored.

- **Why:** SSE-S3 protects data against unauthorized access at the storage layer.
- **How:** Every file upload request is configured to use AES-256 encryption by default.

### 2. Secure Data Transmission (TLS Encryption)
All data transmitted between the client and the cloud service uses **Transport Layer Security (TLS)**, ensuring that the data in transit is encrypted and secure from man-in-the-middle (MITM) attacks.

- **Why:** TLS ensures that data sent over the network is encrypted and protected during transmission.
- **How:** AWS S3 and FastAPI both support TLS, securing data transmission during API interactions.

### 3. User Authentication (OAuth 2.0)
We use **OAuth 2.0** to authenticate and authorize users. The system generates and verifies JWT tokens, ensuring that only authorized users can interact with the API endpoints.

- **Why:** OAuth 2.0 ensures that only authenticated users can access or modify files, providing strong user identity verification.
- **How:** Users must obtain a JWT token via the `/token` endpoint and include it in all subsequent API requests.

### 4. Access Control (RBAC)
Role-Based Access Control (RBAC) is used to manage permissions. Users are assigned roles (e.g., Admin, User), and access is granted based on the role they hold.

- **Why:** RBAC allows us to restrict or grant access to specific resources or actions based on user roles.
- **How:** Set up IAM roles and policies within AWS to manage user permissions for accessing or managing S3 objects.


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


# FastAPI Wallet API with NeonDB and Docker

A wallet management backend built with FastAPI, PostgreSQL-compatible NeonDB, and Docker containerization.  
Includes API endpoints for user management, wallet updates, and transaction history, documented with Swagger UI.

---

**Deployed on Render:** [https://fastapi-wallet.onrender.com/](https://fastapi-wallet.onrender.com/)

## Features

- List all users with wallet balances  
- Add or update wallet amount for a user  
- Fetch wallet transactions by user  
- FastAPI automatic Swagger documentation  
- Containerized with Docker for easy deployment  
- Uses NeonDB serverless Postgres backend  

---

## Project Structure

```
fastapi-wallet/
├── app/                    # FastAPI application code
├── doc/                    # Documentation files (OpenAPI spec)
├── .env                    # Environment variables (not committed to repo)
├── Dockerfile              # Docker setup to build and run the app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Setup and Running Locally

### Prerequisites

- Python 3.11+  
- Docker installed (optional, for containerization)  
- NeonDB account and connection string  

### Clone the repo

```
git clone https://github.com/VathareVinayak/AMRR-TechSols-Pvt-Ltd-Task.git
cd AMRR-TechSols-Pvt-Ltd-Task
```

### Create `.env` file

Create a `.env` file in the project root with this content:

```
DATABASE_URL=postgresql://user:password@host:port/database?sslmode=require
```

Replace with your actual NeonDB credentials.

---

### Install dependencies (without Docker)

```
pip install -r requirements.txt
```

### Run the app locally

```
uvicorn app.main:app --reload
```

Access Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## Docker Setup

### Build Docker image

Run in project root:

```
docker build -t fastapi-wallet .
```

### Run Docker container

```
docker run -p 10000:10000 --env-file .env fastapi-wallet
```

Access Swagger docs:

```
http://localhost:10000/docs
```

---

## API Endpoints

| Method | Endpoint                       | Description                                 |
|--------|--------------------------------|---------------------------------------------|
| GET    | `/users`                      | List all users with wallet balances        |
| PUT    | `/users/{user_id}/wallet`     | Add/update wallet amount for a user        |
| GET    | `/users/{user_id}/transactions` | Fetch wallet transactions for a user      |

---

## Screenshots

### API Testing : Postman

![Swagger UI Screenshot](./doc/Screenshots/swagger_doc.png)

### Running Docker Container

![Docker Container Screenshot](./doc/Screenshots/docker_running.png)

### Render Deployment Successful

![Render Deployment Screenshot](./doc/Screenshots/render_deploy.png)

---

## Contact

Vinayak Vathare  
Email: vinayak.vathare2004@gmail.com

GitHub: [VathareVinayak](https://github.com/VathareVinayak)

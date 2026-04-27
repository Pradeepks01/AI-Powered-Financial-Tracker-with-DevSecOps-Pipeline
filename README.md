# AI-Powered Financial Tracker with DevSecOps Pipeline

![Architecture Diagram](https://raw.githubusercontent.com/Pradeepks01/AI-Powered-Financial-Tracker-with-DevSecOps-Pipeline/feat/gitops-eks/docs/architecture.png)

## 🚀 Overview
The **AI-Powered Financial Tracker** is a state-of-the-art FastAPI application designed to help users manage their finances with AI-driven insights. This project demonstrates a complete **DevSecOps lifecycle**, from automated secure builds to GitOps-based deployment on AWS EKS.

## 🏗️ Architecture
The project follows a modern cloud-native architecture:
- **Frontend/API**: FastAPI backend providing RESTful endpoints.
- **AI Engine**: Integrated with Ollama for intelligent financial analysis.
- **Database**: MySQL for persistent storage of transactions and accounts.
- **CI/CD**: GitHub Actions for building, scanning, and pushing Docker images.
- **GitOps**: ArgoCD for automated synchronization between Git manifests and the EKS cluster.
- **Infrastructure**: AWS EKS (Elastic Kubernetes Service) provisioned via Terraform.
- **Ingress & Security**: Envoy Gateway for traffic management and Cert-Manager for automated TLS.

## 🛠️ Technology Stack
- **Languages**: Python 3.12+
- **Frameworks**: FastAPI, SQLAlchemy, Pydantic v2
- **Containerization**: Docker
- **Orchestration**: Kubernetes (AWS EKS)
- **Infrastructure as Code**: Terraform
- **CI/CD & GitOps**: GitHub Actions, ArgoCD, Trivy (Security Scanning)

## 📂 Project Structure
```text
├── .github/workflows/   # CI/CD Pipeline definitions
├── argocd/              # ArgoCD Application manifests
├── k8s/                 # Kubernetes Deployment, Service, and Config manifests
├── src/                 # FastAPI Source Code
│   ├── api/             # API Endpoints
│   ├── core/            # Core Configuration & Security
│   ├── models/          # Database Models
│   └── services/        # AI & Business Logic
├── terraform/           # IaC for AWS VPC & EKS
├── main.py              # Application Entry Point
└── Dockerfile           # Multi-stage Docker build
```

## 🔐 DevSecOps Pipeline
Our pipeline ensures high security and reliability:
1. **Push**: Developer pushes code to the `feat/gitops-eks` branch.
2. **Build**: GitHub Actions builds the Docker image.
3. **Scan**: (Optional) Security scanning with Trivy.
4. **Publish**: Secure image is pushed to DockerHub (`pradeepks18/ai-financial-tracker-eks`).
5. **Update**: Manifests in `k8s/` are updated with the new image SHA.
6. **Deploy**: ArgoCD detects the change and synchronizes the cluster state.

## 🚦 Getting Started
1. **Local Development**:
   ```bash
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
2. **Infrastructure Setup**:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```
3. **Deployment**:
   Ensure your GitHub Secrets (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`) are configured to enable the automated pipeline.

---
*Maintained by Pradeepks01*

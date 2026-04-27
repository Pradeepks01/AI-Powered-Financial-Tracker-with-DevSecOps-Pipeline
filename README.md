# 💰 AI-Powered Financial Tracker with DevSecOps Pipeline

**A premium, state-of-the-art financial management tool with an integrated AI advisor, secured by an industry-leading DevSecOps pipeline on Amazon EC2.**

---

## 🏗️ Architecture & Features

- **🧠 AI Advisor**: Context-aware financial assistant powered by Ollama (TinyLlama), self-hosted for maximum privacy.
- **🌓 Premium UI**: Stunning Glassmorphism dashboard with Dark/Light mode and separate Login/Register pages.
- **🔐 Secure Auth**: Python-based security with **BCrypt password hashing** and **JWT authentication**.
- **📊 Observability**: Built-in Prometheus metrics via `/actuator/prometheus`.

## 🚀 DevSecOps Pipeline Stages

The CI/CD pipeline enforces **9 sequential security gates** before any code reaches production:

| Stage | Tool | Description |
| :--- | :--- | :--- |
| **1. Secret Scan** | **Gitleaks** | Scans entire Git history for leaked secrets and sensitive data. |
| **2. Lint** | **Flake8** | Enforces Python (PEP8) coding standards for high-quality code. |
| **3. SAST** | **Semgrep** | Scans Python source code for security flaws and OWASP Top 10 vulnerabilities. |
| **4. SCA** | **Pip-audit** | Scans Python dependencies for known CVEs (Software Composition Analysis). |
| **5. Build** | **Docker** | Packages the application into a secure, production-ready container image. |
| **6. Container Scan** | **Trivy** | Scans the Docker image for OS and library-level vulnerabilities. |
| **7. Push** | **Amazon ECR** | Pushes the verified image to AWS ECR only after security scans pass. |
| **8. Deploy** | **SSH / Docker Compose** | Automated deployment to AWS EC2 using rebranded manifests. |
| **9. DAST** | **OWASP ZAP** | Performs dynamic attack surface scanning on the live application. |

---

## 🚢 Technical Implementation

### Frontend (High-Fidelity UI/UX)
- **Glassmorphism Interface**: Using Tailwind CSS and Vanilla JS for a lightweight but premium feel.
- **Dynamic Dashboard**: Real-time stats for Income, Expenses, and Net Savings.
- **Separate Auth Flow**: Dedicated `login.html` and `register.html` for a professional user experience.

### Backend (Python FastAPI)
- **Asynchronous Engine**: Built with FastAPI for high-speed data retrieval.
- **Security**: Integrated JWT flow with `passlib` for secure credential handling.
- **Database**: Relational data persistence using MySQL 8.0.

### 📂 Directory Structure
```text
├── .github/workflows/    # CI/CD DevSecOps Pipeline (GitHub Actions)
├── scripts/              # Setup and utility scripts (e.g., Ollama model pull)
├── src/                  # FastAPI Backend Source Code
│   ├── api/              # API Endpoints (Auth, Chat, Entries)
│   ├── core/             # Configuration and Security (JWT, Hashing)
│   ├── db/               # Database Connection and Models
│   └── schemas/          # Pydantic Validation Schemas
├── templates/            # Frontend HTML (Glassmorphism UI)
├── app-tier.yml          # Production Docker Compose for EC2
├── docker-compose.yml    # Local Development Docker Compose
└── Dockerfile            # Multi-stage optimized Docker build
```

---

## 🚀 Quick Start

### 1. Local Development (Docker)
```bash
docker-compose up --build
```
Access the dashboard at `http://localhost:8000`.

### 2. AWS Secrets Manager
Create a secret named `financial-tracker/prod-secrets` with the following keys:
`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `OLLAMA_URL`.

---

**Developed for the DevSecOps community.** 🚀
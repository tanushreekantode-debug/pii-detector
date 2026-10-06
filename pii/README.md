# 🔐 PII Detector — AWS Powered

A full-stack **Personally Identifiable Information (PII) Detection System** that scans text and identifies sensitive information such as names, email addresses, phone numbers, Aadhaar numbers, PAN numbers, credit card numbers, and other potentially sensitive data.

The application provides a modern web interface where users can submit text and receive detected PII entities with their types, locations, and confidence information.

---

## 🚀 Features

* 🔍 Detect Personally Identifiable Information (PII) from text
* 📧 Email address detection
* 📱 Phone number detection
* 👤 Person/name detection
* 🪪 Aadhaar number detection
* 💳 Credit/debit card number detection
* 🏦 Bank/account-related information detection
* 🧾 PAN number detection
* 🌐 Web-based React frontend
* ⚡ Fast Vite development environment
* ☁️ AWS-based backend/infrastructure
* 🔐 Designed with security and privacy in mind
* 📊 Displays detected PII in a user-friendly format
* 🧩 Modular frontend/backend architecture

---

# 🏗️ Project Architecture

The project is divided into frontend and backend components.

```text
                         ┌─────────────────────┐
                         │       User          │
                         │   Web Browser       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React + Vite      │
                         │     Frontend        │
                         └──────────┬──────────┘
                                    │
                                    │ HTTP/API
                                    ▼
                         ┌─────────────────────┐
                         │    AWS Backend      │
                         │                     │
                         │  PII Detection      │
                         │      Service        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Detection /       │
                         │  Processing Layer   │
                         └─────────────────────┘
```

The exact AWS services used by the project can be configured according to the deployment environment.

---

# 📁 Project Structure

```text
pii-detector/
│
├── pii/
│   │
│   ├── frontend/
│   │   ├── src/
│   │   │   ├── assets/
│   │   │   ├── components/
│   │   │   ├── App.tsx
│   │   │   ├── main.tsx
│   │   │   └── vite-env.d.ts
│   │   │
│   │   ├── public/
│   │   ├── index.html
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── vite.config.ts
│   │   └── ...
│   │
│   └── backend/
│       ├── ...
│       └── ...
│
├── README.md
└── ...
```

> The exact folder structure may vary depending on your current backend implementation.

---

# 🖥️ Frontend

The frontend is built using:

* React
* TypeScript
* Vite
* HTML5
* CSS
* JavaScript/TypeScript

The frontend provides an interface where users can:

1. Enter or paste text.
2. Submit the text for analysis.
3. Send the text to the backend.
4. Receive the PII detection result.
5. View detected entities.
6. Understand which portions of the text contain sensitive information.

---

# ⚙️ Technologies Used

## Frontend

| Technology | Purpose                |
| ---------- | ---------------------- |
| React      | UI development         |
| TypeScript | Type-safe development  |
| Vite       | Development/build tool |
| CSS        | Styling                |
| Fetch/API  | Backend communication  |

## Backend / Cloud

| Technology            | Purpose                  |
| --------------------- | ------------------------ |
| AWS                   | Cloud infrastructure     |
| AWS API services      | Backend communication    |
| PII detection service | Sensitive-data detection |
| IAM                   | AWS permissions/security |

> Update this section if your implementation uses specific services such as AWS Lambda, API Gateway, Amazon Comprehend, S3, DynamoDB, or CloudWatch.

---

# 🔎 What is PII?

**Personally Identifiable Information (PII)** is information that can identify an individual directly or indirectly.

Examples include:

* Full name
* Email address
* Phone number
* Home address
* Government identification number
* Aadhaar number
* PAN number
* Passport number
* Bank account number
* Credit/debit card number
* Date of birth
* IP address

Protecting PII is important for privacy, security, and regulatory compliance.

---

# 🧠 How PII Detection Works

The general workflow is:

```text
User enters text
       │
       ▼
Frontend validates input
       │
       ▼
Text sent to backend
       │
       ▼
PII detection engine
       │
       ▼
Sensitive entities identified
       │
       ▼
Detection results returned
       │
       ▼
Frontend displays results
```

For example, if the user enters:

```text
My name is Rahul Sharma.
My email is rahul@example.com.
My phone number is 9876543210.
```

The system may identify:

```text
PERSON
    Rahul Sharma

EMAIL
    rahul@example.com

PHONE
    9876543210
```

---

# 🛠️ Installation

## Prerequisites

Before running the project, install:

* Node.js
* npm
* Git
* AWS account
* AWS CLI (if required for deployment)
* Required AWS credentials/configuration

Check Node.js:

```bash
node --version
```

Check npm:

```bash
npm --version
```

Check Git:

```bash
git --version
```

---

# 📥 Clone the Repository

Clone the project:

```bash
git clone https://github.com/tanushreek
```

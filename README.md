# pii-phi-pci-scanner

The **pii-phi-pci-scanner** is a Python‑based tool designed to identify sensitive information in files and data sources. It scans for **Personally Identifiable Information (PII)**, **Protected Health Information (PHI)**, and **Payment Card Information (PCI)** to help developers, auditors, and security professionals detect and audit potentially sensitive data. This can be useful for data compliance, risk assessment, and privacy protection in applications and data workflows.

---

## Project Overview

This project provides a flexible scanning framework that can be extended or configured to match patterns for PII, PHI, and PCI. The scanner can work with textual data or file inputs and outputs results that help track sensitive data exposure for remediation.

Sensitive data scanning is a critical component of data privacy and security processes, especially for regulated environments handling health, payment, or identity data. :contentReference[oaicite:1]{index=1}

---

## Features

- Detects **PII patterns** such as names, emails, and phone numbers  
- Identifies **PHI** entries that may contain personal health information  
- Finds **PCI data** such as credit card numbers  
- Modular architecture for adding custom detectors  
- Can be integrated into automated pipelines or CLI workflows  
- Suitable for testing and compliance scanning

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Pattern Detection | Regular Expressions (+ optional NLP models) |
| Deployment | Docker (optional) |
| Output | Console or structured reporting |

---

## Project Structure
```
pii-phi-pci-scanner/
├── app.py # Main application entry point
├── scanner.py # Core scanning logic and pattern detection
├── database.py # Optional database handling
├── requirements.txt # Project Python dependencies
├── Dockerfile # Docker container configuration
├── docker-compose.yml # Docker Compose setup
├── templates/ # HTML templates (if web UI implemented)
├── static/ # Static assets (CSS/JS/images)
├── uploads/ # Uploaded files for scanning
├── tests/ # Unit or integration tests
└── README.md # Project documentation
```

---

## Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+  
- `pip` (Python package manager)  
- Docker and Docker Compose (optional but recommended for deployment)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Manasi-16-08/pii-phi-pci-scanner.git
cd pii-phi-pci-scanner
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

---

## Running the Scanner (Local)

To run the application locally:
```bash
python app.py
```

This typically starts the application, which can be interfaced with via an API or CLI depending on the implementation.

---

### Using Docker (Optional)

To run the application in a containerized environment:
```bash
docker-compose up --build
```

This will build the Docker image and start all required services.

---

### Usage Examples

Once the scanner is running:

-Provide file paths or text input to scan for sensitive data

-Review the console or generated reports for detected PII/PHI/PCI results

-Extend or customize detection patterns as needed.

---

### Running Tests

If the repository includes tests, you can run them with:

```bash
pytest
```

Make sure pytest is installed and configured in your environment.

### Contributions

-Contributions are welcome. To contribute:

-Fork this repository.

-Create a new feature branch.

-Make your changes and commit them with clear messages.

-Submit a Pull Request for review.

### Author

Manasi Tawade

GitHub: https://github.com/Manasi-16-08

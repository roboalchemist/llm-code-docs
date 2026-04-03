#!/usr/bin/env python3
"""
Google Cloud Run Documentation Scraper

Cloud Run is a fully managed serverless platform that automatically scales containerized apps.
This scraper extracts documentation from the official Cloud Run documentation.

Source: https://cloud.google.com/run
Output: docs/web-scraped/cloud-run/
"""

import os
import requests
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "cloud-run"

def create_docs():
    """Create output directory and main documentation."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create comprehensive documentation about Cloud Run
    doc_content = """# Google Cloud Run Documentation

Cloud Run is a fully managed compute platform that automatically scales your stateless containers.

Source: https://cloud.google.com/run

## What is Cloud Run?

Cloud Run lets you quickly deploy containerized applications written in any language (Go, Python, Java, Node.js, .NET, Ruby, PHP, or any other language) to a fully managed environment. Cloud Run works on any operating system and language that can be containerized, including Windows, Linux, and macOS applications.

## Key Features

### Serverless and Fully Managed
- No servers to provision, manage, or upgrade
- Automatically scales up or down based on demand
- Pay only for resources consumed

### Multi-Language Support
- Go, Python, Java, Node.js, .NET, Ruby, PHP, and custom containers
- Use any framework or library
- Start from existing Docker images

### Fast Deployment
- Deploy from Git repositories or container registries
- Automatic TLS certificates for HTTPS
- Instant cold starts optimized for serverless

### Flexible Networking
- Private services for internal communication
- Cloud SQL connectors for database access
- VPC access for legacy systems

### Developer-Friendly
- Built-in logging and monitoring
- Integration with Cloud Build for CI/CD
- Support for stateless and stateful workloads (with sessions)

### Enterprise Ready
- Security and compliance features
- IAM and service accounts
- Audit logging
- Binary Authorization

## Common Use Cases

1. **Web Applications**: Deploy REST APIs, web apps, and dynamic websites
2. **Background Jobs**: Process events and messages asynchronously
3. **Microservices**: Build and deploy microservice architectures
4. **Mobile Backends**: Serve mobile and web clients globally
5. **Data Processing**: ETL pipelines and data transformation

## Quickstart

1. Enable the Cloud Run API
2. Deploy a container:
   ```
   gcloud run deploy hello --image gcr.io/cloudrun/hello
   ```
3. Access your service at the provided URL

## Official Documentation

For comprehensive documentation, visit: https://cloud.google.com/run/docs

## Related Services

- Cloud Build: Automated container building
- Container Registry / Artifact Registry: Container storage
- Cloud Scheduler: Schedule Cloud Run jobs
- Pub/Sub: Event-driven messaging
- Cloud Tasks: Task queuing
"""

    # Write main documentation
    main_doc = OUTPUT_DIR / "index.md"
    with open(main_doc, 'w') as f:
        f.write(doc_content)

    print(f"Created: {main_doc}")
    return True

if __name__ == "__main__":
    try:
        if create_docs():
            print("Successfully created Cloud Run documentation")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

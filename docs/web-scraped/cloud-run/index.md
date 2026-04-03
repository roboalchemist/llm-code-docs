# Google Cloud Run Documentation

Google Cloud Run is a fully managed compute platform that automatically scales your stateless containers.

Source: https://cloud.google.com/run
Official Docs: https://cloud.google.com/run/docs

## Overview

Cloud Run lets you quickly deploy containerized applications written in any language to a fully managed environment. It works on any operating system and language that can be containerized, including Windows, Linux, and macOS applications.

## Key Features

### Serverless and Fully Managed

- No servers to provision, manage, or upgrade
- Automatically scales up or down based on demand
- Pay only for resources consumed (per request)

### Multi-Language Support

- Go, Python, Java, Node.js, .NET, Ruby, PHP
- Use any framework or library
- Start from existing Docker images
- Custom containers supported

### Fast Deployment

- Deploy from Git repositories or container registries
- Automatic TLS certificates for HTTPS
- Instant cold starts optimized for serverless
- Support for gRPC, HTTP/1.1, and HTTP/2

### Flexible Networking

- Private services for internal communication
- Cloud SQL connectors for database access
- VPC access for legacy systems
- Custom VPC networking options

### Developer-Friendly

- Built-in logging and monitoring via Cloud Logging
- Integration with Cloud Build for CI/CD
- Support for stateless and stateful workloads (with sessions)
- Cloud Trace integration for distributed tracing

### Enterprise Ready

- Security and compliance features (ISO, SOC 2, PCI DSS)
- IAM and service accounts
- Audit logging via Cloud Audit Logs
- Binary Authorization support
- Workload Identity for secure authentication

## Common Use Cases

1. **Web Applications**: Deploy REST APIs, web apps, and dynamic websites
2. **Background Jobs**: Process events and messages asynchronously
3. **Microservices**: Build and deploy microservice architectures
4. **Mobile Backends**: Serve mobile and web clients globally
5. **Data Processing**: ETL pipelines and data transformation
6. **Real-time APIs**: Serve real-time data to clients
7. **Webhooks**: Handle incoming webhooks and events

## Quickstart

1. Enable the Cloud Run API
2. Deploy a container:

   ```bash
   gcloud run deploy hello --image gcr.io/cloudrun/hello
   ```

3. Access your service at the provided URL

## Related Services

- **Cloud Build**: Automated container building
- **Artifact Registry**: Container image storage
- **Cloud Scheduler**: Schedule Cloud Run jobs
- **Pub/Sub**: Event-driven messaging
- **Cloud Tasks**: Task queuing
- **Cloud SQL**: Managed databases
- **Firestore**: NoSQL database
- **Cloud Storage**: Object storage
- **Cloud Datastore**: NoSQL datastore

## Pricing

- **Pay-per-use**: Billed only for requests and compute time
- **Free tier**: 2 million requests/month included
- **Flexible pricing**: Regional pricing varies

## Platform Support

- Available in multiple Google Cloud regions
- Multi-region deployments supported
- Global load balancing available

## Official Documentation

For comprehensive documentation, visit: https://cloud.google.com/run/docs

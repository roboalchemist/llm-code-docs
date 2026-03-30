# Source: https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/llms.txt

# Guidance for Connected Mobility on AWS Implementation Guide

> This implementation guide provides an overview of the Guidance for Connected Mobility on AWS, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the Guidance to Amazon Web Services (AWS). This guide is intended for solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals who want to implement connected mobility solutions in their environment.

- [Update the Guidance](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/update-guide.html)
- [Troubleshooting](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/troubleshooting.html)
- [Uninstall the Guidance](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/uninstall.html)
- [Developer guide](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/developer-guide.html)
- [Document history](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/doc-history.html)
- [Notices](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/notices.html)

## [What is Guidance for Connected Mobility on AWS?](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/guidance-overview.html)

- [Features and benefits](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/features-and-benefits.html): The Guidance for Connected Mobility on AWS provides the following features:
- [Use cases](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/use-cases.html): Fleet Operations Management - Commercial fleet operators can digitize their operations, track vehicle locations in real-time, monitor driver performance, and optimize routes for improved efficiency and reduced operational costs.
- [Concepts and definitions](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/concepts-and-definitions.html): Telemetry Data - Real-time data streams from vehicle sensors including GPS coordinates, speed, engine diagnostics, fuel consumption, and battery status transmitted via MQTT protocol.


## [Architecture overview](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/architecture-overview.html)

- [Architecture diagram](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/architecture-diagram.html): The following diagram illustrates the complete architecture for the Guidance for Connected Mobility on AWS, showing the data flow from connected vehicles through ingestion, processing, storage, and visualization layers.
- [Architecture steps](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/architecture-steps.html): The architecture follows a linear data flow optimized for automotive telemetry processing:
- [AWS services in this Guidance](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/aws-services.html)
- [Deploying this Guidance on AWS](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/deploying-guidance.html): This Guidance uses AWS CDK (Cloud Development Kit) for infrastructure as code deployment.
- [Components for Connected Mobility](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/modules-connected-mobility.html): The guidance is organized into functional components that work together to provide comprehensive connected mobility capabilities.
- [AWS Well-Architected design considerations](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/well-architected.html): This Guidance follows AWS Well-Architected Framework best practices across all six pillars:


## [Architecture details](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/architecture-details.html)

- [Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/vpc.html): The guidance deploys a dedicated VPC with public and private subnets across multiple Availability Zones, providing network isolation and high availability for the MSK cluster and Flink applications.
- [Authentication and Authorization](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/authentication.html): The guidance uses Amazon Cognito for user authentication and AWS IAM for service-to-service authorization, providing secure access to the fleet management dashboard and REST APIs.
- [Vehicle Connectivity and Provisioning](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/vehicle-provisioning.html): The guidance uses AWS IoT Core as a simple, scalable connectivity layer for vehicle telemetry ingestion.
- [Basic Ingest and IoT Rules Engine](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/basic-ingest.html): The basic ingest layer uses AWS IoT Core Rules Engine to route vehicle telemetry directly to Amazon MSK without intermediate processing, minimizing latency and eliminating per-message costs through Basic Ingest.
- [Amazon MSK Streaming Layer](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/msk-streaming.html): Amazon MSK provides the durable, ordered message streaming backbone for the telemetry pipeline.
- [Apache Flink Stream Processing](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/flink-processing.html): Apache Flink on Amazon Kinesis Data Analytics provides the real-time stream processing engine for the telemetry pipeline.
- [Multi-Tier Storage Architecture](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/storage-layer.html): The storage layer uses a combination of Redis, DynamoDB, and S3 to optimize for different access patterns and cost requirements.
- [RESTful API Layer](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/apis.html): REST APIs provide programmatic access to fleet data and operations, enabling integration with external systems and custom applications.
- [Fleet Simulator](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/simulator.html): The fleet simulator generates realistic vehicle telemetry for testing, demonstration, and load testing without requiring physical vehicles.
- [IoT Observability and Management](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/observability.html): The System Monitoring provides comprehensive observability and operational management for the AWS IoT Core layer of the Connected Mobility guidance.
- [Fleet Management Dashboard](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/fleet-management.html): The web-based dashboard provides comprehensive fleet management capabilities with real-time data visualization.


## [Plan your deployment](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/plan-your-deployment.html)

- [Cost](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/cost.html): You are responsible for the cost of the AWS services used while running this Guidance.
- [Security](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/security-considerations.html): When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS.
- [Quotas](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/quotas.html): Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.


## [Deploy the guidance](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/deploy_the_guidance.html)

- [Deploy the guidance](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/deploy-guidance.html): The guidance provides both interactive and manual deployment options.
- [Deployment phases](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/deployment-phases.html): Phase 0: Infrastructure Foundation (~5 minutes)
- [Post-deployment validation](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/post-deployment-validation.html): After deployment completes, validate the guidance with these verification steps.
- [CloudFormation templates](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/cloudformation-templates.html): This guidance uses AWS CDK to generate CloudFormation templates.


## [Reference](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/reference.html)

- [Data Dictionary](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/data-dictionary.html): This section defines all telemetry fields, data types, units, and valid ranges used in the Connected Mobility guidance.
- [Event Catalog](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/event-catalog.html): This section documents all safety and maintenance events generated by the simulator and detected by Flink processors.

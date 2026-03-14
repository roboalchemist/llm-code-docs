# Source: https://docs.acceldata.io/documentation/adoc-architecture-an-overview.md

# Architecture

The Acceldata Data Observability Cloud (ADOC) is intended to intelligently and systematically manage and secure your data. Whether using private systems or the cloud, its architecture ensures that multiple users may work with data efficiently, with minimal erros, and with assured safety. 

### Key Components

ADOC architecture has two main components to keep things organized and secure:

**Control Plane**

The Control Plane is designed to be multi-tenant, which means that several users (tenants) share ADOC's cloud management layer (Acceldata Managed). This layer manages user access, policies, data asset discovery, jobs, monitoring, and alert configuration. All of your interactions with ADOC, such as viewing dashboards or configuring monitors, go through this central Control Plane.

**Data Plane**

The Data Plane is often managed by the users and is set in a safe network of Virtual Private Cloud (VPC). This separates the processing of each user's data and the metadata you get from your sources, keeping your data safe and in line with regulations. When you connect your data sources to the Data Plane, it can be databases, data pools, or event streams in the cloud or on premises. It gathers the needed data and sends it securely to the control plane for analysis.

![](https://uploads.developerhub.io/prod/Yoq2/88vs8qn2uuf72gzmkjbnx5f5dgh2qwaay2xxctl15sehvj03v2a5b668gchy4dhf.png)

## Key Terms

- **Tenants:** Separate organizational units or individual users that use ADOC, with their own separate set of users, data configurations, and policies.
- **Customer VPC (Virtual Private Cloud):** A Customer VPC is a private, isolated network environment within a public cloud (like AWS, GCP, or Azure) that belongs to and is fully controlled by the customer.
- **Multi-Tenant Architecture:** This software architecture model allows a single instance of the program (in this case, the ADOC Control Plane), to serve several tenants, or users, at once while maintaining the logical isolation of their data and configurations.

### Learn More

Dive deeper into specific aspects of ADOC's architecture and capabilities:

- [Data Plane Installation Guide](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation)
- [Architecture - Deep Dive](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/adoc-architecture)
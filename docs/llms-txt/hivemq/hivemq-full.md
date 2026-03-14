# Hivemq Documentation

Source: https://docs.hivemq.com/llms-full.txt

---

# HiveMQ Documentation

> HiveMQ is an enterprise MQTT platform for reliable, scalable IoT messaging, event streaming, and real-time AI-ready data intelligence. This documentation covers the HiveMQ MQTT broker, extensions, cloud service, edge gateway, Kubernetes operator, and HiveMQ Pulse.

## Core Platform

- [Getting Started](https://docs.hivemq.com/hivemq/latest/user-guide/getting-started.html): Quick start guide for the HiveMQ MQTT broker

HiveMQ is an MQTT-based industrial data platform for agentic AI designed to bring operational data from the edge into the enterprise. This quick start guide shows you how to choose a HiveMQ deployment path, connect MQTT clients, and move data running HiveMQ locally, in Docker, or in the cloud.

- [System Requirements](https://docs.hivemq.com/hivemq/latest/user-guide/system-requirements.html): Hardware, OS, and JVM requirements

HiveMQ is a high-performance MQTT broker designed to run on server hardware, though it can also run on embedded devices. HiveMQ requires 4GB RAM minimum, 4 or more CPUs, and 100GB disk space exclusively allocated, with OpenJDK JRE 21 for production.

- [Configuration](https://docs.hivemq.com/hivemq/latest/user-guide/configuration.html): Complete broker configuration reference

The default settings of HiveMQ are suitable for most typical use cases. HiveMQ uses XML-based configuration files located in the conf folder and reads the config.xml file one time during startup, requiring a restart to apply changes.

- [Installation](https://docs.hivemq.com/hivemq/latest/user-guide/install-hivemq.html): Installation methods for Linux, Windows, and bare metal

This guide walks you through basic installation and optimization steps for the HiveMQ platform. You can download HiveMQ in a convenient ZIP package with all executable files, initialization scripts, and example configurations needed for successful installation.

- [Docker Deployment](https://docs.hivemq.com/hivemq/latest/user-guide/docker.html): Running HiveMQ in Docker containers

Docker is a popular open-source platform that eases deployment and delivery of applications in a containerized environment. HiveMQ provides a continuously updated Docker repository on Docker Hub that enables you to streamline development, deployment, and management efforts.

- [Clustering](https://docs.hivemq.com/hivemq/latest/user-guide/cluster.html): High availability and cluster configuration

One of the outstanding features of HiveMQ is the ability to form resilient, highly available, and ultra-scalable MQTT broker clusters. HiveMQ employs a sophisticated masterless cluster design that provides true horizontal scalability where each broker node can handle hundreds of thousands to millions of concurrently connected MQTT clients.

- [Listeners](https://docs.hivemq.com/hivemq/latest/user-guide/listeners.html): TCP, WebSocket, and TLS listener configuration

MQTT listeners specify the IP address and port on which HiveMQ accepts incoming connections from MQTT clients. By default, HiveMQ binds to IANA standard port 1883, and supports multiple listener types including TCP, TLS, WebSocket, and Secure WebSocket.

- [Security](https://docs.hivemq.com/hivemq/latest/user-guide/security.html): TLS, authentication, and authorization

HiveMQ is designed from the ground up with maximum security in mind. For mission-critical IoT scenarios, secure end-to-end encrypted communication and advanced authentication and authorization features are essential, with HiveMQ offering flexibility to enable specific security features required by your deployment.

- [Monitoring](https://docs.hivemq.com/hivemq/latest/user-guide/monitoring.html): Metrics, JMX, and monitoring integration

System monitoring is an essential part of every production-software deployment, especially in clustered MQTT broker environments. The highly-performant metrics subsystem of HiveMQ lets you monitor relevant metrics with no reduction in system performance even in low-latency high-throughput environments.

- [Health API](https://docs.hivemq.com/hivemq/latest/user-guide/health-api.html): Readiness and liveness endpoints

The endpoints of the HiveMQ Health API provide operational information about your HiveMQ broker components and extensions. With the Health API, you can capture snapshots that show the current state of health for each node in your HiveMQ cluster to help quickly identify potential issues.

- [Logging](https://docs.hivemq.com/hivemq/latest/user-guide/logging.html): Log configuration and dynamic log levels

HiveMQ implements a powerful Logback logging system that helps you monitor, diagnose, and troubleshoot your applications. The default HiveMQ logging configuration is suitable for most use cases and writes all log data to the log folder of your HiveMQ installation.

- [Shared Subscriptions](https://docs.hivemq.com/hivemq/latest/user-guide/shared-subscriptions.html): Load balancing across subscribers

Shared subscriptions allow the MQTT broker to balance the load of a single subscription across multiple MQTT clients. In a regular MQTT subscription each client receives a copy of every message, while in a shared subscription clients receive messages in an alternating fashion.

- [Troubleshooting](https://docs.hivemq.com/hivemq/latest/user-guide/troubleshooting.html): Common issues and diagnostics

This section provides guidance on troubleshooting common HiveMQ deployment issues. It covers topics such as running HiveMQ on reserved ports between 1 and 1024 on Linux machines using authbind.

- [Restrictions](https://docs.hivemq.com/hivemq/latest/user-guide/restrictions.html): Connection limits, bandwidth throttling, and MQTT message size limits

CPU, memory, and bandwidth are limited resources. HiveMQ connection limits and connection-rate throttling properties are defined in config.xml to limit TCP connections, restrict bandwidth usage, and protect against malicious client attacks. Includes maximum connection limits, incoming bandwidth throttling, and MQTT Client ID and Topic length limits.

- [Overload Protection](https://docs.hivemq.com/hivemq/latest/user-guide/overload-protection.html): Back pressure and cluster overload protection mechanisms

HiveMQ provides built-in cluster overload protection that restricts incoming traffic if the rate of MQTT messages becomes too high. Each node determines its own overload protection level every 100 milliseconds and broadcasts changes to the cluster, selectively applying back pressure on specific MQTT clients during periods of exceptionally high load.

- [Proxy Protocol](https://docs.hivemq.com/hivemq/latest/user-guide/proxy-protocol.html): PROXY protocol support for load balancer deployments

HiveMQ supports the PROXY protocol (v1 and v2) for all listeners, allowing transportation of client details like IP address, port, and SSL information over multiple proxies. Essential when running HiveMQ behind a load balancer, as without PROXY protocol the broker only sees the load balancer connection and loses original client information.

- [Changelog](https://www.hivemq.com/changelog/): Release notes with features, fixes, and deprecations for all HiveMQ products

The HiveMQ Changelog provides a chronological history of releases across HiveMQ Platform, HiveMQ CE, HiveMQ Edge, HiveMQ Cloud, and HiveMQ Platform Operator for Kubernetes. Each entry includes the release date, version number, and a summary of new features, improvements, bug fixes, and deprecations.

- [Changelog RSS Feed](https://www.hivemq.com/changelogs.xml): Machine-readable RSS 2.0 feed of all HiveMQ product releases

Subscribe to the RSS feed to track new HiveMQ releases programmatically. The feed uses standard RSS 2.0 format with title, description, link, and publication date for each release.

## Extensions SDK

- [Extension Developer Guide](https://docs.hivemq.com/hivemq/latest/extensions/index.html): Overview of the HiveMQ extension system

The HiveMQ ecosystem includes numerous open-source and commercial tools and solutions that enable moving data from device to cloud in a secure, reliable, and scalable manner. Our flexible extension framework provides an open API that allows developers to create custom extensions for their specific infrastructures.

- [Quick Start (Gradle)](https://docs.hivemq.com/hivemq/latest/extensions/quick-start-gradle.html): Build your first extension with Gradle

This quick start guide covers the basics needed to get started with extension development for HiveMQ using Gradle. You can use the HiveMQ Hello World Extension as a template that sets up everything you need including the HiveMQ Gradle Plugin and integration testing examples.

- [Interceptors](https://docs.hivemq.com/hivemq/latest/extensions/interceptors.html): MQTT packet interception and modification

HiveMQ Interceptors provide a convenient way for extensions to intercept and modify MQTT messages. Based on the interceptor type, you can register a ClientInitializer or use the GlobalInterceptorRegistry to add the interceptor you want.

- [Services](https://docs.hivemq.com/hivemq/latest/extensions/services.html): Extension services API reference

HiveMQ services provide a convenient way for extensions to interact with the HiveMQ core. You can access HiveMQ Extension SDK services through the Services class to access functionality for client management, subscriptions, retained messages, and more.

- [Authentication](https://docs.hivemq.com/hivemq/latest/extensions/authentication.html): Custom authentication providers

HiveMQ extensions can use different types of authenticators to authenticate MQTT clients registered in the Security Registry. Each extension can register an authenticator, and when multiple security extensions are used, the associated authenticators are called in order with highest priority first.

- [Authorization](https://docs.hivemq.com/hivemq/latest/extensions/authorization.html): Custom authorization providers

The HiveMQ Extension System offers multiple options for authorizing clients to publish and subscribe. The simplest option is Default Permissions set when a client connects, while Publish Authorizer and Subscription Authorizer provide more flexible per-packet basis authorization.

- [Extension Deployment](https://docs.hivemq.com/hivemq/latest/extensions/deployment.html): Building, packaging, and deploying extensions

After creating your extension project with the HiveMQ Extension Archetype, use the Maven package goal to build a distribution ZIP file. Every HiveMQ extension requires a hivemq-extension.xml file alongside the extension JAR, and you can extend the packaging phase to bundle everything automatically.

- [Registries](https://docs.hivemq.com/hivemq/latest/extensions/registries.html): Initializer, Security, and Event registry API reference

HiveMQ registries provide a convenient way for extensions to register callbacks with the HiveMQ core. Available registries include the Initializer Registry (client initializers), Security Registry (authentication and authorization), Event Registry (client lifecycle events), and Metric Registry (custom metrics access).

- [Quick Start (Maven)](https://docs.hivemq.com/hivemq/latest/extensions/quick-start-maven.html): Build your first extension with Maven

This quick start guide covers extension development for HiveMQ using Apache Maven. Use the preconfigured HiveMQ Maven Archetype to create a fully-functional HelloWorld extension project as a basis for developing custom extensions, with all HiveMQ dependencies available in Maven Central.

- [Testing Extensions](https://docs.hivemq.com/hivemq/latest/extensions/testing-extension.html): Integration testing with HiveMQ Testcontainers

Write automated tests for your HiveMQ extension using the official HiveMQ Testcontainers Module or the HiveMQ Testcontainer library. These libraries automatically create HiveMQ Docker containers and deploy your extension inside for integration testing with Gradle or Maven.

## Data Hub

- [Data Hub Overview](https://docs.hivemq.com/hivemq/latest/data-hub/index.html): Policy-driven data governance for MQTT

HiveMQ Data Hub provides mechanisms to define how MQTT data and MQTT client behavior are handled in the HiveMQ broker. Data Validation allows you to implement declarative policies to check data format, while Behavior Validation gives you the ability to model client behavior throughout the entire lifecycle.

- [Schemas](https://docs.hivemq.com/hivemq/latest/data-hub/schemas.html): Data validation with JSON Schema, Protobuf, or Avro

Data validation relies on the interaction between predefined schemas and policies. The HiveMQ Data Hub supports schema definitions with JSON Schema (Draft-04, -06, -07, 2019-09, 2020-12) and Protobuf formats (Version 2 and 3).

- [Policies](https://docs.hivemq.com/hivemq/latest/data-hub/policies.html): Policy definition and enforcement

The integrated policy engines of HiveMQ Data Hub give you the ability to build individual data governance policies that maximize the value of your data pipelines. HiveMQ Data Hub supports two types of policies: data policies and behavior policies.

- [Transformations](https://docs.hivemq.com/hivemq/latest/data-hub/transformations.html): Data transformation pipelines

IoT devices send a wide range of data sets, and the MQTT data you receive often contains diverse data points, formats, and units. The HiveMQ Data Hub transformation feature gives you the ability to add custom JavaScript-based transformation functions to your Data Hub data policies.

- [Behavior Models](https://docs.hivemq.com/hivemq/latest/data-hub/behavior-models.html): Client behavior validation

The HiveMQ Data Hub uses state machines to model the behavior of an MQTT client as it moves through your HiveMQ broker. Behavior validation relies on the interaction between predefined state machine models and policies that offer a simple and powerful way to represent client behavior.

- [Data Hub Quick Start](https://docs.hivemq.com/hivemq/latest/data-hub/quick-start.html): Get started with data policies and schema validation

This quick start guide shows you how to get started with HiveMQ Data Hub using the HiveMQ Control Center interactive UI or the HiveMQ REST API from the command line. Focuses on creating JSON data schemas and data policies, requiring HiveMQ Professional or Enterprise version 4.20.0 or higher.

- [Data Validation](https://docs.hivemq.com/hivemq/latest/data-hub/validation.html): Schema-based payload validation for MQTT messages

Validators ensure that MQTT messages on your broker fulfill your requirements. Schema validators check the format of the MQTT message payload, including field existence and value limits. Since MQTT is data agnostic, validation prevents invalid or incorrectly formatted data from causing unpredictable behavior in downstream services.

- [Actions](https://docs.hivemq.com/hivemq/latest/data-hub/actions.html): Actions triggered by policy violations and state transitions

In HiveMQ Data Hub, an action is a collection of operations the broker performs in response to the outcome of a data-validation or a state transition in behavior-validation. Actions define what happens when validation succeeds or fails, with configurable onSuccess and onFailure pipelines.

- [Use Cases](https://docs.hivemq.com/hivemq/latest/data-hub/use-cases.html): Practical examples for data governance scenarios

A collection of user stories for HiveMQ Data Hub highlighting practical ways to use schemas and policies, including enforcing valid JSON, multiple Protobuf policies on different topics, accepting multiple schemas on a single topic, redirecting legacy schema versions, and updating existing policies.

- [Data Hub Metrics](https://docs.hivemq.com/hivemq/latest/data-hub/metrics.html): Monitoring metrics for policies, schemas, and validations

When enabled, HiveMQ Data Hub exposes metrics for data validation (payload validation counts, schema validation counts, policy outcomes) and behavior validation (client coverage, state transitions, behavior terminations, schema deserializations) as counters, gauges, and timers.

## REST API

- [REST API](https://docs.hivemq.com/hivemq/latest/rest-api/index.html): HiveMQ management REST API documentation

The HiveMQ REST API provides an interface for applications to interact programmatically with the HiveMQ Enterprise MQTT broker. HiveMQ administrators can use the REST API to automate Control Center actions they would normally perform manually such as starting trace recordings or getting lists of connected clients.

- [OpenAPI Specification](https://docs.hivemq.com/hivemq/latest/rest-api/openapi.yaml): HiveMQ REST API OpenAPI 3.0 specification (YAML)

The machine-readable OpenAPI 3.0 schema definition of the HiveMQ REST API. Import into API tools such as Postman or use to generate client code in any programming language. This is a stable URL that always points to the latest version of the specification.

## Control Center

- [Control Center](https://docs.hivemq.com/hivemq-control-center/latest/index.html): Web-based management UI for HiveMQ

HiveMQ Control Center v2 is the new operational dashboard for your HiveMQ Broker that automatically ships alongside the existing Control Center v1. Starting with HiveMQ 4.39, HiveMQ Control Center v2 is generally available and can be used in production.

- [Configuration](https://docs.hivemq.com/hivemq-control-center/latest/configuration.html): Access control, user setup, and security settings

The HiveMQ Control Center works out of the box without any additional installation or configuration. Fine-tune your control center configuration to match your individual use case, including configuring custom users and passwords, access control, and security settings. The default login is admin/hivemq.

- [Clients](https://docs.hivemq.com/hivemq-control-center/latest/clients.html): Client session management, search, and detailed information

The HiveMQ Control Center provides tools to list, view, and manage all MQTT clients known to your HiveMQ Platform. Access detailed information about each client, including subscriptions, connection status, TLS, and more. The Clients view gives you deep insights into every client connected to your HiveMQ Platform.

- [Dashboard](https://docs.hivemq.com/hivemq-control-center/latest/dashboard.html): Real-time cluster metrics and monitoring graphs

The Overview dashboard offers a concise view of the current state of your HiveMQ Platform cluster with immediate insights into key issues. Thumbnail graphs across the top provide a quick snapshot of key metrics such as current usage and cluster throughput. Use the Nodes dropdown to view data for all nodes or a specific cluster node.

- [Trace Recordings](https://docs.hivemq.com/hivemq-control-center/latest/trace-recordings.html): Log and analyze MQTT traffic for specific clients or topics

The Trace Recording feature allows you to log traffic for selected clients or topics using regular expression filters, providing real-time visibility for efficient troubleshooting and analysis. Each node creates its own .trace file, and downloads bundle all node-specific files into a compressed archive for cluster-wide analysis.

- [Integrations](https://docs.hivemq.com/hivemq-control-center/latest/integrations.html): View and manage installed HiveMQ extensions and integrations

HiveMQ supports a wide range of functional add-ons and integrations. The Available Integrations view provides descriptions and download links for commercial and open-source integrations. Enterprise Extensions come preinstalled and disabled by default — enable them by removing the DISABLED file from the extension folder.

## Enterprise Extensions

- [Kafka Extension](https://docs.hivemq.com/hivemq-kafka-extension/latest/index.html): Bidirectional MQTT-Kafka bridge

Apache Kafka is a popular open-source streaming platform that makes it easy to share data between enterprise systems and applications. The HiveMQ Enterprise Extension for Kafka implements the native Kafka protocol inside your HiveMQ broker for bi-directional MQTT messaging to and from Kafka clusters.

- [Kafka Extension Customization](https://docs.hivemq.com/hivemq-kafka-extension/latest/customization.html): Custom transformers for MQTT-Kafka message mapping

The HiveMQ Kafka Extension Customization SDK gives you the ability to customize the management of your Kafka topics and implement custom logic for bidirectional message transfer between HiveMQ and your Kafka clusters. Use the API to programmatically specify sophisticated custom-handling of message transformations.

- [Bridge Extension](https://docs.hivemq.com/hivemq-bridge-extension/latest/index.html): MQTT broker-to-broker bridging

The HiveMQ Enterprise Bridge Extension enables HiveMQ to bridge to one or more MQTT brokers for scalable, reliable, and bi-directional exchange of MQTT messages. It supports customizable topic mapping configuration for bidirectional message exchange with remote MQTT brokers.

- [Enterprise Security Extension](https://docs.hivemq.com/hivemq-enterprise-security-extension/latest/index.html): LDAP, OAuth, JWT, and database authentication

The HiveMQ Enterprise Security Extension expands the role, user, and permission-management capabilities of HiveMQ Enterprise and Professional editions. ESE allows you to use different sources of external authentication and authorization data to authenticate and authorize MQTT clients.

- [ESE Getting Started](https://docs.hivemq.com/hivemq-enterprise-security-extension/latest/getting-started.html): Installation, configuration, and SQL database setup

Step-by-step guide to install and configure the HiveMQ Enterprise Security Extension. Covers placing the license file, enabling the extension, configuring the config.xml, and setting up SQL database connections for authentication and authorization.

- [ESE Reference](https://docs.hivemq.com/hivemq-enterprise-security-extension/latest/ese.html): Realms, pipelines, authentication, authorization, and access control

Comprehensive reference for the HiveMQ Enterprise Security Extension covering realms, pipelines, authentication methods (SQL, LDAP, JWT, OAuth, OIDC), authorization, and access control. Includes configuration for password hashing (MD5, SHA-512, bcrypt, PKCS5S2, Argon2), TLS client certificates, and HTTP-based authentication.

- [Google Cloud Pub/Sub Extension](https://docs.hivemq.com/hivemq-google-cloud-pubsub-extension/latest/index.html): MQTT to Google Cloud Pub/Sub integration

Pub/Sub is a fully-managed messaging service of the Google Cloud platform that allows sending and receiving messages between applications. The HiveMQ Enterprise Extension for Google Cloud Pub/Sub enables you to seamlessly integrate MQTT device data with other Google Cloud services through the Pub/Sub service.

- [Google Cloud Pub/Sub Quick Start](https://docs.hivemq.com/hivemq-google-cloud-pubsub-extension/latest/quick-start.html): Google Cloud setup and extension configuration

Quick start guide for setting up the HiveMQ Enterprise Extension for Google Cloud Pub/Sub. Covers Google Cloud account setup, project creation, Pub/Sub topic and subscription configuration, service account credentials, and HiveMQ extension installation and configuration.

- [Amazon Kinesis Extension](https://docs.hivemq.com/hivemq-amazon-kinesis-extension/latest/index.html): MQTT to AWS Kinesis integration

Amazon Kinesis is a suite of fully-managed AWS services designed to ingest, process, and analyze large-scale data streams in real-time. The HiveMQ Enterprise Extension for Amazon Kinesis makes it easy to move MQTT messaging data between your HiveMQ broker and Amazon Kinesis Data Streams service.

- [Data Lake Extension](https://docs.hivemq.com/hivemq-data-lake-extension/latest/index.html): Stream MQTT data to data lakes

Data lakes are centralized repositories that allow organizations to store vast amounts of raw and processed data in its native format. The HiveMQ Enterprise Data Lake Extension makes it possible to forward MQTT messages directly to your data lake without the need for additional infrastructure.

- [MongoDB Extension](https://docs.hivemq.com/hivemq-mongodb-extension/latest/index.html): Persist MQTT data to MongoDB

MongoDB is an open-source, document-oriented database system designed for scalability, high availability, and performance. MongoDB uses a JSON-like format called BSON to store documents organized in collections, analogous to tables in a relational database.

- [PostgreSQL Extension](https://docs.hivemq.com/hivemq-postgresql-extension/latest/index.html): Persist MQTT data to PostgreSQL

PostgreSQL is an open-source relational database management system widely used to safely store and manage large amounts of data. PostgreSQL supports most features of the current SQL standard and is suitable for various types of applications.

- [MySQL Extension](https://docs.hivemq.com/hivemq-mysql-extension/latest/index.html): Persist MQTT data to MySQL

MySQL is an open-source relational database management system widely used to store and manage structured data. The HiveMQ Enterprise Extension for MySQL enables you to forward MQTT messages from IoT devices to one or more MySQL databases.

- [Microsoft SQL Server Extension](https://docs.hivemq.com/hivemq-microsoft-sql-server-extension/latest/index.html): Persist MQTT data to Microsoft SQL Server

Microsoft SQL Server is a relational database management system from Microsoft used across on-premise and cloud environments to store, manage, and analyze data. The extension enables you to forward MQTT messages from connected IoT devices to one or more Microsoft SQL Server or Azure SQL databases.

- [Snowflake Extension](https://docs.hivemq.com/hivemq-snowflake-extension/latest/index.html): Stream MQTT data to Snowflake

Snowflake is a popular cloud-based data management and data warehousing platform designed to store, process, and analyze data. The HiveMQ Enterprise Extension for Snowflake makes it possible to forward MQTT messages directly to Snowflake via the Snowpipe Streaming SDK without additional infrastructure.

- [Distributed Tracing Extension](https://docs.hivemq.com/hivemq-distributed-tracing-extension/latest/index.html): OpenTelemetry tracing for MQTT

The HiveMQ Enterprise Distributed Tracing Extension is a first-of-its-kind monitoring tool that lets you track the performance of MQTT PUBLISH messages within an MQTT broker. The extension uses an open-standards OpenTelemetry-based approach to add tracing capabilities to the HiveMQ broker and its integrations.

- [Distributed Tracing Spans](https://docs.hivemq.com/hivemq-distributed-tracing-extension/latest/distributed-tracing-spans.html): OpenTelemetry span details and semantic conventions

HiveMQ distributed tracing spans represent work done within a specific trace including time intervals and associated metadata. All captured spans are correlated with OpenTelemetry Resources including Service, Host, Operating System, and Cloud provider attributes. Follows OpenTelemetry semantic conventions for messaging.

## Kubernetes Deployment

- [HiveMQ Platform Operator](https://docs.hivemq.com/hivemq-platform-operator/index.html): Deploy HiveMQ on Kubernetes with the platform operator

The HiveMQ Platform Operator for Kubernetes is a tool for managing your HiveMQ deployments in a Kubernetes environment. The operator allows you to install, scale, configure, and monitor your HiveMQ Platform deployments in a versatile, adaptable manner that automatically reconciles configuration changes.

- [Platform Operator Configuration](https://docs.hivemq.com/hivemq-platform-operator/configuration.html): HiveMQ Platform Helm chart installation and configuration options

Helm offers a streamlined and manageable approach to install HiveMQ on Kubernetes. HiveMQ provides two preconfigured Helm charts, one for the HiveMQ Platform Operator and one for the HiveMQ Platform, with detailed configuration options for operators and platform clusters.

- [Custom Resource Definition](https://docs.hivemq.com/hivemq-platform-operator/crd.html): CRD specification for HiveMQ Platform deployments on Kubernetes

The HiveMQ Platform Custom Resource Definition (CRD) provides all the necessary definitions and configurations to deploy your HiveMQ platform to a Kubernetes system version 1.24 or higher. A single HiveMQ Platform Operator can manage one or more HiveMQ platforms.

- [Kubernetes Distributions](https://docs.hivemq.com/hivemq-platform-operator/k8s-distributions.html): Deployment on EKS, AKS, GKE, and OpenShift

Step-by-step procedures for deploying the HiveMQ Platform Operator on popular Kubernetes distributions including Red Hat OpenShift, Amazon EKS, Azure AKS, and Google GKE, with vendor-specific configuration requirements.

- [Examples](https://docs.hivemq.com/hivemq-platform-operator/examples.html): Deployment examples and Helm chart configurations

Examples showing how to customize HiveMQ Platform deployment with Helm charts, including installing the Kafka extension, custom JDBC drivers, Google Cloud Pub/Sub extension, MQTT Message Log extension, File RBAC extension, projected volumes, RBAC permissions, and triggering rolling restarts.

- [Observability](https://docs.hivemq.com/hivemq-platform-operator/observability.html): Monitoring, metrics, and logging for operator deployments

Events provide detailed information to monitor HiveMQ platforms on Kubernetes. The HiveMQ Platform Operator publishes events whenever the state of a managed HiveMQ platform changes, enabling effective alerting and monitoring of operations.

- [Upgrade Guide](https://docs.hivemq.com/hivemq-platform-operator/upgrade-guide.html): Operator version migration procedures

The HiveMQ Platform Operator Upgrade Guides show you how to upgrade to the latest operator version with detailed information on upgrading Helm charts, the operator, and the HiveMQ Platform. Upgrades always trigger a rolling restart.

- [HiveMQ Operator (Legacy)](https://docs.hivemq.com/hivemq-operator/index.html): Legacy Kubernetes operator

The HiveMQ Kubernetes Operator is an application-specific controller that helps orchestrate and manage the lifecycle of a HiveMQ cluster deployment within Kubernetes. It runs as a custom controller on Kubernetes and communicates with the Kubernetes API Server to convert high-level descriptions into normal Kubernetes resources.

## HiveMQ Cloud

- [HiveMQ Cloud](https://docs.hivemq.com/hivemq-cloud/index.html): Fully managed MQTT cloud service

HiveMQ Cloud is a fully-managed, cloud-native IoT messaging platform that makes trustworthy and scalable IoT device connectivity simple with no installation or server management required. HiveMQ is the industry leader for enterprise-ready, beautifully scalable, large-scale IoT deployments with MQTT.

- [Quick Start Guide](https://docs.hivemq.com/hivemq-cloud/quick-start-guide.html): Create a cluster and connect your first MQTT client

This guide walks you through signing up, selecting a plan (Serverless or Starter), creating your first cluster, setting up credentials, and testing the connection with MQTT CLI or the Web Client.

- [Console](https://docs.hivemq.com/hivemq-cloud/console.html): Web console for cluster, organization, and integration management

The HiveMQ Cloud Console is the web-based management interface for managing organizations, clusters, access management, and integrations with Apache Kafka, Confluent, Amazon Kinesis, and Aiven.

- [Authentication & Authorization](https://docs.hivemq.com/hivemq-cloud/authn-authz.html): Credentials, client certificates, JWT, and role-based access control

HiveMQ Cloud supports multiple authentication methods including username-password credentials, client certificates, and JWT tokens. Role-based access control (RBAC) with default and custom roles provides fine-grained topic-level permissions.

- [Metrics](https://docs.hivemq.com/hivemq-cloud/metrics.html): Cluster monitoring and observability metrics

HiveMQ Cloud provides operational metrics for monitoring cluster health, including counters and gauges for keep-alive, message queuing, dropped messages, and other key indicators. Metric availability varies by plan (Starter vs Enterprise).

- [Troubleshooting](https://docs.hivemq.com/hivemq-cloud/troubleshooting.html): Log streaming, diagnostics, and issue resolution

The troubleshooting logs view provides real-time log streaming with filtering by client ID, timestamp, and event type. Access logs and event logs help diagnose connectivity and operational issues.

- [REST API](https://docs.hivemq.com/hivemq-cloud/rest-api.html): Manage credentials, permissions, and roles programmatically

The HiveMQ Cloud REST API enables programmatic management of MQTT credentials, permissions, and roles. You can create, view, update, and delete access credentials, attach permissions to roles, and automate cluster administration.

- [Cloud REST API OpenAPI Specification](https://docs.hivemq.com/hivemq-cloud/rest-api/openapi.yaml): HiveMQ Cloud REST API OpenAPI specification (YAML)

The machine-readable OpenAPI schema for the HiveMQ Cloud SaaS REST API. Use to generate client code or import into API tools.

- [Cloud Enterprise REST API OpenAPI Specification](https://docs.hivemq.com/hivemq-cloud/rest-api/enterprise/openapi.yaml): HiveMQ Cloud Enterprise REST API OpenAPI specification (YAML)

The machine-readable OpenAPI schema for the HiveMQ Cloud Enterprise REST API, including AsyncAPI event streaming endpoints.

## HiveMQ Edge

- [HiveMQ Edge](https://docs.hivemq.com/hivemq-edge/index.html): Lightweight open-source MQTT gateway for edge computing with protocol translation

HiveMQ Edge is a lightweight, open-source MQTT gateway optimized for Edge computing. Use HiveMQ Edge to translate diverse industrial device protocols into MQTT for streamlined and reliable communication between your operational technology and information technology systems.

- [System Requirements](https://docs.hivemq.com/hivemq-edge/system-requirements.html): OS, JDK, and hardware requirements for Edge

HiveMQ Edge runs on Linux, Windows, and macOS with JDK 17+ (JDK 21+ for version 2025.16+). It is designed for lightweight deployment on edge devices and servers.

- [Installation](https://docs.hivemq.com/hivemq-edge/installing-hivemq-edge.html): Installation on Linux, Windows, or Kubernetes with Helm

This guide covers installation on Linux, Windows, and Kubernetes using Helm charts. It includes directory structure, prerequisites, and reverse proxy configuration.

- [Configuration](https://docs.hivemq.com/hivemq-edge/configuration.html): XML-based broker configuration for Edge

HiveMQ Edge uses XML-based configuration files located in the conf folder. The default configuration binds a TCP listener on port 1883 and is suitable for most typical use cases.

- [Protocol Adapters](https://docs.hivemq.com/hivemq-edge/protocol-adapters.html): OPC UA, Modbus, S7, BACnet, EtherNet/IP, HTTP, and more

HiveMQ Edge includes 12+ pre-built protocol adapters for industrial protocols including OPC UA (northbound and southbound), Modbus TCP, Siemens S7, ADS/TwinCAT, EtherNet/IP, HTTP(S), BACnet, MTConnect, and database adapters. A custom adapter SDK is also available.

- [MQTT Bridging](https://docs.hivemq.com/hivemq-edge/mqtt-bridging.html): Bridge MQTT messages to upstream brokers

MQTT bridging enables bidirectional message exchange between HiveMQ Edge and upstream MQTT brokers. Configure topic mappings to forward data from edge devices to enterprise HiveMQ clusters or cloud services.

- [Security](https://docs.hivemq.com/hivemq-edge/security.html): TLS, authentication, and authorization for Edge

HiveMQ Edge supports TLS/SSL encryption for transport security, along with authentication and authorization mechanisms. Security configuration covers both MQTT client connections and the management API.

- [Workspace](https://docs.hivemq.com/hivemq-edge/workspace.html): Web UI for visual management and observability

The HiveMQ Edge Workspace is a web-based UI that provides a visual canvas for managing adapters, bridges, and data flows. It includes a topology view, configuration toolbar, and real-time observability features.

## HiveMQ Swarm

- [HiveMQ Swarm](https://docs.hivemq.com/hivemq-swarm/latest/index.html): Distributed MQTT load testing and simulation tool

HiveMQ Swarm is an advanced IoT testing and simulation tool that gives you the load and reliability testing ability needed to determine the resilience and capacity of your complete IoT system. IoT solutions usually involve massive distributed systems, and successfully simulating your end-to-end production environment can be a big challenge.

- [Scenarios](https://docs.hivemq.com/hivemq-swarm/latest/scenarios.html): Scenario DSL for defining client groups, subscriptions, and test stages

Scenarios are an important concept in HiveMQ Swarm. Each scenario is an abstract representation of a specific real-life MQTT use case defined in an XML-based DSL. You can define scenarios that represent very large numbers of MQTT clients organized in client groups, with behavior delineated in stages, lifecycles, and commands.

- [Commands](https://docs.hivemq.com/hivemq-swarm/latest/commands.html): Command reference (Connect, Publish, Subscribe, Receive, For, Delay, Timer)

In HiveMQ Swarm, commands represent the actions that each client of a client group completes within a specific lifecycle of your scenario. Available commands include Connect, Publish, Subscribe, Receive, Disconnect, For (loops), Delay, and Timer for controlling client behavior during load tests.

- [Deployment](https://docs.hivemq.com/hivemq-swarm/latest/clustering.html): Distributed architecture with commander/agents, Kubernetes deployment

HiveMQ Swarm gives you the ability to create a clustered test environment that distributes the workload to the appropriate number of worker nodes. Each cluster has a single commander and one or more agents, with the commander distributing workload chunks to agents that organize groups of MQTT clients. Includes Kubernetes deployment with Helm charts.

- [Monitoring](https://docs.hivemq.com/hivemq-swarm/latest/monitoring.html): InfluxDB and Prometheus metrics integration

HiveMQ Swarm supports monitoring via InfluxDB and Prometheus. Configure InfluxDB connections through environment variables or file-based configuration to gather and visualize application metrics from your load testing scenarios.

- [Example Scenarios](https://docs.hivemq.com/hivemq-swarm/latest/example-scenarios.html): Templates for reconnect storms, fan-out, fan-in, steady load, and more

Example scenarios to become familiar with HiveMQ Swarm and as a basis for your own scenarios. Includes templates for reconnect storm testing, fan-out and fan-in patterns, steady load generation, and other common IoT simulation patterns.

## HiveMQ Pulse

- [HiveMQ Pulse](https://docs.hivemq.com/hivemq-pulse/index.html): Distributed data intelligence platform for real-time processing and contextualization of operational data

HiveMQ Pulse is a distributed data intelligence platform that processes and contextualizes data in real time. Pulse turns your operational data infrastructure into a distributed intelligence network that delivers the right information to the right place at the right time.

- [Getting Started](https://docs.hivemq.com/hivemq-pulse/getting-started.html): Account setup, infrastructure connection, and namespace building

This guide walks you through creating a HiveMQ Pulse account, connecting HiveMQ Edge and Enterprise broker infrastructure, building a namespace using ISA-95 hierarchy, and discovering MQTT data sources with automatic approval workflows.

- [Nodes](https://docs.hivemq.com/hivemq-pulse/node-types.html): ISA-95 data modeling hierarchy (Enterprise, Site, Area, Line, Asset, Tag, Field)

HiveMQ Pulse uses an ISA-95 hierarchy model with organizational nodes (Enterprise, Site, Area, Line, Asset, Folder) and data nodes (Tag, Field). Each node has a general tab, data sources, data output with history, and consumer references.

- [Calculations](https://docs.hivemq.com/hivemq-pulse/calculation-types.html): Built-in analytics functions (SMA, OEE, statistics, aggregations)

Pulse provides mathematical operations performed across nodes to produce new values and insights. Available functions include simple operations (sum, min, max, product), statistical functions (mean, median, standard deviation, variance), moving averages (SMA, EMA), and Overall Equipment Effectiveness (OEE).

- [Expression Language](https://docs.hivemq.com/hivemq-pulse/expression-language.html): Domain-specific language for real-time data processing and IoT logic

The Pulse Expression Language is a domain-specific language for real-time data processing in smart manufacturing and IoT. It supports mathematical and logical operations, statistical functions, window functions, variables referencing live data sources, and type safety, with examples for temperature monitoring, production line efficiency, quality control, and predictive maintenance.

- [Governance](https://docs.hivemq.com/hivemq-pulse/governance.html): Data quality validation, deviation tracking, and resolution

Pulse Governance validates data traffic against namespace definitions and automatically detects deviations such as missing fields, unexpected fields, and incorrect data types. Deviations can be resolved by fixing the data source, updating the namespace definition, or ignoring the deviation.

- [Glossary](https://docs.hivemq.com/hivemq-pulse/glossary.html): Terminology reference for Pulse concepts

A comprehensive glossary of 30+ HiveMQ Pulse terms including Agent, Calculation, Contextualisation, Discovery, Expression Language, Governed Data, Unified Namespace, and other key concepts.

## Optional

- [Upgrade Guides](https://docs.hivemq.com/hivemq/latest/upgrade/index.html): Version migration guides from HiveMQ 3.x to 4.x

HiveMQ Upgrade Guides show you how to upgrade from one HiveMQ version to another HiveMQ version. HiveMQ uses semantic versioning for its version numbers with a major.minor.patch scheme where each monthly release is compatible with the next 18 monthly releases.

- [Load Balancer Setup](https://docs.hivemq.com/hivemq/latest/user-guide/load-balancer.html): Load balancer configuration for HiveMQ clusters

A load balancer is a specialized technology used to evenly distribute incoming traffic across a cluster of servers. For production use cases, HiveMQ clusters are usually placed behind a load balancer to enhance scalability and improve overall system performance.

- [Backup & Restore](https://docs.hivemq.com/hivemq/latest/user-guide/backup-restore.html): Data backup and recovery procedures

Backups are an important part of every mission-critical MQTT deployment as all software with persistent data carries the risk of data loss. HiveMQ provides two convenient ways to backup and restore your data: from the HiveMQ Control Center or with the HiveMQ REST API.

- [MQTT Add-ons](https://docs.hivemq.com/hivemq/latest/user-guide/mqtt-add-ons.html): MQTT protocol add-on features

HiveMQ MQTT Add-ons extend the standard functionality of MQTT to satisfy the needs of several key IoT use cases. HiveMQ MQTT Topic Add-ons are special analytical MQTT topics that you can use to automatically collect detailed information for all expired, dropped, or dead MQTT messages.

- [Cloud Installation](https://docs.hivemq.com/hivemq/latest/user-guide/install-in-cloud.html): Deploy HiveMQ on AWS, Azure, GCP

HiveMQ is a cloud-native MQTT messaging broker that is enterprise-ready and well-designed for organizations that want to build and run scalable applications in modern, dynamic environments. You can install HiveMQ on the cloud service provider of your choice with basic installation information provided for frequently-used public cloud providers.

# Source: https://docs.pentaho.com/pdc-whats-new/book-abstract-for-pdc-release-notes.md

# What's new in Pentaho Data Catalog

## Pentaho Data Catalog Overview

A modern organization must be data fit. As data volumes increase, so too does the complexity, necessity, and cost of maintaining data in a state that is ready for business use. To harness data for business decisions and enable artificial intelligence, it is imperative that data is reliable, of high quality, and readily accessible to data users. The need to discover content across structured, semi-structured, and unstructured formats, both on-premises and in the cloud, is more critical than ever. Organizations must continuously monitor their data to identify trends and anomalies and maintain data hygiene in tandem with data growth. Organizations need to bring business vocabulary, governance policies, data and users of data, both applications and people together. Pentaho Data Catalog bridges the gap between raw technical assets and business strategy, ensuring the entire organization speaks the same language.

**Turn metadata into meaningful insights**

Pentaho Data Catalog automatically aligns your business glossary with the physical data dictionary. By leveraging AI/ML and GenAI "fingerprinting," we create a unified view that allows business and technical users to collaborate seamlessly. You gain visibility beyond rows and columns, including BI reports, applications, and ML models, providing a 360-degree view of how data flows through your systems.

**Automate governance and compliance**

Move from manual oversight to automated adherence. Our policy hierarchy and metadata rules provide a rigorous framework for data storage, lifecycle management, and access standards. This ensures your team spends less time auditing and more time innovating, with built-in capabilities to assess and document compliance automatically.

**Accelerate delivery with Data Products**

Simplify the complex. Pentaho Data Catalog empowers you to package data into Data Products, offering a user-friendly interface that streamlines delivery to any target destination. This product-centric approach ensures data is "ready to use," drastically reducing the time-to-value for analysts and stakeholders.

**Optimize costs and reduce risk**

Eliminate the "ROT" (Redundant, Obsolete, and Trivial data) that inflates your storage costs. By analyzing data freshness, duplication, and business context, you can make informed decisions to optimize storage investments against the actual value of the data.

**Tailored user experiences**

Intelligence is only useful if it's accessible. Our interface is configured for the specific role an individual plays in your organization. Whether utilizing the intuitive search or exploring complex relationships via the Galaxy View (Tree and Graph) representation, users see exactly the information they are authorized to access, exactly how they need to see it.

#### **Role‑Based Access Control (RBAC)**

Pentaho Data Catalog implements Role-based Access Control. Within your environment, RBAC is used to:

* Define **who can view, create, update, or delete** business terms, data assets, BI reports, workflows, and configurations.
* Support different personas, such as *Data User, Business User, Business Steward, Data Steward, Administrator, Data Developer*, each with clearly scoped privileges for governance, workflows, and data operations.
* Enforce access control patterns (for example, restricting CUD operations in workflow‑enabled virtual folders to only workflow participants).

RBAC strengthens security by ensuring users see only what they are allowed to see and do only what their responsibilities require, improving governance, reducing risk, and enhancing collaboration.

Documentation for this release is at the following links:

{% embed url="<https://docs.pentaho.com/>" %}

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4>Install Pentaho Data Catalog</h4></td><td>Install PDC with step by step instructions</td><td><a href="https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/">Install Pentaho Data Catalog</a></td></tr><tr><td><h4>Get started with Pentaho Data Catalog</h4></td><td>Set up and begin using PDC</td><td><a href="https://app.gitbook.com/s/uhk9gkhnIr3lLhiJ0Ubq/">Get started with Pentaho Data Catalog</a></td></tr><tr><td><h4>Administer Pentaho Data Catalog</h4></td><td>Configure, manage, and maintain PDC</td><td><a href="https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/">Administer Pentaho Data Catalog</a></td></tr><tr><td><h4>Use Pentaho Data Catalog</h4></td><td>Use PDC for data discovery, governance, and analysic</td><td><a href="https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/">Use Pentaho Data Catalog</a></td></tr><tr><td><h4>PDC API Documentation</h4></td><td>Explore PDC API endpoints</td><td><a href="https://app.gitbook.com/s/nQdK93m35DUFgZ08FhMD/">PDC API Documentation v1</a></td></tr></tbody></table>

## What's new in Pentaho Data Catalog

Pentaho Data Catalog release 10.2.10 introduces new features to discover content across both structured and unstructured formats, whether on-premises or in the cloud.

Learn the highlights of the Pentaho Data Catalog releases.

* [10.2.11](#id-10.2.11)
* [10.2.9](#id-10.2.9)
* [10.2.8](#id-10.2.8)
* [10.2.7](#id-10.2.7)
* [10.2.6](#id-10.2.6)
* [10.2.5](#id-10.2.5)
* [10.2.1](#id-10.2.1)
* [10.2](#id-10.2)

### 10.2.11

**Availability note:** Version 10.2.11 includes all capabilities from 10.2.10 and additional updates. Version 10.2.10 is no longer available for download.

#### Connectivity

* **Apache Iceberg connector enhancements**\
  Expanded support for [Apache Iceberg](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-data-sources-cp/adding-a-data-source-ldc-manage-data-sources-ag#apache-iceberg-data-source), including new profiling options and compatibility with warehouses beyond S3.
* **Databricks connector**\
  Added support for [Databricks](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-data-sources-cp/adding-a-data-source-ldc-manage-data-sources-ag#databricks-data-source) as a new data source. Users can connect, select schemas, profile data, and view stats.
* **Skip SSL certificate validation for S3 data sources**\
  Added an option to skip [SSL certificate validation](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-data-sources-cp/adding-a-data-source-ldc-manage-data-sources-ag) for S3-type data sources, making it easier to connect to devices with self-signed or custom certificates.

#### Discovery and Profiling

* **BIDB statistics enhancements**\
  Updated [BIDB](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-data-catalog-user-features-cp#business-intelligence-database) with new statistics - uniqueness, density, selectivity, lexical min, and lexical max for richer data profiling insights.
* **Updated statistics to show object counts**\
  Profiling now shows accurate [object counts](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#summary-tab) for files with nested arrays (JSONL/XML), improving data insights.
* **Support for profiling compressed files**\
  You can now [profile compressed files](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-unstructured-data) (such as .gz) directly, making it easier to analyze a wider range of data formats.
* **Incremental Import** \
  For file servers and object stores, you can now configure metadata ingestion and profiling to scan only files and folders that were created or modified within a specified time range.
* **Document classification in Data Discovery**\
  Added [document classification](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-processing-data#document-classification) capabilities in the data discovery flow, supporting both ML and GenAI models for semantic term assignment.&#x20;

#### Catalog Customization

* **Custom property enhancements**\
  We’ve improved the experience of [managing custom properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-custom-properties) in this release. Now, you can create, edit, and delete custom properties all from a single landing page in the **Management** view. When creating a custom property, you have the flexibility to select the required hierarchy, root, and entity type. Additionally, Data Label management has also been consolidated into the same **Management** view.
* **UI customizations for default properties**\
  Enhanced the UI to allow customization of default properties for various entities through the **Management** view.
* **New property for Business Glossary**\
  Business glossary elements now support a configurable “**Classification**” property with values such as *Private*, *Public*, and *Company Confidential*.

#### &#x20;Configurable Lifecycle Management

* **Business glossary (beta)**\
  Support for [lifecycle management](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/workflows) of business glossaries using customizable templates that allow for different steps and authorship and review/approval users depending upon the business domain.

#### &#x20;User Experience

* **Conversational chatbot with configurable role-based access (beta)**
  * New natural language (English) user experience for search
  * Public APIs are enhanced to provide batching and other improvements

#### Miscellaneous Improvements

* **Data pipe improvements**
  * Consolidated and enhanced [Data Pipe](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-data-pipe-templates) features for improved reliability and user experience in data movement.
  * Data Products are now supported in Data Pipes.
* **Offline licensing support**\
  Introduced [offline licensing](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/offline-licensing), allowing license file uploads and validation for air-gapped or OEM environments.
* **OCP validation for OpenShift**\
  Added support for OCP validation on OpenShift, expanding compatibility.
* **Open lineage support for 0.5.x and 0.6.x**
  * Parent/Child run linkage (ParentRunFacet)\
    Track transformation hierarchy for steps like ETL Metadata Injection, Mapping (sub-transformation), Simple Mapping (sub-transformation), Single Threader, and Transformation Executor.
  * Each sub-transformation now references its parent run, enabling the lineage graph to render parent-child hierarchy and follow both multiple and nested children.
  * Bulk loader steps support\
    Added minimal lineage support (dataset-level only) for MySQL Bulk Loader, Oracle Bulk Loader, Vertica Bulk Loader, and PostgreSQL Bulk Loader steps.
* **Optimizer improvements**\
  The rehydration process no longer requires a stub file to be present by reading data directly from the migrated metadata. This streamlines workflows and removes unnecessary checks, making the optimizer more flexible.
* **Power BI service enhancements**\
  Improved [Power BI integration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#configure-a-power-bi-service-connection-in-data-catalog) by supporting Service Principal Name (SPN) authentication, handling hidden elements, deleted columns, URL support for report pages, and accurate relationships (lineage) between reports and datasets.
* **Postgres schema changes**\
  Updated Data Catalog to remove use of the '*public*' schema in Postgres, support external Postgres deployments, and provide data copy instructions for migrations.
* **Sub-transformations in lineage graphs**\
  Enhanced lineage visualization now includes sub-transformations, giving you deeper insights into your data flows.
* **Style customization for applicable hierarchies**\
  The style card present in the **Summary** view of the hierarchy now allows organizations to customize the display name and icon for different nodes to match the organization's terminology.

### 10.2.9

The key features in this release are:

* **Manual ML model relationship linking**

  You can now manually link or unlink Training and Production models and view the relationship on the summary page.
* **Business Intelligence (BI) service enhancements**

  The BI service now includes additional tabs with functionality, Custom Properties, Business Terms, Policies, Data Elements, and Comments, which provide better metadata, context, and governance.
* **Edit and delete support for custom properties and enhancements**

  You can now edit and delete custom properties across multiple hierarchies. The interface and functionality are standardized across all hierarchy types for a uniform experience. Additionally, the term **Custom Properties** is now used consistently across all modules (previously referred to as *Properties* in some modules).
* **Request access capability for Data Products**

  Users can request access to Data Products directly from the **Management** > **Request access** card or from **Global Search** results.
* **User interface improvements**

  Several usability improvements have been made across the application, including:

  * Additional editable fields in data source configuration
  * New facets in the discovery search interface
  * Search and filter options on the Workers page
  * Job resubmission from the Workers queue
  * Enhancements to the BI hierarchy view
* **Configure ingest schemas on Data Connections**

  The **Ingest Schemas** feature now includes advanced filtering options. Users can search or filter schemas using regular expressions to refine schema selection during ingestion.
* **Trust score computation using UI and API**

  You can now compute and monitor **Trust Scores** for data assets through both the **UI** and **API**, providing insights into data quality and reliability.
* **Dataset enhancements**
  * Users should now be able to provide labels to use as the display name instead of the column name captured.
  * **Summarized patterns and samples** are now generated for common dataset columns.
  * Profiling can be initiated on both **datasets** and **data collections**.
* **Profiling updates and enhanced support for secrets manager**

  Users can now visualize the profiling reports with both basic and advanced statistics and download the results. Enhanced **Secrets Manager** integration now supports secure configuration of PostgreSQL instances.
* **Lineage and Data Canvas experience hardening**

  Improved the usability and visual accuracy of the **Lineage Canvas**, including clearer relationships, better navigation, and seamless transitions between **Lineage** and **Data Canvas** views.
* **Selective hierarchical glossary export**

  You can now export specific glossaries along with their associated hierarchy (categories and terms), instead of exporting all glossaries.
* **Inclusion of Stakeholders in Glossary**\
  A new **Stakeholders** field has been added to glossary metadata, and some existing fields have been repurposed for better governance tracking.
* **Aurora PostgreSQL**

  Now supports Aurora PostgreSQL as both a data source and metadata repository, with full Secrets Manager integration.
* **LLM for document summary and address detection**

  You can now configure large language models (LLM) and enable a flag to use the configured LLMs so that document summary and address detection flows use the specified LLM in fetching address, sentiment, and document summary.&#x20;
* **User activity logging enhancements**

  Activity tracking is now extended to the **Glossary**, **Policy**, and **Application** services.\
  Logs capture *who performed what action and when* and are ingested into **OpenObserve** for centralized monitoring and analysis. For configuration details, see [User activity logging and dashboard configuration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/user-activity-logging-and-dashboard-configuration "mention").
* **EKS job scaling**

  User will now be able to identify and obtain documentation on the preferred EKS configuration, including its capacity to handle expected workloads.
* **Apache Iceberg data source** (Beta)

  Introduced Apache Iceberg as a data source. This is a Beta release and currently only supports metadata consumption. Users can now add an Iceberg data source, ingest metadata and run metadata rules against an Iceberg data source. However, this implementation does not currently support data profiling processes.
* **Chatbot provider configuration** (beta)

  You can now configure any LLM provider or model for chatbot interactions. This flexibility allows integration with different AI service providers as per organizational requirements.\
  It is available as a beta feature for PDO users.

### 10.2.8&#x20;

The key features in this release are:

* **Lineage enhancements**

  When lineage is sent from Pentaho Data Integration (PDI) to Data Catalog—either during ingestion or as a separate activity—any data connections that exist in PDI but not in PDC are automatically created in PDC. This removes the need to create data connections manually. All steps and transformations are now represented in the lineage graph.
* **Details panel enhancements to show additional information**\
  To improve lineage's value, the Details panel now displays **Trust Score**, **Business Terms**, and **Tags** when you select an asset in the lineage diagram.
* **Improved search with additional facets**\
  To improve the usability of the search functionality, additional facets are added to refine search results. You can now filter search results by **Last Profiled Date**, **Last Accessed Date**, **Last Modified Date**, **Trust Score**, and **Tags**.
* **Edit and save data connection details**\
  You can now update additional fields in existing data connections. Specifically, you can edit and change the host, port, and credentials of a data connection, and you can save them if the connection test is successful. This update allows you to modify existing connections when details change, without needing to delete and recreate them.
* **Metadata scan with include or exclude pattern filters on data connection**\
  When performing a metadata scan, you can now specify what files and folders, or patterns, to include or exclude in the scan. This allows you to limit the scope of scans to specific files or directories in a data source.
* **The default Galaxy view displays relationships**\
  When you switch from Tree view to Galaxy view, the initial display now includes all relationships (edges) of the selected asset.
* **Power BI metadata integration into PDC**\
  Data Catalog now supports the integration of Power BI. You can now connect to Power BI, fetch metadata, and view lineage to track data sources.
* **Power BI templates for sensitivity**\
  You can now apply Power BI sensitivity templates to your Power BI instance and access the sensitivity details in the Power BI application.   &#x20;
* **Text to SQL for Data Pipes**\
  The text 2 SQL functionality is introduced in Data Catalog, where you can enter plain text queries that automatically generate SQL queries based on selected tables and columns. You can approve and run, edit, or regenerate the SQL queries if not satisfied.
* **Document Summary Performance** \
  For better performance of data discovery with document summarization, GPU support has been introduced.
* **Processing of Semi-Structured files**\
  The processing of semi-structured files has shifted from row-based to columnar. At the column level, the Row property now reflects the count of values for that column rather than the total number of rows in the file.

### 10.2.7

The key features in this release are:

* **Version control of datasets**\
  Users can capture the state of a dataset by enabling them to duplicate or append data, with each action creating a new version while preserving all properties and not copying generated values. Dataset columns cannot be removed, duplication is limited to one copy per collection, and all changes are tracked through versioning.
* **Support for AWS S3 authentication modes with Secrets Manager**\
  Extending the AWS S3 data source feature to support secrets in AWS Secrets Manager, retrieve them dynamically, and use them to access S3 resources without hardcoding sensitive information.
* **Data Pipes - Containerization and deployment**\
  Simplified approach for Data Pipes to have Pentaho Data Integration (PDI) components ready to use immediately after deploying the PDC image, without manual setup steps like downloading, unpacking, configuring, or starting services separately.
* **UI improvements**
  * **Design appropriate interface for "published" APIs**
    \
    Support for key APIs—including search, notifications, dataset management, job execution, and status retrieval, many more.
  * **Select and add tables to a Collection/dataset**
    \
    A Data Catalog user can search by a pattern, filter, and multi-select matching results, and add them in bulk to a dataset or collection easily and further **Add to Cart** in the table view of the data canvas.
* **Lineage Canvas enhancements: Delete manual lineage links and support for column-level lineage**\
  Enhances the PDC lineage canvas by allowing users to delete manually added lineage while maintaining the integrity of system-generated lineage and introduces support for column-level lineage transformations to enable detailed tracking of field-level data changes. It also addresses multiple UI and UX bugs to provide a more seamless and intuitive user experience.
* **Profiling Support for Semi-Structured data – Parquet**\
  Profiling support for Parquet and part files enhances users' ability to analyze and tag these file types.
* **Azure Blob to Azure Blob**

  Pentaho Data Optimizer (PDO) users can migrate data between different Azure Blob or ADLS Gen2 instances, enabling movement from hot/expensive storage to cool, cold, or archive tiers to optimize and reduce storage costs. This feature leverages Azure’s tiered storage options, allowing efficient data management based on access frequency and retention needs.
* **Enhance gateway service to support custom model endpoints**

  Users can configure custom model endpoints for both request and response models and specify environment variables required for their machine learning (ML) services. This enables seamless integration and flexible deployment of custom ML models by supporting endpoint customization and necessary runtime configuration.
* **Infrastructure configuration for AWS deployment**
  * Ingest all PDC logs into Amazon CloudWatch to centralize monitoring and log analysis for the AWS deployment.
  * Restrict OpenSearch access by default to enhance security.
  * Confirm compatibility with Kubernetes 1.32 for the deployment.
  * Document Fluentbit configuration steps for connecting to CloudWatch.
  * PDC Helm chart to support using a customer's OpenSearch instance on the public cloud.
* **Production ML models - Nvidia Triton inference server**

  Machine learning (ML) models hierarchy service, which imports metadata up to pre-production, has been extended to capture production model inference details, including data, metadata, and metrics such as successes and failures.
* #### Structured and semi-structured file profiling options

  Data Catalog users can profile both structured and semi-structured files, perform data discovery when selecting multiple files or entire folders simultaneously, and apply profiling actions in bulk across all applicable data types.
* #### Support for IRSA, CAR, and Istio
  * **IAM Roles for Service Accounts (IRSA) support for PDC**: Provides a secure and convenient way to grant Kubernetes pods access to AWS resources.
  * **CAR Integration**: Allow IAM users to assume roles for cross-account AWS service access when interacting with PDC “Data Resource” through the Cross-Account Role (CAR) feature.
  * **Istio on EKS**: Provides a streamlined process to install Istio Service Mesh on Amazon EKS using the EKS add-on in Ambient mode, combined with deploying the PDC application configured to use the AWS ALB Ingress Controller.

### 10.2.6

The key features in this release are:

* **Improved data sampling features**
  * Added support for extracting data samples directly from files, with a new **Extract Samples** feature and an option to **Skip recent days** in the data discovery interface.
  * Enhanced visibility of sample data by capturing and displaying both the **count** and **percentage** of sample values.
* **Masking of sensitive data**\
  Introduced the ability to mask sensitive data within the **View Samples** interface, so that data can now be masked dynamically based on configured **Tags** and **Sensitivity** values.
* **Data profiling**\
  Enhanced profiling capabilities with support for multi-level JSON files.
* **Data Collections**
  * Enhanced **Data Collections** functionality with integration into **Galaxy View**, and the ability to add or remove custom properties, policies, and other relationships.
  * You can now also assign data labels and publish physical assets to a collection.
* **Collapsible cards**\
  On the **Summary** tabs, any empty cards are now collapsed by default. Users can expand the cards as needed, and their configuration will be saved automatically for future sessions.
* **EKS support**
  \
  Enhanced support for deploying Data Catalog on Amazon EKS, including a configuration option to integrate with AWS CloudWatch for monitoring and logging.

### 10.2.5

The key features in this release are:

* **Discovery (faceted search)**

  Support for full text search across asset types in Data Catalog and the ability to filter results using facets.
* **Data delivery**

  Data pipe functionality now supports encryption. This requires Pentaho Data Integration (PDI) engine to be deployed and configured
* **ML Models hierarchy**

  A structured model hierarchy for integrating ML models, versions, experiments, runs, and associated metadata. It also includes governance elements like policies, glossaries, and applications managed within Data Catalog.
* **Tableau support and reports lineage**

  Integrating metadata from Tableau workbooks, reports, dashboards, and other assets, along with their relationships to data sources and datasets, effectively tracks data lineage.
* **Request access**

  Users can request permission to access metadata of data assets in Data Catalog, initiating a workflow for review and approval by data owners or administrators to ensure secure data access management using ServiceNow and JIRA.
* **Data labelling**

  Provide meaningful labels to data assets that enhance data discovery, understanding, governance, and trust within the organizational data landscape to help users quickly grasp the context and characteristics of data assets without needing to inspect the raw data itself.
* **Data profiling enhancements**

  Ability to provide a WHERE clause to filter candidate rows for profiling.
* **Data Products**

  Select data assets (tables and files) to create a collection, provide guidance on the sensitivity and quality of the collection and deliver a data product, to be shared within the organization
* **Document discovery enhancements**

  Support the ability to summarize a document and detect sentiment using ML models
* **Similarity detection for tabular data (Tables and Files)**

  Use the column names to determine potential duplicate tables and files that have similar structures.
* **PDI – PDC Lineage**

  Automatically track, visualize, and analyze data’s entire journey through PDI lineage, making this information accessible in the Pentaho Data Catalog for governance, compliance, and insights.
* **Business Intelligence Database (BIDB) migration to PostgreSQL**\
  The Business Intelligence Database (BIDB) has been migrated from **MongoDB** to **PostgreSQL**.  Users can now connect directly to BIDB using standard **PostgreSQL JDBC/ODBC drivers** with PostgreSQL authentication only.

### 10.2.1

The key features in this release are:

* **Product licensing support**
  * Your software license determines user-based, data source count and data capacity entitlement
  * There are two tiers of users: Business Users and Expert Users
  * Additional licensed features available for Data Optimizer and Data Mastering
* **Data delivery**

  Enhancements to data delivery via Data Pipes to support additional databases, Object and file store options.
* **OT asset hierarchy**

  Offers a comprehensive operational and industrial data context, encompassing policies, applications, and a business glossary. It plays a crucial role in facilitating the convergence of IT and OT systems.
* **Improved rule engine**

  We have enhanced the rule engine to decouple the Definitions from the Rule. You can now create a definition with multiple actions and using this definition create a rule to apply it to all your applicable data sources in a few clicks.
* **Additional data source support**

  Pentaho Data Catalog 10.2.1 now supports Metadata Ingest, Data Profiling and Data Identification of InfluxDB, Redshift, Google Big Query, Sybase and Salesforce.
* **Import and export**

  To facilitate migration and onboarding we have introduced support for importing and exporting the following assets: Data Connections, Dictionaries, Patterns, Rule Definitions, Business Glossary, Policies and Applications.
* **Add relationships and display for BI Assets**

  Pentaho Data Catalog now supports the Term, Policy/Standards and Reference data relations to BI report asset types.
* **User guided sampling**

  We have introduced user guided sampling to allow users to profile data based on a subset of rows rather than profiling all rows in a large table.

### 10.2

The key features in this release are:

* **Data delivery**

  A business user is able to find data and with a few clicks be able to configure a data pipeline that delivers the data to its desired destination.
* **Application catalog**

  Catalog your applications, their governance requirements, ownership, their relationship with data assets, reference data and other elements in the data catalog
* **Governance policies**

  Document regulatory or corporate regulations, policies, standards in the catalog, building a source of record and an intuitive interface to find policies and the data to which they apply.
* **Data lineage**

  Build data lineage for data movement executed by Pentaho ETL. Compatible with open lineage, this capability gives us a quick ROI for customers interested in lineage for Pentaho Data Integration.
* **Galaxy view**

  This release enhances the visual representation of assets (such as data assets, business terms, policies/standards/rules, reference data, and applications) to easily grasp the dependencies, understand potential impact, and collaborate with all the stakeholders to make the right business decision.
* **Trust score**

  Support for bringing data quality scores from the Pentaho Data Quality product, verification of lineage, and assessing sensitivity to build a trust score.
* **License support**

  This release introduces a license solution for the Data Catalog and Pentaho Data Optimizer products. You can configure the number of data sources and Expert users (Steward, Admin, Developer) you can add, and the size of data scanned from file systems.

In addition, there are numerous improvements including extensive rules support, additional support for data sources and technologies, and continued emphasis on ease of use and performance improvements.

# Source: https://docs.pentaho.com/pdc-use/pdc-data-pipe-templates.md

# Data Pipe Template

Data Pipe Templates in Pentaho Data Catalog are configurable, reusable templates that allow users to automate data movement and management tasks across file systems and storage platforms. This feature is designed to simplify repetitive workflows by enabling users to define standard actions, such as duplicating, moving, or purging data, and apply them consistently across various data sources.

## Key capabilities of data pipe templates

The following are the key capabilities of the data pipe template feature:

### **Supports multiple data sources**

Data pipe templates in Data Catalog work seamlessly across various enterprise data environments. Whether the data resides in structured databases, file systems, or modern object stores, you can move, duplicate, and purge the data using data pipe templates. Data pipe templates support data assets across:

* Relational Database Management Systems (RDBMS) like Oracle, MSSQL, MySQL, Postgres, IBM DB2, Snowflake, and Vertica
* File systems like SMB, NFS, and CIFS
* Object store data sources like AWS, HCP, and Azure\
  **Note:** Data sources must be enabled for data movement. You can enable it while adding data sources. If not, you can edit the data source settings and select **Available for Migration** and **Available for Writing** to enable data movement. For more information, see the [Manage data sources](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-data-sources-cp "mention")section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ "mention") guide.

### **Dual engine processing**

The data pipe templates feature supports various RDBMS, file systems, and object storage solutions, enabling flexibility in data movement across different storage types using Data Optimizer and Data Integration engines.

**Important:** The data pipe templates feature uses Data Optimizer and Data Integration engines. To know more about deploying Data Catalog with the Data Integration engine, see  [Deploy Data Catalog with bundled PDI services](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/install-data-catalog/deploy-data-catalog-with-bundled-pdi-services "mention"). For any support with Data Integration engine setup and configuration, contact [Pentaho Support](https://support.pentaho.com/).

#### **Data Integration engine**

The Data Integration engine supports data movement between RDBMS data sources. Templates include:

* RDBMS like MySQL, MSSQL, Oracle, Postgres, and Snowflake:
  * RDBMS to RDBMS
  * RDBMS to file systems
  * RDBMS to object stores
* Object stores like AWS, AZURE GEN2, and HCP:
  * Object stores to object stores
  * Object stores to file systems
* File systems like SMB and HDFS:
  * File system to file system
  * File system to object stores

#### **Data Optimizer engine**

The Data Optimizer engine supports data movement between file system and object store data sources. Templates include:

* File systems like SMB and CIFS:
  * File system to file system
  * File system to object storage
* Object storage like AWS, HCP, and Azure:
  * Object storage to object store
  * Object storage to file system\
    Additionally, you can monitor the process and receive notifications upon task completion. For information on creating a data pipe template, see the [Create a data pipe template](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc_manage-data-pipe-templates#create-a-data-pipe-template) topic in the [Manage data pipe templates](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc_manage-data-pipe-templates) section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/) guide.

**Note:** You can perform specific actions based on the roles and permissions you have in Data Catalog. For more information, see [#default-user-roles-and-permissions](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions#default-user-roles-and-permissions "mention").

### **Cross-platform data duplication and movement**

Data pipe templates facilitate data movement and duplication across heterogeneous data platforms. This includes structured data from relational databases (RDBMS) and unstructured or semi-structured data from file systems and object stores. Data pipe templates support copying or transferring data from relational databases to object stores, enabling the transformation of structured data into industry-standard file formats. This is especially valuable for organizations that:

* Want to consolidate data from RDBMS into a data lake for analytics.
* Need to offload operational data to cheaper storage tiers.
* Require repeatable, auditable data transfers for compliance or governance.\
  The supported formats for data export include:
* CSV (Comma-Separated Values): Ideal for flat file exports and interoperability.
* Parquet: A columnar storage format optimized for analytical workloads and supported by modern data lake technologies.

### **Reusable templates**

Data pipe templates in Data Catalog are designed for reusability, which means you can define a data movement or transformation logic once and apply it across multiple datasets or scopes without the need to recreate or modify the original template. A single data pipe template can be reused to execute actions on different data assets, such as folders and individual files in file systems or object stores, and database tables and columns.

The same template can be run across different environments or projects, simply by changing the scope or execution context; no changes to the logic or structure of the template are needed. With this, you can avoid repetitive configuration of actions like duplication, movement, tagging, or encryption. Instead, you can select an existing template, assign a new scope, and execute the data pipe.

### **Main and optional actions**

In Data Catalog, data pipe templates support two categories of actions that define the behavior of data processing during data migration using data pipe templates:

* **Main Actions**: These define the core behavior of the data pipe template workflow.
* **Optional Actions**: These provide additional governance, tagging, security, and communication enhancements.**Note:** The availability of main and optional actions depends on the engine selected (**Data Integration** or **Data Optimizer**) and the type of main action chosen.

#### **Main actions**

Main actions are required and define what happens to the data selected by the data pipe template. Based on the selected engine and data source type (structured or unstructured), one or more of the following actions become available:

* **Duplicate Data**: Copies data from the source location to a target location while retaining the original. It is commonly used for backups, cloud offloads, or data replication. This action is supported across structured (RDBMS) and unstructured (file/object) data sources. When duplicating structured data (RDBMS), it supports privacy features such as column masking or encryption (if configured via the [Data Integration](#data-integration-engine) engine).
* **Move Data**: Transfers data from the source to the destination and removes it from the source after successful transfer. It is suitable for archiving or shifting datasets to a new environment. Additionally, it ensures storage optimization by preventing data duplication.
* **Purge Data**: Permanently deletes the selected data from the source location without creating a copy. It is useful for cleaning up temporary or obsolete data.

  **CAUTION**: This action is irreversible and should be configured with appropriate access controls.

#### **Optional actions**

Optional actions enhance the data pipe's functionality by adding metadata, security, and communication features. These appear based on the main action selected and offer additional control and visibility over data movement. The optional actions dynamically change based on the selected data sources and main action.

* **Tag Source**: Allows the user to apply a business tag or metadata term to the source data before or after execution.
* **Tag Destination**: Enables tagging of the destination data asset to clarify the context or purpose of duplication or movement.
* **Send Notification**: Triggers a notification to individuals or groups upon completion of the data pipe execution.
* **Allow Stub Creation**: Enables the creation of stubs in place of the moved or purged files. Stubs are placeholders that retain metadata and can facilitate data rehydration in the future if needed.
* **Privacy**: Gives access to privacy configurations such as masking or encrypting sensitive columns for structured (RDBMS) data. It appears only when duplicating structured data to another structured destination using the **Data Integration** engine. It supports Pattern-based, Regex-based masking and encryption using FES/ACS. For more information, see **Advanced data privacy** feature.

  **Note:** The Privacy option is only available when duplicating structured (RDBMS) data and selecting another structured data source as the target.

### **Advanced data privacy**

In Data Catalog, the data pipe template gives data privacy capabilities when duplicating structured (RDBMS) data using the [Data Integration engine](#data-integration-engine). These features help organizations comply with internal security policies and regulatory requirements such as GDPR, HIPAA, and CCPA by ensuring that sensitive information is protected during data movement.

When duplicating data between structured sources, such as PostgreSQL to SQL Server or from Oracle to Amazon RDS, you can apply masking and encryption rules to individual columns within a dataset. This ensures that personally identifiable information (PII) or other sensitive data is not exposed during or after the data movement process.

These privacy actions can be configured during the data pipe template creation process under the **Privacy** option (visible only when duplicating structured data with the **Data Integration** engine).

The data pipe template supports the following masking techniques to protect sensitive information:

* **Pattern-based masking**

  This technique allows you to replace selected characters in a column with a specified masking character (such as \*), while optionally preserving a portion of the original value, either at the beginning or end.

  Example: Mask all but the last four digits of an ID number

  * Original: 7894561234
  * Masked: \*\*\*\*\*\*1234
* **Regex-based masking**

  This method uses regular expressions to identify and transform values based on specific patterns, offering fine-grained control for complex data structures.

  Example: Replace any 10-digit phone number with a standardized masked format.

  * Original: 9876543210
  * Masked: XXX-XXX-XXXX
* **Field Encryption Services (FES)**

  Encrypt specific columns using Field Encryption Services (FES), which applies secure cryptographic algorithms during the duplication process. The encrypted values can only be decrypted by authorized services or users with proper keys.

  Example: Encrypt email addresses in user databases to ensure they are unreadable in non-production environments.
* **Advanced Cryptographic Services (ACS)**

  For organizations with enhanced security requirements, Advanced Cryptographic Services (ACS) offers stronger encryption methods, customizable key management, and integration with enterprise-grade encryption frameworks.

  Example: Use AES-256 encryption with user-managed keys to protect financial or healthcare data as it is replicated to a third-party system.
* **Scheduling support**

  In Data Catalog, you can schedule the execution of data pipe templates at predefined times or recurring intervals like **Daily**, **Weekly**, and **Monthly**. This ensures that actions such as data archiving, replication, or purging occur consistently and in alignment with business processes. To learn more about scheduling, see the [Schedule data movement with a data pipe template](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc_manage-data-pipe-templates#schedule-data-movement-with-a-data-pipe-template) topic in the [Manage data pipe templates](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc_manage-data-pipe-templates) section of the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.

## Data pipe template workflow

A data pipe template in Data Catalog follows this main workflow:

1. Define the data migration scope or choose data from connected databases. Based on the selected asset, structured or unstructured, the data pipe template selects the Data Integration engine for structured data and the Data Optimizer engine for unstructured and file system data sources.
2. Select an action available on **Main Actions**:
   * **Move Data**: Transfers data from the source to the target and removes it from the original location.
   * **Purge Data**: Cleans data from specific locations based on predefined criteria.

     **Note:** The available actions might vary based on the engine used by data pipe template.
   * **Duplicate Data**: Copies data from the source to the target without affecting the original.
3. Select a destination database where you want to move or copy data.

In addition to the primary workflow, data pipe templates support these optional workflow actions:

* **Tag Destination**: Add tags to source and destination data to identify why data is moved or copied.
* **Send Notification**: Notify a person or group of people.
* **Allow Stub Creation**: Create stubs that can be used to rehydrate later.
* **Privacy**: Configure the data privacy rules to secure sensitive information.

![Data pipe template page showing all main and oprtional actions](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-c0eda55b890e1f1c5eceac928969aabe9904f330%2FData%20Pipes%20Landing%20Page%3DGUID-ED032E6A-DA2F-4E4F-89E4-A03CD2B9C52A%3D1%3Den%3DLow.png?alt=media)

To learn more about creating, scheduling, and editing data pipe templates, see the [Manage data pipe templates](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc_manage-data-pipe-templates) section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

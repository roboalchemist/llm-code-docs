# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data.md

# Processing data

You can extract meaningful insights and ensure the effective utilization of data with Data Catalog processing. The significant stages in the processing of data are:

1. **Metadata Ingest**
2. **Data Profiling** (for structured data) and **Data Discovery** (for unstructured data)
3. **Data Identification** for structured data, including delimited files
4. **Usage Statistics** for the Microsoft SQL and Oracle databases
5. **PII Detection**
6. **Calculate Trust Score**

**Note:** Your Data Catalog license determines the number of data sources you can add, and the amount of data you can scan. Databases do not have a data scan quota.

## Metadata Ingest

The **Metadata Ingest** step updates Data Catalog to reflect current metadata changes. The Metadata Ingest step scans the data source for new or modified files since the last run, updating the existing metadata. In addition, it removes metadata for deleted files, ensuring Data Catalog represents the data source accurately.

There are additional options as follows:

**Delete empty folders** - when selected it will delete folders without any child entities from the PDC metadata store

**Incremental Ingest -** Ingests data for Filesystems or Object stores where files/objects Created or Modified time stamps match the time period selected. This will not remove any existing data fro previous ingests and can be used when you only want to ingest data from a particular timeframe. Time periods available are (Last) 12 Hours, 24 Hours, 1 Week, 1 Month and 3 Months.&#x20;

**Note:** If you are close to or have exceeded the quota of data you can scan with your license, you see a message in the upper corner of the screen when you try to start a scan. If you have exceeded the amount of data you can scan, you are unable to start a scan.

## Data Profiling and Data Discovery

The **Data Profiling** and **Data Discovery** steps are crucial for analyzing both structured and unstructured data, respectively.

### **Data Profiling**

In the **Data Profiling** process, Data Catalog examines structured data within JDBC data sources and gathers statistics about the data. It profiles data in the cluster and uses its algorithms to compute detailed properties, including field-level data quality metrics, data statistics, and data patterns.

**Note:** When configuring data profiling, it is considered a best practice to use the default settings as they are suitable for most situations. With the default settings, the data profiling is limited to 500,000 rows.

### **Data Discovery**

In the **Data Discovery** process, Data Catalog examines unstructured data by scanning file contents to compile data statistics, which involves the following steps:

* Calculating checksums to identify duplicates, if the **Compute checksum of document contents** checkbox is selected.
* Extracting document properties from Office365 and PDF files.
* Using dictionaries to scan documents for specific strings and keywords, triggering predefined actions.
* Profiling data within the cluster to ascertain detailed attributes, including quality metrics, statistics, and patterns for delimited files.\
  These processes ensure a thorough understanding and assessment of both structured and unstructured data, setting a solid foundation for subsequent analysis.
* Extracting and classifying text from scanned documents and image files using Optical Character Recognition (OCR). When the OCR option is configured, during Data Discovery and Document Processing, Data Catalog uses the configured OCR engine (Tesseract or EasyOCR) to extract text from image-based content. The extracted text is then scanned against predefined data patterns, enabling users to identify sensitive information, apply tags, and associate matched values with relevant business glossary terms. For more information, see the [PDC OCR feature walkthrough](https://hitachi-vantara.navattic.com/o0h00dd?g=cmh8q0etb000204laaudh3ii2\&s=0).

## Data Identification

The **Data Identification** process helps to manage your structured data, including delimited files. It involves tagging data to make it easier to search, retrieve, and analyze. By associating dictionaries and data patterns with tables and columns, you can ensure that data is appropriately categorized and easily accessed when needed.

**CAUTION:** You must run **Data Profiling** (for structured data) or **Data Discovery** (for unstructured data) before proceeding with any **Data Identification** activities.

## Usage Statistics

When processing supported databases, Data Catalog gives an additional feature, **Usage Statistics**. The Usage Statistics feature is a capability in Data Catalog (PDC) that captures and stores metadata, including the number of times an entity is read, written to, or altered in the [Business Intelligence Database (BIDB)](https://docs.pentaho.com/pdc-use/ldc-data-catalog-user-features-cp#business-intelligence-database).

Usage Statistics provides clear insights into data consumption, highlighting the most frequently accessed entities. This supports resource optimization, strengthens governance through usage audit trails, and enables impact analysis by showing which entities are affected by changes in data flow.

{% hint style="info" %}
Note: The Usage Statistics process is only available for the Microsoft SQL, Oracle, and Snowflake databases.

* Microsoft SQL Server and Oracle: The auditing feature in the respective databases must be enabled to capture and save usage statistics. For Microsoft SQL and Oracle databases, the auditing feature should be enabled. For more information, refer to the official documentation for [Microsoft SQL](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine) and [Oracle](https://docs.oracle.com/cd/E26401_01/doc.122/e22952/T156458T663771.htm).
* Snowflake: Usage statistics are available without additional configuration.
  {% endhint %}

When you run the Usage Statistics process, the Entity Usage Worker job retrieves various usage metrics, including the number of times an entity is read, written, and altered from an audit database, and stores them under the **Entity Usage Statistic View** within the BIDB. You can use this repository for analysis and visualization of the data with third-party BI tools. For more information, see [Business Intelligence Database](https://docs.pentaho.com/pdc-use/ldc-data-catalog-user-features-cp#business-intelligence-database).

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FTfKO1Pro85loytuJ6uEy%2Fimage.png?alt=media&#x26;token=9cadc71a-7ba2-4b8b-8032-e356ec7af020" alt=""><figcaption></figcaption></figure>

Additionally, you can also view certain usage-related properties in the [Properties panel](https://docs.pentaho.com/pdc-use/pdc-data-canvas-explore-your-data#properties-panel) of the [Summary tab](https://docs.pentaho.com/pdc-use/pdc-data-canvas-explore-your-data#content-pane) in [Data Canvas](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data). The properties displayed may vary depending on the selected data asset.

<div align="left"><figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2F5kQWTqsKL5AuOBcEDmxs%2Fimage.png?alt=media&#x26;token=25ad8020-4994-4b75-aada-9852b5025c70" alt=""><figcaption></figcaption></figure></div>

## PII Detection

The PII Detection feature in Data Catalog uses Machine Learning (ML) and Large Language Models (LLMs) to analyze data in JDBC tables and identify Personally Identifiable Information (PII). This feature is specifically trained for Korean and Japanese datasets and automatically detects and classifies sensitive data, such as names, addresses, and ID numbers. It helps you to streamline compliance with privacy regulations by automatically identifying and classifying personally identifiable information (PII) in datasets. To learn more, see [PII Detection](#pii-detection).

**Note:** This feature currently supports only JDBC data sources with Korean and Japanese content.

,When you start PII Detection, Data Catalog scans the selected JDBC table for column names that contain PII entities. Once the process is complete and if PII data is identified:

* A new glossary titled **ML\_PII** is automatically created (if not already present). If the **ML\_PII** glossary already exists, newly identified PII terms are added to it.
* Detected PII entities are tagged with relevant business terms from the **ML\_PII** glossary.

These tags appear in the Business Terms panel of the respective columns.

## Calculate Trust Score

The Calculate Trust Score feature in Data Catalog allows users to compute and monitor the quality and reliability of data assets. The score is calculated using multiple parameters like **Data Quality**, **User Ratings**, **Data Lineage**, and **Classification**. Users can manually or programmatically initiate the computation or refresh the score, ensuring up-to-date trust information for decision-making.

Users can manually or programmatically initiate and refresh the Trust Score calculation via Data Canvas or API. Trust Score calculation considers:

* Data Quality (Completeness, Accuracy, Validity, Uniqueness, Consistency)
* User Ratings (1–5 stars)
* Data Lineage (Verified or Not)
* Glossary Term assigned or not&#x20;

{% hint style="info" %}
This feature is currently available for Tables and Files and is not available in public API's.
{% endhint %}

To initiate the Calculate Trust Score process:

1. Select the table(s) or file(s).
2. Navigate to the **Actions** menu and choose **Process**.\
   The **Choose Process** page appears.
3. On the **Calculate Trust Score** card, click **Start.** \
   The Calculate Trust Score process starts and appears in the **Workers** page.

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FXOdbOaoIIAlZ4vgJ0NhB%2Fimage.png?alt=media&#x26;token=61dafdf4-8841-4d42-9caf-1a420905676f" alt=""><figcaption></figcaption></figure>

After the process completes, the Trust Score calculation result appears in the Key Metrics panel for the selected entity.

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fy8AZEuGYhYj588aHS5MB%2Fimage.png?alt=media&#x26;token=41dc9c1e-c40e-4369-9c35-a6f16556fed6" alt="" width="375"><figcaption></figcaption></figure>

## AI-assisted document processing <a href="#ai-assisted-document-processing" id="ai-assisted-document-processing"></a>

Pentaho Data Catalog provides AI-assisted document processing capabilities, such as [summarize documents](#summarize-documents), [address detection](#address-detection), and [document classification](#document-classification), that use default ML models in the Data Catalog or any custom large language models (LLMs) to analyze unstructured documents and enrich them with meaningful metadata. These capabilities help users understand, organize, and govern unstructured content at scale without manual review.

Data Catalog includes built-in machine-learning models for AI-assisted document processing features. To use more advanced or scalable language models, an administrator can configure custom or third-party LLMs. See [Advanced configuration #Configure Large Language Models in Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#configure-large-language-models-in-data-catalog "mention")for more information.

During data discovery and enrichment, Data Catalog processes supported unstructured documents using built-in or configured language models. Based on the user's need, whether to detect address, summarize, or classify the document, the content will be passed to relevant models or LLM for processing. To know more about how to process unstructured documents, see [pdc-processing-unstructured-data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-unstructured-data "mention").

AI-assisted document processing is supported only for unstructured documents with English-language content. It doesn’t support structured, compressed, or semi-structured files, or scanned PDFs or image files.

The following file types are supported:

* Hypertext markup formats: `htm`, `html`, `shtml`, `dhtml`, `xhtml`
* Microsoft Office formats: `doc`, `docx`, `xls`, `xlsx`, `ppt`, `pptx`
* Apple document formats: `pages`, `numbers`, `key`
* OpenDocument formats: `odp`, `ods`, `odt`, `odg`
* Electronic publication formats: `epub`, `fb2`
* Mail formats: `msg`, `pst`, `edb`, `ost`, `eml`, `mbox`
* XML formats: `xml`, `tld`, `xsd`, `xsl`, `xslt`, `xaml`, `wsdl`, `dtd`
* JSON formats: `json`, `jsonl`
* Other text formats: `rtf`, `txt`, `pdf`

### Summarize documents <a href="#summarize-documents" id="summarize-documents"></a>

The summarize documents feature uses Data Catalog default models or configured large language models (LLMs) to generate concise summaries of unstructured documents in Data Catalog. Document summaries help you to quickly understand the purpose and key content of a document without reading it in full. Summaries generated from the document text are displayed on the entity page. This allows users to search, review, and govern documents more efficiently, especially when working with large volumes of unstructured content. You can use this feature to:

* Quickly understand long or complex documents
* Identify document relevance before detailed review
* Support data discovery and governance workflows involving unstructured content

This feature is particularly useful for legal, policy, contractual, and reference documents where a high-level overview is often sufficient for initial assessment.

### Address Detection <a href="#address-detection" id="address-detection"></a>

The address detection feature uses Data Catalog default models or configured large language models (LLMs) to identify and extract address-related information from unstructured documents in Data Catalog. This capability helps you to detect physical or postal addresses embedded within document content and represent them as metadata in the catalog. By automatically detecting address information, Data Catalog supports governance, compliance, and discovery workflows that require visibility into documents containing location-based or personally identifiable information.

You can use the address detection feature to:

* Identify documents that contain physical or postal addresses
* Support compliance and regulatory review processes
* Improve search and filtering for documents with location-related content

This feature is useful in scenarios involving contracts, correspondence, invoices, forms, and other documents where address information is commonly embedded in free text.

### Document classification <a href="#document-classification" id="document-classification"></a>

Document classification is a AI-assisted document processing capability in Data Catalog that helps in classifying unstructured documents based on their content. This feature extends the document discovery workflow by enabling you to associate meaningful business classifications with files, improving document organization, searchability, and governance.

Using document classification, you can provide one or more classification terms that represent business concepts, such as *Invoice*, *Contract*, or *HR Policy*. Data Catalog semantically matches the classifications returned by the default model or a configured large language model (LLM) with the business terms provided. If the match meets the configured threshold value, Data Catalog assigns the corresponding business terms to the document. This process does not rely on exact keyword matching, allowing Data Catalog to classify documents based on meaning rather than literal text.

#### **Classify documents**

You can use the document classification feature to classify unstructured documents based on their content, rather than relying on exact keyword matches. Perform the following steps to process and classify unstructured documents:

Document classification is triggered through the Data Discovery workflow . You can monitor its progress from the **Workers** page.

**Procedure**

1. Log in to Data Catalog and in the left navigation menu, click **Data Canvas**.
2. Browse or search for the documents that you want to classify.
3. Select one or more documents and click **Process**.\
   The **Choose Process** page opens with **Metadata Ingest**, **Data Discovery**, and **Data Identification** options. To know more about the processes, see [Processing data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data).
4. Click **Data Discovery.**\
   Ensure you have run the **Metadata Ingest** process before proceeding to **Data Discovery**.
5. In the **Document Processing** tab, select **Data Classification**.
6. Click **Add Terms,** select one or more classification terms that represent the business concepts you want Data Catalog to identify in the selected documents, and click **Add**.

   For example, `Invoice, Contract, HR Policy`. If you don’t find the required business terms, you can create them. For more information, see [Manage business glossary](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-business-glossary-administer-pdc "mention").
7. Click **Start Discovering**.\
   You can view the status of the **Data Discovery** process on the **Manage Workers** page.

**Result**

After the classification job completes with a **SUCCESS** status, Data Catalog adds the matching business terms to the processed documents based on the semantic match. Documents without a meaningful match remain unclassified.

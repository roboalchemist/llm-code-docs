# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-unstructured-data.md

# Processing structured, unstructured, and semi-structured files

You can use Data Catalog to profile a wide variety of file types, including structured, unstructured, and semi-structured files. These file-based assets share the same user interface and profiling workflow. During profiling, the system analyzes file content and metadata to extract insights such as field patterns, value distribution, and document structure.

Data Catalog supports profiling of a wide range of file-based data assets. The following table highlights the major categories and commonly used file types that share a unified profiling interface and results:

{% hint style="info" %}
Data Catalog supports more file formats than those listed in the following table. For a comprehensive list of supported file formats and compatibility details, contact [Pentaho Support](https://support.pentaho.com).
{% endhint %}

<table><thead><tr><th width="150.11114501953125">Category</th><th width="162.66656494140625">File Types</th><th>Additional Information</th></tr></thead><tbody><tr><td>Structured files</td><td><code>.csv</code>, <code>.tsv</code>, <code>.psv</code></td><td>Structured files with consistent field delimiters. You can configure header row detection and delimiter type during profiling.</td></tr><tr><td>Compressed files</td><td><code>.gz</code>, <code>.snappy</code>, <code>.deflate</code>, <code>.bz2</code>, <code>.lzo</code>, <code>.lz4</code></td><td> </td></tr><tr><td>Unstructured documents</td><td><code>.pdf</code>, <code>.doc</code>, <code>.docx</code>, <code>.txt</code>, <code>.rtf</code></td><td>Profiling extracts document metadata and textual content. Includes string detection, summarization, and duplicate detection.</td></tr><tr><td>Semi-structured files</td><td><code>.parquet</code> , <code>.json</code>, <code>.avro</code>, <code>.orc</code></td><td>Stores structured data in columnar format. Profiling includes schema detection, field types, null values, and value frequency analysis.</td></tr></tbody></table>

Perform the following steps to process the structured, unstructured, and semi-structured files:

{% hint style="info" %}
Structured (delimited) and semi-structured files are treated as unstructured but can be profiled via Data Discovery with structured outputs.
{% endhint %}

1. Select the structured, unstructured, and semi-structured resources you want to investigate in Data Canvas.

   This can be a file or a folder. To detect duplicates, select the files or folders you want to check for duplicates.

2. Click **Process**.

   The Choose Process pane opens with **Metadata Ingest**, **Data Discovery**, and **Data Identification** options.

   ![Unstructured data processing options](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-3f297e52123374c427a77a73313bdf4297264c2c%2FPDC_Data%20Processing_Unstructured.jpg?alt=media)

3. In the Metadata Ingest card, click **Start** to begin the metadata ingestion.

   You can view the status of the **Metadata Ingest** process on the [Manage Workers](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-worker-processes-cp) page.

   **Note:** If you have already scanned more than 75% of your data quota, you see a message when you start the scan. Even if you cannot scan new data, you still can run Data Discovery or Data Identification on data you have already scanned.

4. To perform the data discovery, click the **Data Discovery** card.

   The **Configure Process** page opens with the three tabs: **Data Discovery**, **Document Processing**, and **Data Profiling**. Configure the process by using the options available under these three tabs.

   **Note:** When configuring data discovery, it is recommended to use the default settings as they are suitable for most situations.

5. In the **Data Discovery** tab, configure the following options:
   1. **Checksum Calculation**

      <table><thead><tr><th width="203.77777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Compute checksum of document content</strong></td><td>Calculates checksums for each file which are used to detect duplicates. After processing, any duplicate files are displayed on the Duplicates tab.</td></tr></tbody></table>
   2. **Advanced Options**

      <table><thead><tr><th width="207.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Files Modified More Than Day(s) Ago</strong></td><td>Filters file processing by modification timestamp.</td></tr><tr><td><strong>Files Accessed More Than Day(s) Ago</strong></td><td>Filters file processing by access timestamp.</td></tr></tbody></table>

6. Click the **Document Processing** tab, and configure the following options:

   1. **Machine Learning Options**\
      **Note:** These options use Machine Learning and Large Language Models.

      <table><thead><tr><th width="208.88885498046875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Summarize Documents</strong></td><td>Generate a concise summary of unstructured files such as .docx, .pdf, and .rtx and more. The summary appears under the Document Summary section of the asset’s Summary tab. Also performs sentiment analysis, which is shown under the Data Labels section. For more information, see <a data-mention href="..#summarize-documents">#summarize-documents</a>.</td></tr><tr><td><strong>Address Detection</strong></td><td>Scans documents for U.S. postal addresses. When this option is selected, you must choose a relevant business term. If addresses are found, the selected business term is automatically tagged to the asset and displayed in the Business Terms panel. For more information, see <a data-mention href="..#address-detection">#address-detection</a>.</td></tr><tr><td><strong>Data Classification</strong></td><td>Classifies unstructured documents based on their semantic content using machine learning. When this option is selected, you provide one or more business terms that represent the classifications you want to identify. Data Catalog analyzes the document content and automatically assigns the matching business terms to documents where a semantic match is found. The assigned classifications are displayed in the Business Terms panel of the asset. For more information, see <a data-mention href="..#document-classification">#document-classification</a>.</td></tr></tbody></table>
   2. **Document Metadata**

      <table><thead><tr><th width="213.77777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Extract document properties</strong></td><td>Collects additional document properties from the file, such as the owner, page count, number of paragraphs, and so on. It applies only to Office365 or PDF files.</td></tr></tbody></table>
   3. **Content Scan for String Detection**

      <table><thead><tr><th width="214.88885498046875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Detect presence of strings</strong></td><td>Based on the applied dictionary, if the dictionary value exists in the file, it applies the actions defined in the dictionary and returns true in the metadata store (mds).</td></tr><tr><td><strong>Determine presence and count of occurrences both</strong></td><td>Based on the applied dictionary, if the dictionary value exists in the file, it returns the aggregate count of the dictionary values within the file in the metadata store and applies the actions defined in the dictionary.</td></tr></tbody></table>
   4. **String Detection**\
      **Note:** During the string detection process, it ignores the rules defined in the dictionaries.

      <table><thead><tr><th width="217.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Add Dictionary</strong></td><td>Select and add available dictionaries to use in string detection and to apply actions specified in the dictionary.</td></tr><tr><td><strong>Add Patterns</strong></td><td>Select and add available patterns to use in string detection and to apply actions specified in the patterns. [PA1]</td></tr></tbody></table>
   5. **Advanced Options**

      <table><thead><tr><th width="220.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Include File Extensions</strong></td><td>Specify the document extension, such as pdf, .doc, .txt, and so on. Profiling is performed for the specified extension. Leave empty to use all supported extensions.</td></tr><tr><td><strong>Restrict Processing to Max File Size of</strong></td><td>Files larger in size than this amount are skipped. For example, 100 MB.</td></tr><tr><td><strong>File Processing Threads</strong></td><td>Number of processing threads for file processing per job (should keep this low if running many jobs).</td></tr><tr><td><strong>Persistence Threads</strong></td><td>Number of persistence writing per job (should keep this low if running many jobs).</td></tr></tbody></table>

7. Click the **Data Profiling** tab for structured (delimited) files and configure:

   <table><thead><tr><th width="225.5555419921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Extract samples</strong></td><td>Extracts a small random sample of data (typically ~200 rows) for preview and validation during profiling and displays it in the summary tab. It is generally used internally.</td></tr><tr><td><strong>Treat First Row as Header (only for structured or delimited files)</strong></td><td>When you set the flag during profiling, the Data Discovery step considers the first row of the data as a header and assigns its values to the column names in the profiled data.If you don't set the flag, the Data Discovery step assigns default names like column-0, column-1, column-2, and so on to the profiled data.</td></tr><tr><td><strong>Skip Recent (days)</strong></td><td>Skips profiling for recently profiled tables. For example, if the days field is set to 7, any table profiled within the last 7 days is skipped.</td></tr><tr><td><strong>Include Patterns*</strong></td><td>Add global patterns to apply during profiling.</td></tr><tr><td><strong>Exclude Patterns*</strong></td><td>Add global patterns to exclude during profiling.Note: If files or folders match both include and exclude patterns, then profiling excludes the patterns.</td></tr></tbody></table>

   \* For more information about patterns and limitations, see [Java documentation](https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/nio/file/FileSystem.html#getPathMatcher\(java.lang.String\)).

8. Click **Start Discovering**.

   You can view the status of the **Data Discovery** process on the [Manage Workers](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-worker-processes-cp) page.

9. (Optional) To perform data identification on structured and semi-structured files, click the **Data Identification** card.

   **Important:** You must perform **Data Discovery** before proceeding with the **Data Identification** process. If the **Data Discovery** process was not completed previously, Data Catalog highlights the Configure Process as **Required**. Expand the **Configure Process** and complete the process.

   <figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FapYzw5gCr1VgMDSmcNR0%2Fimage.png?alt=media&#x26;token=a20e251d-8d40-499c-a3d0-83c047a124ab" alt=""><figcaption></figcaption></figure>

10. Click **Select Methods**, select the **Dictionaries** and **Patterns**, click **Apply**, and then click **Start**.

    You can view the status of the **Data Identification** process on the Manage Workers page.

11. Go to **Data Canvas** and select the processed file to view its properties.

The selected structured, unstructured, or semi-structured files are processed, and the document properties are displayed in the **Document Properties** pane. Samples from structured and semi-structured files are available in the **Sample Data** pane, providing insights into data distribution and characteristics. Additionally, you can also explore the file’s relationships and tags using the [Galaxy View](https://docs.pentaho.com/pdc-use/pdc-galaxy-view).

{% hint style="info" %}
The displayed unstructured properties vary based on the selected unstructured data type.
{% endhint %}

# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data.md

# Data Canvas

Use the Data Canvas page to explore and investigate your data. Here, you can find detailed insights into resource metadata to help you understand and clarify practical applications. Click **Data Canvas** in the left navigation menu to open the Data Canvas view and begin exploring your data. Be sure to add at least one data source to Data Catalog before exploring. See the **Administer Pentaho Data Catalog** document for more information.

The **Data Canvas** is divided into two primary areas:

![Navigation and Content areas of Data Canvas page marked with numbers](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-9459e95d245666e5414d1842068730909c0ef818%2FPDC%20Data%20canvas%20areas%20\(Explore%20your%20data\).png?alt=media)

<table><thead><tr><th width="87.88885498046875">Item</th><th width="139">Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td><strong>Navigation</strong></td><td>Navigate the tree of data resources to find the one you want to explore in the canvas.</td></tr><tr><td>2</td><td><strong>Content</strong></td><td>Displays information about the selected resource. For example, if you select a folder or schema, the metadata appears in the Content pane.</td></tr></tbody></table>

Select a data element in the Navigation pane and view its details in the Content pane. The details vary by resource type. For example, selecting a folder or schema displays the metadata in the Content pane.

## Navigation pane

Navigate the tree of data resources to find the one you want to explore in Data Canvas in Data Catalog. Expand the data source and select the resources you want to work with, then view the structure of your data source in the Content pane. In addition, you can enter a search term in the **Search** field to search for resources such as folders, schemas, tables, files, or fields within the navigation pane.

When you select an individual or multiple resource, the resource name is highlighted in the tree view and the metadata of that resource displays in the Content pane. You can view the name of the selected item and the path in the banner. From the Moremenu, you can choose one of the following actions:

![Process and Move data options on Data Canvas](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-75e36a7ed3e210db270801a5ed1600d058343f14%2FPDC%20Data%20Canvas%20Content%20Pane_Process%20and%20Move%20Data.png?alt=media)

### **Process**

Opens the Choose Process page, where you can view and select available processes to run on the selected resource. For more information, see the Get started with Pentaho Data Catalog document.

### **Move Data**

Opens the Data Pipes page with the selected resource automatically set in the Scope field. You can create a data pipe template that helps to speed the migration, duplication, or purging of datasets. The available actions and engines on the Data Pipes page depend on the type of data source selected. If you select assets from:

* Structured data sources (such as Oracle, PostgreSQL, or MS SQL Server) Data Pipe Templates use the Data Integration engine, and in the main actions, **Duplicate Data**, **Move Data**, and **Purge Data** are available.
* Unstructured data sources (such as object stores and file systems) Data Pipe Templates use the Data Optimizer engine, and in the main actions, only **Move Data** and **Purge Data**are available.\
  For more information, see the **Manage Data Pipes Template** section in the **Administer Pentaho Data Catalog** document.

## Content pane

You can view details about the selected resource in the Content pane in the respective tabs. The details displayed depend on the type of resource selected. For example, if you select a table, then you can view the contents of a column or field, the resource-level metadata with data analysis, cardinality for fields, and sample values.

![Content pane with numbered areas](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-5bfe1310d7c90479796e6434e1a6b9a8f954c837%2FPDC%20Data%20canvas%20with%20More%20menu%20and%20Actions%20button.png?alt=media)

The following table identifies the key details available in the Content pane for a table resource:

<table><thead><tr><th width="127.88885498046875" align="center">Screen area</th><th width="143.33331298828125">Name</th><th>Description</th></tr></thead><tbody><tr><td align="center">1</td><td><strong>Actions</strong> button</td><td><p>Click to view actions available for processing, saving, and copying the data, depending on the selected asset type. The actions you can take in the data content area are:</p><ul><li><strong>Process:</strong> Process the selected data.</li><li><strong>View Galaxy:</strong> Change to a Galaxy view of the data.</li><li><strong>Copy Path:</strong> Copy the data path.</li><li><strong>View Data Movement:</strong> View Data Pipe templates.</li><li><strong>Migrate*:</strong> Choose the location and move the selected data assets.</li><li><strong>Delete*:</strong> Deletes the file from the file server.</li></ul><p><strong>CAUTION:</strong> Once you delete a data asset, you cannot recover it.<br></p><p>* These options appear only when:</p><ol><li>You have a license for Data Optimizer.</li><li>You have imported the data source in Data Optimizer. For more information, see <strong>Importing a data source</strong> in <strong>Administer Pentaho Data Catalog</strong>.</li><li>You have selected a data asset (file type) that Data Optimizer supports.</li></ol></td></tr><tr><td align="center">2</td><td>Data tabs</td><td><p>Click to view additional information about the resource. The tabs you see might vary according to the resource that is selected.</p><ul><li><strong>Summary</strong></li><li><strong>Details</strong></li><li><strong>Properties</strong></li><li><strong>Glossary</strong></li><li><strong>More</strong> - view additional tabs of information, such as <strong>Applications</strong>, <strong>Policies</strong>, <strong>Comment</strong>, and <strong>Similar Items</strong>.</li></ul></td></tr></tbody></table>

### **Summary tab**

In Data Catalog, you can view metadata in graphical formats like value histograms and unique value counts to help you analyze data quickly. You can also view sample values, and profiled samples.

To open a data type profile, navigate to the column in the resource you want to view and click it to explore the field-level data.

When viewing column details, you can see the resource field-level metadata along with data analysis, cardinality for fields, and sample values. To show metadata in the resource field, you need native access to the resource or metadata level as governed by the RBAC settings for your user role.

Depending on the selected resource level or data element, you can view different summaries of information, including the following resource metrics:

#### **Description**

Displays a description of the resource that is imported from the source. You can contribute resource information to the knowledge base to write content and include links to other articles in Data Catalog. To edit the description, click **Edit Description**, which will open a dialog box where you can format the text using tools like bold, italic, underline, and strikeout. You can also align text, insert code blocks, and add links as needed.

#### **System Information**

When you choose an unstructured file, **System Information** displays the timestamps for file creation, modification, and last access.

{% hint style="danger" %}

* In certain file systems, when a file's modification date is less than its creation date, certain APIs, like the SMB network client, might display the more recent date as the modification date.
* In NFS and CIFS data sources, when you modify a file, Data Catalog might display the same timestamp for both the **Date Created** and **Date Last Modified** fields.
  {% endhint %}

#### **Statistics**

When you select a table, you can view the **Field Count** and **Row Count** statistics. The following table identifies the key details available in the **Statistics** pane when you select a column in a table to view:

<table><thead><tr><th width="146.6666259765625">Feature</th><th>Description</th></tr></thead><tbody><tr><td><strong>Null Count</strong></td><td>Number of entries that are null.</td></tr><tr><td><strong>Cardinality</strong></td><td>The number of unique values in a field, where a low cardinality number indicates many repeated values.</td></tr><tr><td><strong>HLL</strong></td><td>An estimate of cardinality of the data, with a roughly ~2% margin of error.</td></tr><tr><td><strong>Blank Count</strong></td><td>The number of entries that are blank.</td></tr><tr><td><strong>Min Width</strong></td><td>The minimum number of character count in a value in the column.</td></tr><tr><td><strong>Max Width</strong></td><td>The maximum number of character count in a value in the column.</td></tr><tr><td><strong>Avg Width</strong></td><td>The average number of character count in a value in the column.</td></tr><tr><td><strong>Uniqueness</strong></td><td>The uniqueness of the values in a field</td></tr><tr><td><strong>Density</strong></td><td>The percentage of fields with actual values</td></tr><tr><td><strong>Selectivity</strong></td><td>The percentage selectivity of a column. The higher the value the more effective a query is in narrowing down a result set</td></tr><tr><td><strong>Stdev Value</strong></td><td>The spread or dispersion of the data points in that column relative to the column's mean (average)</td></tr><tr><td><strong>Lexical Min</strong></td><td>Smallest possible version of a string or array when compared in dictionary (lexicographical) order</td></tr><tr><td><strong>Lexical Max</strong></td><td>Lexical Max: Largest possible version of a string or array when compared in dictionary (lexicographical) order</td></tr><tr><td></td><td></td></tr></tbody></table>

#### **Data Patterns**

In Data Catalog, data pattern analysis offers insightful recommendations based on detected patterns and their frequency. These recommendations include RegEx expressions, catering to different levels of pattern matching precision: loose, moderate, and strict. Data Catalog gives you the flexibility to choose the most appropriate patterns. Simplifying the patterns by focusing on just the characters 'A,' 'a,' 'n,' and 's' reveals the underlying data patterns more clearly. After obtaining a set of simplified patterns along with their respective frequency counts, candidate RegEx expressions can be generated. The following options demonstrate possible RegEx expressions tailored to the desired level of strictness:

<table><thead><tr><th width="208.4444580078125">Pattern</th><th>Description</th></tr></thead><tbody><tr><td>^\w{2}\d{5}$</td><td>Loose Pattern: This pattern is less strict and excludes the last value in the example with 80% confidence.</td></tr><tr><td>^[K]\w\d{5}$</td><td>Strict first letter and five digits: This expression maintains strict criteria for the first letter while allowing for variability in the subsequent characters.</td></tr><tr><td>^[K]\w\d{5,6}$</td><td>Loose on the second character: This pattern ensures 100% confidence but introduces flexibility for the second character.</td></tr><tr><td>^[K][A,L,T,W]\d{5,6}$</td><td>More Strict Pattern: This expression imposes stricter conditions while maintaining 100% confidence.</td></tr><tr><td>^[A-Z][A-Z]\d{5,6}$</td><td>Another 100% confidence pattern that differs in its structure.</td></tr></tbody></table>

{% hint style="warning" %}
If your user role does not grant access to the field or viewing level of the information, the Data Patterns pane does not appear.
{% endhint %}

#### **Sample Data**

During data [profiling of structured data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-structured-data), when you select the **Extract Samples** option, a small random sample of data is extracted and displayed in the *Sample Data* pane under the *Details* tab of a column. It provides sample values from the column to help you preview and validate data, as well as help to understand the data distribution. The Sample Data pane has two tabs: **Raw** and **Aggregated**.

* **Raw** tab: Displays a random set of individual sample values from the column.
  \
  Text names and values are truncated after 200 characters. Use the Raw tab to review how actual values appear in the data set.

  <div align="left"><figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FXykYeVi73mMPNr6rnjYs%2Fimage.png?alt=media&#x26;token=36a0f0a0-704e-4ab9-86fd-13a77b27b3ec" alt="" width="563"><figcaption></figcaption></figure></div>

* **Aggregated** tab: Groups identical values and displays each unique value only once, along with its frequency and percentage. This view helps you quickly identify the most common values and their relative distribution in the column. For example, a value such as “white” appears once in the list, with a count of rows containing that value and its percentage of the total.<br>

  <figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2F9UsQ8dcjZCt29j758x2N%2Fimage.png?alt=media&#x26;token=61f24246-a145-4d72-8271-507161fae1d4" alt=""><figcaption></figcaption></figure>

To view this pane, your role must allow Sample Data Access through native system permissions. If your user role has administrative privileges, you can configure these values. If not, contact your administrator for details.

{% hint style="info" %}
**Important:** Data Catalog governs access to view sample data with the **View samples** permission. Users with this permission can see sample data, but users without the **View samples** permission see the sample data in a masked format, such as **\*\*\*\*\*\* \*\* \*\***, ensuring sensitive information remains protected. For information on permissions, see [Default user roles and permissions](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions#default-user-roles-and-permissions).
{% endhint %}

#### **Lineage**

Displays a visual representation of the history of the selected data, including its origin, flow, and transformations. Data lineage provides visibility into the data’s historical context and authenticity, which helps in understanding how data is manipulated and transformed across different processes and systems. You can click **View Lineage** to focus on the lineage and add a manual lineage.

#### **Key Metrics**

Shows the following important characteristics of the resource:

* **Data Quality:** The **Data Quality** metric is visible if you purchase and configure Pentaho Data Quality, and process data with the **Data Quality Loader** process.
* **Sensitivity:** By default, **Sensitivity** is set to **Unknown**. You can set the **Sensitivity** level to **Low**, **Medium**, or **High**.
* **Data Lineage: Data Lineage** is visible if the resource is the resource is a table, column, or file. By default, **Data Lineage** is **Unverified**. You can set **Data Lineage** to **Verified** or **Unverified**.
* **Trust Score:** By default, the **Trust Score** for a resource is **Untrusted**. You can enter a score, which sets the **Trust Score** to **Untrusted**, **Trusted**, or **Highly Trusted**, depending on the score.

#### **Properties panel**

The **Properties** panel displays a summary of the selected resource, including details such as the last update timestamp, name, version, and type of the resource.

For Microsoft SQL, Oracle, or Snowflake data sources, when the [Usage Statistics](https://docs.pentaho.com/pdc-use/pdc-processing-data#usage-statistics) process is run, the panel also displays usage-related properties. These properties provide insights into how the resource is accessed and modified. Examples include:

* **Read Count**: Number of times the entity has been queried or read.
* **Write Count**: Number of times the entity has been updated or written to.
* **Alter Count**: Number of times the entity’s structure has been altered.
* **Last Accessed Time**: Timestamp of the most recent access.
* **First Accessed Time**: Timestamp of the first recorded access.

{% hint style="info" %}
The availability of usage properties depends on the data source and configuration. For more information, see [#usage-statistics](https://docs.pentaho.com/pdc-use/pdc-processing-data#usage-statistics "mention").
{% endhint %}

#### **Business Terms panel**

Lists associated business terms for the resource. You can also click **Add Term** to open the Business Terms dialog box and add terms to the resource. For more information, see the **Administer Pentaho Data Catalog** document.

#### **Tags panel**

Lists the tags associated with the resource. In addition, you can click and start adding tags like “quality:45” (the key should be unique) to the resource, which helps to identify the resource with tagged keywords.

#### **Custom Properties panel**

Lists the first five custom properties associated with the resource. Custom properties refer to user-defined metadata attributes or fields that can be associated with various data assets, such as databases, tables, files, or documents, to provide additional context and information about those assets. To add a custom property, click **Add Custom Property** and provide the required information. In addition, go to the **Properties** tab to see the complete list of custom properties added to the resource.

#### **Data Storage Administrator view**

If you have the Data Storage Administrator role in Data Catalog, you can have access to enhanced views within the Data Canvas for root-level folders of Object Stores like AWS S3, Azure Blob Storage, and file systems like CIFS, NFS, SMB, and many more. The following are the UI components available in this role-specific view.

<div align="left"><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-88deee9068826ef178f56690e7543a7936caf090%2FCards%20available%20for%20Data%20Storage%20Administrator.png?alt=media" alt="The UI cards available to the Data Storage Administrator role" width="563"></div>

* **Used Capacity:** This tile shows the total storage consumed by all files and folders under the selected data source or root directory. It helps you to quickly identify storage-intensive locations and supports capacity planning.
* **Count of Subfolders:** This tile shows the number of immediate subfolders present under the root directory, offering a quick view of the folder hierarchy and helping to assess structural complexity.
* **Count of Files/Entities:** This tile shows the number of duplicate file groups identified in the data source. With this, you can reduce redundancy and improve storage efficiency by detecting duplicate files.
* **Duplicate Groups:** This tile shows the number of duplicate file groups identified in the data source. With this, you can reduce redundancy and improve storage efficiency by detecting duplicate files.
* **Top 10 Summary View:** This graph is an interactive bar chart that provides a visual overview of key folder-level metrics within the selected data source. You can toggle between three views:
  * **Child Folders**: Displays the top 10 subfolders by count.
  * **Child Files**: Shows the top 10 folders based on the number of contained files.
  * **Used Capacity**: Highlights the top 10 folders by total storage consumed.\
    This visualization helps to compare folder usage patterns, identify high-volume or high-capacity directories, and prioritize areas for optimization.
* **Files by Temperature:** The **Files by Temprature**graph shows the distribution of files based on their access and modification activity, referred to as data temperature. Files are grouped into categories such as Hot, Warm, Cold, or Unclassified (used when temperature metadata is unavailable). This visualization helps to assess how actively data is being used, helping to identify hot (frequently accessed), warm, or cold (rarely accessed) data. Understanding the data temperature helps you to make informed decisions around data retention, archival, and storage cost optimization.

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FclhsWbD4DJGcaRrRNqZ9%2Fimage.png?alt=media&#x26;token=b5fb53c8-66a2-4069-9b1e-50baac0f451a" alt=""><figcaption><p>Count of files by data temperature</p></figcaption></figure>

* **Files by Type**

  The **Files by Type** graph visualizes the distribution of files based on their format, such as CSV, JSON, PDF, DOCX, ZIP, and others. This chart helps you to understand the diversity of file types stored within a data source and evaluate the degree of file format standardization. This visibility of file types supports better metadata governance, content classification, and downstream processing decisions.

  ![Count of files by type](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-788be45743f30309215aa05cff10a38e14fa54d8%2FFiles%20by%20type.png?alt=media)

**Note:** In the graphs, you can hover over the columns to view the exact count of items, along with additional information.

### Details tab

The **Details** tab displays detailed information about child resources. You can view the items available in the selected resource, along with some additional information. The information varies based on the resource selected. For example, if you select a data source, you can view available items like a schema for structured data and folders for file systems. It is a detailed breakdown of folder contents, which can help in storage auditing and metadata review. Each row in the list represents a subfolder and includes:

* **Item Name**: Name of the folder or file
* **Item Type**: Indicates if it's a folder or file.
* **Duplicate Groups**: Number of duplicate file groups within that folder.
* **Used Capacity**: Total size of files in the folder.
* **Oldest Child Date**: Earliest recorded access or modification timestamp of any item within the folder.
* **Youngest Child Date**: Most recent access or modification timestamp.
* **Data Temperature**: A link to view more metadata on created, modified, and accessed dates.

When you select a schema, you can view the number of tables and columns it contains, along with associated tags, row counts, and the last profiled date and time. In addition, you can click **View** in each row to open the corresponding data asset in a focused view within the Data Canvas.

The **Details** tab provides filter options for each column. You can apply these filters to narrow down the displayed assets, making asset selection efficient. When you apply filters and select one or more checkboxes, the **Add to Cart** button becomes active.

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fs8TltRccrPYGjrDZEqK9%2Fimage.png?alt=media&#x26;token=9b20bf90-0e60-4ffd-9b99-401471ee58ad" alt=""><figcaption></figcaption></figure>

Clicking **Add to Cart** adds the selected items to your cart. After items are added, you can [create a data set](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-collections#create-a-dataset) or [data collection](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-collections#create-a-data-collection) based on your selected data type. The processes to create data sets or data collections remain unchanged. For more information, see [Manage collections](https://docs.pentaho.com/pdc-admin/pdc-manage-collections) in the [Administer Pentaho Data Catalog](https://docs.pentaho.com/pdc-admin) guide.

### Properties tab

View the custom properties added to the resource and the details like name and value. You can also add custom properties and edit the value of a property. For more information, see [Resource properties](https://docs.pentaho.com/pdc-use/ldc-resource-properties-user-guide-cp).

### Glossary tab

Explore the business terms information on the resource, such as category, glossary, definition, and purpose. In addition, you can also add business terms to the resource. For more information, see [Business Glossary](https://docs.pentaho.com/pdc-use/pdc-business-glossary).

### Applications tab

Lists any applications associated with the selected resource, with details such as the application name, parent and owner of the application. You can sort the columns and add applications if you have permission to do so. For more information, see [Applications](https://docs.pentaho.com/pdc-use/pdc-applications-ug)**.**

### Policies tab

View the policies and standards associated with the resource. With permission to modify a policy, you can add or delete a standard association. For more information on policies and standards, see [Policies and standards](https://docs.pentaho.com/pdc-use/pdc-policies-and-standards-ug)**.**

### Comment tab

The **Comment** tab is a collaborative feature that allows users to discuss and provide feedback on specific data assets within Data Catalog. You can add comments, share suggestions, or ask questions directly in the tab using the provided text box, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the Mentions tab on the Data Catalog landing page, prompting them to respond if necessary. For more information, see [Tour of the Home page](https://docs.pentaho.com/pdc-use/ldc-quick-start-user-guide-cp#tour-of-the-home-page).

**Note:** In the Comment tab, you can:

* Tag users who have been configured in Data Catalog.
* Only delete the comments you posted.
* Delete any comment if you are an admin.

### Duplicates tab

If the **Compute checksum of document content** checkbox was selected when the **Data Discovery** process was used to process unstructured data, you can see any duplicate files listed on the **Duplicates** tab. Files are determined to be duplicates if they have the same checksum. You can view the contents of each file by clicking **View** on the file listing. For more information, see [Processing unstructured data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-unstructured-data).

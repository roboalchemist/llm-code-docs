# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-collections.md

# Collections

In Pentaho Data Catalog, a **Collection** is a way to logically group data assets, such as schemas, tables, and files, so that you can work with them more efficiently. Whether you are analyzing similar datasets or combining diverse data sources, Collections allow you to organize and manage your data entities based on structure or business use case.

Collections help you bring together related data assets in a meaningful and organized manner. You can group tables, files, or schemas that belong to the same business context or project, making it easier to organize and access them. For Datasets, you can streamline analysis by identifying common columns across multiple tables and using profiling and aggregation jobs to evaluate data structure and quality.

Data Catalog supports two types of Collections:

* **Dataset**: A Dataset is a group of homogeneous data assets, such as tables or files that share the same schema.
* **Data Collection**: A Data Collection is a group of heterogeneous data assets, such as files, tables, or schemas, with different structures.

Collections also support governance by allowing you to assign business terms, trust scores, and sensitivity levels, helping ensure your data meets organizational standards. Once curated, Collections can be shared with your team or published as **Data Products**, making them easily discoverable and reusable across the organization.

**Note:** By default, datasets and data collections are visible only to their owners unless shared explicitly. You can publish a Dataset or Data Collection as a Data Product to make it visible to all users in Data Catalog. For more information, see Components of Collections.

## Components of collections

In Data Catalog, Collections are organized using a hierarchical structure that helps you manage data logically and efficiently. The following table describes the components of this hierarchy:

<table><thead><tr><th width="78.11114501953125" align="center">Item</th><th width="148.5555419921875">Component</th><th>Description</th><th>Example</th></tr></thead><tbody><tr><td align="center">1</td><td>Category</td><td>The top-level container used to group collections by domain, department, or project.</td><td>Finance, Sales, Healthcare, or Marketing Analytics</td></tr><tr><td align="center">2</td><td>Group</td><td>A subfolder within a category that organizes datasets or collections around a specific subject, source, or use case.</td><td>Monthly Reports, Vendor Data, or Customer Feedback</td></tr><tr><td align="center">3</td><td>Dataset</td><td>A collection of homogeneous data, such as tables or files that share the same schema. Datasets support profiling and aggregation.</td><td>A group of .csv files with the same columns from different months</td></tr><tr><td align="center">4</td><td>Data Collection</td><td>A collection of heterogeneous data, such as files, tables, or schemas that differ in structure. Used for organizing logically related but structurally different assets.</td><td>A folder containing SQL tables, Excel files, and PDFs related to a project</td></tr><tr><td align="center">5</td><td>Data Product</td><td>A curated Dataset or Data Collection that meets publishing criteria and is made available for broader discovery and consumption.</td><td>A verified Customer Profile Dataset shared with analysts across teams.</td></tr></tbody></table>

The hierarchy flows from Category > Group > Dataset or Data Collection and can result in a **Data Product** when published.

### Category

In Data Catalog, a **Category** is the top-level container in the **Collections** hierarchy. It helps you group related data assets based on a broader business domain, department, or organizational function. Categories act as entry points that help you to organize and locate collections more easily. It simplifies navigation within Data Catalog, where you can quickly browse and locate relevant Groups and Collections. By structuring data under Categories, teams can standardize how they store and manage related datasets, making collaboration easier and more efficient.

A **Category** contains one or more **Groups**, which in turn contain **Datasets** or **Data Collections**. These collections can be published as **Data Products**. For example, a Finance category may include groups such as Monthly Reports or Audit Logs, each containing relevant Datasets or Data Collections

### Group

In Data Catalog, a **Group** is a child container within a **Category** that helps further organize data assets in the **Collection** hierarchy. It allows users to structure **Collections**, such as **Datasets** and **Data Collections**, based on more specific topics, projects, or data sources within a broader business domain. A Group can also contain nested groups, allowing you to build deeper hierarchies for complex data structures.

Groups provide an intermediate layer of organization between the high-level **Category** and the individual collections, making it easier to maintain clarity and consistency in large or complex data environments. For example, within a Sales Category, you might create Groups such as Quarterly Reports, Customer Feedback, or Channel Partner Data, each containing its respective datasets.

### Dataset

In Data Catalog, a **Dataset** is a collection of homogeneous data assets, such as tables or files that share the same schema or structure. A **Dataset** is ideal when you want to analyze multiple data items that have identical columns and formats, making it possible to evaluate them as a unified group.

A **Dataset** contains a group of two or more tables or files that share the same column structure, allowing them to be analyzed together. It includes the results of processing jobs such as data profiling, which evaluates the structure and quality of each file or table, and aggregation, which computes summary statistics across common columns. For example, a Group called Customer Transactions under the Finance Category might include a Dataset of monthly transaction files that all follow the same format.

In addition to raw data, a Dataset also stores metadata, including tags, sensitivity levels, and trust scores. Additionally, you can associate custom properties, data labels, business terms, external applications, policies, and physical assets on the respective tabs. These attributes help provide context and support governance. A **Dataset** also features a columns canvas, which displays the common columns found across all included files or tables, along with their aggregated metrics, giving users a unified view of the dataset's structure and quality. To learn more about running data profiling or aggregation jobs, see [Processing collections](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-collections).

### Data Collection

In Data Catalog, a **Data Collection** is a logical grouping of heterogeneous data assets, such as files, tables, or schemas that differ in structure or format. Unlike a Dataset, which requires a common schema, you can combine diverse data sources that are related by purpose or business context rather than structure and create a Data Collection. A Data Collection can include a variety of data assets with different schemas and formats. It may contain:

* Tables from different databases
* Files of various types (for example, CSV, Excel, JSON, XML)
* Schemas or partially structured data

**Note:** Data Collection is ideal when you want to group data assets for organizational or governance purposes, even if those assets vary in layout, columns, or type.

A **Data Collection** is created under a **Group**, which belongs to a **Category**. It is present alongside Datasets within the same Group and, like Datasets, can be enriched with metadata or published as a Data Product. For example, within a Group named Vendor Management under the Procurement Category, you might create a Data Collection that includes PDFs, Excel reports, and SQL tables, all related to supplier performance.

In Data Collections, you can apply metadata, including tags, sensitivity levels, and trust scores, to add context and enforce governance standards. Additionally, you can associate custom properties, data labels, business terms, external applications, policies, and physical assets on the respective tabs. Role-based visibility and access controls ensure that only authorized users can view or modify the collection. Data Collections can also be shared with specific users or teams to support collaboration. Additionally, Data Collections can be published as Data Products for broader discovery across the organization, once they meet the required standards.

### Data Product

In Data Catalog, a Data Product is a curated and published version of a Dataset or Data Collection, originating from either a Dataset or a Data Collection, which is organized under a Group and a Category. After enrichment and validation, the Dataset or Data Collection can be promoted to a Data Product by publishing it. This publishing action changes its lifecycle state and makes it available in global search results and for broader consumption. For example, a Customer Insights Dataset under the Marketing Category can be published as a Data Product once it includes profiling results, sensitivity tagging, and trust scoring.

A Data Product contains all the components of its source Collection (Dataset or Data Collection), including the data assets, metadata, tags, and trust scores. Additionally, you can associate custom properties, data labels, business terms, external applications, policies, and physical assets on the respective tabs. It may also contain information about data quality, profiling results (for Datasets), and any associated governance attributes. The following are some sample criteria, which you can consider for publishing a collection as a Data Product:

* A minimum data quality threshold (for example, 60%)
* Assigned sensitivity levels
* A trust score that indicates reliability and governance readiness
* **Note:** Even if the criteria are not met, you can still choose to publish the collection as a Data Product.

Once published, Data Products are searchable through Global Search, can be filtered using metadata facets, and provide quick access to users who need verified data for reporting, analysis, or operational use. To learn more about the global search, see [Global search and discovery](https://docs.hitachivantara.com/r/en-us/pentaho-data-catalog/10.2.x/mk-95pdc000/global-search-and-discovery).

## Access and permissions for collections

In Data Catalog, access to Datasets, Data Collections, and Data Products is governed by user roles and sharing settings. By default, Datasets and Data Collections are visible only to their creators or owners. Other users cannot see or access these collections unless the owner explicitly shares them. The following are the different access levels of a Dataset or Data Collection

* Private (default): Only the creator can view, update, delete, and interact with the collection.
* Shared: The owner can share a collection with specific users, groups, or roles. The owner can grant the following access to other users:
  * **View**: The user can only view the Collection. They cannot make changes or run jobs.
  * **Update**: The user can view and modify the Collection, including editing metadata or adding tags and terms.
  * **Run**: The user can view the Collection and execute supported operations like Profile or Aggregation jobs (applicable only to Datasets).
* **Published as Data Product**: Once the owner publishes a Dataset or Data Collection as a Data Product, it is visible and searchable by all users in the catalog (unless access restrictions are defined), making it easier to discover and reuse trusted data.

To learn more about sharing and publishing collections, see the [**Manage collections** ](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-collections)section in the [**Administer Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

## Explore collections

In Data Catalog, under Collections, you can navigate and view Datasets and Data Collections through three different views: **Browse Collections**, **My Collections**, and **Shared with Me**. These views are designed to help you easily find the data assets you own, access those shared with you, and browse the wider data environment based on your access permissions.

![Different views of collections](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-e09fa3a125f1733bfa0b9895b0638c6072afbbbd%2FPDC%20Explore%20collections.png?alt=media)

### **Browse Collections**

The **Browse Collections** view displays all collections that are visible to you across the organization. This includes collections you created, collections that have been shared with you by others, and any published Data Products. This view is ideal when you need a complete overview of all accessible collections across business domains or departments.

### **My Collections**

The **My Collections** view filters the interface to show only the collections that you have created. These may include private drafts, collections that you have shared with others, or collections you are in the process of enriching or preparing for publication. This view is most useful when you're actively curating datasets or managing work-in-progress data assets.

### **Shared Collections**

The **Shared with Me** view lists all collections that other users have explicitly shared with you. These may include Datasets or Data Collections where you’ve been granted permission to view, update, or run operations. This view helps streamline collaboration by grouping shared resources in one place.

Each of these three views, **Browse Collections**, **My Collections**, and **Shared with Me**, contains the same set of tabs across the top: **All**, **Collections**, and **Data Products**. These tabs help you filter and focus your exploration based on the current state and purpose of the collection.

![My collections](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-cb9385977709b5ebfc97de3960d9e77963dafe66%2FPDC%20My%20collections.png?alt=media)

#### **All**

The **All** tab is the default view and displays every type of collection that is visible within the current context. Whether you are in **Browse Collections**, **My Collections**, or **Shared with Me**, the **All** tab will include Datasets, Data Collections, and Data Products, regardless of whether they are published or still in draft status. This tab is useful when you want a unified view of all relevant assets in one place.

#### **Collection**

The **Collections** tab narrows the display to include only those items that are in draft or shared state, typically unpublished Datasets and Data Collections. This tab is helpful when you are working on assets that are still under development or being enriched with metadata and governance attributes.

#### **Data Products**

The **Data Products** tab displays only those collections that have been published as trusted data products. These collections are intended for broader organizational consumption and usually meet defined quality and governance standards. In this tab, Data Catalog users can find vetted and reusable assets for analysis, reporting, or integration.

In all views and tabs, the data is presented in a table format with the following columns:

<table><thead><tr><th width="155.111083984375">Column Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td>The title of the Dataset or Data Collection. Clicking it opens the asset in focused view.</td></tr><tr><td><strong>Description</strong></td><td>A brief summary of what the collection represents or contains.</td></tr><tr><td><strong>Type</strong></td><td>Indicates whether the item is a Dataset (a collection of homogeneous data), a Data Collection (a collection of heterogeneous data), or a Data Product (a published and curated Dataset or Data Collection available for broader consumption).</td></tr><tr><td><strong>Owner</strong></td><td>Displays the initials of the user who created the collection.</td></tr><tr><td><strong>Date Created</strong></td><td>Shows the exact date and time the collection was initially created.</td></tr></tbody></table>

The right side of each row may include additional actions such as the **Share** icon, which opens the permission settings for the collection. To learn more about sharing Datasets and Data Collections, see [**Share collections**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-collections#share-collections) under the [**Manage Collections**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-collections) section in the [**Administer Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

## Duplicate or versioning of a collection

In Data Catalog, you can duplicate an existing Dataset or Data Collection to create a versioned copy that can be reused, enriched, or customized without impacting the original. A duplicate, or versioned collection, is an independently editable copy of an existing Dataset or Data Collection. It retains all user-defined properties, metadata, and relationships, but is treated as a new collection. You can create a duplicate in the same group or assign it to a different group. Once duplicated, the new collection includes a reference link to the original on its Properties tab, allowing users to trace its lineage and evolve independently. This helps teams experiment, enrich, or adapt datasets for new use cases, without affecting the original.

Duplicating a collection supports data versioning by allowing users to create variations of a collection for different projects or analysis scenarios, without altering the original. It also enables reuse by letting users start with an already curated collection rather than building a new one from scratch. This process ensures safety as the original collection remains unchanged and untouched throughout. Additionally, it enhances governance by clearly identifying duplicates and linking them to their source, facilitating easier tracking of lineage and maintaining data integrity.

When you duplicate a collection, the following properties and settings are preserved:

<table><thead><tr><th width="248.66668701171875">Copied Property</th><th>Description</th></tr></thead><tbody><tr><td>Collection metadata</td><td>Name (edited), description, category, and group</td></tr><tr><td>Data assets</td><td>All included files or tables from the original collection</td></tr><tr><td>Business terms</td><td>Any business glossary terms assigned to the collection</td></tr><tr><td>Sensitivity levels</td><td>Tags that define data sensitivity for compliance and security</td></tr><tr><td>Trust score</td><td>Confidence level assigned to the data asset</td></tr><tr><td>Data quality metrics</td><td>If defined manually, these values are retained</td></tr><tr><td>Tags and custom properties</td><td>Any custom metadata added to enrich the collection</td></tr><tr><td>Relationships and policies</td><td>Includes associations with other assets, such as linked reports or rules</td></tr></tbody></table>

&#x20;

Some system-generated values will not be copied to the duplicated collection:

<table><thead><tr><th width="249.5555419921875" valign="top">Not Copied</th><th valign="top">Reason</th></tr></thead><tbody><tr><td valign="top">Generated columns (Datasets)</td><td valign="top">Created by profiling or aggregation; treated as dynamic, not user-defined</td></tr><tr><td valign="top">Profiling results</td><td valign="top">Must be regenerated for the new collection</td></tr><tr><td valign="top">Sharing permissions</td><td valign="top">You must manually reassign users and roles in the new collection</td></tr><tr><td valign="top">Version history of original</td><td valign="top">The new collection starts its own version lifecycle</td></tr></tbody></table>

&#x20;While the duplicate collection feature offers flexibility and control, it has the following limitations and behavioral constraints in place to maintain data integrity, version traceability, and governance consistency:

* A collection can be duplicated only once. You cannot create multiple duplicates of the same source collection.
* Once duplicated, the original (source) collection cannot be modified. This ensures immutability and maintains a clean version trail.
* You cannot remove columns from a Dataset, either in the original or a duplicate.
* The Duplicate banner is displayed once after creation to provide user awareness and disappears upon navigation.

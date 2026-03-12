# Source: https://docs.pentaho.com/pdc-use/pdc-global-search-and-discovery.md

# Global search and discovery

In Pentaho Data Catalog, you can do a quick and efficient search for data assets across multiple sources from any page within the platform. You can enter a keyword in the universal search bar and retrieve relevant [search results](#id-3.-search-results).

![Global Search](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-4ba705f9c5773e263db5f0e894ba16ec85bea5b8%2FGlobal%20Search%3DGUID-2ABAE946-142B-4996-BA07-0A2ACFD97AF1%3D1%3Den%3DLow.png?alt=media)

In Data Catalog, with global search, you can:

* Search for all Data Catalog assets, such as files, tables, columns, folders, business glossary terms, applications, machine learning (ML) models, and more, including Data Products and Data Collections.
  * Data Products are visible to all users in Data Catalog. They appear in the search results even if you don’t have access to open or use them. However, you can only view or work with a Data Product after the owner grants you access. They are usually shown at the top of the search results to make them easier to find.&#x20;
  * Data Collections (also called Datasets) are only visible in search results to users who either created them or to whom the collection has been shared. If you didn’t create the collection or it wasn’t shared with you, it won’t appear in your search results. This ensures that only the right people can view or access certain collections, helping to keep data secure and relevant for each user.
* Search across metadata attributes, including names, descriptions, classifications, and tags.
* View and select from previously saved searches under the **Saved Searches** dropdown list.
* Search across all connected data sources, including databases, cloud storage, and file systems.

When you perform the global search using a keyword, the results page appears. For example, when it is searched with the ‘firstname’ keyword, the following results page appears.

![](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-61823a47b534bba353bb2eba09886b43265ed3d9%2FGlobal%20search%20result%20page%20for%20keyword%20firstname%3DGUID-FB9DF5FC-A2DC-479B-A9CB-E41336B95374%3D1%3Den%3DLow.png?alt=media)

{% hint style="warning" %}
Search does not return results when the query includes special characters. OpenSearch treats special characters as delimiters. As a result, you can find names containing special characters, but you cannot search using the special characters themselves.

**Workaround:**\
Use only alphanumeric characters (**A–Z**, **a–z**, **0–9**) in your search query. For example, search for *finance* instead of *#finance*, or *finance 2025* instead of *finance\@2025*.
{% endhint %}

When a data product appears in the search results and you don’t have access, see [pdc-requesting-access-cp](https://docs.pentaho.com/pdc-use/pdc-requesting-access-cp "mention") to request "*view*" access to it.

The search results you see are arranged based on your user role. This means that users with different roles will see different types of results at the top of the list. For example, if you are a Data Steward, your search results will show data assets like files, tables, and columns at the top. You might also see examples and entities first, because these are the items you usually work with. Similarly, if you are a Business Steward, your search results will highlight business terms and policies first. These include glossary entries and data usage rules, which are more important for your role.

This role-based ordering helps you find what you need faster, without having to scroll through results that might not be relevant to your job.

{% hint style="info" %}
By default, Data Catalog limits search results to 10,000 items. If your search returns too many results, you might not see everything you’re looking for. To find more specific data assets, you can refine your search using the data facets available on the left side of the results page.
{% endhint %}

The search results page is designed to streamline the data discovery process by providing a clear, organized, and user-friendly interface. On the search result page, you can:

* Refine results using detailed filtering options in data facets.
* Navigate large datasets with a structured grid layout.
* Re-access frequent searches using the **Save Search** functionality.

Using the search results page, you can enhance the data exploration process and quickly locate the correct assets within Data Catalog.

## Components of the search results page

The following components are available on the search results page:

![Components of the search results page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-885067530d6f7e92bae74c0a0240762df1640502%2FSearch%20result%20page%3DGUID-39FB67E1-A423-4430-A653-488B00C01CD9%3D1%3Den%3DLow.png?alt=media)

### **1. Search results count**

The search results page displays the total number of matching results found in Data Catalog for the associated search. This number helps you understand the scope of available data assets for the searched term. Based on the total number of items displayed, you can gauge how broad or specific the search is and decide whether to refine the query or apply filters.

### **2. Data facets**

On the data facets, you can refine search results based on multiple criteria. The available facet categories include:

* **Classification**: Filters results based on metadata classifications such as **Data Elements**, **Business Glossary**, and **Data Collections**.
* **Data**: Facet results by asset type, including files, tables, columns, folders, data product, term, sensitivity, domain, quality score, and so on.
* **Business Terms**: Facet results based on defined business glossary terms.
* **File Format**: Data assets by specific file formats such as DOCX, XLSX, CSV, JSON, and more.
* **Data Source**: Facet results based on connected data sources.
* **Key**: Data assets based on database keys such as **Primary Key** and **Foreign Key**.
* **Date filters**: Refine results by **Last Profiled Date**, **Last Accessed Date**, or **Last Modified Date** within a selected date or date range.
* **Trust Score**: Filter assets by trust score category:
  * **Highly Trusted** (76–100)
  * **Trusted** (51–75)
  * **Untrusted** (0–50)
* **Tags**: Include only assets that contain one or more selected tags.
* **Schema:** Refines search results based on the database schema associated with the data assets.
* **Folders**: Filters search results at the folder level to narrow down data assets stored within specific directories.
* **Bucket**: Refines search results by the object storage bucket name when working with cloud or object-based data sources such as AWS S3 or Hitachi Content Platform.
* **Table**: Refines search results at the table level to help locate specific tables within a data source or schema.

{% hint style="info" %}
The categories in data facets might vary depending on the item you are searching for. Additionally, you can expand or collapse data facets and select multiple facets to refine the results effectively. Use the **Reset** button to clear a selection in the current facet to remove all applied filters and return to the original results view.
{% endhint %}

### **3. Search results**

The Search page displays search results in a grid format, complete with pagination, where each result is represented as a data asset card, allowing you to browse and identify relevant data assets quickly. Each card contains:

{% hint style="info" %}
The card contents may differ depending on the asset's classification.
{% endhint %}

* **Asset Type Icon**: A visual indicator of whether the asset is a file, table, column, or folder.
* **Asset Name**: The name of the data asset.
* **Data Source Path**: The hierarchy path indicating where the asset is stored.
* **Domain**: Shows the business domain if the asset is assigned to one.
* **Status**: An info badge you can hover to view curation or processing status details.
* **Rating**: A star badge with the community rating (0–5).
* **Access state and primary action:**
  * If you have access, the card shows an **Open** button and a lock icon.
  * For Data Products, if you don’t have access, the card shows "Request Access" and a lock icon.\
    Selecting **Request Access** launches the standard access request flow. For more information, see [pdc-requesting-access-cp](https://docs.pentaho.com/pdc-use/pdc-requesting-access-cp "mention").

{% hint style="info" %}
Use the left-panel data facets to sort and filter in the results view to surface the most relevant assets.
{% endhint %}

### **4. Save Search option**

When you apply all the required filters and refine the search results, you can save the search results using the **Save Search** button. This feature helps you to save frequently used search queries for quick access in the future. You can access saved searches from the Search page. For more information, see [Discovery](#discovery) (Search page).

## Discovery

In Data Catalog, you can quickly search, browse, and locate data assets across multiple sources. When you enter a keyword in the Global Search field, Data Catalog automatically redirects you to the Discovery (Search) page, where you can view, filter, and refine search results using data facets. Additionally, you can save the search for future use, and it will then appear in the Saved Searches section of the Discovery landing page.

To access Discovery, in the left navigation menu, click **Discovery**. The Search page (the Discovery landing page) then appears, where you can view recently searched terms and recently viewed assets, and access saved searches for frequently used queries. The following is a detailed breakdown of each section and its functionality:

![Discovery Landing Page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-71ceeff2244cf162c6837a65ae8f8a60963100fd%2FDiscovery%20landing%20page%3DGUID-90788D25-E09A-414D-9144-13D56C2C13B5%3D1%3Den%3DLow.png?alt=media)

### **1. Search summary**

The search summary section displays a quick overview of the available data assets within Data Catalog. This section displays three key metrics: total number of sources, total data assets, and number of glossary terms present in Data Catalog. These statistics help you to gauge the scale of data availability and metadata coverage across different sources. Additionally, this section serves as a quick reference point, allowing you to assess the extent of metadata discovery within Data Catalog.

### **2. Recently Searched**

The Recently Searched section displays a list of previous search terms that users have entered in the global search interface. Each search term appears as a clickable button, allowing you to rerun the same query without having to retype it. This section is particularly useful for users who frequently search for similar datasets, as it saves time and enhances efficiency by providing a quick way to revisit past searches. It also helps users maintain a consistent search workflow, ensuring that they can easily access commonly queried metadata assets.

When you reopen a recent search, any facets you applied earlier, such as classification, data type, or data source, will still be in place, and the results will appear just as they did when you last viewed them. This means you can pick up exactly where you left off, without having to set up your search again.

### **3. Recently Viewed**

The Recently Viewed section displays a list of data assets they have accessed in their recent sessions. This section displays relevant information about the asset, such as its name and associated data source. By clicking on any recently viewed asset, users are taken directly to the metadata details page, allowing them to quickly continue their work without performing a new search. This section is valuable for data stewards, business users, and administrators who need to track their navigation history and frequently revisit specific datasets. It enhances user productivity by reducing the need to manually search for previously accessed data assets, making it easier to analyze, profile, and apply business terms to metadata.

### **4. Saved Searches**

In the Saved Searches section, you can store and manage frequently used search queries and ensure that important search queries are always accessible with a single click. This section displays a table containing the search name, search term, and creation timestamp. You can click a saved search to rerun it, eliminating the need to re-enter queries each time manually. Additionally, you can also remove saved searches to manage the list efficiently. This feature is particularly beneficial if you perform repetitive searches, as it helps you maintain a structured and organized search history.

Similar to recent searches, when you open a saved search, the facets you had applied when the search was saved will also be restored automatically, along with the same page of results you were last on. With this you can quickly return to a familiar search setup and continue your work without reconfiguring filters or scrolling through results again.

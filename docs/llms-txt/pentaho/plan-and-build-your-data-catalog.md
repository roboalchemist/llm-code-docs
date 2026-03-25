# Source: https://docs.pentaho.com/pdc-get-started/pdc-get-started-get-started-cp/plan-and-build-your-data-catalog.md

# Plan and build your Data Catalog

As a data steward, you can start planning and building Data Catalog for your data analysts to use.

## Planning your Data Catalog

It is helpful to plan your data catalog before building it. Use the following guidelines to plan your Data Catalog:

### **Plan data sources to add**

When setting up data analytics with Data Catalog, start by adding the data sources that you want to analyze.

**Note:** The number of data sources you can add and the amount of data you can scan is limited by your license. Databases do not have a data scan quota.

Before adding your data sources, gather the configuration information you need to set up the data sources. Your database administrator is best positioned to help provide the configuration information needed, such as the following information:

* Data source type
* Configuration method, for example: credentials, SSL, or a URI (Uniform Resource Identifier)
  * For credentials, username and password, host name, and port number
  * For SSL, encryption information, for example:
    * Encryption type, such as: Encryption only, Encryption with Server and Client Authentication
    * Trust store type and location
    * Trust store password and cipher suite
    * Key store type, location, and password
  * For URI, known as a connection string, you need a username and password
* Any driver needed
* For Amazon Web Services (AWS) data source types, a configuration method isn't specified. You must have information such as AWS region, account number, IAM username, access key ID, and secret access key to configure these data source types. **Tip:** Data Catalog uses the data source name you enter when setting up the data source throughout the data catalog. As a best practice, adopt a naming convention that is logical for users to understand that you can use for all data sources and types that you add to Data Catalog.

### **Plan business glossaries and business terms**

The business glossary is an organized list of business terms and their definitions intended to serve as the single and definitive reference for an organization. You can associate business terms with data elements, business rules, related terms, and custom attributes to form a comprehensive view of the organization’s business concepts and data landscape.

You can organize business glossary terms in a domain and category hierarchy, or under just a domain, or as a stand-alone term. If you do not specify a domain or category, the term appears as Unassigned.

### **Plan users and permissions**

It is a best practice to plan the access your users need before adding them to the system, to make sure that access to data sources and business data is restricted to only the users who need it. You can add administrators for departments or lines of business and then they can add users with the permissions needed for their specific work responsibilities. You can use communities, which are custom roles, to fine tune access to specific data source types and other Data Catalog assets.

**Note:** The number of Expert user roles you can assign to users is limited by your license. The Expert user roles are:

* Business Steward
* Data Steward
* Admin
* Data Developer

You are now ready to start building your Data Catalog.

## Building your Data Catalog

To get started using Data Catalog, you must add data to the catalog and analyze the data. Use the following steps to get started:

### Step 1: Add data sources

Adding data sources is the first step when building your Data Catalog. Data sources are the building blocks in configuring your catalog. You can connect the different data sources in your data lake, both on premises and hosted in the cloud. As part of this step, you test the data source connections and ingest schemas. You should have already planned your data sources, as described in [Planning your Data Catalog](#planning-your-data-catalog).

**Note:** The number of data sources you can add is limited by your license.

For the steps to add data sources, see the **Administer Pentaho Data Catalog** document.

* **Test connections**

  Before you can save newly-configured data sources, you need to test the connections. This process tests the data source configuration and connectivity, returning helpful information if there is an issue.
* **Ingest schemas**

  Before you can save the newly-configured data sources, you must also load basic database schemas and associated metadata information into Data Catalog.

### Step 2: Profile data

After you ingest the schema for a data source, the data is limited to just the database metadata. Data profiling provides additional information. Data profiling is the process of examining the data of the selected data objects and collecting statistics and informative summaries about that data. The results of this process are available almost immediately, as each individual column, table, or schema is processed.

**Note:** The amount of data you can scan is limited by your license. Databases do not have a data scan quota.

Data profiling is a prerequisite for most data analytic processes within Data Catalog. If the data profile is not valid, you must re-profile the data prior to proceeding with any data identification activities.

**Tip:** As a best practice, keep your selection scope “reasonable.” For example, do not try to process 100,000 tables at once, since this process can take some time depending on the nature of the data. Use the default settings on the Configure Data Profiling page, as they are suitable for most situations.

### Step 3: Identify data

The data identification process uses dictionaries and data pattern analysis to automatically classify data, applying tags defined in dictionary and pattern configuration files. In addition to the dictionaries and patterns included with Data Catalog, you can create your own dictionaries and pattern analysis configuration files that might better suit your organization's needs.

### Step 4: Add glossaries and business terms

You might want to create functional business glossaries and terms that are commonly used in your organization. You can create a business term in a domain and category hierarchy, just under a domain, or as a standalone term. If you do not specify a domain and category, the term appears as unassigned.

For the steps to set up glossaries and terms, see the **Administer Pentaho Data Catalog** document.

### Step 5: Add users

A best practice for adding users is to add the division or department administrators first and then delegate the applicable permissions to them. They can then add their own business and data users, as well as business stewards and data stewards.

**Note:** The number of Expert user roles you can assign to users is limited by your license. The Expert user roles are:

* Business Steward
* Data Steward
* Admin
* Data Developer

For more information on the user roles and permissions that come with Data Catalog, see the **Administer Pentaho Data Catalog** document.

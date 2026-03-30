# Source: https://docs.pentaho.com/pentaho-data-mastering/getting-started-with-pentaho-data-mastering.md

# Getting started with Pentaho Data Mastering

The Pentaho Data Mastering application can be used to maintain your organization's most important data by creating and using Golden Records as the single, trusted, and authoritative source of data. Data can be consolidated from on-premises or cloud sources and the Golden Records can be managed for multiple domains, across multiple business processes and applications within your organization.

The following architecture diagram depicts how data can be transformed into Golden Records by using the Pentaho Data Mastering application.

<figure><img src="https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2FFqg5I8npJSE5YdxLDxk0%2FMDM%20v9.drawio.png?alt=media&#x26;token=088ecc3b-eac7-4ff2-90c7-5613581d56d2" alt=""><figcaption></figcaption></figure>

First, the Pentaho Data Mastering application sources raw data from the data locations that you specify, such as customer relationship management databases (CRM), enterprise resource planning systems (ERP), and source code management repositories (SCM). The raw source data is cleaned, standardized, and stored as unmastered data in a data lake or data warehouse. Next, the unmastered data is processed by the application’s Mastering Engine and turned into Master Records according to the Match Rules and Merge Rules that you configure in the application. Master Records that do not have conflicts, according to the configured rules, are automatically transformed into Golden Records. Master Records that have match or merge conflicts are reviewed, updated, and finally transformed into Golden Records by users that you configure with Data Steward and reviewer roles.

To use the Pentaho Data Mastering application, you must install the server and client, set up users and roles, source the data that you want to maintain, and configure the rules for matching and merging data to create Master Records. When you finish installing and configuring the application, you can use it to review audit history and user activity, manually update records, and manage users, roles, and data sources.

* [Installing Pentaho Data Mastering](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering)

  To set up the Pentaho Data Mastering application, you must install the Pentaho Data Mastering server, components for the OpenObserve platform, and the Keycloak Identity and Access Management (IAM) server.
* [Setting up users and roles](https://docs.pentaho.com/pentaho-data-mastering/setting-up-users-and-roles)

  Set up users and roles in the Keycloak Identity and Access Management (IAM) server to control which actions users are allowed to perform in the Pentaho Data Mastering application.
* [Setting up business domains](https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains)

  Set up business domains to work with specified categories of data so that you can control how that data is processed and managed across all the records in your organization. Business domains might include customer data, product data, supplier data, or financial data.
* [Sourcing data](https://docs.pentaho.com/pentaho-data-mastering/sourcing-data)

  Source raw data from databases, systems, and repositories so that the data can be cleaned, standardized, and stored as unmastered data.
* [Configuring match rules](https://docs.pentaho.com/pentaho-data-mastering/configuring-match-rules)

  Configure match rules to identify matches in data from different sources so that you can control how that data is merged to create Master Records.
* [Configuring merge rules](https://docs.pentaho.com/pentaho-data-mastering/configuring-merge-rules)

  Configure merge rules to control how matched data from different sources is merged to create Master Records. Merge rules are applied to data during the data curation process.
* [Transforming Suggested Row Records into Master Records](https://docs.pentaho.com/pentaho-data-mastering/transforming-suggested-row-records-into-master-records)

  Transform Suggested Row Records into Master Records so that those Master Records can be transformed into Golden Records. Records in the Suggested Row Records table were not automatically transformed into Master Records due to match or merge conflicts or missing key column values. A record in the Suggested Rows table cannot be edited until that record is transformed into a Master Record.
* [Transforming Master Records into Golden Records](https://docs.pentaho.com/pentaho-data-mastering/transforming-master-records-into-golden-records)

  When Master Records are not automatically transformed into Golden Records due to match or merge conflicts, you must resolve the conflicts by updating the Master Records so that the records can be transformed into Golden Records.
* [Transforming Golden Records into Master Records](https://docs.pentaho.com/pentaho-data-mastering/transforming-golden-records-into-master-records)

  Transform Golden Records into Master Records when the Golden Records are outdated, require further modification, or must be removed from the Pentaho Data Mastering application. Golden Records cannot be edited. Only Master Records can be edited.
* [Viewing history](https://docs.pentaho.com/pentaho-data-mastering/viewing-history)

  View history in the Pentaho Data Mastering application to audit changes to master data, such as when a record was created, modified, or deleted, and by whom.
* [Managing users and roles](https://docs.pentaho.com/pentaho-data-mastering/managing-users-and-roles)

  Manage users and roles to update who is allowed to access the Pentaho Data Mastering application and which actions users are allowed to perform in the application, based on their assigned role. To add, remove, or update users, you must make changes in the Keycloak IAM server. You can view, assign, and remove user roles in the Pentaho Data Mastering application.
* [Modifying rules, roles, and data sources in bulk](https://docs.pentaho.com/pentaho-data-mastering/modifying-rules-roles-and-data-sources-in-bulk)

  Modify Match Rules, Merge Rules, User Roles, and Data sources in bulk by exporting the data as a JSON file and editing the information in the JSON file.

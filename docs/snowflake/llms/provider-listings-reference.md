# Source: https://docs.snowflake.com/en/collaboration/provider-listings-reference.md

# Configure listings

When you [create a listing](provider-listings-creating-publishing.md), you must complete additional fields for your
listing before making it available for consumers.

Depending on how you make your listing available, and how consumers access your data product, some sections or fields might be optional.

After you configure your listing, publish it to consumers. See [Publish a listing](provider-listings-creating-publishing.md).

## Basic information

Complete basic information about your listing. The following table describes the fields in the Basic Information section:

| Field Name | Description | Example |
| --- | --- | --- |
| Title | The title of the listing. When consumers view your listing, the title appears below your company name.  The title must have the following characteristics to be approved:   *Should be between 40–60 characters, up to 110 characters* All major words are capitalized (use title case) *Must be unique* Must be different from any other listings offered by your provider profile | Historical Weather by Postcode. |
| Subtitle | Provides a short, informative explanation of your data product that is visible to consumers.  The subtitle cannot exceed 100 characters. Use sentence case for the subtitle and do not repeat the title.  This option is not available for private listings. | Historical weather data by location. |
| Category | Categories help consumers find your data or app on the Snowflake Marketplace. Select the desired category from the drop-down list of available values. You can select up to three categories.  This option is not available for private listings. | Environment |
| Terms of Service | Specifies a link to the listing terms - the service agreement for the listing. Consumers must accept the listing terms before they can access the listing. Listing terms are required for all listings.  Select one of the following:   *Standard Agreement for Marketplace Products: Snowflake provides standard listing terms for   Snowflake Marketplace products, called the Standard Agreement for Marketplace Products. This agreement is available   at: <https://www.snowflake.com/marketplace/standard-agreement/>. You can choose to use the Standard Agreement as the   listing terms. You can learn more about the Standard Agreement by reviewing the FAQs   available at: <https://www.snowflake.com/standard-agreement-for-marketplace-products/>.  By selecting the Standard Agreement for Marketplace Products, you’re confirming that you’ve reviewed it and the   [Disclaimer](https://www.snowflake.com/standard-agreement-for-marketplace-products/) with your legal counsel.* Custom: Specify a URL to the listing terms. The URL must be publicly accessible and   not require authentication to access. The listing terms can be a PDF or other document type that is accessible from a URL. * Listing terms will be provided offline: Only available for private listings offered directly to specific consumers.   This option lets you provide listing terms to your consumers that isn’t available at a URL. | Custom, `https://www.example.com/en/legal` |

## Details

Complete additional details for your listing.

> **Note:**
>
> This section is optional for private listings.

The following table describes the available fields in the Details section:

| Field Name | Description | Example |
| --- | --- | --- |
| Description | Description of the data product shared in the listing. The description helps consumers understand what is in your data product.  Enter a description between 250 and 6000 characters, with line breaks between paragraphs.  Use dashes instead of bullet points. The description must include an introductory paragraph with information about the data product, such as the scope of the dataset.  For listings that include services or secure functions, the description must include the expected workflow for consumers to access your services or secure functions.  The description can also include the data sources for your listing, or additional information not covered in other fields. | ACME is the number one supplier of customized, pinpoint weather warnings to large enterprises, as well as a vital information source for worldwide weather forecasts, data and meteorological consulting services. This listing provides historical weather data for US zip codes that can be used to further enhance your existing data to provide deeper analytics.  Expected Workflow:   *Consumer shares list of zip codes with provider using a private listing.* Provider enriches the zip codes. * Provider shares enriched data back with the consumer using a private listing. |
| Link to Documentation | A link to a page on your website with more detailed documentation for the listing. Documentation must be clear, and reference the correct schema objects present in the data share or Snowflake Native App associated with the listing. The link must be accessible on the internet, and not require authentication to access. | `https://www.example.com/documentation/` |
| Link to Video | A link to an unlisted or public YouTube video for the listing. Private videos are not supported. Video thumbnails are displayed on the listing details page and videos do not play automatically.  **Tip:** When making a video to display on a listing details page, keep the following in mind:   *Video final frames are displayed after videos play and should include a call to action.* Videos should be short, and show actual product usage, with the first 5 seconds being the most important. | <https://www.youtube.com/watch?v=MEFlT3dc3uc> |

## Data product

Configure the data product for your listing. This can be a secure share, a Snowflake Native App, or a Connected App.

You can select objects and have Snowflake create a secure share, or add a share that you already created.
See [Prepare the shares for your listing](provider-listings-preparing.md) for guidance creating shares for paid listings.

When adding a data product to your listing, consider the following:

* Secure shares can only be attached to one listing.
* After the listing is published, you cannot attach a different share.
* You can only see shares that your current role owns.
* The data product must be legally shareable (i.e. you must own the data or have the right to share it).
* Until a listing is published, it can only be associated with a share in the local/primary account. After the
  listing is published, it can be associated with a share in additional regions that you have selected.

The following table describes the available fields in the Data Product section:

| Field Name | Description |
| --- | --- |
| Database Objects or Secure Share | Data that you want to share as part of the listing. |

## Data product - data dictionary

After adding a data product to your listing, you can add a data dictionary. A data dictionary provides consumers insight into the contents
and structure of a free or paid listing offered on the Snowflake Marketplace before installing the data product into their account.

> **Note:**
>
> This section is optional for private listings.

### About data dictionaries

You can use a data dictionary to make the contents of your listing visible to consumers. A data dictionary is generated for tables and
views within a listing. Listings can also include a preview of data, referred to as a Data Dictionary Data Preview.

Your data is visible in two ways:

* Featured objects: Allow the consumer to quickly view the contents of the object. You can select up to five of the most important
  database objects within the listing.
* All objects: Allows the consumer to view all of the objects within a listing. It is auto-generated when you publish a listing.

Data dictionary Data Preview allow both providers and consumers to preview data for tables and views associated with listings.

Previews provide a representative sample of the data, allowing:

* Providers to see exactly what data will be available in a preview.
* Consumers to determine if a listing contains the data they are looking for.

> **Note:**
>
> Data in a listing is automatically made available for preview.
> Providers needn’t do anything special to enable preview.

### Set up a data dictionary for your listing

Before you can add a data dictionary, you must add a data product to the listing. All listings offered on the Snowflake Marketplace must include
a data dictionary.

To set up a data dictionary, do the following:

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Marketplace » Provider Studio » Listings.
3. Find and select the listing where you want to add a data dictionary.
4. Select Save and Create Data Dictionary.

   > **Note:**
   >
   > By saving this share, you agree that Snowflake is permitted to create a data dictionary and associated preview for the share and
   > display it to consumers when the listing is published.
   >
   > Please note, Data Dictionary data previews are automatically updated when underlying data changes.
   >
   > If you data product contains PII or other personal data, please mask those columns as such.
   > For more information, including instructions on how to mask PII and other personal data see Mask PII and other data in data previews.

   After saving the listing the data dictionary displays, listing all of the tables, views, and functions within the
   listing.
5. Search for or select an object that you want to include as a featured object, then select Add to featured.

   Optionally, repeat this step to add additional featured objects. You can have up to five featured objects in a listing.
6. Select Save.

You can edit column descriptions for tables in the Provider Studio, or you can use SQL.
Use the COMMENT parameter in the [CREATE <object>](../sql-reference/sql/create.md) and [ALTER <object>](../sql-reference/sql/alter.md) commands or the [COMMENT](../sql-reference/sql/comment.md)
command to add a comment describing an object or [individual table columns](../sql-reference/sql/alter-table-column.md).

### Mask PII and other data in data previews

Snowflake periodically runs [Data Classification](../user-guide/classify-intro.md) on Data Previews to identify and mask any column with a high likelihood of containing PII
(Personally identifiable information) or other personal data. Personal data includes information relating to an identified or identifiable
person, such as:

* Name, age, email, or mailing address
* Educational or employment information
* Location data or device activity
* Customer records, or account information

Once Snowflake identifies and masks a PII column, an email is sent to the technical contact listed in the provider profile to review the
details. At any time, you can manually select or deselect PII columns in the Data Preview.

To view or modify PII classification results, do the following:

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Marketplace » Provider Studio.
3. Select Listings from the top navigation. To create a listing, see [Create and publish a listing](provider-listings-creating-publishing.md).
4. Select the listing to review.
5. Under Data Dictionary, select Edit.
6. Select the table or view to review.
7. Review the classification results.
   Columns containing PII or any other personal data are classified as “Contains PII”.
8. Select the Data Preview tab to preview the object’s content, which may include masked data.
9. If a column is not identified correctly:

   * If a column is mistakenly identified as containing PII, deselect the checkbox to the left of the Name column to ensure that the
     data in that column is unmasked in the Data Preview.
   * If a column contains PII but has not been identified as such, select the checkbox to the left of the Name column to ensure that
     the data in that column is masked in the Data Preview.
10. Select Save.
11. If you agree with the Data Classification, select Save.

> **Note:**
>
> Data Preview content is generated when a data dictionary is enabled for a listing. Preview data for individual tables and views may not
> be immediately available while data is generated.

> **Note:**
>
> It can take up to 3 to 4 hours for columns selected as PII in Provider Studio to display as masked on the consumer-facing listing.

### Data Preview refresh

If you add or remove objects in your listing, or change the schema of an object, the associated data preview will be refreshed, if enabled.
Updating the object data will not result in a data preview refresh.

> **Note:**
>
> Data Previews are refreshed automatically approximately every few hours. You may not see the refreshed preview immediately after adding
> or removing objects, or updating schemas. If the data within the existing objects (for example, rows in a table) is updated, but there
> are no schema changes or new objects added, the data preview will not be refreshed immediately. In this case, the data preview will only
> be updated during the next biweekly refresh.

## Data product - attributes

After specifying a data product, you can define additional attributes for a listing.

> **Note:**
>
> This section is optional for private listings.

The following table describes the available fields in the Attributes section for a data product:

| Field Name | Description |
| --- | --- |
| Update Frequency | How often your data product is updated in Snowflake. If your data product is updated at different frequencies, choose the highest frequency of updates for your data product. |
| Geographic Coverage | Select one or more geographic regions for which your data product has coverage. If applicable, choose specific countries or U.S. states. |
| Geographic Granularity | If you specify global or multiple states or countries as the geographic coverage of your dataset, select a granularity for the data product.  You can only choose one option, so select the most granular option available in your data product. |
| Time Range | Specify the time period that your data product covers. You can specify custom dates as a fixed time range (2020-01-01 - 2021-01-01) or a dynamic time range (Next/Last X days, weeks, months, or years). |
| Timestamp Granularity | If you specify a time range, select a timestamp granularity for the data product.  You can only choose one option, so select the most granular timestamp type in your data product. |
| Additional attributes (optional) | Any additional information that you want to communicate to your consumers. You can include up to 4 additional attributes of the data. Use 2-5 words for each attribute to maximize readability. Each attribute must be fewer than 80 characters. |

## Access and pricing - listing access

For listings offered on the Snowflake Marketplace, you can view the Listing Access for a listing, and modify it if the listing is still
in draft.

Listing access controls how consumers can access your data product. See [Listing access options](collaboration-listings-about.md) for more details.

## Access and pricing - trial

Add a trial for a limited trial listing offered on the Snowflake Marketplace. To add a trial for a paid listing,
see Access and pricing - pricing & trial.

> **Note:**
>
> This option is required for limited trial listings.

The following table describes the available fields in the Trial section:

| Field | Description |
| --- | --- |
| Trial Type | Choose the type of trial to offer:   *Limited time. Consumers can trial your data product for a limited period of time. Choose this option if you offer your entire   data product to consumers for a short period of time.* Unlimited time. Consumers can trial your data product indefinitely. Choose this option if you offer a sample of your full data   product. For example, weather data for just one city, while your full data product includes weather data for an entire country.   If your listing has an application package as the data product, you can also choose from two other trial types:   *Limited functionality. Consumers have access to limited functionality of your application package.* Limited functionality and time. Consumers have access to limited functionality of your application package for a limited time.   **Caution:** You must limit functionality to your app by using the [SYSTEM$IS_LISTING_TRIAL](../sql-reference/functions/system_is_listing_trial.md) system function.  If you select a limited functionality trial and your application package is not set up to limit functionality in the shared data content or application logic, your app will provide full functionality to trial customers.  See [Limit functionality of your Snowflake Native App for trial consumers](provider-listings-preparing.md) for details on fully configuring limited functionality trials. |

## Access and pricing - pricing & trial

Add the pricing plan and trial for a paid listing in this section.

This section is required for paid listings offered on the Snowflake Marketplace, but trials are optional for paid private listings.

> **Note:**
>
> Only account administrators (users with the ACCOUNTADMIN role) or the listing owner (a role with OWNERSHIP privilege on the listing) can complete this section.

The following table describes the available fields in the Trial & Pricing section:

| Field | Description |
| --- | --- |
| Pricing Plan | Choose the pricing plan for the listing. See [Paid listings pricing models](provider-listings-pricing-model.md). Prices are in US dollars only. |
| Free Trial | Choose the trial type for the listing:   *Limited time: This option lets consumers participate in a free trial for a time period that you specify (1, 7, 30, 60, or 90 days).   The maximum trial period is 90 days. When the trial ends, the consumer account loses access to the data product.   Other accounts in the same organization can perform a new trial of your listing.* Limited functionality: This option lets consumers participate in a free trial with limited functionality of the paid data product.   This trial mode doesn’t expire until the consumer upgrades to the paid listing. * Limited functionality and time: This option lets consumers participate in a free trial for a period that you specify   (1, 7, 30, 60, or 90 days). The trial version offers limited functionality of your data product, and when the trial period ends,   the account performing the trial loses access to the data product. |

## Business needs

Add the business needs that your data product can help consumers with.

> **Note:**
>
> This section is optional for private listings.

The following table describes the available fields in the Business Needs section:

| Field Name | Description | Example |
| --- | --- | --- |
| Business Need | Help consumers find your listing on the Snowflake Marketplace by specifying relevant business needs addressed by your data product. You can select up to six relevant business needs.  If you do not see a relevant business need in the drop-down list, you can create a custom need using 2-4 words. However, consumers cannot filter by custom business needs on the Snowflake Marketplace.  You can edit the list of business needs at any time without resubmitting the listing for approval. | Location Data Enrichment |
| Description | Description of how your listing addresses the selected business needs, using an example specific to a customer use case or business need.  Add a unique description for each business need. | Location Data Enrichment: Identify all of the zip codes associated with a given county, census tract, or core-based statistical area. |

## Sample SQL queries

You can specify valid sample SQL queries that consumers can use to get value out of your data product, or at least verify that your data
product was successfully installed in their Snowflake account.

> **Note:**
>
> At least one valid SQL query is required in order for you to publish a listing on the Snowflake Marketplace.
> It’s recommended to include 3–4 sample queries.
>
> SQL queries are optional when publishing private listings.

The sample SQL has the following requirements:

* The query must return at least one row.
* The query must reference objects that are explicitly in the share.
* Objects must be qualified using `SCHEMA.OBJECT`. Do not include the database name. For example,
  `EXAMPLE_SCHEMA.TABLE_A`.

Select Add to add one SQL query. The following table describes the available fields in the Sample SQL Queries section:

| Field Name | Description | Example |
| --- | --- | --- |
| Title | Descriptive title for the query to help consumers understand how they can use the data product. | Determine if an outdoor event could be affected by rain. |
| Description (Optional) | Description of the example that ties the title to a specific use case for the data product. The description is automatically loaded as a comment when consumers run the sample query after installing your data product. You can also include additional instructions, such as the name of the schema, sample tables, or fields.  Use <*schema*>.<*table*> format when referencing tables and views in your SQL.  Do not include the database name in the query, because consumers create custom database names when they get your listing. | If you are hosting an outdoor event in the next 7 days, use our forecast data to determine if the event might be affected by rain. |
| SQL Query | Code for your sample SQL queries. The queries should directly answer the title and description.  Snowflake automatically validates your sample queries. To be valid, a sample query must return at least one row.  If a query fails to validate, you can save the listing but the listing cannot be published until all sample queries are successfully validated. You must select a warehouse to use to validate the SQL query. |  |

## Region availability (Marketplace listings only)

The following table describes the available fields in the Region Availability section.

| Field Name | Description |
| --- | --- |
| Region Availability | By default, your listing is available in All regions. Choosing all regions ensures the availability of your listing in any future regions added by Snowflake. For paid listings, selecting this option makes the listing available in [supported regions](consumer-listings-paying.md) and any future supported regions added by Snowflake.  If your listing has specific regional limitations, select All regions to change the region availability to Custom regions and select the regions in which you want to offer your data product. When you choose custom regions, your listing is still visible in all Snowflake Marketplace regions, but consumers can only get your data product in the regions you specify. |
| Fulfillment method | Automatic fulfillment is selected by default. With Cross-Cloud Auto-fulfillment, your data product is automatically fulfilled to a region and you incur costs only when there is consumer demand in that region.  When you use auto-fulfillment, you must also select a refresh frequency at which to update the data product shared with consumers. You must select a refresh frequency of a maximum of 8 days. If your data product is a Snowflake Native App, you can only set a refresh frequency on the account level.  For more details on auto-fulfillment, see [Auto-fulfillment for listings](provider-listings-auto-fulfillment.md).  If you can’t use auto-fulfillment, select Manual to manually replicate your data product. To fulfill requests, you must set up accounts in regions with consumer demand, manually replicate the product to each account, create secure shares in each account, and attach those shares to this listing. See [Manually replicate data to fulfill a listing request](provider-listings-managing.md) |

## Connection string identifiers (Connected Apps only)

For Connected Apps, add one or more valid connection string identifiers (CSIDs). Submit the same CSIDs that you submitted when you registered on the Snowflake Partner Network portal.

## Consumer accounts (private listings only)

To publish a listing to specific consumers, you must specify the account identifiers for the accounts that you want to share with:

| Field Name | Description | Example |
| --- | --- | --- |
| Consumer Accounts | Specifies the Snowflake accounts that you want to share your private listing with. You can use Snowflake account identifiers or URLs. See [Finding the organization and account name for an account](../user-guide/admin-account-identifier.md) for details. | `ORGABC.ACCOUNT123` `https://<organization_name>-<account_name>.snowflakecomputing.com` |

If you’re sharing with a consumer account that is in a different region than your account, you must also set up auto-fulfillment:

| Field Name | Description |
| --- | --- |
| Auto-fulfillment | Select the replication interval and frequency for your data product. For example, you can configure replication to occur every two hours. If your data product is an application package, you can only set the refresh frequency and interval on the account level. |

See [Auto-fulfillment for listings](provider-listings-auto-fulfillment.md) for more information.

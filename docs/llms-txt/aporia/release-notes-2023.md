# Source: https://docs.aporia.com/release-notes/release-notes-2023.md

# Release Notes 2023

Welcome 2023! :tada: We are extremely excited for the year ahead as we continuously enhance our platform to ensure that you and your team can observe your models in production, detect issues and improve their performance as efficiently as possible.

In this page, you'll be able to find a constantly-growing list of some of our most impactful new features and enhancements that we release every month.

## October 2023

* Deactivate versions - There is a time when a version gets old and we want to be able to observe it but stop syncing new data. For this scenarios, we are happy to introduce the ability to deactivate an existing version. Don't worry, you can always turn it active again.
* Multiple integrations of the same type - Different teams use differnt slack channels for notifications or want to create different webhook automation once an alert is fired. For this reason, we now support creation of multiple integrations of the same type for all of our available integrations.
* "My Workspaces" view - You can now enjoy our new pinned view where you can observe all models, monitors, alerts and investigation cases, across all their respective workspaces in a single view.

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FAG3atzLzqN6LAbhfstEf%2Fimage.png?alt=media&#x26;token=dc5c9f9b-8e7a-4fe0-b6bd-f209ba98eae7" alt=""><figcaption></figcaption></figure>
* Global filters for dashboards - Sometimes we want to be able to view the same insights for different segments of our data without needing to rebuild our dashboard. For those cases, you can now mark specific segment groups for global filtering. Once marked as such, you will be able to use those segments as global filters in dashboards.

## September 2023

* Code based metrics - This new advanced feature allows users to allow define Pyspark-based metrics that allow for computation on raw data, element-wise operations, and support third-party libraries. For usage example explore our [Code-based metrics guide](https://docs.aporia.com/api-reference/code-based-metrics).
* New version actions - Deletion of versions / datasets is now supported via both UI & REST API.

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FjRUrOmENUdBIn5Z6A9nF%2Fimage.png?alt=media&#x26;token=da9dfccc-18f1-4560-972c-f2cf9caa6a68" alt=""><figcaption></figcaption></figure>
* Resolve multiple alerts - You can now resolve multiple alerts in one click. Just filter the alerts you wish to dispose and click “Resolve All”!
* Extended REST API support - Create and delete data sources is now supported via REST API. For more details read our [REST API docs](https://platform.aporia.com/api/v1/docs#tag/Data-Sources/operation/create_data_source_api_v1__account_name___workspace_name__data_sources_post).

## August 2023

* New DDC - For those of you who store your data in [Microsoft SQL Server](https://docs.aporia.com/data-sources/mssql), you can now directly and easily integrate it using our new data connectors.<br>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FsDHArA1gu73IZd8EzoIE%2Fimage.png?alt=media&#x26;token=a4942db8-5584-47ea-82b2-2d2c5a5bab2b" alt=""><figcaption></figcaption></figure>
* Recalculate metrics API - sync your data on demand without waiting for the upcoming scheduled calculation job. We've added [recalculating metrics on demand](https://platform.aporia.com/api/v1/docs#tag/Metrics-\(Experimental\)/operation/recalculate_metrics_api_v1__account_name___workspace_name__metrics_recalculate_post) via API.
* Extended REST API support - Edit segments is now supported via REST API. Whether it's part of your CI/CD pipeline, triggered by a new value monitor alert, or just to ease building your Dashboards. For more details read our [REST API docs](https://platform.aporia.com/api/v1/docs#tag/Data-Segments-\(Experimental\)/operation/edit_data_segment_api_v1__account_name___workspace_name__data_segments__identifier__put).
* Bug fixes & performance improvements!

## July 2023

* New dashboard widgets - Visualizations are a powerful tool for analyzing your model performance, business impact, data behavior, etc. For this reason we are happy to introduce three new widgets<br>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F7krv8YJjWcDVaEYSYTgV%2Fimage.png?alt=media&#x26;token=f2afae0b-5e1a-4f1a-a78d-20036ef3e515" alt=""><figcaption><p>Metric correlation &#x26; Metric by segment</p></figcaption></figure>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fnj2KqU6V8Xf6jXbprHDn%2Fimage.png?alt=media&#x26;token=3ec56f98-8d60-4ad9-ae7a-aef721d2b526" alt=""><figcaption><p>Histogram over time</p></figcaption></figure>
* API keys - Account admins can now simply manage their API keys by going to `Account Management > API Keys`.
* Drift monitors - Different users might like to monitor drift using different metric to fit they use-case best. For this reason, we added support for choosing the monitored drift metric. Available metrics can be found [here](https://docs.aporia.com/api-reference/metrics-glossary#statistical-distances).
* Metrics on actuals - All our statistical metrics can now be used on actual fields as well. You can easily monitor & visualize them all across the platform. More information about our available metrics can be found [here](https://docs.aporia.com/api-reference/custom-metric-syntax#supported-functions).
* SQL for blob storage - You can now transform data originated in S3/ AzureBlobStorage/ GoogleCloudStorage using a SQL query.

## June 2023

* Cross model dashboards - Sometimes we need to  get insights on multiple models in one place. It could be observe model orchestration or just to get an overall status in one glance. For this reason, we added support for creating [cross model dashboards](https://docs.aporia.com/dashboards/overview#cross-model-dashboards).
* Alert consolidation - Monitors can create unnecessary noise when thresholds are not yet fine-tuned or your team is handling an ongoing issue. Learn how to keep notifications meaningful by [consolidating your alerts within Aporia](https://docs.aporia.com/monitors-and-alerts/alerts-consolidation).
* Extended error information - You will be able to see a full traceback for errors detected while trying to retrieve your datasets/metrics.
* Default investigation case - Depending on your monitor type, a default investigation case will automatically be created to provide you the most relevant tools and tips to quickly get to the root cause of the issue detected. Default investigation cases are now available for prediction drift, data drift and performance degradation monitors.<br>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FRpeprL5Ne3ffoIAASReu%2Fdefault%20IR%20case%202.gif?alt=media&#x26;token=9c3e102d-f5a0-41c9-b4a0-581688820efc" alt=""><figcaption></figcaption></figure>

## May 2023

* Workspaces - For enterprises and organizations which require silos for separate teams/models/data integrations... Aporia introduces workspaces (team silos) managed by Aporia account admins. For more information read our [RBAC docs](https://docs.aporia.com/administration/rbac).
* Role Based Access Control - Full [role based access control](https://docs.aporia.com/administration/rbac) is now available in Aporia! Using account-level and workspace-level permissions, users will only have access to the data and actions for which they are permitted.
* New integrations - We've expanded our integration support and now you can receive alert notifications via your organization Teams & Webhook.
* New data source action - Deleting a data source is available by clicking on the actions button in the data connectors page

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FbuAbbkn9hYtP40nUBQ72%2Fimage.png?alt=media&#x26;token=f2aef024-2c57-4954-b450-c31370115ccc" alt=""><figcaption><p>Delete existing data connector</p></figcaption></figure>
* Filters in custom metrics - In order to build your custom metric you may need to apply different data filtering in different parts of the calculation. For those cases, Aporia supports custom filtering in custom metrics. For more information and examples read our docs.
* Custom segments - Grouping segments with common logic is now available when creating / editing custom segments. Learn how to use it with our updated [Custom Segment Syntax examples](https://docs.aporia.com/api-reference/custom-segment-syntax).
* New DDCs - For those of you who store your data in [BigQuery](https://docs.aporia.com/data-sources/big-query) / Azure Blob Storage, you can now directly and easily integrate it using our new data connectors.
* Value range monitor - You can now create value range monitor to get alerted when your inference data exceeds the desired range.

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FQyymXFdpXsd98zXkigvu%2Fimage.png?alt=media&#x26;token=e1f71bb1-fade-4320-a05f-2fa1ca7df69f" alt=""><figcaption></figcaption></figure>
* Dashboard widgets - You can now control the granularity with which to plot your time series widgets.

## April 2023

* Multiple dashboards per model - Different users might like to get different insights on the same model. For this reason, we added support for creating [multiple dashboards per model](https://docs.aporia.com/release-notes/broken-reference).
* Error detection for datasets - You will be able to see an indication in the relevant places across the platform in case we detected any error while trying to retrieve your datasets.
* Performance improvements - Resolved various performance bottlenecks and dramatically increased performance at scale.
* Edit versions - You can now edit existing stages by clicking on "edit" in the model versions page<br>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F4suoXrtIU3k3nl9G8ACK%2Fimage.png?alt=media&#x26;token=b1ee7dda-b44f-417d-955f-18db4ac71dbe" alt=""><figcaption><p>Edit Training / Serving</p></figcaption></figure>

## March 2023

* REST API - For those of you who would like to create automations for model integration, monitors creation, schema validation, etc. For more information read the [REST API documentation](https://platform.aporia.com/api/v1/docs).
* Default dashboard - Depending on your model type, a default dashboard will automatically be created to provide you a quick overview and insights on your first integrated version.
* Snowflake data source - For those of you who store your data in snowflake, you can now directly and easily integrate it using our new [snowflake data connector.](https://docs.aporia.com/data-sources/snowflake)
* Bug fixes - Resolved errors raised by using special characters in version schema.
* Custom segments - You can now create custom segments using a SQL-based syntax, that empowers you to create that exact segment you wish. For more info, check out our [docs](https://docs.aporia.com/api-reference/custom-segment-syntax).
* New custom metrics actions - Deleting a custom metric is available by clicking on the actions button in the custom metrics page<br>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FHMh1Q9pyLNnqQBlxnO1l%2Fimage.png?alt=media&#x26;token=dc5cca62-fdec-41f6-a112-5db85019cea2" alt=""><figcaption></figcaption></figure>
* Cross-version monitoring - We added the ability to use "all versions" in the monitors configurations. This way you can create monitors to detect issues across the unification of all model versions.

## February 2023

* Azure AD authentication for Postgres data source - In addition to using username & password, you can now configure your Postgres data source to use Azure AD authentication. This is available for accounts using SSO integration with Azure AD.
* New model actions - You can now rename and delete your models. Just click on the actions button in the models management page<br>

  <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FcqBoFryI921ZgLDYYdeY%2Fimage.png?alt=media&#x26;token=17a346f0-90b9-445a-b9de-1786773aa115" alt=""><figcaption></figcaption></figure>
* Ranking metrics support - Accuracy\@k, MRR\@k and nDCG\@k are natively supported in Aporia platform and you can use them in monitors, widgets, custom metrics, etc.
* Databricks deployment over Azure - Aporia deployment over Databricks is now supported for clients using Azure as their cloud provider.
* Bug fixes & performance improvements!

## January 2023

Direct Data Connectors - we are happy to introduce you with our transformative technology that empowers ML teams to effortlessly monitor and track their ML models by seamlessly integrating Aporia with their production database. By directly accessing your existing data lake, you can effortlessly monitor billions of predictions at minimal cloud costs (never duplicate your data!).

For more details read the full [announcement post](https://www.aporia.com/blog/aporia-introduces-direct-data-connectors-monitoring-large-scale-data-made-easy/).

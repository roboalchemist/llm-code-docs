# Source: https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/llms.txt

# AWS Supply Chain User Guide

> AWS Supply Chain; is a cloud-based supply chain management application that works with your existing enterprise resource planning (ERP) and supply chain management systems. Using AWS Supply Chain, you can connect and extract your inventory, supply, and demand related data from existing ERP or supply chain systems into one unified AWS Supply Chain; data model.

- [What is AWS Supply Chain?](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/what-is-service.html)
- [AWS support](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/admin-support-ug.html)
- [Document history](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/doc-history.html)

## [Configuring the AWS Supply Chain dashboard](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/viewing-dashboard.html)

- [Collaboration](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/collaboration.html): How to collaborate with other users in AWS Supply Chain.
- [Notifications](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/notifications.html): How to enable and disable notifications in AWS Supply Chain.


## [AWS Supply Chain Analytics](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/analytics.html)

- [Setting AWS Supply Chain Analytics](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/setting_analytics.html): You must enable AWS Supply Chain Analytics before you can start using Quick dashboards.
- [Configuring AWS Supply Chain Analytics as an administrator](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/configuring_analytics.html): You must configure AWS Supply Chain Analytics to use Analytics dashboard.
- [Creating new analysis](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/creating_new_analysis.html): To create a new analysis, follow the below procedure.
- [Prebuilt dashboards](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/prebuilt_dashboards.html): AWS Supply Chain Analytics supports the following prebuilt dashboards.
- [Application datasets used in AWS Supply Chain Analytics](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/application_datasets.html): The following are the list of application datasets displayed in AWS Supply Chain Analytics.


## [Data lake](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-connections.html)

- [Terminology used in data lake](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_lake_terminology.html): The terminology used in AWS Supply Chain data lake.

### [Data lake dashboard](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_ingestion.html)

You can use AWS Supply Chain data lake to ingest your data from various data sources.

- [Data quality](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_quality_datalake.html): Any identified data quality errors are displayed on the web application under Module errors.

### [Adding a new data source](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/adding_new_flows.html)

You can use AWS Supply Chain to ingest your data stored in your data source and extract your supply chain information.

### [Uploading files for the first time](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/uploading_files.html)

You can use the AWS Supply Chain Auto-association feature to upload your raw data and automatically associate your raw data with AWS Supply Chain data model.

- [Uploading subsequent files to an existing source](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/incremental_file_upload.html): There are two ways to upload subsequent datasets to an existing source.
- [Connecting to an EDI](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/connecting-edi.html)
- [Connecting to S/4 HANA](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/connecting-sap-hana.html): Before you can connect to your S/4 HANA data source, you must complete the following prerequisites.
- [Connecting to SAP ECC 6.0](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/connecting-sap-ecc.html)
- [Adding a new outbound source for Supply Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/adding_new_outbound_connector.html): You can use the new outbound source to upload the updated Supply Planning purchase order requests or plan enhancements.

### [Ingesting data for existing connections](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/ingesting-data.html)

The following are the ingestion options if you're using Amazon S3:

- [Uploading data to an Amazon S3 bucket](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/manually-uploading-data.html)


## [Insights](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/insights.html)

- [Insight settings](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/insight-settings.html): After creating an instance, follow the procedure below:
- [Viewing the network map](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/viewing-network-map.html): After ingesting the required datasets for Insights, the network map displays the current and projected inventory for products and locations in a map view for quick understanding of your inventory health and projected health.

### [Viewing inventory visibility](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/viewing-inventory-visibility.html)

You can use inventory visibility to view the inventory projections for all the ingested products and site combinations.

- [Understanding inventory projections](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/reading-projections.html): This section explains how to read the inventory projections.
- [Creating insight watchlist](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/creating-insights.html): You can create an insight watchlist to track and notify you on supply chain risks and deviations.
- [Viewing inventory insights](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/viewing-inventory-insights.html): When you create a watchlist for a specific product, site, risk type, and planning horizon, depending on the notifications settings, you will get notified when Insights detects an inventory risk.
- [Resolving an inventory risk insight](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/resolving-insights.html): Insights recommends one or more ways to resolve an inventory risk depending on the distance, time horizon, available transportation modes in the ingested data (transportation_lane.trans_mode), shipping costs (transportation_lane.unit_costs), and emissions that you've configured under Insights settings.

### [Lead time insights](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/resolving-lead-time-insights.html)

AWS Supply Chain provides insights on the lead time deviation for a vendor, product, and destination site level.

- [Lead time deviations and recommendations](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/lead-time-deviations.html): For every generated lead time insight, you can select a row to view the historical trend on the vendor's performance on delivering products from a given ship location to the destination location.


## [Order Planning and Tracking](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/work-order.html)

- [Configuring Order Planning and Tracking for the first time](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/setting-up-work-orders.html): As an administrator, you can create multiple processes and milestones to track your orders.

### [Orders settings](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/work-order-settings.html)

You can setup orders and track the material status from vendor to delivery using the following procedure.

- [Organization Labels](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/work-order-labels.html): As an administrator, you can customize the order labels.
- [Orders](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/work-order-dashboard.html): You can view all the orders that are at-risk, delivered, early, late, on time, or watch.
- [Procurement](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/configuring-procurement.html): You can view the procurement details for all the items ordered as part of a order.
- [Logistics](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/configuring-logistics.html): You can view the logistics details for all the items ordered as part of a order.
- [Troubleshooting](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/Troubleshooting.html): This section contains information about how to troubleshoot order planning and tracking issues that may occur.


## [Demand Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-planning.html)

- [Terminology used in Demand Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/servicename-terminology.html): The following is the common terminology that you may frequently use in Demand Planning.
- [Create your first demand plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/onboarding.html): When you log into Demand Planning for the first time, you will be able to view the onboarding pages that highlight key product features and help you get familiar with the Demand Planning capabilities.

### [Data Validation and Demand Pattern Analysis](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-validation-analysis.html)

Data Validation and Demand Pattern Analysis tools help you evaluate the quality of your data and identify key patterns influencing your demand forecasts.

### [Data Validation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-validation.html)

Data Validation is a crucial step early in the forecast creation process that ensures the input data meets the necessary quality standards for forecasting.

- [Data Validation Process](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-validation-process.html): After the preprocessing process described above completes, the data validation process begins.
- [Data Validation Report Access](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-validation-report-access.html): When creating a forecast for the first time, navigate to the Demand Planning module in AWS Supply Chain and choose Create a Plan.
- [Data Validation Error Export](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-validation-error-export.html): Error records can be exported by choosing Download on the Data Validation report page when the validation is checking individual data points that failed.
- [Data Validation Rules](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-validation-rules.html): The validations performed prior to forecast creation are below.

### [Demand Pattern and Recommendation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-patterns.html)

Demand Pattern and Recommendation examines the transformed historical demand input at each configured forecast granularity level (for example, product, location, or channel) to uncover underlying patterns and characteristics in your demand data.

- [Demand Patterns Components](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-patterns-components.html): Demand Patterns analysis happens on three dimensions:
- [Demand Patterns Recommendations](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-patterns-recommendations.html): The system provides targeted recommendations based on identified demand patterns to help improve forecast accuracy.
- [Demand Pattern and Recommendation Report Access](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-patterns-report-access.html)
- [Forecast Algorithms](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-algorithims.html): AWS Supply Chain Demand Planning offers a combination of 25 built-in forecast models to create baseline demand forecasts for products with diverse demand patterns in customersâ datasets.

### [Forecast based on demand drivers](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand_drivers.html)

To enhance forecast accuracy while configuring your forecast, you can use demand drivers.

- [Demand driver configuration](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/configuration_demand_drivers.html): To use demand drivers, you must configure them.
- [Demand driver recommendations](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_setup_demand_drivers.html): While configuring aggregation and filling methods for demand drivers, a general guideline is to assign mean aggregation for both boolean and continuous data types.
- [Product lineage](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product_lineage.html): Product lineage refers to the relationship established between products and their previous versions or alternate products.
- [Product lifecycle](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product_lifecycle.html): Product lifecycle describes the lifecycle of a product from introduction to End of Life (EoL).

### [Manage demand plans](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/dp_dashboard.html)

After the forecast is generated, choose Demand Planning, and then choose Manage Demand Plan.

- [Overview](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/overview_dp.html)
- [Demand plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/changing_category.html): After the forecast is generated, you can review the forecast values on the Demand Plan tab.
- [Forecast lock](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast_lock.html): You can use the forecast lock feature to lock specific periods in your forecast to prevent any further edits or adjustments.
- [Forecast model analyzer](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast_model_analyzer.html): Forecast model analyzer is a self-service tool that you can use to execute forecast experiments on multiple forecast models (forecast period in past and future).
- [Manage Demand Plan settings](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/settings.html): You can update the Demand Planning settings at any time to make sure that your forecasts are more accurate and take effect when the forecast is successfully generated.

### [Role-based access control](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/rolebased.html)

AWS Supply Chain Demand Planning offers two default access levels:

### [Managing user access](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/manage-user-access.html)

AWS Supply Chain administrators can modify roles and permissions.

- [Adding new users](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/add-new-users.html): To add new users, follow these steps:
- [Modifying existing user access](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/modify-user-access.html): To modify existing user access, follow these steps:
- [Creating custom roles](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/create-custom-roles.html): To create custom roles, follow these steps:
- [Dataset requirements](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/dataset-requirements.html): The following are important dataset requirements:


## [Supply Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-planning.html)

### [Auto Replenishment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/auto-replenishment.html)

You can use the Auto Replenishment feature to determine the amount of inventory to hold and when to order more inventory by automating inventory management.

- [Key inputs](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/key-input.html): Auto Replenishment relies on the following inputs to make accurate and informed calculations for inventory replenishment:
- [Planning process](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-process.html): Replenishment requirements are calculated based on the configured network topology for an item.

### [Inventory policies](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory-policies.html)

Auto Replenishment supports three different inventory policies.

- [Absolute inventory level](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/absolute-inventory-level.html): If you use absolute quantities to manage your inventory levels, you can use this policy setting to calculate target inventory level and RoQ.
- [Days of Cover](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/doc-forecast.html): If you use Days of Cover (DoC) to manage your inventory levels, then this would be an appropriate policy setting to drive the calculation of target inventory levels and RoQ.
- [Service level](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/service-level.html): If you use in-stock percentage to manage your inventory levels, you can use this policy setting to drive the calculation of target inventory level and replenishment.
- [Configuring Auto Replenishment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/configuring-auto-replenishment.html): By using Auto Replenishment, you can view the amount of inventory to hold and when to order more inventory by automating inventory management.
- [Business workflow](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/business-workflow.html): Auto Replenishment provides the following workflow for you to manage your inventory replenishment process.

### [Manufacturing Plans](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/manufacturing_plans.html)

Manufacturing Plans helps you to determine production, transfer, and material requirements for multiple levels of sub-assemblies and components in a bill of material (BOM).

- [Key inputs](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/manufacturing_plans_key_inputs.html): Manufacturing Plans depends on various inputs to make accurate and informed calculations for generating material, transfer, and production plans.
- [Planning process](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/manufacturing_plans_planning_process.html): Manufacturing Plans include material, transfer, and production plans.
- [Configuring Manufacturing Plans](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/Configuring_manufacturing_plans.html): Configure Manufacturing Plans to generate material, transfer, and production requirements for components and finished good items.
- [Business workflow](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/sharing_manufacturing_plans.html): Supply Planning provides the following workflow to manage your manufacturing plans.

### [Planning configuration data](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/non-transactional.html)

This section lists all the required fields used by Supply Planning and describes how each field is used.

- [Transactional data](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/transactional.html): Topics


## [N-Tier Visibility](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/partner.html)

- [Using N-Tier Visibility for the first time](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/ntier_firsttime.html): You can use N-Tier Visibility with Supply Planning or Work Order Insights to extend visibility beyond your organization to your external trading partners.

### [N-Tier Visibility dashboard](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/ntier_overview.html)

You can user the n-tier dashboard to navigate through partner onboarding and collaboration.

- [Partner Network](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/partner_network.html): You can view the list of partners that are imported through the AWS Supply Chain data lake into the AWS Supply Chain network.
- [Purchase Orders](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/purchase-orders.html): You can view the list of purchase order data requests that are published to your partners.
- [Forecast Commits](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-commitments.html): You can view the forecast commit data requests that are published to your partners.
- [Responding to requests as a Partner](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/partner_response.html): As a Partner, you can accept or decline Partner requests, review purchase orders and forecast commits.
- [N-Tier Visibility settings](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/ntier-settings.html): You can update the forecast commits and purchase orders response settings in AWS Supply Chain.


## [Sustainability](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/sustainability.html)

### [Sustainability dashboard](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/partner_overview.html)

You can invite partners by using the AWS Supply Chain data lake connectors and by mapping the partner information to Partners or Partner's point-of-contact from Amazon S3 or other ERP systems.

- [Partner Network](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/partner_network_dashboard.html): You can view the partners in your scn network.

### [Data requests](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_requests.html)

You can request data from your partners that have accepted your invite and are in the AWS Supply Chain network.

### [Creating data requests](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/create_data_requests.html)

You can use the simple reporting template to request any type of data from your partners.

- [Data requests examples](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_request_examples.html): Here are some examples on how you can structure the Simple Reporting data form to meet your needs.
- [Emission data forms](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_form_updates.html): You can use the emission data forms to collect scope 1, 2, and 3 emissions from your partner network at the granularity level of a country or facility.
- [Transportation emission forms](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/glec_form.html): You can use the transport emission Global Logistics Emissions Council (GLEC) data forms to collect the emission reports from transportation routes by parcels delivered or by account.
- [Responding to requests as a Partner](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/partner_response_sustainability.html): As a Partner, you can accept or decline Partner requests, review and respond to data requests.
- [Sustainability settings](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/settings_mfa.html): To enhance your account security, you can use multifactor authentication.


## [Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/qinasc.html)

- [Enabling Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/enabling_QinASC.html)

### [Creating and assigning custom user roles to access Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/setting_custom_roles.html)

To create and assign custom user roles in AWS Supply Chain, perform the following procedure:

- [Updating existing custom user roles to access Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/updating_custom_roles.html): To update an existing user permission role in AWS Supply Chain, perform the following procedure:
- [Using Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/using_QinASC.html): After enabling Amazon Q in AWS Supply Chain, perform the following procedure:
- [Sample questions you can ask Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/sample_questions.html)
- [Cross-Region calls with Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/cross_region_calls.html): Amazon Q in AWS Supply Chain has a dependency on Amazon Kendra for retrieving relevant search results from public documentation that may be used to answer your questions.


## [Data entities used in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model.html)

- [Sustainability](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/entities-sustainability.html): The table below list the data entities and columns used by Sustainability for partner invitations and onboarding.
- [N-Tier Visibility](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/entities-n-tier.html): The table below list the data entities and columns used by N-Tier Visibility.
- [Supply Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/entities-supply-planning.html): The table below list the data entities and columns used by Supply Planning.
- [Insights](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/entities-insights.html): The table below list the data entities and columns used by Insights for the Inventory Visibility, Network Map, Inventory Insights, and Rebalance Recommendations features.
- [Order Planning and Tracking](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/entities-work-order-insights.html)

### [Demand Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/required_entities.html)

The following table lists the data entities and columns used by Demand Planning.

- [Prequisites before uploading your dataset](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data_quality.html): To successfully generate a forecast, make sure your dataset adheres to the following.
- [Data mapping example for fulfillment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/fulfillment_scenario.html): Below is an example to map brick and mortar or online sales to outbound order line dataset and optimize the historical demand setup.


## [Data entities supported in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html)

### [Organization](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/organization.html)

This section lists the data entities within the organization category.

- [company](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/organization-company-entity.html): Primary key (PK)
- [geography](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/organization-geography-entity.html): Primary key (PK)
- [trading_partner](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/organization-trading-partner-entity.html): Primary key (PK)
- [trading_partner_poc](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/organization-trading-partner-poc-entity.html): Primary key (PK)

### [Product](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product.html)

This section lists the data entities within the product category.

- [product](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product-product-entity.html): Primary key (PK)
- [product_hierarchy](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product-hierarchy-entity.html): Primary key (PK)
- [product_uom](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product-uom-entity.html): Primary key (PK)
- [product_alternate](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product-alternate-entity.html): Primary key (PK)
- [un_details](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product-un-details-entity.html): Primary key (PK)

### [Network](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/network2.html)

This section lists the data entities within the network category.

- [site](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/network-site-entity.html): Primary key (PK)
- [transportation_lane](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/network-transporation-lane-entity.html): Primary key (PK)

### [Vendor management](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/vendor-management.html)

This section lists the data entities within the vendor management category.

- [vendor_product](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/vendor-management-product-entity.html): Primary key (PK)
- [vendor_lead_time](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/vendor-management-lead-time-entity.html): Primary key (PK)
- [vendor_holiday](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/vendor-management-holiday-entity.html): Primary key (PK)

### [Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning.html)

This section lists the data entities within the planning category.

- [product_bom](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-product-bom-entity.html): Primary key (PK)
- [inv_policy](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-inv-policy-entity.html): Primary key (PK)
- [segmentation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-segmentation-entity.html): Primary key (PK)
- [sourcing_rules](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-sourcing-rules-entity.html): Primary key (PK)
- [sourcing_schedule](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-sourcing-schedule-entity.html): Primary key (PK)
- [sourcing_schedule_details](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-sourcing-schedule-details-entity.html): Primary key (PK)
- [reservation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-reservation-entity.html): Primary key (PK)
- [supply_planning_parameters](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-supply_planning_parameters-entity.html): Primary key (PK)

### [Operation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation.html)

This section lists the data entities within the operation category.

- [process_header](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-header-entity.html): Primary key (PK)
- [process_operation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-operation-entity.html): Primary key (PK)
- [process_product](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-product-entity.html): Primary key (PK)
- [production_process](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-production-process-entity.html): Primary key (PK)
- [work_order_plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/work-order-plan-entity.html): Primary key (PK)

### [Inventory management](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt.html)

This section lists the data entities within the inventory management category.

- [inv_level](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt-inv-level-entity.html): Primary key (PK)

### [Inbound](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment.html)

This section lists the data entities within the inbound category.

- [inbound_order](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-entity.html): Primary key (PK)
- [inbound_order_line](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-entity.html): Primary key (PK)
- [inbound_order_line_schedule](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-schedule-entity.html): Primary key (PK)
- [shipment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-entity.html): Primary key (PK)
- [shipment_stop](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-entity.html): Primary key (PK)
- [shipment_stop_order](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-order-entity.html): Primary key (PK)
- [shipment_lot](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-lot-entity.html): Primary key (PK)

### [Outbound fulfillment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment.html)

This section lists the data entities within the outbound fulfillment category.

- [outbound_order_line](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-order-line-entity.html): Primary key (PK)
- [outbound_shipment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-shipment-entity.html): Primary key (PK)

### [Cost management](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/cost_management.html)

This section lists the data entities within the cost management category.

- [customer_cost](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/customer-cost-entity.html): Primary key (PK)

### [Plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/plan.html)

This section lists the data entities within the plan category.

- [supply_plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-plan-entity.html): Primary key (PK)

### [Forecast](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast.html)

This section lists the data entities within the forecast category.

- [supplementary_time_series](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-supp-timeseries-entity.html)
- [forecast](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-forecast-entity.html): Primary key (PK)

### [Reference](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/reference.html)

This section lists the data entities within the reference category.

- [reference_field](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/reference-fields-entity.html): Primary key (PK)
- [calendar](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/reference-calendar-entity.html): Primary key (PK)
- [uom_conversion](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/reference-uom-conversion-entity.html): Primary key (PK)

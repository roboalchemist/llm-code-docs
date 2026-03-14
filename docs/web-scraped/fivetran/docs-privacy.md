# Source: https://fivetran.com/docs/privacy

Title: Fivetran Privacy Policy

URL Source: https://fivetran.com/docs/privacy

Markdown Content:
Learn how Fivetran respects our users' right to privacy. For more details, see our [Privacy Program Framework](https://www.fivetran.com/legal/privacy-program).

* * *

Retention of customer data[](https://fivetran.com/docs/privacy#retentionofcustomerdata)
---------------------------------------------------------------------------------------

How long we retain customer data depends on the data type:

| Customer Data Type | Retention Period | Note |
| --- | --- | --- |
| Customer data | < 8 hours (usually) | We purge customer data as soon as it is successfully written to the destination, except in the cases below. |
| Temporary data | < 24 hours (usually) | Some data integration or replication processes require ephemeral data specific to a data source (for example, binary logs for MySQL or events streams for Asana). We delete this data as soon as possible, though that may take more than 24 hours in rare cases. |
| Event data from the Webhooks connector and other connectors using webhooks | Varies | If you sync webhooks or event data, we retain that data for a limited time so that it can be re-synced if needed. To find the data retention period for your connector type, see our [Events documentation](https://fivetran.com/docs/connectors/events/webhooks#dataretentionperiod). |
| Customer access keys | Duration of the services | We retain customer database credentials and SaaS OAuth tokens to securely and continuously extract data and troubleshoot customer issues. These credentials are securely stored in a key management system, which is backed by a hardware security module managed by our cloud provider. |
| Customer metadata | Duration of the services | We retain configuration details and data points (such as table and column names) for each connection so that this information can be displayed in your Fivetran dashboard. |
| Email attachments collected by Email connector | Duration of the services | The Email connector collects the email attachments, we back up and store these attachments in an internal S3 bucket so that they can be re-synced if needed. These attachments are retained until you delete your Email connection. |

In the following two cases, customer data is purged as soon as it is successfully written to the destination. If the data writing process takes longer than usual, the data is automatically purged after 30 days using object lifecycle management:

*   **Destination outage**: If your destination is down, we maintain the data that we've read from your source so that we can resume the sync without losing progress once the issue is resolved.
*   **Schema information for data blocking or column hashing purposes**: If you choose to [block or hash columns](https://fivetran.com/docs/using-fivetran/features/data-blocking-column-hashing) before running the [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync) for your new connection, we query your data source and cache your data while we fetch the full schema. We write to the destination only the data you selected as tables and columns from the fully fetched schema and only when you approved the selection.

* * *

Fivetran data residency[](https://fivetran.com/docs/privacy#fivetrandataresidency)
----------------------------------------------------------------------------------

Fivetran runs data connections on servers in the United States (US), Canada, European Union (EU), United Kingdom (UK), Australia, Singapore, India, Japan, Indonesia, and the Middle East. You can select your preferred data processing location when configuring your destination. All connections configured in a destination run in the destination's designated location. This means that in most cases, your data will not leave our region-specific servers during processing. For example, if you configure your destination to use our EU servers, your data will not leave the EU during processing. See our destination documentation to [learn how to configure your data processing location](https://fivetran.com/docs/destinations#choosingyourdataprocessinglocationandcloudserviceprovider).

Certain connectors are exceptions to this policy, such as the email connector and [connectors that sync webhooks and event data](https://fivetran.com/docs/privacy#retentionofcustomerdata) as well as customer support requests unless you have purchased Fivetran's U.S.-only support option. By default, we store email connector and event data in a cloud storage service in one of the following data processing locations:

*   the EU location - for destinations run in the EU location
*   the UK location - for destinations run in the UK location
*   the US location - for all other destinations

Fivetran runs our services on Google Cloud Platform (GCP), Amazon Web Services (AWS), and Azure. The following table lists regions supported by Fivetran for each service provider:

| Geography | GCP Regions | AWS Regions | Azure Regions |
| --- | --- | --- | --- |
| US | us-east4 (N. Virginia)* us-west1 (Oregon) us-central1 (Iowa) | us-east-1 (N. Virginia)* us-east-2 (Ohio) us-west-2 (Oregon) us-gov-west-1 (GovCloud US West) | eastus (Virginia) eastus2 (Virginia)* centralus (Iowa) westus3 (Phoenix) |
| UK | europe-west2 (London) | eu-west-2 (London) | uksouth (London) |
| EU | europe-west3 (Frankfurt) | eu-central-1 (Frankfurt)* eu-west-1 (Dublin) eu-north-1 (Stockholm) | westeurope (Netherlands) germanywestcentral (Frankfurt) |
| Canada | northamerica-northeast1 (Montréal) | ca-central-1 (Montréal) | canadacentral (Toronto) |
| Australia | australia-southeast-1 (Sydney) | ap-southeast-2 (Sydney) | australiaeast (Sydney) |
| Singapore | asia-southeast1 (Singapore) | ap-southeast-1 (Singapore) | southeastasia (Singapore) |
| India | asia-south1 (Mumbai) | ap-south-1 (Mumbai) | centralindia (Pune) |
| Japan | asia-northeast1 (Tokyo) | ap-northeast-1 (Tokyo) | japaneast (Tokyo) |
| South Korea | asia-northeast3 (Seoul) | ap-northeast-2 (Seoul) | koreacentral (Seoul) |
| Indonesia | asia-southeast2 (Jakarta) |  |  |
| Middle East |  |  | uaenorth (Dubai) |
| Switzerland |  |  | switzerlandnorth (Zurich) |

*Default region for a given cloud provider / geography combination. For some cloud providers and geographies, there is only one region available.

Google Cloud Platform is the default cloud service provider. Google Cloud Platform is your only cloud service provider if you're on a [Standard or Free plan](https://www.fivetran.com/pricing/features). You can select a different cloud service provider if you are on an [Enterprise or Business Critical plan](https://fivetran.com/docs/privacy#fivetrandataresidency).

Regardless of the plan you use, you can select the Fivetran processing geography when creating a destination. Fivetran processing is specific to how we read data from your source location. If you are on an [Enterprise or Business Critical plan](https://www.fivetran.com/pricing/features), you also can select the cloud service provider. Lastly, if you are on a Business Critical plan, you can select a cloud region.

| Plan | Choice of Geography | Choice of Service Provider | Choice of Cloud Region |
| --- | --- | --- | --- |
| Free |  |  |  |
| Standard |  |  |  |
| Enterprise |  |  |  |
| Business Critical |  |  |  |

You need to safelist the corresponding [Fivetran IPs](https://fivetran.com/docs/using-fivetran/ips) in your firewall for the geography and region you selected for your destination.

* * *

Sub-processor management[](https://fivetran.com/docs/privacy#subprocessormanagement)
------------------------------------------------------------------------------------

Fivetran uses certain subprocessors to assist us in providing the Fivetran Services as described in the [Terms of Service (TOS)](https://www.fivetran.com/legal/online-service-agreement). We maintain a list of sub-processors and provide notice for any additions.

Defined terms used herein shall have the same meaning as defined in the TOS.

### What is a Subprocessor?[](https://fivetran.com/docs/privacy#whatisasubprocessor)

A subprocessor is a third-party data processor engaged by Fivetran, including entities from within the Fivetran Group, who has or potentially will have access to or process personal data on behalf of a Customer. Fivetran engages different types of subprocessors to perform various functions as explained in the tables below. Fivetran refers to third parties that do not have access to or process personal data on behalf of a Customer, but who are otherwise used to provide the Services, as "subcontractors" and not "subprocessors". The list includes the ability for our customers to request a preferred email contact to receive notifications of changes. Customers may send their preferred email contact to [privacy@fivetran.com](mailto:privacy@fivetran.com).

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Alto Logica LLC | Professional services and support use cases | Global |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Axiata Digital & Analytics Sdn Bhd (dba ADA Asia, which acquired dhiOmics Analytics) | Development and support use cases | India, Southeast Asia |
| Danube Data Labs LLC (dba Danube Data Labs Kft.) | Professional services and support use cases | Global |
| Google LLC | Google Cloud hosting environment for Supplier services | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| AG CONSULTORÍA Y SISTEMAS DE MÉXICO, S.A. DE C.V (dba Growjet) | Professional services | Latin America |
| Infinite Lambda Limited | Professional services and development use cases | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| phData Inc | Professional services | US, India |
| SunnyData Inc. | Professional services | US, Latin America |

#### AI Subprocessors[](https://fivetran.com/docs/privacy#aisubprocessors)

This section is only applicable if you use our AI product(s).

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Anthropic PBC | Development use cases and generative artificial intelligence services | Global |
| Chroma Inc. | Development use cases and generative artificial intelligence services | Global |
| Cohere Inc. | Development and support use cases | Global |
| Google LLC | Development use cases and generative artificial intelligence services | Global |
| OpenAI, L.L.C. | Development and support use cases | Global |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Canada Inc. | Fivetran affiliate company | Canada |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Novi Sad | Fivetran affiliate company | Serbia |
| Fivetran Japan KK | Fivetran affiliate company | Japan |
| Sutro Labs, Inc. (dba Census) | Fivetran affiliate company | US, UK, and Canada |
| Tobiko Software LLC | Fivetran affiliate company | US, UK, Canada, New Zealand, and Greece |

### Access[](https://fivetran.com/docs/privacy#access)

Neither Fivetran nor our subprocessors are able to access your customer data without [your explicit approval](https://fivetran.com/docs/privacy#pipelinedatasubprocessors).

Grid Dynamics Holdings, Inc. (DAXX) and Danube Data Labs LLC are utilized to support Fivetran's HVR and HVA products. They do not have access to customer data by default and would only have access with the explicit authorization of the customer through a Support case using our standard [Diagnostic Data Access process](https://fivetran.com/docs/security#diagnosticdataaccess).

Fivetran uses Alto Logica to outsource hiring for engineering talent, but Fivetran does not outsource the development; these engineers follow all of Fivetran's controls. They use the same authentication and access control systems as our internal full-time employees (Okta MFA) and follow the same procedures as outlined below.

By default Fivetran personnel do not have access to customer data. In the event a customer has a connection failure and contacts Fivetran Support, Fivetran may need to debug the failure against customer data if other troubleshooting fails. In such an event Fivetran Support would request Diagnostic Data Access where the customer’s admin would need to approve Fivetran access in the Fivetran dashboard.Once access has been approved, the request may be routed to one of Fivetran’s engineering teams that develop the Fivetran connectors to investigate the failure. Fivetran maintains a global development organization with teams located in the United States, Ireland, India, the Netherlands, and Serbia. Which team the issue is routed to will depend on the connector that has the customer issue to resolve the failure as quickly as possible. This debugging environment is tightly controlled and activity is monitored by Fivetran’s Security team. Access is automatically revoked after 21 days or when the customer disables Diagnostic Data Access in their dashboard.

Additionally, for customers that cannot have data access from countries outside of the United States, Fivetran offers U.S. only support for an additional cost.

Fivetran uses a single sign-on (SSO) service to manage access control and permission provisioning, based on user role within the organization. Role-based access is established through Fivetran’s single sign-on providers which is integrated with Fivetran’s Human Resources system. Employee role assignments are automatically updated when employment is terminated or departments/roles change. In addition, Fivetran performs quarterly user access reviews of access to customer facing systems.

### History - Archived versions[](https://fivetran.com/docs/privacy#historyarchivedversions)

February 2026
#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_1)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Alto Logica LLC. | Professional services and support use cases | Global |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Axiata Digital & Analytics Sdn Bhd (dba ADA Asia, which acquired dhiOmics Analytics) | Development and support use cases | India, Southeast Asia |
| Danube Data Labs LLC. | Professional services and support use cases | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| Growjet | Professional services | Latin America |
| Infinite Lambda | Professional services and development use cases | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| phData Inc | Professional services | US, India |
| SunnyData | Professional services | US, Latin America |

#### AI Subprocessors[](https://fivetran.com/docs/privacy#aisubprocessors_1)

This section is only applicable if you use our AI product(s).

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| OpenAI, LLC | Development and support use cases | Global |
| Cohere Inc. | Development and support use cases | Global (US, UK, and Canada) |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_1)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Canada Inc. | Fivetran affiliate company | Canada |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Novi Sad | Fivetran affiliate company | Serbia |
| Fivetran Japan KK | Fivetran affiliate company | Japan |
| Sutro Labs, Inc. (dba Census) | Fivetran affiliate company | US, UK, and Canada |

### Access[](https://fivetran.com/docs/privacy#access_1)

Neither Fivetran nor our subprocessors are able to access your customer data without [your explicit approval](https://fivetran.com/docs/privacy#pipelinedatasubprocessors).

Grid Dynamics Holdings, Inc. (DAXX) and Danube Data Labs LLC are utilized to support Fivetran's HVR and HVA products. They do not have access to customer data by default and would only have access with the explicit authorization of the customer through a Support case using our standard [Diagnostic Data Access process](https://fivetran.com/docs/security#diagnosticdataaccess).

Fivetran uses Alto Logica to outsource hiring for engineering talent, but Fivetran does not outsource the development; these engineers follow all of Fivetran's controls. They use the same authentication and access control systems as our internal full-time employees (Okta MFA) and follow the same procedures as outlined below.

By default Fivetran personnel do not have access to customer data. In the event a customer has a connection failure and contacts Fivetran Support, Fivetran may need to debug the failure against customer data if other troubleshooting fails. In such an event Fivetran Support would request Diagnostic Data Access where the customer’s admin would need to approve Fivetran access in the Fivetran dashboard.Once access has been approved, the request may be routed to one of Fivetran’s engineering teams that develop the Fivetran connectors to investigate the failure. Fivetran maintains a global development organization with teams located in the United States, Ireland, India, the Netherlands, and Serbia. Which team the issue is routed to will depend on the connector that has the customer issue to resolve the failure as quickly as possible. This debugging environment is tightly controlled and activity is monitored by Fivetran’s Security team. Access is automatically revoked after 21 days or when the customer disables Diagnostic Data Access in their dashboard.

Additionally, for customers that cannot have data access from countries outside of the United States, Fivetran offers U.S. only support for an additional cost.

Fivetran uses a single sign-on (SSO) service to manage access control and permission provisioning, based on user role within the organization. Role-based access is established through Fivetran’s single sign-on providers which is integrated with Fivetran’s Human Resources system. Employee role assignments are automatically updated when employment is terminated or departments/roles change. In addition, Fivetran performs quarterly user access reviews of access to customer facing systems.

August 2025
Learn how Fivetran respects our users' right to privacy. For more details, see our [Privacy Program Framework](https://www.fivetran.com/legal/privacy-program).

* * *

Retention of customer data[](https://fivetran.com/docs/privacy#retentionofcustomerdata_1)
-----------------------------------------------------------------------------------------

How long we retain customer data depends on the data type:

| Customer Data Type | Retention Period | Note |
| --- | --- | --- |
| Customer data | < 8 hours (usually) | We purge customer data as soon as it is successfully written to the destination, except in the cases below. |
| Temporary data | < 24 hours (usually) | Some data integration or replication processes require ephemeral data specific to a data source (for example, binary logs for MySQL or events streams for Asana). We delete this data as soon as possible, though that may take more than 24 hours in rare cases. |
| Event data from the Webhooks connector and other connectors using webhooks | Varies | If you sync webhooks or event data, we retain that data for a limited time so that it can be re-synced if needed. To find the data retention period for your connector type, see our [Events documentation](https://fivetran.com/docs/connectors/events/webhooks#dataretentionperiod). |
| Customer access keys | Duration of the services | We retain customer database credentials and SaaS OAuth tokens to securely and continuously extract data and troubleshoot customer issues. These credentials are securely stored in a key management system, which is backed by a hardware security module managed by our cloud provider. |
| Customer metadata | Duration of the services | We retain configuration details and data points (such as table and column names) for each connection so that this information can be displayed in your Fivetran dashboard. |
| Email attachments collected by Email connector | Duration of the services | The Email connector collects the email attachments, we back up and store these attachments in an internal S3 bucket so that they can be re-synced if needed. These attachments are retained until you delete your Email connection. |

In the following two cases, customer data is purged as soon as it is successfully written to the destination. If the data writing process takes longer than usual, the data is automatically purged after 30 days using object lifecycle management:

*   **Destination outage**: If your destination is down, we maintain the data that we've read from your source so that we can resume the sync without losing progress once the issue is resolved.
*   **Schema information for data blocking or column hashing purposes**: If you choose to [block or hash columns](https://fivetran.com/docs/using-fivetran/features/data-blocking-column-hashing) before running the [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync) for your new connection, we query your data source and cache your data while we fetch the full schema. We write to the destination only the data you selected as tables and columns from the fully fetched schema and only when you approved the selection.

* * *

Fivetran data residency[](https://fivetran.com/docs/privacy#fivetrandataresidency_1)
------------------------------------------------------------------------------------

Fivetran runs data connections on servers in the United States (US), Canada, European Union (EU), United Kingdom (UK), Australia, Singapore, India, Japan, Indonesia, and the Middle East. You can select your preferred data processing location when configuring your destination. All connections configured in a destination run in the destination's designated location. This means that in most cases, your data will not leave our region-specific servers during processing. For example, if you configure your destination to use our EU servers, your data will not leave the EU during processing. See our destination documentation to [learn how to configure your data processing location](https://fivetran.com/docs/destinations#choosingyourdataprocessinglocationandcloudserviceprovider).

Certain connectors are exceptions to this policy, such as the email connector and [connectors that sync webhooks and event data](https://fivetran.com/docs/privacy#retentionofcustomerdata) as well as customer support requests unless you have purchased Fivetran's U.S.-only support option. By default, we store email connector and event data in a cloud storage service in one of the following data processing locations:

*   the EU location - for destinations run in the EU location
*   the UK location - for destinations run in the UK location
*   the US location - for all other destinations

Fivetran runs our services on Google Cloud Platform (GCP), Amazon Web Services (AWS), and Azure. The following table lists regions supported by Fivetran for each service provider:

| Geography | GCP Regions | AWS Regions | Azure Regions |
| --- | --- | --- | --- |
| US | us-east4 (N. Virginia)* us-west1 (Oregon) us-central1 (Iowa) | us-east-1 (N. Virginia)* us-east-2 (Ohio) us-west-2 (Oregon) us-gov-west-1 (GovCloud US West) | eastus (Virginia) eastus2 (Virginia)* centralus (Iowa) westus3 (Phoenix) |
| UK | europe-west2 (London) | eu-west-2 (London) | uksouth (London) |
| EU | europe-west3 (Frankfurt) | eu-central-1 (Frankfurt)* eu-west-1 (Dublin) eu-north-1 (Stockholm) | westeurope (Netherlands) germanywestcentral (Frankfurt) |
| Canada | northamerica-northeast1 (Montréal) | ca-central-1 (Montréal) | canadacentral (Toronto) |
| Australia | australia-southeast-1 (Sydney) | ap-southeast-2 (Sydney) | australiaeast (Sydney) |
| Singapore | asia-southeast1 (Singapore) | ap-southeast-1 (Singapore) | southeastasia (Singapore) |
| India | asia-south1 (Mumbai) | ap-south-1 (Mumbai) | centralindia (Pune) |
| Japan | asia-northeast1 (Tokyo) | ap-northeast-1 (Tokyo) | japaneast (Tokyo) |
| South Korea | asia-northeast3 (Seoul) | ap-northeast-2 (Seoul) | koreacentral (Seoul) |
| Indonesia | asia-southeast2 (Jakarta) |  |  |
| Middle East |  |  | uaenorth (Dubai) |
| Switzerland |  |  | switzerlandnorth (Zurich) |

*Default region for a given cloud provider / geography combination. For some cloud providers and geographies, there is only one region available.

Google Cloud Platform is the default cloud service provider. Google Cloud Platform is your only cloud service provider if you're on a [Standard or Free plan](https://www.fivetran.com/pricing/features). You can select a different cloud service provider if you are on an [Enterprise or Business Critical plan](https://fivetran.com/docs/privacy#fivetrandataresidency).

Regardless of the plan you use, you can select the Fivetran processing geography when creating a destination. Fivetran processing is specific to how we read data from your source location. If you are on an [Enterprise or Business Critical plan](https://www.fivetran.com/pricing/features), you also can select the cloud service provider. Lastly, if you are on a Business Critical plan, you can select a cloud region.

| Plan | Choice of Geography | Choice of Service Provider | Choice of Cloud Region |
| --- | --- | --- | --- |
| Free |  |  |  |
| Standard |  |  |  |
| Enterprise |  |  |  |
| Business Critical |  |  |  |

You need to safelist the corresponding [Fivetran IPs](https://fivetran.com/docs/using-fivetran/ips) in your firewall for the geography and region you selected for your destination.

* * *

Sub-processor management[](https://fivetran.com/docs/privacy#subprocessormanagement_1)
--------------------------------------------------------------------------------------

Fivetran uses certain subprocessors to assist us in providing the Fivetran Services as described in the [Terms of Service (TOS)](https://www.fivetran.com/legal/online-service-agreement). We maintain a list of sub-processors and provide notice for any additions.

Defined terms used herein shall have the same meaning as defined in the TOS.

### What is a Subprocessor?[](https://fivetran.com/docs/privacy#whatisasubprocessor_1)

A subprocessor is a third-party data processor engaged by Fivetran, including entities from within the Fivetran Group, who has or potentially will have access to or process personal data on behalf of a Customer. Fivetran engages different types of subprocessors to perform various functions as explained in the tables below. Fivetran refers to third parties that do not have access to or process personal data on behalf of a Customer, but who are otherwise used to provide the Services, as "subcontractors" and not "subprocessors". The list includes the ability for our customers to request a preferred email contact to receive notifications of changes. Customers may send their preferred email contact to [privacy@fivetran.com](mailto:privacy@fivetran.com).

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_2)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Alto Logica LLC. | Professional services and support use cases | Global |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Axiata Digital & Analytics Sdn Bhd (dba ADA Asia, which acquired dhiOmics Analytics) | Development and support use cases | India, Southeast Asia |
| Danube Data Labs LLC. | Professional services and support use cases | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| Growjet | Professional services | Latin America |
| Infinite Lambda | Professional services and development use cases | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| phData Inc | Professional services | US, India |

#### AI Subprocessors[](https://fivetran.com/docs/privacy#aisubprocessors_2)

This section is only applicable if you use our AI product(s).

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| OpenAI, LLC | Development and support use cases | Global |
| Cohere Inc. | Development and support use cases | Global (US, UK, and Canada) |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_2)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Canada Inc. | Fivetran affiliate company | Canada |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Novi Sad | Fivetran affiliate company | Serbia |
| Fivetran Japan KK | Fivetran affiliate company | Japan |
| Sutro Labs, Inc. (dba Census) | Fivetran affiliate company | US, UK, and Canada |

### Access[](https://fivetran.com/docs/privacy#access_2)

Neither Fivetran nor our subprocessors are able to access your customer data without [your explicit approval](https://fivetran.com/docs/privacy#pipelinedatasubprocessors).

Grid Dynamics Holdings, Inc. (DAXX) and Danube Data Labs LLC are utilized to support Fivetran's HVR and HVA products. They do not have access to customer data by default and would only have access with the explicit authorization of the customer through a Support case using our standard [Diagnostic Data Access process](https://fivetran.com/docs/security#diagnosticdataaccess).

Fivetran uses Alto Logica to outsource hiring for engineering talent, but Fivetran does not outsource the development; these engineers follow all of Fivetran's controls. They use the same authentication and access control systems as our internal full-time employees (Okta MFA) and follow the same procedures as outlined below.

By default Fivetran personnel do not have access to customer data. In the event a customer has a connection failure and contacts Fivetran Support, Fivetran may need to debug the failure against customer data if other troubleshooting fails. In such an event Fivetran Support would request Diagnostic Data Access where the customer’s admin would need to approve Fivetran access in the Fivetran dashboard.Once access has been approved, the request may be routed to one of Fivetran’s engineering teams that develop the Fivetran connectors to investigate the failure. Fivetran maintains a global development organization with teams located in the United States, Ireland, India, the Netherlands, and Serbia. Which team the issue is routed to will depend on the connector that has the customer issue to resolve the failure as quickly as possible. This debugging environment is tightly controlled and activity is monitored by Fivetran’s Security team. Access is automatically revoked after 21 days or when the customer disables Diagnostic Data Access in their dashboard.

Additionally, for customers that cannot have data access from countries outside of the United States, Fivetran offers U.S. only support for an additional cost.

Fivetran uses a single sign-on (SSO) service to manage access control and permission provisioning, based on user role within the organization. Role-based access is established through Fivetran’s single sign-on providers which is integrated with Fivetran’s Human Resources system. Employee role assignments are automatically updated when employment is terminated or departments/roles change. In addition, Fivetran performs quarterly user access reviews of access to customer facing systems.

May 2025
#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_3)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Alto Logica LLC. | Professional services and support use cases | Global |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Axiata Digital & Analytics Sdn Bhd (dba ADA Asia, which acquired dhiOmics Analytics) | Development and support use cases | India, Southeast Asia |
| Danube Data Labs LLC. | Professional services and support use cases | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| HCL Technologies Limited (doing business as HCLTech, acquired Starschema Inc.) | Professional services and support use cases | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| phData Inc | Professional services | US, India |

#### AI Subprocessors[](https://fivetran.com/docs/privacy#aisubprocessors_3)

This section is only applicable if you use our AI product(s).

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| OpenAI, LLC | Development and support use cases | Global |
| Cohere Inc. | Development and support use cases | Global (US, UK, and Canada) |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_3)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Canada Inc. | Fivetran affiliate company | Canada |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Novi Sad | Fivetran affiliate company | Serbia |
| Fivetran Japan KK | Fivetran affiliate company | Japan |

### Access[](https://fivetran.com/docs/privacy#access_3)

Neither Fivetran nor our subprocessors are able to access your customer data without [your explicit approval](https://fivetran.com/docs/privacy#pipelinedatasubprocessors).

HCL Technologies Limited and Grid Dynamics Holdings, Inc. (DAXX) are both utilized to support Fivetran's HVR and HVA products. They do not have access to customer data by default and would only have access with the explicit authorization of the customer through a Support case using our standard [Diagnostic Data Access process](https://fivetran.com/docs/security#diagnosticdataaccess).

Fivetran uses Alto Logica to outsource hiring for engineering talent, but Fivetran does not outsource the development; these engineers follow all of Fivetran's controls. They use the same authentication and access control systems as our internal full-time employees (Okta MFA) and follow the same procedures as outlined below.

By default Fivetran personnel do not have access to customer data. In the event a customer has a connection failure and contacts Fivetran Support, Fivetran may need to debug the failure against customer data if other troubleshooting fails. In such an event Fivetran Support would request Diagnostic Data Access where the customer’s admin would need to approve Fivetran access in the Fivetran dashboard. Once access has been approved, the request may be routed to one of Fivetran’s engineering teams that develop the Fivetran connectors to investigate the failure. Fivetran maintains a global development organization with teams located in the United States, Ireland, India, the Netherlands, and Serbia. Which team the issue is routed to will depend on the connector that has the customer issue to resolve the failure as quickly as possible. This debugging environment is tightly controlled and activity is monitored by Fivetran’s Security team. Access is automatically revoked after 21 days or when the customer disables Diagnostic Data Access in their dashboard.

Additionally, for customers that cannot have data access from countries outside of the United States, Fivetran offers U.S. only support for an additional cost.

Fivetran uses a single sign-on (SSO) service to manage access control and permission provisioning, based on user role within the organization. Role-based access is established through Fivetran’s single sign-on providers which is integrated with Fivetran’s Human Resources system. Employee role assignments are automatically updated when employment is terminated or departments/roles change. In addition, Fivetran performs quarterly user access reviews of access to customer facing systems.

December 2024
#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_4)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Alto Logica LLC. | Professional services and support use cases | Global |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Axiata Digital & Analytics Sdn Bhd (dba ADA Asia, which acquired dhiOmics Analytics) | Development and support use cases | India, Southeast Asia |
| Danube Data Labs LLC. | Professional services | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| HCL Technologies Limited (doing business as HCLTech, acquired Starschema Inc.) | Professional services and support use cases | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| phData Inc | Professional services | US, India |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_4)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Canada Inc. | Fivetran affiliate company | Canada |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Beograd | Fivetran affiliate company | Serbia |
| Fivetran Japan KK | Fivetran affiliate company | Japan |

### Access[](https://fivetran.com/docs/privacy#access_4)

Neither Fivetran nor our subprocessors are able to access your customer data without [your explicit approval](https://fivetran.com/docs/privacy#pipelinedatasubprocessors).

HCL Technologies Limited and Grid Dynamics Holdings, Inc. (DAXX) are both utilized to support Fivetran's HVR and HVA products. They do not have access to customer data by default and would only have access with the explicit authorization of the customer through a Support case using our standard [Diagnostic Data Access process](https://fivetran.com/docs/security#diagnosticdataaccess).

Fivetran uses Alto Logica to outsource hiring for engineering talent, but Fivetran does not outsource the development; these engineers follow all of Fivetran's controls. They use the same authentication and access control systems as our internal full-time employees (Okta MFA) and follow the same procedures as outlined below.

By default Fivetran personnel do not have access to customer data. In the event a customer has a connection failure and contacts Fivetran Support, Fivetran may need to debug the failure against customer data if other troubleshooting fails. In such an event Fivetran Support would request Diagnostic Data Access where the customer’s admin would need to approve Fivetran access in the Fivetran dashboard.Once access has been approved, the request may be routed to one of Fivetran’s engineering teams that develop the Fivetran connectors to investigate the failure. Fivetran maintains a global development organization with teams located in the United States, Ireland, India, the Netherlands, and Serbia. Which team the issue is routed to will depend on the connector that has the customer issue to resolve the failure as quickly as possible. This debugging environment is tightly controlled and activity is monitored by Fivetran’s Security team. Access is automatically revoked after 21 days or when the customer disables Diagnostic Data Access in their dashboard.

Additionally, for customers that cannot have data access from countries outside of the United States, Fivetran offers U.S. only support for an additional cost.

Fivetran uses a single sign-on (SSO) service to manage access control and permission provisioning, based on user role within the organization. Role-based access is established through Fivetran’s single sign-on providers which is integrated with Fivetran’s Human Resources system. Employee role assignments are automatically updated when employment is terminated or departments/roles change. In addition, Fivetran performs quarterly user access reviews of access to customer facing systems.

September 2024
#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_5)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Alto Logica LLC. | Professional services and support use cases | Global |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| phData Inc | Professional services | US, India |
| Starschema Inc. | Professional services and support use cases | Global |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_5)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Canada Inc. | Fivetran affiliate company | Canada |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Beograd | Fivetran affiliate company | Serbia |

### Access[](https://fivetran.com/docs/privacy#access_5)

Neither Fivetran nor our subprocessors are able to access your customer data without [your explicit approval](https://fivetran.com/docs/privacy#pipelinedatasubprocessors).

Starschema Inc. and Grid Dynamics Holdings, Inc. (DAXX) are both utilized to support Fivetran's HVR and HVA products. They do not have access to customer data by default and would only have access with the explicit authorization of the customer through a Support case using our standard [Diagnostic Data Access process](https://fivetran.com/docs/security#diagnosticdataaccess).

Fivetran uses Alto Logica to outsource hiring for engineering talent, but Fivetran does not outsource the development; these engineers follow all of Fivetran's controls. They use the same Authentication and Access control systems as our internal full-time employees (Okta MFA) and follow the same procedures as outlined below.

By default Fivetran personnel do not have access to customer data. In the event a customer has a connection failure and contacts Fivetran Support, Fivetran may need to debug the failure against customer data if other troubleshooting fails. In such an event Fivetran Support would request Diagnostic Data Access where the customer’s admin would need to approve Fivetran access in the Fivetran dashboard.Once access has been approved, the request may be routed to one of Fivetran’s engineering teams that develop the Fivetran connectors to investigate the failure. Fivetran maintains a global development organization with teams located in the United States, Ireland, India, Amsterdam, and Serbia. Which team the issue is routed to will depend on the connector that has the customer issue to resolve the failure as quickly as possible. This debugging environment is tightly controlled and activity is monitored by Fivetran’s Security team. Access is automatically revoked after 21 days or when the customer disables Diagnostic Data Access in their dashboard.

Additionally, for customers that cannot have data access from countries outside of the United States, Fivetran offers U.S. only support for an additional cost.

Fivetran uses a single sign-on (SSO) service to manage access control and permission provisioning, based on user role within the organization. Role-based access is established though Fivetran’s single sign-on providers which is integrated with Fivetran’s HR system. Employee role assignments are automatically updated when employment is terminated or departments/roles change. In addition, Fivetran performs quarterly user access reviews of access to customer facing systems.

February 2024 - Census Subprocessors List
List of Subprocessors[](https://fivetran.com/docs/privacy#listofsubprocessors)
------------------------------------------------------------------------------

_Last updated: February 26th, 2024_

To support delivery of our Services, Sutro Labs Inc. (dba Census) (“ Census”) may engage and use data processors with access to Customer Data (each, a "Subprocessor"). This page provides important information about the identity, location and role of each Subprocessor.

The Data Subprocessors that Census utilizes can be categorized into two sets:

### Core Data Subprocessors[](https://fivetran.com/docs/privacy#coredatasubprocessors)

| Entity Name | Subprocessing Activity | Entity Country |
| --- | --- | --- |
| Amazon Web Services, Inc. | Cloud Service Provider | USA or EU as selected by customers |
| Google, Inc. | Cloud Service Provider | USA or EU as selected by customers |

### Support Data Subprocessors[](https://fivetran.com/docs/privacy#supportdatasubprocessors)

| Entity Name | Subprocessing Activity | Entity Country |
| --- | --- | --- |
| Channeled | Customer support | United States |
| Chilipiper | Customer support | United States |
| Clearbit | Marketing analytics | United States |
| Datadog | Cloud monitoring | United States |
| Dropbox | Cloud storage | United States |
| FullStory | Customer support | United States |
| Google Workspace | Email, file storage | United States |
| HelpScout | Customer support | United States |
| Hubspot | Customer relationship management | United States |
| Intercom | Customer support | United States |
| Mailgun | Transaction email provider | United States |
| PandaDoc | E-signature platform | United States |
| Posthog | Product analytics | United States |
| salesforce.com, inc. (Heroku) | Cloud Service Provider | United States |
| Segment | Customer Data Platform | United States |
| Slack | Customer support | United States |
| Snowflake Inc. | Data storage and analytics | United States |
| Stripe | Payment processor | United States |
| Zoom | Video conferencing provider | United States |
| Zendesk | Customer support | United States |
| Chameleon | Product Tours and Analytics | United States |

### Updates[](https://fivetran.com/docs/privacy#updates)

As our business grows and evolves, the Subprocessors we engage may also change. We will endeavor to provide the owner of Customer’s account with notice of any new Subprocessors to the extent required under the Agreement, along with posting such updates here. Please check back frequently for updates.

January 2023
#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_6)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| Starschema Inc. | Professional services and support use cases | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |
| Alto Logica LLC. | Professional services and support use cases | Global |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_6)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| HVR Software BV | Fivetran affiliate company | Netherlands |
| Ogranak HVR Software BV – Fivetran Beograd | Fivetran affiliate company | Serbia |

September 2022
#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_7)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | Global |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | Global |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |
| Starschema Inc. | Professional services and support use cases | Global |
| Grid Dynamics Holdings, Inc. (DAXX) | Professional services and support use cases | Global |

#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_7)

Fivetran Inc. maintains affiliate companies in countries where our full-time employees work.Each of these affiliate companies comprises members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Germany GmbH | Fivetran affiliate company | Germany |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |
| HVR Software BV | Fivetran affiliate company | Netherlands |

August 2021
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_8)

Fivetran Inc. maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Kaluga Branch | Branch Office of Fivetran Inc. in Kaluga | Russia |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_8)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | Global |
| Marketo, Inc. | Tool used to conduct email marketing activities | Global |
| SalesLoft, Inc. | Tool used to conduct email marketing activities | Global |
| Stripe, Inc. | Credit card payments | Global |

May 2021
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_9)

Fivetran, Inc maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Kaluga Branch | Branch Office of Fivetran Inc. in Kaluga | Russia |
| Fivetran UK Limited | Fivetran affiliate company | United Kingdom |
| Fivetran Data Australia Pty Ltd | Fivetran affiliate company | Australia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_9)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation_1)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | Global |
| Marketo, Inc. | Tool used to conduct email marketing activities | Global |
| SalesLoft, Inc. | Tool used to conduct email marketing activities | Global |
| Stripe, Inc. | Credit card payments | Global |

November 2020
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_10)

Fivetran, Inc maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Kaluga Branch | Branch Office of Fivetran Inc. in Kaluga | Russia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_10)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | Global |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation_2)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | Global |
| Marketo, Inc. | Tool used to conduct email marketing activities | Global |
| SalesLoft, Inc. | Tool used to conduct email marketing activities | Global |
| Stripe, Inc. | Credit card payments | Global |

August 2020
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_11)

Fivetran, Inc maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Kaluga Branch | Branch Office of Fivetran Inc. in Kaluga | Russia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_11)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | United States, and Europe |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation_3)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | United States, Ireland |
| Sendgrid, Inc. | Email distribution services for service-related notifications | United States, Ireland |
| SalesLoft, Inc. | Tool used to conduct email marketing activities | United States |
| Stripe, Inc. | Credit card payments | United States |

June 2020
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_12)

Fivetran, Inc maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Fivetran Kaluga Branch | Branch Office of Fivetran Inc. in Kaluga | Russia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_12)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | United States, and Europe |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation_4)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | United States, Ireland |
| Sendgrid, Inc. | Email distribution services for service-related notifications | United States, Ireland |
| SalesLoft, Inc. | Tool used to conduct email marketing activities | United States |

June 2019
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_13)

Fivetran, Inc maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Tabalin, Inc | Fivetran affiliate company | Russia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_13)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | United States, and Europe |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation_5)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | United States, Ireland |
| Sendgrid, Inc. | Email distribution services for service-related notifications | United States, Ireland |
| SalesLoft, Inc. | Tool used to conduct email marketing activities | United States |

April 2019
#### Affiliates[](https://fivetran.com/docs/privacy#affiliates_14)

Fivetran, Inc maintains affiliate companies in countries where our full time employees work.Each of these affiliate companies are comprised of full members of the Fivetran team who contribute from outside the United States.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |
| Tabalin, Inc | Fivetran affiliate company | Russia |

#### Pipeline Data Subprocessors[](https://fivetran.com/docs/privacy#pipelinedatasubprocessors_14)

These are subprocessors who have access to Fivetran production systems and data by virtue of the services they provide.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | United States, and Europe |
| Microsoft, Inc. | Azure hosting environment for Supplier services | United States |
| Okta, Inc. | Authentication and authorization for Fivetran employees | Global |

#### Fivetran Customer Information[](https://fivetran.com/docs/privacy#fivetrancustomerinformation_6)

These are subprocessors who may have access to PII (such as full name, email, and billing information) related to active Fivetran customers or potential customers, but have no access to connection data.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | United States, Ireland |
| Sendgrid, Inc. | Email distribution services for service-related notifications | United States, Ireland |
| Outreach | Email distribution services for service and non service-related notifications | United States, Ireland |

October 2018
Fivetran, Inc. (“Fivetran”) uses certain subprocessors to assist it in providing the Fivetran Services as described in the [Terms of Service ("TOS")](https://fivetran.com/terms).Defined terms used herein shall have the same meaning as defined in the TOS.

#### What is a Subprocessor?[](https://fivetran.com/docs/privacy#whatisasubprocessor_2)

A subprocessor is a third-party data processor engaged by Fivetran, including entities from within the Fivetran Group, who has or potentially will have access to or process Customer Data (which may contain personal data). Fivetran engages different types of subprocessors to perform various functions as explained in the tables below. Fivetran refers to third parties that do not have access to or process Service Data but who are otherwise used to provide the Services as “subcontractors” and not subprocessors.

| Name | Nature of Processing | Territory(ies) |
| --- | --- | --- |
| Amazon, Inc. | AWS hosting environment for Supplier services | United States |
| Google, Inc. | Google Cloud hosting environment for Supplier services | United States |
| Salesforce, Inc. | Chat support for services; CRM for Supplier’s business | United States |
| Sendgrid, Inc. | Email distribution services for service-related notifications | United States |
| Outreach | Email distribution services for service and non service-related notifications | United States |
| Fivetran Data Pipeline, Limited | Fivetran affiliate company | Ireland |
| Fivetran India Pvt. Limited | Fivetran affiliate company | India |

* * *

Questions[](https://fivetran.com/docs/privacy#questions)
--------------------------------------------------------

Ensuring our platform is built with privacy is vital to earning and maintaining our customers’ trust. As a leader in automated data integration, we strive to keep Fivetran easy to use while keeping privacy top of mind. To learn more about Fivetran, contact our sales team at sales@fivetran.com. To report a privacy concern, email us at [privacy@fivetran.com](mailto:privacy@fivetran.com) or [DPO@fivetran.com](mailto:DPO@fivetran.com).

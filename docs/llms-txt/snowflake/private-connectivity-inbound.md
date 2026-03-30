# Source: https://docs.snowflake.com/en/user-guide/opencatalog/private-connectivity-inbound.md

# Source: https://docs.snowflake.com/en/user-guide/private-connectivity-inbound.md

# Private connectivity for inbound network traffic

Your connection to Snowflake can be routed over the public Internet or through a private IP address associated with the cloud platform that
hosts your Snowflake account. By using your cloud platform’s private connectivity solution to create private endpoints, you can harden your
security posture so that inbound network traffic uses private connectivity when accessing the following features:

* To the Snowflake Service
* To Snowsight
* To Streamlit in Snowflake
* To internal stages
* To Snowpark Container Services
* To Snowflake Intelligence

## To the Snowflake Service

When the routing is through a private IP address *from your VPC or VNET to the Snowflake VPC or VNet*, that is *private
connectivity to the Snowflake Service*. These connections use [AWS PrivateLink](admin-security-privatelink.md),
[Azure Private Link](privatelink-azure.md), or
[Google Cloud Private Service Connect](private-service-connect-google.md). The service depends on the cloud platform that
hosts your Snowflake account.

## To Snowsight

To use private connectivity to access Snowsight, see [Configuring private connectivity for Snowsight](ui-snowsight-gs.md).

After private connectivity is configured, users can [sign in using private connectivity](ui-snowsight-gs.md).

## To Streamlit in Snowflake

To access Streamlit in Snowflake with AWS PrivateLink, Azure Private Link, or Google Cloud Private Service Connect, see [Private connectivity for Streamlit in Snowflake](../developer-guide/streamlit/object-management/privatelink.md).

## To internal stages

You can use private connectivity to connect to Snowflake internal stages. For information, see the following:

* [AWS VPC interface endpoints for internal stages](private-internal-stages-aws.md)
* [Azure private endpoints for internal stages](private-internal-stages-azure.md)
* [Google Private Service Connect endpoints for internal stages](private-internal-stages-gcp.md)

## To Snowpark Container Services

You can use private connectivity to connect to Snowpark Container Services. For information, see [Inbound connectivity](../developer-guide/snowpark-container-services/private-connectivity.md).

## To Snowflake Intelligence

You can use private connectivity to connect to Snowflake Intelligence. For information, see [Configure Snowflake Intelligence with private connectivity](snowflake-cortex/snowflake-intelligence/deploy-agents.md).

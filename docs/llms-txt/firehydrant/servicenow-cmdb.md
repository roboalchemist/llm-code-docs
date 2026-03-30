# Source: https://docs.firehydrant.com/docs/servicenow-cmdb.md

# ServiceNow CMDB

Integrating ServiceNow CMDB with FireHydrant streamlines service management by maintaining synchronized service records across both platforms. This integration eliminates manual data entry, reduces discrepancies, and provides a single source of truth for your service inventory. Teams can quickly link CMDB items to FireHydrant incidents while automated updates keep service dependencies and relationships current, ensuring consistent and accurate service information for all users.

## Prerequisites

Follow the instructions for setting up [ServiceNow integration](https://docs.firehydrant.com/docs/servicenow-integration), ensuring at least one service table is added. **If you did not add a service table at initial setup, you will need to uninstall/reinstall the integration.**

## Using the FireHydrant CMDB integration

Once you've configured your Service tables during initial setup, FireHydrant will automatically begin importing the services in the tables you've added.

FireHydrant does an initial sync when you set up the integration, and thereafter will resync the FireHydrant catalog with ServiceNow's CMDB tables **once per hour**.

* Any new services in SNOW CMDB tables are automatically created in FireHydrant
* Any changes to existing services' names in SNOW CMDB will replicate changes to the same service in FireHydrant

## Important Notes/Behaviors

* Currently, the ServiceNow CMDB sync is one-way - changes made in FireHydrant will not replicate back to SNOW, including creation, update, and deletion of services in FireHydrant.
* Only the names of the services are sync'd to the linked services in FireHydrant.
* Any services that have blank or empty names in ServiceNow will not be sync'd to FireHydrant.

## Next Steps

* Learn more about [FireHydrant's Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)
* See an [overview of all FireHydrant integrations](https://docs.firehydrant.com/docs/integrations-overview)
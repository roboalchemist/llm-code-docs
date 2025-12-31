# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md.txt

Interface representing a Data Connect connector configuration.

**Signature:**  

    export interface ConnectorConfig 

## Properties

|                                                                  Property                                                                  |  Type  |               Description                |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------|
| [connector](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md#connectorconfigconnector) | string | Name of the Data Connect connector.      |
| [location](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md#connectorconfiglocation)   | string | Location ID of the Data Connect service. |
| [serviceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md#connectorconfigserviceid) | string | Service ID of the Data Connect service.  |

## ConnectorConfig.connector

Name of the Data Connect connector.

**Signature:**  

    connector?: string;

## ConnectorConfig.location

Location ID of the Data Connect service.

**Signature:**  

    location: string;

## ConnectorConfig.serviceId

Service ID of the Data Connect service.

**Signature:**  

    serviceId: string;
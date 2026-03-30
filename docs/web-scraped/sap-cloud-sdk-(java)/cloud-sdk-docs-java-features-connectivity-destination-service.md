# Source: https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service

Title: Connectivity Features | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service

Markdown Content:
The SAP Cloud SDK offers a variety of connectivity features that help to connect to systems and services. At its core, the SAP Cloud SDK uses [`Destination` objects](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#accessing-destinations) as an abstraction of (remote) services.

Ultimately, a `Destination` will be converted into an [HTTP Client](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client) that can be used to actually send requests to the target. Hereby, the SAP Cloud SDK supports both cloud and [on-premise targets](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/on-premise).

Furthermore, the SAP Cloud SDK also offers various means of running and testing applications that use these connectivity features [in non-productive environments](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/running-locally), such as in an CI/CD pipeline. That way, you are well equipped to develop robust and reliable applications.

Accessing Destinations[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#accessing-destinations "Direct link to Accessing Destinations")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A **destination** is an abstraction of a real system or service that applications may want to connect to. It is a representation of the connection details, such as the URL, authentication, proxy settings, and HTTP headers. The **destination** concept is an integral part of the SAP Cloud SDK for Java.

The SAP Cloud SDK offers APIs to load destinations from following sources:

*   From the [BTP Destination Service on Cloud Foundry](https://api.sap.com/api/SAP_CP_CF_Connectivity_Destination/overview).
    *   Via the [`DestinationAccessor` API](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/btp-destination-service)

*   From [Service Bindings](https://github.com/SAP/btp-environment-variable-access/wiki/Fundamentals#service-binding).
    *   Via the [`ServiceBindingDestinationLoader` API](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/service-bindings)

*   From existing `Destination` objects.
    *   Via the [`DefaultHttpDestination` API](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-destinations)

Using Destinations[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#using-destinations "Direct link to Using Destinations")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Once a [`Destination`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/connectivity/Destination.html) has been retrieved, it can be used to connect to the system or service it represents. This is done by converting the given `Destination` into an HTTP client, which is then used to send requests to the system or service.

### For OData and OpenApi Services[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#for-odata-and-openapi-services "Direct link to For OData and OpenApi Services")

While the `Destination` to HTTP client conversion [can be done explicitly](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#for-other-services) to connect to any system or service, the SAP Cloud SDK provides convenient integrations in generated [OData](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator) and [OpenApi](https://sap.github.io/cloud-sdk/docs/java/features/rest/generate-rest-client) clients.

*   OData V4 Example
*   OData V2 Example
*   OpenApi Example

`Destination myDestination;SomeODataV4Service myService;var serviceResponse = myService.getAllEntities().execute(myDestination);`

When running code as above, the SAP Cloud SDK internally takes care of converting the provided `Destination` into a suitable HTTP client. This process is fully transparent to the user and has proven to be sufficient for almost all use cases.

### For Other Services[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#for-other-services "Direct link to For Other Services")

If the [above approach](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#for-odata-and-openapi-services) is not applicable, the `Destination` to HTTP client conversion can be done explicitly as [described here](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client).

### To Read Its Configuration[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/destination-service#to-read-its-configuration "Direct link to To Read Its Configuration")

A `Destination` consists of a set of properties that describe the connection details of the represented system or service. These properties can be read from the `Destination` object as follows:

`Destination myDestination;String destinationName = myDestination.get(DestinationProperty.NAME).getOrElse("");`

Reading those properties is most useful when a `Destination` is retrieved [from the BTP Destination Service](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/btp-destination-service), as it allows to read the properties that have been provided by a user via the BTP Cockpit.

Please refer to [this documentation](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/btp-destination-service#if-authentication-is-not-required) for more details.

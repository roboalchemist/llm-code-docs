# Source: https://ocelot.readthedocs.io/en/latest/features/servicefabric.html

Title: Service Fabric — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/servicefabric.html

Markdown Content:
If you have services deployed in Azure [Service Fabric](https://azure.microsoft.com/en-us/products/service-fabric/) you will normally use the naming service to access them.

This feature allows to set up a route that will work in [Service Fabric](https://azure.microsoft.com/en-us/products/service-fabric/).

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#configuration "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

The most important thing is the `ServiceName`, which is composed of the [Service Fabric](https://azure.microsoft.com/en-us/products/service-fabric/) application name followed by the specific service name. Additionally, the `ServiceDiscoveryProvider` needs to be configured in `GlobalConfiguration`. The example below demonstrates a typical configuration. It assumes that _Service Fabric_ is running on `localhost` and that the naming service is using port `19081`.

> The example below is taken from the [Sample](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#sf-sample), so please check it if this doesn’t make sense!

{
 "Routes": [
 {
 "DownstreamScheme": "http",
 "DownstreamPathTemplate": "/api/values",
 "UpstreamPathTemplate": "/EquipmentInterfaces",
 "UpstreamHttpMethod": [ "Get" ],
 "ServiceName": "OcelotServiceApplication/OcelotApplicationService" }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "RequestIdKey": "Oc-RequestId",
 "ServiceDiscoveryProvider": {
 "Host": "localhost",
 "Port": 19081,
 "Type": "ServiceFabric" }
 }
}

If you are using stateless or guest exe services, Ocelot can proxy through the naming service without requiring additional configuration. However, if you are using stateful or actor services, you must include the `PartitionKind` and `PartitionKey` query string values in the client request, e.g.,

> GET `http://ocelot.com/EquipmentInterfaces?PartitionKind=xxx&PartitionKey=xxx`

There is no way for Ocelot to determine these values automatically.

Placeholders [[2]](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#placeholders "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Ocelot, _placeholders_ for variables can be inserted into the `UpstreamPathTemplate` and `ServiceName` using the format `{something}`.

> **Note**: The _placeholder_ variable must exist in both the `DownstreamPathTemplate` (or `ServiceName`) and the `UpstreamPathTemplate`. Specifically, the `UpstreamPathTemplate` must include all _placeholders_ found in the `DownstreamPathTemplate` and `ServiceName`. Failure to meet this requirement will prevent Ocelot from starting due to validation errors, which are logged.

Once the validation stage is completed, Ocelot replaces the placeholder values in the `UpstreamPathTemplate` with those from the `DownstreamPathTemplate` and/or `ServiceName` for each processed request. Thus, the _Service Fabric_[Placeholders 2](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#sf-placeholders) feature operates similarly to the original routing [Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-placeholders) feature but includes the `ServiceName` property in its processing.

Here is an example of the `version` variable in the _Service Fabric_ service name.

{
 "Routes": [
 {
 "UpstreamPathTemplate": "/api/{version}/{endpoint}",
 "DownstreamPathTemplate": "/{endpoint}",
 "ServiceName": "Service_{version}/Api", }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.com",
 "ServiceDiscoveryProvider": {
 "Host": "localhost",
 "Port": 19081,
 "Type": "ServiceFabric" }
 }
}

When you make Ocelot request:

*   `GET https://ocelot.com/api/1.0/products`

The _Service Fabric_ request will be:

*   `GET http://localhost:19081/Service_1.0/Api/products`

Sample[¶](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#sample "Link to this heading")
------------------------------------------------------------------------------------------------------------

In order to introduce the _Service Fabric_ feature, we have prepared a sample:

This solution includes the following projects:

*   `Ocelot.Samples.ServiceFabric.ApiGateway.csproj`

*   `Ocelot.Samples.ServiceFabric.DownstreamService.csproj`

Complete instructions for running this solution can be found in the [README.md](https://github.com/ThreeMammals/Ocelot/blob/main/samples/ServiceFabric/README.md) file.

Note

Please consider this solution as a demonstration of integration; it is outdated as of 2025. Therefore, this solution is a draft and requires further development for practical usage and deployment in the Azure cloud. Additionally, refer to the team’s notes in the [Service Fabric](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#sd-service-fabric) section!

* * *

# Source: https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client

Title: Use the HttpClient Accessor To Configure Requests To Remote Services | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client

Published Time: Fri, 27 Feb 2026 15:35:45 GMT

Markdown Content:
The SAP Cloud SDK offers basic functionality that helps with connecting to other systems and services like SAP S/4HANA Cloud or On-premise edition. The SAP Cloud SDK leverages the existing API of `HttpClient` and applies conveniently managed properties, e.g. according to a specific destination configuration. In the following paragraphs, the `HttpClientAccessor` API and its usage will be described.

General Usage[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client#general-usage "Direct link to General Usage")
------------------------------------------------------------------------------------------------------------------------------------------

In general an `HttpClient` can be instantiated through the `HttpClientAcessor`. The SAP Cloud SDK itself uses the accessor class for all internal requests as well.

*   Apache Version 4.x
*   Apache Version 5.x

To make use the `HttpClientAccessor`, make sure to include the [cloudplatform-connectivity](https://central.sonatype.com/artifact/com.sap.cloud.sdk.cloudplatform/cloudplatform-connectivity) dependency in your project.

`HttpClient client = HttpClientAccessor.getHttpClient();`

If you need an `HttpClient` to reach a system that has been configured as a Destination (e.g. an SAP S/4HANA system), you may first fetch the destination and then use it as a argument for the accessor:

`Destination destination = DestinationAccessor.getDestination("my-destination");HttpClient client = HttpClientAccessor.getHttpClient(destination);`

When using a destination, the configured destination URL will be used as base path for the subsequent requests for `client`.

note

Please note that similar to other accessor-based APIs, the SAP Cloud SDK offers methods with a `try` prefix to allow for optional VAVR-enhanced API access.

Customization[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client#customization "Direct link to Customization")
------------------------------------------------------------------------------------------------------------------------------------------

When the properties of `HttpClient` are not working for the application, e.g. timeout is too short or too long, then the generation can be customized.

### Configuring the Cache[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client#configuring-the-cache "Direct link to Configuring the Cache")

HTTP Clients are reused to ensure existing connections can be reused for better performance. By default, clients are **cached for at least one hour**. Cache entries are only removed once the http client hasn't been accessed for one hour. This can be configured to allow for better performance.

*   Apache Version 4.x
*   Apache Version 5.x

`DefaultHttpClientCache cache = new DefaultHttpClientCache(1, TimeUnit.DAYS);HttpClientAccessor.setHttpClientCache(cache);`

Implications for Cookies

Cookies are maintained per `HttpClient` object. Once a new client is created (for a destination) cookies from previous requests will no longer be available.

We generally recommend to keep the cache duration for HTTP clients longer or equal to the cache duration of destinations.

### Configuring the Clients[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client#configuring-the-clients "Direct link to Configuring the Clients")

Please find the `HttpClientFactory` interface. They offer a similar method `createHttpClient` with optional destination argument:

*   Apache Version 4.x
*   Apache Version 5.x

`HttpClientFactory factory = new DefaultHttpClientFactory();HttpClient genericClient = factory.createHttpClient();HttpClient destinationClient = factory.createHttpClient(destination);`

The `DefaultHttpClientFactory` type offers a static builder, to enable custom properties for:

*   `timeoutMilliseconds`
*   `maxConnectionsPerRoute`
*   `maxConnectionsTotal`

`HttpClientFactory customFactory = DefaultHttpClientFactory.builder()  .timeoutMilliseconds(60000)  .maxConnectionsPerRoute(100)  .maxConnectionsTotal(200)  .build();`

When inheriting from `DefaultHttpClientFactory` it's possible to provide even deeper customization:

`DefaultHttpClientFactory customFactory = new DefaultHttpClientFactory() {  @Override  protected RequestConfig.Builder getRequestConfigBuilder( HttpDestinationProperties destination ) {    return super.getRequestConfigBuilder(destination)      .setProxy(new HttpHost("proxy", 8080, "http"));  }  @Override  protected HttpClientBuilder getHttpClientBuilder( HttpDestinationProperties destination ) {    return super.getHttpClientBuilder(destination)      .setUserAgent("SDK");  }};`

It is possible to take advantage of calls to `super` - or use your own objects directly. This inheritance enables custom implementation for the following methods:

*   `getHttpClientBuilder`
*   `getRequestConfigBuilder`
*   `getSocketConfigBuilder`
*   `getConnectionManager`

Overriding Default Behavior[​](https://sap.github.io/cloud-sdk/docs/java/features/connectivity/http-client#overriding-default-behavior "Direct link to Overriding Default Behavior")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now the customization of the HTTP client factory is available and we can adjust the default behavior for the accessor:

*   Apache Version 4.x
*   Apache Version 5.x

`HttpClientFactory factory = new MyCustomHttpClientFactory();HttpClientAccessor.setHttpClientFactory(factory);`

From now on the custom factory will be used for every explicit and implicit HTTP request running through the SAP Cloud SDK.

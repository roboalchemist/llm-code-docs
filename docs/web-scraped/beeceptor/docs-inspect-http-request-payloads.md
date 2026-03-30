# Source: https://beeceptor.com/docs/inspect-http-request-payloads/

Title: Inspect HTTP requests | Beeceptor

URL Source: https://beeceptor.com/docs/inspect-http-request-payloads/

Markdown Content:
Inspect HTTP requests | Beeceptor
===============

[Skip to main content](https://beeceptor.com/docs/inspect-http-request-payloads/#__docusaurus_skipToContent_fallback)

[![Image 2: Beeceptor-Logo](https://cdn.beeceptor.com/assets/images/logo.svg)](https://beeceptor.com/)

⌘K

[Create an Endpoint](https://beeceptor.com/)[Features](https://beeceptor.com/use-cases/)[Documentation](https://beeceptor.com/docs/beeceptor-features/)

[Sign in](https://beeceptor.com/docs/inspect-http-request-payloads/#)

*   [Beeceptor Feature Documentation](https://beeceptor.com/docs/beeceptor-features/) 
    *   [Create An Endpoint](https://beeceptor.com/docs/create-endpoint/)
    *   [Inspect HTTP requests](https://beeceptor.com/docs/inspect-http-request-payloads/)
    *   [Mock Rules & API Routes](https://beeceptor.com/docs/mock-rules/) 
        *   [Mock Rules & Request Matching](https://beeceptor.com/docs/create-mocking-server/)
        *   [Request Matching Filters (Advanced)](https://beeceptor.com/docs/request-matching-filters/)
        *   [CRUD Routes](https://beeceptor.com/docs/crud-api/)
        *   [HTTP Callout Rule](https://beeceptor.com/docs/proxy-rule-http-callout/)
        *   [Execution Order](https://beeceptor.com/docs/mock-rules-priority-order/)

    *   [Template Engine](https://beeceptor.com/docs/template-engine/) 
        *   [Reuse Request Data](https://beeceptor.com/docs/parameterized-dynamic-response-payload-using-request-header/)
        *   [Mocking SOAP Services](https://beeceptor.com/docs/soap-services-dynamic-operation-response/)
        *   [Generate Fake Data](https://beeceptor.com/docs/dummy-random-data-generation-during-mock/)
        *   [Generate Fake Data - Common Examples](https://beeceptor.com/docs/dummy-data-generation-examples/)
        *   [Locale for Test Data](https://beeceptor.com/docs/localized-data-generation/)
        *   [Control Flow Constructs (logic)](https://beeceptor.com/docs/template-advance-constructs/)
        *   [Handling Arrays with Template Engine](https://beeceptor.com/docs/template-array-usage/)
        *   [Stateful Mocks](https://beeceptor.com/docs/template-stateful-mocks/)
        *   [Arithmetic Operators](https://beeceptor.com/docs/template-arithmetic-operators/)
        *   [String Operators](https://beeceptor.com/docs/template-string-operators/)
        *   [Date Operators](https://beeceptor.com/docs/template-date-operators/)
        *   [Array/List Operators](https://beeceptor.com/docs/template-array-operators/)
        *   [Comparison Operators](https://beeceptor.com/docs/template-comparison-operators/)
        *   [Miscellaneous Operators](https://beeceptor.com/docs/template-miscellaneous-operators/)
        *   [All Operators](https://beeceptor.com/docs/template-operators/)

    *   [Protocols](https://beeceptor.com/docs/protocols-supported/) 
        *   [Rest API server from OpenAPI Spec](https://beeceptor.com/docs/oas-json-file-create-mock-server/)
        *   [GraphQL server from SDL](https://beeceptor.com/docs/graphql-mock-server/)
        *   [SOAP server from WSDL](https://beeceptor.com/docs/soap-server-from-wsdl/)
        *   [gRPC server from Proto](https://beeceptor.com/docs/grpc-mock-server/)
        *   [Mutual TLS server](https://beeceptor.com/docs/mutual-tls-mtls/)

    *   [Proxying & Intercepting](https://beeceptor.com/docs/forward-proxy-with-mock/)
    *   [Local Tunneling](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/)
    *   [Rate Limits](https://beeceptor.com/docs/rate-limits/)
    *   [Request History](https://beeceptor.com/docs/query-mock-request-history/)
    *   [White Labeled Endpoints](https://beeceptor.com/docs/whitelabel-dummy-api-domain/)
    *   [Stateful Data Management](https://beeceptor.com/docs/mock-data-management/)
    *   [Simulate CORS (Origin Whitelist)](https://beeceptor.com/docs/cors-origin/)
    *   [Response Simulation For Binary Large Objects (BLOB)](https://beeceptor.com/docs/large-binary-response/)
    *   [Sharing Endpoint](https://beeceptor.com/docs/share-and-collaborate/)
    *   [API Connections](https://beeceptor.com/docs/api-connections/)
    *   [Mock Server Security](https://beeceptor.com/docs/security-settings/)
    *   [AI Rules Generator](https://beeceptor.com/docs/ai-assistant/)
    *   [Forward Proxy](https://beeceptor.com/docs/features/forward-proxy/)
    *   [Agentic Mode (MCP)](https://beeceptor.com/docs/mcp-agentic-mode/)
    *   [HTTP Echo Server](https://beeceptor.com/docs/http-echo-service-api/)
    *   [Customize Test Data for OpenAPI Mock Servers](https://beeceptor.com/docs/openapi-mock-server-test-data-generator/)
    *   [Add a “Mock These APIs” Button](https://beeceptor.com/docs/openapi-host-free-button/)
    *   [Beeceptor Error Codes](https://beeceptor.com/docs/error-codes-table/)
    *   [Account Management](https://beeceptor.com/docs/account-management/) 
        *   [Managing Subscriptions And Payments](https://beeceptor.com/docs/manage-subscriptions-and-payments/)
        *   [Enterprise Account Management](https://beeceptor.com/docs/enterprise-subscriptions/)
        *   [Masking HTTP Headers](https://beeceptor.com/docs/masking-headers/)
        *   [IP Whitelisting](https://beeceptor.com/docs/ip-whitelisting-security/)
        *   [Audit Logs](https://beeceptor.com/docs/mock-configuration-audit-logs/)
        *   [Observability (OTLP)](https://beeceptor.com/docs/otlp-observability-tracing/)
        *   [SSO Configuration (SAML)](https://beeceptor.com/docs/saml-sso-configuration/)

*   [Beeceptor API Documentation](https://beeceptor.com/docs/category/beeceptor-api-documentation/) 
*   [API Documentation (V2)](https://beeceptor.com/docs/api/beeceptor-api/) 
*   [Use Cases](https://beeceptor.com/docs/articles/) 
*   [Tutorials](https://beeceptor.com/docs/tutorials/) 
*   [Service Virtualization](https://beeceptor.com/docs/service-virtualization/) 
*   [Building Blocks For Web](https://beeceptor.com/docs/http-building-blocks/) 

*   [](https://beeceptor.com/docs/)
*   [Beeceptor Feature Documentation](https://beeceptor.com/docs/beeceptor-features/)
*   Inspect HTTP requests

On this page

Inspect HTTP requests
=====================

Beeceptor enables you to collect, parse, and view HTTP requests. You can create **named endpoints** and send requests. Use the endpoint's dashboard to inspect headers, request body, query strings, cookies, uploaded files and much more. The dashboard is a real-time log of the requests as they come in.

Inspecting request payload[​](https://beeceptor.com/docs/inspect-http-request-payloads/#inspecting-request-payload "Direct link to Inspecting request payload")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The following demo shows inspecting incoming request's payload and headers. If the request has JSON payload, you can even format the JSON right there. Similarly, on the right side the response parameters can be inspected. Beeceptor by default returns `200` status code if no mocking rule is defined.

Sharing a request[​](https://beeceptor.com/docs/inspect-http-request-payloads/#sharing-a-request "Direct link to Sharing a request")
------------------------------------------------------------------------------------------------------------------------------------

The following demo shows sharing a request with others. You can click on the share icon and give this share a name. This gives you a **permanent link** to share with anyone. The new shareable link/page has request and response payloads and headers.

![Image 3: share-beeceptor-request-url](https://beeceptor.com/docs/assets/images/share-a-request-73359dfca29f3fb3137d7b97f237dedf.gif)

**Tags:**
*   [Features](https://beeceptor.com/docs/tags/features/)

[Previous Create An Endpoint](https://beeceptor.com/docs/create-endpoint/)[Next Mock Rules & API Routes](https://beeceptor.com/docs/mock-rules/)

*   [Inspecting request payload](https://beeceptor.com/docs/inspect-http-request-payloads/#inspecting-request-payload)
*   [Sharing a request](https://beeceptor.com/docs/inspect-http-request-payloads/#sharing-a-request)

[API Documentation](https://beeceptor.com/docs/api/beeceptor-api/)·[Mock Server Catalog](https://beeceptor.com/mock-server/explore/)·[Contact Us](https://app.beeceptor.com/contact)·[FAQ](https://beeceptor.com/faq/)·[Status](https://status.beeceptor.com/)·[Privacy Policy](https://beeceptor.com/pages/privacy/)·[Terms of Service](https://beeceptor.com/pages/terms-of-service/)

© 2026 Beeceptor. All rights reserved.

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api/endpoints-and-response-codes.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/endpoints-and-response-codes.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api/endpoints-and-response-codes.md

# Endpoints and Response Codes

### Endpoints

<table><thead><tr><th width="109">Method</th><th>Endpoint</th><th>Description</th></tr></thead><tbody><tr><td>POST</td><td>https://api.webit.live/api/v1/realtime/serp</td><td>A real time request for a single search term.</td></tr><tr><td>POST</td><td>https://api.webit.live/api/v1/async/serp</td><td>An asynchronous request for a single search term.</td></tr><tr><td>GET</td><td>https://api.webit.live/api/v1/tasks/{Task_ID}</td><td>Check the status of an asynchronous request using a Task ID.</td></tr><tr><td>POST</td><td>https://api.webit.live/api/v1/batch/serp</td><td>An asynchronous request for multiple search terms.</td></tr><tr><td>POST</td><td>https://api.webit.live/api/v1/batches/{batch_id}/progress</td><td>Check the status of a batch request.</td></tr><tr><td>GET</td><td>https://api.webit.live/api/v1/batches/{batch_id}</td><td>Return a summary of a completed batch request.</td></tr></tbody></table>

### **Response Codes**

<table><thead><tr><th width="121">Status</th><th>Description</th></tr></thead><tbody><tr><td>200</td><td>OK</td></tr><tr><td>400</td><td>The requested resource could not be reached</td></tr><tr><td>401</td><td>Unauthorized/invalid credental string</td></tr><tr><td>500</td><td>Internal service error</td></tr><tr><td>501</td><td>An error was encountered by the proxy service</td></tr><tr><td>555</td><td>Request timeout</td></tr></tbody></table>

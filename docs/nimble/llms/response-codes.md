# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/response-codes.md

# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-quick-start-guide/response-codes.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/response-codes.md

# Response codes

In the below tableS, we provide a list of the response codes you may encounter while using Nimble APIs. Our documentation includes all the information needed to ensure you get successful responses every time, but if something unexpected occurs, feel free to reach out to our Customer Success team via Slack or via email at <support@nimbleway.com>.

### Endpoints

<table><thead><tr><th width="107">Method</th><th>Endpoint</th><th>Description</th></tr></thead><tbody><tr><td>POST</td><td>https://api.webit.live/api/v1/realtime/web</td><td>a real time request for a single URL.</td></tr><tr><td>POST</td><td>https://api.webit.live/api/v1/async/web</td><td>an asynchronous request for a single URL.</td></tr><tr><td>GET</td><td>https://api.webit.live/api/v1/tasks/{Task_ID}</td><td>Check the status of an asynchronous request using a Task ID.</td></tr><tr><td>POST</td><td>https://api.webit.live/api/v1/batch/web</td><td>an asynchronous request for multiple URLs.</td></tr><tr><td>POST</td><td>https://api.webit.live/api/v1/batches/{batch_id}/progress</td><td>Check the status of a batch request.</td></tr><tr><td>GET</td><td>https://api.webit.live/api/v1/batches/{batch_id}</td><td>Return a summary of a completed batch request.</td></tr></tbody></table>

### **Response Codes**

| Status | Description                                   |
| ------ | --------------------------------------------- |
| 200    | OK                                            |
| 400    | The requested resource could not be reached   |
| 401    | Unauthorized/invalid credential string        |
| 500    | Internal service error                        |
| 501    | An error was encountered by the proxy service |

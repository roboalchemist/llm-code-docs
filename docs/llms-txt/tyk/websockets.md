# Source: https://tyk.io/docs/advanced-configuration/websockets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Websockets

> How to use websockets in Tyk

As from Tyk gateway v2.2, Tyk supports transparent WebSocket connection upgrades. To enable this feature, set the `enable_websockets` value to `true` in your `tyk.conf` file.

WebSocket proxying is transparent, Tyk will not modify the frames that are sent between client and host, and rate limits are on a per-connection, not per-frame basis.

The WebSocket upgrade is the last middleware to fire in a Tyk request cycle, and so can make use of HA capabilities such as circuit breakers and enforced timeouts.

Tyk needs to decrypt the inbound and re-encrypt the outbound for the copy operations to work, Tyk does not just pass through the WebSocket. When the target is on default SSL port you must explicitly specify the target url for the API:

```{.copyWrapper}  theme={null}
https://target:443/
```

## WebSocket Example

We are going to set up Tyk with a WebSocket proxy using our [Tyk Pro Docker Demo](https://github.com/TykTechnologies/tyk-pro-docker-demo) installation.

We will be using the [Postman WebSocket Echo Service](https://blog.postman.com/introducing-postman-websocket-echo-service/) to test the connection.

**Steps for Configuration**

1. **Setup the API in Tyk**

   Create a new API in Tyk. For this demo we are going to select Open (Keyless) as the **Authentication mode**.

   Set the **Target URL** to `wss://ws.postman-echo.com/raw`

2. **Test the Connection**

   1. From Postman, select **File > New > WebSocket Request** (or from **Workspace > New > WebSocket Request** if using the web based version).

   <img src="https://mintcdn.com/tyk/fZL7TCMxcnOe7SNE/img/dashboard/system-management/postman-websocket-request.png?fit=max&auto=format&n=fZL7TCMxcnOe7SNE&q=85&s=b0cede1198d35735978a215e91d9e934" alt="Postman WebSocket Request" width="1714" height="1142" data-path="img/dashboard/system-management/postman-websocket-request.png" />

   2. Enter your Tyk API URL in the **Enter server URL** field (minus the protocol).
   3. Enter some text in the **New Message** field and click **Send**.
   4. You will see a successful connection.

   <img src="https://mintcdn.com/tyk/fZL7TCMxcnOe7SNE/img/dashboard/system-management/postman-websocket-test.png?fit=max&auto=format&n=fZL7TCMxcnOe7SNE&q=85&s=2c63331008ddce35b37d9444f13d79bb" alt="Postman WebSocket Connection Result" width="2266" height="2088" data-path="img/dashboard/system-management/postman-websocket-test.png" />

   <Note>
     If your API uses an Authentication mode other than Open (Keyless), add the details in the Header tab.
   </Note>

An example Header configuration for using an Authentication Token with an API:

<img src="https://mintcdn.com/tyk/YWsKzO6ZIBtXc1FV/img/dashboard/system-management/websocket-auth-token.png?fit=max&auto=format&n=YWsKzO6ZIBtXc1FV&q=85&s=44dc0820a9742dc8f6890c423377fa98" alt="Postman WebSocket Connection Result with Authorization token" width="2348" height="1608" data-path="img/dashboard/system-management/websocket-auth-token.png" />

See the [Access an API](/api-management/gateway-config-managing-classic#access-an-api) tutorial for details on adding an Authentication Token to your APIs.


Built with [Mintlify](https://mintlify.com).
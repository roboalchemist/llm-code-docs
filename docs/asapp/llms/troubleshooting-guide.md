# Source: https://docs.asapp.com/support/troubleshooting-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Guide

This document outlines some preliminary checks to determine the health and status of the connection between the customer or agent's browser and an ASAPP backend host prior to escalating to the ASAPP Support Team.

<Note>
  You must have access to Chrome Developer Tools in order to use this guide.
</Note>

## Troubleshooting from a Web Browser

### Using Chrome Developer Tools

Please take a moment to familiarize yourself with Chrome Developer Tools, if you are not already. ASAPP will base the troubleshooting efforts for front-end Web SDK use around the Chrome Web Browser.

[https://developers.google.com/web/tools/chrome-devtools/open](https://developers.google.com/web/tools/chrome-devtools/open)

ASAPP will also inspect network traffic as the Web SDK makes API calls to the ASAPP backend. Please also review the documentation on Chrome Developer Tools regarding networking.

[https://developers.google.com/web/tools/chrome-devtools/network](https://developers.google.com/web/tools/chrome-devtools/network)

### API Call HTTP Return Status Codes

In general, you can check connectivity and environment status by looking at the HTTP return codes from the API calls the ASAPP Web SDK makes to the ASAPP backend. You can accomplish this by limiting calls to ASAPP traffic in the Network tab. This will narrow the results to traffic that is using the string "ASAPP" somewhere in the call.

First and foremost, look for traffic that does not return successful 200 HTTP status codes. If there are 400 and 500 level errors, there may be potential network connectivity or configuration issues between the user and ASAPP backend.

Please review HTTP status codes at: [https://www.restapitutorial.com/httpstatuscodes.html](https://www.restapitutorial.com/httpstatuscodes).

To view HTTP return codes:

1. Open **Dev Tools** and navigate to the **Network** tab.
2. Reload the page or navigate to a page with ASAPP chat enabled.
3. Filter network traffic to **ASAPP**.
4. Look at the "Status" for each call. The system highlights failed calls in red.
5. For non-200 status codes, denote what the call is by the "Request URL" and the return status. You can find other helpful information in context in the "Request Payload".

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=bef6f0d8180f0c87703673128bf59b9f" data-og-width="1999" width="1999" data-og-height="879" height="879" data-path="image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8ed42ba22254f64133d0dde63f1cdf9f 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8a0d88ec16c385ca024be2550471bff8 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=214a1cc59281057db4d3e093cf768835 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=880b1a05589eef2d7626a23b894a312d 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=77d2f671a7e9f4545c1dc2a0719aacd7 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e6fe6329-8256-648b-95a2-1cf6f4d5d9d2.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=80070ef54a99bb2a29eff8df74f25055 2500w" />
</Frame>

### Environment Targeting

To determine the ASAPP environment targeted by the front-end, you can look at the network traffic and note what hostname the traffic references. For instance, ...something-demo01.test.asapp.com is the demo environment for that implementation. You will see this on every call to the ASAPP backend and it may be helpful to filter the network traffic to "ASAPP".

1. Open **Dev Tools** and navigate to the **Network** tab.
2. Reload the page or navigate to a page with ASAPP chat enabled.
3. Filter network traffic to **ASAPP**.
4. Look at the "Request URL" for the network call.
5. Parse the hostname from `https://something-demo01.test.asapp.com/api/noauth/ShouldDisplayWebChat?ASAPP-ClientType=web-sdk&amp;amp;ASAPP-ClientVersion=4.0.1-uat\`: something-demo01.test.asapp.com

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3dcdcfa3db5fd3e598564a8051e3e6a3" data-og-width="1999" width="1999" data-og-height="523" height="523" data-path="image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b9ac0639691b8096a35901c7df455fde 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0921f714337aead227d841708da6e389 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2e1b3462ad62499910685b0b28f315ca 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3bcaf1c5cec0606ab4ffc111b66b542f 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a349a56f58151414ae469d4663469034 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a26e6787-2cec-3bb6-25d9-9c29e45e05ad.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=154d3544d5842515de8543dc40e6fa0c 2500w" />
</Frame>

### WebSocket Status

In addition to looking at the API calls, it is important to look at the WebSocket connections in use. You should also be able to inspect the frames within the WebSocket to ensure the system receives messages properly.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=247347509abf2a8f2523ffb19e78a408" data-og-width="1999" width="1999" data-og-height="482" height="482" data-path="image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d406f6ab0e2d180e27880199d1f90d1b 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=75dac38f4e0ad0f21cd138c5e6f73dee 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=847d9fe7cc2e300950d23db95b0051e9 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d4f3c68428567ce62246f34ddb81ba2e 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6c32e4b5361f99eaecdf9eba5e74858c 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9e750335-dd43-9b01-7c8c-abbe0d089f5a.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e1e7d3073ec21e5c1af5111c9131bcc9 2500w" />
</Frame>

[https://developers.google.com/web/tools/chrome-devtools/network/reference#frames](https://developers.google.com/web/tools/chrome-devtools/network/reference#frames)

## Troubleshooting Customer Chat

### Should Display Web Chat

If chat does not display on the desired web page, the first place to check is ASAPP's call for `ShouldDisplayWebChat` via the **Chrome Developer Tool Network** tab. A successful API call response should contain a `DisplayCustomerSupport` field with a value of `true`. If this value is `false` for a page that should display chat, please reach out to the ASAPP Support Team. Superusers can access the Triggers section of ASAPP Admin. This will enable them to determine if the visited URL displays chat.

To troubleshoot:

1. Open **Dev Tools** and navigate to the **Network** tab.
2. Reload the page or navigate to a page with ASAPP chat enabled.
3. Filter network traffic to **ASAPP**.
4. Look at the "Request Payload" for `ShouldDisplayWebChat` and look for a `true` response for `DisplayCustomerSupport`.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=129c31a8d15938360ac25bb21ddd01cb" data-og-width="1999" width="1999" data-og-height="523" height="523" data-path="image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6d50de4ce9cb4951b00bfe351bc95bbe 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=661549423cfd8a5cb573dbdc35c886a3 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=01b9041d37cc4e6e461510dbdb729d8f 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=02976b3cf5455fadead7528011c4b4ec 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8513ce84da2ada2b113190da76adfeb2 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3be4e43e-1912-916e-fb30-22a05fd9787c.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ad17339a3cc370d042afa4a1cd0a6774 2500w" />
</Frame>

### Web SDK Context Input

To view the context provided to the SDK, you can look at the request payload of most SDK API calls. Context input may vary but typical items include:

* Subdivisions
* Segments
* Customer info parameters
* External session IDs

<Card title="Web SDK Context Provider" href="/agent-desk/integrations/web-sdk/web-contextprovider"> Review the ASAPP SDK Web Context Provider page</Card>

To view the context:

1. Open **Dev Tools** and navigate to the **Network** tab.
2. Reload page or navigate to a page with ASAPP chat enabled.
3. Filter network traffic to **ASAPP**.
4. Look at the "Request Payload" for `GetOfferedMessageUnauthed` and open the tree as follows:

**Params -> Params -> Context** -> All Customer Context (including Auth Token)

**Params -> Params -> AuthenticationParams** -> Customer ID

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ddf6a778953a346f5a959afe86817559" data-og-width="1999" width="1999" data-og-height="1305" height="1305" data-path="image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=73024990c09a096b52277c37782c4330 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4b50551f9b587622941cac0a1c8f5247 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c2ed82cff56d85aa3325c8baebe245d9 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1bbc7ca32adac293254f6c38d1f6aa3c 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5d37ce74c7e45dc981720722807f1d0d 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d923376-1aeb-0ef0-67e8-1dc3c9c68cf5.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=16681e9db8abe2bc8a3adcbd4a1f6056 2500w" />
</Frame>

### Customer Authentication Input

For authenticated customer chat sessions, you can see the Auth key within the context parameters used throughout the API calls to ASAPP.

The values passed into the Auth context will depend on the integration.

<Card title="Web SDK Context Provider" href="/agent-desk/integrations/web-sdk/web-contextprovider"> Review the ASAPP SDK Web Context Provider page for the complete use of this key</Card>

## Troubleshooting Agent Chat from Agent Desk

### Connection Status Banners

There are 3 connection statuses:

* Disconnected (Red)
* Reconnecting (Yellow)
* Connected (Green)

You will see a banner on the bottom of the ASAPP Agent Desk with the correlating colors: Red, Yellow, Green. The red and green banners only appear briefly while the connection state changes. However, the yellow banner will remain until a connection is reestablished. The connection state relies on 2 main inputs:

* 204 API calls
* WebSocket echo timeouts

After a timeout grace period of 5 seconds for either of these timeouts, a red or yellow banner will appear.

**Yellow Reconnecting Banner**

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9c11defb1aa0ca590871317c4fadfe00" data-og-width="1113" width="1113" data-og-height="127" height="127" data-path="image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=858284e7315156a427e7230c442f137e 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=cbf480bc51bec1a1310dcffc90547173 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4bda8912cb5eaf59c241b575d8d67df3 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6363455386de4d58519e7eeb73ec081c 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2e01f5416ba6ffded404571bea0ccffb 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d26b34e-5abe-0664-dc13-f116fcfaa244.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ca9476644e408f9d4475a25cd53f0555 2500w" />
</Frame>

### 204 API call

The ASAPP Agent Desk makes API calls to the backend periodically to ensure status and connectivity reporting is functional. Verify the HTTP status and response timing of these calls to look for indicators of an issue. These calls display as the number 204 in the Chrome Developer Tools Network tab.

To view these calls:

1. Open **Dev Tools** and navigate to the **Network** tab.
2. Reload page or navigate to a page with ASAPP chat enabled.
3. Filter network traffic to **ASAPP**.
4. Look at the "204" calls over time to determine good health.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=92fcf0a0d0abd8e05f3657a60d4f717e" data-og-width="1568" width="1568" data-og-height="1096" height="1096" data-path="image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3ac4263d34833f2d85b2137598d005b4 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=67479b1ab069c1735069f5b217146f12 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e7d9418d38e11e342530c47515cf19c8 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=27d7d687b8cc625098d18d470c609b91 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=60386d248c2732d423fe38845671eff9 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca52a4b7-4d0c-e773-323c-195a2e9970c2.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=726c10198d2a5bc48cc86908457df8de 2500w" />
</Frame>

### WebSocket

When a customer chat loads onto the ASAPP Agent Desk, this creates a WebSocket. During the life of that conversation, ASAPP sends continual echoes (requests and responses) to determine WebSocket health and status. ASAPP sends the echoes every 16-18 seconds and has a 6 second timeout by default. If these requests and responses intermittently time out, there is likely a network issue between the Agent Desktop and the ASAPP Desk application.

You can also view messages being sent through WebSocket, as the agent to customer conversation happens:

1. Open **Dev Tools** and navigate to the **Network** tab.
2. Reload page or navigate to a page with ASAPP chat enabled.
3. Click **WS** next to the Filter text box to filter network traffic to WebSocket.
4. Look at the Messages tab in WebSocket.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=76f6e13774912b2848309130e3fb53af" data-og-width="1706" width="1706" data-og-height="300" height="300" data-path="image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ebfddd630a6be8799bec7b08df6de68b 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b2fb2c19d7bf56d7566746f3be5f3b12 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d83e2762df71ad29b40a2bfdf38237c1 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=bd840ffa37500696ef43ced9489df21c 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=fa0a161b1573e2eff10297d4f0df70fb 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9c235a8b-d895-a7de-f904-aee054c0d4f3.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0de8943f5540f336616e02c34dce32f5 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=52a9fe7b9b5fbf9ec1019e7e241d9d85" data-og-width="1568" width="1568" data-og-height="1096" height="1096" data-path="image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a693bedfec6381bd5c97116dbbbe3d23 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5202ec3aab873c3f1fbe4677d3d404b4 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=860fadc5da34027b9d4cc1eb5136cdb3 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=73ca57fb2f13d636533d8d3c357f0ed9 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=dd00f5ad49f22600e839f1ac892b50e0 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9fae80a-dfdb-5446-4bb6-140287c89601.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0247760c503b8f76ebe024ffb8490f60 2500w" />
</Frame>

If you see one of these pairs of echoes missing, it is most likely because Agent Desk did not receive the echo from the ASAPP backend due to packet loss. If the 'Attempting to reconnect..' message shows, Agent Desk attempts to reconnect with the ASAPP backend to establish a new WebSocket. The messages display in red text starting with 'request?ASAPP-ClientType' in the Network tab of Chrome Developer Tools.

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=55cffe2ff9914a76d962cb87779db4de" data-og-width="1999" width="1999" data-og-height="978" height="978" data-path="image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=e9d2dd53d9367cceca0186ef8be6fd15 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=703982752afb507e87e58edbefd1aa24 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=e7a7d17fdfa9f4b12013044ba4f7ff5d 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b198ce21d4443168cfa6353114898c50 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=e37a312de21aee046de29524e6af9a55 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0e90bcea-cc88-8f78-fd2f-99cbcea61c19.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=296b06a06b3c41e2f6c59e553d26f361 2500w" />
</Frame>

If you lose network connectivity and then re-establish it, there will be multiple WebSocket entries visible when you click on **WS**.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=365596038e0a44a530d64036cbb90728" data-og-width="1999" width="1999" data-og-height="519" height="519" data-path="image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=14482f955b133e8718cd3cc0dd0533fc 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=48f0d2fa842e5dc583a2d05431c62517 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5d93f5257f8563b140c2d05a951f109c 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=118a586e3a1b3fc3c342d0a717331126 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=67a37910a7007c1935213f9ebb547164 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7840633a-5eaf-b4ce-a6b5-70f04a5ae40e.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=580617d33a7bf3c51e4218da1b246267 2500w" />
</Frame>

## Troubleshooting Agent Desk/Admin Access Issues

### Using Employee List in ASAPP Admin

If a user has issues logging in to ASAPP, you can view their details within ASAPP Admin after their first successful login. Check the Enabled status, Roles, and Groups for the user to determine if there are any user level issues. ASAPP will reject the user's login attempt if their account is disabled.

To find an employee:

1. Login to ASAPP Admin.
2. Navigate to Employee List.
3. Use the filter to find the desired account.
4. Check account attributes for: Enabled, Roles, and Groups.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=cb0833eca1e1bf285068f15af0b30202" data-og-width="2888" width="2888" data-og-height="720" height="720" data-path="image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=86060033c75ea814df2a02d671cc668e 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a746919a47c0c1d6bf31885554c23848 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e0a8f854a94e8185b7513edede91f1a9 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=6bcc3022623b6c4ee8b8d4f3de27a9ef 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=02113adff57a5f05bf10f58e3cc06a51 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-24a8a576-bca7-11c2-72fb-49a4a810ee58.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=188b7f2b3bf5cbb51ab44fb8b51d93bb 2500w" />
</Frame>

### Employee Roles Mismatch

During the user's SSO login process, ASAPP receives a list of user roles via the Single-Sign-On SAML assertion.

If the user roles in the Employee List is incorrect:

1. Check with your Identity & Access Management team to verify that the user has been added to the correct set of AD Security Groups.
2. Once you have verified the user's AD Security Groups, please ask the user to log out and log back in using the IDP-initiated SSO URL.
3. If you still see a mismatch between the user's AD Security Groups and the ASAPP Employee List, then please reach out to the ASAPP Support Team.

### Errors During User Login

The SSO flow is a series of browser redirects in the following order:

1. Your SSO engine IDP-initiated URL -- typically hosted within your domain. This is the URL that users must use to login.
2. Your system's authentication system -- typically hosted within your domain. If the user is already authenticated, then it will immediately redirect the user back to your SSO engine URL. Otherwise, the user will be presented with the login page and prompted to enter their credentials.
3. ASAPP's SSO engine -- hosted on the auth-\{customerName}.asapp.com domain.
4. ASAPP's Agent/Admin app -- hosted on the \{customerName}.asapp.com domain.

There are several potential errors that may happen during login. In all of these cases, it is beneficial to find out:

1. The SSO login URL being used by the user to login.
2. The error page URL and error message displayed.

#### Incorrect SSO Login URL

Confirm the user logins to the correct SSO URL. Due to browser redirects, users may accidentally bookmark an incorrect URL (e.g., ASAPP's SSO engine URL, instead of your SSO engine IDP-initiated URL).

#### Invalid Role Values in the SSO SAML Assertion

If the user sees a "Failed to authenticate user" error message and the URL is an ASAPP URL (...asapp.com), then please confirm that correct role values are being sent in the SAML assertion. This error message typically indicates that the user role value is not recognizable within ASAPP.

#### Other Login Errors

For any other errors, please check the error page URL. If the error page URL is an ASAPP URL (ends in asapp.com), please reach out to the ASAPP Support Team for help. If the URL is your SSO URL or your system's authentication system, please contact your internal support team.

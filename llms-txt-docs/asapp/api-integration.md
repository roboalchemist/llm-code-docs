# Source: https://docs.asapp.com/agent-desk/digital-agent-desk/api-integration.md

# API Integration

> Learn how to connect the Digital Agent Desk to your backend systems.

ASAPP integrates with Your APIs to provide customers and agents with a more rich and personalized interaction.

ASAPP accomplishes this by making backend calls to Customer APIs in real time, providing customers with the latest up-to-date information.

This involves customers exposing the relevant APIs, securely, for ASAPP to make server to server calls.

## Authentication

Customers should wrap their APIs with secure authentication mechanisms, mainly addressing Customer Authentication and API Authentication.

### API Authentication on behalf of the User

ASAPP leverages our customers existing mechanisms of authenticating their customers, which ideally are the same across different channels.

Any identifier issued should have an expiration that is short, but should also allow for a good user experience without the customer having to authenticate multiple times over a session.

* **Cookie-based Authentication**: This is the traditional way where a user posts login credentials to the customer's server and receives a signed cookie, which is stored on the server and a copy on the browser, and will be used in subsequent interactions for the duration of the session. However, where possible a token-based approach is typically preferred.
* **Token-based Authentication:** In this mechanism a user posts login credentials to the customer's server and is issued a signed JSON Web Token (JWT). This token is not stored on the server making all interactions fully stateless. All requests from the client will include the JWT, which only the server can decode to authenticate every request. For more information on generating and signing JSON Web Tokens, please refer to [https://jwt.io/](https://jwt.io/).

**API Endpoint**: `POST /customer_authenticate`

**Request**

```json  theme={null}
curl -X POST https://api.example.com/auth/customer_authenticate \
-H 'cache-control: no-cache' \
-d 'username=<username>&password=<password>'
```

**Response**

```json  theme={null}
{
  "issued_at" : "1570733606449",
  "JWT" : "<JWT>",
  "expires_in" : "28799"
}
```

<Note>
  ASAPP requires direct access to the "customer\_authenticate" API to retrieve JWTs/cookies programmatically for testing.
</Note>

#### Communicating Customer Identifier with ASAPP

The customer may wish to implement any mechanism to authenticate their customers, as long as they can pass the identifier (cookie, JWT etc.) to ASAPP. The methods of passing this value to ASAPP depend on the chat channel used, either for [Web](/agent-desk/integrations/web-sdk/web-authentication), [iOS](/agent-desk/integrations/ios-sdk/user-authentication), and [Android](/agent-desk/integrations/android-sdk/user-authentication).

#### Customer Identifier Requirements

ASAPP uses this customer identifier as a pass through value, either by including it as an HTTP Header or in the Body, when requesting customer data from the backend APIs. Since the Customer Identifier is the only piece of data ASAPP uses to identify users, it should adhere to the following:

* **Unique**: ASAPP will associate every customer chat with this id allowing ASAPP to tie chats from different channels into one single conversation. It is imperative that the Customer Identifier be unique per customer.
* **Consistent**: The Customer Identifier should remain consistent so that even if the customer returns after a significant amount of time, we are able to identify the customer.
* **Opaque**: The Customer Identifier by itself should not contain any customer Personally Identifiable Information (PII). It should be hashed, encoded and/or encrypted so that when used by itself, it is of no value.

### API Authentication using System-level Credential

Customers may wish to secure backend APIs by restricting access for clients to specific resources for a limited amount of time.

You can implement this using various mechanisms like OAuth 2.0, API Keys, System Credentials etc. This section provides details about OAuth using a Client Credentials Grant, which works well for server to server communication.

#### Client Credentials Grant

In this mechanism, the client sends a HTTP POST request with the following parameters in return for an access\_token.

* **grant\_type**
* **client\_id**
* **client\_secret**

**API Endpoint**: `POST /access_token`

**Request**

```json  theme={null}
curl -X POST https://api.example.com/oauth/access_token?grant_type=client_credentials 
\
-H 'cache-control: no-cache' \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=<client_id>&client_secret=<client_secret>'
```

**Response**

```json  theme={null}
{
  "token_type" : "Bearer",
  "issued_at" : "1570733606449",
  "client_id" : “<client_id>”,
  "access_token" : "<access_token>",
  "scope" : "client_credentials",
  "expires_in" : "28799"
}
```

### API Authorization

The customer may also want to use API keys to provide authorization to specific APIs. API keys are also passed in the HTTP header along with the authentication token.

**API Endpoint:** POST /getprofile

**Request**

```json  theme={null}
curl -X POST https://api.example.com/account/getprofile
-H 'Authorization: Bearer <access_token>' \
-H 'customer-auth: JWT <JWT>' \
-H 'content-type: application/json' \
-H 'api-key: <api_key>' \
```

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=db00e94c4a49fef3d49c7a1202fba7a2" data-og-width="1550" width="1550" data-og-height="1220" height="1220" data-path="image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ad7bb285a5a8d2d79b02f28222127159 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b45c390438d607de4b275c6470c11f9b 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=79f39a4e0a309f2c93e4200cdd155b86 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=fcee31512fbaa2677c03c01d4f07f6b9 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d99421cb2e5dcb67b7ec291e42253798 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b551c5ab-cc5f-53ef-eb15-3073377c72a6.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f251c32cdbbf4613e3040d53c4980b70 2500w" />
</Frame>

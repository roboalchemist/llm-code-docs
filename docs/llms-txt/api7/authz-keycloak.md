# Source: https://docs.api7.ai/hub/authz-keycloak.md

# authz-keycloak

The `authz-keycloak` plugin supports the integration with [Keycloak](https://www.keycloak.org/) to authenticate and authorize users. See Keycloak's [Authorization Services Guide](https://www.keycloak.org/docs/latest/authorization_services/) for more information about the configuration options available in this plugin.

While the plugin was developed for Keycloak, it could theoretically be used with other OAuth/OIDC and UMA-compliant identity providers.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `authz-keycloak` for different scenarios.

To follow along, complete the [preliminary setups](#set-up-keycloak) for Keycloak.

### Set Up Keycloak[â](#set-up-keycloak "Direct link to Set Up Keycloak")

#### Start Keycloak[â](#start-keycloak "Direct link to Start Keycloak")

Start a Keycloak instance named `apisix-quickstart-keycloak` with the administrator name `quickstart-admin` and password `quickstart-admin-pass` in [development mode](https://www.keycloak.org/server/configuration#_starting_keycloak_in_development_mode) in Docker:

```
docker run -d --name "apisix-quickstart-keycloak" \
  -e 'KEYCLOAK_ADMIN=quickstart-admin' \
  -e 'KEYCLOAK_ADMIN_PASSWORD=quickstart-admin-pass' \
  -p 8080:8080 \
  quay.io/keycloak/keycloak:18.0.2 start-dev
```

Save the Keycloak IP to an environment variable to be referenced in future configuration:

```
KEYCLOAK_IP=192.168.42.145    # replace with your host IP
```

Navigate to `http://localhost:8080` in browser and click **Administration Console**:

![admin-console](https://static.api7.ai/uploads/2024/01/12/yEKlaSf5_admin-console.png)

Enter the administratorâs username `quickstart-admin` and password `quickstart-admin-pass` to sign in:

![admin-signin](https://static.api7.ai/uploads/2024/01/12/GYIVrPyb_signin.png)

#### Create a Realm[â](#create-a-realm "Direct link to Create a Realm")

In the left menu, hover over **Master**, and select **Add realm** in the dropdown:

![create-realm](https://static.api7.ai/uploads/2024/01/12/563XIJPK_add-realm.png)

Enter the realm name `quickstart-realm` and click **Create** to create it:

![add-realm](https://static.api7.ai/uploads/2024/01/12/0lD21Z8R_create-realm.png)

#### Create a Client[â](#create-a-client "Direct link to Create a Client")

Click **Clients** > **Create** to open the **Add Client** page:

![create-client](https://static.api7.ai/uploads/2024/01/12/nHxgXyd9_create-client.png)

Enter **Client ID** as `apisix-quickstart-client`, keep the **Client Protocol** as `openid-connect` and **Save**:

![add-client](https://static.api7.ai/uploads/2024/01/12/7YSCHCnp_add-client.png)

The client `apisix-quickstart-client` is created. After redirecting to the detailed page, select `confidential` as the **Access Type**:

![client-access-type-confidential](https://static.api7.ai/uploads/2024/01/12/L7cahPUe_confidential.png)

When the user login is successful during the SSO, Keycloak will carry the state and code to redirect the client to the addresses in **Valid Redirect URIs**. For simplicity of demonstration, enter wildcard `*` to accept any redirect URI:

![client-redirect](https://static.api7.ai/uploads/2024/01/12/B3VGbQbW_redirect-uri.png)

Enable authorization for the client, which should also enable service accounts with an assigned role `uma_protection` automatically:

![enable-authorization](https://static.api7.ai/uploads/2024/01/05/S4we4KO9_enable-auth.png)

Select **Save** to apply custom configurations.

#### Save Client ID and Secret[â](#save-client-id-and-secret "Direct link to Save Client ID and Secret")

Click on **Clients** > `apisix-quickstart-client` > **Credentials**, and copy the client secret from **Secret**:

![client-secret](https://static.api7.ai/uploads/2024/01/12/3VqiXdf9_client-secret.png)

Save the OIDC client ID and secret to environment variables:

```
OIDC_CLIENT_ID=apisix-quickstart-client
OIDC_CLIENT_SECRET=bSaIN3MV1YynmtXvU8lKkfeY0iwpr9cH  # replace with your value
```

#### Request Access Token[â](#request-access-token "Direct link to Request Access Token")

Request an access token from Keycloak:

```
curl -i "http://$KEYCLOAK_IP:8080/realms/quickstart-realm/protocol/openid-connect/token" -X POST \
  -d 'grant_type=client_credentials' \
  -d 'client_id='$OIDC_CLIENT_ID'' \
  -d 'client_secret='$OIDC_CLIENT_SECRET''
```

You should see a response similar to the following:

```
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoT3ludlBPY2d6Y3VWWnYtTU42bXZKMUczb0dOX2d6MFo3WFl6S2FSa1NBIn0.eyJleHAiOjE3MDM4MjU1NjQsImlhdCI6MTcwMzgyNTI2NCwianRpIjoiMWQ4NWE4N2UtZDFhMC00NThmLThiMTItNGZiYWM2ODA5YmYwIiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMS44Mzo4MDgwL3JlYWxtcy9xdWlja3N0YXJ0LXJlYWxtIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjE1OGUzOWFlLTk0YjAtNDI3Zi04ZGU3LTU3MTRhYWYwOGYzOSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFwaXNpeC1xdWlja3N0YXJ0LWNsaWVudCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1xdWlja3N0YXJ0LXJlYWxtIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SG9zdCI6IjE3Mi4xNy4wLjEiLCJjbGllbnRJZCI6ImFwaXNpeC1xdWlja3N0YXJ0LWNsaWVudCIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1hcGlzaXgtcXVpY2tzdGFydC1jbGllbnQiLCJjbGllbnRBZGRyZXNzIjoiMTcyLjE3LjAuMSJ9.TltzSXqrJuVID7aGrb35jn-oc07U_-jugSn-3jKz4A44LwtAsME_8b3qkmR4boMOIht_5pF6bnnp70MFAlg6JKu4_yIQDxF_GAHjnZXEO8OCKhtIKwXm2w-hnnJVIhIdGkIVkbPP0HfILuar_m0hpa53VpPBGYR-OS4pyh0KTUs8MB22xAEqyz9zjCm6SX9vXCqgeVkSpRW2E8NaGEbAdY25uY-ZC4dI_pON87Ey5e8GdD6HQLXQlGIOdCDi3N7k0HDoD9TZRv2bMRPfy4zVYm1ZlClIuF79A-ZBwr0c-XYuq7t6EY0gPGEXB-s0SaKlrIU5S9JBeVXRzYvqAih41g","expires_in":300,"refresh_expires_in":0,"token_type":"Bearer","not-before-policy":0,"scope":"email profile"}
```

Save the token to an environment variable:

```
# replace with your access token
ACCESS_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoT3ludlBPY2d6Y3VWWnYtTU42bXZKMUczb0dOX2d6MFo3WFl6S2FSa1NBIn0.eyJleHAiOjE3MDM4MjU1NjQsImlhdCI6MTcwMzgyNTI2NCwianRpIjoiMWQ4NWE4N2UtZDFhMC00NThmLThiMTItNGZiYWM2ODA5YmYwIiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMS44Mzo4MDgwL3JlYWxtcy9xdWlja3N0YXJ0LXJlYWxtIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjE1OGUzOWFlLTk0YjAtNDI3Zi04ZGU3LTU3MTRhYWYwOGYzOSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFwaXNpeC1xdWlja3N0YXJ0LWNsaWVudCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1xdWlja3N0YXJ0LXJlYWxtIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SG9zdCI6IjE3Mi4xNy4wLjEiLCJjbGllbnRJZCI6ImFwaXNpeC1xdWlja3N0YXJ0LWNsaWVudCIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1hcGlzaXgtcXVpY2tzdGFydC1jbGllbnQiLCJjbGllbnRBZGRyZXNzIjoiMTcyLjE3LjAuMSJ9.TltzSXqrJuVID7aGrb35jn-oc07U_-jugSn-3jKz4A44LwtAsME_8b3qkmR4boMOIht_5pF6bnnp70MFAlg6JKu4_yIQDxF_GAHjnZXEO8OCKhtIKwXm2w-hnnJVIhIdGkIVkbPP0HfILuar_m0hpa53VpPBGYR-OS4pyh0KTUs8MB22xAEqyz9zjCm6SX9vXCqgeVkSpRW2E8NaGEbAdY25uY-ZC4dI_pON87Ey5e8GdD6HQLXQlGIOdCDi3N7k0HDoD9TZRv2bMRPfy4zVYm1ZlClIuF79A-ZBwr0c-XYuq7t6EY0gPGEXB-s0SaKlrIU5S9JBeVXRzYvqAih41g
```

### Use Lazy Load Path and Resource Registration Endpoint[â](#use-lazy-load-path-and-resource-registration-endpoint "Direct link to Use Lazy Load Path and Resource Registration Endpoint")

The examples below demonstrate how you can configure the plugin to dynamically resolve the request URI to resource(s) using the resource registration endpoint instead of the static permissions.

Create a route with `authz-keycloak-route` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "authz-keycloak-route",
    "uri": "/anything",
    "plugins": {
      "authz-keycloak": {
        "lazy_load_paths": true,
        "resource_registration_endpoint": "http://'"$KEYCLOAK_IP"':8080/realms/quickstart-realm/authz/protection/resource_set",
        "discovery": "http://'"$KEYCLOAK_IP"':8080/realms/quickstart-realm/.well-known/uma2-configuration",
        "client_id": "'"$OIDC_CLIENT_ID"'",
        "client_secret": "'"$OIDC_CLIENT_SECRET"'"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

â¶ Set `lazy_load_paths` to `true`.

â· Set `resource_registration_endpoint` to Keycloak's UMA-compliant resource registration endpoint endpoint. Required when `lazy_load_paths` is `true`.

â¸ Set `discovery` to the discovery document endpoint of Keycloak authorization services.

â¹ Set `client_id` to client ID created previously.

âº Set `client_secret` to client secret created previously. Required when `lazy_load_paths` is `true`.

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything" -H "Authorization: Bearer $ACCESS_TOKEN"
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Authorization": "Bearer eyJhbGciOiJSU...",
    ...
  },
  "json": null,
  "method": "GET",
  "origin": "127.0.0.1, 108.180.51.111",
  "url": "http://127.0.0.1/anything"
}
```

### Use Static Permissions[â](#use-static-permissions "Direct link to Use Static Permissions")

The examples below demonstrate how you can configure Keycloak for scope-based permission associated with a client scope policy, and configure the `authz-keycloak` plugin to use static permissions.

#### Create Scope in Keycloak[â](#create-scope-in-keycloak "Direct link to Create Scope in Keycloak")

Go to **Clients** > **`apisix-quickstart-client`** > **Authorization** > **Authorization Scopes**, and click **Create** to open the **Add Scope** page:

![add-scope](https://static.api7.ai/uploads/2024/01/06/bVHhiALe_auth-scope.png)

Enter the scope names as `access` and click **Save**:

![create-new-scope](https://static.api7.ai/uploads/2024/01/06/xPorYwK3_save-scope.png)

#### Create Resource in Keycloak[â](#create-resource-in-keycloak "Direct link to Create Resource in Keycloak")

Go to **Clients** > **`apisix-quickstart-client`** > **Authorization** > **Resources** and click **Create** to open the **Add Resource** page:

![create-resource](https://static.api7.ai/uploads/2024/01/06/15DJ9HAU_create-resource.png)

Enter the resource names `httpbin-anything`, URI `/anything`, scope `access`, and click **Save**:

![save-resource](https://static.api7.ai/uploads/2024/01/06/epuAPgos_save-resource.png)

#### Create Client Scope in Keycloak[â](#create-client-scope-in-keycloak "Direct link to Create Client Scope in Keycloak")

Go to **Client Scopes** and click **Create** to open the **Add client scope** page:

![create-client-scope](https://static.api7.ai/uploads/2024/01/11/PyseoG7T_creat-client-scope.png)

Enter the scope name `httpbin-access` and click **Save**:

![save-client-scope](https://static.api7.ai/uploads/2024/01/12/5xQl0Xbx_save-client-scope.png)

#### Create Policy in Keycloak[â](#create-policy-in-keycloak "Direct link to Create Policy in Keycloak")

Go to **Clients** > **`apisix-quickstart-client`** > **Authorization** > **Policies** > **Create Policies** and select **Client Scope** from the dropdown to open the **Add Client Scope Policy** page:

![create-policy](https://static.api7.ai/uploads/2024/01/06/7UtT3cF6_create-policy.png)

Enter the policy name `access-client-scope-policy` for client scope `httpbin-access`, check the **Required** box, and click **Save**:

![save-policy](https://static.api7.ai/uploads/2024/12/12/2DR0K39f_add_client_scope.png)

#### Create Permission in Keycloak[â](#create-permission-in-keycloak "Direct link to Create Permission in Keycloak")

Go to **Clients** > **`apisix-quickstart-client`** > **Authorization** > **Permissions** > **Create Permissions** and select **Scope-Based** from the dropdown to open the **Add Scope Permission** page:

![create-permission](https://static.api7.ai/uploads/2024/12/12/0PWsJUti_create_permission.png)

Enter the permission name `access-scope-perm`, select the `access` scope, apply the policy `access-client-scope-policy`, and click **Save**:

![add-scope-permission](https://static.api7.ai/uploads/2024/01/12/Y0vlk1Tj_add-scope-permission.png)

#### Assign Client Scope[â](#assign-client-scope "Direct link to Assign Client Scope")

Go to **Clients** > **`apisix-quickstart-client`** > **Client Scopes** and add `httpbin-access` to the default client scopes:

![add-client-scope](https://static.api7.ai/uploads/2024/01/06/sJKUMUcP_add-client-scope.png)

#### Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

Create a route with `authz-keycloak-route` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "authz-keycloak-route",
    "uri": "/anything",
    "plugins": {
      "authz-keycloak": {
        "lazy_load_paths": false,
        "discovery": "http://'"$KEYCLOAK_IP"':8080/realms/quickstart-realm/.well-known/uma2-configuration",
        "permissions": ["httpbin-anything#access"],
        "client_id": "apisix-quickstart-client"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

â¶ Set `lazy_load_paths` to `false`.

â· Set `discovery` to the discovery document endpoint of Keycloak authorization services.

â¸ Set `permissions` to resource `httpbin-anything` and scope `access`.

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything" -H "Authorization: Bearer $ACCESS_TOKEN"
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Authorization": "Bearer eyJhbGciOiJSU...",
    ...
  },
  "json": null,
  "method": "GET",
  "origin": "127.0.0.1, 108.180.51.111",
  "url": "http://127.0.0.1/anything"
}
```

If you remove the client scope `httpbin-access` for `apisix-quickstart-client`, you should receive a `401 Unauthorized` response when requesting the resource.

### Generate Token with Password Grant at Custom Token Endpoint[â](#generate-token-with-password-grant-at-custom-token-endpoint "Direct link to Generate Token with Password Grant at Custom Token Endpoint")

The examples below demonstrate how you can generate a token using with the password grant at a custom endpoint.

#### Create User in Keycloak[â](#create-user-in-keycloak "Direct link to Create User in Keycloak")

To use the password grant, you should first create a user.

Go to **Users** > **Add user** and click on **Add user**:

![add-user](https://static.api7.ai/uploads/2024/01/12/IBCav8aa_add-user.png)

Enter the **Username** as `quickstart-user` and select **Save**:

![save-user](https://static.api7.ai/uploads/2024/01/12/3fUQOFWg_save-user.png)

Click on **Credentials**, then set the **Password** as `quickstart-user-pass`. Switch **Temporary** to `OFF` to that you do not need to change password the first time you log in:

![set-password](https://static.api7.ai/uploads/2024/01/12/aoabcBbC_set-password.png)

#### Configure APISIX[â](#configure-apisix-1 "Direct link to Configure APISIX")

Create a route with `authz-keycloak-route` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "authz-keycloak-route",
    "uri": "/api/*",
    "plugins": {
      "authz-keycloak": {
        "lazy_load_paths": true,
        "resource_registration_endpoint": "http://'"$KEYCLOAK_IP"':8080/realms/quickstart-realm/authz/protection/resource_set",
        "client_id": "'"$OIDC_CLIENT_ID"'",
        "client_secret": "'"$OIDC_CLIENT_SECRET"'",
        "token_endpoint": "http://'"$KEYCLOAK_IP"':8080/realms/quickstart-realm/protocol/openid-connect/token",
        "password_grant_token_generation_incoming_uri": "/api/token"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

â¶ Set `token_endpoint` to the Keycloak token endpoint. Required when discovery document is not provided.

â· Set `password_grant_token_generation_incoming_uri` to a custom URI path users can obtain tokens from.

Send a request to the configured token endpoint. Note that the request should use the POST method and `application/x-www-form-urlencoded` as the `Content-Type`:

```
OIDC_USER=quickstart-user
OIDC_PASSWORD=quickstart-user-pass

curl "http://127.0.0.1:9080/api/token" -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Accept: application/json" \
  -d 'username='$OIDC_USER'' \
  -d 'password='$OIDC_PASSWORD''
```

You should see a JSON response with the access token, similar to the following:

```
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6U3FFaXN6VlpuYi1sRWMzZkp0UHNpU1ZZcGs4RGN3dXI1Mkx5V05aQTR3In0.eyJleHAiOjE2ODAxNjA5NjgsImlhdCI6MTY4MDE2MDY2OCwianRpIjoiMzQ5MTc4YjQtYmExZC00ZWZjLWFlYTUtZGY2MzJiMDJhNWY5IiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguNDIuMTQ1OjgwODAvcmVhbG1zL3F1aWNrc3RhcnQtcmVhbG0iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMTg4MTVjM2EtNmQwNy00YTY2LWJjZjItYWQ5NjdmMmIwMTFmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXBpc2l4LXF1aWNrc3RhcnQtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImIxNmIyNjJlLTEwNTYtNDUxNS1hNDU1LWYyNWUwNzdjY2I3NiIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1xdWlja3N0YXJ0LXJlYWxtIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6ImIxNmIyNjJlLTEwNTYtNDUxNS1hNDU1LWYyNWUwNzdjY2I3NiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoicXVpY2tzdGFydC11c2VyIn0.uD_7zfZv5182aLXu9-YBzBDK0nr2mE4FWb_4saTog2JTqFTPZZa99Gm8AIDJx2ZUcZ_ElkATqNUZ4OpWmL2Se5NecMw3slJReewjD6xgpZ3-WvQuTGpoHdW5wN9-Rjy8ungilrnAsnDA3tzctsxm2w6i9KISxvZrzn5Rbk-GN6fxH01VC5eekkPUQJcJgwuJiEiu70SjGnm21xDN4VGkNRC6jrURoclv3j6AeOqDDIV95kA_MTfBswDFMCr2PQlj5U0RTndZqgSoxwFklpjGV09Azp_jnU7L32_Sq-8coZd0nj5mSdbkJLJ8ZDQDV_PP3HjCP7EHdy4P6TyZ7oGvjw","expires_in":300,"refresh_expires_in":1800,"refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0YjFiNTQ3Yi0zZmZjLTQ5YzQtYjE2Ni03YjdhNzIxMjk1ODcifQ.eyJleHAiOjE2ODAxNjI0NjgsImlhdCI6MTY4MDE2MDY2OCwianRpIjoiYzRjNjNlMTEtZTdlZS00ZmEzLWJlNGYtNDMyZWQ4ZmY5OTQwIiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguNDIuMTQ1OjgwODAvcmVhbG1zL3F1aWNrc3RhcnQtcmVhbG0iLCJhdWQiOiJodHRwOi8vMTkyLjE2OC40Mi4xNDU6ODA4MC9yZWFsbXMvcXVpY2tzdGFydC1yZWFsbSIsInN1YiI6IjE4ODE1YzNhLTZkMDctNGE2Ni1iY2YyLWFkOTY3ZjJiMDExZiIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJhcGlzaXgtcXVpY2tzdGFydC1jbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiYjE2YjI2MmUtMTA1Ni00NTE1LWE0NTUtZjI1ZTA3N2NjYjc2Iiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiYjE2YjI2MmUtMTA1Ni00NTE1LWE0NTUtZjI1ZTA3N2NjYjc2In0.8xYP4bhDg1U9B5cTaEVD7B4oxNp8wwAYEynUne_Jm78","token_type":"Bearer","not-before-policy":0,"session_state":"b16b262e-1056-4515-a455-f25e077ccb76","scope":"profile email"}
```

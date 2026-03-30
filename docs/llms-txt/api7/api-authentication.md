# Source: https://docs.api7.ai/enterprise/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-security/api-authentication.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md

# Set Up API Authentication

For security, you should only allow authenticated and authorized [consumers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md) to access your APIs. API7 Gateway provides several plugins to enable authentication and authorization.

Authentication plugins enabled on services act as locks on your APIs, while consumer credentials serve as the keys to unlock them. In API7 Gateway, you need a unique username and at least one credential to set up a consumer.

Consumers can utilize multiple credentials of different types, and all are treated equally for authentication purposes.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

note

Avoid configuring multiple authentication plugins on the same service/route to prevent conflicts.

## Enable Key Authentication for APIs[â](#enable-key-authentication-for-apis "Direct link to Enable Key Authentication for APIs")

### For a Service[â](#for-a-service "Direct link to For a Service")

To use key authentication for all routes in a service, enable the [Key Auth Plugin](https://docs.api7.ai/hub/key-auth.md) on the service.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the `key-auth` plugin, then click **Enable**.
4. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the service configuration to use key authentication:

adc-service.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    plugins:
      key-auth:
        _meta:
          disable: false
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc-consumer.yaml -f adc-service.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

ApisixService custom resource is not yet available.

### For a Single Route[â](#for-a-single-route "Direct link to For a Single Route")

* Dashboard
* ADC
* Ingress Controller

To use key authentication for a specific route, enable the [Key Auth Plugin](https://docs.api7.ai/hub/key-auth.md) on the route instead of the service.

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Routes** from the side navigation bar.
3. Select your target route, for example, `get-ip`.
4. In the **Plugin** field, click **Enable Plugin**.
5. Search for the `key-auth` plugin, then click **Enable**.
6. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the route configuration to use key authentication:

adc-route.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
        plugins:
          key-auth:
            _meta:
              disable: false
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc-consumer.yaml -f adc-route.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

Create a Kubernetes manifest file for a route, where key authentication is enabled:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: get-ip
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
        methods:
          - GET
      backends:
        - serviceName: httpbin
          servicePort: 80
      authentication:
        enable: true
        type: keyAuth
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

### Validate Key Authentication[â](#validate-key-authentication "Direct link to Validate Key Authentication")

Create a consumer with key authentication credentials by following [configure key authentication credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md#configure-key-authentication-credentials).

Then follow the steps below to validate the key authentication.

1. Send a request without the `apikey` header:

```
curl -i "http://127.0.0.1:9080/ip"  
```

Since the key is not provided, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"Missing API key found in request"}
```

2. Send a request with a wrong key in the `apikey` header:

```
curl -i "http://127.0.0.1:9080/ip" -H "apikey: wrongkey" 
```

Since the key is wrong, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"Invalid API key in request"}
```

3. Send a request with the correct key in the `apikey` header:

```
curl -i "http://127.0.0.1:9080/ip" -H "apikey: alice-primary-key" 
```

With the correct key in the request, you will receive an `HTTP/1.1 200 OK` response.

## Enable Basic Authentication for APIs[â](#enable-basic-authentication-for-apis "Direct link to Enable Basic Authentication for APIs")

### For a Service[â](#for-a-service-1 "Direct link to For a Service")

To use basic authentication for all routes in a service, enable the [Basic Auth Plugin](https://docs.api7.ai/hub/basic-auth.md) on the service.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the `basic-auth` plugin, then click **Enable**.
4. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the service configuration to use JWT authentication:

adc-service.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    plugins:
      basic-auth:
        _meta:
          disable: false
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc-consumer.yaml -f adc-service.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

ApisixService custom resource is not yet available.

### For a Single Route[â](#for-a-single-route-1 "Direct link to For a Single Route")

* Dashboard
* ADC
* Ingress Controller

To use basic authentication for a specific route, enable the [Basic Auth Plugin](https://docs.api7.ai/hub/basic-auth.md) on the route instead of the service.

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Routes** from the side navigation bar.
3. Select your target route, for example, `get-ip`.
4. In the **Plugin** field, click **Enable Plugin**.
5. Search for the `basic-auth` plugin, then click **Enable**.
6. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the route configuration to use basic authentication:

adc-route.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
        plugins:
          basic-auth:
            _meta:
              disable: false
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc-consumer.yaml -f adc-route.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

Create a Kubernetes manifest file for a route, where basic authentication is enabled:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: get-ip
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
        methods:
          - GET
      backends:
        - serviceName: httpbin
          servicePort: 80
      authentication:
        enable: true
        type: basicAuth
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

### Validate Basic Authentication[â](#validate-basic-authentication "Direct link to Validate Basic Authentication")

Create a consumer with basic authentication credentials by following [configure basic authentication credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md#configure-basic-authentication-credentials).

Follow the steps below to validate the basic authentication.

1. Send a request without a basic authentication credential in the header:

```
curl -i "http://127.0.0.1:9080/ip"  
```

Since the credential is not provided, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"Missing authorization in request"}
```

2. Send a request with an invalid basic authentication credential (username and password do not match, or username does not exist) in the header:

```
curl -i "http://127.0.0.1:9080/ip" -u alice:wrong-password
```

Since the password does not match any consumer credential, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"Invalid user authorization"}
```

3. Send a request with the correct basic authentication credential:

```
curl -i "http://127.0.0.1:9080/ip" -u alice:alice-password 
```

With the correct credential in the request, you will receive an `HTTP/1.1 200 OK` response.

## Enable JWT Authentication for APIs[â](#enable-jwt-authentication-for-apis "Direct link to Enable JWT Authentication for APIs")

### For a Service[â](#for-a-service-2 "Direct link to For a Service")

To use JWT authentication for all routes in a service, enable the [JWT Auth Plugin](https://docs.api7.ai/hub/jwt-auth.md) on the service.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the `jwt-auth` plugin, then click **Enable**.
4. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the service configuration to use JWT authentication:

adc-service.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    plugins:
      jwt-auth:
        _meta:
          disable: false
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc-consumer.yaml -f adc-service.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

ApisixService custom resource is not yet available.

### For a Single Route[â](#for-a-single-route-2 "Direct link to For a Single Route")

* Dashboard
* ADC
* Ingress Controller

To use JWT authentication for a specific route, enable the [JWT Auth Plugin](https://docs.api7.ai/hub/jwt-auth.md) on the route instead of the service.

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Routes** from the side navigation bar.
3. Select your target route, for example, `get-ip`.
4. In the **Plugin** field, click **Enable Plugin**.
5. Search for the `jwt-auth` plugin, then click **Enable**.
6. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the route configuration to use JWT authentication:

adc-route.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
        plugins:
          jwt-auth:
            _meta:
              disable: false
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc-consumer.yaml -f adc-route.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

Create a Kubernetes manifest file for a route, where JWT authentication is enabled:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: get-ip
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
        methods:
          - GET
      backends:
        - serviceName: httpbin
          servicePort: 80
      authentication:
        enable: true
        type: jwtAuth
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

### Expose JWT Signing Endpoint[â](#expose-jwt-signing-endpoint "Direct link to Expose JWT Signing Endpoint")

This is a preliminary step to expose the JWT signing endpoint in API7 Enterprise. If you are using symmetric algorithms such as HS256 (default) or HS512 where API7 Enterprise will be both the JWT issuer and validator, this step is mandatory. If you are using asymmetric algorithms such as RS256 or ES256, this step is optional as the issuer and validator can be different parties.

The jwt-auth plugin creates an internal endpoint at /apisix/plugin/jwt/sign to sign JWT. Expose the endpoint with the [Public API Plugin](https://docs.api7.ai/hub/public-api.md):

1. Add a published service named `jwt-auth-api`, and a route with name `jwt-auth-api` and path `/api7/plugin/jwt/sign`
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the `public-api` plugin, then click **Enable**.
4. In the dialog box do the following:

* Add an empty configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

### Validate JWT Authentication[â](#validate-jwt-authentication "Direct link to Validate JWT Authentication")

Create a consumer with JWT credentials by following [configure JWT authentication credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md#configure-varied-authentication-credentials).

Follow the steps below to validate the JWT authentication.

1. Send a request without the credential:

```
curl -i "http://127.0.0.1:9080/ip"  
```

Since the credential is not provided, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"Missing authorization in request"}
```

2. Get JWT token with `key` from the consumer's JWT credential:

```
jwt_token=$(curl -s "http://127.0.0.1:9080/apisix/plugin/jwt/sign?key=john-jwt-key") && echo $jwt_token
```

3. Send a request to your API with `jwt_token` in the header:

```
curl -i "http://127.0.0.1:9080/ip" -H "Authorization: ${jwt_token}"
```

With the correct credential in the request, you will receive an `HTTP/1.1 200 OK` response.

In 30 seconds, the token should expire. Send a request with the same token to verify, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"failed to verify jwt"}
```

## Enable HMAC Authentication for APIs[â](#enable-hmac-authentication-for-apis "Direct link to Enable HMAC Authentication for APIs")

### For a Service[â](#for-a-service-3 "Direct link to For a Service")

To use HMAC authentication for all routes in a service, enable the [HMAC Auth Plugin](https://docs.api7.ai/hub/hmac-auth.md) on the service.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the `hmac-auth` plugin, then click **Enable**.
4. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the service configuration to use JWT authentication:

adc-service.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    plugins:
      jwt-auth:
        _meta:
          disable: false
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc-consumer.yaml -f adc-service.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

ApisixService custom resource is not yet available.

### For a Single Route[â](#for-a-single-route-3 "Direct link to For a Single Route")

* Dashboard
* ADC
* Ingress Controller

To use HMAC authentication for a specific route, enable the [HMAC Auth Plugin](https://docs.api7.ai/hub/hmac-auth.md) on the route instead of the service.

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Routes** from the side navigation bar.
3. Select your target route, for example, `get-ip`.
4. In the **Plugin** field, click **Enable Plugin**.
5. Search for the `hmac-auth` plugin, then click **Enable**.
6. In the dialog box do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
  }
  ```

* Click **Enable**.

Update the route configuration to use HMAC authentication:

adc-route.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
        plugins:
          jwt-auth:
            _meta:
              disable: false
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc-consumer.yaml -f adc-route.yaml
```

note

ADC uses the configuration files as the single source of truth. So make sure to pass both the consumer and service configuration files to the `adc sync` command for both configurations to take effect.

Create a Kubernetes manifest file for a route, where HMAC authentication is enabled:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: get-ip
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
        methods:
          - GET
      backends:
        - serviceName: httpbin
          servicePort: 80
      authentication:
        enable: true
        type: hmacAuth
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

### Validate HMAC Authentication[â](#validate-hmac-authentication "Direct link to Validate HMAC Authentication")

Create a consumer with HMAC credentials by following [configure HMAC authentication credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md#configure-varied-authentication-credentials).

Follow the steps below to validate the HMAC authentication.

1. Generate a signature

You can use the below Python snippet or other stack of your choice:

hmac-sig-header-gen.py

```
import hmac
import hashlib
import base64
from datetime import datetime, timezone
key_id = "john-key"                # key id
secret_key = b"john-hmac-key"      # secret key
request_method = "GET"             # HTTP method
request_path = "/headers"          # route URI
algorithm= "hmac-sha256"           # can use other algorithms in allowed_algorithms
# get current datetime in GMT
# note: the signature will become invalid after the clock skew (default 300s)
# you can regenerate the signature after it becomes invalid, or increase the clock
# skew to prolong the validity within the advised security boundary
gmt_time = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
# construct the signing string (ordered)
# the date and any subsequent custom headers should be lowercased and separated by a
# single space character, i.e. `<key>:<space><value>`
# https://datatracker.ietf.org/doc/html/draft-cavage-http-signatures-12#section-2.1.6
signing_string = (
  f"{key_id}\n"
  f"{request_method} {request_path}\n"
  f"date: {gmt_time}\n"
)

# create signature
signature = hmac.new(secret_key, signing_string.encode('utf-8'), hashlib.sha256).digest()
signature_base64 = base64.b64encode(signature).decode('utf-8')

# construct the request headers
headers = {
  "Date": gmt_time,
  "Authorization": (
    f'Signature keyId="{key_id}",algorithm="{algorithm}",'
    f'headers="@request-target date",'
    f'signature="{signature_base64}"'
  )
}

# print headers
print(headers)
```

Run the Script:

```
python3 hmac-sig-header-gen.py
```

2. Send a request without the headers:

```
curl -i "http://127.0.0.1:9080/ip"  
```

Since the credential is not provided, you will receive an `HTTP/1.1 401 Unauthorized` response with the following response body:

```
{"message":"Missing authorization in request"}
```

3. Send a request to your API with the headers:

```
curl -X GET "http://127.0.0.1:9080/ip" \
  -H "Date: Fri, 06 Sep 2024 06:41:29 GMT" \
  -H 'Authorization: Signature keyId="alice-keyid",algorithm="hmac-sha256",headers="@request-target date",signature="wWfKQvPDr0wHQ4IHdluB4IzeNZcj0bGJs2wvoCOT5rM="'
```

With the correct credential in the request, you will receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "headers":{
    "Accept": "*/*",
    "Authorization": "Signature keyId=\"john-key\",aigorithm=\'hmac-sha256\",headers=\"@reques
    t-target date\", signature=\'HtQm1m8kGvnVlztZ59)XokweovFqQN04Ui6P6NfzjRr4=\'"
    "Date": "Tue, 24 Sep 2024 10:28:41 GMT",
    "Host": "127.0.0.1",
    "User-Agent":"curl/8.7.1",
    "X-Amzn-Trace-Id": "Root=1-66f29481-7355340a05778cbb21e9b25a",
    "X-Consumer-Username": "John",
    "X-Credential-Identifier": "4130bb4a-0fdc-461d-be8d-2bba8a1e36dc",
    "X-Forwarded-Host": "127.0.0.1"
}
}
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)

* API Consumption

  <!-- -->

  * [Manage Consumer Credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md)
  * [Apply list-based access control](https://docs.api7.ai/enterprise/3.3.x/api-consumption/consumer-restriction.md)

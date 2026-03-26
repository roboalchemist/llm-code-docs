# Source: https://docs.api7.ai/hub/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-consumption/consumer-restriction.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-consumption/consumer-restriction.md

# Apply List-Based Access Control

Sometimes, you will require more precise access control than what authentication plugins offer. For example, you might want to keep a whitelist of [consumers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md) who can access your API. Now, a consumer must send an authenticated request and be on the whitelist (and not on the blacklist) to access the API.

note

Consider if the [API Portal](https://docs.api7.ai/enterprise/3.3.x/key-concepts/api-portal.md) is a better solution before implementing consumer-based access control.

This tutorial guides you in configuring precise access control by creating a consumer whitelist through the `consumer-restriction` plugin.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).
3. [Have a consumer with credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md).

## Apply Consumer Whitelist[â](#apply-consumer-whitelist "Direct link to Apply Consumer Whitelist")

When a consumer makes an authenticated request, API7 Gateway passes on the consumer's name to the routes. So, the routes do not need to access the consumer's credentials directly, which is more user-friendly.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to configure, for example, `httpbin` with version `1.0.0`.
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the [Consumer Restriction Plugin](https://docs.api7.ai/hub/consumer-restriction.md), then click **Enable**.
4. In the dialog box, do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
    "whitelist": [
      "Alice"
    ]
  }
  ```

  If you had followed the prerequisite tutorial, you would already have a consumer `Alice` with key authentication credentials.

* Click **Enable**.

5. Create a new consumer `Lisa` with key authentication credentials where **Key** is `lisa-key`.

Update your ADC configuration as such:

adc.yaml

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
      consumer-restriction:
        whitelist:
          - Alice
consumers:
  - username: Alice
    credentials:
      - name: primary-key
        type: key-auth
        config:
          key: alice-primary-key
  - username: Lisa
    credentials:
      - name: lisa-key
        type: key-auth
        config:
          key: lisa-key
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc.yaml
```

Ingress Controller currently does not support ApisixService resource.

To configure the `consumer-restriction` plugin on a route, update your Kubernetes manifest file of the route as such:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: httpbin
  namespace: api7   # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
      backends:
        - serviceName: httpbin
          servicePort: 80
      plugins:
      - name: consumer-restriction
        enable: true
        config:
          whitelist:
          - alice
```

Create another Kubernetes manifest file to configure a consumer `lisa` using the ApisixConsumer custom resource:

consumer.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  name: lisa
  namespace: api7   # replace with your namespace
spec:
  authParameter:
    keyAuth:
      value:
        key: "lisa-key"
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml -f consumer.yaml
```

### Validate[â](#validate "Direct link to Validate")

Make a request to the service as the consumer `Alice`:

```
curl -i "http://127.0.0.1:9080/ip" -H "apikey: alice-primary-key" 
```

You will see that the request is successful with a `200 OK` response because the consumer `Alice` is in the whitelist.

Now, make a request to the service as the newly created consumer `Lisa`:

```
curl -i "http://127.0.0.1:9080/ip" -H "apikey: lisa-key" 
```

You will receive a `403 Forbidden` response with the following response body as the consumer `Lisa` was not added to the whitelist:

```
{"message":"The consumer_name is forbidden."}
```

## Apply Consumer Blacklist[â](#apply-consumer-blacklist "Direct link to Apply Consumer Blacklist")

The `consumer-restriction` plugin prioritizes the blacklist over the whitelist when determining access.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then select the service you want to configure, for example, `httpbin` with version `1.0.0`.
2. Select **Plugins** from the side navigation bar, then click **Enable Plugin**.
3. Search for the `consumer-restriction` plugin, then click **Enable**.
4. In the dialog box, do the following:

* Add the following configuration to the **JSON Editor**:

  ```
  {
    "blacklist": [
      "Lisa"
    ]
  }
  ```

  If you had followed the prerequisite tutorial, you would already have a consumer `Alice` with key authentication credentials.

* Click **Enable**.

5. Create a new consumer `Lisa` with key authentication credentials where **Key** is `lisa-key`.

Update your ADC configuration as such:

adc.yaml

```
services:
  - name: httpbin Service
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    plugins:
      consumer-restriction:
        blacklist:
          - Lisa
consumers:
  - username: Alice
    credentials:
      - name: alice-primary-key
        type: key-auth
        config:
          key: alice-primary-key
  - username: Lisa
    credentials:
      - name: lisa-primary-key
        type: key-auth
        config:
          key: lisa-key
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc.yaml
```

Ingress Controller currently does not support ApisixService resource.

To configure the `consumer-restriction` plugin on a route, update your Kubernetes manifest file of the route as such:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: httpbin
  namespace: api7   # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
      backends:
        - serviceName: httpbin
          servicePort: 80
      plugins:
      - name: consumer-restriction
        enable: true
        config:
          blacklist:
          - lisa
```

Create another Kubernetes manifest file to configure a consumer `lisa` using the ApisixConsumer custom resource:

consumer.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  name: lisa
  namespace: api7   # replace with your namespace
spec:
  authParameter:
    keyAuth:
      value:
        key: "lisa-key"
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml -f consumer.yaml
```

### Validate[â](#validate-1 "Direct link to Validate")

Make a request to the service as the consumer `Alice`:

```
curl -i "http://127.0.0.1:9080/ip" -H "apikey: alice-primary-key" 
```

You will see that the request is successful with a `200 OK` response because the consumer `Alice` is not in the blacklist.

Now, make a request to the service as the newly created consumer `Lisa`:

```
curl -i "http://127.0.0.1:9080/ip" -H "apikey: lisa-key" 
```

You will receive a `403 Forbidden` response with the following response body as the consumer `Lisa` was added to the blacklist:

```
{"message":"The consumer_name is forbidden."}
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)
  * [Consumers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md)

* API Security
  <!-- -->
  * [Set up API authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md)

* API Consumption
  <!-- -->
  * [Manage consumer credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md)

* Plugin Hub
  <!-- -->
  * [Consumer Restriction](https://docs.api7.ai/hub/consumer-restriction.md)

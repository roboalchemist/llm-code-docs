# Source: https://docs.api7.ai/enterprise/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-security/mask-data.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-security/mask-data.md

# Mask Sensitive Data in Logs

Data masking is a data protection technology aimed at preventing the exposure of sensitive information in various environments, thus supporting secure application testing and data analysis without compromising privacy.

The built-in [`data-mask`](https://docs.api7.ai/hub/data-mask) plugin provided by API7 Enterprise can help remove or replace sensitive information in request headers, request bodies, and URL queries.

This guide will walk you through masking sensitive information in the URL-encoded request bodies using API7 Enterprise. The [`file-logger`](https://apisix.apache.org/docs/apisix/plugins/file-logger/) plugin used for logging in the example is only to show that information has been successfully masked. Adjust accordingly per your use case.

Below is an interactive demo providing a hands-on introduction to masking sensitive data in logs.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
* [Have a running API in the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Enable `data-mask` and `file-logger` Plugins[â](#enable-data-mask-and-file-logger-plugins "Direct link to enable-data-mask-and-file-logger-plugins")

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, a no-version `httpbin` service.

2. Under the published service, select **Routes** from the side navigation bar.

3. Select your target route, for example, `/anything`.

4. Click **+ Enable Plugin**.

5. Search for the `data-mask` plugin.

6. Click **Enable**.

7. In the dialog box, do the following:

   * Add the following configuration to the **JSON Editor**:

   ```
   {
   "request": [
   {
       "action": "remove",
       "body_format": "json",
       "name": "$.password",
       "type": "body"
   },
   {
       "action": "replace",
       "body_format": "json",
       "name": "users[*].token",
       "type": "body",
       "value": "*****"
   },
   {
       "action": "regex",
       "body_format": "json",
       "name": "$.users[*].credit.card",
       "regex": "(\\d+)\\-\\d+\\-\\d+\\-(\\d+)",
       "type": "body",
       "value": "$1-****-****-$2"
   }
   ]
   }
   ```

   * Click **Enable**.

8. Under the same route, click **+ Enable Plugin**.

9. Search for the `file-logger` plugin.

10. Click **Enable**.

11. In the dialog box, do the following:

    * Add the following configuration to the **JSON Editor**:

    ```
    {
    "include_req_body": true,
    "path": "/tmp/mask-urlencoded-body.log"
    }
    ```

    * Click **Enable**.

Update the ADC configuration file with the `data-mask` and `file-logger` plugins:

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
    routes:
      - uris:
          - /anything
        name: getting-started-anything
        methods:
          - GET
        plugins:
          data-mask:
            request:
              - action: remove
                body_format: urlencoded
                name: $.password
                type: body
              - action: replace
                body_format: urlencoded
                name: users[*].token
                type: body
                value: "*****"
              - action: regex
                body_format: urlencoded
                name: $.users[*].credit.card
                regex: (\d+)\-\d+\-\d+\-(\d+)
                type: body
                value: $1-****-****-$2
          file-logger:
            include_req_body: true
            path: /tmp/mask-urlencoded-body.log
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc.yaml
```

Update the Kubernetes manifest file of the selected route with `data-mask` and `file-logger` plugins:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: httpbin-route
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: httpbin-route
      match:
        paths:
          - /anything
        methods:
          - GET
      backends:
        - serviceName: httpbin
          servicePort: 80
      plugins:
        - name: data-mask
          enable: true 
          config:
            request:
              - action: remove
                body_format: urlencoded
                name: $.password
                type: body
              - action: replace
                body_format: urlencoded
                name: "users[*].token"
                type: body
                value: "*****"
              - action: regex
                body_format: urlencoded
                name: $.users[*].credit.card
                regex: (\\d+)\\-\\d+\\-\\d+\\-(\\d+)
                type: body
                value: $1-****-****-$2
        - name: file-logger
          enable: true 
          config:
            include_req_body: true
            path: /tmp/mask-urlencoded-body.log
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

## Validate[â](#validate "Direct link to Validate")

1. To validate, send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything" \
  --data-urlencode "password=abc" \
  --data-urlencode "token=xyz" \
  --data-urlencode "card=1234-1234-1234-1234"
```

You should receive an `HTTP/1.1 200 OK` response.

2. Go to your docker, navigate to the `/tmp/mask-urlencoded-body.log` file and examine the log content, you should see a log entry similar to the following:

```
{
  "request": {
    "uri": "/anything",
    "body": "token=*****&card=1234-****-****-1234",
    "method": "POST",
    "url": "http://127.0.0.1:9080/anything"
  }
}
```

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Getting Started
  <!-- -->
  * [Launch Your First API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md)
* Plugin Hub
  <!-- -->
  * [data-mask](https://docs.api7.ai/hub/data-mask)

# Source: https://docs.api7.ai/enterprise/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/canary-upstream.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/canary-upstream.md

# Configure Canary Traffic Shifting

Canary traffic shifting enables testing new [upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md) safely by gradually routing a small portion of traffic to the new upstream while keeping most traffic to the stable baseline upstream. This incremental approach mitigates risk by containing potential issues to a limited number of users, allowing you to identify and resolve problems without impacting your broader user base.

note

Canary traffic shifting differs from a canary release as the API/service version is unchanged. Canary release refers to the simultaneous operation and availability of two versions of the same API/service.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Shift Traffic by Weight Percentage[â](#shift-traffic-by-weight-percentage "Direct link to Shift Traffic by Weight Percentage")

In this example, you will direct 10% of the traffic to a canary upstream. The remaining 90% will continue to be forwarded to the baseline upstream. And gradually direct 50% and 100% of the traffic to the canary upstream.

note

The canary rule applies to all routes in a service and cannot be applied to individual routes.

After the new canary upstream is tested, all traffic can be routed to the canary upstream and it becomes the new baseline upstream. The older baseline upstream can then be removed.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, `httpbin` with version `1.0.0`.

2. Under the published service, select **Upstreams** from the side navigation bar.

3. In the **Connection Configuration** module, click **Edit**, choose `Use Node Host`, and click **Save**.

   <!-- -->

   > Note: Since `mock.api7.ai` enforces HTTPS access, the upstream needs to be configured to use port `443` for the HTTPS endpoint. The `pass_host` parameter must be changed to nodes to ensure a successful handshake with the upstream. Adjust accordingly per your use case.

4. In the **Canary Rules** field, click **Start Canary**.

5. In the dialog box, do the following:

* In the **Weight** field, enter `10`.
* In the **Condition** field, keep the button off.
* Click **Next**.

6. In the **Canary Upstream** field, keep the default setting: `Create a new upstream`.

* Modify the name of the new upstream to `newupstream`.
* Click **Edit** to adjust the host of the node to point to the new backend. For example, use `mock.api7.ai` as the host and `443` as the port.
* Keep the other properties the same as the baseline upstream.

7. Confirm the displayed information and click **Start**. The canary rules start working immediately.

8. Validate the canary rules by sending 10 requests:

   ```
   for i in {1..10}; do "curl 127.0.0.1:9080/headers";  done
   ```

   9 requests will be sent to the baseline upstream address, `httpbin.org`, and you will receive the following response:

   ```
   {
     "headers": {
       "Accept": "*/*",
       "Host": "httpbin.org",
       "User-Agent": "curl/7.74.0",
       "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
       "X-Forwarded-Host": "127.0.0.1"
     }
   }
   ```

   A single request will be sent to the canary upstream address, `mock.api7.ai`:

   ```
   {
     "headers": {
       "accept": "*/*",
       "accept-encoding": "gzip, br",
       "cf-connecting-ip": "159.89.160.194",
       "cf-ipcountry": "IN",
       "cf-ray": "888e28733f9604aa",
       "cf-visitor": "{\"scheme\":\"https\"}",
       "connection": "Keep-Alive",
       "content-type": "application/json",
       "host": "mock.api7.ai",
       "user-agent": "curl/7.74.0",
       "x-application-owner": "API7.ai",
       "x-forwarded-for": "127.0.0.1",
       "x-forwarded-host": "127.0.0.1",
       "x-forwarded-port": "9080",
       "x-forwarded-proto": "https",
       "x-real-ip": "159.89.160.194",
       "X-Application-Owner": "API7.ai",
       "Content-Type": "application/json"
     }
   }
   ```

9. In the **Canary Rules** field, click **Actions** and **Edit**.

10. In the dialog box, do the following:

* Adjust the weight to `50%`.
* Click **Save**.

11. Make more requests to test the canary upstream, until it meets your expectations.
12. In the **Canary Rules** field, click **Actions** and **Finish**.
13. In the dialog box, do the following:

* In the **Baseline Upstream** field, choose `Canary Upstream: newupstream`.
* In the **Delete Unselected Upstream: Default Upstream** field, keep the button on.
* Click **Finish**.

Below is an interactive demo for this use case. Click and follow the steps in this demo, you will better understand how to use it in API7 Enterprise.

Update your ADC configuration file (`adc.yaml`) to include the canary upstream. The complete configuration is given below:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: Test Group
      scheme: https
      nodes:
        - host: httpbin.org
          port: 443
          weight: 100
    plugins:
      api7-traffic-split:
        rules:
          - canary_upstreams:
              - upstream_name: newupstream
                weight: 10
              - weight: 90
        upstreams:
          - name: newupstream
            nodes:
              - host: mock.api7.ai
                port: 443
                weight: 100
            scheme: https
    routes:
      - uris:
          - /headers
        name: getting-started-headers
        methods:
          - GET
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc.yaml
```

Validate the canary rules by sending 10 requests:

```
for i in {1..10}; do curl "127.0.0.1:9080/headers";  done
```

9 requests will be sent to `httpbin.org` and you will receive the following response:

```
{
 "headers": {
   "Accept": "*/*",
   "Host": "httpbin.org",
   "User-Agent": "curl/7.74.0",
   "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
   "X-Forwarded-Host": "127.0.0.1"
 }
}
```

A single request will be sent to `mock.api7.ai`:

```
{
 "headers": {
   "accept": "*/*",
   "accept-encoding": "gzip, br",
   "cf-connecting-ip": "159.89.160.194",
   "cf-ipcountry": "IN",
   "cf-ray": "888e28733f9604aa",
   "cf-visitor": "{\"scheme\":\"https\"}",
   "connection": "Keep-Alive",
   "content-type": "application/json",
   "host": "mock.api7.ai",
   "user-agent": "curl/7.74.0",
   "x-application-owner": "API7.ai",
   "x-forwarded-for": "127.0.0.1",
   "x-forwarded-host": "127.0.0.1",
   "x-forwarded-port": "9080",
   "x-forwarded-proto": "https",
   "x-real-ip": "159.89.160.194",
   "X-Application-Owner": "API7.ai",
   "Content-Type": "application/json"
 }
}
```

Now, update the weights to `50:50` to allow half of the traffic to be routed to the canary upstream:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: Test Group
      scheme: https
      nodes:
        - host: httpbin.org
          port: 443
          weight: 100
    plugins:
      api7-traffic-split:
        rules:
          - canary_upstreams:
              - upstream_name: newupstream
                weight: 50
              - weight: 50
        upstreams:
          - name: newupstream
            nodes:
              - host: mock.api7.ai
                port: 443
                weight: 100
            scheme: https
    routes:
      - uris:
          - /headers
        name: getting-started-headers
        methods:
          - GET
```

Send more requests to test the canary upstream. Finally, update the old upstream with the current upstream to finish the canary traffic shifting:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: Test Group
      scheme: https
      nodes:
        - host: mock.api7.ai
          port: 443
          weight: 100
    routes:
      - uris:
          - /headers
        name: getting-started-headers
        methods:
          - GET
```

You can also keep the old upstream as a canary upstream with a `0` weight to roll back to if there are issues with the new upstream.

ApisixService custom resource is required for the `api7-traffic-split` plugin and is unavailable.

## Shift Traffic by Condition: Request Header[â](#shift-traffic-by-condition-request-header "Direct link to Shift Traffic by Condition: Request Header")

In this example, you will direct requests with the header `version = test` to the canary upstream, while the remaining traffic will continue to the baseline upstream. The canary rule applies to all routes in a service and cannot be applied to individual routes.

* Dashboard
* ADC
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the service, select **Upstreams** from the side navigation bar.
3. In the **Canary Rules** field, click **Start Canary**.
4. In the dialog box, do the following:

* In the **Weight** field, enter `100`.
* In the **Condition** field, turn on the button.
* Fill in the header requirement with `header` evaluation `version == test`.
* Click **Next**.

5. In the **Canary Upstream** field, choose `Create a new upstream`.

* Modify the name of the new upstream to `newupstream`.
* Click **Edit** to adjust the host of the node to point to the new backend. For example, use `mock.api7.ai` as the host and `443` as the port. Then click **Save**.
* Keep the other properties the same as the baseline upstream.

6. Confirm the displayed information and click **Start**. The canary rules start working immediately.

7. Validate the canary rules by sending requests:

   * Send a request with the `version:test` header:

   ```
   curl 127.0.0.1:9080/headers -H "version:test"
   ```

   You shall receive the following response from the canary upstream:

   ```
   {
     "headers": {
       "accept": "*/*",
       "accept-encoding": "gzip, br",
       "cf-connecting-ip": "159.89.160.194",
       "cf-ipcountry": "IN",
       "cf-ray": "888e28733f9604aa",
       "cf-visitor": "{\"scheme\":\"https\"}",
       "connection": "Keep-Alive",
       "content-type": "application/json",
       "host": "mock.api7.ai",
       "user-agent": "curl/7.74.0",
       "x-application-owner": "API7.ai",
       "x-forwarded-for": "127.0.0.1",
       "x-forwarded-host": "127.0.0.1",
       "x-forwarded-port": "9080",
       "x-forwarded-proto": "https",
       "x-real-ip": "159.89.160.194",
       "X-Application-Owner": "API7.ai",
       "Content-Type": "application/json"
     }
   }
   ```

   * Send a request with the wrong header:

   ```
   curl 127.0.0.1:9080/headers -H "version:new"
   ```

   You shall receive the following response from the baseline upstream:

   ```
   {
     "headers": {
       "Accept": "*/*",
       "Host": "httpbin.org",
       "User-Agent": "curl/7.74.0",
       "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
       "X-Forwarded-Host": "127.0.0.1"
     }
   }
   ```

   * Send a request with no header:

   ```
   curl 127.0.0.1:9080/headers
   ```

   * You shall receive the following response from the baseline upstream:

   ```
   {
     "headers": {
       "Accept": "*/*",
       "Host": "httpbin.org",
       "User-Agent": "curl/7.74.0",
       "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
       "X-Forwarded-Host": "127.0.0.1"
     }
   }
   ```

8. Make more requests to test the canary upstream, until it meets your expectations.

9. In the **Canary Rules** field, click **Finish**.

10. In the dialog box, do the following:

* In the **Baseline Upstream** field, choose `Canary Upstream: newupstream`.
* In the **Delete Unselected Upstream: Default Upstream** field, keep the button on.
* Click **Finish**.

Below is an interactive demo for this use case. Click and follow the steps in this demo, you will better understand how to use it in API7 Enterprise.

Update your ADC configuration file (`adc.yaml`) to include the canary upstream. The complete configuration is given below:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: https
      nodes:
        - host: httpbin.org
          port: 443
          weight: 100
    plugins:
      api7-traffic-split:
        rules:
          - canary_upstreams:
              - upstream_name: newupstream
                weight: 100
            match:
              - exprs:
                  - - http_version
                    - ==
                    - test
        upstreams:
          - name: newupstream
            nodes:
              - host: mock.api7.ai
                port: 443
                weight: 100
            scheme: https
    routes:
      - uris:
          - /headers
        name: getting-started-headers
        methods:
          - GET
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc.yaml
```

Validate the canary rules by sending a request with the `version:test` header:

```
curl 127.0.0.1:9080/headers  
```

You will get back a response from the canary upstream:

```
{
 "headers": {
   "accept": "*/*",
   "accept-encoding": "gzip, br",
   "cf-connecting-ip": "159.89.160.194",
   "cf-ipcountry": "IN",
   "cf-ray": "888e28733f9604aa",
   "cf-visitor": "{\"scheme\":\"https\"}",
   "connection": "Keep-Alive",
   "content-type": "application/json",
   "host": "mock.api7.ai",
   "user-agent": "curl/7.74.0",
   "x-application-owner": "API7.ai",
   "x-forwarded-for": "127.0.0.1",
   "x-forwarded-host": "127.0.0.1",
   "x-forwarded-port": "9080",
   "x-forwarded-proto": "https",
   "x-real-ip": "159.89.160.194",
   "X-Application-Owner": "API7.ai",
   "Content-Type": "application/json"
 }
}
```

Send a request with the wrong header:

```
curl 127.0.0.1:9080/headers -H "version:new"
```

You shall receive the following response from the baseline upstream:

```
{
 "headers": {
   "Accept": "*/*",
   "Host": "httpbin.org",
   "User-Agent": "curl/7.74.0",
   "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
   "X-Forwarded-Host": "127.0.0.1"
 }
}
```

Send a request with no header:

```
curl 127.0.0.1:9080/headers
```

You shall receive the following response from the baseline upstream:

```
{
 "headers": {
   "Accept": "*/*",
   "Host": "httpbin.org",
   "User-Agent": "curl/7.74.0",
   "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
   "X-Forwarded-Host": "127.0.0.1"
 }
}
```

Update the old upstream with the current upstream to finish the canary traffic shifting:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: Test Group
      scheme: https
      nodes:
        - host: mock.api7.ai
          port: 443
          weight: 100
    routes:
      - uris:
          - /headers
        name: getting-started-headers
        methods:
          - GET
```

You can also keep the old upstream as a canary upstream with a `0` weight to roll back to if there are issues with the new upstream.

ApisixService custom resource is required for the `api7-traffic-split` plugin and is unavailable.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concept

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md)

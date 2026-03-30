# Source: https://docs.api7.ai/ingress-controller/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/proxy-tcp-traffic.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/proxy-tcp-traffic.md

# Proxy TCP Traffic

API7 Gateway can handle transport layer (L4) TCP and UDP traffic dedicated or in addition to handling application layer (L7) traffic.

This tutorial walks through configuring a [stream route](https://docs.api7.ai/enterprise/3.3.x/key-concepts/stream-routes.md) within a [published service](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) to proxy L4 traffic between clients and a MySQL server.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md) in your gateway group.
3. Install a [MySQL client](https://dev.mysql.com/doc/refman/8.4/en/installing.html) to validate the stream route.

## Start a MySQL Server[â](#start-a-mysql-server "Direct link to Start a MySQL Server")

* Docker
* Kubernetes

If you have installed the gateway instance in Docker and use Dashboard or ADC for configurations, start a MySQL server in the default API7 Enterprise network `api7-ee_api7`:

```
docker run -d \
  --name mysql \
  --network=api7-ee_api7 \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=password \
  mysql:8.4 \
  mysqld --mysql-native-password=ON
```

If you have installed the gateway instance on Kubernetes and use Ingress Controller for configurations, start a MySQL server on Kubernetes:

```
kubectl run mysql --image mysql:8.4 --port 3306 --env="MYSQL_ROOT_PASSWORD=password"
```

Expose the server port through a service:

```
kubectl expose pod mysql --port 3306
```

## Enable Transport Layer (L4) Proxy[â](#enable-transport-layer-l4-proxy "Direct link to Enable Transport Layer (L4) Proxy")

By default, API7 Gateway (data plane) only has application layer (L7) proxy enabled. To also accept transport layer (L4) traffic, configure `proxy_mode` and `stream_proxy` in `config.yaml` [configuration file](https://docs.api7.ai/enterprise/3.3.x/reference/configuration.md) as follows:

```
docker exec {container_name} /bin/sh -c "echo '
apisix:
  proxy_mode: http&stream
  stream_proxy:
    tcp:
      - 2000
' > /usr/local/apisix/conf/config.yaml"
```

â¶ `proxy_mode`: accept both transport layer (L4) and application layer (L7) traffic.

â· `stream_proxy`: configure the interface for transport layer (L4) proxy.

Reload API7 Gateway for configuration changes to take effect:

* Docker
* Kubernetes

```
docker exec {container_name} apisix reload
```

```
kubectl edit configmap $YOUR_GATEWAY_CONFIGMAP
kubectl rollout restart deployment $YOUR_GATEWAY_DEPLOYMENT
```

## Add a Service with Stream Routes[â](#add-a-service-with-stream-routes "Direct link to Add a Service with Stream Routes")

* Dashboard
* ADC
* Ingress Controller

1. Select the **Published Services** of your gateway group from the side navigation bar, then click **Add Service**.
2. Select **Add Manually**.
3. From the dialog box, do the following:

* In the **Name** field, enter `MySQL`.

* In the **Service Type** field, choose `Stream(Layer 4 Proxy)`.

* In the **Upstream Scheme** field, choose `TCP`.

* In the **How to find the upstream** field, choose `Use Nodes`.

* Click **Add Node**.

* In the Add Node dialog box, do the following:

  <!-- -->

  * In the **Host** field, enter your private IP address, such as `192.168.2.103`.
  * In the **Port** field, enter `3306`.
  * In the **Weight** field, use the default value `100`.
  * Click **Add**. This will create a new service in the 'No Version' state.

5. Inside the service, click **Add Stream Route**.
6. Inside the service, click **Add Stream Route**.

* In the **Name** field, enter `stream-route-mysql`.
* In the **Server Address** field, enter `127.0.0.1`.
* In the **Server Port** field, enter `2000`.
* Click **Add**.

To use ADC to create a stream route, use the following configuration:

adc.yaml

```
services:
  - name: MySQL
    upstream:
      name: default
      scheme: tcp
      nodes:
        - host: 127.0.0.1
          port: 3306
          weight: 100
    stream_routes:
      - name: stream-route-mysql
        server_addr: 127.0.0.1
        server_port: 2000
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc.yaml
```

Create a Kubernetes manifest file to configure a stream route using the ApisixRoute custom resource:

stream-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: stream-route-mysql
  namespace: api7
spec:
  stream:
    - name: stream-route-mysql
      protocol: TCP
      match:
        ingressPort: 2000
      backend:
        serviceName: mysql
        servicePort: 3306
```

Apply the configuration to your cluster:

```
kubectl apply -f stream-route.yaml
```

You should see a response of the following:

```
apisixroute.apisix.apache.org/stream-route-mysql created
```

## Validate the Stream Route[â](#validate-the-stream-route "Direct link to Validate the Stream Route")

* Docker
* Kubernetes

If you have installed the gateway instance in Docker and use Dashboard or ADC for configurations, before you can proceed to the verification steps, make sure to expose the server port `2000` to the host machine (`-p2000:2000`).

If you have installed the gateway instance on Kubernetes and use Ingress Controller for configurations, to add the service port, edit the service:

```
kubectl edit svc/api7-ee-3-gateway-gateway
```

Add the service port for MySQL:

```
spec:
  ports:
    ...
    - name: apisix-gateway-mysql
      port: 2000
      protocol: TCP
      targetPort: 2000
    ...
```

Port forward `2000` for the service:

```
kubectl port-forward svc/api7-ee-3-gateway-gateway 2000:2000 &
```

Establish a connection with the MySQL server through API7 Gateway using the MySQL client. Connect as root using the password configured before:

```
mysql --host=127.0.0.1 --port=2000 -u root -p
```

You should see the MySQL prompt as shown below:

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.4.0 MySQL Community Server - GPL
 
Copyright (c) 2000, 2024, Oracle and/or its affiliates.
 
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
 
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
 
mysql>
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md)

* Getting Started
  <!-- -->
  * [Publish Service Version](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md)

* Best Practices
  <!-- -->
  * [API Version Control](https://docs.api7.ai/enterprise/3.3.x/best-practices/api-version-control.md)

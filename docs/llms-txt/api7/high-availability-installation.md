# Source: https://docs.api7.ai/enterprise/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.8.x/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.7.x/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.6.x/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.5.x/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.4.x/high-availability/high-availability-installation.md

# Source: https://docs.api7.ai/enterprise/3.3.x/high-availability/high-availability-installation.md

# High Availability Installation

This document describes how to configure API7 Gateway High Availability in the following aspects:

* Control plane

  <!-- -->

  * API7 Dashboard
  * DP Manager

* Data plane
  <!-- -->
  * API7 Gateway

Not covered:

* PostgreSQL
* Prometheus

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Finish [Prepare for high availability](https://docs.api7.ai/enterprise/3.3.x/high-availability/prepare-for-high-availability.md).
2. Install PostgreSQL (Version 15) and Prometheus (optional, Version 2.48).

## Control Plane[â](#control-plane "Direct link to Control Plane")

API7 Dashboard is the major component of the control plane, which is a Web GUI and processes the business logic. API7 Dashboard is a stateless service, and all the data information is stored in PostgreSQL.

To ensure high availability, you require a control plane cluster that contains multiple control plane nodes. Additionally, it is essential to deploy a load balancer in front of all the control plane nodes. If a node fails, the load balancer can remove it from the pool, ensuring that traffic is not sent to unavailable nodes.

For all control plane nodes, do the following:

1. Copy control plane package to the host machine. You can get the proper package from [preparing for high availability](https://docs.api7.ai/enterprise/3.3.x/high-availability/prepare-for-high-availability.md).
2. Configure `dashboard-config.yaml` to modify the database address:

```
server:
  listen:
    host: "0.0.0.0"
    port: 17080

database:
  dsn: "postgres://$user:$password@$postgresql_address:$postgresql_port/api7ee"
```

3. Start API7 Dashboard:

```
docker run -d -p 17080:17080 -v ./dashboard-config.yaml:/app/conf/config.yaml api7/api7-ee-3-integrated:v3.2.16.3
```

4. Configure `dp-manager-config.yaml` to modify the database address:

```
server:
  listen:
    host: "0.0.0.0"
    port: 17900

database:
  dsn: "postgres://$user:$password@$postgresql_address:$postgresql_port/api7ee"
```

5. Start DP Manager:

```
docker run -d -p 17900:17900 -v ./dp-manager-config.yaml:/usr/local/api7/conf/config.yaml api7/api7-ee-dp-manager:v3.2.16.3
```

## Data Plane[â](#data-plane "Direct link to Data Plane")

API7 Gateway is in charge of accepting traffic from the client and forwarding it to upstreams, so a data plane node can also be called a gateway instance. The API7 Gateway is a stateless component, and all configuration information is stored in PostgreSQL. Therefore, you can deploy multiple nodes to improve the high availability of the data plane.

### Add Gateway Groups[â](#add-gateway-groups "Direct link to Add Gateway Groups")

To ensure high availability, you require a data plane cluster that contains multiple data plane nodes. The data plane cluster can also be called a [Gateway Group](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md). Refer to [Add gateway groups](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-group.md) for instructions.

### Health Check[â](#health-check "Direct link to Health Check")

Deploying a load balancer in front of data plane nodes and enabling health checks are crucial for maintaining high availability and ensuring traffic is not routed to unhealthy nodes.

1. Configure `gateway_conf/config.yaml` to add `status` block for listening interface:

```
apisix:
  status:
    ip: 0.0.0.0
    port: 7085
```

2. Set the load balancer to poll the health check interface at regular intervals. Determine the appropriate frequency for health checks based on your specific requirements and the expected response time of your applications. A common practice is to set health checks to probe every 30 seconds.

```
curl "http://127.0.0.1:7085/status" -v
```

If the data plane is healthy, you should see the following `200 OK` response:

```
*   Trying 127.0.0.1:7085...
* Connected to 127.0.0.1 (127.0.0.1) port 7085 (#0)
> GET /status HTTP/1.1
> Host: 127.0.0.1:7085
> User-Agent: curl/7.74.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: openresty
< Date: Thu, 17 Oct 2024 06:27:38 GMT
< Content-Type: text/plain; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
<
* Connection #0 to host 127.0.0.1 left intact
```

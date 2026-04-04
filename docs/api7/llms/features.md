# Source: https://docs.api7.ai/enterprise-whitepaper/features.md

# Features

## API and Service Governance[â](#api-and-service-governance "Direct link to API and Service Governance")

### Protocols[â](#protocols "Direct link to Protocols")

| Feature                                  | API7 | Kong | Zuul2 | NGINX |
| ---------------------------------------- | ---- | ---- | ----- | ----- |
| HTTP/1.1 and HTTP 2                      | Y    | Y    | Y     | Y     |
| HTTP/3                                   | Y    | Y    | N     | N     |
| TLS / HTTPS                              | Y    | Y    | Y     | Y     |
| MQTT                                     | Y    | N    | N     | N     |
| TCP                                      | Y    | Y    | N     | Y     |
| UDP                                      | Y    | Y    | N     | Y     |
| HTTP to gRPC/Dubbo conversion            | Y    | Y    | N     | N     |
| Websocket                                | Y    | Y    | Y     | Y     |
| Dubbo                                    | Y    | N    | N     | N     |
| Customized Layer 4 and Layer 7 protocols | Y    | N    | N     | N     |

### Platforms[â](#platforms "Direct link to Platforms")

| Feature                                                    | API7 | Kong | Zuul2 | NGINX |
| ---------------------------------------------------------- | ---- | ---- | ----- | ----- |
| Bare Metal                                                 | Y    | Y    | Y     | Y     |
| Virtual Machines                                           | Y    | Y    | Y     | Y     |
| Kubernetes                                                 | Y    | Y    | Y     | Y     |
| ARM64                                                      | Y    | Y    | Y     | Y     |
| Kunpeng (certified by Huawei Cloud)                        | Y    | N    | N     | N     |
| AWS, GCP, Ali Cloud, Tencent Cloud and other public clouds | Y    | Y    | Y     | Y     |

### Fine-grained Routing[â](#fine-grained-routing "Direct link to Fine-grained Routing")

| Feature                                              | API7 | Kong | Zuul2 | NGINX |
| ---------------------------------------------------- | ---- | ---- | ----- | ----- |
| URI Parameter Matching                               | Y    | Y    | Y     | Y     |
| HTTP Header Matching                                 | Y    | Y    | N     | Y     |
| HTTP Request Method Matching                         | Y    | Y    | N     | Y     |
| Support for all NGINX variables matching             | Y    | N    | N     | Y     |
| Support for Lua snippets to implement custom matches | Y    | N    | N     | N     |
| Support for conditional expressions                  | Y    | N    | N     | N     |
| Support IPv6                                         | Y    | Y    | Y     | Y     |
| GeoIP Geological Location Matching                   | Y    | Y    | N     | N     |
| Routing Time To Live (TTL)                           | Y    | N    | N     | N     |
| Priority Matching                                    | Y    | Y    | Y     | N     |

### Load-Balance[â](#load-balance "Direct link to Load-Balance")

| Feature                                      | API7 | Kong | Zuul2 | NGINX |
| -------------------------------------------- | ---- | ---- | ----- | ----- |
| Round Robin                                  | Y    | Y    | Y     | Y     |
| Weighted Round Robin                         | Y    | Y    | Y     | Y     |
| Consistent Hash (Chash)                      | Y    | Y    | N     | Y     |
| Sticky Session                               | Y    | Y    | N     | N     |
| Least Connections                            | Y    | Y    | N     | Y     |
| EWMA                                         |      |      |       |       |
| Support for custom load balancing algorithms |      |      |       |       |

### Rewrite Request[â](#rewrite-request "Direct link to Rewrite Request")

| Feature                                     | API7 | Kong | Zuul2 | NGINX |
| ------------------------------------------- | ---- | ---- | ----- | ----- |
| URI Rewrite                                 | Y    | Y    | Y     | Y     |
| Add, modify and delete HTTP request headers | Y    | Y    | Y     | Y     |
| Support 301 and 302 Redirection             | Y    | Y    | Y     | Y     |
| Force a jump to HTTPS                       | Y    | Y    | N     | Y     |

### Rewrite Response[â](#rewrite-response "Direct link to Rewrite Response")

| Feature                                      | API7 | Kong | Zuul2 | NGINX |
| -------------------------------------------- | ---- | ---- | ----- | ----- |
| Add, modify and delete HTTP response headers | Y    | Y    | Y     | Y     |
| Modify HTTP response code                    | Y    | Y    | Y     | Y     |
| Modify response body                         | Y    | Y    | Y     | Y     |

### Service Discovery and Registration[â](#service-discovery-and-registration "Direct link to Service Discovery and Registration")

| Feature                                      | API7 | Kong | Zuul2 | NGINX |
| -------------------------------------------- | ---- | ---- | ----- | ----- |
| Default etcd and support for etcd clustering | Y    | N    | N     | N     |
| Consul                                       | Y    | N    | N     | N     |
| Eureka                                       | Y    | N    | Y     | N     |
| Nacos                                        | Y    | N    | N     | N     |
| Redis                                        | Y    | N    | N     | N     |

### Fault tolerance and downgrading[â](#fault-tolerance-and-downgrading "Direct link to Fault tolerance and downgrading")

| Feature                                  | API7 | Kong | Zuul2 | NGINX |
| ---------------------------------------- | ---- | ---- | ----- | ----- |
| Traffic Control/ Cluster Traffic Control | Y    | Y    | N     | N     |
| Rate Limit                               | Y    | Y    | N     | Y     |
| Concurrency Limit                        | Y    | Y    | Y     | Y     |
| Upstream Active Health Check             | Y    | Y    | N     | N     |
| Upstream Passive Health Check            | Y    | Y    | N     | Y     |
| Service Meltdown                         | Y    | Y    | Y     | Y     |
| Service Downgrade                        | Y    | Y    | Y     | N     |
| API Meltdown                             | Y    | Y    | N     | N     |
| Timeout                                  | Y    | Y    | Y     | Y     |

### Traffic Control[â](#traffic-control "Direct link to Traffic Control")

| Feature            | API7 | Kong | Zuul2 | NGINX |
| ------------------ | ---- | ---- | ----- | ----- |
| Canary Release     | Y    | Y    | N     | Y     |
| Blue-Green Release | Y    | Y    | N     | Y     |
| Traffic Mirroring  | Y    | N    | N     | Y     |
| Fault Injection    | Y    | N    | N     | N     |

### API Management[â](#api-management "Direct link to API Management")

| Feature                        | API7 | Kong | Zuul2 | NGINX |
| ------------------------------ | ---- | ---- | ----- | ----- |
| Multi API Aggregation          | Y    | N    | N     | N     |
| Version Management             | Y    | N    | N     | N     |
| Release and Abolish API        | Y    | N    | N     | N     |
| Swagger and OpenAPI            | Y    | N    | N     | N     |
| Generate SDK and documentation | Y    | N    | N     | N     |

### Plugins Management[â](#plugins-management "Direct link to Plugins Management")

| Feature                                                | API7 | Kong | Zuul2 | NGINX |
| ------------------------------------------------------ | ---- | ---- | ----- | ----- |
| Dynamically add, modify and delete plugins             | Y    | N    | Y     | N     |
| Plugin orchestration (low code)                        | Y    | N    | N     | N     |
| Support for writing custom plugins in Lua, Java and Go | Y    | Y    | N     | N     |

## Security[â](#security "Direct link to Security")

### User Management[â](#user-management "Direct link to User Management")

| Feature                                               | API7 | Kong | Zuul2 | NGINX |
| ----------------------------------------------------- | ---- | ---- | ----- | ----- |
| RBAC                                                  | Y    | N    | N     | N     |
| Multi-tenancy                                         | Y    | N    | N     | N     |
| Multi-working partition                               | Y    | Y    | N     | N     |
| SSL Certificate Management                            | Y    | Y    | N     | N     |
| Control access with Admin API Key and IP restrictions | Y    | N    | N     | N     |

### Communication Encryption[â](#communication-encryption "Direct link to Communication Encryption")

| Feature                                | API7 | Kong | Zuul2 | NGINX |
| -------------------------------------- | ---- | ---- | ----- | ----- |
| mTLS                                   | Y    | Y    | Y     | Y     |
| Automatic rotation of SSL certificates | Y    | Y    | N     | N     |
| Supports GmSSL                         | Y    | N    | N     | N     |

### Attack Prevention[â](#attack-prevention "Direct link to Attack Prevention")

| Feature                     | API7 | Kong | Zuul2 | NGINX |
| --------------------------- | ---- | ---- | ----- | ----- |
| IP Blacklist and Whitelist  | Y    | Y    | N     | Y     |
| URI Blacklist and Whitelist | Y    | Y    | N     | N     |
| Anti-ReDOS attacks          | Y    | N    | N     | N     |
| Anti-Replay Attack          | Y    | N    | N     | N     |

### Authentication[â](#authentication "Direct link to Authentication")

| Feature                           | API7 | Kong | Zuul2 | NGINX |
| --------------------------------- | ---- | ---- | ----- | ----- |
| key-auth                          | Y    | Y    | N     | N     |
| basic-auth                        | Y    | Y    | N     | Y     |
| JWT                               | Y    | Y    | N     | N     |
| API Signature Verification (HMAC) | Y    | Y    | N     | N     |
| OAuth2                            | Y    | Y    | N     | N     |
| SSO                               | Y    | Y    | N     | N     |
| Auth0, Okta, etc.                 | Y    | Y    | N     | N     |

## Observability[â](#observability "Direct link to Observability")

### Metrics[â](#metrics "Direct link to Metrics")

| Feature    | API7 | Kong | Zuul2 | NGINX |
| ---------- | ---- | ---- | ----- | ----- |
| Prometheus | Y    | Y    | N     | N     |

### Tracing[â](#tracing "Direct link to Tracing")

| Feature           | API7 | Kong | Zuul2 | NGINX |
| ----------------- | ---- | ---- | ----- | ----- |
| Apache SkyWalking | Y    | N    | Y     | N     |
| Zipkin            | Y    | Y    | Y     | N     |
| OpenTracing       | Y    | Y    | Y     | N     |

### Logging[â](#logging "Direct link to Logging")

| Feature     | API7 | Kong | Zuul2 | NGINX |
| ----------- | ---- | ---- | ----- | ----- |
| Kakfa       | Y    | Y    | N     | N     |
| HTTP Logger | Y    | N    | N     | Y     |
| TCP Logger  | Y    | N    | N     | Y     |
| UDP Logger  | Y    | N    | N     | N     |

## Cluster and High Availability[â](#cluster-and-high-availability "Direct link to Cluster and High Availability")

### QPS[â](#qps "Direct link to QPS")

| Feature                 | API7           | Kong | Zuul2 | NGINX          |
| ----------------------- | -------------- | ---- | ----- | -------------- |
| Single Core Performance | Extremely High | High | Low   | Extremely High |

### Latency[â](#latency "Direct link to Latency")

| Feature                     | API7      | Kong     | Zuul2 | NGINX     |
| --------------------------- | --------- | -------- | ----- | --------- |
| Minimum latency per request | Excellent | Moderate | Low   | Excellent |

### Deployment[â](#deployment "Direct link to Deployment")

| Feature                                  | API7 | Kong | Zuul2 | NGINX |
| ---------------------------------------- | ---- | ---- | ----- | ----- |
| Data plane stateless                     | Y    | Y    | Y     | N     |
| Supports Cluster as Configuration Center | Y    | N    | N     | N     |

### Cluster Management[â](#cluster-management "Direct link to Cluster Management")

| Feature                                                      | API7 | Kong | Zuul2 | NGINX |
| ------------------------------------------------------------ | ---- | ---- | ----- | ----- |
| Supports configuration and management of multiple clusters   | Y    | N    | N     | N     |
| Supports isolation of permissions between different clusters | Y    | N    | N     | N     |

### Multi-Layer Network[â](#multi-layer-network "Direct link to Multi-Layer Network")

| Feature                                                         | API7 | Kong | Zuul2 | NGINX |
| --------------------------------------------------------------- | ---- | ---- | ----- | ----- |
| Global deployment, cross-gateway cluster collaboration          | Y    | N    | N     | N     |
| Automatic selection of optimal paths under topological networks | Y    | N    | N     | N     |
| Customized plugins under multiplayer networks                   | Y    | N    | N     | N     |
| Separate deployment with native open source version support     | Y    | N    | N     | N     |

### Dynamic and hot updates[â](#dynamic-and-hot-updates "Direct link to Dynamic and hot updates")

| Feature                                                  | API7 | Kong | Zuul2 | NGINX |
| -------------------------------------------------------- | ---- | ---- | ----- | ----- |
| All changes are hot updated and take effect in real time | Y    | N    | N     | Y     |
| Plugin hot updates                                       | Y    | N    | Y     | N     |
| Hot update of the program itself                         | Y    | Y    | N     | Y     |

## Operations and Maintenance[â](#operations-and-maintenance "Direct link to Operations and Maintenance")

### CLI[â](#cli "Direct link to CLI")

| Feature            | API7 | Kong | Zuul2 | NGINX |
| ------------------ | ---- | ---- | ----- | ----- |
| Command Line Tools | Y    | Y    | N     | Y     |

### Admin API[â](#admin-api "Direct link to Admin API")

| Feature                                       | API7 | Kong | Zuul2 | NGINX |
| --------------------------------------------- | ---- | ---- | ----- | ----- |
| Use REST API for control and easy integration | Y    | Y    | N     | N     |

### Single Node[â](#single-node "Direct link to Single Node")

| Feature                           | API7 | Kong | Zuul2 | NGINX |
| --------------------------------- | ---- | ---- | ----- | ----- |
| Use yaml file to define all rules | Y    | Y    | Y     | N     |

### Rollback[â](#rollback "Direct link to Rollback")

| Feature                                   | API7 | Kong | Zuul2 | NGINX |
| ----------------------------------------- | ---- | ---- | ----- | ----- |
| Supports unlimited rollback of operations | Y    | N    | N     | N     |

### Helm charts[â](#helm-charts "Direct link to Helm charts")

| Feature               | API7 | Kong | Zuul2 | NGINX |
| --------------------- | ---- | ---- | ----- | ----- |
| Easier O\&M under k8s | Y    | N    | N     | Y     |

### Global Plugins[â](#global-plugins "Direct link to Global Plugins")

| Feature             | API7 | Kong | Zuul2 | NGINX |
| ------------------- | ---- | ---- | ----- | ----- |
| Simplify operations | Y    | Y    | Y     | N     |

### Health Check[â](#health-check "Direct link to Health Check")

| Feature                                                      | API7 | Kong | Zuul2 | NGINX |
| ------------------------------------------------------------ | ---- | ---- | ----- | ----- |
| Versioning and operational monitoring of data plane nodes    | Y    | Y    | Y     | N     |
| Provides configuration center status and version information | Y    | Y    | N     | N     |
| Node load status monitoring                                  | Y    | Y    | N     | N     |

### Service Observability[â](#service-observability "Direct link to Service Observability")

| Feature                           | API7 | Kong | Zuul2 | NGINX |
| --------------------------------- | ---- | ---- | ----- | ----- |
| Service Invocation Topology       | Y    | Y    | N     | N     |
| Data Throughput                   | Y    | Y    | Y     | N     |
| Response time statistics          | Y    | Y    | Y     | N     |
| Upstream response time statistics | Y    | Y    | Y     | N     |
| Status Code Statistics            | Y    | Y    | Y     | N     |
| API call statistics               | Y    | Y    | N     | N     |

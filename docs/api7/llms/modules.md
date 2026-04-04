# Source: https://docs.api7.ai/enterprise-whitepaper/modules.md

# Modules

API7 mainly contains the following functional modules:

## User System[â](#user-system "Direct link to User System")

With the help of user system, the administrator will assign certain accesses and resources for each user in the system, and the user cannot override the accesses to the resources. API7 supports account password login and SSO login.

## Permission System[â](#permission-system "Direct link to Permission System")

API7 has a built-in Role-Based AccessControl system (RBAC), which allows administrators to create different roles with the help of the console, and by binding users to roles, fine-grained permission control can be achieved.

## Multi-tenancy[â](#multi-tenancy "Direct link to Multi-tenancy")

API7 supports multi-tenancy based on working partition isolation, where administrators can create different working partitions and specify which users have access to which resources on the working partition.

## Multi-environment[â](#multi-environment "Direct link to Multi-environment")

API7 supports multiple etcd clusters, with no data sharing among clusters.

## Authentication[â](#authentication "Direct link to Authentication")

API7 includes a variety of authentication plugins, such as basic-auth, jwt-auth, key-auth, wolf-rbac, and so on. In addition, with the built-in HMAC plugin, request parameters can be signed and verified using AK/SK to achieve tamper-proof requests and replay-proof requests, and to achieve the purpose of authentication.

## Service Routing[â](#service-routing "Direct link to Service Routing")

API7 is based on Radixtree for efficient route matching, and is currently the fastest API gateway for matching routes. It supports full path matching, prefix matching, and also supports using NGINX built-in variables as matching conditions to achieve fine-grained routing. In addition, API7 supports traffic mirroring and advanced route matching for fine-grained route management features such as grayscale publishing. It also supports service discovery and multiple registries, and has the ability to triage requests based on parameters such as Header, Query, and Cookie.

## Protocol Conversion[â](#protocol-conversion "Direct link to Protocol Conversion")

API7 supports many communication protocols, such as TCP/UDP, Dubbo, MQTT, gRPC, WebSocket, etc. API7 is able to convert HTTP protocol to other protocols of back-end services. API7 exposes a unified HTTP portal to the outside world, and administrators can complete the protocol conversion settings through the console interface, and support the parameter mapping of requests and back-end services. APIs can be configured through the console interface.

## Service Governance[â](#service-governance "Direct link to Service Governance")

API7 supports service meltdown, flow limiting, rate limiting, IP blacklist and white list, fault isolation, etc., which can be easily and clearly set through the dashboard control panel.

## Custom plugins[â](#custom-plugins "Direct link to Custom plugins")

API7 has more than 60 built-in plugins, covering various categories such as security protection, traffic control, logging, etc., which can meet the needs of most enterprises. For specific business, API7 now supports custom plugins written in Lua, and the plugins can be applied to all stages of traffic in and out. Thanks to the fully dynamic capability, new and modified plugins can take effect in real time without downtime and restart, avoiding interruption of business.

## Analysis and Monitoring[â](#analysis-and-monitoring "Direct link to Analysis and Monitoring")

API7 has built-in analysis and monitoring functions such as request auditing, monitoring and alerting, statistical reports, etc. API7 can record information of each request of all nodes and conduct statistics of successful requests and abnormal requests. You can view the number of successful requests, failed requests, error codes, request delays and other metrics in the console. In addition, with the ability of Grafana, API7 can meet the demand for more multi-dimensional analysis and monitoring.

## API Management[â](#api-management "Direct link to API Management")

API7 supports API version management, API grouping, API release, API abolishment, online debugging and other functions, and is compatible with OpenAPI 3.0 standard, enabling API document generation, API import/export and other features to execute users' data migration operations.

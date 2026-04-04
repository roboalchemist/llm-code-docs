# Source: https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/

Title: Multi-DC Deployment - Pattern 1

URL Source: https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/

Published Time: Tue, 10 Mar 2026 10:30:59 GMT

Markdown Content:
[](https://github.com/wso2/docs-apim/edit/4.6.0/en/docs/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1.md "Edit this page")[](https://github.com/wso2/docs-apim/raw/4.6.0/en/docs/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1.md "View source of this page")
Configure Pattern 1: Geo-Regional Synchronized API Management with Replicated Databases[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#configure-pattern-1-geo-regional-synchronized-api-management-with-replicated-databases "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 1: Multi-DC Pattern 1](https://apim.docs.wso2.com/en/4.6.0/assets/img/setup-and-install/multi-dc-pattern-1.png)](https://apim.docs.wso2.com/en/4.6.0/assets/img/setup-and-install/multi-dc-pattern-1.png)

All the regions are identical in this pattern. therefore, the documentation will provide information about configuring a single region.

Step 1: Configure the Database with replication[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-1-configure-the-database-with-replication "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Supported Databases[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#supported-databases "Permanent link")

*   MSSQL
*   Oracle
*   PostgreSQL

Note

When setting up the database with replication for the multi-dc deployment, it is recommended to use the provided script. The file structure is as follows.

```
<APIM-Home>
└── dbscripts
    └── multi-dc
        ├── OGG
        │   └── oracle
        │       ├── Readme.txt
        │       ├── apimgt
        │       │   ├── sequences.sql
        │       │   ├── sequences_23c.sql
        │       │   ├── tables.sql
        │       │   └── tables_23c.sql
        │       ├── sequence.sql
        │       ├── sequences_23c.sql
        │       ├── tables.sql
        │       └── tables_23c.sql
        ├── Postgresql
        │   ├── ReadMe.txt
        │   ├── apimgt
        │   │   └── tables.sql
        │   └── tables.sql
        └── SQLServer
            └── mssql
                ├── ReadMe.txt
                ├── apimgt
                │   └── tables.sql
                └── tables.sql
```

You should consult your database administrator on replication related configurations.

Note

Bi-directional replication in the multi-DC setup was tested using Virtual Machine (VM)-based databases. If you intend to use a cloud-based database service, consult the relevant cloud provider for any limitations related to configuring an active-active database setup in their environment.

Step 2: Configure the API Manager Nodes[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-2-configure-the-api-manager-nodes "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Step 1 - Install WSO2 API-M[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-1-install-wso2-api-m "Permanent link")

To install and set up the API-M servers:

1.   Download the WSO2 API Control Plane, WSO2 Universal Gateway and WSO2 Traffic Manager component distributions from the [WSO2 API Manager website](https://wso2.com/api-manager/).

### Step 2 - Install and configure the databases[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-2-install-and-configure-the-databases "Permanent link")

You can create the required databases for the API-M deployment in a separate server and point to the databases from the respective nodes.

For information, see [Installing and Configuring the Databases](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/setting-up-databases/overview/).

### Step 3 - Configure your deployment with production hardening[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-3-configure-your-deployment-with-production-hardening "Permanent link")

Ensure that you have taken into account the respective security hardening factors (e.g., changing and encrypting the default passwords, configuring JVM security, etc.) before deploying WSO2 API-M.

For more information, see [Production Deployment Guidelines](https://apim.docs.wso2.com/en/latest/install-and-setup/deploying-wso2-api-manager/production-deployment-guidelines/#common-guidelines-and-checklist).

### Step 4 - Create and import SSL certificates[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-4-create-and-import-ssl-certificates "Permanent link")

Create an SSL certificate for each of the WSO2 API-M nodes and import them to the keystore and the truststore. This ensures that hostname mismatch issues in the certificates will not occur.

Note

The same primary keystore should be used for all API Manager instances to decrypt the registry resources. For more information, see [Configuring the Primary Keystore](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/security/configuring-keystores/configuring-keystores-in-wso2-api-manager/#configuring-the-primary-keystore).

For more information, see [Creating SSL Certificates](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/security/configuring-keystores/keystore-basics/creating-new-keystores/).

### Step 5 - Configure API-M Analytics[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-5-configure-api-m-analytics "Permanent link")

API Manager Analytics is delivered via the API Manager Analytics cloud solution. You need to configure the WSO2 Universal Gateway distribution to publish analytics data to the cloud.

See the instructions on [configuring the Gateway](https://apim.docs.wso2.com/en/latest/monitoring/api-analytics/moesif-analytics/moesif-integration-guide/) with the cloud-based analytics solution.

### Step 6 - Configure and start the component nodes[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-6-configure-and-start-the-component-nodes "Permanent link")

Let's configure the API-M nodes in the deployment.

#### Configure the Gateway nodes

Configure the Gateway to communicate with the API Control Plane and the Traffic Manager nodes.

Follow the instructions given below to configure the Gateway node so that it can communicate with the API Control Plane node:

1.   Open the `<UNIVERSAL-GW_HOME>/repository/conf/deployment.toml` file of the Gateway node.

2.   Add the following configurations to the deployment.toml file.

    *   **Connect the Gateway to the API Control Plane node**:

API Control Plane with High Availability Single API Control Plane

```
# Key Manager configuration
[apim.key_manager]
service_url = "https://[control-plane-LB-host]/services/"
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://[control-plane-LB-host]/services/"
event_listening_endpoints = ["tcp://control-plane-1-host:5672", "tcp://control-plane-2-host:5672"]
```

```
# Key Manager configuration
[apim.key_manager]
service_url = "https://[control-plane-host]:${mgt.transport.https.port}/services/"
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://[control-plane-host]:${mgt.transport.https.port}/services/"
event_listening_endpoints = ["tcp://control-plane-host:5672"]
```

Info

Event hub configuration is used to retrieve Gateway artifacts. Using `event_listening_endpoints`, the Gateway will create a JMS connection with the event hub that is then used to subscribe for API/Application/Subscription and Key Manager operations-related events. The `service_url` points to the internal API that resides in the event hub that is used to pull artifacts and information from the database.

    *   **Connecting the Gateway to the Traffic Manager node**:

Traffic Manager with HA Single Traffic Manager

```
[apim.throttling]
throttle_decision_endpoints = ["tcp://traffic-manager-1-host:5672", "tcp://Traffic-Manager-2-host:5672"]

[[apim.throttling.url_group]]
traffic_manager_urls = ["tcp://traffic-manager-1-host:9611"]
traffic_manager_auth_urls = ["ssl://traffic-manager-1-host:9711"]

[[apim.throttling.url_group]]
traffic_manager_urls = ["tcp://traffic-manager-2-host:9611"]
traffic_manager_auth_urls = ["ssl://traffic-manager-2-host:9711"]
```

```
[apim.throttling]
throttle_decision_endpoints = ["tcp://traffic-manager-host:5672"]

[[apim.throttling.url_group]]
traffic_manager_urls = ["tcp://traffic-manager-host:9611"]
traffic_manager_auth_urls = ["ssl://traffic-manager-host:9711"]
```

Info

Rate limiting configurations are used by the Gateway to connect with the Traffic Manager. The Gateway will publish Gateway invocation-related events to the TM using the `apim.throttling.url_group`. Traffic Managers will receive these events and rate limiting decisions will be published to the Gateway. To receive these rate limiting decisions, the Gateway has to create a JMS connection using `throttle_decision_endpoints` and listen.

**Enabling TLS/SSL for Gateway to Traffic Manager JMS communications**

If required, you can enable TLS/SSL for the JMS communications happening between the Gateway and Traffic Manager nodes.

Add the following configuration to the Gateway node for this purpose.

```
[apim.throttling.jms]
topic_connection_factory = "amqp://<![CDATA[<username>]]>:<![CDATA[<password>]]>@clientid/carbon?brokerlist='tcp://tm.wso2.com:8672?ssl='true'%26ssl_cert_alias='<certificate_alias_in_truststore>'%26trust_store='<path_to_trust_store>'%26trust_store_password='<truststore_password>'%26key_store='<path_to_key_store>'%26key_store_password='<keystore_password>''"
```

Also update your Traffic Manager node to include the following configuration to enable secure broker connections.

```
[broker.transport.amqp.ssl_connection]
enabled = true
port = 8672
ssl_enabled_protocols = "TLSv1,TLSv1.2"
ciphers = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"

[broker.transport.amqp.ssl_connection.keystore]
location = "repository/resources/security/wso2carbon.jks"
password = "wso2carbon"
cert_type = "SunX509"

[broker.transport.amqp.ssl_connection.truststore]
location = "repository/resources/security/client-truststore.jks"
password = "wso2carbon"
cert_type = "SunX509"
```

3.   Add the following configurations to the deployment.toml file to configure the Gateway environment. Change the `gateway_labels` property based on your Gateway environment.

```
[apim.sync_runtime_artifacts.gateway]
gateway_labels =["Default"]
``` Info

Once an API is deployed/undeployed, the API Control Plane will send a deploy/undeploy event to the Gateways. Using this configuration, the Gateway will filter out its relevant deploy/undeploy events and retrieve the artifacts. 
4.   Add the following configuration to set a unique identifier for each Gateway node when setting up a distributed deployment on VMs.

Format Example

```
[apim.gateway_notification]
gateway_id = "<unique-gateway-id>"
``` ```
[apim.gateway_notification]
gateway_id = "gateway_00"
```   Info

To further optimize the gateway notification feature, you can use additional `gateway_notification` configurations. For more information, see [API-M Revision Deployment Monitoring](https://apim.docs.wso2.com/en/latest/reference/config-catalog/#api-m-gateway-notification-configurations). 
5.   Enable JSON Web Token (JWT) if required. For instructions, see [Generating JSON Web Token](https://apim.docs.wso2.com/en/latest/deploy-and-publish/deploy-on-gateway/api-gateway/passing-enduser-attributes-to-the-backend-via-api-gateway).

6.   Add the public certificate of the private key (that is used for signing the tokens) to the truststore under the "gateway_certificate_alias" alias. For instructions, see [Create and import SSL certificates](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/security/configuring-keystores/keystore-basics/creating-new-keystores).

Note

This is not applicable if you use the default certificates, which are the certificates that are shipped with the product itself. 
7.   Follow the steps given below to configure High Availability (HA) for the Universal Gateway:

    1.   Create a copy of the WSO2 Universal Gateway node that you just configured. This is the second node of the Gateway cluster.

    2.   Configure a load balancer fronting the two Gateway nodes in your deployment. For instructions, see [Configuring the Proxy Server and the Load Balancer](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/setting-up-proxy-server-and-the-load-balancer/configuring-the-proxy-server-and-the-load-balancer).

Note

To keep custom runtime artifacts deployed in the Gateway, add the following configuration in the `<UNIVERSAL-GW_HOME>/repository/conf/deployment.toml` file of the Gateway nodes.

```
[apim.sync_runtime_artifacts.gateway.skip_list]
apis = ["api1.xml","api2.xml"]
endpoints = ["endpoint1.xml"]
sequences = ["post_with_nobody.xml"]
local_entries = ["file.xml"]
```  
    3.   Open the `deployment.toml` files of each Gateway node and add the cluster hostname. For example, if the hostname is `gw.am.wso2.com` the configuration will be:

```
[server]
hostname = "gw.wso2.com"
``` 
    4.   Specify the following incoming connection configurations in the `deployment.toml` files of both nodes.

```
[transport.http]
properties.port = 9763
properties.proxyPort = 80

[transport.https]
properties.port = 9443
properties.proxyPort = 443
``` 
    5.   Open the server's `/etc/hosts` file and map the hostnames to IPs.

Format:

```
<GATEWAY-IP> gw.wso2.com
``` 
Example:

```
xxx.xxx.xxx.xx4 gw.wso2.com
``` 

###### Sample configuration for the Gateway

HA Cluster Single Node

```
[server]
hostname = "gw.wso2.com"
node_ip = "127.0.0.1"
server_role = "default"

[user_store]
type = "database_unique_id"

[super_admin]
username = "admin"
password = "admin"
create_admin_account = true

[database.shared_db]
type = "mysql"
hostname = "db.wso2.com"
name = "shared_db"
port = "3306"
username = "sharedadmin"
password = "sharedadmin"

[keystore.tls]
file_name =  "wso2carbon.jks"
type =  "JKS"
password =  "wso2carbon"
alias =  "wso2carbon"
key_password =  "wso2carbon"

[truststore]
file_name = "client-truststore.jks"
type = "JKS"
password = "wso2carbon"

[transport.http]
properties.port = 9763
properties.proxyPort = 80

[transport.https]
properties.port = 9443
properties.proxyPort = 443

# key manager implementation
[apim.key_manager]
service_url = "https://api.am.wso2.com/services/"

[apim.sync_runtime_artifacts.gateway]
gateway_labels =["Default"]

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://api.am.wso2.com/services/"
event_listening_endpoints = ["tcp://apim-cp-1:5672", "tcp://apim-cp-2:5672"]

# Traffic Manager configurations
[apim.throttling]
throttle_decision_endpoints = ["tcp://traffic-manager-1:5672", "tcp://traffic-manager-2:5672"]

[[apim.throttling.url_group]]
traffic_manager_urls=["tcp://traffic-manager-1:9611"]
traffic_manager_auth_urls=["ssl://traffic-manager-1:9711"]

[[apim.throttling.url_group]]
traffic_manager_urls=["tcp://traffic-manager-2:9611"]
traffic_manager_auth_urls=["ssl://traffic-manager-2:9711"]
```

```
[server]
hostname = "gw.wso2.com"
node_ip = "127.0.0.1"
server_role = "default"
offset=0

[user_store]
type = "database_unique_id"

[super_admin]
username = "admin"
password = "admin"
create_admin_account = true

[database.shared_db]
type = "h2"
url = "jdbc:h2:./repository/database/WSO2SHARED_DB;DB_CLOSE_ON_EXIT=FALSE"
username = "wso2carbon"
password = "wso2carbon"

[keystore.tls]
file_name =  "wso2carbon.jks"
type =  "JKS"
password =  "wso2carbon"
alias =  "wso2carbon"
key_password =  "wso2carbon"

[truststore]
file_name = "client-truststore.jks"
type = "JKS"
password = "wso2carbon"

# Key Manager configuration
[apim.key_manager]
service_url = "https://cp.wso2.com:9443/services/"
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"

# Traffic Manager configurations
[apim.throttling]
throttle_decision_endpoints = ["tcp://tm.wso2.com:5672"]

[[apim.throttling.url_group]]
traffic_manager_urls=["tcp://tm.wso2.com:9611"]
traffic_manager_auth_urls=["ssl://tm.wso2.com:9711"]

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://cp.wso2.com:9443/services/"
event_listening_endpoints = ["tcp://cp.wso2.com:5672"]

[apim.sync_runtime_artifacts.gateway]
gateway_labels =["Default"]
```

#### Configure the API Control Plane nodes

Follow the steps given below to configure the API Control Plane nodes to communicate with the Universal Gateway.

1.   Open the `<ACP_HOME>/repository/conf/deployment.toml` file of the API Control Plane node.

2.   Add the following configurations to the deployment.toml file.

**Connecting the API Control Plane to the Gateway node**:

Gateway with High Availability Single gateway

```
[[apim.gateway.environment]]
name = "Default"
type = "hybrid"
display_in_api_console = true
description = "This is a hybrid gateway that handles both production and sandbox token traffic."
show_as_token_endpoint_url = true
service_url = "https://[api-gateway-LB-host]/services/"
ws_endpoint = "ws://[api-gateway-LB-host-or-ip]:9099"
wss_endpoint = "wss://[api-gateway-LB-host-or-ip]:8099"
http_endpoint = "http://[api-gateway-LB-host]"
https_endpoint = "https://[api-gateway-LB-host]"
``` ```
[[apim.gateway.environment]]
name = "Default"
type = "hybrid"
display_in_api_console = true
description = "This is a hybrid gateway that handles both production and sandbox token traffic."
show_as_token_endpoint_url = true
service_url = "https://[api-gateway-host]:9443/services/"
ws_endpoint = "ws://[api-gateway-host]:9099"
wss_endpoint = "wss://[api-gateway-host]:8099"
http_endpoint = "http://[api-gateway-host]:${http.nio.port}"
https_endpoint = "https://[api-gateway-host]:${https.nio.port}"
```   Info

This configuration is used for deploying APIs to the Gateway and for connecting the Developer Portal component to the Gateway if the Gateway is shared across tenants. If the Gateway is not used in multiple tenants, you can create a [Gateway Environment using the Admin Portal](https://apim.docs.wso2.com/en/latest/manage-apis/deploy-and-publish/deploy-on-gateway/deploy-api/exposing-apis-via-custom-hostnames/#using-a-new-gateway-environment-to-expose-apis-via-custom-hostnames).

Note that in the above configurations, the `service_url` points to the `9443` port of the Gateway node, while `http_endpoint` and `https_endpoint` points to the `http` and `https nio ports` (8280 and 8243). 
**Add Event Hub Configurations**:

Info

**Enabling TLS/SSL for event hub JMS communications**

If required, you can enable TLS/SSL for the JMS communications of event hub. Update your event hub configurations to include the following for this purpose.

```
[apim.event_hub]
enable = true
jms.username = "<username>"
jms.password = "<password>"
jms.ssl = "true'&amp;ssl_cert_alias='<certificate_alias_in_truststore>'&amp;trust_store='<path_to_trust_store>'&amp;trust_store_password='<truststore_password>'&amp;key_store='<path_to_key_store>'&amp;key_store_password='<keystore_password>"
ssl = "true'&amp;ssl_cert_alias='<certificate_alias_in_truststore>'&amp;trust_store='<path_to_trust_store>'&amp;trust_store_password='<truststore_password>'&amp;key_store='<path_to_key_store>'&amp;key_store_password='<keystore_password>"
event_listening_endpoints = ["tcp://control-plane-host:8672"]
``` 
To enable secure broker connections add the following configuration to the Control Plane node.

```
[broker.transport.amqp.ssl_connection]
enabled = true
port = 8672
ssl_enabled_protocols = "TLSv1,TLSv1.2"
ciphers = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"

[broker.transport.amqp.ssl_connection.keystore]
location = "repository/resources/security/wso2carbon.jks"
password = "wso2carbon"
cert_type = "SunX509"

[broker.transport.amqp.ssl_connection.truststore]
location = "repository/resources/security/client-truststore.jks"
password = "wso2carbon"
cert_type = "SunX509"
```  API Control Plane with High Availability Single API Control Plane

```
# Event Hub configurations
[apim.event_hub]
enable = true
username= "$ref{super_admin.username}"
password= "$ref{super_admin.password}"
service_url = "https://localhost:${mgt.transport.https.port}/services/"
event_listening_endpoints = ["tcp://localhost:5672"]
event_duplicate_url = ["tcp://apim-cp-2:5672"]

[[apim.event_hub.publish.url_group]]
urls = ["tcp://control-plane-1-host:9611"]
auth_urls = ["ssl://control-plane-1-host:9711"]

[[apim.event_hub.publish.url_group]]
urls = ["tcp://control-plane-2-host:9611"]
auth_urls = ["ssl://control-plane-2-host:9711"]
``` ```
# Event Hub configurations
[apim.event_hub]
enable = true
username= "$ref{super_admin.username}"
password= "$ref{super_admin.password}"
service_url = "https://localhost:${mgt.transport.https.port}/services/"
event_listening_endpoints = ["tcp://localhost:5672"]

[[apim.event_hub.publish.url_group]]
urls = ["tcp://control-plane-host:9611"]
auth_urls = ["ssl://control-plane-host:9711"]
```   Info

As there are two event hubs in a HA setup, each event hub has to publish events to both event streams. This will be done through the event streams created with `apim.event_hub.publish.url_group`. The token revocation events that are received to an event hub will be duplicated to the other event hub using `event_duplicate_url`. 
**Add Event Listener Configurations**:

The below configurations are only added to the API Control Plane if you are using the Resident Key Manager (resides in the API Control Plane). If you are using WSO2 IS as Key Manager, you need to add these in the IS node. Once you add the below configurations, the Control Plane or Identity Server will listen to token revocation events and invoke the `notification_endpoint` regarding the revoked token.

API Control Plane with High Availability Single API Control Plane

```
# Event Listener configurations
[[event_listener]]
id = "token_revocation"
type = "org.wso2.carbon.identity.core.handler.AbstractIdentityHandler"
name = "org.wso2.is.notification.ApimOauthEventInterceptor"
order = 1

[event_listener.properties]
notification_endpoint = "https://[control-plane-LB-host]/internal/data/v1/notify"
username = "${admin.username}"
password = "${admin.password}"
'header.X-WSO2-KEY-MANAGER' = "default"
``` ```
# Event Listener configurations
[[event_listener]]
id = "token_revocation"
type = "org.wso2.carbon.identity.core.handler.AbstractIdentityHandler"
name = "org.wso2.is.notification.ApimOauthEventInterceptor"
order = 1

[event_listener.properties]
notification_endpoint = "https://[control-plane-host]:${mgt.transport.https.port}/internal/data/v1/notify"
username = "${admin.username}"
password = "${admin.password}"
'header.X-WSO2-KEY-MANAGER' = "default"
```   
3.   If required, encrypt the Auth Keys (access tokens, client secrets, and authorization codes), see [Encrypting OAuth Keys](https://apim.docs.wso2.com/en/latest/manage-apis/design/api-security/oauth2/encrypting-oauth2-tokens).

4.   Optionally, add the following configuration to enable distributed cache invalidation within the API Control Plane nodes.

```
[apim.cache_invalidation]
enabled = true
domain = "control-plane-domain"
``` 
5.   Follow the steps given below to configure High Availability (HA) for the API Control Plane:

    1.   Create a copy of the API Control Plane node that you just configured. This is the second node of the API Control Plane cluster.

    2.   Configure a load balancer fronting the two API Control Plane nodes in your deployment. For instructions, see [Configuring the Proxy Server and the Load Balancer](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/setting-up-proxy-server-and-the-load-balancer/configuring-the-proxy-server-and-the-load-balancer).

###### Sample configuration for the API Control Plane

HA Cluster Single Node

```
[server]
hostname = "api.am.wso2.com"
node_ip = "127.0.0.1"
server_role="default"
base_path = "${carbon.protocol}://${carbon.host}:${carbon.management.port}"

[user_store]
type = "database_unique_id"

[super_admin]
username = "admin"
password = "admin"
create_admin_account = true

[database.apim_db]
type = "mysql"
hostname = "db.wso2.com"
name = "apim_db"
port = "3306"
username = "apimadmin"
password = "apimadmin"

[database.shared_db]
type = "mysql"
hostname = "db.wso2.com"
name = "shared_db"
port = "3306"
username = "sharedadmin"
password = "sharedadmin"

[keystore.tls]
file_name =  "wso2carbon.jks"
type =  "JKS"
password =  "wso2carbon"
alias =  "wso2carbon"
key_password =  "wso2carbon"

[truststore]
file_name = "client-truststore.jks"
type = "JKS"
password = "wso2carbon"

[[apim.gateway.environment]]
name = "Default"
type = "hybrid"
display_in_api_console = true
description = "This is a hybrid gateway that handles both production and sandbox token traffic."
show_as_token_endpoint_url = true
service_url = "https://[api-gateway-LB-host]/services/"
ws_endpoint = "ws://[api-gateway-LB-host]:9099"
wss_endpoint = "wss://[api-gateway-LB-host]:8099"
http_endpoint = "http://[api-gateway-LB-host]"
https_endpoint = "https://[api-gateway-LB-host]"

[apim.devportal]
url = "https://api.am.wso2.com/devportal"

[transport.https.properties]
proxyPort = 443

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://api.am.wso2.com/services/"
event_listening_endpoints = ["tcp://localhost:5672"]
event_duplicate_url = ["tcp://apim-cp-2:5672"]

[[apim.event_hub.publish.url_group]]
urls = ["tcp://apim-cp-1:9611"]
auth_urls = ["ssl://apim-cp-1:9711"]

[[apim.event_hub.publish.url_group]]
urls = ["tcp://apim-cp-2:9611"]
auth_urls = ["ssl://apim-cp-2:9711"]

# key manager implementation
[apim.key_manager]
service_url = "https://api.am.wso2.com/services/"
username= "$ref{super_admin.username}"
password= "$ref{super_admin.password}"
type = "default"

[[event_listener]]
id = "token_revocation"
type = "org.wso2.carbon.identity.core.handler.AbstractIdentityHandler"
name = "org.wso2.is.notification.ApimOauthEventInterceptor"
order = 1

[event_listener.properties]
notification_endpoint = "https://api.am.wso2.com/internal/data/v1/notify"
username = "${admin.username}"
password = "${admin.password}"
'header.X-WSO2-KEY-MANAGER' = "default"
```

```
[server]
hostname = "cp.wso2.com"
node_ip = "127.0.0.1"
server_role = "default"
offset=0

[user_store]
type = "database_unique_id"

[super_admin]
username = "admin"
password = "admin"
create_admin_account = true

[database.apim_db]
type = "mysql"
hostname = "db.wso2.com"
name = "apim_db"
port = "3306"
username = "apimadmin"
password = "apimadmin"

[database.shared_db]
type = "mysql"
hostname = "db.wso2.com"
name = "shared_db"
port = "3306"
username = "sharedadmin"
password = "sharedadmin"

[keystore.tls]
file_name =  "wso2carbon.jks"
type =  "JKS"
password =  "wso2carbon"
alias =  "wso2carbon"
key_password =  "wso2carbon"

# Gateway configuration
[[apim.gateway.environment]]
name = "Default"
type = "hybrid"
display_in_api_console = true
description = "This is a hybrid gateway that handles both production and sandbox token traffic."
show_as_token_endpoint_url = true
service_url = "https://gw.wso2.com:9443/services/"
username= "${admin.username}"
password= "${admin.password}"
ws_endpoint = "ws://gw.wso2.com:9099"
wss_endpoint = "wss://gw.wso2.com:8099"
http_endpoint = "http://gw.wso2.com:8280"
https_endpoint = "https://gw.wso2.com:8243"

# Event Listener configurations
[[event_listener]]
id = "token_revocation"
type = "org.wso2.carbon.identity.core.handler.AbstractIdentityHandler"
name = "org.wso2.is.notification.ApimOauthEventInterceptor"
order = 1

[event_listener.properties]
notification_endpoint = "https://cp.wso2.com:9443/internal/data/v1/notify"
username = "${admin.username}"
password = "${admin.password}"
'header.X-WSO2-KEY-MANAGER' = "default"

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://cp.wso2.com:9443/services/"
event_listening_endpoints = ["tcp://cp.wso2.com:5672"]

[[apim.event_hub.publish.url_group]]
urls = ["tcp://cp.wso2.com:9611"]
auth_urls = ["ssl://cp.wso2.com:9711"]
```

#### Configure the Traffic Manager Nodes

Configure the Traffic Manager to communicate with the API Control Plane.

1.   Open the `<TM_HOME>/repository/conf/deployment.toml` file of the Traffic Manager node.

2.   Add the following configurations to the deployment.toml file.

**Connecting the Traffic Manager to the API Control Plane node**:

API Control Plane with High Availability Single API Control Plane

```
# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://[control-plane-LB-host]/services/"
event_listening_endpoints = ["tcp://control-plane-1-host:5672", "tcp://control-plane-2-host:5672"]
``` ```
# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://[control-plane-host]/services/"
event_listening_endpoints = ["tcp://control-plane-host:5672"]
```   Info

With `event_listening_endpoints`, the Traffic Manager is subscribed to the JMS stream of both event hubs. Once a policy-related event is received, it will pull the execution plans from the `service_url`. 
If the Traffic Manager node is configured with High Availability (HA), configure rate limiting as follows.

```
[apim.throttling]
event_duplicate_url = ["tcp://traffic-manager-2-host:5672"]
throttle_decision_endpoints = ["tcp://localhost:5672"]
``` Info

The `event_duplicate_url` will publish rate limiting decisions to the other Traffic Manager node to maintain consistency. 
3.   Follow the steps given below to configure High Availability (HA) for the Traffic Manager.

    1.   Create a copy of the Traffic Manager node that you just configured. This is the second node of the Traffic Manager cluster.

    2.   Configure a load balancer fronting the two Traffic Manager nodes in your deployment.

Note

In each startup of a Traffic Manager node, the rate-limiting policies are redeployed by retrieving the latest policy details from the database. This maintains the consistency between the Traffic Manager nodes. If you need to avoid redeploying certain rate-limiting policies, add the following configuration to the `<TM_HOME>/repository/conf/deployment.toml` file in the Traffic Manager node.

```
[apim.throttling]
skip_redeploying_policies = ["throttle_policy_1","throttle_policy_2"]
```  

###### Sample configuration for the Traffic Manager

HA Cluster Single Node

```
[server]
hostname = "tm.am.wso2.com"
node_ip = "127.0.0.1"
server_role = "default"

[transport.https.properties]
proxyPort = 443

[user_store]
type = "database_unique_id"

[super_admin]
username = "admin"
password = "admin"
create_admin_account = true

[database.shared_db]
type = "mysql"
hostname = "db.wso2.com"
name = "shared_db"
port = "3306"
username = "sharedadmin"
password = "sharedadmin"

[keystore.tls]
file_name =  "wso2carbon.jks"
type =  "JKS"
password =  "wso2carbon"
alias =  "wso2carbon"
key_password =  "wso2carbon"

[truststore]
file_name = "client-truststore.jks"
type = "JKS"
password = "wso2carbon"

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://api.am.wso2.com/services/"
event_listening_endpoints = ["tcp://apim-cp-1:5672", "tcp://apim-cp-2:5672"]

# Traffic Manager configurations
[apim.throttling]
event_duplicate_url = ["tcp://traffic-manager-2:5672"]
throttle_decision_endpoints = ["tcp://localhost:5672"]
```

```
[server]
hostname = "tm.wso2.com"
node_ip = "127.0.0.1"
server_role = "default"
offset=0

[user_store]
type = "database_unique_id"

[super_admin]
username = "admin"
password = "admin"
create_admin_account = true

[database.shared_db]
type = "h2"
url = "jdbc:h2:./repository/database/WSO2SHARED_DB;DB_CLOSE_ON_EXIT=FALSE"
username = "wso2carbon"
password = "wso2carbon"

[keystore.tls]
file_name =  "wso2carbon.jks"
type =  "JKS"
password =  "wso2carbon"
alias =  "wso2carbon"
key_password =  "wso2carbon"

[truststore]
file_name = "client-truststore.jks"
type = "JKS"
password = "wso2carbon"

# Event Hub configurations
[apim.event_hub]
enable = true
username = "$ref{super_admin.username}"
password = "$ref{super_admin.password}"
service_url = "https://cp.wso2.com:9443/services/"
event_listening_endpoints = ["tcp://cp.wso2.com:5672"]
```

### Step 7 - Start the API-M nodes[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-7-start-the-api-m-nodes "Permanent link")

Once you have successfully configured all the API-M nodes in the deployment, you can start the servers.

*   Starting the Gateway nodes

Open a terminal, navigate to the `<UNIVERSAL-GW_HOME>/bin` folder, and execute the following command:

Linux/Mac OS Windows

```
cd <UNIVERSAL-GW_HOME>/bin/
sh gateway.sh
``` ```
cd <UNIVERSAL-GW_HOME>\bin\
gateway.bat --run
```   
*   Start the API Control Plane nodes

Open a terminal, navigate to the `<ACP_HOME>/bin` folder, and execute the following command:

Linux/Mac OS Windows

```
cd <ACP_HOME>/bin/
sh api-cp.sh
``` ```
cd <ACP_HOME>\bin\
api-cp.bat --run
```   
*   Start the Traffic Manager nodes

Open a terminal, navigate to the `<TM_HOME>/bin` folder, and execute the following command:

Linux/Mac OS Windows

```
cd <TM_HOME>/bin/
sh traffic-manager.sh
``` ```
cd <TM_HOME>\bin\
traffic-manager.bat --run
```   

Step 3: Configure the Communication Between Control Plane Nodes Across Regions[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#step-3-configure-the-communication-between-control-plane-nodes-across-regions "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In a multi-datacenter (multi-DC) deployment of WSO2 API Manager, each region operates independently and communicates with other regions through their respective event hubs via JMS (Java Message Service) events. This pattern allows for efficient inter-region coordination and notification for various events, including API-related events, application-related events, key manager-related events, and token revocation events.

It should be noted that this cross-region communication via JMS events and event hubs is not supported out of the box in WSO2 API Manager. Therefore, organizations deploying multi-DC setups are required to implement custom data publishers in each region's control plane node. These custom data publishers are designed to publish data to the event hubs in different regions, facilitating communication between them.

4 data publishers should be implemented per control plane where the following data publishers are utilized,

**Data Publisher****Purpose**
Notifications data publisher Publishes data related to the “org.wso2.apimgt.notification.stream” event stream. This event stream consists of events related to APIs, Applications, Policies etc.
Token revocation data publisher Publishes data related to “org.wso2.apimgt.token.revocation.stream” event stream. This event stream is responsible for token revocation related events.
Key management data publisher Publishes data related to “org.wso2.apimgt.keymgt.stream” event stream. This event stream is responsible for key manager related events such as key manager addition, updating and deletion.
Async Webhooks data publisher Publishes data from “org.wso2.apimgt.webhooks.request.stream” event stream. This event stream is responsible for the request data from deployed webhooks in the API gateway.
Blocking Event Data Publisher Publishes data from “org.wso2.blocking.request.stream” event stream. This event stream is responsible for blocking tasks such as application blocking, IP blocking etc.

Moreover, jndi.properties files should be added per region to provide information on the connection of the event hub.

Since the control planes are only connected through the JMS connections, the TCP port 5672 should be exposed to the external parties (Other regions' control planes).

[![Image 2: Multi-DC CP to CP Communication](https://apim.docs.wso2.com/en/4.6.0/assets/img/setup-and-install/multi-dc-cp-to-cp-communication.png)](https://apim.docs.wso2.com/en/4.6.0/assets/img/setup-and-install/multi-dc-cp-to-cp-communication.png)

Follow the steps below to configure the control plane node(s) in region 1 to communicate with the region 2 control plane. Similarly region 1 configurations should be added to the region 2 control plane.

1.   Add the following event publishers to the `<APIM-HOME>/repository/deployment/server/eventpublishers` directory of the control plane.

**notificationJMSPublisherRegion2.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
  <eventPublisher name="notificationJMSPublisherRegion2" statistics="disable"
  trace="disable"
  xmlns="http://wso2.org/carbon/eventpublisher">
  <from streamName="org.wso2.apimgt.notification.stream" version="1.0.0"/>
  <mapping customMapping="disable" type="json"/>
  <to eventAdapterType="jms">
  <property name="java.naming.factory.initial">org.wso2.andes.jndi.PropertiesFileInitialContextFactory</property>
  <property name="java.naming.provider.url">repository/conf/jndi-region2.properties</property>
  <property name="transport.jms.DestinationType">topic</property>
  <property name="transport.jms.Destination">notification</property>
  <property name="transport.jms.ConcurrentPublishers">allow</property>
  <property name="transport.jms.ConnectionFactoryJNDIName">TopicConnectionFactory</property>
  </to>
  </eventPublisher>
```

**tokenRevocationJMSPublisherRegion2.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
  <eventPublisher name="tokenRevocationJMSPublisherRegion2" statistics="disable"
                  trace="disable"
      xmlns="http://wso2.org/carbon/eventpublisher">
      <from streamName="org.wso2.apimgt.token.revocation.stream" version="1.0.0"/>
      <mapping customMapping="disable" type="json"/>
      <to eventAdapterType="jms">
          <property name="java.naming.factory.initial">org.wso2.andes.jndi.PropertiesFileInitialContextFactory</property>
          <property name="java.naming.provider.url">repository/conf/jndi-region2.properties</property>
          <property name="transport.jms.DestinationType">topic</property>
          <property name="transport.jms.Destination">tokenRevocation</property>
          <property name="transport.jms.ConcurrentPublishers">allow</property>
          <property name="transport.jms.ConnectionFactoryJNDIName">TopicConnectionFactory</property>
      </to>
  </eventPublisher>
```

**keymgtEventJMSEventPublisherRegion2.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
  <eventPublisher name="keymgtEventJMSEventPublisherRegion2" statistics="disable"
    trace="disable" xmlns="http://wso2.org/carbon/eventpublisher">
    <from streamName="org.wso2.apimgt.keymgt.stream" version="1.0.0"/>
    <mapping customMapping="disable" type="json"/>
    <to eventAdapterType="jms">
      <property name="java.naming.factory.initial">org.wso2.andes.jndi.PropertiesFileInitialContextFactory</property>
      <property name="java.naming.provider.url">repository/conf/jndi-region2.properties</property>
      <property name="transport.jms.DestinationType">topic</property>
      <property name="transport.jms.Destination">keyManager</property>
      <property name="transport.jms.ConcurrentPublishers">allow</property>
      <property name="transport.jms.ConnectionFactoryJNDIName">TopicConnectionFactory</property>
    </to>
  </eventPublisher>
```

**asyncWebhooksEventPublisherRegion2.xml** (This is optional only if you have webhook streaming APIs in your deployment)

```
<?xml version="1.0" encoding="UTF-8"?>
      <eventPublisher name="asyncWebhooksEventPublisher-1.0.0-Region2" statistics="disable" processing="disable"
      trace="disable"
      xmlns="http://wso2.org/carbon/eventpublisher">
      <from streamName="org.wso2.apimgt.webhooks.request.stream" version="1.0.0"/>
      <mapping customMapping="disable" type="json"/>
      <to eventAdapterType="jms">
      <property name="java.naming.factory.initial">org.wso2.andes.jndi.PropertiesFileInitialContextFactory</property>
      <property name="java.naming.provider.url">repository/conf/jndi2-region2.properties</property>
      <property name="transport.jms.DestinationType">topic</property>
      <property name="transport.jms.Destination">asyncWebhooksData</property>
      <property name="transport.jms.ConcurrentPublishers">allow</property>
      <property name="transport.jms.ConnectionFactoryJNDIName">TopicConnectionFactory</property>
      </to>
      </eventPublisher>
```

**blockingEventJMSPublisherRegion2.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
  <eventPublisher name="blockingEventJMSPublisher" statistics="disable"
    trace="disable" xmlns="http://wso2.org/carbon/eventpublisher">
    <from streamName="org.wso2.blocking.request.stream" version="1.0.0"/>
    <mapping customMapping="disable" type="json"/>
    <to eventAdapterType="jms">
      <property name="java.naming.factory.initial">org.wso2.andes.jndi.PropertiesFileInitialContextFactory</property>
      <property name="java.naming.provider.url">repository/conf/jndi2-region2.properties</property>
      <property name="transport.jms.DestinationType">topic</property>
      <property name="transport.jms.Destination">throttleData</property>
      <property name="transport.jms.ConcurrentPublishers">allow</property>
      <property name="transport.jms.ConnectionFactoryJNDIName">TopicConnectionFactory</property>
    </to>
  </eventPublisher>
```

1.   Add the following JNDI configuration file to `<APIM-HOME>/repository/conf directory`.

**jndi-region2.properties**

```
connectionfactory.TopicConnectionFactory = amqp://admin:admin@clientid/carbon?brokerlist='tcp://<region2-cp-host>:5672'

  topic.tokenRevocation = tokenRevocation
  topic.keyManager = keyManager
  topic.notification = notification
  topic.asyncWebhooksData = asyncWebhooksData
```

 Replace `<region2-cp-host>` with the host of the control plane of the region where this data is published. In pattern 1, all the event hubs publish data to all the eventhubs. Therefore, all the event hubs (control plane nodes) in all the regions should be configured to publish data to other regions. 
Optional Step[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/#optional-step "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have secondary user stores, make sure that the userstores directory is shared between the regions.

Note

When a secondary user store is initially added, a new directory called userstores will be created at /repository/deployment/server location. All the secondary user store related configurations will be stored in the userstores directory.

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/tutorials/authentication.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/tutorials/authentication.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/tutorials/authentication.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/tutorials/authentication.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/tutorials/authentication.md

# Source: https://docs.pinot.apache.org/operators/tutorials/authentication.md

# Authentication

Apache Pinot 0.8.0+ comes out of the box with support for HTTP Basic Auth. While disabled by default for easier setup, authentication and authorization can be added to any environment simply via configuration. ACLs can be set on both API and table levels. This upgrade can be performed with zero downtime in any environment that provides replication.

For external access, Pinot exposes two primary APIs via the following components:

* **pinot-controller** handles cluster management and configuration
* **pinot-broker** handles incoming SQL queries

Both components can be protected via auth and even be configured independently. This makes it is possible to separate accounts for administrative functions such as table creation from accounts that are read the contents of tables in production.

Additionally, all other Pinot components such as **pinot-server** and **pinot-minion** can be configured to authenticate themselves to pinot-controller via the same mechanism. This can be done independently of (and in addition to) using 2-way TLS/SSL to ensure intra-cluster authentication on the lower networking layer.

## Quickstart

If you'd rather dive directly into the action with an all-in-one running example, we provide an **AuthQuickstart** runnable with Apache Pinot. This sample app is preconfigured with the settings below but intended only as a dev-friendly, local, single-node deployment.

{% content-ref url="authentication/basic-auth-access-control" %}
[basic-auth-access-control](https://docs.pinot.apache.org/operators/tutorials/authentication/basic-auth-access-control)
{% endcontent-ref %}

{% content-ref url="authentication/zkbasicauthaccesscontrol" %}
[zkbasicauthaccesscontrol](https://docs.pinot.apache.org/operators/tutorials/authentication/zkbasicauthaccesscontrol)
{% endcontent-ref %}

##

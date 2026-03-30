# Source: https://docs.pinot.apache.org/release-0.9.0/operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/operating-pinot/rebalance.md

# Source: https://docs.pinot.apache.org/operators/operating-pinot/rebalance.md

# Rebalance

Rebalance operation is used to recompute assignment of brokers or servers in the cluster. This is not a single command, but more of a series of steps that need to be taken.

In case of servers, rebalance operation is used to balance the distribution of the segments amongst the servers being used by a Pinot table. This is typically done after capacity changes, or config changes such as replication or segment assignment strategies.

In case of brokers, rebalance operation is used to recalculate the broker assignment to the tables. This is typically done after capacity changes (scale up/down brokers).

In few cases such as when a server is tagged or untagged to a tenant i.e. server is added or removed from a tenant we need to rebalance all the tables that belong to that tenant.

{% content-ref url="rebalance/rebalance-servers" %}
[rebalance-servers](https://docs.pinot.apache.org/operators/operating-pinot/rebalance/rebalance-servers)
{% endcontent-ref %}

{% content-ref url="rebalance/rebalance-brokers" %}
[rebalance-brokers](https://docs.pinot.apache.org/operators/operating-pinot/rebalance/rebalance-brokers)
{% endcontent-ref %}

{% content-ref url="rebalance/rebalance-tenant" %}
[rebalance-tenant](https://docs.pinot.apache.org/operators/operating-pinot/rebalance/rebalance-tenant)
{% endcontent-ref %}

##

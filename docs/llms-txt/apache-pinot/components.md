# Source: https://docs.pinot.apache.org/release-0.4.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-0.9.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/components.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/components.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/concepts/components.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/concepts/components.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/concepts/components.md

# Source: https://docs.pinot.apache.org/basics/concepts/components.md

# Components

Apache Pinot™ is a database designed to deliver highly concurrent, ultra-low-latency queries on large datasets through a set of common data model abstractions. Delivering on these goals requires several foundational architectural commitments, including:

* Storing data in columnar form to support high-performance scanning
* Sharding of data to scale both storage and computation
* A distributed architecture designed to scale capacity linearly
* A tabular data model read by SQL queries

## Components

Learn about the major components and logical abstractions used in Pinot.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M60c-RR9kCYIjTMDn2J%2F-M60c8gIYuj9VugbZGLf%2Fpinot-system-architecture.png?alt=media\&token=a17c7347-2625-4091-ad3f-911ec126eb86)

#### Operator reference

{% content-ref url="components/cluster" %}
[cluster](https://docs.pinot.apache.org/basics/concepts/components/cluster)
{% endcontent-ref %}

{% content-ref url="components/cluster/controller" %}
[controller](https://docs.pinot.apache.org/basics/concepts/components/cluster/controller)
{% endcontent-ref %}

{% content-ref url="components/cluster/broker" %}
[broker](https://docs.pinot.apache.org/basics/concepts/components/cluster/broker)
{% endcontent-ref %}

{% content-ref url="components/cluster/server" %}
[server](https://docs.pinot.apache.org/basics/concepts/components/cluster/server)
{% endcontent-ref %}

{% content-ref url="components/cluster/minion" %}
[minion](https://docs.pinot.apache.org/basics/concepts/components/cluster/minion)
{% endcontent-ref %}

{% content-ref url="components/cluster/tenant" %}
[tenant](https://docs.pinot.apache.org/basics/concepts/components/cluster/tenant)
{% endcontent-ref %}

#### Developer reference

{% content-ref url="components/table" %}
[table](https://docs.pinot.apache.org/basics/concepts/components/table)
{% endcontent-ref %}

{% content-ref url="components/table/schema" %}
[schema](https://docs.pinot.apache.org/basics/concepts/components/table/schema)
{% endcontent-ref %}

{% content-ref url="components/table/segment" %}
[segment](https://docs.pinot.apache.org/basics/concepts/components/table/segment)
{% endcontent-ref %}

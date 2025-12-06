# Source: https://docs.vespa.ai/en/reference/applications/services/services.html.md

# services.xml

 

_services.xml_ specifies the clusters an application should have and their capabilities. It is placed in the root of the[application package](../../../basics/applications.html).

Elements:

```
[services [version]](#services)[container [version]](container.html)- specifies a container cluster[content [version]](content.html)- specifies a content cluster[admin [version]](admin.html)- control plane configuration (rarely needed)[routing [version] - how content should be routed (rarely needed)](../../../writing/document-routing.html#routing-services)
```

## \<services\>

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| version | required | number | | 1.0 in this version of Vespa |

Optional subelements (one or more of _container_ or _content_ is required):

- [\<container\>](container.html)
- [\<content\>](content.html)
- [\<admin\>](admin.html)
- [\<routing\>](../../../writing/document-routing.html#routing-services)

The rest of this document describes tags that are used within multiple services tags.

## \<nodes\>

The _nodes_ element configures the hardware resources of a cluster, and so is used in both container and content clusters. This tag works differently on Vespa Cloud and self-managed instances:

- Vespa Cloud: The number of nodes are specified by a _count_ attribute, and the resources of each node by a [resource](#resources) child element. 
- Self-managed: _nodes_ have a [node](#node) child element for each node, A node referred to in _services.xml_ must be defined in [hosts.xml](../hosts.html) using _hostalias_. 

It is possible to specify both to make an application package work in both environments, and it is always possible to deploy either type for development on the other: When the nodes tag has Vespa Cloud content it is interpreted as a single-node cluster in a self-hosted environment and vice versa.

| Attribute | type | Default | Description |
| --- | --- | --- | --- |
| **count** | integer or range | | Vespa Cloud: The number of nodes of the cluster. |
| **exclusive** | boolean | false | Optional. Vespa Cloud: If true these nodes will never be placed on shared hosts even when this would otherwise be allowed (which is only for content nodes in some environments). When nodes are allocated exclusively, the resources must match the resources of the host exactly. |
| **groups** | integer or range | | Vespa Cloud content nodes only, optional: Integer or range. Sets the number of groups into which content nodes should be divided. Each group will have an equal share of the nodes, and one or more complete copies of the corpus and index, and each query will be routed to just one group - see [grouped distribution](/en/content/elasticity.html#grouped-distribution). This allows [scaling](/en/performance/sizing-examples.html) to a higher query load than is possible with just a single group. |
| **group-size** | integer or range | | Vespa Cloud content nodes only, optional: Integer or range where either value can be skipped (replaced by an empty string) to create a one-sided limit. This can be set as an alternative to explicitly setting `groups`: The group sizes used will always be within these limits (inclusive), for any `count`. |

If neither _groups_ nor _group-size_ is set, all nodes belong to a single group. Read more in [topology](../../../performance/topology-and-resizing).

Ranges are expressed by the syntax `[lower-limit, upper-limit]`; Both limits are inclusive. Any value set as a range will be [autoscaled](../../../operations/autoscaling.html).

## \<resources\>

Under [nodes](#nodes) on Vespa Cloud: Specifies the resources each node in the cluster should have.

The resources must match a node flavor in[AWS](https://cloud.vespa.ai/en/reference/aws-flavors.html),[GCP](https://cloud.vespa.ai/en/reference/gcp-flavors.html)[Azure](https://cloud.vespa.ai/en/reference/azure-flavors.html), depending on where you are deploying. Exception: If you use remote disk, you can specify any number lower than the max size.

**Subelements:** [\<gpu\>](#gpu)

| Attribute | type | Default | Description |
| --- | --- | --- | --- |
| **vcpu** | float or range | 2 | CPU (virtual threads) |
| **memory** | float or range, each followed by a byte unit, such as "Gb" | 8 Gb in container clusters, 16 Gb in content clusters | Memory |
| **disk** | float or range, each followed by a byte unit, such as "Gb" | 50 in container clusters, 300 in content clusters | Disk space. To fit core dumps/heap dumps, the disk space should be larger than 3 x memory size for content nodes, 2 x memory size for container nodes. |
| **storage-type** | string (enum) | `any` | The type of storage to use. This is useful to specify local storage when network storage provides insufficient io operations or too noisy io performance: 
- `local`: Node-local storage is required.
- `remote`: Network storage must be used.
- `any`: Both remote or local storage may be used.

 |
| **disk-speed** | string (enum) | `fast` | The required disk speed category: 
- `fast`: SSD-like disk speed is required
- `slow`: This is sized for spinning disk speed
- `any`: Performance does not depend on disk speed (often suitable for container clusters).

 |
| **architecture** | string (enum) | `any` | Node CPU architecture: 
- `x86_64`
- `arm64`
- `any`: Use any of the available architectures.

 |

Ranges are expressed by the syntax `[lower-limit, upper-limit]`; Both limits are inclusive. Any value set as a range will be [autoscaled](../../../operations/autoscaling.html).

## \<node\>

Under [nodes](#nodes) on self-managed systems: Specifies a node that should be a member in the cluster.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| hostalias | required | string | | 

a host name which must be mapped to a full hostname in [hosts.xml](../hosts.html)

 |

## \<gpu\>

Under [resources](#resources) on Vespa Cloud: Declares GPU resources to provision.

Limitations:

- Available in AWS zones only
- Valid for container clusters only

| Attribute | type | Description |
| --- | --- | --- |
| **count** | integer | Number of GPUs |
| **memory** | integer, followed by a byte unit, such as "Gb" | Amount of memory per GPU. Total amount of GPU memory available is this number multiplied by `count`. |

Example:

```
```
<nodes count="2">
    <resources vcpu="4" memory="16Gb" disk="125Gb">
        <gpu count="1" memory="16Gb"/>
    </resources>
</nodes>
```
```

## Generic configuration using \<config\>

Most elements in _services.xml_ accept a sub-element named _config_._config_ elements can be included on different levels in the XML structure and the lower-level ones will override values in the higher-level ones (example below). The _config_ element must include the attribute _name_, which gives the full name of the configuration option in question, including the namespace. The name can either refer to configuration definitions that are shipped with Vespa or ones that are part of the [application package](../config-files.html). For a complete example on generic configuration see the[application package](../config-files.html#generic-configuration-in-services-xml) reference.

```
```
<container id="default" version="1.0">
    <handler id="com.yahoo.vespatest.ConfiguredHandler">
        <config name="vespatest.response">
            <response>configured string</response>
        </config>
    </handler>
</container>
```
```

## Modular Configuration

Some features are configurable using XML files in subdirectories of the application package. This means that the configuration found in these XML files will be used as if it was inlined in _services.xml_. This is supported for [search chains](search.html#chain),[docproc chains](docproc.html) and[routing tables](../../../writing/document-routing.html#routing-services).

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [\<services\>](#services)
- [\<nodes\>](#nodes)
- [\<resources\>](#resources)
- [\<node\>](#node)
- [\<gpu\>](#gpu)
- [Generic configuration using \<config\>](#generic-config)
- [Modular Configuration](#modular)


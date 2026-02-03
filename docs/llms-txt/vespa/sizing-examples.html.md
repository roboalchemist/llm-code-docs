# Source: https://docs.vespa.ai/en/performance/sizing-examples.html.md

# Vespa Scaling Configuration Examples

 

This guide has a set of example configurations for content clusters using flat or grouped data distribution. Data is distributed over nodes and groups using a Vespa's [distribution algorithm](../reference/applications/services/content.html#distribution). See [Scaling Vespa](sizing-search.html) for when to use grouped or flat data distribution. These examples illustrate common deployment patterns. In all examples, the number of stateless [container](../jdisc/) nodes is fixed. The examples are [services.xml](../reference/applications/services/content.html) deployed using [Application Packages](../application-packages.html).

Refer to the [multinode-HA](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode-HA) sample application for how to get started from a deployable multinode starting point. The examples below are trimmed down for readability in the `admin` and `container` sections. See the [appendix](#appendix-hosts-xml) for _hosts.xml_ to use when testing deployments.

Also read [changing topology](/en/content/elasticity.html#changing-topology) and [topology and resizing](https://cloud.vespa.ai/en/topology-and-resizing) is intro documents before continuing.

## Flat Distribution

Flat (single group) distribution with [min-redundancy](../reference/applications/services/content.html#min-redundancy)=3. Data is distributed and partitioned over 9 nodes and there are 3 replicas of each document, stored on 3 different nodes. Queries are dispatched in parallel to all nodes. In case of a node failure, the remaining nodes will index (make ready) and activate the _not ready_ (stored) copies to restore full search coverage.

```
```
<services version="1.0">
    <admin version="2.0">
        <configservers>
            <configserver hostalias="node0" />
        </configservers>
        <cluster-controllers>
            <cluster-controller hostalias="node0" />
        </cluster-controllers>
        <slobroks>
            <slobrok hostalias="node0" />
        </slobroks>
        <adminserver hostalias="node0" />
    </admin>

    <container id="stateless-container-cluster" version="1.0">
        <search/>
        <document-api/>
        <nodes>
            <node hostalias="node0"/>
        </nodes>
    </container>

    <content id="my-content" version="1.0">
        <documents>
            <document type="music" mode="index"/>
        </documents>
        <min-redundancy>3</min-redundancy>
        <nodes>
            <node hostalias="node0" distribution-key="0"/>
            <node hostalias="node1" distribution-key="1"/>
            <node hostalias="node2" distribution-key="2"/>
            <node hostalias="node3" distribution-key="3"/>
            <node hostalias="node4" distribution-key="4"/>
            <node hostalias="node5" distribution-key="5"/>
            <node hostalias="node6" distribution-key="6"/>
            <node hostalias="node7" distribution-key="7"/>
            <node hostalias="node8" distribution-key="8"/>
        </nodes>
    </content>
</services>
```
```

## Grouped Distribution

When using grouped distribution in an indexed content cluster, the following restrictions apply:

- There can only be a single level of leaf groups under the top group
- Each leaf group must have the same number of nodes 
- The number of leaf groups must be a factor of the _redundancy_
- The [distribution partitions](../reference/applications/services/content.html#distribution) must be specified such that the redundancy per group is equal

With a low number of nodes per group, it's important to remember that a node failure will cause the data to be re-distributed to the remaining nodes and their memory footprint and disk usage will grow when those nodes start activating the documents originally activated on the failed node. E.g. with 2 nodes per group, the remaining healthy node will start activating all the content, which will cause a 2x memory and disk footprint compared with the ideal state.

The [min-node-ratio-per-group](../reference/applications/services/content.html#min-node-ratio-per-group) controls the data distribution behavior inside a group in cases of node failures. This sets a lower bound on the ratio of nodes within groups that must be online and accepting feed and query traffic, before the entire group is automatically taken out of service from both feed and search/serving. Once number of nodes in the group have been restored, and ideal state has been achieved, the group will be automatically set in service.

## 9 nodes, 3 groups with 3 nodes per group

This example has 3 groups and each group index all the documents over the 3 nodes in the group. With 3 groups there are 3 replicas in total of each document, and each replica is indexed and active. Losing a node does not reduce search coverage.

```
```
<services version="1.0">
    <admin version="2.0">
        <configservers>
            <configserver hostalias="node0" />
        </configservers>
        <cluster-controllers>
            <cluster-controller hostalias="node0" />
        </cluster-controllers>
        <slobroks>
            <slobrok hostalias="node0" />
        </slobroks>
        <adminserver hostalias="node0" />
    </admin>

    <container id="stateless-container-cluster" version="1.0">
        <search/>
        <document-api/>
        <nodes>
            <node hostalias="node0"/>
        </nodes>
    </container>

    <content id="my-content" version="1.0">
        <documents>
            <document type="music" mode="index"/>
        </documents>
        <min-redundancy>3</min-redundancy>
        <group>
            <distribution partitions="1|1|*"/>
            <group name="group0" distribution-key="0">
                <node hostalias="node0" distribution-key="0"/>
                <node hostalias="node1" distribution-key="1"/>
                <node hostalias="node2" distribution-key="2"/>
            </group>
            <group name="group1" distribution-key="1">
                <node hostalias="node3" distribution-key="3"/>
                <node hostalias="node4" distribution-key="4"/>
                <node hostalias="node5" distribution-key="5"/>
            </group>
            <group name="group2" distribution-key="2">
                <node hostalias="node6" distribution-key="6"/>
                <node hostalias="node7" distribution-key="7"/>
                <node hostalias="node8" distribution-key="8"/>
            </group>
        </group>
    </content>
</services>
```
```

## 9 nodes, 9 groups with 1 node per group

This example has 9 groups and each group index all the documents on a single node. With 9 groups there are 9 replicas in total of each document, and each replica is indexed and active. Losing a node does not reduce search coverage. With a single node, indexing throughput is limited by the single node performance, as all data needs to go all nodes.

```
```
<services version="1.0">
    <admin version="2.0">
        <configservers>
            <configserver hostalias="node0" />
        </configservers>
        <cluster-controllers>
            <cluster-controller hostalias="node0" />
        </cluster-controllers>
        <slobroks>
            <slobrok hostalias="node0" />
        </slobroks>
        <adminserver hostalias="node0" />
    </admin>

    <container id="stateless-container-cluster" version="1.0">
        <search/>
        <document-api/>
        <nodes>
            <node hostalias="node0"/>
        </nodes>
    </container>

    <content id="my-content" version="1.0">
        <documents>
            <document type="music" mode="index"/>
        </documents>
        <min-redundancy>9</min-redundancy>
        <group>
            <distribution partitions="1|1|1|1|1|1|1|1|*"/>
            <group name="group0" distribution-key="0">
                <node hostalias="node0" distribution-key="0"/>
            </group>
            <group name="group1" distribution-key="1">
                <node hostalias="node1" distribution-key="1"/>
            </group>
            <group name="group2" distribution-key="2">
                <node hostalias="node2" distribution-key="2"/>
            </group>
            <group name="group3" distribution-key="3">
                <node hostalias="node3" distribution-key="3"/>
            </group>
            <group name="group4" distribution-key="4">
                <node hostalias="node4" distribution-key="4"/>
            </group>
            <group name="group5" distribution-key="5">
                <node hostalias="node5" distribution-key="5"/>
            </group>
            <group name="group6" distribution-key="6">
                <node hostalias="node6" distribution-key="6"/>
            </group>
            <group name="group7" distribution-key="7">
                <node hostalias="node7" distribution-key="7"/>
            </group>
            <group name="group8" distribution-key="8">
                <node hostalias="node8" distribution-key="8"/>
            </group>
        </group>
    </content>
</services>
```
```

## Serving Availability Tuning

When using flat distribution, _soft failing nodes_ is a challenge for serving with high availability and low latency. Soft failing nodes are nodes which answers health checks from [cluster controllers](../content/content-nodes.html) and search container dispatch health checks, but still experiences issues which impacts serving latency (e.g. cpu frequency throttling due to thermal heating, memory corruptions and so forth). In a cluster with a flat distribution, the slowest node determines the latency, as the query request is dispatched to all content nodes in parallel. The probability of a soft failing node increases with the number of nodes used to distribute the data over.

Use [adaptive coverage timeout](../reference/applications/services/content.html#coverage) to prevent slow soft failing nodes to impact availability. This allows the dispatcher to stop waiting for the slowest node(s). See also [graceful search degradation](graceful-degradation.html).

Grouped distributions are less impacted by soft failing nodes in general, as queries are dispatched to one group at a time using a [dispatch policy](../reference/applications/services/content.html#dispatch-policy). The _adaptive_ policy takes group latency into account when deciding which group the query request should be routed to.

## Changing Group Configuration

It is easy to change the group topology without service disruption, with a few caveats - read more in [elasticity](../content/elasticity.html#changing-topology).

## Appendix: hosts.xml

```
```
<hosts>
    <host name="localhost">
        <alias>node0</alias>
    </host>
    <host name="localhost1">
        <alias>node1</alias>
    </host>
    <host name="localhost2">
        <alias>node2</alias>
    </host>
    <host name="localhost3">
        <alias>node3</alias>
    </host>
    <host name="localhost4">
        <alias>node4</alias>
    </host>
    <host name="localhost5">
        <alias>node5</alias>
    </host>
    <host name="localhost6">
        <alias>node6</alias>
    </host>
    <host name="localhost7">
        <alias>node7</alias>
    </host>
    <host name="localhost8">
        <alias>node8</alias>
    </host>
</hosts>
```
```

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Flat Distribution](#flat-distribution)
- [Grouped Distribution](#grouped-distribution)
- [9 nodes, 3 groups with 3 nodes per group](#9-nodes-3-groups-with-3-nodes-per-group)
- [9 nodes, 9 groups with 1 node per group](#9-nodes-3-groups-with-1-node-per-group)
- [Serving Availability Tuning](#serving-availability-tuning)
- [Changing Group Configuration](#changing-group-configuration)
- [Appendix: hosts.xml](#appendix-hosts-xml)


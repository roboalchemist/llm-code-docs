# Source: https://documentation.wazuh.com/current/user-manual/wazuh-indexer/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Wazuh indexer

The Wazuh indexer is a real-time, full-text search and analytics engine for security data. Log data ingested into the Wazuh server is analyzed and forwarded to the indexer for indexing and storage. These events are then queried on the Wazuh dashboard.

The Wazuh indexer stores data as JSON documents. Each document associates a set of keys, field names, or attributes with their corresponding values, which can be characters, numbers, booleans, dates, arrays of values, geolocations, or other kinds of data.

The Wazuh indexer can be configured as a single-node or multi-node cluster, providing scalability and high availability. It distributes documents across different containers, known as shards. In turn, it distributes these shards across cluster nodes. By distributing the documents across multiple shards and distributing those shards across multiple nodes, the Wazuh indexer ensures redundancy. Redundancy ensures the Wazuh indexer's availability in the event of a failure and boosts query capacity across cluster nodes.

> ##### Contents
> 
> * [Wazuh indexer indices](wazuh-indexer-indices.md)
> * [Re-indexing](re-indexing.md)
> * [Wazuh indexer tuning](wazuh-indexer-tuning.md)
> * [Migrating Wazuh indices](migrating-wazuh-indices.md)
> * [Wazuh indexer configuration on hardened endpoints](wazuh-indexer-on-hardened-endpoints.md)

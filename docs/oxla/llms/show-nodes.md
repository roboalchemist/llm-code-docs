# Source: https://docs.oxla.com/sql-reference/sql-statements/show-nodes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SHOW NODES

## Overview

The `SHOW NODES` statement returns the current state of the cluster and is only available to the superuser.

<Info>It is not case-sensitive, so `show nodes`, `Show Nodes`, and `SHOW NODES` do the same thing</Info>

## Example

To view the current cluster state, you need to execute the following command:

```sql  theme={null}
SHOW NODES;
```

Once it's done, you'll see a table with the information about each node in the cluster, in a following way:

```sql  theme={null}
     name      | election_state  | followers_count | connected_nodes_count | degradation_error 
---------------+-----------------+-----------------+-----------------------+-------------------
 n_oxla_node_1 | LEADER_FOLLOWER |               0 |                     3 | 
 n_oxla_node_3 | LEADER          |               3 |                     3 | 
 n_oxla_node_2 | LEADER_FOLLOWER |               0 |                     3 | 
(3 rows)
```

Each row represents the state of an individual node within the cluster, where:

* `name`: name of the node
* `election_state`: current state of the node (e.g. `LEADER`)
* `followers_count`: number of nodes following the leader, which applies to the leader node
* `connected_nodes_count`: total number of nodes connected, including itself
* `degradation_error`: error message if the node is not working correctly, otherwise it shows `NULL`

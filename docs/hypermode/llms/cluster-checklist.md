# Source: https://docs.hypermode.com/dgraph/self-managed/cluster-checklist.md

# Cluster Checklist

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

In setting up a cluster be sure the check the following.

* Is at least one Dgraph Zero node running?
* Is each Dgraph Alpha instance in the cluster set up correctly?
* Will each Dgraph Alpha instance be accessible to all peers on 7080 (+ any port
  offset)?
* Does each instance have a unique ID on startup?
* Has `--bindall=true` been set for networked communication?

See the [Production Checklist](./production-checklist) docs for more info.

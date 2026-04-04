# Source: https://docs.hypermode.com/dgraph/self-managed/cluster-types.md

# Cluster Types

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

### Terminology

An N-node cluster is a Dgraph cluster that contains N number of Dgraph
instances. For example, a 6-node cluster means six Dgraph instances. The
replication setting specifies the number of Dgraph Alpha replicas that are in
each group. If this is higher than 1, each Alpha in a group holds a full copy of
that group's data. The replication setting is a configuration flag
(`--replicas`) on Dgraph Zero. Sharding is done (typically for databases near 1
TB in size) by creating multiple Dgraph Alpha groups. Every Dgraph Alpha group
is automatically assigned a set of distinct predicates to store and serve, thus
dividing up the data.

Examples of different cluster settings:

* No sharding
  * 2-node cluster: 1 Zero, 1 Alpha (one group).
  * HA equivalent: x3 = 6-node cluster.
* With 2-way sharding:
  * 3-node cluster: 1 Zero, 2 Alphas (two groups).
  * HA equivalent: x3 = 9-node cluster.

In the following examples we outline the two most common cluster configurations:
a 2-node cluster and a 6-node cluster.

### Basic setup: 2-node cluster

We provide sample configuration for both
[Docker Compose](https://github.com/hypermodeinc/dgraph/blob/master/contrib/config/docker/docker-compose.yml)
and
[Kubernetes](https://github.com/hypermodeinc/dgraph/tree/master/contrib/config/kubernetes/dgraph-single)
for a 2-node cluster. You can also run Dgraph directly on your host machines.

<img src="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=4704ea077054e654329816d19e7e73e3" alt="2-node cluster" width="585" height="150" data-path="images/dgraph/self-managed/deploy-guide-1.png" srcset="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?w=280&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=838ced42aed9a730803b8c76b3c9e66d 280w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?w=560&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=4ee3183a22990242f1087ac66bb1d7fa 560w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?w=840&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=cf1221f90bfdd67d39539eba0b735292 840w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?w=1100&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=7a9922ea7e04d948a45c9f90f3d2e25f 1100w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?w=1650&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=cb43653517d462a5c9535c63139cbd8f 1650w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-1.png?w=2500&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=15f169dec9a340437087c8a576d107d3 2500w" data-optimize="true" data-opv="2" />

Configuration can be set either as command-line flags, environment variables, or
in a file (see [Configuration](./config)).

Dgraph Zero:

* The `--my` flag should be set to the address:port (the internal-gRPC port)
  that's accessible to the Dgraph Alpha (default: `localhost:5080`).
* The `--raft` superflag's `idx` option should be set to a unique Raft ID within
  the Dgraph Zero group (default: `1`).
* The `--wal` flag should be set to the directory path to store write-ahead-log
  entries on disk (default: `zw`).
* The `--bindall` flag should be set to true for machine-to-machine
  communication (default: `true`).
* Recommended: For better issue diagnostics, set the log level verbosity to 2
  with the option `--v=2`.

Dgraph Alpha:

* The `--my` flag should be set to the address:port (the internal-gRPC port)
  that's accessible to the Dgraph Zero (default: `localhost:7080`).
* The `--zero` flag should be set to the corresponding Zero address set for
  Dgraph Zero's `--my` flag.
* The `--postings` flag should be set to the directory path for data storage
  (default: `p`).
* The `--wal` flag should be set to the directory path for write-ahead-log
  entries (default: `w`)
* The `--bindall` flag should be set to true for machine-to-machine
  communication (default: `true`).
* Recommended: For better issue diagnostics, set the log level verbosity to 2
  `--v=2`.

### High availability setup: 6-node cluster

We provide sample configuration for both
[Docker Compose](https://github.com/hypermodeinc/dgraph/blob/master/contrib/config/docker/docker-compose-ha.yml)
and
[Kubernetes](https://github.com/hypermodeinc/dgraph/tree/master/contrib/config/kubernetes/dgraph-ha)
for a 6-node cluster with 3 Alpha replicas per group. You can also run Dgraph
directly on your host machines.

A Dgraph cluster can be configured in a high-availability setup with Dgraph Zero
and Dgraph Alpha each set up with peers. These peers are part of Raft consensus
groups, which elect a single leader among themselves. The non-leader peers are
called followers. In the event that the peers can't communicate with the leader
(for example, a network partition or a machine shuts down), the group
automatically elects a new leader to continue.

Configuration can be set either as command-line flags, environment variables, or
in a file (see [Configuration](./config)).

In this setup, we assume the following hostnames are set:

* `zero1`
* `zero2`
* `zero3`
* `alpha1`
* `alpha2`
* `alpha3`

We configure the cluster with 3 Alpha replicas per group. The cluster
group-membership topology looks like the following:

<img src="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=f736c59262c1de1196527b5f4ba793cf" alt="Dgraph cluster image" width="566" height="145" data-path="images/dgraph/self-managed/deploy-guide-2.png" srcset="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?w=280&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=710c4a151d99fdd0174bc2ba439255e8 280w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?w=560&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=6d49c4bfc7f0934fea5b17f39e16350e 560w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?w=840&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=57989cddf9091e3871b9f035f8aedf04 840w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?w=1100&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=bca8976a6d120202ae15c3733f47750b 1100w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?w=1650&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=308b18eb112ef1aa0f70040372889898 1650w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/self-managed/deploy-guide-2.png?w=2500&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=925e0291f7fbdb94df80e6e8f5cb9584 2500w" data-optimize="true" data-opv="2" />

#### Set up Dgraph Zero group

In the Dgraph Zero group you must set unique Raft IDs (`--raft` superflag's
`idx` option) per Dgraph Zero. Dgraph will not auto-assign Raft IDs to Dgraph
Zero instances.

The first Dgraph Zero that starts will initiate the database cluster. Any
following Dgraph Zero instances must connect to the cluster via the `--peer`
flag to join. If the `--peer` flag is omitted from the peers, then the Dgraph
Zero will create its own independent Dgraph cluster.

**First Dgraph Zero** example:
`dgraph zero --replicas=3 --raft idx=1 --my=zero1:5080`

The `--my` flag must be set to the address:port of this instance that peers will
connect to. The `--raft` superflag's `idx` option sets its Raft ID to `1`.

**Second Dgraph Zero** example:
`dgraph zero --replicas=3 --raft idx=2 --my=zero2:5080 --peer=zero1:5080`

The `--my` flag must be set to the address:port of this instance that peers will
connect to. The `--raft` superflag's `idx` option sets its Raft ID to 2, and the
`--peer` flag specifies a request to connect to the Dgraph cluster of zero1
instead of initializing a new one.

**Third Dgraph Zero** example:
`dgraph zero --replicas=3 --raft idx=3 --my=zero3:5080 --peer=zero1:5080`:

The `--my` flag must be set to the address:port of this instance that peers will
connect to. The `--raft` superflag's `idx` option sets its Raft ID to 3, and the
`--peer` flag specifies a request to connect to the Dgraph cluster of zero1
instead of initializing a new one.

Dgraph Zero configuration options:

* The `--my` flag should be set to the address:port (the internal-gRPC port)
  that will be accessible to Dgraph Alpha (default: `localhost:5080`).
* The `--raft` superflag's `idx` option should be set to a unique Raft ID within
  the Dgraph Zero group (default: `1`).
* The `--wal` flag should be set to the directory path to store write-ahead-log
  entries on disk (default: `zw`).
* The `--bindall` flag should be set to true for machine-to-machine
  communication (default: `true`).
* Recommended: For more informative log info, set the log level verbosity to 2
  with the option `--v=2`.

#### Set up Dgraph Alpha group

The number of replica members per Alpha group depends on the setting of Dgraph
Zero's `--replicas` flag. Above, it's set to 3. So when Dgraph Alphas join the
cluster, Dgraph Zero will assign it to an Alpha group to fill in its members up
to the limit per group set by the `--replicas` flag.

First Alpha example: `dgraph alpha --my=alpha1:7080 --zero=zero1:5080`

Second Alpha example: `dgraph alpha --my=alpha2:7080 --zero=zero1:5080`

Third Alpha example: `dgraph alpha --my=alpha3:7080 --zero=zero1:5080`

Dgraph Alpha configuration options:

* The `--my` flag should be set to the address:port (the internal-gRPC port)
  that will be accessible to the Dgraph Zero (default: `localhost:7080`).
* The `--zero` flag should be set to the corresponding Zero address set for
  Dgraph Zero's `--my`flag.
* The `--postings` flag should be set to the directory path for data storage
  (default: `p`).
* The `--wal` flag should be set to the directory path for write-ahead-log
  entries (default: `w`)
* The `--bindall` flag should be set to true for machine-to-machine
  communication (default: `true`).
* Recommended: For more informative log info, set the log level verbosity to 2
  `--v=2`.

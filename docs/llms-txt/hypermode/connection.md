# Source: https://docs.hypermode.com/dgraph/ratel/connection.md

# Connection

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

## Recent servers

This section provides a list of recent connected clusters. You can select any
item on the list to connect.

The list also has an icon which indicates the version of the cluster running:

* Green icon: Running the latest version.
* Yellow icon: Running a specific version.
* Red icon: No connection found.
* Delete icon: Remove the address form the list.

<img src="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=a5fa486b879806201b24fa2a2afb392f" alt="Ratel UI" width="639" height="480" data-path="images/dgraph/ratel/ratel_ui.png" srcset="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?w=280&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=ab73c8cca98f50154d788ba8d859845e 280w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?w=560&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=b648b555eb7cf6bce7d70822e1553da3 560w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?w=840&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=73eb94413d586cc9a8c8b8c6b38ec52e 840w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?w=1100&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=542f292dba4598406a1462e2f93293b6 1100w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?w=1650&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=a72713617657b21311d9930c56f18179 1650w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/ratel/ratel_ui.png?w=2500&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=33c1ceab00c2cd560ea6075c9e62bb65 2500w" data-optimize="true" data-opv="2" />

## URL Input box

In this box you add a valid Dgraph Alpha address. When you click `Connect` Ratel
establishes a connection with the cluster. After Ratel has established a
connection (all icons are green), click the `Continue` button.

Under the input box you have tree icons which gives you the status of the
connection.

* Network Access: Uses an "Energy Plug" icon.
* Server Health: Uses a "Heart" icon.
* Logging in: a "lock" icon.

<Tip>
  To connect to a standard Dgraph instance, you only need to click `Connect`.
  There's a specific section to [login using ACL](#acl-account) ([Enterprise
  feature](/dgraph/enterprise/access-control-lists)).
</Tip>

## Cluster settings

### ACL account

The ACL account login is necessary only when you have ACL features enabled.

<Note>
  The default password for a cluster started from scratch is `password` and the
  user is `groot`.
</Note>

### Dgraph Zero

If you use a custom address for Zero instance, you should inform here.

### Extra settings

Query timeout (seconds): this is a timeout for queries and mutations. If the
operation takes too long, it is dropped after `x` seconds in the cluster.

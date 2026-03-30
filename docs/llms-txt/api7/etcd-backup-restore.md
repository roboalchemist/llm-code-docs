# Source: https://docs.api7.ai/apisix/production/recovery/etcd-backup-restore.md

# Back Up and Restore etcd

etcd clusters are generally fault-tolerant. Still, there might be scenarios where multiple etcd nodes may fail and lose access to the cluster. To recover from such failures, etcd supports backup and restore features for recreating instances without data loss.

Setting up backups can help store the state of an APISIX instance. This is also useful while upgrading APISIX to ensure your configuration is saved.

This document shows how to back up and restore from etcd with both APISIX and etcd running in Docker. Most steps work similarly for other deployments.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [Get APISIX](https://docs.api7.ai/apisix/getting-started/.md) step to install APISIX.
* Complete the [Configure Routes](https://docs.api7.ai/apisix/getting-started/configure-routes.md) guide to create routes.

## Back Up through a Temporary Container[â](#back-up-through-a-temporary-container "Direct link to Back Up through a Temporary Container")

etcd comes packaged with [etcdctl](https://etcd.io/docs/v3.5/dev-guide/interacting_v3/), a CLI for working with the etcd APIs. etcdctl supports the [`etcdctl snapshot`](https://etcd.io/docs/v3.3/op-guide/recovery/) command, which can take a backup of the etcd database.

The example below runs this command on a temporary Docker container and creates a backup in the host machine.

First, create a folder, `backup`, to store the backup in the host machine. This folder is mounted as a volume to the temporary container.

Create the temporary container for backing up etcd in the same network as the APISIX and etcd containers and run the `etcdctl snapshot` command providing the etcd endpoints:

```
export NET_NAME=apisix-quickstart-net
export ETCD_LISTEN_PORT=2379
export ETCD_NAME="etcd-quickstart"

docker run --rm \
    -v ./backup:/backup \
    -e ETCDCTL_API=3 \
    --network "$NET_NAME" \
    bitnami/etcd:3.5.7 \
    etcdctl --endpoints="http://$ETCD_NAME:$ETCD_LISTEN_PORT" snapshot save /backup/snapshot.db
```

If successful, you should see a response similar to the following:

```
{"level":"info","ts":"2024-03-26T06:14:17.173Z","caller":"snapshot/v3_snapshot.go:65","msg":"created temporary db file","path":"/backup/snapshot.db.part"}
{"level":"info","ts":"2024-03-26T06:14:17.178Z","logger":"client","caller":"v3@v3.5.7/maintenance.go:212","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":"2024-03-26T06:14:17.178Z","caller":"snapshot/v3_snapshot.go:73","msg":"fetching snapshot","endpoint":"http://etcd-quickstart:2379"}
{"level":"info","ts":"2024-03-26T06:14:17.182Z","logger":"client","caller":"v3@v3.5.7/maintenance.go:220","msg":"completed snapshot read; closing"}
{"level":"info","ts":"2024-03-26T06:14:17.182Z","caller":"snapshot/v3_snapshot.go:88","msg":"fetched snapshot","endpoint":"http://etcd-quickstart:2379","size":"25 kB","took":"now"}
{"level":"info","ts":"2024-03-26T06:14:17.183Z","caller":"snapshot/v3_snapshot.go:97","msg":"saved","path":"/backup/snapshot.db"}
Snapshot saved at /backup/snapshot.db
```

## Back Up Directly on the etcd Container[â](#back-up-directly-on-the-etcd-container "Direct link to Back Up Directly on the etcd Container")

`etcdctl snapshot` can also be run directly on the etcd container. Note that this might require setting up directory permissions for the Docker container.

```
export ETCD_NAME="etcd-quickstart"
docker exec -e ETCD_LISTEN_PORT=2379 -it $ETCD_NAME etcdctl --endpoints="http://127.0.0.1:$ETCD_LISTEN_PORT" snapshot save ./backup/snapshot.db
```

Make sure to create volume mounts to the host machine so that the `/backup/snapshot.db` file can be accessed in the host machine.

## Back Up from the Host Machine[â](#back-up-from-the-host-machine "Direct link to Back Up from the Host Machine")

etcdctl can be run on the host machine if the etcd API endpoints are accessible. etcd endpoints can be [exposed securely](https://etcd.io/docs/v3.5/op-guide/security/) through TLS.

Note that etcdctl should be installed on the host machine. Download the binaries for the appropriate operating system or use a package manager to install etcdctl.

Run etcdctl on the host machine to save the snapshot:

```
export ETCD_LISTEN_PORT=2379
export ETCD_ADDRESS="127.0.0.1"
etcdctl --endpoints="http://$ETCD_ADDRESS:$ETCD_LISTEN_PORT" snapshot save ./backup/snapshot.db
```

## Restore from Backups[â](#restore-from-backups "Direct link to Restore from Backups")

To restore from a backup, run:

```
etcdctl snapshot restore ./backup/snapshot.db
```

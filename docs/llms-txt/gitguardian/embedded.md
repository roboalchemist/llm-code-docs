# Source: https://docs.gitguardian.com/self-hosting/installation/databases/embedded.md

# Embedded PostgreSQL and Redis

> Use the embedded PostgreSQL and Redis databases included with GitGuardian self-hosted KOTS installations.

## Introduction

To deploy the GitGuardian app, a PostgreSQL instance and a Redis instance are
required. This page is dedicated to helping you set up and managed an embedded
one.

:::caution
The GitGuardian application comes bundled with basic PostgreSQL and Redis. These are suitable for testing and small-scale infrastructures but are not intended for production use. For a more robust setup, we recommend using external, production-grade PostgreSQL and Redis.
:::

## High-Availability

Embedded databases are **not** highly available.

## Installation

Select "Embedded Postgres/Redis" on the configuration page during the
installation, and choose the disk size if needed. But in most cases, the default
disk size is enough.

## Upsizing the disk

### On an existing cluster

If you installed the GitGuardian app on one of your clusters, you need to follow
these steps:

- Make sure your default storage class handles volume expansion
- Check the `allowVolumeExpansion` flag for your default storage class. To get
  information about your storage classes, run `kubectl get storageclasses`:

```bash
> kubectl get storageclasses.storage.k8s.io
NAME                PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
default (default)   ceph.rook.io/block   Delete          Immediate           false                  2d17h
```

- If needed, run `kubectl patch storageclass <your-storage-class-name> -p '{"allowVolumeExpansion": true}'`.
- Go to the KOTS Admin Console, select the "Config" tab, edit the disk size,
  save the new configuration, and deploy it.
- Upsizing will be done on the next restart of the PostgreSQL or Redis
  container. You can force it by deleting the pod. This will cause a small
  interruption in the application.

#### Rook version >= 1.4.3

Follow these steps:

- Set the `allowVolumeExpansion` flag to true with `kubectl patch storageclass default -p '{"allowVolumeExpansion": true}'`
- Go to the KOTS Admin Console, select the "Config" tab, edit the disk size,
  save the new configuration, and deploy it.
- Upsizing will be done on the next restart of the PostgreSQL or Redis
  container. You can force it by deleting the pod. This will cause a small
  interruption in the application.

#### Rook version 1.0.4

This version of Rook Ceph does not handle volume expansion through Kubernetes.
It's also not easily upgradeable. You can follow the procedure below to increase
the size of your PostgreSQL or Redis disk. If you wish to upgrade from rook
1.0.4 to rook >= 1.4.3, you will need to do a backup/restore of your instance.
To do this, follow
[this procedure](../../management/infrastructure-management/backup).

**Before continuing, please make sure you have functional backups. Documentation
is available [here](../../management/infrastructure-management/backup)**

First, make sure the package `e2fsprogs` is installed on your instance.

To upsize the disk for PostgreSQL, run these commands. You can change the disk
size (50G here), by using the same value in the first two commands.

```bash
kubectl -n rook-ceph exec $(kubectl -n rook-ceph get pod -l app=rook-ceph-operator -o name | head -n1) -- rbd -p replicapool resize $(kubectl -n default get pvc -o custom-columns=NAME:.metadata.name,VOLUME:.spec.volumeName | grep postgresql-data | awk '{print $2}') --size 50G
kubectl -n rook-ceph exec $(kubectl -n rook-ceph get pod -l app=rook-ceph-operator -o name | head -n1) -- rbd -p replicapool resize $(kubectl -n default get pvc -o custom-columns=NAME:.metadata.name,VOLUME:.spec.volumeName | grep postgresql-backup | awk '{print $2}') --size 50G

sudo resize2fs /dev/$(lsblk | grep $(kubectl -n default get pvc -o custom-columns=NAME:.metadata.name,VOLUME:.spec.volumeName | grep postgresql-data | awk '{print $2}') | awk '{print $1}')
sudo resize2fs /dev/$(lsblk | grep $(kubectl -n default get pvc -o custom-columns=NAME:.metadata.name,VOLUME:.spec.volumeName | grep postgresql-backup | awk '{print $2}') | awk '{print $1}')
```

To upsize the disk for Redis, run these commands. You can change the disk size (20G here).

```bash Inline
kubectl -n rook-ceph exec $(kubectl -n rook-ceph get pod -l app=rook-ceph-operator -o name | head -n1) -- rbd -p replicapool resize $(kubectl -n default get pvc -o custom-columns=NAME:.metadata.name,VOLUME:.spec.volumeName | grep redis-data | awk '{print $2}') --size 20G

sudo resize2fs /dev/$(lsblk | grep $(kubectl -n default get pvc -o custom-columns=NAME:.metadata.name,VOLUME:.spec.volumeName | grep redis-data | awk '{print $2}') | awk '{print $1}')
```

Resizing is done live, you do not need to restart the container.

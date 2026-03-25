# Source: https://docs.logrocket.com/docs/recovering-from-read-only-mode.md

# Recovering from Read-Only Mode

Sometimes- such as an accidental downgrade in Logrocket versions, a failed upgrade, or instances where one of the Clickhouse shard replica pods may have crashed- your Clickhouse will automatically go into read-only mode, preventing any data from being written. If you are on Logrocket `22.107.0` or above, is a script in the toolbox which should fix this:

<Callout icon="🚧" theme="warn">
  You must be on Logrocket `22.107.0` for the script to be in the toolbox. If you are not on that version or later, you must edit the toolbox deployment's image so the pod that is created has the script. To do this, run the following:

  `kubectl edit deployment/toolbox`

  Find the `image:` tag. After the URL, there will be a `:` followed by your Logrocket version. Replace that version with `22.107.0` and save the changes before proceeding.
</Callout>

```shell
# Spin up the toolbox
kubectl scale deployment/toolbox --replicas 1

# Once the toolbox pod is running, run the script

kubectl exec -it deployment/toolbox -- ./ch-restore-replica.sh
```

This should restore Clickhouse to a functional state. If this works for you, you do not need to follow the instructions below.

# Recovering from Keeper communication issues

<Callout icon="❗️" theme="error">
  Only run these steps if the `ch-restore-replica.sh` script results in a `Session expired. (KEEPER_EXCEPTION)` error.
</Callout>

If, when running the above steps, you encounter a `Session expired. (KEEPER_EXCEPTION)` error, it will be necessary to restart some of the pods in a particular order.

Firstly, scale the `analytics-worker` deployment down to 0 to prevent it from attempting to write data into Clickhouse:

```shell
kubectl scale deployment/analytics-worker --replicas 0
```

Next, scale the shard replicas down to 0:

```shell
kubectl scale statefulset/logrocket-clickhouse-shard0 --replicas 0
```

Once that's done, restart keeper:

```shell
kubectl rollout restart statefulset/logrocket-clickhouse-keeper
```

You can use this command to monitor the status of the restart:

```shell
kubectl rollout status statefulset/logrocket-clickhouse-keeper
```

Once the restart of Keeper is complete, bring the shards back up:

```shell
kubectl scale statefulset/logrocket-clickhouse-shard0 --replicas 2
```

You can monitor the status of that scale-up with this command:

```shell
kubectl rollout status statefulset/logrocket-clickhouse-shard0
```

Once that's done and everything is back up and running, re-run the `ch-restore-replica.sh` script, and Clickhouse should be restored to working order. Once that's done, scale `analytics-worker` back up to start writing into Clickhouse again:

```shell
kubectl scale deployment/analytics-worker --replicas 1
```
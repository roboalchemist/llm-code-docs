# Source: https://planetscale.com/docs/vitess/sharding/sharding-new-tables.md

# Sharding new tables

> This tutorial shows you how to create new tables in a sharded keyspace. If you have an existing table that you want to shard, follow the [Sharding quickstart](/docs/vitess/sharding/sharding-quickstart) instead.

<Warning>
  Misconfiguration can cause availability issues. We recommend thoroughly reading through the documentation in the [Sharding section](/docs/vitess/sharding) of the docs prior to making any changes. If you have any questions, please [reach out to our support team](https://docs/support.planetscale.com).
</Warning>

Before you begin, we recommend the following reading:

<Columns cols={2}>
  <Card title="What is a keyspace?" icon="key" horizontal href="/docs/vitess/sharding" />

  <Card title="Vindexes" icon="info" horizontal href="/docs/vitess/sharding/vindexes" />

  <Card title="Sharding quickstart" icon="rocket" horizontal href="/docs/vitess/sharding/sharding-quickstart" />

  <Card title="Avoiding cross-shard queries" icon="messages-question" horizontal href="/docs/vitess/sharding/avoiding-cross-shard-queries" />

  <Card title="Sequence tables" icon="table" horizontal href="/docs/vitess/sharding/sequence-tables" />
</Columns>

<Info>
  Sharded keyspaces are not supported on databases with foreign key constraints enabled.
</Info>

When adding a new table to your database cluster, you have the option to shard it from the start. This can be a good option if you expect the table to grow incredibly quickly, or if you already have some other sharded tables that you know you will frequently join with this new table and want to avoid cross-shard queries.

Before you get started, you need a sharded keyspace. If you already have one, you can skip the next section.

## 1. Add a sharded keyspace

<Warning>
  If you are using [Vitess global routing](https://vitess.io/docs/api/reference/features/global-routing/), you must take extra care when adding a sharded keyspace to your database (for example, if you are using `@primary`).
  Before creating one, you must ensure that all tables from your first *unsharded keyspace* are added to the `VSchema` of that *unsharded keyspace*. Eg:

  ```
  {
    "tables": {
      "users": { }
      ...
    }
  }
  ```

  Otherwise, queries will fail. [Learn more about VSchema.](/docs/vitess/sharding/vschema)
</Warning>

Navigate to the [Clusters page](/docs/vitess/cluster-configuration).

<Steps>
  <Step>
    Click "New keyspace".
  </Step>

  <Step>
    Enter the keyspace name. For example, if your existing unsharded keyspace is named `metal`, you may create a sharded keyspace named `metal-sharded`.
  </Step>

  <Step>
    Select the number of shards you want to create in this keyspace.

    <Note>
      The cost of adding this additional keyspace largely depends on the number of shards you choose, the cluster size, and if you'd like to add additional replicas.
    </Note>
  </Step>

  <Step>
    Choose the cluster sizes you would like to use for this keyspace. Keep in mind, if you are creating a sharded keyspace, this will spin up multiple clusters of the selected size. For example, if you are creating 4 shards and choose the `PS-80` cluster size, we will create 4 `PS-80`s, each with 1 primary and 2 replicas.
  </Step>

  <Step>
    Select the number of *additional* replicas, if any, that you'd like to add to each cluster. Each cluster comes with 2 replicas by default, so any number you choose will be in addition to those 2.
  </Step>

  <Step>
    Review the new monthly cost for this keyspace below. This is in addition to your existing unsharded keyspace, as well as any other keyspaces you add.
  </Step>

  <Step>
    Once satisfied, click "Create keyspace".
  </Step>
</Steps>

## 2. Copy the sharded tables to the new keyspace and remove `AUTO_INCREMENT`

Let's say we're creating a new sharded table called `exercise_logs` that looks like this:

```sql  theme={null}
CREATE TABLE exercise_logs (
  id BIGINT UNSIGNED AUTO_INCREMENT,
  user_id BIGINT UNSIGNED,
  exercise_id BIGINT UNSIGNED,
  created_at DATETIME,
  reps SMALLINT UNSIGNED,
  sets SMALLINT UNSIGNED,
  weight SMALLINT UNSIGNED,
  notes VARCHAR(1024),
  PRIMARY KEY(id)
);
```

When a table is spread across multiple shards, using `AUTO_INCREMENT` on your primary key can cause problems. Because each shard is its own separate MySQL instance, the shards do not have the context to know whether or not a primary key for a table entry is already in use on other shards. This means you risk two different table entries being assigned the same primary key.

To avoid this, it is a best practice to use [sequence tables](/docs/vitess/sharding/sequence-tables) instead. We will cover how to set these up shortly. First, make sure you remove any `AUTO_INCREMENT`s from the tables you're sharding.

Switch to the new keyspace, and create the table there with no `AUTO_INCREMENT`:

```sql  theme={null}
use `metal-sharded`;

CREATE TABLE exercise_logs (
  id BIGINT UNSIGNED,
  user_id BIGINT UNSIGNED,
  exercise_id BIGINT UNSIGNED,
  created_at DATETIME,
  reps SMALLINT UNSIGNED,
  sets SMALLINT UNSIGNED,
  weight SMALLINT UNSIGNED,
  notes VARCHAR(1024),
  PRIMARY KEY(id)
);
```

## Add sequence tables to unsharded keyspace

As mentioned earlier, you should use [sequence tables](/docs/vitess/sharding/sequence-tables) in place of `AUTO_INCREMENT` for your sharded tables.

Your sequence tables will live in the source unsharded keyspace.

<Steps>
  <Step>
    Switch back to your original unsharded keyspace.

    ```sql  theme={null}
    use `metal`;
    ```
  </Step>

  <Step>
    Create the new sequence table for `exercise_logs`. If you're adding multiple new tables, create a sequence table for each:

    ```sql  theme={null}
    CREATE TABLE `exercise_logs_seq` ( `id` bigint, `user_id` bigint, `exercise_id` bigint, `created_at` datetime, `reps` smallint unsigned, `sets` smallint unsigned, `weight` smallint unsigned, notes varchar(1024), PRIMARY KEY (`id`) ) COMMENT='vitess_sequence';
    ```
  </Step>
</Steps>

Note `COMMENT='vitess_sequence'` at the end. This must be added for every sequence table you create.

## Add the sequence tables to the VSchema

The following will add the sequence tables to the source keyspace VSchema (`metal`):

```sql  theme={null}
alter vschema add sequence `metal`.exercise_logs_seq;
```

Next, add the following to specify that those sequence tables should be used as the sequence tables for the sharded tables in the new target keyspace VSchema (`metal-sharded`):

```sql  theme={null}
alter vschema on metal-sharded.exercise_logs add auto_increment id using `metal`.exercise_logs_seq;
```

The resulting VSchema for `metal` will look like this:

```json  theme={null}
{
  "tables": {
    "exercise_logs_seq": {
      "type": "sequence"
    }
  }
}
```

## 6. Add the tables to the source keyspace VSchema (`metal`)

You now need to add all tables to your source keyspace (`metal` for this example) VSchema. The VSchema is used to route queries to the proper keyspace. When you only had one keyspace, you didn't need to worry about this. But now that you've added a new sharded keyspace, Vitess will need to check the VSchema of each keyspace to route queries.

For more infomation, see the [VSchema documentation](/docs/vitess/sharding/vschema).

For this step, it's often easier to do from the UI instead of with an `ALTER` statement.

<Steps>
  <Step>
    On the Clusters page, click on your source unsharded keyspace (`metal`).
  </Step>

  <Step>
    Select the branch you created in the previous step.
  </Step>

  <Step>
    Click "VSchema".
  </Step>

  <Step>
    Add in **all tables** that exist in this keyspace. This is what our `metal` keyspace looks like:

    ```json  theme={null}
    {
      "tables": {
        "exercises": {},
        "exercise_log": {},
        "programs": {},
        "users": {}
      }
    }
    ```
  </Step>

  <Step>
    Click "Save changes"
  </Step>
</Steps>

## 7. Targeting the correct keyspace

Once you have more than one keyspace, with tables distributed across both keyspaces, your application may not know how to properly route queries to the correct keyspace.

If you originally set up your application configuration code with something like `DATABASE_NAME=your_database_name`, where `your_database_name` is the name of your original unsharded keyspace, you will need to update your configuration code so that all queries don't go straight to that keyspace.

The preferred way to do this is to just leave off the database name completely in your application configuration code. PlanetScale will be able to route traffic correctly just using the connection username and password.

While this is the preferred way, it's sometimes not possible. For example, many frameworks and ORMs require that you include a database name.

In those cases, you should use `@primary`. This will send any incoming queries first to our [Global Edge Network](https://planetscale.com/blog/introducing-global-replica-credentials#building-planetscale-global-network), which will see that you're targeting a primary. Edge will then send the request to the VTGate(s)/load balancer. We typically will use [Vitess's Global Routing](https://vitess.io/docs/api/reference/features/global-routing/) to direct the query to the correct keyspace and, optionally, correct shard.

<Note>
  If you explicitly wish to target a replica for some or all reads, using `@replica` will have the same effect as `@primary` in that it will automatically route the request to the correct keyspace.
</Note>

[Global Replica Credentials](/docs/vitess/scaling/replicas#1-create-a-global-replica-credential-recommended) are not currently supported in this context. You can still target replicas instead of your primary with `@replica`, but it will not automatically route the query to the *closest* replica.

For more information, refer to the [Targeting the correct keyspace documentation](/docs/vitess/sharding/targeting-correct-keyspace).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
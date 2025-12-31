# Source: https://planetscale.com/docs/vitess/sharding/pre-sharding-checklist.md

# Pre-sharding checklist

> When you begin a new [unsharded to sharded workflow](/docs/vitess/sharding/sharding-quickstart), there are a number of steps that happen behind the scenes. This document covers some of the pre-sharding work that PlanetScale handles for you.

<Note>
  If you started a workflow while following the [Sharding quickstart](/docs/vitess/sharding/sharding-quickstart) and saw a lot of incomplete steps in the validation phase, you need follow the instructions in this document, and then go back to the quickstart to continue the workflow.

  If you did not get those warnings, you're on a newer Vitess branch, and you do not need to take any action here.
</Note>

## Copy the sharded tables to the new keyspace and remove `AUTO_INCREMENT`

When you begin the workflow, we first copy the schema(s) of the table(s) you wish to shard over to the specified target keyspace. However, there is an intermediate step here: remove any existing `AUTO_INCREMENT`s on the primary key for these table(s).

When a table is spread across multiple shards, using `AUTO_INCREMENT` on your primary key can cause problems. Because each shard is its own separate MySQL instance, the shards do not have the context to know whether or not a primary key for a table entry is already in use on other shards. This means you risk two different table entries being assigned the same primary key.

To avoid this, it is a best practice to use [sequence tables](/docs/vitess/sharding/sequence-tables) instead. We will cover how to set these up shortly. First, let's remove `AUTO_INCREMENT` from the tables you're sharding:

1. Make a copy of the table schema(s) that are moving to this new keyspace. Leave off `AUTO_INCREMENT` if it previously existed. For this example, we'll create the `users` and `notifications` tables that will live on that keyspace.

<Note>
  Besides dropping `AUTO_INCREMENT`, the table schema must match exactly what you have on your original source keyspace. To quickly grab the SQL to create the table, you can go to your "Branches" tab in the dashboard, click your main branch, click the table you need to copy over, and copy the `CREATE TABLE` SQL. Again, make sure to remove `AUTO_INCREMENT`.
</Note>

```sql  theme={null}
CREATE TABLE `users` ( `id` bigint NOT NULL, `name` varchar(255) NOT NULL, `email` varchar(255) NOT NULL, `password` varchar(255) NOT NULL, PRIMARY KEY (`id`), UNIQUE KEY `index_users_on_email` (`email`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `notifications` ( `id` bigint NOT NULL, `content` varchar(255) NOT NULL, `user_id` bigint NOT NULL, `created_at` datetime(6) NOT NULL, `updated_at` datetime(6) NOT NULL, PRIMARY KEY (`id`), KEY `index_notifications_on_user_id` (`user_id`), KEY `index_notifications_on_user_id_and_created_at` (`user_id`,`created_at`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
    Create 2 new sequence tables: one for `notifications` and one for `users`.

    ```sql  theme={null}
    CREATE TABLE `notifications_seq` ( `id` bigint NOT NULL, `next_id` bigint DEFAULT NULL, `cache` bigint DEFAULT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='vitess_sequence';

    CREATE TABLE `users_seq` ( `id` bigint NOT NULL, `next_id` bigint DEFAULT NULL, `cache` bigint DEFAULT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='vitess_sequence';
    ```
  </Step>
</Steps>

## Add the sequence tables to the VSchema

The following will add the sequence tables to the source keyspace VSchema (`metal`):

```sql  theme={null}
alter vschema add sequence `metal`.notifications_seq;
alter vschema add sequence `metal`.users_seq;
```

Next, add the following to specify that those sequence tables should be used as the sequence tables for the sharded tables in the new target keyspace VSchema (`metal-sharded`):

```sql  theme={null}
alter vschema on metal-sharded.notifications add auto_increment id using `metal`.notifications_seq;
alter vschema on metal-sharded.users add auto_increment id using `metal`.users_seq;
```

The resulting VSchema for `metal` will look like this:

```json  theme={null}
{
  "tables": {
    "notifications_seq": {
      "type": "sequence"
    },
    "users_seq": {
      "type": "sequence"
    }
  }
}
```

## Add the tables to the source keyspace VSchema (`metal`)

<Note>
  If you are using Vitess global routing you may have already completed this.
  If so, you can skip this step.
</Note>

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

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
# Source: https://upstash.com/docs/redis/sdks/ts/commands/transaction.md

# Transactions

> Transactions

You can use transactions or pipelines with the `multi` or `pipeline` method.

Transactions are executed atomically, while pipelines are not. In pipelines you can execute multiple commands at once, but other commands from other clients can be executed in between.

<CodeGroup>
  ```ts Pipeline theme={"system"}
  const p = redis.pipeline();
  p.set("foo", "bar");
  p.get("foo");
  const res = await p.exec();
  ```

  ```ts Transaction theme={"system"}
  const tx = redis.multi();
  tx.set("foo", "bar");
  tx.get("foo");
  const res = await tx.exec();
  ```
</CodeGroup>

For more information on pipelines and transactions, see
[the Pipeline page](https://docs.upstash.com/redis/sdks/ts/pipelining/pipeline-transaction).

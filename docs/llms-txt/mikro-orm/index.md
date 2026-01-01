# Source: https://mikro-orm.io/index.md

![\[object Object\]](/img/icons/lock-icon.svg)

### Implicit Transactions

MikroORM allows handling [transactions](https://mikro-orm.io/docs/transactions.md) automatically. When you call `em.flush()`, all [computed changes](https://mikro-orm.io/docs/unit-of-work.md#how-mikroorm-detects-changes) are wrapped inside a database transaction.

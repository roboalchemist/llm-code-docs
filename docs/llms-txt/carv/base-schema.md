# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/base-schema.md

# Base Schema

### Blocks

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS sonarx_base.blocks (
  block_number DECIMAL(38, 0),
  timestamp DECIMAL(38, 0),
  datetime TIMESTAMP,
  block_hash STRING,
  block_parent_hash STRING,
  nonce DECIMAL(38, 0),
  sha3_uncles STRING,
  logs_bloom STRING,
  transactions_root STRING,
  state_root STRING,
  receipts_root STRING,
  miner STRING,
  mix_hash STRING,
  extra_data STRING,
  difficulty DECIMAL(38, 0),
  total_difficulty DECIMAL(38, 0),
  size DECIMAL(38, 0),
  gas_limit DECIMAL(38, 0),
  gas_used DECIMAL(38, 0),
  transaction_count DECIMAL(38, 0),
  base_fee_per_gas DECIMAL(38, 0),
  blob_gas_used DECIMAL(38, 0),
  excess_blob_gas DECIMAL(38, 0),
  parent_beacon_block_root STRING,
  withdrawals_root STRING,
  withdrawal_count DECIMAL(38, 0),
  date_created TIMESTAMP,
  date_updated TIMESTAMP)
PARTITIONED BY (
  `date` STRING)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://aws-public-blockchain/v1.1/sonarx/base/blocks'
TBLPROPERTIES (
);
```

### Transactions

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS sonarx_base.`transactions` (
  block_number DECIMAL(38, 0),
  datetime TIMESTAMP,
  `timestamp` DECIMAL(38, 0),
  transaction_hash STRING,
  transaction_index DECIMAL(38, 0),
  nonce DECIMAL(38, 0),
  block_hash STRING,
  from_address STRING,
  to_address STRING,
  value DOUBLE,
  transaction_fee DOUBLE,
  gas_price DOUBLE,
  gas_price_gwei DOUBLE,
  effective_gas_price DOUBLE,
  effective_gas_price_gwei DOUBLE,
  max_fee_per_gas DOUBLE,
  max_fee_per_gas_gwei DOUBLE,
  max_priority_fee_per_gas DOUBLE,
  max_priority_fee_per_gas_gwei DOUBLE,
  gas_limit DECIMAL(38, 0),
  gas_used DECIMAL(38, 0),
  gas_used_pct DECIMAL(38, 6),
  cumulative_gas_used DECIMAL(38, 0),
  input STRING,
  transaction_type DECIMAL(38, 0),
  contract_address STRING,
  status DECIMAL(38, 0),
  source_value DOUBLE,
  deposit_receipt_version DECIMAL(38, 0),
  mint DECIMAL(38, 0),
  source_hash STRING,
  y_parity DECIMAL(38, 0),
  l1_gas_price DOUBLE,
  l1_gas_price_gwei DOUBLE,
  l1_gas_used DECIMAL(38, 0),
  l1_fee_scalar DOUBLE,
  l1_fee DOUBLE,
  l2_fee DOUBLE,
  deposit_nonce DECIMAL(38, 0),
  date_created TIMESTAMP,
  date_updated TIMESTAMP)
PARTITIONED BY (
  `date` STRING)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://aws-public-blockchain/v1.1/sonarx/base/transactions'
TBLPROPERTIES (
);
```

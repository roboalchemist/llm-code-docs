# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/ethereum-schema.md

# Ethereum Schema

### Blocks

```sql
CREATE EXTERNAL TABLE `eth.blocks`(
  `timestamp` timestamp, 
  `number` bigint, 
  `hash` string, 
  `parent_hash` string, 
  `nonce` string, 
  `sha3_uncles` string, 
  `logs_bloom` string, 
  `transactions_root` string, 
  `state_root` string, 
  `receipts_root` string, 
  `miner` string, 
  `difficulty` double, 
  `total_difficulty` double, 
  `size` bigint, 
  `extra_data` string, 
  `gas_limit` bigint, 
  `gas_used` bigint, 
  `transaction_count` bigint, 
  `base_fee_per_gas` bigint)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/eth/blocks'
TBLPROPERTIES (
)
```

### Transactions

```sql
CREATE EXTERNAL TABLE `eth.transactions`(
  `hash` string, 
  `nonce` bigint, 
  `transaction_index` bigint, 
  `from_address` string, 
  `to_address` string, 
  `value` double, 
  `gas` bigint, 
  `gas_price` bigint, 
  `input` string, 
  `receipt_cumulative_gas_used` bigint, 
  `receipt_gas_used` bigint, 
  `receipt_contract_address` string, 
  `receipt_root` string, 
  `receipt_status` bigint, 
  `block_timestamp` timestamp, 
  `block_number` bigint, 
  `block_hash` string, 
  `max_fee_per_gas` bigint, 
  `max_priority_fee_per_gas` bigint, 
  `transaction_type` bigint, 
  `receipt_effective_gas_price` bigint)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/eth/transactions'
TBLPROPERTIES (
)
```

### Contracts

```sql
CREATE EXTERNAL TABLE `eth.contracts`(
  `address` string, 
  `bytecode` string, 
  `block_timestamp` timestamp, 
  `block_number` bigint, 
  `block_hash` string)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/eth/contracts'
TBLPROPERTIES (
)
```

### Logs

```sql
CREATE EXTERNAL TABLE `eth.logs`(
  `log_index` bigint, 
  `transaction_hash` string, 
  `transaction_index` bigint, 
  `address` string, 
  `data` string, 
  `topics` array<string>, 
  `block_timestamp` timestamp, 
  `block_number` bigint, 
  `block_hash` string)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/eth/logs'
TBLPROPERTIES (
)
```

### Token\_transfers

```sql
CREATE EXTERNAL TABLE `eth.token_transfers`(
  `token_address` string, 
  `from_address` string, 
  `to_address` string, 
  `value` double, 
  `transaction_hash` string, 
  `log_index` bigint, 
  `block_timestamp` timestamp, 
  `block_number` bigint, 
  `block_hash` string)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/eth/token_transfers'
TBLPROPERTIES (
)
```

### Traces

```sql
CREATE EXTERNAL TABLE `eth.traces`(
  `transaction_hash` string, 
  `transaction_index` bigint, 
  `from_address` string, 
  `to_address` string, 
  `value` double, 
  `input` string, 
  `output` string, 
  `trace_type` string, 
  `call_type` string, 
  `reward_type` string, 
  `gas` double, 
  `gas_used` double, 
  `subtraces` bigint, 
  `trace_address` string, 
  `error` string, 
  `status` bigint, 
  `block_timestamp` timestamp, 
  `block_number` bigint, 
  `block_hash` string, 
  `trace_id` string)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/eth/traces'
TBLPROPERTIES (
)
```

# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/bitcoin-schema.md

# Bitcoin Schema

### Blocks

```sql
CREATE EXTERNAL TABLE `btc.blocks`(
  `hash` string, 
  `size` bigint, 
  `stripped_size` bigint, 
  `weight` bigint, 
  `number` bigint, 
  `version` bigint, 
  `merkle_root` string, 
  `timestamp` timestamp, 
  `nonce` bigint, 
  `bits` string, 
  `coinbase_param` string, 
  `transaction_count` bigint, 
  `mediantime` timestamp, 
  `difficulty` double, 
  `chainwork` string, 
  `previousblockhash` string)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/btc/blocks'
TBLPROPERTIES (
) 
```

### Transactions

```sql
CREATE EXTERNAL TABLE `transactions`(
  `hash` string, 
  `size` bigint, 
  `virtual_size` bigint, 
  `version` bigint, 
  `lock_time` bigint, 
  `block_hash` string, 
  `block_number` bigint, 
  `block_timestamp` timestamp, 
  `index` bigint, 
  `input_count` bigint, 
  `output_count` bigint, 
  `input_value` double, 
  `output_value` double, 
  `is_coinbase` boolean, 
  `fee` double, 
  `inputs` array<struct<index:bigint,spent_transaction_hash:string,spent_output_index:bigint,script_asm:string,script_hex:string,sequence:bigint,required_signatures:bigint,type:string,address:string,value:double>>, 
  `outputs` array<struct<index:bigint,script_asm:string,script_hex:string,required_signatures:bigint,type:string,address:string,value:double>>)
PARTITIONED BY ( 
  `date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://aws-public-blockchain/v1.0/btc/transactions'
TBLPROPERTIES (
)
```

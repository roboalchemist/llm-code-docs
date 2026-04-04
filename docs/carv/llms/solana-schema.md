# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/solana-schema.md

# Solana Schema

### Blocks

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS solana.blocks(
    slot bigint,
    block_hash string,
    block_timestamp timestamp,
    height bigint,
    previous_block_hash string,
    transaction_count bigint,
    leader_reward DECIMAL(38, 0),
    leader string
)
PARTITIONED BY (
  `date` STRING)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://carv-dev-blockchain/solana/v1.0/blocks'
TBLPROPERTIES (
);
```

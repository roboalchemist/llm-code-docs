# Source: https://posthog.com/docs/how-posthog-works/recordings-ingestion.md

# Session replay ingestion - Docs

## Overview

We use `rrweb` to collect "snapshot data" from the browser. This data is gathered by the capture API and sent to ingestion.

Because we use Kafka for ingestion, there is a maximum allowed message size and snapshot data is often larger than that. Replay has its own ingestion infrastructure with larger limits.

We store recording snapshot data in blob storage and aggregated session information in the `session_replay_events` table. As a result in capture (`posthog-recordings` deployment), we no longer need to chunk recordings.

The ingestion workload batches sessions to disk and periodically flushes them to blob storage. This is to enable us to write fewer files to storage reducing the operational cost of the system.

## Recording metadata

The ingestion workload generates metadata and stores it in the `session_replay_events` table in ClickHouse. This is used to power the session replay UI. It uses the [ClickHouse Aggregating MergeTree engine](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/aggregatingmergetree) to power the table.

In combination with the blob storage ingestion workload, this means we're storing at least a hundred times less data per row in ClickHouse than in the original infrastructure. And compressing it about twice as much. 🔥

flowchart TB clickhouse\_replay\_summary\_table\[(Session replay summary table)\] received\_snapshot\_event\[clients send snapshot data\] kafka\_recordings\_topic>Kafka recordings topic\] kafka\_clickhouse\_replay\_summary\_topic>Kafka clickhouse replay summary topic\] subgraph recordings blob ingestion workload recordings\_blob\_consumer-->|1. statefully batch|disk disk-->recordings\_blob\_consumer recordings\_blob\_consumer-->|2. periodic flush|blob\_storage recordings\_blob\_consumer-->|3. after flush|kafka\_clickhouse\_replay\_summary\_topic kafka\_clickhouse\_replay\_summary\_topic-->clickhouse\_replay\_summary\_table end received\_snapshot\_event --> capture capture -->|compress into kafka messages| kafka\_recordings\_topic kafka\_recordings\_topic --> recordings\_blob\_consumer

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better
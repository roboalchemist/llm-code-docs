faktory
# Struct DataSnapshot 
Source 

```
#[non_exhaustive]pub struct DataSnapshot {
    pub total_failures: u64,
    pub total_processed: u64,
    pub total_enqueued: u64,
    pub total_queues: u64,
    pub queues: BTreeMap<String, u64>,
    pub tasks: Value,
}
```

## Fields (Non-exhaustive)§
§`total_failures: u64`

Total number of job failures.
§`total_processed: u64`

Total number of processed jobs.
§`total_enqueued: u64`

Total number of enqueued jobs.
§`total_queues: u64`

Total number of queues.
§`queues: BTreeMap<String, u64>`

Queues stats.

A mapping between a queue name and its size (number of jobs on the queue).
The keys of this map effectively make up a list of queues that are currently
registered in the Faktory service.
§`tasks: Value`👎Deprecated: marked as deprecated in the Faktory source code and is likely to be completely removed in the future, so please do not rely on this data

***Deprecated***. Faktory’s task runner stats.

Note that this is exposed as a “generic” `serde_json::Value` since this info
belongs to deep implementation details of the Faktory service.

## Trait Implementations§
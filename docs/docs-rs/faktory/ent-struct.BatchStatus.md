faktory::ent
# Struct BatchStatus 
Source 

```
pub struct BatchStatus {
    pub bid: BatchId,
    pub created_at: DateTime<Utc>,
    pub description: Option<String>,
    pub total: usize,
    pub pending: usize,
    pub failed: usize,
    pub parent_bid: Option<BatchId>,
    pub complete_callback_state: CallbackState,
    pub success_callback_state: CallbackState,
}
```
Available on **crate feature `ent`** only.
## Fields§
§`bid: BatchId`

Id of this batch.
§`created_at: DateTime<Utc>`

Batch creation date and time.
§`description: Option<String>`

Batch description, if any.
§`total: usize`

Number of jobs in this batch.
§`pending: usize`

Number of pending jobs.
§`failed: usize`

Number of failed jobs.
§`parent_bid: Option<BatchId>`

Id of the parent batch, provided this batch is a child (“nested”) batch.
§`complete_callback_state: CallbackState`

State of the `complete` callback.

See with_complete_callback.
§`success_callback_state: CallbackState`

State of the `success` callback.

See with_success_callback.

## Implementations§
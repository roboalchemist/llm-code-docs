faktory
# Struct Job 
Source 

```
pub struct Job {
    pub queue: String,
    pub kind: String,
    pub created_at: Option<DateTime<Utc>>,
    pub enqueued_at: Option<DateTime<Utc>>,
    pub at: Option<DateTime<Utc>>,
    pub reserve_for: Option<Duration>,
    pub retry: Option<isize>,
    pub priority: Option<u8>,
    pub backtrace: Option<usize>,
    pub custom: HashMap<String, Value>,
    /* private fields */
}
```

## Fields§
§`queue: String`

The queue this job belongs to. Usually `default`.
§`kind: String`

The job’s type. Called `kind` because `type` is reserved.
§`created_at: Option<DateTime<Utc>>`

When this job was created.
§`enqueued_at: Option<DateTime<Utc>>`

When this job was supplied to the Faktory server.
§`at: Option<DateTime<Utc>>`

When this job is scheduled for.

Defaults to immediately.
§`reserve_for: Option<Duration>`

How long to allow this job to run for.

Defaults to 600 seconds.
§`retry: Option<isize>`

Number of times to retry this job.

Defaults to 25.
§`priority: Option<u8>`

The priority of this job from 1-9 (9 is highest).

Pushing a job with priority 9 will effectively put it at the front of the queue.
Defaults to 5.
§`backtrace: Option<usize>`

Number of lines of backtrace to keep if this job fails.

Defaults to 0.
§`custom: HashMap<String, Value>`

Extra context to include with the job.

Faktory workers can have plugins and middleware which need to store additional context with
the job payload. Faktory supports a custom hash to store arbitrary key/values in the JSON.
This can be extremely helpful for cross-cutting concerns which should propagate between
systems, e.g. locale for user-specific text translations, request_id for tracing execution
across a complex distributed system, etc.

## Implementations§
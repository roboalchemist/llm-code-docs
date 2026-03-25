faktory
# Struct Failure 
Source 

```
#[non_exhaustive]pub struct Failure {
    pub retry_count: usize,
    pub retry_remaining: usize,
    pub failed_at: DateTime<Utc>,
    pub next_at: Option<DateTime<Utc>>,
    pub message: Option<String>,
    pub backtrace: Option<Vec<String>>,
    /* private fields */
}
```

## Fields (Non-exhaustive)§
§`retry_count: usize`

Number of times this job has been retried.
§`retry_remaining: usize`

Number of remaining retry attempts.

This is the difference between how many times this job
*can* be retried (see `Job::retry`) and the number of retry
attempts that have already been made (see `Failure::retry_count`).
§`failed_at: DateTime<Utc>`

Last time this job failed.
§`next_at: Option<DateTime<Utc>>`

When this job will be retried.

This will be `None` if there are no retry
attempts (see `Failure::retry_remaining`) left.
§`message: Option<String>`

Error message, if any.
§`backtrace: Option<Vec<String>>`

Stack trace from last failure, if any.

## Trait Implementations§
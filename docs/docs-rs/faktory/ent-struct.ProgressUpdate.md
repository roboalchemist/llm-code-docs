faktory::ent
# Struct ProgressUpdate 
Source 

```
pub struct ProgressUpdate {
    pub jid: JobId,
    pub percent: Option<u8>,
    pub desc: Option<String>,
    pub reserve_until: Option<DateTime<Utc>>,
}
```
Available on **crate feature `ent`** only.
## Fields§
§`jid: JobId`

Id of the tracked job.
§`percent: Option<u8>`

Percentage of the job’s completion.
§`desc: Option<String>`

Arbitrary description that may be useful to whoever is tracking the job’s progress.
§`reserve_until: Option<DateTime<Utc>>`

Allows to extend the job’s reservation, if more time is needed to execute it.

Note that you cannot shorten the initial reservation via
specifying an instant that is sooner than the job’s initial reservation deadline.

## Implementations§
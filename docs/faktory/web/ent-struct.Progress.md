faktory::ent
# Struct Progress 
Source 

```
pub struct Progress {
    pub jid: JobId,
    pub state: JobState,
    pub updated_at: Option<DateTime<Utc>>,
    pub percent: Option<u8>,
    pub desc: Option<String>,
}
```
Available on **crate feature `ent`** only.
## Fields§
§`jid: JobId`

Id of the tracked job.
§`state: JobState`

Job’s state.
§`updated_at: Option<DateTime<Utc>>`

When this job was last updated.
§`percent: Option<u8>`

Percentage of the job’s completion.
§`desc: Option<String>`

Arbitrary description that may be useful to whoever is tracking the job’s progress.

## Implementations§
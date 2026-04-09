faktory
# Struct FaktoryState 
Source 

```
pub struct FaktoryState {
    pub now: DateTime<Utc>,
    pub server_utc_time: NaiveTime,
    pub data: DataSnapshot,
    pub server: ServerSnapshot,
}
```

## Fields§
§`now: DateTime<Utc>`

Server time.
§`server_utc_time: NaiveTime`

Server time (naive representation).

Faktory sends it as a string formatted as “%H:%M:%S UTC” (e.g. “19:47:39 UTC”)
and it is being parsed as `NaiveTime`.

Most of the time, though, you will want to use `FaktoryState::now` instead.
§`data: DataSnapshot`

Faktory service information.
§`server: ServerSnapshot`

Faktory’s server process information.

## Trait Implementations§
supernova::models
# Struct GroupSchedulingPeriodic 
Source 

```
pub struct GroupSchedulingPeriodic {
    pub title: Option<String>,
    pub weekday: Weekday,
    pub time: NaiveTime,
    pub start_date: NaiveDate,
    pub end_date: NaiveDate,
    pub duration: u16,
    pub revoked: bool,
}
```

## Fields§
§`title: Option<String>`§`weekday: Weekday`§`time: NaiveTime`§`start_date: NaiveDate`§`end_date: NaiveDate`§`duration: u16`§`revoked: bool`
## Trait Implementations§
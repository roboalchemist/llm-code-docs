victorops::types
# Struct ApiTeamSchedule 
Source 

```
pub struct ApiTeamSchedule {
    pub team: Option<ApiTeam>,
    pub schedules: Vec<ApiEscalationPolicySchedule>,
}
```

## Fields§
§`team: Option<ApiTeam>`

The team this schedule belongs to.
§`schedules: Vec<ApiEscalationPolicySchedule>`

The escalation policy schedules for this team.

## Trait Implementations§
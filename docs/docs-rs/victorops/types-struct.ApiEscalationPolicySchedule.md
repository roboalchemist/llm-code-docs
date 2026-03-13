victorops::types
# Struct ApiEscalationPolicySchedule 
Source 

```
pub struct ApiEscalationPolicySchedule {
    pub policy: Option<ApiEscalationPolicy>,
    pub schedule: Vec<ApiOnCallEntry>,
    pub overrides: Vec<ApiOnCallOverride>,
}
```

## Fields§
§`policy: Option<ApiEscalationPolicy>`

The escalation policy this schedule belongs to.
§`schedule: Vec<ApiOnCallEntry>`

The schedule entries for this escalation policy.
§`overrides: Vec<ApiOnCallOverride>`

The on-call overrides for this escalation policy.

## Trait Implementations§
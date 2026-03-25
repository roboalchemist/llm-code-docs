victorops::types
# Struct EscalationPolicy 
Source 

```
pub struct EscalationPolicy {
    pub name: String,
    pub team_id: String,
    pub ignore_custom_paging_policies: bool,
    pub steps: Vec<EscalationPolicySteps>,
    pub id: String,
}
```

## Fields§
§`name: String`

The name of the escalation policy.
§`team_id: String`

The team slug/ID that this escalation policy belongs to.
§`ignore_custom_paging_policies: bool`

Whether to ignore custom paging policies.
§`steps: Vec<EscalationPolicySteps>`

The escalation steps for this policy.
§`id: String`

The unique slug/ID of the escalation policy.

## Trait Implementations§
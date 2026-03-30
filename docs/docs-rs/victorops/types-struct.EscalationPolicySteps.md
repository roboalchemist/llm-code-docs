victorops::types
# Struct EscalationPolicySteps 
Source 

```
pub struct EscalationPolicySteps {
    pub timeout: i32,
    pub entries: Vec<EscalationPolicyStepEntry>,
}
```

## Fields§
§`timeout: i32`

The timeout in seconds before escalating to the next step.
§`entries: Vec<EscalationPolicyStepEntry>`

The list of entries/targets for this escalation step.

## Trait Implementations§
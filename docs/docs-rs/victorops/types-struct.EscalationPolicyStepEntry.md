victorops::types
# Struct EscalationPolicyStepEntry 
Source 

```
pub struct EscalationPolicyStepEntry {
    pub execution_type: Option<String>,
    pub user: Option<HashMap<String, String>>,
    pub rotation_group: Option<HashMap<String, String>>,
    pub webhook: Option<HashMap<String, String>>,
    pub email: Option<HashMap<String, String>>,
    pub target_policy: Option<HashMap<String, String>>,
}
```

## Fields§
§`execution_type: Option<String>`

The type of execution for this escalation step.
§`user: Option<HashMap<String, String>>`

User information for user-based escalation targets.
§`rotation_group: Option<HashMap<String, String>>`

Rotation group information for rotation-based escalation targets.
§`webhook: Option<HashMap<String, String>>`

Webhook information for webhook-based escalation targets.
§`email: Option<HashMap<String, String>>`

Email information for email-based escalation targets.
§`target_policy: Option<HashMap<String, String>>`

Target policy information for policy-based escalation targets.

## Trait Implementations§
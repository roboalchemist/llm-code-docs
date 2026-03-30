victorops::types
# Struct Incident 
Source 

```
pub struct Incident {}
```

## Fields§
§`alert_count: Option<i32>`

The number of alerts in this incident.
§`current_phase: Option<String>`

The current phase or state of the incident.
§`entity_display_name: Option<String>`

The display name of the entity that triggered the incident.
§`entity_id: Option<String>`

The unique identifier of the entity that triggered the incident.
§`entity_state: Option<String>`

The state of the entity that triggered the incident.
§`entity_type: Option<String>`

The type of entity that triggered the incident.
§`host: Option<String>`

The host associated with the incident.
§`incident_number: Option<String>`

The incident number or identifier.
§`last_alert_id: Option<String>`

The ID of the last alert in this incident.
§`last_alert_time: Option<DateTime<Utc>>`

The timestamp of the last alert in this incident.
§`service: Option<String>`

The service associated with the incident.
§`start_time: Option<DateTime<Utc>>`

The timestamp when the incident started.
§`paged_teams: Vec<String>`

The list of teams that were paged for this incident.
§`paged_users: Vec<String>`

The list of users that were paged for this incident.
§`paged_policies: Vec<PagedPolicy>`

The list of escalation policies that were triggered for this incident.
§`transitions: Vec<Transition>`

The state transitions that occurred during this incident.

## Trait Implementations§
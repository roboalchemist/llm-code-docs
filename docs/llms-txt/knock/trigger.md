# Source: https://docs.knock.app/api-reference/workflows/trigger.md

### Trigger workflow

Trigger a workflow (specified by the key) to run for the given recipients, using the parameters provided. Returns an identifier for the workflow run request. All workflow runs are executed asynchronously. This endpoint also handles [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients) for the `actor`, `recipient`, and `tenant` fields.

#### Endpoint

`POST /v1/workflows/{key}/trigger`

**Rate limit tier:** 5

#### Path parameters

- **key** (string) *required* - Key of the workflow to trigger.

#### Request body

A request to trigger a notification workflow.

##### Example

```json
{
  "actor": "mr_dna",
  "cancellation_key": "isla_nublar_incident_1993",
  "data": {
    "affected_areas": [
      "visitor_center",
      "raptor_pen",
      "trex_paddock"
    ],
    "attraction_id": "paddock_rex_01",
    "evacuation_protocol": "active",
    "message": "Life finds a way",
    "severity": "critical",
    "system_status": "fences_failing"
  },
  "recipients": [
    "dr_grant",
    "dr_sattler",
    "dr_malcolm"
  ],
  "tenant": "ingen_isla_nublar"
}
```

#### Responses

##### 200

OK

###### Example

```json
{
  "workflow_run_id": "123e4567-e89b-12d3-a456-426614174000"
}
```


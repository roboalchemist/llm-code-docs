# Source: https://docs.api7.ai/enterprise/reference/approval-variables.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/approval-variables.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/approval-variables.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/approval-variables.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/approval-variables.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/approval-variables.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/approval-variables.md

# Approval Variables and Templates

Approval notifications (emails and messages) can be customized with pre-defined variables to provide dynamic content.

## Approval Variables[â](#approval-variables "Direct link to Approval Variables")

Approval variables are data evaluations in the template that are delimited by `{{` and `}}`.

The following variables are available to be used in creating alert notifications (message, email subject, email content).

| **Variable**          | **Description**                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------- |
| `{{ .ApprovalID}}`    | Unique ID of the approval.                                                                                    |
| `{{ .ApplicantName}}` | Name of applicant.                                                                                            |
| `{{ .Event}}`         | Can be `API Product Subscription`, or `Developer Sign Up`                                                     |
| `{{ .AppliedAt}}`     | Time of the submission                                                                                        |
| `{{ .ResourceName}}`  | Name of event related resource: API Product for `API Product Subscription`, Developer for `Developer Sign Up` |

* `AppliedAt` can customize [time format](https://go.dev/src/time/format.go)

```
{{ .AppliedAt.Format }}
```

## Templates[â](#templates "Direct link to Templates")

### Message (JSON)[â](#message-json "Direct link to Message (JSON)")

```
"applicant": "{{.ApplicantName}}"
"timestamp": "{{.AppliedAt.Format "2006 Jan 02 15:04:05"}}"
"id": "{{.ApprovalID}}"
"event": "{{.Event}}"
"resource": "{{.ResourceName}}"
```

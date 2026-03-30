# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/alert-template.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/alert-template.md

# Alert Variables and Templates

Alert policy notifications (emails and messages) can be customized with pre-defined variables to provide dynamic content.

## Alert Variables[â](#alert-variables "Direct link to Alert Variables")

Alert variables are data evaluations in the template that are delimited by `{{` and `}}`.

The following variables are available to be used in creating alert notifications(alert message, alert email subject, alert email content)

| **Variable**                 | **Description**                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `{{ .AlertPolicyName }}`     | Name of the alert policy.                                                                                   |
| `{{ .Description }}`         | Description of the alert policy.                                                                            |
| `{{ .Severity }}`            | Severity of the alert policy.                                                                               |
| `{{ .TriggerGatewayGroup }}` | The names of the gateway groups that trigger alerts. Multiple groups may be specified, separated by commas. |
| `{{ .AlertTime }}`           | Time of the alert.                                                                                          |
| `{{ .AlertDetail }}`         | Detailed description of the specific event(s) triggering the alert. Multiple events are listed separately.  |

* `AlertTime` can be formatted using a [custom time format](https://go.dev/src/time/format.go), such as:

```
{{ .AlertTime.Format "2024 Dec 31 17:00:00" }}
```

* The `AlertDetail` field is a string that can contain multiple event details, separated by newline characters (`\n`). To use this field in a JSON body, ensure proper escaping of newline characters.

```
{{ .AlertDetail | escape }}
```

## Templates[â](#templates "Direct link to Templates")

Examples to configure alert notifications.

### Alert Email Subject[â](#alert-email-subject "Direct link to Alert Email Subject")

```
`[API7 Alert] No Enough Healthy Gateway Instances in {{.TriggerGatewayGruop}} - [{{.Severity}}]`.
```

### Alert Email Content[â](#alert-email-content "Direct link to Alert Email Content")

```
Dear [Recipient Name],

We are writing to inform you that an alert has been triggered for the API7 Gateway at {{.AlertTime.Format "2006 Jan 02 15:04:05"}}. The specific alert severity is {{.Severity}}.

Alert Details:

Gateway Groups: {{.TriggerGatewayGroup}}
Alert Message: {{.AlertDetail}}
```

Recommended Actions:

Investigate further: Please go check the related logs and metrics for more details. Restart service: Consider restarting the service. Escalate to on-call team: If the issue persists, please contact the on-call team.

### Alert Message (JSON)[â](#alert-message-json "Direct link to Alert Message (JSON)")

```
"text": "{{.AlertDetail | escape}}".
"timestamp": "{{.AlertTime.Format "2006 Jan 02 15:04:05"}}"
"system": "API7 Gateway, {{.TriggerGatewayGroup}}"
```

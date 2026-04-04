# Source: https://docs.rootly.com/workflows/workflows.md

# Source: https://docs.rootly.com/integrations/zoom/workflows.md

# Source: https://docs.rootly.com/integrations/webex/workflows.md

# Source: https://docs.rootly.com/integrations/service-now/workflows.md

# Source: https://docs.rootly.com/integrations/pagerduty/workflows.md

# Source: https://docs.rootly.com/integrations/notion/workflows.md

# Source: https://docs.rootly.com/integrations/microsoft-teams/workflows.md

# Source: https://docs.rootly.com/integrations/linear/workflows.md

# Source: https://docs.rootly.com/integrations/google-meet/workflows.md

# Source: https://docs.rootly.com/integrations/google-docs/workflows.md

# Source: https://docs.rootly.com/integrations/google-calendar/workflows.md

# Source: https://docs.rootly.com/integrations/dropbox-paper/workflows.md

# Source: https://docs.rootly.com/integrations/confluence/workflows.md

# Source: https://docs.rootly.com/integrations/coda/workflows.md

# Source: https://docs.rootly.com/integrations/clickup/workflows.md

# Source: https://docs.rootly.com/integrations/asana/workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflows

> Configure Asana workflow actions to create tasks and manage project items from Rootly incidents.

## Create an Asana Task

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/yHcXrOapKHrppc-2/images/integrations/asana/workflows/workflows-1.webp?fit=max&auto=format&n=yHcXrOapKHrppc-2&q=85&s=41e73a18c6e064d1ca42943e6fd9e029" width="873" height="1123" data-path="images/integrations/asana/workflows/workflows-1.webp" />
</Frame>

## Create an Asana Subtask

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/yHcXrOapKHrppc-2/images/integrations/asana/workflows/workflows-2.webp?fit=max&auto=format&n=yHcXrOapKHrppc-2&q=85&s=9a9f4961dc9f8125ed22bbbce3c73cf3" width="869" height="1000" data-path="images/integrations/asana/workflows/workflows-2.webp" />
</Frame>

## Update an Asana Task

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/yHcXrOapKHrppc-2/images/integrations/asana/workflows/workflows-3.webp?fit=max&auto=format&n=yHcXrOapKHrppc-2&q=85&s=cf4dac8ed1a956cd077219041572de31" width="878" height="1009" data-path="images/integrations/asana/workflows/workflows-3.webp" />
</Frame>

## Custom fields

```JSON  theme={null}
"custom_fields": {
    "4578152156": "Not Started", // For textfield type
    "5678904321": "On Hold", // For textfield type
    "5678904322": "1004598149" // For single enum type
    "5678904322": ["459021796", "1004598149"] // For multi enum type
},

"custom_fields": {
    "4578152156": "{{ incident.severity }}", // For textfield type
    "5678904321": "{{ incident.status }}", // For textfield type
},

"custom_fields": {
    "4578152156": "{{ incident.severity }}", // For textfield type
    // For single enum type
    {% if incident.severity == "sev0" %}
        "5678904322": "1004598149" // Custom Field ID <=> Enum ID
    {% elsif incident.severity == "sev1" %}
        "5678904322": "1004598149" // Custom Field ID <=> Enum ID
    {% endif %}
},
```


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.datadoghq.com/getting_started/site.md

# Source: https://docs.datadoghq.com/agent/troubleshooting/site.md

---
title: Agent Site Issues
description: >-
  Configure the Datadog Agent to send data to the correct Datadog site by
  setting the site parameter or DD_SITE environment variable.
breadcrumbs: Docs > Agent > Agent Troubleshooting > Agent Site Issues
---

# Agent Site Issues

By default the Agent sends its data to Datadog US site: `app.datadoghq.com`. If your organization is on another site, you must update the `site` parameter in your [Agent main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) or set the `DD_SITE` environment variable.

To update the Datadog documentation to your site, use the selector on the right. You are currently viewing documentation for: .

Set the `DD_SITE` variable to or update the parameter `site` parameter in your `datadog.yaml`

```yaml
## @param site - string - optional - default: datadoghq.com
## The site of the Datadog intake to send Agent data to.
#
site: 
```

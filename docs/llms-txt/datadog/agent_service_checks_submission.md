# Source: https://docs.datadoghq.com/developers/service_checks/agent_service_checks_submission.md

---
title: 'Service Check Submission: Agent Check'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: 'Docs > Developers > Service Check > Service Check Submission: Agent Check'
---

# Service Check Submission: Agent Check

To submit a service check to Datadog within a custom Agent check, use the predefined `service_check()` function in the `AgentCheck` class.

```python
self.service_check(name, status, tags=None, hostname=None, message=None)
```

Find below the different parameters and data types available for the `service_check()` function:

| Parameter  | Type            | Required | Default Value | Description                                                                                                   |
| ---------- | --------------- | -------- | ------------- | ------------------------------------------------------------------------------------------------------------- |
| `name`     | string          | yes      | -             | The name of the service check.                                                                                |
| `status`   | int             | yes      | -             | A constant describing the service status: `0` for OK, `1` for Warning, `2` for Critical, and `3` for Unknown. |
| `tags`     | list of strings | no       | `None`        | A list of tags to associate with this Service Check.                                                          |
| `hostname` | string          | no       | current host  | A hostname to associate with this Service check. Defaults to the current host.                                |
| `message`  | string          | no       | `None`        | Additional information or a description of why this status occurred.                                          |

## Example{% #example %}

Here is an example of a dummy Agent check sending only one service check periodically. See [Writing a Custom Agent Check](https://docs.datadoghq.com/developers/custom_checks/write_agent_check/) to learn more.

1. Create a new directory, `service_check_example.d/`, in the [`conf.d/` folder](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-configuration-directory) of your Agent.

1. In your `service_check_example.d/` folder, create an empty configuration file named `service_check_example.yaml` with the following content:

   ```yaml
   instances: [{}]
   ```

1. Up one level from the `conf.d/` folder, go to the `checks.d/` folder.

1. Within this folder, create a custom check file named `service_check_example.py` with the content below:

In the `service_check_example.py` file:

   ```python
   from datadog_checks.base import AgentCheck
   
   __version__ = "1.0.0"
   
   class MyClass(AgentCheck):
       def check(self, instance):
           self.service_check('example_service_check', 0, message='Example application is up and running.')
       
```

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent)

1. Ensure that your custom check is correctly running with the [Agent status command](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-information). You should see something like this:

   ```text
   =========
   Collector
   =========
   
     Running Checks
     ==============
   
       (...)
   
       service_check_example (1.0.0)
       -----------------------------
         Instance ID: service_check_example:d884b5186b651429 [OK]
         Total Runs: 1
         Metric Samples: Last Run: 0, Total: 0
         Events: Last Run: 0, Total: 0
         Service Checks: Last Run: 1, Total: 1
         Average Execution Time : 2ms
   
       (...)
   ```

1. Finally, see your [Datadog service check summary](https://app.datadoghq.com/check/summary) to see your service check reporting:

{% image
   source="https://datadog-docs.imgix.net/images/developers/service_checks/agent_service_checks_submission/service_check.e17806e524fae496e4ebc543cf73763e.png?auto=format"
   alt="Service Checks" /%}

## Further reading{% #further-reading %}

- [Write an Agent Custom Check](https://docs.datadoghq.com/developers/custom_checks/write_agent_check/)

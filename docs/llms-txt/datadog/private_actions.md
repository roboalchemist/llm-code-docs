# Source: https://docs.datadoghq.com/actions/private_actions.md

---
title: Private Actions Overview
description: >-
  Allow workflows and apps to interact with private network services using
  Docker-based private action runners with secure authentication.
breadcrumbs: Docs > Private Actions Overview
source_url: https://docs.datadoghq.com/private_actions/index.html
---

# Private Actions Overview

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Private actions allow your Datadog workflows and apps to interact with services hosted on your private network without exposing them to the public internet. To use private actions, you must install a private action runner on a host in your network using Docker or [Kubernetes](https://github.com/DataDog/helm-charts/tree/main/charts/private-action-runner) and pair the runner with a [connection](https://docs.datadoghq.com/service_management/workflows/connections/).

{% alert level="danger" %}
To install a private action runner, your organization must have [Remote Configuration](https://docs.datadoghq.com/remote_configuration) enabled.
{% /alert %}

When you first start the runner, it generates a private key for authentication with Datadog's servers. This private key is never accessible by Datadog and ensures you exclusive access. Datadog uses a public key derived from the private key as the means to authenticate specific runners.

## Modes{% #modes %}

A private action runner can be used with App Builder, Workflow Automation, or both.

The following is a general overview diagram for private actions:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/private_action_runner_-_diagram_general.8fc6e71da9565c0f7b8f899a17cfd9af.png?auto=format"
   alt="Overview diagram illustrating how Private actions interact with Datadog and the user's browser" /%}

### Mode differences{% #mode-differences %}

The following table explains some distinctions between App Builder and Workflows modes, including their triggering mechanisms and operational models.

| Distinction          | App Builder mode                                                             | Workflows mode                                             |
| -------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Triggermechanism** | Human-driven - each action is initiated by user interaction with an App      | Can run automatically without direct human intervention    |
| **Triggermodel**     | Push model - actions are triggered by directly accessing a URL on the runner | Pull model - periodically checks for tasks to execute      |
| **Datahandling**     | Keeps data in your private environment and does not send it to Datadog       | Reports the result of private action executions to Datadog |

The difference in models can result in varying latencies. App Builder mode's push model might lead to more immediate responses, whereas the pull model in Workflows mode might introduce delays based on polling frequency.

### App Builder mode{% #app-builder-mode %}

When your private action runner is in App Builder mode, queries that call your private services are sent directly from the user's browser to the private action runner, which proxies requests to your services. At no point does your data enter Datadog when the runner is in App Builder mode; it communicates with Datadog only for enrollment and authentication purposes.

In the following diagram, **App Management** refers to backend App Builder actions that are unrelated to the Private Action runner, such as deleting an app.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/private_action_runner_-_diagram_app_builder.d409612422aafd2b44eb0ba771fc120d.png?auto=format"
   alt="Overview diagram illustrating how Private actions work in App Builder mode, including authentication" /%}

#### Authentication{% #authentication %}

To ensure secure communication, the Datadog frontend sends a single-use scoped token with each request, which the runner validates using a private key. This mechanism ensures that your data remains within your network and does not enter Datadog while maintaining the integrity and security of your private actions.

#### Runner hostname{% #runner-hostname %}

In App Builder mode, the user's browser talks directly to your private action runner. As a result, you must specify a custom domain name that points to your runner. To set up your domain, point an `A` or `CNAME` record to your network's ingress. Your ingress must be capable of terminating HTTPS requests and forwarding them to the runner container on port 9016. The domain and ingress do not have to be accessible to the public internet; the `A` or `CNAME` record can point, for example, to a load balancer that is only accessible through your company's VPN.

### Workflow Automation mode{% #workflow-automation-mode %}

If your private action runner runs in Workflows-only mode, you do not need to perform any setup beyond the initial enrollment. The private action runner continuously polls for tasks from your Datadog account, executes them by interacting with your internal service, and reports the result back to Datadog.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/private_action_runner_-_diagram_workflow.9034fc43fe904c71755911b987a8475e.png?auto=format"
   alt="Overview diagram illustrating how Private actions work in Workflow Automation mode" /%}

### Both{% #both %}

When you select the option to use both modes, the runner dynamically adjusts the mode it uses based on the type of request it receives. This ensures smooth operation whether the runner is handling app requests, Workflow Automation executions, or a combination of both.

## Monitor your Private Action Runners with Datadog Metrics{% #monitor-your-private-action-runners-with-datadog-metrics %}

While setting up your Private Action Runners, you can enable observability metrics to monitor your runners' health and private action usage. These metrics can be used in Datadog products like Dashboards and Monitors. To get started quickly, you can use the provided [out-of-the-box Dashboard](https://app.datadoghq.com/dash/integration/private_actions_runner).

## Further reading{% #further-reading %}

- [App Builder Connections](https://docs.datadoghq.com/service_management/app_builder/connections)
- [Workflow Connections](https://docs.datadoghq.com/service_management/workflows/connections)
- [Use Private Actions](https://docs.datadoghq.com/actions/private_actions/use_private_actions)
- [Run a Script with the Private Action Runner](https://docs.datadoghq.com/actions/private_actions/run_script)
- [Handling Private Action Credentials](https://docs.datadoghq.com/actions/private_actions/private_action_credentials)
- [Remediate Kubernetes incidents faster using private actions in your apps and workflows](https://www.datadoghq.com/blog/private-actions/)
- [How we created a single app to automate repetitive tasks with Datadog Workflow Automation, Datastore, and App Builder](https://www.datadoghq.com/blog/pm-app-automation/)

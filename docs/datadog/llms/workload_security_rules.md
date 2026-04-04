# Source: https://docs.datadoghq.com/security/workload_protection/workload_security_rules.md

# Source: https://docs.datadoghq.com/security/threats/workload_security_rules.md

---
title: Workload Protection Detection Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Workload Protection > Workload Protection Detection
  Rules
---

# Workload Protection Detection Rules

This topic explains how Workload Protection actively monitors system activity and evaluates it against a set of out-of-the-box (OOTB) rules to detect suspicious behavior.

## Proactively block threats with Active Protection{% #proactively-block-threats-with-active-protection %}

By default, all OOTB Agent crypto mining threat detection rules are enabled and actively monitoring for threats.

[Active Protection](https://docs.datadoghq.com/security/workload_protection/guide/active-protection) enables you to proactively block and terminate crypto mining threats identified by the Datadog Agent threat detection rules.

## Workload Protection rules construction{% #workload-protection-rules-construction %}

Workload Protection rules consist of two different components: Agent rules and threat detection rules.

- **Agent rules:** [Agent rules](https://app.datadoghq.com/security/configuration/workload/agent-rules) are evaluated on the Agent host. Workload Protection first evaluates activity within the Datadog Agent against Agent expressions to decide what activity to collect. Agent expressions use Datadog's [Security Language (SECL)](https://docs.datadoghq.com/security/workload_protection/agent_expressions).

For example, here is the *Agent rule* expression `cryptominer_args`:

  ```text
  exec.args_flags in ["cpu-priority", "donate-level", ~"randomx-1gb-pages"] ||
  exec.args in [
      ~"*stratum+tcp*",
      ~"*stratum+ssl*",
      ~"*stratum1+tcp*",
      ~"*stratum1+ssl*",
      ~"*stratum2+tcp*",
      ~"*stratum2+ssl*",
      ~"*nicehash*",
      ~"*yespower*"
  ]
  ```

- **Threat detection rules:** [Threat detection rules](https://app.datadoghq.com/security/configuration/rules?product=cws) are evaluated on the Datadog backend. Threat detection rules are composed of existing Agent rules and additional expression parameters.

Here is the *threat detection rule* `Process arguments match cryptocurrency miner`. It uses the Agent rules, `cryptominer_args` and `windows_cryptominer_process`, identified by `@agent.rule_id`, with additional expression parameters:

  ```text
  @agent.rule_id:(cryptominer_args || windows_cryptominer_process)
  -@process.executable.path:"/usr/bin/grep"
  ```

### Workload Protection rules pipeline{% #workload-protection-rules-pipeline %}

Workload Protection uses the following pipeline when evaluating events:

1. The Agent rules evaluate system activity on the Agent host.
1. When activity matches an Agent rule expression, the Agent generates a detection event and passes it to the Datadog backend.
1. The Datadog backend evaluates the detection event to see if it matches any threat detection rules that use the Agent rule that sent the event.
1. If there is a match, a signal is generated and displayed in [Signals](https://docs.datadoghq.com/security/workload_protection/security_signals).
1. Any [Notification Rules](https://app.datadoghq.com/security/configuration/notification-rules) that match the severity, detection rule type, tags, and attributes of the signal are triggered.

The following diagram illustrates this pipeline:

{% image
   source="https://datadog-docs.imgix.net/images/security/cws/threat_detection_pipeline_2.41a4d342a31348e7b0d0b0ed52de82d0.png?auto=format"
   alt="Workload Protection detection pipeline" /%}

### Saving resources by design{% #saving-resources-by-design %}

Workload Protection detection rules are complex, correlating several datapoints, sometimes across different hosts, and including third party data. This complexity would result in considerable compute resource demands on the Agent host if all rules were evaluated there.

Datadog solves this problem by keeping the Agent lightweight with only a few rules, and processes most rules using the threat detection rules on the Datadog backend.

Only when the Agent observes an event that matches its rules does it send a detection to the Datadog backend. The Datadog backend then evaluates the detection to determine if it meets its threat detection rule expressions. Only if there is a match does the Datadog backend create a signal.

### Custom rule design{% #custom-rule-design %}

Understanding the dependency threat detection rules have on Agent rules is important when you want to use custom rules. Custom rules help to detect events Datadog is not detecting with its OOTB rules.

There are two use cases:

- **Create a threat detection rule using an existing Agent rule:** To create a threat detection rule that uses an existing Agent rule, you only need to create a threat detection rule that references the Agent rule and adds any additional expression parameters you need.
- **Create a threat detection rule using a new Agent rule:** To detect an event that the current Agent rules do not support, create a custom Agent rule to detect that event, and then create a custom threat detection rule that uses the custom Agent rule.

For a detailed explanation, see [Workload Protection Detection Rules](https://docs.datadoghq.com/security/workload_protection/workload_security_rules/custom_rules).

## Agent rules summary{% #agent-rules-summary %}

Agent rules contain Agent expressions that determine which activities the Agent collects. A full set of Agent rules is called a policy. Datadog provides you with several [out-of-the-box Agent rules](https://app.datadoghq.com/security/configuration/workload/agent-rules) powered by the default Agent policy.

With [Remote Configuration](https://docs.datadoghq.com/remote_configuration/) enabled, you automatically receive new and updated Workload Protection Agent rules when they're released. These bundled Agent rules are used in the [default detection rules](https://docs.datadoghq.com/security/default_rules/#cat-workload-security).

{% alert level="info" %}
Remote Configuration for Workload Protection is in Preview. If you have any feedback or questions, contact [Datadog support](https://docs.datadoghq.com/help).
{% /alert %}

### Agent expressions{% #agent-expressions %}

Agent expressions use [Datadog's Security Language (SECL)](https://docs.datadoghq.com/security/workload_protection/agent_expressions) to define behavior based on activity in your hosts and containers, as shown in the following examples:

#### Detect when the `passwd` command is executed{% #detect-when-the-passwd-command-is-executed %}

To detect when the `passwd` command is executed, there are a few attributes to note.

On most Linux distributions, the `passwd` utility is installed at `/usr/bin/passwd`. Execution events include `exec`, `execve`, `fork`, and other system calls. In the Workload Protection environment, all of these events are identified by the `exec` symbol.

Putting it all together, the rule expression is `exec.file.path == "/usr/bin/passwd"`.

The `passwd` command rule is already present in the default Workload Protection Agent policy. However, Agent expressions can also be more advanced, and can define rules that match on process ancestors or use wildcards for broader detections.

#### Detect when a PHP or Nginx process launches Bash{% #detect-when-a-php-or-nginx-process-launches-bash %}

To detect when a PHP or Nginx process launches Bash, there are a few attributes to note.

On most Linux distributions, Bash is installed at `/usr/bin/bash`. As in the previous example, to detect execution, include `exec.file.path == "/usr/bin/bash"` in your rule. This ensures the rule is accounting for the execution of Bash, and also Bash as a child process of PHP or Nginx.

A process ancestor's filename in Workload Protection is an attribute with the symbol `process.ancestors.file.name`. To check if the ancestor is Nginx, add `process.ancestors.file.name == "nginx"`. Since PHP runs as multiple processes, use a wildcard to expand the rule to any process with the prefix `php`. To check if the ancestor is a PHP process, add `process.ancestors.file.name =~ "php*"`.

Putting it all together, the rule expression is `exec.file.path == "/usr/bin/bash" && (process.ancestors.file.name == "nginx" || process.ancestors.file.name =~ "php*")`.

## Detection rules summary{% #detection-rules-summary %}

Detection rules run in the Datadog backend after events are sent over as logs. The logs are then evaluated based on patterns of events described in the [detection rules](https://app.datadoghq.com/security/configuration/rules?product=cws). If the pattern matches a detection rule, a [security signal](https://docs.datadoghq.com/security/workload_protection/security_signals) is generated. Datadog continuously develops new detection rules, which are automatically imported into your account.

## Further Reading{% #further-reading %}

- [Setting Up Workload Protection](https://docs.datadoghq.com/security/workload_protection/)
- [Agent Expressions](https://docs.datadoghq.com/security/workload_protection/agent_expressions)
- [Workload Protection Events](https://docs.datadoghq.com/security/threats/backend)
- [Learn more about Security notification variables](https://docs.datadoghq.com/security/notifications/variables/)

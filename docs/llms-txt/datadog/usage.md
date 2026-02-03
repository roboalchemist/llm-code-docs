# Source: https://docs.datadoghq.com/events/guides/usage.md

# Source: https://docs.datadoghq.com/coterm/usage.md

---
title: Using Datadog CoTerm
description: >-
  Learn how to record terminal sessions, create shims for automatic recording,
  and configure CoTerm to protect against dangerous commands.
breadcrumbs: Docs > Datadog CoTerm > Using Datadog CoTerm
---

# Using Datadog CoTerm

## View recorded terminal sessions{% #view-recorded-terminal-sessions %}

At the beginning and end of every recorded terminal session, CoTerm displays a link to view the session in Datadog. You can also [view all recorded terminal sessions](https://app.datadoghq.com/terminal-streams).

## CoTerm CLI command structure{% #coterm-cli-command-structure %}

```shell
ddcoterm [OPTIONS] [-- <COMMAND>...] [COMMAND]
```

Run `ddcoterm --help` for all options and commands.

## Record a terminal session{% #record-a-terminal-session %}

CoTerm records terminal sessions that you can play back and review in Datadog. For your security, sensitive data (such as passwords and API keys) are [automatically redacted](https://docs.datadoghq.com/sensitive_data_scanner/). Any processes launched in the terminal session are recorded as [events](https://docs.datadoghq.com/events/).

### Launch and record an interactive terminal session{% #launch-and-record-an-interactive-terminal-session %}

To manually launch Datadog CoTerm and record the entirety of your terminal session:

```shell
ddcoterm
```

When you end the session, CoTerm stops recording and sends the captured process data to Datadog.

### Record the output of a command{% #record-the-output-of-a-command %}

To run an individual command and record its output:

```shell
ddcoterm -- datadog-agent status
```

This launches CoTerm and runs `datadog-agent status`. When the process completes, CoTerm stops recording and sends the captured process data to Datadog.

## Automatically record a command{% #automatically-record-a-command %}

To configure CoTerm to automatically record all future invocations of a particular command, create a shim:

```shell
ddcoterm shim create datadog-agent
```

After you create a shim, restart your terminal or source your profile. (For example, run `source ~/.bashrc`.) If you are using a shell other than Bash or Zsh, add `path/to/.ddcoterm/overrides` to your PATH manually.

## Protect against dangerous terminal commands{% #protect-against-dangerous-terminal-commands %}

To prevent the accidental execution of designated terminal commands, you can configure CoTerm to act as a linter. For more control, you can use CoTerm with [Datadog Case Management](https://docs.datadoghq.com/incident_response/case_management/) to require approval for designated commands.

### Lint a command{% #lint-a-command %}

When you try to execute a designated command (for example, `kubectl scale`), CoTerm can display warnings and prompt you for confirmation.

1. Create a shim for your command: `ddcoterm shim create kubectl`

1. Configure a linting rule in your `.ddcoterm/config.yaml` file. For details on how to configure linting in CoTerm, see [CoTerm Configuration Rules](https://docs.datadoghq.com/coterm/rules).

In the `.ddcoterm/config.yaml` file:

   ```yaml
   process_config:
     commands:
       - command: "kubectl"
         lints:
           - |
             if has_arg("scale") and flags.context == nil then
               return string.format("No kubectl context specified (effective context: '%s'). It is recommended to always explicitly specify the context when running `kubectl scale`.", k8s_context)
             end
      
```

With this configuration, CoTerm intercepts any `kubectl scale` command without a `--context` flag.

{% image
   source="https://datadog-docs.imgix.net/images/coterm/linter-warning.b95d396c74546f13c7f7ed63c0a9c8f4.png?auto=format"
   alt="Command line interface. The user has run 'kubectl scale foo'. The output says 'Warning from CoTerm: No kubectl context specified (effective context: 'minikube'). It is recommended to always explicitly specify the context when running kubectl scale. Do you want to continue? (y/n)'" /%}

### Require approval for commands{% #require-approval-for-commands %}

For even more dangerous commands, CoTerm can require explicit approval by another team member (through Case Management) before running the command.

1. Create a shim for your command: `ddcoterm shim create kubectl`

1. Configure requiring approval in your `.ddcoterm/config.yaml` file. For details, see [CoTerm Configuration Rules](https://docs.datadoghq.com/coterm/rules).

In the `.ddcoterm/config.yaml` file:

   ```yaml
   process_config:
     commands:
       - command: "kubectl"
         rules:
           # Record and require approval for all executions of `kubectl scale` in a production context
           - rule: |
               local applicable = has_arg("scale") and k8s_context:match("prod")
               local user_message = "Proceed with caution. This command may disrupt your Kubernetes cluster setup."
               local approver_message = "Ensure that the user has documented a rollback plan before approving."
               return applicable, user_message, approver_message
             actions: ["record", "logs", "process_info", "approval"]
      
```

With this configuration, when you run a `kubectl scale --context prod` command, CoTerm creates an approval request in [Case Management](https://docs.datadoghq.com/incident_response/case_management/). If you opt to associate the approval request with an active [incident](https://docs.datadoghq.com/incident_response/incident_management/), other incident responders are automatically added as approvers. After this request is approved, your command executes. You can also configure [case automation rules](https://docs.datadoghq.com/incident_response/case_management/automation_rules/) to trigger workflows based on approval requests.

#### Manually require approval{% #manually-require-approval %}

To create an approval request manually, run:

```shell
ddcoterm approve
```

#### Bypass approval{% #bypass-approval %}

To bypass approval and run your command, set the `COTERM_BREAK_GLASS` environment variable.

For example:

```shell
COTERM_BREAK_GLASS=true kubectl delete foo
```

## Further reading{% #further-reading %}

- [Datadog CoTerm](https://docs.datadoghq.com/coterm)
- [Install Datadog CoTerm](https://docs.datadoghq.com/coterm/install)
- [CoTerm Configuration Rules](https://docs.datadoghq.com/coterm/rules)

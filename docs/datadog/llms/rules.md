# Source: https://docs.datadoghq.com/security/notifications/rules.md

# Source: https://docs.datadoghq.com/coterm/rules.md

---
title: CoTerm Configuration Rules
description: >-
  Configure CoTerm with Lua-based lints and rules to validate commands, require
  approvals, and control actions for specific terminal commands.
breadcrumbs: Docs > Datadog CoTerm > CoTerm Configuration Rules
---

# CoTerm Configuration Rules

You can configure CoTerm to take specific actions when it intercepts certain commands by adding lints and rules to your `.ddcoterm/config.yaml` file under `process_config`.

These lints and rules are written in [Lua](https://en.wikipedia.org/wiki/Lua_%28programming_language%29). For syntax and further details, see [Lua's documentation](https://lua.org/docs.html).

## Lints{% #lints %}

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

Each item under `lints` is a Lua snippet that can return a string. Lints are evaluated in order. If a lint returns a string, that string is shown to the user as a warning prompt:

{% image
   source="https://datadog-docs.imgix.net/images/coterm/linter-warning.b95d396c74546f13c7f7ed63c0a9c8f4.png?auto=format"
   alt="Command line interface. The user has run 'kubectl scale foo'. The output says 'Warning from CoTerm: No kubectl context specified (effective context: 'minikube'). It is recommended to always explicitly specify the context when running kubectl scale. Do you want to continue? (y/n)'" /%}

The user then has the option to continue or abort.

## Rules{% #rules %}

```yaml
process_config:
  commands:
    - command: "kubectl"
      rules:
        # Record and require approval for all executions of `kubectl scale` in a production context
        - rule: |
            local k8s_context = flags.context or k8s_current_context or "unknown"
            local matches = has_arg("scale") and k8s_context:match("prod")
            local user_message = "Proceed with caution. This command may disrupt your Kubernetes cluster setup."
            local approver_message = "Ensure that the user has documented a rollback plan before approving."
            return matches, user_message, approver_message
          actions: ["record", "logs", "process_info", "approval"]
        # Record all other executions of kubectl scale, but don't require approval and don't bother with messages for users+approvers
        - rule: has_arg("scale")
          actions: ["record", "logs", "process_info"]
        # For all other kubectl commands, just run the command with ~zero overhead; no recording, no requiring approval
        - rule: true
          actions: []
```

Rules are more powerful than lints. For each item under `rules`, set `rule`, a Lua snippet that returns 1-3 values; and `actions`, a list of actions for CoTerm to take.

### Rule return values{% #rule-return-values %}

Each `rule` returns 1-3 values: `boolean, [string], [string]`.

1. (required) A Boolean, whether the rule matches.
1. (optional) A string, containing a message for the user. This string provides context to the user. It is only displayed if the first return value is `true`.
1. (optional) A string, containing a message for the approver. If the first return value is `true` and the corresponding `actions` field contains `approval`, this string is displayed in the approval request in Datadog.

### Actions{% #actions %}

CoTerm can take the following actions when `rule` returns `true`:

- `record`: Record the terminal session and send it to Datadog.
- `logs`: Generate Datadog logs, containing searchable snapshots of terminal output.
- `process_info`: Record all processes launched inside the terminal session and generate an event for each process.
- `approval`: Require approval before running the command.
- `incidents`: Associate the recording with the [Datadog Incident](https://docs.datadoghq.com/incident_response/incident_management/) that the user is responding to, if any. If the user is responding to more than one incident, they are prompted to pick one.

To take no action (other than running the command) when `rule` returns `true`, set `actions: []`.

### Rule evaluation{% #rule-evaluation %}

Rules are evaluated in order. CoTerm runs the actions specified for the first rule that evaluates to `true`, and does not evaluate any further rules.

## Action hierarchy{% #action-hierarchy %}

You can specify actions for CoTerm to take in a number of different ways. CoTerm decides which actions to take according to the following hierarchy:

1. **CLI flags**: If you specify actions in CLI flags (such as `--save-level`, `--approval`), CoTerm takes only the actions specified through these CLI flags. This overrides all other configurations.
1. **Lua configuration file**: If no CLI flags specify actions, but a Lua rule in `.ddcoterm/config.yaml` evaluates to `true`, CoTerm takes the actions specified with the first rule that evaluates to `true`. Overrides all configurations other than CLI flags.
1. **`process_config.default_actions`**: If no CLI flags specify actions, and no Lua rules match, CoTerm takes the actions specified in `process_config.default_actions` in `.ddcoterm/config.yaml`, if any.
1. **Default actions**: If no CLI flags specify actions, no Lua rules match, and `process_config.default_actions` is not set, CoTerm takes the following actions: `["record", "logs", "process_info"]`.

## Lua environment and helper functions{% #lua-environment-and-helper-functions %}

All Lua snippets are executed inside a sandboxed [Luau](https://luau.org/) runtime. CoTerm injects the following variables and functions into the runtime:

### Global variables{% #global-variables %}

{% dl %}

{% dt %}
`executable` - string
{% /dt %}

{% dd %}
The executable in your command.For `kubectl foo bar`, `executable` is `kubectl`.
{% /dd %}

{% dt %}
`args` - array<string>
{% /dt %}

{% dd %}
The arguments in your command.For `kubectl foo --bar=baz`, `args` is `["foo", "--bar=baz"]`.
{% /dd %}

{% dt %}
`flags` - table
{% /dt %}

{% dd %}
A [table](https://www.lua.org/pil/2.5.html) of any `--` key-value flags in your command.For `command foo --bar baz` or `command foo --bar=baz`, `flags` has one entry where `key` is `bar` and `value` is `baz`. That is, `flags.bar = baz`.
{% /dd %}

{% dt %}
`k8s_current_context` - string
{% /dt %}

{% dd %}
The `current-context` value from `~./kube/config`. If this value is not found, `k8s_current_context` is [nil](https://www.lua.org/pil/2.1.html).
{% /dd %}

{% /dl %}

### Helper functions{% #helper-functions %}

{% dl %}

{% dt %}
`has_arg(<string>)`
{% /dt %}

{% dd %}
Returns `true` if argument is present.For `kubectl foo bar`, `has_arg("bar")` returns `true`.
{% /dd %}

{% /dl %}

## Further reading{% #further-reading %}

- [Datadog CoTerm](https://docs.datadoghq.com/coterm)
- [Install Datadog CoTerm](https://docs.datadoghq.com/coterm/install)
- [Using CoTerm](https://docs.datadoghq.com/coterm/usage)

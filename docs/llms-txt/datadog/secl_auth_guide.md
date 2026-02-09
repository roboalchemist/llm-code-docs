# Source: https://docs.datadoghq.com/security/workload_protection/secl_auth_guide.md

---
title: Writing Custom Rule Expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Workload Protection > Writing Custom Rule
  Expressions
---

# Writing Custom Rule Expressions

This guide shows you how to write effective SECL (Security Language) rules for Datadog Workload Protection.

## SECL overview{% #secl-overview %}

Datadog SECL is a custom domain-specific language used to create Agent expressions and policies within Datadog Workload Protection. SECL allows security teams to define real-time threat detection rules by specifying conditions, operators, and patterns that security agents can monitor across hosts, containers, applications, and cloud infrastructure.

## How SECL rules fit together{% #how-secl-rules-fit-together %}

Think of SECL as a local filter: it runs inside the Agent on each host, watching kernel and OS events. When an event matches your SECL expression, the Agent raises a detection.

Datadog threat detection rules act as backend logic: they combine one or more Agent rules (using `@agent.rule_id`), add thresholds, suppress noise, and decide how alerts are routed.

In summary, the Agent rule finds raw behavior and the detection rule turns it into a usable signal.

{% alert level="info" %}
This guide describes how to create rule expressions manually, but Workload Protection also provides the Assisted rule creator wizard to walk you through creating the Agent and detections rules together. See [Create the custom Agent and detection rules together.](https://docs.datadoghq.com/security/threats/workload_security_rules/custom_rules/?tab=host#create-the-custom-agent-and-detection-rules-together)
{% /alert %}

### Agent expression syntax{% #agent-expression-syntax %}

The standard format of a SECL expression is:

```plaintext
<event-type>.<event-attribute> <operator> <value> [<operator> <event-type>.<event-attribute>] ...
```

Using this format, an example rule for a Linux system looks like this:

```plaintext
open.file.path == "/etc/shadow" && process.file.path not in ["/usr/sbin/vipw"]
```

## Quickstart{% #quickstart %}

Here's a summary of the process:

1. Go to Workload Protection [Policies](https://app.datadoghq.com/security/workload-protection/policies).
1. Click **New Policy** to create a policy, or select an existing policy from the list to open it.
1. In the policy, click **Add Agent Rule**, and then click **Manual rule creator**.
1. In **Define the agent expression**, enter your expression using the following steps.
1. Select **Linux** or **Windows**. Most expression fields are OS-specific.
1. Choose a trigger (event type). Choose a trigger that aligns with the behavior you want to catch, but not everything that could happen.
   - Examples: `exec`, `open`, `connect`, `create`, `dns`, etc.
1. Anchor the trigger on one or two stable fields. Example:
   - Linux: `exec.file.path`, `process.ancestors.file.name`.
   - Windows: `file.path`, `exec.args`, `open_key.registry.key_path`.
1. Add context to the trigger. Examples:
   - Parent ancestry: `process.ancestors.*`
   - User info: `process.user`, `process.uid`
   - Containers: `container.*`
   - Time: `process.created_at > 5s`
1. Insert safe exceptions. Examples: `not in [...]`, `!~`. In SECL, you can implement "allowlists" (the conditions that are included or excluded from detection) using ordinary operators like `not in`, `!~`, or conditional exclusions.
1. Name and save the rule.

### Test the rule{% #test-the-rule %}

To view Agent events that match the expression, view the rule details, and then click **View Events**. The [Agent Events explorer](https://app.datadoghq.com/security/workload-protection/agent-events) opens and displays the Agent events that match the expression. In **Agent Events**, you can see the raw telemetry: every kernel/OS event that matched the SECL rule before suppression or aggregation.

When viewing raw Agent events, do the following:

1. Confirm the rule is firing on the intended activity.
1. Measure the scope and frequency across hosts/environments.
1. Decide if this is the expected baseline or a true threat.
1. If events are benign, add a suppression or update your expression with allowlist conditions.
1. If events are suspicious, escalate by passing the finding into your incident process, or take action to stop or isolate the suspicious workload.

To test detection rules, view the rule details, and then click **[Number] detection rules found**. The Detection Rules explorer opens and displays the backend logic layer: the detection rule, linked signals, metadata, JSON definition, tags, and version history.

When viewing the backend logic for a detection rule, do the following:

1. Confirm that the rule name, description, and JSON (net_util_in_container) clarify what the rule is supposed to catch.
1. Measure whether the rule is noisy or precise by reviewing the aggregate metrics (query histogram, signals over time, affected hosts)..
1. Decide if the detected activity is expected (baseline) or suspicious (threat).
1. Suppress/allowlist if benign, escalate/contain if suspicious.

## Rule authoring tips{% #rule-authoring-tips %}

- Always set the operating system (OS).
- Anchor on ancestry to reduce noise. Use `process.ancestors.file.name`.
- Use durations (for example, `> 5s`, `10m`, `2h`) to target narrow execution windows.
- Use exact match (`==`) whenever possible as it results in the lowest noise.
- List membership (`in [...]`) is best for allowlists or controlled sets of values.
- Use a glob match (`~"/path/*"`) for path families as it is safer and faster than regex.
- Use regex (`=~`) only when globs/lists can't be used. Keep the regex expression as narrow as possible. As a rule of thumb, start with `==` or `in [...]`. Reach for regex only as a last resort.
- Use negation (`not in [...]`, `!~`) to carve out exceptions explicitly (for example, trusted tools).
- Use CIDR operators (`in CIDR`, `not in CIDR`) for network boundaries.
- Name rules by behavior, with a format that follows *What + Who + Context*.
- Tag generously: `team`, `app`, `env`, `MITRE`, `severity`.

### Avoid common mistakes{% #avoid-common-mistakes %}

| Pattern                                              | Explanation                                       |
| ---------------------------------------------------- | ------------------------------------------------- |
| `open.file.path == "/etc/passwd"`, `exec.comm != ""` | Too broad. Matches a lot of valid use cases.      |
| `fd.name contains "/"`                               | Matches nearly every file I/O event.              |
| `container.id != ""`                                 | Useful only if scoped with a more specific field. |

## Common building blocks{% #common-building-blocks %}

For information and examples of common building blocks like operators, patterns, regular expressions, duration, and platform-specific syntax, see [Creating Agent Rule Expressions](https://docs.datadoghq.com/security/workload_protection/agent_expressions).

## Example library{% #example-library %}

### Linux{% #linux %}

#### Access to sensitive files (allowlist safe tools){% #access-to-sensitive-files-allowlist-safe-tools %}

```plaintext
open.file.path in ["/etc/shadow", "/etc/sudoers"] &&
process.file.path not in ["/usr/sbin/vipw", "/usr/sbin/visudo"]
```

#### Nginx or PHP spawning bash{% #nginx-or-php-spawning-bash %}

```plaintext
exec.file.path == "/usr/bin/bash" &&
(
  process.ancestors.file.name == "nginx" ||
  process.ancestors.file.name =~ "php*"
)
```

#### Suspicious IMDS access from container{% #suspicious-imds-access-from-container %}

```plaintext
connect &&
network.destination.ip in ["169.254.169.254"] &&
container.id != ""
```

#### Kernel module loads outside maintenance window{% #kernel-module-loads-outside-maintenance-window %}

```plaintext
load_module &&
process.user != "root" &&
process.ancestors.file.name not in ["modprobe", "insmod"]
```

#### Sensitive file read shortly after start{% #sensitive-file-read-shortly-after-start %}

```plaintext
open.file.path == "/etc/secret" &&
process.file.name == "java" &&
process.created_at > 5s
```

#### Outbound to non-corporate IPs (CIDR allowlist){% #outbound-to-non-corporate-ips-cidr-allowlist %}

```plaintext
connect &&
network.destination.ip not in [10.0.0.0/8, 192.168.0.0/16, 172.16.0.0/12]
```

### Windows{% #windows %}

#### Registry persistence via run key{% #registry-persistence-via-run-key %}

```plaintext
set_key_value &&
open_key.registry.key_path =~ "*\\Software\\Microsoft\\Windows\\CurrentVersion\\Run*"
```

#### Unsigned Binary Launching PowerShell{% #unsigned-binary-launching-powershell %}

```plaintext
exec.file.path =~ "*\\WindowsPowerShell\\v1.0\\powershell.exe" &&
process.parent.file.path !~ "*\\Program Files*" &&
process.user_sid != "S-1-5-18"
```

### Cross-platform{% #cross-platform %}

#### Crypto-miner indicators{% #crypto-miner-indicators %}

```plaintext
exec.args_flags in ["cpu-priority", "donate-level", ~"randomx-1gb-pages"] ||
exec.args in [~"*stratum+tcp*", ~"*nicehash*", ~"*yespower*"]
```

## Rollout strategy{% #rollout-strategy %}

| Phase        | Action                                                        |
| ------------ | ------------------------------------------------------------- |
| **Draft**    | Author rule with YAML metadata and proper filters.            |
| **Simulate** | Use Agent in read-only mode.                                  |
| **Validate** | Run in staging workloads. Validate behavior with real events. |
| **Tune**     | Add suppressions, `not in`, `container.image`, etc.           |
| **Scale**    | Reference in backend detection rules for full rollout.        |

After validatation and deployment, continue monitoring rule performance to keep false positives low and coverage strong as workloads evolve.

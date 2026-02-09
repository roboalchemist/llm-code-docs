# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/command-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/command-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/command-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/command-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/command-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/command-injection.md

---
title: Avoid command injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid command injection
---

# Avoid command injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/command-injection`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

In Go, the `exec.Command` function is used to run external commands. Using this function carelessly can lead to command injection vulnerabilities. Carefully review the data flow that leads to a command execution and ensures no data can be injected by a third-party.

Command injection occurs when untrusted input is passed directly to a system shell, allowing an attacker to execute arbitrary commands. This can result in unauthorized access to the system, data leaks, or other security breaches.

Avoid executing commands constructed using user-provided data, or if you must, always validate and sanitize user inputs before passing them to `exec.Command`.

## How to remediate?{% #how-to-remediate %}

Either remove the user-controlled data, filter the potential command with a list of allowed command or sanitize the command before execution.

If there still are variables in the arguments to `exec.Command` after remediation, include the following comment before the line to suppress the warning:

```
// no-dd-sa:go-security/command-injection
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import (
	"context"
	"os"
	"os/exec"
)

func main() {
	cmdName := os.Args[1]
	ctx := context.Background()
	cmd := exec.CommandContext(ctx, cmdName, "init")
	output, err := cmd.CombinedOutput()

	userInput := os.Args[2]
	cmd = exec.CommandContext(ctx, "/bin/sh", "-c", userInput)
	cmd = exec.CommandContext(ctx, "sh", "-c", userInput)
	cmd = exec.CommandContext(ctx, "cmd", "/c", userInput)
	cmd = exec.CommandContext(ctx, "cmd.exe", "/C", userInput)
	cmd = exec.CommandContext(ctx, "powershell.exe", "-Command", userInput)
}
```

```go
import (
	"os"
	"os/exec"
)

func main() {
	cmdName := os.Args[1]
	ctx := context.Background()
	cmd := exec.Command(cmdName, "init")
	output, err := cmd.CombinedOutput()

		userInput := os.Args[2]
	cmd = exec.Command("/bin/sh", "-c", userInput)
	cmd = exec.Command("sh", "-c", userInput)
	cmd = exec.Command("cmd", "/c", userInput)
	cmd = exec.Command("cmd.exe", "/C", userInput)
	cmd = exec.Command("powershell.exe", "-Command", userInput)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import (
    "os"
    "os/exec"
)

func main () {
    res, err := exec.Command(/bin/ls", "something")

    directory := os.Args[1]
    cmd := exec.Command("/bin/ls", directory)
    cmd = exec.Command("/bin/sh", "-c", "/bin/ls", ".")
    output, err := cmd.CombinedOutput()
}
```

```go
import (
    "context"
    "os"
    "os/exec"
)

func main () {
    ctx := context.Background()
    res, err := exec.CommandContext(ctx, "/bin/ls")

    directory := os.Args[1]
    cmd := exec.CommandContext(ctx, "/bin/ls", directory)
    cmd = exec.CommandContext(ctx, "/bin/sh", "-c", "/bin/ls -a")
    output, err := cmd.CombinedOutput()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 
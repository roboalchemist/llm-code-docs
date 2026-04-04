# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/avoid-runtime-injection.md

---
title: Avoid using user input for runtime commands
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using user input for runtime commands
---

# Avoid using user input for runtime commands

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/avoid-runtime-injection`

**Language:** Kotlin

**Severity:** Error

**Category:** Security

**CWE**: [73](https://cwe.mitre.org/data/definitions/73.html)

## Description{% #description %}

This rule helps prevent severe security vulnerabilities such as command injection and path injection. Command injection occurs when an attacker can influence the formation of a system command that your app executes, potentially allowing them to execute arbitrary commands on your system. Path injection is similar but involves influencing file or library paths, which can lead to unauthorized file access or loading malicious libraries.

To avoid this, sanitize and validate user input before using it in a system command or file path. For example, you can use an allowlist of permitted commands or library names. Alternatively, you can use the array form of `runtime.exec` or `ProcessBuilder`, which doesn't involve string concatenation or interpolation that could lead to command injection.

It's essential to be aware of the risks and to validate and sanitize user input rigorously. It's always safer to avoid using user input directly in system commands or file paths.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
class CommandExecutor {
    fun executeCommand(userInput: String) {
        val runtime = Runtime.getRuntime()
        // Dangerous: Command injection possible
        runtime.exec("ls " + userInput)
        runtime.exec("/bin/sh -c ${userInput}")
        runtime.exec(String.format("cat %s", userInput))
    }

    fun loadDynamicLibrary(libName: String) {
        val runtime = Runtime.getRuntime()
        // Dangerous: Path injection possible
        runtime.loadLibrary("lib" + libName)
        runtime.loadLibrary("lib ${libName}")
        runtime.loadLibrary(String.format("%s.dll", libName))
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class CommandExecutor {
    fun executeCommand(userInput: String) {
        val runtime = Runtime.getRuntime()
        // Safe: Use array form with fixed command and arguments
        runtime.exec(arrayOf("ls", userInput))

        // Safe: Use ProcessBuilder with argument list
        ProcessBuilder("cat", userInput)
            .redirectError(ProcessBuilder.Redirect.INHERIT)
            .start()
    }

    fun loadDynamicLibrary() {
        val runtime = Runtime.getRuntime()
        // Safe: Use fixed, known library names
        runtime.loadLibrary("mylib")

        // Alternative: Use allowlist for library names
        val allowedLibs = setOf("lib1", "lib2")
        if (libName in allowedLibs) {
            runtime.loadLibrary(libName)
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}

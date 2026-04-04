# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/os-popen-command-injection.md

---
title: Unsanitized data is sent to popen, causing command injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Unsanitized data is sent to popen, causing command injection
---

# Unsanitized data is sent to popen, causing command injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/os-popen-command-injection`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

This rule identifies potential OS Command Injection vulnerabilities. These occur when user-supplied data from a POST request's JSON body, such as input from `request.get_json()` or `data.get("<key>")`, is passed directly to the `os.popen()` function without sanitization or validation. This vulnerability allows an attacker to craft a JSON payload containing malicious commands. The server then executes these commands with the privileges of the running application, which can lead to unauthorized server access, data breaches, or denial of service.

## How to Remediate{% #how-to-remediate %}

To prevent OS Command Injection vulnerabilities when handling user input for shell commands:

1. **Avoid `os.popen()` with user input.** Prefer using the `subprocess` module. Pass commands and arguments as a list (for example, `subprocess.run(["command", "arg1", "arg2"], shell=False)`). This method avoids shell interpretation of the command string.
1. **Sanitize input if direct shell execution is unavoidable.** Use functions such as `shlex.quote()` for any part of the command that originates from user input.
1. **Implement allowlisting.** Permit only a predefined set of commands or command patterns. Map user input to these safe, fixed command strings.
1. **Adhere to the principle of least privilege.** Run the application with the minimum privileges necessary for its operation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"


@app.route("/run", methods=["POST"])
def run_command():
    data = request.get_json()
    command = data.get("command") if data else None
    if not command:
        return "Missing 'command' in request body", 400
    stream = os.popen(command)
    output = stream.read()
    return f"<pre>{output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os
import shlex
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/run_safe_shlex", methods=["POST"])
def run_command_safe_shlex():
    data = request.get_json()
    user_command = data.get("command") if data else None
    if not user_command:
        return "Missing 'command' in request body", 400

    # Sanitize using shlex.quote for commands meant for the shell
    # This is safer but still relies on os.popen, ideally move to subprocess
    safe_arg = shlex.quote(user_command)
    # Example: using it as an argument to a fixed command like echo
    stream = os.popen(f"echo {safe_arg}") # user_command is now an argument
    output = stream.read()
    return f"<pre>{output}</pre>"

@app.route("/run_safe_whitelist", methods=["POST"])
def run_command_safe_whitelist():
    data = request.get_json()
    action = data.get("action") if data else None
    if not action:
        return "Missing 'action' in request body", 400

    actual_command = ""
    if action == "list_users":
        actual_command = "whoami" # Fixed, safe command
    elif action == "show_date":
        actual_command = "date"   # Fixed, safe command
    else:
        return "Invalid action", 400

    stream = os.popen(actual_command) # Executes a whitelisted, fixed command
    output = stream.read()
    return f"<pre>{output}</pre>"

@app.route("/run_safe_subprocess", methods=["POST"])
def run_command_safe_subprocess():
    data = request.get_json()
    command_parts = data.get("command_array") if data else None # Expecting ["ls", "-l", "/tmp"]
    if not command_parts or not isinstance(command_parts, list):
        return "Missing 'command_array' (list) in request body", 400

    # Using subprocess with a list of arguments and shell=False is safest
    try:
        # Whitelist allowed executable
        if command_parts[0] not in ["ls", "echo", "whoami", "date"]:
            return "Command not allowed", 400

        result = subprocess.run(command_parts, capture_output=True, text=True, check=True, shell=False)
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}", 500
    except FileNotFoundError:
        return f"Command not found: {command_parts[0]}", 400


# This should not be flagged as command_from_config is not from request.get_json()
@app.route("/run_config_command", methods=["POST"])
def run_config_command():
    # data = request.get_json() # Input not used for command
    command_from_config = "ls -l /etc"
    stream = os.popen(command_from_config)
    output = stream.read()
    return f"<pre>{output}</pre>"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}

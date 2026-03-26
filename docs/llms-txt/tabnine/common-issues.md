# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/common-issues.md

# Common Issues

Solutions to frequently encountered problems.

### Performance Issues

#### Slow Responses

**Causes**:

* Slow network
* Large file context
* Complex prompts

**Solutions**:

{% stepper %}
{% step %}
**Check network**

Run:

```bash
ping api.tabnine.com
```

{% endstep %}

{% step %}
**Be more specific in prompts**

Make prompts concise and targeted to reduce processing.
{% endstep %}

{% step %}
**Reduce file references**

Limit the amount of file content referenced in a single request.
{% endstep %}

{% step %}
**Try a different model**

Use the `/model` command to switch models.
{% endstep %}
{% endstepper %}

#### High Memory Usage

**Normal**: 50-200 MB

**If excessive**:

{% stepper %}
{% step %}
**Clear conversation**

Run:

```
/clear
```

{% endstep %}

{% step %}
**Restart Tabnine CLI**

Restart the Tabnine CLI process to free memory.
{% endstep %}

{% step %}
**Reduce context size**

Limit context or file sizes referenced in prompts.
{% endstep %}
{% endstepper %}

### Connection Issues

#### Cannot Connect to API

**Symptoms**: "Failed to connect"

**Solutions**:

{% stepper %}
{% step %}
**Check internet**

Run:

```bash
ping api.tabnine.com
```

{% endstep %}

{% step %}
**Check firewall**

Ensure port 443 is allowed.
{% endstep %}

{% step %}
**Check proxy settings**

Verify proxy environment variables or client proxy configuration.
{% endstep %}

{% step %}
**Try debug mode**

Run:

```bash
DEBUG=1 tabnine
```

{% endstep %}
{% endstepper %}

#### Proxy Issues

**Solution**: Set proxy variables:

```bash
export NODE_USE_ENV_PROXY=1
export HTTP_PROXY=http://proxy:8080
export HTTPS_PROXY=http://proxy:8080
tabnine
```

### File Access Issues

#### Cannot Read Files

**Symptoms**: "Permission denied" or file not found

**Solutions**:

{% stepper %}
{% step %}
**Check file permissions**

Ensure the process has read permissions for the file.
{% endstep %}

{% step %}
**Verify file path**

Confirm the path is correct.
{% endstep %}

{% step %}
**Check working directory**

Ensure you're running commands from the intended working directory.
{% endstep %}

{% step %}
**Use absolute paths**

Try using absolute file paths to avoid path resolution issues.
{% endstep %}
{% endstepper %}

#### Cannot Write Files

**Symptoms**: Cannot create or modify files

**Solutions**:

{% stepper %}
{% step %}
**Check directory permissions**

Ensure write permissions are available for the target directory.
{% endstep %}

{% step %}
**Verify disk space**

Confirm there is sufficient disk space.
{% endstep %}

{% step %}
**Check file locks**

Make sure the file is not locked by another process.
{% endstep %}
{% endstepper %}

### Feature Issues

#### Remote Code Search Not Working

**Solutions**:

{% stepper %}
{% step %}
**Check enabled**

Open settings: `/settings` → Tools → Remote Code Search
{% endstep %}

{% step %}
**Verify account access**

Ensure your account has the necessary access.
{% endstep %}

{% step %}
**Check indexing**

Confirm the codebase is indexed in Tabnine account settings.
{% endstep %}
{% endstepper %}

#### Coaching Not Working

**Solutions**:

{% stepper %}
{% step %}
**Check enabled**

Open settings: `/settings` → Tools → Coaching Guidelines
{% endstep %}

{% step %}
**Verify account access**

Ensure your account has the necessary access.
{% endstep %}

{% step %}
**Be specific in prompts**

Try more specific prompts when requesting coaching.
{% endstep %}
{% endstepper %}

### Other Issues

#### Command Not Found

**Symptoms**: `tabnine: command not found`

**Solutions**:

{% stepper %}
{% step %}
**Verify installation**

Confirm Tabnine CLI is installed (see [**Installation Guide**](https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started/installation)).
{% endstep %}

{% step %}
**Check PATH**

Ensure your PATH includes the installation directory.
{% endstep %}

{% step %}
**Run with full path**

Example:

```bash
~/.local/bin/tabnine
```

(Linux/macOS)
{% endstep %}
{% endstepper %}

#### Unexpected Behavior

**Solution**: Enable debug mode:

```bash
DEBUG=1 tabnine
```

This shows detailed logs to help identify the issue.

### Getting More Help

* [**FAQ**](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/faq) - Frequently asked questions
* **Debug Mode**: `DEBUG=1 tabnine`
* **Report Issue**: Use `/bug` command in Tabnine CLI

<details>

<summary>Still having issues? (FAQ &#x26; reporting)</summary>

* See the FAQ: [**FAQ**](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/faq)
* Enable debug logs:

```bash
DEBUG=1 tabnine
```

* Report an issue using the `/bug` command in Tabnine CLI.

</details>

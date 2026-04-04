# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting.md

# Troubleshooting

Solutions to common problems and questions about Tabnine CLI.

### Quick Troubleshooting

#### Slow Performance?

* Check network connection.
* Be more specific in prompts.
* Try a different model: `/model`.
* See [Common Issues - Performance](https://docs.tabnine.com/main/getting-started/tabnine-cli/common-issues#performance-issues).

#### Can't Access Files?

* Check file permissions.
* Verify working directory.
* Use absolute paths.
* See [Common Issues - File Access](https://docs.tabnine.com/main/getting-started/tabnine-cli/common-issues#file-access-issues).

#### Can't interact with the agent?

* Ensure you have network connection to your Tabnine host
* Tabnine CLI requires **Tabnine Agents** to be enabled for your team.
  * If sign-in works but agent workflows/tools don’t, ask your admin to enable Agents.
* Restart Tabnine CLI after Agents are enabled.
* See the [FAQ](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/faq) for details.

#### Other Issues?

* Try clearing: `/clear` or `Ctrl+L`.
* Check the [FAQ](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/faq) for answers.
* See [Common Issues](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/common-issues) for solutions.

### Specific Issues

Here are some solutions to frequently encountered problems.

#### Performance Issues

**Slow Responses**

**Causes**:

* Slow network
* Large file context
* Complex prompts

**Solutions**:

1. **Check network:** Run the following to check for network issues:
   1. ```bash
      ping api.tabnine.com
      ```
2. **Be more specific in prompts** – Make prompts concise and targeted to reduce processing.
3. **Reduce file references** – Limit the amount of file content referenced in a single request.
4. **Try a different model** – Use the `/model` command to switch models.

**High Memory Usage**

**Normal**: 50-200 MB

If the memory usage is excessive, try the following:

1. **Clear the conversation:**
   1. ```bash
      /clear
      ```
2. **Restart Tabnine-CLI:** Restart the Tabnine CLI process to free memory.
3. **Reduce context size:** Limit context or file sizes referenced in prompts.

#### Connection Issues

**Cannot Connect to API**

**Symptoms**: "Failed to connect"

**Solutions**:

1. Check internet – Run:

```bash
ping api.tabnine.com
```

2. Check firewall – Ensure port 443 is allowed.
3. Check proxy settings – Verify proxy environment variables or client proxy configuration.
4. Try debug mode – Run:

```bash
DEBUG=1 tabnine
```

**Proxy Issues**

**Solution**: Set proxy variables:

```bash
export NODE_USE_ENV_PROXY=1
export HTTP_PROXY=http://proxy:8080
export HTTPS_PROXY=http://proxy:8080
tabnine
```

#### File Access Issues

**Cannot Read Files**

**Symptoms**: "Permission denied" or file not found

**Solutions**:

1. Check file permissions – Ensure the process has read permissions for the file.
2. Verify file path – Confirm the path is correct.
3. Check working directory – Ensure you're running commands from the intended working directory.
4. Use absolute paths – Try using absolute file paths to avoid path resolution issues.

**Cannot Write Files**

**Symptoms**: Cannot create or modify files

**Solutions**:

* Check directory permissions – Ensure write permissions are available for the target directory.
* Verify disk space – Confirm there is sufficient disk space.
* Check file locks – Make sure the file is not locked by another process.

#### Feature Issues

**Remote Code Search Not Working**

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

**Coaching Not Working**

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

**Agent Features Not Working**

If sign-in works but Tabnine CLI can’t communicate with the agent (or agent tools are missing), your team may not have Agents enabled.

Ask your Tabnine admin to enable **Tabnine Agents** for your team in the Admin Console, then restart Tabnine CLI.

#### Other Issues

**Command Not Found**

**Symptoms**: `tabnine: command not found`

**Solutions**:

* Verify installation – Confirm Tabnine CLI is installed (see [**Installation Guide**](https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started/installation)).
* Check PATH – Ensure your PATH includes the installation directory.
* Run with full PATH – Example:

```bash
~/.local/bin/tabnine
```

**Unexpected Behavior**

**Solution**: Enable debug mode:

```bash
DEBUG=1 tabnine
```

This shows detailed logs to help identify the issue.

### Still Having Issues?

Use `/bug` in Tabnine CLI to report the issue.

# Source: https://help.aikido.dev/ide-plugins/troubleshooting/troubleshooting-ide-plugin-connectivity.md

# Troubleshooting IDE Plugin Connectivity

If the Aikido IDE plugin cannot connect or login is not persistent, it’s likely due to a network restriction or firewall rule.

To function correctly, the plugin must be able to access the following domains over HTTPS (port 443):

```
*.aikido.dev
or
ide.aikido.dev
```

## Troubleshooting

### 1. Check connectivity from your terminal

**macOS / Linux (bash)**

```
# Test DNS resolution
nslookup ide.aikido.dev

# Test HTTPS connectivity
curl -v https://ide.aikido.dev/ping

# Or check if the port is open
nc -vz ide.aikido.dev 443
```

**Windows (PowerShell)**

```
# Test DNS resolution
Resolve-DnsName ide.aikido.dev

# Test HTTPS connectivity
Invoke-WebRequest -Uri https://ide.aikido.dev/ping -UseBasicParsing

# Test port connectivity
Test-NetConnection ide.aikido.dev -Port 443
```

### 2. Verify proxy or firewall settings

* Ensure your proxy or corporate firewall allows outbound HTTPS connections to \*.aikido.dev.
* If you’re using a VPN, try disabling it temporarily to see if it affects connectivity.
* Confirm no SSL interception or certificate pinning issues are blocking access.

### 3. Still having issues?

If all tests fail or you receive timeouts, please share the command output with the Aikido team so we can help diagnose further.

{% content-ref url="visual-studio-information-for-support" %}
[visual-studio-information-for-support](https://help.aikido.dev/ide-plugins/troubleshooting/visual-studio-information-for-support)
{% endcontent-ref %}

{% content-ref url="jetbrains-information-for-support" %}
[jetbrains-information-for-support](https://help.aikido.dev/ide-plugins/troubleshooting/jetbrains-information-for-support)
{% endcontent-ref %}

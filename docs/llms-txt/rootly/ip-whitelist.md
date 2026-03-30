# Source: https://docs.rootly.com/integrations/ip-whitelist.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Whitelist

> Configure IP whitelisting for Rootly integrations to ensure secure network communication with your infrastructure and third-party services.

## Overview

When configuring integrations with Rootly, you may need to whitelist specific IP addresses to allow secure communication between Rootly and your internal systems or third-party services.

## 🛡️ Security Considerations

IP whitelisting provides an additional layer of security by:

* **Restricting access** to only trusted IP addresses
* **Preventing unauthorized connections** from unknown sources
* **Ensuring compliance** with your organization's security policies
* **Protecting sensitive data** during integration communication

## 📍 Rootly Outbound IP Addresses

All Rootly integrations use the following outbound IP addresses for external communication:

<Note>
  Add these IP addresses to your firewall rules or security group configurations to allow Rootly integrations to function properly.
</Note>

### Production IP Addresses

```
34.232.217.139/32
18.213.181.255/32
```

<Note>
  **IP Address Stability**: These IP addresses are permanent and will never change. You can safely configure long-term firewall rules and security policies using these addresses without concern for future updates.
</Note>

## 🔍 Common Integration Requirements

### Webhook Endpoints

When setting up webhooks that receive data from Rootly:

* Whitelist both IP addresses in your webhook endpoint configuration
* Ensure your endpoint accepts HTTPS connections
* Verify SSL certificates are properly configured

### API Access

For integrations that make API calls to your services:

* Configure API gateway or load balancer rules
* Update firewall policies to allow the IP addresses
* Test connectivity after configuration changes

## 🧪 Testing Your Configuration

After whitelisting the IP addresses:

1. **Verify integration connectivity** in your Rootly dashboard
2. **Check integration logs** for any connection errors
3. **Test webhook delivery** if applicable
4. **Monitor firewall logs** to confirm allowed traffic

<Warning>
  Failing to properly whitelist these IP addresses may result in integration failures, webhook delivery issues, or incomplete data synchronization.
</Warning>

***

**Need Help?** If you encounter issues with IP whitelisting, contact [support@rootly.com](mailto:support@rootly.com) with your integration details and network configuration.


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.axonius.com/docs/trend-micro-apex-one.md

# Trend Micro Apex One (OfficeScan)

The Trend Micro Apex One (formerly OfficeScan) adapter is an endpoint security solution protecting against malware, scripts, injection, ransomware, memory and browser attacks, and exploits.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Trend Micro Apex Central IP Address** *(required)* - The IP address of the Trend Micro Apex Central server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Application ID** *(required)* - The application unique Identifier assigned for Axonius to consume Trend Micro Control Manager Automation APIs.
3. **API Key** *(required)* - The request signature key assigned for Axonius to consume Trend Micro Control Manager Automation APIs.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Trend Micro Apex One.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trend%20Micro%20Apex%20One.png)

## APIs

You first need to use the **Automation API Access Settings** screen in **Trend Micro Control Manager** to allow Axonius to consume Control Manager Automation APIs. For details, see [Trend Micro Online Help Center](http://docs.trendmicro.com/en-us/enterprise/control-manager-70/automation-api-guide/automation-api-guide1/adding-an-applicatio.aspx).

## Required Ports

For details, see [Ports and protocols used by OfficeScan/Apex One that should be allowed through a firewall or router](https://success.trendmicro.com/solution/1054836-ports-and-protocols-used-by-officescan-apex-one-that-should-be-allowed-through-a-firewall-or-router#collapseOne).
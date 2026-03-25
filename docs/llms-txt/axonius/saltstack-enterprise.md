# Source: https://docs.axonius.com/docs/saltstack-enterprise.md

# vRealize Automation SaltStack Config (formerly SaltStack Enterprise)

vRealize Automation SaltStack Config intelligent automation delivers event-driven security, cloud, and configuration management.

<Callout icon="📘" theme="info">
  Note

  Axonius also supports **SaltStack Open Source** (designated adapter). For more information how to create a user and start the API service for SaltStack Open Source, see [REST API for Salt](https://docs.saltproject.io/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html).
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **vRealize Automation SaltStack Config Domain** *(required)* - vRealize Automation SaltStack Config server hostname or IP (e.g. saltstack.company.com)

2. **User Name** and **Password** *(required)* - These values must be created in vRealize Automation SaltStack Config.  The user account must have the needed permissions to log into the vRealize Automation SaltStack Config web UI, and view data about minions. For more details, see [Creating an Axonius User in vRealize Automation SaltStack Config](/docs/saltstack-enterprise#creating-an-axonius-user-in-vrealize-automation-saltstack-config).

3. **Config Name** *(required, default: internal)* – This is the value labelled “internal” on the vRealize Automation SaltStack Config web UI login page.

4. **Verify SSL** - Select whether to verify the SSL certificate offered by the host supplied in **vRealize Automation SaltStack Config Domain**. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).

<Image alt="SaltStack" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SaltStack.png" />

## Creating an Axonius User in vRealize Automation SaltStack Config

**To create an Axonius User in vRealize Automation SaltStack Config**

1. From the **vRealize Automation SaltStack Config UI**, navigate to the **System Administration** page.
2. From the **Roles** tab, create a new role. In the role, under **Resource Access** add Read-Only permissions to all relevant targets, which should include all the "Minions" in the system.
3. Under **Local Users**, create a new user and assign the new role to it.
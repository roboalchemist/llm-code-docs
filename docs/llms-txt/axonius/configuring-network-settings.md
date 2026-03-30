# Source: https://docs.axonius.com/docs/configuring-network-settings.md

# Configuring Network Settings

Use the **Network** settings page to manage your general network configurations.

## Subnet Parsing

The **Insert all possible Subnets on Device Network Interface** setting is enabled by default. When enabled, Axonius calculates and inserts all possible common subnets based on the device's IP addresses.

To reduce noise in subnet data, disable this setting. When disabled, Axonius checks which subnets the device is actually inserted into and receiving traffic from (as determined by the authoritative source), and fetches only these subnets.

## Internal CIDRs List

Listing all the internal CIDRs in your organization affects how Axonius classifies the access status of your Network assets - whether they are public or private (internal). This helps Axonius avoid false positives when considering a network as public.

For example, a certain block of IPs might include a public IP address. However, this block was purchased by your organization long ago, and since it's owned by the organization, all traffic within this block should be considered private.

In the **Internal CIDRs** field, enter a list of CIDR masks in `X.X.X.X/X` format. Note that if you don't stick to that format, you won't be able to save your changes.

![NetworkInternalCIDRs](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-5OZY7UP9.png)

### Managing CIDRs using API V2 Endpoints

If you want to add or remove a bulk of CIDRs (for example, 1000+) in a direct, scalable way, you can do it using Axonius V2 API instead of manually handling them from the Network Settings page.

Use the following API endpoints:

`GET /api/v2/internal_cidrs` - Retrieve the current list of configured internal CIDRs.
`PATCH /api/v2/internal_cidrs` - Add and/or remove CIDRs in a single request (supports bulk operations).
`DELETE /api/v2/internal_cidrs` - Remove all configured CIDRs at once.
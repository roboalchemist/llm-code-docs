# Source: https://docs.base44.com/documentation/enterprise/ip-allowlist.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding an IP allowlist for your workspace

> Control who can access your workspace by allowing sign-in only from approved IP addresses.

IP allowlist lets you restrict access to your enterprise workspace and its apps so that only people on specific networks can sign in. This is useful if your team connects from a known office network or VPN and you want to block access from other locations. Requests from IP addresses that are not in the allowlist receive a 403 Forbidden response.

When IP allowlist is enabled, all apps in the workspace are protected by the allowlist.

<Warning>
  Important:

  * IP allowlist is only available for enterprise workspaces.
  * Only workspace owners and admins can view or change IP allowlist settings.
  * Blocked access covers:
    * Published apps (people using the app)
    * Apps in builder mode (development and editing)
  * Supported IP formats:
    * Single IP: 192.168.1.1
    * CIDR notation: 192.168.1.0/24
    * IP range: 192.168.1.10-192.168.1.20
</Warning>

***

## Setting up an IP allowlist

1. Click your profile icon at the top right of your account.
2. Click the relevant workspace name.
3. Click **Settings** in your profile menu.
4. Click **Auth and security**.
5. Scroll to the **IP Allowlist** section.
6. Enable the **IP Allowlist** toggle.
7. In the list, enter the IP addresses or ranges you want to allow.
8. Click **Add**.

<Frame caption="Adding IP allowlist in your workspace">
    <img src="https://mintcdn.com/base44/iYNb0mom7jmWBtLR/images/ipallowlist.png?fit=max&auto=format&n=iYNb0mom7jmWBtLR&q=85&s=4736c750a6a839b1379dc22e4b506089" alt="Adding IP allowlist in your workspace" width="1440" height="857" data-path="images/ipallowlist.png" />
</Frame>

***

## FAQs

Click a question below to learn more about using IP allowlist for your workspace.

<AccordionGroup>
  <Accordion title="What if my internet provider changes my IP address?">
    If your public IP changes, you need to update the allowlist with the new IP. If your IP changes often, it is usually better to route access through a stable VPN endpoint or office network instead of adding individual home IPs.
  </Accordion>

  <Accordion title="Does IP allowlist replace authentication or SSO?">
    No. IP allowlist adds a network-level restriction on top of your existing sign-in and SSO setup. People still need valid credentials to sign in, even if they connect from an allowed IP.
  </Accordion>

  <Accordion title="Does IP allowlist affect outgoing connections from my apps?">
    No. IP allowlist controls who can access your workspace and its apps. It does not block or filter outbound connections that your apps make to external services or APIs.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).
# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-in-fortinets-fortigate.md

# How to Allow List in Fortinet's FortiGate

Fortinet **FortiGate’s Web Filter** can be configured to allow user access to Keepnet’s phishing simulation domains that may otherwise be blocked due to filtering. If your users can't access the simulation links during simulations, it’s recommended to allowlist the domains in FortiGate’s web filtering settings. This article provides step-by-step guidance for allowlisting using the FortiGate's **Static URL Filter** feature.

## Before You Start

FortiGate offers two ways to allow traffic through the web filter:

1. **Static URL Filter** (recommended here) — add specific domains to a list that is allowed by the firewall.
2. **Web Rating Overrides** — an alternate method that applies when using FortiGuard category-based filtering. For details on this option, please see Fortinet’s documentation on [Web Rating Overrides](https://docs.fortinet.com/document/fortigate/latest/administration-guide/122974/web-rating-override).

## Allowlisting via Static URL Filter

Follow these steps to add Keepnet’s domains to a FortiGate web filter profile.

1. **Sign in to Keepnet's platform** and go to **Phishing Simulator > Settings > Domains** page to download all the simulation domains.
2. Sign in to your **Fortinet administration portal.**
3. Go to **Security Profiles** > **Web Filter**.
4. Choose either a newly created web filter profile or an existing one configured for your phishing simulation traffic.
5. Inside the web filter settings, expand the **Static URL Filter** section. Turn on **URL Filter** and then click **Create New**.
6. In the URL field, add each Keepnet's phishing simulation domains— input only the domain (for example `example.com`, *without* `https://`).
7. **Set Matching Options**
   * **Type**: Simple
   * **Action**: Allow
   * **Status**: Enabled
8. Save your web filter profile to enforce the new list of allowed URLs.

## Test the Configuration

Once complete, **wait a few minutes** for changes to apply and then run a **small test phishing simulation** to check whether pilot users can successfully visit the simulation links. If domains are still blocked, review your FortiGate policy order, ensure the web filter is applied to the correct traffic policy, and consult FortiGate support if needed.

# Source: https://planetscale.com/docs/vitess/imports/import-tool-migration-addresses.md

# Import public IP addresses

> When importing a database using our [Import tool](/docs/vitess/imports/database-imports), you need to grant a set of IP addresses access to your external MySQL database so that PlanetScale can make the connection.

## Overview

To import your external database into PlanetScale, you need to allowlist PlanetScale's IP addresses in your database firewall or security group. This lets PlanetScale connect to your database during the import process.

## Where to find your IP addresses

The IP addresses you need to allowlist are shown during the import workflow on the **Connect to external database** step. You'll see a blue info box on the connection page that lists all the IP addresses that need access to your external database.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=51adf62afe74c5afa2d007872c634a6c" alt="IP addresses displayed on the connection step of import workflow" data-og-width="1568" width="1568" data-og-height="1108" height="1108" data-path="docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?w=280&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=c84c4251bbf4dbf0cb359a37ef24becf 280w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?w=560&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=d1a5bdf99d8f7866ab46a1fc1b0affe3 560w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?w=840&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=a3268e6deb7c6b562227d1f838321a12 840w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?w=1100&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=13295745ac6d799a06abdb173ceca0f9 1100w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?w=1650&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=b346ee0c98c7ebbc1f00ec9b7c65202e 1650w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows-ip-addresses/import-ips.png?w=2500&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=a6b91f5f2ac8993e930c1dc7d9477657 2500w" />
</Frame>

## Provider-specific firewall guides

If PlanetScale detects that you're connecting to a known database provider (like Amazon RDS, Aurora, Azure, GCP Cloud SQL, or DigitalOcean), you'll also see a direct link to that provider's firewall configuration documentation.

## Important notes

* **Region-specific IPs** - The IP addresses differ by region. Make sure you're using the IPs shown for your selected region.
* **IPs may change** - IP addresses can change occasionally. Always use the IPs shown in the import workflow.
* **All IPs required** - You need to allowlist all the IP addresses shown, not just one.

<Note>
  **Note**

  This guide is meant to be used alongside the [Database Imports guide](/docs/vitess/imports/database-imports) or one of the provider-specific migration guides.
</Note>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
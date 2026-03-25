# Source: https://help.aikido.dev/dast-surface-monitoring/attack-surface-scanning/add-or-ignore-subdomains-in-attack-surface.md

# Add or Ignore Subdomains in Attack Surface

By default, Aikido automatically discovers subdomains related to your domain. In some cases, you may want to manually add a subdomain (for assets that aren’t detected automatically) or exclude a subdomain (for assets that fall outside of your scope or don’t need scanning).

## Why manage subdomains?

* Add subdomains: Ensure important assets (like api.example.com) are included in your security scans.
* Exclude subdomains: Reduce noise and avoid scanning third-party or out-of-scope services (like a test environment or marketing site hosted elsewhere).

## Adding a subdomain

1. Navigate to your domain overview page.
2. Go to the Subdomains tab.
3. Click Add Subdomain in the top right.<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F7cDE793ijGNS7wiUCczY%2FScreenshot%202025-09-19%20at%2011.00.48.png?alt=media&#x26;token=fe3577c0-9414-4103-9e06-f25d6322f4e3" alt=""><figcaption></figcaption></figure>
4. Enter the subdomain you want to monitor.<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FTXDG5p8PVpQYhtYTHOyO%2FScreenshot%202025-09-19%20at%2011.00.36.png?alt=media&#x26;token=e52951fa-c335-44ba-b778-0e265d13d1b8" alt=""><figcaption></figcaption></figure>
5. Confirm to include it in future scans.

## Excluding a subdomain

1. From the Subdomains tab, find the subdomain in the list.
2. Open the Actions menu (three dots on the right).<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJKaJOInHjbn4Nivnm9TO%2FScreenshot%202025-09-19%20at%2011.00.30.png?alt=media&#x26;token=185c6221-d62d-4454-808e-79401bf8a740" alt=""><figcaption></figcaption></figure>
3. Select Exclude Subdomain.
4. The subdomain will no longer be scanned.

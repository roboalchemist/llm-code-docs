# Source: https://docs.intelligems.io/incident-report-12-28-2025-cdn-outage.md

# Incident Report (12/28/2025): CDN Outage

**Date:** December 28–29, 2025\
**Duration:** \~16 hours\
**Status:** Resolved

### Summary

On **Sunday, December 28, 2025**, Intelligems experienced a platform-wide outage caused by an unexpected failure in our CDN (Content Delivery Network) SSL certificate renewal process. As a result, Intelligems experiences failed to load for shoppers, and experiments and experiences were effectively paused.

The issue was fully resolved by **Monday, December 29, 2025 at approximately 8:45 AM ET**, and traffic has since returned to normal.

### Customer Impact

During the outage window:

* Intelligems experiences and experiments did not load for shoppers
* Experiments behaved as **paused**
* **No page-view data was collected**, and this data cannot be retroactively recovered
* Orders that occurred during the outage were **not attributed** to Intelligems

There was **no impact to storefront availability**, checkout, or order processing outside of Intelligems functionality.

### Timeline

* **September 19, 2025**\
  AWS rotated SSL certificates on the S3 service backing our CDN. This change introduced a latent incompatibility with custom domain validation but did not cause immediate issues.
* **September–December 2025**\
  Our CDN continued functioning normally due to a still-valid Cloudflare Edge SSL certificate.
* **Sunday, December 28, 2025 – 4:10 PM ET**\
  The Cloudflare Edge SSL certificate expired and attempted to auto-renew.
* **Certificate renewal failed**\
  Renewal failed because stricter origin validation surfaced the earlier S3 certificate incompatibility.
* **Sunday night / Monday morning**\
  The CDN became inaccessible due to the missing valid SSL certificate.
* **Monday, December 29, 2025 – \~8:45 AM ET**\
  The certificate was successfully re-validated, DNS and CDN rules were updated, and traffic began recovering globally.

### Root Cause

The outage was caused by a **failed automatic SSL certificate renewal** for our CDN domain.

Contributing factors:

* An AWS S3 SSL certificate change in September removed support for custom hostname validation
* The issue remained hidden while the Cloudflare Edge certificate was still valid
* When renewal occurred, stricter validation failed, causing the certificate to be removed
* Without a valid edge certificate, the CDN could not serve content

### Resolution

The incident was resolved by:

* Updating DNS validation records
* Adjusting CDN page rules to allow certificate validation
* Successfully re-provisioning the SSL certificate
* Allowing time for global DNS and CDN propagation

Service was restored incrementally as propagation completed.

### Preventative Actions

We are taking the following steps to prevent a recurrence:

* Migrating to a **more robust CDN architecture** with explicit origin compatibility
* Adding **certificate-expiration monitoring and alerting**
* Implementing **renewal dry-runs** and validation checks
* Establishing a clearer **on-call escalation process** for infrastructure incidents

### Data & Attribution Notes

* Page-view data during the outage window is **not recoverable**
* Orders placed during the outage may appear unattributed
* Our support team can help review specific orders affected during this period

### Closing

We sincerely apologize for the disruption and any impact this caused to your business. Reliability is critical to the trust you place in Intelligems, and we are treating this incident as a clear opportunity to strengthen our infrastructure and processes.

If you have questions about specific orders or data during the outage window, please reach out to our support team.

— **The Intelligems Team**

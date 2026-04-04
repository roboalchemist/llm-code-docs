# Source: https://docs.upsun.com/domains/steps.md

# Set up a custom domain

Once your project is ready for production, replace the automatically generated domain with your own custom domain.
Note that adding a domain disables the automatically generated URL for your Production environment only.

You can also [customize the URLs for your preview environments](https://docs.upsun.com/domains/steps/custom-domains-preview-environments.md).

## Before you begin

You need:

- A project that's ready to go live
- A domain with access to its settings with the registrar
- A registrar that allows `CNAME` records or [one of the alternatives](https://docs.upsun.com/domains/steps/dns.md) on [apex domains](https://docs.upsun.com/glossary.md#apex-domain)
- Optional: The [CLI](https://docs.upsun.com../../administration/cli.md) installed locally

If you are planning to use several subdomains of the same domain on different projects,
see how to [manage multiple subdomains](https://docs.upsun.com/domains/steps/subdomains.md) *before* you add your domain to Upsun.

## 1. Get the target for your project

You want to point your DNS record to the automatically generated URL.
Your domain needs to point to that target for your site to go live.

 - Navigate to your production environment and click **Settings Settings**.
 - Select the **Domains** tab.
 - In the **Configure your domain** section, copy the content of the **CNAME record** field.

## 2. Configure your DNS provider

Your DNS provider (usually your registrar) is where you manage your domain.
Most registrars offer similar functionalities regarding DNS configuration but use different terminology or configuration.
For example, some registrars require you to use an `@` to create custom records on the apex domain, while others don't.
Check your registrar's documentation.

Note that depending on your registrar and the time to live (TTL) you set,
it can take anywhere from 15 minutes to 72 hours for DNS changes to be taken into account.

To configure your CDN and your domain name to point to your project:

 - Open your CDN’s management system.
 - Point the CDN at your [target](#1-get-the-target-for-your-project).
 - Open your registrar’s domain management system.
 - Open your registrar’s domain management system and configure your DNS zone settings to point at your CDN.
The address or ``CNAME`` record to use varies by CDN provider.
Refer to the official documentation of your DNS provider and CDN provider.
 - Check that redirects and subdomains are set correctly for the [TLS certificate ownership verification](https://docs.upsun.com/domains/troubleshoot.md#ownership-verification).
 - [Disable the router cache](https://docs.upsun.com/domains/cdn.md#disable-the-router-cache).
 - Optional: For increased security and to prevent the CDN from being bypassed,
you can force all traffic to [go through the CDN](https://docs.upsun.com/domains/cdn.md#prevent-direct-access-to-your-server).
 - Optional: If you have multiple domains you want to be served by the same app, add a ``CNAME`` record for each of them.
That includes the ``www`` subdomain if you are using it in your [routes configuration](https://docs.upsun.com/define-routes.md).

Adding a custom domain sets your site as [visible to search engines](https://docs.upsun.com/environments/search-engine-visibility.md#how-its-done).
See how you can further [configure your CDN](https://docs.upsun.com/domains/cdn.md).

## 3. Set your domain

Add a single domain to your project:

 - Select the project where you want to add a domain.
 - Click Settings **Settings**.
 - Click **Domains**.
 - In the **Domain** field, enter your domain.
 - Click **Add domain**.

## What's next

* [Use a content delivery network](https://docs.upsun.com../cdn.md)
* [Use subdomains across multiple projects](https://docs.upsun.com/domains/steps/subdomains.md)
* [Use a custom TLS certificate](https://docs.upsun.com/domains/steps/tls.md)


# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Domain

> Learn about setting up endpoints with custom domains

# Overview

Using a Custom Domain with an [Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), you can send traffic from your own domain to your [Apps](/core-concepts/apps/overview) running on Aptible.

# Endpoint Hostname

When you set up an Endpoint using a Custom Domain, Aptible will provide you with an Endpoint Hostname of the form `elb-XXX.aptible.in`.

<Tip> The following things are **not** Endpoint Hostnames:
`app.your-domain.io` is your Custom Domain and `app-123.on-aptible.com` is a [Default Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain). In contrast, this is an Endpoint Hostname: `elb-foobar-123.aptible.in`. </Tip>

You should **not** send traffic directly to the Endpoint Hostname. Instead, to finish setting up your Endpoint, create a CNAME from your own domain to the Endpoint Hostname.

<Info> You can't create a CNAME for a domain apex (i.e. you **can** create a CNAME from `app.foo.com`, but you can't create one from `foo.com`). If you'd like to point your domain apex at an Aptible Endpoint, review the instructions here: [How do I use my domain apex with Aptible?](/how-to-guides/app-guides/use-domain-apex-with-endpoints/overview). </Info>

<Warning>Warning: Do **not** create a DNS A record mapping directly to the IP addresses for an Aptible Endpoint, or use the Endpoint IP addresses directly: those IP addresses change periodically, so your records and configuration would eventually go stale. </Warning>

# SSL / TLS Certificate

For Endpoints that require [SSL / TLS Certificates](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#ssl--tls-certificates), you have two options:

* Bring your own [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate): in this case, you're responsible for making sure the certificate you use is valid for the domain name you're using.
* Use [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls): in this case, you'll have to provide Aptible with the domain name you plan to use, and Aptible will take care of certificate provisioning and renewal for you.

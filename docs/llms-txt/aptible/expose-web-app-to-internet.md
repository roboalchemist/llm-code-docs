# Source: https://www.aptible.com/docs/how-to-guides/app-guides/expose-web-app-to-internet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to expose a web app to the Internet

This guide assumes you already have a web app running on Aptible. If you don't have one already, you can create one using one of our [Quickstart Guides](/getting-started/deploy-starter-template/overview).

This guide will walk you through the process of setting up an [HTTP(S) endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) with [external placement](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#endpoint-placement) using a [custom domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) and [managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls).

Let's unpack this sentence:

* [HTTP(S) Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview): the endpoint will accept HTTPS and HTTP traffic. Aptible will handle HTTPS termination for you, so your app simply needs to process HTTP requests.

* [External Placement](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#endpoint-placement): the endpoint will be reachable from the public internet.

* [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain): the endpoint will use a domain you provide(e.g. `www.example.com`).

* [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls): Aptible will provision an SSL / TLS certificate on your behalf.

Learn more about other choices here: [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview). Let's move on to the process.

## Create the endpoint

In the Aptible Dashboard:

* Navigate to your app

* Navigate to the Endpoints tab

* Create a new endpoint

  * Update the following settings and leave the rest as default:

    * **Type**: Custom Domain with Managed HTTPS.

    * **Endpoint Placement**: External.

    * **Domain Name**: the domain name you intend to use. In the example above, that was `www.example.com`, but yours will be different.

* Save and wait for the endpoint to provision. If provisioning fails, jump to [Endpoint Provisioning Failed](/how-to-guides/app-guides/expose-web-app-to-internet#endpoint-provisioning-failed).

> 📘 The domain name you choose should **not** be a domain apex. For example, [www.example.com](http://www.example.com/) is fine, but just example.com is not.

> For more information, see: [How do I use my domain apex with Aptible?](/how-to-guides/app-guides/use-domain-apex-with-endpoints/overview)

## Create a CNAME to the endpoint

Aptible will present you with an [endpoint hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname) and [managed HTTPS validation records](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls#managed-https-validation-records) once the endpoint provisions. The two have different but overlapping use cases.

### Endpoint hostname

The Endpoint Hostname is a domain name that points to your endpoint.

However, you shouldn't send your traffic directly there. Instead, you should create a CNAME DNS record (using your DNS provider) from the name you intend to use with your app (`www.example.com` in the example above) to the Endpoint Hostname.

So, create that CNAME now.

### Validation records

Managed TLS uses the validation records to provision a certificate for your domain via [Let's Encrypt](https://letsencrypt.org/). When you create those records, Aptible can provide certificates for you. If you don't create them, then Let's Encrypt won't let Aptible provision certificates for you.

As it happens, the CNAME you created for the Endpoint Hostname is *also* a validation record. That makes sense: you're sending your traffic to the endpoint; that's enough proof for Let's Encrypt that you're indeed using Aptible and that we should be able to create certificates for you. Note that there are two validation records. We recommend you create both, but you're not going to need the second one (the one starting with `_acme-challenge`) for this tutorial.

## Validate the endpoint

Confirm that you've created the CNAME from your domain name to the Endpoint Hostname in the Dashboard. Aptible will provision a certificate for you, then deploy it across your app.

If all goes well, you'll see a success message (if not, see [Endpoint Certificate Renewal Failed](/how-to-guides/app-guides/expose-web-app-to-internet#endpoint-certificate-renewal-failed) below).

You can navigate to your custom domain (over HTTP or HTTPS), and your app will be accessible.

## Next steps

Now that your app is available over HTTPS, enabling an automated [HTTPS Redirect](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-redirect) is a good idea.

You can also learn more about endpoints here: [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview).

## Troubleshooting

### Endpoint Provisioning Failed

If endpoint provisioning fails, restart your app using the [`aptible restart`](/reference/aptible-cli/cli-commands/cli-restart) command. You will see a prompt asking you to do so.

Note this failure is most likely due to an app health check failure. We have troubleshooting instructions here: [My deploy failed with *HTTP health checks failed*](/how-to-guides/troubleshooting/common-errors-issues/http-health-check-failed).

If this doesn't help, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support).

### Endpoint Certificate Renewal Failed

This failure is probably due to an issue with the CNAME you created. There are two possible causes here:

* The CNAME change is taking a little to propagate. Here, it's a good idea to wait for a few minutes (or seconds, if you're in a hurry!) and then retry via the Dashboard.

* The CNAME is wrong. An excellent way to check for this is to access your domain name (`www.example.com` in the examples above, but yours will be different). If you see an Aptible page saying something like "you're almost done", you probably got it right, and you can retry via the Dashboard. If not, double-check the CNAME you created.

If this doesn't help, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support).

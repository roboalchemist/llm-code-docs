# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/shared-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Shared Endpoints

HTTP(S) endpoints can be configured to share their underlying load balancer with other endpoints on the stack, reducing the cost of the endpoint. The main limitations of shared endpoints are:

* Clients using the endpoint must support [Server Name Identification (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication), and send the appropriate `Host` request header. SNI was first implemented in 2004 and has been nearly universally supported by clients since 2014 so only obscure or legacy clients will have issues connecting.
* Wildcard DNS records are not supported. Shared endpoints require a fully qualified domain name. A wildcard certificate can be used in conjunction with providing a domain (see [Configuration](#configuration) for details).
* Some attributes of how Endpoints handle requests are set at the load balancer level, and changing these attributes will migrate your Endpoint to a different load balancer. This comes with some implications for open connections to your endpoint, which are detailed below in the [Configuration](#configuration) section.

## Creating Shared Endpoints

Shared endpoints can be created:

* By checking the "Shared" box when creating an HTTP(S) endpoint using the [Aptible Dashboard](https://app.aptible.com).
* By using the `--shared` flag when creating an HTTP(S) endpoint using the [`aptible endpoints:https:create`](/reference/aptible-cli/cli-commands/cli-endpoints-https-create) CLI command.

Similarly, a dedicated endpoint can be converted to a shared endpoint:

* By checking the "Shared" box when updating a HTTP(S) endpoint using the [Aptible Dashboard](https://app.aptible.com).
* By using the `--shared` flag when updating an HTTP(S) endpoint using the [`aptible endpoints:https:modify`](/reference/aptible-cli/cli-commands/cli-endpoints-https-modify) CLI command.

### Converting to a Dedicated Endpoint

Shared endpoints cannot be converted back to dedicated. To go back to using a dedicated endpoint, create a new dedicated endpoint with the same configuration then delate the shared endpoint when it's no longer needed.

### Configuration

Shared endpoints support the same configuration options as dedicated HTTP(S) endpoints. The only exceptions of note are:

* Shared endpoints using a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) must specify a fully qualified domain when creating or migrating to a shared endpoint. This is the `--managed-tls-domain` option for CLI commands.
* Shared endpoints do not support managed wildcard domains, a fully qualified domain name must be used with [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls).

The following attributes necessitate changing or replacing the load balancer:

* [IP Filtering](/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering)
* [Endpoint Timeouts (`IDLE_TIMEOUT`)](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#timeouts)
* [Support TLS Protocols (`SSL_PROTOCOLS_OVERRIDE`)](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-protocols)

When making changes to the above attributes, the operation will necessarily take longer in order to avoid interrupting open connections. The following steps are taken, which allow HTTP clients to reconnect smoothly to the new load balancer, before your service is removed from the old load balancer:

1. Wait for DNS changes to propegate
2. Wait for the HTTP client keep-alive timeout to elapse
3. Wait for the TCP idle timeout to elapse
4. Wait up to 15 seconds for in-flight response to to finish sending

If your `IDLE_TIMEOUT` is set to 10 minutes or less, the process will complete without any disruption to a properly functioning client connection. For customers with an `IDLE_TIMEOUT` configured above 10 minutes, we recommend using a dedicated endpoint to avoid interruptions, or reaching out to [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for guidance.

<Warning>Converting an endpoint from dedicated to shared has the same behavior descibed above.</Warning>

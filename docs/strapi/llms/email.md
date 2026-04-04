# Email

The Email feature enables Strapi applications to send emails from a server or an external provider.

</IdentityCard>

## Configuration

Most configuration options for the Email feature are handled via your Strapi project's code. The Email feature is not configurable in the admin panel, however users can test email delivery if it has been setup by an administrator.

:::info Provider vs. Host
- The email provider refers to the package that Strapi calls to send an email (e.g. official providers such as Sendgrid or community packages such as `@strapi/provider-email-nodemailer`). Providers implement the logic for sending mail when Strapi invokes them.
- The provider host (or server) refers to the connection details (e.g. an SMTP hostname, port, or REST API endpoint) that the provider exposes. Some providers hide these details behind an API key, while others require you to supply host-related options in your configuration.

The Email feature only handles outbound delivery. Receiving or parsing incoming messages is outside the scope of the built-in plugin and must be implemented with your email provider's inbound webhooks or a custom integration.
:::

### Admin panel settings

**Path to configure the feature:** 

</Tabs>

:::tip Deliverability
For best deliverability, configure SPF/DKIM with your email provider and ensure the `defaultFrom` domain aligns with the domain you verified with the provider.
:::

##### Configuring providers

Newly installed providers are enabled and configured in [the `/config/plugins` file](/cms/configurations/plugins). If this file does not exist you must create it.

Each provider will have different configuration settings available. Review the respective entry for that provider in the [Marketplace](/cms/plugins/installing-plugins-via-marketplace) or 

</Tabs>

:::note

* When using a different provider per environment, specify the correct configuration in `/config/env/${yourEnvironment}/plugins.js|ts` (See [Environments](/cms/configurations/environment)).
* Only one email provider will be active at a time. If the email provider setting isn't picked up by Strapi, verify the `plugins.js|ts` file is in the correct folder.
* When testing the new email provider with those two email templates created during strapi setup, the _shipper email_ on the template defaults to `no-reply@strapi.io` and needs to be updated according to your email provider, otherwise it will fail the test (See [Configure templates locally](/cms/features/users-permissions#templating-emails)).

:::

###### Configuration per environment

When configuring your provider you might want to change the configuration based on the `NODE_ENV` environment variable or use environment specific credentials.

You can set a specific configuration in the `/config/env/{env}/plugins.js|ts` configuration file and it will be used to overwrite the default configuration.

Some providers expose SMTP-style connection details instead of (or in addition to) an API key. Add those values in `providerOptions` so Strapi can reach the provider host. For instance, the community Nodemailer provider expects the host, port, and authentication credentials:

</Tabs>

If your provider gives you a single URL instead of host and port values, pass that URL (for example `https://api.eu.mailgun.net`) in `providerOptions` using the key the package expects.

##### Creating providers

To implement your own custom provider you must 

</Tabs>

In the send function you will have access to:

* `providerOptions` that contains configurations written in `plugins.js|ts`
* `settings` that contains configurations written in `plugins.js|ts`
* `options` that contains options you send when you call the send function from the email plugin service

You can review the 

</Tabs>
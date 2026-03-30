# Source: https://redocly.com/blog/updates-2021-11.md

November felt like a wrap-up month at Redocly, in the sense that we wrapped up some really big projects and made some nifty UX improvements to our products such as the OpenAPI VS Code extension, Redoc and the Developer portal.

Let's have a quick look at our new features, enhancements and documentation-related news from November 2021.

We are also on a lookout for developers and documentarians at Redocly, so if you are interested in joining a leader in the API design and documentation space, keep reading for more details.

## Redocly OpenAPI VS Code extension

After several months of incremental improvements, we're happy to announce a **new major release** of the *Redocly OpenAPI extension for VS Code*. For this new version, we focused on improving the usability of the extension, paying special attention to first-time OpenAPI authors and those who prefer a guided approach to writing API definitions.

Here are [five reasons](/blog/new-release-redocly-openapi-vscode-extension) to try it today.

## API registry

**Clearer warnings with API validation**

When validating your API definitions, the API registry now shows the exact rule name that generated a warning in the **Results** output.

**Improved cancel subscription form**

We value your feedback on all things Redocly, so we improved the **Cancel subscription** form and added the ability for users to provide cancellation reason as feedback. This will help us better understand the user experience and improve our products.

**Configurable access control**

Organization owners can now disable the *Log in with Redocly account* option on the **Settings > Access control** page if they want to use only SSO login for their organization.

When you configure the access to SSO-only, the login flow will indicate that SSO is required for users trying to log in.

**Using wildcards in domain names**

When generating new license keys from the **Workflows > Settings > On-premise license keys** page, you can now use wildcards in domain names.

You can only use one wildcard in each configured domain.

This also applies to Reference docs.

**Changelog**
Find out about other fixes and enhancements by visiting the [Workflows changelog](/docs-legacy/workflows/changelog).

![Workflow features](/assets/workflows.3eb9e6233ed54c01e56fbc7ef66291faa9ea4a94475d1521ff5f0bf3b04d92b3.978384e4.png)

## Reference docs

**Support for separators in sidebar**

Reference docs now supports two new configuration options - `separator` and `separatorLine` for items configured in `sidebarLinks`.

We've also added support for the corresponding theming option called `sidebar > separatorLineColor`.

**Sending header information with every request**

We implemented a new configuration option called `sendXUserAgentInTryIt` to enable sending the `X-User-Agent: Redocly Try it API console` header with every request made from the *Try it* console.

**NOTE:** Before you can use this, make sure you add `X-User-Agent` to your [`Access-Control-Allow-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) CORS header.

**Automatic wrapping of long server URLs**

- Long server URLs in the *Try it* console now automatically wrap and adjust to the width of their containing element, giving you a clearer look at the full server URL values.
- The **Copy** button for server URLs has also been removed to declutter the space.


**Support for PKCE for OAuth2**

The *Try it* console now supports PKCE for OAuth2 authorization code flow. To enable it for a specific security definition, add the [`x-usePkce: true`](/docs-legacy/api-reference-docs/specification-extensions/x-use-pkce) specification extension.


```yaml
components:
  securitySchemes:
    oauth2_auth:
      type: "oauth2"
      flows:
        authorizationCode:
          x-usePkce: true,
          authorizationUrl: "https://example.com/authorize",
          tokenUrl: "https://example.com/token",
          scopes: {
            api: "Grants complete read/write access to the API"
```

**Reference docs changelog**
Here's a link to the entire [Reference docs changelog](/docs-legacy/api-reference-docs/changelog).

![Reference docs features](/assets/refdocs.bbb0c598669f5fcc4ed106cf15eb57362166b4f9632eccc273e27c6fbb97101f.978384e4.png)

## Developer portal

**Support for Amplitude analytics**
You can now use [Amplitude analytics](https://amplitude.com/) with the portal product. For more information on how to configure this, check the [Amplitude analytics](/docs-legacy/developer-portal/configuration/siteconfig/analytics#amplitude) topic.

**Exclude page URLs from sitemap**

There may be instances where you don't want certain page links included in your sitemap. You can now use the `excludeFromSearch` option in the front matter of a page to exclude its URL from *sitemap.xml*.

**Create interactive step-by-step guides**

We've added a number of new properties to the `OpenApiTryIt` component to help you create interactive step-by-step guides.

The new properties are:

- `id` *(optional)*
- `needs` *(optional)*
- `placeholder` *(optional)*
- `serverVariables` *(optional)*


For more information, see the [Developer portal changelog](/docs-legacy/developer-portal/changelog).

**New home for configuration options**

We've reorganized configuration options for modifying the `<head>` contents in your portal. Instead of adding these options to the `meta` section in `siteConfig.yaml` or to the top level of page front matter, you should now define them in a new section called [seo](/docs-legacy/developer-portal/configuration/siteconfig/seo).

This means you can now use the same configuration syntax in front matter and in `siteConfig.yaml` - a big win for consistency!

Specifically, this affects the following configuration options:

- `description`
- `image`
- `keywords`
- `title`
- `lang`
- `sitemap` in front matter
- `siteUrl` in the `siteConfig.yaml` file, and
- `x-meta` [specification extension](/docs-legacy/api-reference-docs/specification-extensions/x-meta) supported in integrated Reference docs pages.


Important
We recommend migrating to this new configuration approach as soon as possible. Although we currently support this, the old approach is now considered deprecated and will display warnings in the portal build log.

**Set up JSON-LD parameters**

You can now set up [JSON-LD](https://json-ld.org/) parameters for your portal in the `siteConfig.yaml` file or in the front matter for individual MD(X) pages in the portal.

**Developer portal changelog**
Read the entire list of fixes and enhancements on the [Developer portal changelog](/docs-legacy/developer-portal/changelog).

![Developer portal features](/assets/devportal.c653352a809d5345b0d11dc586e86f6da66f8e7357e54d2bc57a029b3709da8a.978384e4.png)

## OpenAPI CLI and Redoc

**OpenAPI CLI changelog**
Read more about OpenAPI CLI fixes and enhancements by visiting the [OpenAPI CLI changelog](/docs/cli/changelog).

**Redoc changelog**

To find out more about Redoc CLI fixes and enhancements, see the [Redoc changelog](https://github.com/Redocly/redoc/blob/master/CHANGELOG.md).

## Documentation updates

In the last month, our technical writing team spent a good chunk of time attending to customer feedback around documentation.

We added new topics for:

- Portal settings:
  - [Custom domain](/docs-legacy/developer-portal/settings/custom-domain),
  - [Notifications](/docs-legacy/developer-portal/settings/notifications) and
  - [Delete portal](/docs-legacy/developer-portal/settings/delete-portal)
- [SEO configuration with JSON-LD options](/docs-legacy/developer-portal/configuration/siteconfig/seo)
- [Self-hosted routing](/docs-legacy/api-reference-docs/guides/on-premise)


## Google Season of Docs 2021 - Completed

The Google Season of Docs for 2021 is now over and we published a [case study](/gsod-casestudy) to highlight our experience with the program.

## Redocly hiring documentarians and developers!

We have some rather ambitious plans for 2022, and to help us with that, we are on the lookout for a couple of documentation and developer experience professionals right now.

The technical writing team at Redocly has been pretty busy with some cool docs stuff, and are a great bunch of folks to work with.

If you are keen, or know someone who would be a good fit in the Redocly docs team, have a look at these roles and get in touch:

- [Technical Writer](https://redocly.com/careers/#technical-writer)
- [Developer Advocate](https://redocly.com/careers/#developer-advocate)


If you are a developer, we have a total of **33** (yes, you read that right!) developer roles going at the moment.

For a taste of what's involved, check out our [Full Stack Developer](https://redocly.com/careers#full-stack-developer) posting and get in touch with us pronto!
# Source: https://redocly.com/blog/updates-2021-05.md

The fifth month of the lap around the sun heralded another busy period at Redocly. We worked on, and delivered tons of new features, in addition to our regular fixes and enhancements.

This post is a round up of our product updates, enhancements and documentation-related news from May 2021.

## OpenAPI CLI

**Optional `--lint` parameter supported in `bundle`**
The `bundle` command now supports an optional `--lint` parameter. Refer to the [Redocly OpenAPI CLI commands - bundle](/docs/cli/commands/bundle) topic.

**Support for OpenAPI 3.1**

Way back in February 2021, when the OpenAPI Initiative released the OpenAPI specification 3.1.0, it unpacked quite some goodies for the developers and the API community.

Redocly's **OpenAPI CLI** tool now supports OpenAPI 3.1. You can now lint, validate, and bundle your OAS 3.1 definitions with OpenAPI CLI.

![OpenAPI CLI features](/assets/cli.fa8e21a5046048a9bfd9f13a81c927211e33979af473a4439e17b50d2403e31c.978384e4.png)

## Workflows

**Support for Single Sign-On (SSO) and multiple identity providers (IdPs)**

This feature is only available to Enterprise customers.

You can configure access via SSO:

- on a project level (specific API versions, Reference docs, and Developer portals), or
- across the entire Workflows organization, effectively allowing your users to log into Workflows with SSO instead of Redocly accounts.


To find out how to set this up, refer to our [Setting up access control](/docs-legacy/settings/access-control) guide.

You can also configure multiple identity providers and use them simultaneously across different projects. Refer to our [Configuring multiple identity providers](/docs-legacy/settings/identity-providers) guide for more information.

**Automatically expand schemas in Reference docs**

Workflows now supports the option to automatically expand schemas in your Reference docs.

You can configure it using **Settings > API reference settings > Live configuration > General > Schema expansion level**. Using this setting, you can:

- Set this option to `all` to expand all schemas regardless of their level, or
- Set it to a number to expand schemas up to the specified level.


**Improvements to roles and permissions**

This month, we've introduced new roles called `Admin`, `Maintainer` and `Reader` for your API definitions, Reference docs, and Developer portals, to indicate your access to each project.

*A project refers to any API definitions/registries, API versions, Reference docs or Developer portal you create using the [Workflows](https://app.redocly.com) app.*
To find out more, refer to our [Roles and permissions](/docs-legacy/people/roles-permissions) topic.

**Limiting builds**

We have improved and reintroduced the feature that lets you limit the amount of files [Workflows](https://app.redocly.com/) will pull from your GitHub repository during the build process. This is useful for preventing build timeout issues and reduces the risk of exceeding build limits for your plan.
For more information, refer to the [limiting builds](/docs-legacy/workflows/sources/github#connect-a-monorepo) section.

**Workflows changelog**
Find out about other fixes and enhancements by visiting the [Workflows changelog](/docs-legacy/workflows/changelog).

![Workflow features](/assets/workflows.3eb9e6233ed54c01e56fbc7ef66291faa9ea4a94475d1521ff5f0bf3b04d92b3.978384e4.png)

## Reference docs

**Support for custom Username/Password label text**

You can now replace the default "Username" and "Password" label text in the Try it authorization section with any custom text. For example, you can use the following options in your Reference docs configuration file(s):


```yaml
labels:
  tryItAuthBasicUsername: 'Your custom username label'
  tryItAuthBasicPassword: 'Your custom password label'
```

**Expand schemas in Reference docs**

A new configuration option `schemaExpansionLevel` lets you automatically expand schemas in your Reference docs.

You can set it to `all` to expand all schemas regardless of their level, or set it to a number to expand schemas up to the specified level. For example, `schemaFieldExpandLevel: 3` expands schemas up to three levels deep.

The default value is `0`, which means no schemas are expanded automatically.

**Using custom dynamic values**

The reference-docs CLI tool now supports an option called `--html-template-variables`. You can use it to pass custom dynamic values to your Reference docs HTML template at build time.

**Reference docs changelog**

Here's a link to the entire [Reference docs changelog](/docs-legacy/api-reference-docs/changelog).

![Reference docs features](/assets/refdocs.bbb0c598669f5fcc4ed106cf15eb57362166b4f9632eccc273e27c6fbb97101f.978384e4.png)

## Developer portal

**Control group items behavior**

The Developer portal sidebar now supports a new configuration option called `selectFirstItemOnExpand` to control the behavior of group items.

When this option is set to `true`, selecting the group name in the sidebar automatically activates the first item in the group.

**Upgrade to Reference docs library**
Upgraded the `@redocly/reference-docs` library to version `1.5.4`. To find out more, refer to the [Reference docs changelog](/docs-legacy/api-reference-docs/changelog).

**Configure login and authentication settings for the portal**

If the content on your portal is protected behind a login, you can now set up the `login` component without having to implement custom overrides.

- Use the `siteConfig.yaml file` to define the settings for your login button and menu.
- Customize the user avatar in the `components > login` section of the `theme.ts` file.


The `login` component is disabled by default, so you have to configure login and authentication settings for the portal manually.

**Support for login page in local development mode**

The portal now supports a login page in local development mode, making it easier to simulate the login process for debugging purposes.

**Improvements to our Apigee integration portal**

The following Apigee page components are now built into the portal and can be imported from `@redocly/developer-portal/apigee`:

- `AppPage`
- `AppsPage`
- `CreateAppPage`
Check the [developer portal starter repository](https://github.com/Redocly/developer-portal-starter) for an example, and refer to our [Apigee integration documentation](/docs-legacy/developer-portal/guides/apigee-integration-portal/overview) to understand how Apigee works with Redocly Developer portal


**Improved configuration of analytics integrations**

We have tweaked a few things with our `analytics` component in our main portal configuration file `siteConfig.yaml`.

- All analytics integrations are now configured under the top-level `analytics` key.
- You can now integrate FullStory analytics into your developer portal.



```yaml
analytics:
  fullstory:
    fs_org: YOUR_ORG_ID
```

When configured, the FullStory integration will work only in production, not in the local development mode.

**Google Global Site Tag integration**

You can now integrate [Google Global Site Tag](https://github.com/gatsbyjs/gatsby/tree/master/packages/gatsby-plugin-google-gtag) into your developer portal.

When configured, this integration will work only in production, not in the local development mode.

For information on how to set it up, refer to our [Site Config - analytics](/docs-legacy/developer-portal/configuration/siteconfig/analytics) topic.

**Theming images, keywords and buttons**

- Rich metadata images are now supported in the front matter of MD(X) pages. Add `image: /path/to/image-file` to the front matter of a page to set up its preview image. This image is displayed when sharing the link to the page on social media.
- You can now set the contents of the `<meta name="keywords">` tag in your portal, by providing the keywords as a comma-separated list in the `meta` section of the `siteConfig.yaml` file, or the page front matter. For more information, refer to our [Site Config - meta](/docs-legacy/developer-portal/configuration/siteconfig/meta) topic.
- We have added support for button styles. You can change the font weight and font family of the button text, control button shadowing and hover behavior, and set the border radius for the button element.


**Developer portal changelog**
Read the entire list of features and fixes on the [Developer portal changelog](/docs-legacy/developer-portal/changelog).

![Developer portal features](/assets/devportal.c653352a809d5345b0d11dc586e86f6da66f8e7357e54d2bc57a029b3709da8a.978384e4.png)

## Recap - Product videos

Here's a list of our product videos that explain Redocly's most popular features and key concepts.

- [API registry tour](https://www.youtube.com/watch?v=nj7v2oOnTj0)
- [Pagination in Reference docs](https://www.youtube.com/watch?v=7dMPPFVJx7A)
- [OpenAPI custom rule](https://www.youtube.com/watch?v=hLjzV-RmSno)
- [Getting ready to start your OpenAPI definition](https://www.youtube.com/watch?v=0ccz2lX4SpU)
- [OpenAPI help with path parameters](https://www.youtube.com/watch?v=AuJMFx_v6dY)
- [Set up Cognito and access controls for a Developer portal](https://www.youtube.com/watch?v=3LCeZsc-Z6o)


## Google Season of Docs 2021

This year, Redocly submitted a proposal for hiring technical writers to work on our open-source projects (Redoc and OpenAPI CLI), as part of Google's Season of Docs.

Redocly has hired 2 technical writers, [Sylwia Vargas](https://twitter.com/SylwiaVargas) and [Anton Zolotukhin](https://www.linkedin.com/in/bandantonio/) as part of the Google Season of Docs to work on its open-source tools, **Redoc** and **OpenAPI CLI**. We are excited to have them onboard and look forward to working with them.

Read more about the announcement at [Contribute to documenting Redocly's open-source tools](https://redocly.com/gsod/).

## Redocly at Evolution of TC 2021

Our Technical Writer Advocate will be sharing his experiences on *Documenting API Developer Portals* at the [Evolution of TC 2021](https://evolution-of-tc.com/program), which will be held online on June 9-11.
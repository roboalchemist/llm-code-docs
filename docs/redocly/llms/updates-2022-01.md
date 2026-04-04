# Source: https://redocly.com/blog/updates-2022-01.md

In the blink of an eye, January is over!

The holiday season didn't dampen the pace of enhancing our consumers' experience with our products. While we all enjoyed a well earned year-end break, there was still a lot of activity amongst the Redocly product teams.

Let's have a quick look at our new features, enhancements and documentation-related news from January 2022, and also some you may have missed from December 2021 (it was the holiday season, so we won't hold that against you!)

**Hot off the press!**

You're in for a treat: we revamped and published our brand new website yesterday. This new site has been fully redesigned to enhance your experience with our products, know more about our mission, read our technical docs, and of course get started on creating superior API docs.

Head over to [Redocly](https://redocly.com/) to check it out.

## Workflows

**Download proxy bundles for Apigee integration**

Enterprise customers can use the **Settings > API gateways** page to download Apigee X and Apigee Edge proxy bundles.

**Disable default URL setting**

Added an option to disable the default `redoc.ly` URL in the custom domain settings for Reference and Portal projects.

**Access Redocly compliance reports**

Using the newly added **Security** section under settings, you can access Redocly compliance reports and other documents related to the security of our services.

**Informative tooltips**

We've made tooltips more informative throughout the Workflows interface. Hovering over text like *Last updated ... ago* shows the exact date and time when the version or project was updated.

**Configure organization-level role privileges**

Customers on the Enterprise plan can configure organization-level role privileges. For more information, read the [role privileges](/docs-legacy/settings/role-privileges) topic.

**Edit environment variables**

You can now edit environment variables for API registry and portals. To find out how to do this, read our [environment variables settings](/docs-legacy/api-registry/settings/environment-variables) topic.

**Support for inline OIDC configuration**

Implemented support for inline OIDC configuration in the **Settings > Identity providers > OpenID Connect** dialog.

Organization owners can provide the configuration manually by selecting the *Insert configuration as JSON* option in the dialog.

**Access your billing history**

Organization owners now have access to the billing history. Use the **Settings > Billing** page to view details about your subscription and usage limits.

## API registry

**New format for API registry links**

The registry API uses a new format for *bundle* and *assets* links. The old format is deprecated, and we recommend switching to the new format.

Bundle links

```diff
- Old bundle link format
- https://api.test.org/registry/org/api/version/bundle/main/uuid/openapi.yaml
+ New bundle link format
+ https://api.test.org/registry/bundle/org/api/version/openapi.yaml?branch=main&job=uuid
```

Assets links

```diff
- Old asset link format
- https://api.test.org/registry/org/api/version/assets/markdown.md?branch_name=branchName
+ New asset link format
+ https://api.test.org/registry/assets/org/api/version/markdown.md?branch=branchName
```

**Link for copying folder assets**

The *Assets* page in the API registry shows the **Copy link** button for folder assets.

**Changelog**

Find out about other fixes and enhancements by visiting the [Workflows changelog](/docs-legacy/workflows/changelog).

![Workflow features](/assets/workflows.3eb9e6233ed54c01e56fbc7ef66291faa9ea4a94475d1521ff5f0bf3b04d92b3.978384e4.png)

## Reference docs

**Download button for `Try it`**

We added a nifty `Download` button to allow you to download any file that is returned as a response in the "Try it" console. If the response is not a file, but just plain text, you can always use the `Copy` button to copy the text.

**New theming option**

Our new theming option `backgroundColor` allows you to theme your request and response schema panels.

**New object description and configuration option**

We implemented object description for `oneOf/anyOf`, and added support for markdown syntax for the `oneOf/anyOf` objects.

If you want to hide this feature, you can also use the new config option `hideOneOfDescription`.

**Reference docs changelog**
Here's a link to the entire [Reference docs changelog](/docs-legacy/api-reference-docs/changelog).

![Reference docs features](/assets/refdocs.bbb0c598669f5fcc4ed106cf15eb57362166b4f9632eccc273e27c6fbb97101f.978384e4.png)

## Developer portal

**Use Google Optimize with your portal**
Added support for [Google Optimize](https://www.gatsbyjs.com/plugins/gatsby-plugin-google-marketing-platform/). To configure it for your portal, read more on the [Analytics page](/docs-legacy/developer-portal/configuration/siteconfig/analytics).

**Support for multiple sidebars**
We added support for multiple `sidebars.yaml` files and introduced a few changes to sidebar configuration in the portal. For more information, read the [migration guide](/docs-legacy/developer-portal/guides/migration-guide-sidebars).

**Developer portal changelog**
Read the entire list of fixes and enhancements on the [Developer portal changelog](/docs-legacy/developer-portal/changelog).

![Developer portal features](/assets/devportal.c653352a809d5345b0d11dc586e86f6da66f8e7357e54d2bc57a029b3709da8a.978384e4.png)

## OpenAPI CLI and Redoc

**OpenAPI CLI changelog**
Read more about OpenAPI CLI fixes and enhancements by visiting the [OpenAPI CLI changelog](/docs/cli/changelog).

**Redoc changelog**

To find out more about Redoc CLI fixes and enhancements, see the [Redoc changelog](https://github.com/Redocly/redoc/blob/master/CHANGELOG.md).

## Google Season of Docs 2021 - successfully completed!

As first-time participants, we had a really good experience with the Google Season of Docs for 2021. We published a [case study](/gsod-casestudy) to highlight our experience with the program.

Google announced a [list of successful projects](https://developers.google.com/season-of-docs/docs/participants) as part of the 2021 program.

## Documentation updates

It's never a dull moment with the documentation team at Redocly. While our product team is growing rapidly and adding some amazing new features, the tech writing team has been busy working with them to document and improve our developer experience.

Across December and January, we added new topics for:

- [Role privileges settings](/docs-legacy/settings/role-privileges)
- [Apigee instructions for mdx files](/docs-legacy/developer-portal/guides/apigee-integration-portal/overview)
- [Custom registry assets](/docs-legacy/api-registry/guides/view-download-assets)
- [Portal redirect guide](/docs-legacy/developer-portal/guides/redirects)
- [Environment variables settings](/docs-legacy/api-registry/settings/environment-variables)
- [Disable redoc.ly URL setting](/docs-legacy/api-reference-docs/settings/custom-domain)
- [Security reports](/docs-legacy/settings/security)


## Redocly now hiring documentarians!

While the developer team is growing quite rapidly, we are still on the lookout for a couple of documentation and developer experience professionals right now.

The technical writing team at Redocly has been pretty busy with some cool docs stuff, and are a great bunch of folks to work with.

If you are keen, or know someone who would be a good fit in the Redocly docs team, have a look at these roles and get in touch:

- [Technical Writer](https://redocly.com/careers/#technical-writer)
- [Developer Advocate](https://redocly.com/careers/#developer-advocate)
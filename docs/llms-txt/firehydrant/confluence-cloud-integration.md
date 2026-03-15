# Source: https://docs.firehydrant.com/docs/confluence-cloud-integration.md

# Confluence Cloud

FireHydrant can export incident retrospectives to Confluence, and you can flexibly configure the templated information posted to Confluence.

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions or the `manage_integrations` permission in FireHydrant to authorize and configure integrations
* You will also need a service account/user with Administrator privileges in Atlassian/Confluence Cloud.

> 📘 Note:
>
> FireHydrant recommends using a generic Confluence Cloud service account rather than an individual named user to avoid problems if the named employee were to depart the organization.
>
> The default authorized user configuring this integration will be the named "author" of the page that is created in Confluence.

## Installation

<Image alt="Confluence tile on the integrations page" align="center" width="650px" src="https://files.readme.io/e9ab93a-image.png">
  Confluence tile on the integrations page
</Image>

1. On FireHydrant, navigate to your [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for "confluence." Click the '+' on the tile.
2. On the next page, click **Authorize Application**. This will take you to the Atlassian login screen, or it will take you back to the integration page settings in FireHydrant if already logged in and approved.
3. From here, you can select which space you'd like FireHydrant to post into.

<Image alt="Selecting the space to post into" align="center" width="650px" src="https://files.readme.io/5c77939-image.png">
  Selecting the space to post into
</Image>

> 📘 Note:
>
> FireHydrant currently supports one target Atlassian org and one space within that org for Confluence. If you require multiple spaces or orgs, please submit this feedback to support.

## Uninstalling Confluence Cloud

To uninstall, navigate to the Confluence settings page via the integrations page, click the **Uninstall** tab, and then **Uninstall Confluence Cloud**.

Note that if you uninstall Confluence Cloud, this will not automatically remove any configured Confluence Runbook steps from your Runbooks, and those steps will simply fail upon execution.

## Next Steps

Now that you've installed Confluence:

* You're ready to set up a Runbook step to [Export Retrospective to Confluence](https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence)
* You can look into other Retrospective export integrations like [Google Docs](https://docs.firehydrant.com/docs/google-docs-integration)
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)
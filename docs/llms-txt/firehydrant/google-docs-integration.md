# Source: https://docs.firehydrant.com/docs/google-docs-integration.md

# Google Docs

FireHydrant supports retrospective data export to Google Docs.

## Prerequisites

* You must have [FireHydrant Owner access](/docs/role-based-feature-access-for-users-non-users-owners-members-and-collaborators)
* An existing Google workspace user\*

> 📘 \*Note:
>
> FireHydrant recommends configuring Google Docs with a Google service account that has permissions to access Drive rather than an individual named employee account. This helps avoid issues if an employee were to depart.

## Configuring the Integration

<Image alt="Google Docs tile on the integrations page" align="center" width="650px" src="https://files.readme.io/c0beba1-image.png">
  Google Docs tile on the integrations page
</Image>

1. Navigate to FireHydrant's [Integrations](https://app.firehydrant.io/organizations/integrations) page and search for the Google Docs tile. Click on the '+'.
2. On the next page, click **Authorize Application**.  If you're not logged in, this will take you to the Google authorization workflow. Otherwise, you will be asked to confirm the integration.

## Using Google Docs

Once you've set up the integration, you can automate exports [via the Runbook step](https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs).

> 📘 Note:
>
> Exported retrospectives are stored in a folder named FireHydrant Retrospectives at the Google Drive root of the user who authorized the integration.

### Rich Text Formatting

FireHydrant preserves rich text formatting (RTF) when exporting retrospectives to Google Docs, including:

* Text styling (bold, italic, underline)
* Lists (ordered and unordered)
* Headings and hierarchical structure
* Links and other formatting elements

This ensures that your retrospectives maintain their formatting and readability when exported from FireHydrant to Google Docs.

## Next Steps

* Learn more about [Retrospectives](https://docs.firehydrant.com/docs/incident-followup) on FireHydrant
* See how you can automate other steps of your Incident Management with [Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks)
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)
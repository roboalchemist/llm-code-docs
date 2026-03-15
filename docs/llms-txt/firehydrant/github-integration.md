# Source: https://docs.firehydrant.com/docs/github-integration.md

# GitHub

FireHydrant's GitHub integration allows you to track a change--from its origin in a pull request to its eventual impact on your system.

> 📘 Note:
>
> Currently FireHydrant supports connecting to one GitHub org.

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions in FireHydrant to configure integrations
* You will need admin permissions in your GitHub organization to install apps
* FireHydrant will need read access to checks, code, commit statuses, deployments, metadata, and pull requests. FireHydrant needs access to only whichever repositories you want linked with FireHydrant.

## Installing the GitHub integration

<Image alt="GitHub tile on the integrations page" align="center" width="650px" src="https://files.readme.io/28a316b-image.png">
  GitHub tile on the integrations page
</Image>

1. Navigate to FireHydrant's [Integrations](https://app.firehydrant.io/organizations/integrations) page located at **Settings> Integrations list** and search for the GitHub tile. Click the '+'.
2. On the next page, click **Authorize Application**. This will take you to the login page for GitHub, or the org selection page if already logged in.
3. On this page, click the GitHub organization you'd like to integrate FireHydrant with, and then either all repositories or only select repositories. Click **Install**.

## Linking services

After you install the GitHub app, you can link repositories with specific Services or Functionalities. This unlocks automatically logging merges into your main branch as [Change Events](https://docs.firehydrant.com/docs/change-events) for specific components in FireHydrant.

You can link in bulk by navigating to **Catalog** > **ervices | Functionalities]**\*\* > **Add functionality** > **Import from third party**, or you can link individual components by going to the specific component in FireHydrant, editing its settings, and then linking a repository from there:

<Image alt="Adding a repository link on a Service/Functionality's **Edit** page" align="center" width="400px" src="https://files.readme.io/4b9e341-image.png">
  Adding a repository link on a Service/Functionality's **Edit** page
</Image>

To learn more, visit [Import and Link Components](https://docs.firehydrant.com/docs/import-and-link-components). After importing or linking one or more services or functionalities from GitHub, the associated pull requests appear on the Change Events page as PRs are merged into your primary branch.

## Example of a change event

Whenever a pull request is merged to the primary branch in the repo, the change event will show:

* Name of PR and what time it occurred
* Labels for **base**, **source**, **merged\_by**, and **repository** from GitHub
* **Revision** and **branch** from GitHub
* Associated Services and Environments
* Associated Change Events
* Diff link to GitHub

Here's an example of what that looks like:

<Image alt="Example Change Event from a PR merge" align="center" width="650px" src="https://files.readme.io/bd223ce-image.png">
  Example Change Event from a PR merge
</Image>

## Next Steps

* Learn more about [Change Events](https://docs.firehydrant.com/docs/change-events) and how responders can more quickly identify breaking changes during incidents
* See how [the Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) takes your incident management to the next level with metrics and tying together teams and resources with their areas of ownership
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)
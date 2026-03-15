# Source: https://docs.firehydrant.com/docs/linear-integration.md

# Linear

FireHydrant's Linear integration allows you to create issues and link them to incidents and follow-ups on FireHydrant. Once you've configured Linear, you will be able to:

1. Automatically create Linear issues when incidents are declared in FireHydrant
2. Create Follow-up items in Linear from FireHydrant
3. Map additional fields from FireHydrant into Linear

## Prerequisites

* Ensure you have <Glossary>Owner</Glossary> permissions. Only users with the Owner role can manage integrations in FireHydrant.
* You'll need a **service account**/**user** with administrative permissions in Linear

> 📘 Note:
>
> FireHydrant will create and manage data as the user logged in to Linear during installation. FireHydrant recommends using a generic Linear service account rather than an individual named user to avoid problems if the named employee were to depart the organization.

## Installing the integration

1. Go to the [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for the Linear tile.

<Image alt="Settings > Integration List > Search 'linear'" align="center" width="650px" src="https://files.readme.io/0f7037c-CleanShot_2024-05-28_at_15.08.11.png">
  Settings > Integration List > Search 'linear'
</Image>

2. Once here, click the `[ + ]` button to kick off the OAuth flow between FireHydrant and Linear. You should see a screen that looks like this. If you need to switch which Linear workspace you're connecting, you can use the dropdown at the top left corner.

   <Image alt="FireHydrant permissions request" align="center" width="400px" src="https://files.readme.io/f3de7ab-CleanShot_2024-05-28_at_15.18.49.png">
     FireHydrant permissions request
   </Image>
3. Once you've authorized FireHydrant, you'll be returned to the integration page to see the new integration connected! 🙌

## Configuring projects

Once FireHydrant has been authorized to Linear, you'll need to add projects in FireHydrant to link with Teams in Linear. This tells FireHydrant which Team(s) to create issues in and other important information like issue type.

**This is a mandatory step for the integration to work.**

1. Click "+ Add project" near the bottom right on the Linear integration settings page.

   <Image alt="Adding a Linear project configuration" align="center" width="400px" src="https://files.readme.io/39be692-CleanShot_2024-05-28_at_15.22.41.png">
     Adding a Linear project configuration
   </Image>
2. Select which Team/project to map in the modal and "Add project."
3. On this next screen, you can map issue types and statuses for both incident tickets and Follow-ups.

<Image alt="Mapping milestones to Linear ticket status" align="center" width="650px" src="https://files.readme.io/1e62e6b39e1dad96e926ebda90037dfd22339af8e10eb6ab9ebf459430c3c484-CleanShot_2025-01-08_at_17.33.15.png">
  Mapping milestones to Linear ticket status
</Image>

## Next Steps

Now that you've configured Linear, it's time to use it in your incident management:

* Look at the [Create a Linear Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-linear-issue) Runbook step to see how you can automatically create a Linear issue for each incident
* [Create follow-up tickets in Linear](https://docs.firehydrant.com/docs/managing-follow-ups) so you can schedule and prioritize work uncovered during incidents
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)
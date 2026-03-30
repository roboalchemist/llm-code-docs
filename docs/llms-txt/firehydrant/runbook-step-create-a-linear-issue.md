# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-linear-issue.md

# Create a Linear Issue

<Image alt="Create a Linear issue step" align="center" width="650px" src="https://files.readme.io/1ac0850-CleanShot_2024-05-28_at_16.04.31.png">
  Create a Linear issue step
</Image>

Our [Linear](https://docs.firehydrant.com/docs/linear-integration) integration allows the creation of Linear issues directly from FireHydrant. This Runbook step is for creating FireHydrant incident tickets as Linear issues. For creating Follow-ups, visit [Managing Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups).

> 📘 Note:
>
> Currently, FireHydrant only allows one top-level Linear issue per FireHydrant incident.

## Prerequisites

You must have the [Linear integration](https://docs.firehydrant.com/docs/linear-integration) and at least one project/Team configured to create issues.

## Adding the step

1. To add the step, edit a Runbook or create a new one, click "+ Add step," and search for Linear.

   <Image alt="Searching for Linear from the list of available steps" align="center" width="650px" src="https://files.readme.io/c2f9c18-CleanShot_2024-05-28_at_16.07.24.png">
     Searching for Linear from the list of available steps
   </Image>
2. On the step configuration page, you'll fill in the fields for this step in your Runbook:
   1. **Name**: A name for this step. This is how it will appear on the executed Runbook steps list during an incident.
   2. **Linear Team**: The Linear Team you'd like to create the incident ticket/issue in. If you don't see any options here, make sure you've gone through steps to [configure a Linear Team/project](https://docs.firehydrant.com/docs/linear-integration) on the installation page.
   3. **Ticket Summary**: The name of the ticket\*\*
   4. **Ticket Description**: A longer description for the ticket\*\*
   5. **Assign Ticket to a Role**: You can optionally assign this issue in Linear to whoever is assigned to a specific [Incident role](https://docs.firehydrant.com/docs/incident-roles) in FireHydrant. We attempt to match users by using email addresses, so ensure the user's email address in Linear matches their address in FireHydrant.

\*\*These two fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables), which allows you to use incident data/parameters dynamically at runtime (for example, the incident's name).
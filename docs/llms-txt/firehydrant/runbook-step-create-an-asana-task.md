# Source: https://docs.firehydrant.com/docs/runbook-step-create-an-asana-task.md

# Create an Asana Task

<Image alt="Create an Asana Task step" align="center" width="650px" src="https://files.readme.io/f47a1a4-image.png">
  Create an Asana Task step
</Image>

Our [Asana](https://docs.firehydrant.com/docs/asana-integration)integration allows teams to ensure your incident management process is consistent with their project management setup. It's common for teams to create an Asana task from a FireHydrant Runbook when an incident is declared, for example.

When you create an overarching incident task in Asana, any created [Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups) in Asana will automatically be linked to this parent task.

> 📘 Note:
>
> Currently, FireHydrant only allows one top-level incident Asana task per FireHydrant incident.

## Prerequisites

You must have the [Asana](https://docs.firehydrant.com/docs/asana-integration) integration installed and at least one project configured to create tasks.

## Adding the step

1. To add the step, edit a Runbook or create a new one, click "+ Add step", and search for Asana and click on it.

<Image alt="Create Asana tickets from Runbook step" align="center" width="650px" src="https://files.readme.io/1b2d710-image.png">
  Create Asana tickets from Runbook step
</Image>

2. Select the project you want to create the task in
3. Fill in the **Task Summary** and **Description**. These two fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables), which allows you to use incident data/parameters dynamically, for example, the name of the incident.
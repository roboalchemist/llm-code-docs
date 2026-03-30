# Source: https://docs.edgeimpulse.com/studio/organizations/data-campaigns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data campaigns

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

The "data campaigns" feature allows you to quickly track your experiments and your models' development progresses. It is an overview of your pipelines where you can easily extract useful information from your datasets and correlate those metrics with your model performances.

It has been primarily designed to follow clinical research data processes. In August 2023, we released this feature for every enterprise user as we see value in being able to track metrics between your datasets and your projects.

<Frame caption="Data campaigns overview">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-campaigns.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=ba0c0477f71741a8b2e2fe89b2ba8adc" width="1600" height="520" data-path=".assets/images/studio-data-campaigns.png" />
</Frame>

## Setting up your dashboard

To get started, navigate to the **Data campaigns** tab in your organization:

<Frame caption="Data campaigns">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-campaigns-empty.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=381ec0efb5e4ce3d366985e1961f3881" width="1600" height="667" data-path=".assets/images/studio-data-campaigns-empty.png" />
</Frame>

Click on **+ Create new dashboard**.

Give your dashboard a name, and select one or more collaborators to receive the daily updates by email. If you don't want to be spammed, you can select when you want to receive these updates, either *Always*, *On new data, changes or on error*, or *Never*. Finally, set the last number of days shown in the graphs:

<Frame caption="Add data campaign dashboard">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-campaigns-add-dashboard.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=20f2a5512171a1ad0f4cfa090a0e3267" width="1600" height="891" data-path=".assets/images/studio-data-campaigns-add-dashboard.png" />
</Frame>

You can create as many dashboards as needed, simply click on **+ Create a new dashboard** from the dropdown available under your current dashboard:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-campaign-create-second-dashboard.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=422131a8a9e6c4dfa9185c126a8a8d6b" width="1356" height="984" data-path=".assets/images/data-campaign-create-second-dashboard.png" />
</Frame>

If you want to delete a dashboard, Click on **Actions...** -> **Delete dashboard**

## Setting up your campaign

Once your dashboard is created, you can add your custom campaigns. It's where you will specify which metrics are important to you and your use case. Click on **Actions...** -> **Add campaign**

<Frame caption="Add data campaign">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-campaigns-add-campaign.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=b507b70d8e671db35335e9e634c16bce" width="1600" height="562" data-path=".assets/images/studio-data-campaigns-add-campaign.png" />
</Frame>

Fill the form to create your campaign:

**Name**: Name of your data campaign.

**Description**: Description of your data campaign.

**Campaign coordinators**: Add the collaborators that are engaged with this campaign

**Datasets**: Select the datasets you want to visualize in your campaign. You can add several datasets.

**Projects**: Select the projects you want to visualize in your campaign.
You can add several projects.

**Pipelines**: Select the pipeline that is associated with your campaign.
*Note that this is for reference only, it is currently not displayed in your campaign*

**Links**: Select between the link type you need. Options are Github, Spreadsheet, Text Document, Code repository, List or Folder.
Add a name and the link. This place is useful for other collaborators to have all the needed information about your project, gathered in one place under your campaign.

**Addition queries to track**:
These queries are data filters that need to be written in the SQL WHERE format. See [Querying data](/knowledge/guides/reference-designs/health-reference-design/querying-clinical-data) for more information.
For example `metadata->`age >= 18\` will return the data samples from adult patients.

You can then save your data campaign and it will be added to your dashboard:

<Frame caption="Create or edit data campaign">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-campaigns-edit-campaign.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=5b2dd7360f084d0af925da89008d0de2" width="1600" height="897" data-path=".assets/images/studio-data-campaigns-edit-campaign.png" />
</Frame>

This dashboard shows the metrics' progress from the [Health reference design data](/knowledge/guides/reference-designs/health-reference-design)

<Frame caption="Create or edit data campaign">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-campaigns-overview.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=a215527c5f06297b8b2e078b57da984d" width="1600" height="454" data-path=".assets/images/studio-data-campaigns-overview.png" />
</Frame>

If you want to edit or delete your campaign, click on the "**⋮**" button on the right side of your campaign:

<Frame caption="Edit campaign">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-campaigns-edit-campaign.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=0321ba71a1b6bc5acd10bfcb6061eec9" width="1600" height="505" data-path=".assets/images/data-campaigns-edit-campaign.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
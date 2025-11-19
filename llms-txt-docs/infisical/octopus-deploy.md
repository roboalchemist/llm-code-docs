# Source: https://infisical.com/docs/integrations/cicd/octopus-deploy.md

# Octopus Deploy

> Learn how to sync secrets from Infisical to Octopus Deploy

Prerequisites:

* Set up and add secrets to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Create a Service Account for Infisical in Octopus Deploy">
    Navigate to **Configuration** > **Users** and click on the **Create Service Account** button.

        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-user-settings.png"
          alt="integrations octopus deploy
    users"
        />

    Fill out the required fields and click on the **Save** button.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-create-service-account.png" alt="integrations octopus deploy service
    account" />
  </Step>

  <Step title="Generate an API Key for your Service Account">
    On the **Service Account** user page, expand the **API Keys** section and click on the **New API Key** button.

        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-create-api-key.png"
          alt="integrations octopus deploy
    new api key"
        />

    Fill out the required fields and click on the **Generate New** button.

        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-generate-api-key.png"
          alt="integrations octopus deploy
    generate api key"
        />

    <Note>If you configure your access token to expire,
    you will need to generate a new API key for Infisical prior to this date to keep your integration running.</Note>

    Copy the generated **API Key** and click on the **Close** button.

        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-copy-api-key.png"
          alt="integrations octopus deploy
    copy api key"
        />
  </Step>

  <Step title="Create a Service Accounts Team and assign your Service Account">
    <Note>You can skip creating a new team if you already have an Octopus Deploy team configured with
    the **Project Contributor** role to assign your Service Account to.</Note>

    Navigate to **Configuration** > **Teams** and click on the **Add Team** button.

        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-team-settings.png"
          alt="integrations octopus deploy
    teams"
        />

    Create a new team for **Service Accounts** and click on the **Save** button.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-create-team.png" alt="integrations octopus deploy add
    team" />

    On the **Members** tab, click on the **Add Member** button, add your **Infisical Service Account** and click on the **Add** button.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-add-to-team.png" alt="integrations octopus deploy add service account to team" />

    On the **User Roles** tab, click on the **Include User Role** button, and add the **Project Contributor** role. Optionally,
    click on the **Define Scope** button to further refine what projects your Service Account has access to. Click on the **Apply** button once complete.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-add-role.png" alt="integrations octopus deploy add user roles to team" />

    Save your team changes by clicking on the **Save** button.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-save-team.png" alt="integrations octopus deploy save team changes" />
  </Step>

  <Step title="Setup Integration">
    In Infisical, navigate to your **Project** > **Integrations** page and select the **Octopus Deploy** integration.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-integrations.png" alt="integration octopus deploy" />

    Enter your **Instance URL** and **API Key** from **Octopus Deploy** to authorize Infisical.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-authorize.png" alt="integration octopus deploy" />

    Select a **Space** and **Project** from **Octopus Deploy** to sync secrets to; configuring additional **Scope Values** as needed. Click on the **Create Integration** button once configured.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-create.png" alt="integration octopus deploy" />

    Your Infisical secrets will begin to sync to **Octopus Deploy**.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/octopus-deploy/integrations-octopus-deploy-sync.png" alt="integration octopus deploy" />
  </Step>
</Steps>

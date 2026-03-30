# Source: https://pipedream.com/docs/apps/integrated-apps/google-workspace-admin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Workspace Admin

<Note>
  Since this Google Workspace Admin app needs to access your sensitive data, **you need to manually allow Pipedream to access your Google Workspace Admin API**.

  Please follow the steps below
</Note>

<Steps>
  <Step title="Navigate to App Access Control">
    Access your [Google Workspace Admin Console > Security > API Controls > App Access Control](https://admin.google.com/ac/owl/list?tab=configuredApps)
  </Step>

  <Step title="Add a New App">
    Click **Configure new app**.
  </Step>

  <Step title="Search for Pipedream's Client ID">
    In the search box that appears, search the following Client ID for Pipedream:

    ```text  theme={null}
    516759972233-moq227c92qubo5fd452kd52m3lddgkofd.apps.googleusercontent.com
    ```
  </Step>

  <Step title="Select the App">
    The Pipedream app will appear. Select it and click **Select**.
  </Step>

  <Step title="Confirm the Selection">
    Check the box for the Client ID you just added, and then click **Select** again.
  </Step>

  <Step title="Configure Scope">
    Allow either all users in your company or specific org units

    Then click **Continue**.
  </Step>

  <Step title="Configure Access">
    Choose the option **Trusted** or **Specific Google data** and click **Continue**.
  </Step>

  <Step title="Review and Finish">
    Review your configuration and click **Finish**
  </Step>
</Steps>

Built with [Mintlify](https://mintlify.com).

# Source: https://infisical.com/docs/integrations/app-connections/dns-made-easy.md

# DNS Made Easy

> Learn how to configure a DNS Made Easy Connection for Infisical.

Infisical supports connecting to DNS Made Easy using API key and secret key for secure access to your DNS Made Easy service.

## Configure API key and secret Key for Infisical

<Steps>
  <Step title="Generate API key and secret key">
    Navigate to your DNS Made Easy dashboard and go to **Account Information** under the **Config** top menu.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/dns-made-easy/nav-to-account-info.png" alt="Navigate to Account Information" />

    If your **API Key** and **Secret Key** are already available, proceed to step 2.

    Otherwise, check the **Generate New API Credentials** then click the **Save** button to generate the new API credentials.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/dns-made-easy/generate-new-api-credentials.png" alt="Generate API Credentials" />
  </Step>

  <Step title="Copy Your API Key and Secret Key">
    After creation, copy your API key and secret key.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/dns-made-easy/copy-api-credentials.png" alt="Generated API Token" />

    <Warning>
      Keep your API key and secret key secure and do not share it.
      Anyone with access to this token can manage your DNS Made Easy resources.
    </Warning>
  </Step>
</Steps>

## Setup DNS Made Easy Connection in Infisical

<Steps>
  <Step title="Navigate to App Connections">
    Navigate to the **App Connections** page in the desired project. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App
    Connections Tab" />
  </Step>

  <Step title="Add Connection">
    Select the **DNS Made Easy Connection** option from the connection options
    modal. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/dns-made-easy/dns-made-easy-app-connection-select.png" alt="Select DNS Made Easy
    Connection" />
  </Step>

  <Step title="Input Credentials">
    Enter your DNS Made Easy API key and secret key in the provided fields and
    click **Connect to DNS Made Easy** to establish the connection. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/dns-made-easy/dns-made-easy-app-connection-form.png" alt="Connect to
    DNS Made
    Easy" />
  </Step>

  <Step title="Connection Created">
    Your **DNS Made Easy Connection** is now available for use in your Infisical
    projects. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/dns-made-easy/dns-made-easy-app-connection-created.png" alt="DNS Made Easy Connection
    Created" />
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://infisical.com/docs/llms.txt
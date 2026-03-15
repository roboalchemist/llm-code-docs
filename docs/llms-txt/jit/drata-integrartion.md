# Source: https://docs.jit.io/docs/drata-integrartion.md

# Drata Integration

# Overview

> 📘 Note
>
> The Drata integration is currently enabled by the Jit team.\
> Self-service configuration will be available in a future release.

Integrating with Drata enables you to:

* Automate evidence submission for key technical SOC2 controls to the Drata platform.\
  Learn more in [SOC2 by Drata](https://docs.jit.io/docs/soc2-by-drata).

# Integration steps

* Step 1 (Classic Drata UI): Create an API token in your Drata account.
* Step 1 (New Drata UI): Create an API token in your Drata account.
* Step 2: Assign and create secrets and tokens in Jit.
* Step 3: Configure the integration in Jit.

## Step 1 (Classic Drata UI): Create an API Token in Your Drata Account

1. Log in to <https://app.drata.com> > Click on your profile name > `Settings`.
2.

[block:image]{"images":[{"image":["https://files.readme.io/4bc5f75-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

Click `API Keys`.
3\.
[block:image]{"images":[{"image":["https://files.readme.io/a6a6c4f-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

Click `Create API Key`.
4\.
[block:image]{"images":[{"image":["https://files.readme.io/4786c16-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

Fill out the Create API Key Form using the guidance below and be sure to save it:
5\. - **Expiration Date**: We recommend a long expiration date so that your integration does not unexpectedly stop working.

* The following scopes must be enabled:
  * *Personnel: Personnel details - R*
  * *Controls: Control List - R*
  * *Workspaces: List workspaces - R*
  * *Evidence Library:List Evidence - R,Add Evidence- W, Update Evidence - W, Delete Evidence - W*

6.

[block:image]{"images":[{"image":["https://files.readme.io/fc0354f-image.png",null,""],"align":"center","sizing":"600px"}]}[/block]

[block:image]{"images":[{"image":["https://files.readme.io/d64ff7d-image.png",null,""],"align":"center","sizing":"600px"}]}[/block]

[block:image]{"images":[{"image":["https://files.readme.io/33c7422-image.png",null,""],"align":"center","sizing":"600px"}]}[/block]

[block:image]{"images":[{"image":["https://files.readme.io/d0d8f4677f561bab612b8beb0aaa8d02ee79768b8f9eb26719393827529c3350-image.png",null,""],"align":"center","sizing":"600px"}]}[/block]

Copy the API Key and save it somewhere secure!

## Step 1 (New Drata UI): Create an API Token in Your Drata Account

1. Log in to <https://app.drata.com> > Click on `Settings`> `API Keys`

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/71dac7a5c6f78139ab47fb407685b562807d48f0f104600bc3a3c4c4ebf3df6e-image_26.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "300px"
    }
  ]
}
[/block]

2. Click `Create API Key`

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/db0b48f82341ba7312c5103b477d2b235ede66756c370fe871025cf26489b755-image_27.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "800px"
    }
  ]
}
[/block]

<br />

3. Fill out the Create API Key Form using the guidance below, and be sure to save it:
4. * **Expiration Date**: We recommend a long expiration date so that your integration does not unexpectedly stop working.
   * The following scopes must be enabled:
     * Personnel: Get Personnel - Read
     * Controls: Control List - Read
     * Workspaces: List workspaces - Read
     * Evidence Library:
       * List Evidence - Read
       * Create Evidence- Write
       * Update Evidence - Write
       * Delete Evidence - Write
5. Copy the API Key and save it somewhere secure!

## Step 2: Assign and create secrets and tokens in Jit

1. Create a secret for the Drata API key:
   1. In the **Jit platform**, go to **Settings > Secrets**.
   2. Click on **Create new secret**, and create a secret named `DRATA_API_KEY` and add the Drata API Key you've just created.
2. Create a Jit API Token:

   1. Click on **Settings > Users & Permissions**.
   2. Click on **API Token > Generate Token**.
   3. ![](https://files.readme.io/0895227-image.png)

      Create a new Key, give it a meaningful description, and select a `developer` Role.
   4. Copy both the `Client ID` and `Secret Key` to a secret location.
3. Store these back to the Jit secrets, go back to **Settings > Secrets**:
   1. Click on **Create new secret**, and create a secret named `JIT_CLIENT_ID` and add the Jit `Client ID` you just created.
   2. Click on **Create new secret**, and create a secret named `JIT_CLIENT_SECRET` and add the Jit `Secret Key` you just created.
4. Make sure the names are as described for the integration to work properly.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39fd706-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "600px"
    }
  ]
}
[/block]

## Step 3: Enable the Drata integration in Jit

> 📘 Enable the Drata integration in Jit
>
> Jit currently does not support self-service configuration of the Drata integration.
>
> To complete the integration, the Jit team will enable the Drata evidence sync for you.

1. Complete Steps 1 and 2 above.
2. Contact Jit support and provide:
   * Your **Drata workspace name**
   * The **email address** associated with your Drata account
   * Confirmation that the Drata API token has been created

Once enabled, Jit will start syncing evidence to Drata automatically.

### How to find your Drata workspace name and email

**Drata workspace name**

If workspaces are enabled:

* Go to Drata, then select Settings > Company Info.

* Scroll down to Workspaces section and copy the name of the workspace you want to send evidence to.

  If workspaces are not enabled:

* Go to Drata, then select Settings > Company Info.

* Copy the Project Name.

**Drata account email**

* Enter the email address of the Drata user who created the API key.

## Step 4: Enable Drata in your security plans

After the Drata integration has been enabled by the Jit team, you can use it in your security plans.

Enabling Drata in a security plan allows Jit to associate findings and controls with Drata for compliance context and reporting.

Jit will now periodically send the Jit report to your Drata workspace, according to your [SOC2 by Drata plan](https://docs.jit.io/docs/soc2-by-drata).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/468772202bfc8a7fe19ee1f9827b4d4ab64d5eedd391d226385bb530ce2a227f-Screenshot_2025-05-12_at_12.26.41.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7ea9adee119869c05fd23317833ed7877ca3a48023be8ec6c7b3eb2a4d003fab-Screenshot_2025-05-12_at_12.26.51.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]
# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/invicti.md

# Invicti

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

You can connect OX to your Invicti instance to import Dynamic Application Security Testing (DAST) results. This allows you to view DAST issues alongside other security findings in the OX Security platform.

Integrating Invicti with OX provides you with unified view of vulnerabilities across your application stack. OX automatically pulls Invicti DAST scan results and displays them in the Active Issues page.

> **Notes:**
>
> * Some advanced Invicti capabilities, such as automatic crawling of subdomains, depend on your Invicti configuration and may affect what data is shown in OX.
> * The Invicti connector does not support automatic discovery of credentials from the Invicti UI. You must obtain the required credentials manually.
> * If your Invicti instance requires a token instead of a username and password, consult your Invicti administrator.

## Step 1: Get an Invicti API token \[Invicti]

1. Log in to **Invicti Enterprise**.
2. Select **\[Your Name]** (top right) > **API Settings**.
3. If prompted, enter your **Current password**.
4. To display your **User ID** and **API token**, select **Submit** .
5. Copy the token and store it in a secure location.

{% hint style="info" %}
If your organization uses Single Sign-On (SSO), the **API Settings** page may open without a password prompt. If SSO is enabled but you’re still prompted for a password, go to **Settings > Single Sign-On** and select **Enforce to authenticate only with single sign-on**.
{% endhint %}

## Step 2: Connect Invicti to OX \[OX]

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **Invicti**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-66859245dfb8efc3d04ea0e7dc618c1acf116f2b%2FInvicti_connect.png?alt=media" alt="" width="362"><figcaption></figcaption></figure>

1. In the **Configure your Invicti credentials** box, provide the following details:

| Field            | Description                                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------------------- |
| Invicti host URL | Use the base URL of your Invicti instance: [https://www.netsparkercloud.com](https://www.netsparkercloud.com/) |
| User Name        | Your Invicti username.                                                                                         |
| Password         | Your Invicti password.                                                                                         |

1. Select **CONNECT**.
2. To select specific Invicti projects to import, click the gear icon next to the **DELETE** button.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b7b3ba10314c29db54c380bda3f342616a498767%2Fselect%20projects.png?alt=media" alt="" width="263"><figcaption></figcaption></figure>

1. Select the Invicti projects and select **SAVE**.

When connected, OX starts pulling DAST data from Invicti.

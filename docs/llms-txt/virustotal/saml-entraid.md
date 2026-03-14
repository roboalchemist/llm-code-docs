# Source: https://virustotal.readme.io/docs/saml-entraid.md

# Configure SAML with Entra ID

You can configure VirusTotal to use SAML with Microsoft EntraID. These are the recommended steps for this set-up.

# Configuring the Entra ID Application

## 1. Entra ID application

In your Azure portal, search for Enterprise Applications.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_enterprise_applications_20250527.png",
        null,
        "Azure Enterprise Applications"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

Press the "Create a new application" button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_new_application_20250527.png",
        null,
        "Create new application on Entra ID"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

## 2. Application configuration

Provide a name to the new application (as an example, **VirusTotalSSO**).

Select the "Integrate any other application you don’t find in the gallery (Non-gallery)" option.

Press the "Create" button at the bottom in order to create the instance of the new application.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_app_configuration_20250527.png",
        null,
        "Configure application on Entra ID"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

## 3. Single sign on setup

On the "Overview" tab of the new application, press the "Set up single sign on" button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_setup_sso_20250527.png",
        null,
        "Set up Single Sign on"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

Select the "SAML" option.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_saml_option_20250527.png",
        null,
        "Single sign on methods"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

## 4. SAML configuration

On the SAML setup, select "Basic SAML configuration" and press "Edit" button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_basic_saml_configuration_20250527.png",
        null,
        "Basic SAML configuration"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

Press "Add identifier" in order to configure the **Entity ID**. The **Entity ID** must be the same as the **Audience** in the VirusTotal SAML configuration on the group page. Choose a unique string as an example, **VirusTotal\_group\_id\_SSO**.

Press "Add reply URL" in order to configure the **Reply URL**. The **Reply URL** must be `https://virustotalcloud.firebaseapp.com/__/auth/handler`.

Press "Save" in order to save the changes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_saml_params_20250527.png",
        null,
        "Saved options"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

> ⚠️
>
> Note that both **Entity ID** and **Reply URL** are mandatory.

## 4. Required data

> ℹ️
>
> Check those fields on the image at the bottom of the section.

### SAML certificate

Download the certificate from the "SAML Certificate" section.

> ⚠️
>
> Use the base64 format to download the certificate.

### Login URL

Copy the **Login URL** from the section 4: "Setup VirusTotalSSO" section.

### Azure AD identifier

Copy the **Azure AD Identifier** from the section 4: "Setup VirusTotalSSO".

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_get_data_20250527.png",
        null,
        "Parameters to be used on the VirusTotal group settings page"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

# Configuring the SSO in VirusTotal

## 1. Group settings page

Open your group settings page: `https://www.virustotal.com/gui/group/<group_id>/settings`

> ℹ️
>
> Note that only Group admin are able to see the settings page.

On "Single sign-on" section select the **Other (SAML)** option in "Identity provider" dropdown.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_vt_samls_20250514.png",
        null,
        "Available SSO options"
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

> ⚠️
>
> Do **NOT** enable the "All my group users must mandatorily sign in using this identity provider" until you've fully confirmed your SAML configuration is working and your organization can successfully sign in.
> Enabling this setting with an incorrect configuration could lock all your users out of the platform.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_vt_selected_provider_20250514.png",
        null,
        "Enforce SAML checkbox"
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

## 2. Required fields

Include the information provided by the Azure application on the different fields:

### Identity provider issuer

Add the **Azure AD identifier** provided in [step 4: Required data](#required-data).

### Identity provider single sign-on URL

Add the **Login URL** provided in [step 4: Required data](#required-data).

### Audience

Add the **Entity ID** used on [step 3: Configure SAML](#configure-saml). In our example, the value "VirusTotal\_group\_id\_SSO".

### X.509 certificate

Add the content of the downloaded certificate in [step 4: Required data](#required-data).

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_vt_fields_20251119.png",
        null,
        "Fields on group settings page"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

Save your SSO settings to activate SAML.

## 3. Sign-in URL

The **Sign-in URL** will appear once the settings are saved.

> ℹ️
>
> Share this **Sign-in URL** with your group members so they can authenticate on the platform using SSO.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/entraid_vt_signing_url_20250527.png",
        null,
        "Sign in URL"
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

# Manage user access to VirusTotal on Entra ID platform

Open the application you previously created within Entra ID.

Navigate to the "Users and Groups" section. Here, you can manage which users will have access to the VirusTotal platform via SSO.

> ℹ️
>
> Once you've confirmed that everything is working correctly, you can enforce SSO authentication for your group selecting the "All my group users must mandatorily sign in using this identity provider" option on the group settings page.
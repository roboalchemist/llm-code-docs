# Source: https://virustotal.readme.io/docs/saml-okta.md

# Configure SAML with Okta

# Set up

You can configure VirusTotal to use SAML with Okta. These are the recommended steps for this set-up:

## 1. Okta Admin Panel

In the Okta Admin Panel, go to the Applications tab:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_adminpanel_20231026.png",
        null,
        "Okta Administration Panel"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 2. Applications tab

In the Applications tab, click on “Create App Integration”

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_createapp_20231026.png",
        null,
        "Okta Create APP"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 3. Select “SAML 2.0”

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_createappsaml_20231026.png",
        null,
        "Okta Create APP choose SAML"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 4. Provide an app name and a logo

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_generalsettings_20231026.png",
        null,
        "Okta General Settings"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 5. Fill in the fields

Fill the following fields with the following information:
\* **Single sign on URL:**
<https://virustotalcloud.firebaseapp.com/__/auth/handler>
\* **Audience URI:** You can use any string you want as “Audience URI” as long as it's exactly the same in VirusTotal and in Okta. Alternatively, you can also introduce the Single sign on URL mentioned above
\* **Name ID:** “EmailAddress”
\* **Application username:** “Email”
\* Leave all other fields with their default values:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_ssourl_20231026.png",
        null,
        "Okta SSO URL"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 6. Configuration is finished. View Setup Instructions

Once your configuration is finished, this is how your configuration should look. Click on the “View Setup Instructions” button:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_setupinstructions_20231026.png",
        null,
        "Okta Setup Instructions"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 7. Overview

You should see something like this:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_details_20231026.png",
        null,
        "Okta "
      ],
      "align": "center"
    }
  ]
}
[/block]

## 8. Copy data in VirusTotal

Copy those values in your VirusTotal’s group configuration available at <https://www.virustotal.com/gui/group/GROUP_NAME/settings> and click on Save SSO data:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_vtgroupsettings_20231026.png",
        null,
        "Okta VT group settings"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 9. Copy the VirusTotal sign-in URL

Copy the URL at the “VirusTotal sign-in URL” section and use it to configure a bookmark app that will launch the sign-in process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_copyurl_20231026.png",
        null,
        "Okta Copy URL"
      ],
      "align": "center"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_addbookmark_20231026.png",
        null,
        "Okta Add Bookmark"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 10. Bookmark app

Your users must use the bookmark app to login into VirusTotal. Make sure the SAML app is hidden for them.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/okta_hideicon_20231026.png",
        null,
        "Okta Hide Icon"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Troubleshooting

This section aims to provide steps to solve the most common issues when setting up a SAML configuration.

* *Unable to Process request due to missing initial state. This may happen if browser sessionStorage is inaccessible or accidentally cleared*: Check the reply URL is configured correctly on your IdP configuration.

* *Pop up blocked*: The signin dialog opens in a popup, so you need to explicitly allow virustotal.com to open popups.

* *Response <Issuer> mismatch*: the field "identity provider issuer" must be an URL to your SAML provider.

* *Error: app\_not\_configured\_for\_user*: Specifically when configuring SAML using Google Workspace. This error occurs when attempting to log into signin.blackbaud.com using a BBID enabled Google account while another Google account is already signed in in the browser

* *User is not assigned to this application.*: Contact your group administrators so they can add you to the user list on Okta.

If you still need assistance, [contact our support team](https://www.virustotal.com/gui/contact-us/technical-support) attaching the SAML XML configuration.
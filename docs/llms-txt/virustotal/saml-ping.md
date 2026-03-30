# Source: https://virustotal.readme.io/docs/saml-ping.md

# Configure SAML with Ping

# Set up

## 1. Create app

In the Ping Identity dashboard, go to applications and create a new application by clicking on the "+" icon in the upper part of the application.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/saml_ping_1.png",
        null,
        "PingIdentity dashboard"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 2. Configure app

Fill the necessary data, select "SAML" as application type and finally click on "Configure":

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/saml_ping_2.png",
        null,
        "Create SAML app"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 3. ACS URL and audience

Fill the ACS URL (which is `https://virustotalcloud.firebaseapp.com/__/auth/handler`) and the entity ID (which will be used as audience in the VirusTotal config). The entity ID must be unique so make sure not to use a generic string such as "test" or "example". After that click on "Save".

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/saml_ping_3.png",
        null,
        "ACS URL and audience"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 4. Retrieve app data

Enable the app and retrieve the necessary data required on the VirusTotal configuration: the certificate, issuer ID and SSO URL:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/saml_ping_4.png",
        null,
        "Certificate, issuer ID and SSO URL"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 5. VirusTotal configuration

Fill this data in the VirusTotal configuration:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/saml_ping_5.png",
        null,
        "VT configuration"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 6. Attribute mappings

Edit the attribute mappings to use email instead of user ID. To do so, go back to the PingIdentity dashboard and click on the "Attribute mappings" tab. Click on the "edit" button highlighted in the following screenshot:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/account-management/saml_ping_6.png",
        null,
        "Correct attribute mappings"
      ],
      "align": "center"
    }
  ]
}
[/block]

## 7. Login URL

Share the login URL with your users to login in VirusTotal.
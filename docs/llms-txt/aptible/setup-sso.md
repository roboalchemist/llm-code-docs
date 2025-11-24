# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/setup-sso.md

# How to set up Single Sign On (SSO)

> To use SSO, you must configure both the SSO provider and Aptible with metadata related to the SAML protocol. This documentation covers the process in general terms applicable to any SSO provider. Then, it covers in detail the setup process in Okta.

## Generic SSO Provider Configuration

To set up the SSO provider, it needs the following four pieces of information unique to Aptible. The values for each are available in your Organization's Single Sign On the settings page, accessible only by [Account Owners](/core-concepts/security-compliance/access-permissions), if you do not yet have SSO configured.

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=069d095b0162f81621986c136918f019" alt="" data-og-width="2100" width="2100" data-og-height="1324" height="1324" data-path="images/sso1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7fb84e102f90404940d62d14d5e0b6f5 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=bf47a62180f8819f6e1511e19bfb3dee 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c114a4dfdcf914ebddd56af0400892f4 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=2f501e0493770b488aa6ef83aab27855 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=43f52df965c729e3655cddb6cfdd64cc 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso1.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5ed9f319c6b77e2878dd90c53f00e593 2500w" />

You should reference your SSO Provider's walkthrough for setting up a SAML application alongside this documentation.

* [Okta](https://developer.okta.com/docs/guides/saml-application-setup/overview/)

* [Google GSuite](https://support.google.com/a/answer/6087519)

* [Auth0 (Aptible Guide)](/how-to-guides/platform-guides/setup-sso-auth0)

## Single Sign On URL

The SAML protocol relies on a series of redirects to pass information back and forth between the SSO provider and Aptible. The SSO provider needs the Aptible URLs set ahead of time to securely complete this process. This URL is also called the Assertion Consumer Service (ACS) or SAML Consume URL by some providers.

Google uses the term `SSO URL` to refer to the redirect URL on their server. This value is called the `ACS URL` in their guide.

This is the first URL provided on the Aptible settings page. It should end in `saml/consume`.

## Audience URI

This is a unique identifier used by the SSO provider to match incoming login requests to your specific account with them. This may also be referred to as the Service Provider (SP) Entity ID.

Google uses the term `Entity ID` to refer to this value in its guide.

This is the second value on the Aptible information page. It should end in `saml/metadata`

> 📘 This URL provides all the metadata needed by an SSO provider to setup SAML for your account with Aptible. If your SSO provider, has an option to use this metadata, you can provide this URL to automate setup. Neither Okta nor Google allow for setup this way.

## Name ID Format

SAML requires a special "name" field that uniquely identifies the same user in both the SSO Provider and Aptible. Aptible requires that this field be the user's email address. That is how users are uniquely identified in our system.

There are several standard formats for this field. If your SSO supports the `EmailAddress`, `emailAddress`, or `Email` formats, one of which should be selected. If not, the `Unspecified` format, should be used. If none of those are available, `Persistent` format is also acceptable.

Some SSO providers do not require manual setting of the Name ID format and will automatically assign one based on the attribute selected in the next step.

## Application Attribute or Name ID Attribute

This tells the SSO provider want information to include as the required Name ID. The information it stores about your users is generally called attributes but may also be called fields or other names. This **must be set so that is the same email address as used on the Aptible account**. Most SSO providers have an email attribute that can be selected here. If not, you may have to create a custom attribute in your SSO provider.

You may optionally configure the SSO provider to send additional attributes, such as the user's full name. Aptible currently ignores any additional attributes sent.

> ❗️ Warning

> If the email address sent by the SSO provider does not exactly match the email address associated with their Aptible account, the user will not be able to login via your SSO provider. If users are having issues logging in, you should confirm those email addresses match.

## Other configuration fields

Your SSO provider may have many other configuration fields. You should be able to leave these at their default settings. We provide some general guidance if you do want to customize your settings. However, your SSO provider's documentation should supersede any information here as these values can vary from provider to provider.

* **Default RelayState or Start URL**: This allows you to set a default page on Aptible that your users will be taken to when logging in. We direct the user to the product they were using when they started logging in. You can override that behavior here if you want them to always start on a particular product.

* **Encryption, Signature, Digest Algorithms**: Prefer options with `SHA-256` over those with `SHA-1`.

## Aptible SSO Configuration

Once your have completed the SSO provider configuration, they should provide you with **XML Metadata** either as a URL or via file download.

Return to the Single Sign On settings page for your Organization, where you copied the values for setting up your SSO provider. Then click on the "Configure an SSO Provider"

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=72e3379f35cd1304df39b82e30d035b8" alt="" data-og-width="2100" width="2100" data-og-height="1324" height="1324" data-path="images/sso2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=41536165b21ec41b6aa5917a3174a7eb 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=106cfd028392563e704ff94a86b3fe7a 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7ee73df269bd976b8c5035b53bc493e0 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=20f9bca7144f449af2ccc79721cd338b 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7b33344d81bb4c78004cda574e53ce90 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso2.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e3f56ed365225264dec75463a1ae3b41 2500w" />

In the resulting modal box, enter either the URL or the XML contents of the file. You only need to enter one. If you enter both, Aptible will use the URL to retrieve the metadata. Aptible will then complete our setup automatically.

> 📘 Note

> Aptible only supports SSO configurations with a single certificate at this time. If you get an error when applying your configuration, check to see if it contains multiple `KeyDescriptor` elements. If you require multiple certificates please notify [Aptible Support](/how-to-guides/troubleshooting/aptible-support).

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=36c3e9fac78f1b9f515ff24864e4f5f2" alt="" data-og-width="1318" width="1318" data-og-height="1140" height="1140" data-path="images/sso3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a1f537229583586a99264ae95cdedc00 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=eedab109764ed12a00e0f9ba20029035 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=55cce2671210110ad81679b143de8ba4 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=aecf8824e06352abbe9603628c5ba4ce 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=68f008c5bb96e0d22e94970449e82d89 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso3.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=ae4beb3e7ce74a6f9d595a9742758f3a 2500w" />

> ❗️ Warning

> When you retrieve the metadata, you should ensure the SSO provider's site is an HTTPS site. This ensure that the metadata is not tampered with during download. If an attacker could alter that metadata, they could substitute their own information and hi-jack your SSO configuration.

Once processing is complete, you should see data from your SSO provider. You can confirm these with the SSO provider's website to ensure they are correct.

You can optionally enable additional SSO feature within Aptible at this point:

## Okta Walkthrough

As a complement to the generic guide, we will present a detailed walkthrough for configuring Okta as an SSO provider to an Aptible Organization.

## Sign in to Okta with an admin account

* Click Applications in the main menu.

* Click Add Application and then Create New App.

## Setup a Web application with SAML 2.0

* The default platform should be Web. If not, select that option.

* Select SAML 2.0 as the Sign on method.

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f715ab37ec20cb5287d416ec910dcd6d" alt="" data-og-width="1408" width="1408" data-og-height="818" height="818" data-path="images/sso4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=ffd34183be466ef5e7d8fb4e12dfb1d2 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=931823cd6eb525a79677f8fa406b8343 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=224c02ba29f21390a7b9ceac13ea5a26 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=349c648dc12a7578ed8360806319eb79 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f3fc7a26eee6a85e468f993c3bf8c588 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso4.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=41605e048be41b6d7f6fa4c161a7c7d2 2500w" />

## Create SAML Integration

* Enter `Aptible Deploy` or another name of your choice.

* You may download and use our [logo](https://mintlify.s3-us-west-1.amazonaws.com/aptible/images/aptible_logo.png) for an image.

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e36c0f5d63b629dd4ce5d8231bb42ad2" alt="" data-og-width="2072" width="2072" data-og-height="1288" height="1288" data-path="images/sso5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8c7e99be829987b2f389399f31c6662d 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f6f1ae7b6c0f372748c53f69bd0f804c 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1697421fc62e8a4406f774c78bc181a8 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=65f4c3b5dd0876af6251364a9ddec28f 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4147535261f824a2043caaed6671cb13 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso5.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=52de2f2dc8d21e22b9e5d983cf949970 2500w" />

## Enter SAML Settings from Aptible Single Sign On Settings Page

* Open the Organization settings in Aptible Dashboard

* Select the Single Sign On settings in the sidebar

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=26edc04ad115aaa4d4383d6defb7b9d8" alt="" data-og-width="2100" width="2100" data-og-height="1324" height="1324" data-path="images/sso6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8ad564e4eb3944635d9f864fcfdc4a78 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=712ff7fdfae11ea605304432a0faa8fc 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7513a59dd612ead15678586dbd28e265 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7a6c0c7acf82459dd596602149e5add2 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6c077fdd136f3cf2edc0ede51353202b 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso6.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=000cdc90730aa57ffab8980057b28380 2500w" />

* Copy and paste the Single Sign On URL

* Copy and paste the Audience URI

* Select `EmailAddress` for the Name ID format dropdown

* Select `Email` in the Application username dropdown

* Leave all other values as their defaults

* Click Next

<img src="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=d8b0107c34a2224fcc09fdc0c9c14b6d" alt="" data-og-width="1538" width="1538" data-og-height="1132" height="1132" data-path="images/sso7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?w=280&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=2ccb4d3e685019dff7836314f0d8e2ff 280w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?w=560&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=643911df4c2f93992bbd124d5176c977 560w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?w=840&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=eba84f2a61a660a1cb98be69413da4d3 840w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?w=1100&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=36ff8f33a251df1e85bc7a90f66ae0e7 1100w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?w=1650&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=0b7cbadf7f373878faa9589748108872 1650w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso7.png?w=2500&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=33c28644b6dfd9746ee0eca789273ec9 2500w" />

## Fill-in Okta's Feedback Page

* Okta will prompt you for feedback on the SAML setup.

* Select "I'm an Okta customer adding an internal app"

* Optionally, provide additional feedback.

* When complete, click Finish.

<img src="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=95ab69e432aac15f8b57acb7d338530d" alt="" data-og-width="1538" width="1538" data-og-height="1490" height="1490" data-path="images/sso8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?w=280&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=c2754d7acd60e5063c098fd556f4df36 280w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?w=560&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=1b637856204cd748a4bbc6e17c67cff0 560w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?w=840&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=20326978400bb8db21478895a72558de 840w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?w=1100&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=3f0f6256c2209cfde29f99ed7f6f420b 1100w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?w=1650&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=ece0de41890085de20faee8e31f07448 1650w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso8.png?w=2500&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=ab12c4db65ae2faaf725d0fea30894e2 2500w" />

* Copy the link for Identity Provider metadata

<img src="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=e56ad6ec675d307616541a0be3e34838" alt="" data-og-width="1538" width="1538" data-og-height="1490" height="1490" data-path="images/sso9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?w=280&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=e4d632ddb69c0d516ab5ba738f220f3b 280w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?w=560&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=21abda43e0496eba5b3e34aeddd21d04 560w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?w=840&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=877d14d6c0701162fafbba7ea2eeec1e 840w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?w=1100&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=a1fe0118daeba82261901b8dbc91e831 1100w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?w=1650&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=d724a1094f45ce7257f174a3d490ae55 1650w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/sso9.png?w=2500&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=888338f7a8d2ee07cae99da1ff53cf70 2500w" />

* Open the Single Sign On settings page for your Organization in Aptible

* Click "Configure an SSO Provider"

* Paste the metadata URL into the box

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5ad1d7263947d1a84192acfc8cec536c" alt="" data-og-width="1472" width="1472" data-og-height="1222" height="1222" data-path="images/sso10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6dcf2d2dab9073b48211ab058aaf15d2 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=ea68874d0f9928ee674189b9fb3dc832 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=2e16cb5e479a2d2dd4733758b675be1b 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=33c3a536b4fb635eb45444f3d3c93a34 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=39ac6b7ee6f1e15acab47e509d14182a 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sso10.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6cd5e732d3503e8de735a31bd74738b1 2500w" />

## Assign Users to Aptible Deploy

* Follow [Okta's guide to assign users](https://developer.okta.com/docs/guides/saml-application-setup/assign-users-to-the-app/) to the new application.

## Frequently Asked Questions

**What happens if my SSO provider suffers downtime?**

Users can continue to use their Aptible credentials to login even after SSO is enabled. If you also enabled [SSO enforcement](/core-concepts/security-compliance/authentication/sso#require-sso-for-access) then your Account Owners can still login with their Aptible credentials and disable enforcement until the SSO provider is back online.

**Does Aptible offer automated provisioning of SSO users?**

Aptible supports SCIM 2.0 provisioning. Please refer to our [Provisioning Guide](/core-concepts/security-compliance/authentication/scim).

**Does Aptible support Single Logout?**

We do not at this time. If this would be helpful for your Organization, please let us know.

**How can I learn more about SAML?**

There are many good references available on the Internet. We suggest the following starting points:

* [Understanding SAML](https://developer.okta.com/docs/concepts/saml/)

* [The Beer Drinker's Guide to SAML](https://duo.com/blog/the-beer-drinkers-guide-to-saml)

* [Overview of SAML](https://developers.onelogin.com/saml)

* [How SAML Authentication Works](https://auth0.com/blog/how-saml-authentication-works/)

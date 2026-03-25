# Source: https://docs.brightdata.com/general/authentication/How_to_set_up_Azure_SSO_Entra_ID_with_Bright_Data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Entra ID (formerly Azure Active Directory) SSO and provisioning with Bright Data

* Prepare application

* Setup SSO

* Setup SCIM provisioning

## Prepare Application

* Go to [https://entra.microsoft.com/](https://entra.microsoft.com/) and log in to your account.

* Create Enterprise application:

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_1.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=5c1f6c72ee5a46225e799d033b50806e" alt="" width="1827" height="928" data-path="images/general/authentication/entra-sso/entra_1.png" />

* Click “Create your own application”

* Enter name of your application

* Select “Integrate any other application you don't find in the gallery (Non-gallery)”

* Click “Create”

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_2.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=59a4c25f2d2670958806050db191754f" alt="" width="1827" height="929" data-path="images/general/authentication/entra-sso/entra_2.png" />

## Setup SSO

* Go to [https://brightdata.com](https://brightdata.com) and log in to your account.

* Choose Settings->Account settings->Passwords & authentication in left side menu and toggle Microsoft Entra ID (Azur AD) switch

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_3.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=443a8bb966ba43de9c83b646b939795a" alt="" width="1727" height="919" data-path="images/general/authentication/entra-sso/entra_3.png" />

* From “App registrations” view select your application.

* Copy “Application (client) ID” to “Client ID”

* Copy “Directory (tenant) ID” to “OAuth2 issuer (tenant)”

* Go to “Add a certificate or secret”

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_4.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=f990afd4810220988b64276a84f24043" alt="" width="1824" height="930" data-path="images/general/authentication/entra-sso/entra_4.png" />

* At secrets screen click “New client secret”

* Fill Description

* Click “Add”

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_5.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=6f88cd89b7c03d1dd716e387e58fc2fa" alt="" width="1823" height="930" data-path="images/general/authentication/entra-sso/entra_5.png" />

* Once secret is created copy secret value to “Client secret”.

* Copy “Sign-in redirect URI” to be used at next step

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_6.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=102eae8e919e9fb913fe866dd60e9514" alt="" width="1828" height="929" data-path="images/general/authentication/entra-sso/entra_6.png" />

* At “Authentication” screen click “Add platform” and select “Web”

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/entra-sso/entra_7.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=8e669ab7617f11823b6b5bbf34593165" alt="" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_7.png" />

* Paste previously copied “Sign-in redirect URI” to the “Redirect URIs” and save settings by clicking “Configure”:

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/entra-sso/entra_8.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=85894520a15c28d47d42d7b013f0d34b" alt="" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_8.png" />

* Activate EntraID integration at BrighData control panel and test login:

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/entra-sso/entra_9.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=25f26a778deb482db04e503fce584f39" alt="" width="892" height="916" data-path="images/general/authentication/entra-sso/entra_9.png" />

## Setup SCIM provisioning

* Copy “Auth token” from SCIM section of BrightData EntraID settings:

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_10.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=55428290253bb5aa811dfc4498a975b4" alt="" width="671" height="878" data-path="images/general/authentication/entra-sso/entra_10.png" />

* Select your application from “Enterprise Applications” view and go to “Provisioning” settings:

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_11.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=5df253d68b16b0a965205708ecff3633" alt="" width="1559" height="930" data-path="images/general/authentication/entra-sso/entra_11.png" />

* Select “Provisioning” under “Manage” menu:

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_12.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=dadaf9a34f71bfc1582ebf71370f6b72" alt="" width="1557" height="931" data-path="images/general/authentication/entra-sso/entra_12.png" />

* Select “Automatic” Provisioning Mode

* Fill “Tenant URL” with [https://brightdata.com/users/auth/scim](https://brightdata.com/users/auth/scim) value

* Fill “Secret Token” with previously copied value from BrightData control panel settings

* Test Connection. You should see successful message in top right corner
  Save Settings

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_13.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=790a1458505acedb0d0babdcf0962201" alt="" width="1823" height="931" data-path="images/general/authentication/entra-sso/entra_13.png" />

* Return to “Overview” tab and click “Start provisioning”.

* You can test provisioning at “Provision on demand” page, but first assign your users to BrightData application at “Users and groups” page:

<img src="https://mintcdn.com/brightdata/2RrKkArDJDw55ilE/images/general/authentication/entra-sso/entra_14.png?fit=max&auto=format&n=2RrKkArDJDw55ilE&q=85&s=ced6d1d8ae07a81a2a08712635255303" alt="" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_14.png" />

# Site configuration settings

Review and manage the following site configuration options in the System
Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and then selecting **Site Configuration**:

- [Customization](#customization)
- [Localization](#localization)
- [Users and Teams](#users-and-teams)
- [Notifications](#notifications)
- [System-wide notifications](#system-wide-notifications)
- [Emoji](#emoji)
- [Posts](#posts)
- [File Sharing and Downloads](#file-sharing-and-downloads)
- [Public Links](#public-links)
- [Notices](#notices)
- [Connected Workspaces](#connected-workspaces)

:::: tip
::: title
Tip
:::

System admins managing a self-hosted Mattermost deployment can edit the
`config.json` file as described in the following tables. Each
configuration value below includes a JSON path to access the value
programmatically in the `config.json` file using a JSON-aware tool. For
example, the `SiteName` value is under `TeamSettings`.

- If using a tool such as [jq](https://stedolan.github.io/jq/), you\'d
  enter: `cat config/config.json | jq '.TeamSettings.SiteName'`
- When working with the `config.json` file manually, look for an object
  such as `TeamSettings`, then within that object, find the key
  `SiteName`.
::::

------------------------------------------------------------------------

## Customization

Access the following configuration settings in the System Console by
going to **Site Configuration \> Customization**.

### Site name

+----------------------------------+-----------------------------------+
| Name of the site shown in login  | - System Config path: **Site      |
| screens and user interface.      |   Configuration \>                |
|                                  |   Customization**                 |
| String input. Maximum 30         | - `config.json` setting:          |
| characters. Default is           |   `TeamSettings` \> `SiteName`    |
| `Mattermost`                     | - Environment variable:           |
|                                  |   `MM_TEAMSETTINGS_SITENAME`      |
+----------------------------------+-----------------------------------+

### Site description

+--------------------------------------+-------------------------------------------+
| Text displayed above the login form. | - System Config path: **Site              |
| When not specified, the phrase \"Log |   Configuration \> Customization**        |
| in\" is displayed.                   | - `config.json` setting: `TeamSettings`   |
|                                      |   \> `CustomDescriptionText`              |
| String input.                        | - Environment variable:                   |
|                                      |   `MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT` |
+--------------------------------------+-------------------------------------------+

### Enable custom branding

+----------------------------------+---------------------------------------+
| - **true**: Enables the display  | - System Config path: **Site          |
|   of a custom image and text on  |   Configuration \> Customization**    |
|   the login page                 | - `config.json` setting:              |
| - **false**: **(Default)**       |   `TeamSettings` \>                   |
|   Custom branding is disabled    |   `EnableCustomBrand` \> `false`      |
|                                  | - Environment variable:               |
| See also the [custom brand       |   `MM_TEAMSETTINGS_ENABLECUSTOMBRAND` |
| image](#custom-brand-image) and  |                                       |
| [custom brand                    |                                       |
| text](#custom-brand-text)        |                                       |
| configuration settings for more  |                                       |
| branding options.                |                                       |
+----------------------------------+---------------------------------------+

### Custom brand image

+----------------------------------------------------+-------------------+
| A JPG image for display on the login page. The     | - System Config   |
| image **must** be uploaded through the System      |   path: **Site    |
| Console. There is no `config.json` setting. The    |   Configuration   |
| file should be **smaller than 2 MB**.              |   \>              |
|                                                    |   Customization** |
| [Enable custom branding](#enable-custom-branding)  | - `config.json`   |
| must be set to **true** to display the image.      |   setting: N/A    |
|                                                    | - Environment     |
|                                                    |   variable: N/A   |
+----------------------------------------------------+-------------------+

### Custom brand text

+---------------------------------------------------------------------------------------+-------------------------------------+
| Text that will be shown below the **Custom brand image** on the login page. You can   | - System Config path: **Site        |
| format this text using the same                                                       |   Configuration \> Customization**  |
| `Markdown formatting </end-user-guide/collaborate/format-messages>`{.interpreted-text | - `config.json` setting:            |
| role="doc"} as in Mattermost messages.                                                |   `TeamSettings` \>                 |
|                                                                                       |   `CustomBrandText`                 |
| String input. Maximum 500 characters. [Enable custom                                  | - Environment variable:             |
| branding](#enable-custom-branding) must be set to **true** to display the text.       |   `MM_TEAMSETTINGS_CUSTOMBRANDTEXT` |
+---------------------------------------------------------------------------------------+-------------------------------------+

### Enable Ask Community link

+---------------------------------------------------+-------------------------------------------------+
| > - **true**: **(Default)** A link to the         | > - System Config path: **Site Configuration \> |
| >   [Mattermost                                   | >   Customization**                             |
| >   Community](https://mattermost.com/community/) | > - `config.json` setting: `SupportSettings` \> |
| >   appears as **Ask the community** under the    | >   `EnableAskCommunityLink` \> `true`          |
| >   **Help** menu in the channel header.          | > - Environment variable:                       |
| > - **false**: The link does not appear.          | >   `MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK` |
| >                                                 |                                                 |
| > The link does not display on mobile apps.       |                                                 |
+---------------------------------------------------+-------------------------------------------------+

### Help link

+-------------------------------------------------+---------------------------------+
| This field sets the URL for the Help link on    | - System Config path: **Site    |
| the login and sign up pages, as well as the     |   Configuration \>              |
| **Help Resources** link under the **Help** menu |   Customization**               |
| in the channel header.                          | - `config.json` setting:        |
|                                                 |   `SupportSettings` \>          |
| String input. Default is                        |   `HelpLink`                    |
| `https://about.mattermost.com/default-help/`.   | - Environment variable:         |
|                                                 |   `MM_SUPPORTSETTINGS_HELPLINK` |
+-------------------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

If this value is empty, the Help link is hidden on the login and sign up
pages. However, the **Help Resources** link remains available under the
**Help** menu.
::::

### Terms of Use link

+------------------------------------------------------------+-------------------------------------------+
| This field sets the URL for the Terms of Use of a          | - System Config path: **Site              |
| self-hosted site. A link to the terms appears at the       |   Configuration \> Customization**        |
| bottom of the sign-up and login pages.                     | - `config.json` setting:                  |
|                                                            |   `SupportSettings` \>                    |
| The default URL links to a [Terms of                       |   `TermsOfServiceLink`                    |
| Use](https://mattermost.com/terms-of-use/) page hosted on  | - Environment variable:                   |
| `mattermost.com`. This includes the Mattermost Acceptable  |   `MM_SUPPORTSETTINGS_TERMSOFSERVICELINK` |
| Use Policy explaining the terms under which Mattermost     |                                           |
| software is provided to end users. If you change the       |                                           |
| default link to add your own terms, the new terms **must   |                                           |
| include a link** to the default terms so end users are     |                                           |
| aware of the Mattermost Acceptable Use Policy.             |                                           |
|                                                            |                                           |
| String input. Default is                                   |                                           |
| `https://about.mattermost.com/default-terms/`.             |                                           |
+------------------------------------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

\- Customers with a Mattermost subscription may replace or override the
Acceptable Use Policy with their own acceptable use or conduct policies,
based on contractual terms with Mattermost, so long as your own terms
either incorporate the Acceptable Use Policy or include equivalent
terms. If you change the default link to add your own terms for using
the service you provide, your new terms must include a [link to the
default
terms](https://mattermost.com/terms-of-use/#acceptable-use-policy) so
end users are aware of the Mattermost Acceptable Use Policy for
Mattermost software. - This setting is applicable to self-hosted
deployments only and doesn\'t change the **Terms of Use** link in the
**About Mattermost** window.
::::

### Privacy Policy link

+---------------------------------------------------------+------------------------------------------+
| This field sets the URL for the Privacy Policy of a     | - System Config path: **Site             |
| self-hosted site. A link to the policy appears at the   |   Configuration \> Customization**       |
| bottom of the sign-up and login pages. If this field is | - `config.json` setting:                 |
| empty, the link does not appear.                        |   `SupportSettings` \>                   |
|                                                         |   `PrivacyPolicyLink`                    |
| String input. Default is                                | - Environment variable:                  |
| `https://about.mattermost.com/default-privacy-policy/`. |   `MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK` |
+---------------------------------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable to self-hosted deployments only and
doesn\'t change the **Privacy Policy** link in the **About Mattermost**
window.
::::

### About link

+------------------------------------------------------+----------------------------------+
| This field sets the URL for a page containing        | - System Config path: **Site     |
| general information about a self-hosted site. A link |   Configuration \>               |
| to the About page appears at the bottom of the       |   Customization**                |
| sign-up and login pages. If this field is empty the  | - `config.json` setting:         |
| link does not appear.                                |   `SupportSettings` \>           |
|                                                      |   `AboutLink`                    |
| String input. Default is                             | - Environment variable:          |
| `https://about.mattermost.com/default-about/`.       |   `MM_SUPPORTSETTINGS_ABOUTLINK` |
+------------------------------------------------------+----------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### Forgot Password custom link

+-----------------------------------+-------------------------------------------+
| When the **Forgot Password** link | - System Config path: **Site              |
| is enabled on the Mattermost      |   Configuration \> Forgot password custom |
| login page, users are taken to a  |   link**                                  |
| custom URL to recover or change   | - `config.json` setting:                  |
| their password.                   |   `SupportSettings` \>                    |
|                                   |   `ForgetPasswordLink`                    |
| Leave this field blank to use     | - Environment variable:                   |
| Mattermost\'s Password Reset      |   `MM_SUPPORTSETTINGS_FORGETPASSWORDLINK` |
| workflow.                         |                                           |
+-----------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

This configuration setting applies to all Mattermost clients, including
web, desktop app, and mobile app. You can control whether the **Forgot
Password** link is visible or hidden in clients by going to
**Authentication \> Password \> Enable Forgot Password Link**. See the
`configuration <administration-guide/configure/authentication-configuration-settings:enable forgot password link>`{.interpreted-text
role="ref"} documentation for details.
::::

### Report a Problem

With self-hosted deployments, you can specify how the **Report a
Problem** option behaves in the Mattermost app via the **Help** menu:

- **Default link**: Uses the default Mattermost URL to report a problem.
  Customers with a Mattermost subscription are directed to the
  [Mattermost Support
  Portal](https://support.mattermost.com/hc/en-us/requests/new).
  Community deployments are directed to [create a new issue on the
  Mattermost GitHub
  repository](https://github.com/mattermost/mattermost/issues/new).
- **Email address**: Enables you to
  `enter an email address <administration-guide/configure/site-configuration-settings:report a problem email address>`{.interpreted-text
  role="ref"} that users will be prompted to send a message to when they
  choose **Report a Problem** in Mattermost.
- **Custom link**: Enables you to
  `enter a URL <administration-guide/configure/site-configuration-settings:report a problem link>`{.interpreted-text
  role="ref"} that users will be directed to when they choose **Report a
  Problem** in Mattermost.
- **Hide link**: Removes the **Report a Problem** option from
  Mattermost.

### Report a Problem link

+-------------------------------------------+-------------------------------------------+
| This field sets the URL for the **Report  | - System Config path: **Site              |
| a Problem** link in the channel header    |   Configuration \> Customization**        |
| **Help** menu. If this field is empty the | - `config.json` setting:                  |
| link does not appear.                     |   `SupportSettings` \>                    |
|                                           |   `ReportAProblemLink`                    |
| String input. Default is                  | - Environment variable:                   |
| `https://mattermost.com/pl/report-a-bug`. |   `MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK` |
+-------------------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### Report a Problem email address

+----------------------------------------+-------------------------------------------+
| This field sets the email address for  | - System Config path: **Site              |
| the **Report a Problem** link in the   |   Configuration \> Customization**        |
| channel header **Help** menu.          | - `config.json` setting:                  |
|                                        |   `SupportSettings` \>                    |
| String input. Cannot be left blank.    |   `ReportAProblemMail`                    |
|                                        | - Environment variable:                   |
|                                        |   `MM_SUPPORTSETTINGS_REPORTAPROBLMEMAIL` |
+----------------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### Allow mobile app log downloads

+-----------------------------------+------------------------------------------+
| Enable users to download mobile   | - System Config path: **Site             |
| app logs for troubleshooting.     |   Configuration \> Customization**       |
| When the **Report a Problem**     | - `config.json` setting:                 |
| link is shown, mobile logs can be |   `SupportSettings` \>                   |
| downloaded as part of the         |   `AllowDownloadLogs`                    |
| reporting flow.                   | - Environment variable:                  |
|                                   |   `MM_SUPPORTSETTINGS_ALLOWDOWNLOADLOGS` |
| - **true** (**Default**): Users   |                                          |
|   can download mobile app logs.   |                                          |
| - **false** Users can\'t download |                                          |
|   mobile app logs.                |                                          |
+-----------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### Mattermost apps download page link

+--------------------------------------------+------------------------------------------+
| This field sets the URL for the Download   | - System Config path: **Site             |
| Apps link in the **Product** menu. If this |   Configuration \> Customization**       |
| field is empty, the link does not appear.  | - `config.json` setting:                 |
|                                            |   `NativeAppSettings` \>                 |
| If you have an Enterprise App Store, set   |   `AppDownloadLink`                      |
| the link to the appropriate download page  | - Environment variable:                  |
| for your Mattermost apps.                  |   `MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK` |
|                                            |                                          |
| String input. Default is                   |                                          |
| `https://mattermost.com/pl/download-apps`. |                                          |
+--------------------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### Android app download link

+----------------------------------------------------+-------------------------------------------------+
| This field sets the URL to download the Mattermost | - System Config path: **Site Configuration \>   |
| Android app. Users who access the Mattermost site  |   Customization**                               |
| on a mobile browser will be prompted to download   | - `config.json` setting: `NativeAppSettings` \> |
| the app through this link. If this field is empty, |   `AndroidAppDownloadLink`                      |
| the prompt does not appear.                        | - Environment variable:                         |
|                                                    |   `MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK` |
| If you have an Enterprise App Store, link to your  |                                                 |
| Android app.                                       |                                                 |
|                                                    |                                                 |
| String input. Default is                           |                                                 |
| `https://mattermost.com/pl/android-app/`.          |                                                 |
+----------------------------------------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### iOS app download link

+----------------------------------------------------+---------------------------------------------+
| This field sets the URL to download the Mattermost | - System Config path: **Site Configuration  |
| iOS app. Users who access the site on a mobile     |   \> Customization**                        |
| browser will be prompted to download the app       | - `config.json` setting:                    |
| through this link. If this field is empty, the     |   `NativeAppSettings` \>                    |
| prompt does not appear.                            |   `IosAppDownloadLink`                      |
|                                                    | - Environment variable:                     |
| If you use an Enterprise App Store, link to your   |   `MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK` |
| iOS app.                                           |                                             |
|                                                    |                                             |
| String input. Default is                           |                                             |
| `https://mattermost.com/pl/ios-app/`.              |                                             |
+----------------------------------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only.
::::

### Enable desktop app landing page

+-----------------------------+-------------------------------------------------+
| - **true**: **(Default)**   | - System Config path: **Site Configuration \>   |
|   Prompts users to use the  |   Customization**                               |
|   desktop app.              | - `config.json` setting: `ServiceSettings` \>   |
| - **false**: Doesn\'t       |   `EnableDesktopLandingPage` \> `true`          |
|   prompt users to use the   | - Environment variable:                         |
|   desktop app.              |   `MM_SERVICESETTINGS_ENABLEDESKTOPLANDINGPAGE` |
+-----------------------------+-------------------------------------------------+

### App custom URL schemes

This setting isn\'t available in the System Console and can only be set
in `config.json`.

Define valid custom URL schemes for redirect links provided by
custom-built mobile Mattermost apps. This ensures users are redirected
to the custom-built mobile app and not Mattermost\'s mobile client.

When configured, after OAuth or SAML user authentication is complete,
custom URL schemes sent by mobile clients are validated to ensure they
don\'t include default schemes such as `http` or `https`. Mobile users
are then redirected back to the mobile app using the custom scheme URL
provided by the mobile client. We recommend that you update your mobile
client values as well with valid custom URL schemes.

+----------------------------------------------------------------------------------------+
| This feature\'s `config.json` setting is `"NativeAppSettings.AppCustomURLSchemes"`     |
| with an array of strings as input separated by spaces.                                 |
+----------------------------------------------------------------------------------------+
| For example:                                                                           |
|                                                                                        |
| - `MM_NativeAppSettings_AppCustomURLSchemes = mmauth:// mmauthbeta://`                 |
| - Via mmctl:                                                                           |
|   `mmctl config set NativeAppSettings.AppCustomURLSchemes "mmauth://" "mmauthbeta://"` |
+----------------------------------------------------------------------------------------+

### Mobile external browser

+-------------------------------------+------------------------------------------------+
| From Mattermost v10.2 and Mobile    | - System Config path: N/A                      |
| v2.2.1, this setting configures the | - `config.json` setting:                       |
| mobile app to use an external       |   `NativeAppSettings.MobileExternalBrowser`    |
| mobile browser to perform SSO       | - Environment variable:                        |
| authentication.                     |   `MM_NATIVEAPPSETTINGS_MOBILEEXTERNALBROWSER` |
|                                     |                                                |
| - **true**: The mobile app uses the |                                                |
|   default internal mobile browser   |                                                |
|   to perform SSO authentication.    |                                                |
| - **false**: **(Default)** The      |                                                |
|   mobile app uses an external       |                                                |
|   mobile browser to perform SSO     |                                                |
|   authentication.                   |                                                |
+-------------------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

- This setting is applicable to self-hosted deployments only.
- We recommend enabling this configuration setting when there are issues
  with the mobile app SSO redirect flow.
::::

------------------------------------------------------------------------

## Localization

Access the following configuration settings in the System Console by
going to **Site Configuration \> Localization**. Changes to
configuration settings in this section require a server restart before
taking effect.

### Default server language

+-----------------------------------+-------------------------------------------------+
| The default language for system   | - System Config path: **Site Configuration \>   |
| messages and logs.                |   Localization**                                |
|                                   | - `config.json` setting: `LocalizationSettings` |
| Options: `"bg"`, `"de"`, `"en"`,  |   \> `DefaultServerLocale`                      |
| `"en-AU"`, `"es"`, `"fa"`,        | - Environment variable:                         |
| `"fr"`, `"hu"`, `"it"`, `"ja"`,   |   `MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE` |
| `"ko"`, `"nl"`, `"pl"`,           |                                                 |
| `"pt-br"`, `"ro"`, `"ru"`,        |                                                 |
| `"sv"`, `"tr"`, `"uk"`, `"vi"`,   |                                                 |
| `"zh-Hans"`, and `"zh-Hant"`.     |                                                 |
|                                   |                                                 |
| Default is `"en"`.                |                                                 |
+-----------------------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

Changing this configuration setting changes the default server language
for users who haven\'t set a language preference via **Settings**.
Mattermost applies the user\'s language preference when specified.
::::

### Default client language

+-----------------------------------+-------------------------------------------------+
| The default language for new      | - System Config path: **Site Configuration \>   |
| users and pages where the user    |   Localization**                                |
| isn\'t logged in.                 | - `config.json` setting: `LocalizationSettings` |
|                                   |   \> `DefaultClientLocale`                      |
| Options: `"bg"`, `"de"`, `"en"`,  | - Environment variable:                         |
| `"en-AU"`, `"es"`, `"fa"`,        |   `MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE` |
| `"fr"`, `"hu"`, `"it"`, `"ja"`,   |                                                 |
| `"ko"`, `"nl"`, `"pl"`,           |                                                 |
| `"pt-br"`, `"ro"`, `"ru"`,        |                                                 |
| `"sv"`, `"tr"`, `"uk"`, `"vi"`,   |                                                 |
| `"zh-Hans"`, and `"zh-Hant"`.     |                                                 |
|                                   |                                                 |
| Default is `"en"`.                |                                                 |
+-----------------------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

Changing this configuration setting changes the default client language
for users who haven\'t set a language preference via **Settings**.
Mattermost applies the user\'s language preference when specified.
::::

### Available languages

+------------------------------------+----------------------------------------------+
| Sets the list of languages users   | - System Config path: **Site Configuration   |
| see under **Settings \> Display \> |   \> Localization**                          |
| Language**. If this field is left  | - `config.json` setting:                     |
| blank, users see all supported     |   `LocalizationSettings` \>                  |
| languages. Newly supported         |   `AvailableLocales`                         |
| languages are added automatically. | - Environment variable:                      |
| If this field is not blank, it     |   `MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES` |
| must contain the **Default client  |                                              |
| language**, in addition to any     |                                              |
| other languages. For example, to   |                                              |
| limit the language choices to US   |                                              |
| English and Español (es), the      |                                              |
| string would be `"en,es"`.         |                                              |
|                                    |                                              |
| Options: `"bg"`, `"de"`, `"en"`,   |                                              |
| `"en-AU"`, `"es"`, `"fa"`, `"fr"`, |                                              |
| `"hu"`, `"it"`, `"ja"`, `"ko"`,    |                                              |
| `"nl"`, `"pl"`, `"pt-br"`, `"ro"`, |                                              |
| `"ru"`, `"sv"`, `"tr"`, `"uk"`,    |                                              |
| `"vi"`, `"zh-Hans"`, and           |                                              |
| `"zh-Hant"`.                       |                                              |
|                                    |                                              |
| Default is `"en"`.                 |                                              |
+------------------------------------+----------------------------------------------+

### Enable experimental locales

Enable work in progress languages in Mattermost to review translations
and identify translation gaps.

+-------------------------+------------------------------------------------------+
| - **true**: Work in     | - System Config path: **Site Configuration \>        |
|   progress languages    |   Localization**                                     |
|   are available in      | - `config.json` setting: `LocalizationSettings` \>   |
|   Mattermost in         |   `EnableExperimentalLocales` \> `false`             |
|   addition to           | - Environment variable:                              |
|   officially supported  |   `MM_LOCALIZATIONETTINGS_ENABLEEXPERIMENTALLOCALES` |
|   languages.            |                                                      |
| - **false**:            |                                                      |
|   **(Default)** Only    |                                                      |
|   officially supported  |                                                      |
|   languages are         |                                                      |
|   available in          |                                                      |
|   Mattermost.           |                                                      |
+-------------------------+------------------------------------------------------+

:::: note
::: title
Note
:::

- Cloud system admins can request this configuration setting to be
  enabled for their instance by contacting their Mattermost Account
  Manager.
- Work in progress languages may be incomplete. Strings missing
  translations display in US English.
- Currently, only web and desktop app product strings are impacted by
  this configuration setting. Server and mobile product strings aren\'t
  impacted by this setting.
- See the
  `language <end-user-guide/preferences/manage-your-display-options:language>`{.interpreted-text
  role="ref"} documentation for details on selecting a language
  preference in Mattermost.
::::

------------------------------------------------------------------------

## Users and teams

Access the following configuration settings in the System Console by
going to **Site Configuration \> Users and Teams**.

### Max users per team

+----------------------------------------------------------------------------------------+-------------------------------------+
| The **Max users per team** is the maximum total number of users per team, including    | - System Config path: **Site        |
| activated and deactivated users.                                                       |   Configuration \> Users and        |
|                                                                                        |   Teams**                           |
| In Mattermost, a team of people should be a small organization with a specific goal.   | - `config.json` setting:            |
| In the physical world, a team could sit around a single table. The default maximum     |   `TeamSettings` \>                 |
| (50) should be enough for most teams, but with appropriate                             |   `MaxUsersPerTeam` \> `50`         |
| [hardware](https://docs.mattermost.com/install/software-hardware-requirements.html),   | - Environment variable:             |
| this limit can be increased to thousands of users.                                     |   `MM_TEAMSETTINGS_MAXUSERSPERTEAM` |
|                                                                                        |                                     |
| `Channels </end-user-guide/collaborate/collaborate-within-channels>`{.interpreted-text |                                     |
| role="doc"} are another way of organizing communications within teams on various       |                                     |
| topics.                                                                                |                                     |
|                                                                                        |                                     |
| Numerical input. Default is **50** self-hosted deployments, and **10000** for Cloud    |                                     |
| deployments.                                                                           |                                     |
+----------------------------------------------------------------------------------------+-------------------------------------+

### Max channels per team

+------------------------------------+----------------------------------------+
| The maximum number of channels per | - System Config path: **Site           |
| team, including both active and    |   Configuration \> Users and Teams**   |
| archived channels.                 | - `config.json` setting:               |
|                                    |   `TeamSettings` \>                    |
| Numerical input. Default is        |   `MaxChannelsPerTeam` \> `2000`       |
| **2000** for self-hosted           | - Environment variable:                |
| deployments, and **10000** for     |   `MM_TEAMSETTINGS_MAXCHANNELSPERTEAM` |
| Cloud deployments.                 |                                        |
+------------------------------------+----------------------------------------+

### Enable join/leave messages by default

+---------------------------------+-----------------------------------------------------+
| Specify the default             | - System Config path: **Site Configuration \> Users |
| configuration of system         |   and Teams**                                       |
| messages displayed when users   | - `config.json` setting: `TeamSettings` \>          |
| join or leave channels.         |   `EnableJoinLeaveMessageByDefault` \> `true`       |
|                                 | - Environment variable:                             |
| - **true**: **(Default)**       |   `MM_TEAMSETTINGS_ENABLEJOINLEAVEMESSAGEBYDEFAULT` |
|   Join/Leave messages are       |                                                     |
|   displayed.                    |                                                     |
| - **false**: Join/Leave         |                                                     |
|   messages are hidden.          |                                                     |
|                                 |                                                     |
| Users can override this default |                                                     |
| by going to **Settings \>       |                                                     |
| Advanced \> Enable Join/Leave   |                                                     |
| Messages**.                     |                                                     |
+---------------------------------+-----------------------------------------------------+

### Enable users to open direct message channels with

+-------------------------------------------------------------+-------------------------------------------+
| This setting determines whether a user can open a direct    | - System Config path: **Site              |
| message channel with anyone on the Mattermost server or     |   Configuration \> Users and Teams**      |
| only to members of the same team. This setting only affects | - `config.json` setting: `TeamSettings`   |
| the options presented in the user interface. It does not    |   \> `RestrictDirectMessage`              |
| affect permissions on the backend server.                   | - Environment variable:                   |
|                                                             |   `MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE` |
| - **Any user on the Mattermost server**: **(Default)**      |                                           |
|   Users can send a direct message to any user through the   |                                           |
|   **Direct Messages \> More** menu. `config.json` setting:  |                                           |
|   `"any"`                                                   |                                           |
| - **Any member of the team**: The **Direct Messages \>      |                                           |
|   More** menu only allows direct messages to users on the   |                                           |
|   same team. Pressing `Ctrl`{.interpreted-text role="kbd"}  |                                           |
|   `K`{.interpreted-text role="kbd"} on Windows or Linux, or |                                           |
|   `⌘`{.interpreted-text role="kbd"} `K`{.interpreted-text   |                                           |
|   role="kbd"} on Mac, only lists other users on the team    |                                           |
|   currently being viewed. A user who is a member of         |                                           |
|   multiple teams can only send direct messages to the team  |                                           |
|   that is being viewed. However, the user can receive       |                                           |
|   messages from other teams, regardless of the team         |                                           |
|   currently being viewed. `config.json` setting: `"team"`   |                                           |
+-------------------------------------------------------------+-------------------------------------------+

### Teammate name display

+---------------------------------------------------------------------+-----------------------------------------+
| This setting determines how names appear in posts and under the     | - System Config path: **Site            |
| **Direct Messages** list. Users can change this setting in their    |   Configuration \> Users and Teams**    |
| interface under **Settings \> Display \> Teammate Name Display**,   | - `config.json` setting: `TeamSettings` |
| unless this setting is locked by a system admin via the **Lock      |   \> `TeammateNameDisplay` \>           |
| teammate name display for all users** configuration setting.        |   `username`                            |
|                                                                     | - Environment variable:                 |
| - **Show username**: **(Default for self-hosted deployments)**      |   `MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY` |
|   Displays usernames. `config.json` option: `"username"`.           |                                         |
| - **Show nickname if one exists\...**: Displays the user\'s         |                                         |
|   nickname. If the user doesn\'t have a nickname, their full name   |                                         |
|   is displayed. If the user doesn\'t have a full name, their        |                                         |
|   username is displayed. `config.json` option:                      |                                         |
|   `"nickname_full_name"`.                                           |                                         |
| - **Show first and last name**: **(Default for Cloud deployments)** |                                         |
|   Displays user\'s full name. If the user doesn\'t have a full      |                                         |
|   name, their username is displayed. Recommended when using         |                                         |
|   `SAML </administration-guide/onboard/sso-saml>`{.interpreted-text |                                         |
|   role="doc"} or                                                    |                                         |
|   `LDAP </administration-guide/onboard/ad-ldap>`{.interpreted-text  |                                         |
|   role="doc"} if first name and last name attributes are            |                                         |
|   configured. `config.json` option: `"full_name"`.                  |                                         |
+---------------------------------------------------------------------+-----------------------------------------+

### Lock teammate name display for all users

+---------------------------------------+---------------------------------------------+
| This setting controls whether users   | - System Config path: **Site Configuration  |
| can change settings under **Settings  |   \> Users and Teams**                      |
| \> Display \> Teammate Name           | - `config.json` setting: `TeamSettings` \>  |
| Display**.                            |   `LockTeammateNameDisplay` \> `false`      |
|                                       | - Environment variable:                     |
| - **true**: Users **cannot** change   |   `MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY` |
|   the Teammate Name Display.          |                                             |
| - **false**: **(Default)** Users can  |                                             |
|   change the Teammate Name Display    |                                             |
|   setting.                            |                                             |
+---------------------------------------+---------------------------------------------+

### Allow users to view archived channels

+-------------------------------------+------------------------------------------------------+
| - **true**: **(Default)** Allows    | - System Config path: **Site Configuration \> Users  |
|   users to access the content of    |   and Teams**                                        |
|   archived channels of which they   | - `config.json` setting: `TeamSettings` \>           |
|   were a member.                    |   `ExperimentalViewArchivedChannels` \> `true`       |
| - **false**: Users are unable to    | - Environment variable:                              |
|   access content in archived        |   `MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS` |
|   channels.                         |                                                      |
+-------------------------------------+------------------------------------------------------+

:::: note
::: title
Note
:::

\- From Mattermost v11, this configuration setting is always enabled and
no longer configurable. Users can always access archived channels where
they are members. - Cloud admins can\'t modify this configuration
setting.
::::

### Show email address

+-------------------------------------+-----------------------------------------+
| - **true**: **(Default)** All users | - System Config path: **Site            |
|   can see the email addresses of    |   Configuration \> Users and teams**    |
|   every other user.                 | - `config.json` setting:                |
| - **false**: Hides email addresses  |   `PrivacySettings` \>                  |
|   in the client user interface,     |   `ShowEmailAddress` \> `true`          |
|   except from system admins and the | - Environment variable:                 |
|   System Roles with read/write      |   `MM_PRIVACYSETTINGS_SHOWEMAILADDRESS` |
|   access to Compliance, Billing, or |                                         |
|   User Management                   |                                         |
|   (users/teams/channels/groups      |                                         |
|   etc).                             |                                         |
+-------------------------------------+-----------------------------------------+

### Show full name

+-----------------------------------------+-------------------------------------+
| - **true**: **(Default)** Full names    | - System Config path: **Site        |
|   are visible to all users in the       |   Configuration \> Users and        |
|   client user interface.                |   Teams**                           |
| - **false**: Hides full names from all  | - `config.json` setting:            |
|   users, except system admins. Username |   `PrivacySettings` \>              |
|   is shown in place of the full name.   |   `ShowFullName` \> `true`          |
|                                         | - Environment variable:             |
|                                         |   `MM_PRIVACYSETTINGS_SHOWFULLNAME` |
+-----------------------------------------+-------------------------------------+

### Enable custom user statuses

+-------------------------------------+----------------------------------------------+
| - **true**: **(Default)** Users can | - System Config path: **Site Configuration   |
|   set status messages and emojis    |   \> Users and Teams**                       |
|   that are visible to all users.    | - `config.json` setting: `TeamSettings` \>   |
| - **false**: Users cannot set       |   `EnableCustomUserStatuses` \> `true`       |
|   custom statuses.                  | - Environment variable:                      |
|                                     |   `MM_TEAMSETTINGS_ENABLECUSTOMUSERSTATUSES` |
+-------------------------------------+----------------------------------------------+

### Enable last active time

+-------------------------------------+------------------------------------------+
| - **true**: **(Default)** Users can | - System Config path: **Site             |
|   see when deactivated users were   |   Configuration \> Users and Teams**     |
|   last active on a user\'s profile  | - `config.json` setting: `TeamSettings`  |
|   and in direct message channel     |   \> `EnableLastActiveTime` \> `true`    |
|   headers.                          | - Environment variable:                  |
| - **false**: Users can\'t see when  |   `MM_TEAMSETTINGS_ENABLELASTACTIVETIME` |
|   deactivated users were last       |                                          |
|   online.                           |                                          |
+-------------------------------------+------------------------------------------+

### Enable custom user groups

+-------------------------------------+-------------------------------------------+
| - **true**: **(Default)** Users     | - System Config path: **Site              |
|   with appropriate permissions can  |   Configuration \> Users and Teams**      |
|   create custom user groups, and    | - `config.json` setting:                  |
|   users can \@mention custom user   |   `ServiceSettings` \>                    |
|   groups in Mattermost              |   `EnableCustomGroups` \> `true`          |
|   conversations.                    | - Environment variable:                   |
| - **false**: Custom user groups     |   `MM_SERVICESETTINGS_ENABLECUSTOMGROUPS` |
|   cannot be created.                |                                           |
+-------------------------------------+-------------------------------------------+

### User statistics update time

+-----------------------------------+------------------------------------------------+
| Set the server time for updating  | - System Config path: **Site Configuration \>  |
| the user post statistics,         |   Users and Teams**                            |
| including each user\'s total      | - `config.json` setting: `ServiceSettings` \>  |
| message count, and the timestamp  |   `RefreshPostStatsRunTime` \> `00:00`         |
| of each user\'s most recently     | - Environment variable:                        |
| sent message.                     |   `MM_SERVICESETTINGS_REFRESHPOSTSTATSRUNTIME` |
|                                   |                                                |
| Must be a 24-hour time stamp in   |                                                |
| the form `HH:MM` based on the     |                                                |
| local time of the server. Default |                                                |
| is **00:00**.                     |                                                |
+-----------------------------------+------------------------------------------------+

------------------------------------------------------------------------

## Notifications

Access the following configuration settings in the System Console by
going to **Site Configuration \> Notifications**.

### Show \@channel, \@all, or \@here confirmation dialog

+------------------------------------------+---------------------------------------------------------+
| - **true**: **(Default)** Requires users | - System Config path: **Site Configuration \>           |
|   to confirm when posting \@channel,     |   Notifications**                                       |
|   \@all, \@here, or group mentions in    | - `config.json` setting: `TeamSettings` \>              |
|   channels with more than 5 members.     |   `EnableConfirmNotificationsToChannel` \> `true`       |
| - **false**: No confirmation is          | - Environment variable:                                 |
|   required.                              |   `MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL` |
+------------------------------------------+---------------------------------------------------------+

### Enable email notifications

+----------------------------------------------+---------------------------------------------+
| - **true**: **(Default)** Enables automatic  | - System Config path: **Site Configuration  |
|   email notifications for posts.             |   \> Notifications**                        |
| - **false**: Disables notifications. A       | - `config.json` setting: `EmailSettings` \> |
|   developer may choose this option to speed  |   `SendEmailNotifications` \> `ture`        |
|   development by skipping email setup (see   | - Environment variable:                     |
|   also the **Enable preview mode banner**    |   `MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS` |
|   setting).                                  |                                             |
+----------------------------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

\- Cloud admins can\'t modify this configuration setting. - If this
setting is **false**, and the SMTP server is set up, account-related
emails (such as authentication messages) will be sent regardless of this
setting. - Email invitations and account deactivation emails aren\'t
affected by this setting. - If you don\'t plan on
`configuring Mattermost for email </administration-guide/configure/smtp-email>`{.interpreted-text
role="doc"}, disabling this configuration setting in larger deployments
may improve server performance in the following areas, particularly in
high-traffic environments where performance is a key concern:

- **Reduced Server Load**: Generating and sending emails requires
  processing power and resources. By disabling email notifications, you
  reduce the load on the server, which can be reallocated to other
  tasks.
- **Decreased I/O Operations**: Sending emails involves input/output
  (I/O) operations, such as writing to logs and databases, and handling
  communication with the email server. Reducing these I/O operations can
  improve overall system efficiency.
- **Lowered Network Traffic**: Each email sent contributes to network
  traffic. Disabling email notifications decreases the amount of data
  being transmitted, which can lead to better performance, especially in
  environments with limited bandwidth.
- **Faster Response Times**: With fewer background tasks (like sending
  emails) to handle, the application can potentially respond to user
  requests more quickly, improving perceived performance.
- **Resource Allocation**: Resources like CPU cycles, memory, and
  network bandwidth that would have been used for sending emails can be
  used elsewhere, possibly improving the performance of other critical
  components of the system.
- However, disabling email notifications can negatively impact user
  experience, communication efficiency, and overall productivity. It\'s
  important to balance performance improvements with the needs of your
  organization and users.
::::

### Enable preview mode banner {#email-preview-mode-banner-config}

+----------------------------------------------+----------------------------------------------+
| - **true**: **(Default)** When **Send email  | - System Config path: **Site Configuration   |
|   notifications** is **false**, users see    |   \> Notifications**                         |
|   the Preview Mode banner. This banner       | - `config.json` setting: `EmailSettings` \>  |
|   alerts users that email notifications are  |   `EnablePreviewModeBanner` \> `true`        |
|   disabled.                                  | - Environment variable:                      |
| - **false**: Preview Mode banner does not    |   `MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER` |
|   appear.                                    |                                              |
+----------------------------------------------+----------------------------------------------+

:::: note
::: title
Note
:::

Cloud admins can\'t modify this configuration setting.
::::

### Enable email batching

+----------------------------------+------------------------------------------+
| - **true**: Multiple email       | - System Config path: **Site             |
|   notifications for mentions and |   Configuration \> Notifications**       |
|   direct messages over a given   | - `config.json` setting: `EmailSettings` |
|   time period are batched into a |   \> `EnableEmailBatching` \> `false`    |
|   single email.                  | - Environment variable:                  |
| - **false**: **(Default)** Email |   `MM_EMAILSETTINGS_ENABLEEMAILBATCHING` |
|   notifications are sent for     |                                          |
|   each mention or direct         |                                          |
|   message.                       |                                          |
+----------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

- Cloud admins can\'t modify this configuration setting.
- The
  `Site Url <administration-guide/configure/environment-configuration-settings:site url>`{.interpreted-text
  role="ref"} and
  `SMTP Email Server <administration-guide/configure/environment-configuration-settings:smtp server>`{.interpreted-text
  role="ref"} must be configured to allow email batching.
- Regardless of how this setting is configured, users can
  `disable email-based notifications altogether <end-user-guide/preferences/manage-your-notifications:email notifications>`{.interpreted-text
  role="ref"}.
- When email batching is enabled, users can
  `customize how often to receive batched notifications <end-user-guide/preferences/manage-your-notifications:email notifications>`{.interpreted-text
  role="ref"}. The default frequency is 15 minutes.
- Email batching in
  `High Availability Mode <administration-guide/configure/environment-configuration-settings:enable high availability mode>`{.interpreted-text
  role="ref"} is planned, but not yet supported.
::::

### Email notification contents

+------------------------------------------------------+----------------------------------------------------+
| - **Send full message contents**: **(Default)**      | - System Config path: **Site Configuration \>      |
|   Email notifications include the full message       |   Notifications**                                  |
|   contents, along with the name of the sender and    | - `config.json` setting: `EmailSettings` \>        |
|   the channel. `config.json` setting: `"full"`       |   `EmailNotificationContentsType`                  |
| - **Send generic description with only sender        | - Environment variable:                            |
|   name**: Only the name of the sender and team name  |   `MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE` |
|   are included in email notifications. Use this      |                                                    |
|   option if Mattermost contains confidential         |                                                    |
|   information and policy dictates it cannot be       |                                                    |
|   stored in email. `config.json` setting:            |                                                    |
|   `"generic"`                                        |                                                    |
+------------------------------------------------------+----------------------------------------------------+

### Notification display name

+------------------------------------------+-----------------------------------+
| Display name for email notifications     | - System Config path: **Site      |
| sent from the Mattermost system.         |   Configuration \>                |
|                                          |   Notifications**                 |
| String input. No default setting. This   | - `config.json` setting:          |
| field is required when changing settings |   `EmailSettings` \>              |
| in the System Console.                   |   `FeedbackName`                  |
|                                          | - Environment variable:           |
|                                          |   `MM_EMAILSETTINGS_FEEDBACKNAME` |
+------------------------------------------+-----------------------------------+

### Notification from address

+--------------------------------------------+------------------------------------+
| Email address for notification emails from | - System Config path: **Site       |
| the Mattermost system. This address should |   Configuration \> Notifications** |
| be monitored by a system admin.            | - `config.json` setting:           |
|                                            |   `EmailSettings` \>               |
| String input. Default is                   |   `FeedbackEmail`                  |
| `test@example.com`. This field is required | - Environment variable:            |
| when changing settings in the System       |   `MM_EMAILSETTINGS_FEEDBACKEMAIL` |
| Console.                                   |                                    |
+--------------------------------------------+------------------------------------+

:::: note
::: title
Note
:::

Cloud admins can\'t modify this configuration setting.
::::

### Support email address

+--------------------------------------------------------+-------------------------------------+
| Sets a user support (or feedback) email address that   | - System Config path: **Site        |
| is displayed on email notifications and during the     |   Configuration \> Notifications**  |
| Getting Started tutorial. This address should be       | - `config.json` setting:            |
| monitored by a system admin. If no value is set, email |   `SupportSettings` \>              |
| notifications will not contain a way for users to      |   `SupportEmail`                    |
| request assistance.                                    | - Environment variable:             |
|                                                        |   `MM_SUPPORTSETTINGS_SUPPORTEMAIL` |
| String input. Default is `feedback@mattermost.com`.    |                                     |
| This field is required when changing settings in the   |                                     |
| System Console.                                        |                                     |
+--------------------------------------------------------+-------------------------------------+

### Notification reply-to address

+------------------------------------------------+-------------------------------------+
| Email address used in the reply-to header when | - System Config path: **Site        |
| sending notification emails from the           |   Configuration \> Notifications**  |
| Mattermost system. This address should be      | - `config.json` setting:            |
| monitored by a system admin.                   |   `EmailSettings` \>                |
|                                                |   `ReplyToAddress`                  |
| String input. Default is `test@example.com`.   | - Environment variable:             |
|                                                |   `MM_EMAILSETTINGS_REPLYTOADDRESS` |
+------------------------------------------------+-------------------------------------+

### Notification footer mailing address

+----------------------------------------------+-------------------------------------------+
| Optional setting to include the              | - System Config path: **Site              |
| organization\'s name and mailing address in  |   Configuration \> Notifications**        |
| the footer of email notifications. If not    | - `config.json` setting: `EmailSettings`  |
| set, nothing will appear.                    |   \> `FeedbackOrganization`               |
|                                              | - Environment variable:                   |
| String input.                                |   `MM_EMAILSETTINGS_FEEDBACKORGANIZATION` |
+----------------------------------------------+-------------------------------------------+

### Push notification contents

+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| - **Generic description with only sender name**: Push notifications include the sender\'s name, but not the channel name or  | - System Config path: **Site Configuration \> |
|   message contents. `config.json` setting: `"generic_no_channel"`                                                            |   Notifications**                             |
|                                                                                                                              | - `config.json` setting: `EmailSettings` \>   |
| - **Generic description with sender and channel names**: **(Default)** Push notifications include the name of the sender and |   `PushNotificationContents`                  |
|   channel, but not the message contents. `config.json` setting: `"generic"`                                                  | - Environment variable:                       |
|                                                                                                                              |   `MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS` |
| - **Full message content sent in the notification payload**: Includes the message contents in the push notification payload, |                                               |
|   which may be sent through [Apple\'s Push Notification                                                                      |                                               |
|   service](https://developer.apple.com/documentation/usernotifications) or [Google\'s Firebase Cloud                         |                                               |
|   Messaging](https://firebase.google.com/docs/cloud-messaging) . We **highly recommended** this option only be used with an  |                                               |
|   `https` protocol to encrypt the connection and protect confidential information. `config.json` setting: `"full"`           |                                               |
|                                                                                                                              |                                               |
| - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification       |                                               |
|   payload contains no message content. Instead it contains a unique message ID used to fetch message content from the        |                                               |
|   Mattermost server when a push notification is received via a [notification service app                                     |                                               |
|   extension](https://developer.apple.com/documentation/usernotifications/modifying-content-in-newly-delivered-notifications) |                                               |
|   on iOS or [an expandable notification pattern](https://developer.android.com/develop/ui/views/notifications/expanded) on   |                                               |
|   Android.                                                                                                                   |                                               |
|                                                                                                                              |                                               |
|   If the server cannot be reached, a generic push notification is displayed without message content or sender name. For      |                                               |
|   customers who wrap the Mattermost mobile application in a secure container, the container must fetch the message contents  |                                               |
|   using the unique message ID when push notifications are received.                                                          |                                               |
|                                                                                                                              |                                               |
|   If the container is unable to execute the fetch, the push notification contents cannot be received by the customer\'s      |                                               |
|   mobile application without passing the message contents through Apple\'s or Google\'s notification service. `config.json`  |                                               |
|   setting: `"id_loaded"`                                                                                                     |                                               |
+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

### Enable notification monitoring

+----------------------+--------------------------------------------------+
| Enable or disable    | - System Config path: **Environment \>           |
| notification metrics |   Performance Monitoring**                       |
| data collection.     | - `config.json` setting: `MetricsSettings` \>    |
|                      |   `EnableNotificationMetrics` \> `true`          |
| - **true**:          | - Environment variable:                          |
|   **(Default)**      |   `MM_METRICSSETTINGS_ENABLENOTIFICATIONMETRICS` |
|   Mattermost         |                                                  |
|   notification data  |                                                  |
|   collection is      |                                                  |
|   enabled for        |                                                  |
|   client-side web    |                                                  |
|   and desktop app    |                                                  |
|   users.             |                                                  |
| - **false**:         |                                                  |
|   Mattermost         |                                                  |
|   notification data  |                                                  |
|   collection is      |                                                  |
|   disabled.          |                                                  |
+----------------------+--------------------------------------------------+

:::: note
::: title
Note
:::

See the
`performance monitoring <administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring:getting started>`{.interpreted-text
role="ref"} documentation to learn more about Mattermost Notification
Health metrics.
::::

------------------------------------------------------------------------

## System-wide notifications

Access the following configuration settings in the System Console by
going to **Site Configuration \> System-wide notifications**.

### Enable system-wide notifications

+-----------------------------+---------------------------------------------------------+
| - **true**: Enable          | - System Config path: **Site Configuration \>           |
|   system-wide notifications |   System-wide notifications**                           |
|   to display at the top of  | - `config.json` setting: `AnnouncementSettings` \>      |
|   the Mattermost interface  |   `SystemWideNotifications` \> `false`                  |
|   for all users across all  | - Environment variable:                                 |
|   teams.                    |   `MM_ANNOUNCEMENTSETTINGS_SYSTEMWIDENOTIFICATIONS`     |
| - **false**: **(Default)**  |                                                         |
|   Disable system-wide       |                                                         |
|   notifications.            |                                                         |
+-----------------------------+---------------------------------------------------------+

### Banner text

+-----------------------------+-------------------------------------------+
| The text of the system-wide | - System Config path: **Site              |
| notification, when enabled. |   Configuration \> System-wide            |
|                             |   notifications**                         |
| String input.               | - `config.json` setting:                  |
|                             |   `AnnouncementSettings` \> `BannerText`  |
|                             | - Environment variable:                   |
|                             |   `MM_ANNOUNCEMENTSETTINGS_BANNERTEXT`    |
+-----------------------------+-------------------------------------------+

### Banner color

+--------------------------+-------------------------------------------+
| The background color of  | - System Config path: **Site              |
| system-wide              |   Configuration \> System-wide            |
| notifications.           |   notifications**                         |
|                          | - `config.json` setting:                  |
| String input of a CSS    |   `AnnouncementSettings` \> `BannerColor` |
| color value.             |   \> `"#f2a93b"`                          |
|                          | - Environment variable:                   |
|                          |   `MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR`   |
+--------------------------+-------------------------------------------+

### Banner text color

+-------------------------+---------------------------------------------+
| The color of the text   | - System Config path: **Site Configuration  |
| in system-wide          |   \> System-wide notifications**            |
| notifications.          | - `config.json` setting:                    |
|                         |   `AnnouncementSettings` \>                 |
| String input of a CSS   |   `BannerTextColor` \> `"#333333"`          |
| color value.            | - Environment variable:                     |
|                         |   `MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR` |
+-------------------------+---------------------------------------------+

### Allow banner dismissal

+--------------------------------+--------------------------------------------------+
| - **true**: **(Default)**      | - System Config path: **Site Configuration \>    |
|   Users can dismiss the        |   System-wide notifications**                    |
|   system-wide notification. It | - `config.json` setting: `AnnouncementSettings`  |
|   will re-appear the next time |   \> `AllowBannerDismissal` \> `true`            |
|   the user logs in, and when   | - Environment variable:                          |
|   the text is updated by an    |   `MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL` |
|   admin, or when an admin      |                                                  |
|   disables system-wide         |                                                  |
|   notifications and reenables  |                                                  |
|   them.                        |                                                  |
| - **false**: Users cannot      |                                                  |
|   dismiss the banner.          |                                                  |
+--------------------------------+--------------------------------------------------+

------------------------------------------------------------------------

## Emoji

Access the following configuration settings in the System Console by
going to **Site Configuration \> Emoji**.

### Enable emoji picker

+--------------------------------------+------------------------------------------+
| - **true**: **(Default)** Enables an | - System Config path: **Site             |
|   emoji picker when composing        |   Configuration \> Emoji**               |
|   messages and for message           | - `config.json` setting:                 |
|   reactions.                         |   `ServiceSettings` \>                   |
| - **false**: Disables the emoji      |   `EnableEmojiPicker` \> `true`          |
|   picker in message composition and  | - Environment variable:                  |
|   reactions.                         |   `MM_SERVICESETTINGS_ENABLEEMOJIPICKER` |
+--------------------------------------+------------------------------------------+

### Enable custom emoji

+---------------------------------+------------------------------------------+
| - **true**: **(Default)**       | - System Config path: **Site             |
|   Allows users to add up to     |   Configuration \> Emoji**               |
|   6000 emojis through a         | - `config.json` setting:                 |
|   **Custom Emoji** option in    |   `ServiceSettings` \>                   |
|   the emoji picker. Emojis can  |   `EnableCustomEmoji` \> `true`          |
|   be GIF, PNG, or JPG files up  | - Environment variable:                  |
|   to 512 KB in size.            |   `MM_SERVICESETTINGS_ENABLECUSTOMEMOJI` |
| - **false**: Disables custom    |                                          |
|   emojis.                       |                                          |
+---------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

While Mattermost supports up to 6000 custom emojis, an increase in
custom emojis can slow your server\'s performance.
::::

------------------------------------------------------------------------

## Posts

Access the following configuration settings in the System Console by
going to **Site Configuration \> Posts**.

### Automatically follow threads

+-------------------------------------+-----------------------------------------+
| - **true**: **(Default)** Enables   | - System Config path: **Site            |
|   automatic following for all       |   Configuration \> Posts**              |
|   threads that a user starts, or in | - `config.json` setting:                |
|   which the user participates or is |   `ServiceSettings` \>                  |
|   mentioned. A **Threads** table in |   `ThreadAutoFollow` \> `true`          |
|   the database tracks threads and   | - Environment variable:                 |
|   thread participants. A            |   `MM_SERVICESETTINGS_THREADAUTOFOLLOW` |
|   **ThreadMembership** table tracks |                                         |
|   followed threads for each user    |                                         |
|   and whether the thread is read or |                                         |
|   unread.                           |                                         |
| - **false**: Disables automatic     |                                         |
|   following of threads.             |                                         |
+-------------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable to self-hosted deployments only. - This
setting **must** be enabled for
`threaded discussions </end-user-guide/collaborate/organize-conversations>`{.interpreted-text
role="doc"} to function. - Enabling this setting does not automatically
follow threads based on previous user actions. For example, threads a
user participated in prior to enabling this setting won\'t be
automatically followed, unless the user adds a new comment or is
mentioned in the thread.
::::

### Threaded discussions

:::: important
::: title
Important
:::

Customers upgrading from a legacy Mattermost release prior to v7.0 must
review the [administrator\'s guide to enabling threaded
discussions](https://support.mattermost.com/hc/en-us/articles/6880701948564-Administrator-s-guide-to-enabling-Collapsed-Reply-Threads)
(formerly known as Collapsed Reply Threads) prior to enabling this
functionality.
::::

+---------------------------------------------------------------------------+-----------------------------------------+
| - **Always On**: **(Default)** Enables `threaded discussions              | - System Config path: **Site            |
|   </end-user-guide/collaborate/organize-conversations>`{.interpreted-text |   Configuration \> Posts**              |
|   role="doc"} on the server and for all users. This is the recommended    | - `config.json` setting:                |
|   configuration for optimal user experience and to ensure consistency in  |   `ServiceSettings` \>                  |
|   how users read and respond to threaded conversations. `config.json`     |   `CollapsedThreads`                    |
|   setting: `"always_on"`                                                  | - Environment variable:                 |
| - **Default On**: Enables threaded discussions on the server and for all  |   `MM_SERVICESETTINGS_COLLAPSEDTHREADS` |
|   users.                                                                  |                                         |
| - **Default Off**: Enables threaded discussions on the server but **not** |                                         |
|   for users.                                                              |                                         |
| - **Disabled**: Users cannot enable threaded discussions. `config.json`   |                                         |
|   setting: `"disabled"`                                                   |                                         |
+---------------------------------------------------------------------------+-----------------------------------------+

### Message priority

:::: tip
::: title
Tip
:::

[Mattermost Enterprise or Professional](https://mattermost.com/pricing)
customers can additionally request message acknowledgements to track
that specific, time-sensitive messages have been seen and actioned. See
the
`message priority </end-user-guide/collaborate/message-priority>`{.interpreted-text
role="doc"} documentation to learn more.
::::

+---------------------------------+-------------------------------------+
| - **true**: **(Default)**       | - System Config path: **Site        |
|   Enables message priority for  |   Configuration \> Posts**          |
|   all users which enables them  | - `config.json` setting:            |
|   to set a visual indiciator    |   `ServiceSettings` \>              |
|   for important or urgent root  |   `PostPriority` \> `true`          |
|   messages.                     | - Environment variable:             |
| - **false**: Disables the       |   `MM_SERVICESETTINGS_POSTPRIORITY` |
|   ability to set message        |                                     |
|   priority and request          |                                     |
|   acknowledgements.             |                                     |
+---------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

Disabling this configuration setting in larger deployments may improve
server performance in the following areas, particularly in environments
where performance and responsiveness are critical:

- Simplified Processing: When post priority is enabled, the system has
  to manage and prioritize posts based on their designated priority
  levels. This adds additional processing overhead as the system must
  evaluate and sort posts accordingly. By disabling this feature, all
  posts are treated equally, which simplifies the processing logic and
  reduces the computational load.
- Reduced Latency: With post priority enabled, there might be delays
  introduced while the system determines the priority of each post and
  processes them in the correct order. Disabling post priority can lead
  to more consistent and potentially quicker handling of posts because
  the system processes them on a first-come, first-served basis.
- Lower Resource Utilization: Managing post priorities can consume
  additional system resources such as CPU and memory. Disabling this
  feature can free up these resources, allowing the system to allocate
  them to other tasks, thereby improving overall performance.
- Improved Scalability: In a high-traffic environment, the complexity of
  managing post priorities can become more pronounced. Disabling this
  feature simplifies the system\'s operations, making it easier to scale
  as the number of users and posts increases.
::::

### Persistent notifications

+------------------------------+-----------------------------------------------------+
| - **true**: **(Default)**    | - System Config path: **Site Configuration \>       |
|   Users can trigger          |   Posts**                                           |
|   repeating notifications to | - `config.json` setting: `ServiceSettings` \>       |
|   mentioned recipients of    |   `AllowPersistentNotifications` \> `true`          |
|   urgent messages.           | - Environment variable:                             |
| - **false**: Disables the    |   `MM_SERVICESETTINGS_ALLOWPERSISTENTNOTIFICATIONS` |
|   ability to send repeating  |                                                     |
|   notifications.             |                                                     |
+------------------------------+-----------------------------------------------------+

### Maximum number of recipients for persistent notifications

+---------------------------+------------------------------------------------------------+
| The maximum number of     | - System Config path: **Site Configuration \> Posts**      |
| recipients users may send | - `config.json` setting: `ServiceSettings` \>              |
| persistent notifications  |   `PersistentNotificationMaxRecipients` \> `5`             |
| to.                       | - Environment variable:                                    |
|                           |   `MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXRECIPIENTS` |
| Numerical input. Default  |                                                            |
| is **5**.                 |                                                            |
+---------------------------+------------------------------------------------------------+

### Frequency of persistent notifications

+--------------------------+--------------------------------------------------------------+
| The number of minutes    | - System Config path: **Site Configuration \> Posts**        |
| between repeated         | - `config.json` setting: `ServiceSettings` \>                |
| notifications for urgent |   `PersistentNotificationIntervalMinutes` \> `5`             |
| messages sent with       | - Environment variable:                                      |
| persistent               |   `MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONINTERVALMINUTES` |
| notifications.           |                                                              |
|                          |                                                              |
| Numerical input. Default |                                                              |
| is **5**. Minimum is     |                                                              |
| **2**.                   |                                                              |
+--------------------------+--------------------------------------------------------------+

### Total number of persistent notifications per post

+---------------------------+-------------------------------------------------------+
| The maximum number of     | - System Config path: **Site Configuration \> Posts** |
| times users may receive   | - `config.json` setting: `ServiceSettings` \>         |
| persistent notifications. |   `PersistentNotificationMaxCount` \> `6`             |
|                           | - Environment variable:                               |
| Numerical input. Default  |   `MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXCOUNT` |
| is **6**.                 |                                                       |
+---------------------------+-------------------------------------------------------+

### Enable burn-on-read messages

`Burn-on-read messages <end-user-guide/collaborate/send-messages:send burn-on-read messages>`{.interpreted-text
role="ref"} have irreversible behavior:

- Once a recipient reveals a burn-on-read message, it can\'t be hidden
  again.
- Once a burn-on-read message expires or is burned, it is permanently
  deleted and can\'t be recovered.
- Recipients can\'t reply to, edit, or thread burn-on-read messages.

+---------------------------------------+-----------------------------------------+
| Enable or disable burn-on-read        | - System Config path: **Site            |
| messages.                             |   Configuration \> Posts**              |
|                                       | - `config.json` setting:                |
| - **false**: **(Default)** The option |   `ServiceSettings` \>                  |
|   to send a burn-on-read message      |   `EnableBurnOnRead` \> `false`         |
|   isn\'t available.                   | - Environment variable:                 |
| - **true**: Users can send            |   `MM_SERVICESETTINGS_ENABLEBURNONREAD` |
|   burn-on-read messages in channels,  |                                         |
|   direct messages, and group          |                                         |
|   messages.                           |                                         |
+---------------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

Disabling this feature prevents users from sending new burn-on-read
messages. Once disabled, users can interact with existing burn-on-read
messages.
::::

### Burn-on-read duration

+---------------------------------------+--------------------------------------------------+
| Sets the countdown duration for       | - System Config path: **Site Configuration \>    |
| burn-on-read messages once they are   |   Posts**                                        |
| revealed. After a recipient reveals a | - `config.json` setting: `ServiceSettings` \>    |
| burn-on-read message, the message is  |   `BurnOnReadDurationSeconds` \> `600`           |
| deleted for that user after the       | - Environment variable:                          |
| specified duration. This setting      |   `MM_SERVICESETTINGS_BURNONREADDURATIONSECONDS` |
| applies to all burn-on-read messages. |                                                  |
|                                       |                                                  |
| Numerical input in seconds. Default   |                                                  |
| is **600** seconds (10 minutes).      |                                                  |
+---------------------------------------+--------------------------------------------------+

### Maximum time to live for burn-on-read messages

+---------------------------------------+-----------------------------------------------------------+
| Sets the maximum duration that        | - System Config path: **Site Configuration \> Posts**     |
| burn-on-read messages can exist after | - `config.json` setting: `ServiceSettings` \>             |
| they are sent. The message is deleted |   `BurnOnReadMaximumTimeToLiveSeconds` \> `604800`        |
| after the specified duration, even if | - Environment variable:                                   |
| it hasn\'t been revealed by all       |   `MM_SERVICESETTINGS_BURNONREADMAXIMUMTIMETOLIVESECONDS` |
| recipients.                           |                                                           |
|                                       |                                                           |
| Numerical input in seconds. Default   |                                                           |
| is **604800** seconds (7 days).       |                                                           |
+---------------------------------------+-----------------------------------------------------------+

### Enable website link previews

:::: important
::: title
Important
:::

The server must be connected to the internet to generate previews. This
connection can be established through a
`firewall or outbound proxy <deployment-guide/server/preparations:outbound proxy configuration>`{.interpreted-text
role="ref"} if necessary.
::::

+---------------------------------------------------+-------------------------------------------+
| - **true**: The server generates a preview of the | - System Config path: **Site              |
|   first website, image, or YouTube video linked   |   Configuration \> Posts**                |
|   in a message. Users can disable website         | - `config.json` setting:                  |
|   previews, but not image or YouTube previews,    |   `ServiceSettings` \>                    |
|   under **Settings \> Display \> Website Link     |   `EnableLinkPreviews` \> `true`          |
|   Previews**.                                     | - Environment variable:                   |
| - **false**: **(Default)** All previews are       |   `MM_SERVICESETTINGS_ENABLELINKPREVIEWS` |
|   disabled and the server does not request        |                                           |
|   metadata for any links contained in messages.   |                                           |
+---------------------------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

Disabling this configuration setting in larger deployments may improve
server performance in the following areas:

- Reduced Network Requests: When link previews are enabled, the system
  needs to fetch metadata (such as title, description, or image) from
  the linked webpage. This requires additional network requests, which
  can slow down the system.
- Lower Server Load: Creating link previews involves parsing the content
  of the linked pages. If many users are sharing links, the server will
  have to perform numerous network requests and process a lot of
  additional data, increasing the load on the server.
- Less Data Processing: Every link shared needs to be processed to
  extract the necessary preview information. This processing consumes
  CPU and memory resources, which can otherwise be reserved for other
  tasks.
- Decreased Client-Side Rendering Time: On the client side, rendering
  link previews (adding text, images, and layouts) takes time and
  resources. Disabling link previews means that clients do not need to
  render these elements, leading to faster message display.
- Saved Bandwidth: Link previews often include images and other data
  from the linked content. By disabling them, you save the bandwidth
  that would be used to download these additional resources.
- However, disabling link previews can negatively impact user
  experience, communication efficiency, and overall productivity. It\'s
  important to balance performance improvements with the needs of your
  organization and users.
::::

### Disable link previews for specific domains

+----------------------------------------+---------------------------------------------+
| Use this setting to disable previews   | - System Config path: **Site Configuration  |
| of links for specific domains.         |   \> Posts**                                |
|                                        | - `config.json` setting: `ServiceSettings`  |
| String input of a comma-separated list |   \> `RestrictLinkPreviews`                 |
| of domains, for example:               | - Environment variable:                     |
| `"mattermost.com, images.example.com"` |   `MM_SERVICESETTINGS_RESTRICTLINKPREVIEWS` |
+----------------------------------------+---------------------------------------------+

### Enable message link previews

+----------------------------------------------------------------------------------------------------+------------------------------------------------+
| - **true**: **(Default)**                                                                          | - System Config path: **Site Configuration \>  |
|   `Share links to Mattermost messages </end-user-guide/collaborate/share-links>`{.interpreted-text |   Posts**                                      |
|   role="doc"} will generate a preview for any users that have access to the original message.      | - `config.json` setting: `ServiceSettings` \>  |
| - **false**: Share links do not generate a preview.                                                |   `EnablePermalinkPreviews` \> `true`          |
|                                                                                                    | - Environment variable:                        |
|                                                                                                    |   `MM_SERVICESETTINGS_ENABLEPERMALINKPREVIEWS` |
+----------------------------------------------------------------------------------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

Disabling this configuration setting in larger deployments may improve
server performance in the following areas, particularly in environments
with high message throughput or limited resources:

- Reduced Server Load: When permalink previews are enabled, the server
  has to generate preview summaries for each shared link. This generates
  additional requests to fetch metadata and may involve parsing web
  pages, which increases the processing load on the server.
- Less Data Transfer: Permalink previews include additional metadata
  such as images, titles, and descriptions. Disabling previews reduces
  the amount of data that needs to be transferred, which can decrease
  bandwidth usage and improve message load times, particularly for
  channels with a high volume of links.
- Faster Message Rendering: On the client-side, rendering messages with
  multimedia previews takes more time compared to plain text messages.
  Disabling previews can reduce rendering complexity and improve client
  performance, especially on devices with limited resources.
- Network Latency: Fetching metadata for link previews may introduce
  network latency, as the server must reach out to external resources.
  Disabling this can eliminate these delays, ensuring faster message
  processing and display.
- Simplified Message Handling: In the absence of previews, messages are
  simpler and less resource-intensive to store, retrieve, and display.
  This can contribute to overall improved system responsiveness and
  efficiency.
- However, disabling permalink previews can negatively impact user
  experience, communication efficiency, and overall productivity. It\'s
  important to balance performance improvements with the needs of your
  organization and users.
::::

### Enable SVGs

+-----------------------------------+-----------------------------------+
| - **true**: Enables previews of   | - System Config path: **Site      |
|   SVG files attached to messages. |   Configuration \> Posts**        |
| - **false**: **(Default)**        | - `config.json` setting:          |
|   Disables previews of SVG files. |   `ServiceSettings` \>            |
|                                   |   `EnableSVGs` \> `false`         |
|                                   | - Environment variable:           |
|                                   |   `MM_SERVICESETTINGS_ENABLESVGS` |
+-----------------------------------+-----------------------------------+

:::: warning
::: title
Warning
:::

Enabling SVGs is not recommended in environments where not all users are
trusted.
::::

### Enable LaTeX code block rendering

+-------------------------------------------------------------------------------------------------------+------------------------------------+
| - **true**: Enables rendering of                                                                      | - System Config path: **Site       |
|   `LaTeX in code blocks <end-user-guide/collaborate/format-messages:math formulas>`{.interpreted-text |   Configuration \> Posts**         |
|   role="ref"}.                                                                                        | - `config.json` setting:           |
| - **false**: **(Default)** Disables rendering in blocks. Instead, LaTeX code is highlighted.          |   `ServiceSettings` \>             |
|                                                                                                       |   `EnableLatex` \> `false`         |
|                                                                                                       | - Environment variable:            |
|                                                                                                       |   `MM_SERVICESETTINGS_ENABLELATEX` |
+-------------------------------------------------------------------------------------------------------+------------------------------------+

:::: warning
::: title
Warning
:::

Enabling LaTeX rendering is not recommended in environments where not
all users are trusted.
::::

### Enable inline LaTeX rendering

+--------------------------------------------------------------------------------------------------------+------------------------------------------+
| - **true**: Enables rendering of                                                                       | - System Config path: **Site             |
|   `LaTeX in message text <end-user-guide/collaborate/format-messages:math formulas>`{.interpreted-text |   Configuration \> Posts**               |
|   role="ref"}.                                                                                         | - `config.json` setting:                 |
| - **false**: **(Default)** Disables inline rendering of LaTeX. Instead, LaTeX in message text is       |   `ServiceSettings` \>                   |
|   highlighted. LaTeX can also be rendered in a code block, if that feature is enabled. See **Enable    |   `EnableInlineLatex` \> `false`         |
|   LaTeX code block rendering**.                                                                        | - Environment variable:                  |
|                                                                                                        |   `MM_SERVICESETTINGS_ENABLEINLINELATEX` |
+--------------------------------------------------------------------------------------------------------+------------------------------------------+

:::: warning
::: title
Warning
:::

Enabling LaTeX rendering isn\'t recommended in environments where not
all users are trusted.
::::

### Custom URL schemes

+--------------------------------------------------+-----------------------------------------+
| A list of URL schemes that will automatically    | - System Config path: **Site            |
| create a link in message text, for example:      |   Configuration \> Posts**              |
| `["git", "smtp"]`. These schemes always create   | - `config.json` setting:                |
| links: `http`, `https`, `ftp`, `tel`, and        |   `DisplaySettings` \>                  |
| `mailto`.                                        |   `CustomURLSchemes` \> `[]`            |
|                                                  | - Environment variable:                 |
| `config.json` setting: an array of strings       |   `MM_DISPLAYSETTINGS_CUSTOMURLSCHEMES` |
+--------------------------------------------------+-----------------------------------------+

### Maximum Markdown nodes

+------------------------------+-----------------------------------------+
| The maximum number of        | - System Config path: **Site            |
| Markdown elements (such as   |   Configuration \> Posts**              |
| emojis, links, or table      | - `config.json` setting:                |
| cells), that can be included |   `DisplaySettings` \>                  |
| in a single piece of text in |   `MaxMarkdownNodes` \> `0`             |
| a message.                   | - Environment variable:                 |
|                              |   `MM_DISPLAYSETTINGS_MAXMARKDOWNNODES` |
| Numerical input. Default is  |                                         |
| **0** which applies a        |                                         |
| Mattermost-specified limit.  |                                         |
+------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

This limit applies to all Mattermost clients, including web, desktop
app, and mobile app.
::::

### Google API key

+-------------------------------------------------------+-------------------------------------------+
| If a key is provided in this setting, Mattermost      | - System Config path: **Site              |
| displays titles of embedded YouTube videos and        |   Configuration \> Posts**                |
| detects if a video is no longer available. Setting a  | - `config.json` setting:                  |
| key should also prevent Google from throttling access |   `ServiceSettings` \>                    |
| to embedded videos that receive a high number of      |   `GoogleDeveloperKey`                    |
| views.                                                | - Environment variable:                   |
|                                                       |   `MM_SERVICESETTINGS_GOOGLEDEVELOPERKEY` |
| String input.                                         |                                           |
+-------------------------------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

- This setting is applicable to self-hosted deployments only.
- This key is used in client-side Javascript, and must have the YouTube
  Data API added as a service.
::::

### Enable server syncing of message drafts

+--------------------------+-------------------------------------------+
| Enable or disable the    | - System Config path: **Site              |
| ability to synchronize   |   Configuration \> Posts**                |
| draft messages across    | - `config.json` setting:                  |
| all supported Mattermost |   `ServiceSettings` \>                    |
| clients.                 |   `AllowSyncedDrafts` \> `true`           |
|                          | - Environment variable:                   |
| - **true**:              |   `MM_SERVICESETTINGS_ALLOWSYNCEDDRAFTS`  |
|   **(Default)** Message  |                                           |
|   drafts are saved on    |                                           |
|   the server and may be  |                                           |
|   accessed from          |                                           |
|   different clients.     |                                           |
|   Users may still        |                                           |
|   disable server         |                                           |
|   synchronization of     |                                           |
|   draft messages by      |                                           |
|   going to **Settings \> |                                           |
|   Advanced Settings**.   |                                           |
| - **false**: Draft       |                                           |
|   messages are stored    |                                           |
|   locally on each        |                                           |
|   device.                |                                           |
+--------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

While drafts can be very useful for maintaining work continuity,
especially in collaborative environments, disabling draft
synchronization across devices can lead to noticeable performance
improvements by reducing the computational and data management overhead
as follows:

- Reduced Data Synchronization: When drafts are enabled and synchronized
  across devices, the system needs to handle those data synchronization
  operations which can consume significant bandwidth and computing
  resources. Disabling draft syncing reduces the load on servers and
  networks.
- Lower Storage Usage: Storing drafts requires additional database
  operations and storage space. Each draft is an extra piece of data
  that needs to be saved, managed, and retrieved. Without drafts, the
  system has fewer records to keep, which can streamline database
  operations.
- Decreased Client Processing: On the client side, draft management
  involves monitoring changes, saving drafts periodically, and handling
  conflict resolution if multiple drafts are edited from different
  devices. Disabling drafts reduces these client-side processes, thus
  freeing up memory and CPU resources.
- Simplified Architecture: Maintaining synced drafts often requires
  complex backend logic to ensure consistency and avoid data conflicts.
  Simplifying this architecture by removing draft syncing can lead to
  more efficient and faster backend operations.
- Improved User Experience: Users may experience faster load times and
  reduced latency without the overhead of draft syncing. This can be
  particularly noticeable in environments with limited or variable
  internet connectivity.
- However, disabling draft synchronization can negatively impact user
  experience, communication efficiency, and overall productivity. It\'s
  important to balance performance improvements with the needs of your
  organization and users.
::::

### Unique emoji reaction limit

+------------------------+--------------------------------------------------------+
| Limit the number of    | - System Config path: **Site Configuration \> Posts**  |
| unique emoji reactions | - `config.json` setting: `ServiceSettings` \>          |
| on each message.       |   `UniqueEmojiReactionLimitPerPost` \> `50`            |
| Increasing this limit  | - Environment variable:                                |
| can lead to poor       |   `MM_SERVICESETTINGS_UNIQUEEMOJIREACTIONLIMITPERPOST` |
| client performance.    |                                                        |
|                        |                                                        |
| Numerical input.       |                                                        |
| Default is **50**.     |                                                        |
| Maximum is 500.        |                                                        |
+------------------------+--------------------------------------------------------+

------------------------------------------------------------------------

## Content flagging

Access the following configuration settings in the System Console by
going to **Site Configuration \> Content Flagging**.

### Enable content flagging

+------------------------+------------------------------------------------------+
| - **true**: Enables    | - System Config path: **Site Configuration \>        |
|   the Content Flagging |   Content Flagging**                                 |
|   feature.             | - `config.json` setting: `ContentFlaggingSettings`   |
| - **false**:           |   \> `EnableContentFlagging` \> `false`              |
|   **(Default)**        | - Environment variable:                              |
|   Disables the         |   `MM_CONTENTFLAGGINGSETTINGS_ENABLECONTENTFLAGGING` |
|   feature.             |                                                      |
+------------------------+------------------------------------------------------+

### Notification settings

+-----------------------+-----------------------------------------------+
| Default notification  | - System Config path: **Site Configuration \> |
| recipients for each   |   Content Flagging**                          |
| event:                | - `config.json` setting:                      |
|                       |   `ContentFlaggingSettings` \>                |
| - Events: flagged,    |   `NotificationSettings` \>                   |
|   assigned, removed,  |   `EventTargetMapping`                        |
|   dismissed           | - Environment variable: N/A                   |
| - Recipients:         |                                               |
|   reviewers, author,  |                                               |
|   reporter            |                                               |
|                       |                                               |
| Default mappings      |                                               |
| include:              |                                               |
|                       |                                               |
| - flagged = reviewers |                                               |
| - assigned =          |                                               |
|   reviewers           |                                               |
| - removed =           |                                               |
|   reviewers, author,  |                                               |
|   reporter            |                                               |
| - dismissed =         |                                               |
|   reviewers, reporter |                                               |
+-----------------------+-----------------------------------------------+

### Additional settings

+------------------------+---------------------------------------------+
| Specify the reasons    | - System Config path: **Site Configuration  |
| for flagging.          |   \> Content Flagging**                     |
|                        | - `config.json` setting:                    |
| Default reasons        |   `ContentFlaggingSettings` \>              |
| include:               |   `AdditionalSettings` \> `Reasons`         |
|                        | - Environment variable: N/A                 |
| - Inappropriate        |                                             |
|   content              |                                             |
| - Sensitive data       |                                             |
| - Security concern     |                                             |
| - Harassment or abuse  |                                             |
| - Spam or phishing     |                                             |
+------------------------+---------------------------------------------+

### Require reporters to add comment

+-------------------------+---------------------------------------------------------------------------+
| - **true**:             | - System Config path: **Site Configuration \> Content Flagging**          |
|   **(Default)**         | - `config.json` setting: `ContentFlaggingSettings` \>                     |
|   Reporters must add a  |   `AdditionalSettings` \> `ReporterCommentRequired` \> `true`             |
|   comment when          | - Environment variable:                                                   |
|   flagging.             |   `MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_REPORTERCOMMENTREQUIRED` |
| - **false**: Reporters  |                                                                           |
|   aren\'t required to   |                                                                           |
|   add a comment.        |                                                                           |
+-------------------------+---------------------------------------------------------------------------+

### Require reviewers to add comment

+-------------------------+---------------------------------------------------------------------------+
| - **true**:             | - System Config path: **Site Configuration \> Content Flagging**          |
|   **(Default)**         | - `config.json` setting: `ContentFlaggingSettings` \>                     |
|   Reviewers must add a  |   `AdditionalSettings` \> `ReviewerCommentRequired` \> `true`             |
|   comment when          | - Environment variable:                                                   |
|   reviewing flagged     |   `MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_REVIEWERCOMMENTREQUIRED` |
|   content.              |                                                                           |
| - **false**: Reviewers  |                                                                           |
|   aren\'t required to   |                                                                           |
|   add a comment.        |                                                                           |
+-------------------------+---------------------------------------------------------------------------+

### Hide message from channel while it is being reviewed

+-------------------------+----------------------------------------------------------------------+
| - **true**:             | - System Config path: **Site Configuration \> Content Flagging**     |
|   **(Default)** Hide    | - `config.json` setting: `ContentFlaggingSettings` \>                |
|   flagged content from  |   `AdditionalSettings` \> `HideFlaggedContent` \> `true`             |
|   the channel while     | - Environment variable:                                              |
|   under review.         |   `MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_HIDEFLAGGEDCONTENT` |
| - **false**: Keep       |                                                                      |
|   flagged content       |                                                                      |
|   visible while under   |                                                                      |
|   review.               |                                                                      |
+-------------------------+----------------------------------------------------------------------+

### Same reviewers for all teams

+----------------------+-----------------------------------------------------------------+
| - **true**:          | - System Config path: **Site Configuration \> Content           |
|   **(Default)** Use  |   Flagging**                                                    |
|   the same set of    | - `config.json` setting: `ContentFlaggingSettings` \>           |
|   reviewers across   |   `ReviewerSettings` \> `CommonReviewers` \> `true`             |
|   all teams.         | - Environment variable:                                         |
| - **false**:         |   `MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_COMMONREVIEWERS` |
|   Reviewers can be   |                                                                 |
|   managed per team.  |                                                                 |
+----------------------+-----------------------------------------------------------------+

### System administrators as reviewers

+---------------------+-------------------------------------------------------------------------+
| - **true**: Include | - System Config path: **Site Configuration \> Content Flagging**        |
|   system            | - `config.json` setting: `ContentFlaggingSettings` \>                   |
|   administrators as |   `ReviewerSettings` \> `SystemAdminsAsReviewers` \> `false`            |
|   reviewers.        | - Environment variable:                                                 |
| - **false**:        |   `MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_SYSTEMADMINSASREVIEWERS` |
|   **(Default)**     |                                                                         |
|   System            |                                                                         |
|   administrators    |                                                                         |
|   are not included  |                                                                         |
|   by default.       |                                                                         |
+---------------------+-------------------------------------------------------------------------+

### Team administrators as reviewers

+----------------------+-----------------------------------------------------------------------+
| - **true**:          | - System Config path: **Site Configuration \> Content Flagging**      |
|   **(Default)**      | - `config.json` setting: `ContentFlaggingSettings` \>                 |
|   Include team       |   `ReviewerSettings` \> `TeamAdminsAsReviewers` \> `true`             |
|   administrators as  | - Environment variable:                                               |
|   reviewers for      |   `MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_TEAMADMINSASREVIEWERS` |
|   their respective   |                                                                       |
|   teams.             |                                                                       |
| - **false**: Team    |                                                                       |
|   administrators     |                                                                       |
|   aren\'t included   |                                                                       |
|   as reviewers.      |                                                                       |
+----------------------+-----------------------------------------------------------------------+

------------------------------------------------------------------------

## File sharing and downloads

Access the following configuration settings in the System Console by
going to **Site Configuration \> File Sharing and Downloads**.

### Allow file sharing

+---------------------------------------------+-------------------------------------------+
| - **true**: **(Default)** Allows users to   | - System Config path: **Site              |
|   attach files to messages.                 |   Configuration \> File Sharing and       |
| - **false**: Prevents users from attaching  |   Downloads**                             |
|   files (including images) to a message.    | - `config.json` setting: `FileSettings`   |
|   This affects users on all clients and     |   \> `EnableFileAttachments` \> `true`    |
|   devices, including mobile apps.           | - Environment variable:                   |
|                                             |   `MM_FILESETTINGS_ENABLEFILEATTACHMENTS` |
+---------------------------------------------+-------------------------------------------+

### Allow file uploads on mobile

+-------------------------------------+----------------------------------------+
| - **true**: **(Default)** Allows    | - System Config path: **Site           |
|   users to attach files to messages |   Configuration \> File Sharing and    |
|   from mobile apps.                 |   Downloads**                          |
| - **false**: Prevents users from    | - `config.json` setting:               |
|   attaching files (including        |   `FileSettings` \>                    |
|   images) to messages from mobile   |   `EnableMobileUpload` \> `true`       |
|   apps.                             | - Environment variable:                |
|                                     |   `MM_FILESETTINGS_ENABLEMOBILEUPLOAD` |
+-------------------------------------+----------------------------------------+

### Allow file downloads on mobile

+---------------------------------------+------------------------------------------+
| - **true**: **(Default)** Enables     | - System Config path: **Site             |
|   file downloads on mobile apps.      |   Configuration \> File sharing and      |
| - **false**: Disables file downloads  |   downloads**                            |
|   on mobile apps. Users can still     | - `config.json` setting: `FileSettings`  |
|   download files from a mobile web    |   \> `EnableMobileDownload` \> `true`    |
|   browser.                            | - Environment variable:                  |
|                                       |   `MM_FILESETTINGS_ENABLEMOBILEDOWNLOAD` |
+---------------------------------------+------------------------------------------+

### Enable secure file preview on mobile

This setting improves an organization\'s mobile security posture by
restricting file access while still allowing essential file viewing
capabilities.

+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| - **true**: Prevents file downloads, previews, and sharing for most file types, even when the                                                    | - System Config path: **Site Configuration \>     |
|   `Allow file downloads on mobile <administration-guide/configure/site-configuration-settings:allow file downloads on mobile>`{.interpreted-text |   File sharing and downloads**                    |
|   role="ref"} configuration setting is enabled. Allows in-app previews for PDFs, videos, and images only. Files are stored temporarily in the    | - `config.json` setting: `FileSettings` \>        |
|   app\'s cache and cannot be exported or shared.                                                                                                 |   `MobileEnableSecureFilePreview` \> `false`      |
| - **false**: **(Default)** Secure file preview mode is disabled.                                                                                 | - Environment variable:                           |
|                                                                                                                                                  |   `MM_FILESETTINGS_MOBILEENABLESECUREFILEPREVIEW` |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+

### Allow PDF link navigation on mobile

+------------------------------+--------------------------------------------------+
| - **true**: **(Default)**    | - System Config path: **Site Configuration \>    |
|   Enables tapping links      |   File sharing and downloads**                   |
|   inside PDFs when Secure    | - `config.json` setting: `FileSettings` \>       |
|   File Preview Mode is       |   `MobileAllowPdfLinkNavigation` \> `true`       |
|   active. Links will open in | - Environment variable:                          |
|   the device browser or      |   `MM_FILESETTINGS_MOBILEALLOWPDFLINKNAVIGATION` |
|   supported app.             |                                                  |
| - **false**: Disables link   |                                                  |
|   navigation in PDFs when    |                                                  |
|   Secure File Preview Mode   |                                                  |
|   is active.                 |                                                  |
+------------------------------+--------------------------------------------------+

:::: note
::: title
Note
:::

This setting has no effect when the
`Secure file preview on mobile <administration-guide/configure/site-configuration-settings:enable secure file preview on mobile>`{.interpreted-text
role="ref"} configuration setting is disabled.
::::

------------------------------------------------------------------------

## Public Links

With self-hosted deployments, you can access the following configuration
settings in the System Console by going to **Site Configuration \>
Public Links**.

### Enable public file links

+------------------------------------------------------------------------------------------+--------------------------------------+
| - **true**: Allows users to create                                                       | - System Config path: **Site         |
|   `public links </end-user-guide/collaborate/share-files-in-messages>`{.interpreted-text |   Configuration \> Public Links**    |
|   role="doc"} to files attached to Mattermost messages.                                  | - `config.json` setting:             |
| - **false**: **(Default)** Prevents users from creating public links to files and        |   `FileSettings` \>                  |
|   disables all previously created links.                                                 |   `EnablePublicLink` \> `false`      |
|                                                                                          | - Environment variable:              |
|                                                                                          |   `MM_FILESETTINGS_ENABLEPUBLICLINK` |
+------------------------------------------------------------------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

When set to **false**, anyone who tries to visit a previously created
public link will receive an error message. If the setting is returned to
**true**, previously created links will be accessible, unless the
**Public link salt** has been regenerated.
::::

### Public link salt

+--------------------------------------------------------+------------------------------------+
| 32-character salt added to the URL of public file      | - System Config path: **Site       |
| links. Changing this setting will **invalidate** all   |   Configuration \> Public Links**  |
| previously generated links. The salt is randomly       | - `config.json` setting:           |
| generated when Mattermost is installed, and can be     |   `FileSettings` \>                |
| regenerated by selecting **Regenerate** in the System  |   `PublicLinkSalt`                 |
| Console.                                               | - Environment variable:            |
|                                                        |   `MM_FILESETTINGS_PUBLICLINKSALT` |
| String input.                                          |                                    |
+--------------------------------------------------------+------------------------------------+

------------------------------------------------------------------------

## Notices

Access the following configuration settings in the System Console by
going to **Site Configuration \> Notices**.

### Enable admin notices

+--------------------------------------------------------------------------------------------+-------------------------------------------------+
| - **true**: **(Default)** System admins will receive                                       | - System Config path: **Site Configuration \>   |
|   `in-product notices </administration-guide/manage/in-product-notices>`{.interpreted-text |   Notices** -                                   |
|   role="doc"} about server upgrades and administration features.                           | - `config.json` setting: `AnnouncementSettings` |
| - **false**: System admins will not receive specific notices. Admins will still receive    |   \> `AdminNoticesEnabled` \> `true`            |
|   notices for all users (see **Enable end user notices**)                                  | - Environment variable:                         |
|                                                                                            |   `MM_ANNOUNCEMENTSETTINGS_ADMINNOTICESENABLED` |
+--------------------------------------------------------------------------------------------+-------------------------------------------------+

### Enable end user notices

+--------------------------------------------------------------------------------------------+------------------------------------------------+
| - **true**: **(Default)** All users receive                                                | - System Config path: **Site Configuration \>  |
|   `in-product notices </administration-guide/manage/in-product-notices>`{.interpreted-text |   Notices**                                    |
|   role="doc"} about client upgrades and end user features.                                 | - `config.json` setting:                       |
| - **false**: Users will not receive in-product notices.                                    |   `AnnouncementSettings` \>                    |
|                                                                                            |   `UserNoticesEnabled` \> `true`               |
|                                                                                            | - Environment variable:                        |
|                                                                                            |   `MM_ANNOUNCEMENTSETTINGS_USERNOTICESENABLED` |
+--------------------------------------------------------------------------------------------+------------------------------------------------+

## Connected workspaces

The following settings aren\'t available in the System Console and can
only be set in `config.json`.

When connected workspaces are enabled, system admins can
`create and manage connected workspaces </administration-guide/onboard/connected-workspaces>`{.interpreted-text
role="doc"} in the System Console by going to **Site Configuration \>
Connected Workspaces**.

### Enable connected workspaces

Enable the ability to establish secure connections between Mattermost
instances, and invite secured connections to shared channels where users
can participate as they would in any public and private channel.

Connected workspaces requires Mattermost Enterprise servers running
v10.2 or later.

By default, both configuration settings are disabled and must be enabled
in order to share channels with secure connections. Enabling connected
workspace functionality requires a server restart.

This feature\'s two `config.json` settings include:

- `ConnectedWorkspacesSettings.EnableRemoteClusterService: false` with
  options `true` and `false`.
- `ConnectedWorkspacesSettings.EnableSharedChannels: false` with options
  `true` and `false`.

:::: note
::: title
Note
:::

- Neither setting is available in the System Console and can only be set
  in `config.json` under `ConnectedWorkspacesSettings`.
- System admins for Cloud deployments can submit a request to have these
  required configuration settings enabled for their Cloud deployment
  instance.
- Following an upgrade to Mattermost v10.2 or later, existing
  configuration values for shared channels, including
  `EnableSharedChannels` and `EnableRemoteClusterService` are
  automatically converted to connected workspace configuration settings
  in the `config.json` file. The
  `deprecated shared channels experimental settings <administration-guide/configure/deprecated-configuration-settings:shared channels settings>`{.interpreted-text
  role="ref"} remain in the `config.json` file to support backwards
  compatibility.
::::

### Disable shared channel status sync

Disable member status and availability synchronization between connected
workspaces.

+------------------------------------+-------------------------------------+
| - **true**: Channel as well as     | - System Config path: N/A           |
|   member status and availability   | - `config.json` setting:            |
|   isn\'t synchronized.             |   `ConnectedWorkspacesSettings` \>  |
| - **false**: **(Default)** Channel |   `DisableSharedChannelsStatusSync` |
|   as well as channel member status |   \> `false`                        |
|   and availability is synchronized | - Environment variable: N/A         |
|   at regular intervals.            |                                     |
+------------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

Enabling these features can increase the load on your Mattermost
server's CPU, memory, and database due to frequent updates, database
queries, and API communication. Excessive sync frequency and retries can
overwhelm system resources, potentially causing performance degradation
or instability. Monitor your system carefully when enabling these
features.
::::

### Default maximum posts per sync

+------------------------------+---------------------------------------+
| Define the default maximum   | - System Config path: N/A             |
| number of mesages to         | - `config.json` setting:              |
| synchronize at a time.       |   `ConnectedWorkspacesSettings` \>    |
|                              |   `DefaultMaxPostsPerSync` \> `50`    |
| Default is **50**.           | - Environment variable: N/A           |
+------------------------------+---------------------------------------+

### Sync users on connection open

Automatically synchronize users when a new connection between workspaces
is established. This ensures that remote users are immediately
discoverable for direct and group messages without requiring them to
post in a shared channel first.

+-------------------------------------+---------------------------------+
| - **true**: **(Default)** Users are | - System Config path: N/A       |
|   automatically synchronized when a | - `config.json` setting:        |
|   new connection is established.    |   `ConnectedWorkspacesSettings` |
| - **false**: Users are not          |   \>                            |
|   automatically synchronized when a |   `SyncUsersOnConnectionOpen`   |
|   new connection is established.    |   \> `true`                     |
|                                     | - Environment variable: N/A     |
+-------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

Enabling these features can increase the load on your Mattermost
server's CPU, memory, and database due to frequent updates, database
queries, and API communication. Excessive sync frequency and retries can
overwhelm system resources, potentially causing performance degradation
or instability. Monitor your system carefully when enabling these
features.
::::

### Global user sync batch size

+----------------------------+-----------------------------------------+
| The number of users to     | - System Config path: N/A               |
| sync in each batch when    | - `config.json` setting:                |
| performing global user     |   `ConnectedWorkspacesSettings` \>      |
| synchronization between    |   `GlobalUserSyncBatchSize` \> `100`    |
| connected workspaces.      | - Environment variable: N/A             |
|                            |                                         |
| Default is **100**.        |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

Enabling these features can increase the load on your Mattermost
server's CPU, memory, and database due to frequent updates, database
queries, and API communication. Excessive sync frequency and retries can
overwhelm system resources, potentially causing performance degradation
or instability. Monitor your system carefully when enabling these
features.
::::

### Member sync batch size

+----------------------------+-----------------------------------------+
| The number of channel      | - System Config path: N/A               |
| members to sync in each    | - `config.json` setting:                |
| batch when synchronizing   |   `ConnectedWorkspacesSettings` \>      |
| channel membership between |   `MemberSyncBatchSize` \> `100`        |
| connected workspaces.      | - Environment variable: N/A             |
|                            |                                         |
| Default is **100**.        |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

Enabling these features can increase the load on your Mattermost
server's CPU, memory, and database due to frequent updates, database
queries, and API communication. Excessive sync frequency and retries can
overwhelm system resources, potentially causing performance degradation
or instability. Monitor your system carefully when enabling these
features.
::::

------------------------------------------------------------------------

## config.json-only settings

The following self-hosted deployment settings are only configurable in
the `config.json` file and are not available in the System Console.

### Cross-team search

+--------------------------+----------------------------------------------+
| Disable the ability to   | - System Config path: N/A                    |
| search across all teams  | - `config.json` setting:                     |
| or a specific team.      |   `ServiceSettings.EnableCrossTeamSearch` \> |
|                          |   `true`                                     |
| - **true**:              | - Environment variable:                      |
|   **(Default)**          |   `MM_SERVICESETTINGS_ENABLECROSSTEAMSEARCH` |
|   Cross-team search is   |                                              |
|   enabled. Searches can  |                                              |
|   be performed against   |                                              |
|   all channels the user  |                                              |
|   is a member of across  |                                              |
|   all teams, a specific  |                                              |
|   team, or the current   |                                              |
|   team.                  |                                              |
| - **false**: Cross-team  |                                              |
|   search is disabled.    |                                              |
|   Searches are performed |                                              |
|   on all channels the    |                                              |
|   user is member of      |                                              |
|   within the current     |                                              |
|   team only.             |                                              |
+--------------------------+----------------------------------------------+

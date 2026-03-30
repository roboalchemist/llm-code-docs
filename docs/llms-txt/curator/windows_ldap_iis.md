# Source: https://docs.curator.interworks.com/setup/authentication/windows_ldap_iis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows LDAP

> A guide to setting up Windows LDAP authentication for Curator using IIS.

<Danger>
  Curator no longer supports IIS on new installations.
</Danger>

For current information on how to set up Active Directory on Windows, please see our
[Active Directory](/setup/authentication/active_directory) documentation.

*The information below is only for reference on legacy/existing installations.  It is *highly* recommended that you
reinstall with Apache for stability, please see our
[Windows Apache Installation](/setup/installation/windows_installation)
documentation for steps on how to achieve the best Curator experience for Windows.*

Using IIS, you can use the user's AD credentials automatically.

Enable Windows Authentication in "Add/Remove Windows Features". (Sometimes this is known as Add Roles and Features)
Server Roles > Web Server (IIS) > Web Server > Security > Window Authentication.
*Note: This may be found in the Server Manager, not IIS*

Once this is added, go to your site in IIS, click "Authentication". Change "Windows Authentication" to "Enabled" and
"Anonymous Authentication" to "Disabled".

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4b0f0275238796a2040386feb6f1cf73" alt="Authentication settings" data-og-width="500" width="500" data-og-height="220" height="220" data-path="assets/images/setup/authentication/IIS_LDAP_Pass_auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e54bb6097d77653617e5222fa3793d67 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=581e667e8b3687f1361aeb5f978d73d9 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c79b552a2fda57c22bf4cdbf2b9f9254 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=10e9850128d0cab2304bb7246ea93f3c 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=2c8cc54127d58413a8c4c64bcee0be5e 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_auth.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=76b8edbac7a45bfe156c607f0e1ccdf9 2500w" />

Go to the site in the IIS Manager and open the Configuration Editor

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=83cf0ea21d5e6f27930a70e59a42b678" alt="Configuration editor" data-og-width="250" width="250" data-og-height="241" height="241" data-path="assets/images/setup/authentication/IIS_LDAP_Pass_manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=774d7c7dc294782662fb6012d283c2d5 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f7ed950b8b2042d97696c2c0cc91fd0e 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8afb686d115f367e5885d39e3212e7b7 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=84c9af8c52feaeab3add637ab6bd28c2 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=860dee484e7367915d24064f4f0aa78c 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_manager.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=bb43f0236ba21c60ce941d6294e2e5eb 2500w" />

Choose "system.webServer/serverRuntime" for the Section selection. Select UseWorkerProcessUser. Click Apply.

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=fb79802e5dbd9f360173080a224800c7" alt="Configuration editor settings" data-og-width="600" width="600" data-og-height="247" height="247" data-path="assets/images/setup/authentication/IIS_LDAP_Pass_configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=34c63331a165d16ad9c62a7c65029e1c 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=26318361db3be36103ecb47735ff5ca1 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6779c1803934aa7105990833c40e1874 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=827c208483b7ace25768f63c56060a2c 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=536974e25efe8ba3f9b66cb921d847c6 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_configure.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=3348be7537d6e52519549f2a9c3cd2b3 2500w" />

In Curator's Tableau Server Settings, select "Active Directory" as the Authentication Type.

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=5614181e730520385028ea077bca63ed" alt="Portal settings" data-og-width="600" width="600" data-og-height="297" height="297" data-path="assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e8ba02226b82213e32a6f7a82dd34896 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6d3424e65503a524eaba17f40bcfb367 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=7f8d75c384b0e10e6e2c1b9a857eb760 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=2bf1fb45903b11021984e6cc6c369400 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4699c9b938e7383c6903391b3a9cdeb6 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/IIS_LDAP_Pass_portal_settings.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a90bafcce2320cd52eeb49129c79d780 2500w" />

If you have issues, make sure to disable UAC, to allow access to the filesystem.  You can find this setting under
Control Panel > System and Security > User Account Control Settings.

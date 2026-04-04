# Source: https://firebase.google.com/docs/projects/iam/permissions.md.txt

**Permissions are granted to your project members via[*roles*](https://firebase.google.com/docs/projects/iam/roles).**A role is a collection of permissions. When you assign a role to a project member, you grant that project member all the permissions that the role contains.

This page describes the actions enabled by permissions that you might find listed in a Firebase-supported role. These permissions fall into two categories:

- [Required Identity and Access Management (IAM) permissions](https://firebase.google.com/docs/projects/iam/permissions#required-permissions)for all roles or for specific actions within Firebase

- [Firebase product-specific IAM permissions](https://firebase.google.com/docs/projects/iam/permissions#product-permissions)

| **Important:** If you're creating a[custom role](https://firebase.google.com/docs/projects/iam/roles-custom), review the sections on this page about[*required permissions*](https://firebase.google.com/docs/projects/iam/permissions#required-permissions)to ensure that you include all necessary permissions in your custom role.

## Required permissions

Firebase IAM includes permissions which are:

- [Required to use any Firebase product or service.](https://firebase.google.com/docs/projects/iam/permissions#required_all_roles)

- [Required to perform some Firebase service-specific actions.](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_service)

- [Required to perform some Firebase management-specific actions.](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_management)

For a general list and description of permissions specific to a Firebase product or service, refer to the appropriate section within[Firebase product-specific IAM permissions](https://firebase.google.com/docs/projects/iam/permissions#product-permissions).

### Required permissions included in all roles

The permissions listed in the following table are required to use any Firebase product or service.

These permissions are automatically included in each of the[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).
| If you're creating a[custom role](https://firebase.google.com/docs/projects/iam/roles-custom), you must include each of the following permissions in your custom role.

|                                                                                                            Permission                                                                                                            |                                       Description                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **firebase.\*** - firebase.clients.get - firebase.clients.list - firebase.links.list - firebase.projects.get                                                                                                                     | Grants permissions to retrieve Firebase project information                             |
| **resourcemanager.\*** - resourcemanager.projects.get - resourcemanager.projects.getIamPolicy - resourcemanager.projects.list                                                                                                    | Grants permissions to retrieve Firebase project information                             |
| **serviceusage.\*** - apikeys.keys.get - apikeys.keys.list - apikeys.keys.lookup - serviceusage.operations.get - serviceusage.operations.list - serviceusage.quotas.get - serviceusage.services.get - serviceusage.services.list | Grants permissions to check for the state of Google APIs and to runFirebaseCLI commands |

### Required permissions for Firebase service-specific actions

The permissions listed in the following table are required to perform some Firebase service-specific actions.

When needed, these permissions are automatically included in each of the[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).
| If you're creating a[custom role](https://firebase.google.com/docs/projects/iam/roles-custom), review the following list of actions to ensure that you include all necessary permissions in your custom role.

|                                                                                                                            Action                                                                                                                             |        Required permission        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Access Firebase project integrations with collaboration tools (including Slack, Jira, and PagerDuty)                                                                                                                                                          | **firebaseextensions.configs.\*** |
| View usage and analytics from StackDriver                                                                                                                                                                                                                     | **monitoring.timeSeries.list**    |
| Run[FirebaseCLI](https://firebase.google.com/docs/cli)commands For more information, refer to the Google Cloud documentation about[Runtime Configurator Access](https://cloud.google.com/deployment-manager/runtime-configurator/access-control#permissions). | **runtimeconfig.\***              |

### Required permissions for Firebase management-specific actions

The permissions listed in the following table are*additional*permissions that are required to perform some Firebase management-specific actions.
| If you're creating a[custom role](https://firebase.google.com/docs/projects/iam/roles-custom), review the following list of permissions and associated actions to ensure that you include all necessary permissions in your custom role.

|       Management permission and associated actions       |                                  Required additional permission                                   |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `firebase.billingPlans.update`                                                                                                                              ||
| Change the billing plan for a Firebase project           | resourcemanager.projects.createBillingAssignment resourcemanager.projects.deleteBillingAssignment |
| `firebase.projects.delete`                                                                                                                                  ||
| Delete a Firebase project                                | resourcemanager.projects.delete                                                                   |
| `firebase.projects.update`                                                                                                                                  ||
| Add Firebase resources to an existingGoogle Cloudproject | resourcemanager.projects.get serviceusage.services.enable serviceusage.services.get               |
| Change the name of a Firebase project                    | resourcemanager.projects.update                                                                   |
| Add SHA certificate fingerprints for Android apps        | clientauthconfig.clients.create                                                                   |
| Remove SHA certificate fingerprints for Android apps     | clientauthconfig.clients.delete                                                                   |
| Update App Store ID or Team ID for Apple apps            | clientauthconfig.clients.get clientauthconfig.clients.update                                      |

## Firebase product-specific IAM permissions

The following tables list the permissions that are specific to a Firebase product or service. You can use these permissions to[create custom roles](https://cloud.google.com/iam/docs/creating-custom-roles).
| **Note:** The sections below might also include configuration options for achieving specific permissions that aren't included in the[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).

### Firebase Management permissions

Note that some of the following management permissions[require*additional*permissions for certain actions](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_management).

|            Permission name             |                                                                                 Description                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebase.billingPlans.get              | Retrieve the current[Firebase billing plan](https://firebase.google.com/pricing)for a project                                                                                |
| firebase.billingPlans.update           | Change the current[Firebase billing plan](https://firebase.google.com/pricing)for a project                                                                                  |
| firebase.clients.create                | Add new apps to a project                                                                                                                                                    |
| firebase.clients.delete                | Delete existing apps from a project                                                                                                                                          |
| firebase.clients.get                   | Retrieve details and configurations for apps in a project                                                                                                                    |
| firebase.clients.list                  | Retrieve a list of apps in a project                                                                                                                                         |
| firebase.clients.undelete              | Undelete a deleted app before its data is permanently deleted                                                                                                                |
| firebase.clients.update                | Update details and configurations for apps in a project                                                                                                                      |
| firebase.links.create                  | Create new links to Google systems (Firebaseconsole \> Project Settings \> Integrations)                                                                                     |
| firebase.links.delete                  | Delete links to Google systems (Firebaseconsole \> Project Settings \> Integrations)                                                                                         |
| firebase.links.list                    | Retrieve a list of links to Google systems (Firebaseconsole \> Project Settings \> Integrations)                                                                             |
| firebase.links.update                  | Update existing links to Google systems (Firebaseconsole \> Project Settings \> Integrations)                                                                                |
| firebase.playLinks.get                 | Retrieve details about a link to Google Play (Firebaseconsole \> Project Settings \> Integrations \> Google Play)                                                            |
| firebase.playLinks.list                | Retrieve a list of links to Google Play (Firebaseconsole \> Project Settings \> Integrations \> Google Play)                                                                 |
| firebase.playLinks.update              | Create new links and update existing links to Google Play (Firebaseconsole \> Project Settings \> Integrations \> Google Play)                                               |
| firebase.projects.delete               | Delete existing projects                                                                                                                                                     |
| firebase.projects.get                  | Retrieve details and Firebase resources for a project                                                                                                                        |
| firebase.projects.update               | Modify the attributes of an existing project Receive alerts for applicable Firebase products and features ([learn more](https://support.google.com/firebase/answer/7276542)) |
| firebaseinstallations.instances.delete | Delete a Firebase installation ID and the data tied to that installation ([learn more](https://firebase.google.com/docs/projects/manage-installations#delete-fid))           |

### Google Analyticspermissions

The following permissions grant access to theAnalyticsproperty linked to the Firebase project. They allow Firebase project members to accessAnalyticsdata, including audiences, user properties, funnels, reports, conversions, etc.
| **Note:** InGoogle Analytics, each Firebase project member, based on their highest`firebaseanalytics.*`permission, is mapped to a linked user that has a specificAnalyticsrole.Google AnalyticsAdmins can modify the defaultAnalyticsrole assigned to a linked user. For more information, see[User access (roles inAnalytics)](https://support.google.com/analytics/answer/9289234#access)in theAnalyticsHelp.
| **Note:** To grant the permissions of`firebaseanalytics.resources.googleAnalyticsAdditionalAccess`or`firebaseanalytics.resources.googleAnalyticsRestrictedAccess`to a Firebase project member, you'll need to create and assign a[custom role](https://firebase.google.com/docs/projects/iam/roles-custom).

|                       Permission name                       |                                                      Description                                                       |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| firebaseanalytics.resources.googleAnalyticsEdit             | By default, grants theAnalyticsEditor role to the linkedAnalyticsproperty                                              |
| firebaseanalytics.resources.googleAnalyticsAdditionalAccess | By default, grants theAnalyticsMarketer role to the linkedAnalyticsproperty                                            |
| firebaseanalytics.resources.googleAnalyticsReadAndAnalyze   | By default, grants theAnalyticsViewer role to the linkedAnalyticsproperty                                              |
| firebaseanalytics.resources.googleAnalyticsRestrictedAccess | By default, grants theAnalyticsViewer role to the linkedAnalyticsproperty with no access to revenue data and cost data |

| **Important:** If you linked your Firebase project to a Google Analytics 4 property before January 4, 2023, then the Firebase linked users may have different roles and data access in Analytics than described in the table above. Analytics administrators can verify and edit roles and data access from the Analytics UI (**Admin \> linked property \> Property Access Management**).

### Firebase AI Logicpermissions

|         Permission name         |                 Description                 |
|---------------------------------|---------------------------------------------|
| firebasevertexai.configs.get    | Retrieve configuration forFirebase AI Logic |
| firebasevertexai.configs.update | Update configuration forFirebase AI Logic   |

### Firebase App Checkpermissions

|                  Permission name                  |                        Description                        |
|---------------------------------------------------|-----------------------------------------------------------|
| firebaseappcheck.appAttestConfig.get              | Retrieve the App Attest configuration of an app           |
| firebaseappcheck.appAttestConfig.update           | Update the App Attest configuration of an app             |
| firebaseappcheck.appCheckTokens.verify            | VerifyApp Checktokens issued for a Firebase project       |
| firebaseappcheck.debugTokens.get                  | Retrieve debug tokens of an app                           |
| firebaseappcheck.debugTokens.update               | Create, update, or delete debug tokens of an app          |
| firebaseappcheck.deviceCheckConfig.get            | Retrieve the DeviceCheck configuration of an app          |
| firebaseappcheck.deviceCheckConfig.update         | Update the DeviceCheck configuration of an app            |
| firebaseappcheck.playIntegrityConfig.get          | Retrieve the Play Integrity configuration of an app       |
| firebaseappcheck.playIntegrityConfig.update       | Update the Play Integrity configuration of an app         |
| firebaseappcheck.recaptchaEnterpriseConfig.get    | Retrieve the reCAPTCHA Enterprise configuration of an app |
| firebaseappcheck.recaptchaEnterpriseConfig.update | Update the reCAPTCHA Enterprise configuration of an app   |
| firebaseappcheck.recaptchaV3Config.get            | Retrieve the reCAPTCHA v3 configuration of an app         |
| firebaseappcheck.recaptchaV3Config.update         | Update the reCAPTCHA v3 configuration of an app           |
| firebaseappcheck.safetyNetConfig.get              | Retrieve the SafetyNet configuration of an app            |
| firebaseappcheck.safetyNetConfig.update           | Update the SafetyNet configuration of an app              |
| firebaseappcheck.services.get                     | Retrieve service enforcement configurations of a project  |
| firebaseappcheck.services.update                  | Update service enforcement configurations of a project    |

### Firebase App Distributionpermissions

|          Permission name          |                               Description                               |
|-----------------------------------|-------------------------------------------------------------------------|
| firebaseappdistro.releases.list   | Retrieve a list of existing distributions and Invite Links              |
| firebaseappdistro.releases.update | Create, delete, and modify distributions Create and delete Invite Links |
| firebaseappdistro.testers.list    | Retrieve a list of existing testers in a project                        |
| firebaseappdistro.testers.update  | Create and delete testers in a project                                  |
| firebaseappdistro.groups.list     | Retrieve a list of existing tester groups in a project                  |
| firebaseappdistro.groups.update   | Create and delete tester groups in a project                            |

### Firebase Authenticationpermissions

|          Permission name           |                           Description                           |
|------------------------------------|-----------------------------------------------------------------|
| firebaseauth.configs.create        | Create theAuthenticationconfiguration                           |
| firebaseauth.configs.get           | Retrieve theAuthenticationconfiguration                         |
| firebaseauth.configs.getHashConfig | Get the password hash config and password hash of user accounts |
| firebaseauth.configs.getSecret     | Get the client secret in theAuthenticationconfiguration         |
| firebaseauth.configs.update        | Update the existingAuthenticationconfiguration                  |
| firebaseauth.users.create          | Create new users inAuthentication                               |
| firebaseauth.users.createSession   | Create session cookie for a logged-in user                      |
| firebaseauth.users.delete          | Delete existing users inAuthentication                          |
| firebaseauth.users.get             | Retrieve a list of existingAuthenticationusers                  |
| firebaseauth.users.sendEmail       | Send emails to the users                                        |
| firebaseauth.users.update          | Update existing users inAuthentication                          |

### Firebase A/B Testingpermissions*(beta)*

| **Caution:** These product-specific permissions are**beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.  
| Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

|          Permission name          |                       Description                        |
|-----------------------------------|----------------------------------------------------------|
| firebaseabt.experimentresults.get | Retrieve the results of an experiment                    |
| firebaseabt.experiments.create    | Create new experiments                                   |
| firebaseabt.experiments.delete    | Delete existing experiments                              |
| firebaseabt.experiments.get       | Retrieve details of an existing experiment               |
| firebaseabt.experiments.list      | Retrieve a list of existing experiments                  |
| firebaseabt.experiments.update    | Update an existing experiment                            |
| firebaseabt.projectmetadata.get   | Retrieve analytics metadata for setting up an experiment |

### Firebase App Hostingpermissions*(beta)*

| **Caution:** These product-specific permissions are**beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.  
| Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

|          Permission name           |                                                                        Description                                                                        |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebaseapphosting.backends.create | Create a newApp Hostingbackend for a Firebase project.                                                                                                    |
| firebaseapphosting.backends.delete | Delete an existingApp Hostingbackend from a Firebase project.                                                                                             |
| firebaseapphosting.backends.get    | Retrieve information about a specificApp Hostingbackend in a Firebase project.                                                                            |
| firebaseapphosting.backends.list   | List all availableApp Hostingbackends in a Firebase project.                                                                                              |
| firebaseapphosting.backends.update | Modify the configuration or settings of an existingApp Hostingbackend.                                                                                    |
| firebaseapphosting.builds.create   | Initiate a new build process for anApp Hostingbackend in a Firebase project.                                                                              |
| firebaseapphosting.builds.delete   | Delete existing builds in anApp Hostingbackend.                                                                                                           |
| firebaseapphosting.builds.get      | Retrieve details of an existing build in anApp Hostingbackend.                                                                                            |
| firebaseapphosting.builds.list     | List all builds associated with anApp Hostingbackend in a Firebase project.                                                                               |
| firebaseapphosting.builds.update   | Modify the configuration of an existing non-finalizedApp Hostingbuild.                                                                                    |
| firebaseapphosting.domains.create  | Create a new domain association for anApp Hostingbackend in a Firebase project.                                                                           |
| firebaseapphosting.domains.delete  | Remove a domain association from anApp Hostingbackend.                                                                                                    |
| firebaseapphosting.domains.get     | Retrieve information about a specific domain associated with anApp Hostingsite.                                                                           |
| firebaseapphosting.domains.list    | List all domains associated withApp Hosting.                                                                                                              |
| firebaseapphosting.domains.update  | Modify settings or configurations for a domain linked to anApp Hostingbackend.                                                                            |
| firebaseapphosting.rollouts.create | Initiate a new rollout to promote a existing build to the currently serving version for thatApp Hostingbackend.                                           |
| firebaseapphosting.rollouts.get    | Retrieve information about a specificApp Hostingrollout.                                                                                                  |
| firebaseapphosting.rollouts.list   | List all rollouts associated with anApp Hostingbackend.                                                                                                   |
| firebaseapphosting.traffic.get     | Retrieve the current traffic split and rollout policy for anApp Hostingsite.                                                                              |
| firebaseapphosting.traffic.list    | Identical in function to \`firebaseapphosting.traffic.get\`, with added capability to retrieve a list across backends for which you have this permission. |
| firebaseapphosting.traffic.update  | Modify the current traffic split and rollout policy for anApp Hostingbackend.                                                                             |

### Cloud Firestorepermissions

For a list and descriptions ofCloud Firestorepermissions, refer to the[Google Cloud documentation](https://cloud.google.com/datastore/docs/access/iam#permissions).

### Cloud Storagepermissions

For a list and descriptions ofCloud Storagepermissions, refer to the[Google Cloud documentation](https://cloud.google.com/storage/docs/access-control/iam-permissions).

### Firebase Security Rules (Cloud FirestoreandCloud Storage) permissions

| **Caution:** These permissions control access to security rules forCloud Storage***and*** forCloud Firestore.  
| For permissions that control access to security rules forFirebase Realtime Database, refer to the[Realtime Databasepermissions](https://firebase.google.com/docs/projects/iam/permissions#realtime-database).

|           Permission name            |                     Description                      |
|--------------------------------------|------------------------------------------------------|
| firebaserules.releases.create        | Create releases                                      |
| firebaserules.releases.delete        | Delete releases                                      |
| firebaserules.releases.get           | Retrieve releases                                    |
| firebaserules.releases.getExecutable | Retrieve the binary executable payloads for releases |
| firebaserules.releases.list          | Retrieve a list of releases                          |
| firebaserules.releases.update        | Update ruleset references for releases               |
| firebaserules.rulesets.create        | Create new rulesets                                  |
| firebaserules.rulesets.delete        | Delete existing ruleset                              |
| firebaserules.rulesets.get           | Retrieve rulesets with source                        |
| firebaserules.rulesets.list          | Find ruleset metadata (no source)                    |
| firebaserules.rulesets.test          | Test sources for correctness                         |

### Cloud Functions for Firebasepermissions

For a list and descriptions ofCloud Functionspermissions, refer to the[IAM documentation](https://cloud.google.com/functions/docs/reference/iam/permissions).

Be aware that the deployment of functions requires a specific configuration of permissions that aren't included in the standard[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined). To deploy functions, use one of the following options:

- Delegate the deployment of functions to a project[**Owner**](https://firebase.google.com/docs/projects/iam/roles-basic).

  If you're deploying only non-HTTP functions, then a project[**Editor**](https://firebase.google.com/docs/projects/iam/roles-basic)can deploy your functions.
- Delegate deployment of functions to a project member who has the following two roles:

  - Cloud Functions Admin role ([`roles/cloudfunctions.admin`](https://cloud.google.com/functions/docs/reference/iam/roles))
  - Service Account User role ([`roles/iam.serviceAccountUser`](https://cloud.google.com/iam/docs/service-accounts#user-role))

  A project Owner can assign these roles to a project member[using theGoogle Cloudconsole or gcloud CLI](https://cloud.google.com/iam/docs/granting-changing-revoking-access). For detailed steps and security implications for this role configuration, refer to the[IAM documentation](https://cloud.google.com/functions/docs/reference/iam/roles#additional-configuration).

### Firebase messaging campaigns permissions

These permissions apply to campaigns forFirebase Cloud MessagingandFirebase In-App Messaging.

|               Permission name               |              Description               |
|---------------------------------------------|----------------------------------------|
| firebasemessagingcampaigns.campaigns.create | Create new campaigns                   |
| firebasemessagingcampaigns.campaigns.delete | Delete existing campaigns              |
| firebasemessagingcampaigns.campaigns.get    | Retrieve details of existing campaigns |
| firebasemessagingcampaigns.campaigns.list   | Retrieve a list of existing campaigns  |
| firebasemessagingcampaigns.campaigns.update | Update existing campaigns              |
| firebasemessagingcampaigns.campaigns.start  | Start existing campaigns               |
| firebasemessagingcampaigns.campaigns.stop   | Update existing campaigns              |

### Firebase Cloud Messagingpermissions

|        Permission name         |                                Description                                |
|--------------------------------|---------------------------------------------------------------------------|
| cloudmessaging.messages.create | Send notifications and data messages through theFCMHTTP API and Admin SDK |

| The followingFirebase Cloud Messagingpermissions are deprecated. Use an appropriate[`firebasemessagingcampaigns.*`permission](https://firebase.google.com/docs/projects/iam/permissions#messaging-campaigns)instead.

|            Permission name            |                             Description                             |
|---------------------------------------|---------------------------------------------------------------------|
| firebasenotifications.messages.create | Create new messages in the Notifications composer                   |
| firebasenotifications.messages.delete | Delete existing messages in the Notifications composer              |
| firebasenotifications.messages.get    | Retrieve details of existing messages in the Notifications composer |
| firebasenotifications.messages.list   | Retrieve a list of existing messages in the Notifications composer  |
| firebasenotifications.messages.update | Update existing messages in the Notifications composer              |

### Firebase Crashlyticspermissions

|          Permission name          |                                   Description                                   |
|-----------------------------------|---------------------------------------------------------------------------------|
| firebasecrashlytics.config.get    | RetrieveCrashlyticsconfiguration settings                                       |
| firebasecrashlytics.config.update | UpdateCrashlyticsconfiguration settings                                         |
| firebasecrashlytics.data.get      | Retrieve metrics associated withCrashlyticsissues and sessions                  |
| firebasecrashlytics.issues.get    | Retrieve details aboutCrashlyticsissues, including notes attached to issues     |
| firebasecrashlytics.issues.list   | Retrieve a list ofCrashlyticsissues                                             |
| firebasecrashlytics.issues.update | Open, close, and mute existingCrashlyticsissues Update notes attached to issues |
| firebasecrashlytics.sessions.get  | Retrieve details aboutCrashlyticscrash sessions                                 |

|       Permission name       |                                                                                                              Description                                                                                                               |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebasecrash.issues.update | | *Deprecated.* Use an appropriate[`firebasecrashlytics.*`permission](https://firebase.google.com/docs/projects/iam/permissions#crashlytics)instead. Update existingCrashlyticsissues, create notes on issues, and set velocity alerts |
| firebasecrash.reports.get   | | *Deprecated.* Use an appropriate[`firebasecrashlytics.*`permission](https://firebase.google.com/docs/projects/iam/permissions#crashlytics)instead. Retrieve existingCrashlyticsreports                                               |

### Firebase Dynamic Linkspermissions

|             Permission name              |                   Description                    |
|------------------------------------------|--------------------------------------------------|
| firebasedynamiclinks.domains.create      | Create newDynamic Linksdomains                   |
| firebasedynamiclinks.domains.delete      | Delete existingDynamic Linksdomains              |
| firebasedynamiclinks.domains.get         | Retrieve details of existingDynamic Linksdomains |
| firebasedynamiclinks.domains.list        | Retrieve a list of existingDynamic Linksdomains  |
| firebasedynamiclinks.domains.update      | Update existingDynamic Linksdomains              |
| firebasedynamiclinks.links.create        | Create newDynamic Links                          |
| firebasedynamiclinks.links.get           | Retrieve details of existingDynamic Links        |
| firebasedynamiclinks.links.list          | Retrieve a list of existingDynamic Links         |
| firebasedynamiclinks.links.update        | Update existingDynamic Links                     |
| firebasedynamiclinks.stats.get           | RetrieveDynamic Linksstatistics                  |
| firebasedynamiclinks.destinations.list   | Retrieve existingDynamic Linksdestinations       |
| firebasedynamiclinks.destinations.update | Update existingDynamic Linksdestinations         |

### Firebase Extensionspublishing permissions

|                Permission name                |                          Description                           |
|-----------------------------------------------|----------------------------------------------------------------|
| firebaseextensionspublisher.extensions.create | Upload new versions of an extension                            |
| firebaseextensionspublisher.extensions.delete | Delete or deprecate versions of an extension                   |
| firebaseextensionspublisher.extensions.get    | Retrieve details about an extension version                    |
| firebaseextensionspublisher.extensions.list   | List all extension versions uploaded by this publisher project |

### Firebase Hostingpermissions

| [Custom roles](https://firebase.google.com/docs/projects/iam/roles-custom)cannot currently be used for controlling access toFirebase Hostingresources. To grant a project member access toHosting, you can assign them one of the following predefined roles (as appropriate for their access needs):  
| [Firebase Develop Admin or Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-category#develop_roles)or[Firebase HostingAdmin or Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-product#hosting).

|       Permission name        |                                                                Description                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| firebasehosting.sites.create | Create new[Hostingresources](https://firebase.google.com/docs/hosting/manage-hosting-resources)for a Firebase project                      |
| firebasehosting.sites.delete | Delete existing[Hostingresources](https://firebase.google.com/docs/hosting/manage-hosting-resources)for a Firebase project                 |
| firebasehosting.sites.get    | Retrieve details of an existing[Hostingresources](https://firebase.google.com/docs/hosting/manage-hosting-resources)for a Firebase project |
| firebasehosting.sites.list   | Retrieve a list of[Hostingresources](https://firebase.google.com/docs/hosting/manage-hosting-resources)for a Firebase project              |
| firebasehosting.sites.update | Update existing[Hostingresources](https://firebase.google.com/docs/hosting/manage-hosting-resources)for a Firebase project                 |

### Firebase In-App Messagingpermissions*(beta)*

| **Caution:** These product-specific permissions are**beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.  
| Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.
| The followingFirebase In-App Messagingpermissions are deprecated. Use an appropriate[`firebasemessagingcampaigns.*`permission](https://firebase.google.com/docs/projects/iam/permissions#messaging-campaigns)instead.

|             Permission name             |              Description               |
|-----------------------------------------|----------------------------------------|
| firebaseinappmessaging.campaigns.create | Create new campaigns                   |
| firebaseinappmessaging.campaigns.delete | Delete existing campaigns              |
| firebaseinappmessaging.campaigns.get    | Retrieve details of existing campaigns |
| firebaseinappmessaging.campaigns.list   | Retrieve a list of existing campaigns  |
| firebaseinappmessaging.campaigns.update | Update existing campaigns              |

### Firebase MLpermissions*(beta)*

| **Caution:** These product-specific permissions are**beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.  
| Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

|         Permission name         |                 Description                 |
|---------------------------------|---------------------------------------------|
| firebaseml.models.create        | Create new ML models                        |
| firebaseml.models.update        | Update existing ML models                   |
| firebaseml.models.delete        | Delete existing ML models                   |
| firebaseml.models.get           | Retrieve details of existing ML models      |
| firebaseml.models.list          | Retrieve a list of existing ML models       |
| firebaseml.modelversions.create | Create new model versions                   |
| firebaseml.modelversions.get    | Retrieve details of existing model versions |
| firebaseml.modelversions.list   | Retrieve a list of existing model versions  |
| firebaseml.modelversions.update | Update existing model versions              |

### Firebase Performance Monitoringpermissions

|          Permission name          |                       Description                        |
|-----------------------------------|----------------------------------------------------------|
| firebaseperformance.config.create | Create new issue threshold configurations                |
| firebaseperformance.config.delete | Delete existing issue threshold configurations           |
| firebaseperformance.config.update | Modify alert and existing issue threshold configurations |
| firebaseperformance.data.get      | View all performance data and issue threshold values     |

### Firebase Realtime Databasepermissions

|           Permission name           |                                                                                    Description                                                                                    |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebasedatabase.instances.create   | Create new database instances                                                                                                                                                     |
| firebasedatabase.instances.get      | Retrieve the metadata of existing database instances Read-only access to the data in an existing database instance                                                                |
| firebasedatabase.instances.list     | Retrieve a list of existing database instances                                                                                                                                    |
| firebasedatabase.instances.update   | Full read and write access to the data in existing database instances Enable and disable database instances Retrieve and modify security rules for existing database instances    |
| firebasedatabase.instances.disable  | Disable active database instances Existing data is kept but is not accessible for reads/writes.                                                                                   |
| firebasedatabase.instances.reenable | Re-enable disabled database instances Existing data is again accessible for reads/writes.                                                                                         |
| firebasedatabase.instances.delete   | Delete disabled database instances Deleted database names cannot be reused. The data in a deleted database instance is permanently deleted after 20 days.                         |
| firebasedatabase.instances.undelete | Undelete a deleted database instance before its data is permanently deleted The data in a deleted database instance is permanently deleted 20 days after the instance is deleted. |

### Firebase Remote Configpermissions

|      Permission name       |        Description        |
|----------------------------|---------------------------|
| cloudconfig.configs.get    | RetrieveRemote Configdata |
| cloudconfig.configs.update | UpdateRemote Configdata   |

### Firebase Test Labpermissions

Test Labrequires access toCloud Storagebuckets, so it requires a specific configuration of permissions that aren't all included in the standard[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined). To grant access toTest Lab, use one of the following options:

- **For tests started fromFirebaseconsole**

  - Test your app in a dedicated separate Firebase project.

  - Add members who needTest Labaccess, then assign them legacy project roles using the[Firebaseconsole](https://console.firebase.google.com/).

    - To allow a member to run tests withTest Lab, assign project**Editor**or above.
    - To allow a member to view test results inTest Lab, assign project**Viewer**or above.
- **For tests started from the[gcloud CLI](https://firebase.google.com/docs/test-lab/android/command-line), the[Testing API](https://firebase.google.com/docs/test-lab/reference/testing/rest), or[Gradle Managed Devices](https://firebase.google.com/docs/test-lab/android/android-studio#gmd-testlab-plugin)while using your ownCloud Storagebucket**

  - Assign a pair of predefined roles (which together grant the required set of permissions) using the[Google Cloudconsole](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

    - To allow a member to run tests withTest Lab, assign both:

      - Firebase Test Lab Admin (`roles/cloudtestservice.testAdmin`)
      - Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)
    - To allow a member to view test results inTest Lab, assign both:

      - Firebase Test Lab Viewer (`roles/cloudtestservice.testViewer`)
      - Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)

| **Caution:** Members assigned these predefined roles can access*all* Cloud Storagebuckets associated with the Firebase project, potentially including customer data.

|             Permission name             |                              Description                               |
|-----------------------------------------|------------------------------------------------------------------------|
| cloudtestservice.environmentcatalog.get | Retrieve the catalog of supported test environments for a project      |
| cloudtestservice.matrices.create        | Request to run a matrix of tests according to the given specifications |
| cloudtestservice.matrices.get           | Retrieve the status of a test matrix                                   |
| cloudtestservice.matrices.update        | Update an unfinished test matrix                                       |
| cloudtoolresults.executions.list        | Retrieve a list of Executions for a History                            |
| cloudtoolresults.executions.get         | Retrieve an existing Execution                                         |
| cloudtoolresults.executions.create      | Create a new Execution                                                 |
| cloudtoolresults.executions.update      | Update an existing Execution                                           |
| cloudtoolresults.histories.list         | Retrieve a list of Histories                                           |
| cloudtoolresults.histories.get          | Retrieve an existing History                                           |
| cloudtoolresults.histories.create       | Create a new History                                                   |
| cloudtoolresults.settings.create        | Create new tool results settings                                       |
| cloudtoolresults.settings.get           | Retrieve existing tool results settings                                |
| cloudtoolresults.settings.update        | Update tool results settings                                           |
| cloudtoolresults.steps.list             | Retrieve a list of Steps for an Execution                              |
| cloudtoolresults.steps.get              | Retrieve an existing Step                                              |
| cloudtoolresults.steps.create           | Create a new Step                                                      |
| cloudtoolresults.steps.update           | Update an existing Step                                                |

### Integrations with external services permissions

|          Permission name          |                                                       Description                                                       |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| firebaseextensions.configs.create | Create new extension configurations for external services (Firebaseconsole \> Project Settings \> Integrations)         |
| firebaseextensions.configs.delete | Delete existing extension configurations for external services (Firebaseconsole \> Project Settings \> Integrations)    |
| firebaseextensions.configs.list   | Retrieve a list of extension configurations for external services (Firebaseconsole \> Project Settings \> Integrations) |
| firebaseextensions.configs.update | Update existing extension configurations for external services (Firebaseconsole \> Project Settings \> Integrations)    |
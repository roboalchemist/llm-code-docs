# Source: https://firebase.google.com/docs/projects/iam/permissions.md.txt

# Firebase IAM permissions

**Permissions are granted to your project members via
[*roles*](https://firebase.google.com/docs/projects/iam/roles).** A role is a collection of permissions.
When you assign a role to a project member, you grant that project member all
the permissions that the role contains.

This page describes the actions enabled by permissions that you might find
listed in a Firebase-supported role. These permissions fall into two categories:

- [Required Identity and Access Management (IAM) permissions](https://firebase.google.com/docs/projects/iam/permissions#required-permissions)
  for all roles or for specific actions within Firebase

- [Firebase product-specific IAM permissions](https://firebase.google.com/docs/projects/iam/permissions#product-permissions)

> [!IMPORTANT]
> **Important:** If you're creating a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom), review the sections on this page about [*required permissions*](https://firebase.google.com/docs/projects/iam/permissions#required-permissions) to ensure that you include all necessary permissions in your custom role.

## Required permissions

Firebase IAM includes permissions which are:

- [Required to use any Firebase product or service.](https://firebase.google.com/docs/projects/iam/permissions#required_all_roles)

- [Required to perform some Firebase service-specific actions.](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_service)

- [Required to perform some Firebase management-specific actions.](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_management)

For a general list and description of permissions specific to a Firebase product
or service, refer to the appropriate section within
[Firebase product-specific IAM permissions](https://firebase.google.com/docs/projects/iam/permissions#product-permissions).

### Required permissions included in all roles

The permissions listed in the following table are required to use any
Firebase product or service.

These permissions are automatically included in each of the
[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).

> [!CAUTION]
> If you're creating a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom), you must include each of the following permissions in your custom role.

| Permission | Description |
|---|---|
| **firebase.\*** - firebase.clients.get - firebase.clients.list - firebase.links.list - firebase.projects.get | Grants permissions to retrieve Firebase project information |
| **resourcemanager.\*** - resourcemanager.projects.get - resourcemanager.projects.getIamPolicy - resourcemanager.projects.list | Grants permissions to retrieve Firebase project information |
| **serviceusage.\*** - apikeys.keys.get - apikeys.keys.list - apikeys.keys.lookup - serviceusage.operations.get - serviceusage.operations.list - serviceusage.quotas.get - serviceusage.services.get - serviceusage.services.list | Grants permissions to check for the state of Google APIs and to run Firebase CLI commands |

### Required permissions for Firebase service-specific actions

The permissions listed in the following table are required to perform some
Firebase service-specific actions.

When needed, these permissions are automatically included in each of the
[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).

> [!CAUTION]
> If you're creating a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom), review the following list of actions to ensure that you include all necessary permissions in your custom role.

| Action | Required permission |
|---|---|
| Access Firebase project integrations with collaboration tools (including Slack, Jira, and PagerDuty) | **firebaseextensions.configs.\*** |
| View usage and analytics from StackDriver | **monitoring.timeSeries.list** |
| Run [Firebase CLI](https://firebase.google.com/docs/cli) commands For more information, refer to the Google Cloud documentation about [Runtime Configurator Access](https://cloud.google.com/deployment-manager/runtime-configurator/access-control#permissions). | **runtimeconfig.\*** |

### Required permissions for Firebase management-specific actions

The permissions listed in the following table are *additional* permissions that
are required to perform some Firebase management-specific actions.

> [!CAUTION]
> If you're creating a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom), review the following list of permissions and associated actions to ensure that you include all necessary permissions in your custom role.

| Management permission and associated actions | Required additional permission |
|---|---|
| `firebase.billingPlans.update` ||
| Change the billing plan for a Firebase project | resourcemanager.projects.createBillingAssignment resourcemanager.projects.deleteBillingAssignment |
| `firebase.projects.delete` ||
| Delete a Firebase project | resourcemanager.projects.delete |
| `firebase.projects.update` ||
| Add Firebase resources to an existing Google Cloud project | resourcemanager.projects.get serviceusage.services.enable serviceusage.services.get |
| Change the name of a Firebase project | resourcemanager.projects.update |
| Add SHA certificate fingerprints for Android apps | clientauthconfig.clients.create |
| Remove SHA certificate fingerprints for Android apps | clientauthconfig.clients.delete |
| Update App Store ID or Team ID for Apple apps | clientauthconfig.clients.get clientauthconfig.clients.update |

## Firebase product-specific IAM permissions

The following tables list the permissions that are specific to a Firebase
product or service. You can use these permissions to
[create custom roles](https://cloud.google.com/iam/docs/creating-custom-roles).

> [!NOTE]
> **Note:** The sections below might also include configuration options for achieving specific permissions that aren't included in the [Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).

### Firebase Management permissions

Note that some of the following management permissions
[require *additional* permissions for certain actions](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_management).

| Permission name | Description |
|---|---|
| firebase.billingPlans.get | Retrieve the current [Firebase billing plan](https://firebase.google.com/pricing) for a project |
| firebase.billingPlans.update | Change the current [Firebase billing plan](https://firebase.google.com/pricing) for a project |
| firebase.clients.create | Add new apps to a project |
| firebase.clients.delete | Delete existing apps from a project |
| firebase.clients.get | Retrieve details and configurations for apps in a project |
| firebase.clients.list | Retrieve a list of apps in a project |
| firebase.clients.undelete | Undelete a deleted app before its data is permanently deleted |
| firebase.clients.update | Update details and configurations for apps in a project |
| firebase.links.create | Create new links to Google systems (Firebase console \> Project Settings \> Integrations) |
| firebase.links.delete | Delete links to Google systems (Firebase console \> Project Settings \> Integrations) |
| firebase.links.list | Retrieve a list of links to Google systems (Firebase console \> Project Settings \> Integrations) |
| firebase.links.update | Update existing links to Google systems (Firebase console \> Project Settings \> Integrations) |
| firebase.playLinks.get | Retrieve details about a link to Google Play (Firebase console \> Project Settings \> Integrations \> Google Play) |
| firebase.playLinks.list | Retrieve a list of links to Google Play (Firebase console \> Project Settings \> Integrations \> Google Play) |
| firebase.playLinks.update | Create new links and update existing links to Google Play (Firebase console \> Project Settings \> Integrations \> Google Play) |
| firebase.projects.delete | Delete existing projects |
| firebase.projects.get | Retrieve details and Firebase resources for a project |
| firebase.projects.update | Modify the attributes of an existing project Receive alerts for applicable Firebase products and features ([learn more](https://support.google.com/firebase/answer/7276542)) |
| firebaseinstallations.instances.delete | Delete a Firebase installation ID and the data tied to that installation ([learn more](https://firebase.google.com/docs/projects/manage-installations#delete-fid)) |

### Google Analytics permissions

The following permissions grant access to the Analytics property linked to
the Firebase project. They allow Firebase project members to access
Analytics data, including audiences, user properties, funnels, reports,
conversions, etc.

> [!NOTE]
> **Note:** In Google Analytics, each Firebase project member, based on their highest `firebaseanalytics.*` permission, is mapped to a linked user that has a specific Analytics role. Google Analytics Admins can modify the default Analytics role assigned to a linked user. For more information, see [User access (roles in Analytics)](https://support.google.com/analytics/answer/9289234#access) in the Analytics Help.

> [!NOTE]
> **Note:** To grant the permissions of `firebaseanalytics.resources.googleAnalyticsAdditionalAccess` or `firebaseanalytics.resources.googleAnalyticsRestrictedAccess` to a Firebase project member, you'll need to create and assign a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom).

| Permission name | Description |
|---|---|
| firebaseanalytics.resources.googleAnalyticsEdit | By default, grants the Analytics Editor role to the linked Analytics property |
| firebaseanalytics.resources.googleAnalyticsAdditionalAccess | By default, grants the Analytics Marketer role to the linked Analytics property |
| firebaseanalytics.resources.googleAnalyticsReadAndAnalyze | By default, grants the Analytics Viewer role to the linked Analytics property |
| firebaseanalytics.resources.googleAnalyticsRestrictedAccess | By default, grants the Analytics Viewer role to the linked Analytics property with no access to revenue data and cost data |

> [!IMPORTANT]
> **Important:** If you linked your Firebase project to a Google Analytics 4 property before January 4, 2023, then the Firebase linked users may have different roles and data access in Analytics than described in the table above. Analytics administrators can verify and edit roles and data access from the Analytics UI (**Admin \> linked property \> Property Access Management**).

### Firebase AI Logic permissions

| Permission name | Description |
|---|---|
| firebasevertexai.configs.get | Retrieve configuration for Firebase AI Logic |
| firebasevertexai.configs.update | Update configuration for Firebase AI Logic |

### Firebase App Check permissions

| Permission name | Description |
|---|---|
| firebaseappcheck.appAttestConfig.get | Retrieve the App Attest configuration of an app |
| firebaseappcheck.appAttestConfig.update | Update the App Attest configuration of an app |
| firebaseappcheck.appCheckTokens.verify | Verify App Check tokens issued for a Firebase project |
| firebaseappcheck.debugTokens.get | Retrieve debug tokens of an app |
| firebaseappcheck.debugTokens.update | Create, update, or delete debug tokens of an app |
| firebaseappcheck.deviceCheckConfig.get | Retrieve the DeviceCheck configuration of an app |
| firebaseappcheck.deviceCheckConfig.update | Update the DeviceCheck configuration of an app |
| firebaseappcheck.playIntegrityConfig.get | Retrieve the Play Integrity configuration of an app |
| firebaseappcheck.playIntegrityConfig.update | Update the Play Integrity configuration of an app |
| firebaseappcheck.recaptchaEnterpriseConfig.get | Retrieve the reCAPTCHA Enterprise configuration of an app |
| firebaseappcheck.recaptchaEnterpriseConfig.update | Update the reCAPTCHA Enterprise configuration of an app |
| firebaseappcheck.recaptchaV3Config.get | Retrieve the reCAPTCHA v3 configuration of an app |
| firebaseappcheck.recaptchaV3Config.update | Update the reCAPTCHA v3 configuration of an app |
| firebaseappcheck.safetyNetConfig.get | Retrieve the SafetyNet configuration of an app |
| firebaseappcheck.safetyNetConfig.update | Update the SafetyNet configuration of an app |
| firebaseappcheck.services.get | Retrieve service enforcement configurations of a project |
| firebaseappcheck.services.update | Update service enforcement configurations of a project |

### Firebase App Distribution permissions

| Permission name | Description |
|---|---|
| firebaseappdistro.releases.list | Retrieve a list of existing distributions and Invite Links |
| firebaseappdistro.releases.update | Create, delete, and modify distributions Create and delete Invite Links |
| firebaseappdistro.testers.list | Retrieve a list of existing testers in a project |
| firebaseappdistro.testers.update | Create and delete testers in a project |
| firebaseappdistro.groups.list | Retrieve a list of existing tester groups in a project |
| firebaseappdistro.groups.update | Create and delete tester groups in a project |

### Firebase Authentication permissions

| Permission name | Description |
|---|---|
| firebaseauth.configs.create | Create the Authentication configuration |
| firebaseauth.configs.get | Retrieve the Authentication configuration |
| firebaseauth.configs.getHashConfig | Get the password hash config and password hash of user accounts |
| firebaseauth.configs.getSecret | Get the client secret in the Authentication configuration |
| firebaseauth.configs.update | Update the existing Authentication configuration |
| firebaseauth.users.create | Create new users in Authentication |
| firebaseauth.users.createSession | Create session cookie for a logged-in user |
| firebaseauth.users.delete | Delete existing users in Authentication |
| firebaseauth.users.get | Retrieve a list of existing Authentication users |
| firebaseauth.users.sendEmail | Send emails to the users |
| firebaseauth.users.update | Update existing users in Authentication |

### Firebase A/B Testing permissions *(beta)*

> [!CAUTION]
> **Caution:** These product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

| Permission name | Description |
|---|---|
| firebaseabt.experimentresults.get | Retrieve the results of an experiment |
| firebaseabt.experiments.create | Create new experiments |
| firebaseabt.experiments.delete | Delete existing experiments |
| firebaseabt.experiments.get | Retrieve details of an existing experiment |
| firebaseabt.experiments.list | Retrieve a list of existing experiments |
| firebaseabt.experiments.update | Update an existing experiment |
| firebaseabt.projectmetadata.get | Retrieve analytics metadata for setting up an experiment |

### Firebase App Hosting permissions *(beta)*

> [!CAUTION]
> **Caution:** These product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

| Permission name | Description |
|---|---|
| firebaseapphosting.backends.create | Create a new App Hosting backend for a Firebase project. |
| firebaseapphosting.backends.delete | Delete an existing App Hosting backend from a Firebase project. |
| firebaseapphosting.backends.get | Retrieve information about a specific App Hosting backend in a Firebase project. |
| firebaseapphosting.backends.list | List all available App Hosting backends in a Firebase project. |
| firebaseapphosting.backends.update | Modify the configuration or settings of an existing App Hosting backend. |
| firebaseapphosting.builds.create | Initiate a new build process for an App Hosting backend in a Firebase project. |
| firebaseapphosting.builds.delete | Delete existing builds in an App Hosting backend. |
| firebaseapphosting.builds.get | Retrieve details of an existing build in an App Hosting backend. |
| firebaseapphosting.builds.list | List all builds associated with an App Hosting backend in a Firebase project. |
| firebaseapphosting.builds.update | Modify the configuration of an existing non-finalized App Hosting build. |
| firebaseapphosting.domains.create | Create a new domain association for an App Hosting backend in a Firebase project. |
| firebaseapphosting.domains.delete | Remove a domain association from an App Hosting backend. |
| firebaseapphosting.domains.get | Retrieve information about a specific domain associated with an App Hosting site. |
| firebaseapphosting.domains.list | List all domains associated with App Hosting. |
| firebaseapphosting.domains.update | Modify settings or configurations for a domain linked to an App Hosting backend. |
| firebaseapphosting.rollouts.create | Initiate a new rollout to promote a existing build to the currently serving version for that App Hosting backend. |
| firebaseapphosting.rollouts.get | Retrieve information about a specific App Hosting rollout. |
| firebaseapphosting.rollouts.list | List all rollouts associated with an App Hosting backend. |
| firebaseapphosting.traffic.get | Retrieve the current traffic split and rollout policy for an App Hosting site. |
| firebaseapphosting.traffic.list | Identical in function to \`firebaseapphosting.traffic.get\`, with added capability to retrieve a list across backends for which you have this permission. |
| firebaseapphosting.traffic.update | Modify the current traffic split and rollout policy for an App Hosting backend. |

### Cloud Firestore permissions

For a list and descriptions of Cloud Firestore permissions, refer to the
[Google Cloud documentation](https://cloud.google.com/datastore/docs/access/iam#permissions).

### Cloud Storage permissions

For a list and descriptions of Cloud Storage permissions, refer to the
[Google Cloud documentation](https://cloud.google.com/storage/docs/access-control/iam-permissions).

### Firebase Security Rules (Cloud Firestore and Cloud Storage) permissions

> [!CAUTION]
> **Caution:** These permissions control access to security rules for Cloud Storage ***and*** for Cloud Firestore.  
> For permissions that control access to security rules for Firebase Realtime Database, refer to the [Realtime Database permissions](https://firebase.google.com/docs/projects/iam/permissions#realtime-database).

| Permission name | Description |
|---|---|
| firebaserules.releases.create | Create releases |
| firebaserules.releases.delete | Delete releases |
| firebaserules.releases.get | Retrieve releases |
| firebaserules.releases.getExecutable | Retrieve the binary executable payloads for releases |
| firebaserules.releases.list | Retrieve a list of releases |
| firebaserules.releases.update | Update ruleset references for releases |
| firebaserules.rulesets.create | Create new rulesets |
| firebaserules.rulesets.delete | Delete existing ruleset |
| firebaserules.rulesets.get | Retrieve rulesets with source |
| firebaserules.rulesets.list | Find ruleset metadata (no source) |
| firebaserules.rulesets.test | Test sources for correctness |

### Cloud Functions for Firebase permissions

For a list and descriptions of Cloud Functions permissions, refer to the
[IAM documentation](https://cloud.google.com/functions/docs/reference/iam/permissions).

Be aware that the deployment of functions requires a specific configuration of
permissions that aren't included in the standard
[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).
To deploy functions, use one of the following options:

- Delegate the deployment of functions to a project
  [**Owner**](https://firebase.google.com/docs/projects/iam/roles-basic).

  If you're deploying only non-HTTP functions, then a project
  [**Editor**](https://firebase.google.com/docs/projects/iam/roles-basic) can deploy your functions.
- Delegate deployment of functions to a project member who has the following two
  roles:

  - Cloud Functions Admin role ([`roles/cloudfunctions.admin`](https://cloud.google.com/functions/docs/reference/iam/roles))
  - Service Account User role ([`roles/iam.serviceAccountUser`](https://cloud.google.com/iam/docs/service-accounts#user-role))

  A project Owner can assign these roles to a project member
  [using the Google Cloud console or gcloud CLI](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
  For detailed steps and security implications for this role configuration, refer to the
  [IAM documentation](https://cloud.google.com/functions/docs/reference/iam/roles#additional-configuration).

### Firebase messaging campaigns permissions

These permissions apply to campaigns for Firebase Cloud Messaging and
Firebase In-App Messaging.

| Permission name | Description |
|---|---|
| firebasemessagingcampaigns.campaigns.create | Create new campaigns |
| firebasemessagingcampaigns.campaigns.delete | Delete existing campaigns |
| firebasemessagingcampaigns.campaigns.get | Retrieve details of existing campaigns |
| firebasemessagingcampaigns.campaigns.list | Retrieve a list of existing campaigns |
| firebasemessagingcampaigns.campaigns.update | Update existing campaigns |
| firebasemessagingcampaigns.campaigns.start | Start existing campaigns |
| firebasemessagingcampaigns.campaigns.stop | Update existing campaigns |

### Firebase Cloud Messaging permissions

| Permission name | Description |
|---|---|
| cloudmessaging.messages.create | Send notifications and data messages through the FCM HTTP API and Admin SDK |

> [!WARNING]
> The following Firebase Cloud Messaging permissions are deprecated. Use an appropriate [`firebasemessagingcampaigns.*`
> permission](https://firebase.google.com/docs/projects/iam/permissions#messaging-campaigns) instead.

| Permission name | Description |
|---|---|
| firebasenotifications.messages.create | Create new messages in the Notifications composer |
| firebasenotifications.messages.delete | Delete existing messages in the Notifications composer |
| firebasenotifications.messages.get | Retrieve details of existing messages in the Notifications composer |
| firebasenotifications.messages.list | Retrieve a list of existing messages in the Notifications composer |
| firebasenotifications.messages.update | Update existing messages in the Notifications composer |

### Firebase Crashlytics permissions

| Permission name | Description |
|---|---|
| firebasecrashlytics.config.get | Retrieve Crashlytics configuration settings |
| firebasecrashlytics.config.update | Update Crashlytics configuration settings |
| firebasecrashlytics.data.get | Retrieve metrics associated with Crashlytics issues and sessions |
| firebasecrashlytics.issues.get | Retrieve details about Crashlytics issues, including notes attached to issues |
| firebasecrashlytics.issues.list | Retrieve a list of Crashlytics issues |
| firebasecrashlytics.issues.update | Open, close, and mute existing Crashlytics issues Update notes attached to issues |
| firebasecrashlytics.sessions.get | Retrieve details about Crashlytics crash sessions |

| Permission name | Description |
|---|---|
| firebasecrash.issues.update | > [!WARNING] > *Deprecated.* Use an appropriate [`firebasecrashlytics.*` permission](https://firebase.google.com/docs/projects/iam/permissions#crashlytics) instead. Update existing Crashlytics issues, create notes on issues, and set velocity alerts |
| firebasecrash.reports.get | > [!WARNING] > *Deprecated.* Use an appropriate [`firebasecrashlytics.*` permission](https://firebase.google.com/docs/projects/iam/permissions#crashlytics) instead. Retrieve existing Crashlytics reports |

### Firebase Dynamic Links permissions

| Permission name | Description |
|---|---|
| firebasedynamiclinks.domains.create | Create new Dynamic Links domains |
| firebasedynamiclinks.domains.delete | Delete existing Dynamic Links domains |
| firebasedynamiclinks.domains.get | Retrieve details of existing Dynamic Links domains |
| firebasedynamiclinks.domains.list | Retrieve a list of existing Dynamic Links domains |
| firebasedynamiclinks.domains.update | Update existing Dynamic Links domains |
| firebasedynamiclinks.links.create | Create new Dynamic Links |
| firebasedynamiclinks.links.get | Retrieve details of existing Dynamic Links |
| firebasedynamiclinks.links.list | Retrieve a list of existing Dynamic Links |
| firebasedynamiclinks.links.update | Update existing Dynamic Links |
| firebasedynamiclinks.stats.get | Retrieve Dynamic Links statistics |
| firebasedynamiclinks.destinations.list | Retrieve existing Dynamic Links destinations |
| firebasedynamiclinks.destinations.update | Update existing Dynamic Links destinations |

### Firebase Extensions publishing permissions

| Permission name | Description |
|---|---|
| firebaseextensionspublisher.extensions.create | Upload new versions of an extension |
| firebaseextensionspublisher.extensions.delete | Delete or deprecate versions of an extension |
| firebaseextensionspublisher.extensions.get | Retrieve details about an extension version |
| firebaseextensionspublisher.extensions.list | List all extension versions uploaded by this publisher project |

### Firebase Hosting permissions

> [!CAUTION]
> [Custom roles](https://firebase.google.com/docs/projects/iam/roles-custom) cannot currently be used for controlling access to Firebase Hosting resources. To grant a project member access to Hosting, you can assign them one of the following predefined roles (as appropriate for their access needs):  
> [Firebase Develop Admin or Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-category#develop_roles) or [Firebase Hosting Admin or Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-product#hosting).

| Permission name | Description |
|---|---|
| firebasehosting.sites.create | Create new [Hosting resources](https://firebase.google.com/docs/hosting/manage-hosting-resources) for a Firebase project |
| firebasehosting.sites.delete | Delete existing [Hosting resources](https://firebase.google.com/docs/hosting/manage-hosting-resources) for a Firebase project |
| firebasehosting.sites.get | Retrieve details of an existing [Hosting resources](https://firebase.google.com/docs/hosting/manage-hosting-resources) for a Firebase project |
| firebasehosting.sites.list | Retrieve a list of [Hosting resources](https://firebase.google.com/docs/hosting/manage-hosting-resources) for a Firebase project |
| firebasehosting.sites.update | Update existing [Hosting resources](https://firebase.google.com/docs/hosting/manage-hosting-resources) for a Firebase project |

### Firebase In-App Messaging permissions *(beta)*

> [!CAUTION]
> **Caution:** These product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

> [!WARNING]
> The following Firebase In-App Messaging permissions are deprecated. Use an appropriate [`firebasemessagingcampaigns.*`
> permission](https://firebase.google.com/docs/projects/iam/permissions#messaging-campaigns) instead.

| Permission name | Description |
|---|---|
| firebaseinappmessaging.campaigns.create | Create new campaigns |
| firebaseinappmessaging.campaigns.delete | Delete existing campaigns |
| firebaseinappmessaging.campaigns.get | Retrieve details of existing campaigns |
| firebaseinappmessaging.campaigns.list | Retrieve a list of existing campaigns |
| firebaseinappmessaging.campaigns.update | Update existing campaigns |

### Firebase ML permissions *(beta)*

> [!CAUTION]
> **Caution:** These product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

| Permission name | Description |
|---|---|
| firebaseml.models.create | Create new ML models |
| firebaseml.models.update | Update existing ML models |
| firebaseml.models.delete | Delete existing ML models |
| firebaseml.models.get | Retrieve details of existing ML models |
| firebaseml.models.list | Retrieve a list of existing ML models |
| firebaseml.modelversions.create | Create new model versions |
| firebaseml.modelversions.get | Retrieve details of existing model versions |
| firebaseml.modelversions.list | Retrieve a list of existing model versions |
| firebaseml.modelversions.update | Update existing model versions |

### Firebase Performance Monitoring permissions

| Permission name | Description |
|---|---|
| firebaseperformance.config.create | Create new issue threshold configurations |
| firebaseperformance.config.delete | Delete existing issue threshold configurations |
| firebaseperformance.config.update | Modify alert and existing issue threshold configurations |
| firebaseperformance.data.get | View all performance data and issue threshold values |

### Firebase Realtime Database permissions

| Permission name | Description |
|---|---|
| firebasedatabase.instances.create | Create new database instances |
| firebasedatabase.instances.get | Retrieve the metadata of existing database instances Read-only access to the data in an existing database instance |
| firebasedatabase.instances.list | Retrieve a list of existing database instances |
| firebasedatabase.instances.update | Full read and write access to the data in existing database instances Enable and disable database instances Retrieve and modify security rules for existing database instances |
| firebasedatabase.instances.disable | Disable active database instances <br /> Existing data is kept but is not accessible for reads/writes. |
| firebasedatabase.instances.reenable | Re-enable disabled database instances <br /> Existing data is again accessible for reads/writes. |
| firebasedatabase.instances.delete | Delete disabled database instances <br /> Deleted database names cannot be reused. The data in a deleted database instance is permanently deleted after 20 days. |
| firebasedatabase.instances.undelete | Undelete a deleted database instance before its data is permanently deleted <br /> The data in a deleted database instance is permanently deleted 20 days after the instance is deleted. |

### Firebase Remote Config permissions

| Permission name | Description |
|---|---|
| cloudconfig.configs.get | Retrieve Remote Config data |
| cloudconfig.configs.update | Update Remote Config data |

### Firebase Test Lab permissions

Test Lab requires access to Cloud Storage buckets, so it requires a
specific configuration of permissions that aren't all included in the standard
[Firebase predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined).
To grant access to Test Lab, use one of the following options:

- **For tests started from Firebase console**

  - Test your app in a dedicated separate Firebase project.

  - Add members who need Test Lab access, then assign them legacy project
    roles using the [Firebase console](https://console.firebase.google.com/).

    - To allow a member to run tests with Test Lab, assign project **Editor** or above.
    - To allow a member to view test results in Test Lab, assign project **Viewer** or above.
- **For tests started from
  the [gcloud CLI](https://firebase.google.com/docs/test-lab/android/command-line),
  the [Testing API](https://firebase.google.com/docs/test-lab/reference/testing/rest), or
  [Gradle Managed Devices](https://firebase.google.com/docs/test-lab/android/android-studio#gmd-testlab-plugin)
  while using your own Cloud Storage bucket**

  - Assign a pair of predefined roles (which together grant the required set
    of permissions) using the
    [Google Cloud console](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

    - To allow a member to run tests with Test Lab, assign both:

      - Firebase Test Lab Admin (`roles/cloudtestservice.testAdmin`)
      - Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)
    - To allow a member to view test results in Test Lab, assign both:

      - Firebase Test Lab Viewer (`roles/cloudtestservice.testViewer`)
      - Firebase Analytics Viewer (`roles/firebase.analyticsViewer`)

> [!CAUTION]
> **Caution:** Members assigned these predefined roles can access *all* Cloud Storage buckets associated with the Firebase project, potentially including customer data.

| Permission name | Description |
|---|---|
| cloudtestservice.environmentcatalog.get | Retrieve the catalog of supported test environments for a project |
| cloudtestservice.matrices.create | Request to run a matrix of tests according to the given specifications |
| cloudtestservice.matrices.get | Retrieve the status of a test matrix |
| cloudtestservice.matrices.update | Update an unfinished test matrix |
| cloudtoolresults.executions.list | Retrieve a list of Executions for a History |
| cloudtoolresults.executions.get | Retrieve an existing Execution |
| cloudtoolresults.executions.create | Create a new Execution |
| cloudtoolresults.executions.update | Update an existing Execution |
| cloudtoolresults.histories.list | Retrieve a list of Histories |
| cloudtoolresults.histories.get | Retrieve an existing History |
| cloudtoolresults.histories.create | Create a new History |
| cloudtoolresults.settings.create | Create new tool results settings |
| cloudtoolresults.settings.get | Retrieve existing tool results settings |
| cloudtoolresults.settings.update | Update tool results settings |
| cloudtoolresults.steps.list | Retrieve a list of Steps for an Execution |
| cloudtoolresults.steps.get | Retrieve an existing Step |
| cloudtoolresults.steps.create | Create a new Step |
| cloudtoolresults.steps.update | Update an existing Step |

### Integrations with external services permissions

| Permission name | Description |
|---|---|
| firebaseextensions.configs.create | Create new extension configurations for external services (Firebase console \> Project Settings \> Integrations) |
| firebaseextensions.configs.delete | Delete existing extension configurations for external services (Firebase console \> Project Settings \> Integrations) |
| firebaseextensions.configs.list | Retrieve a list of extension configurations for external services (Firebase console \> Project Settings \> Integrations) |
| firebaseextensions.configs.update | Update existing extension configurations for external services (Firebase console \> Project Settings \> Integrations) |
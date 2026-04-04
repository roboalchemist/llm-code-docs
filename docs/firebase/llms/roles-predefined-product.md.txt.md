# Source: https://firebase.google.com/docs/projects/iam/roles-predefined-product.md.txt

# Firebase product-level predefined roles

These roles grant full read/write or read-only access to *specific* Firebase
products.

Assign these roles to project members using the
[Google Cloud console](https://console.cloud.google.com/iam-admin/iam).

> [!NOTE]
> **Note:** The following permissions are in *all* the Firebase product-level predefined roles:   
> - firebase.clients.get  
> - firebase.clients.list  
> - firebase.projects.get  
> - resourcemanager.projects.get  
> - resourcemanager.projects.list

## Firebase AI Logic roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase AI Logic Admin** `roles/firebasevertexai.admin` | Full read/write access to Firebase AI Logic resources | **Firebase AI Logic Admin** permissions firebasevertexai.configs.update firebasevertexai.configs.get |
| **Firebase AI Logic Viewer** `roles/firebasevertexai.viewer` | Read-only access to Firebase AI Logic resources | **Firebase AI Logic Viewer** permissions firebasevertexai.configs.get |

## Firebase App Check roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase App Check Admin** `roles/firebaseappcheck.admin` | Full read/write access to App Check resources | **App Check Admin** permissions firebaseappcheck.appAttestConfig.get firebaseappcheck.appAttestConfig.update firebaseappcheck.appCheckTokens.verify firebaseappcheck.debugTokens.get firebaseappcheck.debugTokens.update firebaseappcheck.deviceCheckConfig.get firebaseappcheck.deviceCheckConfig.update firebaseappcheck.playIntegrityConfig.get firebaseappcheck.playIntegrityConfig.update firebaseappcheck.recaptchaEnterpriseConfig.get firebaseappcheck.recaptchaEnterpriseConfig.update firebaseappcheck.recaptchaV3Config.get firebaseappcheck.recaptchaV3Config.update firebaseappcheck.safetyNetConfig.get firebaseappcheck.safetyNetConfig.update firebaseappcheck.services.get firebaseappcheck.services.update |
| **Firebase App Check Viewer** `roles/firebaseappcheck.viewer` | Read-only access to App Check resources | **App Check Viewer** permissions firebaseappcheck.appAttestConfig.get firebaseappcheck.debugTokens.get firebaseappcheck.deviceCheckConfig.get firebaseappcheck.playIntegrityConfig.get firebaseappcheck.recaptchaEnterpriseConfig.get firebaseappcheck.recaptchaV3Config.get firebaseappcheck.safetyNetConfig.get firebaseappcheck.services.get |
| **Firebase App Check Token Verifier** `roles/firebaseappcheck.tokenVerifier` | Access to token verification capabilities for App Check | **App Check Token Verifier** permissions firebaseappcheck.appCheckTokens.verify |

## Firebase App Distribution roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase App Distribution Admin** `roles/firebaseappdistro.admin` | Full read/write access to App Distribution resources | **App Distribution Admin** permissions firebaseappdistro.releases.list firebaseappdistro.releases.update firebaseappdistro.testers.list firebaseappdistro.testers.update firebaseappdistro.groups.list firebaseappdistro.groups.update |
| **Firebase App Distribution Viewer** `roles/firebaseappdistro.viewer` | Read-only access to App Distribution resources | **App Distribution Viewer** permissions firebaseappdistro.releases.list firebaseappdistro.testers.list firebaseappdistro.groups.list |

## Firebase App Hosting roles

> [!NOTE]
> **Note:** A project Owner must create the *first* App Hosting backend for a project. After this initial setup, App Hosting Admins also can create and manage additional backends.

| Role | Description | Permissions |
|---|---|---|
| **Firebase App Hosting Compute Runner** `roles/firebaseapphosting.computeRunner` | Minimal access required to build and run App Hosting backends. Typically granted to service accounts. | **App Hosting Compute Runner** permissions [firebaseapphosting.builds.update](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) [storage.objects.setRetention](https://cloud.google.com/iam/docs/roles-permissions/storage#storage.objects.setRetention) As well as all permissions included in these roles: [firebaseapphosting.viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-product#apphosting-viewer) [artifactregistry.createOnPushWriter](https://cloud.google.com/iam/docs/understanding-roles#artifactregistry.createOnPushWriter) [logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#logging.logWriter) [cloudtrace.agent](https://cloud.google.com/iam/docs/understanding-roles#cloudtrace.agent) [monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#monitoring.metricWriter) [storage.objectUser](https://cloud.google.com/iam/docs/understanding-roles#storage.objectUser) [developerconnect.readTokenAccessor](https://cloud.google.com/iam/docs/understanding-roles#developerconnect.readTokenAccessor) |
| **Firebase App Hosting Admin** `roles/firebaseapphosting.admin` | Full read/write access to App Hosting resources | **App Hosting Admin** permissions firebaseapphosting.backends.create firebaseapphosting.backends.delete firebaseapphosting.backends.get firebaseapphosting.backends.list firebaseapphosting.backends.update firebaseapphosting.builds.create firebaseapphosting.builds.delete firebaseapphosting.builds.get firebaseapphosting.builds.list firebaseapphosting.builds.update firebaseapphosting.domains.create firebaseapphosting.domains.delete firebaseapphosting.domains.get firebaseapphosting.domains.list firebaseapphosting.domains.update firebaseapphosting.locations.get firebaseapphosting.locations.list firebaseapphosting.operations.cancel firebaseapphosting.operations.delete firebaseapphosting.operations.get firebaseapphosting.operations.list firebaseapphosting.rollouts.create firebaseapphosting.rollouts.delete firebaseapphosting.rollouts.get firebaseapphosting.rollouts.list firebaseapphosting.rollouts.update firebaseapphosting.traffic.get firebaseapphosting.traffic.list firebaseapphosting.traffic.update |
| **Firebase App Hosting Viewer** `roles/firebaseapphosting.viewer` | Read-only access to App Hosting resources | **App Hosting Viewer** permissions firebaseapphosting.backends.get firebaseapphosting.backends.list firebaseapphosting.builds.get firebaseapphosting.builds.list firebaseapphosting.domains.get firebaseapphosting.domains.list firebaseapphosting.locations.get firebaseapphosting.locations.list firebaseapphosting.operations.list firebaseapphosting.operations.get firebaseapphosting.rollouts.get firebaseapphosting.rollouts.list firebaseapphosting.traffic.get firebaseapphosting.traffic.list |
| **Firebase App Hosting Developer** `roles/firebaseapphosting.developer` | Full read/write access to App Hosting backends, builds, and releases resources. | **App Hosting Developer** permissions firebaseapphosting.backends.update firebaseapphosting.builds.create firebaseapphosting.builds.delete firebaseapphosting.builds.update firebaseapphosting.operations.delete firebaseapphosting.operations.cancel firebaseapphosting.rollouts.create firebaseapphosting.rollouts.delete firebaseapphosting.rollouts.update firebaseapphosting.traffic.update |

## Firebase Authentication roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Authentication Admin** `roles/firebaseauth.admin` | Full read/write access to Authentication resources | **Authentication Admin** permissions firebaseauth.configs.create firebaseauth.configs.get firebaseauth.configs.getHashConfig firebaseauth.configs.getSecret firebaseauth.configs.update firebaseauth.users.create firebaseauth.users.createSession firebaseauth.users.delete firebaseauth.users.get firebaseauth.users.sendEmail firebaseauth.users.update |
| **Firebase Authentication Viewer** `roles/firebaseauth.viewer` | Read-only access to Authentication resources | **Authentication Viewer** permissions firebaseauth.configs.get firebaseauth.users.get |

## Firebase A/B Testing roles *(beta)*


> [!CAUTION]
> **Caution:** These roles and their product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

<br />

| Role | Description | Permissions |
|---|---|---|
| **Firebase A/B Testing Admin** `roles/firebaseabt.admin` *(beta)* | Full read/write access to A/B Testing resources | **A/B Testing Admin** permissions firebaseabt.experimentresults.get firebaseabt.experiments.create firebaseabt.experiments.delete firebaseabt.experiments.get firebaseabt.experiments.list firebaseabt.experiments.update firebaseabt.projectmetadata.get |
| **Firebase A/B Testing Viewer** `roles/firebaseabt.viewer` *(beta)* | Read-only access to A/B Testing resources | **A/B Testing Viewer** permissions firebaseabt.experimentresults.get firebaseabt.experiments.get firebaseabt.experiments.list firebaseabt.projectmetadata.get |

## Cloud Firestore roles

Find available Cloud Firestore roles in the
[Google Cloud documentation](https://cloud.google.com/datastore/docs/access/iam).

To allow a project member to edit and publish security rules in the
Firebase console or to deploy security rules via the Firebase CLI, you
can create then assign them a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom)
that includes the
[`firebaserules.*` permissions](https://firebase.google.com/docs/projects/iam/permissions#security-rules).

## Cloud Storage roles

Find available Cloud Storage roles in the
[Google Cloud documentation](https://cloud.google.com/storage/docs/access-control/iam-roles).

To allow a project member to edit and publish security rules in the
Firebase console or to deploy security rules via the Firebase CLI, you
can create then assign them a [custom role](https://firebase.google.com/docs/projects/iam/roles-custom)
that includes the
[`firebaserules.*` permissions](https://firebase.google.com/docs/projects/iam/permissions#security-rules).

## Cloud Functions for Firebase roles

Find available Cloud Functions for Firebase roles in the
[Google Cloud documentation](https://cloud.google.com/functions/docs/reference/iam/roles).

## Firebase messaging campaigns roles

These roles apply to campaigns for Firebase Cloud Messaging and
Firebase In-App Messaging.

| Role | Description | Permissions |
|---|---|---|
| **Firebase messaging campaigns Admin** `roles/firebasemessagingcampaigns.admin` | Full read/write access to campaigns resources for Cloud Messaging and In-App Messaging | **Firebase messaging campaigns Admin** permissions firebasemessagingcampaigns.campaigns.create firebasemessagingcampaigns.campaigns.delete firebasemessagingcampaigns.campaigns.get firebasemessagingcampaigns.campaigns.list firebasemessagingcampaigns.campaigns.update firebasemessagingcampaigns.campaigns.start firebasemessagingcampaigns.campaigns.stop |
| **Firebase messaging campaigns Viewer** `roles/firebasemessagingcampaigns.viewer` | Read-only access to campaigns resources for Cloud Messaging and In-App Messaging | **Firebase messaging campaigns Viewer** permissions firebasemessagingcampaigns.campaigns.get firebasemessagingcampaigns.campaigns.list |

## Firebase Cloud Messaging roles

In addition to an Firebase Cloud Messaging API role, you might also need to
assign an appropriate
[Firebase messaging campaigns role](https://firebase.google.com/docs/projects/iam/roles-predefined-product#messaging-campaigns).

| Role | Description | Permissions |
|---|---|---|
| **Firebase Cloud Messaging API Admin** `roles/firebasecloudmessaging.admin` | Full read/write access to Firebase Cloud Messaging API resources. | **Firebase Cloud Messaging API Admin** permissions cloudmessaging.messages.create fcmdata.deliverydata.list resourcemanager.projects.get resourcemanager.projects.list |

> [!WARNING]
> The following Firebase Cloud Messaging roles are deprecated. Use an appropriate [Firebase Cloud Messaging API role](https://firebase.google.com/docs/projects/iam/roles-predefined-product#messaging) and an appropriate [Firebase messaging campaigns role](https://firebase.google.com/docs/projects/iam/roles-predefined-product#messaging-campaigns) instead.

| Role | Description | Permissions |
|---|---|---|
| **Firebase Cloud Messaging Admin** `roles/firebasenotifications.admin` | Full read/write access to Cloud Messaging resources | **Cloud Messaging Admin** permissions firebasenotifications.messages.create firebasenotifications.messages.delete firebasenotifications.messages.get firebasenotifications.messages.list firebasenotifications.messages.update |
| **Firebase Cloud Messaging Viewer** `roles/firebasenotifications.viewer` | Read-only access to Cloud Messaging resources | **Cloud Messaging Viewer** permissions firebasenotifications.messages.get firebasenotifications.messages.list |

## Firebase Crashlytics roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Crashlytics Admin** `roles/firebasecrashlytics.admin` | Full read/write access to Crashlytics resources | **Crashlytics Admin** permissions firebasecrashlytics.config.get firebasecrashlytics.config.update firebasecrashlytics.data.get firebasecrashlytics.issues.get firebasecrashlytics.issues.list firebasecrashlytics.issues.update firebasecrashlytics.sessions.get |
| **Firebase Crashlytics Viewer** `roles/firebasecrashlytics.viewer` | Read-only access to Crashlytics resources | **Crashlytics Viewer** permissions firebasecrashlytics.config.get firebasecrashlytics.data.get firebasecrashlytics.issues.get firebasecrashlytics.issues.list firebasecrashlytics.sessions.get |

## Firebase Dynamic Links roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Dynamic Links Admin** `roles/firebasedynamiclinks.admin` | Full read/write access to Dynamic Links resources | **Dynamic Links Admin** permissions firebasedynamiclinks.destinations.list firebasedynamiclinks.destinations.update firebasedynamiclinks.domains.create firebasedynamiclinks.domains.delete firebasedynamiclinks.domains.get firebasedynamiclinks.domains.list firebasedynamiclinks.domains.update firebasedynamiclinks.links.create firebasedynamiclinks.links.get firebasedynamiclinks.links.list firebasedynamiclinks.links.update firebasedynamiclinks.stats.get |
| **Firebase Dynamic Links Viewer** `roles/firebasedynamiclinks.viewer` | Read-only access to Dynamic Links resources | **Dynamic Links Viewer** permissions firebasedynamiclinks.destinations.list firebasedynamiclinks.domains.get firebasedynamiclinks.domains.list firebasedynamiclinks.links.get firebasedynamiclinks.links.list firebasedynamiclinks.stats.get |

## Firebase Extensions publisher roles


> [!CAUTION]
> **Caution:** These roles and their product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

<br />

| Role | Description | Permissions |
|---|---|---|
| **Firebase Extensions Publisher - Extensions Admin** `roles/firebaseextensionspublisher.extensionsAdmin` *(beta)* | Upload, publish, and view details and metrics for Firebase Extensions | **Firebase Extensions Publisher - Extensions Admin** permissions firebaseextensionspublisher.extensions.create firebaseextensionspublisher.extensions.delete firebaseextensionspublisher.extensions.get firebaseextensionspublisher.extensions.list |
| **Firebase Extensions Publisher - Extensions Viewer** `roles/firebaseextensionspublisher.extensionsViewer` *(beta)* | View details and metrics for Firebase Extensions uploaded by this publisher | **Firebase Extensions Publisher - Extensions Viewer** permissions firebaseextensionspublisher.extensions.get firebaseextensionspublisher.extensions.list |

## Firebase Hosting roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Hosting Admin** `roles/firebasehosting.admin` | Full read/write access to Hosting resources | **Hosting Admin** permissions firebasehosting.sites.create firebasehosting.sites.delete firebasehosting.sites.get firebasehosting.sites.list firebasehosting.sites.update |
| **Firebase Hosting Viewer** `roles/firebasehosting.viewer` | Read-only access to Hosting resources | **Hosting Viewer** permissions firebasehosting.sites.get firebasehosting.sites.list |

> [!IMPORTANT]
> **Important:** To deploy via the Firebase CLI, a project member must ***also*** be assigned the [API Keys Viewer role
> (`roles/serviceusage.apiKeysViewer`)](https://cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.apiKeysViewer).

## Firebase In-App Messaging roles *(beta)*


> [!CAUTION]
> **Caution:** These roles and their product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

<br />

> [!WARNING]
> The following Firebase In-App Messaging roles are deprecated. Use an appropriate [Firebase messaging campaigns role](https://firebase.google.com/docs/projects/iam/roles-predefined-product#messaging-campaigns) instead.

| Role | Description | Permissions |
|---|---|---|
| **Firebase In-App Messaging Admin** `roles/firebaseinappmessaging.admin` *(beta)* | Full read/write access to In-App Messaging resources | **In-App Messaging Admin** permissions firebaseinappmessaging.campaigns.create firebaseinappmessaging.campaigns.delete firebaseinappmessaging.campaigns.get firebaseinappmessaging.campaigns.list firebaseinappmessaging.campaigns.update |
| **Firebase In-App Messaging Viewer** `roles/firebaseinappmessaging.viewer` *(beta)* | Read-only access to In-App Messaging resources | **In-App Messaging Viewer** permissions firebaseinappmessaging.campaigns.get firebaseinappmessaging.campaigns.list |

## Firebase ML roles *(beta)*


> [!CAUTION]
> **Caution:** These roles and their product-specific permissions are **beta releases** . This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy.   
> Feature availability and support for these Firebase IAM roles will continue to improve as the tool matures.

<br />

| Role | Description | Permissions |
|---|---|---|
| **Firebase ML Admin** `roles/firebaseml.admin` *(beta)* | Full read/write access to Firebase ML resources | **Firebase ML Admin** permissions firebaseml.models.create firebaseml.models.get firebaseml.models.list firebaseml.models.update firebaseml.models.delete firebaseml.modelversions.create firebaseml.modelversions.get firebaseml.modelversions.list firebaseml.modelversions.update firebaseml.modelversions.delete firebaseml.compressionjobs.create firebaseml.compressionjobs.get firebaseml.compressionjobs.list firebaseml.compressionjobs.update firebaseml.compressionjobs.delete firebaseml.compressionjobs.start |
| **Firebase ML Viewer** `roles/firebaseml.viewer` *(beta)* | Read-only access to Firebase ML resources | **Firebase ML Viewer** permissions firebaseml.models.get firebaseml.models.list firebaseml.modelversions.get firebaseml.modelversions.list firebaseml.compressionjobs.get firebaseml.compressionjobs.list |

## Firebase Performance Monitoring roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Performance Monitoring Admin** `roles/firebaseperformance.admin` | Full read/write access to Performance Monitoring resources <br /> Configure and receive Performance Monitoring alerts | **Performance Monitoring Admin** permissions firebaseperformance.config.create firebaseperformance.config.delete firebaseperformance.config.update firebaseperformance.data.get |
| **Firebase Performance Monitoring Viewer** `roles/firebaseperformance.viewer` | Read-only access to Performance Monitoring resources | **Performance Monitoring Viewer** permissions firebaseperformance.data.get |

## Firebase Realtime Database roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Realtime Database Admin** `roles/firebasedatabase.admin` | Full read/write access to Realtime Database resources | **Realtime Database Admin** permissions firebasedatabase.instances.create firebasedatabase.instances.get firebasedatabase.instances.list firebasedatabase.instances.update |
| **Firebase Realtime Database Viewer** `roles/firebasedatabase.viewer` | Read-only access to Realtime Database resources | **Realtime Database Viewer** permissions firebasedatabase.instances.get firebasedatabase.instances.list |

## Firebase Remote Config roles

| Role | Description | Permissions |
|---|---|---|
| **Firebase Remote Config Admin** `roles/cloudconfig.admin` | Full read/write access to Remote Config resources | **Remote Config Admin** permissions cloudconfig.configs.get cloudconfig.configs.update |
| **Firebase Remote Config Viewer** `roles/cloudconfig.viewer` | Read-only access to Remote Config resources | **Remote Config Viewer** permissions cloudconfig.configs.get |

## Firebase Test Lab roles

Firebase Test Lab requires access to Cloud Storage buckets, so it
requires a very specific set of permissions that aren't all included in the
standard Firebase predefined roles. To grant access to Test Lab, use one of
the solutions described in the
[Firebase Test Lab permissions](https://firebase.google.com/docs/projects/iam/permissions#test-lab)
section.
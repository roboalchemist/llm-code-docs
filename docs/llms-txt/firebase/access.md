# Source: https://firebase.google.com/docs/extensions/publishers/access.md.txt

<br />

For an extension to perform its specified actions, Firebase grants each instance of an installed extension limited access to the project and its data via a***service account***.

## What's a service account?

A[service account](https://cloud.google.com/iam/docs/understanding-service-accounts)is a special type of Google user account. It represents a non-human user that can make authorized API calls to Google services.

During installation of an extension, Firebase creates a service account for the extension in the project. Each installed instance of an extension has its own service account. If an extension instance is uninstalled, Firebase deletes the extension's service account.

Service accounts created for extensions are in the format:

**ext-** <var translate="no">extension-instance-id</var>***@*** <var translate="no">project-id</var>**.iam.gserviceaccount.com**

Firebase limits an extension's access to a project and its data by assigning specific[roles (bundles of permissions)](https://firebase.google.com/docs/projects/iam/roles)to the service account of the extension. When you build an extension, you determine which roles your extension requires to operate, then you list these roles and the reason your extension needs these roles in your`extension.yaml`file (see[example](https://firebase.google.com/docs/extensions/publishers/access#how-to-assign-roles)at the bottom of this page).

## Determine which roles your extension requires

When you build your extension, you determine the level of access that your extension requires to operate.
| An extension's access should be strictly limited to the scope of its tasks, so only assign roles to an extension's service account that are absolutely necessary.

During installation, theFirebaseCLI prompts for the user to accept the access level granted by each role. If your extension requests more roles than it actually needs, then users may be less likely to install it.

1. Determine if your extension interacts with a product:

   - **If your extension*interacts*with a product**, then you need to give your extension access to that product.

     For example, if your extension*writes* data to aRealtime Databaseinstance, then your extension needs aRealtime Databaserole (specifically,`firebasedatabase.admin`).
   - **If your extension just*listens*for a triggering event from a product** , then your extension does***not***need a role associated with that product.

     For example, if your extension*triggers* upon a write to aRealtime Databaseinstance (but doesn't write anything to the database), then your extension does***not*** need aRealtime Databaserole.
2. After you've determined with which products your extension*interacts*, you need to decide which role is required for that specific interaction. Some products offer different roles depending on the action or set of actions performed.

   For example, say your extension interacts with aCloud Storagebucket. The`storage.objectCreator`role would allow the extension to*create* an object in aCloud Storagebucket, but that role wouldn't allow the extension to view, delete, or overwrite objects. To enable the extension to perform those additional actions, you need to assign the`storage.objectAdmin`role instead.

Refer to the section at the bottom of this page to view all the[supported roles](https://firebase.google.com/docs/extensions/publishers/access#supported-roles)that you may assign your extension's service account. To learn about each role's description and permissions granted, visit the[Firebase documentation](https://firebase.google.com/docs/projects/iam/roles-predefined-product)or[Google Cloud documentation](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles). You can also look up roles in the Google Cloud console's[IAM \& Admin panel](https://console.cloud.google.com/iam-admin/roles).

## How to assign roles to an extension

List the IAM roles required for your extension to operate in the`roles`section of your`extension.yaml`file.

Here's an example for an extension that listens to a specifiedFirebase Realtime Databasepath. When triggered, the extension updates a user account email (interaction withFirebase Authentication) and sends a notification (interaction withFirebase Cloud Messaging). Notice the following:

- Even though the extension*triggers* from aRealtime Databaseevent, the`firebasedatabase.admin`role isn't listed (listening isn't considered an*interaction*).
- Since the extension*interacts* withAuthenticationandCloud Messaging, the extension requires roles to access those products (`firebaseauth.admin`and`firebasenotifications.admin`, respectively).

    # extension.yaml
    ...

    # Roles assigned to the extension's service account by Firebase during installation
    roles:
      - role: firebaseauth.admin
        reason: Required to update the email address of the user account

      - role: firebasenotifications.admin
        reason: Required to send a notification that the email address has been updated

    ...

In your`extension.yaml`file, use the following fields to assign a role to an extension's service account:

|        **Field**        | **Type** |                                                                                     **Description**                                                                                      |
|-------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `role` *(required)*     | string   | Name of the[IAM role](https://firebase.google.com/docs/extensions/publishers/access#supported-roles)needed by the extension to operate                                                   |
| `reason` *(required)*   | string   | Brief description of the reason why the extension needs the access granted by the role Make sure to provide enough detail so that a user can understand how the extension uses the role. |
| `resource` *(optional)* | string   | Which resource's IAM policy this role should be added to. If omitted, defaults to`projects/${project_id}`. Supported values are`projects/*`and`projects/*/buckets/*`.                    |

## Reduce the scope of roles

Extensions should follow the principle of least privilege and only request access to the resources they need. You can limit an extension's scope of access by using the`role.resource`field. For example, if your extension needs to write objects to a Cloud Storage bucket, you could use the following role:  

    roles:
      - role: storage.objectCreator
        reason: Needed in order to write
        resource: projects/${PROJECT_ID}/buckets/${STORAGE_BUCKET}

This lets the extension access only the bucket it needs, and not others on the same project.

This field supports projects (`projects/{project_id}`) and Storage buckets (`projects/{project_id}/buckets/{bucket_id}`).

## Supported roles for extensions

The following table lists the supported IAM roles for interacting with Firebase products. Most of the roles in this table are[Firebase product-level roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product), but some are managed directly by Google Cloud (specifically,[Cloud Firestore](https://cloud.google.com/datastore/docs/access/iam)and[Cloud Storage](https://cloud.google.com/storage/docs/access-control/iam-roles)).

### Firebase products

| **If your extension interacts with...** |                                                                                                                                     **Assign one of these roles...**                                                                                                                                     |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cloud Firestore                         | datastore.importExportAdmin datastore.indexAdmin datastore.owner datastore.user datastore.viewer                                                                                                                                                                                                         |
| Cloud Storage for Firebase              | storage.admin storage.objectAdmin storage.objectCreator storage.objectViewer                                                                                                                                                                                                                             |
| Firebase App Distribution               | firebaseappdistro.admin firebaseappdistro.viewer                                                                                                                                                                                                                                                         |
| Firebase Authentication                 | firebaseauth.admin firebaseauth.viewer                                                                                                                                                                                                                                                                   |
| Firebase A/B Testing                    | firebaseabt.admin firebaseabt.viewer                                                                                                                                                                                                                                                                     |
| Firebase Cloud Messaging                | firebasenotifications.admin firebasenotifications.viewer**Note:** Extensions currently don't support any roles that permit sending FCM messages. For now, as a workaround, you can use the[FCM REST API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send)to send messages. |
| Firebase Crashlytics                    | firebasecrashlytics.admin firebasecrashlytics.viewer                                                                                                                                                                                                                                                     |
| Firebase Hosting                        | firebasehosting.admin firebasehosting.viewer                                                                                                                                                                                                                                                             |
| Firebase In-App Messaging               | firebaseinappmessaging.admin firebaseinappmessaging.viewer                                                                                                                                                                                                                                               |
| Firebase ML                             | firebaseml.admin firebaseml.viewer                                                                                                                                                                                                                                                                       |
| Firebase Performance Monitoring         | firebaseperformance.viewer firebaseperformance.reader firebaseperformance.writer                                                                                                                                                                                                                         |
| Firebase Realtime Database              | firebasedatabase.admin firebasedatabase.viewer                                                                                                                                                                                                                                                           |
| Security rules                          | firebaserules.viewer firebaserules.developer firebaserules.deployer                                                                                                                                                                                                                                      |
| Google Analytics                        | firebaseanalytics.admin firebaseanalytics.viewer                                                                                                                                                                                                                                                         |

### Google Cloud products

Learn about these roles in the[Google Cloud documentation](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles).

| **If your extension interacts with...** |                                                                              **Assign one of these roles...**                                                                               |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Actions                                 | actions.Admin actions.Viewer                                                                                                                                                                |
| Apigee                                  | apigee.analyticsAgent apigee.analyticsEditor apigee.analyticsViewer apigee.apiCreator apigee.deployer apigee.developerAdmin apigee.readOnlyAdmin apigee.synchronizerManager                 |
| App Engine                              | appengine.appAdmin appengine.appViewer appengine.codeViewer appengine.deployer appengine.serviceAdmin                                                                                       |
| AutoML                                  | automl.editor automl.predictor automl.viewer                                                                                                                                                |
| BigQuery                                | bigquery.connectionAdmin bigquery.connectionUser bigquery.dataEditor bigquery.dataOwner bigquery.dataViewer bigquery.jobUser bigquery.metadataViewer bigquery.readSessionUser bigquery.user |
| Cloud Bigtable                          | bigtable.reader bigtable.user bigtable.viewer                                                                                                                                               |
| Billing                                 | billing.viewer                                                                                                                                                                              |
| Hangout Chats                           | chat.owner chat.reader                                                                                                                                                                      |
| Cloud Asset                             | cloudasset.owner cloudasset.viewer                                                                                                                                                          |
| Cloud Data Fusion                       | datafusion.admin datafusion.viewer                                                                                                                                                          |
| Cloud Debugger                          | clouddebugger.agent clouddebugger.user                                                                                                                                                      |
| Cloud Functions                         | cloudfunctions.invoker cloudfunctions.viewer                                                                                                                                                |
| Cloud IAP                               | iap.admin iap.httpsResourceAccessor iap.settingsAdmin iap.tunnelResourceAccessor                                                                                                            |
| Cloud IoT                               | cloudiot.deviceController cloudiot.editor cloudiot.provisioner cloudiot.viewer                                                                                                              |
| Stackdriver Profiler                    | cloudprofiler.agent cloudprofiler.user                                                                                                                                                      |
| Cloud Scheduler                         | cloudscheduler.admin cloudscheduler.jobRunner cloudscheduler.viewer                                                                                                                         |
| Cloud Security Scanner                  | cloudsecurityscanner.editor cloudsecurityscanner.runner cloudsecurityscanner.viewer                                                                                                         |
| Cloud SQL                               | cloudsql.client cloudsql.editor cloudsql.viewer                                                                                                                                             |
| Cloud Trace                             | cloudtrace.admin cloudtrace.agent cloudtrace.user                                                                                                                                           |
| Dataflow                                | dataflow.developer dataflow.viewer dataflow.worker                                                                                                                                          |
| Dialogflow                              | dialogflow.admin dialogflow.client dialogflow.reader                                                                                                                                        |
| Cloud Data Loss Prevention              | dlp.reader dlp.user                                                                                                                                                                         |
| Error Reporting                         | errorreporting.user errorreporting.viewer errorreporting.writer                                                                                                                             |
| Eventarc                                | eventarc.publisher eventarc.eventReceiver                                                                                                                                                   |
| Cloud Filestore                         | file.editor file.viewer                                                                                                                                                                     |
| Logging                                 | logging.configWriter logging.logWriter logging.privateLogViewer logging.viewer                                                                                                              |
| Machine Learning Engine                 | ml.developer ml.jobOwner ml.modelOwner ml.modelUser ml.operationOwner ml.viewer                                                                                                             |
| Monitoring                              | monitoring.editor monitoring.metricWriter monitoring.viewer                                                                                                                                 |
| AI Notebooks                            | notebooks.admin notebooks.viewer                                                                                                                                                            |
| Pub/Sub                                 | pubsub.editor pubsub.publisher pubsub.subscriber pubsub.viewer                                                                                                                              |
| Memorystore Redis                       | redis.editor redis.viewer                                                                                                                                                                   |
| Cloud Run                               | run.invoker                                                                                                                                                                                 |
| Source                                  | source.reader source.writer                                                                                                                                                                 |
| Cloud Spanner                           | spanner.databaseAdmin spanner.databaseReader spanner.databaseUser spanner.viewer                                                                                                            |
| Service Usage                           | serviceusage.apiKeysMetadataViewer                                                                                                                                                          |
| Cloud Storage Transfer Service          | storagetransfer.user storagetransfer.viewer                                                                                                                                                 |
| Cloud Transcoder                        | transcoder.admin transcoder.viewer                                                                                                                                                          |
| Vertex AI                               | aiplatform.user                                                                                                                                                                             |
| Other                                   | identitytoolkit.admin identitytoolkit.viewer                                                                                                                                                |
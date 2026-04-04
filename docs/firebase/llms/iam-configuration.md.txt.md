# Source: https://firebase.google.com/docs/data-connect/iam-configuration.md.txt

To use Firebase Data Connect, you'll need to assign IAM roles that allow
managing connectors, accessing Cloud SQL, and generating SDKs. Make sure the
service account running Data Connect has the required permissions.

## Granular IAM roles for Data Connect

Firebase basic roles and predefined roles map to lower-level
Data Connect roles. Refer to the table for the mapping.

To manage individual IAM role assignments for Data Connect at a more
granular level, use the [Google Cloud console](https://console.cloud.google.com).

> [!NOTE]
> **Note:** For workflows associated with these IAM roles, see the [guide to
> managing services and databases](https://firebase.google.com/docs/data-connect/manage-services-and-databases#manage-data-connect-users).

| IAM role | Permissions |
|---|---|
| `firebasedataconnect.googleapis.com/admin` <br /> **Firebase Data Connect API Admin** <br /> This role includes Firebase Data Connect API Viewer. It is equivalent to `firebasedataconnect.*`. <br /> This is provided by the Cloud Owner, Cloud Editor, Firebase Admin and Firebase Develop Admin roles. | Full access to Firebase Data Connect API resources, including data. <br /> `firebasedataconnect.googleapis.com/operations.delete` `firebasedataconnect.googleapis.com/operations.cancel` `firebasedataconnect.googleapis.com/services.create` `firebasedataconnect.googleapis.com/services.update` `firebasedataconnect.googleapis.com/services.delete` `firebasedataconnect.googleapis.com/services.executeGraphql` `firebasedataconnect.googleapis.com/services.executeGraphqlRead` `firebasedataconnect.googleapis.com/schemas.create` `firebasedataconnect.googleapis.com/schemas.update` `firebasedataconnect.googleapis.com/schemas.delete` `firebasedataconnect.googleapis.com/schemaRevisions.create` `firebasedataconnect.googleapis.com/schemaRevisions.delete` `firebasedataconnect.googleapis.com/connectors.create` `firebasedataconnect.googleapis.com/connectors.update` `firebasedataconnect.googleapis.com/connectors.delete` `firebasedataconnect.googleapis.com/connectorRevisions.create` `firebasedataconnect.googleapis.com/connectorRevisions.delete` |
| `firebasedataconnect.googleapis.com/viewer` <br /> **Firebase Data Connect API Viewer** <br /> This is provided by the Cloud Owner, Cloud Editor, Cloud Viewer, Firebase Admin, Firebase Viewer, Firebase Develop Admin and Firebase Develop Viewer roles. | Read-only access to Firebase Data Connect API resources. Role does not grant access to data. <br /> `cloudresourcemanager.googleapis.com/projects.list` `cloudresourcemanager.googleapis.com/projects.get` <br /> `firebasedataconnect.googleapis.com/operations.list` `firebasedataconnect.googleapis.com/operations.get` `firebasedataconnect.googleapis.com/locations.list` `firebasedataconnect.googleapis.com/locations.get` `firebasedataconnect.googleapis.com/services.list` `firebasedataconnect.googleapis.com/services.get` `firebasedataconnect.googleapis.com/schemas.list` `firebasedataconnect.googleapis.com/schemas.get` `firebasedataconnect.googleapis.com/schemaRevisions.list` `firebasedataconnect.googleapis.com/schemaRevisions.get` `firebasedataconnect.googleapis.com/connectors.list` `firebasedataconnect.googleapis.com/connectors.get` `firebasedataconnect.googleapis.com/connectorRevisions.list` `firebasedataconnect.googleapis.com/connectorRevisions.get` |
| `firebasedataconnect.googleapis.com/dataAdmin` <br /> **Firebase Data Connect API Data Admin** <br /> This is provided by the Cloud Owner, Cloud Editor, Firebase Admin and Firebase Develop Admin roles. | Full read and write access to data sources. <br /> `firebasedataconnect.googleapis.com/services.executeGraphql` `firebasedataconnect.googleapis.com/services.executeGraphqlRead` |
| `firebasedataconnect.googleapis.com/dataViewer` <br /> **Firebase Data Connect API Data Viewer** <br /> This is provided by the Cloud Owner, Cloud Editor, Firebase Admin and Firebase Develop Admin roles. | Read-only access to data sources. <br /> `firebasedataconnect.googleapis.com/services.executeGraphqlRead` |
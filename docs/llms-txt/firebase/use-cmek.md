# Source: https://firebase.google.com/docs/firestore/use-cmek.md.txt

# Source: https://firebase.google.com/docs/firestore/enterprise/use-cmek.md.txt

<br />

This page describes how to perform tasks related to[customer-managed encryption keys (CMEK) for Cloud Firestore with MongoDB compatibility](https://firebase.google.com/docs/firestore/enterprise/cmek). For more information about CMEK in general, including when and why to enable it, see the[Cloud KMS documentation](https://cloud.google.com/kms/docs/cmek).
| **Note:** For information about access to this release, see the[access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA).

## Prepare your CMEK keys

Before you can create a CMEK-protected Cloud Firestore with MongoDB compatibility database, you must complete the following steps:

1. [Request access to the Cloud Firestore with MongoDB compatibility CMEK feature](https://firebase.google.com/docs/firestore/enterprise/use-cmek#request-cmek-access).
2. [Create (or retrieve) a Cloud Firestore with MongoDB compatibility service agent](https://firebase.google.com/docs/firestore/enterprise/use-cmek#create-service-agent).
3. [Create a CMEK key](https://firebase.google.com/docs/firestore/enterprise/use-cmek#create-key).
4. [Configure IAM settings for that key](https://firebase.google.com/docs/firestore/enterprise/use-cmek#set-iam).

Complete these steps for each project that will contain CMEK-protected Cloud Firestore with MongoDB compatibility databases. If you later create a new CMEK key, you must configure IAM settings for that key.
| **Note:** The`gcloud`commands on this page show placeholders for twoGoogle Cloudprojects: the project that contains Cloud Firestore with MongoDB compatibility databases,<var translate="no">FIRESTORE_PROJECT</var>, and the project that contains your CMEK key(s),<var translate="no">KMS_PROJECT</var>. However, you can use the same project for your Cloud Firestore with MongoDB compatibility databases and CMEK keys.

### Request access

Before you create a Cloud Firestore with MongoDB compatibility service agent, request access to the CMEK feature by filling in the[access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA).

### Create a Cloud Firestore with MongoDB compatibility service agent

Before you create a CMEK key, you must have a Cloud Firestore with MongoDB compatibility[service agent](https://cloud.google.com/iam/docs/service-agents), which is a type of Google-managed service account that Cloud Firestore with MongoDB compatibility uses to access the key.

Run the[services identity create](https://cloud.google.com/sdk/gcloud/reference/beta/services/identity/create)command to create the service agent that Cloud Firestore with MongoDB compatibility uses to access the CMEK key on your behalf. This command creates the service account if it does not already exist, then displays it.  

    gcloud beta services identity create \
        --service=firestore.googleapis.com \
        --project <var translate="no">FIRESTORE_PROJECT</var>

Replace<var translate="no">FIRESTORE_PROJECT</var>with the project you plan to use for your Cloud Firestore with MongoDB compatibility databases.

The command displays the service agent ID, which is formatted like an email address. Record the output email string, because you'll use it in a later step.  

    Service identity created:
    service-xxx@gcp-sa-firestore.

### Create a key

You can use a key created directly in Cloud KMS or an externally managed key that you make available with[Cloud External Key Manager](https://cloud.google.com/kms/docs/ekm).

The Cloud KMS[key location](https://cloud.google.com/kms/docs/locations)must be the same as the location of the Cloud Firestore with MongoDB compatibility database that it will be used with.

- For[regional database locations](https://firebase.google.com/docs/firestore/enterprise/locations#location-r), use the same location name for key ring, key, and database because the location names have a one-to-one mapping.

  For example, if you want to create a CMEK-protected database in`us-west1`, create a key ring and key in`us-west1`.
- For[multi-region database locations](https://firebase.google.com/docs/firestore/enterprise/locations#location-mr), use the location name of the[KMS multi-region location](https://cloud.google.com/kms/docs/locations):

  - Use the Cloud KMS`us`multi-region location for the Cloud Firestore with MongoDB compatibility`nam5`multi-region location.

  - Use the Cloud KMS`europe`multi-region location for the Cloud Firestore with MongoDB compatibility`eur3`multi-region location.

In theGoogle Cloudproject where you want to manage your keys, complete the following:

1. [Enable the Cloud KMS API](https://console.cloud.google.com/flows/enableapi?apiid=cloudkms.googleapis.com).

2. Create a key ring and a key using one of the following options:

   - [Create the key ring and key directly in Cloud KMS](https://cloud.google.com/kms/docs/creating-keys).
   - Use an externally managed key.[Create the external key](https://cloud.google.com/kms/docs/ekm-internet#create_external_key)and then[create an Cloud EKM key](https://cloud.google.com/kms/docs/ekm-internet#create_ekm_key)to make the key available through Cloud KMS.

### Configure IAM settings for the key

### Console

To grant an Cloud KMS role to your service agent, do the following. You are also able to grant permission at the key or key-ring level if you want lower granularity.

1. In the Google Cloud console, go to the**IAM**page.

   [Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)
2. Click**Add**.

3. Enter the email-formatted ID for your Cloud Firestore with MongoDB compatibility service agent.

4. Select the**Cloud KMS CryptoKey Encrypter/Decrypter**role.

5. Click**Save**.

### gcloud

Grant the`cloudkms.cryptoKeyEncrypterDecrypter`role to your service agent:  

    gcloud kms keys add-iam-policy-binding <var translate="no">KMS_KEY</var> \
    --keyring <var translate="no">KMS_KEYRING</var>\
    --location <var translate="no">KMS_LOCATION</var> \
    --member serviceAccount:<var translate="no">SERVICE_AGENT_EMAIL</var> \
    --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
    --project <var translate="no">KMS_PROJECT</var>

Replace the following:

- <var translate="no">KMS_KEY</var>with the name that you assigned to the key
- <var translate="no">KMS_KEYRING</var>with the KMS key ring that contains the key
- <var translate="no">KMS_LOCATION</var>with the region that contains the key ring
- <var translate="no">SERVICE_AGENT_EMAIL</var>with the email-formatted identifier for the service agent that you are granting access to
- <var translate="no">KMS_PROJECT</var>with the project that contains the key

The terminal should display a response similar to the following:  

    Updated IAM policy for key <var translate="no">KMS_KEY</var>.
    bindings:
    - members:
    - serviceAccount:
    service-{project-number}@gcp-sa-firestore.
    role: roles/cloudkms.cryptoKeyEncrypterDecrypter

## Create a CMEK-enabled database

After your CMEK keys are created and configured, you can create a CMEK-protected database. Existing Cloud Firestore with MongoDB compatibility databases that are protected by Google default encryption can't be converted to use CMEK.

You can choose an encryption type and key only when you create a CMEK-enabled database.  

### Console

1. In the Google Cloud console, go to the**Databases**page.

   [Go to the Databases page](https://console.cloud.google.com/firestore/databases)
2. Click**Create a Firestore Database**.

3. Enter a database ID.

4. Select Enterprise Edition.

5. Select a location for your database.

6. Click**Show Encryption Options** , and then select**Cloud KMS key**.

7. Select or enter the resource name for the CMEK key that you want to use for the database.

   | **Note:** You can't add or change the CMEK key later.
8. The list of keys is limited to the currentGoogle Cloudproject and the database location that you selected. To use a key from a differentGoogle Cloudproject, click**Switch Project** or**Enter Key Manually**.

9. If you are prompted to grant key permission to the Cloud Firestore with MongoDB compatibility service account, click**Grant** . To create a CMEK database, your Cloud Firestore with MongoDB compatibility service account must be granted the`cloudkms.cryptoKeyEncrypterDecrypter`role.

10. Select security rules for mobile and web clients.

11. Click**Create Database**.

After the database is created, you can verify that the database is CMEK-enabled by viewing**Database details**:

- If your database is protected by CMEK, the**Encryption type** field shows as**Customer-managed** and the**Encryption key**field lists the corresponding Cloud KMS and the key version that is used to protect this database.
- If your database is not protected by CMEK, the**Encryption type** field shows as**Google-managed**.

### gcloud

Before you create a CMEK-enabled database withGoogle Cloud CLI, install the latest version and authorize thegcloud CLI. For more information, see[Install thegcloud CLI](https://cloud.google.com/sdk/docs/install).  

    gcloud firestore databases create \
        --location=<var translate="no">FIRESTORE_DATABASE_LOCATION</var> \
        --database=<var translate="no">DATABASE_ID</var> \
        --edition=enterprise \
        --kms-key-name=<var translate="no">KMS_KEY_NAME</var> \
        --project=<var translate="no">FIRESTORE_PROJECT</var>

Replace the following:

- <var translate="no">FIRESTORE_DATABASE_LOCATION</var>with the location for the database
- <var translate="no">DATABASE_ID</var>with an ID for the database
- <var translate="no">KMS_KEY_NAME</var>with the name you assigned to the key. Use the full resource name for the key in the following format:

  `projects/`<var translate="no">KMS_PROJECT</var>`/locations/`<var translate="no">KMS_LOCATION</var>`/keyRings/`<var translate="no">KMS_KEYRING_ID</var>`/cryptoKeys/`<var translate="no">KMS_KEY_ID</var>
- <var translate="no">FIRESTORE_PROJECT</var>with the project to use for your Cloud Firestore with MongoDB compatibility database

### Access a CMEK-protected database

All the read, write, and query operations sent to a CMEK-protected database should function the same as with a Google default encrypted database. For example, you don't need to provide a key for each request.

## Restore a CMEK-protected database

Before you restore CMEK-protected database from a backup:

- Decide if you want to restore the database to CMEK encryption, to[Google's default encryption](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption)(non-CMEK), or to the same encryption as the backup.
- Prepare the key (primary-version) and the key version that you used to encrypt the backup. Enable both the key and the key version.

### gcloud

### Restore a CMEK-protected database to CMEK encryption

To restore to CMEK encryption, run the[`gcloud firestore databases restore`](https://cloud.google.com/sdk/gcloud/reference/alpha/firestore/databases/restore)command with the optional`encryption-type`and`kms-key-name`flags to configure the encryption type for the restored database. If you don't specify the encryption type, the restored database will use the same encryption configuration as the backup.  

    gcloud firestore databases restore \
    --encryption-type=customer-managed-encryption \
    --kms-key-name=<var translate="no">KMS_KEY_NAME</var>

Replace<var translate="no">KMS_KEY_NAME</var>with the name that you assigned to the key. Use the full resource name for the key in the following format:

`projects/`<var translate="no">KMS_PROJECT</var>`/locations/`<var translate="no">KMS_LOCATION</var>`/keyRings/`<var translate="no">KMS_KEYRING_ID</var>`/cryptoKeys/`<var translate="no">KMS_KEY_ID</var>

### Restore a CMEK-protected database to default encryption

To restore to[Google's default encryption](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption)(non-CMEK), set the`encryption-type`flag in the following way:  

    gcloud firestore databases restore \
    --encryption-type=google-default-encryption

### Restore a CMEK-protected database to the same encryption type as the backup

To restore to the same encryption type as the backup, set the`encryption-type`flag in the following way:  

    gcloud firestore databases restore --encryption-type=use-source-encryption

### Firebase CLI

### Restore a CMEK-protected database to CMEK encryption

To restore to CMEK encryption, use the optional`encryption-type`and`kms-key-name`flag. If you don't specify the encryption type, the restored database will use the same encryption configuration as the backup.  

    firebase firestore:databases:restore \
    --database <var translate="no">DATABASE_ID</var> \
    --backup 'projects/<var translate="no">FIRESTORE_PROJECT</var>/locations/<var translate="no">FIRESTORE_LOCATION</var>/backups/<var translate="no">BACKUP_ID</var>' \
    --encryption-type CUSTOMER_MANAGED_ENCRYPTION \
    --kms-key-name projects/<var translate="no">KMS_PROJECT</var>/locations/<var translate="no">KMS_LOCATION</var>/keyRings/<var translate="no">KMS_KEYRING_ID</var>/cryptoKeys/<var translate="no">KMS_KEY_ID</var> \
    --project <var translate="no">FIRESTORE_PROJECT</var>

Replace the following:

- <var translate="no">DATABASE_ID</var>with the ID of your database
- <var translate="no">FIRESTORE_PROJECT</var>with the project to use for your Cloud Firestore with MongoDB compatibility database
- <var translate="no">FIRESTORE_LOCATION</var>with the location of your Cloud Firestore with MongoDB compatibility database
- <var translate="no">BACKUP_ID</var>with the ID of your backup
- <var translate="no">KMS_PROJECT</var>with the project that contains your CMEK key
- <var translate="no">KMS_LOCATION</var>with the location that contains your CMEK key and key ring
- <var translate="no">KMS_KEYRING_ID</var>with the ID of your CMEK key ring

Confirm that your restored Cloud Firestore with MongoDB compatibility database is CMEK-encrypted:  

    firebase firestore:databases:get <var translate="no">DATABASE_ID</var> --project <var translate="no">FIRESTORE_PROJECT</var>

### Restore a CMEK-protected database to default encryption

To restore to[Google's default encryption](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption)(non-CMEK), set the`encryption-type`flag in the following way:  

    firebase firestore:databases:restore \
    --database <var translate="no">DATABASE_ID</var> \
    --backup 'projects/<var translate="no">FIRESTORE_PROJECT</var>/locations/<var translate="no">FIRESTORE_LOCATION</var>/backups/<var translate="no">BACKUP_ID</var>' \
    --encryption-type GOOGLE_DEFAULT_ENCRYPTION \
    --project <var translate="no">FIRESTORE_PROJECT</var>

Replace the following:

- <var translate="no">DATABASE_ID</var>with the ID of your database
- <var translate="no">FIRESTORE_PROJECT</var>with the project to use for your Cloud Firestore with MongoDB compatibility database
- <var translate="no">FIRESTORE_LOCATION</var>with the location of your Cloud Firestore with MongoDB compatibility database
- <var translate="no">BACKUP_ID</var>with the ID of your backup

### Restore a CMEK-protected database to the same encryption type as the backup

To restore to the same encryption type as the backup, set the`encryption-type`flag in the following way:  

    firebase firestore:databases:restore \
    --database <var translate="no">DATABASE_ID</var> \
    --backup 'projects/<var translate="no">FIRESTORE_PROJECT</var>/locations/<var translate="no">FIRESTORE_LOCATION</var>/backups/<var translate="no">BACKUP_ID</var>' \
    --encryption-type USE_SOURCE_ENCRYPTION

Replace the following:

- <var translate="no">DATABASE_ID</var>with the ID of your database
- <var translate="no">FIRESTORE_PROJECT</var>with the project to use for your Cloud Firestore with MongoDB compatibility database
- <var translate="no">FIRESTORE_LOCATION</var>with the location of your Cloud Firestore with MongoDB compatibility database
- <var translate="no">BACKUP_ID</var>with the ID of your backup

## Clone a CMEK-protected database

Before you clone a CMEK-protected database:

- Decide if you want to clone the database to CMEK encryption, to[Google's default encryption](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption)(non-CMEK), or to the same encryption as the source database.
- Prepare the key (primary-version) and the key version that you used to encrypt the source database. Enable both the key and the key version.

### gcloud

### Clone a CMEK-protected database to CMEK encryption

To clone to CMEK encryption, run the[gcloud firestore databases clone](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/clone)command with the optional`encryption-type`and`kms-key-name`flags to configure the encryption type for the cloned database. If you don't specify the encryption type, the cloned database will use the same encryption configuration as the source database.  

    gcloud firestore databases clone \
    --encryption-type=customer-managed-encryption \
    --kms-key-name=<var translate="no">KMS_KEY_NAME</var>

Replace<var translate="no">KMS_KEY_NAME</var>with the name that you assigned to the key. Use the full resource name for the key in the following format:  

    projects/<var translate="no">KMS_PROJECT</var>/locations/<var translate="no">KMS_LOCATION</var>/keyRings/<var translate="no">KMS_KEYRING_ID</var>/cryptoKeys/<var translate="no">KMS_KEY_ID</var>

### Clone a CMEK-protected database to default encryption

To clone to[Google's default encryption](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption)(non-CMEK), set the`encryption-type`flag in the following way:  

    gcloud firestore databases clone \
    --encryption-type=google-default-encryption

### Clone a CMEK-protected database to the same encryption type as the source database

To clone to the same encryption type as the source database, set the`encryption-type`flag in the following way:  

    gcloud firestore databases clone \
    --encryption-type=use-source-encryption

This is also the default behavior if`--encryption-type`is unspecified.

### Firebase CLI

### Clone a CMEK-protected database to CMEK encryption

To clone to CMEK encryption, run the`firebase firestore:databases:clone`command with the optional`encryption-type`and`kms-key-name`flags to configure the encryption type for the cloned database. If you don't specify the encryption type, the cloned database will use the same encryption configuration as the source database.  

    firebase firestore:databases:clone \
    <var translate="no">SOURCE_DATABASE</var> \
    <var translate="no">DESTINATION_DATABASE</var> \
    --encryption-type=CUSTOMER_MANAGED_ENCRYPTION \
    --kms-key-name=<var translate="no">KMS_KEY_NAME</var>

Replace<var translate="no">KMS_KEY_NAME</var>with the name that you assigned to the key. Use the full resource name for the key in the following format:  

    projects/<var translate="no">KMS_PROJECT</var>/locations/<var translate="no">KMS_LOCATION</var>/keyRings/<var translate="no">KMS_KEYRING_ID</var>/cryptoKeys/<var translate="no">KMS_KEY_ID</var>

### Clone a CMEK-protected database to default encryption

To clone to[Google's default encryption](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption)(non-CMEK), set the`encryption-type`flag in the following way:  

    firebase firestore:databases:clone \
    <var translate="no">SOURCE_DATABASE</var> \
    <var translate="no">DESTINATION_DATABASE</var> \
    --encryption-type=GOOGLE_DEFAULT_ENCRYPTION

### Clone a CMEK-protected database to the same encryption type as the source database

To clone to the same encryption type as the source database, set the`encryption-type`flag in the following way:  

      firebase firestore:databases:clone \
    <var translate="no">SOURCE_DATABASE</var> \
    <var translate="no">DESTINATION_DATABASE</var> \
    --encryption-type=USE_SOURCE_ENCRYPTION

This is also the default behavior if`--encryption-type`is unspecified.

## View the key in use

### gcloud

You can use the[databases describe](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/describe)gcloud CLIcommand to confirm database CMEK configuration:  

    gcloud firestore databases describe \
      --database=<var translate="no">DATABASE_ID</var> \
      --project=<var translate="no">FIRESTORE_PROJECT</var>

You should see CMEK information in the`cmekConfig`field in the response similar to the following:  

    cmekConfig:
        activeKeyVersion:
        - projects/PROJECT_ID/locations/us/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME/cryptoKeyVersions/1
        kmsKeyName: projects/PROJECT_ID/locations/us/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME
      locationId: nam5
      name: projects/PROJECT_ID/databases/DATABASE_ID

The response includes the following information:

- `kmsKeyName`: the full key resource name of the key that's used to encrypt your CMEK-protected database.
- `activeKeyVersion`: a list of all[key versions](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions)in use by the CMEK-protected database. During[key rotation](https://cloud.google.com/kms/docs/key-rotation), you can have multiple active key versions. Both the old key version and new key version need to be available during key rotation. Don't disable the old key version until it no longer appears in the`activeKeyVersion`field.

### REST API

HTTP request:  

    GET https://firestore.googleapis.com/v1/{name=projects/FIRESTORE_PROJECT/databases/DATABASE_ID}

In the request body configure CMEK in the`cmek_config.kms_key_name`field. Set to the full resource ID of a Cloud KMS key. Only a key in the same location as this database is allowed.

This value should be the Cloud KMS key resource ID in the format of`projects/{KMS_PROJECT}/locations/{KMS_LOCATION}/keyRings/{KMS_KEYRING_ID}/cryptoKeys/{KMS_KEY_ID}`.

For more details for other fields, see the[`database create`page](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/create).

Example request:  

    curl 'https://firestore.googleapis.com/v1/projects/FIRESTORE_PROJECT/databases/{DATABASE_ID}' \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-type: application/json"

Example response:  

    {
      "name": "projects/FIRESTORE_PROJECT/databases/{DATABASE_ID}",
      "locationId": "{FIRESTORE_DATABASE_LOCATION}",
      "type": "FIRESTORE_NATIVE",
      "cmekConfig": {
        "kmsKeyName": "projects/{KMS_PROJECT}/locations/{KMS_LOCATION}/keyRings/{KMS_KEYRING_ID}/cryptoKeys/{KMS_KEY_ID}",
        "activeKeyVersion": [
          "projects/{KMS_PROJECT}/locations/{KMS_LOCATION}/keyRings/{KMS_KEYRING_ID}/cryptoKeys/{KMS_KEY_ID}/cryptoKeyVersions/1"
        ]
      },
      ...
    }

## Disable a key

To disable a key associated with a database, complete the following:

1. [View the key versions in use for a database](https://firebase.google.com/docs/firestore/enterprise/use-cmek#view-key)
2. [Disable those key versions](https://cloud.google.com/kms/docs/enable-disable#disable)
3. Wait for the change to take effect and check if the data is no longer accessible. Changes typically take effect within minutes, but can take up to 3 hours.

When a key used by a database is disabled, expect to receive a`INVALID_ARGUMENT`exception with additional details in the error message, for example:  

    {
      "error": {
        "code": 400,
        "message": "Failed: (InvalidArgument) The customer-managed encryption key required by the requested resource is not accessible. Error reason: projects/{FIRESTORE_PROJECT}/locations/{KMS_LOCATION}/keyRings/{KMS_KEYRING_ID}/cryptoKeys/{KMS_KEY_ID}/cryptoKeyVersions/1 is not enabled, current state is: DISABLED.",
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.DebugInfo",
            "detail": "Failed: (InvalidArgument) The customer-managed encryption key required by the requested resource is not accessible. Error reason: projects/{FIRESTORE_PROJECT}/locations/{KMS_LOCATION}/keyRings/{KMS_KEYRING_ID}/cryptoKeys/{KMS_KEY_ID}/cryptoKeyVersions/1 is not enabled, current state is: DISABLED."
          }
        ]
      }
    }

## Enable a key

To re-enable a key associated with a database, complete the following:

1. [View the key versions in use for a database](https://firebase.google.com/docs/firestore/enterprise/use-cmek#view-key)
2. [Enable those key versions](https://cloud.google.com/kms/docs/enable-disable#enable)
3. Wait for the change to take effect and check if the data is no longer accessible. Changes typically take effect within minutes, but can take up to 3 hours.

## View audit logs for a Cloud KMS key

Before you enable Cloud KMS Data Access audit logs, you should be familiar with[Cloud Audit Logs](https://cloud.google.com/logging/docs/audit).

[Cloud KMS Data Access audit logs](https://cloud.google.com/kms/docs/audit-logging)show you when Cloud Firestore with MongoDB compatibility or any other products that are configured to use your CMEK key make encrypt or decrypt calls to Cloud KMS. Cloud Firestore with MongoDB compatibility does not issue an encrypt or decrypt call on every data request, but instead maintains a poller that checks the key periodically. The polling results appear in the audit logs.

You can set up and interact with the audit logs in the[Google Cloud console](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console):

1. Make sure that[logging is enabled](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable)for the Cloud KMS API in your project.

2. Go to**Cloud Logging**in the Google Cloud console.

   [Go toCloud Logging](https://console.cloud.google.com/logs/query)
3. Limit the log entries to your Cloud KMS key by adding the following lines to the Query builder:

       resource.type="cloudkms_cryptokey"
       resource.labels.key_ring_id = <var translate="no">KMS_KEYRING</var>
       resource.labels.crypto_key_id = <var translate="no">KMS_KEY</var>
       resource.labels.location=<var translate="no">KMS_LOCATION</var>

   Replace the following:
   - <var translate="no">KMS_KEY</var>with the name of the CMEK key
   - <var translate="no">KMS_KEYRING</var>with the KMS key ring that contains the key
   - <var translate="no">KMS_LOCATION</var>with the location of the key and key ring

   The log shows a couple log entries about every five minutes per database. The log entries look similar to these examples:  

       Info 2021-03-20 08:02:24.869 EDT Cloudkms.googleapis.com Decrypt projects/cloud-kms-project/locations/us-central1/keyRings/firestore-keys/cryptoKeys/my-cmek-key service-123456789123@gcp-sa-firestore.
       audit_log, method: "Decrypt", principal_email: "service-1234567891011@gcp-sa-firestore."

       Info 2021-03-20 08:02:24.913 EDT Cloudkms.googleapis.com Encrypt projects/cloud-kms-project/locations/us-central1/keyRings/firestore-keys/cryptoKeys/my-cmek-key service-123456789123@gcp-sa-firestore.
       audit_log, method: "Encrypt", principal_email: "service-123456789123@gcp-sa-firestore."

See[Understanding audit logs](https://cloud.google.com/logging/docs/audit/understanding-audit-logs)for details about interpreting audit logs.

## Configure a CMEK organization policy

To specify encryption compliance requirements for Cloud Firestore with MongoDB compatibility databases in your organization, use a[CMEK organization policy constraint](https://cloud.google.com/kms/docs/cmek-org-policy).

### Require CMEK protection

Configure`constraints/gcp.restrictNonCmekServices`to require CMEK for Cloud Firestore with MongoDB compatibility database creation. Set the constraint to`deny`and add`firestore.googleapis.com`to the deny list, for example:  

    gcloud resource-manager org-policies deny gcp.restrictNonCmekServices  is:firestore.googleapis.com --project=<var translate="no">FIRESTORE_PROJECT</var>

Replace<var translate="no">FIRESTORE_PROJECT</var>with the project to restrict.

To learn more about configuring organization policies, see[Creating and editing policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).

After the policy takes effect, you receive a`FAILED_PRECONDITION`exception and error message if you try to create a non-CMEK database under the affected project. For example, an exception looks like:  

    {
      "error": {
        "code": 400,
        "message": "Constraint 'constraints/gcp.restrictNonCmekServices' violated for 'projects/FIRESTORE_PROJECT' attempting to perform the operation 'google.firestore.admin.v1.FirestoreAdmin.CreateDatabase' with violated value 'firestore.googleapis.com'. See https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints for more information.",
        "status": "FAILED_PRECONDITION",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
            "violations": [
              {
                "type": "constraints/gcp.restrictNonCmekServices",
                "subject": "orgpolicy:projects/FIRESTORE_PROJECT",
                "description": "Constraint 'constraints/gcp.restrictNonCmekServices' violated for 'projects/FIRESTORE_PROJECT' attempting to perform the operation 'google.firestore.admin.v1.FirestoreAdmin.CreateDatabase' with violated value 'firestore.googleapis.com'. See https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints for more information."
              }
            ]

### Limit the use of keys for CMEK

To limit which Cloud KMS keys are used for CMEK protection, configure the`constraints/gcp.restrictCmekCryptoKeyProjects`constraint.

As a list constraint, the accepted values are resource hierarchy indicators (for example,`projects/PROJECT_ID`,`under:folders/FOLDER_ID`, and`under:organizations/ORGANIZATION_ID`). Use this constraint by configuring a list of resource hierarchy indicators and setting the constraint to**Allow**. This configuration restricts supported services so that CMEK keys can be chosen only from the listed projects, folders, and organizations. Requests to create CMEK-protected resources in configured services don't succeed without a Cloud Firestore with MongoDB compatibility key from one of the allowed resources.

The following example allows only keys from the<var translate="no">ALLOWED_KEY_PROJECT_ID</var>for CMEK-protected databases in the specified project:  

    gcloud resource-manager org-policies allow gcp.restrictCmekCryptoKeyProjects \
    under:projects/<var>ALLOWED_KEY_PROJECT_ID</var> \
    --project=<var>FIRESTORE_PROJECT</var>

After the policy takes effect, you receive a`FAILED_PRECONDITION`exception and an error message if you violate the constraint. An exception looks like the following:  

    {
      "error": {
        "code": 400,
        "message": "Constraint 'constraints/gcp.restrictCmekCryptoKeyProjects' violated for 'projects/FIRESTORE_PROJECT' attempting to perform the operation 'google.firestore.admin.v1.FirestoreAdmin.CreateDatabase' with violated value 'projects/{NOT_ALLOWED_KEY_PROJECT}'. See https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints for more information.",
        "status": "FAILED_PRECONDITION",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
            "violations": [
              {
                "type": "constraints/gcp.restrictCmekCryptoKeyProjects",
                "subject": "orgpolicy:projects/FIRESTORE_PROJECT",
                "description": "Constraint 'constraints/gcp.restrictCmekCryptoKeyProjects' violated for 'projects/FIRESTORE_PROJECT' attempting to perform the operation 'google.firestore.admin.v1.FirestoreAdmin.CreateDatabase' with violated value 'projects/{NOT_ALLOWED_KEY_PROJECT}'. See https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints for more information."
              }
            ]
          }
        ]
      }
    }

## What's next

- [Read the overview of Cloud Firestore with MongoDB compatibility and CMEK](https://firebase.google.com/docs/firestore/enterprise/cmek)
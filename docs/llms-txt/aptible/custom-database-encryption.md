# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-encryption/custom-database-encryption.md

# Custom Database Encryption

This section covers encryption using AWS Key Management Service. For more information about Aptible's default managed encryption, see [Database Encryption at rest](/core-concepts/managed-databases/managing-databases/database-encryption/overview).

Aptible supports providing your own encryption key for [Database](/core-concepts/managed-databases/overview) volumes using [AWS Key Management Service (KMS) customer-managed customer master keys (CMK)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). This layer of encryption is applied in addition to Aptible’s existing Database Encryption. Encryption using AWS KMS CMKs is ideal for those who want to retain absolute control over when their data is destroyed or for those who need to rotate their database encryption keys regularly.

> ❗️ CMKs are completely managed outside of Aptible. As a result, if there is an issue accessing a CMK, Aptible will be unable to decrypt the data. **If a CMK is deleted, Aptible will be unable to recover the data.**

# Creating a New CMK

CMKs used by Aptible must be symmetric and must not use imported key material. The CMK must be created in the same region as the Database that will be using the key. Aptible can support all other CMK options.

After creating a CMK, the key must be shared with Aptible's AWS account. When creating the CMK in the AWS console, you can specify that you would like to share the CMK with the AWS account ID `916150859591`. Alternatively, you can include the following statements in the policy for the key:

```json  theme={null}
{
    "Sid": "Allow use of the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::916150859591:root"
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*"
},
{
    "Sid": "Allow attachment of persistent resources",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::916150859591:root"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:ListGrants",
        "kms:RevokeGrant"
    ],
    "Resource": "*",
    "Condition": {
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
}
```

# Creating a new Database encrypted with a CMK

New databases encrypted with a CMK can be created via the Aptible CLI using the [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) command. The CMK should be passed in using the `--key-arn` flag, for example:

```shell  theme={null}
aptible db:create $HANDLE --type $TYPE --key-arn arn:aws:kms:us-east-1:111111111111:key/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
```

# Key Rotation

Custom encryption keys can be rotated through AWS. However, this method does not re-encrypt the existing data as described in the [CMK key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) documentation. In order to do this, the key must be manually rotated by updating the CMK in Aptible.

# Updating CMKs

CMKs can be added or rotated by creating a backup and restoring from the backup via the Aptible CLI command [`aptible backup:restore`](/reference/aptible-cli/cli-commands/cli-backup-restore)

```shell  theme={null}
aptible backup:restore $BACKUP_ID --key-arn arn:aws:kms:us-east-1:111111111111:key/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
```

Rotating keys this way will inevitably cause downtime while the backup is restored. Therefore, if you need to conform to a strict key rotation schedule that requires all data to be re-encrypted, you may want to consider implementing [Application-Level Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/application-level-encryption) to reduce or possibly even mitigate downtime when rotating.

# Invalid CMKs

There are a number of reasons that a CMK might be invalid, including being created in the wrong region and failure to share the CMK with Aptible's AWS account.

When the CMK is unavailable, you will hit one of the following errors:

```
ERROR -- : SUMMARY: Execution failed because of:
ERROR -- : - FAILED: Create 10 GB database volume
WARN -- :
ERROR -- : There was an error creating the volume. If you are using a custom encryption key, this may be because you have not shared the key with Aptible.
```

```
ERROR -- : SUMMARY: Execution failed because of:
ERROR -- : - FAILED: Attach volume
```

To resolve this, you will need to ensure that the key has been correctly created and shared with Aptible.

# Source: https://docs.aws.amazon.com/secretsmanager/latest/apireference/llms.txt

# AWS Secrets Manager API Reference

> AWS Secrets Manager provides a service to enable you to store, manage, and retrieve, secrets.

- [Welcome](https://docs.aws.amazon.com/secretsmanager/latest/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/secretsmanager/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/secretsmanager/latest/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Operations.html)

- [BatchGetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html): Retrieves the contents of the encrypted fields SecretString or SecretBinary for up to 20 secrets.
- [CancelRotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CancelRotateSecret.html): Turns off automatic rotation, and if a rotation is currently in progress, cancels the rotation.
- [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html): Creates a new secret.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteResourcePolicy.html): Deletes the resource-based permission policy attached to the secret.
- [DeleteSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html): Deletes a secret and all of its versions.
- [DescribeSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html): Retrieves the details of a secret.
- [GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html): Generates a random password.
- [GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html): Retrieves the JSON text of the resource-based policy document attached to the secret.
- [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html): Retrieves the contents of the encrypted fields SecretString or SecretBinary from the specified version of a secret, whichever contains content.
- [ListSecrets](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html): Lists the secrets that are stored by Secrets Manager in the AWS account, not including secrets that are marked for deletion.
- [ListSecretVersionIds](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html): Lists the versions of a secret.
- [PutResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutResourcePolicy.html): Attaches a resource-based permission policy to a secret.
- [PutSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html): Creates a new version of your secret by creating a new encrypted value and attaching it to the secret. version can contain a new SecretString value or a new SecretBinary value.
- [RemoveRegionsFromReplication](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RemoveRegionsFromReplication.html): For a secret that is replicated to other Regions, deletes the secret replicas from the Regions you specify.
- [ReplicateSecretToRegions](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicateSecretToRegions.html): Replicates the secret to a new Regions.
- [RestoreSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RestoreSecret.html): Cancels the scheduled deletion of a secret by removing the DeletedDate time stamp.
- [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html): Configures and starts the asynchronous process of rotating the secret.
- [StopReplicationToReplica](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html): Removes the link between the replica secret and the primary secret and promotes the replica to a primary secret in the replica Region.
- [TagResource](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html): Attaches tags to a secret.
- [UntagResource](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html): Removes specific tags from a secret.
- [UpdateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html): Modifies the details of a secret, including metadata and the secret value.
- [UpdateSecretVersionStage](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecretVersionStage.html): Modifies the staging labels attached to a version of a secret.
- [ValidateResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ValidateResourcePolicy.html): Validates that a resource policy does not grant a wide range of principals access to your secret.


## [Data Types](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Types.html)

- [APIErrorType](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_APIErrorType.html): The error Secrets Manager encountered while retrieving an individual secret as part of .
- [ExternalSecretRotationMetadataItem](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ExternalSecretRotationMetadataItem.html): The metadata needed to successfully rotate a managed external secret.
- [Filter](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Filter.html): Allows you to add filters when you use the search function in Secrets Manager.
- [ReplicaRegionType](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicaRegionType.html): A custom type that specifies a Region and the KmsKeyId for a replica secret.
- [ReplicationStatusType](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicationStatusType.html): A replication object consisting of a RegionReplicationStatus object and includes a Region, KMSKeyId, status, and status message.
- [RotationRulesType](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotationRulesType.html): A structure that defines the rotation configuration for the secret.
- [SecretListEntry](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_SecretListEntry.html): A structure that contains the details about a secret.
- [SecretValueEntry](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_SecretValueEntry.html): A structure that contains the secret value and other details for a secret.
- [SecretVersionsListEntry](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_SecretVersionsListEntry.html): A structure that contains information about one version of a secret.
- [Tag](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Tag.html): A structure that contains information about a tag.
- [ValidationErrorsEntry](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ValidationErrorsEntry.html): Displays errors that occurred during validation of the resource policy.

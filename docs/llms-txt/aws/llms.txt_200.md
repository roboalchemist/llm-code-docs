# Source: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/llms.txt

# AWS CloudHSM API Reference

> Welcome to the AWS CloudHSM API Reference.

- [Welcome](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Operations.html)

- [CopyBackupToRegion](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CopyBackupToRegion.html): Copy an AWS CloudHSM cluster backup to a different region.
- [CreateCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateCluster.html): Creates a new AWS CloudHSM cluster.
- [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html): Creates a new hardware security module (HSM) in the specified AWS CloudHSM cluster.
- [DeleteBackup](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteBackup.html): Deletes a specified AWS CloudHSM backup.
- [DeleteCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteCluster.html): Deletes the specified AWS CloudHSM cluster.
- [DeleteHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteHsm.html): Deletes the specified HSM.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteResourcePolicy.html): Deletes an AWS CloudHSM resource policy.
- [DescribeBackups](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeBackups.html): Gets information about backups of AWS CloudHSM clusters.
- [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html): Gets information about AWS CloudHSM clusters.
- [GetResourcePolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_GetResourcePolicy.html): Retrieves the resource policy document attached to a given resource.
- [InitializeCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_InitializeCluster.html): Claims an AWS CloudHSM cluster by submitting the cluster certificate issued by your issuing certificate authority (CA) and the CA's root certificate.
- [ListTags](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ListTags.html): Gets a list of tags for the specified AWS CloudHSM cluster.
- [ModifyBackupAttributes](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ModifyBackupAttributes.html): Modifies attributes for AWS CloudHSM backup.
- [ModifyCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ModifyCluster.html): Modifies AWS CloudHSM cluster.
- [PutResourcePolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_PutResourcePolicy.html): Creates or updates an AWS CloudHSM resource policy.
- [RestoreBackup](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_RestoreBackup.html): Restores a specified AWS CloudHSM backup that is in the PENDING_DELETION state.
- [TagResource](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_TagResource.html): Adds or overwrites one or more tags for the specified AWS CloudHSM cluster.
- [UntagResource](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_UntagResource.html): Removes the specified tag or tags from the specified AWS CloudHSM cluster.


## [Data Types](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Types.html)

- [Backup](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Backup.html): Contains information about a backup of an AWS CloudHSM cluster.
- [BackupRetentionPolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_BackupRetentionPolicy.html): A policy that defines the number of days to retain backups.
- [Certificates](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Certificates.html): Contains one or more certificates or a certificate signing request (CSR).
- [Cluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Cluster.html): Contains information about an AWS CloudHSM cluster.
- [DestinationBackup](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DestinationBackup.html): Contains information about the backup that will be copied and created by the operation.
- [Hsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Hsm.html): Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.
- [Tag](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Tag.html): Contains a tag.

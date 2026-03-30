# Source: https://docs.aws.amazon.com/signer/latest/api/llms.txt

# AWS Signer API Reference

> AWS Signer is a fully managed code-signing service to help you ensure the trust and integrity of your code.

- [Welcome](https://docs.aws.amazon.com/signer/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/signer/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/signer/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/signer/latest/api/API_Operations.html)

- [AddProfilePermission](https://docs.aws.amazon.com/signer/latest/api/API_AddProfilePermission.html): Adds cross-account permissions to a signing profile.
- [CancelSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html): Changes the state of an ACTIVE signing profile to CANCELED.
- [DescribeSigningJob](https://docs.aws.amazon.com/signer/latest/api/API_DescribeSigningJob.html): Returns information about a specific code signing job.
- [GetRevocationStatus](https://docs.aws.amazon.com/signer/latest/api/API_GetRevocationStatus.html): Retrieves the revocation status of one or more of the signing profile, signing job, and signing certificate.
- [GetSigningPlatform](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningPlatform.html): Returns information on a specific signing platform.
- [GetSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html): Returns information on a specific signing profile.
- [ListProfilePermissions](https://docs.aws.amazon.com/signer/latest/api/API_ListProfilePermissions.html): Lists the cross-account permissions associated with a signing profile.
- [ListSigningJobs](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningJobs.html): Lists all your signing jobs.
- [ListSigningPlatforms](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningPlatforms.html): Lists all signing platforms available in AWS Signer that match the request parameters.
- [ListSigningProfiles](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningProfiles.html): Lists all available signing profiles in your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/signer/latest/api/API_ListTagsForResource.html): Returns a list of the tags associated with a signing profile resource.
- [PutSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_PutSigningProfile.html): Creates a signing profile.
- [RemoveProfilePermission](https://docs.aws.amazon.com/signer/latest/api/API_RemoveProfilePermission.html): Removes cross-account permissions from a signing profile.
- [RevokeSignature](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSignature.html): Changes the state of a signing job to REVOKED.
- [RevokeSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html): Changes the state of a signing profile to REVOKED.
- [SignPayload](https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html): Signs a binary payload and returns a signature envelope.
- [StartSigningJob](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html): Initiates a signing job to be performed on the code provided.
- [TagResource](https://docs.aws.amazon.com/signer/latest/api/API_TagResource.html): Adds one or more tags to a signing profile.
- [UntagResource](https://docs.aws.amazon.com/signer/latest/api/API_UntagResource.html): Removes one or more tags from a signing profile.


## [Data Types](https://docs.aws.amazon.com/signer/latest/api/API_Types.html)

- [Destination](https://docs.aws.amazon.com/signer/latest/api/API_Destination.html): Points to an S3Destination object that contains information about your S3 bucket.
- [EncryptionAlgorithmOptions](https://docs.aws.amazon.com/signer/latest/api/API_EncryptionAlgorithmOptions.html): The encryption algorithm options that are available to a code-signing job.
- [HashAlgorithmOptions](https://docs.aws.amazon.com/signer/latest/api/API_HashAlgorithmOptions.html): The hash algorithms that are available to a code-signing job.
- [Permission](https://docs.aws.amazon.com/signer/latest/api/API_Permission.html): A cross-account permission for a signing profile.
- [S3Destination](https://docs.aws.amazon.com/signer/latest/api/API_S3Destination.html): The name and prefix of the Amazon S3 bucket where AWS Signer saves your signed objects.
- [S3SignedObject](https://docs.aws.amazon.com/signer/latest/api/API_S3SignedObject.html): The Amazon S3 bucket name and key where Signer saved your signed code image.
- [S3Source](https://docs.aws.amazon.com/signer/latest/api/API_S3Source.html): Information about the Amazon S3 bucket where you saved your unsigned code.
- [SignatureValidityPeriod](https://docs.aws.amazon.com/signer/latest/api/API_SignatureValidityPeriod.html): The validity period for a signing job.
- [SignedObject](https://docs.aws.amazon.com/signer/latest/api/API_SignedObject.html): Points to an S3SignedObject object that contains information about your signed code image.
- [SigningConfiguration](https://docs.aws.amazon.com/signer/latest/api/API_SigningConfiguration.html): The configuration of a signing operation.
- [SigningConfigurationOverrides](https://docs.aws.amazon.com/signer/latest/api/API_SigningConfigurationOverrides.html): A signing configuration that overrides the default encryption or hash algorithm of a signing job.
- [SigningImageFormat](https://docs.aws.amazon.com/signer/latest/api/API_SigningImageFormat.html): The image format of a AWS Signer platform or profile.
- [SigningJob](https://docs.aws.amazon.com/signer/latest/api/API_SigningJob.html): Contains information about a signing job.
- [SigningJobRevocationRecord](https://docs.aws.amazon.com/signer/latest/api/API_SigningJobRevocationRecord.html): Revocation information for a signing job.
- [SigningMaterial](https://docs.aws.amazon.com/signer/latest/api/API_SigningMaterial.html): The ACM certificate that is used to sign your code.
- [SigningPlatform](https://docs.aws.amazon.com/signer/latest/api/API_SigningPlatform.html): Contains information about the signing configurations and parameters that are used to perform a code-signing job.
- [SigningPlatformOverrides](https://docs.aws.amazon.com/signer/latest/api/API_SigningPlatformOverrides.html): Any overrides that are applied to the signing configuration of a signing platform.
- [SigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_SigningProfile.html): Contains information about the ACM certificates and signing configuration parameters that can be used by a given code signing user.
- [SigningProfileRevocationRecord](https://docs.aws.amazon.com/signer/latest/api/API_SigningProfileRevocationRecord.html): Revocation information for a signing profile.
- [Source](https://docs.aws.amazon.com/signer/latest/api/API_Source.html): An S3Source object that contains information about the S3 bucket where you saved your unsigned code.

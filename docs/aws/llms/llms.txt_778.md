# Source: https://docs.aws.amazon.com/signer/latest/developerguide/llms.txt

# AWS Signer Developer Guide

> Learn how to use AWS Signer to sign code and authenticate integrity.

- [What is AWS Signer?](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html)
- [Revoke signatures](https://docs.aws.amazon.com/signer/latest/developerguide/revocation.html)
- [Monitor](https://docs.aws.amazon.com/signer/latest/developerguide/monitoring-overview.html)
- [Document History](https://docs.aws.amazon.com/signer/latest/developerguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/signer/latest/developerguide/glossary.html)

## [Get started](https://docs.aws.amazon.com/signer/latest/developerguide/getting-started.html)

- [Set up](https://docs.aws.amazon.com/signer/latest/developerguide/iam-setup.html): Learn how to configure users and security policies for AWS Signer.
- [Create a signing profile](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profiles.html): Learn how to create a AWS Signer signing profile.
- [Set up cross-account signing](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profile-cross-account.html): Learn about how to use cross-account signing with signer profiles.


## [Code signing workflows](https://docs.aws.amazon.com/signer/latest/developerguide/workflows.html)

### [Internet of Things (IoT)](https://docs.aws.amazon.com/signer/latest/developerguide/iot-workflow.html)

Learn how to sign binary files that will be deployed in IoT devices.

- [Obtain certificate](https://docs.aws.amazon.com/signer/latest/developerguide/obtain-cert.html): Learn how to import a code signing certificate for IoT applications.
- [Create source S3 bucket](https://docs.aws.amazon.com/signer/latest/developerguide/s3-source-iot.html): Learn how to add your unsigned package files to an Amazon S3 bucket.
- [Create destination S3 bucket](https://docs.aws.amazon.com/signer/latest/developerguide/s3-destination-iot.html): Learn how to create an Amazon S3 bucket where AWS Signer can write your signed object files.
- [Create a signing job](https://docs.aws.amazon.com/signer/latest/developerguide/signing-jobs-iot.html): Perform a signing job for IoT using the CLI or API.

### [AWS Lambda](https://docs.aws.amazon.com/signer/latest/developerguide/lambda-workflow.html)

Learn how to sign zipped files containing code that will be deployed in AWS Lambda.

- [Creating source S3 bucket](https://docs.aws.amazon.com/signer/latest/developerguide/s3-source-lambda.html): Learn how to add your unsigned package files to an Amazon S3 bucket.
- [Create destination S3 bucket](https://docs.aws.amazon.com/signer/latest/developerguide/s3-destination-lambda.html): Learn how to create an Amazon S3 bucket where AWS Signer can write your signed object files.
- [Create a signing job](https://docs.aws.amazon.com/signer/latest/developerguide/signing-jobs-lambda.html): Perform signing jobs using the console, CLI, or API.

### [Container images](https://docs.aws.amazon.com/signer/latest/developerguide/container-workflow.html)

Follow this workflow to use AWS Signer to sign container images for storage in Amazon ECR.

- [Prerequisites](https://docs.aws.amazon.com/signer/latest/developerguide/image-signing-prerequisites.html): Learn how to install and configure the software dependencies needed for container image signing.
- [Sign an image](https://docs.aws.amazon.com/signer/latest/developerguide/image-signing-steps.html): Procedure for using Notation to sign a container image.
- [Locally verify an image](https://docs.aws.amazon.com/signer/latest/developerguide/image-verification.html): Learn how to verify the integrity and ownership of your signed image using Notation.
- [Verify an image on Amazon EKS](https://docs.aws.amazon.com/signer/latest/developerguide/kubernetes-verification.html): Learn how to verify image signatures at the time of deployment.


## [Security](https://docs.aws.amazon.com/signer/latest/developerguide/security.html)

### [Identity and Access Management for Signer](https://docs.aws.amazon.com/signer/latest/developerguide/authen-overview.html)

Control access to your code-signing resources.

- [Customer managed policies for Signer](https://docs.aws.amazon.com/signer/latest/developerguide/authen-custmanagedpolicies.html): Control access to AWS Signer resources in your AWS account by attaching customer managed policies to users, groups, or roles.
- [Inline policies for Signer](https://docs.aws.amazon.com/signer/latest/developerguide/authen-inlinepolicies.html): Control access to AWS Signer actions in your AWS account by attaching inline policies to users, groups, or roles.
- [Signer actions in IAM](https://docs.aws.amazon.com/signer/latest/developerguide/authen-apipermissions.html): Describes the AWS Identity and Access Management actions that you can use with Signer.


## [Code examples](https://docs.aws.amazon.com/signer/latest/developerguide/api-toplevel.html)

### [Actions](https://docs.aws.amazon.com/signer/latest/developerguide/code-examples-actions.html)

The following code examples demonstrate how to perform individual Signer actions with the AWS Java SDK.

- [AddProfilePermission](https://docs.aws.amazon.com/signer/latest/developerguide/api-addprofilepermission.html): Learn how to program the AddProfilePermission operation in AWS Signer using Java.
- [CancelSigningProfile](https://docs.aws.amazon.com/signer/latest/developerguide/api-cancelsigningprofile.html): Learn how to program the CancelSigningProfile operation in AWS Signer using Java.
- [DescribeSigningJob](https://docs.aws.amazon.com/signer/latest/developerguide/api-describesigningjob.html): Learn how to program the DescribeSigningJob operation in AWS Signer using Java.
- [GetRevocationStatus](https://docs.aws.amazon.com/signer/latest/developerguide/api-getrevocationstatus.html): Learn how to program the GetRevocationStatus operation in AWS Signer using Java.
- [GetSigningPlatform](https://docs.aws.amazon.com/signer/latest/developerguide/api-getsigningplatform.html): Learn how to program the GetSigningPlatform operation in AWS Signer using Java.
- [GetSigningProfile](https://docs.aws.amazon.com/signer/latest/developerguide/api-getsigningprofile.html): Learn how to program the GetSigningProfile operation in AWS Signer using Java.
- [ListProfilePermissions](https://docs.aws.amazon.com/signer/latest/developerguide/api-listprofilepermissions.html): Learn how to program the ListProfilePermissions operation in AWS Signer using Java.
- [ListSigningJobs](https://docs.aws.amazon.com/signer/latest/developerguide/api-listsigningjobs.html): Learn how to program the ListSigningJobs operation in AWS Signer using Java.
- [ListSigningPlatforms](https://docs.aws.amazon.com/signer/latest/developerguide/api-listsigningplatforms.html): Learn how to program the ListSigningPlatforms operation in AWS Signer using Java.
- [ListSigningProfiles](https://docs.aws.amazon.com/signer/latest/developerguide/api-listsigningprofiles.html): Learn how to program the ListSigningProfiles operation in AWS Signer using Java.
- [ListTagsForResource](https://docs.aws.amazon.com/signer/latest/developerguide/api-listtagsforresource.html): Learn how to program the ListTagsForResource operation in AWS Signer using Java.
- [PutSigningProfile](https://docs.aws.amazon.com/signer/latest/developerguide/api-putsigningprofile.html): Learn how to program the PutSigningProfile operation in AWS Signer using Java.
- [RemoveProfilePermission](https://docs.aws.amazon.com/signer/latest/developerguide/api-removeprofilepermission.html): Learn how to program the RemoveProfilePermission operation in AWS Signer using Java.
- [RevokeSignature](https://docs.aws.amazon.com/signer/latest/developerguide/api-revokesignature.html): Learn how to program the RevokeSignature operation in AWS Signer using Java.
- [RevokeSigningProfile](https://docs.aws.amazon.com/signer/latest/developerguide/api-revokesigningprofile.html): Learn how to program the RevokeSigningProfile operation in AWS Signer using Java.
- [SignPayload](https://docs.aws.amazon.com/signer/latest/developerguide/api-signpayload.html): Learn how to program the SignPayload operation in AWS Signer using Java.
- [StartSigningJob](https://docs.aws.amazon.com/signer/latest/developerguide/api-startsigningjob.html): Learn how to program the StartSigningJob operation in AWS Signer using Java.
- [TagResource](https://docs.aws.amazon.com/signer/latest/developerguide/api-tagresource.html): Learn how to program the TagResource operation in AWS Signer using Java.
- [UntagResource](https://docs.aws.amazon.com/signer/latest/developerguide/api-untagresource.html): Learn how to program the UntagResource operation in AWS Signer using Java.

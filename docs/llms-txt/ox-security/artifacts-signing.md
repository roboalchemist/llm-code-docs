# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/artifacts-signing.md

# Securing Docker Images

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

You can securely sign your Docker images stored in AWS Elastic Container Registry (ECR) using AWS Signer. This process ensures the integrity and authenticity of Docker images by centralizing signing requests within OX app, providing you clear visibility into the signing activities.

By incorporating artifact signing into your CI/CD pipelines, you can streamline operations and enhance software supply chain security.

The following guidelines present the necessary steps to configure and execute securing Docker images, including granting OX the required permissions and integrating the signing process into your workflow.

### Granting AWS Signer Permissions

You can grant AWS Signer permissions only for a signing profile that you already have in AWS Signer.

#### To grant AWS Signer Permissions

1. Navigate to the **AWS Signer** service in your AWS Management Console.
2. Create a new signing profile that aligns with your specific requirements. For container image signing, we recommend selecting the appropriate platform, such as `Notation-OCI-SHA384-ECDSA`.
3. Save the signing profile name for the granting access process.
4. To grant access to your signing profile, use the AWS Command Line Interface (CLI) and execute the following command:

   ```bash
   aws signer add-profile-permission \
       --profile-name "<SigningProfileName>" \
       --principal "<OX_AWS_Account_ID>" \
       --action signer:SignPayload \
       --statement-id "<UniqueStatementID>" \
       --region <AWS_REGION>
   ```

| Parameter              | Description                                                                         |
| ---------------------- | ----------------------------------------------------------------------------------- |
| `<SigningProfileName>` | The name of the signing profile in AWS Signer.                                      |
| `<OX_AWS_Account_ID>`  | The AWS Account ID of OX that is granted the permission.                            |
| `signer:SignPayload`   | The action to be allowed, which in this case is the ability to sign payloads.       |
| `<UniqueStatementID>`  | A unique identifier for the permission statement, e.g., "OxSecurityAccountSigning". |
| `<AWS_REGION>`         | The AWS region where the signing profile and related resources are located.         |

1. Ensure that the JSON policy remains valid after adding this statement.
2. Save the updated repository policy.
3. To verify the AWS Signer permissions, use the following AWS CLI command or review the repository policy directly within the ECR console:

   ```bash
   aws signer list-profile-permissions --profile-name "<YourSigningProfileName>"
   ```

### Granting ECR Repository Permissions

1. In the **Amazon ECR** console, select the repository that contains the Docker images you intend to have signed.
2. Navigate to the **Permissions** tab and click **Edit repository policy**.
3. To allow OXSecurity AWS account to push images, add the following policy statement to your existing repository policy:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AllowCrossAccountAccess",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::<OX_AWS_Account_ID>:root"
               },
               "Action": [
                   "ecr:BatchCheckLayerAvailability",
                   "ecr:BatchGetImage",
                   "ecr:CompleteLayerUpload",
                   "ecr:GetDownloadUrlForLayer",
                   "ecr:InitiateLayerUpload",
                   "ecr:PutImage",
                   "ecr:UploadLayerPart"
               ]
           }
       ]
   }
   ```

4. Save the updated repository policy.

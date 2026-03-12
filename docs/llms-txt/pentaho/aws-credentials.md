# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/aws-credentials.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/s3-csv-input-cp/aws-credentials.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/aws-credentials.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/s3-csv-input-cp/aws-credentials.md

# AWS credentials

The S3 CSV Input step provides credentials to the Amazon Web Services SDK for Java using a credential provider chain. The default credential provider chain looks for AWS credentials in the following locations and in the following order:

* **Environment variables**

  The variables *AWS\_ACCESS\_KEY\_ID*, *AWS\_SECRET\_ACCESS\_KEY*, and *AWS\_SESSION\_TOKEN*. See [AWS Environment Variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-environment.html).
* **AWS credentials file**

  The credentials file, located in the `/.aws` directory on Linux, macOS, and Unix operating systems, and in the "`%UserProfile%\.aws` directory on Windows operating systems. See[AWS Configuration and Credential Files](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html)
* **CLI configuration file**

  The `config` file is located in the same directory as the `credentials` file. The `config` file can contain a default profile, named profiles, and CLI-specific configuration parameters for each profile.
* **ECS container credentials**

  These credentials are provided by the Amazon Elastic Container Service on container instances set up by the ECS administrator. See [AWS Using an IAM Role to Grant Permissions to Applications](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).
* **Instance profile credentials**

  These credentials are delivered through the Amazon EC2 metadata service, and can be used on EC2 instances with an assigned instance role.

The S3 CSV Input step can use any of these methods to authenticate AWS credentials. For more information on setting up AWS credentials, see [Working with AWS Credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html).

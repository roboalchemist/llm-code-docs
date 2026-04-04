# Source: https://docs.aws.amazon.com/AmazonECR/latest/public/llms.txt

# Amazon ECR Public User Guide

> Store Docker and Open Container Initiative (OCI) images in public repositories in the AWS cloud with Amazon Elastic Container Registry Public.

- [What is Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html)
- [Amazon ECR Public Gallery](https://docs.aws.amazon.com/AmazonECR/latest/public/public-gallery.html)
- [Making requests](https://docs.aws.amazon.com/AmazonECR/latest/public/public-ecr-requests.html)
- [Moving an image through its lifecycle in Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/getting-started-cli.html)
- [Logging actions with AWS CloudTrail](https://docs.aws.amazon.com/AmazonECR/latest/public/logging-using-cloudtrail.html)
- [Service quotas](https://docs.aws.amazon.com/AmazonECR/latest/public/public-service-quotas.html)
- [Troubleshooting](https://docs.aws.amazon.com/AmazonECR/latest/public/public-troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/AmazonECR/latest/public/public-doc-history.html)

## [Public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html)

- [Registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registry-auth.html): Authenticate and authorize access to Amazon ECR public registries for pulling public container images using the AWS CLI credential helper, AWS Identity and IAM roles, or Kubernetes tools.
- [Required IAM permissions](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registry-settings-iam.html): How to use IAM to control access permissions for configuring settings on Amazon ECR public registries, such as enabling or disabling Docker content trust scanning.
- [Updating registry settings](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registry-settings.html): How to manage settings for your Amazon ECR public registry such as enabling Docker content trust scanning to verify image publisher signatures and ensure downloaded images haven't been tampered with.


## [Public repositories](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repositories.html)

- [Creating a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-create.html): The process of creating a new public repository in Amazon ECR Public to store and manage your own Docker or OCI container images that can be publicly accessed.
- [Editing a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-edit.html): Explains how to edit the metadata of an Amazon ECR public repository, including updating repository details and adding or removing repository policies.
- [Repository catalog data](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html): Describes how to view and manage catalog data for Amazon ECR public repositories, including image details, vulnerability data, and Amazon Inspector scanning reports.
- [Viewing public repository information](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-info.html): Overview of Amazon ECR public repositories, which allow users to store, manage, share, and deploy Docker container images publicly.
- [Deleting a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-delete.html): Outlines the process for permanently deleting an Amazon ECR public repository, including details on prerequisites, considerations, and the required steps to complete the deletion.

### [Public repository policies in Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policies.html)

Explains how to manage repository policies for Amazon ECR public repositories, which control access permissions and settings for the repositories.

- [Setting a repository policy statement in Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/set-public-repository-policy.html): Provides instructions on how to set a repository policy for an Amazon ECR public repository to control access and permissions.
- [Deleting a public repository policy statement in Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/delete-public-repository-policy.html): The process for deleting a repository policy from an Amazon ECR public repository, which removes any access control or settings defined by the policy.
- [Public repository policy examples in Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policy-examples.html): Provides example repository policy statements for Amazon ECR public repositories to help users understand and define access controls and permissions.

### [Tag a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/ecr-public-using-tags.html)

Assign your own metadata tags to Amazon ECR Public repositories.

- [Adding tags](https://docs.aws.amazon.com/AmazonECR/latest/public/tag-resources-console.html): Explains how to add tags to an Amazon ECR public repository.
- [Deleting tags](https://docs.aws.amazon.com/AmazonECR/latest/public/ecr-public-deleting-tags-repositories-console.html): Explains how to delete tags to an Amazon ECR public repository.


## [Public images](https://docs.aws.amazon.com/AmazonECR/latest/public/public-images.html)

- [Pushing an image](https://docs.aws.amazon.com/AmazonECR/latest/public/docker-push-ecr-image.html): Provides instructions on how to push a Docker image to an Amazon ECR public repository, allowing users to store and share their container images publicly.
- [Pushing a multi-architecture image](https://docs.aws.amazon.com/AmazonECR/latest/public/docker-push-multi-architecture-image.html): Page outlines the steps for pushing multi-architecture Docker container images to an Amazon ECR public repository, enabling users to distribute and deploy their applications across different architectures.
- [Pushing a Helm chart](https://docs.aws.amazon.com/AmazonECR/latest/public/push-oci-artifact.html): Page describes how to push an Open Container Initiative (OCI) artifact to an Amazon ECR public repository, allowing users to store and share OCI-compliant container images and other artifacts publicly.
- [Pulling an image](https://docs.aws.amazon.com/AmazonECR/latest/public/docker-pull-ecr-image.html): Page provides instructions on how to pull a Docker container image from an Amazon ECR public repository, enabling users to deploy and run publicly available container images.
- [Deleting an image](https://docs.aws.amazon.com/AmazonECR/latest/public/public-image-delete.html): Page explains the process of deleting a Docker image from an Amazon ECR public repository, including prerequisites, considerations, and steps to permanently remove the image.
- [Container image manifest formats](https://docs.aws.amazon.com/AmazonECR/latest/public/image-manifest-formats.html): Page describes the different image manifest formats supported by Amazon ECR for public repositories, including Docker Image Manifest V2 Schema 2 and Open Container Initiative (OCI) Image Layout.


## [Security](https://docs.aws.amazon.com/AmazonECR/latest/public/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/AmazonECR/latest/public/security-iam.html)

How to authenticate requests and manage access your Amazon ECR Public resources.

- [How Amazon ECR Public works with IAM](https://docs.aws.amazon.com/AmazonECR/latest/public/security_iam_service-with-iam.html): Page covers security best practices for Amazon ECR public repositories, including repository policies, encryption, access management, and compliance considerations to help users secure their public container images.
- [AWS managed policies for Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/public-security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon ECR Public and recent changes to those policies.
- [Identity-based policy examples](https://docs.aws.amazon.com/AmazonECR/latest/public/security_iam_id-based-policy-examples.html): Page provides example identity-based policy statements for Amazon ECR that demonstrate how to control access to public repositories using IAM policies.
- [Using tag-based access control in Amazon ECR public](https://docs.aws.amazon.com/AmazonECR/latest/public/ecr-supported-iam-actions-tagging.html): Page lists the IAM actions and resource-level permissions that can be used to control access to Amazon ECR public repositories, including tagging support.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonECR/latest/public/security_iam_troubleshoot.html): Page provides guidance on troubleshooting and resolving issues related to IAM permissions and policies for Amazon ECR public repositories.

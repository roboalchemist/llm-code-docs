# Source: https://docs.aws.amazon.com/cloud9/latest/APIReference/llms.txt

# AWS Cloud9 API Reference

> AWS Cloud9 is a collection of tools that you can use to code, build, run, test, debug, and release software in the cloud.

- [Welcome](https://docs.aws.amazon.com/cloud9/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloud9/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloud9/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_Operations.html)

- [CreateEnvironmentEC2](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentEC2.html): Creates an AWS Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.
- [CreateEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentMembership.html): Adds an environment member to an AWS Cloud9 development environment.
- [DeleteEnvironment](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DeleteEnvironment.html): Deletes an AWS Cloud9 development environment.
- [DeleteEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DeleteEnvironmentMembership.html): Deletes an environment member from a development environment.
- [DescribeEnvironmentMemberships](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironmentMemberships.html): Gets information about environment members for an AWS Cloud9 development environment.
- [DescribeEnvironments](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironments.html): Gets information about AWS Cloud9 development environments.
- [DescribeEnvironmentStatus](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironmentStatus.html): Gets status information for an AWS Cloud9 development environment.
- [ListEnvironments](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_ListEnvironments.html): Gets a list of AWS Cloud9 development environment identifiers.
- [ListTagsForResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_ListTagsForResource.html): Gets a list of the tags associated with an AWS Cloud9 development environment.
- [TagResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_TagResource.html): Adds tags to an AWS Cloud9 development environment.
- [UntagResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UntagResource.html): Removes tags from an AWS Cloud9 development environment.
- [UpdateEnvironment](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UpdateEnvironment.html): Changes the settings of an existing AWS Cloud9 development environment.
- [UpdateEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UpdateEnvironmentMembership.html): Changes the settings of an existing environment member for an AWS Cloud9 development environment.


## [Data Types](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_Types.html)

- [Environment](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_Environment.html): Information about an AWS Cloud9 development environment.
- [EnvironmentLifecycle](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_EnvironmentLifecycle.html): Information about the current creation or deletion lifecycle state of an AWS Cloud9 development environment.
- [EnvironmentMember](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_EnvironmentMember.html): Information about an environment member for an AWS Cloud9 development environment.
- [Tag](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_Tag.html): Metadata that is associated with AWS resources.

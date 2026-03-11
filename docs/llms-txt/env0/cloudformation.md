# Source: https://docs.envzero.com/guides/admin-guide/templates/cloudformation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS Cloudformation Integration

> Manage AWS CloudFormation stacks with env zero for automated cloud resource provisioning and drift detection

AWS CloudFormation lets you model, provision, and manage AWS and third-party resources by treating Infrastructure as Code. With CloudFormation, you declare all your resources and dependencies in a template file, which defines a collection of resources as a single unit called a stack. CloudFormation creates and deletes all member resources of the stack together and manages all dependencies between the resources.

Manage your CloudFormation stack within env zero to enjoy features such as [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment), [Policies](/guides/policies-governance/policies) and [RBAC](/guides/admin-guide/user-role-and-team-management/rbac). You can also use [Custom Flows](/guides/admin-guide/custom-flows) to alter the deployment by running commands, or [Workflows](/guides/admin-guide/workflows) to orchestrate multiple IaC stacks and dependencies between them.

## Environment Deployment

1. Create a CloudFormation [template](/guides/admin-guide/templates).
2. Create an [Environment](/guides/admin-guide/environments). You can set the stack name or env zero can generate a random name for you.

## CloudFormation Stack Parameters

To provide parameters to a CloudFormation stack, use [env zero Variables](/guides/admin-guide/variables). Any environment variable prefixed with `ENV0_CF_PARAM_` will be passed as a parameter to the CloudFormation stack. For example, if you set the environment variable `ENV0_CF_PARAM_STAGE=dev`, the CloudFormation stack will receive the parameter `STAGE=dev`.

env zero creates a file containing all the parameters and their values, and passes it to the deploy command (`--parameter-overrides file://<parameters_file>`.

You can control the name of the parameters file by setting the `ENV0_CF_PARAMETERS_FILE` environment variable. This can be helpful if you already have a parameters file (from VCS or generated using [Custom Flows](/guides/admin-guide/custom-flows)). env zero will merge it with parameters from any `ENV0_CF_PARAM_XXX` environment variables.  See the section below for an example of a parameters file.

## Execution Steps

Other than common steps such as Clone, Loading Variables, etc., env zero executes the following steps for CloudFormation environments:

* On Deploy:
  1. CloudFormation Describe Change Set\
     `awsv2 cloudformation deploy --stack-name <stack_name> --template-file <template_file> --no-execute-changeset --parameter-overrides file://<parameters_file>`\
     `awsv2 cloudformation describe-change-set --change-set-name <change_set_name>`
  2. CloudFormation deploy\
     `awsv2 cloudformation deploy --stack-name <stack_name> --template-file <template_file> --parameter-overrides file://<parameters_file>`
  3. CloudFormation Stack Outputs\
     `awsv2 cloudformation describe-stacks --stack-name <stack_name>`

* On Destroy:
  1. CloudFormation List Stack Resources (to list resources that will be destroyed)\
     `awsv2 cloudformation list-stack-resources --stack-name <stack_name>`
  2. CloudFormation Delete Stack\
     `awsv2 cloudformation delete-stack --stack-name <stack_name>`\
     `awsv2 cloudformation wait stack-delete-complete --stack-name <stack_name>`

* Drift Detection:
  1. Cloudformation - Detect stack drift (To trigger Drift detection)\
     `awsv2 cloudformation detect-stack-drift --stack-name <stack_name>`
  2. Cloudformation - Describe stack drift detection status\
     `awsv2 cloudformation describe-stack-drift-detection-status --stack-drift-detection-id <drift_detection_id>`
  3. Cloudformation - Describe stack resources drift\
     `awsv2 cloudformation describe-stack-resources-drift --stack-name <stack_name> --stack-resource-drift-status-filters MODIFIED CREATED NOT_CHECKED`

<Info>
  **Drift Detection**

  Not all Cloudformation resources support Drift Detection.

  <Info>
    You can find a complete list of supported [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html).

    For Drift Detection to function properly you might need to have certain permissions in place. You can find further information [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html#drift-considerations)
  </Info>
</Info>

## Providing custom CloudFormation CLI Arguments

Occasionally, you may need to pass CLI arguments as CloudFormation commands.

These can be passed to CloudFormation by setting Environment Variables on env zero, prefixed by `ENV0_CF_CLI_ARGS_`.  An example of a CloudFormation command (with an underscore for dashes)  would look like this: `ENV0_CF_CLI_ARGS_deploy`, `ENV0_CF_CLI_ARGS_delete_stack` etc.

A common use case is when trying to create IAM resources.  CloudFormation [may require you](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html) to explicitly acknowledge that your stack template contains certain capabilities in order for AWS CloudFormation to create the stack.

In that case, you could set `ENV0_CF_CLI_ARGS_deploy` to `--capabilities CAPABILITY_NAMED_IAM`.\
Multiple arguments may be set, separated by a blank space (` `).

### Templates exceeding 51,200 bytes must be deployed via an S3 Bucket

If your templates exceed the size limit, you must specify a bucket to store the template. In env zero set `ENV0_CF_CLI_ARGS_deploy=--s3-bucket=<bucket>`  where `bucket` is an s3 bucket to store the template.

## Import existing CloudFormation Stacks

env zero can manage existing CloudFormation stacks. To import an existing stack into env zero, please follow the instructions below:

1. Commit the template used to create the stack into a Git repository
2. Prepare any parameters you've used to configure the stack
3. Create an Environment from VCS or template. If using a template, please refer to our [Template Docs](docs:template) for creating a CloudFormation template in env zero
4. Add the parameters as described above (ENV0\_CF\_PARAM\_\*)
5. Specify the Stack Name, exactly as listed in the AWS console

## Example of a CloudFormation parameters file

Here's an example of a parameters JSON file you could either create or use with your CloudFormation stack:

```json  theme={null}
[
  {
    "ParameterKey": "BucketName",
    "ParameterValue": "hello-world"
  },
  {
    "ParameterKey": "Description",
    "ParameterValue": "This is my description."
  }
]
```

## Adding Custom Tags

Using `ENV0_CUSTOM_TAGS` you can add additional tags to your CloudFormation stack.  Read more [here](/guides/admin-guide/additional-controls/#adding-custom-resource-tagging).

Built with [Mintlify](https://mintlify.com).

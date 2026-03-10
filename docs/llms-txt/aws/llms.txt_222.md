# Source: https://docs.aws.amazon.com/codedeploy/latest/userguide/llms.txt

# AWS CodeDeploy User Guide

> Automate code deployments to any instance using CodeDeploy, including Amazon EC2 instances and instances running on-premises, with this User Guide.

- [Resources](https://docs.aws.amazon.com/codedeploy/latest/userguide/resources.html)
- [Document history](https://docs.aws.amazon.com/codedeploy/latest/userguide/document-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/codedeploy/latest/userguide/glossary.html)

## [What is CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

- [Primary components](https://docs.aws.amazon.com/codedeploy/latest/userguide/primary-components.html): Learn about the primary components used in CodeDeploy deployments.

### [Deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps.html)

Learn about the components and workflow of a CodeDeploy deployment.

- [Deployments on an AWS Lambda Compute Platform](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-lambda.html): This topic provides information about the components and workflow of CodeDeploy deployments that use the AWS Lambda compute platform.
- [Deployments on an Amazon ECS Compute Platform](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-ecs.html): This topic provides information about the components and workflow of CodeDeploy deployments that use the Amazon ECS compute platform.
- [Deployments on an EC2/On-Premises Compute Platform](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-server.html): This topic provides information about the components and workflow of CodeDeploy deployments that use the EC2/On-Premises compute platform.
- [Application specification files](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-specification-files.html): Learn about the AppSpec file, a YAML-formatted file used to automate and manage the CodeDeploy deployment process.


## [Getting started](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-codedeploy.html)

- [Step 1: Setting up](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-setting-up.html): Learn about the steps you must perform to set up your environment for CodeDeploy.
- [Step 2: Create a service role](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html): Learn how to use the IAM console or the AWS CLI to create an IAM role that gives CodeDeploy permission to access to your instances.
- [Step 3: Limit the CodeDeploy user's permissions](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-policy.html): Learn about the minimum permissions that the CodeDeploy user needs to configure and manage CodeDeploy.
- [Step 4: Create an IAM instance profile](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-iam-instance-profile.html): Learn how to use the AWS CLI and the CodeDeploy console to create an IAM instance profile.


## [Product and service integrations](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations.html)

### [Integration with other AWS services](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws.html)

Learn about CodeDeploy integrations with other AWS services.

- [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html): Learn how to integrate Amazon EC2 Auto Scaling with CodeDeploy to launch or terminate Amazon EC2 instances automatically.
- [Elastic Load Balancing](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html): Learn how to integrate CodeDeploy with Elastic Load Balancing.

### [Integration with partner products and services](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-partners.html)

Learn about CodeDeploy integrations with partner products and services.

- [GitHub](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-partners-github.html): Learn how to integrate GitHub with CodeDeploy to deploy applications from GitHub repositories to instances.
- [Integration examples from the community](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-community.html): Learn more about CodeDeploy integrations in blog posts, articles, and community-provided examples.


## [Tutorials](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials.html)

### [Tutorial: Deploy WordPress to a non-Windows instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress.html)

Learn how to use CodeDeploy to deploy a sample application to a single Amazon EC2 instance running Amazon Linux or Red Hat Enterprise Linux (RHEL).

- [Step 1: Launch an Amazon EC2 instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-launch-instance.html): Follow the steps in this topic to launch, configure, and connect to an Amazon Linux or Red Hat Enterprise Linux (RHEL) Amazon EC2 instance to deploy the WordPress application.
- [Step 2: Configure your source content](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-configure-content.html): Follow the steps in this CodeDeploy tutorial to deploy the WordPress application to an Amazon EC2 instance.
- [Step 3: Upload your application to Amazon S3](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-upload-application.html): Follow the steps in this CodeDeploy tutorial to upload a WordPress application revision.
- [Step 4: Deploy your application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-deploy-application.html): Follow the steps in this CodeDeploy tutorial to deploy a WordPress application revision.
- [Step 5: Update and redeploy your application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-update-and-redeploy-application.html): Follow the steps in this CodeDeploy tutorial to update and redeploy a revision of the WordPress application.
- [Step 6: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-clean-up.html): To avoid ongoing charges, follow these steps to clean up resources used in the CodeDeploy WordPress tutorial.

### [Tutorial: Deploy a Hello World application to a Windows Server instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows.html)

Follow the steps in this CodeDeploy tutorial to deploy a sample application to a single Amazon EC2 instance running Windows Server.

- [Step 1: Launch an Amazon EC2 instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows-launch-instance.html): Follow the steps in this CodeDeploy tutorial to launch and connect to an Amazon EC2 instance running Windows Server to deploy the Hello World! application.
- [Step 2: Configure your source content](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows-configure-content.html): Follow the steps in this CodeDeploy tutorial to deploy a "Hello, World!" application.
- [Step 3: Upload your application to Amazon S3](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows-upload-application.html): Follow the steps in this CodeDeploy tutorial to upload a "Hello, World!" application revision.
- [Step 4: Deploy your application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows-deploy-application.html): Follow the steps in this CodeDeploy tutorial to deploy a Hello World! application revision.
- [Step 5: Update and redeploy your application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows-update-and-redeploy-application.html): Follow the steps in this CodeDeploy tutorial to update and redeploy a revision of the "Hello, World!" application.
- [Step 6: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows-clean-up.html): Follow these steps to clean up the resources used in the CodeDeploy "Hello, World!" tutorial.

### [Tutorial: Deploy an application to an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance.html)

Follow the steps in this tutorial to learn how to use CodeDeploy to deploy an application revision to an on-premises instance.

- [Prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-prerequisites.html): Before you start this tutorial, you must complete the prerequisites in , which include configuring a user, installing or upgrading the AWS CLI, and creating a service role.
- [Step 1: Configure the on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-1-configure-instance.html): Before you can deploy to your on-premises instance, you must configure it.
- [Step 2: Create a sample application revision](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-2-create-sample-revision.html): In this step, you create a sample application revision to deploy to your on-premises instance.
- [Step 3: Bundle and upload your application revision to Amazon S3](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-3-bundle-sample-revision.html): Before you can deploy your application revision, you'll need to bundle the files, and then upload the file bundle to an Amazon S3 bucket.
- [Step 4: Deploy your application revision](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-4-deploy-sample-revision.html): After you've uploaded your application revision to an Amazon S3 bucket, try deploying it to your on-premises instance.
- [Step 5: Verify your deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-5-verify-deployment.html): To verify the deployment was successful, follow the instructions in , and then return to this page.
- [Step 6: Clean up resources](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-6-clean-up-resources.html): To avoid ongoing charges for resources you created for this tutorial, delete the Amazon S3 bucket if you'll no longer be using it.

### [Tutorial: Deploy to an Auto Scaling group](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group.html)

Follow this CodeDeploy tutorial to learn how to deploy an application revision to an Auto Scaling group.

- [Prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-prerequisites.html): Learn about the prerequisites that must be met before you practice deploying to an Auto Scaling group.
- [Step 1: Create and configure the Auto Scaling group](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-create-auto-scaling-group.html): Learn how to create and configure an Auto Scaling group to use in the CodeDeploy tutorial for deploying to an Auto Scaling group.
- [Step 2: Deploy the application to the Auto Scaling group](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-create-deployment.html): Learn how to deploy an application revision to an instance in the CodeDeploy Auto Scaling group tutorial.
- [Step 3: Check your results](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-verify.html): Learn how to verify the initial deployment results in the CodeDeploy Auto Scaling group tutorial.
- [Step 4: Increase the number of Amazon EC2 instances in the Auto Scaling group](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-scale-up.html): Learn how to scale out additional instances in the CodeDeploy Auto Scaling group tutorial.
- [Step 5: Check your results again](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-reverify.html): Learn how to verify the results of the second deployment in the CodeDeploy Auto Scaling group tutorial.
- [Step 6: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group-clean-up.html): Learn how to delete the Auto Scaling group created for the CodeDeploy Auto Scaling group tutorial to avoid ongoing charges.

### [Tutorial: Deploy an application from GitHub](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github.html)

Follow the steps in this CodeDeploy tutorial to deploy an application from GitHub to one or more Amazon EC2 instances.

- [Prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-prerequisites.html): Learn about the prerequisites that must be met before you practice deploying an application from GitHub.
- [Step 1: Set up a GitHub account](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-create-github-account.html): Follow the steps to create an account in GitHub before you practice deploying an application from GitHub using CodeDeploy.
- [Step 2: Create a GitHub repository](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-create-github-repository.html): Follow the steps to create a repository in GitHub before you practice deploying an application from GitHub using CodeDeploy.
- [Step 3: Upload a sample application to your GitHub repository](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-upload-sample-revision.html): Follow the steps to upload a sample application to a repository in GitHub in the CodeDeploy GitHub tutorial.
- [Step 4: Provision an instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-provision-instance.html): Follow the steps to provision an instance in an Amazon EC2 Auto Scaling group in the CodeDeploy GitHub tutorial.
- [Step 5: Create an application and deployment group](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-create-application.html): Follow the steps to create an application and deployment group in the CodeDeploy GitHub tutorial.
- [Step 6: Deploy the application to the instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-deploy-application.html): Follow the steps to deploy an application revision to an instance in the CodeDeploy GitHub tutorial.
- [Step 7: Monitor and verify the deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-verify.html): Follow the steps to verify the first deployment to an Amazon EC2 Auto Scaling group in the CodeDeploy GitHub tutorial.
- [Step 8: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-clean-up.html): Learn how to clean up the resources created for the CodeDeploy GitHub tutorial in order to avoid ongoing charges.

### [Tutorial: Deploy an application into Amazon ECS](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-deployment.html)

Follow the steps in this CodeDeploy tutorial to use CodeDeploy to deploy an updated application into Amazon ECS.

- [Prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-prereqs.html): To complete this tutorial, you must first:
- [Step 1: Update your Amazon ECS application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-update-the-ecs-application.html): In this section, you update your Amazon ECS application with a new revision of its task definition.
- [Step 2: Create the AppSpec file](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-create-appspec-file.html): In this section, you create your AppSpec file and upload it to the Amazon S3 bucket you created in the section.
- [Step 3: Use the CodeDeploy console to deploy your application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-deployment-deploy.html): In this section, you create a CodeDeploy application and deployment group to deploy your updated application into Amazon ECS.
- [Step 4: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-clean-up.html): The next tutorial, , builds on this tutorial and uses the CodeDeploy application and deployment group you created.

### [Tutorial: Deploy an Amazon ECS service with a validation test](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-deployment-with-hooks.html)

Follow the steps in this CodeDeploy tutorial to use CodeDeploy to deploy an updated Amazon ECS service with a deployment validation test.

- [Prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-prereqs.html): To successfully complete this tutorial, you must first:
- [Step 1: Create a test listener](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-create-second-listener.html): An Amazon ECS deployment with validation tests requires a second listener.
- [Step 2: Update your Amazon ECS application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-update-the-ecs-application.html): In this section, you update your Amazon ECS application to use a new revision of its task definition.
- [Step 3: Create a lifecycle hook Lambda function](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-create-hooks.html): In this section, you implement one Lambda function for your Amazon ECS deployment's AfterAllowTestTraffic hook.
- [Step 4: Update your AppSpec file](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-create-appspec-file.html): In this section, you update your AppSpec file with a Hooks section.
- [Step 5: Use the CodeDeploy console to deploy your Amazon ECS service](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-deployment.html): In this section, you update your deployment group by specifying the port for your test listener.
- [Step 6: View your Lambda hook function output in CloudWatch Logs](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-view-cw-logs.html): If your CodeDeploy deployment is successful, the validation tests in your Lambda hook fuctions are successful, too.
- [Step 7: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutoria-ecs-with-hooks-clean-up.html): When you have finished this tutorial, clean up the resources associated with it to avoid incurring charges for resources that you aren't using.

### [Tutorial: Deploy a Lambda function using AWS SAM](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam.html)

Follow the steps in this tutorial to use CodeDeploy and an AWS Serverless Application Model (AWS SAM) template to deploy an updated Lambda function.

- [Prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-prereqs.html): To complete this tutorial, you must first:

### [Step 1: Set up your infrastructure](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-setup-infrastructure.html)

This topic shows you how to use AWS SAM to create files for your AWS SAM template and your Lambda functions.

### [Create your files](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-create-files.html)

To create your infrastructure, you must create the following files:

- [Create your AWS SAM template](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-template.html): Create an AWS SAM template file that specifies the components in your infrastructure.
- [Create a file for your Lambda function](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-create-lambda-function.html): Create the file for the function you update and deploy later in this tutorial.
- [Create a file for your BeforeAllowTraffic Lambda function](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-create-lambda-before-traffic.html): Create the file for your beforeAllowTraffic hook Lambda function.
- [Create a file for your AfterAllowTraffic Lambda function](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-create-lambda-after-traffic.html): Create the file for your afterAllowTraffic hook Lambda function.
- [Package the AWS SAM application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-package.html): You should now have four files in your SAM-Tutorial directory:
- [Deploy the AWS SAM application](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-deploy.html): Use the AWS SAM sam deploy command with the package.yml file to create your Lambda functions and CodeDeploy application and deployment group using CloudFormation.
- [(Optional) inspect and test your infrastructure](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-confirm-components.html): This topic shows how to view your infrastructure components and test your Lambda function.
- [Step 2: Update the Lambda function](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-update-function.html): In this topic, you update your myDateTimeFunction.js file.
- [Step 3: Deploy the updated Lambda function](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-deploy-update.html): In this step, you use your updated myDateTimeFunction.js to update and initiate the deployment of your Lambda function.
- [Step 4: View your deployment results](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-deploy-view-results.html): In this step, you view the results of your deployment.
- [Step 5: Clean up](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-clean-up.html): To avoid further charges for resources you used during this tutorial, delete the resources created by your AWS SAM template and the CloudWatch logs created by your Lambda validation functions.


## [Working with the CodeDeploy agent](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent.html)

### [Managing CodeDeploy agent operations](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations.html)

Learn how to install, uninstall, reinstall, or update the CodeDeploy agent and verify the CodeDeploy agent is running.

- [Verify the CodeDeploy agent is running](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-verify.html): Learn how to verify that the CodeDeploy agent is running.
- [Determine the version of the CodeDeploy agent](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-version.html): Learn how to determine which version of the CodeDeploy is running on an instance.

### [Install the CodeDeploy agent](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install.html)

Learn how to install the CodeDeploy agent.

- [Install the CodeDeploy agent using AWS Systems Manager](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ssm.html): You can use the AWS Management Console or the AWS CLI to install the CodeDeploy agent to your Amazon EC2 or on-premises instances by using AWS Systems Manager.

### [Install the CodeDeploy agent using the command line](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-cli.html)

- [Install the CodeDeploy agent for Amazon Linux or RHEL](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html): Sign in to the instance, and run the following commands, one at a time.
- [Install the CodeDeploy agent for Ubuntu Server](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html)
- [Install the CodeDeploy agent for Windows Server](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-windows.html): On Windows Server instances, you can use one of these methods to download and install the CodeDeploy agent:

### [Update the CodeDeploy agent](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-update.html)

Learn how to update the version of the CodeDeploy agent that is running on an instance.

- [Update the CodeDeploy agent on Amazon Linux or RHEL](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-update-linux.html): To configure automatic, scheduled updates of the CodeDeploy agent using AWS Systems Manager, follow the steps in Install the CodeDeploy agent with AWS Systems Manager.
- [Update the CodeDeploy agent on Ubuntu Server](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-update-ubuntu.html): To configure automatic, scheduled updates of the CodeDeploy agent using AWS Systems Manager, follow the steps in Install the CodeDeploy agent with AWS Systems Manager.
- [Update the CodeDeploy agent on Windows Server](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-update-windows.html): You can enable automatic updates of the CodeDeploy agent with AWS Systems Manager.
- [Uninstall the CodeDeploy agent](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-uninstall.html): Learn how to uninstall the CodeDeploy agent from an instance.
- [Send CodeDeploy agent logs to CloudWatch](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-cloudwatch-agent.html): You can send CodeDeploy agent metric and log data to CloudWatch using the unified CloudWatch agent, or more simply, the CloudWatch agent.


## [Working with instances](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances.html)

- [Tagging instances for CodeDeploy deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html): Learn how CodeDeploy uses instance tags and tag filter sets to identify the instances to be included in a deployment group.

### [Working with Amazon EC2 instances](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-ec2.html)

Learn how to create and configure an Amazon EC2 instance for use in CodeDeploy deployments.

- [Create an Amazon EC2 instance for CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-ec2-create.html): Learn how to launch an Amazon EC2 instance configured for use in CodeDeploy deployments.
- [Create an Amazon EC2 instance (CloudFormation template)](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-ec2-create-cloudformation-template.html): Learn how to use an CloudFormation template configured for use in CodeDeploy deployments to launch an Amazon EC2 instance running Amazon Linux or Windows Server.
- [Configure an Amazon EC2 instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-ec2-configure.html): Learn how to configure an Amazon EC2 instance running Amazon Linux, Ubuntu Server, Red Hat Enterprise Linux, or Windows Server for use in CodeDeploy deployments.

### [Working with on-premises instances](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html)

Learn how to configure an on-premises instance for use in CodeDeploy deployments.

- [Prerequisites for configuring an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises-prerequisites.html): Learn about the prerequisites that must be met before you can register an on-premises instance using CodeDeploy.

### [Register an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-register.html)

Learn how to register on-premises instances to be used in CodeDeploy deployments.

- [Use the register-on-premises-instance command (IAM Session ARN) to register an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/register-on-premises-instance-iam-session-arn.html): Learn how to use the CodeDeploy register-on-premises-instance command with an IAM session ARN to register an on-premises instance.
- [Use the register command (IAM user ARN) to register an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises-register-instance.html): Learn how to use the CodeDeploy 'register' command to register an on-premises instance.
- [Use the register-on-premises-instance command (IAM user ARN) to register an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/register-on-premises-instance-iam-user-arn.html): Learn how to use the CodeDeploy register-on-premises-instance command with an IAM user ARN to register an on-premises instance.

### [Managing on-premises instances operations](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations.html)

Learn how to work with an on-premises instance after it has been registered with CodeDeploy.

- [Get information about a single on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations-view-details-single.html): Learn how to view details about an on-premises instance after it has been registered with CodeDeploy.
- [Get information about multiple on-premises instances](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations-view-details-multiple.html): Learn how to view details about multiple on-premises instances after they have been registered with AWS CodeDeploy.
- [Manually remove on-premises instance tags from an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations-remove-tags.html): Learn how to remove tags from an on-premises instance after it has been registered with CodeDeploy.
- [Automatically uninstall the CodeDeploy agent and remove the configuration file from an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations-uninstall-agent.html): Learn how to uninstall the CodeDeploy agent from an on-premises instance after it has been registered with CodeDeploy.
- [Automatically deregister an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations-deregister-automatically.html): Learn how to deregister an on-premises instance automatically after it has been registered with CodeDeploy.
- [Manually deregister an on-premises instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/on-premises-instances-operations-deregister-manually.html): Learn how deregister an on-premises instance manually after it has been registered with CodeDeploy.
- [View instance details](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-view-details.html): Learn how to use the CodeDeploy console or the AWS CLI to view details about instances used in a deployment.
- [Instance health](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html): Learn how CodeDeploy monitors the health status of the instances in a deployment group.


## [Working with deployment configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)

- [Create a deployment configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html): Learn how to use the AWS CLI to create a deployment configuration in CodeDeploy.
- [View deployment configuration details](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-view-details.html): Learn how to use the CodeDeploy console or the AWS CLI to view details about deployment configurations.
- [Delete a deployment configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-delete.html): Learn how to use the AWS CLI to delete a CodeDeploy deployment configuration.


## [Working with applications](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications.html)

### [Create an application](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create.html)

Learn how to use the CodeDeploy console or the AWS CLI to create an application.

- [Create an application for an in-place deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-in-place.html): Learn how to use the CodeDeploy console to create an application for an in-place deployment.
- [Create an application for a blue/green deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-blue-green.html): Learn how to use the CodeDeploy console to create an application for a blue/green deployment.
- [Create an application for an Amazon ECS service deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-ecs.html): You can use the CodeDeploy console to create an application for an Amazon ECS service deployment.
- [Create an application for an AWS Lambda function deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-lambda.html): You can use the CodeDeploy console to create an application for an AWS Lambda function deployment.
- [Create an application (CLI)](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-cli.html): Learn how to use the AWS CLI to create an application, which is simply a unique identifier to group the options for a CodeDeploy deployment.
- [View application details](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-view-details.html): Learn how to use the CodeDeploy console or the AWS CLI to view details about all applications.
- [Create a notification rule](https://docs.aws.amazon.com/codedeploy/latest/userguide/notification-rule-create.html): Learn how to create a notification rule for AWS CodeDeploy.
- [Rename an application](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-rename.html): Learn how to use the AWS CLI or CodeDeploy APIs to change application names in CodeDeploy.
- [Delete an application](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-delete.html): Learn how to use the CodeDeploy console or the AWS CLI to delete an application in CodeDeploy.


## [Working with deployment groups](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups.html)

### [Create a deployment group](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create.html)

Learn how to use the CodeDeploy console or the AWS CLI to create a deployment group.

- [Create a deployment group for an in-place deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-in-place.html): Learn how to create a deployment group that you can use for a CodeDeploy in-place deployment.
- [Create a deployment group for an EC2/On-Premises blue/green deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-blue-green.html): Learn how to use the CodeDeploy console or the AWS CLI to create an application for a blue/green deployment.
- [Create a deployment group for an Amazon ECS deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-ecs.html)
- [Set up a load balancer in Elastic Load Balancing for CodeDeploy Amazon EC2 deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-load-balancer.html): Learn how to create a Classic Load Balancer, Application Load Balancer, or Network Load Balancer in Elastic Load Balancing that you will use to register the instances in your replacement environment.
- [Set up a load balancer, target groups, and listeners for CodeDeploy Amazon ECS deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-load-balancer-for-ecs.html): Learn how to create an Application Load Balancer in Elastic Load Balancing that you will use to register the instances in your replacement environment.
- [Create a deployment group (CLI)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-cli.html): Learn how to use the AWS CLI to create a deployment group for CodeDeploy deployments.
- [View deployment group details](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-view-details.html): Learn how to use the CodeDeploy console or the AWS CLI to view details about all deployment groups associated with an application.
- [Change deployment group settings](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-edit.html): Learn how to use the CodeDeploy console or the AWS CLI to change the settings of a deployment group.
- [Configure advanced options for a deployment group](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-configure-advanced-options.html): Learn how to configure advanced options for a deployment group, including Amazon SNS notification triggers, Amazon CloudWatch alarms, and automatic rollbacks.
- [Delete a deployment group](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-delete.html): Learn how to use the CodeDeploy console and the AWS CLI to delete a deployment group.


## [Working with application revisions](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions.html)

- [Plan a revision](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-plan.html): Learn how to plan a revision for CodeDeploy.
- [Add an AppSpec File](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-appspec-file.html): Learn about the AppSpec file, which includes instructions for CodeDeploy to follow as it deploys a revision to instances.
- [Choose a repository type](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-repository-type.html): Learn about the use of repositories for storing application revisions in CodeDeploy.
- [Push a revision](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-push.html): Learn how to use the AWS CLI to push an application revision file bundle for CodeDeploy to Amazon S3.
- [View application revision details](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-view-details.html): Learn how to use the CodeDeploy console or the AWS CLI to view details about all application revisions for a specific application.
- [Register an application revision](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-register.html): Learn how to use the AWS CLI to register an application revision in Amazon S3 with CodeDeploy.


## [Working with deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments.html)

### [Create a deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create.html)

Learn how to use the CodeDeploy console to create a deployment.

- [Deployment prerequisites](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-prerequisites.html): Learn about the prerequisites for creating a deployment in CodeDeploy.
- [Create an Amazon ECS Compute Platform deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-console-ecs.html): Learn how to use the CodeDeploy console to create an Amazon ECS compute platform deployment.
- [Create an AWS Lambda Compute Platform deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-console-lambda.html): Learn how to use the CodeDeploy console to create an AWS Lambda compute platform deployment.

### [Create an EC2/On-Premises Compute Platform deployment (console)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-console.html)

Learn how to use the CodeDeploy console to create an EC2/On-Premises compute platform deployment.

- [Specify information about a revision stored in an Amazon S3 bucket](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-console-s3.html): Learn how to specify information about an application revision stored in an Amazon S3 bucket to use in a CodeDeploy deployment.
- [Specify information about a revision stored in a GitHub repository](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-console-github.html): Learn how to specify information about an application revision stored in a GitHub repository to use in a CodeDeploy deployment.
- [Create an Amazon ECS Compute Platform deployment (CLI)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-ecs-cli.html): Learn how to use the AWS CLI to create a CodeDeploy deployment to the Amazon ECS compute platform.
- [Create an AWS Lambda Compute Platform deployment (CLI)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-lambda-cli.html): Learn how to use the AWS CLI to create a CodeDeploy deployment to the AWS Lambda compute platform.

### [Create an EC2/On-Premises Compute Platform deployment (CLI)](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-cli.html)

Learn how to use the AWS CLI to create a CodeDeploy deployment to the EC2/On-Premises compute platform.

- [Connect a CodeDeploy application to a GitHub repository](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-cli-github.html): Learn how to create a connection between a CodeDeploy application and a code repository in GitHub.
- [Create an Amazon ECS blue/green deployment through CloudFormation](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-ecs-cfn.html): You can use AWS CloudFormation to manage Amazon ECS blue/green deployments through CodeDeploy.
- [View deployment details](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-view-details.html): Learn how to use the CodeDeploy console or the AWS CLI to view details about deployments.
- [View deployment log data](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-view-logs.html): Learn how to view deployment log data generated by a CodeDeploy deployment.
- [Stop a deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-stop.html): Learn how to use the CodeDeploy console or the AWS CLI to stop a CodeDeploy deployment.
- [Redeploy and roll back a deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html): Learn how to redeploy a revision you previously deployed with CodeDeploy.
- [Deploy an application in a different AWS account](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-cross-account.html): Learn how to initiate deployments in another of your organizationâs accounts by using an IAM role that provides cross-account access.
- [Validate a deployment package on a local machine](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-local.html): Learn how you can use the CodeDeploy agent to run test deployments on local development machines and validate the integrity of application specification files and deployable content.


## [Monitoring deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring.html)

### [Monitoring deployments with Amazon CloudWatch tools](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudwatch.html)

Learn how to monitor CodeDeploy deployments using various CloudWatch tools.

### [Monitoring deployments with CloudWatch alarms](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms.html)

Learn how to create a CloudWatch alarm for an instance or Amazon EC2 Auto Scaling group you are using in your CodeDeploy operations.

- [Grant CloudWatch permissions to a service role](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms-grant-permissions.html): Learn how to give a service role permission to access CloudWatch resources for CodeDeploy.
- [Monitoring deployments with Amazon CloudWatch Events](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudwatch-events.html): Learn how to use Amazon CloudWatch Events to detect and react to changes in the state of an instance or a deployment in your CodeDeploy operations.
- [Monitoring deployments with AWS CloudTrail](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudtrail.html): Learn how to use the information collected by AWS CloudTrail to determine which request was made to CodeDeploy, the source IP address from which the request was made, who made the request, when it was made, and other details.

### [Monitoring deployments with Amazon SNS event notifications](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications.html)

Learn how to create and manage triggers for receiving notifications through Amazon SNS about CodeDeploy deployment and instance events.

- [Grant Amazon SNS permissions to a service role](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-permisssions.html): Learn how to give a service role permission to access Amazon SNS resources for CodeDeploy instance or deployment events.
- [Create a trigger for a CodeDeploy event](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html): Learn how to create a trigger for events in a CodeDeploy instance or deployment.
- [Edit a trigger in a deployment group](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-edit-trigger.html): Learn how to modify triggers for events in a CodeDeploy deployment group.
- [Delete a trigger from a deployment group](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-delete-trigger.html): Learn how to delete triggers for events in a CodeDeploy deployment group.
- [JSON data formats for triggers](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-json-format.html): View examples of the JSON output format that is created when a trigger for a deployment or instance is activated in a custom notification workflow.


## [Security](https://docs.aws.amazon.com/codedeploy/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/codedeploy/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS CodeDeploy.

### [Identity and access management](https://docs.aws.amazon.com/codedeploy/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your CodeDeploy resources.

- [How AWS CodeDeploy works with IAM](https://docs.aws.amazon.com/codedeploy/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to CodeDeploy, you should understand which IAM features are available to use with CodeDeploy.
- [AWS managed (predefined) policies for CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/managed-policies.html): Describes the AWS managed policies for CodeDeploy.
- [CodeDeploy updates to AWS managed policies](https://docs.aws.amazon.com/codedeploy/latest/userguide/managed-policies-updates.html): Lists changes to the AWS managed policies for CodeDeploy.
- [Identity-based policy examples](https://docs.aws.amazon.com/codedeploy/latest/userguide/security_iam_id-based-policy-examples.html): By default, users don't have permission to create or modify CodeDeploy resources.
- [Troubleshooting](https://docs.aws.amazon.com/codedeploy/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with CodeDeploy and IAM.
- [CodeDeploy permissions reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html): Describes the CodeDeploy API operations and the corresponding actions you grant permissions to perform.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/codedeploy/latest/userguide/security_confused_deputy.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Incident response](https://docs.aws.amazon.com/codedeploy/latest/userguide/incident-response.html): Describes monitoring, logging, and incident response in CodeDeploy.
- [Compliance validation](https://docs.aws.amazon.com/codedeploy/latest/userguide/CodeDeploy-compliance.html): Learn which AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/codedeploy/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and learn about AWS CodeDeploy features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/codedeploy/latest/userguide/infrastructure-security.html): Learn how AWS CodeDeploy isolates service traffic.


## [Reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference.html)

### [AppSpec file reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html)

Learn about the structure and sections of the AppSpec file used in CodeDeploy.

### [AppSpec File structure](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure.html)

Learn about the high-level structure of the CodeDeploy AppSpec File.

- [AppSpec 'files' section (EC2/On-Premises deployments only)](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-files.html): Learn about the 'files' section in the CodeDeploy application specification file for deployments to an EC2/On-Premises compute platform.
- [AppSpec 'resources' section (Amazon ECS and AWS Lambda deployments only)](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-resources.html): Learn about the 'resources' section in the CodeDeploy application specification file for deployments to the AWS Lambda compute platform.
- [AppSpec 'permissions' section (EC2/On-Premises deployments only)](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-permissions.html): Learn about the 'permissions' section in the CodeDeploy application specification file for deployments to the EC2/On-Premises compute platform.
- [AppSpec 'hooks' section](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html): Learn about the 'hooks' section in the CodeDeploy application specification file.
- [AppSpec File example](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-example.html): View an example of a CodeDeploy AppSpec File.
- [Validate your AppSpec File and file location](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-validate.html): Learn how to validate the content in a CodeDeploy AppSpec File.
- [Agent configuration reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-agent-configuration.html): Learn how to configure the CodeDeploy agent, a software package that enables an instance to be used in CodeDeploy deployments.
- [CloudFormation template reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-cloudformation-templates.html): Learn about using CloudFormation to create CodeDeploy applications, deployment groups, deployment configurations, and Amazon EC2 instances.
- [Use CodeDeploy with Amazon Virtual Private Cloud](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html): Learn how to configure the CodeDeploy agent, a software package that enables an instance to be used in CodeDeploy deployments.
- [Resource kit reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html): Learn about the contents of the CodeDeploy Resource Kit.
- [Quotas](https://docs.aws.amazon.com/codedeploy/latest/userguide/limits.html): Learn about the quotas and naming constraints for CodeDeploy.


## [Troubleshooting](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting.html)

- [General troubleshooting issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-general.html): Troubleshoot general issues you might encounter when you use CodeDeploy.
- [Troubleshoot EC2/On-Premises deployment issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-deployments.html): Troubleshoot deployment issues you might encounter when you use CodeDeploy to deploy to an EC2/On-Premises compute platform.
- [Troubleshoot Amazon ECS deployment issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-ecs.html): Troubleshoot deployment issues you might encounter when you use CodeDeploy to deploy to an Amazon ECS compute platform.
- [Troubleshoot AWS Lambda deployment issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-deployments-lambda.html): Troubleshoot deployment issues you might encounter when you use CodeDeploy to deploy to an AWS Lambda compute platform.
- [Troubleshoot deployment group issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-deployment-groups.html): Troubleshoot issues with deployment groups you might encounter when you use CodeDeploy.
- [Troubleshoot instance issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-ec2-instances.html): Troubleshoot instance issues you might encounter when you use CodeDeploy.
- [Troubleshoot GitHub token issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-github-token-issues.html): Troubleshoot GitHub token issues you might encounter when you create a CodeDeploy deployment.
- [Troubleshoot Amazon EC2 Auto Scaling issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-auto-scaling.html): Troubleshoot Amazon EC2 Auto Scaling issues you might encounter when you use CodeDeploy.
- [Error codes](https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html): Find information about error codes returned during failed CodeDeploy deployments

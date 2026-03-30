# Source: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/llms.txt

# AWS Infrastructure Composer Developer Guide

> Design and build your modern infrastructure using a visual builder.

- [Troubleshooting](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/ref-troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/doc-history.html)

## [What is Infrastructure Composer?](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/what-is-composer.html)

- [Serverless concepts](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/what-is-concepts.html): Overview of basic serverless concepts that you should know before using AWS Infrastructure Composer.


## [Cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards-intro.html)

- [Enhanced component cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards-component-intro-enhanced.html): Learn about enhanced component card in Infrastructure Composer.
- [Standard component cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards-resource-intro.html): Read about an example of a standard component card in Infrastructure Composer.
- [Card connections](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-connecting.html): Connect cards together to design your serverless application using AWS Infrastructure Composer.


## [Getting started](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/getting-started.html)

- [Take a tour of the console](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/getting-started-tour.html): Try the built-in Infrastructure Composer tour to learn how to develop a serverless application using the visual canvas.
- [Load and modify](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/getting-started-demo.html): Create an Infrastructure Composer demo project and learn to use the visual canvas by adding resources.
- [Build](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/getting-started-build.html): Use Infrastructure Composer to build a CRUD serverless application that manages users in a database.


## [Where to use Infrastructure Composer](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer.html)

### [Infrastructure Composer console](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-console.html)

This section covers the specific use cases of using AWS Infrastructure Composer from the AWS Management Console.

- [Visual overview](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-visual.html): Visual reference information for Infrastructure Composer.

### [Manage your project](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-project.html)

Manage your project from the Infrastructure Composer

- [Create a new project](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-project-new.html): Create a new project in Infrastructure Composer.
- [Import an existing project folder](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-project-import-folder.html): Import a project in Infrastructure Composer.
- [Import an existing project template](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-project-import-template.html): Import a project template in Infrastructure Composer.
- [Save an existing project template](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-project-save-template.html): Save a project template in Infrastructure Composer.
- [Connect to your local IDE](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/other-services-ide.html): To connect the Infrastructure Composer console with your local integrated development environment (IDE), use local sync mode.
- [Allow web page access](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-fsa.html): This section provides a reference of the File System Access API.

### [Locally sync and save](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-project-local-sync.html)

Localy sync and save you Infrastructure Composer project using local sync mode.

- [Activate local sync](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-how-to-locally-sync.html): Follow this topic to activate local sync mode.
- [Load an existing project with local sync](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-how-to-load-with-local-sync.html): Follow this topic to load a project with local sync activated.
- [Import from Lambda console](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/other-services-lambda.html): Infrastructure Composer from the AWS Management Console provides an integration with the Lambda console.
- [Export canvas](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-features-export.html): Reference information fo exporting an image of the canvas in the Infrastructure Composer console.

### [CloudFormation console mode](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-console-cfn-mode.html)

This section describes how and why you can use Infrastructure Composer in CloudFormation console mode.

- [Access this mode](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/setting-up-composer-cfn-mode.html): Follow the guidance in this section to access Infrastructure Composer in CloudFormation console mode.
- [Visualize a deployment](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/composer-cfn-mode-visualize.html): Follow the guidance in this section to visualize a deployment with Infrastructure Composer in CloudFormation console mode.
- [Create a new template](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/composer-cfn-mode-create.html): Follow the guidance in this section to create a new template with Infrastructure Composer in CloudFormation console mode.
- [Update an existing stack](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/composer-cfn-mode-update.html): Follow the guidance in this section to update an existing stack with Infrastructure Composer in CloudFormation console mode.

### [AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-ide.html)

This section covers the specific use cases of using AWS Infrastructure Composer from the AWS Toolkit for Visual Studio Code.

- [Visual overview](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-ide-visual.html): This topic provides a visual overview of Infrastructure Composer's interface from AWS Toolkit for Visual Studio Code.
- [Access from VS Code](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/setting-up-composer-access-ide.html): This section describes how you can access AWS Infrastructure Composer from the AWS Toolkit for Visual Studio Code.
- [Sync to AWS Cloud](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-ide-sync.html): Use the sync button in Infrastructure Composer to deploy your application to the AWS Cloud.
- [Infrastructure Composer with Amazon Q](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-ide-cw.html): Use Amazon Q within Infrastructure Composer to generate the infrastructure code for your AWS resources as you design your application.


## [How to compose](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-basics.html)

- [Place cards on the canvas](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-navigation.html): This section describes how you select and drag resource cards in Infrastructure Composer's visual canvas.
- [Group cards together](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-navigation-gestures-group.html): This section describes how you group Infrastructure Composer cards on its visual canvas.

### [Connect cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-navigation-gestures-connect.html)

This section describes how you connect Infrastructure Composer cards in its visual canvas.

- [Examples](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-connecting-examples.html): Use the examples in this section to get an idea of how to connect cards in Infrastructure Composer.
- [Disconnect cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-navigation-gestures-disconnect.html): disconnect AWS resources using enhanced component cards and standard component cards.
- [Arrange cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/reference-navigation-gestures-arrange.html): This section describes how you arrange Infrastructure Composer cards in its visual canvas.

### [Configure and modify cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards.html)

Configure cards in Infrastructure Composer to design and build your application architecture through a visual canvas.

### [Enhanced cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards-use-enhanced-component.html)

Configure enhanced component cards in Infrastructure Composer to design and build your application architecture through a visual canvas.

- [Amazon RDS card](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-rds.html): Use the Amazon RDS Database (External) enhanced component card to connect to an Amazon RDS DB cluster, instance, or proxy on an external template.
- [Step Functions card](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-sf.html): AWS Infrastructure Composer features an integration with AWS Step FunctionsÂ Workflow Studio
- [Standard cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-standard-cards.html): Configure standard component cards in Infrastructure Composer to design and build your application architecture through a visual canvas.
- [Delete cards](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-cards-delete.html): This section provides instructions for deleting cards in AWS Infrastructure Composer.
- [View code updates](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-change-inspector.html): Use the Change Inspector in Infrastructure Composer console to view code updates as you design your application.

### [Reference external files](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files.html)

Reference external files in Infrastructure Composer to reuse repeated code with AWS SAM templates.

- [Best practices](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-best-practices.html): Follow best practices for using external file references in Infrastructure Composer
- [Create an external file reference](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-new.html): Create external file references in Infrastructure Composer
- [Load a project](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-load.html): Load external file references in Infrastructure Composer
- [Create an application using the AWS SAMÂ CLI](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-examples-example3.html): This example uses the AWS SAMÂ CLI to create an application that references an external file for its state machine definition.
- [Reference an OpenAPI specification](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-examples-example1.html): This example uses Infrastructure Composer from the console to reference an external OpenAPI specification file that defines a API Gateway REST API.

### [Integrate with Amazon VPC](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc.html)

Use Infrastructure Composer to visualize and connect to a Amazon VPC that is defined on an external template.

- [Identify resources and information](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc-tag.html): Identify resources in a Amazon VPC using the VPC tag.
- [Configure functions](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc-configure.html): To start configuring a Lambda function with a VPC that is defined on another template, use the Lambda Function enhanced component card.
- [Parameters in imported templates](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc-import.html): Use and add parameters from an imported template for an external VPC with Infrastructure Composer
- [Adding new parameters to imported templates](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc-import-add.html): When you import an existing template with parameters defined, you can also create new parameters.
- [Configure a Lambda function with a VPC in another template](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc-examples.html): This section provides an example of using Infrastructure Composer with Amazon VPC.


## [Deploy to the AWS Cloud](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/other-services-cfn.html)

- [Set up the AWS SAMÂ CLI](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/other-services-cfn-sam-using.html): Use AWS SAM and Infrastructure Composer deploy your application.
- [Build and deploy](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/other-services-cfn-sam-examples-example1.html): Use this example to learn how to build and deploy an Infrastructure Composer application with AWS SAM
- [Delete a stack](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/other-services-cfn-sam-examples-example2.html): Use this example to learn how to delete an Infrastructure Composer application with AWS SAM


## [Security](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/security.html)

- [Data protection](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Infrastructure Composer.

### [AWS Identity and Access Management](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/security-iam.html)

How to authenticate requests and manage access your Infrastructure Composer resources.

- [How AWS Infrastructure Composer works with IAM](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/security_iam_service-with-iam.html): Learn how AWS Infrastructure Composer works with AWS Identity and Access Management
- [Compliance validation](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Infrastructure Composer features for data resiliency.

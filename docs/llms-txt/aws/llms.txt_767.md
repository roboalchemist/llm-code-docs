# Source: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/llms.txt

# AWS Service Catalog Administrator Guide

> AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, databases, and more to complete multi-tier application architectures.

- [External Engines](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/external-engine.html)
- [Document History](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/history.html)

## [What Is Service Catalog?](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)

- [Overview](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html): Get started with Service Catalog by learning basic concepts.
- [Quotas](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/limits.html): Your AWS account has the following default quotas for AWS Organizations, constraint, portfolio, product, provisioned product, regional, service action, and TagOptions.


## [Setting Up](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/setup.html)

- [Grant permissions to administrators](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-iamadmin.html): Update your IAM permissions to meet the requirements for catalog administration.
- [Grant permissions to end users](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-iamenduser.html): Grant IAM permissions to the AWS Service Catalog end users who will launch your product.

### [Install and configure the Terraform provisioning engine](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/install-config-engine.html)

Install and configure a Terraform provisioning engine in AWS Service Catalog.

- [Adding Confused Deputy to your Terraform provisioning engine](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/confused-deputy-TRFM-engine.html)


## [Getting Started](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted.html)

- [Getting Started Library](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-library.html): AWS Service Catalog provides a Getting Started Library of well-architected product templates so you can get started quickly.

### [Getting started with an CloudFormation product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-CFN.html)

Learn the basics of AWS Service Catalog administration with a tutorial.

- [Step 1: Download the template](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-template.html): Download a sample CloudFormation template for use with the AWS Service Catalog tutorial.
- [Step 2: Create a key pair](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-keypair.html): Create an Amazon EC2 key pair so that the end user can launch the product for this tutorial.
- [Step 3: Create a portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-portfolio.html): Create a AWS Service Catalog portfolio to organize your products and distribute them to users.
- [Step 4: Create a new product in the portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-product.html): Create a new product in the portfolio you created in the previous step.
- [Step 5: Add a template constraint](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-constraint.html): Add a template constraint to your AWS Service Catalog portfolio to restrict how a product is used.
- [Step 6: Add a launch constraint](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-launchconstraint.html): Define a launch constraint to designate an IAM role that AWS Service Catalog can assume when an end user launches a product.
- [Step 7: Grant end users access to the portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-deploy.html): Grant users access to your AWS Service Catalog portfolio to allow them to launch products.
- [Step 8: Test the end user experience](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-verify.html): Test your AWS Service Catalog portfolio by logging in with an end user account and launching the product.

### [Getting started with a Terraform product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-Terraform.html)

Learn the basics of AWS Service Catalog administration with a tutorial for creating a Terraform product.

- [Updating to External product type](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/update_terraform_open_source_to_external.html): Learn how to update your existing Terraform Open Source products and provisioned products to the External product type.
- [Prerequisite: Configure your Terraform provisioning engine](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-terraform-engine.html): As a prerequisite to creating Terraform products in AWS Service Catalog, you must install and configure a provisioning engine in your Service Catalog administrator account (hub account).
- [Step 1: Terraform configuration file download](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-template-Terraform.html): Download a sample Terraform configuration file for use with the AWS Service Catalog tutorial.
- [Step 2: Create a Terraform product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-product-Terraform.html): Create a new Terraform product.
- [Step 3: Create a portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-portfolio-Terraform.html): Create a AWS Service Catalog portfolio to organize your products and distribute them to users.
- [Step 4: Add product to portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-portfolio-add-product-Terraform.html): In this step, add the Terraform product you created in Step 2 to the portfolio.
- [Step 5: Create launch roles](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-launchrole-Terraform.html): Create the launch role for your Terraform product.
- [Step 6: Add a launch constraint](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-launchconstraint-Terraform.html): Create a launch constraint designating the IAM role that the Terraform provisioning engine and AWS Service Catalog can assume when an end user launches a product.
- [Step 7: Grant end user access](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-deploy-Terraform.html): Grant users access to your AWS Service Catalog portfolio to allow them to launch products.
- [Step 8: Share portfolio with end user](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-share-portfolio-end-user-Terraform.html): Share the portfolio containing the Terraform product with end users.
- [Step 9: Test the end user experience](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-verify-Terraform.html): Test your AWS Service Catalog portfolio by logging in with an end user account and launching the Terraform product.
- [Step 10: Monitoring Terraform provisioning operations](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-monitoring-Terraform.html): If you want to monitor provisioning operations, you can review Amazon CloudWatch logs and AWS Step Functions for any provisioning workflow.


## [Security](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security.html)

- [Data Protection](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Service Catalog.

### [Identity and Access Management](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html)

Access to AWS Service Catalog requires credentials.

- [Identity-based policy examples for AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security_iam_service-with-iam-id-based-policies-examples.html): Topics
- [AWS managed policies](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AppRegistry and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html): How to use service-linked roles to give AWS Service Catalog access to resources in your AWS account.
- [Troubleshooting AWS Service Catalog identity and access](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security_iam_troubleshoot.html): How to troubleshoot IAM in AWS Service Catalog
- [Controlling Access](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/access-control.html): a AWS Service Catalog portfolio gives your administrators a level of access control for your groups of end users.
- [Logging and Monitoring](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-and-monitoring.html): Learn how AWS Service Catalog detects and alerts for incidents with logging and monitoring using AWS CloudTrail.
- [Compliance Validation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/service-catalog-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Service Catalog features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html): Learn how AWS Service Catalog isolates service traffic.
- [Security Best Practices](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html): Learn about security best practices in AWS Service Catalog.


## [Managing Catalogs](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs.html)

### [Managing Portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios.html)

Create AWS Service Catalog portfolios, add products to them, and configure constraints, tags, and permissions in the AWS Management Console.

- [Creating and Deleting Portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/portfoliomgmt-create.html): Create and delete portfolios in the AWS Management Console.
- [Adding products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/portfoliomgmt-products.html): Add products to a AWS Service Catalog portfolio.
- [Adding Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/portfoliomgmt-constraints.html): Add constraints to products in a AWS Service Catalog portfolio to extend the base product with rules that apply to users of the portfolio.
- [Granting Access to Users](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html): Grant users access to AWS Service Catalog portfolios to allow them to launch the products that it contains.
- [Sharing a Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.html): Enable a AWS Service Catalog administrator for another AWS account to distribute your products to end users by sharing your AWS Service Catalog portfolio with that AWS account.
- [Sharing and Importing Portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing.html): To make your AWS Service Catalog products available to users who are not in your AWS account (such as users who belong to other organizations or to other AWS accounts in your organization), you share your portfolios with their AWS accounts.

### [Managing Products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_products.html)

Create, update, and delete AWS Service Catalog products in the administrator console.

- [Creating Products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-cloudresource.html): Create new AWS Service Catalogproducts in the AWS Management Console.
- [Adding products to portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_adding-products.html): A section about adding AWS Service Catalog products to portfolios to distribute them to users.
- [Updating products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-update.html): A section about creating a new version of a AWS Service Catalog product when you update the underlying template.

### [Syncing products to template files from external repositories](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/git-synced-sc-products.html)

Learn how to create and configure products that you connect to template files from an external repository provider.

- [AWS Region support for Git-synced products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/git-sync-supported-regions.html): AWS Service Catalog supports Git-synced produtcs in AWS Regions as indicated in the table below.

### [Deleting products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-delete.html)

A section about deleting AWS Service Catalog products from your account.

- [Deleting products using the AWS CLI](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/product-delete-cli.html): A section about using the AWS CLI to delete a product from a portfolio.
- [Resolving failed resource disassociations when deleting a product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/product-delete-exception.html): A section about resolving delete product exceptions if AWS Service Catalog fails to delete a product with multiple associated resources.
- [Managing Versions](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/managing-versions.html): Managing product versions in AWS Service Catalog.

### [Using Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html)

Apply constraints to a AWS Service Catalog product to control how a product is launched and which rules are applied when the product is launched from a specific portfolio.

- [Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html): Apply the launch constraint to designate an IAM role that AWS Service Catalog assumes when an end user launches, updates, or terminates a product.
- [Notification Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-notification.html)
- [Tag Update Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-resourceupdate.html): Tag update constraints allow administrators to allow or disallow updates to AWS Service Catalog tags in a provisioned product.
- [Stack Set Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-stackset.html): Stack set constraints allow you to specify multiple accounts and regions for your AWS Service Catalog product launch.

### [Template Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_constraints_template-constraints.html)

You can add template constraints to a AWS Service Catalog product to limit the options that are available to end users when they launch that product.

- [Template Constraint Rules](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html): Template constraint rules in a AWS Service Catalog portfolio describe when end users can use the template and which values they can specify for parameters.
- [Using Service Actions](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-actions.html): AWS Service Catalog service actions enable you to allow end users to perform operational tasks, troubleshoot issues, run approved commands, or request permissions in AWS Service Catalog.
- [Adding AWS Marketplace Products to Your Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_marketplace-products.html): Add AWS Marketplace products to your portfolios to make those products available to your AWS Service Catalog end users.
- [Using CloudFormation StackSets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html): AWS Service Catalog users can use CloudFormation StackSets to deploy products across multiple regions and accounts.
- [Managing Budgets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_budgets.html): Create budgets with AWS Budgets and associate them with AWS Service Catalog products and portfolios.


## [Managing Provisioned Products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/provisioned-products.html)

- [Managing provisioned products as the administrator](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/provisioned-products-admin.html): This section describes how to view and manage all of your provisioned products as the administrator.
- [Changing Provisioned Product Owner](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/change-pp-owner.html): You can change the owner of a provisioned product anytime.
- [Updating templates for provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/pp-templates.html): How to update templates for provisioned products
- [Tutorial: Identifying User Resource Allocation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/provisioned-products-tutorial.html): You can identify the user who provisioned a product and resources associated with the product using the AWS Service Catalog console.
- [Managing Terraform Open Source product status errors](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/provisioned-products-lifecycle.html): Terraform Open Source ProvisionProduct failures are routed to the TAINTED state, allowing each provisioned product to proceed to UpdateProvisionedProduct.
- [Managing the Terraform Open Source product state file](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-terraform-engine-state.html): Every Terraform Open Source provisioned product has a single-state file.


## [Managing Tags](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/managing-tags.html)

- [AutoTags](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/autotags.html): Use AutoTags in AWS Service Catalog.

### [TagOption Library](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions.html)

Use TagOptions in AWS Service Catalog.

- [Launching a Product with TagOptions](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions-launching.html): When a user launches a product that has TagOptions, AWS Service Catalog performs the following actions on your behalf:
- [Managing TagOptions](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions-manage.html): As an administrator, you can perform the following actions to manage TagOptions in the TagOptions library:
- [Using TagOptions with AWS Organizations tag policies](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoption-policies.html): This topic provides a brief overview of tag policies for AWS Organizations and TagOptions for AWS Service Catalog.


## [Monitoring](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/service-catalog-monitoring.html)

- [Monitoring Tools](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/monitoring-automated-manual.html): Configure AWS tools to monitor AWS Service Catalog.

### [CloudWatch Metrics](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/cloudwatch-metrics.html)

You can monitor your AWS Service Catalog resources using Amazon CloudWatch, which collects and processes raw data from AWS Service Catalog into readable metrics.

- [Viewing AWS Service Catalog Metrics](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/viewing-cloudwatch-metrics.html): You can view Amazon CloudWatch metrics in the Amazon CloudWatch console, which provides a fine-grained and customizable display of your resources, as well as the number of running tasks in a service.
- [CloudTrail logs](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-using-cloudtrail.html): Learn about logging AWS Service Catalog with AWS CloudTrail.


## [Console branding](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/console-branding.html)

- [AWS Region support for console branding](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/branding-supported-regions.html): Review which AWS Regions support AWS Service Catalog console branding preferences.

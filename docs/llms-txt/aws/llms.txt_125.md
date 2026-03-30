# Source: https://docs.aws.amazon.com/autoscaling/plans/userguide/llms.txt

# AWS Auto Scaling Scaling Plans User Guide

> Use AWS Auto Scaling to quickly discover all of the scalable resources for your application and set up automatic scaling in a matter of minutes.

- [What is a scaling plan?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)
- [How scaling plans work](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html)
- [Best practices](https://docs.aws.amazon.com/autoscaling/plans/userguide/best-practices-for-scaling-plans.html)
- [Migrate your scaling plan](https://docs.aws.amazon.com/autoscaling/plans/userguide/migrate-scaling-plan.html)
- [Quotas](https://docs.aws.amazon.com/autoscaling/plans/userguide/scaling-plan-quotas.html)
- [Document history](https://docs.aws.amazon.com/autoscaling/plans/userguide/scaling-plan-doc-history.html)

## [Getting started](https://docs.aws.amazon.com/autoscaling/plans/userguide/getting-started-with-scaling-plans.html)

- [Step 1: Find your scalable resources](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-select-application.html): This section includes a hands-on introduction to creating scaling plans in the AWS Auto Scaling console.
- [Step 2: Specify the scaling strategy](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-configure-scaling-plan.html): Use the following procedure to specify scaling strategies for the resources that were found in the previous step.
- [Step 3: Configure advanced settings (optional)](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-specify-custom-settings.html): Now that you have specified the scaling strategy to use for each resource type, you can choose to customize any of the default settings on a per resource basis using the Configure advanced settings step.
- [Step 4: Create your scaling plan](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-create-scaling-plan.html): On the Review and create page, review the details of your scaling plan and choose Create scaling plan.
- [Step 5: Clean up](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-delete-scaling-plan.html): After you have completed the getting started tutorial, you can choose to keep your scaling plan.
- [Step 6: Next steps](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-next-steps.html): Now that you have familiarized yourself with scaling plans and some of its features, you may want to try creating your own scaling plan template using CloudFormation.


## [Security](https://docs.aws.amazon.com/autoscaling/plans/userguide/security.html)

- [AWS PrivateLink](https://docs.aws.amazon.com/autoscaling/plans/userguide/scaling-plan-vpc-endpoints.html): Access the AWS Auto Scaling API from your VPC without sending traffic over the internet.
- [Data protection](https://docs.aws.amazon.com/autoscaling/plans/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Auto Scaling.

### [Identity and access management](https://docs.aws.amazon.com/autoscaling/plans/userguide/auth-and-access-control.html)

How to use IAM to control access to your scaling plans.

- [How scaling plans work with IAM](https://docs.aws.amazon.com/autoscaling/plans/userguide/security_iam_service-with-iam.html): Before you use IAM to manage who can create, access, and manage AWS Auto Scaling scaling plans, you should understand what IAM features are available to use with scaling plans.
- [Service-linked roles](https://docs.aws.amazon.com/autoscaling/plans/userguide/aws-auto-scaling-service-linked-roles.html): AWS Auto Scaling uses service-linked roles for the permissions that it requires to call other AWS on your behalf when you work with a scaling plan.
- [Identity-based policy examples](https://docs.aws.amazon.com/autoscaling/plans/userguide/security_iam_id-based-policy-examples.html): By default, a brand new IAM user has no permissions to do anything.
- [Compliance validation](https://docs.aws.amazon.com/autoscaling/plans/userguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/autoscaling/plans/userguide/infrastructure-security.html): Learn how AWS Auto Scaling isolates service traffic.

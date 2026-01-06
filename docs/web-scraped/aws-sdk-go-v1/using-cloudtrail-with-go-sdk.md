# Source: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-cloudtrail-with-go-sdk.html

[](/pdfs/sdk-for-go/v1/developer-guide/aws-sdk-go-dg.pdf#using-cloudtrail-with-go-sdk "Open PDF")

[Documentation](/index.html)[AWS SDK for Go](/sdk-for-go/index.html)[Developer Guide](welcome.html)

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# AWS CloudTrail Examples Using the AWS SDK for Go

CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

The examples assume you have already set up and configured the SDK (that is, you’ve imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](./setting-up.html) and [Configuring the AWS SDK for Go](./configuring-sdk.html).

You can download complete versions of these example files from the [aws-doc-sdk-examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/go/example_code/cloudtrail) repository on GitHub.

###### Topics

  * [Listing the CloudTrail Trails](./cloudtrail-example-describe-trails.html)

  * [Creating a CloudTrail Trail](./cloudtrail-example-create-trail.html)

  * [Listing CloudTrail Trail Events](./cloudtrail-example-lookup-events.html)

  * [Deleting a CloudTrail Trail](./cloudtrail-example-delete-trail.html)




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

SDK Request Examples

Listing the CloudTrail Trails

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

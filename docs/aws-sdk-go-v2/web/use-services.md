# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/use-services.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#use-services "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

# Use the AWS SDK for Go v2 with AWS services

To make calls to an AWS service, you must first construct a service client instance. A service client provides low-level access to every API action for that service. For example, you create an Amazon S3 service client to make calls to Amazon S3 APIs. 

When you call service operations, you pass in input parameters as a struct. A successful call will result in an output struct containing the service API response. For example, after you successfully call an Amazon S3 create bucket action, the action returns an output struct with the bucket's location. 

For the list of service clients, including their methods and parameters, see the [AWS SDK for Go API Reference](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2). 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Handling Errors in the SDK

Amazon S3 checksums

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

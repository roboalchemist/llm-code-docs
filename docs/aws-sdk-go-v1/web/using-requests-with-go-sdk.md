# Source: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-requests-with-go-sdk.html

[](/pdfs/sdk-for-go/v1/developer-guide/aws-sdk-go-dg.pdf#using-requests-with-go-sdk "Open PDF")

[Documentation](/index.html)[AWS SDK for Go](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Using context.Context with SDK RequestsUsing API Field Setters with SDK Requests

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# AWS SDK for Go Request Examples

The AWS SDK for Go examples can help you write your own applications. The examples assume you have already set up and configured the SDK (that is, you have imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](./setting-up.html) and [Configuring the AWS SDK for Go](./configuring-sdk.html).

## Using context.Context with SDK Requests

In Go 1.7, the `context.Context` type was added to `http.Request`. This type provides an easy way to implement deadlines and cancellations on requests.

To use this pattern with the SDK, call `WithContext` on the `HTTPRequest` field of the SDK’s `request.Request` type, and provide your `Context value`. The following example highlights this process with a timeout on Amazon SQS`ReceiveMessage`.
    
    
    req, resp := svc.ReceiveMessageRequest(params)
    req.HTTPRequest = req.HTTPRequest.WithContext(ctx)
    
    err := req.Send()
    if err != nil {
        fmt.Println("Got error receiving message:")
        fmt.Println(err.Error())
    } else {
        fmt.Println(resp)
    }
    

## Using API Field Setters with SDK Requests

In addition to setting API parameters by using struct fields, you can also use chainable setters on the API operation parameter fields. This enables you to use a chain of setters to set the fields of the API struct.
    
    
    svc := s3.New(sess)
    
    _, err := svc.PutObject((&s3.PutObjectInput{}).
        SetBucket(*bucket).
        SetKey(*key).
        SetBody(strings.NewReader("object body")), //.
    //      SetWebsiteRedirectLocation("https://example.com/something"),
    )
    

You can also use this pattern with nested fields in API operation requests.
    
    
    resp, err := svc.UpdateService((&ecs.UpdateServiceInput{}).
        SetService("myService").
        SetDeploymentConfiguration((&ecs.DeploymentConfiguration{}).
            SetMinimumHealthyPercent(80),
        ),
    )
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Code Examples

AWS CloudTrail Examples

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

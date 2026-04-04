# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/handle-errors.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#handle-errors "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Logging ErrorsService Client ErrorsRetrieving Request Identifiers

# Handling Errors in the AWS SDK for Go V2

The AWS SDK for Go returns errors that satisfy the Go `error` interface type. You can use the `Error()` method to get a formatted string of the SDK error message without any special handling. Errors returned by the SDK may implement an `Unwrap` method. The `Unwrap` method is used by the SDK to provide additional contextual information to errors, while providing access to the underlying error or chain of errors. The `Unwrap` method should be used with the [errors.As](https://golang.org/pkg/errors#As) to handle unwrapping error chains. 

It is important that your application check whether an error occurred after invoking a function or method that can return an `error` interface type. The most basic form of error handling looks similar to the following example: 
    
    
    if err != nil {
        // Handle error
        return
    }
    

## Logging Errors

The simplest form of error handling is traditionally to log or print the error message before returning or exiting from the application. 
    
    
    import "log"
    
    // ...
    
    if err != nil {
        log.Printf("error: %s", err.Error())
        return
    }
    

## Service Client Errors

The SDK wraps all errors returned by service clients with the [smithy.OperationError](https://pkg.go.dev/github.com/aws/smithy-go#OperationError) error type. `OperationError` provides contextual information about the service name and operation that is associated with an underlying error. This information can be useful for applications that perform batches of operations to one or more services, with a centralized error handling mechanism. Your application can use `errors.As` to access this `OperationError` metadata. 
    
    
    import "log"
    import "github.com/aws/smithy-go"
    
    // ...
    
    if err != nil {
        var oe *smithy.OperationError
        if errors.As(err, &oe) {
            log.Printf("failed to call service: %s, operation: %s, error: %v", oe.Service(), oe.Operation(), oe.Unwrap())
        }
        return
    }
    

### API Error Responses

Service operations can return modeled error types to indicate specific errors. These modeled types can be used with `errors.As` to unwrap and determine if the operation failure was due to a specific error. For example, Amazon S3 `CreateBucket` can return a [BucketAlreadyExists](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3/types#BucketAlreadyExists) error if a bucket of the same name already exists. 

For example, to check if an error was a `BucketAlreadyExists` error: 
    
    
    import "log"
    import "github.com/aws/aws-sdk-go-v2/service/s3/types"
    
    // ...
    
    if err != nil {
        var bne *types.BucketAlreadyExists
        if errors.As(err, &bne) {
            log.Println("error:", bne)
        }
        return
    }
    

All service API response errors implement the [smithy.APIError](https://pkg.go.dev/github.com/aws/smithy-go/#APIError) interface type. This interface can be used to handle both modeled or un-modeled service error responses. This type provides access to the error code and message returned by the service. Additionally, this type provides indication of whether the fault of the error was due to the client or server if known. 
    
    
    import "log"
    import "github.com/aws/smithy-go"
    
    // ...
    
    if err != nil {
        var ae smithy.APIError
        if errors.As(err, &ae) {
            log.Printf("code: %s, message: %s, fault: %s", ae.ErrorCode(), ae.ErrorMessage(), ae.ErrorFault().String())
        }
        return
    }
    

## Retrieving Request Identifiers

When working with AWS Support, you may be asked to provide the request identifier that identifies the request you are attempting to troubleshoot. You can use [http.ResponseError](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws/transport/http#ResponseError) and use the `ServiceRequestID()` method to retrieve the request identifier associated with error response. 
    
    
    import "log"
    import awshttp "github.com/aws/aws-sdk-go-v2/aws/transport/http"
    
    // ...
    
    if err != nil {
        var re *awshttp.ResponseError
        if errors.As(err, &re) {
            log.Printf("requestID: %s, error: %v", re.ServiceRequestID(), re.Unwrap());
        }
        return
    }
    

### Amazon S3 Request Identifiers

Amazon S3 requests contain additional identifiers that can be used to assist AWS Support with troubleshooting your request. You can use [s3.ResponseError](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#ResponseError) and call `ServiceRequestID()` and `ServiceHostID()` to retrieve the request ID and host ID. 
    
    
    import "log"
    import "github.com/aws/aws-sdk-go-v2/service/s3"
    
    // ...
    
    if err != nil {
        var re s3.ResponseError
        if errors.As(err, &re) {
            log.Printf("requestID: %s, hostID: %s request failure", re.ServiceRequestID(), re.ServiceHostID());
        }
        return
    }
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Using the SDK

Use AWS services

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

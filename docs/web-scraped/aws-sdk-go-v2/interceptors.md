# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/interceptors.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#interceptors "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Interceptors vs. middlewareAvailable interceptor hooksInterceptor registrationGlobal interceptor configuration

# HTTP Interceptors

You can use interceptors to hook into the execution of API requests and responses. Interceptors are open-ended mechanisms in which the SDK calls code that you write to inject behavior into the request/response lifecycle. This way, you can modify an in-flight request, debug request processing, view exceptions, and more. 

## Interceptors vs. middleware

The AWS SDK for Go v2 provides both interceptors and middleware for customizing request processing. While both serve similar purposes, they are designed for different audiences and use cases: 

  * **Interceptors** are designed for SDK users who want to customize request/response processing with a simple, HTTP-focused API. They provide specific hook points in the request lifecycle and work directly with HTTP requests and responses. 

  * **Middleware** is a more advanced, transport-agnostic system primarily used internally by the SDK. While powerful, middleware requires deeper knowledge of SDK internals and involves more complex interfaces. 




Key advantages of interceptors over middleware for common use cases: 

  * **HTTP-focused** : Interceptors work directly with HTTP requests and responses, eliminating the need for transport type checking that middleware requires. 

  * **Simpler interfaces** : Each interceptor hook has a specific, focused interface rather than the generic middleware pattern. 

  * **Clearer execution model** : Interceptors execute at well-defined points in the request lifecycle without requiring knowledge of middleware stack ordering. 




###### Note

Interceptors are built on top of the existing middleware system, so both can coexist in the same application. Middleware remains available for advanced use cases that require transport-agnostic behavior or complex stack manipulation. 

## Available interceptor hooks

The AWS SDK for Go v2 provides interceptor hooks at various stages of the request lifecycle. Each hook corresponds to a specific interface that you can implement: 

  * `BeforeExecution` \- First hook called during operation execution 

  * `BeforeSerialization` \- Before input message is serialized into transport request 

  * `AfterSerialization` \- After input message is serialized into transport request 

  * `BeforeRetryLoop` \- Before entering the retry loop 

  * `BeforeAttempt` \- First hook called inside retry loop 

  * `BeforeSigning` \- Before transport request is signed 

  * `AfterSigning` \- After transport request is signed 

  * `BeforeTransmit` \- Before transport request is sent 

  * `AfterTransmit` \- After receiving transport response 

  * `BeforeDeserialization` \- Before transport response is deserialized 

  * `AfterDeserialization` \- After unmarshalling transport response 

  * `AfterAttempt` \- Last hook called inside retry loop 

  * `AfterExecution` \- Last hook called during operation execution 




You can implement multiple interfaces in a single interceptor to hook into multiple stages of the request lifecycle. 

## Interceptor registration

You register interceptors when you construct a service client or when you override configuration for a specific operation. The registration differs depending on whether you want the interceptor to apply to all operations for your client or only specific ones. 

Interceptors are managed through an interceptor registry that provides methods to add and remove interceptors. The following example shows a simple interceptor that adds an AWS X-Ray trace ID header to outgoing requests before the signing process: 
    
    
    type recursionDetection struct{}
    
    func (recursionDetection) BeforeSigning(ctx context.Context, in *smithyhttp.InterceptorContext) error {
        if traceID := os.Getenv("_X_AMZN_TRACE_ID"); traceID != "" {
            in.Request.Header.Set("X-Amzn-Trace-Id", traceID)
        }
        return nil
    }
    
    // use it on the client
    svc := s3.NewFromConfig(cfg, func(o *s3.Options) {
        o.Interceptors.AddBeforeSigning(recursionDetection{})
    })

The interceptor registry is added to client Options, which enables per-operation interceptor configuration: 
    
    
    // ... or use it per-operation
    s3.ListBuckets(context.Background(), &s3.ListBucketsInput{
    }, func(o *s3.Options) {
       o.Interceptors.AddBeforeSigning(recursionDetection{})
    })

## Global interceptor configuration

You can also register interceptors globally using the `config.LoadDefaultConfig` function with the appropriate `With*` options for each interceptor type. This applies the interceptor to all AWS service clients created from that configuration: 
    
    
    type myExecutionInterceptor struct{}
    
    func (*myExecutionInterceptor) AfterExecution(ctx context.Context, in *smithyhttp.InterceptorContext) error {
        // Add your custom logic here
        return nil
    }
    
    cfg, err := config.LoadDefaultConfig(context.Background(),
        config.WithAfterExecution(&myExecutionInterceptor{}))
    if err != nil {
        panic(err)
    }
    
    // every service client created from the above config
    // will include this interceptor
    svc := s3.NewFromConfig(cfg)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

HTTP Client

Logging

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

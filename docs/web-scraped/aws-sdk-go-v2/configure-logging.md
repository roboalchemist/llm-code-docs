# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-logging.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#configure-logging "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

LoggerClientLogMode

# Logging

The AWS SDK for Go has logging facilities available that allow your application to enable debugging information for debugging and diagnosing request issues or failures. The [Logger](https://pkg.go.dev/github.com/aws/smithy-go/logging#Logger) interface and [ClientLogMode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ClientLogMode) are the main components available to you for determining how and what should be logged by clients. 

## Logger

When constructing an [Config](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#Config) using [LoadDefaultConfig](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#LoadDefaultConfig) a default `Logger` is configured to send log messages to the process' standard error (stderr). A custom logger that satisfies the [Logger](https://pkg.go.dev/github.com/aws/smithy-go/logging#Logger) interface can be passed as an argument to `LoadDefaultConfig` by wrapping it with [config.WithLogger](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#WithLogger). 

For example, to configure our clients to use our `applicationLogger`: 
    
    
    cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithLogger(applicationLogger))
    

Now clients configured using the constructed `aws.Config` will send log messages to `applicationLogger`. 

### Context-Aware Loggers

A Logger implementation may implement the optional [ContextLogger](https://pkg.go.dev/github.com/aws/smithy-go/logging#ContextLogger) interface. Loggers that implement this interface will have their `WithContext` methods invoked with the current context. This allows your logging implementations to return a new `Logger` that can write additional logging metadata based on values present in the context. 

## ClientLogMode

By default, service clients do not produce log messages. To configure clients to send log messages for debugging purposes, use the [ClientLogMode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ClientLogMode) member on `Config`. `ClientLogMode` can be set to enable debugging messaging for: 

  * Signature Version 4 (SigV4) Signing 

  * Request Retries 

  * HTTP Requests 

  * HTTP Responses 




For example, to enable logging of HTTP requests and retries: 
    
    
    cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithClientLogMode(aws.LogRetries | aws.LogRequest))
    

See [ClientLogMode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ClientLogMode) for the different client log modes available. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Interceptors

Retries and Timeouts

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

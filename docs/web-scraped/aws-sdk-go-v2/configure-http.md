# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-http.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#configure-http "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Overriding During Configuration LoadingTimeoutDialerTransport

# Customize the HTTP Client

The AWS SDK for Go uses a default HTTP client with default configuration values. Although you can change some of these configuration values, the default HTTP client and transport are not sufficiently configured for customers using the AWS SDK for Go in an environment with high throughput and low latency requirements. For more information, please refer to the [Frequently Asked Questions](./faq-gosdk.html) as configuration recommendations vary based on specific workloads. This section describes how to configure a custom HTTP client, and use that client to create AWS SDK for Go calls. 

To assist you in creating a custom HTTP client, this section describes how to the [NewBuildableClient](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws/transport/http#NewBuildableClient) to configure custom settings, and use that client with an AWS SDK for Go service client. 

Let's define what we want to customize. 

## Overriding During Configuration Loading

Custom HTTP clients can be provided when calling [LoadDefaultConfig](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#LoadDefaultConfig) by wrapping the client using [WithHTTPClient](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#WithHTTP) and passing the resulting value to `LoadDefaultConfig`. For example, to pass `customClient` as our client: 
    
    
    cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithHTTPClient(customClient))
    

## Timeout

The `BuildableHTTPClient` can be configured with a request timeout limit. This timeout includes the time to connect, process any redirects, and read the complete response body. For example, to modify the client timeout: 
    
    
    import "github.com/aws/aws-sdk-go-v2/aws/transport/http"
    
    // ...
    
    httpClient := http.NewBuildableClient().WithTimeout(time.Second*5)
    

## Dialer

The `BuildableHTTPClient` provides a builder mechanics for constructing clients with modified [Dialer](https://golang.org/pkg/net/#Dialer) options. The following example shows how to configure a clients `Dialer` settings. 
    
    
    import awshttp "github.com/aws/aws-sdk-go-v2/aws/transport/http"
    import "net"
    
    // ...
    
    httpClient := awshttp.NewBuildableClient().WithDialerOptions(func(d *net.Dialer) {
        d.KeepAlive = -1
        d.Timeout = time.Millisecond*500
    })
    

### Settings

#### Dialer.KeepAlive

This setting represents the keep-alive period for an active network connection. 

Set to a negative value to disable keep-alives. 

Set to **0** to enable keep-alives if supported by the protocol and operating system. 

Network protocols or operating systems that do not support keep-alives ignore this field. By default, TCP enables keep alive. 

See [https://golang.org/pkg/net/#Dialer.KeepAlive](https://golang.org/pkg/net/#Dialer.KeepAlive)

Set `KeepAlive` as **time.Duration**. 

#### Dialer.Timeout

This setting represents the maximum amount of time a dial waits for a connection to be created. 

Default is 30 seconds. 

See [https://golang.org/pkg/net/#Dialer.Timeout](https://golang.org/pkg/net/#Dialer.Timeout)

Set `Timeout` as **time.Duration**. 

## Transport

The `BuildableHTTPClient` provides a builder mechanics for constructing clients with modified [Transport](https://golang.org/pkg/net/http#Transport) options. 

### Configuring a Proxy

If you cannot directly connect to the internet, you can use Go-supported environment variables (`HTTP_PROXY`/`HTTPS_PROXY`) or create a custom HTTP client to configure your proxy. The following example configures the client to use `PROXY_URL` as the proxy endpoint: 
    
    
    import awshttp "github.com/aws/aws-sdk-go-v2/aws/transport/http"
    import "net/http"
    
    // ...
    
    httpClient := awshttp.NewBuildableClient().WithTransportOptions(func(tr *http.Transport) {
        proxyURL, err := url.Parse("PROXY_URL")
        if err != nil {
            log.Fatal(err)
        }
        tr.Proxy = http.ProxyURL(proxyURL)
    })
    

### Other Settings

Below are a few other `Transport` settings that can be modified to tune the HTTP client. Any additional settings not described here can be found in the [Transport](https://golang.org/pkg/net/http/#Transport) type documentation. These settings can be applied as shown in the following example: 
    
    
    import awshttp "github.com/aws/aws-sdk-go-v2/aws/transport/http"
    import "net/http"
    
    // ...
    
    httpClient := awshttp.NewBuildableClient().WithTransportOptions(func(tr *http.Transport) {
        tr.ExpectContinueTimeout = 0
        tr.MaxIdleConns = 10
    })
    

#### Transport.ExpectContinueTimeout

If the request has an "Expect: 100-continue" header, this setting represents the maximum amount of time to wait for a server's first response headers after fully writing the request headers, This time does not include the time to send the request header. The HTTP client sends its payload after this timeout is exhausted. 

Default 1 second. 

Set to **0** for no timeout and send request payload without waiting. One use case is when you run into issues with proxies or third party services that take a session similar to the use of Amazon S3 in the function shown later. 

See [https://golang.org/pkg/net/http/#Transport.ExpectContinueTimeout](https://golang.org/pkg/net/http/#Transport.ExpectContinueTimeout)

Set `ExpectContinue` as **time.Duration**. 

#### Transport.IdleConnTimeout

This setting represents the maximum amount of time to keep an idle network connection alive between HTTP requests. 

Set to **0** for no limit. 

See [https://golang.org/pkg/net/http/#Transport.IdleConnTimeout](https://golang.org/pkg/net/http/#Transport.IdleConnTimeout)

Set `IdleConnTimeout` as **time.Duration**. 

#### Transport.MaxIdleConns

This setting represents the maximum number of idle (keep-alive) connections across all hosts. One use case for increasing this value is when you are seeing many connections in a short period from the same clients 

**0** means no limit. 

See [https://golang.org/pkg/net/http/#Transport.MaxIdleConns](https://golang.org/pkg/net/http/#Transport.MaxIdleConns)

Set`MaxIdleConns` as **int**. 

#### Transport.MaxIdleConnsPerHost

This setting represents the maximum number of idle (keep-alive) connections to keep per-host. One use case for increasing this value is when you are seeing many connections in a short period from the same clients 

Default is two idle connections per host. 

Set to **0** to use DefaultMaxIdleConnsPerHost (2). 

See [https://golang.org/pkg/net/http/#Transport.MaxIdleConnsPerHost](https://golang.org/pkg/net/http/#Transport.MaxIdleConnsPerHost)

Set `MaxIdleConnsPerHost` as **int**. 

#### Transport.ResponseHeaderTimeout

This setting represents the maximum amount of time to wait for a client to read the response header. 

If the client isn't able to read the response's header within this duration, the request fails with a timeout error. 

Be careful setting this value when using long-running Lambda functions, as the operation does not return any response headers until the Lambda function has finished or timed out. However, you can still use this option with the ** InvokeAsync** API operation. 

Default is no timeout; wait forever. 

See [https://golang.org/pkg/net/http/#Transport.ResponseHeaderTimeout](https://golang.org/pkg/net/http/#Transport.ResponseHeaderTimeout)

Set `ResponseHeaderTimeout` as **time.Duration**. 

#### Transport.TLSHandshakeTimeout

This setting represents the maximum amount of time waiting for a TLS handshake to be completed. 

Default is 10 seconds. 

Zero means no timeout. 

See [https://golang.org/pkg/net/http/#Transport.TLSHandshakeTimeout](https://golang.org/pkg/net/http/#Transport.TLSHandshakeTimeout)

Set `TLSHandshakeTimeout` as **time.Duration**. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Client Endpoints

Interceptors

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

# Source: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/custom-http.html

[](/pdfs/sdk-for-go/v1/developer-guide/aws-sdk-go-dg.pdf#custom-http "Open PDF")

[Documentation](/index.html)[AWS SDK for Go](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Dialer.KeepAliveDialer.TimeoutTransport.ExpectContinueTimeoutTransport.IdleConnTimeoutTransport.MaxIdleConnsTransport.MaxIdleConnsPerHostTransport.ResponseHeaderTimeoutTransport.TLSHandshakeTimeoutCreate Import StatementCreating a Timeout StructCreating a Function to Create a Custom HTTP ClientUsing a Custom HTTP Client

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Creating a Custom HTTP Client

The AWS SDK for Go uses a default HTTP client with default configuration values. Although you can change some of these configuration values, the default HTTP client and transport are not sufficiently configurable for customers using the AWS SDK for Go in an environment with high throughput and low latency requirements. This section describes how to create a custom HTTP client, and use that client to create AWS SDK for Go calls.

To assist you in creating a custom HTTP client, this section describes how to create a structure to encapsulate the custom settings, create a function to create a custom HTTP client based on those settings, and use that custom HTTP client to call an AWS SDK for Go service client.

Let’s define what we want to customize.

## Dialer.KeepAlive

This setting represents the keep-alive period for an active network connection.

Set to a negative value to disable keep-alives.

Set to **0** to enable keep-alives if supported by the protocol and operating system.

Network protocols or operating systems that do not support keep-alives ignore this field. By default, TCP enables keep alive.

See [https://golang.org/pkg/net/#Dialer.KeepAlive](https://golang.org/pkg/net/#Dialer.KeepAlive)

We’ll call this `ConnKeepAlive` as **time.Duration**.

## Dialer.Timeout

This setting represents the maximum amount of time a dial to wait for a connection to be created.

Default is 30 seconds.

See [https://golang.org/pkg/net/#Dialer.Timeout](https://golang.org/pkg/net/#Dialer.Timeout)

We’ll call this `Connect` as **time.Duration**.

## Transport.ExpectContinueTimeout

This setting represents the maximum amount of time to wait for a server’s first response headers after fully writing the request headers, if the request has an “Expect: 100-continue” header. This time does not include the time to send the request header. The HTTP client sends its payload after this timeout is exhausted.

Default 1 second.

Set to **0** for no timeout and send request payload without waiting. One use case is when you run into issues with proxies or third party services that take a session similar to the use of Amazon S3 in the function shown later.

See [https://golang.org/pkg/net/http/#Transport.ExpectContinueTimeout](https://golang.org/pkg/net/http/#Transport.ExpectContinueTimeout)

We’ll call this `ExpectContinue` as **time.Duration**.

## Transport.IdleConnTimeout

This setting represents the maximum amount of time to keep an idle network connection alive between HTTP requests.

Set to **0** for no limit.

See [https://golang.org/pkg/net/http/#Transport.IdleConnTimeout](https://golang.org/pkg/net/http/#Transport.IdleConnTimeout)

We’ll call this `IdleConn` as **time.Duration**.

## Transport.MaxIdleConns

This setting represents the maximum number of idle (keep-alive) connections across all hosts. One use case for increasing this value is when you are seeing many connections in a short period from the same clients

**0** means no limit.

See [https://golang.org/pkg/net/http/#Transport.MaxIdleConns](https://golang.org/pkg/net/http/#Transport.MaxIdleConns)

We’ll call this `MaxAllIdleConns` as **int**.

## Transport.MaxIdleConnsPerHost

This setting represents the maximum number of idle (keep-alive) connections to keep per-host. One use case for increasing this value is when you are seeing many connections in a short period from the same clients

Default is two idle connections per host.

Set to **0** to use DefaultMaxIdleConnsPerHost (2).

See [https://golang.org/pkg/net/http/#Transport.MaxIdleConnsPerHost](https://golang.org/pkg/net/http/#Transport.MaxIdleConnsPerHost)

We’ll call this `MaxHostIdleConns` as **int**.

## Transport.ResponseHeaderTimeout

This setting represents the maximum amount of time to wait for a client to read the response header.

If the client isn’t able to read the response’s header within this duration, the request fails with a timeout error.

Be careful setting this value when using long-running Lambda functions, as the operation does not return any response headers until the Lambda function has finished or timed out. However, you can still use this option with the **InvokeAsync** API operation.

Default is no timeout; wait forever.

See [https://golang.org/pkg/net/http/#Transport.ResponseHeaderTimeout](https://golang.org/pkg/net/http/#Transport.ResponseHeaderTimeout)

We’ll call this `ResponseHeader` as **time.Duration**.

## Transport.TLSHandshakeTimeout

This setting represents the maximum amount of time waiting for a TLS handshake to be completed.

Default is 10 seconds.

Zero means no timeout.

See [https://golang.org/pkg/net/http/#Transport.TLSHandshakeTimeout](https://golang.org/pkg/net/http/#Transport.TLSHandshakeTimeout)

We’ll call this `TLSHandshake` as **time.Duration**.

## Create Import Statement

The complete example imports the following Go packages.
    
    
    import (
        "bytes"
        "context"
        "flag"
        "fmt"
        "io"
        "net"
        "net/http"
        "time"
    
        "github.com/aws/aws-sdk-go/aws"
        "github.com/aws/aws-sdk-go/aws/session"
        "github.com/aws/aws-sdk-go/service/s3"
    
        "golang.org/x/net/http2"
    )
    
    

## Creating a Timeout Struct

Let’s create a struct to hold the timeout values we want to be able to set on our HTTP client.
    
    
    type HTTPClientSettings struct {
        Connect          time.Duration
        ConnKeepAlive    time.Duration
        ExpectContinue   time.Duration
        IdleConn         time.Duration
        MaxAllIdleConns  int
        MaxHostIdleConns int
        ResponseHeader   time.Duration
        TLSHandshake     time.Duration
    }
    
    

## Creating a Function to Create a Custom HTTP Client

Next let’s create a function that takes a **ClientTimeout** struct and creates a custom HTTP client based on those timeout values.
    
    
    func NewHTTPClientWithSettings(httpSettings HTTPClientSettings) (*http.Client, error) {
        var client http.Client
        tr := &http.Transport{
            ResponseHeaderTimeout: httpSettings.ResponseHeader,
            Proxy:                 http.ProxyFromEnvironment,
            DialContext: (&net.Dialer{
                KeepAlive: httpSettings.ConnKeepAlive,
                DualStack: true,
                Timeout:   httpSettings.Connect,
            }).DialContext,
            MaxIdleConns:          httpSettings.MaxAllIdleConns,
            IdleConnTimeout:       httpSettings.IdleConn,
            TLSHandshakeTimeout:   httpSettings.TLSHandshake,
            MaxIdleConnsPerHost:   httpSettings.MaxHostIdleConns,
            ExpectContinueTimeout: httpSettings.ExpectContinue,
        }
    
        // So client makes HTTP/2 requests
        err := http2.ConfigureTransport(tr)
        if err != nil {
            return &client, err
        }
    
        return &http.Client{
            Transport: tr,
        }, nil
    }
    
    

## Using a Custom HTTP Client

Let’s create a custom HTTP client and use it to create an Amazon S3 client.

The following example creates an **http.Client** that is configured to have:

  * a five second TCP connection timeout

  * a five second TLS handshake timeout

  * a five second wait for the HTTP response headers



    
    
    httpClient, err := NewHTTPClientWithSettings(HTTPClientSettings{
        Connect:          5 * time.Second,
        ExpectContinue:   1 * time.Second,
        IdleConn:         90 * time.Second,
        ConnKeepAlive:    30 * time.Second,
        MaxAllIdleConns:  100,
        MaxHostIdleConns: 10,
        ResponseHeader:   5 * time.Second,
        TLSHandshake:     5 * time.Second,
    })
    if err != nil {
        fmt.Println("Got an error creating custom HTTP client:")
        fmt.Println(err)
        return
    }
    
    sess := session.Must(session.NewSession(&aws.Config{
        HTTPClient: httpClient,
    }))
    
    svc := s3.New(sess)
    

All of these settings give the client approximately 15 seconds create a connection, do a TLS handshake, and receive the response headers from the service. The time that the client takes to read the response body is not covered by these timeouts. To specify a total timeout for the request to include reading the response body, use the AWS SDK for Go client’s **WithContext** API operation methods, such as the Amazon S3 operation [PutObjectWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/#S3.PutObjectWithContext) with a **context.Withtimeout**.

The following example uses a timeout context to limit the total time an API request can be active to a maximum of 20 seconds. The SDK must be able to read the full HTTP response body (Object body) within the timeout or the SDK returns a timeout error. For API operations that return an **io.ReadCloser** in their response type, the Context’s timeout includes reading the content from the **io.ReadCloser**.
    
    
    ctx, cancelFn := context.WithTimeout(context.TODO(), 20*time.Second)
    defer cancelFn()
    
    resp, err := svc.GetObjectWithContext(ctx, &s3.GetObjectInput{
        Bucket: bucket,
        Key:    object,
    })
    if err != nil {
        return body, err
    }
    
    return resp.Body, nil
    

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/s3/CustomClient/CustomHttpClient.go) on GitHub.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Configuring the SDK

Using Sessions

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

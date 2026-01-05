# Source: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/tls.html

[](/pdfs/sdk-for-go/v1/developer-guide/aws-sdk-go-dg.pdf#tls "Open PDF")

[Documentation](/index.html)[AWS SDK for Go](/sdk-for-go/index.html)[Developer Guide](welcome.html)

How do I set my TLS version?

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Enforcing a minimum TLS version in the AWS SDK for Go

To add increased security when communicating with AWS services, you should configure your client to use TLS 1.2 or later.

###### Note

As of [Go 1.18](https://go.dev/doc/go1.18#tls10), the TLS configuration used by the `net/http#Client` defaults to TLS 1.2 as a minimum, and disables support for TLS 1.0 and TLS 1.1.

## How do I set my TLS version?

You can set the TLS version to 1.2 using the following code.

  1. Create a custom HTTP transport to require a minimum version of TLS 1.2
         
         tr := &http.Transport{
             TLSClientConfig: &tls.Config{
                 MinVersion: tls.VersionTLS12,
             },
         }

  2. Configure the transport.
         
         // In Go versions earlier than 1.13
         err := http2.ConfigureTransport(tr)
         if err != nil {
             fmt.Println("Got an error configuring HTTP transport")
             fmt.Println(err)
             return
         }
         
         // In Go versions later than 1.13
         tr.ForceAttemptHTTP2 = true

  3. Create an HTTP client with the configured transport, and use that to create a session. REGION is the AWS Region, such as _us-west-2_.
         
         client := http.Client{Transport: tr}
         
         sess := session.Must(session.NewSession(&aws.Config{
             Region:     &REGION,
             HTTPClient: &client,
         }))

  4. Use the following function to confirm your TLS version.
         
         func GetTLSVersion(tr *http.Transport) string {
             switch tr.TLSClientConfig.MinVersion {
             case tls.VersionTLS10:
                 return "TLS 1.0"
             case tls.VersionTLS11:
                 return "TLS 1.1"
             case tls.VersionTLS12:
                 return "TLS 1.2"
             case tls.VersionTLS13:
                 return "TLS 1.3"
             }
         
             return "Unknown"
         }

  5. Confirm your TLS version by calling _GetTLSVersion_.
         
         if tr, ok := sess.Config.HTTPClient.Transport.(*http.Transport); ok {
             log.Printf("Client uses %v", GetTLSVersion(tr))
         }




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Infrastructure Security

S3 Encryption Client Migration

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

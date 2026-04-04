# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-cloudfront.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#sdk-utilities-cloudfront "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Amazon CloudFront URL Signer

# Amazon CloudFront Utilities

## Amazon CloudFront URL Signer

The Amazon CloudFront URL signer simplifies the process of creating signed URLs. A signed URL includes information, such as an expiration date and time, that enables you to control access to your content. Signed URLs are useful when you want to distribute content through the internet, but want to restrict access to certain users (for example, to users who have paid a fee). 

To sign a URL, create a `URLSigner` instance with your CloudFront key pair ID and the associated private key. Then call the `Sign` or `SignWithPolicy` method and include the URL to sign. For more information about Amazon CloudFront key pairs, see [Creating CloudFront Key Pairs for Your Trusted Signers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html#private-content-creating-cloudfront-key-pairs) in the CloudFront Developer Guide. 

The following example creates a signed URL that's valid for one hour after it is created. 
    
    
    import "github.com/aws/aws-sdk-go-v2/feature/cloudfront/sign"
    
    // ...
    
    signer := sign.NewURLSigner(keyID, privKey)
    
    signedURL, err := signer.Sign(rawURL, time.Now().Add(1*time.Hour))
    if err != nil {
        log.Fatalf("Failed to sign url, err: %s\n", err.Error())
        return
    }
    

For more information about the signing utility, see the [sign](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/cloudfront/sign) package in the AWS SDK for Go API Reference. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon RDS Utilities

Amazon EC2 Instance Metadata Service

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

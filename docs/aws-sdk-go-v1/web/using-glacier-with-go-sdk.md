# Source: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-glacier-with-go-sdk.html

[](/pdfs/sdk-for-go/v1/developer-guide/aws-sdk-go-dg.pdf#using-glacier-with-go-sdk "Open PDF")

[Documentation](/index.html)[AWS SDK for Go](/sdk-for-go/index.html)[Developer Guide](welcome.html)

The ScenarioPrerequisitesCreate a VaultUpload an Archive

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Amazon Glacier Examples Using the AWS SDK for Go

Amazon Glacier is a secure, durable, and extremely low-cost cloud storage service for data archiving and long-term backup. The AWS SDK for Go examples can integrate Amazon Glacier into your applications. The examples assume you have already set up and configured the SDK (that is, you’ve imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](./setting-up.html) and [Configuring the AWS SDK for Go](./configuring-sdk.html).

You can download complete versions of these example files from the [aws-doc-sdk-examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/go/example_code/glacier) repository on GitHub.

## The Scenario

Amazon Glacier is a secure cloud storage service for data archiving and long-term backup. The service is optimized for infrequently accessed data where a retrieval time of several hours is suitable. These examples show you how to create a vault and upload an archive with Go. The methods used include:

  * [CreateVault](https://docs.aws.amazon.com/sdk-for-go/api/service/glacier/#Glacier.CreateVault)

  * [UploadArchive](https://docs.aws.amazon.com/sdk-for-go/api/service/glacier/#Glacier.UploadArchive)




## Prerequisites

  * You have [set up](./setting-up.html) and [configured](./configuring-sdk.html) the AWS SDK for Go.

  * You are familiar with the Amazon Glacier data model. To learn more, see [Amazon Glacier Data Model](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-data-model.html) in the Amazon Glacier Developer Guide.




## Create a Vault

The following example uses the Amazon Glacier[CreateVault](https://docs.aws.amazon.com/sdk-for-go/api/service/glacier/#Glacier.CreateVault) operation to create a vault named `YOUR_VAULT_NAME`.
    
    
    import (
        "log"
    
        "github.com/aws/aws-sdk-go/aws"
        "github.com/aws/aws-sdk-go/aws/session"
        "github.com/aws/aws-sdk-go/service/glacier"
    )
    
    func main() {
        // Initialize a session that the SDK uses to load
        // credentials from the shared credentials file ~/.aws/credentials
        // and configuration from the shared configuration file ~/.aws/config.
        sess := session.Must(session.NewSessionWithOptions(session.Options{
            SharedConfigState: session.SharedConfigEnable,
        }))
    
        // Create Glacier client in default region
        svc := glacier.New(sess)
    
        // start snippet
        _, err := svc.CreateVault(&glacier.CreateVaultInput{
            VaultName: aws.String("YOUR_VAULT_NAME"),
        })
        if err != nil {
            log.Println(err)
            return
        }
    
        log.Println("Created vault!")
        // end snippet
    }
    

## Upload an Archive

The following example assumes you have a vault named `YOUR_VAULT_NAME`. It uses the Amazon Glacier[UploadArchive](https://docs.aws.amazon.com/sdk-for-go/api/service/glacier/#Glacier.UploadArchive) operation to upload a single reader object as an entire archive. The AWS SDK for Go automatically computes the tree hash checksum for the data to be uploaded.
    
    
    import (
        "bytes"
        "log"
    
        "github.com/aws/aws-sdk-go/aws/session"
        "github.com/aws/aws-sdk-go/service/glacier"
    )
    
    func main() {
        // Initialize a session that the SDK uses to load
        // credentials from the shared credentials file ~/.aws/credentials
        // and configuration from the shared configuration file ~/.aws/config.
        sess := session.Must(session.NewSessionWithOptions(session.Options{
            SharedConfigState: session.SharedConfigEnable,
        }))
    
        // Create Glacier client in default region
        svc := glacier.New(sess)
    
        // start snippet
        vaultName := "YOUR_VAULT_NAME"
    
        result, err := svc.UploadArchive(&glacier.UploadArchiveInput{
            VaultName: &vaultName,
            Body:      bytes.NewReader(make([]byte, 2*1024*1024)), // 2 MB buffer
        })
        if err != nil {
            log.Println("Error uploading archive.", err)
            return
        }
    
        log.Println("Uploaded to archive", *result.ArchiveId)
        // end snippet
    }
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Using Elastic IP Addresses in Amazon EC2

IAM Examples

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

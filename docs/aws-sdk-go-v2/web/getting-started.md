# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/getting-started.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#getting-started "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Get an Amazon AccountInstall the AWS SDK for Go v2Get your AWS access keysInvoke an Operation

# Get started with AWS SDK for Go

The AWS SDK for Go requires a minimum version of Go 1.23. You can view your current version of Go by running the following command: 
    
    
    go version

For information about installing or upgrading your version of Go, see [Download and install](https://go.dev/doc/install) in the Go documentation. 

## Get an Amazon Account

Before you can use the AWS SDK for Go v2, you must have an Amazon account. See [Create an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) for details. 

## Install the AWS SDK for Go v2

The AWS SDK for Go v2 uses Go modules, which was a feature introduced in Go 1.11. Initialize your local project by running the following Go command. 
    
    
    go mod init example

After initializing your Go module project, you will be able to retrieve the SDK and its required dependencies using the `go get` command. These dependencies will be recorded in the `go.mod` file which was created by the previous command. 

The following commands show how to retrieve the standard set of SDK modules to use in your application. 
    
    
    go get github.com/aws/aws-sdk-go-v2
    go get github.com/aws/aws-sdk-go-v2/config
    

This will retrieve the core SDK module, and the config module which is used for loading the AWS shared configuration. 

Next you can install one or more AWS service API clients required by your application. All API clients are located under `github.com/aws/aws-sdk-go-v2/service` import hierarchy. A complete set of currently supported API clients can be found [here](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service). To install a service client, execute the following command to retrieve the module and record the dependency in your `go.mod` file. In this example we retrieve the Amazon S3 API client. 
    
    
    go get github.com/aws/aws-sdk-go-v2/service/s3

## Get your AWS access keys

Access keys consist of an access key ID and secret access key, which are used to sign programmatic requests that you make to AWS. If you don’t have access keys, you can create them by using the [AWS Management Console](https://console.aws.amazon.com/console/home). We recommend that you use IAM access keys instead of AWS root account access keys. IAM lets you securely control access to AWS services and resources in your AWS account. 

###### Note

To create access keys, you must have permissions to perform the required IAM actions. For more information, see [Permissions required to access IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions-required.html) in the IAM User Guide. 

### To get your access key ID and secret access key.

  1. Open the [IAM console](https://console.aws.amazon.com/iam/home). 

  2. On the navigation menu, choose **Users**. 

  3. Choose your IAM user name (not the check box). 

  4. Open the **Security credentials** tab, and then choose **Create access key**. 

  5. To see the new access key, choose **Show**. Your credentials resemble the following: 

     * Access key ID: `AKIAIOSFODNN7EXAMPLE`

     * Secret access key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

  6. To download the key pair, choose **Download .csv file**. Store the keys in a secure location. 




###### Warning

Keep the keys confidential to protect your AWS account, and never share them with anyone outside your organization. 

### Related topics

  * [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in IAM User Guide. 

  * [AWS Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in Amazon Web Services General Reference. 




## Invoke an Operation

After you have installed the SDK, you import AWS packages into your Go applications to use the SDK, as shown in the following example, which imports the AWS, Config, and Amazon S3 libraries. After importing the SDK packages, the AWS SDK Shared Configuration is loaded, a client is constructed, and an API operation is invoked. 
    
    
    package main
    
    import (
        "context"
        "log"
        "github.com/aws/aws-sdk-go-v2/aws"
        "github.com/aws/aws-sdk-go-v2/config"
        "github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    func main() {
        // Load the Shared AWS Configuration (~/.aws/config)
        cfg, err := config.LoadDefaultConfig(context.TODO())
        if err != nil {
            log.Fatal(err)
        }
    
        // Create an Amazon S3 service client
        client := s3.NewFromConfig(cfg)
    
        // Get the first page of results for ListObjectsV2 for a bucket
        output, err := client.ListObjectsV2(context.TODO(), &s3.ListObjectsV2Input{
            Bucket: aws.String("amzn-s3-demo-bucket"),
        })
        if err != nil {
            log.Fatal(err)
        }
    
        log.Println("first page results")
        for _, object := range output.Contents {
            log.Printf("key=%s size=%d", aws.ToString(object.Key), *object.Size)
        }
    }
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

What is the AWS SDK for Go v2?

Configure the SDK

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

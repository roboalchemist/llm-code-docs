# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-rds.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#sdk-utilities-rds "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

IAM Authentication

# Amazon RDS Utilities

## IAM Authentication

The [auth](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/rds/auth) package provides utilities for generating authentication tokens for connecting to Amazon RDS MySQL and PostgreSQL database instances. Using the [BuildAuthToken](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/rds/auth#BuildAuthToken) method, you generate a database authorization token by providing the database endpoint, AWS Region, username, and a [aws.CredentialProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#CredentialsProvider) implementation that returns IAM credentials with permission to connect to the database using IAM database authentication. To learn more about configuring Amazon RDS with IAM authentication, see the following Amazon RDS Developer Guide resources: 

  * [Enabling and disabling IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html)

  * [Creating and using an IAM policy for IAM database access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.html)

  * [Creating a database account using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html)




The following example shows how to generate an authentication token to connect to an Amazon RDS database: 
    
    
    import "context"
    import "github.com/aws/aws-sdk-go-v2/config"
    import "github.com/aws/aws-sdk-go-v2/feature/rds/auth"
    
    // ...
    
    cfg, err := config.LoadDefaultConfig(context.TODO())
    if err != nil {
        panic("configuration error: " + err.Error())
    }
    
    authenticationToken, err := auth.BuildAuthToken(
        context.TODO(),
        "mydb.123456789012.us-east-1.rds.amazonaws.com:3306", // Database Endpoint (With Port)
        "us-east-1", // AWS Region
        "jane_doe", // Database Account
        cfg.Credentials,
    )
    if err != nil {
        panic("failed to create authentication token: " + err.Error())
    }
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

SDK Utilities

Amazon CloudFront Utilities

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

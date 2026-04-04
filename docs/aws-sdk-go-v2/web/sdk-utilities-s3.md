# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-s3.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#sdk-utilities-s3 "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Amazon S3 Transfer ManagersUnseekable Streaming Input

# Amazon S3 Utilities

## Amazon S3 Transfer Managers

The Amazon S3 upload and download managers can break up large objects, so they can be transferred in multiple parts, in parallel. This makes it easy to resume interrupted transfers. 

### Amazon S3 Upload Manager

The Amazon S3 upload manager determines if a file can be split into smaller parts and uploaded in parallel. You can customize the number of parallel uploads and the size of the uploaded parts. 

The following example uses the Amazon S3 `Uploader` to upload a file. Using `Uploader` is similar to the `s3.PutObject()` operation. 
    
    
    import "context"
    import "github.com/aws/aws-sdk-go-v2/config"
    import "github.com/aws/aws-sdk-go-v2/service/s3"
    import "github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    
    // ...
    
    cfg, err := config.LoadDefaultConfig(context.TODO())
    if err != nil {
        log.Printf("error: %v", err)
        return
    }
    
    client := s3.NewFromConfig(cfg)
    
    uploader := manager.NewUploader(client)
    result, err := uploader.Upload(context.TODO(), &s3.PutObjectInput{
        Bucket: aws.String("amzn-s3-demo-bucket"),
        Key:    aws.String("my-object-key"),
        Body:   uploadFile,
    })
    

#### Configuration Options

When you instantiate an `Uploader` instance using [NewUploader](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#NewUploader), you can specify several configuration options to customize how objects are uploaded. Options are overridden by providing one or more arguments to `NewUploader`. These options include: 

  * `PartSize` – Specifies the buffer size, in bytes, of each part to upload. The minimum size per part is 5 MiB. 

  * `Concurrency` – Specifies the number of parts to upload in parallel. 

  * `LeavePartsOnError` – Indicates whether to leave successfully uploaded parts in Amazon S3. 




The `Concurrency` value limits the concurrent number of part uploads that can occur for a given `Upload` call. This is not a global client concurrency limit. Tweak the `PartSize` and `Concurrency` configuration values to find the optimal configuration. For example, systems with high-bandwidth connections can send bigger parts and more uploads in parallel. 

For example, your application configures `Uploader` with a `Concurrency` of setting of `5`. If your application then calls `Upload` from two different goroutines, the result is `10` concurrent part uploads (2 goroutines * 5 `Concurrency`). 

###### Warning

Your application is expected to limit the concurrent calls to `Upload` to prevent application resource exhaustion. 

Below is an example to set the default part size during `Uploader` creation: 
    
    
    uploader := manager.NewUploader(client, func(u *Uploader) {
        u.PartSize = 10 * 1024 * 1024, // 10 MiB
    })
    

For more information about `Uploader` and its configurations, see [Uploader](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#Uploader) in the AWS SDK for Go API Reference. 

#### PutObjectInput Body Field (io.ReadSeeker vs. io.Reader)

The `Body` field of the `s3.PutObjectInput` struct is an `io.Reader` type. However, this field can be populated with a type that satisfies both the `io.ReadSeeker` and `io.ReaderAt` interface to improve application resource utilization of the host environment. The following example creates the type `ReadSeekerAt` that satisfies both interfaces: 
    
    
    type ReadSeekerAt interface {
        io.ReadSeeker
        io.ReaderAt
    }
    

For `io.Reader` types, the bytes of the reader must be buffered in memory before the part can be uploaded. When you increase the `PartSize` or `Concurrency` value, the required memory (RAM) for the `Uploader` increases significantly. The required memory is approximately _`PartSize`_ * _`Concurrency`_. For example, specifying 100 MB for `PartSize` and 10 for `Concurrency`, requires at least 1 GB. 

Because an `io.Reader` type cannot determine its size before reading its bytes, `Uploader` cannot calculate how many parts will be uploaded. Consequently, `Uploader` can reach the Amazon S3 upload limit of 10,000 parts for large files if you set the `PartSize` too low. If you try to upload more than 10,000 parts, the upload stops and returns an error. 

For `body` values that implement the `ReadSeekerAt` type, the `Uploader` doesn't buffer the body contents in memory before sending it to Amazon S3. `Uploader` calculates the expected number of parts before uploading the file to Amazon S3. If the current value of `PartSize` requires more than 10,000 parts to upload the file, `Uploader` increases the part size value so that fewer parts are required. 

#### Handling Failed Uploads

If an upload to Amazon S3 fails, by default, `Uploader` uses the Amazon S3 `AbortMultipartUpload` operation to remove the uploaded parts. This functionality ensures that failed uploads do not consume Amazon S3 storage. 

You can set `LeavePartsOnError` to true so that the `Uploader` doesn't delete successfully uploaded parts. This is useful for resuming partially completed uploads. To operate on uploaded parts, you must get the `UploadID` of the failed upload. The following example demonstrates how to use the `manager.MultiUploadFailure` error interface type to get the `UploadID`. 
    
    
    result, err := uploader.Upload(context.TODO(), &s3.PutObjectInput{
        Bucket: aws.String("amzn-s3-demo-bucket"),
        Key:    aws.String("my-object-key"),
        Body:   uploadFile,
    })
    output, err := u.upload(input)
    if err != nil {
        var mu manager.MultiUploadFailure
        if errors.As(err, &mu) {
            // Process error and its associated uploadID
            fmt.Println("Error:", mu)
            _ = mu.UploadID() // retrieve the associated UploadID
        } else {
            // Process error generically
            fmt.Println("Error:", err.Error())
        }
        return
    }
    

#### Overriding Uploader Options Per Upload

You can override the `Uploader` options when calling `Upload` by providing one or more arguments to the method. These overrides are concurrency-safe modifications and do not affect ongoing uploads, or subsequent `Upload` calls to the manager. For example, to override the `PartSize` configuration for a specific upload request: 
    
    
    params := &s3.PutObjectInput{
        Bucket: aws.String("amzn-s3-demo-bucket"),
        Key:    aws.String("my-key"),
        Body:   myBody,
    }
    resp, err := uploader.Upload(context.TODO(), params, func(u *manager.Uploader) {
        u.PartSize = 10 * 1024 * 1024, // 10 MiB
    })
    

#### Examples

##### Upload a Folder to Amazon S3

The following example uses the `path/filepath` package to recursively gather a list of files and upload them to the specified Amazon S3 bucket. The keys of the Amazon S3 objects are prefixed with the file's relative path. 
    
    
    package main
    
    import (
        "context"
        "log"
        "os"
        "path/filepath"
    
        "github.com/aws/aws-sdk-go-v2/aws"
        "github.com/aws/aws-sdk-go-v2/config"
        "github.com/aws/aws-sdk-go-v2/feature/s3/manager"
        "github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    var (
        localPath string
        bucket    string
        prefix    string
    )
    
    func init() {
        if len(os.Args) != 4 {
            log.Fatalln("Usage:", os.Args[0], "<local path> <bucket> <prefix>")
        }
        localPath = os.Args[1]
        bucket = os.Args[2]
        prefix = os.Args[3]
    }
    
    func main() {
        walker := make(fileWalk)
        go func() {
            // Gather the files to upload by walking the path recursively 
            if err := filepath.Walk(localPath, walker.Walk); err != nil {
                log.Fatalln("Walk failed:", err)
            }
            close(walker)
        }()
    
        cfg, err := config.LoadDefaultConfig(context.TODO())
        if err != nil {
            log.Fatalln("error:", err)
        }
        
        // For each file found walking, upload it to Amazon S3
        uploader := manager.NewUploader(s3.NewFromConfig(cfg))
        for path := range walker {
            rel, err := filepath.Rel(localPath, path)
            if err != nil {
                log.Fatalln("Unable to get relative path:", path, err)
            }
            file, err := os.Open(path)
            if err != nil {
                log.Println("Failed opening file", path, err)
                continue
            }
            defer file.Close()
            result, err := uploader.Upload(context.TODO(), &s3.PutObjectInput{
                Bucket: &bucket,
                Key:    aws.String(filepath.Join(prefix, rel)),
                Body:   file,
            })
            if err != nil {
                log.Fatalln("Failed to upload", path, err)
            }
            log.Println("Uploaded", path, result.Location)
        }
    }
    
    type fileWalk chan string
    
    func (f fileWalk) Walk(path string, info os.FileInfo, err error) error {
        if err != nil {
            return err
        }
        if !info.IsDir() {
            f <- path
        }
        return nil
    }
    

### Download Manager

The Amazon S3 [Downloader](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#Downloader) manager determines if a file can be split into smaller parts and downloaded in parallel. You can customize the number of parallel downloads and the size of the downloaded parts. 

#### Example: Download a File

The following example uses the Amazon S3 `Downloader` to download a file. Using `Downloader` is similar to the [s3.GetObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObject) operation. 
    
    
    import "context"
    import "github.com/aws/aws-sdk-go-v2/aws"
    import "github.com/aws/aws-sdk-go-v2/config"
    import "github.com/aws/aws-sdk-go-v2/service/s3"
    import "github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    
    // ...
    
    cfg, err := config.LoadDefaultConfig(context.TODO())
    if err != nil {
        log.Println("error:", err)
        return
    }
    
    client := s3.NewFromConfig(cfg)
    
    downloader := manager.NewDownloader(client)
    numBytes, err := downloader.Download(context.TODO(), downloadFile, &s3.GetObjectInput{
        Bucket: aws.String("amzn-s3-demo-bucket"), 
        Key:    aws.String("my-key"),
    })
    

The `downloadFile` parameter is an `io.WriterAt` type. The `WriterAt` interface enables the `Downloader` to write multiple parts of the file in parallel. 

#### Configuration Options

When you instantiate a `Downloader` instance, you can specify configuration options to customize how objects are downloaded: 

  * `PartSize` – Specifies the buffer size, in bytes, of each part to download. The minimum size per part is 5 MB. 

  * `Concurrency` – Specifies the number of parts to download in parallel. 




The `Concurrency` value limits the concurrent number of part download that can occur for a given `Download` call. This is not a global client concurrency limit. Tweak the `PartSize` and `Concurrency` configuration values to find the optimal configuration. For example, systems with high-bandwidth connections can receive bigger parts and more downloads in parallel. 

For example, your application configures `Downloader` with a `Concurrency` of `5`. Your application then calls `Download` from two different goroutines, the result will be `10` concurrent part downloads (2 goroutines * 5 `Concurrency`). 

###### Warning

Your application is expected to limit the concurrent calls to `Download` to prevent application resource exhaustion. 

For more information about `Downloader` and its other configuration options, see [manager.Downloader](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager/#Downloader) in the AWS SDK for Go API Reference. 

#### Overriding Downloader Options Per Download

You can override the `Downloader` options when calling `Download` by providing one or more functional arguments to the method. These overrides are concurrency safe modifications and do not affect ongoing uploads, or subsequent `Download` calls to the manager. For example, to override the `PartSize` configuration for a specific upload request: 
    
    
    params := &s3.GetObjectInput{
        Bucket: aws.String("amzn-s3-demo-bucket"),
        Key:    aws.String("my-key"),
    }
    resp, err := downloader.Download(context.TODO(), targetWriter, params, func(u *manager.Downloader) {
        u.PartSize = 10 * 1024 * 1024, // 10 MiB
    })
    

##### Examples

##### Download All Objects in a Bucket

The following example uses pagination to gather a list of objects from an Amazon S3 bucket. Then it downloads each object to a local file. 
    
    
    package main
    
    import (
        "context"
        "fmt"
        "log"
        "os"
        "path/filepath"
    
        "github.com/aws/aws-sdk-go-v2/aws"
        "github.com/aws/aws-sdk-go-v2/config"
        "github.com/aws/aws-sdk-go-v2/feature/s3/manager"
        "github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    var (
        Bucket         = "amzn-s3-demo-bucket" // Download from this bucket
        Prefix         = "logs/"    // Using this key prefix
        LocalDirectory = "s3logs"   // Into this directory
    )
    
    func main() {
        cfg, err := config.LoadDefaultConfig(context.TODO())
        if err != nil {
            log.Fatalln("error:", err)
        }
    
        client := s3.NewFromConfig(cfg)
        manager := manager.NewDownloader(client)
    
        paginator := s3.NewListObjectsV2Paginator(client, &s3.ListObjectsV2Input{
            Bucket: &Bucket,
            Prefix: &Prefix,
        })
    
        for paginator.HasMorePages() {
            page, err := paginator.NextPage(context.TODO())
            if err != nil {
                log.Fatalln("error:", err)
            }
            for _, obj := range page.Contents {
                if err := downloadToFile(manager, LocalDirectory, Bucket, aws.ToString(obj.Key)); err != nil {
                    log.Fatalln("error:", err)
                }
            }
        }
    }
    
    func downloadToFile(downloader *manager.Downloader, targetDirectory, bucket, key string) error {
        // Create the directories in the path
        file := filepath.Join(targetDirectory, key)
        if err := os.MkdirAll(filepath.Dir(file), 0775); err != nil {
            return err
        }
    
        // Set up the local file
        fd, err := os.Create(file)
        if err != nil {
            return err
        }
        defer fd.Close()
    
        // Download the file using the AWS SDK for Go
        fmt.Printf("Downloading s3://%s/%s to %s...\n", bucket, key, file)
        _, err = downloader.Download(context.TODO(), fd, &s3.GetObjectInput{Bucket: &bucket, Key: &key})
    
        return err
    }
    

### GetBucketRegion

[GetBucketRegion](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#GetBucketRegion) is a utility function for determining the AWS Region location of an Amazon S3 Bucket. `GetBucketRegion` takes an Amazon S3 client and uses it to determine the location of the requested Bucket within the AWS Partition associated with the client's configured Region. 

For example, to find the Region for the Bucket ``amzn-s3-demo-bucket``: 
    
    
    cfg, err := config.LoadDefaultConfig(context.TODO())
    if err != nil {
        log.Println("error:", err)
        return
    }
    
    bucket := "amzn-s3-demo-bucket"
    region, err := manager.GetBucketRegion(ctx, s3.NewFromConfig(cfg), bucket)
    if err != nil {
        var bnf manager.BucketNotFound
        if errors.As(err, &bnf) {
            log.Printf("unable to find bucket %s's Region\n", bucket)
        } else {
            log.Println("error:", err)
        }
        return
    }
    fmt.Printf("Bucket %s is in %s region\n", bucket, region)
    

If `GetBucketRegion` is not able to resolve the location of a Bucket, the function returns a [BucketNotFound](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#BucketNotFound) error type as shown in the example. 

## Unseekable Streaming Input

For API operations like `PutObject` and `UploadPart`, the Amazon S3 client expects the value of the `Body` input parameter to implement the [io.Seeker](https://pkg.go.dev/io#Seeker) interface by default. The `io.Seeker` interface is used by the client to determine the length of the value to upload, and to compute payload hash for the [request signature](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html). If the `Body` input parameter value does not implement `io.Seeker`, your application will receive an error. 
    
    
    operation error S3: PutObject, failed to compute payload hash: failed to seek
    body to start, request stream is not seekable
    

You can change this behavior by modifying the operation method's [Middleware](./middleware.html) using functional options. The [WithAPIOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#WithAPIOptions) helper returns a functional option for zero or more middleware mutators. To disable the client computing the payload hash and use [Unsigned Payload](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-header-based-auth.html) request signature add [v4.SwapComputePayloadSHA256ForUnsignedPayloadMiddleware](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws/signer/v4#SwapComputePayloadSHA256ForUnsignedPayloadMiddleware). 
    
    
    resp, err := client.PutObject(context.TODO(), &s3.PutObjectInput{
        Bucket: &bucketName,
        Key: &objectName,
        Body: bytes.NewBuffer([]byte(`example object!`)),
        ContentLength: 15, // length of body
    }, s3.WithAPIOptions(
        v4.SwapComputePayloadSHA256ForUnsignedPayloadMiddleware,
    ))
    

###### Warning

Amazon S3 requires the content length to be provided for all object's uploaded to a bucket. Since the `Body` input parameter does not implement `io.Seeker` interface, the client will not be able to compute the `ContentLength` parameter for the request. The parameter must be provided by the application. The request will fail if the `ContentLength` parameter is not provided. 

Use the SDK's Amazon S3 Upload Manager for uploads that are not seekable and do not have a known length. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon EC2 Instance Metadata Service

Middleware

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/s3-checksums.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#s3-checksums "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Upload an objectDownload an object

# Data integrity protection with checksums

Amazon Simple Storage Service (Amazon S3) provides the ability to specify a checksum when you upload an object. When you specify a checksum, it is stored with the object and can be validated when the object is downloaded.

Checksums provide an additional layer of data integrity when you transfer files. With checksums, you can verify data consistency by confirming that the received file matches the original file. For more information about checksums with Amazon S3, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) including the [supported algorithms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums).

You have the flexibility to choose the algorithm that best fits your needs and let the SDK calculate the checksum. Alternatively, you can provide a pre-computed checksum value by using one of the supported algorithms. 

###### Note

Beginning with version [v1.74.1 of the Amazon S3 module](https://github.com/aws/aws-sdk-go-v2/blob/v1.34.0/service/s3/CHANGELOG.md#v1741-2025-01-24), the SDK provides default integrity protections by automatically calculating a `CRC32` checksum for uploads. The SDK calculates this checksum if you don't provide a precalculated checksum value or if you don't specify an algorithm that the SDK should use to calculate a checksum.

The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html).

We discuss checksums in two request phases: uploading an object and downloading an object.

## Upload an object

When you upload an object with the `putObject` method and provide a checksum algorithm, the SDK computes the checksum for the specified algorithm.

The following code snippet shows a request to upload an object with a `CRC32` checksum. When the SDK sends the request, it calculates the `CRC32` checksum and uploads the object. Amazon S3 validates the integrity of the content by calculating the checksum and comparing it to the checksum provided by the SDK. Amazon S3 then stores the checksum with the object.
    
    
    out, err := s3Client.PutObject(context.Background(), &s3.PutObjectInput{
         Bucket:            aws.String("bucket"),
         Key:               aws.String("key"),
         ChecksumAlgorithm: types.ChecksumAlgorithmCrc32,
         Body:              strings.NewReader("Hello World"),
     })

If you don't provide a checksum algorithm with the request, the checksum behavior varies depending on the version of the SDK that you use as shown in the following table.

**Checksum behavior when no checksum algorithm is provided**

Amazon S3 module version of AWS SDK for Go | Checksum behavior  
---|---  
Earlier than v1.74.1 | The SDK doesn't automatically calculate a CRC-based checksum and provide it in the request.  
v1.74.1 or later |  The SDK uses the `CRC32` algorithm to calculate the checksum and provides it in the request. Amazon S3 validates the integrity of the transfer by computing its own `CRC32` checksum and compares it to the checksum provided by the SDK. If the checksums match, the checksum is saved with the object.   
  
### Use a pre-calculated checksum value

A pre-calculated checksum value provided with the request disables automatic computation by the SDK and uses the provided value instead.

The following example shows a request with a pre-calculated SHA256 checksum.
    
    
    out, err := s3Client.PutObject(context.Background(), &s3.PutObjectInput{
         Bucket:        aws.String("bucket"),
         Key:           aws.String("key"),
         ChecksumCRC32: aws.String("checksumvalue"),
         Body:          strings.NewReader("Hello World"),
     })

If Amazon S3 determines the checksum value is incorrect for the specified algorithm, the service returns an error response.

### Multipart uploads

You can also use checksums with multipart uploads.

The AWS SDK for Go provides two options to use checksums with multipart uploads. The first option uses the transfer manager that specifies the `CRC32` algorithm for the upload.
    
    
    s3Client := s3.NewFromConfig(cfg)
         transferManager := manager.NewUploader(s3Client)
         out, err := transferManager.Upload(context.Background(), &s3.PutObjectInput{
                 Bucket:            aws.String("bucket"),
                 Key:               aws.String("key"),
                 Body:              large file to trigger multipart upload,
                 ChecksumAlgorithm: types.ChecksumAlgorithmCrc32,
         })

If you don't provide a checksum algorithm when using the transfer manager for uploads, the SDK automatically calculates and checksum based on the `CRC32` algorithm. The SDK performs this calculation for all versions of the SDK.

The second option uses the [Amazon S3](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3) client to perform the multipart upload. If you specify a checksum with this approach, you must specify the algorithm to use on the initiation of the upload. You must also specify the algorithm for each part request and provide the checksum calculated for each part after it is uploaded.
    
    
    s3Client := s3.NewFromConfig(cfg)
         createMultipartUploadOutput, err := s3Client.CreateMultipartUpload(context.Background(), &s3.CreateMultipartUploadInput{
                 Bucket:            aws.String("bucket"),
                 Key:               aws.String("key"),
                 ChecksumAlgorithm: types.ChecksumAlgorithmCrc32,
              })
         if err != nil {
                 log.Fatal("err create multipart upload ", err)
         }
    
         var partsBody []io.Reader // this is just an example parts content, you should load your target file in your code
         partNum := int32(1)
         var completedParts []types.CompletedPart
         for _, body := range partsBody {
             uploadPartOutput, err := s3Client.UploadPart(context.Background(), &s3.UploadPartInput{
                 Bucket:            aws.String("bucket"),
                 Key:               aws.String("key"),
                 ChecksumAlgorithm: types.ChecksumAlgorithmCrc32,
                 Body:              body,
                 PartNumber:        aws.Int32(partNum),
                 UploadId:          createMultipartUploadOutput.UploadId,
             })
             if err != nil {
                 log.Fatal("err upload part ", err)
             }
    
             completedParts = append(completedParts, types.CompletedPart{
                 PartNumber:    aws.Int32(partNum),
                 ETag:          uploadPartOutput.ETag,
                 ChecksumCRC32: uploadPartOutput.ChecksumCRC32,
             })
             partNum++
         }
    
         completeMultipartUploadOutput, err := s3Client.CompleteMultipartUpload(context.Background(), &s3.CompleteMultipartUploadInput{
             Bucket:   aws.String("bucket"),
             Key:      aws.String("key"),
             UploadId: createMultipartUploadOutput.UploadId,
             MultipartUpload: &types.CompletedMultipartUpload{
                 Parts: completedParts,
             },
         })
         if err != nil {
             log.Fatal("err complete multipart upload ", err)
         }

## Download an object

When you use the [GetObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObject) method to download an object, the SDK automatically validates the checksum when the `ChecksumMode` field of `GetObjectInput` is set to `types.ChecksumModeEnabled`. 

The request in the following snippet directs the SDK to validate the checksum in the response by calculating the checksum and comparing the values.
    
    
    out, err := s3Client.GetObject(context.Background(), &s3.GetObjectInput{
         Bucket:       aws.String("bucket"),
         Key:          aws.String("key"),
         ChecksumMode: types.ChecksumModeEnabled,
     })

If the object wasn't uploaded with a checksum, no validation takes place.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Use AWS services

SDK Utilities

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

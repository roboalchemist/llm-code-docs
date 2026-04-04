# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_s3_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_s3_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

BasicsActionsScenariosServerless examples

# Amazon S3 examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon S3.

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Amazon S3.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"errors"
    	"fmt"
    
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/smithy-go"
    )
    
    // main uses the AWS SDK for Go V2 to create an Amazon Simple Storage Service
    // (Amazon S3) client and list up to 10 buckets in your account.
    // This example uses the default settings specified in your shared credentials
    // and config files.
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
    		fmt.Println(err)
    		return
    	}
    	s3Client := s3.NewFromConfig(sdkConfig)
    	count := 10
    	fmt.Printf("Let's list up to %v buckets for your account.\n", count)
    	result, err := s3Client.ListBuckets(ctx, &s3.ListBucketsInput{})
    	if err != nil {
    		var ae smithy.APIError
    		if errors.As(err, &ae) && ae.ErrorCode() == "AccessDenied" {
    			fmt.Println("You don't have permission to list buckets for this account.")
    		} else {
    			fmt.Printf("Couldn't list buckets for your account. Here's why: %v\n", err)
    		}
    		return
    	}
    	if len(result.Buckets) == 0 {
    		fmt.Println("You don't have any buckets!")
    	} else {
    		if count > len(result.Buckets) {
    			count = len(result.Buckets)
    		}
    		for _, bucket := range result.Buckets[:count] {
    			fmt.Printf("\t%v\n", *bucket.Name)
    		}
    	}
    }
    
    
    

  * For API details, see [ListBuckets](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListBuckets) in _AWS SDK for Go API Reference_. 




###### Topics

  * Basics

  * Actions

  * Scenarios

  * Serverless examples




## Basics

The following code example shows how to:

  * Create a bucket and upload a file to it.

  * Download an object from a bucket.

  * Copy an object to a subfolder in a bucket.

  * List the objects in a bucket.

  * Delete the bucket objects and the bucket.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 

Define a struct that wraps bucket and object actions used by the scenario.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // ListBuckets lists the buckets in the current account.
    func (basics BucketBasics) ListBuckets(ctx context.Context) ([]types.Bucket, error) {
    	var err error
    	var output *s3.ListBucketsOutput
    	var buckets []types.Bucket
    	bucketPaginator := s3.NewListBucketsPaginator(basics.S3Client, &s3.ListBucketsInput{})
    	for bucketPaginator.HasMorePages() {
    		output, err = bucketPaginator.NextPage(ctx)
    		if err != nil {
    			var apiErr smithy.APIError
    			if errors.As(err, &apiErr) && apiErr.ErrorCode() == "AccessDenied" {
    				fmt.Println("You don't have permission to list buckets for this account.")
    				err = apiErr
    			} else {
    				log.Printf("Couldn't list buckets for your account. Here's why: %v\n", err)
    			}
    			break
    		} else {
    			buckets = append(buckets, output.Buckets...)
    		}
    	}
    	return buckets, err
    }
    
    
    
    // BucketExists checks whether a bucket exists in the current account.
    func (basics BucketBasics) BucketExists(ctx context.Context, bucketName string) (bool, error) {
    	_, err := basics.S3Client.HeadBucket(ctx, &s3.HeadBucketInput{
    		Bucket: aws.String(bucketName),
    	})
    	exists := true
    	if err != nil {
    		var apiError smithy.APIError
    		if errors.As(err, &apiError) {
    			switch apiError.(type) {
    			case *types.NotFound:
    				log.Printf("Bucket %v is available.\n", bucketName)
    				exists = false
    				err = nil
    			default:
    				log.Printf("Either you don't have access to bucket %v or another error occurred. "+
    					"Here's what happened: %v\n", bucketName, err)
    			}
    		}
    	} else {
    		log.Printf("Bucket %v exists and you already own it.", bucketName)
    	}
    
    	return exists, err
    }
    
    
    
    // CreateBucket creates a bucket with the specified name in the specified Region.
    func (basics BucketBasics) CreateBucket(ctx context.Context, name string, region string) error {
    	_, err := basics.S3Client.CreateBucket(ctx, &s3.CreateBucketInput{
    		Bucket: aws.String(name),
    		CreateBucketConfiguration: &types.CreateBucketConfiguration{
    			LocationConstraint: types.BucketLocationConstraint(region),
    		},
    	})
    	if err != nil {
    		var owned *types.BucketAlreadyOwnedByYou
    		var exists *types.BucketAlreadyExists
    		if errors.As(err, &owned) {
    			log.Printf("You already own bucket %s.\n", name)
    			err = owned
    		} else if errors.As(err, &exists) {
    			log.Printf("Bucket %s already exists.\n", name)
    			err = exists
    		}
    	} else {
    		err = s3.NewBucketExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(name)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to exist.\n", name)
    		}
    	}
    	return err
    }
    
    
    
    // UploadFile reads from a file and puts the data into an object in a bucket.
    func (basics BucketBasics) UploadFile(ctx context.Context, bucketName string, objectKey string, fileName string) error {
    	file, err := os.Open(fileName)
    	if err != nil {
    		log.Printf("Couldn't open file %v to upload. Here's why: %v\n", fileName, err)
    	} else {
    		defer file.Close()
    		_, err = basics.S3Client.PutObject(ctx, &s3.PutObjectInput{
    			Bucket: aws.String(bucketName),
    			Key:    aws.String(objectKey),
    			Body:   file,
    		})
    		if err != nil {
    			var apiErr smithy.APIError
    			if errors.As(err, &apiErr) && apiErr.ErrorCode() == "EntityTooLarge" {
    				log.Printf("Error while uploading object to %s. The object is too large.\n"+
    					"To upload objects larger than 5GB, use the S3 console (160GB max)\n"+
    					"or the multipart upload API (5TB max).", bucketName)
    			} else {
    				log.Printf("Couldn't upload file %v to %v:%v. Here's why: %v\n",
    					fileName, bucketName, objectKey, err)
    			}
    		} else {
    			err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    				ctx, &s3.HeadObjectInput{Bucket: aws.String(bucketName), Key: aws.String(objectKey)}, time.Minute)
    			if err != nil {
    				log.Printf("Failed attempt to wait for object %s to exist.\n", objectKey)
    			}
    		}
    	}
    	return err
    }
    
    
    
    // UploadLargeObject uses an upload manager to upload data to an object in a bucket.
    // The upload manager breaks large data into parts and uploads the parts concurrently.
    func (basics BucketBasics) UploadLargeObject(ctx context.Context, bucketName string, objectKey string, largeObject []byte) error {
    	largeBuffer := bytes.NewReader(largeObject)
    	var partMiBs int64 = 10
    	uploader := manager.NewUploader(basics.S3Client, func(u *manager.Uploader) {
    		u.PartSize = partMiBs * 1024 * 1024
    	})
    	_, err := uploader.Upload(ctx, &s3.PutObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    		Body:   largeBuffer,
    	})
    	if err != nil {
    		var apiErr smithy.APIError
    		if errors.As(err, &apiErr) && apiErr.ErrorCode() == "EntityTooLarge" {
    			log.Printf("Error while uploading object to %s. The object is too large.\n"+
    				"The maximum size for a multipart upload is 5TB.", bucketName)
    		} else {
    			log.Printf("Couldn't upload large object to %v:%v. Here's why: %v\n",
    				bucketName, objectKey, err)
    		}
    	} else {
    		err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(bucketName), Key: aws.String(objectKey)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist.\n", objectKey)
    		}
    	}
    
    	return err
    }
    
    
    
    // DownloadFile gets an object from a bucket and stores it in a local file.
    func (basics BucketBasics) DownloadFile(ctx context.Context, bucketName string, objectKey string, fileName string) error {
    	result, err := basics.S3Client.GetObject(ctx, &s3.GetObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	})
    	if err != nil {
    		var noKey *types.NoSuchKey
    		if errors.As(err, &noKey) {
    			log.Printf("Can't get object %s from bucket %s. No such key exists.\n", objectKey, bucketName)
    			err = noKey
    		} else {
    			log.Printf("Couldn't get object %v:%v. Here's why: %v\n", bucketName, objectKey, err)
    		}
    		return err
    	}
    	defer result.Body.Close()
    	file, err := os.Create(fileName)
    	if err != nil {
    		log.Printf("Couldn't create file %v. Here's why: %v\n", fileName, err)
    		return err
    	}
    	defer file.Close()
    	body, err := io.ReadAll(result.Body)
    	if err != nil {
    		log.Printf("Couldn't read object body from %v. Here's why: %v\n", objectKey, err)
    	}
    	_, err = file.Write(body)
    	return err
    }
    
    
    
    // DownloadLargeObject uses a download manager to download an object from a bucket.
    // The download manager gets the data in parts and writes them to a buffer until all of
    // the data has been downloaded.
    func (basics BucketBasics) DownloadLargeObject(ctx context.Context, bucketName string, objectKey string) ([]byte, error) {
    	var partMiBs int64 = 10
    	downloader := manager.NewDownloader(basics.S3Client, func(d *manager.Downloader) {
    		d.PartSize = partMiBs * 1024 * 1024
    	})
    	buffer := manager.NewWriteAtBuffer([]byte{})
    	_, err := downloader.Download(ctx, buffer, &s3.GetObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	})
    	if err != nil {
    		log.Printf("Couldn't download large object from %v:%v. Here's why: %v\n",
    			bucketName, objectKey, err)
    	}
    	return buffer.Bytes(), err
    }
    
    
    
    // CopyToFolder copies an object in a bucket to a subfolder in the same bucket.
    func (basics BucketBasics) CopyToFolder(ctx context.Context, bucketName string, objectKey string, folderName string) error {
    	objectDest := fmt.Sprintf("%v/%v", folderName, objectKey)
    	_, err := basics.S3Client.CopyObject(ctx, &s3.CopyObjectInput{
    		Bucket:     aws.String(bucketName),
    		CopySource: aws.String(fmt.Sprintf("%v/%v", bucketName, objectKey)),
    		Key:        aws.String(objectDest),
    	})
    	if err != nil {
    		var notActive *types.ObjectNotInActiveTierError
    		if errors.As(err, &notActive) {
    			log.Printf("Couldn't copy object %s from %s because the object isn't in the active tier.\n",
    				objectKey, bucketName)
    			err = notActive
    		}
    	} else {
    		err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(bucketName), Key: aws.String(objectDest)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist.\n", objectDest)
    		}
    	}
    	return err
    }
    
    
    
    // CopyToBucket copies an object in a bucket to another bucket.
    func (basics BucketBasics) CopyToBucket(ctx context.Context, sourceBucket string, destinationBucket string, objectKey string) error {
    	_, err := basics.S3Client.CopyObject(ctx, &s3.CopyObjectInput{
    		Bucket:     aws.String(destinationBucket),
    		CopySource: aws.String(fmt.Sprintf("%v/%v", sourceBucket, objectKey)),
    		Key:        aws.String(objectKey),
    	})
    	if err != nil {
    		var notActive *types.ObjectNotInActiveTierError
    		if errors.As(err, &notActive) {
    			log.Printf("Couldn't copy object %s from %s because the object isn't in the active tier.\n",
    				objectKey, sourceBucket)
    			err = notActive
    		}
    	} else {
    		err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(destinationBucket), Key: aws.String(objectKey)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist.\n", objectKey)
    		}
    	}
    	return err
    }
    
    
    
    // ListObjects lists the objects in a bucket.
    func (basics BucketBasics) ListObjects(ctx context.Context, bucketName string) ([]types.Object, error) {
    	var err error
    	var output *s3.ListObjectsV2Output
    	input := &s3.ListObjectsV2Input{
    		Bucket: aws.String(bucketName),
    	}
    	var objects []types.Object
    	objectPaginator := s3.NewListObjectsV2Paginator(basics.S3Client, input)
    	for objectPaginator.HasMorePages() {
    		output, err = objectPaginator.NextPage(ctx)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucketName)
    				err = noBucket
    			}
    			break
    		} else {
    			objects = append(objects, output.Contents...)
    		}
    	}
    	return objects, err
    }
    
    
    
    // DeleteObjects deletes a list of objects from a bucket.
    func (basics BucketBasics) DeleteObjects(ctx context.Context, bucketName string, objectKeys []string) error {
    	var objectIds []types.ObjectIdentifier
    	for _, key := range objectKeys {
    		objectIds = append(objectIds, types.ObjectIdentifier{Key: aws.String(key)})
    	}
    	output, err := basics.S3Client.DeleteObjects(ctx, &s3.DeleteObjectsInput{
    		Bucket: aws.String(bucketName),
    		Delete: &types.Delete{Objects: objectIds, Quiet: aws.Bool(true)},
    	})
    	if err != nil || len(output.Errors) > 0 {
    		log.Printf("Error deleting objects from bucket %s.\n", bucketName)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucketName)
    				err = noBucket
    			}
    		} else if len(output.Errors) > 0 {
    			for _, outErr := range output.Errors {
    				log.Printf("%s: %s\n", *outErr.Key, *outErr.Message)
    			}
    			err = fmt.Errorf("%s", *output.Errors[0].Message)
    		}
    	} else {
    		for _, delObjs := range output.Deleted {
    			err = s3.NewObjectNotExistsWaiter(basics.S3Client).Wait(
    				ctx, &s3.HeadObjectInput{Bucket: aws.String(bucketName), Key: delObjs.Key}, time.Minute)
    			if err != nil {
    				log.Printf("Failed attempt to wait for object %s to be deleted.\n", *delObjs.Key)
    			} else {
    				log.Printf("Deleted %s.\n", *delObjs.Key)
    			}
    		}
    	}
    	return err
    }
    
    
    
    // DeleteBucket deletes a bucket. The bucket must be empty or an error is returned.
    func (basics BucketBasics) DeleteBucket(ctx context.Context, bucketName string) error {
    	_, err := basics.S3Client.DeleteBucket(ctx, &s3.DeleteBucketInput{
    		Bucket: aws.String(bucketName)})
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucketName)
    			err = noBucket
    		} else {
    			log.Printf("Couldn't delete bucket %v. Here's why: %v\n", bucketName, err)
    		}
    	} else {
    		err = s3.NewBucketNotExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(bucketName)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to be deleted.\n", bucketName)
    		} else {
    			log.Printf("Deleted %s.\n", bucketName)
    		}
    	}
    	return err
    }
    
    
    

Run an interactive scenario that shows you how to work with S3 buckets and objects.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/s3/actions"
    )
    
    // RunGetStartedScenario is an interactive example that shows you how to use Amazon
    // Simple Storage Service (Amazon S3) to create an S3 bucket and use it to store objects.
    //
    // 1. Create a bucket.
    // 2. Upload a local file to the bucket.
    // 3. Download an object to a local file.
    // 4. Copy an object to a different folder in the bucket.
    // 5. List objects in the bucket.
    // 6. Delete all objects in the bucket.
    // 7. Delete the bucket.
    //
    // This example creates an Amazon S3 service client from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // It uses a questioner from the `demotools` package to get input during the example.
    // This package can be found in the ..\..\demotools folder of this repo.
    func RunGetStartedScenario(ctx context.Context, sdkConfig aws.Config, questioner demotools.IQuestioner) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			_, isMock := questioner.(*demotools.MockQuestioner)
    			if isMock || questioner.AskBool("Do you want to see the full error message (y/n)?", "y") {
    				log.Println(r)
    			}
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon S3 getting started demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	s3Client := s3.NewFromConfig(sdkConfig)
    	bucketBasics := actions.BucketBasics{S3Client: s3Client}
    
    	count := 10
    	log.Printf("Let's list up to %v buckets for your account:", count)
    	buckets, err := bucketBasics.ListBuckets(ctx)
    	if err != nil {
    		panic(err)
    	}
    	if len(buckets) == 0 {
    		log.Println("You don't have any buckets!")
    	} else {
    		if count > len(buckets) {
    			count = len(buckets)
    		}
    		for _, bucket := range buckets[:count] {
    			log.Printf("\t%v\n", *bucket.Name)
    		}
    	}
    
    	bucketName := questioner.Ask("Let's create a bucket. Enter a name for your bucket:",
    		demotools.NotEmpty{})
    	bucketExists, err := bucketBasics.BucketExists(ctx, bucketName)
    	if err != nil {
    		panic(err)
    	}
    	if !bucketExists {
    		err = bucketBasics.CreateBucket(ctx, bucketName, sdkConfig.Region)
    		if err != nil {
    			panic(err)
    		} else {
    			log.Println("Bucket created.")
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	fmt.Println("Let's upload a file to your bucket.")
    	smallFile := questioner.Ask("Enter the path to a file you want to upload:",
    		demotools.NotEmpty{})
    	const smallKey = "doc-example-key"
    	err = bucketBasics.UploadFile(ctx, bucketName, smallKey, smallFile)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Uploaded %v as %v.\n", smallFile, smallKey)
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's download %v to a file.", smallKey)
    	downloadFileName := questioner.Ask("Enter a name for the downloaded file:", demotools.NotEmpty{})
    	err = bucketBasics.DownloadFile(ctx, bucketName, smallKey, downloadFileName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("File %v downloaded.", downloadFileName)
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's copy %v to a folder in the same bucket.", smallKey)
    	folderName := questioner.Ask("Enter a folder name: ", demotools.NotEmpty{})
    	err = bucketBasics.CopyToFolder(ctx, bucketName, smallKey, folderName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Copied %v to %v/%v.\n", smallKey, folderName, smallKey)
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Let's list the objects in your bucket.")
    	questioner.Ask("Press Enter when you're ready.")
    	objects, err := bucketBasics.ListObjects(ctx, bucketName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Found %v objects.\n", len(objects))
    	var objKeys []string
    	for _, object := range objects {
    		objKeys = append(objKeys, *object.Key)
    		log.Printf("\t%v\n", *object.Key)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	if questioner.AskBool("Do you want to delete your bucket and all of its "+
    		"contents? (y/n)", "y") {
    		log.Println("Deleting objects.")
    		err = bucketBasics.DeleteObjects(ctx, bucketName, objKeys)
    		if err != nil {
    			panic(err)
    		}
    		log.Println("Deleting bucket.")
    		err = bucketBasics.DeleteBucket(ctx, bucketName)
    		if err != nil {
    			panic(err)
    		}
    		log.Printf("Deleting downloaded file %v.\n", downloadFileName)
    		err = os.Remove(downloadFileName)
    		if err != nil {
    			panic(err)
    		}
    	} else {
    		log.Println("Okay. Don't forget to delete objects from your bucket to avoid charges.")
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [CopyObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.CopyObject)

    * [CreateBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.CreateBucket)

    * [DeleteBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.DeleteBucket)

    * [DeleteObjects](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.DeleteObjects)

    * [GetObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObject)

    * [ListObjectsV2](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListObjectsV2)

    * [PutObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObject)




## Actions

The following code example shows how to use `CopyObject`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // CopyToBucket copies an object in a bucket to another bucket.
    func (basics BucketBasics) CopyToBucket(ctx context.Context, sourceBucket string, destinationBucket string, objectKey string) error {
    	_, err := basics.S3Client.CopyObject(ctx, &s3.CopyObjectInput{
    		Bucket:     aws.String(destinationBucket),
    		CopySource: aws.String(fmt.Sprintf("%v/%v", sourceBucket, objectKey)),
    		Key:        aws.String(objectKey),
    	})
    	if err != nil {
    		var notActive *types.ObjectNotInActiveTierError
    		if errors.As(err, &notActive) {
    			log.Printf("Couldn't copy object %s from %s because the object isn't in the active tier.\n",
    				objectKey, sourceBucket)
    			err = notActive
    		}
    	} else {
    		err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(destinationBucket), Key: aws.String(objectKey)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist.\n", objectKey)
    		}
    	}
    	return err
    }
    
    
    

  * For API details, see [CopyObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.CopyObject) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateBucket`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 

Create a bucket with default configuration.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // CreateBucket creates a bucket with the specified name in the specified Region.
    func (basics BucketBasics) CreateBucket(ctx context.Context, name string, region string) error {
    	_, err := basics.S3Client.CreateBucket(ctx, &s3.CreateBucketInput{
    		Bucket: aws.String(name),
    		CreateBucketConfiguration: &types.CreateBucketConfiguration{
    			LocationConstraint: types.BucketLocationConstraint(region),
    		},
    	})
    	if err != nil {
    		var owned *types.BucketAlreadyOwnedByYou
    		var exists *types.BucketAlreadyExists
    		if errors.As(err, &owned) {
    			log.Printf("You already own bucket %s.\n", name)
    			err = owned
    		} else if errors.As(err, &exists) {
    			log.Printf("Bucket %s already exists.\n", name)
    			err = exists
    		}
    	} else {
    		err = s3.NewBucketExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(name)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to exist.\n", name)
    		}
    	}
    	return err
    }
    
    
    

Create a bucket with object locking and wait for it to exist.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // CreateBucketWithLock creates a new S3 bucket with optional object locking enabled
    // and waits for the bucket to exist before returning.
    func (actor S3Actions) CreateBucketWithLock(ctx context.Context, bucket string, region string, enableObjectLock bool) (string, error) {
    	input := &s3.CreateBucketInput{
    		Bucket: aws.String(bucket),
    		CreateBucketConfiguration: &types.CreateBucketConfiguration{
    			LocationConstraint: types.BucketLocationConstraint(region),
    		},
    	}
    
    	if enableObjectLock {
    		input.ObjectLockEnabledForBucket = aws.Bool(true)
    	}
    
    	_, err := actor.S3Client.CreateBucket(ctx, input)
    	if err != nil {
    		var owned *types.BucketAlreadyOwnedByYou
    		var exists *types.BucketAlreadyExists
    		if errors.As(err, &owned) {
    			log.Printf("You already own bucket %s.\n", bucket)
    			err = owned
    		} else if errors.As(err, &exists) {
    			log.Printf("Bucket %s already exists.\n", bucket)
    			err = exists
    		}
    	} else {
    		err = s3.NewBucketExistsWaiter(actor.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(bucket)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to exist.\n", bucket)
    		}
    	}
    
    	return bucket, err
    }
    
    
    

  * For API details, see [CreateBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.CreateBucket) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteBucket`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // DeleteBucket deletes a bucket. The bucket must be empty or an error is returned.
    func (basics BucketBasics) DeleteBucket(ctx context.Context, bucketName string) error {
    	_, err := basics.S3Client.DeleteBucket(ctx, &s3.DeleteBucketInput{
    		Bucket: aws.String(bucketName)})
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucketName)
    			err = noBucket
    		} else {
    			log.Printf("Couldn't delete bucket %v. Here's why: %v\n", bucketName, err)
    		}
    	} else {
    		err = s3.NewBucketNotExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(bucketName)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to be deleted.\n", bucketName)
    		} else {
    			log.Printf("Deleted %s.\n", bucketName)
    		}
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.DeleteBucket) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteObject`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // DeleteObject deletes an object from a bucket.
    func (actor S3Actions) DeleteObject(ctx context.Context, bucket string, key string, versionId string, bypassGovernance bool) (bool, error) {
    	deleted := false
    	input := &s3.DeleteObjectInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    	}
    	if versionId != "" {
    		input.VersionId = aws.String(versionId)
    	}
    	if bypassGovernance {
    		input.BypassGovernanceRetention = aws.Bool(true)
    	}
    	_, err := actor.S3Client.DeleteObject(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in %s.\n", key, bucket)
    			err = noKey
    		} else if errors.As(err, &apiErr) {
    			switch apiErr.ErrorCode() {
    			case "AccessDenied":
    				log.Printf("Access denied: cannot delete object %s from %s.\n", key, bucket)
    				err = nil
    			case "InvalidArgument":
    				if bypassGovernance {
    					log.Printf("You cannot specify bypass governance on a bucket without lock enabled.")
    					err = nil
    				}
    			}
    		}
    	} else {
    		err = s3.NewObjectNotExistsWaiter(actor.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(bucket), Key: aws.String(key)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s in bucket %s to be deleted.\n", key, bucket)
    		} else {
    			deleted = true
    		}
    	}
    	return deleted, err
    }
    
    
    

  * For API details, see [DeleteObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.DeleteObject) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteObjects`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // DeleteObjects deletes a list of objects from a bucket.
    func (actor S3Actions) DeleteObjects(ctx context.Context, bucket string, objects []types.ObjectIdentifier, bypassGovernance bool) error {
    	if len(objects) == 0 {
    		return nil
    	}
    
    	input := s3.DeleteObjectsInput{
    		Bucket: aws.String(bucket),
    		Delete: &types.Delete{
    			Objects: objects,
    			Quiet:   aws.Bool(true),
    		},
    	}
    	if bypassGovernance {
    		input.BypassGovernanceRetention = aws.Bool(true)
    	}
    	delOut, err := actor.S3Client.DeleteObjects(ctx, &input)
    	if err != nil || len(delOut.Errors) > 0 {
    		log.Printf("Error deleting objects from bucket %s.\n", bucket)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucket)
    				err = noBucket
    			}
    		} else if len(delOut.Errors) > 0 {
    			for _, outErr := range delOut.Errors {
    				log.Printf("%s: %s\n", *outErr.Key, *outErr.Message)
    			}
    			err = fmt.Errorf("%s", *delOut.Errors[0].Message)
    		}
    	} else {
    		for _, delObjs := range delOut.Deleted {
    			err = s3.NewObjectNotExistsWaiter(actor.S3Client).Wait(
    				ctx, &s3.HeadObjectInput{Bucket: aws.String(bucket), Key: delObjs.Key}, time.Minute)
    			if err != nil {
    				log.Printf("Failed attempt to wait for object %s to be deleted.\n", *delObjs.Key)
    			} else {
    				log.Printf("Deleted %s.\n", *delObjs.Key)
    			}
    		}
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteObjects](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.DeleteObjects) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetObject`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // DownloadFile gets an object from a bucket and stores it in a local file.
    func (basics BucketBasics) DownloadFile(ctx context.Context, bucketName string, objectKey string, fileName string) error {
    	result, err := basics.S3Client.GetObject(ctx, &s3.GetObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	})
    	if err != nil {
    		var noKey *types.NoSuchKey
    		if errors.As(err, &noKey) {
    			log.Printf("Can't get object %s from bucket %s. No such key exists.\n", objectKey, bucketName)
    			err = noKey
    		} else {
    			log.Printf("Couldn't get object %v:%v. Here's why: %v\n", bucketName, objectKey, err)
    		}
    		return err
    	}
    	defer result.Body.Close()
    	file, err := os.Create(fileName)
    	if err != nil {
    		log.Printf("Couldn't create file %v. Here's why: %v\n", fileName, err)
    		return err
    	}
    	defer file.Close()
    	body, err := io.ReadAll(result.Body)
    	if err != nil {
    		log.Printf("Couldn't read object body from %v. Here's why: %v\n", objectKey, err)
    	}
    	_, err = file.Write(body)
    	return err
    }
    
    
    

  * For API details, see [GetObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObject) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetObjectLegalHold`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // GetObjectLegalHold retrieves the legal hold status for an S3 object.
    func (actor S3Actions) GetObjectLegalHold(ctx context.Context, bucket string, key string, versionId string) (*types.ObjectLockLegalHoldStatus, error) {
    	var status *types.ObjectLockLegalHoldStatus
    	input := &s3.GetObjectLegalHoldInput{
    		Bucket:    aws.String(bucket),
    		Key:       aws.String(key),
    		VersionId: aws.String(versionId),
    	}
    
    	output, err := actor.S3Client.GetObjectLegalHold(ctx, input)
    	if err != nil {
    		var noSuchKeyErr *types.NoSuchKey
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noSuchKeyErr) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noSuchKeyErr
    		} else if errors.As(err, &apiErr) {
    			switch apiErr.ErrorCode() {
    			case "NoSuchObjectLockConfiguration":
    				log.Printf("Object %s does not have an object lock configuration.\n", key)
    				err = nil
    			case "InvalidRequest":
    				log.Printf("Bucket %s does not have an object lock configuration.\n", bucket)
    				err = nil
    			}
    		}
    	} else {
    		status = &output.LegalHold.Status
    	}
    
    	return status, err
    }
    
    
    

  * For API details, see [GetObjectLegalHold](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectLegalHold) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetObjectLockConfiguration`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // GetObjectLockConfiguration retrieves the object lock configuration for an S3 bucket.
    func (actor S3Actions) GetObjectLockConfiguration(ctx context.Context, bucket string) (*types.ObjectLockConfiguration, error) {
    	var lockConfig *types.ObjectLockConfiguration
    	input := &s3.GetObjectLockConfigurationInput{
    		Bucket: aws.String(bucket),
    	}
    
    	output, err := actor.S3Client.GetObjectLockConfiguration(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		} else if errors.As(err, &apiErr) && apiErr.ErrorCode() == "ObjectLockConfigurationNotFoundError" {
    			log.Printf("Bucket %s does not have an object lock configuration.\n", bucket)
    			err = nil
    		}
    	} else {
    		lockConfig = output.ObjectLockConfiguration
    	}
    
    	return lockConfig, err
    }
    
    
    

  * For API details, see [GetObjectLockConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectLockConfiguration) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetObjectRetention`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // GetObjectRetention retrieves the object retention configuration for an S3 object.
    func (actor S3Actions) GetObjectRetention(ctx context.Context, bucket string, key string) (*types.ObjectLockRetention, error) {
    	var retention *types.ObjectLockRetention
    	input := &s3.GetObjectRetentionInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    	}
    
    	output, err := actor.S3Client.GetObjectRetention(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noKey
    		} else if errors.As(err, &apiErr) {
    			switch apiErr.ErrorCode() {
    			case "NoSuchObjectLockConfiguration":
    				err = nil
    			case "InvalidRequest":
    				log.Printf("Bucket %s does not have locking enabled.", bucket)
    				err = nil
    			}
    		}
    	} else {
    		retention = output.Retention
    	}
    
    	return retention, err
    }
    
    
    

  * For API details, see [GetObjectRetention](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectRetention) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `HeadBucket`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // BucketExists checks whether a bucket exists in the current account.
    func (basics BucketBasics) BucketExists(ctx context.Context, bucketName string) (bool, error) {
    	_, err := basics.S3Client.HeadBucket(ctx, &s3.HeadBucketInput{
    		Bucket: aws.String(bucketName),
    	})
    	exists := true
    	if err != nil {
    		var apiError smithy.APIError
    		if errors.As(err, &apiError) {
    			switch apiError.(type) {
    			case *types.NotFound:
    				log.Printf("Bucket %v is available.\n", bucketName)
    				exists = false
    				err = nil
    			default:
    				log.Printf("Either you don't have access to bucket %v or another error occurred. "+
    					"Here's what happened: %v\n", bucketName, err)
    			}
    		}
    	} else {
    		log.Printf("Bucket %v exists and you already own it.", bucketName)
    	}
    
    	return exists, err
    }
    
    
    

  * For API details, see [HeadBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.HeadBucket) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListBuckets`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // ListBuckets lists the buckets in the current account.
    func (basics BucketBasics) ListBuckets(ctx context.Context) ([]types.Bucket, error) {
    	var err error
    	var output *s3.ListBucketsOutput
    	var buckets []types.Bucket
    	bucketPaginator := s3.NewListBucketsPaginator(basics.S3Client, &s3.ListBucketsInput{})
    	for bucketPaginator.HasMorePages() {
    		output, err = bucketPaginator.NextPage(ctx)
    		if err != nil {
    			var apiErr smithy.APIError
    			if errors.As(err, &apiErr) && apiErr.ErrorCode() == "AccessDenied" {
    				fmt.Println("You don't have permission to list buckets for this account.")
    				err = apiErr
    			} else {
    				log.Printf("Couldn't list buckets for your account. Here's why: %v\n", err)
    			}
    			break
    		} else {
    			buckets = append(buckets, output.Buckets...)
    		}
    	}
    	return buckets, err
    }
    
    
    

  * For API details, see [ListBuckets](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListBuckets) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListObjectVersions`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // ListObjectVersions lists all versions of all objects in a bucket.
    func (actor S3Actions) ListObjectVersions(ctx context.Context, bucket string) ([]types.ObjectVersion, error) {
    	var err error
    	var output *s3.ListObjectVersionsOutput
    	var versions []types.ObjectVersion
    	input := &s3.ListObjectVersionsInput{Bucket: aws.String(bucket)}
    	versionPaginator := s3.NewListObjectVersionsPaginator(actor.S3Client, input)
    	for versionPaginator.HasMorePages() {
    		output, err = versionPaginator.NextPage(ctx)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucket)
    				err = noBucket
    			}
    			break
    		} else {
    			versions = append(versions, output.Versions...)
    		}
    	}
    	return versions, err
    }
    
    
    

  * For API details, see [ListObjectVersions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListObjectVersions) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListObjectsV2`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // ListObjects lists the objects in a bucket.
    func (basics BucketBasics) ListObjects(ctx context.Context, bucketName string) ([]types.Object, error) {
    	var err error
    	var output *s3.ListObjectsV2Output
    	input := &s3.ListObjectsV2Input{
    		Bucket: aws.String(bucketName),
    	}
    	var objects []types.Object
    	objectPaginator := s3.NewListObjectsV2Paginator(basics.S3Client, input)
    	for objectPaginator.HasMorePages() {
    		output, err = objectPaginator.NextPage(ctx)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucketName)
    				err = noBucket
    			}
    			break
    		} else {
    			objects = append(objects, output.Contents...)
    		}
    	}
    	return objects, err
    }
    
    
    

  * For API details, see [ListObjectsV2](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListObjectsV2) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `PutObject`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 

Put an object in a bucket by using the low-level API.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // UploadFile reads from a file and puts the data into an object in a bucket.
    func (basics BucketBasics) UploadFile(ctx context.Context, bucketName string, objectKey string, fileName string) error {
    	file, err := os.Open(fileName)
    	if err != nil {
    		log.Printf("Couldn't open file %v to upload. Here's why: %v\n", fileName, err)
    	} else {
    		defer file.Close()
    		_, err = basics.S3Client.PutObject(ctx, &s3.PutObjectInput{
    			Bucket: aws.String(bucketName),
    			Key:    aws.String(objectKey),
    			Body:   file,
    		})
    		if err != nil {
    			var apiErr smithy.APIError
    			if errors.As(err, &apiErr) && apiErr.ErrorCode() == "EntityTooLarge" {
    				log.Printf("Error while uploading object to %s. The object is too large.\n"+
    					"To upload objects larger than 5GB, use the S3 console (160GB max)\n"+
    					"or the multipart upload API (5TB max).", bucketName)
    			} else {
    				log.Printf("Couldn't upload file %v to %v:%v. Here's why: %v\n",
    					fileName, bucketName, objectKey, err)
    			}
    		} else {
    			err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    				ctx, &s3.HeadObjectInput{Bucket: aws.String(bucketName), Key: aws.String(objectKey)}, time.Minute)
    			if err != nil {
    				log.Printf("Failed attempt to wait for object %s to exist.\n", objectKey)
    			}
    		}
    	}
    	return err
    }
    
    
    

Upload an object to a bucket by using a transfer manager.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // UploadObject uses the S3 upload manager to upload an object to a bucket.
    func (actor S3Actions) UploadObject(ctx context.Context, bucket string, key string, contents string) (string, error) {
    	var outKey string
    	input := &s3.PutObjectInput{
    		Bucket:            aws.String(bucket),
    		Key:               aws.String(key),
    		Body:              bytes.NewReader([]byte(contents)),
    		ChecksumAlgorithm: types.ChecksumAlgorithmSha256,
    	}
    	output, err := actor.S3Manager.Upload(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    	} else {
    		err := s3.NewObjectExistsWaiter(actor.S3Client).Wait(ctx, &s3.HeadObjectInput{
    			Bucket: aws.String(bucket),
    			Key:    aws.String(key),
    		}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist in %s.\n", key, bucket)
    		} else {
    			outKey = *output.Key
    		}
    	}
    	return outKey, err
    }
    
    
    

  * For API details, see [PutObject](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObject) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `PutObjectLegalHold`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // PutObjectLegalHold sets the legal hold configuration for an S3 object.
    func (actor S3Actions) PutObjectLegalHold(ctx context.Context, bucket string, key string, versionId string, legalHoldStatus types.ObjectLockLegalHoldStatus) error {
    	input := &s3.PutObjectLegalHoldInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    		LegalHold: &types.ObjectLockLegalHold{
    			Status: legalHoldStatus,
    		},
    	}
    	if versionId != "" {
    		input.VersionId = aws.String(versionId)
    	}
    
    	_, err := actor.S3Client.PutObjectLegalHold(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noKey
    		}
    	}
    
    	return err
    }
    
    
    

  * For API details, see [PutObjectLegalHold](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObjectLegalHold) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `PutObjectLockConfiguration`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 

Set the object lock configuration of a bucket.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // EnableObjectLockOnBucket enables object locking on an existing bucket.
    func (actor S3Actions) EnableObjectLockOnBucket(ctx context.Context, bucket string) error {
    	// Versioning must be enabled on the bucket before object locking is enabled.
    	verInput := &s3.PutBucketVersioningInput{
    		Bucket: aws.String(bucket),
    		VersioningConfiguration: &types.VersioningConfiguration{
    			MFADelete: types.MFADeleteDisabled,
    			Status:    types.BucketVersioningStatusEnabled,
    		},
    	}
    	_, err := actor.S3Client.PutBucketVersioning(ctx, verInput)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    		return err
    	}
    
    	input := &s3.PutObjectLockConfigurationInput{
    		Bucket: aws.String(bucket),
    		ObjectLockConfiguration: &types.ObjectLockConfiguration{
    			ObjectLockEnabled: types.ObjectLockEnabledEnabled,
    		},
    	}
    	_, err = actor.S3Client.PutObjectLockConfiguration(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    	}
    
    	return err
    }
    
    
    

Set the default retention period of a bucket.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // ModifyDefaultBucketRetention modifies the default retention period of an existing bucket.
    func (actor S3Actions) ModifyDefaultBucketRetention(
    	ctx context.Context, bucket string, lockMode types.ObjectLockEnabled, retentionPeriod int32, retentionMode types.ObjectLockRetentionMode) error {
    
    	input := &s3.PutObjectLockConfigurationInput{
    		Bucket: aws.String(bucket),
    		ObjectLockConfiguration: &types.ObjectLockConfiguration{
    			ObjectLockEnabled: lockMode,
    			Rule: &types.ObjectLockRule{
    				DefaultRetention: &types.DefaultRetention{
    					Days: aws.Int32(retentionPeriod),
    					Mode: retentionMode,
    				},
    			},
    		},
    	}
    	_, err := actor.S3Client.PutObjectLockConfiguration(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    	}
    
    	return err
    }
    
    
    

  * For API details, see [PutObjectLockConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObjectLockConfiguration) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `PutObjectRetention`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // PutObjectRetention sets the object retention configuration for an S3 object.
    func (actor S3Actions) PutObjectRetention(ctx context.Context, bucket string, key string, retentionMode types.ObjectLockRetentionMode, retentionPeriodDays int32) error {
    	input := &s3.PutObjectRetentionInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    		Retention: &types.ObjectLockRetention{
    			Mode:            retentionMode,
    			RetainUntilDate: aws.Time(time.Now().AddDate(0, 0, int(retentionPeriodDays))),
    		},
    		BypassGovernanceRetention: aws.Bool(true),
    	}
    
    	_, err := actor.S3Client.PutObjectRetention(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noKey
    		}
    	}
    
    	return err
    }
    
    
    

  * For API details, see [PutObjectRetention](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObjectRetention) in _AWS SDK for Go API Reference_. 




## Scenarios

The following code example shows how to create a presigned URL for Amazon S3 and upload an object.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 

Create functions that wrap S3 presigning actions.
    
    
    import (
    	"context"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	v4 "github.com/aws/aws-sdk-go-v2/aws/signer/v4"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    // Presigner encapsulates the Amazon Simple Storage Service (Amazon S3) presign actions
    // used in the examples.
    // It contains PresignClient, a client that is used to presign requests to Amazon S3.
    // Presigned requests contain temporary credentials and can be made from any HTTP client.
    type Presigner struct {
    	PresignClient *s3.PresignClient
    }
    
    
    
    // GetObject makes a presigned request that can be used to get an object from a bucket.
    // The presigned request is valid for the specified number of seconds.
    func (presigner Presigner) GetObject(
    	ctx context.Context, bucketName string, objectKey string, lifetimeSecs int64) (*v4.PresignedHTTPRequest, error) {
    	request, err := presigner.PresignClient.PresignGetObject(ctx, &s3.GetObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	}, func(opts *s3.PresignOptions) {
    		opts.Expires = time.Duration(lifetimeSecs * int64(time.Second))
    	})
    	if err != nil {
    		log.Printf("Couldn't get a presigned request to get %v:%v. Here's why: %v\n",
    			bucketName, objectKey, err)
    	}
    	return request, err
    }
    
    
    
    // PutObject makes a presigned request that can be used to put an object in a bucket.
    // The presigned request is valid for the specified number of seconds.
    func (presigner Presigner) PutObject(
    	ctx context.Context, bucketName string, objectKey string, lifetimeSecs int64) (*v4.PresignedHTTPRequest, error) {
    	request, err := presigner.PresignClient.PresignPutObject(ctx, &s3.PutObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	}, func(opts *s3.PresignOptions) {
    		opts.Expires = time.Duration(lifetimeSecs * int64(time.Second))
    	})
    	if err != nil {
    		log.Printf("Couldn't get a presigned request to put %v:%v. Here's why: %v\n",
    			bucketName, objectKey, err)
    	}
    	return request, err
    }
    
    
    
    // DeleteObject makes a presigned request that can be used to delete an object from a bucket.
    func (presigner Presigner) DeleteObject(ctx context.Context, bucketName string, objectKey string) (*v4.PresignedHTTPRequest, error) {
    	request, err := presigner.PresignClient.PresignDeleteObject(ctx, &s3.DeleteObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	})
    	if err != nil {
    		log.Printf("Couldn't get a presigned request to delete object %v. Here's why: %v\n", objectKey, err)
    	}
    	return request, err
    }
    
    
    
    func (presigner Presigner) PresignPostObject(ctx context.Context, bucketName string, objectKey string, lifetimeSecs int64) (*s3.PresignedPostRequest, error) {
    	request, err := presigner.PresignClient.PresignPostObject(ctx, &s3.PutObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	}, func(options *s3.PresignPostOptions) {
    		options.Expires = time.Duration(lifetimeSecs) * time.Second
    	})
    	if err != nil {
    		log.Printf("Couldn't get a presigned post request to put %v:%v. Here's why: %v\n", bucketName, objectKey, err)
    	}
    	return request, nil
    }
    
    
    
    

Run an interactive example that generates and uses presigned URLs to upload, download, and delete an S3 object.
    
    
    import (
    	"bytes"
    	"context"
    	"io"
    	"log"
    	"mime/multipart"
    	"net/http"
    	"os"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/s3/actions"
    )
    
    
    
    // RunPresigningScenario is an interactive example that shows you how to get presigned
    // HTTP requests that you can use to move data into and out of Amazon Simple Storage
    // Service (Amazon S3). The presigned requests contain temporary credentials and can
    // be used by an HTTP client.
    //
    // 1. Get a presigned request to put an object in a bucket.
    // 2. Use the net/http package to use the presigned request to upload a local file to the bucket.
    // 3. Get a presigned request to get an object from a bucket.
    // 4. Use the net/http package to use the presigned request to download the object to a local file.
    // 5. Get a presigned request to delete an object from a bucket.
    // 6. Use the net/http package to use the presigned request to delete the object.
    //
    // This example creates an Amazon S3 presign client from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // It uses a questioner from the `demotools` package to get input during the example.
    // This package can be found in the ..\..\demotools folder of this repo.
    //
    // It uses an IHttpRequester interface to abstract HTTP requests so they can be mocked
    // during testing.
    func RunPresigningScenario(ctx context.Context, sdkConfig aws.Config, questioner demotools.IQuestioner, httpRequester IHttpRequester) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			_, isMock := questioner.(*demotools.MockQuestioner)
    			if isMock || questioner.AskBool("Do you want to see the full error message (y/n)?", "y") {
    				log.Println(r)
    			}
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon S3 presigning demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	s3Client := s3.NewFromConfig(sdkConfig)
    	bucketBasics := actions.BucketBasics{S3Client: s3Client}
    	presignClient := s3.NewPresignClient(s3Client)
    	presigner := actions.Presigner{PresignClient: presignClient}
    
    	bucketName := questioner.Ask("We'll need a bucket. Enter a name for a bucket "+
    		"you own or one you want to create:", demotools.NotEmpty{})
    	bucketExists, err := bucketBasics.BucketExists(ctx, bucketName)
    	if err != nil {
    		panic(err)
    	}
    	if !bucketExists {
    		err = bucketBasics.CreateBucket(ctx, bucketName, sdkConfig.Region)
    		if err != nil {
    			panic(err)
    		} else {
    			log.Println("Bucket created.")
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's presign a request to upload a file to your bucket.")
    	uploadFilename := questioner.Ask("Enter the path to a file you want to upload:",
    		demotools.NotEmpty{})
    	uploadKey := questioner.Ask("What would you like to name the uploaded object?",
    		demotools.NotEmpty{})
    	uploadFile, err := os.Open(uploadFilename)
    	if err != nil {
    		panic(err)
    	}
    	defer uploadFile.Close()
    	presignedPutRequest, err := presigner.PutObject(ctx, bucketName, uploadKey, 60)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Got a presigned %v request to URL:\n\t%v\n", presignedPutRequest.Method,
    		presignedPutRequest.URL)
    	log.Println("Using net/http to send the request...")
    	info, err := uploadFile.Stat()
    	if err != nil {
    		panic(err)
    	}
    	putResponse, err := httpRequester.Put(presignedPutRequest.URL, info.Size(), uploadFile)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("%v object %v with presigned URL returned %v.", presignedPutRequest.Method,
    		uploadKey, putResponse.StatusCode)
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's presign a request to download the object.")
    	questioner.Ask("Press Enter when you're ready.")
    	presignedGetRequest, err := presigner.GetObject(ctx, bucketName, uploadKey, 60)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Got a presigned %v request to URL:\n\t%v\n", presignedGetRequest.Method,
    		presignedGetRequest.URL)
    	log.Println("Using net/http to send the request...")
    	getResponse, err := httpRequester.Get(presignedGetRequest.URL)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("%v object %v with presigned URL returned %v.", presignedGetRequest.Method,
    		uploadKey, getResponse.StatusCode)
    	defer getResponse.Body.Close()
    	downloadBody, err := io.ReadAll(getResponse.Body)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Downloaded %v bytes. Here are the first 100 of them:\n", len(downloadBody))
    	log.Println(strings.Repeat("-", 88))
    	log.Println(string(downloadBody[:100]))
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Now we'll create a new request to put the same object using a presigned post request")
    	questioner.Ask("Press Enter when you're ready.")
    	presignPostRequest, err := presigner.PresignPostObject(ctx, bucketName, uploadKey, 60)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Got a presigned post request to url %v with values %v\n", presignPostRequest.URL, presignPostRequest.Values)
    	log.Println("Using net/http multipart to send the request...")
    	uploadFile, err = os.Open(uploadFilename)
    	if err != nil {
    		panic(err)
    	}
    	defer uploadFile.Close()
    	multiPartResponse, err := sendMultipartRequest(presignPostRequest.URL, presignPostRequest.Values, uploadFile, uploadKey, httpRequester)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Presign post object %v with presigned URL returned %v.", uploadKey, multiPartResponse.StatusCode)
    
    	log.Println("Let's presign a request to delete the object.")
    	questioner.Ask("Press Enter when you're ready.")
    	presignedDelRequest, err := presigner.DeleteObject(ctx, bucketName, uploadKey)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Got a presigned %v request to URL:\n\t%v\n", presignedDelRequest.Method,
    		presignedDelRequest.URL)
    	log.Println("Using net/http to send the request...")
    	delResponse, err := httpRequester.Delete(presignedDelRequest.URL)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("%v object %v with presigned URL returned %v.\n", presignedDelRequest.Method,
    		uploadKey, delResponse.StatusCode)
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Define an HTTP request wrapper used by the example to make HTTP requests.
    
    
    // IHttpRequester abstracts HTTP requests into an interface so it can be mocked during
    // unit testing.
    type IHttpRequester interface {
    	Get(url string) (resp *http.Response, err error)
    	Post(url, contentType string, body io.Reader) (resp *http.Response, err error)
    	Put(url string, contentLength int64, body io.Reader) (resp *http.Response, err error)
    	Delete(url string) (resp *http.Response, err error)
    }
    
    // HttpRequester uses the net/http package to make HTTP requests during the scenario.
    type HttpRequester struct{}
    
    func (httpReq HttpRequester) Get(url string) (resp *http.Response, err error) {
    	return http.Get(url)
    }
    func (httpReq HttpRequester) Post(url, contentType string, body io.Reader) (resp *http.Response, err error) {
    	postRequest, err := http.NewRequest("POST", url, body)
    	if err != nil {
    		return nil, err
    	}
    	postRequest.Header.Set("Content-Type", contentType)
    	return http.DefaultClient.Do(postRequest)
    }
    
    func (httpReq HttpRequester) Put(url string, contentLength int64, body io.Reader) (resp *http.Response, err error) {
    	putRequest, err := http.NewRequest("PUT", url, body)
    	if err != nil {
    		return nil, err
    	}
    	putRequest.ContentLength = contentLength
    	return http.DefaultClient.Do(putRequest)
    }
    func (httpReq HttpRequester) Delete(url string) (resp *http.Response, err error) {
    	delRequest, err := http.NewRequest("DELETE", url, nil)
    	if err != nil {
    		return nil, err
    	}
    	return http.DefaultClient.Do(delRequest)
    }
    
    
    

The following code example shows how to work with S3 object lock features.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples). 

Run an interactive scenario demonstrating Amazon S3 object lock features.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"strings"
    
    	"s3_object_lock/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // ObjectLockScenario contains the steps to run the S3 Object Lock workflow.
    type ObjectLockScenario struct {
    	questioner demotools.IQuestioner
    	resources  Resources
    	s3Actions  *actions.S3Actions
    	sdkConfig  aws.Config
    }
    
    // NewObjectLockScenario constructs a new ObjectLockScenario instance.
    func NewObjectLockScenario(sdkConfig aws.Config, questioner demotools.IQuestioner) ObjectLockScenario {
    	scenario := ObjectLockScenario{
    		questioner: questioner,
    		resources:  Resources{},
    		s3Actions:  &actions.S3Actions{S3Client: s3.NewFromConfig(sdkConfig)},
    		sdkConfig:  sdkConfig,
    	}
    	scenario.s3Actions.S3Manager = manager.NewUploader(scenario.s3Actions.S3Client)
    	scenario.resources.init(scenario.s3Actions, questioner)
    	return scenario
    }
    
    type nameLocked struct {
    	name   string
    	locked bool
    }
    
    var createInfo = []nameLocked{
    	{"standard-bucket", false},
    	{"lock-bucket", true},
    	{"retention-bucket", false},
    }
    
    // CreateBuckets creates the S3 buckets required for the workflow.
    func (scenario *ObjectLockScenario) CreateBuckets(ctx context.Context) {
    	log.Println("Let's create some S3 buckets to use for this workflow.")
    	success := false
    	for !success {
    		prefix := scenario.questioner.Ask(
    			"This example creates three buckets. Enter a prefix to name your buckets (remember bucket names must be globally unique):")
    
    		for _, info := range createInfo {
    			log.Println(fmt.Sprintf("%s.%s", prefix, info.name))
    			bucketName, err := scenario.s3Actions.CreateBucketWithLock(ctx, fmt.Sprintf("%s.%s", prefix, info.name), scenario.sdkConfig.Region, info.locked)
    			if err != nil {
    				switch err.(type) {
    				case *types.BucketAlreadyExists, *types.BucketAlreadyOwnedByYou:
    					log.Printf("Couldn't create bucket %s.\n", bucketName)
    				default:
    					panic(err)
    				}
    				break
    			}
    			scenario.resources.demoBuckets[info.name] = &DemoBucket{
    				name:       bucketName,
    				objectKeys: []string{},
    			}
    			log.Printf("Created bucket %s.\n", bucketName)
    		}
    
    		if len(scenario.resources.demoBuckets) < len(createInfo) {
    			scenario.resources.deleteBuckets(ctx)
    		} else {
    			success = true
    		}
    	}
    
    	log.Println("S3 buckets created.")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // EnableLockOnBucket enables object locking on an existing bucket.
    func (scenario *ObjectLockScenario) EnableLockOnBucket(ctx context.Context) {
    	log.Println("\nA bucket can be configured to use object locking.")
    	scenario.questioner.Ask("Press Enter to continue.")
    
    	var err error
    	bucket := scenario.resources.demoBuckets["retention-bucket"]
    	err = scenario.s3Actions.EnableObjectLockOnBucket(ctx, bucket.name)
    	if err != nil {
    		switch err.(type) {
    		case *types.NoSuchBucket:
    			log.Printf("Couldn't enable object locking on bucket %s.\n", bucket.name)
    		default:
    			panic(err)
    		}
    	} else {
    		log.Printf("Object locking enabled on bucket %s.", bucket.name)
    	}
    
    	log.Println(strings.Repeat("-", 88))
    }
    
    // SetDefaultRetentionPolicy sets a default retention governance policy on a bucket.
    func (scenario *ObjectLockScenario) SetDefaultRetentionPolicy(ctx context.Context) {
    	log.Println("\nA bucket can be configured to use object locking with a default retention period.")
    
    	bucket := scenario.resources.demoBuckets["retention-bucket"]
    	retentionPeriod := scenario.questioner.AskInt("Enter the default retention period in days: ")
    	err := scenario.s3Actions.ModifyDefaultBucketRetention(ctx, bucket.name, types.ObjectLockEnabledEnabled, int32(retentionPeriod), types.ObjectLockRetentionModeGovernance)
    	if err != nil {
    		switch err.(type) {
    		case *types.NoSuchBucket:
    			log.Printf("Couldn't configure a default retention period on bucket %s.\n", bucket.name)
    		default:
    			panic(err)
    		}
    	} else {
    		log.Printf("Default retention policy set on bucket %s with %d day retention period.", bucket.name, retentionPeriod)
    		bucket.retentionEnabled = true
    	}
    
    	log.Println(strings.Repeat("-", 88))
    }
    
    // UploadTestObjects uploads test objects to the S3 buckets.
    func (scenario *ObjectLockScenario) UploadTestObjects(ctx context.Context) {
    	log.Println("Uploading test objects to S3 buckets.")
    
    	for _, info := range createInfo {
    		bucket := scenario.resources.demoBuckets[info.name]
    		for i := 0; i < 2; i++ {
    			key, err := scenario.s3Actions.UploadObject(ctx, bucket.name, fmt.Sprintf("example-%d", i),
    				fmt.Sprintf("Example object content #%d in bucket %s.", i, bucket.name))
    			if err != nil {
    				switch err.(type) {
    				case *types.NoSuchBucket:
    					log.Printf("Couldn't upload %s to bucket %s.\n", key, bucket.name)
    				default:
    					panic(err)
    				}
    			} else {
    				log.Printf("Uploaded %s to bucket %s.\n", key, bucket.name)
    				bucket.objectKeys = append(bucket.objectKeys, key)
    			}
    		}
    	}
    
    	scenario.questioner.Ask("Test objects uploaded. Press Enter to continue.")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // SetObjectLockConfigurations sets object lock configurations on the test objects.
    func (scenario *ObjectLockScenario) SetObjectLockConfigurations(ctx context.Context) {
    	log.Println("Now let's set object lock configurations on individual objects.")
    
    	buckets := []*DemoBucket{scenario.resources.demoBuckets["lock-bucket"], scenario.resources.demoBuckets["retention-bucket"]}
    	for _, bucket := range buckets {
    		for index, objKey := range bucket.objectKeys {
    			switch index {
    			case 0:
    				if scenario.questioner.AskBool(fmt.Sprintf("\nDo you want to add a legal hold to %s in %s (y/n)? ", objKey, bucket.name), "y") {
    					err := scenario.s3Actions.PutObjectLegalHold(ctx, bucket.name, objKey, "", types.ObjectLockLegalHoldStatusOn)
    					if err != nil {
    						switch err.(type) {
    						case *types.NoSuchKey:
    							log.Printf("Couldn't set legal hold on %s.\n", objKey)
    						default:
    							panic(err)
    						}
    					} else {
    						log.Printf("Legal hold set on %s.\n", objKey)
    					}
    				}
    			case 1:
    				q := fmt.Sprintf("\nDo you want to add a 1 day Governance retention period to %s in %s?\n"+
    					"Reminder: Only a user with the s3:BypassGovernanceRetention permission is able to delete this object\n"+
    					"or its bucket until the retention period has expired. (y/n) ", objKey, bucket.name)
    				if scenario.questioner.AskBool(q, "y") {
    					err := scenario.s3Actions.PutObjectRetention(ctx, bucket.name, objKey, types.ObjectLockRetentionModeGovernance, 1)
    					if err != nil {
    						switch err.(type) {
    						case *types.NoSuchKey:
    							log.Printf("Couldn't set retention period on %s in %s.\n", objKey, bucket.name)
    						default:
    							panic(err)
    						}
    					} else {
    						log.Printf("Retention period set to 1 for %s.", objKey)
    						bucket.retentionEnabled = true
    					}
    				}
    			}
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    const (
    	ListAll = iota
    	DeleteObject
    	DeleteRetentionObject
    	OverwriteObject
    	ViewRetention
    	ViewLegalHold
    	Finish
    )
    
    // InteractWithObjects allows the user to interact with the objects and test the object lock configurations.
    func (scenario *ObjectLockScenario) InteractWithObjects(ctx context.Context) {
    	log.Println("Now you can interact with the objects to explore the object lock configurations.")
    	interactiveChoices := []string{
    		"List all objects and buckets.",
    		"Attempt to delete an object.",
    		"Attempt to delete an object with retention period bypass.",
    		"Attempt to overwrite a file.",
    		"View the retention settings for an object.",
    		"View the legal hold settings for an object.",
    		"Finish the workflow."}
    
    	choice := ListAll
    	for choice != Finish {
    		objList := scenario.GetAllObjects(ctx)
    		objChoices := scenario.makeObjectChoiceList(objList)
    		choice = scenario.questioner.AskChoice("Choose an action from the menu:\n", interactiveChoices)
    		switch choice {
    		case ListAll:
    			log.Println("The current objects in the example buckets are:")
    			for _, objChoice := range objChoices {
    				log.Println("\t", objChoice)
    			}
    		case DeleteObject, DeleteRetentionObject:
    			objChoice := scenario.questioner.AskChoice("Enter the number of the object to delete:\n", objChoices)
    			obj := objList[objChoice]
    			deleted, err := scenario.s3Actions.DeleteObject(ctx, obj.bucket, obj.key, obj.versionId, choice == DeleteRetentionObject)
    			if err != nil {
    				switch err.(type) {
    				case *types.NoSuchKey:
    					log.Println("Nothing to delete.")
    				default:
    					panic(err)
    				}
    			} else if deleted {
    				log.Printf("Object %s deleted.\n", obj.key)
    			}
    		case OverwriteObject:
    			objChoice := scenario.questioner.AskChoice("Enter the number of the object to overwrite:\n", objChoices)
    			obj := objList[objChoice]
    			_, err := scenario.s3Actions.UploadObject(ctx, obj.bucket, obj.key, fmt.Sprintf("New content in object %s.", obj.key))
    			if err != nil {
    				switch err.(type) {
    				case *types.NoSuchBucket:
    					log.Println("Couldn't upload to nonexistent bucket.")
    				default:
    					panic(err)
    				}
    			} else {
    				log.Printf("Uploaded new content to object %s.\n", obj.key)
    			}
    		case ViewRetention:
    			objChoice := scenario.questioner.AskChoice("Enter the number of the object to view:\n", objChoices)
    			obj := objList[objChoice]
    			retention, err := scenario.s3Actions.GetObjectRetention(ctx, obj.bucket, obj.key)
    			if err != nil {
    				switch err.(type) {
    				case *types.NoSuchKey:
    					log.Printf("Can't get retention configuration for %s.\n", obj.key)
    				default:
    					panic(err)
    				}
    			} else if retention != nil {
    				log.Printf("Object %s has retention mode %s until %v.\n", obj.key, retention.Mode, retention.RetainUntilDate)
    			} else {
    				log.Printf("Object %s does not have object retention configured.\n", obj.key)
    			}
    		case ViewLegalHold:
    			objChoice := scenario.questioner.AskChoice("Enter the number of the object to view:\n", objChoices)
    			obj := objList[objChoice]
    			legalHold, err := scenario.s3Actions.GetObjectLegalHold(ctx, obj.bucket, obj.key, obj.versionId)
    			if err != nil {
    				switch err.(type) {
    				case *types.NoSuchKey:
    					log.Printf("Can't get legal hold configuration for %s.\n", obj.key)
    				default:
    					panic(err)
    				}
    			} else if legalHold != nil {
    				log.Printf("Object %s has legal hold %v.", obj.key, *legalHold)
    			} else {
    				log.Printf("Object %s does not have legal hold configured.", obj.key)
    			}
    		case Finish:
    			log.Println("Let's clean up.")
    		}
    		log.Println(strings.Repeat("-", 88))
    	}
    }
    
    type BucketKeyVersionId struct {
    	bucket    string
    	key       string
    	versionId string
    }
    
    // GetAllObjects gets the object versions in the example S3 buckets and returns them in a flattened list.
    func (scenario *ObjectLockScenario) GetAllObjects(ctx context.Context) []BucketKeyVersionId {
    	var objectList []BucketKeyVersionId
    	for _, info := range createInfo {
    		bucket := scenario.resources.demoBuckets[info.name]
    		versions, err := scenario.s3Actions.ListObjectVersions(ctx, bucket.name)
    		if err != nil {
    			switch err.(type) {
    			case *types.NoSuchBucket:
    				log.Printf("Couldn't get object versions for %s.\n", bucket.name)
    			default:
    				panic(err)
    			}
    		} else {
    			for _, version := range versions {
    				objectList = append(objectList,
    					BucketKeyVersionId{bucket: bucket.name, key: *version.Key, versionId: *version.VersionId})
    			}
    		}
    	}
    	return objectList
    }
    
    // makeObjectChoiceList makes the object version list into a list of strings that are displayed
    // as choices.
    func (scenario *ObjectLockScenario) makeObjectChoiceList(bucketObjects []BucketKeyVersionId) []string {
    	choices := make([]string, len(bucketObjects))
    	for i := 0; i < len(bucketObjects); i++ {
    		choices[i] = fmt.Sprintf("%s in %s with VersionId %s.",
    			bucketObjects[i].key, bucketObjects[i].bucket, bucketObjects[i].versionId)
    	}
    	return choices
    }
    
    // Run runs the S3 Object Lock scenario.
    func (scenario *ObjectLockScenario) Run(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			_, isMock := scenario.questioner.(*demotools.MockQuestioner)
    			if isMock || scenario.questioner.AskBool("Do you want to see the full error message (y/n)?", "y") {
    				log.Println(r)
    			}
    			scenario.resources.Cleanup(ctx)
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon S3 Object Lock Feature Scenario.")
    	log.Println(strings.Repeat("-", 88))
    
    	scenario.CreateBuckets(ctx)
    	scenario.EnableLockOnBucket(ctx)
    	scenario.SetDefaultRetentionPolicy(ctx)
    	scenario.UploadTestObjects(ctx)
    	scenario.SetObjectLockConfigurations(ctx)
    	scenario.InteractWithObjects(ctx)
    
    	scenario.resources.Cleanup(ctx)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Define a struct that wraps S3 actions used in this example.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // S3Actions wraps S3 service actions.
    type S3Actions struct {
    	S3Client  *s3.Client
    	S3Manager *manager.Uploader
    }
    
    
    
    // CreateBucketWithLock creates a new S3 bucket with optional object locking enabled
    // and waits for the bucket to exist before returning.
    func (actor S3Actions) CreateBucketWithLock(ctx context.Context, bucket string, region string, enableObjectLock bool) (string, error) {
    	input := &s3.CreateBucketInput{
    		Bucket: aws.String(bucket),
    		CreateBucketConfiguration: &types.CreateBucketConfiguration{
    			LocationConstraint: types.BucketLocationConstraint(region),
    		},
    	}
    
    	if enableObjectLock {
    		input.ObjectLockEnabledForBucket = aws.Bool(true)
    	}
    
    	_, err := actor.S3Client.CreateBucket(ctx, input)
    	if err != nil {
    		var owned *types.BucketAlreadyOwnedByYou
    		var exists *types.BucketAlreadyExists
    		if errors.As(err, &owned) {
    			log.Printf("You already own bucket %s.\n", bucket)
    			err = owned
    		} else if errors.As(err, &exists) {
    			log.Printf("Bucket %s already exists.\n", bucket)
    			err = exists
    		}
    	} else {
    		err = s3.NewBucketExistsWaiter(actor.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(bucket)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to exist.\n", bucket)
    		}
    	}
    
    	return bucket, err
    }
    
    
    
    // GetObjectLegalHold retrieves the legal hold status for an S3 object.
    func (actor S3Actions) GetObjectLegalHold(ctx context.Context, bucket string, key string, versionId string) (*types.ObjectLockLegalHoldStatus, error) {
    	var status *types.ObjectLockLegalHoldStatus
    	input := &s3.GetObjectLegalHoldInput{
    		Bucket:    aws.String(bucket),
    		Key:       aws.String(key),
    		VersionId: aws.String(versionId),
    	}
    
    	output, err := actor.S3Client.GetObjectLegalHold(ctx, input)
    	if err != nil {
    		var noSuchKeyErr *types.NoSuchKey
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noSuchKeyErr) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noSuchKeyErr
    		} else if errors.As(err, &apiErr) {
    			switch apiErr.ErrorCode() {
    			case "NoSuchObjectLockConfiguration":
    				log.Printf("Object %s does not have an object lock configuration.\n", key)
    				err = nil
    			case "InvalidRequest":
    				log.Printf("Bucket %s does not have an object lock configuration.\n", bucket)
    				err = nil
    			}
    		}
    	} else {
    		status = &output.LegalHold.Status
    	}
    
    	return status, err
    }
    
    
    
    // GetObjectLockConfiguration retrieves the object lock configuration for an S3 bucket.
    func (actor S3Actions) GetObjectLockConfiguration(ctx context.Context, bucket string) (*types.ObjectLockConfiguration, error) {
    	var lockConfig *types.ObjectLockConfiguration
    	input := &s3.GetObjectLockConfigurationInput{
    		Bucket: aws.String(bucket),
    	}
    
    	output, err := actor.S3Client.GetObjectLockConfiguration(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		} else if errors.As(err, &apiErr) && apiErr.ErrorCode() == "ObjectLockConfigurationNotFoundError" {
    			log.Printf("Bucket %s does not have an object lock configuration.\n", bucket)
    			err = nil
    		}
    	} else {
    		lockConfig = output.ObjectLockConfiguration
    	}
    
    	return lockConfig, err
    }
    
    
    
    // GetObjectRetention retrieves the object retention configuration for an S3 object.
    func (actor S3Actions) GetObjectRetention(ctx context.Context, bucket string, key string) (*types.ObjectLockRetention, error) {
    	var retention *types.ObjectLockRetention
    	input := &s3.GetObjectRetentionInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    	}
    
    	output, err := actor.S3Client.GetObjectRetention(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noKey
    		} else if errors.As(err, &apiErr) {
    			switch apiErr.ErrorCode() {
    			case "NoSuchObjectLockConfiguration":
    				err = nil
    			case "InvalidRequest":
    				log.Printf("Bucket %s does not have locking enabled.", bucket)
    				err = nil
    			}
    		}
    	} else {
    		retention = output.Retention
    	}
    
    	return retention, err
    }
    
    
    
    // PutObjectLegalHold sets the legal hold configuration for an S3 object.
    func (actor S3Actions) PutObjectLegalHold(ctx context.Context, bucket string, key string, versionId string, legalHoldStatus types.ObjectLockLegalHoldStatus) error {
    	input := &s3.PutObjectLegalHoldInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    		LegalHold: &types.ObjectLockLegalHold{
    			Status: legalHoldStatus,
    		},
    	}
    	if versionId != "" {
    		input.VersionId = aws.String(versionId)
    	}
    
    	_, err := actor.S3Client.PutObjectLegalHold(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noKey
    		}
    	}
    
    	return err
    }
    
    
    
    // ModifyDefaultBucketRetention modifies the default retention period of an existing bucket.
    func (actor S3Actions) ModifyDefaultBucketRetention(
    	ctx context.Context, bucket string, lockMode types.ObjectLockEnabled, retentionPeriod int32, retentionMode types.ObjectLockRetentionMode) error {
    
    	input := &s3.PutObjectLockConfigurationInput{
    		Bucket: aws.String(bucket),
    		ObjectLockConfiguration: &types.ObjectLockConfiguration{
    			ObjectLockEnabled: lockMode,
    			Rule: &types.ObjectLockRule{
    				DefaultRetention: &types.DefaultRetention{
    					Days: aws.Int32(retentionPeriod),
    					Mode: retentionMode,
    				},
    			},
    		},
    	}
    	_, err := actor.S3Client.PutObjectLockConfiguration(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    	}
    
    	return err
    }
    
    
    
    // EnableObjectLockOnBucket enables object locking on an existing bucket.
    func (actor S3Actions) EnableObjectLockOnBucket(ctx context.Context, bucket string) error {
    	// Versioning must be enabled on the bucket before object locking is enabled.
    	verInput := &s3.PutBucketVersioningInput{
    		Bucket: aws.String(bucket),
    		VersioningConfiguration: &types.VersioningConfiguration{
    			MFADelete: types.MFADeleteDisabled,
    			Status:    types.BucketVersioningStatusEnabled,
    		},
    	}
    	_, err := actor.S3Client.PutBucketVersioning(ctx, verInput)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    		return err
    	}
    
    	input := &s3.PutObjectLockConfigurationInput{
    		Bucket: aws.String(bucket),
    		ObjectLockConfiguration: &types.ObjectLockConfiguration{
    			ObjectLockEnabled: types.ObjectLockEnabledEnabled,
    		},
    	}
    	_, err = actor.S3Client.PutObjectLockConfiguration(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    	}
    
    	return err
    }
    
    
    
    // PutObjectRetention sets the object retention configuration for an S3 object.
    func (actor S3Actions) PutObjectRetention(ctx context.Context, bucket string, key string, retentionMode types.ObjectLockRetentionMode, retentionPeriodDays int32) error {
    	input := &s3.PutObjectRetentionInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    		Retention: &types.ObjectLockRetention{
    			Mode:            retentionMode,
    			RetainUntilDate: aws.Time(time.Now().AddDate(0, 0, int(retentionPeriodDays))),
    		},
    		BypassGovernanceRetention: aws.Bool(true),
    	}
    
    	_, err := actor.S3Client.PutObjectRetention(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in bucket %s.\n", key, bucket)
    			err = noKey
    		}
    	}
    
    	return err
    }
    
    
    
    // UploadObject uses the S3 upload manager to upload an object to a bucket.
    func (actor S3Actions) UploadObject(ctx context.Context, bucket string, key string, contents string) (string, error) {
    	var outKey string
    	input := &s3.PutObjectInput{
    		Bucket:            aws.String(bucket),
    		Key:               aws.String(key),
    		Body:              bytes.NewReader([]byte(contents)),
    		ChecksumAlgorithm: types.ChecksumAlgorithmSha256,
    	}
    	output, err := actor.S3Manager.Upload(ctx, input)
    	if err != nil {
    		var noBucket *types.NoSuchBucket
    		if errors.As(err, &noBucket) {
    			log.Printf("Bucket %s does not exist.\n", bucket)
    			err = noBucket
    		}
    	} else {
    		err := s3.NewObjectExistsWaiter(actor.S3Client).Wait(ctx, &s3.HeadObjectInput{
    			Bucket: aws.String(bucket),
    			Key:    aws.String(key),
    		}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist in %s.\n", key, bucket)
    		} else {
    			outKey = *output.Key
    		}
    	}
    	return outKey, err
    }
    
    
    
    // ListObjectVersions lists all versions of all objects in a bucket.
    func (actor S3Actions) ListObjectVersions(ctx context.Context, bucket string) ([]types.ObjectVersion, error) {
    	var err error
    	var output *s3.ListObjectVersionsOutput
    	var versions []types.ObjectVersion
    	input := &s3.ListObjectVersionsInput{Bucket: aws.String(bucket)}
    	versionPaginator := s3.NewListObjectVersionsPaginator(actor.S3Client, input)
    	for versionPaginator.HasMorePages() {
    		output, err = versionPaginator.NextPage(ctx)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucket)
    				err = noBucket
    			}
    			break
    		} else {
    			versions = append(versions, output.Versions...)
    		}
    	}
    	return versions, err
    }
    
    
    
    // DeleteObject deletes an object from a bucket.
    func (actor S3Actions) DeleteObject(ctx context.Context, bucket string, key string, versionId string, bypassGovernance bool) (bool, error) {
    	deleted := false
    	input := &s3.DeleteObjectInput{
    		Bucket: aws.String(bucket),
    		Key:    aws.String(key),
    	}
    	if versionId != "" {
    		input.VersionId = aws.String(versionId)
    	}
    	if bypassGovernance {
    		input.BypassGovernanceRetention = aws.Bool(true)
    	}
    	_, err := actor.S3Client.DeleteObject(ctx, input)
    	if err != nil {
    		var noKey *types.NoSuchKey
    		var apiErr *smithy.GenericAPIError
    		if errors.As(err, &noKey) {
    			log.Printf("Object %s does not exist in %s.\n", key, bucket)
    			err = noKey
    		} else if errors.As(err, &apiErr) {
    			switch apiErr.ErrorCode() {
    			case "AccessDenied":
    				log.Printf("Access denied: cannot delete object %s from %s.\n", key, bucket)
    				err = nil
    			case "InvalidArgument":
    				if bypassGovernance {
    					log.Printf("You cannot specify bypass governance on a bucket without lock enabled.")
    					err = nil
    				}
    			}
    		}
    	} else {
    		err = s3.NewObjectNotExistsWaiter(actor.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(bucket), Key: aws.String(key)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s in bucket %s to be deleted.\n", key, bucket)
    		} else {
    			deleted = true
    		}
    	}
    	return deleted, err
    }
    
    
    
    // DeleteObjects deletes a list of objects from a bucket.
    func (actor S3Actions) DeleteObjects(ctx context.Context, bucket string, objects []types.ObjectIdentifier, bypassGovernance bool) error {
    	if len(objects) == 0 {
    		return nil
    	}
    
    	input := s3.DeleteObjectsInput{
    		Bucket: aws.String(bucket),
    		Delete: &types.Delete{
    			Objects: objects,
    			Quiet:   aws.Bool(true),
    		},
    	}
    	if bypassGovernance {
    		input.BypassGovernanceRetention = aws.Bool(true)
    	}
    	delOut, err := actor.S3Client.DeleteObjects(ctx, &input)
    	if err != nil || len(delOut.Errors) > 0 {
    		log.Printf("Error deleting objects from bucket %s.\n", bucket)
    		if err != nil {
    			var noBucket *types.NoSuchBucket
    			if errors.As(err, &noBucket) {
    				log.Printf("Bucket %s does not exist.\n", bucket)
    				err = noBucket
    			}
    		} else if len(delOut.Errors) > 0 {
    			for _, outErr := range delOut.Errors {
    				log.Printf("%s: %s\n", *outErr.Key, *outErr.Message)
    			}
    			err = fmt.Errorf("%s", *delOut.Errors[0].Message)
    		}
    	} else {
    		for _, delObjs := range delOut.Deleted {
    			err = s3.NewObjectNotExistsWaiter(actor.S3Client).Wait(
    				ctx, &s3.HeadObjectInput{Bucket: aws.String(bucket), Key: delObjs.Key}, time.Minute)
    			if err != nil {
    				log.Printf("Failed attempt to wait for object %s to be deleted.\n", *delObjs.Key)
    			} else {
    				log.Printf("Deleted %s.\n", *delObjs.Key)
    			}
    		}
    	}
    	return err
    }
    
    
    
    

Clean up resources.
    
    
    import (
    	"context"
    	"log"
    	"s3_object_lock/actions"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // DemoBucket contains metadata for buckets used in this example.
    type DemoBucket struct {
    	name             string
    	retentionEnabled bool
    	objectKeys       []string
    }
    
    // Resources keeps track of AWS resources created during the ObjectLockScenario and handles
    // cleanup when the scenario finishes.
    type Resources struct {
    	demoBuckets map[string]*DemoBucket
    
    	s3Actions  *actions.S3Actions
    	questioner demotools.IQuestioner
    }
    
    // init initializes objects in the Resources struct.
    func (resources *Resources) init(s3Actions *actions.S3Actions, questioner demotools.IQuestioner) {
    	resources.s3Actions = s3Actions
    	resources.questioner = questioner
    	resources.demoBuckets = map[string]*DemoBucket{}
    }
    
    // Cleanup deletes all AWS resources created during the ObjectLockScenario.
    func (resources *Resources) Cleanup(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong during cleanup.\n%v\n", r)
    			log.Println("Use the AWS Management Console to remove any remaining resources " +
    				"that were created for this scenario.")
    		}
    	}()
    
    	wantDelete := resources.questioner.AskBool("Do you want to remove all of the AWS resources that were created "+
    		"during this demo (y/n)?", "y")
    	if !wantDelete {
    		log.Println("Be sure to remove resources when you're done with them to avoid unexpected charges!")
    		return
    	}
    
    	log.Println("Removing objects from S3 buckets and deleting buckets...")
    	resources.deleteBuckets(ctx)
    	//resources.deleteRetentionObjects(resources.retentionBucket, resources.retentionObjects)
    
    	log.Println("Cleanup complete.")
    }
    
    // deleteBuckets empties and then deletes all buckets created during the ObjectLockScenario.
    func (resources *Resources) deleteBuckets(ctx context.Context) {
    	for _, info := range createInfo {
    		bucket := resources.demoBuckets[info.name]
    		resources.deleteObjects(ctx, bucket)
    		_, err := resources.s3Actions.S3Client.DeleteBucket(ctx, &s3.DeleteBucketInput{
    			Bucket: aws.String(bucket.name),
    		})
    		if err != nil {
    			panic(err)
    		}
    	}
    	for _, info := range createInfo {
    		bucket := resources.demoBuckets[info.name]
    		err := s3.NewBucketNotExistsWaiter(resources.s3Actions.S3Client).Wait(
    			ctx, &s3.HeadBucketInput{Bucket: aws.String(bucket.name)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for bucket %s to be deleted.\n", bucket.name)
    		} else {
    			log.Printf("Deleted %s.\n", bucket.name)
    		}
    	}
    	resources.demoBuckets = map[string]*DemoBucket{}
    }
    
    // deleteObjects deletes all objects in the specified bucket.
    func (resources *Resources) deleteObjects(ctx context.Context, bucket *DemoBucket) {
    	lockConfig, err := resources.s3Actions.GetObjectLockConfiguration(ctx, bucket.name)
    	if err != nil {
    		panic(err)
    	}
    	versions, err := resources.s3Actions.ListObjectVersions(ctx, bucket.name)
    	if err != nil {
    		switch err.(type) {
    		case *types.NoSuchBucket:
    			log.Printf("No objects to get from %s.\n", bucket.name)
    		default:
    			panic(err)
    		}
    	}
    	delObjects := make([]types.ObjectIdentifier, len(versions))
    	for i, version := range versions {
    		if lockConfig != nil && lockConfig.ObjectLockEnabled == types.ObjectLockEnabledEnabled {
    			status, err := resources.s3Actions.GetObjectLegalHold(ctx, bucket.name, *version.Key, *version.VersionId)
    			if err != nil {
    				switch err.(type) {
    				case *types.NoSuchKey:
    					log.Printf("Couldn't determine legal hold status for %s in %s.\n", *version.Key, bucket.name)
    				default:
    					panic(err)
    				}
    			} else if status != nil && *status == types.ObjectLockLegalHoldStatusOn {
    				err = resources.s3Actions.PutObjectLegalHold(ctx, bucket.name, *version.Key, *version.VersionId, types.ObjectLockLegalHoldStatusOff)
    				if err != nil {
    					switch err.(type) {
    					case *types.NoSuchKey:
    						log.Printf("Couldn't turn off legal hold for %s in %s.\n", *version.Key, bucket.name)
    					default:
    						panic(err)
    					}
    				}
    			}
    		}
    		delObjects[i] = types.ObjectIdentifier{Key: version.Key, VersionId: version.VersionId}
    	}
    	err = resources.s3Actions.DeleteObjects(ctx, bucket.name, delObjects, bucket.retentionEnabled)
    	if err != nil {
    		switch err.(type) {
    		case *types.NoSuchBucket:
    			log.Println("Nothing to delete.")
    		default:
    			panic(err)
    		}
    	}
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [GetObjectLegalHold](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectLegalHold)

    * [GetObjectLockConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectLockConfiguration)

    * [GetObjectRetention](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectRetention)

    * [PutObjectLegalHold](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObjectLegalHold)

    * [PutObjectLockConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObjectLockConfiguration)

    * [PutObjectRetention](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.PutObjectRetention)




The following code example shows how to upload or download large files to and from Amazon S3.

For more information, see [Uploading an object using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-upload-object.html).

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples). 

Create functions that use upload and download managers to break the data into parts and transfer them concurrently.
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/s3/types"
    	"github.com/aws/smithy-go"
    )
    
    // BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
    // used in the examples.
    // It contains S3Client, an Amazon S3 service client that is used to perform bucket
    // and object actions.
    type BucketBasics struct {
    	S3Client *s3.Client
    }
    
    
    
    // UploadLargeObject uses an upload manager to upload data to an object in a bucket.
    // The upload manager breaks large data into parts and uploads the parts concurrently.
    func (basics BucketBasics) UploadLargeObject(ctx context.Context, bucketName string, objectKey string, largeObject []byte) error {
    	largeBuffer := bytes.NewReader(largeObject)
    	var partMiBs int64 = 10
    	uploader := manager.NewUploader(basics.S3Client, func(u *manager.Uploader) {
    		u.PartSize = partMiBs * 1024 * 1024
    	})
    	_, err := uploader.Upload(ctx, &s3.PutObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    		Body:   largeBuffer,
    	})
    	if err != nil {
    		var apiErr smithy.APIError
    		if errors.As(err, &apiErr) && apiErr.ErrorCode() == "EntityTooLarge" {
    			log.Printf("Error while uploading object to %s. The object is too large.\n"+
    				"The maximum size for a multipart upload is 5TB.", bucketName)
    		} else {
    			log.Printf("Couldn't upload large object to %v:%v. Here's why: %v\n",
    				bucketName, objectKey, err)
    		}
    	} else {
    		err = s3.NewObjectExistsWaiter(basics.S3Client).Wait(
    			ctx, &s3.HeadObjectInput{Bucket: aws.String(bucketName), Key: aws.String(objectKey)}, time.Minute)
    		if err != nil {
    			log.Printf("Failed attempt to wait for object %s to exist.\n", objectKey)
    		}
    	}
    
    	return err
    }
    
    
    
    // DownloadLargeObject uses a download manager to download an object from a bucket.
    // The download manager gets the data in parts and writes them to a buffer until all of
    // the data has been downloaded.
    func (basics BucketBasics) DownloadLargeObject(ctx context.Context, bucketName string, objectKey string) ([]byte, error) {
    	var partMiBs int64 = 10
    	downloader := manager.NewDownloader(basics.S3Client, func(d *manager.Downloader) {
    		d.PartSize = partMiBs * 1024 * 1024
    	})
    	buffer := manager.NewWriteAtBuffer([]byte{})
    	_, err := downloader.Download(ctx, buffer, &s3.GetObjectInput{
    		Bucket: aws.String(bucketName),
    		Key:    aws.String(objectKey),
    	})
    	if err != nil {
    		log.Printf("Couldn't download large object from %v:%v. Here's why: %v\n",
    			bucketName, objectKey, err)
    	}
    	return buffer.Bytes(), err
    }
    
    
    

Run an interactive scenario that shows you how to use the upload and download managers in context.
    
    
    import (
    	"context"
    	"crypto/rand"
    	"log"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/s3/actions"
    )
    
    // RunLargeObjectScenario is an interactive example that shows you how to use Amazon
    // Simple Storage Service (Amazon S3) to upload and download large objects.
    //
    // 1. Create a bucket.
    // 3. Upload a large object to the bucket by using an upload manager.
    // 5. Download a large object by using a download manager.
    // 8. Delete all objects in the bucket.
    // 9. Delete the bucket.
    //
    // This example creates an Amazon S3 service client from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // It uses a questioner from the `demotools` package to get input during the example.
    // This package can be found in the ..\..\demotools folder of this repo.
    func RunLargeObjectScenario(ctx context.Context, sdkConfig aws.Config, questioner demotools.IQuestioner) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			_, isMock := questioner.(*demotools.MockQuestioner)
    			if isMock || questioner.AskBool("Do you want to see the full error message (y/n)?", "y") {
    				log.Println(r)
    			}
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon S3 large object demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	s3Client := s3.NewFromConfig(sdkConfig)
    	bucketBasics := actions.BucketBasics{S3Client: s3Client}
    
    	bucketName := questioner.Ask("Let's create a bucket. Enter a name for your bucket:",
    		demotools.NotEmpty{})
    	bucketExists, err := bucketBasics.BucketExists(ctx, bucketName)
    	if err != nil {
    		panic(err)
    	}
    	if !bucketExists {
    		err = bucketBasics.CreateBucket(ctx, bucketName, sdkConfig.Region)
    		if err != nil {
    			panic(err)
    		} else {
    			log.Println("Bucket created.")
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	mibs := 30
    	log.Printf("Let's create a slice of %v MiB of random bytes and upload it to your bucket. ", mibs)
    	questioner.Ask("Press Enter when you're ready.")
    	largeBytes := make([]byte, 1024*1024*mibs)
    	_, _ = rand.Read(largeBytes)
    	largeKey := "doc-example-large"
    	log.Println("Uploading...")
    	err = bucketBasics.UploadLargeObject(ctx, bucketName, largeKey, largeBytes)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Uploaded %v MiB object as %v", mibs, largeKey)
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's download the %v MiB object.", mibs)
    	questioner.Ask("Press Enter when you're ready.")
    	log.Println("Downloading...")
    	largeDownload, err := bucketBasics.DownloadLargeObject(ctx, bucketName, largeKey)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Downloaded %v bytes.", len(largeDownload))
    	log.Println(strings.Repeat("-", 88))
    
    	if questioner.AskBool("Do you want to delete your bucket and all of its "+
    		"contents? (y/n)", "y") {
    		log.Println("Deleting object.")
    		err = bucketBasics.DeleteObjects(ctx, bucketName, []string{largeKey})
    		if err != nil {
    			panic(err)
    		}
    		log.Println("Deleting bucket.")
    		err = bucketBasics.DeleteBucket(ctx, bucketName)
    		if err != nil {
    			panic(err)
    		}
    	} else {
    		log.Println("Okay. Don't forget to delete objects from your bucket to avoid charges.")
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

## Serverless examples

The following code example shows how to implement a Lambda function that receives an event triggered by uploading an object to an S3 bucket. The function retrieves the S3 bucket name and object key from the event parameter and calls the Amazon S3 API to retrieve and log the content type of the object.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 

Consuming an S3 event with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    func handler(ctx context.Context, s3Event events.S3Event) error {
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		log.Printf("failed to load default config: %s", err)
    		return err
    	}
    	s3Client := s3.NewFromConfig(sdkConfig)
    
    	for _, record := range s3Event.Records {
    		bucket := record.S3.Bucket.Name
    		key := record.S3.Object.URLDecodedKey
    		headOutput, err := s3Client.HeadObject(ctx, &s3.HeadObjectInput{
    			Bucket: &bucket,
    			Key:    &key,
    		})
    		if err != nil {
    			log.Printf("error getting head of object %s/%s: %s", bucket, key, err)
    			return err
    		}
    		log.Printf("successfully retrieved %s/%s of type %s", bucket, key, *headOutput.ContentType)
    	}
    
    	return nil
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon Redshift

Amazon SNS

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

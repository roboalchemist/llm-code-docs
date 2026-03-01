# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store/mocks

Title: mocks package - go.temporal.io/server/common/archiver/s3store/mocks - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store/mocks

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
go.temporal.io/server
 
common
 
archiver
 
s3store
 
mocks
mocks
package
Version: v1.30.0 Latest 
Published: Feb 4, 2026 
License: MIT 
Imports: 5 
Imported by: 0
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/temporalio/temporal
Links
 Open Source Insights
Jump to ...
Documentation
Source Files
 Documentation ¶
Overview ¶

Package mocks is a generated GoMock package.

Index ¶
type MockS3API
func NewMockS3API(ctrl *gomock.Controller) *MockS3API
func (m *MockS3API) AbortMultipartUpload(arg0 *s3.AbortMultipartUploadInput) (*s3.AbortMultipartUploadOutput, error)
func (m *MockS3API) AbortMultipartUploadRequest(arg0 *s3.AbortMultipartUploadInput) (*request.Request, *s3.AbortMultipartUploadOutput)
func (m *MockS3API) AbortMultipartUploadWithContext(arg0 aws.Context, arg1 *s3.AbortMultipartUploadInput, arg2 ...request.Option) (*s3.AbortMultipartUploadOutput, error)
func (m *MockS3API) CompleteMultipartUpload(arg0 *s3.CompleteMultipartUploadInput) (*s3.CompleteMultipartUploadOutput, error)
func (m *MockS3API) CompleteMultipartUploadRequest(arg0 *s3.CompleteMultipartUploadInput) (*request.Request, *s3.CompleteMultipartUploadOutput)
func (m *MockS3API) CompleteMultipartUploadWithContext(arg0 aws.Context, arg1 *s3.CompleteMultipartUploadInput, ...) (*s3.CompleteMultipartUploadOutput, error)
func (m *MockS3API) CopyObject(arg0 *s3.CopyObjectInput) (*s3.CopyObjectOutput, error)
func (m *MockS3API) CopyObjectRequest(arg0 *s3.CopyObjectInput) (*request.Request, *s3.CopyObjectOutput)
func (m *MockS3API) CopyObjectWithContext(arg0 aws.Context, arg1 *s3.CopyObjectInput, arg2 ...request.Option) (*s3.CopyObjectOutput, error)
func (m *MockS3API) CreateBucket(arg0 *s3.CreateBucketInput) (*s3.CreateBucketOutput, error)
func (m *MockS3API) CreateBucketRequest(arg0 *s3.CreateBucketInput) (*request.Request, *s3.CreateBucketOutput)
func (m *MockS3API) CreateBucketWithContext(arg0 aws.Context, arg1 *s3.CreateBucketInput, arg2 ...request.Option) (*s3.CreateBucketOutput, error)
func (m *MockS3API) CreateMultipartUpload(arg0 *s3.CreateMultipartUploadInput) (*s3.CreateMultipartUploadOutput, error)
func (m *MockS3API) CreateMultipartUploadRequest(arg0 *s3.CreateMultipartUploadInput) (*request.Request, *s3.CreateMultipartUploadOutput)
func (m *MockS3API) CreateMultipartUploadWithContext(arg0 aws.Context, arg1 *s3.CreateMultipartUploadInput, arg2 ...request.Option) (*s3.CreateMultipartUploadOutput, error)
func (m *MockS3API) CreateSession(arg0 *s3.CreateSessionInput) (*s3.CreateSessionOutput, error)
func (m *MockS3API) CreateSessionRequest(arg0 *s3.CreateSessionInput) (*request.Request, *s3.CreateSessionOutput)
func (m *MockS3API) CreateSessionWithContext(arg0 aws.Context, arg1 *s3.CreateSessionInput, arg2 ...request.Option) (*s3.CreateSessionOutput, error)
func (m *MockS3API) DeleteBucket(arg0 *s3.DeleteBucketInput) (*s3.DeleteBucketOutput, error)
func (m *MockS3API) DeleteBucketAnalyticsConfiguration(arg0 *s3.DeleteBucketAnalyticsConfigurationInput) (*s3.DeleteBucketAnalyticsConfigurationOutput, error)
func (m *MockS3API) DeleteBucketAnalyticsConfigurationRequest(arg0 *s3.DeleteBucketAnalyticsConfigurationInput) (*request.Request, *s3.DeleteBucketAnalyticsConfigurationOutput)
func (m *MockS3API) DeleteBucketAnalyticsConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketAnalyticsConfigurationInput, ...) (*s3.DeleteBucketAnalyticsConfigurationOutput, error)
func (m *MockS3API) DeleteBucketCors(arg0 *s3.DeleteBucketCorsInput) (*s3.DeleteBucketCorsOutput, error)
func (m *MockS3API) DeleteBucketCorsRequest(arg0 *s3.DeleteBucketCorsInput) (*request.Request, *s3.DeleteBucketCorsOutput)
func (m *MockS3API) DeleteBucketCorsWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketCorsInput, arg2 ...request.Option) (*s3.DeleteBucketCorsOutput, error)
func (m *MockS3API) DeleteBucketEncryption(arg0 *s3.DeleteBucketEncryptionInput) (*s3.DeleteBucketEncryptionOutput, error)
func (m *MockS3API) DeleteBucketEncryptionRequest(arg0 *s3.DeleteBucketEncryptionInput) (*request.Request, *s3.DeleteBucketEncryptionOutput)
func (m *MockS3API) DeleteBucketEncryptionWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketEncryptionInput, arg2 ...request.Option) (*s3.DeleteBucketEncryptionOutput, error)
func (m *MockS3API) DeleteBucketIntelligentTieringConfiguration(arg0 *s3.DeleteBucketIntelligentTieringConfigurationInput) (*s3.DeleteBucketIntelligentTieringConfigurationOutput, error)
func (m *MockS3API) DeleteBucketIntelligentTieringConfigurationRequest(arg0 *s3.DeleteBucketIntelligentTieringConfigurationInput) (*request.Request, *s3.DeleteBucketIntelligentTieringConfigurationOutput)
func (m *MockS3API) DeleteBucketIntelligentTieringConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketIntelligentTieringConfigurationInput, ...) (*s3.DeleteBucketIntelligentTieringConfigurationOutput, error)
func (m *MockS3API) DeleteBucketInventoryConfiguration(arg0 *s3.DeleteBucketInventoryConfigurationInput) (*s3.DeleteBucketInventoryConfigurationOutput, error)
func (m *MockS3API) DeleteBucketInventoryConfigurationRequest(arg0 *s3.DeleteBucketInventoryConfigurationInput) (*request.Request, *s3.DeleteBucketInventoryConfigurationOutput)
func (m *MockS3API) DeleteBucketInventoryConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketInventoryConfigurationInput, ...) (*s3.DeleteBucketInventoryConfigurationOutput, error)
func (m *MockS3API) DeleteBucketLifecycle(arg0 *s3.DeleteBucketLifecycleInput) (*s3.DeleteBucketLifecycleOutput, error)
func (m *MockS3API) DeleteBucketLifecycleRequest(arg0 *s3.DeleteBucketLifecycleInput) (*request.Request, *s3.DeleteBucketLifecycleOutput)
func (m *MockS3API) DeleteBucketLifecycleWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketLifecycleInput, arg2 ...request.Option) (*s3.DeleteBucketLifecycleOutput, error)
func (m *MockS3API) DeleteBucketMetricsConfiguration(arg0 *s3.DeleteBucketMetricsConfigurationInput) (*s3.DeleteBucketMetricsConfigurationOutput, error)
func (m *MockS3API) DeleteBucketMetricsConfigurationRequest(arg0 *s3.DeleteBucketMetricsConfigurationInput) (*request.Request, *s3.DeleteBucketMetricsConfigurationOutput)
func (m *MockS3API) DeleteBucketMetricsConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketMetricsConfigurationInput, ...) (*s3.DeleteBucketMetricsConfigurationOutput, error)
func (m *MockS3API) DeleteBucketOwnershipControls(arg0 *s3.DeleteBucketOwnershipControlsInput) (*s3.DeleteBucketOwnershipControlsOutput, error)
func (m *MockS3API) DeleteBucketOwnershipControlsRequest(arg0 *s3.DeleteBucketOwnershipControlsInput) (*request.Request, *s3.DeleteBucketOwnershipControlsOutput)
func (m *MockS3API) DeleteBucketOwnershipControlsWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketOwnershipControlsInput, ...) (*s3.DeleteBucketOwnershipControlsOutput, error)
func (m *MockS3API) DeleteBucketPolicy(arg0 *s3.DeleteBucketPolicyInput) (*s3.DeleteBucketPolicyOutput, error)
func (m *MockS3API) DeleteBucketPolicyRequest(arg0 *s3.DeleteBucketPolicyInput) (*request.Request, *s3.DeleteBucketPolicyOutput)
func (m *MockS3API) DeleteBucketPolicyWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketPolicyInput, arg2 ...request.Option) (*s3.DeleteBucketPolicyOutput, error)
func (m *MockS3API) DeleteBucketReplication(arg0 *s3.DeleteBucketReplicationInput) (*s3.DeleteBucketReplicationOutput, error)
func (m *MockS3API) DeleteBucketReplicationRequest(arg0 *s3.DeleteBucketReplicationInput) (*request.Request, *s3.DeleteBucketReplicationOutput)
func (m *MockS3API) DeleteBucketReplicationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketReplicationInput, ...) (*s3.DeleteBucketReplicationOutput, error)
func (m *MockS3API) DeleteBucketRequest(arg0 *s3.DeleteBucketInput) (*request.Request, *s3.DeleteBucketOutput)
func (m *MockS3API) DeleteBucketTagging(arg0 *s3.DeleteBucketTaggingInput) (*s3.DeleteBucketTaggingOutput, error)
func (m *MockS3API) DeleteBucketTaggingRequest(arg0 *s3.DeleteBucketTaggingInput) (*request.Request, *s3.DeleteBucketTaggingOutput)
func (m *MockS3API) DeleteBucketTaggingWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketTaggingInput, arg2 ...request.Option) (*s3.DeleteBucketTaggingOutput, error)
func (m *MockS3API) DeleteBucketWebsite(arg0 *s3.DeleteBucketWebsiteInput) (*s3.DeleteBucketWebsiteOutput, error)
func (m *MockS3API) DeleteBucketWebsiteRequest(arg0 *s3.DeleteBucketWebsiteInput) (*request.Request, *s3.DeleteBucketWebsiteOutput)
func (m *MockS3API) DeleteBucketWebsiteWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketWebsiteInput, arg2 ...request.Option) (*s3.DeleteBucketWebsiteOutput, error)
func (m *MockS3API) DeleteBucketWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketInput, arg2 ...request.Option) (*s3.DeleteBucketOutput, error)
func (m *MockS3API) DeleteObject(arg0 *s3.DeleteObjectInput) (*s3.DeleteObjectOutput, error)
func (m *MockS3API) DeleteObjectRequest(arg0 *s3.DeleteObjectInput) (*request.Request, *s3.DeleteObjectOutput)
func (m *MockS3API) DeleteObjectTagging(arg0 *s3.DeleteObjectTaggingInput) (*s3.DeleteObjectTaggingOutput, error)
func (m *MockS3API) DeleteObjectTaggingRequest(arg0 *s3.DeleteObjectTaggingInput) (*request.Request, *s3.DeleteObjectTaggingOutput)
func (m *MockS3API) DeleteObjectTaggingWithContext(arg0 aws.Context, arg1 *s3.DeleteObjectTaggingInput, arg2 ...request.Option) (*s3.DeleteObjectTaggingOutput, error)
func (m *MockS3API) DeleteObjectWithContext(arg0 aws.Context, arg1 *s3.DeleteObjectInput, arg2 ...request.Option) (*s3.DeleteObjectOutput, error)
func (m *MockS3API) DeleteObjects(arg0 *s3.DeleteObjectsInput) (*s3.DeleteObjectsOutput, error)
func (m *MockS3API) DeleteObjectsRequest(arg0 *s3.DeleteObjectsInput) (*request.Request, *s3.DeleteObjectsOutput)
func (m *MockS3API) DeleteObjectsWithContext(arg0 aws.Context, arg1 *s3.DeleteObjectsInput, arg2 ...request.Option) (*s3.DeleteObjectsOutput, error)
func (m *MockS3API) DeletePublicAccessBlock(arg0 *s3.DeletePublicAccessBlockInput) (*s3.DeletePublicAccessBlockOutput, error)
func (m *MockS3API) DeletePublicAccessBlockRequest(arg0 *s3.DeletePublicAccessBlockInput) (*request.Request, *s3.DeletePublicAccessBlockOutput)
func (m *MockS3API) DeletePublicAccessBlockWithContext(arg0 aws.Context, arg1 *s3.DeletePublicAccessBlockInput, ...) (*s3.DeletePublicAccessBlockOutput, error)
func (m *MockS3API) EXPECT() *MockS3APIMockRecorder
func (m *MockS3API) GetBucketAccelerateConfiguration(arg0 *s3.GetBucketAccelerateConfigurationInput) (*s3.GetBucketAccelerateConfigurationOutput, error)
func (m *MockS3API) GetBucketAccelerateConfigurationRequest(arg0 *s3.GetBucketAccelerateConfigurationInput) (*request.Request, *s3.GetBucketAccelerateConfigurationOutput)
func (m *MockS3API) GetBucketAccelerateConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketAccelerateConfigurationInput, ...) (*s3.GetBucketAccelerateConfigurationOutput, error)
func (m *MockS3API) GetBucketAcl(arg0 *s3.GetBucketAclInput) (*s3.GetBucketAclOutput, error)
func (m *MockS3API) GetBucketAclRequest(arg0 *s3.GetBucketAclInput) (*request.Request, *s3.GetBucketAclOutput)
func (m *MockS3API) GetBucketAclWithContext(arg0 aws.Context, arg1 *s3.GetBucketAclInput, arg2 ...request.Option) (*s3.GetBucketAclOutput, error)
func (m *MockS3API) GetBucketAnalyticsConfiguration(arg0 *s3.GetBucketAnalyticsConfigurationInput) (*s3.GetBucketAnalyticsConfigurationOutput, error)
func (m *MockS3API) GetBucketAnalyticsConfigurationRequest(arg0 *s3.GetBucketAnalyticsConfigurationInput) (*request.Request, *s3.GetBucketAnalyticsConfigurationOutput)
func (m *MockS3API) GetBucketAnalyticsConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketAnalyticsConfigurationInput, ...) (*s3.GetBucketAnalyticsConfigurationOutput, error)
func (m *MockS3API) GetBucketCors(arg0 *s3.GetBucketCorsInput) (*s3.GetBucketCorsOutput, error)
func (m *MockS3API) GetBucketCorsRequest(arg0 *s3.GetBucketCorsInput) (*request.Request, *s3.GetBucketCorsOutput)
func (m *MockS3API) GetBucketCorsWithContext(arg0 aws.Context, arg1 *s3.GetBucketCorsInput, arg2 ...request.Option) (*s3.GetBucketCorsOutput, error)
func (m *MockS3API) GetBucketEncryption(arg0 *s3.GetBucketEncryptionInput) (*s3.GetBucketEncryptionOutput, error)
func (m *MockS3API) GetBucketEncryptionRequest(arg0 *s3.GetBucketEncryptionInput) (*request.Request, *s3.GetBucketEncryptionOutput)
func (m *MockS3API) GetBucketEncryptionWithContext(arg0 aws.Context, arg1 *s3.GetBucketEncryptionInput, arg2 ...request.Option) (*s3.GetBucketEncryptionOutput, error)
func (m *MockS3API) GetBucketIntelligentTieringConfiguration(arg0 *s3.GetBucketIntelligentTieringConfigurationInput) (*s3.GetBucketIntelligentTieringConfigurationOutput, error)
func (m *MockS3API) GetBucketIntelligentTieringConfigurationRequest(arg0 *s3.GetBucketIntelligentTieringConfigurationInput) (*request.Request, *s3.GetBucketIntelligentTieringConfigurationOutput)
func (m *MockS3API) GetBucketIntelligentTieringConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketIntelligentTieringConfigurationInput, ...) (*s3.GetBucketIntelligentTieringConfigurationOutput, error)
func (m *MockS3API) GetBucketInventoryConfiguration(arg0 *s3.GetBucketInventoryConfigurationInput) (*s3.GetBucketInventoryConfigurationOutput, error)
func (m *MockS3API) GetBucketInventoryConfigurationRequest(arg0 *s3.GetBucketInventoryConfigurationInput) (*request.Request, *s3.GetBucketInventoryConfigurationOutput)
func (m *MockS3API) GetBucketInventoryConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketInventoryConfigurationInput, ...) (*s3.GetBucketInventoryConfigurationOutput, error)
func (m *MockS3API) GetBucketLifecycle(arg0 *s3.GetBucketLifecycleInput) (*s3.GetBucketLifecycleOutput, error)
func (m *MockS3API) GetBucketLifecycleConfiguration(arg0 *s3.GetBucketLifecycleConfigurationInput) (*s3.GetBucketLifecycleConfigurationOutput, error)
func (m *MockS3API) GetBucketLifecycleConfigurationRequest(arg0 *s3.GetBucketLifecycleConfigurationInput) (*request.Request, *s3.GetBucketLifecycleConfigurationOutput)
func (m *MockS3API) GetBucketLifecycleConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketLifecycleConfigurationInput, ...) (*s3.GetBucketLifecycleConfigurationOutput, error)
func (m *MockS3API) GetBucketLifecycleRequest(arg0 *s3.GetBucketLifecycleInput) (*request.Request, *s3.GetBucketLifecycleOutput)
func (m *MockS3API) GetBucketLifecycleWithContext(arg0 aws.Context, arg1 *s3.GetBucketLifecycleInput, arg2 ...request.Option) (*s3.GetBucketLifecycleOutput, error)
func (m *MockS3API) GetBucketLocation(arg0 *s3.GetBucketLocationInput) (*s3.GetBucketLocationOutput, error)
func (m *MockS3API) GetBucketLocationRequest(arg0 *s3.GetBucketLocationInput) (*request.Request, *s3.GetBucketLocationOutput)
func (m *MockS3API) GetBucketLocationWithContext(arg0 aws.Context, arg1 *s3.GetBucketLocationInput, arg2 ...request.Option) (*s3.GetBucketLocationOutput, error)
func (m *MockS3API) GetBucketLogging(arg0 *s3.GetBucketLoggingInput) (*s3.GetBucketLoggingOutput, error)
func (m *MockS3API) GetBucketLoggingRequest(arg0 *s3.GetBucketLoggingInput) (*request.Request, *s3.GetBucketLoggingOutput)
func (m *MockS3API) GetBucketLoggingWithContext(arg0 aws.Context, arg1 *s3.GetBucketLoggingInput, arg2 ...request.Option) (*s3.GetBucketLoggingOutput, error)
func (m *MockS3API) GetBucketMetricsConfiguration(arg0 *s3.GetBucketMetricsConfigurationInput) (*s3.GetBucketMetricsConfigurationOutput, error)
func (m *MockS3API) GetBucketMetricsConfigurationRequest(arg0 *s3.GetBucketMetricsConfigurationInput) (*request.Request, *s3.GetBucketMetricsConfigurationOutput)
func (m *MockS3API) GetBucketMetricsConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketMetricsConfigurationInput, ...) (*s3.GetBucketMetricsConfigurationOutput, error)
func (m *MockS3API) GetBucketNotification(arg0 *s3.GetBucketNotificationConfigurationRequest) (*s3.NotificationConfigurationDeprecated, error)
func (m *MockS3API) GetBucketNotificationConfiguration(arg0 *s3.GetBucketNotificationConfigurationRequest) (*s3.NotificationConfiguration, error)
func (m *MockS3API) GetBucketNotificationConfigurationRequest(arg0 *s3.GetBucketNotificationConfigurationRequest) (*request.Request, *s3.NotificationConfiguration)
func (m *MockS3API) GetBucketNotificationConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketNotificationConfigurationRequest, ...) (*s3.NotificationConfiguration, error)
func (m *MockS3API) GetBucketNotificationRequest(arg0 *s3.GetBucketNotificationConfigurationRequest) (*request.Request, *s3.NotificationConfigurationDeprecated)
func (m *MockS3API) GetBucketNotificationWithContext(arg0 aws.Context, arg1 *s3.GetBucketNotificationConfigurationRequest, ...) (*s3.NotificationConfigurationDeprecated, error)
func (m *MockS3API) GetBucketOwnershipControls(arg0 *s3.GetBucketOwnershipControlsInput) (*s3.GetBucketOwnershipControlsOutput, error)
func (m *MockS3API) GetBucketOwnershipControlsRequest(arg0 *s3.GetBucketOwnershipControlsInput) (*request.Request, *s3.GetBucketOwnershipControlsOutput)
func (m *MockS3API) GetBucketOwnershipControlsWithContext(arg0 aws.Context, arg1 *s3.GetBucketOwnershipControlsInput, ...) (*s3.GetBucketOwnershipControlsOutput, error)
func (m *MockS3API) GetBucketPolicy(arg0 *s3.GetBucketPolicyInput) (*s3.GetBucketPolicyOutput, error)
func (m *MockS3API) GetBucketPolicyRequest(arg0 *s3.GetBucketPolicyInput) (*request.Request, *s3.GetBucketPolicyOutput)
func (m *MockS3API) GetBucketPolicyStatus(arg0 *s3.GetBucketPolicyStatusInput) (*s3.GetBucketPolicyStatusOutput, error)
func (m *MockS3API) GetBucketPolicyStatusRequest(arg0 *s3.GetBucketPolicyStatusInput) (*request.Request, *s3.GetBucketPolicyStatusOutput)
func (m *MockS3API) GetBucketPolicyStatusWithContext(arg0 aws.Context, arg1 *s3.GetBucketPolicyStatusInput, arg2 ...request.Option) (*s3.GetBucketPolicyStatusOutput, error)
func (m *MockS3API) GetBucketPolicyWithContext(arg0 aws.Context, arg1 *s3.GetBucketPolicyInput, arg2 ...request.Option) (*s3.GetBucketPolicyOutput, error)
func (m *MockS3API) GetBucketReplication(arg0 *s3.GetBucketReplicationInput) (*s3.GetBucketReplicationOutput, error)
func (m *MockS3API) GetBucketReplicationRequest(arg0 *s3.GetBucketReplicationInput) (*request.Request, *s3.GetBucketReplicationOutput)
func (m *MockS3API) GetBucketReplicationWithContext(arg0 aws.Context, arg1 *s3.GetBucketReplicationInput, arg2 ...request.Option) (*s3.GetBucketReplicationOutput, error)
func (m *MockS3API) GetBucketRequestPayment(arg0 *s3.GetBucketRequestPaymentInput) (*s3.GetBucketRequestPaymentOutput, error)
func (m *MockS3API) GetBucketRequestPaymentRequest(arg0 *s3.GetBucketRequestPaymentInput) (*request.Request, *s3.GetBucketRequestPaymentOutput)
func (m *MockS3API) GetBucketRequestPaymentWithContext(arg0 aws.Context, arg1 *s3.GetBucketRequestPaymentInput, ...) (*s3.GetBucketRequestPaymentOutput, error)
func (m *MockS3API) GetBucketTagging(arg0 *s3.GetBucketTaggingInput) (*s3.GetBucketTaggingOutput, error)
func (m *MockS3API) GetBucketTaggingRequest(arg0 *s3.GetBucketTaggingInput) (*request.Request, *s3.GetBucketTaggingOutput)
func (m *MockS3API) GetBucketTaggingWithContext(arg0 aws.Context, arg1 *s3.GetBucketTaggingInput, arg2 ...request.Option) (*s3.GetBucketTaggingOutput, error)
func (m *MockS3API) GetBucketVersioning(arg0 *s3.GetBucketVersioningInput) (*s3.GetBucketVersioningOutput, error)
func (m *MockS3API) GetBucketVersioningRequest(arg0 *s3.GetBucketVersioningInput) (*request.Request, *s3.GetBucketVersioningOutput)
func (m *MockS3API) GetBucketVersioningWithContext(arg0 aws.Context, arg1 *s3.GetBucketVersioningInput, arg2 ...request.Option) (*s3.GetBucketVersioningOutput, error)
func (m *MockS3API) GetBucketWebsite(arg0 *s3.GetBucketWebsiteInput) (*s3.GetBucketWebsiteOutput, error)
func (m *MockS3API) GetBucketWebsiteRequest(arg0 *s3.GetBucketWebsiteInput) (*request.Request, *s3.GetBucketWebsiteOutput)
func (m *MockS3API) GetBucketWebsiteWithContext(arg0 aws.Context, arg1 *s3.GetBucketWebsiteInput, arg2 ...request.Option) (*s3.GetBucketWebsiteOutput, error)
func (m *MockS3API) GetObject(arg0 *s3.GetObjectInput) (*s3.GetObjectOutput, error)
func (m *MockS3API) GetObjectAcl(arg0 *s3.GetObjectAclInput) (*s3.GetObjectAclOutput, error)
func (m *MockS3API) GetObjectAclRequest(arg0 *s3.GetObjectAclInput) (*request.Request, *s3.GetObjectAclOutput)
func (m *MockS3API) GetObjectAclWithContext(arg0 aws.Context, arg1 *s3.GetObjectAclInput, arg2 ...request.Option) (*s3.GetObjectAclOutput, error)
func (m *MockS3API) GetObjectAttributes(arg0 *s3.GetObjectAttributesInput) (*s3.GetObjectAttributesOutput, error)
func (m *MockS3API) GetObjectAttributesRequest(arg0 *s3.GetObjectAttributesInput) (*request.Request, *s3.GetObjectAttributesOutput)
func (m *MockS3API) GetObjectAttributesWithContext(arg0 aws.Context, arg1 *s3.GetObjectAttributesInput, arg2 ...request.Option) (*s3.GetObjectAttributesOutput, error)
func (m *MockS3API) GetObjectLegalHold(arg0 *s3.GetObjectLegalHoldInput) (*s3.GetObjectLegalHoldOutput, error)
func (m *MockS3API) GetObjectLegalHoldRequest(arg0 *s3.GetObjectLegalHoldInput) (*request.Request, *s3.GetObjectLegalHoldOutput)
func (m *MockS3API) GetObjectLegalHoldWithContext(arg0 aws.Context, arg1 *s3.GetObjectLegalHoldInput, arg2 ...request.Option) (*s3.GetObjectLegalHoldOutput, error)
func (m *MockS3API) GetObjectLockConfiguration(arg0 *s3.GetObjectLockConfigurationInput) (*s3.GetObjectLockConfigurationOutput, error)
func (m *MockS3API) GetObjectLockConfigurationRequest(arg0 *s3.GetObjectLockConfigurationInput) (*request.Request, *s3.GetObjectLockConfigurationOutput)
func (m *MockS3API) GetObjectLockConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetObjectLockConfigurationInput, ...) (*s3.GetObjectLockConfigurationOutput, error)
func (m *MockS3API) GetObjectRequest(arg0 *s3.GetObjectInput) (*request.Request, *s3.GetObjectOutput)
func (m *MockS3API) GetObjectRetention(arg0 *s3.GetObjectRetentionInput) (*s3.GetObjectRetentionOutput, error)
func (m *MockS3API) GetObjectRetentionRequest(arg0 *s3.GetObjectRetentionInput) (*request.Request, *s3.GetObjectRetentionOutput)
func (m *MockS3API) GetObjectRetentionWithContext(arg0 aws.Context, arg1 *s3.GetObjectRetentionInput, arg2 ...request.Option) (*s3.GetObjectRetentionOutput, error)
func (m *MockS3API) GetObjectTagging(arg0 *s3.GetObjectTaggingInput) (*s3.GetObjectTaggingOutput, error)
func (m *MockS3API) GetObjectTaggingRequest(arg0 *s3.GetObjectTaggingInput) (*request.Request, *s3.GetObjectTaggingOutput)
func (m *MockS3API) GetObjectTaggingWithContext(arg0 aws.Context, arg1 *s3.GetObjectTaggingInput, arg2 ...request.Option) (*s3.GetObjectTaggingOutput, error)
func (m *MockS3API) GetObjectTorrent(arg0 *s3.GetObjectTorrentInput) (*s3.GetObjectTorrentOutput, error)
func (m *MockS3API) GetObjectTorrentRequest(arg0 *s3.GetObjectTorrentInput) (*request.Request, *s3.GetObjectTorrentOutput)
func (m *MockS3API) GetObjectTorrentWithContext(arg0 aws.Context, arg1 *s3.GetObjectTorrentInput, arg2 ...request.Option) (*s3.GetObjectTorrentOutput, error)
func (m *MockS3API) GetObjectWithContext(arg0 aws.Context, arg1 *s3.GetObjectInput, arg2 ...request.Option) (*s3.GetObjectOutput, error)
func (m *MockS3API) GetPublicAccessBlock(arg0 *s3.GetPublicAccessBlockInput) (*s3.GetPublicAccessBlockOutput, error)
func (m *MockS3API) GetPublicAccessBlockRequest(arg0 *s3.GetPublicAccessBlockInput) (*request.Request, *s3.GetPublicAccessBlockOutput)
func (m *MockS3API) GetPublicAccessBlockWithContext(arg0 aws.Context, arg1 *s3.GetPublicAccessBlockInput, arg2 ...request.Option) (*s3.GetPublicAccessBlockOutput, error)
func (m *MockS3API) HeadBucket(arg0 *s3.HeadBucketInput) (*s3.HeadBucketOutput, error)
func (m *MockS3API) HeadBucketRequest(arg0 *s3.HeadBucketInput) (*request.Request, *s3.HeadBucketOutput)
func (m *MockS3API) HeadBucketWithContext(arg0 aws.Context, arg1 *s3.HeadBucketInput, arg2 ...request.Option) (*s3.HeadBucketOutput, error)
func (m *MockS3API) HeadObject(arg0 *s3.HeadObjectInput) (*s3.HeadObjectOutput, error)
func (m *MockS3API) HeadObjectRequest(arg0 *s3.HeadObjectInput) (*request.Request, *s3.HeadObjectOutput)
func (m *MockS3API) HeadObjectWithContext(arg0 aws.Context, arg1 *s3.HeadObjectInput, arg2 ...request.Option) (*s3.HeadObjectOutput, error)
func (m *MockS3API) ListBucketAnalyticsConfigurations(arg0 *s3.ListBucketAnalyticsConfigurationsInput) (*s3.ListBucketAnalyticsConfigurationsOutput, error)
func (m *MockS3API) ListBucketAnalyticsConfigurationsRequest(arg0 *s3.ListBucketAnalyticsConfigurationsInput) (*request.Request, *s3.ListBucketAnalyticsConfigurationsOutput)
func (m *MockS3API) ListBucketAnalyticsConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketAnalyticsConfigurationsInput, ...) (*s3.ListBucketAnalyticsConfigurationsOutput, error)
func (m *MockS3API) ListBucketIntelligentTieringConfigurations(arg0 *s3.ListBucketIntelligentTieringConfigurationsInput) (*s3.ListBucketIntelligentTieringConfigurationsOutput, error)
func (m *MockS3API) ListBucketIntelligentTieringConfigurationsRequest(arg0 *s3.ListBucketIntelligentTieringConfigurationsInput) (*request.Request, *s3.ListBucketIntelligentTieringConfigurationsOutput)
func (m *MockS3API) ListBucketIntelligentTieringConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketIntelligentTieringConfigurationsInput, ...) (*s3.ListBucketIntelligentTieringConfigurationsOutput, error)
func (m *MockS3API) ListBucketInventoryConfigurations(arg0 *s3.ListBucketInventoryConfigurationsInput) (*s3.ListBucketInventoryConfigurationsOutput, error)
func (m *MockS3API) ListBucketInventoryConfigurationsRequest(arg0 *s3.ListBucketInventoryConfigurationsInput) (*request.Request, *s3.ListBucketInventoryConfigurationsOutput)
func (m *MockS3API) ListBucketInventoryConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketInventoryConfigurationsInput, ...) (*s3.ListBucketInventoryConfigurationsOutput, error)
func (m *MockS3API) ListBucketMetricsConfigurations(arg0 *s3.ListBucketMetricsConfigurationsInput) (*s3.ListBucketMetricsConfigurationsOutput, error)
func (m *MockS3API) ListBucketMetricsConfigurationsRequest(arg0 *s3.ListBucketMetricsConfigurationsInput) (*request.Request, *s3.ListBucketMetricsConfigurationsOutput)
func (m *MockS3API) ListBucketMetricsConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketMetricsConfigurationsInput, ...) (*s3.ListBucketMetricsConfigurationsOutput, error)
func (m *MockS3API) ListBuckets(arg0 *s3.ListBucketsInput) (*s3.ListBucketsOutput, error)
func (m *MockS3API) ListBucketsRequest(arg0 *s3.ListBucketsInput) (*request.Request, *s3.ListBucketsOutput)
func (m *MockS3API) ListBucketsWithContext(arg0 aws.Context, arg1 *s3.ListBucketsInput, arg2 ...request.Option) (*s3.ListBucketsOutput, error)
func (m *MockS3API) ListDirectoryBuckets(arg0 *s3.ListDirectoryBucketsInput) (*s3.ListDirectoryBucketsOutput, error)
func (m *MockS3API) ListDirectoryBucketsPages(arg0 *s3.ListDirectoryBucketsInput, ...) error
func (m *MockS3API) ListDirectoryBucketsPagesWithContext(arg0 aws.Context, arg1 *s3.ListDirectoryBucketsInput, ...) error
func (m *MockS3API) ListDirectoryBucketsRequest(arg0 *s3.ListDirectoryBucketsInput) (*request.Request, *s3.ListDirectoryBucketsOutput)
func (m *MockS3API) ListDirectoryBucketsWithContext(arg0 aws.Context, arg1 *s3.ListDirectoryBucketsInput, arg2 ...request.Option) (*s3.ListDirectoryBucketsOutput, error)
func (m *MockS3API) ListMultipartUploads(arg0 *s3.ListMultipartUploadsInput) (*s3.ListMultipartUploadsOutput, error)
func (m *MockS3API) ListMultipartUploadsPages(arg0 *s3.ListMultipartUploadsInput, ...) error
func (m *MockS3API) ListMultipartUploadsPagesWithContext(arg0 aws.Context, arg1 *s3.ListMultipartUploadsInput, ...) error
func (m *MockS3API) ListMultipartUploadsRequest(arg0 *s3.ListMultipartUploadsInput) (*request.Request, *s3.ListMultipartUploadsOutput)
func (m *MockS3API) ListMultipartUploadsWithContext(arg0 aws.Context, arg1 *s3.ListMultipartUploadsInput, arg2 ...request.Option) (*s3.ListMultipartUploadsOutput, error)
func (m *MockS3API) ListObjectVersions(arg0 *s3.ListObjectVersionsInput) (*s3.ListObjectVersionsOutput, error)
func (m *MockS3API) ListObjectVersionsPages(arg0 *s3.ListObjectVersionsInput, ...) error
func (m *MockS3API) ListObjectVersionsPagesWithContext(arg0 aws.Context, arg1 *s3.ListObjectVersionsInput, ...) error
func (m *MockS3API) ListObjectVersionsRequest(arg0 *s3.ListObjectVersionsInput) (*request.Request, *s3.ListObjectVersionsOutput)
func (m *MockS3API) ListObjectVersionsWithContext(arg0 aws.Context, arg1 *s3.ListObjectVersionsInput, arg2 ...request.Option) (*s3.ListObjectVersionsOutput, error)
func (m *MockS3API) ListObjects(arg0 *s3.ListObjectsInput) (*s3.ListObjectsOutput, error)
func (m *MockS3API) ListObjectsPages(arg0 *s3.ListObjectsInput, arg1 func(*s3.ListObjectsOutput, bool) bool) error
func (m *MockS3API) ListObjectsPagesWithContext(arg0 aws.Context, arg1 *s3.ListObjectsInput, ...) error
func (m *MockS3API) ListObjectsRequest(arg0 *s3.ListObjectsInput) (*request.Request, *s3.ListObjectsOutput)
func (m *MockS3API) ListObjectsV2(arg0 *s3.ListObjectsV2Input) (*s3.ListObjectsV2Output, error)
func (m *MockS3API) ListObjectsV2Pages(arg0 *s3.ListObjectsV2Input, arg1 func(*s3.ListObjectsV2Output, bool) bool) error
func (m *MockS3API) ListObjectsV2PagesWithContext(arg0 aws.Context, arg1 *s3.ListObjectsV2Input, ...) error
func (m *MockS3API) ListObjectsV2Request(arg0 *s3.ListObjectsV2Input) (*request.Request, *s3.ListObjectsV2Output)
func (m *MockS3API) ListObjectsV2WithContext(arg0 aws.Context, arg1 *s3.ListObjectsV2Input, arg2 ...request.Option) (*s3.ListObjectsV2Output, error)
func (m *MockS3API) ListObjectsWithContext(arg0 aws.Context, arg1 *s3.ListObjectsInput, arg2 ...request.Option) (*s3.ListObjectsOutput, error)
func (m *MockS3API) ListParts(arg0 *s3.ListPartsInput) (*s3.ListPartsOutput, error)
func (m *MockS3API) ListPartsPages(arg0 *s3.ListPartsInput, arg1 func(*s3.ListPartsOutput, bool) bool) error
func (m *MockS3API) ListPartsPagesWithContext(arg0 aws.Context, arg1 *s3.ListPartsInput, ...) error
func (m *MockS3API) ListPartsRequest(arg0 *s3.ListPartsInput) (*request.Request, *s3.ListPartsOutput)
func (m *MockS3API) ListPartsWithContext(arg0 aws.Context, arg1 *s3.ListPartsInput, arg2 ...request.Option) (*s3.ListPartsOutput, error)
func (m *MockS3API) PutBucketAccelerateConfiguration(arg0 *s3.PutBucketAccelerateConfigurationInput) (*s3.PutBucketAccelerateConfigurationOutput, error)
func (m *MockS3API) PutBucketAccelerateConfigurationRequest(arg0 *s3.PutBucketAccelerateConfigurationInput) (*request.Request, *s3.PutBucketAccelerateConfigurationOutput)
func (m *MockS3API) PutBucketAccelerateConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketAccelerateConfigurationInput, ...) (*s3.PutBucketAccelerateConfigurationOutput, error)
func (m *MockS3API) PutBucketAcl(arg0 *s3.PutBucketAclInput) (*s3.PutBucketAclOutput, error)
func (m *MockS3API) PutBucketAclRequest(arg0 *s3.PutBucketAclInput) (*request.Request, *s3.PutBucketAclOutput)
func (m *MockS3API) PutBucketAclWithContext(arg0 aws.Context, arg1 *s3.PutBucketAclInput, arg2 ...request.Option) (*s3.PutBucketAclOutput, error)
func (m *MockS3API) PutBucketAnalyticsConfiguration(arg0 *s3.PutBucketAnalyticsConfigurationInput) (*s3.PutBucketAnalyticsConfigurationOutput, error)
func (m *MockS3API) PutBucketAnalyticsConfigurationRequest(arg0 *s3.PutBucketAnalyticsConfigurationInput) (*request.Request, *s3.PutBucketAnalyticsConfigurationOutput)
func (m *MockS3API) PutBucketAnalyticsConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketAnalyticsConfigurationInput, ...) (*s3.PutBucketAnalyticsConfigurationOutput, error)
func (m *MockS3API) PutBucketCors(arg0 *s3.PutBucketCorsInput) (*s3.PutBucketCorsOutput, error)
func (m *MockS3API) PutBucketCorsRequest(arg0 *s3.PutBucketCorsInput) (*request.Request, *s3.PutBucketCorsOutput)
func (m *MockS3API) PutBucketCorsWithContext(arg0 aws.Context, arg1 *s3.PutBucketCorsInput, arg2 ...request.Option) (*s3.PutBucketCorsOutput, error)
func (m *MockS3API) PutBucketEncryption(arg0 *s3.PutBucketEncryptionInput) (*s3.PutBucketEncryptionOutput, error)
func (m *MockS3API) PutBucketEncryptionRequest(arg0 *s3.PutBucketEncryptionInput) (*request.Request, *s3.PutBucketEncryptionOutput)
func (m *MockS3API) PutBucketEncryptionWithContext(arg0 aws.Context, arg1 *s3.PutBucketEncryptionInput, arg2 ...request.Option) (*s3.PutBucketEncryptionOutput, error)
func (m *MockS3API) PutBucketIntelligentTieringConfiguration(arg0 *s3.PutBucketIntelligentTieringConfigurationInput) (*s3.PutBucketIntelligentTieringConfigurationOutput, error)
func (m *MockS3API) PutBucketIntelligentTieringConfigurationRequest(arg0 *s3.PutBucketIntelligentTieringConfigurationInput) (*request.Request, *s3.PutBucketIntelligentTieringConfigurationOutput)
func (m *MockS3API) PutBucketIntelligentTieringConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketIntelligentTieringConfigurationInput, ...) (*s3.PutBucketIntelligentTieringConfigurationOutput, error)
func (m *MockS3API) PutBucketInventoryConfiguration(arg0 *s3.PutBucketInventoryConfigurationInput) (*s3.PutBucketInventoryConfigurationOutput, error)
func (m *MockS3API) PutBucketInventoryConfigurationRequest(arg0 *s3.PutBucketInventoryConfigurationInput) (*request.Request, *s3.PutBucketInventoryConfigurationOutput)
func (m *MockS3API) PutBucketInventoryConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketInventoryConfigurationInput, ...) (*s3.PutBucketInventoryConfigurationOutput, error)
func (m *MockS3API) PutBucketLifecycle(arg0 *s3.PutBucketLifecycleInput) (*s3.PutBucketLifecycleOutput, error)
func (m *MockS3API) PutBucketLifecycleConfiguration(arg0 *s3.PutBucketLifecycleConfigurationInput) (*s3.PutBucketLifecycleConfigurationOutput, error)
func (m *MockS3API) PutBucketLifecycleConfigurationRequest(arg0 *s3.PutBucketLifecycleConfigurationInput) (*request.Request, *s3.PutBucketLifecycleConfigurationOutput)
func (m *MockS3API) PutBucketLifecycleConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketLifecycleConfigurationInput, ...) (*s3.PutBucketLifecycleConfigurationOutput, error)
func (m *MockS3API) PutBucketLifecycleRequest(arg0 *s3.PutBucketLifecycleInput) (*request.Request, *s3.PutBucketLifecycleOutput)
func (m *MockS3API) PutBucketLifecycleWithContext(arg0 aws.Context, arg1 *s3.PutBucketLifecycleInput, arg2 ...request.Option) (*s3.PutBucketLifecycleOutput, error)
func (m *MockS3API) PutBucketLogging(arg0 *s3.PutBucketLoggingInput) (*s3.PutBucketLoggingOutput, error)
func (m *MockS3API) PutBucketLoggingRequest(arg0 *s3.PutBucketLoggingInput) (*request.Request, *s3.PutBucketLoggingOutput)
func (m *MockS3API) PutBucketLoggingWithContext(arg0 aws.Context, arg1 *s3.PutBucketLoggingInput, arg2 ...request.Option) (*s3.PutBucketLoggingOutput, error)
func (m *MockS3API) PutBucketMetricsConfiguration(arg0 *s3.PutBucketMetricsConfigurationInput) (*s3.PutBucketMetricsConfigurationOutput, error)
func (m *MockS3API) PutBucketMetricsConfigurationRequest(arg0 *s3.PutBucketMetricsConfigurationInput) (*request.Request, *s3.PutBucketMetricsConfigurationOutput)
func (m *MockS3API) PutBucketMetricsConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketMetricsConfigurationInput, ...) (*s3.PutBucketMetricsConfigurationOutput, error)
func (m *MockS3API) PutBucketNotification(arg0 *s3.PutBucketNotificationInput) (*s3.PutBucketNotificationOutput, error)
func (m *MockS3API) PutBucketNotificationConfiguration(arg0 *s3.PutBucketNotificationConfigurationInput) (*s3.PutBucketNotificationConfigurationOutput, error)
func (m *MockS3API) PutBucketNotificationConfigurationRequest(arg0 *s3.PutBucketNotificationConfigurationInput) (*request.Request, *s3.PutBucketNotificationConfigurationOutput)
func (m *MockS3API) PutBucketNotificationConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketNotificationConfigurationInput, ...) (*s3.PutBucketNotificationConfigurationOutput, error)
func (m *MockS3API) PutBucketNotificationRequest(arg0 *s3.PutBucketNotificationInput) (*request.Request, *s3.PutBucketNotificationOutput)
func (m *MockS3API) PutBucketNotificationWithContext(arg0 aws.Context, arg1 *s3.PutBucketNotificationInput, arg2 ...request.Option) (*s3.PutBucketNotificationOutput, error)
func (m *MockS3API) PutBucketOwnershipControls(arg0 *s3.PutBucketOwnershipControlsInput) (*s3.PutBucketOwnershipControlsOutput, error)
func (m *MockS3API) PutBucketOwnershipControlsRequest(arg0 *s3.PutBucketOwnershipControlsInput) (*request.Request, *s3.PutBucketOwnershipControlsOutput)
func (m *MockS3API) PutBucketOwnershipControlsWithContext(arg0 aws.Context, arg1 *s3.PutBucketOwnershipControlsInput, ...) (*s3.PutBucketOwnershipControlsOutput, error)
func (m *MockS3API) PutBucketPolicy(arg0 *s3.PutBucketPolicyInput) (*s3.PutBucketPolicyOutput, error)
func (m *MockS3API) PutBucketPolicyRequest(arg0 *s3.PutBucketPolicyInput) (*request.Request, *s3.PutBucketPolicyOutput)
func (m *MockS3API) PutBucketPolicyWithContext(arg0 aws.Context, arg1 *s3.PutBucketPolicyInput, arg2 ...request.Option) (*s3.PutBucketPolicyOutput, error)
func (m *MockS3API) PutBucketReplication(arg0 *s3.PutBucketReplicationInput) (*s3.PutBucketReplicationOutput, error)
func (m *MockS3API) PutBucketReplicationRequest(arg0 *s3.PutBucketReplicationInput) (*request.Request, *s3.PutBucketReplicationOutput)
func (m *MockS3API) PutBucketReplicationWithContext(arg0 aws.Context, arg1 *s3.PutBucketReplicationInput, arg2 ...request.Option) (*s3.PutBucketReplicationOutput, error)
func (m *MockS3API) PutBucketRequestPayment(arg0 *s3.PutBucketRequestPaymentInput) (*s3.PutBucketRequestPaymentOutput, error)
func (m *MockS3API) PutBucketRequestPaymentRequest(arg0 *s3.PutBucketRequestPaymentInput) (*request.Request, *s3.PutBucketRequestPaymentOutput)
func (m *MockS3API) PutBucketRequestPaymentWithContext(arg0 aws.Context, arg1 *s3.PutBucketRequestPaymentInput, ...) (*s3.PutBucketRequestPaymentOutput, error)
func (m *MockS3API) PutBucketTagging(arg0 *s3.PutBucketTaggingInput) (*s3.PutBucketTaggingOutput, error)
func (m *MockS3API) PutBucketTaggingRequest(arg0 *s3.PutBucketTaggingInput) (*request.Request, *s3.PutBucketTaggingOutput)
func (m *MockS3API) PutBucketTaggingWithContext(arg0 aws.Context, arg1 *s3.PutBucketTaggingInput, arg2 ...request.Option) (*s3.PutBucketTaggingOutput, error)
func (m *MockS3API) PutBucketVersioning(arg0 *s3.PutBucketVersioningInput) (*s3.PutBucketVersioningOutput, error)
func (m *MockS3API) PutBucketVersioningRequest(arg0 *s3.PutBucketVersioningInput) (*request.Request, *s3.PutBucketVersioningOutput)
func (m *MockS3API) PutBucketVersioningWithContext(arg0 aws.Context, arg1 *s3.PutBucketVersioningInput, arg2 ...request.Option) (*s3.PutBucketVersioningOutput, error)
func (m *MockS3API) PutBucketWebsite(arg0 *s3.PutBucketWebsiteInput) (*s3.PutBucketWebsiteOutput, error)
func (m *MockS3API) PutBucketWebsiteRequest(arg0 *s3.PutBucketWebsiteInput) (*request.Request, *s3.PutBucketWebsiteOutput)
func (m *MockS3API) PutBucketWebsiteWithContext(arg0 aws.Context, arg1 *s3.PutBucketWebsiteInput, arg2 ...request.Option) (*s3.PutBucketWebsiteOutput, error)
func (m *MockS3API) PutObject(arg0 *s3.PutObjectInput) (*s3.PutObjectOutput, error)
func (m *MockS3API) PutObjectAcl(arg0 *s3.PutObjectAclInput) (*s3.PutObjectAclOutput, error)
func (m *MockS3API) PutObjectAclRequest(arg0 *s3.PutObjectAclInput) (*request.Request, *s3.PutObjectAclOutput)
func (m *MockS3API) PutObjectAclWithContext(arg0 aws.Context, arg1 *s3.PutObjectAclInput, arg2 ...request.Option) (*s3.PutObjectAclOutput, error)
func (m *MockS3API) PutObjectLegalHold(arg0 *s3.PutObjectLegalHoldInput) (*s3.PutObjectLegalHoldOutput, error)
func (m *MockS3API) PutObjectLegalHoldRequest(arg0 *s3.PutObjectLegalHoldInput) (*request.Request, *s3.PutObjectLegalHoldOutput)
func (m *MockS3API) PutObjectLegalHoldWithContext(arg0 aws.Context, arg1 *s3.PutObjectLegalHoldInput, arg2 ...request.Option) (*s3.PutObjectLegalHoldOutput, error)
func (m *MockS3API) PutObjectLockConfiguration(arg0 *s3.PutObjectLockConfigurationInput) (*s3.PutObjectLockConfigurationOutput, error)
func (m *MockS3API) PutObjectLockConfigurationRequest(arg0 *s3.PutObjectLockConfigurationInput) (*request.Request, *s3.PutObjectLockConfigurationOutput)
func (m *MockS3API) PutObjectLockConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutObjectLockConfigurationInput, ...) (*s3.PutObjectLockConfigurationOutput, error)
func (m *MockS3API) PutObjectRequest(arg0 *s3.PutObjectInput) (*request.Request, *s3.PutObjectOutput)
func (m *MockS3API) PutObjectRetention(arg0 *s3.PutObjectRetentionInput) (*s3.PutObjectRetentionOutput, error)
func (m *MockS3API) PutObjectRetentionRequest(arg0 *s3.PutObjectRetentionInput) (*request.Request, *s3.PutObjectRetentionOutput)
func (m *MockS3API) PutObjectRetentionWithContext(arg0 aws.Context, arg1 *s3.PutObjectRetentionInput, arg2 ...request.Option) (*s3.PutObjectRetentionOutput, error)
func (m *MockS3API) PutObjectTagging(arg0 *s3.PutObjectTaggingInput) (*s3.PutObjectTaggingOutput, error)
func (m *MockS3API) PutObjectTaggingRequest(arg0 *s3.PutObjectTaggingInput) (*request.Request, *s3.PutObjectTaggingOutput)
func (m *MockS3API) PutObjectTaggingWithContext(arg0 aws.Context, arg1 *s3.PutObjectTaggingInput, arg2 ...request.Option) (*s3.PutObjectTaggingOutput, error)
func (m *MockS3API) PutObjectWithContext(arg0 aws.Context, arg1 *s3.PutObjectInput, arg2 ...request.Option) (*s3.PutObjectOutput, error)
func (m *MockS3API) PutPublicAccessBlock(arg0 *s3.PutPublicAccessBlockInput) (*s3.PutPublicAccessBlockOutput, error)
func (m *MockS3API) PutPublicAccessBlockRequest(arg0 *s3.PutPublicAccessBlockInput) (*request.Request, *s3.PutPublicAccessBlockOutput)
func (m *MockS3API) PutPublicAccessBlockWithContext(arg0 aws.Context, arg1 *s3.PutPublicAccessBlockInput, arg2 ...request.Option) (*s3.PutPublicAccessBlockOutput, error)
func (m *MockS3API) RestoreObject(arg0 *s3.RestoreObjectInput) (*s3.RestoreObjectOutput, error)
func (m *MockS3API) RestoreObjectRequest(arg0 *s3.RestoreObjectInput) (*request.Request, *s3.RestoreObjectOutput)
func (m *MockS3API) RestoreObjectWithContext(arg0 aws.Context, arg1 *s3.RestoreObjectInput, arg2 ...request.Option) (*s3.RestoreObjectOutput, error)
func (m *MockS3API) SelectObjectContent(arg0 *s3.SelectObjectContentInput) (*s3.SelectObjectContentOutput, error)
func (m *MockS3API) SelectObjectContentRequest(arg0 *s3.SelectObjectContentInput) (*request.Request, *s3.SelectObjectContentOutput)
func (m *MockS3API) SelectObjectContentWithContext(arg0 aws.Context, arg1 *s3.SelectObjectContentInput, arg2 ...request.Option) (*s3.SelectObjectContentOutput, error)
func (m *MockS3API) UploadPart(arg0 *s3.UploadPartInput) (*s3.UploadPartOutput, error)
func (m *MockS3API) UploadPartCopy(arg0 *s3.UploadPartCopyInput) (*s3.UploadPartCopyOutput, error)
func (m *MockS3API) UploadPartCopyRequest(arg0 *s3.UploadPartCopyInput) (*request.Request, *s3.UploadPartCopyOutput)
func (m *MockS3API) UploadPartCopyWithContext(arg0 aws.Context, arg1 *s3.UploadPartCopyInput, arg2 ...request.Option) (*s3.UploadPartCopyOutput, error)
func (m *MockS3API) UploadPartRequest(arg0 *s3.UploadPartInput) (*request.Request, *s3.UploadPartOutput)
func (m *MockS3API) UploadPartWithContext(arg0 aws.Context, arg1 *s3.UploadPartInput, arg2 ...request.Option) (*s3.UploadPartOutput, error)
func (m *MockS3API) WaitUntilBucketExists(arg0 *s3.HeadBucketInput) error
func (m *MockS3API) WaitUntilBucketExistsWithContext(arg0 aws.Context, arg1 *s3.HeadBucketInput, arg2 ...request.WaiterOption) error
func (m *MockS3API) WaitUntilBucketNotExists(arg0 *s3.HeadBucketInput) error
func (m *MockS3API) WaitUntilBucketNotExistsWithContext(arg0 aws.Context, arg1 *s3.HeadBucketInput, arg2 ...request.WaiterOption) error
func (m *MockS3API) WaitUntilObjectExists(arg0 *s3.HeadObjectInput) error
func (m *MockS3API) WaitUntilObjectExistsWithContext(arg0 aws.Context, arg1 *s3.HeadObjectInput, arg2 ...request.WaiterOption) error
func (m *MockS3API) WaitUntilObjectNotExists(arg0 *s3.HeadObjectInput) error
func (m *MockS3API) WaitUntilObjectNotExistsWithContext(arg0 aws.Context, arg1 *s3.HeadObjectInput, arg2 ...request.WaiterOption) error
func (m *MockS3API) WriteGetObjectResponse(arg0 *s3.WriteGetObjectResponseInput) (*s3.WriteGetObjectResponseOutput, error)
func (m *MockS3API) WriteGetObjectResponseRequest(arg0 *s3.WriteGetObjectResponseInput) (*request.Request, *s3.WriteGetObjectResponseOutput)
func (m *MockS3API) WriteGetObjectResponseWithContext(arg0 aws.Context, arg1 *s3.WriteGetObjectResponseInput, arg2 ...request.Option) (*s3.WriteGetObjectResponseOutput, error)
type MockS3APIMockRecorder
func (mr *MockS3APIMockRecorder) AbortMultipartUpload(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) AbortMultipartUploadRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) AbortMultipartUploadWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) CompleteMultipartUpload(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CompleteMultipartUploadRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CompleteMultipartUploadWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) CopyObject(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CopyObjectRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CopyObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateBucket(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateBucketRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateBucketWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateMultipartUpload(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateMultipartUploadRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateMultipartUploadWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateSession(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateSessionRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) CreateSessionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucket(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketAnalyticsConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketAnalyticsConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketAnalyticsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketCors(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketCorsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketCorsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketEncryption(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketEncryptionRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketEncryptionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketInventoryConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketInventoryConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketInventoryConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketLifecycle(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketLifecycleRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketLifecycleWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketMetricsConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketMetricsConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketMetricsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketOwnershipControls(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketOwnershipControlsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketOwnershipControlsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketPolicy(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketPolicyRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketPolicyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketReplication(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketReplicationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketReplicationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketTagging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketTaggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketWebsite(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketWebsiteRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketWebsiteWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteBucketWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObject(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectTagging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectTaggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjects(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeleteObjectsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeletePublicAccessBlock(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeletePublicAccessBlockRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) DeletePublicAccessBlockWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAccelerateConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAccelerateConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAccelerateConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAcl(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAclRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAnalyticsConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAnalyticsConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketAnalyticsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketCors(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketCorsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketCorsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketEncryption(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketEncryptionRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketEncryptionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketIntelligentTieringConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketIntelligentTieringConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketIntelligentTieringConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketInventoryConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketInventoryConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketInventoryConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLifecycle(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLifecycleConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLifecycleConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLifecycleConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLifecycleRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLifecycleWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLocation(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLocationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLocationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLogging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLoggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketLoggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketMetricsConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketMetricsConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketMetricsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketNotification(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketNotificationConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketNotificationConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketNotificationConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketNotificationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketNotificationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketOwnershipControls(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketOwnershipControlsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketOwnershipControlsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketPolicy(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketPolicyRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketPolicyStatus(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketPolicyStatusRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketPolicyStatusWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketPolicyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketReplication(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketReplicationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketReplicationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketRequestPayment(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketRequestPaymentRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketRequestPaymentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketTagging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketTaggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketVersioning(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketVersioningRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketVersioningWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketWebsite(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketWebsiteRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetBucketWebsiteWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObject(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectAcl(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectAclRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectAttributes(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectAttributesRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectAttributesWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectLegalHold(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectLegalHoldRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectLegalHoldWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectLockConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectLockConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectLockConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectRetention(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectRetentionRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectRetentionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectTagging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectTaggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectTorrent(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectTorrentRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectTorrentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetPublicAccessBlock(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetPublicAccessBlockRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) GetPublicAccessBlockWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) HeadBucket(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) HeadBucketRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) HeadBucketWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) HeadObject(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) HeadObjectRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) HeadObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketAnalyticsConfigurations(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketAnalyticsConfigurationsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketAnalyticsConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurations(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurationsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketInventoryConfigurations(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketInventoryConfigurationsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketInventoryConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketMetricsConfigurations(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketMetricsConfigurationsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketMetricsConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBuckets(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListBucketsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListDirectoryBuckets(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsPages(arg0, arg1 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListMultipartUploads(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListMultipartUploadsPages(arg0, arg1 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListMultipartUploadsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListMultipartUploadsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListMultipartUploadsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectVersions(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectVersionsPages(arg0, arg1 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectVersionsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectVersionsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectVersionsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjects(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsPages(arg0, arg1 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsV2(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsV2Pages(arg0, arg1 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsV2PagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsV2Request(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsV2WithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListObjectsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListParts(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListPartsPages(arg0, arg1 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListPartsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListPartsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) ListPartsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAccelerateConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAccelerateConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAccelerateConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAcl(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAclRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAnalyticsConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAnalyticsConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketAnalyticsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketCors(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketCorsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketCorsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketEncryption(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketEncryptionRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketEncryptionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketIntelligentTieringConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketIntelligentTieringConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketIntelligentTieringConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketInventoryConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketInventoryConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketInventoryConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLifecycle(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLifecycleConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLifecycleConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLifecycleConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLifecycleRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLifecycleWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLogging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLoggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketLoggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketMetricsConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketMetricsConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketMetricsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketNotification(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketNotificationConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketNotificationConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketNotificationConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketNotificationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketNotificationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketOwnershipControls(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketOwnershipControlsRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketOwnershipControlsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketPolicy(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketPolicyRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketPolicyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketReplication(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketReplicationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketReplicationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketRequestPayment(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketRequestPaymentRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketRequestPaymentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketTagging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketTaggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketVersioning(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketVersioningRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketVersioningWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketWebsite(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketWebsiteRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutBucketWebsiteWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObject(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectAcl(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectAclRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectLegalHold(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectLegalHoldRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectLegalHoldWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectLockConfiguration(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectLockConfigurationRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectLockConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectRetention(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectRetentionRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectRetentionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectTagging(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectTaggingRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutPublicAccessBlock(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutPublicAccessBlockRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) PutPublicAccessBlockWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) RestoreObject(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) RestoreObjectRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) RestoreObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) SelectObjectContent(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) SelectObjectContentRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) SelectObjectContentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) UploadPart(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) UploadPartCopy(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) UploadPartCopyRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) UploadPartCopyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) UploadPartRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) UploadPartWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilBucketExists(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilBucketExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilBucketNotExists(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilBucketNotExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilObjectExists(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilObjectExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilObjectNotExists(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) WaitUntilObjectNotExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
func (mr *MockS3APIMockRecorder) WriteGetObjectResponse(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) WriteGetObjectResponseRequest(arg0 any) *gomock.Call
func (mr *MockS3APIMockRecorder) WriteGetObjectResponseWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call
Constants ¶

This section is empty.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type MockS3API ¶
added in v1.3.0
type MockS3API struct {
	// contains filtered or unexported fields
}

MockS3API is a mock of S3API interface.

func NewMockS3API ¶
added in v1.3.0
func NewMockS3API(ctrl *gomock.Controller) *MockS3API

NewMockS3API creates a new mock instance.

func (*MockS3API) AbortMultipartUpload ¶
added in v1.3.0
func (m *MockS3API) AbortMultipartUpload(arg0 *s3.AbortMultipartUploadInput) (*s3.AbortMultipartUploadOutput, error)

AbortMultipartUpload mocks base method.

func (*MockS3API) AbortMultipartUploadRequest ¶
added in v1.3.0
func (m *MockS3API) AbortMultipartUploadRequest(arg0 *s3.AbortMultipartUploadInput) (*request.Request, *s3.AbortMultipartUploadOutput)

AbortMultipartUploadRequest mocks base method.

func (*MockS3API) AbortMultipartUploadWithContext ¶
added in v1.3.0
func (m *MockS3API) AbortMultipartUploadWithContext(arg0 aws.Context, arg1 *s3.AbortMultipartUploadInput, arg2 ...request.Option) (*s3.AbortMultipartUploadOutput, error)

AbortMultipartUploadWithContext mocks base method.

func (*MockS3API) CompleteMultipartUpload ¶
added in v1.3.0
func (m *MockS3API) CompleteMultipartUpload(arg0 *s3.CompleteMultipartUploadInput) (*s3.CompleteMultipartUploadOutput, error)

CompleteMultipartUpload mocks base method.

func (*MockS3API) CompleteMultipartUploadRequest ¶
added in v1.3.0
func (m *MockS3API) CompleteMultipartUploadRequest(arg0 *s3.CompleteMultipartUploadInput) (*request.Request, *s3.CompleteMultipartUploadOutput)

CompleteMultipartUploadRequest mocks base method.

func (*MockS3API) CompleteMultipartUploadWithContext ¶
added in v1.3.0
func (m *MockS3API) CompleteMultipartUploadWithContext(arg0 aws.Context, arg1 *s3.CompleteMultipartUploadInput, arg2 ...request.Option) (*s3.CompleteMultipartUploadOutput, error)

CompleteMultipartUploadWithContext mocks base method.

func (*MockS3API) CopyObject ¶
added in v1.3.0
func (m *MockS3API) CopyObject(arg0 *s3.CopyObjectInput) (*s3.CopyObjectOutput, error)

CopyObject mocks base method.

func (*MockS3API) CopyObjectRequest ¶
added in v1.3.0
func (m *MockS3API) CopyObjectRequest(arg0 *s3.CopyObjectInput) (*request.Request, *s3.CopyObjectOutput)

CopyObjectRequest mocks base method.

func (*MockS3API) CopyObjectWithContext ¶
added in v1.3.0
func (m *MockS3API) CopyObjectWithContext(arg0 aws.Context, arg1 *s3.CopyObjectInput, arg2 ...request.Option) (*s3.CopyObjectOutput, error)

CopyObjectWithContext mocks base method.

func (*MockS3API) CreateBucket ¶
added in v1.3.0
func (m *MockS3API) CreateBucket(arg0 *s3.CreateBucketInput) (*s3.CreateBucketOutput, error)

CreateBucket mocks base method.

func (*MockS3API) CreateBucketRequest ¶
added in v1.3.0
func (m *MockS3API) CreateBucketRequest(arg0 *s3.CreateBucketInput) (*request.Request, *s3.CreateBucketOutput)

CreateBucketRequest mocks base method.

func (*MockS3API) CreateBucketWithContext ¶
added in v1.3.0
func (m *MockS3API) CreateBucketWithContext(arg0 aws.Context, arg1 *s3.CreateBucketInput, arg2 ...request.Option) (*s3.CreateBucketOutput, error)

CreateBucketWithContext mocks base method.

func (*MockS3API) CreateMultipartUpload ¶
added in v1.3.0
func (m *MockS3API) CreateMultipartUpload(arg0 *s3.CreateMultipartUploadInput) (*s3.CreateMultipartUploadOutput, error)

CreateMultipartUpload mocks base method.

func (*MockS3API) CreateMultipartUploadRequest ¶
added in v1.3.0
func (m *MockS3API) CreateMultipartUploadRequest(arg0 *s3.CreateMultipartUploadInput) (*request.Request, *s3.CreateMultipartUploadOutput)

CreateMultipartUploadRequest mocks base method.

func (*MockS3API) CreateMultipartUploadWithContext ¶
added in v1.3.0
func (m *MockS3API) CreateMultipartUploadWithContext(arg0 aws.Context, arg1 *s3.CreateMultipartUploadInput, arg2 ...request.Option) (*s3.CreateMultipartUploadOutput, error)

CreateMultipartUploadWithContext mocks base method.

func (*MockS3API) CreateSession ¶
added in v1.23.1
func (m *MockS3API) CreateSession(arg0 *s3.CreateSessionInput) (*s3.CreateSessionOutput, error)

CreateSession mocks base method.

func (*MockS3API) CreateSessionRequest ¶
added in v1.23.1
func (m *MockS3API) CreateSessionRequest(arg0 *s3.CreateSessionInput) (*request.Request, *s3.CreateSessionOutput)

CreateSessionRequest mocks base method.

func (*MockS3API) CreateSessionWithContext ¶
added in v1.23.1
func (m *MockS3API) CreateSessionWithContext(arg0 aws.Context, arg1 *s3.CreateSessionInput, arg2 ...request.Option) (*s3.CreateSessionOutput, error)

CreateSessionWithContext mocks base method.

func (*MockS3API) DeleteBucket ¶
added in v1.3.0
func (m *MockS3API) DeleteBucket(arg0 *s3.DeleteBucketInput) (*s3.DeleteBucketOutput, error)

DeleteBucket mocks base method.

func (*MockS3API) DeleteBucketAnalyticsConfiguration ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketAnalyticsConfiguration(arg0 *s3.DeleteBucketAnalyticsConfigurationInput) (*s3.DeleteBucketAnalyticsConfigurationOutput, error)

DeleteBucketAnalyticsConfiguration mocks base method.

func (*MockS3API) DeleteBucketAnalyticsConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketAnalyticsConfigurationRequest(arg0 *s3.DeleteBucketAnalyticsConfigurationInput) (*request.Request, *s3.DeleteBucketAnalyticsConfigurationOutput)

DeleteBucketAnalyticsConfigurationRequest mocks base method.

func (*MockS3API) DeleteBucketAnalyticsConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketAnalyticsConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketAnalyticsConfigurationInput, arg2 ...request.Option) (*s3.DeleteBucketAnalyticsConfigurationOutput, error)

DeleteBucketAnalyticsConfigurationWithContext mocks base method.

func (*MockS3API) DeleteBucketCors ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketCors(arg0 *s3.DeleteBucketCorsInput) (*s3.DeleteBucketCorsOutput, error)

DeleteBucketCors mocks base method.

func (*MockS3API) DeleteBucketCorsRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketCorsRequest(arg0 *s3.DeleteBucketCorsInput) (*request.Request, *s3.DeleteBucketCorsOutput)

DeleteBucketCorsRequest mocks base method.

func (*MockS3API) DeleteBucketCorsWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketCorsWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketCorsInput, arg2 ...request.Option) (*s3.DeleteBucketCorsOutput, error)

DeleteBucketCorsWithContext mocks base method.

func (*MockS3API) DeleteBucketEncryption ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketEncryption(arg0 *s3.DeleteBucketEncryptionInput) (*s3.DeleteBucketEncryptionOutput, error)

DeleteBucketEncryption mocks base method.

func (*MockS3API) DeleteBucketEncryptionRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketEncryptionRequest(arg0 *s3.DeleteBucketEncryptionInput) (*request.Request, *s3.DeleteBucketEncryptionOutput)

DeleteBucketEncryptionRequest mocks base method.

func (*MockS3API) DeleteBucketEncryptionWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketEncryptionWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketEncryptionInput, arg2 ...request.Option) (*s3.DeleteBucketEncryptionOutput, error)

DeleteBucketEncryptionWithContext mocks base method.

func (*MockS3API) DeleteBucketIntelligentTieringConfiguration ¶
added in v1.5.7
func (m *MockS3API) DeleteBucketIntelligentTieringConfiguration(arg0 *s3.DeleteBucketIntelligentTieringConfigurationInput) (*s3.DeleteBucketIntelligentTieringConfigurationOutput, error)

DeleteBucketIntelligentTieringConfiguration mocks base method.

func (*MockS3API) DeleteBucketIntelligentTieringConfigurationRequest ¶
added in v1.5.7
func (m *MockS3API) DeleteBucketIntelligentTieringConfigurationRequest(arg0 *s3.DeleteBucketIntelligentTieringConfigurationInput) (*request.Request, *s3.DeleteBucketIntelligentTieringConfigurationOutput)

DeleteBucketIntelligentTieringConfigurationRequest mocks base method.

func (*MockS3API) DeleteBucketIntelligentTieringConfigurationWithContext ¶
added in v1.5.7
func (m *MockS3API) DeleteBucketIntelligentTieringConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketIntelligentTieringConfigurationInput, arg2 ...request.Option) (*s3.DeleteBucketIntelligentTieringConfigurationOutput, error)

DeleteBucketIntelligentTieringConfigurationWithContext mocks base method.

func (*MockS3API) DeleteBucketInventoryConfiguration ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketInventoryConfiguration(arg0 *s3.DeleteBucketInventoryConfigurationInput) (*s3.DeleteBucketInventoryConfigurationOutput, error)

DeleteBucketInventoryConfiguration mocks base method.

func (*MockS3API) DeleteBucketInventoryConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketInventoryConfigurationRequest(arg0 *s3.DeleteBucketInventoryConfigurationInput) (*request.Request, *s3.DeleteBucketInventoryConfigurationOutput)

DeleteBucketInventoryConfigurationRequest mocks base method.

func (*MockS3API) DeleteBucketInventoryConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketInventoryConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketInventoryConfigurationInput, arg2 ...request.Option) (*s3.DeleteBucketInventoryConfigurationOutput, error)

DeleteBucketInventoryConfigurationWithContext mocks base method.

func (*MockS3API) DeleteBucketLifecycle ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketLifecycle(arg0 *s3.DeleteBucketLifecycleInput) (*s3.DeleteBucketLifecycleOutput, error)

DeleteBucketLifecycle mocks base method.

func (*MockS3API) DeleteBucketLifecycleRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketLifecycleRequest(arg0 *s3.DeleteBucketLifecycleInput) (*request.Request, *s3.DeleteBucketLifecycleOutput)

DeleteBucketLifecycleRequest mocks base method.

func (*MockS3API) DeleteBucketLifecycleWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketLifecycleWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketLifecycleInput, arg2 ...request.Option) (*s3.DeleteBucketLifecycleOutput, error)

DeleteBucketLifecycleWithContext mocks base method.

func (*MockS3API) DeleteBucketMetricsConfiguration ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketMetricsConfiguration(arg0 *s3.DeleteBucketMetricsConfigurationInput) (*s3.DeleteBucketMetricsConfigurationOutput, error)

DeleteBucketMetricsConfiguration mocks base method.

func (*MockS3API) DeleteBucketMetricsConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketMetricsConfigurationRequest(arg0 *s3.DeleteBucketMetricsConfigurationInput) (*request.Request, *s3.DeleteBucketMetricsConfigurationOutput)

DeleteBucketMetricsConfigurationRequest mocks base method.

func (*MockS3API) DeleteBucketMetricsConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketMetricsConfigurationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketMetricsConfigurationInput, arg2 ...request.Option) (*s3.DeleteBucketMetricsConfigurationOutput, error)

DeleteBucketMetricsConfigurationWithContext mocks base method.

func (*MockS3API) DeleteBucketOwnershipControls ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketOwnershipControls(arg0 *s3.DeleteBucketOwnershipControlsInput) (*s3.DeleteBucketOwnershipControlsOutput, error)

DeleteBucketOwnershipControls mocks base method.

func (*MockS3API) DeleteBucketOwnershipControlsRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketOwnershipControlsRequest(arg0 *s3.DeleteBucketOwnershipControlsInput) (*request.Request, *s3.DeleteBucketOwnershipControlsOutput)

DeleteBucketOwnershipControlsRequest mocks base method.

func (*MockS3API) DeleteBucketOwnershipControlsWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketOwnershipControlsWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketOwnershipControlsInput, arg2 ...request.Option) (*s3.DeleteBucketOwnershipControlsOutput, error)

DeleteBucketOwnershipControlsWithContext mocks base method.

func (*MockS3API) DeleteBucketPolicy ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketPolicy(arg0 *s3.DeleteBucketPolicyInput) (*s3.DeleteBucketPolicyOutput, error)

DeleteBucketPolicy mocks base method.

func (*MockS3API) DeleteBucketPolicyRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketPolicyRequest(arg0 *s3.DeleteBucketPolicyInput) (*request.Request, *s3.DeleteBucketPolicyOutput)

DeleteBucketPolicyRequest mocks base method.

func (*MockS3API) DeleteBucketPolicyWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketPolicyWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketPolicyInput, arg2 ...request.Option) (*s3.DeleteBucketPolicyOutput, error)

DeleteBucketPolicyWithContext mocks base method.

func (*MockS3API) DeleteBucketReplication ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketReplication(arg0 *s3.DeleteBucketReplicationInput) (*s3.DeleteBucketReplicationOutput, error)

DeleteBucketReplication mocks base method.

func (*MockS3API) DeleteBucketReplicationRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketReplicationRequest(arg0 *s3.DeleteBucketReplicationInput) (*request.Request, *s3.DeleteBucketReplicationOutput)

DeleteBucketReplicationRequest mocks base method.

func (*MockS3API) DeleteBucketReplicationWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketReplicationWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketReplicationInput, arg2 ...request.Option) (*s3.DeleteBucketReplicationOutput, error)

DeleteBucketReplicationWithContext mocks base method.

func (*MockS3API) DeleteBucketRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketRequest(arg0 *s3.DeleteBucketInput) (*request.Request, *s3.DeleteBucketOutput)

DeleteBucketRequest mocks base method.

func (*MockS3API) DeleteBucketTagging ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketTagging(arg0 *s3.DeleteBucketTaggingInput) (*s3.DeleteBucketTaggingOutput, error)

DeleteBucketTagging mocks base method.

func (*MockS3API) DeleteBucketTaggingRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketTaggingRequest(arg0 *s3.DeleteBucketTaggingInput) (*request.Request, *s3.DeleteBucketTaggingOutput)

DeleteBucketTaggingRequest mocks base method.

func (*MockS3API) DeleteBucketTaggingWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketTaggingWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketTaggingInput, arg2 ...request.Option) (*s3.DeleteBucketTaggingOutput, error)

DeleteBucketTaggingWithContext mocks base method.

func (*MockS3API) DeleteBucketWebsite ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketWebsite(arg0 *s3.DeleteBucketWebsiteInput) (*s3.DeleteBucketWebsiteOutput, error)

DeleteBucketWebsite mocks base method.

func (*MockS3API) DeleteBucketWebsiteRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketWebsiteRequest(arg0 *s3.DeleteBucketWebsiteInput) (*request.Request, *s3.DeleteBucketWebsiteOutput)

DeleteBucketWebsiteRequest mocks base method.

func (*MockS3API) DeleteBucketWebsiteWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketWebsiteWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketWebsiteInput, arg2 ...request.Option) (*s3.DeleteBucketWebsiteOutput, error)

DeleteBucketWebsiteWithContext mocks base method.

func (*MockS3API) DeleteBucketWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteBucketWithContext(arg0 aws.Context, arg1 *s3.DeleteBucketInput, arg2 ...request.Option) (*s3.DeleteBucketOutput, error)

DeleteBucketWithContext mocks base method.

func (*MockS3API) DeleteObject ¶
added in v1.3.0
func (m *MockS3API) DeleteObject(arg0 *s3.DeleteObjectInput) (*s3.DeleteObjectOutput, error)

DeleteObject mocks base method.

func (*MockS3API) DeleteObjectRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectRequest(arg0 *s3.DeleteObjectInput) (*request.Request, *s3.DeleteObjectOutput)

DeleteObjectRequest mocks base method.

func (*MockS3API) DeleteObjectTagging ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectTagging(arg0 *s3.DeleteObjectTaggingInput) (*s3.DeleteObjectTaggingOutput, error)

DeleteObjectTagging mocks base method.

func (*MockS3API) DeleteObjectTaggingRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectTaggingRequest(arg0 *s3.DeleteObjectTaggingInput) (*request.Request, *s3.DeleteObjectTaggingOutput)

DeleteObjectTaggingRequest mocks base method.

func (*MockS3API) DeleteObjectTaggingWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectTaggingWithContext(arg0 aws.Context, arg1 *s3.DeleteObjectTaggingInput, arg2 ...request.Option) (*s3.DeleteObjectTaggingOutput, error)

DeleteObjectTaggingWithContext mocks base method.

func (*MockS3API) DeleteObjectWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectWithContext(arg0 aws.Context, arg1 *s3.DeleteObjectInput, arg2 ...request.Option) (*s3.DeleteObjectOutput, error)

DeleteObjectWithContext mocks base method.

func (*MockS3API) DeleteObjects ¶
added in v1.3.0
func (m *MockS3API) DeleteObjects(arg0 *s3.DeleteObjectsInput) (*s3.DeleteObjectsOutput, error)

DeleteObjects mocks base method.

func (*MockS3API) DeleteObjectsRequest ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectsRequest(arg0 *s3.DeleteObjectsInput) (*request.Request, *s3.DeleteObjectsOutput)

DeleteObjectsRequest mocks base method.

func (*MockS3API) DeleteObjectsWithContext ¶
added in v1.3.0
func (m *MockS3API) DeleteObjectsWithContext(arg0 aws.Context, arg1 *s3.DeleteObjectsInput, arg2 ...request.Option) (*s3.DeleteObjectsOutput, error)

DeleteObjectsWithContext mocks base method.

func (*MockS3API) DeletePublicAccessBlock ¶
added in v1.3.0
func (m *MockS3API) DeletePublicAccessBlock(arg0 *s3.DeletePublicAccessBlockInput) (*s3.DeletePublicAccessBlockOutput, error)

DeletePublicAccessBlock mocks base method.

func (*MockS3API) DeletePublicAccessBlockRequest ¶
added in v1.3.0
func (m *MockS3API) DeletePublicAccessBlockRequest(arg0 *s3.DeletePublicAccessBlockInput) (*request.Request, *s3.DeletePublicAccessBlockOutput)

DeletePublicAccessBlockRequest mocks base method.

func (*MockS3API) DeletePublicAccessBlockWithContext ¶
added in v1.3.0
func (m *MockS3API) DeletePublicAccessBlockWithContext(arg0 aws.Context, arg1 *s3.DeletePublicAccessBlockInput, arg2 ...request.Option) (*s3.DeletePublicAccessBlockOutput, error)

DeletePublicAccessBlockWithContext mocks base method.

func (*MockS3API) EXPECT ¶
added in v1.3.0
func (m *MockS3API) EXPECT() *MockS3APIMockRecorder

EXPECT returns an object that allows the caller to indicate expected use.

func (*MockS3API) GetBucketAccelerateConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetBucketAccelerateConfiguration(arg0 *s3.GetBucketAccelerateConfigurationInput) (*s3.GetBucketAccelerateConfigurationOutput, error)

GetBucketAccelerateConfiguration mocks base method.

func (*MockS3API) GetBucketAccelerateConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketAccelerateConfigurationRequest(arg0 *s3.GetBucketAccelerateConfigurationInput) (*request.Request, *s3.GetBucketAccelerateConfigurationOutput)

GetBucketAccelerateConfigurationRequest mocks base method.

func (*MockS3API) GetBucketAccelerateConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketAccelerateConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketAccelerateConfigurationInput, arg2 ...request.Option) (*s3.GetBucketAccelerateConfigurationOutput, error)

GetBucketAccelerateConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketAcl ¶
added in v1.3.0
func (m *MockS3API) GetBucketAcl(arg0 *s3.GetBucketAclInput) (*s3.GetBucketAclOutput, error)

GetBucketAcl mocks base method.

func (*MockS3API) GetBucketAclRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketAclRequest(arg0 *s3.GetBucketAclInput) (*request.Request, *s3.GetBucketAclOutput)

GetBucketAclRequest mocks base method.

func (*MockS3API) GetBucketAclWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketAclWithContext(arg0 aws.Context, arg1 *s3.GetBucketAclInput, arg2 ...request.Option) (*s3.GetBucketAclOutput, error)

GetBucketAclWithContext mocks base method.

func (*MockS3API) GetBucketAnalyticsConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetBucketAnalyticsConfiguration(arg0 *s3.GetBucketAnalyticsConfigurationInput) (*s3.GetBucketAnalyticsConfigurationOutput, error)

GetBucketAnalyticsConfiguration mocks base method.

func (*MockS3API) GetBucketAnalyticsConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketAnalyticsConfigurationRequest(arg0 *s3.GetBucketAnalyticsConfigurationInput) (*request.Request, *s3.GetBucketAnalyticsConfigurationOutput)

GetBucketAnalyticsConfigurationRequest mocks base method.

func (*MockS3API) GetBucketAnalyticsConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketAnalyticsConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketAnalyticsConfigurationInput, arg2 ...request.Option) (*s3.GetBucketAnalyticsConfigurationOutput, error)

GetBucketAnalyticsConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketCors ¶
added in v1.3.0
func (m *MockS3API) GetBucketCors(arg0 *s3.GetBucketCorsInput) (*s3.GetBucketCorsOutput, error)

GetBucketCors mocks base method.

func (*MockS3API) GetBucketCorsRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketCorsRequest(arg0 *s3.GetBucketCorsInput) (*request.Request, *s3.GetBucketCorsOutput)

GetBucketCorsRequest mocks base method.

func (*MockS3API) GetBucketCorsWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketCorsWithContext(arg0 aws.Context, arg1 *s3.GetBucketCorsInput, arg2 ...request.Option) (*s3.GetBucketCorsOutput, error)

GetBucketCorsWithContext mocks base method.

func (*MockS3API) GetBucketEncryption ¶
added in v1.3.0
func (m *MockS3API) GetBucketEncryption(arg0 *s3.GetBucketEncryptionInput) (*s3.GetBucketEncryptionOutput, error)

GetBucketEncryption mocks base method.

func (*MockS3API) GetBucketEncryptionRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketEncryptionRequest(arg0 *s3.GetBucketEncryptionInput) (*request.Request, *s3.GetBucketEncryptionOutput)

GetBucketEncryptionRequest mocks base method.

func (*MockS3API) GetBucketEncryptionWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketEncryptionWithContext(arg0 aws.Context, arg1 *s3.GetBucketEncryptionInput, arg2 ...request.Option) (*s3.GetBucketEncryptionOutput, error)

GetBucketEncryptionWithContext mocks base method.

func (*MockS3API) GetBucketIntelligentTieringConfiguration ¶
added in v1.5.7
func (m *MockS3API) GetBucketIntelligentTieringConfiguration(arg0 *s3.GetBucketIntelligentTieringConfigurationInput) (*s3.GetBucketIntelligentTieringConfigurationOutput, error)

GetBucketIntelligentTieringConfiguration mocks base method.

func (*MockS3API) GetBucketIntelligentTieringConfigurationRequest ¶
added in v1.5.7
func (m *MockS3API) GetBucketIntelligentTieringConfigurationRequest(arg0 *s3.GetBucketIntelligentTieringConfigurationInput) (*request.Request, *s3.GetBucketIntelligentTieringConfigurationOutput)

GetBucketIntelligentTieringConfigurationRequest mocks base method.

func (*MockS3API) GetBucketIntelligentTieringConfigurationWithContext ¶
added in v1.5.7
func (m *MockS3API) GetBucketIntelligentTieringConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketIntelligentTieringConfigurationInput, arg2 ...request.Option) (*s3.GetBucketIntelligentTieringConfigurationOutput, error)

GetBucketIntelligentTieringConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketInventoryConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetBucketInventoryConfiguration(arg0 *s3.GetBucketInventoryConfigurationInput) (*s3.GetBucketInventoryConfigurationOutput, error)

GetBucketInventoryConfiguration mocks base method.

func (*MockS3API) GetBucketInventoryConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketInventoryConfigurationRequest(arg0 *s3.GetBucketInventoryConfigurationInput) (*request.Request, *s3.GetBucketInventoryConfigurationOutput)

GetBucketInventoryConfigurationRequest mocks base method.

func (*MockS3API) GetBucketInventoryConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketInventoryConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketInventoryConfigurationInput, arg2 ...request.Option) (*s3.GetBucketInventoryConfigurationOutput, error)

GetBucketInventoryConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketLifecycle ¶
added in v1.3.0
func (m *MockS3API) GetBucketLifecycle(arg0 *s3.GetBucketLifecycleInput) (*s3.GetBucketLifecycleOutput, error)

GetBucketLifecycle mocks base method.

func (*MockS3API) GetBucketLifecycleConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetBucketLifecycleConfiguration(arg0 *s3.GetBucketLifecycleConfigurationInput) (*s3.GetBucketLifecycleConfigurationOutput, error)

GetBucketLifecycleConfiguration mocks base method.

func (*MockS3API) GetBucketLifecycleConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketLifecycleConfigurationRequest(arg0 *s3.GetBucketLifecycleConfigurationInput) (*request.Request, *s3.GetBucketLifecycleConfigurationOutput)

GetBucketLifecycleConfigurationRequest mocks base method.

func (*MockS3API) GetBucketLifecycleConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketLifecycleConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketLifecycleConfigurationInput, arg2 ...request.Option) (*s3.GetBucketLifecycleConfigurationOutput, error)

GetBucketLifecycleConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketLifecycleRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketLifecycleRequest(arg0 *s3.GetBucketLifecycleInput) (*request.Request, *s3.GetBucketLifecycleOutput)

GetBucketLifecycleRequest mocks base method.

func (*MockS3API) GetBucketLifecycleWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketLifecycleWithContext(arg0 aws.Context, arg1 *s3.GetBucketLifecycleInput, arg2 ...request.Option) (*s3.GetBucketLifecycleOutput, error)

GetBucketLifecycleWithContext mocks base method.

func (*MockS3API) GetBucketLocation ¶
added in v1.3.0
func (m *MockS3API) GetBucketLocation(arg0 *s3.GetBucketLocationInput) (*s3.GetBucketLocationOutput, error)

GetBucketLocation mocks base method.

func (*MockS3API) GetBucketLocationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketLocationRequest(arg0 *s3.GetBucketLocationInput) (*request.Request, *s3.GetBucketLocationOutput)

GetBucketLocationRequest mocks base method.

func (*MockS3API) GetBucketLocationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketLocationWithContext(arg0 aws.Context, arg1 *s3.GetBucketLocationInput, arg2 ...request.Option) (*s3.GetBucketLocationOutput, error)

GetBucketLocationWithContext mocks base method.

func (*MockS3API) GetBucketLogging ¶
added in v1.3.0
func (m *MockS3API) GetBucketLogging(arg0 *s3.GetBucketLoggingInput) (*s3.GetBucketLoggingOutput, error)

GetBucketLogging mocks base method.

func (*MockS3API) GetBucketLoggingRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketLoggingRequest(arg0 *s3.GetBucketLoggingInput) (*request.Request, *s3.GetBucketLoggingOutput)

GetBucketLoggingRequest mocks base method.

func (*MockS3API) GetBucketLoggingWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketLoggingWithContext(arg0 aws.Context, arg1 *s3.GetBucketLoggingInput, arg2 ...request.Option) (*s3.GetBucketLoggingOutput, error)

GetBucketLoggingWithContext mocks base method.

func (*MockS3API) GetBucketMetricsConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetBucketMetricsConfiguration(arg0 *s3.GetBucketMetricsConfigurationInput) (*s3.GetBucketMetricsConfigurationOutput, error)

GetBucketMetricsConfiguration mocks base method.

func (*MockS3API) GetBucketMetricsConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketMetricsConfigurationRequest(arg0 *s3.GetBucketMetricsConfigurationInput) (*request.Request, *s3.GetBucketMetricsConfigurationOutput)

GetBucketMetricsConfigurationRequest mocks base method.

func (*MockS3API) GetBucketMetricsConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketMetricsConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketMetricsConfigurationInput, arg2 ...request.Option) (*s3.GetBucketMetricsConfigurationOutput, error)

GetBucketMetricsConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketNotification ¶
added in v1.3.0
func (m *MockS3API) GetBucketNotification(arg0 *s3.GetBucketNotificationConfigurationRequest) (*s3.NotificationConfigurationDeprecated, error)

GetBucketNotification mocks base method.

func (*MockS3API) GetBucketNotificationConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetBucketNotificationConfiguration(arg0 *s3.GetBucketNotificationConfigurationRequest) (*s3.NotificationConfiguration, error)

GetBucketNotificationConfiguration mocks base method.

func (*MockS3API) GetBucketNotificationConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketNotificationConfigurationRequest(arg0 *s3.GetBucketNotificationConfigurationRequest) (*request.Request, *s3.NotificationConfiguration)

GetBucketNotificationConfigurationRequest mocks base method.

func (*MockS3API) GetBucketNotificationConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketNotificationConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetBucketNotificationConfigurationRequest, arg2 ...request.Option) (*s3.NotificationConfiguration, error)

GetBucketNotificationConfigurationWithContext mocks base method.

func (*MockS3API) GetBucketNotificationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketNotificationRequest(arg0 *s3.GetBucketNotificationConfigurationRequest) (*request.Request, *s3.NotificationConfigurationDeprecated)

GetBucketNotificationRequest mocks base method.

func (*MockS3API) GetBucketNotificationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketNotificationWithContext(arg0 aws.Context, arg1 *s3.GetBucketNotificationConfigurationRequest, arg2 ...request.Option) (*s3.NotificationConfigurationDeprecated, error)

GetBucketNotificationWithContext mocks base method.

func (*MockS3API) GetBucketOwnershipControls ¶
added in v1.3.0
func (m *MockS3API) GetBucketOwnershipControls(arg0 *s3.GetBucketOwnershipControlsInput) (*s3.GetBucketOwnershipControlsOutput, error)

GetBucketOwnershipControls mocks base method.

func (*MockS3API) GetBucketOwnershipControlsRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketOwnershipControlsRequest(arg0 *s3.GetBucketOwnershipControlsInput) (*request.Request, *s3.GetBucketOwnershipControlsOutput)

GetBucketOwnershipControlsRequest mocks base method.

func (*MockS3API) GetBucketOwnershipControlsWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketOwnershipControlsWithContext(arg0 aws.Context, arg1 *s3.GetBucketOwnershipControlsInput, arg2 ...request.Option) (*s3.GetBucketOwnershipControlsOutput, error)

GetBucketOwnershipControlsWithContext mocks base method.

func (*MockS3API) GetBucketPolicy ¶
added in v1.3.0
func (m *MockS3API) GetBucketPolicy(arg0 *s3.GetBucketPolicyInput) (*s3.GetBucketPolicyOutput, error)

GetBucketPolicy mocks base method.

func (*MockS3API) GetBucketPolicyRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketPolicyRequest(arg0 *s3.GetBucketPolicyInput) (*request.Request, *s3.GetBucketPolicyOutput)

GetBucketPolicyRequest mocks base method.

func (*MockS3API) GetBucketPolicyStatus ¶
added in v1.3.0
func (m *MockS3API) GetBucketPolicyStatus(arg0 *s3.GetBucketPolicyStatusInput) (*s3.GetBucketPolicyStatusOutput, error)

GetBucketPolicyStatus mocks base method.

func (*MockS3API) GetBucketPolicyStatusRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketPolicyStatusRequest(arg0 *s3.GetBucketPolicyStatusInput) (*request.Request, *s3.GetBucketPolicyStatusOutput)

GetBucketPolicyStatusRequest mocks base method.

func (*MockS3API) GetBucketPolicyStatusWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketPolicyStatusWithContext(arg0 aws.Context, arg1 *s3.GetBucketPolicyStatusInput, arg2 ...request.Option) (*s3.GetBucketPolicyStatusOutput, error)

GetBucketPolicyStatusWithContext mocks base method.

func (*MockS3API) GetBucketPolicyWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketPolicyWithContext(arg0 aws.Context, arg1 *s3.GetBucketPolicyInput, arg2 ...request.Option) (*s3.GetBucketPolicyOutput, error)

GetBucketPolicyWithContext mocks base method.

func (*MockS3API) GetBucketReplication ¶
added in v1.3.0
func (m *MockS3API) GetBucketReplication(arg0 *s3.GetBucketReplicationInput) (*s3.GetBucketReplicationOutput, error)

GetBucketReplication mocks base method.

func (*MockS3API) GetBucketReplicationRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketReplicationRequest(arg0 *s3.GetBucketReplicationInput) (*request.Request, *s3.GetBucketReplicationOutput)

GetBucketReplicationRequest mocks base method.

func (*MockS3API) GetBucketReplicationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketReplicationWithContext(arg0 aws.Context, arg1 *s3.GetBucketReplicationInput, arg2 ...request.Option) (*s3.GetBucketReplicationOutput, error)

GetBucketReplicationWithContext mocks base method.

func (*MockS3API) GetBucketRequestPayment ¶
added in v1.3.0
func (m *MockS3API) GetBucketRequestPayment(arg0 *s3.GetBucketRequestPaymentInput) (*s3.GetBucketRequestPaymentOutput, error)

GetBucketRequestPayment mocks base method.

func (*MockS3API) GetBucketRequestPaymentRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketRequestPaymentRequest(arg0 *s3.GetBucketRequestPaymentInput) (*request.Request, *s3.GetBucketRequestPaymentOutput)

GetBucketRequestPaymentRequest mocks base method.

func (*MockS3API) GetBucketRequestPaymentWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketRequestPaymentWithContext(arg0 aws.Context, arg1 *s3.GetBucketRequestPaymentInput, arg2 ...request.Option) (*s3.GetBucketRequestPaymentOutput, error)

GetBucketRequestPaymentWithContext mocks base method.

func (*MockS3API) GetBucketTagging ¶
added in v1.3.0
func (m *MockS3API) GetBucketTagging(arg0 *s3.GetBucketTaggingInput) (*s3.GetBucketTaggingOutput, error)

GetBucketTagging mocks base method.

func (*MockS3API) GetBucketTaggingRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketTaggingRequest(arg0 *s3.GetBucketTaggingInput) (*request.Request, *s3.GetBucketTaggingOutput)

GetBucketTaggingRequest mocks base method.

func (*MockS3API) GetBucketTaggingWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketTaggingWithContext(arg0 aws.Context, arg1 *s3.GetBucketTaggingInput, arg2 ...request.Option) (*s3.GetBucketTaggingOutput, error)

GetBucketTaggingWithContext mocks base method.

func (*MockS3API) GetBucketVersioning ¶
added in v1.3.0
func (m *MockS3API) GetBucketVersioning(arg0 *s3.GetBucketVersioningInput) (*s3.GetBucketVersioningOutput, error)

GetBucketVersioning mocks base method.

func (*MockS3API) GetBucketVersioningRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketVersioningRequest(arg0 *s3.GetBucketVersioningInput) (*request.Request, *s3.GetBucketVersioningOutput)

GetBucketVersioningRequest mocks base method.

func (*MockS3API) GetBucketVersioningWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketVersioningWithContext(arg0 aws.Context, arg1 *s3.GetBucketVersioningInput, arg2 ...request.Option) (*s3.GetBucketVersioningOutput, error)

GetBucketVersioningWithContext mocks base method.

func (*MockS3API) GetBucketWebsite ¶
added in v1.3.0
func (m *MockS3API) GetBucketWebsite(arg0 *s3.GetBucketWebsiteInput) (*s3.GetBucketWebsiteOutput, error)

GetBucketWebsite mocks base method.

func (*MockS3API) GetBucketWebsiteRequest ¶
added in v1.3.0
func (m *MockS3API) GetBucketWebsiteRequest(arg0 *s3.GetBucketWebsiteInput) (*request.Request, *s3.GetBucketWebsiteOutput)

GetBucketWebsiteRequest mocks base method.

func (*MockS3API) GetBucketWebsiteWithContext ¶
added in v1.3.0
func (m *MockS3API) GetBucketWebsiteWithContext(arg0 aws.Context, arg1 *s3.GetBucketWebsiteInput, arg2 ...request.Option) (*s3.GetBucketWebsiteOutput, error)

GetBucketWebsiteWithContext mocks base method.

func (*MockS3API) GetObject ¶
added in v1.3.0
func (m *MockS3API) GetObject(arg0 *s3.GetObjectInput) (*s3.GetObjectOutput, error)

GetObject mocks base method.

func (*MockS3API) GetObjectAcl ¶
added in v1.3.0
func (m *MockS3API) GetObjectAcl(arg0 *s3.GetObjectAclInput) (*s3.GetObjectAclOutput, error)

GetObjectAcl mocks base method.

func (*MockS3API) GetObjectAclRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectAclRequest(arg0 *s3.GetObjectAclInput) (*request.Request, *s3.GetObjectAclOutput)

GetObjectAclRequest mocks base method.

func (*MockS3API) GetObjectAclWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectAclWithContext(arg0 aws.Context, arg1 *s3.GetObjectAclInput, arg2 ...request.Option) (*s3.GetObjectAclOutput, error)

GetObjectAclWithContext mocks base method.

func (*MockS3API) GetObjectAttributes ¶
added in v1.17.0
func (m *MockS3API) GetObjectAttributes(arg0 *s3.GetObjectAttributesInput) (*s3.GetObjectAttributesOutput, error)

GetObjectAttributes mocks base method.

func (*MockS3API) GetObjectAttributesRequest ¶
added in v1.17.0
func (m *MockS3API) GetObjectAttributesRequest(arg0 *s3.GetObjectAttributesInput) (*request.Request, *s3.GetObjectAttributesOutput)

GetObjectAttributesRequest mocks base method.

func (*MockS3API) GetObjectAttributesWithContext ¶
added in v1.17.0
func (m *MockS3API) GetObjectAttributesWithContext(arg0 aws.Context, arg1 *s3.GetObjectAttributesInput, arg2 ...request.Option) (*s3.GetObjectAttributesOutput, error)

GetObjectAttributesWithContext mocks base method.

func (*MockS3API) GetObjectLegalHold ¶
added in v1.3.0
func (m *MockS3API) GetObjectLegalHold(arg0 *s3.GetObjectLegalHoldInput) (*s3.GetObjectLegalHoldOutput, error)

GetObjectLegalHold mocks base method.

func (*MockS3API) GetObjectLegalHoldRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectLegalHoldRequest(arg0 *s3.GetObjectLegalHoldInput) (*request.Request, *s3.GetObjectLegalHoldOutput)

GetObjectLegalHoldRequest mocks base method.

func (*MockS3API) GetObjectLegalHoldWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectLegalHoldWithContext(arg0 aws.Context, arg1 *s3.GetObjectLegalHoldInput, arg2 ...request.Option) (*s3.GetObjectLegalHoldOutput, error)

GetObjectLegalHoldWithContext mocks base method.

func (*MockS3API) GetObjectLockConfiguration ¶
added in v1.3.0
func (m *MockS3API) GetObjectLockConfiguration(arg0 *s3.GetObjectLockConfigurationInput) (*s3.GetObjectLockConfigurationOutput, error)

GetObjectLockConfiguration mocks base method.

func (*MockS3API) GetObjectLockConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectLockConfigurationRequest(arg0 *s3.GetObjectLockConfigurationInput) (*request.Request, *s3.GetObjectLockConfigurationOutput)

GetObjectLockConfigurationRequest mocks base method.

func (*MockS3API) GetObjectLockConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectLockConfigurationWithContext(arg0 aws.Context, arg1 *s3.GetObjectLockConfigurationInput, arg2 ...request.Option) (*s3.GetObjectLockConfigurationOutput, error)

GetObjectLockConfigurationWithContext mocks base method.

func (*MockS3API) GetObjectRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectRequest(arg0 *s3.GetObjectInput) (*request.Request, *s3.GetObjectOutput)

GetObjectRequest mocks base method.

func (*MockS3API) GetObjectRetention ¶
added in v1.3.0
func (m *MockS3API) GetObjectRetention(arg0 *s3.GetObjectRetentionInput) (*s3.GetObjectRetentionOutput, error)

GetObjectRetention mocks base method.

func (*MockS3API) GetObjectRetentionRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectRetentionRequest(arg0 *s3.GetObjectRetentionInput) (*request.Request, *s3.GetObjectRetentionOutput)

GetObjectRetentionRequest mocks base method.

func (*MockS3API) GetObjectRetentionWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectRetentionWithContext(arg0 aws.Context, arg1 *s3.GetObjectRetentionInput, arg2 ...request.Option) (*s3.GetObjectRetentionOutput, error)

GetObjectRetentionWithContext mocks base method.

func (*MockS3API) GetObjectTagging ¶
added in v1.3.0
func (m *MockS3API) GetObjectTagging(arg0 *s3.GetObjectTaggingInput) (*s3.GetObjectTaggingOutput, error)

GetObjectTagging mocks base method.

func (*MockS3API) GetObjectTaggingRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectTaggingRequest(arg0 *s3.GetObjectTaggingInput) (*request.Request, *s3.GetObjectTaggingOutput)

GetObjectTaggingRequest mocks base method.

func (*MockS3API) GetObjectTaggingWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectTaggingWithContext(arg0 aws.Context, arg1 *s3.GetObjectTaggingInput, arg2 ...request.Option) (*s3.GetObjectTaggingOutput, error)

GetObjectTaggingWithContext mocks base method.

func (*MockS3API) GetObjectTorrent ¶
added in v1.3.0
func (m *MockS3API) GetObjectTorrent(arg0 *s3.GetObjectTorrentInput) (*s3.GetObjectTorrentOutput, error)

GetObjectTorrent mocks base method.

func (*MockS3API) GetObjectTorrentRequest ¶
added in v1.3.0
func (m *MockS3API) GetObjectTorrentRequest(arg0 *s3.GetObjectTorrentInput) (*request.Request, *s3.GetObjectTorrentOutput)

GetObjectTorrentRequest mocks base method.

func (*MockS3API) GetObjectTorrentWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectTorrentWithContext(arg0 aws.Context, arg1 *s3.GetObjectTorrentInput, arg2 ...request.Option) (*s3.GetObjectTorrentOutput, error)

GetObjectTorrentWithContext mocks base method.

func (*MockS3API) GetObjectWithContext ¶
added in v1.3.0
func (m *MockS3API) GetObjectWithContext(arg0 aws.Context, arg1 *s3.GetObjectInput, arg2 ...request.Option) (*s3.GetObjectOutput, error)

GetObjectWithContext mocks base method.

func (*MockS3API) GetPublicAccessBlock ¶
added in v1.3.0
func (m *MockS3API) GetPublicAccessBlock(arg0 *s3.GetPublicAccessBlockInput) (*s3.GetPublicAccessBlockOutput, error)

GetPublicAccessBlock mocks base method.

func (*MockS3API) GetPublicAccessBlockRequest ¶
added in v1.3.0
func (m *MockS3API) GetPublicAccessBlockRequest(arg0 *s3.GetPublicAccessBlockInput) (*request.Request, *s3.GetPublicAccessBlockOutput)

GetPublicAccessBlockRequest mocks base method.

func (*MockS3API) GetPublicAccessBlockWithContext ¶
added in v1.3.0
func (m *MockS3API) GetPublicAccessBlockWithContext(arg0 aws.Context, arg1 *s3.GetPublicAccessBlockInput, arg2 ...request.Option) (*s3.GetPublicAccessBlockOutput, error)

GetPublicAccessBlockWithContext mocks base method.

func (*MockS3API) HeadBucket ¶
added in v1.3.0
func (m *MockS3API) HeadBucket(arg0 *s3.HeadBucketInput) (*s3.HeadBucketOutput, error)

HeadBucket mocks base method.

func (*MockS3API) HeadBucketRequest ¶
added in v1.3.0
func (m *MockS3API) HeadBucketRequest(arg0 *s3.HeadBucketInput) (*request.Request, *s3.HeadBucketOutput)

HeadBucketRequest mocks base method.

func (*MockS3API) HeadBucketWithContext ¶
added in v1.3.0
func (m *MockS3API) HeadBucketWithContext(arg0 aws.Context, arg1 *s3.HeadBucketInput, arg2 ...request.Option) (*s3.HeadBucketOutput, error)

HeadBucketWithContext mocks base method.

func (*MockS3API) HeadObject ¶
added in v1.3.0
func (m *MockS3API) HeadObject(arg0 *s3.HeadObjectInput) (*s3.HeadObjectOutput, error)

HeadObject mocks base method.

func (*MockS3API) HeadObjectRequest ¶
added in v1.3.0
func (m *MockS3API) HeadObjectRequest(arg0 *s3.HeadObjectInput) (*request.Request, *s3.HeadObjectOutput)

HeadObjectRequest mocks base method.

func (*MockS3API) HeadObjectWithContext ¶
added in v1.3.0
func (m *MockS3API) HeadObjectWithContext(arg0 aws.Context, arg1 *s3.HeadObjectInput, arg2 ...request.Option) (*s3.HeadObjectOutput, error)

HeadObjectWithContext mocks base method.

func (*MockS3API) ListBucketAnalyticsConfigurations ¶
added in v1.3.0
func (m *MockS3API) ListBucketAnalyticsConfigurations(arg0 *s3.ListBucketAnalyticsConfigurationsInput) (*s3.ListBucketAnalyticsConfigurationsOutput, error)

ListBucketAnalyticsConfigurations mocks base method.

func (*MockS3API) ListBucketAnalyticsConfigurationsRequest ¶
added in v1.3.0
func (m *MockS3API) ListBucketAnalyticsConfigurationsRequest(arg0 *s3.ListBucketAnalyticsConfigurationsInput) (*request.Request, *s3.ListBucketAnalyticsConfigurationsOutput)

ListBucketAnalyticsConfigurationsRequest mocks base method.

func (*MockS3API) ListBucketAnalyticsConfigurationsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListBucketAnalyticsConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketAnalyticsConfigurationsInput, arg2 ...request.Option) (*s3.ListBucketAnalyticsConfigurationsOutput, error)

ListBucketAnalyticsConfigurationsWithContext mocks base method.

func (*MockS3API) ListBucketIntelligentTieringConfigurations ¶
added in v1.5.7
func (m *MockS3API) ListBucketIntelligentTieringConfigurations(arg0 *s3.ListBucketIntelligentTieringConfigurationsInput) (*s3.ListBucketIntelligentTieringConfigurationsOutput, error)

ListBucketIntelligentTieringConfigurations mocks base method.

func (*MockS3API) ListBucketIntelligentTieringConfigurationsRequest ¶
added in v1.5.7
func (m *MockS3API) ListBucketIntelligentTieringConfigurationsRequest(arg0 *s3.ListBucketIntelligentTieringConfigurationsInput) (*request.Request, *s3.ListBucketIntelligentTieringConfigurationsOutput)

ListBucketIntelligentTieringConfigurationsRequest mocks base method.

func (*MockS3API) ListBucketIntelligentTieringConfigurationsWithContext ¶
added in v1.5.7
func (m *MockS3API) ListBucketIntelligentTieringConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketIntelligentTieringConfigurationsInput, arg2 ...request.Option) (*s3.ListBucketIntelligentTieringConfigurationsOutput, error)

ListBucketIntelligentTieringConfigurationsWithContext mocks base method.

func (*MockS3API) ListBucketInventoryConfigurations ¶
added in v1.3.0
func (m *MockS3API) ListBucketInventoryConfigurations(arg0 *s3.ListBucketInventoryConfigurationsInput) (*s3.ListBucketInventoryConfigurationsOutput, error)

ListBucketInventoryConfigurations mocks base method.

func (*MockS3API) ListBucketInventoryConfigurationsRequest ¶
added in v1.3.0
func (m *MockS3API) ListBucketInventoryConfigurationsRequest(arg0 *s3.ListBucketInventoryConfigurationsInput) (*request.Request, *s3.ListBucketInventoryConfigurationsOutput)

ListBucketInventoryConfigurationsRequest mocks base method.

func (*MockS3API) ListBucketInventoryConfigurationsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListBucketInventoryConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketInventoryConfigurationsInput, arg2 ...request.Option) (*s3.ListBucketInventoryConfigurationsOutput, error)

ListBucketInventoryConfigurationsWithContext mocks base method.

func (*MockS3API) ListBucketMetricsConfigurations ¶
added in v1.3.0
func (m *MockS3API) ListBucketMetricsConfigurations(arg0 *s3.ListBucketMetricsConfigurationsInput) (*s3.ListBucketMetricsConfigurationsOutput, error)

ListBucketMetricsConfigurations mocks base method.

func (*MockS3API) ListBucketMetricsConfigurationsRequest ¶
added in v1.3.0
func (m *MockS3API) ListBucketMetricsConfigurationsRequest(arg0 *s3.ListBucketMetricsConfigurationsInput) (*request.Request, *s3.ListBucketMetricsConfigurationsOutput)

ListBucketMetricsConfigurationsRequest mocks base method.

func (*MockS3API) ListBucketMetricsConfigurationsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListBucketMetricsConfigurationsWithContext(arg0 aws.Context, arg1 *s3.ListBucketMetricsConfigurationsInput, arg2 ...request.Option) (*s3.ListBucketMetricsConfigurationsOutput, error)

ListBucketMetricsConfigurationsWithContext mocks base method.

func (*MockS3API) ListBuckets ¶
added in v1.3.0
func (m *MockS3API) ListBuckets(arg0 *s3.ListBucketsInput) (*s3.ListBucketsOutput, error)

ListBuckets mocks base method.

func (*MockS3API) ListBucketsRequest ¶
added in v1.3.0
func (m *MockS3API) ListBucketsRequest(arg0 *s3.ListBucketsInput) (*request.Request, *s3.ListBucketsOutput)

ListBucketsRequest mocks base method.

func (*MockS3API) ListBucketsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListBucketsWithContext(arg0 aws.Context, arg1 *s3.ListBucketsInput, arg2 ...request.Option) (*s3.ListBucketsOutput, error)

ListBucketsWithContext mocks base method.

func (*MockS3API) ListDirectoryBuckets ¶
added in v1.23.1
func (m *MockS3API) ListDirectoryBuckets(arg0 *s3.ListDirectoryBucketsInput) (*s3.ListDirectoryBucketsOutput, error)

ListDirectoryBuckets mocks base method.

func (*MockS3API) ListDirectoryBucketsPages ¶
added in v1.23.1
func (m *MockS3API) ListDirectoryBucketsPages(arg0 *s3.ListDirectoryBucketsInput, arg1 func(*s3.ListDirectoryBucketsOutput, bool) bool) error

ListDirectoryBucketsPages mocks base method.

func (*MockS3API) ListDirectoryBucketsPagesWithContext ¶
added in v1.23.1
func (m *MockS3API) ListDirectoryBucketsPagesWithContext(arg0 aws.Context, arg1 *s3.ListDirectoryBucketsInput, arg2 func(*s3.ListDirectoryBucketsOutput, bool) bool, arg3 ...request.Option) error

ListDirectoryBucketsPagesWithContext mocks base method.

func (*MockS3API) ListDirectoryBucketsRequest ¶
added in v1.23.1
func (m *MockS3API) ListDirectoryBucketsRequest(arg0 *s3.ListDirectoryBucketsInput) (*request.Request, *s3.ListDirectoryBucketsOutput)

ListDirectoryBucketsRequest mocks base method.

func (*MockS3API) ListDirectoryBucketsWithContext ¶
added in v1.23.1
func (m *MockS3API) ListDirectoryBucketsWithContext(arg0 aws.Context, arg1 *s3.ListDirectoryBucketsInput, arg2 ...request.Option) (*s3.ListDirectoryBucketsOutput, error)

ListDirectoryBucketsWithContext mocks base method.

func (*MockS3API) ListMultipartUploads ¶
added in v1.3.0
func (m *MockS3API) ListMultipartUploads(arg0 *s3.ListMultipartUploadsInput) (*s3.ListMultipartUploadsOutput, error)

ListMultipartUploads mocks base method.

func (*MockS3API) ListMultipartUploadsPages ¶
added in v1.3.0
func (m *MockS3API) ListMultipartUploadsPages(arg0 *s3.ListMultipartUploadsInput, arg1 func(*s3.ListMultipartUploadsOutput, bool) bool) error

ListMultipartUploadsPages mocks base method.

func (*MockS3API) ListMultipartUploadsPagesWithContext ¶
added in v1.3.0
func (m *MockS3API) ListMultipartUploadsPagesWithContext(arg0 aws.Context, arg1 *s3.ListMultipartUploadsInput, arg2 func(*s3.ListMultipartUploadsOutput, bool) bool, arg3 ...request.Option) error

ListMultipartUploadsPagesWithContext mocks base method.

func (*MockS3API) ListMultipartUploadsRequest ¶
added in v1.3.0
func (m *MockS3API) ListMultipartUploadsRequest(arg0 *s3.ListMultipartUploadsInput) (*request.Request, *s3.ListMultipartUploadsOutput)

ListMultipartUploadsRequest mocks base method.

func (*MockS3API) ListMultipartUploadsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListMultipartUploadsWithContext(arg0 aws.Context, arg1 *s3.ListMultipartUploadsInput, arg2 ...request.Option) (*s3.ListMultipartUploadsOutput, error)

ListMultipartUploadsWithContext mocks base method.

func (*MockS3API) ListObjectVersions ¶
added in v1.3.0
func (m *MockS3API) ListObjectVersions(arg0 *s3.ListObjectVersionsInput) (*s3.ListObjectVersionsOutput, error)

ListObjectVersions mocks base method.

func (*MockS3API) ListObjectVersionsPages ¶
added in v1.3.0
func (m *MockS3API) ListObjectVersionsPages(arg0 *s3.ListObjectVersionsInput, arg1 func(*s3.ListObjectVersionsOutput, bool) bool) error

ListObjectVersionsPages mocks base method.

func (*MockS3API) ListObjectVersionsPagesWithContext ¶
added in v1.3.0
func (m *MockS3API) ListObjectVersionsPagesWithContext(arg0 aws.Context, arg1 *s3.ListObjectVersionsInput, arg2 func(*s3.ListObjectVersionsOutput, bool) bool, arg3 ...request.Option) error

ListObjectVersionsPagesWithContext mocks base method.

func (*MockS3API) ListObjectVersionsRequest ¶
added in v1.3.0
func (m *MockS3API) ListObjectVersionsRequest(arg0 *s3.ListObjectVersionsInput) (*request.Request, *s3.ListObjectVersionsOutput)

ListObjectVersionsRequest mocks base method.

func (*MockS3API) ListObjectVersionsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListObjectVersionsWithContext(arg0 aws.Context, arg1 *s3.ListObjectVersionsInput, arg2 ...request.Option) (*s3.ListObjectVersionsOutput, error)

ListObjectVersionsWithContext mocks base method.

func (*MockS3API) ListObjects ¶
added in v1.3.0
func (m *MockS3API) ListObjects(arg0 *s3.ListObjectsInput) (*s3.ListObjectsOutput, error)

ListObjects mocks base method.

func (*MockS3API) ListObjectsPages ¶
added in v1.3.0
func (m *MockS3API) ListObjectsPages(arg0 *s3.ListObjectsInput, arg1 func(*s3.ListObjectsOutput, bool) bool) error

ListObjectsPages mocks base method.

func (*MockS3API) ListObjectsPagesWithContext ¶
added in v1.3.0
func (m *MockS3API) ListObjectsPagesWithContext(arg0 aws.Context, arg1 *s3.ListObjectsInput, arg2 func(*s3.ListObjectsOutput, bool) bool, arg3 ...request.Option) error

ListObjectsPagesWithContext mocks base method.

func (*MockS3API) ListObjectsRequest ¶
added in v1.3.0
func (m *MockS3API) ListObjectsRequest(arg0 *s3.ListObjectsInput) (*request.Request, *s3.ListObjectsOutput)

ListObjectsRequest mocks base method.

func (*MockS3API) ListObjectsV2 ¶
added in v1.3.0
func (m *MockS3API) ListObjectsV2(arg0 *s3.ListObjectsV2Input) (*s3.ListObjectsV2Output, error)

ListObjectsV2 mocks base method.

func (*MockS3API) ListObjectsV2Pages ¶
added in v1.3.0
func (m *MockS3API) ListObjectsV2Pages(arg0 *s3.ListObjectsV2Input, arg1 func(*s3.ListObjectsV2Output, bool) bool) error

ListObjectsV2Pages mocks base method.

func (*MockS3API) ListObjectsV2PagesWithContext ¶
added in v1.3.0
func (m *MockS3API) ListObjectsV2PagesWithContext(arg0 aws.Context, arg1 *s3.ListObjectsV2Input, arg2 func(*s3.ListObjectsV2Output, bool) bool, arg3 ...request.Option) error

ListObjectsV2PagesWithContext mocks base method.

func (*MockS3API) ListObjectsV2Request ¶
added in v1.3.0
func (m *MockS3API) ListObjectsV2Request(arg0 *s3.ListObjectsV2Input) (*request.Request, *s3.ListObjectsV2Output)

ListObjectsV2Request mocks base method.

func (*MockS3API) ListObjectsV2WithContext ¶
added in v1.3.0
func (m *MockS3API) ListObjectsV2WithContext(arg0 aws.Context, arg1 *s3.ListObjectsV2Input, arg2 ...request.Option) (*s3.ListObjectsV2Output, error)

ListObjectsV2WithContext mocks base method.

func (*MockS3API) ListObjectsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListObjectsWithContext(arg0 aws.Context, arg1 *s3.ListObjectsInput, arg2 ...request.Option) (*s3.ListObjectsOutput, error)

ListObjectsWithContext mocks base method.

func (*MockS3API) ListParts ¶
added in v1.3.0
func (m *MockS3API) ListParts(arg0 *s3.ListPartsInput) (*s3.ListPartsOutput, error)

ListParts mocks base method.

func (*MockS3API) ListPartsPages ¶
added in v1.3.0
func (m *MockS3API) ListPartsPages(arg0 *s3.ListPartsInput, arg1 func(*s3.ListPartsOutput, bool) bool) error

ListPartsPages mocks base method.

func (*MockS3API) ListPartsPagesWithContext ¶
added in v1.3.0
func (m *MockS3API) ListPartsPagesWithContext(arg0 aws.Context, arg1 *s3.ListPartsInput, arg2 func(*s3.ListPartsOutput, bool) bool, arg3 ...request.Option) error

ListPartsPagesWithContext mocks base method.

func (*MockS3API) ListPartsRequest ¶
added in v1.3.0
func (m *MockS3API) ListPartsRequest(arg0 *s3.ListPartsInput) (*request.Request, *s3.ListPartsOutput)

ListPartsRequest mocks base method.

func (*MockS3API) ListPartsWithContext ¶
added in v1.3.0
func (m *MockS3API) ListPartsWithContext(arg0 aws.Context, arg1 *s3.ListPartsInput, arg2 ...request.Option) (*s3.ListPartsOutput, error)

ListPartsWithContext mocks base method.

func (*MockS3API) PutBucketAccelerateConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutBucketAccelerateConfiguration(arg0 *s3.PutBucketAccelerateConfigurationInput) (*s3.PutBucketAccelerateConfigurationOutput, error)

PutBucketAccelerateConfiguration mocks base method.

func (*MockS3API) PutBucketAccelerateConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketAccelerateConfigurationRequest(arg0 *s3.PutBucketAccelerateConfigurationInput) (*request.Request, *s3.PutBucketAccelerateConfigurationOutput)

PutBucketAccelerateConfigurationRequest mocks base method.

func (*MockS3API) PutBucketAccelerateConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketAccelerateConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketAccelerateConfigurationInput, arg2 ...request.Option) (*s3.PutBucketAccelerateConfigurationOutput, error)

PutBucketAccelerateConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketAcl ¶
added in v1.3.0
func (m *MockS3API) PutBucketAcl(arg0 *s3.PutBucketAclInput) (*s3.PutBucketAclOutput, error)

PutBucketAcl mocks base method.

func (*MockS3API) PutBucketAclRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketAclRequest(arg0 *s3.PutBucketAclInput) (*request.Request, *s3.PutBucketAclOutput)

PutBucketAclRequest mocks base method.

func (*MockS3API) PutBucketAclWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketAclWithContext(arg0 aws.Context, arg1 *s3.PutBucketAclInput, arg2 ...request.Option) (*s3.PutBucketAclOutput, error)

PutBucketAclWithContext mocks base method.

func (*MockS3API) PutBucketAnalyticsConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutBucketAnalyticsConfiguration(arg0 *s3.PutBucketAnalyticsConfigurationInput) (*s3.PutBucketAnalyticsConfigurationOutput, error)

PutBucketAnalyticsConfiguration mocks base method.

func (*MockS3API) PutBucketAnalyticsConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketAnalyticsConfigurationRequest(arg0 *s3.PutBucketAnalyticsConfigurationInput) (*request.Request, *s3.PutBucketAnalyticsConfigurationOutput)

PutBucketAnalyticsConfigurationRequest mocks base method.

func (*MockS3API) PutBucketAnalyticsConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketAnalyticsConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketAnalyticsConfigurationInput, arg2 ...request.Option) (*s3.PutBucketAnalyticsConfigurationOutput, error)

PutBucketAnalyticsConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketCors ¶
added in v1.3.0
func (m *MockS3API) PutBucketCors(arg0 *s3.PutBucketCorsInput) (*s3.PutBucketCorsOutput, error)

PutBucketCors mocks base method.

func (*MockS3API) PutBucketCorsRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketCorsRequest(arg0 *s3.PutBucketCorsInput) (*request.Request, *s3.PutBucketCorsOutput)

PutBucketCorsRequest mocks base method.

func (*MockS3API) PutBucketCorsWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketCorsWithContext(arg0 aws.Context, arg1 *s3.PutBucketCorsInput, arg2 ...request.Option) (*s3.PutBucketCorsOutput, error)

PutBucketCorsWithContext mocks base method.

func (*MockS3API) PutBucketEncryption ¶
added in v1.3.0
func (m *MockS3API) PutBucketEncryption(arg0 *s3.PutBucketEncryptionInput) (*s3.PutBucketEncryptionOutput, error)

PutBucketEncryption mocks base method.

func (*MockS3API) PutBucketEncryptionRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketEncryptionRequest(arg0 *s3.PutBucketEncryptionInput) (*request.Request, *s3.PutBucketEncryptionOutput)

PutBucketEncryptionRequest mocks base method.

func (*MockS3API) PutBucketEncryptionWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketEncryptionWithContext(arg0 aws.Context, arg1 *s3.PutBucketEncryptionInput, arg2 ...request.Option) (*s3.PutBucketEncryptionOutput, error)

PutBucketEncryptionWithContext mocks base method.

func (*MockS3API) PutBucketIntelligentTieringConfiguration ¶
added in v1.5.7
func (m *MockS3API) PutBucketIntelligentTieringConfiguration(arg0 *s3.PutBucketIntelligentTieringConfigurationInput) (*s3.PutBucketIntelligentTieringConfigurationOutput, error)

PutBucketIntelligentTieringConfiguration mocks base method.

func (*MockS3API) PutBucketIntelligentTieringConfigurationRequest ¶
added in v1.5.7
func (m *MockS3API) PutBucketIntelligentTieringConfigurationRequest(arg0 *s3.PutBucketIntelligentTieringConfigurationInput) (*request.Request, *s3.PutBucketIntelligentTieringConfigurationOutput)

PutBucketIntelligentTieringConfigurationRequest mocks base method.

func (*MockS3API) PutBucketIntelligentTieringConfigurationWithContext ¶
added in v1.5.7
func (m *MockS3API) PutBucketIntelligentTieringConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketIntelligentTieringConfigurationInput, arg2 ...request.Option) (*s3.PutBucketIntelligentTieringConfigurationOutput, error)

PutBucketIntelligentTieringConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketInventoryConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutBucketInventoryConfiguration(arg0 *s3.PutBucketInventoryConfigurationInput) (*s3.PutBucketInventoryConfigurationOutput, error)

PutBucketInventoryConfiguration mocks base method.

func (*MockS3API) PutBucketInventoryConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketInventoryConfigurationRequest(arg0 *s3.PutBucketInventoryConfigurationInput) (*request.Request, *s3.PutBucketInventoryConfigurationOutput)

PutBucketInventoryConfigurationRequest mocks base method.

func (*MockS3API) PutBucketInventoryConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketInventoryConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketInventoryConfigurationInput, arg2 ...request.Option) (*s3.PutBucketInventoryConfigurationOutput, error)

PutBucketInventoryConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketLifecycle ¶
added in v1.3.0
func (m *MockS3API) PutBucketLifecycle(arg0 *s3.PutBucketLifecycleInput) (*s3.PutBucketLifecycleOutput, error)

PutBucketLifecycle mocks base method.

func (*MockS3API) PutBucketLifecycleConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutBucketLifecycleConfiguration(arg0 *s3.PutBucketLifecycleConfigurationInput) (*s3.PutBucketLifecycleConfigurationOutput, error)

PutBucketLifecycleConfiguration mocks base method.

func (*MockS3API) PutBucketLifecycleConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketLifecycleConfigurationRequest(arg0 *s3.PutBucketLifecycleConfigurationInput) (*request.Request, *s3.PutBucketLifecycleConfigurationOutput)

PutBucketLifecycleConfigurationRequest mocks base method.

func (*MockS3API) PutBucketLifecycleConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketLifecycleConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketLifecycleConfigurationInput, arg2 ...request.Option) (*s3.PutBucketLifecycleConfigurationOutput, error)

PutBucketLifecycleConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketLifecycleRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketLifecycleRequest(arg0 *s3.PutBucketLifecycleInput) (*request.Request, *s3.PutBucketLifecycleOutput)

PutBucketLifecycleRequest mocks base method.

func (*MockS3API) PutBucketLifecycleWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketLifecycleWithContext(arg0 aws.Context, arg1 *s3.PutBucketLifecycleInput, arg2 ...request.Option) (*s3.PutBucketLifecycleOutput, error)

PutBucketLifecycleWithContext mocks base method.

func (*MockS3API) PutBucketLogging ¶
added in v1.3.0
func (m *MockS3API) PutBucketLogging(arg0 *s3.PutBucketLoggingInput) (*s3.PutBucketLoggingOutput, error)

PutBucketLogging mocks base method.

func (*MockS3API) PutBucketLoggingRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketLoggingRequest(arg0 *s3.PutBucketLoggingInput) (*request.Request, *s3.PutBucketLoggingOutput)

PutBucketLoggingRequest mocks base method.

func (*MockS3API) PutBucketLoggingWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketLoggingWithContext(arg0 aws.Context, arg1 *s3.PutBucketLoggingInput, arg2 ...request.Option) (*s3.PutBucketLoggingOutput, error)

PutBucketLoggingWithContext mocks base method.

func (*MockS3API) PutBucketMetricsConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutBucketMetricsConfiguration(arg0 *s3.PutBucketMetricsConfigurationInput) (*s3.PutBucketMetricsConfigurationOutput, error)

PutBucketMetricsConfiguration mocks base method.

func (*MockS3API) PutBucketMetricsConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketMetricsConfigurationRequest(arg0 *s3.PutBucketMetricsConfigurationInput) (*request.Request, *s3.PutBucketMetricsConfigurationOutput)

PutBucketMetricsConfigurationRequest mocks base method.

func (*MockS3API) PutBucketMetricsConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketMetricsConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketMetricsConfigurationInput, arg2 ...request.Option) (*s3.PutBucketMetricsConfigurationOutput, error)

PutBucketMetricsConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketNotification ¶
added in v1.3.0
func (m *MockS3API) PutBucketNotification(arg0 *s3.PutBucketNotificationInput) (*s3.PutBucketNotificationOutput, error)

PutBucketNotification mocks base method.

func (*MockS3API) PutBucketNotificationConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutBucketNotificationConfiguration(arg0 *s3.PutBucketNotificationConfigurationInput) (*s3.PutBucketNotificationConfigurationOutput, error)

PutBucketNotificationConfiguration mocks base method.

func (*MockS3API) PutBucketNotificationConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketNotificationConfigurationRequest(arg0 *s3.PutBucketNotificationConfigurationInput) (*request.Request, *s3.PutBucketNotificationConfigurationOutput)

PutBucketNotificationConfigurationRequest mocks base method.

func (*MockS3API) PutBucketNotificationConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketNotificationConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutBucketNotificationConfigurationInput, arg2 ...request.Option) (*s3.PutBucketNotificationConfigurationOutput, error)

PutBucketNotificationConfigurationWithContext mocks base method.

func (*MockS3API) PutBucketNotificationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketNotificationRequest(arg0 *s3.PutBucketNotificationInput) (*request.Request, *s3.PutBucketNotificationOutput)

PutBucketNotificationRequest mocks base method.

func (*MockS3API) PutBucketNotificationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketNotificationWithContext(arg0 aws.Context, arg1 *s3.PutBucketNotificationInput, arg2 ...request.Option) (*s3.PutBucketNotificationOutput, error)

PutBucketNotificationWithContext mocks base method.

func (*MockS3API) PutBucketOwnershipControls ¶
added in v1.3.0
func (m *MockS3API) PutBucketOwnershipControls(arg0 *s3.PutBucketOwnershipControlsInput) (*s3.PutBucketOwnershipControlsOutput, error)

PutBucketOwnershipControls mocks base method.

func (*MockS3API) PutBucketOwnershipControlsRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketOwnershipControlsRequest(arg0 *s3.PutBucketOwnershipControlsInput) (*request.Request, *s3.PutBucketOwnershipControlsOutput)

PutBucketOwnershipControlsRequest mocks base method.

func (*MockS3API) PutBucketOwnershipControlsWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketOwnershipControlsWithContext(arg0 aws.Context, arg1 *s3.PutBucketOwnershipControlsInput, arg2 ...request.Option) (*s3.PutBucketOwnershipControlsOutput, error)

PutBucketOwnershipControlsWithContext mocks base method.

func (*MockS3API) PutBucketPolicy ¶
added in v1.3.0
func (m *MockS3API) PutBucketPolicy(arg0 *s3.PutBucketPolicyInput) (*s3.PutBucketPolicyOutput, error)

PutBucketPolicy mocks base method.

func (*MockS3API) PutBucketPolicyRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketPolicyRequest(arg0 *s3.PutBucketPolicyInput) (*request.Request, *s3.PutBucketPolicyOutput)

PutBucketPolicyRequest mocks base method.

func (*MockS3API) PutBucketPolicyWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketPolicyWithContext(arg0 aws.Context, arg1 *s3.PutBucketPolicyInput, arg2 ...request.Option) (*s3.PutBucketPolicyOutput, error)

PutBucketPolicyWithContext mocks base method.

func (*MockS3API) PutBucketReplication ¶
added in v1.3.0
func (m *MockS3API) PutBucketReplication(arg0 *s3.PutBucketReplicationInput) (*s3.PutBucketReplicationOutput, error)

PutBucketReplication mocks base method.

func (*MockS3API) PutBucketReplicationRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketReplicationRequest(arg0 *s3.PutBucketReplicationInput) (*request.Request, *s3.PutBucketReplicationOutput)

PutBucketReplicationRequest mocks base method.

func (*MockS3API) PutBucketReplicationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketReplicationWithContext(arg0 aws.Context, arg1 *s3.PutBucketReplicationInput, arg2 ...request.Option) (*s3.PutBucketReplicationOutput, error)

PutBucketReplicationWithContext mocks base method.

func (*MockS3API) PutBucketRequestPayment ¶
added in v1.3.0
func (m *MockS3API) PutBucketRequestPayment(arg0 *s3.PutBucketRequestPaymentInput) (*s3.PutBucketRequestPaymentOutput, error)

PutBucketRequestPayment mocks base method.

func (*MockS3API) PutBucketRequestPaymentRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketRequestPaymentRequest(arg0 *s3.PutBucketRequestPaymentInput) (*request.Request, *s3.PutBucketRequestPaymentOutput)

PutBucketRequestPaymentRequest mocks base method.

func (*MockS3API) PutBucketRequestPaymentWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketRequestPaymentWithContext(arg0 aws.Context, arg1 *s3.PutBucketRequestPaymentInput, arg2 ...request.Option) (*s3.PutBucketRequestPaymentOutput, error)

PutBucketRequestPaymentWithContext mocks base method.

func (*MockS3API) PutBucketTagging ¶
added in v1.3.0
func (m *MockS3API) PutBucketTagging(arg0 *s3.PutBucketTaggingInput) (*s3.PutBucketTaggingOutput, error)

PutBucketTagging mocks base method.

func (*MockS3API) PutBucketTaggingRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketTaggingRequest(arg0 *s3.PutBucketTaggingInput) (*request.Request, *s3.PutBucketTaggingOutput)

PutBucketTaggingRequest mocks base method.

func (*MockS3API) PutBucketTaggingWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketTaggingWithContext(arg0 aws.Context, arg1 *s3.PutBucketTaggingInput, arg2 ...request.Option) (*s3.PutBucketTaggingOutput, error)

PutBucketTaggingWithContext mocks base method.

func (*MockS3API) PutBucketVersioning ¶
added in v1.3.0
func (m *MockS3API) PutBucketVersioning(arg0 *s3.PutBucketVersioningInput) (*s3.PutBucketVersioningOutput, error)

PutBucketVersioning mocks base method.

func (*MockS3API) PutBucketVersioningRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketVersioningRequest(arg0 *s3.PutBucketVersioningInput) (*request.Request, *s3.PutBucketVersioningOutput)

PutBucketVersioningRequest mocks base method.

func (*MockS3API) PutBucketVersioningWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketVersioningWithContext(arg0 aws.Context, arg1 *s3.PutBucketVersioningInput, arg2 ...request.Option) (*s3.PutBucketVersioningOutput, error)

PutBucketVersioningWithContext mocks base method.

func (*MockS3API) PutBucketWebsite ¶
added in v1.3.0
func (m *MockS3API) PutBucketWebsite(arg0 *s3.PutBucketWebsiteInput) (*s3.PutBucketWebsiteOutput, error)

PutBucketWebsite mocks base method.

func (*MockS3API) PutBucketWebsiteRequest ¶
added in v1.3.0
func (m *MockS3API) PutBucketWebsiteRequest(arg0 *s3.PutBucketWebsiteInput) (*request.Request, *s3.PutBucketWebsiteOutput)

PutBucketWebsiteRequest mocks base method.

func (*MockS3API) PutBucketWebsiteWithContext ¶
added in v1.3.0
func (m *MockS3API) PutBucketWebsiteWithContext(arg0 aws.Context, arg1 *s3.PutBucketWebsiteInput, arg2 ...request.Option) (*s3.PutBucketWebsiteOutput, error)

PutBucketWebsiteWithContext mocks base method.

func (*MockS3API) PutObject ¶
added in v1.3.0
func (m *MockS3API) PutObject(arg0 *s3.PutObjectInput) (*s3.PutObjectOutput, error)

PutObject mocks base method.

func (*MockS3API) PutObjectAcl ¶
added in v1.3.0
func (m *MockS3API) PutObjectAcl(arg0 *s3.PutObjectAclInput) (*s3.PutObjectAclOutput, error)

PutObjectAcl mocks base method.

func (*MockS3API) PutObjectAclRequest ¶
added in v1.3.0
func (m *MockS3API) PutObjectAclRequest(arg0 *s3.PutObjectAclInput) (*request.Request, *s3.PutObjectAclOutput)

PutObjectAclRequest mocks base method.

func (*MockS3API) PutObjectAclWithContext ¶
added in v1.3.0
func (m *MockS3API) PutObjectAclWithContext(arg0 aws.Context, arg1 *s3.PutObjectAclInput, arg2 ...request.Option) (*s3.PutObjectAclOutput, error)

PutObjectAclWithContext mocks base method.

func (*MockS3API) PutObjectLegalHold ¶
added in v1.3.0
func (m *MockS3API) PutObjectLegalHold(arg0 *s3.PutObjectLegalHoldInput) (*s3.PutObjectLegalHoldOutput, error)

PutObjectLegalHold mocks base method.

func (*MockS3API) PutObjectLegalHoldRequest ¶
added in v1.3.0
func (m *MockS3API) PutObjectLegalHoldRequest(arg0 *s3.PutObjectLegalHoldInput) (*request.Request, *s3.PutObjectLegalHoldOutput)

PutObjectLegalHoldRequest mocks base method.

func (*MockS3API) PutObjectLegalHoldWithContext ¶
added in v1.3.0
func (m *MockS3API) PutObjectLegalHoldWithContext(arg0 aws.Context, arg1 *s3.PutObjectLegalHoldInput, arg2 ...request.Option) (*s3.PutObjectLegalHoldOutput, error)

PutObjectLegalHoldWithContext mocks base method.

func (*MockS3API) PutObjectLockConfiguration ¶
added in v1.3.0
func (m *MockS3API) PutObjectLockConfiguration(arg0 *s3.PutObjectLockConfigurationInput) (*s3.PutObjectLockConfigurationOutput, error)

PutObjectLockConfiguration mocks base method.

func (*MockS3API) PutObjectLockConfigurationRequest ¶
added in v1.3.0
func (m *MockS3API) PutObjectLockConfigurationRequest(arg0 *s3.PutObjectLockConfigurationInput) (*request.Request, *s3.PutObjectLockConfigurationOutput)

PutObjectLockConfigurationRequest mocks base method.

func (*MockS3API) PutObjectLockConfigurationWithContext ¶
added in v1.3.0
func (m *MockS3API) PutObjectLockConfigurationWithContext(arg0 aws.Context, arg1 *s3.PutObjectLockConfigurationInput, arg2 ...request.Option) (*s3.PutObjectLockConfigurationOutput, error)

PutObjectLockConfigurationWithContext mocks base method.

func (*MockS3API) PutObjectRequest ¶
added in v1.3.0
func (m *MockS3API) PutObjectRequest(arg0 *s3.PutObjectInput) (*request.Request, *s3.PutObjectOutput)

PutObjectRequest mocks base method.

func (*MockS3API) PutObjectRetention ¶
added in v1.3.0
func (m *MockS3API) PutObjectRetention(arg0 *s3.PutObjectRetentionInput) (*s3.PutObjectRetentionOutput, error)

PutObjectRetention mocks base method.

func (*MockS3API) PutObjectRetentionRequest ¶
added in v1.3.0
func (m *MockS3API) PutObjectRetentionRequest(arg0 *s3.PutObjectRetentionInput) (*request.Request, *s3.PutObjectRetentionOutput)

PutObjectRetentionRequest mocks base method.

func (*MockS3API) PutObjectRetentionWithContext ¶
added in v1.3.0
func (m *MockS3API) PutObjectRetentionWithContext(arg0 aws.Context, arg1 *s3.PutObjectRetentionInput, arg2 ...request.Option) (*s3.PutObjectRetentionOutput, error)

PutObjectRetentionWithContext mocks base method.

func (*MockS3API) PutObjectTagging ¶
added in v1.3.0
func (m *MockS3API) PutObjectTagging(arg0 *s3.PutObjectTaggingInput) (*s3.PutObjectTaggingOutput, error)

PutObjectTagging mocks base method.

func (*MockS3API) PutObjectTaggingRequest ¶
added in v1.3.0
func (m *MockS3API) PutObjectTaggingRequest(arg0 *s3.PutObjectTaggingInput) (*request.Request, *s3.PutObjectTaggingOutput)

PutObjectTaggingRequest mocks base method.

func (*MockS3API) PutObjectTaggingWithContext ¶
added in v1.3.0
func (m *MockS3API) PutObjectTaggingWithContext(arg0 aws.Context, arg1 *s3.PutObjectTaggingInput, arg2 ...request.Option) (*s3.PutObjectTaggingOutput, error)

PutObjectTaggingWithContext mocks base method.

func (*MockS3API) PutObjectWithContext ¶
added in v1.3.0
func (m *MockS3API) PutObjectWithContext(arg0 aws.Context, arg1 *s3.PutObjectInput, arg2 ...request.Option) (*s3.PutObjectOutput, error)

PutObjectWithContext mocks base method.

func (*MockS3API) PutPublicAccessBlock ¶
added in v1.3.0
func (m *MockS3API) PutPublicAccessBlock(arg0 *s3.PutPublicAccessBlockInput) (*s3.PutPublicAccessBlockOutput, error)

PutPublicAccessBlock mocks base method.

func (*MockS3API) PutPublicAccessBlockRequest ¶
added in v1.3.0
func (m *MockS3API) PutPublicAccessBlockRequest(arg0 *s3.PutPublicAccessBlockInput) (*request.Request, *s3.PutPublicAccessBlockOutput)

PutPublicAccessBlockRequest mocks base method.

func (*MockS3API) PutPublicAccessBlockWithContext ¶
added in v1.3.0
func (m *MockS3API) PutPublicAccessBlockWithContext(arg0 aws.Context, arg1 *s3.PutPublicAccessBlockInput, arg2 ...request.Option) (*s3.PutPublicAccessBlockOutput, error)

PutPublicAccessBlockWithContext mocks base method.

func (*MockS3API) RestoreObject ¶
added in v1.3.0
func (m *MockS3API) RestoreObject(arg0 *s3.RestoreObjectInput) (*s3.RestoreObjectOutput, error)

RestoreObject mocks base method.

func (*MockS3API) RestoreObjectRequest ¶
added in v1.3.0
func (m *MockS3API) RestoreObjectRequest(arg0 *s3.RestoreObjectInput) (*request.Request, *s3.RestoreObjectOutput)

RestoreObjectRequest mocks base method.

func (*MockS3API) RestoreObjectWithContext ¶
added in v1.3.0
func (m *MockS3API) RestoreObjectWithContext(arg0 aws.Context, arg1 *s3.RestoreObjectInput, arg2 ...request.Option) (*s3.RestoreObjectOutput, error)

RestoreObjectWithContext mocks base method.

func (*MockS3API) SelectObjectContent ¶
added in v1.3.0
func (m *MockS3API) SelectObjectContent(arg0 *s3.SelectObjectContentInput) (*s3.SelectObjectContentOutput, error)

SelectObjectContent mocks base method.

func (*MockS3API) SelectObjectContentRequest ¶
added in v1.3.0
func (m *MockS3API) SelectObjectContentRequest(arg0 *s3.SelectObjectContentInput) (*request.Request, *s3.SelectObjectContentOutput)

SelectObjectContentRequest mocks base method.

func (*MockS3API) SelectObjectContentWithContext ¶
added in v1.3.0
func (m *MockS3API) SelectObjectContentWithContext(arg0 aws.Context, arg1 *s3.SelectObjectContentInput, arg2 ...request.Option) (*s3.SelectObjectContentOutput, error)

SelectObjectContentWithContext mocks base method.

func (*MockS3API) UploadPart ¶
added in v1.3.0
func (m *MockS3API) UploadPart(arg0 *s3.UploadPartInput) (*s3.UploadPartOutput, error)

UploadPart mocks base method.

func (*MockS3API) UploadPartCopy ¶
added in v1.3.0
func (m *MockS3API) UploadPartCopy(arg0 *s3.UploadPartCopyInput) (*s3.UploadPartCopyOutput, error)

UploadPartCopy mocks base method.

func (*MockS3API) UploadPartCopyRequest ¶
added in v1.3.0
func (m *MockS3API) UploadPartCopyRequest(arg0 *s3.UploadPartCopyInput) (*request.Request, *s3.UploadPartCopyOutput)

UploadPartCopyRequest mocks base method.

func (*MockS3API) UploadPartCopyWithContext ¶
added in v1.3.0
func (m *MockS3API) UploadPartCopyWithContext(arg0 aws.Context, arg1 *s3.UploadPartCopyInput, arg2 ...request.Option) (*s3.UploadPartCopyOutput, error)

UploadPartCopyWithContext mocks base method.

func (*MockS3API) UploadPartRequest ¶
added in v1.3.0
func (m *MockS3API) UploadPartRequest(arg0 *s3.UploadPartInput) (*request.Request, *s3.UploadPartOutput)

UploadPartRequest mocks base method.

func (*MockS3API) UploadPartWithContext ¶
added in v1.3.0
func (m *MockS3API) UploadPartWithContext(arg0 aws.Context, arg1 *s3.UploadPartInput, arg2 ...request.Option) (*s3.UploadPartOutput, error)

UploadPartWithContext mocks base method.

func (*MockS3API) WaitUntilBucketExists ¶
added in v1.3.0
func (m *MockS3API) WaitUntilBucketExists(arg0 *s3.HeadBucketInput) error

WaitUntilBucketExists mocks base method.

func (*MockS3API) WaitUntilBucketExistsWithContext ¶
added in v1.3.0
func (m *MockS3API) WaitUntilBucketExistsWithContext(arg0 aws.Context, arg1 *s3.HeadBucketInput, arg2 ...request.WaiterOption) error

WaitUntilBucketExistsWithContext mocks base method.

func (*MockS3API) WaitUntilBucketNotExists ¶
added in v1.3.0
func (m *MockS3API) WaitUntilBucketNotExists(arg0 *s3.HeadBucketInput) error

WaitUntilBucketNotExists mocks base method.

func (*MockS3API) WaitUntilBucketNotExistsWithContext ¶
added in v1.3.0
func (m *MockS3API) WaitUntilBucketNotExistsWithContext(arg0 aws.Context, arg1 *s3.HeadBucketInput, arg2 ...request.WaiterOption) error

WaitUntilBucketNotExistsWithContext mocks base method.

func (*MockS3API) WaitUntilObjectExists ¶
added in v1.3.0
func (m *MockS3API) WaitUntilObjectExists(arg0 *s3.HeadObjectInput) error

WaitUntilObjectExists mocks base method.

func (*MockS3API) WaitUntilObjectExistsWithContext ¶
added in v1.3.0
func (m *MockS3API) WaitUntilObjectExistsWithContext(arg0 aws.Context, arg1 *s3.HeadObjectInput, arg2 ...request.WaiterOption) error

WaitUntilObjectExistsWithContext mocks base method.

func (*MockS3API) WaitUntilObjectNotExists ¶
added in v1.3.0
func (m *MockS3API) WaitUntilObjectNotExists(arg0 *s3.HeadObjectInput) error

WaitUntilObjectNotExists mocks base method.

func (*MockS3API) WaitUntilObjectNotExistsWithContext ¶
added in v1.3.0
func (m *MockS3API) WaitUntilObjectNotExistsWithContext(arg0 aws.Context, arg1 *s3.HeadObjectInput, arg2 ...request.WaiterOption) error

WaitUntilObjectNotExistsWithContext mocks base method.

func (*MockS3API) WriteGetObjectResponse ¶
added in v1.10.0
func (m *MockS3API) WriteGetObjectResponse(arg0 *s3.WriteGetObjectResponseInput) (*s3.WriteGetObjectResponseOutput, error)

WriteGetObjectResponse mocks base method.

func (*MockS3API) WriteGetObjectResponseRequest ¶
added in v1.10.0
func (m *MockS3API) WriteGetObjectResponseRequest(arg0 *s3.WriteGetObjectResponseInput) (*request.Request, *s3.WriteGetObjectResponseOutput)

WriteGetObjectResponseRequest mocks base method.

func (*MockS3API) WriteGetObjectResponseWithContext ¶
added in v1.10.0
func (m *MockS3API) WriteGetObjectResponseWithContext(arg0 aws.Context, arg1 *s3.WriteGetObjectResponseInput, arg2 ...request.Option) (*s3.WriteGetObjectResponseOutput, error)

WriteGetObjectResponseWithContext mocks base method.

type MockS3APIMockRecorder ¶
added in v1.3.0
type MockS3APIMockRecorder struct {
	// contains filtered or unexported fields
}

MockS3APIMockRecorder is the mock recorder for MockS3API.

func (*MockS3APIMockRecorder) AbortMultipartUpload ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) AbortMultipartUpload(arg0 any) *gomock.Call

AbortMultipartUpload indicates an expected call of AbortMultipartUpload.

func (*MockS3APIMockRecorder) AbortMultipartUploadRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) AbortMultipartUploadRequest(arg0 any) *gomock.Call

AbortMultipartUploadRequest indicates an expected call of AbortMultipartUploadRequest.

func (*MockS3APIMockRecorder) AbortMultipartUploadWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) AbortMultipartUploadWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

AbortMultipartUploadWithContext indicates an expected call of AbortMultipartUploadWithContext.

func (*MockS3APIMockRecorder) CompleteMultipartUpload ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CompleteMultipartUpload(arg0 any) *gomock.Call

CompleteMultipartUpload indicates an expected call of CompleteMultipartUpload.

func (*MockS3APIMockRecorder) CompleteMultipartUploadRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CompleteMultipartUploadRequest(arg0 any) *gomock.Call

CompleteMultipartUploadRequest indicates an expected call of CompleteMultipartUploadRequest.

func (*MockS3APIMockRecorder) CompleteMultipartUploadWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CompleteMultipartUploadWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

CompleteMultipartUploadWithContext indicates an expected call of CompleteMultipartUploadWithContext.

func (*MockS3APIMockRecorder) CopyObject ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CopyObject(arg0 any) *gomock.Call

CopyObject indicates an expected call of CopyObject.

func (*MockS3APIMockRecorder) CopyObjectRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CopyObjectRequest(arg0 any) *gomock.Call

CopyObjectRequest indicates an expected call of CopyObjectRequest.

func (*MockS3APIMockRecorder) CopyObjectWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CopyObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

CopyObjectWithContext indicates an expected call of CopyObjectWithContext.

func (*MockS3APIMockRecorder) CreateBucket ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CreateBucket(arg0 any) *gomock.Call

CreateBucket indicates an expected call of CreateBucket.

func (*MockS3APIMockRecorder) CreateBucketRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CreateBucketRequest(arg0 any) *gomock.Call

CreateBucketRequest indicates an expected call of CreateBucketRequest.

func (*MockS3APIMockRecorder) CreateBucketWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CreateBucketWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

CreateBucketWithContext indicates an expected call of CreateBucketWithContext.

func (*MockS3APIMockRecorder) CreateMultipartUpload ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CreateMultipartUpload(arg0 any) *gomock.Call

CreateMultipartUpload indicates an expected call of CreateMultipartUpload.

func (*MockS3APIMockRecorder) CreateMultipartUploadRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CreateMultipartUploadRequest(arg0 any) *gomock.Call

CreateMultipartUploadRequest indicates an expected call of CreateMultipartUploadRequest.

func (*MockS3APIMockRecorder) CreateMultipartUploadWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) CreateMultipartUploadWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

CreateMultipartUploadWithContext indicates an expected call of CreateMultipartUploadWithContext.

func (*MockS3APIMockRecorder) CreateSession ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) CreateSession(arg0 any) *gomock.Call

CreateSession indicates an expected call of CreateSession.

func (*MockS3APIMockRecorder) CreateSessionRequest ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) CreateSessionRequest(arg0 any) *gomock.Call

CreateSessionRequest indicates an expected call of CreateSessionRequest.

func (*MockS3APIMockRecorder) CreateSessionWithContext ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) CreateSessionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

CreateSessionWithContext indicates an expected call of CreateSessionWithContext.

func (*MockS3APIMockRecorder) DeleteBucket ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucket(arg0 any) *gomock.Call

DeleteBucket indicates an expected call of DeleteBucket.

func (*MockS3APIMockRecorder) DeleteBucketAnalyticsConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketAnalyticsConfiguration(arg0 any) *gomock.Call

DeleteBucketAnalyticsConfiguration indicates an expected call of DeleteBucketAnalyticsConfiguration.

func (*MockS3APIMockRecorder) DeleteBucketAnalyticsConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketAnalyticsConfigurationRequest(arg0 any) *gomock.Call

DeleteBucketAnalyticsConfigurationRequest indicates an expected call of DeleteBucketAnalyticsConfigurationRequest.

func (*MockS3APIMockRecorder) DeleteBucketAnalyticsConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketAnalyticsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketAnalyticsConfigurationWithContext indicates an expected call of DeleteBucketAnalyticsConfigurationWithContext.

func (*MockS3APIMockRecorder) DeleteBucketCors ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketCors(arg0 any) *gomock.Call

DeleteBucketCors indicates an expected call of DeleteBucketCors.

func (*MockS3APIMockRecorder) DeleteBucketCorsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketCorsRequest(arg0 any) *gomock.Call

DeleteBucketCorsRequest indicates an expected call of DeleteBucketCorsRequest.

func (*MockS3APIMockRecorder) DeleteBucketCorsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketCorsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketCorsWithContext indicates an expected call of DeleteBucketCorsWithContext.

func (*MockS3APIMockRecorder) DeleteBucketEncryption ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketEncryption(arg0 any) *gomock.Call

DeleteBucketEncryption indicates an expected call of DeleteBucketEncryption.

func (*MockS3APIMockRecorder) DeleteBucketEncryptionRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketEncryptionRequest(arg0 any) *gomock.Call

DeleteBucketEncryptionRequest indicates an expected call of DeleteBucketEncryptionRequest.

func (*MockS3APIMockRecorder) DeleteBucketEncryptionWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketEncryptionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketEncryptionWithContext indicates an expected call of DeleteBucketEncryptionWithContext.

func (*MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfiguration ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfiguration(arg0 any) *gomock.Call

DeleteBucketIntelligentTieringConfiguration indicates an expected call of DeleteBucketIntelligentTieringConfiguration.

func (*MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfigurationRequest ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfigurationRequest(arg0 any) *gomock.Call

DeleteBucketIntelligentTieringConfigurationRequest indicates an expected call of DeleteBucketIntelligentTieringConfigurationRequest.

func (*MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfigurationWithContext ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) DeleteBucketIntelligentTieringConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketIntelligentTieringConfigurationWithContext indicates an expected call of DeleteBucketIntelligentTieringConfigurationWithContext.

func (*MockS3APIMockRecorder) DeleteBucketInventoryConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketInventoryConfiguration(arg0 any) *gomock.Call

DeleteBucketInventoryConfiguration indicates an expected call of DeleteBucketInventoryConfiguration.

func (*MockS3APIMockRecorder) DeleteBucketInventoryConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketInventoryConfigurationRequest(arg0 any) *gomock.Call

DeleteBucketInventoryConfigurationRequest indicates an expected call of DeleteBucketInventoryConfigurationRequest.

func (*MockS3APIMockRecorder) DeleteBucketInventoryConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketInventoryConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketInventoryConfigurationWithContext indicates an expected call of DeleteBucketInventoryConfigurationWithContext.

func (*MockS3APIMockRecorder) DeleteBucketLifecycle ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketLifecycle(arg0 any) *gomock.Call

DeleteBucketLifecycle indicates an expected call of DeleteBucketLifecycle.

func (*MockS3APIMockRecorder) DeleteBucketLifecycleRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketLifecycleRequest(arg0 any) *gomock.Call

DeleteBucketLifecycleRequest indicates an expected call of DeleteBucketLifecycleRequest.

func (*MockS3APIMockRecorder) DeleteBucketLifecycleWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketLifecycleWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketLifecycleWithContext indicates an expected call of DeleteBucketLifecycleWithContext.

func (*MockS3APIMockRecorder) DeleteBucketMetricsConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketMetricsConfiguration(arg0 any) *gomock.Call

DeleteBucketMetricsConfiguration indicates an expected call of DeleteBucketMetricsConfiguration.

func (*MockS3APIMockRecorder) DeleteBucketMetricsConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketMetricsConfigurationRequest(arg0 any) *gomock.Call

DeleteBucketMetricsConfigurationRequest indicates an expected call of DeleteBucketMetricsConfigurationRequest.

func (*MockS3APIMockRecorder) DeleteBucketMetricsConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketMetricsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketMetricsConfigurationWithContext indicates an expected call of DeleteBucketMetricsConfigurationWithContext.

func (*MockS3APIMockRecorder) DeleteBucketOwnershipControls ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketOwnershipControls(arg0 any) *gomock.Call

DeleteBucketOwnershipControls indicates an expected call of DeleteBucketOwnershipControls.

func (*MockS3APIMockRecorder) DeleteBucketOwnershipControlsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketOwnershipControlsRequest(arg0 any) *gomock.Call

DeleteBucketOwnershipControlsRequest indicates an expected call of DeleteBucketOwnershipControlsRequest.

func (*MockS3APIMockRecorder) DeleteBucketOwnershipControlsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketOwnershipControlsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketOwnershipControlsWithContext indicates an expected call of DeleteBucketOwnershipControlsWithContext.

func (*MockS3APIMockRecorder) DeleteBucketPolicy ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketPolicy(arg0 any) *gomock.Call

DeleteBucketPolicy indicates an expected call of DeleteBucketPolicy.

func (*MockS3APIMockRecorder) DeleteBucketPolicyRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketPolicyRequest(arg0 any) *gomock.Call

DeleteBucketPolicyRequest indicates an expected call of DeleteBucketPolicyRequest.

func (*MockS3APIMockRecorder) DeleteBucketPolicyWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketPolicyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketPolicyWithContext indicates an expected call of DeleteBucketPolicyWithContext.

func (*MockS3APIMockRecorder) DeleteBucketReplication ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketReplication(arg0 any) *gomock.Call

DeleteBucketReplication indicates an expected call of DeleteBucketReplication.

func (*MockS3APIMockRecorder) DeleteBucketReplicationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketReplicationRequest(arg0 any) *gomock.Call

DeleteBucketReplicationRequest indicates an expected call of DeleteBucketReplicationRequest.

func (*MockS3APIMockRecorder) DeleteBucketReplicationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketReplicationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketReplicationWithContext indicates an expected call of DeleteBucketReplicationWithContext.

func (*MockS3APIMockRecorder) DeleteBucketRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketRequest(arg0 any) *gomock.Call

DeleteBucketRequest indicates an expected call of DeleteBucketRequest.

func (*MockS3APIMockRecorder) DeleteBucketTagging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketTagging(arg0 any) *gomock.Call

DeleteBucketTagging indicates an expected call of DeleteBucketTagging.

func (*MockS3APIMockRecorder) DeleteBucketTaggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketTaggingRequest(arg0 any) *gomock.Call

DeleteBucketTaggingRequest indicates an expected call of DeleteBucketTaggingRequest.

func (*MockS3APIMockRecorder) DeleteBucketTaggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketTaggingWithContext indicates an expected call of DeleteBucketTaggingWithContext.

func (*MockS3APIMockRecorder) DeleteBucketWebsite ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketWebsite(arg0 any) *gomock.Call

DeleteBucketWebsite indicates an expected call of DeleteBucketWebsite.

func (*MockS3APIMockRecorder) DeleteBucketWebsiteRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketWebsiteRequest(arg0 any) *gomock.Call

DeleteBucketWebsiteRequest indicates an expected call of DeleteBucketWebsiteRequest.

func (*MockS3APIMockRecorder) DeleteBucketWebsiteWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketWebsiteWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketWebsiteWithContext indicates an expected call of DeleteBucketWebsiteWithContext.

func (*MockS3APIMockRecorder) DeleteBucketWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteBucketWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteBucketWithContext indicates an expected call of DeleteBucketWithContext.

func (*MockS3APIMockRecorder) DeleteObject ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObject(arg0 any) *gomock.Call

DeleteObject indicates an expected call of DeleteObject.

func (*MockS3APIMockRecorder) DeleteObjectRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectRequest(arg0 any) *gomock.Call

DeleteObjectRequest indicates an expected call of DeleteObjectRequest.

func (*MockS3APIMockRecorder) DeleteObjectTagging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectTagging(arg0 any) *gomock.Call

DeleteObjectTagging indicates an expected call of DeleteObjectTagging.

func (*MockS3APIMockRecorder) DeleteObjectTaggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectTaggingRequest(arg0 any) *gomock.Call

DeleteObjectTaggingRequest indicates an expected call of DeleteObjectTaggingRequest.

func (*MockS3APIMockRecorder) DeleteObjectTaggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteObjectTaggingWithContext indicates an expected call of DeleteObjectTaggingWithContext.

func (*MockS3APIMockRecorder) DeleteObjectWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteObjectWithContext indicates an expected call of DeleteObjectWithContext.

func (*MockS3APIMockRecorder) DeleteObjects ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjects(arg0 any) *gomock.Call

DeleteObjects indicates an expected call of DeleteObjects.

func (*MockS3APIMockRecorder) DeleteObjectsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectsRequest(arg0 any) *gomock.Call

DeleteObjectsRequest indicates an expected call of DeleteObjectsRequest.

func (*MockS3APIMockRecorder) DeleteObjectsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeleteObjectsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeleteObjectsWithContext indicates an expected call of DeleteObjectsWithContext.

func (*MockS3APIMockRecorder) DeletePublicAccessBlock ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeletePublicAccessBlock(arg0 any) *gomock.Call

DeletePublicAccessBlock indicates an expected call of DeletePublicAccessBlock.

func (*MockS3APIMockRecorder) DeletePublicAccessBlockRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeletePublicAccessBlockRequest(arg0 any) *gomock.Call

DeletePublicAccessBlockRequest indicates an expected call of DeletePublicAccessBlockRequest.

func (*MockS3APIMockRecorder) DeletePublicAccessBlockWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) DeletePublicAccessBlockWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

DeletePublicAccessBlockWithContext indicates an expected call of DeletePublicAccessBlockWithContext.

func (*MockS3APIMockRecorder) GetBucketAccelerateConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAccelerateConfiguration(arg0 any) *gomock.Call

GetBucketAccelerateConfiguration indicates an expected call of GetBucketAccelerateConfiguration.

func (*MockS3APIMockRecorder) GetBucketAccelerateConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAccelerateConfigurationRequest(arg0 any) *gomock.Call

GetBucketAccelerateConfigurationRequest indicates an expected call of GetBucketAccelerateConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketAccelerateConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAccelerateConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketAccelerateConfigurationWithContext indicates an expected call of GetBucketAccelerateConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketAcl ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAcl(arg0 any) *gomock.Call

GetBucketAcl indicates an expected call of GetBucketAcl.

func (*MockS3APIMockRecorder) GetBucketAclRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAclRequest(arg0 any) *gomock.Call

GetBucketAclRequest indicates an expected call of GetBucketAclRequest.

func (*MockS3APIMockRecorder) GetBucketAclWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketAclWithContext indicates an expected call of GetBucketAclWithContext.

func (*MockS3APIMockRecorder) GetBucketAnalyticsConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAnalyticsConfiguration(arg0 any) *gomock.Call

GetBucketAnalyticsConfiguration indicates an expected call of GetBucketAnalyticsConfiguration.

func (*MockS3APIMockRecorder) GetBucketAnalyticsConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAnalyticsConfigurationRequest(arg0 any) *gomock.Call

GetBucketAnalyticsConfigurationRequest indicates an expected call of GetBucketAnalyticsConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketAnalyticsConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketAnalyticsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketAnalyticsConfigurationWithContext indicates an expected call of GetBucketAnalyticsConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketCors ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketCors(arg0 any) *gomock.Call

GetBucketCors indicates an expected call of GetBucketCors.

func (*MockS3APIMockRecorder) GetBucketCorsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketCorsRequest(arg0 any) *gomock.Call

GetBucketCorsRequest indicates an expected call of GetBucketCorsRequest.

func (*MockS3APIMockRecorder) GetBucketCorsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketCorsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketCorsWithContext indicates an expected call of GetBucketCorsWithContext.

func (*MockS3APIMockRecorder) GetBucketEncryption ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketEncryption(arg0 any) *gomock.Call

GetBucketEncryption indicates an expected call of GetBucketEncryption.

func (*MockS3APIMockRecorder) GetBucketEncryptionRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketEncryptionRequest(arg0 any) *gomock.Call

GetBucketEncryptionRequest indicates an expected call of GetBucketEncryptionRequest.

func (*MockS3APIMockRecorder) GetBucketEncryptionWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketEncryptionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketEncryptionWithContext indicates an expected call of GetBucketEncryptionWithContext.

func (*MockS3APIMockRecorder) GetBucketIntelligentTieringConfiguration ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) GetBucketIntelligentTieringConfiguration(arg0 any) *gomock.Call

GetBucketIntelligentTieringConfiguration indicates an expected call of GetBucketIntelligentTieringConfiguration.

func (*MockS3APIMockRecorder) GetBucketIntelligentTieringConfigurationRequest ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) GetBucketIntelligentTieringConfigurationRequest(arg0 any) *gomock.Call

GetBucketIntelligentTieringConfigurationRequest indicates an expected call of GetBucketIntelligentTieringConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketIntelligentTieringConfigurationWithContext ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) GetBucketIntelligentTieringConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketIntelligentTieringConfigurationWithContext indicates an expected call of GetBucketIntelligentTieringConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketInventoryConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketInventoryConfiguration(arg0 any) *gomock.Call

GetBucketInventoryConfiguration indicates an expected call of GetBucketInventoryConfiguration.

func (*MockS3APIMockRecorder) GetBucketInventoryConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketInventoryConfigurationRequest(arg0 any) *gomock.Call

GetBucketInventoryConfigurationRequest indicates an expected call of GetBucketInventoryConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketInventoryConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketInventoryConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketInventoryConfigurationWithContext indicates an expected call of GetBucketInventoryConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketLifecycle ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLifecycle(arg0 any) *gomock.Call

GetBucketLifecycle indicates an expected call of GetBucketLifecycle.

func (*MockS3APIMockRecorder) GetBucketLifecycleConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLifecycleConfiguration(arg0 any) *gomock.Call

GetBucketLifecycleConfiguration indicates an expected call of GetBucketLifecycleConfiguration.

func (*MockS3APIMockRecorder) GetBucketLifecycleConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLifecycleConfigurationRequest(arg0 any) *gomock.Call

GetBucketLifecycleConfigurationRequest indicates an expected call of GetBucketLifecycleConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketLifecycleConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLifecycleConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketLifecycleConfigurationWithContext indicates an expected call of GetBucketLifecycleConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketLifecycleRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLifecycleRequest(arg0 any) *gomock.Call

GetBucketLifecycleRequest indicates an expected call of GetBucketLifecycleRequest.

func (*MockS3APIMockRecorder) GetBucketLifecycleWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLifecycleWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketLifecycleWithContext indicates an expected call of GetBucketLifecycleWithContext.

func (*MockS3APIMockRecorder) GetBucketLocation ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLocation(arg0 any) *gomock.Call

GetBucketLocation indicates an expected call of GetBucketLocation.

func (*MockS3APIMockRecorder) GetBucketLocationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLocationRequest(arg0 any) *gomock.Call

GetBucketLocationRequest indicates an expected call of GetBucketLocationRequest.

func (*MockS3APIMockRecorder) GetBucketLocationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLocationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketLocationWithContext indicates an expected call of GetBucketLocationWithContext.

func (*MockS3APIMockRecorder) GetBucketLogging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLogging(arg0 any) *gomock.Call

GetBucketLogging indicates an expected call of GetBucketLogging.

func (*MockS3APIMockRecorder) GetBucketLoggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLoggingRequest(arg0 any) *gomock.Call

GetBucketLoggingRequest indicates an expected call of GetBucketLoggingRequest.

func (*MockS3APIMockRecorder) GetBucketLoggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketLoggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketLoggingWithContext indicates an expected call of GetBucketLoggingWithContext.

func (*MockS3APIMockRecorder) GetBucketMetricsConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketMetricsConfiguration(arg0 any) *gomock.Call

GetBucketMetricsConfiguration indicates an expected call of GetBucketMetricsConfiguration.

func (*MockS3APIMockRecorder) GetBucketMetricsConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketMetricsConfigurationRequest(arg0 any) *gomock.Call

GetBucketMetricsConfigurationRequest indicates an expected call of GetBucketMetricsConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketMetricsConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketMetricsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketMetricsConfigurationWithContext indicates an expected call of GetBucketMetricsConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketNotification ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketNotification(arg0 any) *gomock.Call

GetBucketNotification indicates an expected call of GetBucketNotification.

func (*MockS3APIMockRecorder) GetBucketNotificationConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketNotificationConfiguration(arg0 any) *gomock.Call

GetBucketNotificationConfiguration indicates an expected call of GetBucketNotificationConfiguration.

func (*MockS3APIMockRecorder) GetBucketNotificationConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketNotificationConfigurationRequest(arg0 any) *gomock.Call

GetBucketNotificationConfigurationRequest indicates an expected call of GetBucketNotificationConfigurationRequest.

func (*MockS3APIMockRecorder) GetBucketNotificationConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketNotificationConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketNotificationConfigurationWithContext indicates an expected call of GetBucketNotificationConfigurationWithContext.

func (*MockS3APIMockRecorder) GetBucketNotificationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketNotificationRequest(arg0 any) *gomock.Call

GetBucketNotificationRequest indicates an expected call of GetBucketNotificationRequest.

func (*MockS3APIMockRecorder) GetBucketNotificationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketNotificationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketNotificationWithContext indicates an expected call of GetBucketNotificationWithContext.

func (*MockS3APIMockRecorder) GetBucketOwnershipControls ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketOwnershipControls(arg0 any) *gomock.Call

GetBucketOwnershipControls indicates an expected call of GetBucketOwnershipControls.

func (*MockS3APIMockRecorder) GetBucketOwnershipControlsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketOwnershipControlsRequest(arg0 any) *gomock.Call

GetBucketOwnershipControlsRequest indicates an expected call of GetBucketOwnershipControlsRequest.

func (*MockS3APIMockRecorder) GetBucketOwnershipControlsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketOwnershipControlsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketOwnershipControlsWithContext indicates an expected call of GetBucketOwnershipControlsWithContext.

func (*MockS3APIMockRecorder) GetBucketPolicy ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketPolicy(arg0 any) *gomock.Call

GetBucketPolicy indicates an expected call of GetBucketPolicy.

func (*MockS3APIMockRecorder) GetBucketPolicyRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketPolicyRequest(arg0 any) *gomock.Call

GetBucketPolicyRequest indicates an expected call of GetBucketPolicyRequest.

func (*MockS3APIMockRecorder) GetBucketPolicyStatus ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketPolicyStatus(arg0 any) *gomock.Call

GetBucketPolicyStatus indicates an expected call of GetBucketPolicyStatus.

func (*MockS3APIMockRecorder) GetBucketPolicyStatusRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketPolicyStatusRequest(arg0 any) *gomock.Call

GetBucketPolicyStatusRequest indicates an expected call of GetBucketPolicyStatusRequest.

func (*MockS3APIMockRecorder) GetBucketPolicyStatusWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketPolicyStatusWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketPolicyStatusWithContext indicates an expected call of GetBucketPolicyStatusWithContext.

func (*MockS3APIMockRecorder) GetBucketPolicyWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketPolicyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketPolicyWithContext indicates an expected call of GetBucketPolicyWithContext.

func (*MockS3APIMockRecorder) GetBucketReplication ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketReplication(arg0 any) *gomock.Call

GetBucketReplication indicates an expected call of GetBucketReplication.

func (*MockS3APIMockRecorder) GetBucketReplicationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketReplicationRequest(arg0 any) *gomock.Call

GetBucketReplicationRequest indicates an expected call of GetBucketReplicationRequest.

func (*MockS3APIMockRecorder) GetBucketReplicationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketReplicationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketReplicationWithContext indicates an expected call of GetBucketReplicationWithContext.

func (*MockS3APIMockRecorder) GetBucketRequestPayment ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketRequestPayment(arg0 any) *gomock.Call

GetBucketRequestPayment indicates an expected call of GetBucketRequestPayment.

func (*MockS3APIMockRecorder) GetBucketRequestPaymentRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketRequestPaymentRequest(arg0 any) *gomock.Call

GetBucketRequestPaymentRequest indicates an expected call of GetBucketRequestPaymentRequest.

func (*MockS3APIMockRecorder) GetBucketRequestPaymentWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketRequestPaymentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketRequestPaymentWithContext indicates an expected call of GetBucketRequestPaymentWithContext.

func (*MockS3APIMockRecorder) GetBucketTagging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketTagging(arg0 any) *gomock.Call

GetBucketTagging indicates an expected call of GetBucketTagging.

func (*MockS3APIMockRecorder) GetBucketTaggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketTaggingRequest(arg0 any) *gomock.Call

GetBucketTaggingRequest indicates an expected call of GetBucketTaggingRequest.

func (*MockS3APIMockRecorder) GetBucketTaggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketTaggingWithContext indicates an expected call of GetBucketTaggingWithContext.

func (*MockS3APIMockRecorder) GetBucketVersioning ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketVersioning(arg0 any) *gomock.Call

GetBucketVersioning indicates an expected call of GetBucketVersioning.

func (*MockS3APIMockRecorder) GetBucketVersioningRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketVersioningRequest(arg0 any) *gomock.Call

GetBucketVersioningRequest indicates an expected call of GetBucketVersioningRequest.

func (*MockS3APIMockRecorder) GetBucketVersioningWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketVersioningWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketVersioningWithContext indicates an expected call of GetBucketVersioningWithContext.

func (*MockS3APIMockRecorder) GetBucketWebsite ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketWebsite(arg0 any) *gomock.Call

GetBucketWebsite indicates an expected call of GetBucketWebsite.

func (*MockS3APIMockRecorder) GetBucketWebsiteRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketWebsiteRequest(arg0 any) *gomock.Call

GetBucketWebsiteRequest indicates an expected call of GetBucketWebsiteRequest.

func (*MockS3APIMockRecorder) GetBucketWebsiteWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetBucketWebsiteWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetBucketWebsiteWithContext indicates an expected call of GetBucketWebsiteWithContext.

func (*MockS3APIMockRecorder) GetObject ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObject(arg0 any) *gomock.Call

GetObject indicates an expected call of GetObject.

func (*MockS3APIMockRecorder) GetObjectAcl ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectAcl(arg0 any) *gomock.Call

GetObjectAcl indicates an expected call of GetObjectAcl.

func (*MockS3APIMockRecorder) GetObjectAclRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectAclRequest(arg0 any) *gomock.Call

GetObjectAclRequest indicates an expected call of GetObjectAclRequest.

func (*MockS3APIMockRecorder) GetObjectAclWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectAclWithContext indicates an expected call of GetObjectAclWithContext.

func (*MockS3APIMockRecorder) GetObjectAttributes ¶
added in v1.17.0
func (mr *MockS3APIMockRecorder) GetObjectAttributes(arg0 any) *gomock.Call

GetObjectAttributes indicates an expected call of GetObjectAttributes.

func (*MockS3APIMockRecorder) GetObjectAttributesRequest ¶
added in v1.17.0
func (mr *MockS3APIMockRecorder) GetObjectAttributesRequest(arg0 any) *gomock.Call

GetObjectAttributesRequest indicates an expected call of GetObjectAttributesRequest.

func (*MockS3APIMockRecorder) GetObjectAttributesWithContext ¶
added in v1.17.0
func (mr *MockS3APIMockRecorder) GetObjectAttributesWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectAttributesWithContext indicates an expected call of GetObjectAttributesWithContext.

func (*MockS3APIMockRecorder) GetObjectLegalHold ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectLegalHold(arg0 any) *gomock.Call

GetObjectLegalHold indicates an expected call of GetObjectLegalHold.

func (*MockS3APIMockRecorder) GetObjectLegalHoldRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectLegalHoldRequest(arg0 any) *gomock.Call

GetObjectLegalHoldRequest indicates an expected call of GetObjectLegalHoldRequest.

func (*MockS3APIMockRecorder) GetObjectLegalHoldWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectLegalHoldWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectLegalHoldWithContext indicates an expected call of GetObjectLegalHoldWithContext.

func (*MockS3APIMockRecorder) GetObjectLockConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectLockConfiguration(arg0 any) *gomock.Call

GetObjectLockConfiguration indicates an expected call of GetObjectLockConfiguration.

func (*MockS3APIMockRecorder) GetObjectLockConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectLockConfigurationRequest(arg0 any) *gomock.Call

GetObjectLockConfigurationRequest indicates an expected call of GetObjectLockConfigurationRequest.

func (*MockS3APIMockRecorder) GetObjectLockConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectLockConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectLockConfigurationWithContext indicates an expected call of GetObjectLockConfigurationWithContext.

func (*MockS3APIMockRecorder) GetObjectRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectRequest(arg0 any) *gomock.Call

GetObjectRequest indicates an expected call of GetObjectRequest.

func (*MockS3APIMockRecorder) GetObjectRetention ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectRetention(arg0 any) *gomock.Call

GetObjectRetention indicates an expected call of GetObjectRetention.

func (*MockS3APIMockRecorder) GetObjectRetentionRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectRetentionRequest(arg0 any) *gomock.Call

GetObjectRetentionRequest indicates an expected call of GetObjectRetentionRequest.

func (*MockS3APIMockRecorder) GetObjectRetentionWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectRetentionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectRetentionWithContext indicates an expected call of GetObjectRetentionWithContext.

func (*MockS3APIMockRecorder) GetObjectTagging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectTagging(arg0 any) *gomock.Call

GetObjectTagging indicates an expected call of GetObjectTagging.

func (*MockS3APIMockRecorder) GetObjectTaggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectTaggingRequest(arg0 any) *gomock.Call

GetObjectTaggingRequest indicates an expected call of GetObjectTaggingRequest.

func (*MockS3APIMockRecorder) GetObjectTaggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectTaggingWithContext indicates an expected call of GetObjectTaggingWithContext.

func (*MockS3APIMockRecorder) GetObjectTorrent ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectTorrent(arg0 any) *gomock.Call

GetObjectTorrent indicates an expected call of GetObjectTorrent.

func (*MockS3APIMockRecorder) GetObjectTorrentRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectTorrentRequest(arg0 any) *gomock.Call

GetObjectTorrentRequest indicates an expected call of GetObjectTorrentRequest.

func (*MockS3APIMockRecorder) GetObjectTorrentWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectTorrentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectTorrentWithContext indicates an expected call of GetObjectTorrentWithContext.

func (*MockS3APIMockRecorder) GetObjectWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetObjectWithContext indicates an expected call of GetObjectWithContext.

func (*MockS3APIMockRecorder) GetPublicAccessBlock ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetPublicAccessBlock(arg0 any) *gomock.Call

GetPublicAccessBlock indicates an expected call of GetPublicAccessBlock.

func (*MockS3APIMockRecorder) GetPublicAccessBlockRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetPublicAccessBlockRequest(arg0 any) *gomock.Call

GetPublicAccessBlockRequest indicates an expected call of GetPublicAccessBlockRequest.

func (*MockS3APIMockRecorder) GetPublicAccessBlockWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) GetPublicAccessBlockWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

GetPublicAccessBlockWithContext indicates an expected call of GetPublicAccessBlockWithContext.

func (*MockS3APIMockRecorder) HeadBucket ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) HeadBucket(arg0 any) *gomock.Call

HeadBucket indicates an expected call of HeadBucket.

func (*MockS3APIMockRecorder) HeadBucketRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) HeadBucketRequest(arg0 any) *gomock.Call

HeadBucketRequest indicates an expected call of HeadBucketRequest.

func (*MockS3APIMockRecorder) HeadBucketWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) HeadBucketWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

HeadBucketWithContext indicates an expected call of HeadBucketWithContext.

func (*MockS3APIMockRecorder) HeadObject ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) HeadObject(arg0 any) *gomock.Call

HeadObject indicates an expected call of HeadObject.

func (*MockS3APIMockRecorder) HeadObjectRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) HeadObjectRequest(arg0 any) *gomock.Call

HeadObjectRequest indicates an expected call of HeadObjectRequest.

func (*MockS3APIMockRecorder) HeadObjectWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) HeadObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

HeadObjectWithContext indicates an expected call of HeadObjectWithContext.

func (*MockS3APIMockRecorder) ListBucketAnalyticsConfigurations ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketAnalyticsConfigurations(arg0 any) *gomock.Call

ListBucketAnalyticsConfigurations indicates an expected call of ListBucketAnalyticsConfigurations.

func (*MockS3APIMockRecorder) ListBucketAnalyticsConfigurationsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketAnalyticsConfigurationsRequest(arg0 any) *gomock.Call

ListBucketAnalyticsConfigurationsRequest indicates an expected call of ListBucketAnalyticsConfigurationsRequest.

func (*MockS3APIMockRecorder) ListBucketAnalyticsConfigurationsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketAnalyticsConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListBucketAnalyticsConfigurationsWithContext indicates an expected call of ListBucketAnalyticsConfigurationsWithContext.

func (*MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurations ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurations(arg0 any) *gomock.Call

ListBucketIntelligentTieringConfigurations indicates an expected call of ListBucketIntelligentTieringConfigurations.

func (*MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurationsRequest ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurationsRequest(arg0 any) *gomock.Call

ListBucketIntelligentTieringConfigurationsRequest indicates an expected call of ListBucketIntelligentTieringConfigurationsRequest.

func (*MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurationsWithContext ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) ListBucketIntelligentTieringConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListBucketIntelligentTieringConfigurationsWithContext indicates an expected call of ListBucketIntelligentTieringConfigurationsWithContext.

func (*MockS3APIMockRecorder) ListBucketInventoryConfigurations ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketInventoryConfigurations(arg0 any) *gomock.Call

ListBucketInventoryConfigurations indicates an expected call of ListBucketInventoryConfigurations.

func (*MockS3APIMockRecorder) ListBucketInventoryConfigurationsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketInventoryConfigurationsRequest(arg0 any) *gomock.Call

ListBucketInventoryConfigurationsRequest indicates an expected call of ListBucketInventoryConfigurationsRequest.

func (*MockS3APIMockRecorder) ListBucketInventoryConfigurationsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketInventoryConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListBucketInventoryConfigurationsWithContext indicates an expected call of ListBucketInventoryConfigurationsWithContext.

func (*MockS3APIMockRecorder) ListBucketMetricsConfigurations ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketMetricsConfigurations(arg0 any) *gomock.Call

ListBucketMetricsConfigurations indicates an expected call of ListBucketMetricsConfigurations.

func (*MockS3APIMockRecorder) ListBucketMetricsConfigurationsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketMetricsConfigurationsRequest(arg0 any) *gomock.Call

ListBucketMetricsConfigurationsRequest indicates an expected call of ListBucketMetricsConfigurationsRequest.

func (*MockS3APIMockRecorder) ListBucketMetricsConfigurationsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketMetricsConfigurationsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListBucketMetricsConfigurationsWithContext indicates an expected call of ListBucketMetricsConfigurationsWithContext.

func (*MockS3APIMockRecorder) ListBuckets ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBuckets(arg0 any) *gomock.Call

ListBuckets indicates an expected call of ListBuckets.

func (*MockS3APIMockRecorder) ListBucketsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketsRequest(arg0 any) *gomock.Call

ListBucketsRequest indicates an expected call of ListBucketsRequest.

func (*MockS3APIMockRecorder) ListBucketsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListBucketsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListBucketsWithContext indicates an expected call of ListBucketsWithContext.

func (*MockS3APIMockRecorder) ListDirectoryBuckets ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) ListDirectoryBuckets(arg0 any) *gomock.Call

ListDirectoryBuckets indicates an expected call of ListDirectoryBuckets.

func (*MockS3APIMockRecorder) ListDirectoryBucketsPages ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsPages(arg0, arg1 any) *gomock.Call

ListDirectoryBucketsPages indicates an expected call of ListDirectoryBucketsPages.

func (*MockS3APIMockRecorder) ListDirectoryBucketsPagesWithContext ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call

ListDirectoryBucketsPagesWithContext indicates an expected call of ListDirectoryBucketsPagesWithContext.

func (*MockS3APIMockRecorder) ListDirectoryBucketsRequest ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsRequest(arg0 any) *gomock.Call

ListDirectoryBucketsRequest indicates an expected call of ListDirectoryBucketsRequest.

func (*MockS3APIMockRecorder) ListDirectoryBucketsWithContext ¶
added in v1.23.1
func (mr *MockS3APIMockRecorder) ListDirectoryBucketsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListDirectoryBucketsWithContext indicates an expected call of ListDirectoryBucketsWithContext.

func (*MockS3APIMockRecorder) ListMultipartUploads ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListMultipartUploads(arg0 any) *gomock.Call

ListMultipartUploads indicates an expected call of ListMultipartUploads.

func (*MockS3APIMockRecorder) ListMultipartUploadsPages ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListMultipartUploadsPages(arg0, arg1 any) *gomock.Call

ListMultipartUploadsPages indicates an expected call of ListMultipartUploadsPages.

func (*MockS3APIMockRecorder) ListMultipartUploadsPagesWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListMultipartUploadsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call

ListMultipartUploadsPagesWithContext indicates an expected call of ListMultipartUploadsPagesWithContext.

func (*MockS3APIMockRecorder) ListMultipartUploadsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListMultipartUploadsRequest(arg0 any) *gomock.Call

ListMultipartUploadsRequest indicates an expected call of ListMultipartUploadsRequest.

func (*MockS3APIMockRecorder) ListMultipartUploadsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListMultipartUploadsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListMultipartUploadsWithContext indicates an expected call of ListMultipartUploadsWithContext.

func (*MockS3APIMockRecorder) ListObjectVersions ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectVersions(arg0 any) *gomock.Call

ListObjectVersions indicates an expected call of ListObjectVersions.

func (*MockS3APIMockRecorder) ListObjectVersionsPages ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectVersionsPages(arg0, arg1 any) *gomock.Call

ListObjectVersionsPages indicates an expected call of ListObjectVersionsPages.

func (*MockS3APIMockRecorder) ListObjectVersionsPagesWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectVersionsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call

ListObjectVersionsPagesWithContext indicates an expected call of ListObjectVersionsPagesWithContext.

func (*MockS3APIMockRecorder) ListObjectVersionsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectVersionsRequest(arg0 any) *gomock.Call

ListObjectVersionsRequest indicates an expected call of ListObjectVersionsRequest.

func (*MockS3APIMockRecorder) ListObjectVersionsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectVersionsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListObjectVersionsWithContext indicates an expected call of ListObjectVersionsWithContext.

func (*MockS3APIMockRecorder) ListObjects ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjects(arg0 any) *gomock.Call

ListObjects indicates an expected call of ListObjects.

func (*MockS3APIMockRecorder) ListObjectsPages ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsPages(arg0, arg1 any) *gomock.Call

ListObjectsPages indicates an expected call of ListObjectsPages.

func (*MockS3APIMockRecorder) ListObjectsPagesWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call

ListObjectsPagesWithContext indicates an expected call of ListObjectsPagesWithContext.

func (*MockS3APIMockRecorder) ListObjectsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsRequest(arg0 any) *gomock.Call

ListObjectsRequest indicates an expected call of ListObjectsRequest.

func (*MockS3APIMockRecorder) ListObjectsV2 ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsV2(arg0 any) *gomock.Call

ListObjectsV2 indicates an expected call of ListObjectsV2.

func (*MockS3APIMockRecorder) ListObjectsV2Pages ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsV2Pages(arg0, arg1 any) *gomock.Call

ListObjectsV2Pages indicates an expected call of ListObjectsV2Pages.

func (*MockS3APIMockRecorder) ListObjectsV2PagesWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsV2PagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call

ListObjectsV2PagesWithContext indicates an expected call of ListObjectsV2PagesWithContext.

func (*MockS3APIMockRecorder) ListObjectsV2Request ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsV2Request(arg0 any) *gomock.Call

ListObjectsV2Request indicates an expected call of ListObjectsV2Request.

func (*MockS3APIMockRecorder) ListObjectsV2WithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsV2WithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListObjectsV2WithContext indicates an expected call of ListObjectsV2WithContext.

func (*MockS3APIMockRecorder) ListObjectsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListObjectsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListObjectsWithContext indicates an expected call of ListObjectsWithContext.

func (*MockS3APIMockRecorder) ListParts ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListParts(arg0 any) *gomock.Call

ListParts indicates an expected call of ListParts.

func (*MockS3APIMockRecorder) ListPartsPages ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListPartsPages(arg0, arg1 any) *gomock.Call

ListPartsPages indicates an expected call of ListPartsPages.

func (*MockS3APIMockRecorder) ListPartsPagesWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListPartsPagesWithContext(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call

ListPartsPagesWithContext indicates an expected call of ListPartsPagesWithContext.

func (*MockS3APIMockRecorder) ListPartsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListPartsRequest(arg0 any) *gomock.Call

ListPartsRequest indicates an expected call of ListPartsRequest.

func (*MockS3APIMockRecorder) ListPartsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) ListPartsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

ListPartsWithContext indicates an expected call of ListPartsWithContext.

func (*MockS3APIMockRecorder) PutBucketAccelerateConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAccelerateConfiguration(arg0 any) *gomock.Call

PutBucketAccelerateConfiguration indicates an expected call of PutBucketAccelerateConfiguration.

func (*MockS3APIMockRecorder) PutBucketAccelerateConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAccelerateConfigurationRequest(arg0 any) *gomock.Call

PutBucketAccelerateConfigurationRequest indicates an expected call of PutBucketAccelerateConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketAccelerateConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAccelerateConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketAccelerateConfigurationWithContext indicates an expected call of PutBucketAccelerateConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketAcl ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAcl(arg0 any) *gomock.Call

PutBucketAcl indicates an expected call of PutBucketAcl.

func (*MockS3APIMockRecorder) PutBucketAclRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAclRequest(arg0 any) *gomock.Call

PutBucketAclRequest indicates an expected call of PutBucketAclRequest.

func (*MockS3APIMockRecorder) PutBucketAclWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketAclWithContext indicates an expected call of PutBucketAclWithContext.

func (*MockS3APIMockRecorder) PutBucketAnalyticsConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAnalyticsConfiguration(arg0 any) *gomock.Call

PutBucketAnalyticsConfiguration indicates an expected call of PutBucketAnalyticsConfiguration.

func (*MockS3APIMockRecorder) PutBucketAnalyticsConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAnalyticsConfigurationRequest(arg0 any) *gomock.Call

PutBucketAnalyticsConfigurationRequest indicates an expected call of PutBucketAnalyticsConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketAnalyticsConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketAnalyticsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketAnalyticsConfigurationWithContext indicates an expected call of PutBucketAnalyticsConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketCors ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketCors(arg0 any) *gomock.Call

PutBucketCors indicates an expected call of PutBucketCors.

func (*MockS3APIMockRecorder) PutBucketCorsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketCorsRequest(arg0 any) *gomock.Call

PutBucketCorsRequest indicates an expected call of PutBucketCorsRequest.

func (*MockS3APIMockRecorder) PutBucketCorsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketCorsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketCorsWithContext indicates an expected call of PutBucketCorsWithContext.

func (*MockS3APIMockRecorder) PutBucketEncryption ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketEncryption(arg0 any) *gomock.Call

PutBucketEncryption indicates an expected call of PutBucketEncryption.

func (*MockS3APIMockRecorder) PutBucketEncryptionRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketEncryptionRequest(arg0 any) *gomock.Call

PutBucketEncryptionRequest indicates an expected call of PutBucketEncryptionRequest.

func (*MockS3APIMockRecorder) PutBucketEncryptionWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketEncryptionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketEncryptionWithContext indicates an expected call of PutBucketEncryptionWithContext.

func (*MockS3APIMockRecorder) PutBucketIntelligentTieringConfiguration ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) PutBucketIntelligentTieringConfiguration(arg0 any) *gomock.Call

PutBucketIntelligentTieringConfiguration indicates an expected call of PutBucketIntelligentTieringConfiguration.

func (*MockS3APIMockRecorder) PutBucketIntelligentTieringConfigurationRequest ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) PutBucketIntelligentTieringConfigurationRequest(arg0 any) *gomock.Call

PutBucketIntelligentTieringConfigurationRequest indicates an expected call of PutBucketIntelligentTieringConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketIntelligentTieringConfigurationWithContext ¶
added in v1.5.7
func (mr *MockS3APIMockRecorder) PutBucketIntelligentTieringConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketIntelligentTieringConfigurationWithContext indicates an expected call of PutBucketIntelligentTieringConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketInventoryConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketInventoryConfiguration(arg0 any) *gomock.Call

PutBucketInventoryConfiguration indicates an expected call of PutBucketInventoryConfiguration.

func (*MockS3APIMockRecorder) PutBucketInventoryConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketInventoryConfigurationRequest(arg0 any) *gomock.Call

PutBucketInventoryConfigurationRequest indicates an expected call of PutBucketInventoryConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketInventoryConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketInventoryConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketInventoryConfigurationWithContext indicates an expected call of PutBucketInventoryConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketLifecycle ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLifecycle(arg0 any) *gomock.Call

PutBucketLifecycle indicates an expected call of PutBucketLifecycle.

func (*MockS3APIMockRecorder) PutBucketLifecycleConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLifecycleConfiguration(arg0 any) *gomock.Call

PutBucketLifecycleConfiguration indicates an expected call of PutBucketLifecycleConfiguration.

func (*MockS3APIMockRecorder) PutBucketLifecycleConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLifecycleConfigurationRequest(arg0 any) *gomock.Call

PutBucketLifecycleConfigurationRequest indicates an expected call of PutBucketLifecycleConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketLifecycleConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLifecycleConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketLifecycleConfigurationWithContext indicates an expected call of PutBucketLifecycleConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketLifecycleRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLifecycleRequest(arg0 any) *gomock.Call

PutBucketLifecycleRequest indicates an expected call of PutBucketLifecycleRequest.

func (*MockS3APIMockRecorder) PutBucketLifecycleWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLifecycleWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketLifecycleWithContext indicates an expected call of PutBucketLifecycleWithContext.

func (*MockS3APIMockRecorder) PutBucketLogging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLogging(arg0 any) *gomock.Call

PutBucketLogging indicates an expected call of PutBucketLogging.

func (*MockS3APIMockRecorder) PutBucketLoggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLoggingRequest(arg0 any) *gomock.Call

PutBucketLoggingRequest indicates an expected call of PutBucketLoggingRequest.

func (*MockS3APIMockRecorder) PutBucketLoggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketLoggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketLoggingWithContext indicates an expected call of PutBucketLoggingWithContext.

func (*MockS3APIMockRecorder) PutBucketMetricsConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketMetricsConfiguration(arg0 any) *gomock.Call

PutBucketMetricsConfiguration indicates an expected call of PutBucketMetricsConfiguration.

func (*MockS3APIMockRecorder) PutBucketMetricsConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketMetricsConfigurationRequest(arg0 any) *gomock.Call

PutBucketMetricsConfigurationRequest indicates an expected call of PutBucketMetricsConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketMetricsConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketMetricsConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketMetricsConfigurationWithContext indicates an expected call of PutBucketMetricsConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketNotification ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketNotification(arg0 any) *gomock.Call

PutBucketNotification indicates an expected call of PutBucketNotification.

func (*MockS3APIMockRecorder) PutBucketNotificationConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketNotificationConfiguration(arg0 any) *gomock.Call

PutBucketNotificationConfiguration indicates an expected call of PutBucketNotificationConfiguration.

func (*MockS3APIMockRecorder) PutBucketNotificationConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketNotificationConfigurationRequest(arg0 any) *gomock.Call

PutBucketNotificationConfigurationRequest indicates an expected call of PutBucketNotificationConfigurationRequest.

func (*MockS3APIMockRecorder) PutBucketNotificationConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketNotificationConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketNotificationConfigurationWithContext indicates an expected call of PutBucketNotificationConfigurationWithContext.

func (*MockS3APIMockRecorder) PutBucketNotificationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketNotificationRequest(arg0 any) *gomock.Call

PutBucketNotificationRequest indicates an expected call of PutBucketNotificationRequest.

func (*MockS3APIMockRecorder) PutBucketNotificationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketNotificationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketNotificationWithContext indicates an expected call of PutBucketNotificationWithContext.

func (*MockS3APIMockRecorder) PutBucketOwnershipControls ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketOwnershipControls(arg0 any) *gomock.Call

PutBucketOwnershipControls indicates an expected call of PutBucketOwnershipControls.

func (*MockS3APIMockRecorder) PutBucketOwnershipControlsRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketOwnershipControlsRequest(arg0 any) *gomock.Call

PutBucketOwnershipControlsRequest indicates an expected call of PutBucketOwnershipControlsRequest.

func (*MockS3APIMockRecorder) PutBucketOwnershipControlsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketOwnershipControlsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketOwnershipControlsWithContext indicates an expected call of PutBucketOwnershipControlsWithContext.

func (*MockS3APIMockRecorder) PutBucketPolicy ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketPolicy(arg0 any) *gomock.Call

PutBucketPolicy indicates an expected call of PutBucketPolicy.

func (*MockS3APIMockRecorder) PutBucketPolicyRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketPolicyRequest(arg0 any) *gomock.Call

PutBucketPolicyRequest indicates an expected call of PutBucketPolicyRequest.

func (*MockS3APIMockRecorder) PutBucketPolicyWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketPolicyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketPolicyWithContext indicates an expected call of PutBucketPolicyWithContext.

func (*MockS3APIMockRecorder) PutBucketReplication ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketReplication(arg0 any) *gomock.Call

PutBucketReplication indicates an expected call of PutBucketReplication.

func (*MockS3APIMockRecorder) PutBucketReplicationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketReplicationRequest(arg0 any) *gomock.Call

PutBucketReplicationRequest indicates an expected call of PutBucketReplicationRequest.

func (*MockS3APIMockRecorder) PutBucketReplicationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketReplicationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketReplicationWithContext indicates an expected call of PutBucketReplicationWithContext.

func (*MockS3APIMockRecorder) PutBucketRequestPayment ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketRequestPayment(arg0 any) *gomock.Call

PutBucketRequestPayment indicates an expected call of PutBucketRequestPayment.

func (*MockS3APIMockRecorder) PutBucketRequestPaymentRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketRequestPaymentRequest(arg0 any) *gomock.Call

PutBucketRequestPaymentRequest indicates an expected call of PutBucketRequestPaymentRequest.

func (*MockS3APIMockRecorder) PutBucketRequestPaymentWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketRequestPaymentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketRequestPaymentWithContext indicates an expected call of PutBucketRequestPaymentWithContext.

func (*MockS3APIMockRecorder) PutBucketTagging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketTagging(arg0 any) *gomock.Call

PutBucketTagging indicates an expected call of PutBucketTagging.

func (*MockS3APIMockRecorder) PutBucketTaggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketTaggingRequest(arg0 any) *gomock.Call

PutBucketTaggingRequest indicates an expected call of PutBucketTaggingRequest.

func (*MockS3APIMockRecorder) PutBucketTaggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketTaggingWithContext indicates an expected call of PutBucketTaggingWithContext.

func (*MockS3APIMockRecorder) PutBucketVersioning ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketVersioning(arg0 any) *gomock.Call

PutBucketVersioning indicates an expected call of PutBucketVersioning.

func (*MockS3APIMockRecorder) PutBucketVersioningRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketVersioningRequest(arg0 any) *gomock.Call

PutBucketVersioningRequest indicates an expected call of PutBucketVersioningRequest.

func (*MockS3APIMockRecorder) PutBucketVersioningWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketVersioningWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketVersioningWithContext indicates an expected call of PutBucketVersioningWithContext.

func (*MockS3APIMockRecorder) PutBucketWebsite ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketWebsite(arg0 any) *gomock.Call

PutBucketWebsite indicates an expected call of PutBucketWebsite.

func (*MockS3APIMockRecorder) PutBucketWebsiteRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketWebsiteRequest(arg0 any) *gomock.Call

PutBucketWebsiteRequest indicates an expected call of PutBucketWebsiteRequest.

func (*MockS3APIMockRecorder) PutBucketWebsiteWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutBucketWebsiteWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutBucketWebsiteWithContext indicates an expected call of PutBucketWebsiteWithContext.

func (*MockS3APIMockRecorder) PutObject ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObject(arg0 any) *gomock.Call

PutObject indicates an expected call of PutObject.

func (*MockS3APIMockRecorder) PutObjectAcl ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectAcl(arg0 any) *gomock.Call

PutObjectAcl indicates an expected call of PutObjectAcl.

func (*MockS3APIMockRecorder) PutObjectAclRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectAclRequest(arg0 any) *gomock.Call

PutObjectAclRequest indicates an expected call of PutObjectAclRequest.

func (*MockS3APIMockRecorder) PutObjectAclWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectAclWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutObjectAclWithContext indicates an expected call of PutObjectAclWithContext.

func (*MockS3APIMockRecorder) PutObjectLegalHold ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectLegalHold(arg0 any) *gomock.Call

PutObjectLegalHold indicates an expected call of PutObjectLegalHold.

func (*MockS3APIMockRecorder) PutObjectLegalHoldRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectLegalHoldRequest(arg0 any) *gomock.Call

PutObjectLegalHoldRequest indicates an expected call of PutObjectLegalHoldRequest.

func (*MockS3APIMockRecorder) PutObjectLegalHoldWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectLegalHoldWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutObjectLegalHoldWithContext indicates an expected call of PutObjectLegalHoldWithContext.

func (*MockS3APIMockRecorder) PutObjectLockConfiguration ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectLockConfiguration(arg0 any) *gomock.Call

PutObjectLockConfiguration indicates an expected call of PutObjectLockConfiguration.

func (*MockS3APIMockRecorder) PutObjectLockConfigurationRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectLockConfigurationRequest(arg0 any) *gomock.Call

PutObjectLockConfigurationRequest indicates an expected call of PutObjectLockConfigurationRequest.

func (*MockS3APIMockRecorder) PutObjectLockConfigurationWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectLockConfigurationWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutObjectLockConfigurationWithContext indicates an expected call of PutObjectLockConfigurationWithContext.

func (*MockS3APIMockRecorder) PutObjectRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectRequest(arg0 any) *gomock.Call

PutObjectRequest indicates an expected call of PutObjectRequest.

func (*MockS3APIMockRecorder) PutObjectRetention ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectRetention(arg0 any) *gomock.Call

PutObjectRetention indicates an expected call of PutObjectRetention.

func (*MockS3APIMockRecorder) PutObjectRetentionRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectRetentionRequest(arg0 any) *gomock.Call

PutObjectRetentionRequest indicates an expected call of PutObjectRetentionRequest.

func (*MockS3APIMockRecorder) PutObjectRetentionWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectRetentionWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutObjectRetentionWithContext indicates an expected call of PutObjectRetentionWithContext.

func (*MockS3APIMockRecorder) PutObjectTagging ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectTagging(arg0 any) *gomock.Call

PutObjectTagging indicates an expected call of PutObjectTagging.

func (*MockS3APIMockRecorder) PutObjectTaggingRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectTaggingRequest(arg0 any) *gomock.Call

PutObjectTaggingRequest indicates an expected call of PutObjectTaggingRequest.

func (*MockS3APIMockRecorder) PutObjectTaggingWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectTaggingWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutObjectTaggingWithContext indicates an expected call of PutObjectTaggingWithContext.

func (*MockS3APIMockRecorder) PutObjectWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutObjectWithContext indicates an expected call of PutObjectWithContext.

func (*MockS3APIMockRecorder) PutPublicAccessBlock ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutPublicAccessBlock(arg0 any) *gomock.Call

PutPublicAccessBlock indicates an expected call of PutPublicAccessBlock.

func (*MockS3APIMockRecorder) PutPublicAccessBlockRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutPublicAccessBlockRequest(arg0 any) *gomock.Call

PutPublicAccessBlockRequest indicates an expected call of PutPublicAccessBlockRequest.

func (*MockS3APIMockRecorder) PutPublicAccessBlockWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) PutPublicAccessBlockWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

PutPublicAccessBlockWithContext indicates an expected call of PutPublicAccessBlockWithContext.

func (*MockS3APIMockRecorder) RestoreObject ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) RestoreObject(arg0 any) *gomock.Call

RestoreObject indicates an expected call of RestoreObject.

func (*MockS3APIMockRecorder) RestoreObjectRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) RestoreObjectRequest(arg0 any) *gomock.Call

RestoreObjectRequest indicates an expected call of RestoreObjectRequest.

func (*MockS3APIMockRecorder) RestoreObjectWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) RestoreObjectWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

RestoreObjectWithContext indicates an expected call of RestoreObjectWithContext.

func (*MockS3APIMockRecorder) SelectObjectContent ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) SelectObjectContent(arg0 any) *gomock.Call

SelectObjectContent indicates an expected call of SelectObjectContent.

func (*MockS3APIMockRecorder) SelectObjectContentRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) SelectObjectContentRequest(arg0 any) *gomock.Call

SelectObjectContentRequest indicates an expected call of SelectObjectContentRequest.

func (*MockS3APIMockRecorder) SelectObjectContentWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) SelectObjectContentWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

SelectObjectContentWithContext indicates an expected call of SelectObjectContentWithContext.

func (*MockS3APIMockRecorder) UploadPart ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) UploadPart(arg0 any) *gomock.Call

UploadPart indicates an expected call of UploadPart.

func (*MockS3APIMockRecorder) UploadPartCopy ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) UploadPartCopy(arg0 any) *gomock.Call

UploadPartCopy indicates an expected call of UploadPartCopy.

func (*MockS3APIMockRecorder) UploadPartCopyRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) UploadPartCopyRequest(arg0 any) *gomock.Call

UploadPartCopyRequest indicates an expected call of UploadPartCopyRequest.

func (*MockS3APIMockRecorder) UploadPartCopyWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) UploadPartCopyWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

UploadPartCopyWithContext indicates an expected call of UploadPartCopyWithContext.

func (*MockS3APIMockRecorder) UploadPartRequest ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) UploadPartRequest(arg0 any) *gomock.Call

UploadPartRequest indicates an expected call of UploadPartRequest.

func (*MockS3APIMockRecorder) UploadPartWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) UploadPartWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

UploadPartWithContext indicates an expected call of UploadPartWithContext.

func (*MockS3APIMockRecorder) WaitUntilBucketExists ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilBucketExists(arg0 any) *gomock.Call

WaitUntilBucketExists indicates an expected call of WaitUntilBucketExists.

func (*MockS3APIMockRecorder) WaitUntilBucketExistsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilBucketExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

WaitUntilBucketExistsWithContext indicates an expected call of WaitUntilBucketExistsWithContext.

func (*MockS3APIMockRecorder) WaitUntilBucketNotExists ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilBucketNotExists(arg0 any) *gomock.Call

WaitUntilBucketNotExists indicates an expected call of WaitUntilBucketNotExists.

func (*MockS3APIMockRecorder) WaitUntilBucketNotExistsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilBucketNotExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

WaitUntilBucketNotExistsWithContext indicates an expected call of WaitUntilBucketNotExistsWithContext.

func (*MockS3APIMockRecorder) WaitUntilObjectExists ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilObjectExists(arg0 any) *gomock.Call

WaitUntilObjectExists indicates an expected call of WaitUntilObjectExists.

func (*MockS3APIMockRecorder) WaitUntilObjectExistsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilObjectExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

WaitUntilObjectExistsWithContext indicates an expected call of WaitUntilObjectExistsWithContext.

func (*MockS3APIMockRecorder) WaitUntilObjectNotExists ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilObjectNotExists(arg0 any) *gomock.Call

WaitUntilObjectNotExists indicates an expected call of WaitUntilObjectNotExists.

func (*MockS3APIMockRecorder) WaitUntilObjectNotExistsWithContext ¶
added in v1.3.0
func (mr *MockS3APIMockRecorder) WaitUntilObjectNotExistsWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

WaitUntilObjectNotExistsWithContext indicates an expected call of WaitUntilObjectNotExistsWithContext.

func (*MockS3APIMockRecorder) WriteGetObjectResponse ¶
added in v1.10.0
func (mr *MockS3APIMockRecorder) WriteGetObjectResponse(arg0 any) *gomock.Call

WriteGetObjectResponse indicates an expected call of WriteGetObjectResponse.

func (*MockS3APIMockRecorder) WriteGetObjectResponseRequest ¶
added in v1.10.0
func (mr *MockS3APIMockRecorder) WriteGetObjectResponseRequest(arg0 any) *gomock.Call

WriteGetObjectResponseRequest indicates an expected call of WriteGetObjectResponseRequest.

func (*MockS3APIMockRecorder) WriteGetObjectResponseWithContext ¶
added in v1.10.0
func (mr *MockS3APIMockRecorder) WriteGetObjectResponseWithContext(arg0, arg1 any, arg2 ...any) *gomock.Call

WriteGetObjectResponseWithContext indicates an expected call of WriteGetObjectResponseWithContext.

 Source Files ¶
View all Source files
generate.go
s3api.go
Why Go
Use Cases
Case Studies
Get Started
Playground
Tour
Stack Overflow
Help
Packages
Standard Library
Sub-repositories
About Go Packages
About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct
Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly
Copyright
Terms of Service
Privacy Policy
Report an Issue

Theme Toggle

Shortcuts Modal

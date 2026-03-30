# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector

Title: connector package - go.temporal.io/server/common/archiver/gcloud/connector - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector

Markdown Content:
Package connector is a generated GoMock package.

Package connector is a generated GoMock package.

*   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#pkg-variables)
*   [type BucketHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#BucketHandleWrapper)
*   [type Client](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#Client)
*       *   [func NewClient(ctx context.Context, config *config.GstorageArchiver) (Client, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewClient)
    *   [func NewClientWithParams(clientD GcloudStorageClient) (Client, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewClientWithParams)

*   [type GcloudStorageClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#GcloudStorageClient)
*   [type MockBucketHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper)
*       *   [func NewMockBucketHandleWrapper(ctrl *gomock.Controller) *MockBucketHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockBucketHandleWrapper)

*       *   [func (m *MockBucketHandleWrapper) Attrs(ctx context.Context) (*storage.BucketAttrs, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.Attrs)
    *   [func (m *MockBucketHandleWrapper) EXPECT() *MockBucketHandleWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.EXPECT)
    *   [func (m *MockBucketHandleWrapper) Object(name string) ObjectHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.Object)
    *   [func (m *MockBucketHandleWrapper) Objects(ctx context.Context, q *storage.Query) ObjectIteratorWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.Objects)

*   [type MockBucketHandleWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder)
*       *   [func (mr *MockBucketHandleWrapperMockRecorder) Attrs(ctx any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder.Attrs)
    *   [func (mr *MockBucketHandleWrapperMockRecorder) Object(name any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder.Object)
    *   [func (mr *MockBucketHandleWrapperMockRecorder) Objects(ctx, q any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder.Objects)

*   [type MockClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient)
*       *   [func NewMockClient(ctrl *gomock.Controller) *MockClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockClient)

*       *   [func (m *MockClient) EXPECT() *MockClientMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient.EXPECT)
    *   [func (m *MockClient) Exist(ctx context.Context, URI archiver.URI, fileName string) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient.Exist)
    *   [func (m *MockClient) Get(ctx context.Context, URI archiver.URI, file string) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient.Get)
    *   [func (m *MockClient) Query(ctx context.Context, URI archiver.URI, fileNamePrefix string) ([]string, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient.Query)
    *   [func (m *MockClient) QueryWithFilters(ctx context.Context, URI archiver.URI, fileNamePrefix string, ...) ([]string, bool, int, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient.QueryWithFilters)
    *   [func (m *MockClient) Upload(ctx context.Context, URI archiver.URI, fileName string, file []byte) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient.Upload)

*   [type MockClientMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder)
*       *   [func (mr *MockClientMockRecorder) Exist(ctx, URI, fileName any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder.Exist)
    *   [func (mr *MockClientMockRecorder) Get(ctx, URI, file any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder.Get)
    *   [func (mr *MockClientMockRecorder) Query(ctx, URI, fileNamePrefix any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder.Query)
    *   [func (mr *MockClientMockRecorder) QueryWithFilters(ctx, URI, fileNamePrefix, pageSize, offset, filters any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder.QueryWithFilters)
    *   [func (mr *MockClientMockRecorder) Upload(ctx, URI, fileName, file any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder.Upload)

*   [type MockGcloudStorageClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockGcloudStorageClient)
*       *   [func NewMockGcloudStorageClient(ctrl *gomock.Controller) *MockGcloudStorageClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockGcloudStorageClient)

*       *   [func (m *MockGcloudStorageClient) Bucket(URI string) BucketHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockGcloudStorageClient.Bucket)
    *   [func (m *MockGcloudStorageClient) EXPECT() *MockGcloudStorageClientMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockGcloudStorageClient.EXPECT)

*   [type MockGcloudStorageClientMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockGcloudStorageClientMockRecorder)
*       *   [func (mr *MockGcloudStorageClientMockRecorder) Bucket(URI any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockGcloudStorageClientMockRecorder.Bucket)

*   [type MockObjectHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper)
*       *   [func NewMockObjectHandleWrapper(ctrl *gomock.Controller) *MockObjectHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockObjectHandleWrapper)

*       *   [func (m *MockObjectHandleWrapper) Attrs(ctx context.Context) (*storage.ObjectAttrs, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.Attrs)
    *   [func (m *MockObjectHandleWrapper) EXPECT() *MockObjectHandleWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.EXPECT)
    *   [func (m *MockObjectHandleWrapper) NewReader(ctx context.Context) (ReaderWrapper, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.NewReader)
    *   [func (m *MockObjectHandleWrapper) NewWriter(ctx context.Context) WriterWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.NewWriter)

*   [type MockObjectHandleWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder)
*       *   [func (mr *MockObjectHandleWrapperMockRecorder) Attrs(ctx any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder.Attrs)
    *   [func (mr *MockObjectHandleWrapperMockRecorder) NewReader(ctx any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder.NewReader)
    *   [func (mr *MockObjectHandleWrapperMockRecorder) NewWriter(ctx any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder.NewWriter)

*   [type MockObjectIteratorWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectIteratorWrapper)
*       *   [func NewMockObjectIteratorWrapper(ctrl *gomock.Controller) *MockObjectIteratorWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockObjectIteratorWrapper)

*       *   [func (m *MockObjectIteratorWrapper) EXPECT() *MockObjectIteratorWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectIteratorWrapper.EXPECT)
    *   [func (m *MockObjectIteratorWrapper) Next() (*storage.ObjectAttrs, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectIteratorWrapper.Next)

*   [type MockObjectIteratorWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectIteratorWrapperMockRecorder)
*       *   [func (mr *MockObjectIteratorWrapperMockRecorder) Next() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectIteratorWrapperMockRecorder.Next)

*   [type MockReaderWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapper)
*       *   [func NewMockReaderWrapper(ctrl *gomock.Controller) *MockReaderWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockReaderWrapper)

*       *   [func (m *MockReaderWrapper) Close() error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapper.Close)
    *   [func (m *MockReaderWrapper) EXPECT() *MockReaderWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapper.EXPECT)
    *   [func (m *MockReaderWrapper) Read(p []byte) (int, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapper.Read)

*   [type MockReaderWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapperMockRecorder)
*       *   [func (mr *MockReaderWrapperMockRecorder) Close() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapperMockRecorder.Close)
    *   [func (mr *MockReaderWrapperMockRecorder) Read(p any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockReaderWrapperMockRecorder.Read)

*   [type MockWriterWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapper)
*       *   [func NewMockWriterWrapper(ctrl *gomock.Controller) *MockWriterWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#NewMockWriterWrapper)

*       *   [func (m *MockWriterWrapper) Close() error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapper.Close)
    *   [func (m *MockWriterWrapper) CloseWithError(err error) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapper.CloseWithError)
    *   [func (m *MockWriterWrapper) EXPECT() *MockWriterWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapper.EXPECT)
    *   [func (m *MockWriterWrapper) Write(p []byte) (int, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapper.Write)

*   [type MockWriterWrapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapperMockRecorder)
*       *   [func (mr *MockWriterWrapperMockRecorder) Close() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapperMockRecorder.Close)
    *   [func (mr *MockWriterWrapperMockRecorder) CloseWithError(err any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapperMockRecorder.CloseWithError)
    *   [func (mr *MockWriterWrapperMockRecorder) Write(p any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockWriterWrapperMockRecorder.Write)

*   [type ObjectHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#ObjectHandleWrapper)
*   [type ObjectIteratorWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#ObjectIteratorWrapper)
*   [type Precondition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#Precondition)
*   [type ReaderWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#ReaderWrapper)
*   [type WriterWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#WriterWrapper)

This section is empty.

This section is empty.

#### type [BucketHandleWrapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate.go#L27)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#BucketHandleWrapper "Go to BucketHandleWrapper")

BucketHandleWrapper is an interface that expose some methods from gcloud storage bucket

type Client interface {
 Upload(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), fileName [string](https://pkg.go.dev/builtin#string), file [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error) Get(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), file [string](https://pkg.go.dev/builtin#string)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))  Query(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), fileNamePrefix [string](https://pkg.go.dev/builtin#string)) ([][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))  QueryWithFilters(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), fileNamePrefix [string](https://pkg.go.dev/builtin#string), pageSize, offset [int](https://pkg.go.dev/builtin#int), filters [][Precondition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#Precondition)) ([][string](https://pkg.go.dev/builtin#string), [bool](https://pkg.go.dev/builtin#bool), [int](https://pkg.go.dev/builtin#int), [error](https://pkg.go.dev/builtin#error))  Exist(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), fileName [string](https://pkg.go.dev/builtin#string)) ([bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error)) }

Client is a wrapper around Google cloud storages client library.

NewClient return a Temporal gcloudstorage.Client based on default google service account creadentials (ScopeFullControl required). Bucket must be created by Iaas scripts, in other words, this library doesn't create the required Bucket. Optionaly you can set your credential path throught "GOOGLE_APPLICATION_CREDENTIALS" environment variable or through temporal config file. You can find more info about "Google Setting Up Authentication for Server to Server Production Applications" under the following link [https://cloud.google.com/docs/authentication/production](https://cloud.google.com/docs/authentication/production)

func NewClientWithParams(clientD [GcloudStorageClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#GcloudStorageClient)) ([Client](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#Client), [error](https://pkg.go.dev/builtin#error))

NewClientWithParams return a gcloudstorage.Client based on input parameters

type GcloudStorageClient interface {
 Bucket(URI [string](https://pkg.go.dev/builtin#string)) [BucketHandleWrapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#BucketHandleWrapper)}

GcloudStorageClient is an interface that expose some methods from gcloud storage client

#### type [MockBucketHandleWrapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L59)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper "Go to MockBucketHandleWrapper")added in v1.5.7

type MockBucketHandleWrapper struct {
	
}

MockBucketHandleWrapper is a mock of BucketHandleWrapper interface.

#### func (*MockBucketHandleWrapper) [Attrs](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L83)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.Attrs "Go to MockBucketHandleWrapper.Attrs")added in v1.5.7

Attrs mocks base method.

#### func (*MockBucketHandleWrapper) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L78)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.EXPECT "Go to MockBucketHandleWrapper.EXPECT")added in v1.5.7

EXPECT returns an object that allows the caller to indicate expected use.

#### func (*MockBucketHandleWrapper) [Object](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L98)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.Object "Go to MockBucketHandleWrapper.Object")added in v1.5.7

Object mocks base method.

#### func (*MockBucketHandleWrapper) [Objects](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L112)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapper.Objects "Go to MockBucketHandleWrapper.Objects")added in v1.5.7

Objects mocks base method.

#### type [MockBucketHandleWrapperMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L66)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder "Go to MockBucketHandleWrapperMockRecorder")added in v1.5.7

type MockBucketHandleWrapperMockRecorder struct {
	
}

MockBucketHandleWrapperMockRecorder is the mock recorder for MockBucketHandleWrapper.

#### func (*MockBucketHandleWrapperMockRecorder) [Attrs](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L92)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder.Attrs "Go to MockBucketHandleWrapperMockRecorder.Attrs")added in v1.5.7

Attrs indicates an expected call of Attrs.

#### func (*MockBucketHandleWrapperMockRecorder) [Object](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L106)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder.Object "Go to MockBucketHandleWrapperMockRecorder.Object")added in v1.5.7

Object indicates an expected call of Object.

#### func (*MockBucketHandleWrapperMockRecorder) [Objects](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L120)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockBucketHandleWrapperMockRecorder.Objects "Go to MockBucketHandleWrapperMockRecorder.Objects")added in v1.5.7

Objects indicates an expected call of Objects.

type MockClient struct {
	
}

MockClient is a mock of Client interface.

NewMockClient creates a new mock instance.

func (m *[MockClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClient)) EXPECT() *[MockClientMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

Exist mocks base method.

Get mocks base method.

Query mocks base method.

QueryWithFilters mocks base method.

Upload mocks base method.

type MockClientMockRecorder struct {
	
}

MockClientMockRecorder is the mock recorder for MockClient.

Exist indicates an expected call of Exist.

Get indicates an expected call of Get.

Query indicates an expected call of Query.

func (mr *[MockClientMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockClientMockRecorder)) QueryWithFilters(ctx, URI, fileNamePrefix, pageSize, offset, filters [any](https://pkg.go.dev/builtin#any)) *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

QueryWithFilters indicates an expected call of QueryWithFilters.

Upload indicates an expected call of Upload.

type MockGcloudStorageClient struct {
	
}

MockGcloudStorageClient is a mock of GcloudStorageClient interface.

NewMockGcloudStorageClient creates a new mock instance.

Bucket mocks base method.

EXPECT returns an object that allows the caller to indicate expected use.

type MockGcloudStorageClientMockRecorder struct {
	
}

MockGcloudStorageClientMockRecorder is the mock recorder for MockGcloudStorageClient.

Bucket indicates an expected call of Bucket.

#### type [MockObjectHandleWrapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L126)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper "Go to MockObjectHandleWrapper")added in v1.5.7

type MockObjectHandleWrapper struct {
	
}

MockObjectHandleWrapper is a mock of ObjectHandleWrapper interface.

#### func (*MockObjectHandleWrapper) [Attrs](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L150)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.Attrs "Go to MockObjectHandleWrapper.Attrs")added in v1.5.7

Attrs mocks base method.

#### func (*MockObjectHandleWrapper) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L145)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.EXPECT "Go to MockObjectHandleWrapper.EXPECT")added in v1.5.7

EXPECT returns an object that allows the caller to indicate expected use.

#### func (*MockObjectHandleWrapper) [NewReader](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L165)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.NewReader "Go to MockObjectHandleWrapper.NewReader")added in v1.5.7

NewReader mocks base method.

#### func (*MockObjectHandleWrapper) [NewWriter](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L180)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapper.NewWriter "Go to MockObjectHandleWrapper.NewWriter")added in v1.5.7

NewWriter mocks base method.

#### type [MockObjectHandleWrapperMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L133)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder "Go to MockObjectHandleWrapperMockRecorder")added in v1.5.7

type MockObjectHandleWrapperMockRecorder struct {
	
}

MockObjectHandleWrapperMockRecorder is the mock recorder for MockObjectHandleWrapper.

#### func (*MockObjectHandleWrapperMockRecorder) [Attrs](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L159)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder.Attrs "Go to MockObjectHandleWrapperMockRecorder.Attrs")added in v1.5.7

Attrs indicates an expected call of Attrs.

#### func (*MockObjectHandleWrapperMockRecorder) [NewReader](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L174)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder.NewReader "Go to MockObjectHandleWrapperMockRecorder.NewReader")added in v1.5.7

NewReader indicates an expected call of NewReader.

#### func (*MockObjectHandleWrapperMockRecorder) [NewWriter](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate_mock.go#L188)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#MockObjectHandleWrapperMockRecorder.NewWriter "Go to MockObjectHandleWrapperMockRecorder.NewWriter")added in v1.5.7

NewWriter indicates an expected call of NewWriter.

type MockObjectIteratorWrapper struct {
	
}

MockObjectIteratorWrapper is a mock of ObjectIteratorWrapper interface.

NewMockObjectIteratorWrapper creates a new mock instance.

EXPECT returns an object that allows the caller to indicate expected use.

Next mocks base method.

type MockObjectIteratorWrapperMockRecorder struct {
	
}

MockObjectIteratorWrapperMockRecorder is the mock recorder for MockObjectIteratorWrapper.

Next indicates an expected call of Next.

type MockReaderWrapper struct {
	
}

MockReaderWrapper is a mock of ReaderWrapper interface.

NewMockReaderWrapper creates a new mock instance.

Close mocks base method.

EXPECT returns an object that allows the caller to indicate expected use.

Read mocks base method.

type MockReaderWrapperMockRecorder struct {
	
}

MockReaderWrapperMockRecorder is the mock recorder for MockReaderWrapper.

Close indicates an expected call of Close.

Read indicates an expected call of Read.

type MockWriterWrapper struct {
	
}

MockWriterWrapper is a mock of WriterWrapper interface.

NewMockWriterWrapper creates a new mock instance.

Close mocks base method.

CloseWithError mocks base method.

EXPECT returns an object that allows the caller to indicate expected use.

Write mocks base method.

type MockWriterWrapperMockRecorder struct {
	
}

MockWriterWrapperMockRecorder is the mock recorder for MockWriterWrapper.

Close indicates an expected call of Close.

CloseWithError indicates an expected call of CloseWithError.

Write indicates an expected call of Write.

#### type [ObjectHandleWrapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/gcloud/connector/client_delegate.go#L40)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/gcloud/connector#ObjectHandleWrapper "Go to ObjectHandleWrapper")

ObjectHandleWrapper is an interface that expose some methods from gcloud storage object

ObjectIteratorWrapper is an interface that expose some methods from gcloud storage objectIterator

type Precondition func(subject interface{}) [bool](https://pkg.go.dev/builtin#bool)

Precondition is a function that allow you to filter a query result. If subject match params conditions then return true, else return false.

ReaderWrapper is an interface that expose some methods from gcloud storage reader

WriterWrapper is an interface that expose some methods from gcloud storage writer

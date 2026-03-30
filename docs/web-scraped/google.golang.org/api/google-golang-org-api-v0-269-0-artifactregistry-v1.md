# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/artifactregistry/v1

Title: artifactregistry package - google.golang.org/api/artifactregistry/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/artifactregistry/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
artifactregistry
 
v1
artifactregistry
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 11
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/googleapis/google-api-go-client
Links
 Open Source Insights
Jump to ...
Documentation
Overview
Index
Constants
Variables
Functions
Types
Source Files
 Documentation ¶
Overview ¶
Library status
Creating a client
Other authentication options

Package artifactregistry provides access to the Artifact Registry API.

For product documentation, see: https://cloud.google.com/artifacts/docs/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/artifactregistry/v1"
...
ctx := context.Background()
artifactregistryService, err := artifactregistry.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use google.golang.org/api/option.WithScopes:

artifactregistryService, err := artifactregistry.NewService(ctx, option.WithScopes(artifactregistry.CloudPlatformReadOnlyScope))


To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

artifactregistryService, err := artifactregistry.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
artifactregistryService, err := artifactregistry.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AptArtifact
func (s AptArtifact) MarshalJSON() ([]byte, error)
type AptRepository
func (s AptRepository) MarshalJSON() ([]byte, error)
type Attachment
func (s Attachment) MarshalJSON() ([]byte, error)
type BatchDeleteVersionsMetadata
func (s BatchDeleteVersionsMetadata) MarshalJSON() ([]byte, error)
type BatchDeleteVersionsRequest
func (s BatchDeleteVersionsRequest) MarshalJSON() ([]byte, error)
type Binding
func (s Binding) MarshalJSON() ([]byte, error)
type CleanupPolicy
func (s CleanupPolicy) MarshalJSON() ([]byte, error)
type CleanupPolicyCondition
func (s CleanupPolicyCondition) MarshalJSON() ([]byte, error)
type CleanupPolicyMostRecentVersions
func (s CleanupPolicyMostRecentVersions) MarshalJSON() ([]byte, error)
type CommonRemoteRepository
func (s CommonRemoteRepository) MarshalJSON() ([]byte, error)
type DockerImage
func (s DockerImage) MarshalJSON() ([]byte, error)
type DockerRepository
func (s DockerRepository) MarshalJSON() ([]byte, error)
type DockerRepositoryConfig
func (s DockerRepositoryConfig) MarshalJSON() ([]byte, error)
type DownloadFileResponse
type Empty
type ExportArtifactMetadata
func (s ExportArtifactMetadata) MarshalJSON() ([]byte, error)
type ExportArtifactRequest
func (s ExportArtifactRequest) MarshalJSON() ([]byte, error)
type ExportArtifactResponse
func (s ExportArtifactResponse) MarshalJSON() ([]byte, error)
type ExportedFile
func (s ExportedFile) MarshalJSON() ([]byte, error)
type Expr
func (s Expr) MarshalJSON() ([]byte, error)
type GenericArtifact
func (s GenericArtifact) MarshalJSON() ([]byte, error)
type GoModule
func (s GoModule) MarshalJSON() ([]byte, error)
type GoogetArtifact
func (s GoogetArtifact) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1File
func (s GoogleDevtoolsArtifactregistryV1File) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1Rule
func (s GoogleDevtoolsArtifactregistryV1Rule) MarshalJSON() ([]byte, error)
type Hash
func (s Hash) MarshalJSON() ([]byte, error)
type ImageManifest
func (s ImageManifest) MarshalJSON() ([]byte, error)
type ImportAptArtifactsErrorInfo
func (s ImportAptArtifactsErrorInfo) MarshalJSON() ([]byte, error)
type ImportAptArtifactsGcsSource
func (s ImportAptArtifactsGcsSource) MarshalJSON() ([]byte, error)
type ImportAptArtifactsMetadata
type ImportAptArtifactsRequest
func (s ImportAptArtifactsRequest) MarshalJSON() ([]byte, error)
type ImportAptArtifactsResponse
func (s ImportAptArtifactsResponse) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsErrorInfo
func (s ImportGoogetArtifactsErrorInfo) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsGcsSource
func (s ImportGoogetArtifactsGcsSource) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsMetadata
type ImportGoogetArtifactsRequest
func (s ImportGoogetArtifactsRequest) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsResponse
func (s ImportGoogetArtifactsResponse) MarshalJSON() ([]byte, error)
type ImportYumArtifactsErrorInfo
func (s ImportYumArtifactsErrorInfo) MarshalJSON() ([]byte, error)
type ImportYumArtifactsGcsSource
func (s ImportYumArtifactsGcsSource) MarshalJSON() ([]byte, error)
type ImportYumArtifactsMetadata
type ImportYumArtifactsRequest
func (s ImportYumArtifactsRequest) MarshalJSON() ([]byte, error)
type ImportYumArtifactsResponse
func (s ImportYumArtifactsResponse) MarshalJSON() ([]byte, error)
type KfpArtifact
func (s KfpArtifact) MarshalJSON() ([]byte, error)
type ListAttachmentsResponse
func (s ListAttachmentsResponse) MarshalJSON() ([]byte, error)
type ListDockerImagesResponse
func (s ListDockerImagesResponse) MarshalJSON() ([]byte, error)
type ListFilesResponse
func (s ListFilesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListMavenArtifactsResponse
func (s ListMavenArtifactsResponse) MarshalJSON() ([]byte, error)
type ListNpmPackagesResponse
func (s ListNpmPackagesResponse) MarshalJSON() ([]byte, error)
type ListPackagesResponse
func (s ListPackagesResponse) MarshalJSON() ([]byte, error)
type ListPythonPackagesResponse
func (s ListPythonPackagesResponse) MarshalJSON() ([]byte, error)
type ListRepositoriesResponse
func (s ListRepositoriesResponse) MarshalJSON() ([]byte, error)
type ListRulesResponse
func (s ListRulesResponse) MarshalJSON() ([]byte, error)
type ListTagsResponse
func (s ListTagsResponse) MarshalJSON() ([]byte, error)
type ListVersionsResponse
func (s ListVersionsResponse) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type MavenArtifact
func (s MavenArtifact) MarshalJSON() ([]byte, error)
type MavenRepository
func (s MavenRepository) MarshalJSON() ([]byte, error)
type MavenRepositoryConfig
func (s MavenRepositoryConfig) MarshalJSON() ([]byte, error)
type NpmPackage
func (s NpmPackage) MarshalJSON() ([]byte, error)
type NpmRepository
func (s NpmRepository) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadata
type Package
func (s Package) MarshalJSON() ([]byte, error)
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectSettings
func (s ProjectSettings) MarshalJSON() ([]byte, error)
type ProjectsGetProjectSettingsCall
func (c *ProjectsGetProjectSettingsCall) Context(ctx context.Context) *ProjectsGetProjectSettingsCall
func (c *ProjectsGetProjectSettingsCall) Do(opts ...googleapi.CallOption) (*ProjectSettings, error)
func (c *ProjectsGetProjectSettingsCall) Fields(s ...googleapi.Field) *ProjectsGetProjectSettingsCall
func (c *ProjectsGetProjectSettingsCall) Header() http.Header
func (c *ProjectsGetProjectSettingsCall) IfNoneMatch(entityTag string) *ProjectsGetProjectSettingsCall
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsGetVpcscConfigCall
func (c *ProjectsLocationsGetVpcscConfigCall) Context(ctx context.Context) *ProjectsLocationsGetVpcscConfigCall
func (c *ProjectsLocationsGetVpcscConfigCall) Do(opts ...googleapi.CallOption) (*VPCSCConfig, error)
func (c *ProjectsLocationsGetVpcscConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetVpcscConfigCall
func (c *ProjectsLocationsGetVpcscConfigCall) Header() http.Header
func (c *ProjectsLocationsGetVpcscConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetVpcscConfigCall
type ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Header() http.Header
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error
type ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsOperationsService
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsRepositoriesAptArtifactsImportCall
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAptArtifactsImportCall
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAptArtifactsImportCall
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Header() http.Header
type ProjectsLocationsRepositoriesAptArtifactsService
func NewProjectsLocationsRepositoriesAptArtifactsService(s *Service) *ProjectsLocationsRepositoriesAptArtifactsService
func (r *ProjectsLocationsRepositoriesAptArtifactsService) Import(parent string, importaptartifactsrequest *ImportAptArtifactsRequest) *ProjectsLocationsRepositoriesAptArtifactsImportCall
func (r *ProjectsLocationsRepositoriesAptArtifactsService) Upload(parent string, uploadaptartifactrequest *UploadAptArtifactRequest) *ProjectsLocationsRepositoriesAptArtifactsUploadCall
type ProjectsLocationsRepositoriesAptArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAptArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadAptArtifactMediaResponse, error)
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAptArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesAptArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesAptArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesAptArtifactsUploadCallDEPRECATED
type ProjectsLocationsRepositoriesAttachmentsCreateCall
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) AttachmentId(attachmentId string) *ProjectsLocationsRepositoriesAttachmentsCreateCall
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsCreateCall
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsCreateCall
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Header() http.Header
type ProjectsLocationsRepositoriesAttachmentsDeleteCall
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsDeleteCall
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsDeleteCall
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesAttachmentsGetCall
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsGetCall
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Do(opts ...googleapi.CallOption) (*Attachment, error)
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsGetCall
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesAttachmentsGetCall
type ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Do(opts ...googleapi.CallOption) (*ListAttachmentsResponse, error)
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Filter(filter string) *ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesAttachmentsListCall
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Pages(ctx context.Context, f func(*ListAttachmentsResponse) error) error
type ProjectsLocationsRepositoriesAttachmentsService
func NewProjectsLocationsRepositoriesAttachmentsService(s *Service) *ProjectsLocationsRepositoriesAttachmentsService
func (r *ProjectsLocationsRepositoriesAttachmentsService) Create(parent string, attachment *Attachment) *ProjectsLocationsRepositoriesAttachmentsCreateCall
func (r *ProjectsLocationsRepositoriesAttachmentsService) Delete(name string) *ProjectsLocationsRepositoriesAttachmentsDeleteCall
func (r *ProjectsLocationsRepositoriesAttachmentsService) Get(name string) *ProjectsLocationsRepositoriesAttachmentsGetCall
func (r *ProjectsLocationsRepositoriesAttachmentsService) List(parent string) *ProjectsLocationsRepositoriesAttachmentsListCall
type ProjectsLocationsRepositoriesCreateCall
func (c *ProjectsLocationsRepositoriesCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesCreateCall
func (c *ProjectsLocationsRepositoriesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesCreateCall
func (c *ProjectsLocationsRepositoriesCreateCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesCreateCall) RepositoryId(repositoryId string) *ProjectsLocationsRepositoriesCreateCall
type ProjectsLocationsRepositoriesDeleteCall
func (c *ProjectsLocationsRepositoriesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesDeleteCall
func (c *ProjectsLocationsRepositoriesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesDeleteCall
func (c *ProjectsLocationsRepositoriesDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesDockerImagesGetCall
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesDockerImagesGetCall
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Do(opts ...googleapi.CallOption) (*DockerImage, error)
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesDockerImagesGetCall
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesDockerImagesGetCall
type ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Do(opts ...googleapi.CallOption) (*ListDockerImagesResponse, error)
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesDockerImagesListCall
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Pages(ctx context.Context, f func(*ListDockerImagesResponse) error) error
type ProjectsLocationsRepositoriesDockerImagesService
func NewProjectsLocationsRepositoriesDockerImagesService(s *Service) *ProjectsLocationsRepositoriesDockerImagesService
func (r *ProjectsLocationsRepositoriesDockerImagesService) Get(name string) *ProjectsLocationsRepositoriesDockerImagesGetCall
func (r *ProjectsLocationsRepositoriesDockerImagesService) List(parent string) *ProjectsLocationsRepositoriesDockerImagesListCall
type ProjectsLocationsRepositoriesExportArtifactCall
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesExportArtifactCall
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesExportArtifactCall
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Header() http.Header
type ProjectsLocationsRepositoriesFilesDeleteCall
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesDeleteCall
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesDeleteCall
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesFilesDownloadCall
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesDownloadCall
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Do(opts ...googleapi.CallOption) (*DownloadFileResponse, error)
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Download(opts ...googleapi.CallOption) (*http.Response, error)
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesDownloadCall
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesFilesDownloadCall
type ProjectsLocationsRepositoriesFilesGetCall
func (c *ProjectsLocationsRepositoriesFilesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesGetCall
func (c *ProjectsLocationsRepositoriesFilesGetCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1File, error)
func (c *ProjectsLocationsRepositoriesFilesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesGetCall
func (c *ProjectsLocationsRepositoriesFilesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesFilesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesFilesGetCall
type ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) Do(opts ...googleapi.CallOption) (*ListFilesResponse, error)
func (c *ProjectsLocationsRepositoriesFilesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) Filter(filter string) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesFilesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesFilesListCall
func (c *ProjectsLocationsRepositoriesFilesListCall) Pages(ctx context.Context, f func(*ListFilesResponse) error) error
type ProjectsLocationsRepositoriesFilesPatchCall
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesPatchCall
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1File, error)
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesPatchCall
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesFilesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesFilesPatchCall
type ProjectsLocationsRepositoriesFilesService
func NewProjectsLocationsRepositoriesFilesService(s *Service) *ProjectsLocationsRepositoriesFilesService
func (r *ProjectsLocationsRepositoriesFilesService) Delete(name string) *ProjectsLocationsRepositoriesFilesDeleteCall
func (r *ProjectsLocationsRepositoriesFilesService) Download(name string) *ProjectsLocationsRepositoriesFilesDownloadCall
func (r *ProjectsLocationsRepositoriesFilesService) Get(name string) *ProjectsLocationsRepositoriesFilesGetCall
func (r *ProjectsLocationsRepositoriesFilesService) List(parent string) *ProjectsLocationsRepositoriesFilesListCall
func (r *ProjectsLocationsRepositoriesFilesService) Patch(name string, ...) *ProjectsLocationsRepositoriesFilesPatchCall
func (r *ProjectsLocationsRepositoriesFilesService) Upload(parent string, uploadfilerequest *UploadFileRequest) *ProjectsLocationsRepositoriesFilesUploadCall
type ProjectsLocationsRepositoriesFilesUploadCall
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesUploadCall
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Do(opts ...googleapi.CallOption) (*UploadFileMediaResponse, error)
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesUploadCall
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesFilesUploadCall
func (c *ProjectsLocationsRepositoriesFilesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesFilesUploadCall
func (c *ProjectsLocationsRepositoriesFilesUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesFilesUploadCallDEPRECATED
type ProjectsLocationsRepositoriesGenericArtifactsService
func NewProjectsLocationsRepositoriesGenericArtifactsService(s *Service) *ProjectsLocationsRepositoriesGenericArtifactsService
func (r *ProjectsLocationsRepositoriesGenericArtifactsService) Upload(parent string, uploadgenericartifactrequest *UploadGenericArtifactRequest) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall
type ProjectsLocationsRepositoriesGenericArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadGenericArtifactMediaResponse, error)
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesGenericArtifactsUploadCallDEPRECATED
type ProjectsLocationsRepositoriesGetCall
func (c *ProjectsLocationsRepositoriesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGetCall
func (c *ProjectsLocationsRepositoriesGetCall) Do(opts ...googleapi.CallOption) (*Repository, error)
func (c *ProjectsLocationsRepositoriesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGetCall
func (c *ProjectsLocationsRepositoriesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesGetCall
type ProjectsLocationsRepositoriesGetIamPolicyCall
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGetIamPolicyCall
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGetIamPolicyCall
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesGetIamPolicyCall
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsRepositoriesGetIamPolicyCall
type ProjectsLocationsRepositoriesGoModulesService
func NewProjectsLocationsRepositoriesGoModulesService(s *Service) *ProjectsLocationsRepositoriesGoModulesService
func (r *ProjectsLocationsRepositoriesGoModulesService) Upload(parent string, uploadgomodulerequest *UploadGoModuleRequest) *ProjectsLocationsRepositoriesGoModulesUploadCall
type ProjectsLocationsRepositoriesGoModulesUploadCall
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGoModulesUploadCall
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Do(opts ...googleapi.CallOption) (*UploadGoModuleMediaResponse, error)
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGoModulesUploadCall
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesGoModulesUploadCall
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesGoModulesUploadCall
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesGoModulesUploadCallDEPRECATED
type ProjectsLocationsRepositoriesGoogetArtifactsImportCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGoogetArtifactsImportCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGoogetArtifactsImportCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Header() http.Header
type ProjectsLocationsRepositoriesGoogetArtifactsService
func NewProjectsLocationsRepositoriesGoogetArtifactsService(s *Service) *ProjectsLocationsRepositoriesGoogetArtifactsService
func (r *ProjectsLocationsRepositoriesGoogetArtifactsService) Import(parent string, importgoogetartifactsrequest *ImportGoogetArtifactsRequest) *ProjectsLocationsRepositoriesGoogetArtifactsImportCall
func (r *ProjectsLocationsRepositoriesGoogetArtifactsService) Upload(parent string, uploadgoogetartifactrequest *UploadGoogetArtifactRequest) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall
type ProjectsLocationsRepositoriesGoogetArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadGoogetArtifactMediaResponse, error)
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCallDEPRECATED
type ProjectsLocationsRepositoriesKfpArtifactsService
func NewProjectsLocationsRepositoriesKfpArtifactsService(s *Service) *ProjectsLocationsRepositoriesKfpArtifactsService
func (r *ProjectsLocationsRepositoriesKfpArtifactsService) Upload(parent string, uploadkfpartifactrequest *UploadKfpArtifactRequest) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall
type ProjectsLocationsRepositoriesKfpArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadKfpArtifactMediaResponse, error)
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesKfpArtifactsUploadCallDEPRECATED
type ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) Do(opts ...googleapi.CallOption) (*ListRepositoriesResponse, error)
func (c *ProjectsLocationsRepositoriesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) Filter(filter string) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesListCall
func (c *ProjectsLocationsRepositoriesListCall) Pages(ctx context.Context, f func(*ListRepositoriesResponse) error) error
type ProjectsLocationsRepositoriesMavenArtifactsGetCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesMavenArtifactsGetCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Do(opts ...googleapi.CallOption) (*MavenArtifact, error)
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesMavenArtifactsGetCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesMavenArtifactsGetCall
type ProjectsLocationsRepositoriesMavenArtifactsListCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesMavenArtifactsListCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListMavenArtifactsResponse, error)
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesMavenArtifactsListCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesMavenArtifactsListCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesMavenArtifactsListCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesMavenArtifactsListCall
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Pages(ctx context.Context, f func(*ListMavenArtifactsResponse) error) error
type ProjectsLocationsRepositoriesMavenArtifactsService
func NewProjectsLocationsRepositoriesMavenArtifactsService(s *Service) *ProjectsLocationsRepositoriesMavenArtifactsService
func (r *ProjectsLocationsRepositoriesMavenArtifactsService) Get(name string) *ProjectsLocationsRepositoriesMavenArtifactsGetCall
func (r *ProjectsLocationsRepositoriesMavenArtifactsService) List(parent string) *ProjectsLocationsRepositoriesMavenArtifactsListCall
type ProjectsLocationsRepositoriesNpmPackagesGetCall
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesNpmPackagesGetCall
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Do(opts ...googleapi.CallOption) (*NpmPackage, error)
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesNpmPackagesGetCall
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesNpmPackagesGetCall
type ProjectsLocationsRepositoriesNpmPackagesListCall
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesNpmPackagesListCall
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Do(opts ...googleapi.CallOption) (*ListNpmPackagesResponse, error)
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesNpmPackagesListCall
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesNpmPackagesListCall
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesNpmPackagesListCall
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesNpmPackagesListCall
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Pages(ctx context.Context, f func(*ListNpmPackagesResponse) error) error
type ProjectsLocationsRepositoriesNpmPackagesService
func NewProjectsLocationsRepositoriesNpmPackagesService(s *Service) *ProjectsLocationsRepositoriesNpmPackagesService
func (r *ProjectsLocationsRepositoriesNpmPackagesService) Get(name string) *ProjectsLocationsRepositoriesNpmPackagesGetCall
func (r *ProjectsLocationsRepositoriesNpmPackagesService) List(parent string) *ProjectsLocationsRepositoriesNpmPackagesListCall
type ProjectsLocationsRepositoriesPackagesDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesPackagesGetCall
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesGetCall
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Do(opts ...googleapi.CallOption) (*Package, error)
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesGetCall
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesGetCall
type ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) Do(opts ...googleapi.CallOption) (*ListPackagesResponse, error)
func (c *ProjectsLocationsRepositoriesPackagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) Filter(filter string) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPackagesListCall
func (c *ProjectsLocationsRepositoriesPackagesListCall) Pages(ctx context.Context, f func(*ListPackagesResponse) error) error
type ProjectsLocationsRepositoriesPackagesPatchCall
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesPatchCall
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Do(opts ...googleapi.CallOption) (*Package, error)
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesPatchCall
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPackagesPatchCall
type ProjectsLocationsRepositoriesPackagesService
func NewProjectsLocationsRepositoriesPackagesService(s *Service) *ProjectsLocationsRepositoriesPackagesService
func (r *ProjectsLocationsRepositoriesPackagesService) Delete(name string) *ProjectsLocationsRepositoriesPackagesDeleteCall
func (r *ProjectsLocationsRepositoriesPackagesService) Get(name string) *ProjectsLocationsRepositoriesPackagesGetCall
func (r *ProjectsLocationsRepositoriesPackagesService) List(parent string) *ProjectsLocationsRepositoriesPackagesListCall
func (r *ProjectsLocationsRepositoriesPackagesService) Patch(name string, package_ *Package) *ProjectsLocationsRepositoriesPackagesPatchCall
type ProjectsLocationsRepositoriesPackagesTagsCreateCall
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsCreateCall
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Do(opts ...googleapi.CallOption) (*Tag, error)
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsCreateCall
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) TagId(tagId string) *ProjectsLocationsRepositoriesPackagesTagsCreateCall
type ProjectsLocationsRepositoriesPackagesTagsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesPackagesTagsGetCall
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsGetCall
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Do(opts ...googleapi.CallOption) (*Tag, error)
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsGetCall
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesTagsGetCall
type ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Do(opts ...googleapi.CallOption) (*ListTagsResponse, error)
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Filter(filter string) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Pages(ctx context.Context, f func(*ListTagsResponse) error) error
type ProjectsLocationsRepositoriesPackagesTagsPatchCall
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsPatchCall
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Do(opts ...googleapi.CallOption) (*Tag, error)
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsPatchCall
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPackagesTagsPatchCall
type ProjectsLocationsRepositoriesPackagesTagsService
func NewProjectsLocationsRepositoriesPackagesTagsService(s *Service) *ProjectsLocationsRepositoriesPackagesTagsService
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Create(parent string, tag *Tag) *ProjectsLocationsRepositoriesPackagesTagsCreateCall
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Delete(name string) *ProjectsLocationsRepositoriesPackagesTagsDeleteCall
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Get(name string) *ProjectsLocationsRepositoriesPackagesTagsGetCall
func (r *ProjectsLocationsRepositoriesPackagesTagsService) List(parent string) *ProjectsLocationsRepositoriesPackagesTagsListCall
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Patch(name string, tag *Tag) *ProjectsLocationsRepositoriesPackagesTagsPatchCall
type ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesPackagesVersionsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Force(force bool) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesPackagesVersionsGetCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsGetCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Do(opts ...googleapi.CallOption) (*Version, error)
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsGetCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesVersionsGetCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) View(view string) *ProjectsLocationsRepositoriesPackagesVersionsGetCall
type ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Do(opts ...googleapi.CallOption) (*ListVersionsResponse, error)
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Filter(filter string) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Pages(ctx context.Context, f func(*ListVersionsResponse) error) error
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) View(view string) *ProjectsLocationsRepositoriesPackagesVersionsListCall
type ProjectsLocationsRepositoriesPackagesVersionsPatchCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Do(opts ...googleapi.CallOption) (*Version, error)
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall
type ProjectsLocationsRepositoriesPackagesVersionsService
func NewProjectsLocationsRepositoriesPackagesVersionsService(s *Service) *ProjectsLocationsRepositoriesPackagesVersionsService
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) BatchDelete(parent string, batchdeleteversionsrequest *BatchDeleteVersionsRequest) *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) Delete(name string) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) Get(name string) *ProjectsLocationsRepositoriesPackagesVersionsGetCall
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) List(parent string) *ProjectsLocationsRepositoriesPackagesVersionsListCall
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) Patch(name string, version *Version) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall
type ProjectsLocationsRepositoriesPatchCall
func (c *ProjectsLocationsRepositoriesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPatchCall
func (c *ProjectsLocationsRepositoriesPatchCall) Do(opts ...googleapi.CallOption) (*Repository, error)
func (c *ProjectsLocationsRepositoriesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPatchCall
func (c *ProjectsLocationsRepositoriesPatchCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPatchCall
type ProjectsLocationsRepositoriesPythonPackagesGetCall
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPythonPackagesGetCall
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Do(opts ...googleapi.CallOption) (*PythonPackage, error)
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPythonPackagesGetCall
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPythonPackagesGetCall
type ProjectsLocationsRepositoriesPythonPackagesListCall
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPythonPackagesListCall
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Do(opts ...googleapi.CallOption) (*ListPythonPackagesResponse, error)
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPythonPackagesListCall
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPythonPackagesListCall
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPythonPackagesListCall
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPythonPackagesListCall
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Pages(ctx context.Context, f func(*ListPythonPackagesResponse) error) error
type ProjectsLocationsRepositoriesPythonPackagesService
func NewProjectsLocationsRepositoriesPythonPackagesService(s *Service) *ProjectsLocationsRepositoriesPythonPackagesService
func (r *ProjectsLocationsRepositoriesPythonPackagesService) Get(name string) *ProjectsLocationsRepositoriesPythonPackagesGetCall
func (r *ProjectsLocationsRepositoriesPythonPackagesService) List(parent string) *ProjectsLocationsRepositoriesPythonPackagesListCall
type ProjectsLocationsRepositoriesRulesCreateCall
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesCreateCall
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1Rule, error)
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesCreateCall
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesRulesCreateCall) RuleId(ruleId string) *ProjectsLocationsRepositoriesRulesCreateCall
type ProjectsLocationsRepositoriesRulesDeleteCall
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesDeleteCall
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesDeleteCall
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Header() http.Header
type ProjectsLocationsRepositoriesRulesGetCall
func (c *ProjectsLocationsRepositoriesRulesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesGetCall
func (c *ProjectsLocationsRepositoriesRulesGetCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1Rule, error)
func (c *ProjectsLocationsRepositoriesRulesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesGetCall
func (c *ProjectsLocationsRepositoriesRulesGetCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesRulesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesRulesGetCall
type ProjectsLocationsRepositoriesRulesListCall
func (c *ProjectsLocationsRepositoriesRulesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesListCall
func (c *ProjectsLocationsRepositoriesRulesListCall) Do(opts ...googleapi.CallOption) (*ListRulesResponse, error)
func (c *ProjectsLocationsRepositoriesRulesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesListCall
func (c *ProjectsLocationsRepositoriesRulesListCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesRulesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesRulesListCall
func (c *ProjectsLocationsRepositoriesRulesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesRulesListCall
func (c *ProjectsLocationsRepositoriesRulesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesRulesListCall
func (c *ProjectsLocationsRepositoriesRulesListCall) Pages(ctx context.Context, f func(*ListRulesResponse) error) error
type ProjectsLocationsRepositoriesRulesPatchCall
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesPatchCall
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1Rule, error)
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesPatchCall
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesRulesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesRulesPatchCall
type ProjectsLocationsRepositoriesRulesService
func NewProjectsLocationsRepositoriesRulesService(s *Service) *ProjectsLocationsRepositoriesRulesService
func (r *ProjectsLocationsRepositoriesRulesService) Create(parent string, ...) *ProjectsLocationsRepositoriesRulesCreateCall
func (r *ProjectsLocationsRepositoriesRulesService) Delete(name string) *ProjectsLocationsRepositoriesRulesDeleteCall
func (r *ProjectsLocationsRepositoriesRulesService) Get(name string) *ProjectsLocationsRepositoriesRulesGetCall
func (r *ProjectsLocationsRepositoriesRulesService) List(parent string) *ProjectsLocationsRepositoriesRulesListCall
func (r *ProjectsLocationsRepositoriesRulesService) Patch(name string, ...) *ProjectsLocationsRepositoriesRulesPatchCall
type ProjectsLocationsRepositoriesService
func NewProjectsLocationsRepositoriesService(s *Service) *ProjectsLocationsRepositoriesService
func (r *ProjectsLocationsRepositoriesService) Create(parent string, repository *Repository) *ProjectsLocationsRepositoriesCreateCall
func (r *ProjectsLocationsRepositoriesService) Delete(name string) *ProjectsLocationsRepositoriesDeleteCall
func (r *ProjectsLocationsRepositoriesService) ExportArtifact(repository string, exportartifactrequest *ExportArtifactRequest) *ProjectsLocationsRepositoriesExportArtifactCall
func (r *ProjectsLocationsRepositoriesService) Get(name string) *ProjectsLocationsRepositoriesGetCall
func (r *ProjectsLocationsRepositoriesService) GetIamPolicy(resource string) *ProjectsLocationsRepositoriesGetIamPolicyCall
func (r *ProjectsLocationsRepositoriesService) List(parent string) *ProjectsLocationsRepositoriesListCall
func (r *ProjectsLocationsRepositoriesService) Patch(name string, repository *Repository) *ProjectsLocationsRepositoriesPatchCall
func (r *ProjectsLocationsRepositoriesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsRepositoriesSetIamPolicyCall
func (r *ProjectsLocationsRepositoriesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsRepositoriesTestIamPermissionsCall
type ProjectsLocationsRepositoriesSetIamPolicyCall
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesSetIamPolicyCall
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesSetIamPolicyCall
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Header() http.Header
type ProjectsLocationsRepositoriesTestIamPermissionsCall
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesTestIamPermissionsCall
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesTestIamPermissionsCall
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsRepositoriesYumArtifactsImportCall
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesYumArtifactsImportCall
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesYumArtifactsImportCall
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Header() http.Header
type ProjectsLocationsRepositoriesYumArtifactsService
func NewProjectsLocationsRepositoriesYumArtifactsService(s *Service) *ProjectsLocationsRepositoriesYumArtifactsService
func (r *ProjectsLocationsRepositoriesYumArtifactsService) Import(parent string, importyumartifactsrequest *ImportYumArtifactsRequest) *ProjectsLocationsRepositoriesYumArtifactsImportCall
func (r *ProjectsLocationsRepositoriesYumArtifactsService) Upload(parent string, uploadyumartifactrequest *UploadYumArtifactRequest) *ProjectsLocationsRepositoriesYumArtifactsUploadCall
type ProjectsLocationsRepositoriesYumArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesYumArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadYumArtifactMediaResponse, error)
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesYumArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Header() http.Header
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesYumArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesYumArtifactsUploadCall
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ProjectsLocationsRepositoriesYumArtifactsUploadCallDEPRECATED
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) GetVpcscConfig(name string) *ProjectsLocationsGetVpcscConfigCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
func (r *ProjectsLocationsService) UpdateVpcscConfig(name string, vpcscconfig *VPCSCConfig) *ProjectsLocationsUpdateVpcscConfigCall
type ProjectsLocationsUpdateVpcscConfigCall
func (c *ProjectsLocationsUpdateVpcscConfigCall) Context(ctx context.Context) *ProjectsLocationsUpdateVpcscConfigCall
func (c *ProjectsLocationsUpdateVpcscConfigCall) Do(opts ...googleapi.CallOption) (*VPCSCConfig, error)
func (c *ProjectsLocationsUpdateVpcscConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsUpdateVpcscConfigCall
func (c *ProjectsLocationsUpdateVpcscConfigCall) Header() http.Header
func (c *ProjectsLocationsUpdateVpcscConfigCall) UpdateMask(updateMask string) *ProjectsLocationsUpdateVpcscConfigCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
func (r *ProjectsService) GetProjectSettings(name string) *ProjectsGetProjectSettingsCall
func (r *ProjectsService) UpdateProjectSettings(name string, projectsettings *ProjectSettings) *ProjectsUpdateProjectSettingsCall
type ProjectsUpdateProjectSettingsCall
func (c *ProjectsUpdateProjectSettingsCall) Context(ctx context.Context) *ProjectsUpdateProjectSettingsCall
func (c *ProjectsUpdateProjectSettingsCall) Do(opts ...googleapi.CallOption) (*ProjectSettings, error)
func (c *ProjectsUpdateProjectSettingsCall) Fields(s ...googleapi.Field) *ProjectsUpdateProjectSettingsCall
func (c *ProjectsUpdateProjectSettingsCall) Header() http.Header
func (c *ProjectsUpdateProjectSettingsCall) UpdateMask(updateMask string) *ProjectsUpdateProjectSettingsCall
type PythonPackage
func (s PythonPackage) MarshalJSON() ([]byte, error)
type PythonRepository
func (s PythonRepository) MarshalJSON() ([]byte, error)
type RemoteRepositoryConfig
func (s RemoteRepositoryConfig) MarshalJSON() ([]byte, error)
type Repository
func (s Repository) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SetIamPolicyRequest
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type Tag
func (s Tag) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type UploadAptArtifactMediaResponse
func (s UploadAptArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadAptArtifactMetadata
type UploadAptArtifactRequest
type UploadAptArtifactResponse
func (s UploadAptArtifactResponse) MarshalJSON() ([]byte, error)
type UploadFileMediaResponse
func (s UploadFileMediaResponse) MarshalJSON() ([]byte, error)
type UploadFileRequest
func (s UploadFileRequest) MarshalJSON() ([]byte, error)
type UploadGenericArtifactMediaResponse
func (s UploadGenericArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadGenericArtifactMetadata
type UploadGenericArtifactRequest
func (s UploadGenericArtifactRequest) MarshalJSON() ([]byte, error)
type UploadGoModuleMediaResponse
func (s UploadGoModuleMediaResponse) MarshalJSON() ([]byte, error)
type UploadGoModuleMetadata
type UploadGoModuleRequest
type UploadGoogetArtifactMediaResponse
func (s UploadGoogetArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadGoogetArtifactMetadata
type UploadGoogetArtifactRequest
type UploadGoogetArtifactResponse
func (s UploadGoogetArtifactResponse) MarshalJSON() ([]byte, error)
type UploadKfpArtifactMediaResponse
func (s UploadKfpArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadKfpArtifactMetadata
type UploadKfpArtifactRequest
func (s UploadKfpArtifactRequest) MarshalJSON() ([]byte, error)
type UploadYumArtifactMediaResponse
func (s UploadYumArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadYumArtifactMetadata
type UploadYumArtifactRequest
type UploadYumArtifactResponse
func (s UploadYumArtifactResponse) MarshalJSON() ([]byte, error)
type UpstreamCredentials
func (s UpstreamCredentials) MarshalJSON() ([]byte, error)
type UpstreamPolicy
func (s UpstreamPolicy) MarshalJSON() ([]byte, error)
type UsernamePasswordCredentials
func (s UsernamePasswordCredentials) MarshalJSON() ([]byte, error)
type VPCSCConfig
func (s VPCSCConfig) MarshalJSON() ([]byte, error)
type Version
func (s Version) MarshalJSON() ([]byte, error)
type VirtualRepositoryConfig
func (s VirtualRepositoryConfig) MarshalJSON() ([]byte, error)
type VulnerabilityScanningConfig
func (s VulnerabilityScanningConfig) MarshalJSON() ([]byte, error)
type YumArtifact
func (s YumArtifact) MarshalJSON() ([]byte, error)
type YumRepository
func (s YumRepository) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// See, edit, configure, and delete your Google Cloud data and see the email
	// address for your Google Account.
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"

	// View your data across Google Cloud services and see the email address of
	// your Google Account
	CloudPlatformReadOnlyScope = "https://www.googleapis.com/auth/cloud-platform.read-only"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type AptArtifact ¶
added in v0.51.0
type AptArtifact struct {
	// Architecture: Output only. Operating system architecture of the artifact.
	Architecture string `json:"architecture,omitempty"`
	// Component: Output only. Repository component of the artifact.
	Component string `json:"component,omitempty"`
	// ControlFile: Output only. Contents of the artifact's control metadata file.
	ControlFile string `json:"controlFile,omitempty"`
	// Name: Output only. The Artifact Registry resource name of the artifact.
	Name string `json:"name,omitempty"`
	// PackageName: Output only. The Apt package name of the artifact.
	PackageName string `json:"packageName,omitempty"`
	// PackageType: Output only. An artifact is a binary or source package.
	//
	// Possible values:
	//   "PACKAGE_TYPE_UNSPECIFIED" - Package type is not specified.
	//   "BINARY" - Binary package.
	//   "SOURCE" - Source package.
	PackageType string `json:"packageType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Architecture") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Architecture") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AptArtifact: A detailed representation of an Apt artifact. Information in the record is derived from the archive's control file. See https://www.debian.org/doc/debian-policy/ch-controlfields.html

func (AptArtifact) MarshalJSON ¶
added in v0.51.0
func (s AptArtifact) MarshalJSON() ([]byte, error)
type AptRepository ¶
added in v0.137.0
type AptRepository struct {
	// CustomRepository: Customer-specified remote repository.
	CustomRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository `json:"customRepository,omitempty"`
	// PublicRepository: One of the publicly available Apt repositories supported
	// by Artifact Registry.
	PublicRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository `json:"publicRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRepository") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AptRepository: Configuration for an Apt remote repository.

func (AptRepository) MarshalJSON ¶
added in v0.137.0
func (s AptRepository) MarshalJSON() ([]byte, error)
type Attachment ¶
added in v0.200.0
type Attachment struct {
	// Annotations: Optional. User annotations. These attributes can only be set
	// and used by the user, and not by Artifact Registry. See
	// https://google.aip.dev/128#annotations for more details such as format and
	// size limitations.
	Annotations map[string]string `json:"annotations,omitempty"`
	// AttachmentNamespace: The namespace this attachment belongs to. E.g. If an
	// attachment is created by artifact analysis, namespace is set to
	// `artifactanalysis.googleapis.com`.
	AttachmentNamespace string `json:"attachmentNamespace,omitempty"`
	// CreateTime: Output only. The time when the attachment was created.
	CreateTime string `json:"createTime,omitempty"`
	// Files: Required. The files that belong to this attachment. If the file ID
	// part contains slashes, they are escaped. E.g.
	// `projects/p1/locations/us-central1/repositories/repo1/files/sha:`.
	Files []string `json:"files,omitempty"`
	// Name: The name of the attachment. E.g.
	// `projects/p1/locations/us/repositories/repo/attachments/sbom`.
	Name string `json:"name,omitempty"`
	// OciVersionName: Output only. The name of the OCI version that this
	// attachment created. Only populated for Docker attachments. E.g.
	// `projects/p1/locations/us-central1/repositories/repo1/packages/p1/versions/v1
	// `.
	OciVersionName string `json:"ociVersionName,omitempty"`
	// Target: Required. The target the attachment is for, can be a Version,
	// Package or Repository. E.g.
	// `projects/p1/locations/us-central1/repositories/repo1/packages/p1/versions/v1
	// `.
	Target string `json:"target,omitempty"`
	// Type: Type of attachment. E.g. `application/vnd.spdx+json`
	Type string `json:"type,omitempty"`
	// UpdateTime: Output only. The time when the attachment was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Annotations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Annotations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Attachment: An Attachment refers to additional metadata that can be attached to artifacts in Artifact Registry. An attachment consists of one or more files.

func (Attachment) MarshalJSON ¶
added in v0.200.0
func (s Attachment) MarshalJSON() ([]byte, error)
type BatchDeleteVersionsMetadata ¶
added in v0.78.0
type BatchDeleteVersionsMetadata struct {
	// FailedVersions: The versions the operation failed to delete.
	FailedVersions []string `json:"failedVersions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FailedVersions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FailedVersions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchDeleteVersionsMetadata: The metadata of an LRO from deleting multiple versions.

func (BatchDeleteVersionsMetadata) MarshalJSON ¶
added in v0.78.0
func (s BatchDeleteVersionsMetadata) MarshalJSON() ([]byte, error)
type BatchDeleteVersionsRequest ¶
added in v0.130.0
type BatchDeleteVersionsRequest struct {
	// Names: Required. The names of the versions to delete. The maximum number of
	// versions deleted per batch is determined by the service and is dependent on
	// the available resources in the region.
	Names []string `json:"names,omitempty"`
	// ValidateOnly: If true, the request is performed without deleting data,
	// following AIP-163.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Names") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Names") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchDeleteVersionsRequest: The request to delete multiple versions across a repository.

func (BatchDeleteVersionsRequest) MarshalJSON ¶
added in v0.130.0
func (s BatchDeleteVersionsRequest) MarshalJSON() ([]byte, error)
type Binding ¶
added in v0.66.0
type Binding struct {
	// Condition: The condition that is associated with this binding. If the
	// condition evaluates to `true`, then this binding applies to the current
	// request. If the condition evaluates to `false`, then this binding does not
	// apply to the current request. However, a different role binding might grant
	// the same role to one or more of the principals in this binding. To learn
	// which resources support conditions in their IAM policies, see the IAM
	// documentation
	// (https://cloud.google.com/iam/help/conditions/resource-policies).
	Condition *Expr `json:"condition,omitempty"`
	// Members: Specifies the principals requesting access for a Google Cloud
	// resource. `members` can have the following values: * `allUsers`: A special
	// identifier that represents anyone who is on the internet; with or without a
	// Google account. * `allAuthenticatedUsers`: A special identifier that
	// represents anyone who is authenticated with a Google account or a service
	// account. Does not include identities that come from external identity
	// providers (IdPs) through identity federation. * `user:{emailid}`: An email
	// address that represents a specific Google account. For example,
	// `alice@example.com` . * `serviceAccount:{emailid}`: An email address that
	// represents a Google service account. For example,
	// `my-other-app@appspot.gserviceaccount.com`. *
	// `serviceAccount:{projectid}.svc.id.goog[{namespace}/{kubernetes-sa}]`: An
	// identifier for a Kubernetes service account
	// (https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts).
	// For example, `my-project.svc.id.goog[my-namespace/my-kubernetes-sa]`. *
	// `group:{emailid}`: An email address that represents a Google group. For
	// example, `admins@example.com`. * `domain:{domain}`: The G Suite domain
	// (primary) that represents all the users of that domain. For example,
	// `google.com` or `example.com`. *
	// `principal://iam.googleapis.com/locations/global/workforcePools/{pool_id}/sub
	// ject/{subject_attribute_value}`: A single identity in a workforce identity
	// pool. *
	// `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/
	// group/{group_id}`: All workforce identities in a group. *
	// `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/
	// attribute.{attribute_name}/{attribute_value}`: All workforce identities with
	// a specific attribute value. *
	// `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/
	// *`: All identities in a workforce identity pool. *
	// `principal://iam.googleapis.com/projects/{project_number}/locations/global/wo
	// rkloadIdentityPools/{pool_id}/subject/{subject_attribute_value}`: A single
	// identity in a workload identity pool. *
	// `principalSet://iam.googleapis.com/projects/{project_number}/locations/global
	// /workloadIdentityPools/{pool_id}/group/{group_id}`: A workload identity pool
	// group. *
	// `principalSet://iam.googleapis.com/projects/{project_number}/locations/global
	// /workloadIdentityPools/{pool_id}/attribute.{attribute_name}/{attribute_value}
	// `: All identities in a workload identity pool with a certain attribute. *
	// `principalSet://iam.googleapis.com/projects/{project_number}/locations/global
	// /workloadIdentityPools/{pool_id}/*`: All identities in a workload identity
	// pool. * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus
	// unique identifier) representing a user that has been recently deleted. For
	// example, `alice@example.com?uid=123456789012345678901`. If the user is
	// recovered, this value reverts to `user:{emailid}` and the recovered user
	// retains the role in the binding. *
	// `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus
	// unique identifier) representing a service account that has been recently
	// deleted. For example,
	// `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the
	// service account is undeleted, this value reverts to
	// `serviceAccount:{emailid}` and the undeleted service account retains the
	// role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An email
	// address (plus unique identifier) representing a Google group that has been
	// recently deleted. For example,
	// `admins@example.com?uid=123456789012345678901`. If the group is recovered,
	// this value reverts to `group:{emailid}` and the recovered group retains the
	// role in the binding. *
	// `deleted:principal://iam.googleapis.com/locations/global/workforcePools/{pool
	// _id}/subject/{subject_attribute_value}`: Deleted single identity in a
	// workforce identity pool. For example,
	// `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-po
	// ol-id/subject/my-subject-attribute-value`.
	Members []string `json:"members,omitempty"`
	// Role: Role that is assigned to the list of `members`, or principals. For
	// example, `roles/viewer`, `roles/editor`, or `roles/owner`. For an overview
	// of the IAM roles and permissions, see the IAM documentation
	// (https://cloud.google.com/iam/docs/roles-overview). For a list of the
	// available pre-defined roles, see here
	// (https://cloud.google.com/iam/docs/understanding-roles).
	Role string `json:"role,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Condition") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Condition") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Binding: Associates `members`, or principals, with a `role`.

func (Binding) MarshalJSON ¶
added in v0.66.0
func (s Binding) MarshalJSON() ([]byte, error)
type CleanupPolicy ¶
added in v0.130.0
type CleanupPolicy struct {
	// Action: Policy action.
	//
	// Possible values:
	//   "ACTION_UNSPECIFIED" - Action not specified.
	//   "DELETE" - Delete action.
	//   "KEEP" - Keep action.
	Action string `json:"action,omitempty"`
	// Condition: Policy condition for matching versions.
	Condition *CleanupPolicyCondition `json:"condition,omitempty"`
	// Id: The user-provided ID of the cleanup policy.
	Id string `json:"id,omitempty"`
	// MostRecentVersions: Policy condition for retaining a minimum number of
	// versions. May only be specified with a Keep action.
	MostRecentVersions *CleanupPolicyMostRecentVersions `json:"mostRecentVersions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Action") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Action") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CleanupPolicy: Artifact policy configuration for repository cleanup policies.

func (CleanupPolicy) MarshalJSON ¶
added in v0.130.0
func (s CleanupPolicy) MarshalJSON() ([]byte, error)
type CleanupPolicyCondition ¶
added in v0.130.0
type CleanupPolicyCondition struct {
	// NewerThan: Match versions newer than a duration.
	NewerThan string `json:"newerThan,omitempty"`
	// OlderThan: Match versions older than a duration.
	OlderThan string `json:"olderThan,omitempty"`
	// PackageNamePrefixes: Match versions by package prefix. Applied on any prefix
	// match.
	PackageNamePrefixes []string `json:"packageNamePrefixes,omitempty"`
	// TagPrefixes: Match versions by tag prefix. Applied on any prefix match.
	TagPrefixes []string `json:"tagPrefixes,omitempty"`
	// TagState: Match versions by tag status.
	//
	// Possible values:
	//   "TAG_STATE_UNSPECIFIED" - Tag status not specified.
	//   "TAGGED" - Applies to tagged versions only.
	//   "UNTAGGED" - Applies to untagged versions only.
	//   "ANY" - Applies to all versions.
	TagState string `json:"tagState,omitempty"`
	// VersionNamePrefixes: Match versions by version name prefix. Applied on any
	// prefix match.
	VersionNamePrefixes []string `json:"versionNamePrefixes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewerThan") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewerThan") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CleanupPolicyCondition: CleanupPolicyCondition is a set of conditions attached to a CleanupPolicy. If multiple entries are set, all must be satisfied for the condition to be satisfied.

func (CleanupPolicyCondition) MarshalJSON ¶
added in v0.130.0
func (s CleanupPolicyCondition) MarshalJSON() ([]byte, error)
type CleanupPolicyMostRecentVersions ¶
added in v0.130.0
type CleanupPolicyMostRecentVersions struct {
	// KeepCount: Minimum number of versions to keep.
	KeepCount int64 `json:"keepCount,omitempty"`
	// PackageNamePrefixes: List of package name prefixes that will apply this
	// rule.
	PackageNamePrefixes []string `json:"packageNamePrefixes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "KeepCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "KeepCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CleanupPolicyMostRecentVersions: CleanupPolicyMostRecentVersions is an alternate condition of a CleanupPolicy for retaining a minimum number of versions.

func (CleanupPolicyMostRecentVersions) MarshalJSON ¶
added in v0.130.0
func (s CleanupPolicyMostRecentVersions) MarshalJSON() ([]byte, error)
type CommonRemoteRepository ¶
added in v0.197.0
type CommonRemoteRepository struct {
	// Uri: Required. A common public repository base for remote repository.
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CommonRemoteRepository: Common remote repository settings type.

func (CommonRemoteRepository) MarshalJSON ¶
added in v0.197.0
func (s CommonRemoteRepository) MarshalJSON() ([]byte, error)
type DockerImage ¶
type DockerImage struct {
	// ArtifactType: ArtifactType of this image, e.g.
	// "application/vnd.example+type". If the `subject_digest` is set and no
	// `artifact_type` is given, the `media_type` will be considered as the
	// `artifact_type`. This field is returned as the `metadata.artifactType` field
	// in the Version resource.
	ArtifactType string `json:"artifactType,omitempty"`
	// BuildTime: The time this image was built. This field is returned as the
	// 'metadata.buildTime' field in the Version resource. The build time is
	// returned to the client as an RFC 3339 string, which can be easily used with
	// the JavaScript Date constructor.
	BuildTime string `json:"buildTime,omitempty"`
	// ImageManifests: Optional. For multi-arch images (manifest lists), this field
	// contains the list of image manifests.
	ImageManifests []*ImageManifest `json:"imageManifests,omitempty"`
	// ImageSizeBytes: Calculated size of the image. This field is returned as the
	// 'metadata.imageSizeBytes' field in the Version resource.
	ImageSizeBytes int64 `json:"imageSizeBytes,omitempty,string"`
	// MediaType: Media type of this image, e.g.
	// "application/vnd.docker.distribution.manifest.v2+json". This field is
	// returned as the 'metadata.mediaType' field in the Version resource.
	MediaType string `json:"mediaType,omitempty"`
	// Name: Required. registry_location, project_id, repository_name and image id
	// forms a unique image
	// name:`projects//locations//repositories//dockerImages/`. For example,
	// "projects/test-project/locations/us-west4/repositories/test-repo/dockerImages
	// /
	// nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf
	// ", where "us-west4" is the registry_location, "test-project" is the
	// project_id, "test-repo" is the repository_name and
	// "nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7c
	// f" is the image's digest.
	Name string `json:"name,omitempty"`
	// Tags: Tags attached to this image.
	Tags []string `json:"tags,omitempty"`
	// UpdateTime: Output only. The time when the docker image was last updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// UploadTime: Time the image was uploaded.
	UploadTime string `json:"uploadTime,omitempty"`
	// Uri: Required. URL to access the image. Example:
	// us-west4-docker.pkg.dev/test-project/test-repo/nginx@sha256:e9954c1fc875017be
	// 1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf
	Uri string `json:"uri,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ArtifactType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ArtifactType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DockerImage: DockerImage represents a docker artifact. The following fields are returned as untyped metadata in the Version resource, using camelcase keys (i.e. metadata.imageSizeBytes): * imageSizeBytes * mediaType * buildTime

func (DockerImage) MarshalJSON ¶
func (s DockerImage) MarshalJSON() ([]byte, error)
type DockerRepository ¶
added in v0.110.0
type DockerRepository struct {
	// CustomRepository: Customer-specified remote repository.
	CustomRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository `json:"customRepository,omitempty"`
	// PublicRepository: One of the publicly available Docker repositories
	// supported by Artifact Registry.
	//
	// Possible values:
	//   "PUBLIC_REPOSITORY_UNSPECIFIED" - Unspecified repository.
	//   "DOCKER_HUB" - Docker Hub.
	PublicRepository string `json:"publicRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRepository") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DockerRepository: Configuration for a Docker remote repository.

func (DockerRepository) MarshalJSON ¶
added in v0.110.0
func (s DockerRepository) MarshalJSON() ([]byte, error)
type DockerRepositoryConfig ¶
added in v0.114.0
type DockerRepositoryConfig struct {
	// ImmutableTags: The repository which enabled this flag prevents all tags from
	// being modified, moved or deleted. This does not prevent tags from being
	// created.
	ImmutableTags bool `json:"immutableTags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ImmutableTags") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ImmutableTags") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DockerRepositoryConfig: DockerRepositoryConfig is docker related repository details. Provides additional configuration details for repositories of the docker format type.

func (DockerRepositoryConfig) MarshalJSON ¶
added in v0.114.0
func (s DockerRepositoryConfig) MarshalJSON() ([]byte, error)
type DownloadFileResponse ¶
added in v0.169.0
type DownloadFileResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

DownloadFileResponse: The response to download a file.

type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type ExportArtifactMetadata ¶
added in v0.255.0
type ExportArtifactMetadata struct {
	// ExportedFiles: The exported artifact files.
	ExportedFiles []*ExportedFile `json:"exportedFiles,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExportedFiles") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExportedFiles") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExportArtifactMetadata: The LRO metadata for exporting an artifact.

func (ExportArtifactMetadata) MarshalJSON ¶
added in v0.255.0
func (s ExportArtifactMetadata) MarshalJSON() ([]byte, error)
type ExportArtifactRequest ¶
added in v0.255.0
type ExportArtifactRequest struct {
	// GcsPath: The Cloud Storage path to export the artifact to. Should start with
	// the bucket name, and optionally have a directory path. Examples:
	// `dst_bucket`, `dst_bucket/sub_dir`. Existing objects with the same path will
	// be overwritten.
	GcsPath string `json:"gcsPath,omitempty"`
	// SourceTag: The artifact tag to export.
	// Format:projects/{project}/locations/{location}/repositories/{repository}/pack
	// ages/{package}/tags/{tag}
	SourceTag string `json:"sourceTag,omitempty"`
	// SourceVersion: The artifact version to export. Format:
	// projects/{project}/locations/{location}/repositories/{repository}/packages/{p
	// ackage}/versions/{version}
	SourceVersion string `json:"sourceVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcsPath") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcsPath") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExportArtifactRequest: The request for exporting an artifact to a destination.

func (ExportArtifactRequest) MarshalJSON ¶
added in v0.255.0
func (s ExportArtifactRequest) MarshalJSON() ([]byte, error)
type ExportArtifactResponse ¶
added in v0.255.0
type ExportArtifactResponse struct {
	// ExportedVersion: The exported version. Should be the same as the request
	// version with fingerprint resource name.
	ExportedVersion *Version `json:"exportedVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExportedVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExportedVersion") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExportArtifactResponse: The response for exporting an artifact to a destination.

func (ExportArtifactResponse) MarshalJSON ¶
added in v0.255.0
func (s ExportArtifactResponse) MarshalJSON() ([]byte, error)
type ExportedFile ¶
added in v0.255.0
type ExportedFile struct {
	// GcsObjectPath: Cloud Storage Object path of the exported file. Examples:
	// `dst_bucket/file1`, `dst_bucket/sub_dir/file1`
	GcsObjectPath string `json:"gcsObjectPath,omitempty"`
	// Hashes: The hashes of the file content.
	Hashes []*Hash `json:"hashes,omitempty"`
	// Name: Name of the exported artifact file. Format:
	// `projects/p1/locations/us/repositories/repo1/files/file1`
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcsObjectPath") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcsObjectPath") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExportedFile: The exported artifact file.

func (ExportedFile) MarshalJSON ¶
added in v0.255.0
func (s ExportedFile) MarshalJSON() ([]byte, error)
type Expr ¶
added in v0.66.0
type Expr struct {
	// Description: Optional. Description of the expression. This is a longer text
	// which describes the expression, e.g. when hovered over it in a UI.
	Description string `json:"description,omitempty"`
	// Expression: Textual representation of an expression in Common Expression
	// Language syntax.
	Expression string `json:"expression,omitempty"`
	// Location: Optional. String indicating the location of the expression for
	// error reporting, e.g. a file name and a position in the file.
	Location string `json:"location,omitempty"`
	// Title: Optional. Title for the expression, i.e. a short string describing
	// its purpose. This can be used e.g. in UIs which allow to enter the
	// expression.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Description") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Description") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Expr: Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at https://github.com/google/cel-spec. Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() < 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

func (Expr) MarshalJSON ¶
added in v0.66.0
func (s Expr) MarshalJSON() ([]byte, error)
type GenericArtifact ¶
added in v0.178.0
type GenericArtifact struct {
	// CreateTime: Output only. The time when the Generic module is created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Resource name of the generic artifact. project, location, repository,
	// package_id and version_id create a unique generic artifact. i.e.
	// "projects/test-project/locations/us-west4/repositories/test-repo/
	// genericArtifacts/package_id:version_id"
	Name string `json:"name,omitempty"`
	// UpdateTime: Output only. The time when the Generic module is updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// Version: The version of the generic artifact.
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GenericArtifact: GenericArtifact represents a generic artifact

func (GenericArtifact) MarshalJSON ¶
added in v0.178.0
func (s GenericArtifact) MarshalJSON() ([]byte, error)
type GoModule ¶
added in v0.129.0
type GoModule struct {
	// CreateTime: Output only. The time when the Go module is created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: The resource name of a Go module.
	Name string `json:"name,omitempty"`
	// UpdateTime: Output only. The time when the Go module is updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// Version: The version of the Go module. Must be a valid canonical version as
	// defined in https://go.dev/ref/mod#glos-canonical-version.
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoModule: GoModule represents a Go module.

func (GoModule) MarshalJSON ¶
added in v0.129.0
func (s GoModule) MarshalJSON() ([]byte, error)
type GoogetArtifact ¶
added in v0.123.0
type GoogetArtifact struct {
	// Architecture: Output only. Operating system architecture of the artifact.
	Architecture string `json:"architecture,omitempty"`
	// Name: Output only. The Artifact Registry resource name of the artifact.
	Name string `json:"name,omitempty"`
	// PackageName: Output only. The GooGet package name of the artifact.
	PackageName string `json:"packageName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Architecture") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Architecture") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogetArtifact: A detailed representation of a GooGet artifact.

func (GoogetArtifact) MarshalJSON ¶
added in v0.123.0
func (s GoogetArtifact) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1File ¶
added in v0.66.0
type GoogleDevtoolsArtifactregistryV1File struct {
	// Annotations: Optional. Client specified annotations.
	Annotations map[string]string `json:"annotations,omitempty"`
	// CreateTime: Output only. The time when the File was created.
	CreateTime string `json:"createTime,omitempty"`
	// FetchTime: Output only. The time when the last attempt to refresh the file's
	// data was made. Only set when the repository is remote.
	FetchTime string `json:"fetchTime,omitempty"`
	// Hashes: The hashes of the file content.
	Hashes []*Hash `json:"hashes,omitempty"`
	// Name: The name of the file, for example:
	// `projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt`.
	// If the file ID part contains slashes, they are escaped.
	Name string `json:"name,omitempty"`
	// Owner: The name of the Package or Version that owns this file, if any.
	Owner string `json:"owner,omitempty"`
	// SizeBytes: The size of the File in bytes.
	SizeBytes int64 `json:"sizeBytes,omitempty,string"`
	// UpdateTime: Output only. The time when the File was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Annotations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Annotations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1File: Files store content that is potentially associated with Packages or Versions.

func (GoogleDevtoolsArtifactregistryV1File) MarshalJSON ¶
added in v0.66.0
func (s GoogleDevtoolsArtifactregistryV1File) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository ¶
added in v0.169.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository struct {
	// Uri: An http/https uri reference to the upstream remote repository, for ex:
	// "https://my.apt.registry/".
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepo sitory: Customer-specified publicly available remote repository.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository) MarshalJSON ¶
added in v0.169.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository ¶
added in v0.137.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository struct {
	// RepositoryBase: A common public repository base for Apt.
	//
	// Possible values:
	//   "REPOSITORY_BASE_UNSPECIFIED" - Unspecified repository base.
	//   "DEBIAN" - Debian.
	//   "UBUNTU" - Ubuntu LTS/Pro.
	//   "DEBIAN_SNAPSHOT" - Archived Debian.
	RepositoryBase string `json:"repositoryBase,omitempty"`
	// RepositoryPath: A custom field to define a path to a specific repository
	// from the base.
	RepositoryPath string `json:"repositoryPath,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RepositoryBase") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RepositoryBase") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepo sitory: Publicly available Apt repositories constructed from a common repository base and a custom repository path.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository) MarshalJSON ¶
added in v0.137.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository ¶
added in v0.169.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository struct {
	// Uri: An http/https uri reference to the custom remote repository, for ex:
	// "https://registry-1.docker.io".
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomR epository: Customer-specified publicly available remote repository.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository) MarshalJSON ¶
added in v0.169.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository ¶
added in v0.169.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository struct {
	// Uri: An http/https uri reference to the upstream remote repository, for ex:
	// "https://my.maven.registry/".
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRe pository: Customer-specified publicly available remote repository.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository) MarshalJSON ¶
added in v0.169.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository ¶
added in v0.169.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository struct {
	// Uri: An http/https uri reference to the upstream remote repository, for ex:
	// "https://my.npm.registry/".
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepo sitory: Customer-specified publicly available remote repository.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository) MarshalJSON ¶
added in v0.169.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository ¶
added in v0.169.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository struct {
	// Uri: An http/https uri reference to the upstream remote repository, for ex:
	// "https://my.python.registry/".
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomR epository: Customer-specified publicly available remote repository.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository) MarshalJSON ¶
added in v0.169.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository ¶
added in v0.169.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository struct {
	// Uri: An http/https uri reference to the upstream remote repository, for ex:
	// "https://my.yum.registry/".
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepo sitory: Customer-specified publicly available remote repository.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository) MarshalJSON ¶
added in v0.169.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository ¶
added in v0.137.0
type GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository struct {
	// RepositoryBase: A common public repository base for Yum.
	//
	// Possible values:
	//   "REPOSITORY_BASE_UNSPECIFIED" - Unspecified repository base.
	//   "CENTOS" - CentOS.
	//   "CENTOS_DEBUG" - CentOS Debug.
	//   "CENTOS_VAULT" - CentOS Vault.
	//   "CENTOS_STREAM" - CentOS Stream.
	//   "ROCKY" - Rocky.
	//   "EPEL" - Fedora Extra Packages for Enterprise Linux (EPEL).
	RepositoryBase string `json:"repositoryBase,omitempty"`
	// RepositoryPath: A custom field to define a path to a specific repository
	// from the base.
	RepositoryPath string `json:"repositoryPath,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RepositoryBase") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RepositoryBase") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepo sitory: Publicly available Yum repositories constructed from a common repository base and a custom repository path.

func (GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository) MarshalJSON ¶
added in v0.137.0
func (s GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository) MarshalJSON() ([]byte, error)
type GoogleDevtoolsArtifactregistryV1Rule ¶
added in v0.200.0
type GoogleDevtoolsArtifactregistryV1Rule struct {
	// Action: The action this rule takes.
	//
	// Possible values:
	//   "ACTION_UNSPECIFIED" - Action not specified.
	//   "ALLOW" - Allow the operation.
	//   "DENY" - Deny the operation.
	Action string `json:"action,omitempty"`
	// Condition: Optional. A CEL expression for conditions that must be met in
	// order for the rule to apply. If not provided, the rule matches all objects.
	Condition *Expr `json:"condition,omitempty"`
	// Name: The name of the rule, for example:
	// `projects/p1/locations/us-central1/repositories/repo1/rules/rule1`.
	Name string `json:"name,omitempty"`
	// Possible values:
	//   "OPERATION_UNSPECIFIED" - Operation not specified.
	//   "DOWNLOAD" - Download operation.
	Operation string `json:"operation,omitempty"`
	// PackageId: The package ID the rule applies to. If empty, this rule applies
	// to all packages inside the repository.
	PackageId string `json:"packageId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Action") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Action") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleDevtoolsArtifactregistryV1Rule: A rule defines the deny or allow action of the operation it applies to and the conditions required for the rule to apply. You can set one rule for an entire repository and one rule for each package within.

func (GoogleDevtoolsArtifactregistryV1Rule) MarshalJSON ¶
added in v0.200.0
func (s GoogleDevtoolsArtifactregistryV1Rule) MarshalJSON() ([]byte, error)
type Hash ¶
added in v0.66.0
type Hash struct {
	// Type: The algorithm used to compute the hash value.
	//
	// Possible values:
	//   "HASH_TYPE_UNSPECIFIED" - Unspecified.
	//   "SHA256" - SHA256 hash.
	//   "MD5" - MD5 hash.
	//   "DIRSUM_SHA256" - Dirsum SHA256 hash.
	Type string `json:"type,omitempty"`
	// Value: The hash value.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Type") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Type") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Hash: A hash of file content.

func (Hash) MarshalJSON ¶
added in v0.66.0
func (s Hash) MarshalJSON() ([]byte, error)
type ImageManifest ¶
added in v0.258.0
type ImageManifest struct {
	// Architecture: Optional. The CPU architecture of the image. Values are
	// provided by the Docker client and are not validated by Artifact Registry.
	// Example values include "amd64", "arm64", "ppc64le", "s390x", "riscv64",
	// "mips64le", etc.
	Architecture string `json:"architecture,omitempty"`
	// Digest: Optional. The manifest digest, in the format "sha256:".
	Digest string `json:"digest,omitempty"`
	// MediaType: Optional. The media type of the manifest, e.g.,
	// "application/vnd.docker.distribution.manifest.v2+json"
	MediaType string `json:"mediaType,omitempty"`
	// Os: Optional. The operating system of the image. Values are provided by the
	// Docker client and are not validated by Artifact Registry. Example values
	// include "linux", "windows", "darwin", "aix", etc.
	Os string `json:"os,omitempty"`
	// OsFeatures: Optional. The required OS features for the image, for example on
	// Windows `win32k`.
	OsFeatures []string `json:"osFeatures,omitempty"`
	// OsVersion: Optional. The OS version of the image, for example on Windows
	// `10.0.14393.1066`.
	OsVersion string `json:"osVersion,omitempty"`
	// Variant: Optional. The variant of the CPU in the image, for example `v7` to
	// specify ARMv7 when architecture is `arm`.
	Variant string `json:"variant,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Architecture") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Architecture") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImageManifest: Details of a single image manifest within a multi-arch image.

func (ImageManifest) MarshalJSON ¶
added in v0.258.0
func (s ImageManifest) MarshalJSON() ([]byte, error)
type ImportAptArtifactsErrorInfo ¶
added in v0.51.0
type ImportAptArtifactsErrorInfo struct {
	// Error: The detailed error status.
	Error *Status `json:"error,omitempty"`
	// GcsSource: Google Cloud Storage location requested.
	GcsSource *ImportAptArtifactsGcsSource `json:"gcsSource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Error") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Error") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportAptArtifactsErrorInfo: Error information explaining why a package was not imported.

func (ImportAptArtifactsErrorInfo) MarshalJSON ¶
added in v0.51.0
func (s ImportAptArtifactsErrorInfo) MarshalJSON() ([]byte, error)
type ImportAptArtifactsGcsSource ¶
added in v0.51.0
type ImportAptArtifactsGcsSource struct {
	// Uris: Cloud Storage paths URI (e.g., gs://my_bucket//my_object).
	Uris []string `json:"uris,omitempty"`
	// UseWildcards: Supports URI wildcards for matching multiple objects from a
	// single URI.
	UseWildcards bool `json:"useWildcards,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uris") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uris") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportAptArtifactsGcsSource: Google Cloud Storage location where the artifacts currently reside.

func (ImportAptArtifactsGcsSource) MarshalJSON ¶
added in v0.51.0
func (s ImportAptArtifactsGcsSource) MarshalJSON() ([]byte, error)
type ImportAptArtifactsMetadata ¶
added in v0.75.0
type ImportAptArtifactsMetadata struct {
}

ImportAptArtifactsMetadata: The operation metadata for importing artifacts.

type ImportAptArtifactsRequest ¶
added in v0.66.0
type ImportAptArtifactsRequest struct {
	// GcsSource: Google Cloud Storage location where input content is located.
	GcsSource *ImportAptArtifactsGcsSource `json:"gcsSource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcsSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcsSource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportAptArtifactsRequest: The request to import new apt artifacts.

func (ImportAptArtifactsRequest) MarshalJSON ¶
added in v0.66.0
func (s ImportAptArtifactsRequest) MarshalJSON() ([]byte, error)
type ImportAptArtifactsResponse ¶
added in v0.51.0
type ImportAptArtifactsResponse struct {
	// AptArtifacts: The Apt artifacts imported.
	AptArtifacts []*AptArtifact `json:"aptArtifacts,omitempty"`
	// Errors: Detailed error info for packages that were not imported.
	Errors []*ImportAptArtifactsErrorInfo `json:"errors,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AptArtifacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AptArtifacts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportAptArtifactsResponse: The response message from importing APT artifacts.

func (ImportAptArtifactsResponse) MarshalJSON ¶
added in v0.51.0
func (s ImportAptArtifactsResponse) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsErrorInfo ¶
added in v0.123.0
type ImportGoogetArtifactsErrorInfo struct {
	// Error: The detailed error status.
	Error *Status `json:"error,omitempty"`
	// GcsSource: Google Cloud Storage location requested.
	GcsSource *ImportGoogetArtifactsGcsSource `json:"gcsSource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Error") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Error") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportGoogetArtifactsErrorInfo: Error information explaining why a package was not imported.

func (ImportGoogetArtifactsErrorInfo) MarshalJSON ¶
added in v0.123.0
func (s ImportGoogetArtifactsErrorInfo) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsGcsSource ¶
added in v0.122.0
type ImportGoogetArtifactsGcsSource struct {
	// Uris: Cloud Storage paths URI (e.g., `gs://my_bucket/my_object`).
	Uris []string `json:"uris,omitempty"`
	// UseWildcards: Supports URI wildcards for matching multiple objects from a
	// single URI.
	UseWildcards bool `json:"useWildcards,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uris") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uris") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportGoogetArtifactsGcsSource: Google Cloud Storage location where the artifacts currently reside.

func (ImportGoogetArtifactsGcsSource) MarshalJSON ¶
added in v0.122.0
func (s ImportGoogetArtifactsGcsSource) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsMetadata ¶
added in v0.123.0
type ImportGoogetArtifactsMetadata struct {
}

ImportGoogetArtifactsMetadata: The operation metadata for importing artifacts.

type ImportGoogetArtifactsRequest ¶
added in v0.122.0
type ImportGoogetArtifactsRequest struct {
	// GcsSource: Google Cloud Storage location where input content is located.
	GcsSource *ImportGoogetArtifactsGcsSource `json:"gcsSource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcsSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcsSource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportGoogetArtifactsRequest: The request to import new googet artifacts.

func (ImportGoogetArtifactsRequest) MarshalJSON ¶
added in v0.122.0
func (s ImportGoogetArtifactsRequest) MarshalJSON() ([]byte, error)
type ImportGoogetArtifactsResponse ¶
added in v0.123.0
type ImportGoogetArtifactsResponse struct {
	// Errors: Detailed error info for packages that were not imported.
	Errors []*ImportGoogetArtifactsErrorInfo `json:"errors,omitempty"`
	// GoogetArtifacts: The GooGet artifacts updated.
	GoogetArtifacts []*GoogetArtifact `json:"googetArtifacts,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Errors") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Errors") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportGoogetArtifactsResponse: The response message from importing artifacts.

func (ImportGoogetArtifactsResponse) MarshalJSON ¶
added in v0.123.0
func (s ImportGoogetArtifactsResponse) MarshalJSON() ([]byte, error)
type ImportYumArtifactsErrorInfo ¶
added in v0.51.0
type ImportYumArtifactsErrorInfo struct {
	// Error: The detailed error status.
	Error *Status `json:"error,omitempty"`
	// GcsSource: Google Cloud Storage location requested.
	GcsSource *ImportYumArtifactsGcsSource `json:"gcsSource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Error") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Error") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportYumArtifactsErrorInfo: Error information explaining why a package was not imported.

func (ImportYumArtifactsErrorInfo) MarshalJSON ¶
added in v0.51.0
func (s ImportYumArtifactsErrorInfo) MarshalJSON() ([]byte, error)
type ImportYumArtifactsGcsSource ¶
added in v0.51.0
type ImportYumArtifactsGcsSource struct {
	// Uris: Cloud Storage paths URI (e.g., gs://my_bucket//my_object).
	Uris []string `json:"uris,omitempty"`
	// UseWildcards: Supports URI wildcards for matching multiple objects from a
	// single URI.
	UseWildcards bool `json:"useWildcards,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uris") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uris") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportYumArtifactsGcsSource: Google Cloud Storage location where the artifacts currently reside.

func (ImportYumArtifactsGcsSource) MarshalJSON ¶
added in v0.51.0
func (s ImportYumArtifactsGcsSource) MarshalJSON() ([]byte, error)
type ImportYumArtifactsMetadata ¶
added in v0.75.0
type ImportYumArtifactsMetadata struct {
}

ImportYumArtifactsMetadata: The operation metadata for importing artifacts.

type ImportYumArtifactsRequest ¶
added in v0.66.0
type ImportYumArtifactsRequest struct {
	// GcsSource: Google Cloud Storage location where input content is located.
	GcsSource *ImportYumArtifactsGcsSource `json:"gcsSource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcsSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcsSource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportYumArtifactsRequest: The request to import new yum artifacts.

func (ImportYumArtifactsRequest) MarshalJSON ¶
added in v0.66.0
func (s ImportYumArtifactsRequest) MarshalJSON() ([]byte, error)
type ImportYumArtifactsResponse ¶
added in v0.51.0
type ImportYumArtifactsResponse struct {
	// Errors: Detailed error info for packages that were not imported.
	Errors []*ImportYumArtifactsErrorInfo `json:"errors,omitempty"`
	// YumArtifacts: The yum artifacts imported.
	YumArtifacts []*YumArtifact `json:"yumArtifacts,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Errors") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Errors") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportYumArtifactsResponse: The response message from importing YUM artifacts.

func (ImportYumArtifactsResponse) MarshalJSON ¶
added in v0.51.0
func (s ImportYumArtifactsResponse) MarshalJSON() ([]byte, error)
type KfpArtifact ¶
added in v0.98.0
type KfpArtifact struct {
	// Name: Output only. Resource name of the KFP artifact. Since users don't
	// directly interact with this resource, the name will be derived from the
	// associated version. For example, when version =
	// ".../versions/sha256:abcdef...", the name will be
	// ".../kfpArtifacts/sha256:abcdef...".
	Name string `json:"name,omitempty"`
	// Version: The version associated with the KFP artifact. Must follow the
	// Semantic Versioning standard.
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Name") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Name") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

KfpArtifact: A detailed representation of a KFP artifact.

func (KfpArtifact) MarshalJSON ¶
added in v0.98.0
func (s KfpArtifact) MarshalJSON() ([]byte, error)
type ListAttachmentsResponse ¶
added in v0.200.0
type ListAttachmentsResponse struct {
	// Attachments: The attachments returned.
	Attachments []*Attachment `json:"attachments,omitempty"`
	// NextPageToken: The token to retrieve the next page of attachments, or empty
	// if there are no more attachments to return.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attachments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attachments") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAttachmentsResponse: The response from listing attachments.

func (ListAttachmentsResponse) MarshalJSON ¶
added in v0.200.0
func (s ListAttachmentsResponse) MarshalJSON() ([]byte, error)
type ListDockerImagesResponse ¶
added in v0.41.0
type ListDockerImagesResponse struct {
	// DockerImages: The docker images returned.
	DockerImages []*DockerImage `json:"dockerImages,omitempty"`
	// NextPageToken: The token to retrieve the next page of artifacts, or empty if
	// there are no more artifacts to return.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DockerImages") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DockerImages") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDockerImagesResponse: The response from listing docker images.

func (ListDockerImagesResponse) MarshalJSON ¶
added in v0.41.0
func (s ListDockerImagesResponse) MarshalJSON() ([]byte, error)
type ListFilesResponse ¶
added in v0.66.0
type ListFilesResponse struct {
	// Files: The files returned.
	Files []*GoogleDevtoolsArtifactregistryV1File `json:"files,omitempty"`
	// NextPageToken: The token to retrieve the next page of files, or empty if
	// there are no more files to return.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Files") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Files") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListFilesResponse: The response from listing files.

func (ListFilesResponse) MarshalJSON ¶
added in v0.66.0
func (s ListFilesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse ¶
added in v0.74.0
type ListLocationsResponse struct {
	// Locations: A list of locations that matches the specified filter in the
	// request.
	Locations []*Location `json:"locations,omitempty"`
	// NextPageToken: The standard List next-page token.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Locations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Locations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListLocationsResponse: The response message for Locations.ListLocations.

func (ListLocationsResponse) MarshalJSON ¶
added in v0.74.0
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListMavenArtifactsResponse ¶
added in v0.86.0
type ListMavenArtifactsResponse struct {
	// MavenArtifacts: The maven artifacts returned.
	MavenArtifacts []*MavenArtifact `json:"mavenArtifacts,omitempty"`
	// NextPageToken: The token to retrieve the next page of artifacts, or empty if
	// there are no more artifacts to return.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "MavenArtifacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MavenArtifacts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListMavenArtifactsResponse: The response from listing maven artifacts.

func (ListMavenArtifactsResponse) MarshalJSON ¶
added in v0.86.0
func (s ListMavenArtifactsResponse) MarshalJSON() ([]byte, error)
type ListNpmPackagesResponse ¶
added in v0.86.0
type ListNpmPackagesResponse struct {
	// NextPageToken: The token to retrieve the next page of artifacts, or empty if
	// there are no more artifacts to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// NpmPackages: The npm packages returned.
	NpmPackages []*NpmPackage `json:"npmPackages,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListNpmPackagesResponse: The response from listing npm packages.

func (ListNpmPackagesResponse) MarshalJSON ¶
added in v0.86.0
func (s ListNpmPackagesResponse) MarshalJSON() ([]byte, error)
type ListPackagesResponse ¶
added in v0.66.0
type ListPackagesResponse struct {
	// NextPageToken: The token to retrieve the next page of packages, or empty if
	// there are no more packages to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Packages: The packages returned.
	Packages []*Package `json:"packages,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListPackagesResponse: The response from listing packages.

func (ListPackagesResponse) MarshalJSON ¶
added in v0.66.0
func (s ListPackagesResponse) MarshalJSON() ([]byte, error)
type ListPythonPackagesResponse ¶
added in v0.86.0
type ListPythonPackagesResponse struct {
	// NextPageToken: The token to retrieve the next page of artifacts, or empty if
	// there are no more artifacts to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// PythonPackages: The python packages returned.
	PythonPackages []*PythonPackage `json:"pythonPackages,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListPythonPackagesResponse: The response from listing python packages.

func (ListPythonPackagesResponse) MarshalJSON ¶
added in v0.86.0
func (s ListPythonPackagesResponse) MarshalJSON() ([]byte, error)
type ListRepositoriesResponse ¶
added in v0.46.0
type ListRepositoriesResponse struct {
	// NextPageToken: The token to retrieve the next page of repositories, or empty
	// if there are no more repositories to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Repositories: The repositories returned.
	Repositories []*Repository `json:"repositories,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListRepositoriesResponse: The response from listing repositories.

func (ListRepositoriesResponse) MarshalJSON ¶
added in v0.46.0
func (s ListRepositoriesResponse) MarshalJSON() ([]byte, error)
type ListRulesResponse ¶
added in v0.200.0
type ListRulesResponse struct {
	// NextPageToken: The token to retrieve the next page of rules, or empty if
	// there are no more rules to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Rules: The rules returned.
	Rules []*GoogleDevtoolsArtifactregistryV1Rule `json:"rules,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListRulesResponse: The response from listing rules.

func (ListRulesResponse) MarshalJSON ¶
added in v0.200.0
func (s ListRulesResponse) MarshalJSON() ([]byte, error)
type ListTagsResponse ¶
added in v0.66.0
type ListTagsResponse struct {
	// NextPageToken: The token to retrieve the next page of tags, or empty if
	// there are no more tags to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Tags: The tags returned.
	Tags []*Tag `json:"tags,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListTagsResponse: The response from listing tags.

func (ListTagsResponse) MarshalJSON ¶
added in v0.66.0
func (s ListTagsResponse) MarshalJSON() ([]byte, error)
type ListVersionsResponse ¶
added in v0.66.0
type ListVersionsResponse struct {
	// NextPageToken: The token to retrieve the next page of versions, or empty if
	// there are no more versions to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Versions: The versions returned.
	Versions []*Version `json:"versions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListVersionsResponse: The response from listing versions.

func (ListVersionsResponse) MarshalJSON ¶
added in v0.66.0
func (s ListVersionsResponse) MarshalJSON() ([]byte, error)
type Location ¶
added in v0.74.0
type Location struct {
	// DisplayName: The friendly name for this location, typically a nearby city
	// name. For example, "Tokyo".
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Cross-service attributes for the location. For example
	// {"cloud.googleapis.com/region": "us-east1"}
	Labels map[string]string `json:"labels,omitempty"`
	// LocationId: The canonical id for this location. For example: "us-east1".
	LocationId string `json:"locationId,omitempty"`
	// Metadata: Service-specific metadata. For example the available capacity at
	// the given location.
	Metadata googleapi.RawMessage `json:"metadata,omitempty"`
	// Name: Resource name for the location, which may vary between
	// implementations. For example:
	// "projects/example-project/locations/us-east1"
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DisplayName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Location: A resource that represents a Google Cloud location.

func (Location) MarshalJSON ¶
added in v0.74.0
func (s Location) MarshalJSON() ([]byte, error)
type MavenArtifact ¶
added in v0.86.0
type MavenArtifact struct {
	// ArtifactId: Artifact ID for the artifact.
	ArtifactId string `json:"artifactId,omitempty"`
	// CreateTime: Output only. Time the artifact was created.
	CreateTime string `json:"createTime,omitempty"`
	// GroupId: Group ID for the artifact. Example: com.google.guava
	GroupId string `json:"groupId,omitempty"`
	// Name: Required. registry_location, project_id, repository_name and
	// maven_artifact forms a unique artifact For example,
	// "projects/test-project/locations/us-west4/repositories/test-repo/mavenArtifac
	// ts/ com.google.guava:guava:31.0-jre", where "us-west4" is the
	// registry_location, "test-project" is the project_id, "test-repo" is the
	// repository_name and "com.google.guava:guava:31.0-jre" is the maven artifact.
	Name string `json:"name,omitempty"`
	// PomUri: Required. URL to access the pom file of the artifact. Example:
	// us-west4-maven.pkg.dev/test-project/test-repo/com/google/guava/guava/31.0/gua
	// va-31.0.pom
	PomUri string `json:"pomUri,omitempty"`
	// UpdateTime: Output only. Time the artifact was updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// Version: Version of this artifact.
	Version string `json:"version,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ArtifactId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ArtifactId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MavenArtifact: MavenArtifact represents a maven artifact.

func (MavenArtifact) MarshalJSON ¶
added in v0.86.0
func (s MavenArtifact) MarshalJSON() ([]byte, error)
type MavenRepository ¶
added in v0.110.0
type MavenRepository struct {
	// CustomRepository: Customer-specified remote repository.
	CustomRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository `json:"customRepository,omitempty"`
	// PublicRepository: One of the publicly available Maven repositories supported
	// by Artifact Registry.
	//
	// Possible values:
	//   "PUBLIC_REPOSITORY_UNSPECIFIED" - Unspecified repository.
	//   "MAVEN_CENTRAL" - Maven Central.
	PublicRepository string `json:"publicRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRepository") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MavenRepository: Configuration for a Maven remote repository.

func (MavenRepository) MarshalJSON ¶
added in v0.110.0
func (s MavenRepository) MarshalJSON() ([]byte, error)
type MavenRepositoryConfig ¶
added in v0.66.0
type MavenRepositoryConfig struct {
	// AllowSnapshotOverwrites: The repository with this flag will allow publishing
	// the same snapshot versions.
	AllowSnapshotOverwrites bool `json:"allowSnapshotOverwrites,omitempty"`
	// VersionPolicy: Version policy defines the versions that the registry will
	// accept.
	//
	// Possible values:
	//   "VERSION_POLICY_UNSPECIFIED" - VERSION_POLICY_UNSPECIFIED - the version
	// policy is not defined. When the version policy is not defined, no validation
	// is performed for the versions.
	//   "RELEASE" - RELEASE - repository will accept only Release versions.
	//   "SNAPSHOT" - SNAPSHOT - repository will accept only Snapshot versions.
	VersionPolicy string `json:"versionPolicy,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowSnapshotOverwrites") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowSnapshotOverwrites") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MavenRepositoryConfig: MavenRepositoryConfig is maven related repository details. Provides additional configuration details for repositories of the maven format type.

func (MavenRepositoryConfig) MarshalJSON ¶
added in v0.66.0
func (s MavenRepositoryConfig) MarshalJSON() ([]byte, error)
type NpmPackage ¶
added in v0.86.0
type NpmPackage struct {
	// CreateTime: Output only. Time the package was created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Required. registry_location, project_id, repository_name and
	// npm_package forms a unique package For example,
	// "projects/test-project/locations/us-west4/repositories/test-repo/npmPackages/
	//  npm_test:1.0.0", where "us-west4" is the registry_location, "test-project"
	// is the project_id, "test-repo" is the repository_name and npm_test:1.0.0" is
	// the npm package.
	Name string `json:"name,omitempty"`
	// PackageName: Package for the artifact.
	PackageName string `json:"packageName,omitempty"`
	// Tags: Tags attached to this package.
	Tags []string `json:"tags,omitempty"`
	// UpdateTime: Output only. Time the package was updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// Version: Version of this package.
	Version string `json:"version,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NpmPackage: NpmPackage represents an npm artifact.

func (NpmPackage) MarshalJSON ¶
added in v0.86.0
func (s NpmPackage) MarshalJSON() ([]byte, error)
type NpmRepository ¶
added in v0.110.0
type NpmRepository struct {
	// CustomRepository: Customer-specified remote repository.
	CustomRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository `json:"customRepository,omitempty"`
	// PublicRepository: One of the publicly available Npm repositories supported
	// by Artifact Registry.
	//
	// Possible values:
	//   "PUBLIC_REPOSITORY_UNSPECIFIED" - Unspecified repository.
	//   "NPMJS" - npmjs.
	PublicRepository string `json:"publicRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRepository") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NpmRepository: Configuration for a Npm remote repository.

func (NpmRepository) MarshalJSON ¶
added in v0.110.0
func (s NpmRepository) MarshalJSON() ([]byte, error)
type Operation ¶
type Operation struct {
	// Done: If the value is `false`, it means the operation is still in progress.
	// If `true`, the operation is completed, and either `error` or `response` is
	// available.
	Done bool `json:"done,omitempty"`
	// Error: The error result of the operation in case of failure or cancellation.
	Error *Status `json:"error,omitempty"`
	// Metadata: Service-specific metadata associated with the operation. It
	// typically contains progress information and common metadata such as create
	// time. Some services might not provide such metadata. Any method that returns
	// a long-running operation should document the metadata type, if any.
	Metadata googleapi.RawMessage `json:"metadata,omitempty"`
	// Name: The server-assigned name, which is only unique within the same service
	// that originally returns it. If you use the default HTTP mapping, the `name`
	// should be a resource name ending with `operations/{unique_id}`.
	Name string `json:"name,omitempty"`
	// Response: The normal, successful response of the operation. If the original
	// method returns no data on success, such as `Delete`, the response is
	// `google.protobuf.Empty`. If the original method is standard
	// `Get`/`Create`/`Update`, the response should be the resource. For other
	// methods, the response should have the type `XxxResponse`, where `Xxx` is the
	// original method name. For example, if the original method name is
	// `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
	Response googleapi.RawMessage `json:"response,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Done") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Done") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Operation: This resource represents a long-running operation that is the result of a network API call.

func (Operation) MarshalJSON ¶
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadata ¶
added in v0.75.0
type OperationMetadata struct {
}

OperationMetadata: Metadata type for longrunning-operations, currently empty.

type Package ¶
added in v0.66.0
type Package struct {
	// Annotations: Optional. Client specified annotations.
	Annotations map[string]string `json:"annotations,omitempty"`
	// CreateTime: The time when the package was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: The display name of the package.
	DisplayName string `json:"displayName,omitempty"`
	// Name: The name of the package, for example:
	// `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1`. If the
	// package ID part contains slashes, the slashes are escaped.
	Name string `json:"name,omitempty"`
	// UpdateTime: The time when the package was last updated. This includes
	// publishing a new version of the package.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Annotations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Annotations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Package: Packages are named collections of versions.

func (Package) MarshalJSON ¶
added in v0.66.0
func (s Package) MarshalJSON() ([]byte, error)
type Policy ¶
added in v0.66.0
type Policy struct {
	// Bindings: Associates a list of `members`, or principals, with a `role`.
	// Optionally, may specify a `condition` that determines how and when the
	// `bindings` are applied. Each of the `bindings` must contain at least one
	// principal. The `bindings` in a `Policy` can refer to up to 1,500 principals;
	// up to 250 of these principals can be Google groups. Each occurrence of a
	// principal counts towards these limits. For example, if the `bindings` grant
	// 50 different roles to `user:alice@example.com`, and not to any other
	// principal, then you can add another 1,450 principals to the `bindings` in
	// the `Policy`.
	Bindings []*Binding `json:"bindings,omitempty"`
	// Etag: `etag` is used for optimistic concurrency control as a way to help
	// prevent simultaneous updates of a policy from overwriting each other. It is
	// strongly suggested that systems make use of the `etag` in the
	// read-modify-write cycle to perform policy updates in order to avoid race
	// conditions: An `etag` is returned in the response to `getIamPolicy`, and
	// systems are expected to put that etag in the request to `setIamPolicy` to
	// ensure that their change will be applied to the same version of the policy.
	// **Important:** If you use IAM Conditions, you must include the `etag` field
	// whenever you call `setIamPolicy`. If you omit this field, then IAM allows
	// you to overwrite a version `3` policy with a version `1` policy, and all of
	// the conditions in the version `3` policy are lost.
	Etag string `json:"etag,omitempty"`
	// Version: Specifies the format of the policy. Valid values are `0`, `1`, and
	// `3`. Requests that specify an invalid value are rejected. Any operation that
	// affects conditional role bindings must specify version `3`. This requirement
	// applies to the following operations: * Getting a policy that includes a
	// conditional role binding * Adding a conditional role binding to a policy *
	// Changing a conditional role binding in a policy * Removing any role binding,
	// with or without a condition, from a policy that includes conditions
	// **Important:** If you use IAM Conditions, you must include the `etag` field
	// whenever you call `setIamPolicy`. If you omit this field, then IAM allows
	// you to overwrite a version `3` policy with a version `1` policy, and all of
	// the conditions in the version `3` policy are lost. If a policy does not
	// include any conditions, operations on that policy may specify any valid
	// version or leave the field unset. To learn which resources support
	// conditions in their IAM policies, see the IAM documentation
	// (https://cloud.google.com/iam/help/conditions/resource-policies).
	Version int64 `json:"version,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Bindings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Bindings") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** ``` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } ``` **YAML example:** ``` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 ``` For a description of IAM and its features, see the IAM documentation (https://cloud.google.com/iam/docs/).

func (Policy) MarshalJSON ¶
added in v0.66.0
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectSettings ¶
added in v0.66.0
type ProjectSettings struct {
	// LegacyRedirectionState: The redirection state of the legacy repositories in
	// this project.
	//
	// Possible values:
	//   "REDIRECTION_STATE_UNSPECIFIED" - No redirection status has been set.
	//   "REDIRECTION_FROM_GCR_IO_DISABLED" - Redirection is disabled.
	//   "REDIRECTION_FROM_GCR_IO_ENABLED" - Redirection is enabled.
	//   "REDIRECTION_FROM_GCR_IO_FINALIZED" - Redirection is enabled, and has been
	// finalized so cannot be reverted.
	//   "REDIRECTION_FROM_GCR_IO_ENABLED_AND_COPYING" - Redirection is enabled and
	// missing images are copied from GCR
	//   "REDIRECTION_FROM_GCR_IO_PARTIAL_AND_COPYING" - Redirection is partially
	// enabled and missing images are copied from GCR
	LegacyRedirectionState string `json:"legacyRedirectionState,omitempty"`
	// Name: The name of the project's settings. Always of the form:
	// projects/{project-id}/projectSettings In update request: never set In
	// response: always set
	Name string `json:"name,omitempty"`
	// PullPercent: The percentage of pull traffic to redirect from GCR to AR when
	// using partial redirection.
	PullPercent int64 `json:"pullPercent,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "LegacyRedirectionState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LegacyRedirectionState") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProjectSettings: The Artifact Registry settings that apply to a Project.

func (ProjectSettings) MarshalJSON ¶
added in v0.66.0
func (s ProjectSettings) MarshalJSON() ([]byte, error)
type ProjectsGetProjectSettingsCall ¶
added in v0.66.0
type ProjectsGetProjectSettingsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsGetProjectSettingsCall) Context ¶
added in v0.66.0
func (c *ProjectsGetProjectSettingsCall) Context(ctx context.Context) *ProjectsGetProjectSettingsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsGetProjectSettingsCall) Do ¶
added in v0.66.0
func (c *ProjectsGetProjectSettingsCall) Do(opts ...googleapi.CallOption) (*ProjectSettings, error)

Do executes the "artifactregistry.projects.getProjectSettings" call. Any non-2xx status code is an error. Response headers are in either *ProjectSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsGetProjectSettingsCall) Fields ¶
added in v0.66.0
func (c *ProjectsGetProjectSettingsCall) Fields(s ...googleapi.Field) *ProjectsGetProjectSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsGetProjectSettingsCall) Header ¶
added in v0.66.0
func (c *ProjectsGetProjectSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsGetProjectSettingsCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsGetProjectSettingsCall) IfNoneMatch(entityTag string) *ProjectsGetProjectSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsGetCall ¶
added in v0.74.0
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
added in v0.74.0
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
added in v0.74.0
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "artifactregistry.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
added in v0.74.0
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
added in v0.74.0
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
added in v0.74.0
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsGetVpcscConfigCall ¶
added in v0.110.0
type ProjectsLocationsGetVpcscConfigCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetVpcscConfigCall) Context ¶
added in v0.110.0
func (c *ProjectsLocationsGetVpcscConfigCall) Context(ctx context.Context) *ProjectsLocationsGetVpcscConfigCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetVpcscConfigCall) Do ¶
added in v0.110.0
func (c *ProjectsLocationsGetVpcscConfigCall) Do(opts ...googleapi.CallOption) (*VPCSCConfig, error)

Do executes the "artifactregistry.projects.locations.getVpcscConfig" call. Any non-2xx status code is an error. Response headers are in either *VPCSCConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetVpcscConfigCall) Fields ¶
added in v0.110.0
func (c *ProjectsLocationsGetVpcscConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetVpcscConfigCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetVpcscConfigCall) Header ¶
added in v0.110.0
func (c *ProjectsLocationsGetVpcscConfigCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetVpcscConfigCall) IfNoneMatch ¶
added in v0.110.0
func (c *ProjectsLocationsGetVpcscConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetVpcscConfigCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall ¶
added in v0.74.0
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "artifactregistry.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
added in v0.232.0
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

func (*ProjectsLocationsListCall) Fields ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsListCall) Filter ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 (https://google.aip.dev/160).

func (*ProjectsLocationsListCall) Header ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsListCall) IfNoneMatch ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsListCall) PageSize ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

func (*ProjectsLocationsListCall) PageToken ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

func (*ProjectsLocationsListCall) Pages ¶
added in v0.74.0
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsGetCall ¶
added in v0.70.0
type ProjectsLocationsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsGetCall) Context ¶
added in v0.70.0
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsGetCall) Do ¶
added in v0.70.0
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsGetCall) Fields ¶
added in v0.70.0
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsGetCall) Header ¶
added in v0.70.0
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsGetCall) IfNoneMatch ¶
added in v0.70.0
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsService ¶
added in v0.70.0
type ProjectsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOperationsService ¶
added in v0.70.0
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (*ProjectsLocationsOperationsService) Get ¶
added in v0.70.0
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

type ProjectsLocationsRepositoriesAptArtifactsImportCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesAptArtifactsImportCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesAptArtifactsImportCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAptArtifactsImportCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesAptArtifactsImportCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.aptArtifacts.import" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesAptArtifactsImportCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAptArtifactsImportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesAptArtifactsImportCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesAptArtifactsImportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesAptArtifactsService ¶
added in v0.66.0
type ProjectsLocationsRepositoriesAptArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesAptArtifactsService ¶
added in v0.66.0
func NewProjectsLocationsRepositoriesAptArtifactsService(s *Service) *ProjectsLocationsRepositoriesAptArtifactsService
func (*ProjectsLocationsRepositoriesAptArtifactsService) Import ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesAptArtifactsService) Import(parent string, importaptartifactsrequest *ImportAptArtifactsRequest) *ProjectsLocationsRepositoriesAptArtifactsImportCall

Import: Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

parent: The name of the parent resource where the artifacts will be imported.
func (*ProjectsLocationsRepositoriesAptArtifactsService) Upload ¶
added in v0.68.0
func (r *ProjectsLocationsRepositoriesAptArtifactsService) Upload(parent string, uploadaptartifactrequest *UploadAptArtifactRequest) *ProjectsLocationsRepositoriesAptArtifactsUploadCall

Upload: Directly uploads an Apt artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored.

parent: The name of the parent resource where the artifacts will be uploaded.
type ProjectsLocationsRepositoriesAptArtifactsUploadCall ¶
added in v0.68.0
type ProjectsLocationsRepositoriesAptArtifactsUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall) Context ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAptArtifactsUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall) Do ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadAptArtifactMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.aptArtifacts.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadAptArtifactMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall) Fields ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAptArtifactsUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall) Header ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall) Media ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesAptArtifactsUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall) ProgressUpdater ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesAptArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesAptArtifactsUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesAptArtifactsUploadCall)
ResumableMedia
DEPRECATED
added in v0.68.0
type ProjectsLocationsRepositoriesAttachmentsCreateCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesAttachmentsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesAttachmentsCreateCall) AttachmentId ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) AttachmentId(attachmentId string) *ProjectsLocationsRepositoriesAttachmentsCreateCall

AttachmentId sets the optional parameter "attachmentId": Required. The attachment id to use for this attachment.

func (*ProjectsLocationsRepositoriesAttachmentsCreateCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesAttachmentsCreateCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.attachments.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesAttachmentsCreateCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesAttachmentsCreateCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesAttachmentsDeleteCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesAttachmentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesAttachmentsDeleteCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesAttachmentsDeleteCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.attachments.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesAttachmentsDeleteCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesAttachmentsDeleteCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesAttachmentsGetCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesAttachmentsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesAttachmentsGetCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesAttachmentsGetCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Do(opts ...googleapi.CallOption) (*Attachment, error)

Do executes the "artifactregistry.projects.locations.repositories.attachments.get" call. Any non-2xx status code is an error. Response headers are in either *Attachment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesAttachmentsGetCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesAttachmentsGetCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesAttachmentsGetCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesAttachmentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesAttachmentsListCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesAttachmentsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesAttachmentsListCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesAttachmentsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Do(opts ...googleapi.CallOption) (*ListAttachmentsResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.attachments.list" call. Any non-2xx status code is an error. Response headers are in either *ListAttachmentsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesAttachmentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) Filter ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Filter(filter string) *ProjectsLocationsRepositoriesAttachmentsListCall

Filter sets the optional parameter "filter": An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * `target` * `type` * `attachment_namespace`

func (*ProjectsLocationsRepositoriesAttachmentsListCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesAttachmentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) PageSize ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesAttachmentsListCall

PageSize sets the optional parameter "pageSize": The maximum number of attachments to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) PageToken ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesAttachmentsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesAttachmentsListCall) Pages ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesAttachmentsListCall) Pages(ctx context.Context, f func(*ListAttachmentsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesAttachmentsService ¶
added in v0.200.0
type ProjectsLocationsRepositoriesAttachmentsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesAttachmentsService ¶
added in v0.200.0
func NewProjectsLocationsRepositoriesAttachmentsService(s *Service) *ProjectsLocationsRepositoriesAttachmentsService
func (*ProjectsLocationsRepositoriesAttachmentsService) Create ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesAttachmentsService) Create(parent string, attachment *Attachment) *ProjectsLocationsRepositoriesAttachmentsCreateCall

Create: Creates an attachment. The returned Operation will finish once the attachment has been created. Its response will be the created attachment.

parent: The name of the parent resource where the attachment will be created.
func (*ProjectsLocationsRepositoriesAttachmentsService) Delete ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesAttachmentsService) Delete(name string) *ProjectsLocationsRepositoriesAttachmentsDeleteCall

Delete: Deletes an attachment. The returned Operation will finish once the attachments has been deleted. It will not have any Operation metadata and will return a `google.protobuf.Empty` response.

- name: The name of the attachment to delete.

func (*ProjectsLocationsRepositoriesAttachmentsService) Get ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesAttachmentsService) Get(name string) *ProjectsLocationsRepositoriesAttachmentsGetCall

Get: Gets an attachment.

- name: The name of the attachment to retrieve.

func (*ProjectsLocationsRepositoriesAttachmentsService) List ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesAttachmentsService) List(parent string) *ProjectsLocationsRepositoriesAttachmentsListCall

List: Lists attachments.

- parent: The name of the parent resource whose attachments will be listed.

type ProjectsLocationsRepositoriesCreateCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesCreateCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesCreateCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesCreateCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesCreateCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesCreateCall) RepositoryId ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesCreateCall) RepositoryId(repositoryId string) *ProjectsLocationsRepositoriesCreateCall

RepositoryId sets the optional parameter "repositoryId": Required. The repository id to use for this repository.

type ProjectsLocationsRepositoriesDeleteCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesDeleteCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesDeleteCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesDeleteCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesDeleteCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesDockerImagesGetCall ¶
added in v0.61.0
type ProjectsLocationsRepositoriesDockerImagesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesDockerImagesGetCall) Context ¶
added in v0.61.0
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesDockerImagesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesDockerImagesGetCall) Do ¶
added in v0.61.0
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Do(opts ...googleapi.CallOption) (*DockerImage, error)

Do executes the "artifactregistry.projects.locations.repositories.dockerImages.get" call. Any non-2xx status code is an error. Response headers are in either *DockerImage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesDockerImagesGetCall) Fields ¶
added in v0.61.0
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesDockerImagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesDockerImagesGetCall) Header ¶
added in v0.61.0
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesDockerImagesGetCall) IfNoneMatch ¶
added in v0.61.0
func (c *ProjectsLocationsRepositoriesDockerImagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesDockerImagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesDockerImagesListCall ¶
added in v0.41.0
type ProjectsLocationsRepositoriesDockerImagesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesDockerImagesListCall) Context ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesDockerImagesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) Do ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Do(opts ...googleapi.CallOption) (*ListDockerImagesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.dockerImages.list" call. Any non-2xx status code is an error. Response headers are in either *ListDockerImagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) Fields ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesDockerImagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) Header ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) IfNoneMatch ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesDockerImagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) OrderBy ¶
added in v0.93.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesDockerImagesListCall

OrderBy sets the optional parameter "orderBy": The field to order the results by.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) PageSize ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesDockerImagesListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) PageToken ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesDockerImagesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesDockerImagesListCall) Pages ¶
added in v0.41.0
func (c *ProjectsLocationsRepositoriesDockerImagesListCall) Pages(ctx context.Context, f func(*ListDockerImagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesDockerImagesService ¶
added in v0.41.0
type ProjectsLocationsRepositoriesDockerImagesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesDockerImagesService ¶
added in v0.41.0
func NewProjectsLocationsRepositoriesDockerImagesService(s *Service) *ProjectsLocationsRepositoriesDockerImagesService
func (*ProjectsLocationsRepositoriesDockerImagesService) Get ¶
added in v0.61.0
func (r *ProjectsLocationsRepositoriesDockerImagesService) Get(name string) *ProjectsLocationsRepositoriesDockerImagesGetCall

Get: Gets a docker image.

- name: The name of the docker images.

func (*ProjectsLocationsRepositoriesDockerImagesService) List ¶
added in v0.41.0
func (r *ProjectsLocationsRepositoriesDockerImagesService) List(parent string) *ProjectsLocationsRepositoriesDockerImagesListCall

List: Lists docker images.

parent: The name of the parent resource whose docker images will be listed.
type ProjectsLocationsRepositoriesExportArtifactCall ¶
added in v0.255.0
type ProjectsLocationsRepositoriesExportArtifactCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesExportArtifactCall) Context ¶
added in v0.255.0
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesExportArtifactCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesExportArtifactCall) Do ¶
added in v0.255.0
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.exportArtifact" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesExportArtifactCall) Fields ¶
added in v0.255.0
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesExportArtifactCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesExportArtifactCall) Header ¶
added in v0.255.0
func (c *ProjectsLocationsRepositoriesExportArtifactCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesFilesDeleteCall ¶
added in v0.182.0
type ProjectsLocationsRepositoriesFilesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesFilesDeleteCall) Context ¶
added in v0.182.0
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesFilesDeleteCall) Do ¶
added in v0.182.0
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.files.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesFilesDeleteCall) Fields ¶
added in v0.182.0
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesFilesDeleteCall) Header ¶
added in v0.182.0
func (c *ProjectsLocationsRepositoriesFilesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesFilesDownloadCall ¶
added in v0.178.0
type ProjectsLocationsRepositoriesFilesDownloadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesFilesDownloadCall) Context ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesDownloadCall

Context sets the context to be used in this call's Do and Download methods.

func (*ProjectsLocationsRepositoriesFilesDownloadCall) Do ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Do(opts ...googleapi.CallOption) (*DownloadFileResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.files.download" call. Any non-2xx status code is an error. Response headers are in either *DownloadFileResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesFilesDownloadCall) Download ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Download(opts ...googleapi.CallOption) (*http.Response, error)

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

func (*ProjectsLocationsRepositoriesFilesDownloadCall) Fields ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesDownloadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesFilesDownloadCall) Header ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesFilesDownloadCall) IfNoneMatch ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesFilesDownloadCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesFilesDownloadCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesFilesGetCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesFilesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesFilesGetCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesFilesGetCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesGetCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1File, error)

Do executes the "artifactregistry.projects.locations.repositories.files.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleDevtoolsArtifactregistryV1File.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesFilesGetCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesFilesGetCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesFilesGetCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesFilesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesFilesListCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesFilesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesFilesListCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesFilesListCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) Do(opts ...googleapi.CallOption) (*ListFilesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.files.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesFilesListCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesFilesListCall) Filter ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) Filter(filter string) *ProjectsLocationsRepositoriesFilesListCall

Filter sets the optional parameter "filter": An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * `name` * `owner` * `annotations` Examples of using a filter: To filter the results of your request to files with the name `my_file.txt` in project `my-project` in the `us-central` region, in repository `my-repo`, append the following filter expression to your request: * `name="projects/my-project/locations/us-central1/repositories/my-repo/files/m y-file.txt" You can also use wildcards to match any number of characters before or after the value: * `name="projects/my-project/locations/us-central1/repositories/my-repo/files/m y-*" * `name="projects/my-project/locations/us-central1/repositories/my-repo/files/* file.txt" * `name="projects/my-project/locations/us-central1/repositories/my-repo/files/* file*" To filter the results of your request to files owned by the version `1.0` in package `pkg1`, append the following filter expression to your request: * `owner="projects/my-project/locations/us-central1/repositories/my-repo/packag es/my-package/versions/1.0" To filter the results of your request to files with the annotation key-value pair [`external_link`: `external_link_value`], append the following filter expression to your request: * "annotations.external_link:external_link_value" To filter just for a specific annotation key `external_link`, append the following filter expression to your request: * "annotations.external_link" If the annotation key or value contains special characters, you can escape them by surrounding the value with backticks. For example, to filter the results of your request to files with the annotation key-value pair [`external.link`:`https://example.com/my-file`], append the following filter expression to your request: * “ "annotations.`external.link`:`https://example.com/my-file" “ You can also filter with annotations with a wildcard to match any number of characters before or after the value: * “ "annotations.*_link:`*example.com*" “

func (*ProjectsLocationsRepositoriesFilesListCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesFilesListCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesFilesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesFilesListCall) OrderBy ¶
added in v0.70.0
func (c *ProjectsLocationsRepositoriesFilesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesFilesListCall

OrderBy sets the optional parameter "orderBy": The field to order the results by.

func (*ProjectsLocationsRepositoriesFilesListCall) PageSize ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesFilesListCall

PageSize sets the optional parameter "pageSize": The maximum number of files to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesFilesListCall) PageToken ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesFilesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesFilesListCall) Pages ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesFilesListCall) Pages(ctx context.Context, f func(*ListFilesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesFilesPatchCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesFilesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesFilesPatchCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesFilesPatchCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1File, error)

Do executes the "artifactregistry.projects.locations.repositories.files.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleDevtoolsArtifactregistryV1File.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesFilesPatchCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesFilesPatchCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesFilesPatchCall) UpdateMask ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesFilesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

type ProjectsLocationsRepositoriesFilesService ¶
added in v0.66.0
type ProjectsLocationsRepositoriesFilesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesFilesService ¶
added in v0.66.0
func NewProjectsLocationsRepositoriesFilesService(s *Service) *ProjectsLocationsRepositoriesFilesService
func (*ProjectsLocationsRepositoriesFilesService) Delete ¶
added in v0.182.0
func (r *ProjectsLocationsRepositoriesFilesService) Delete(name string) *ProjectsLocationsRepositoriesFilesDeleteCall

Delete: Deletes a file and all of its content. It is only allowed on generic repositories. The returned operation will complete once the file has been deleted.

- name: The name of the file to delete.

func (*ProjectsLocationsRepositoriesFilesService) Download ¶
added in v0.178.0
func (r *ProjectsLocationsRepositoriesFilesService) Download(name string) *ProjectsLocationsRepositoriesFilesDownloadCall

Download: Download a file.

- name: The name of the file to download.

func (*ProjectsLocationsRepositoriesFilesService) Get ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesFilesService) Get(name string) *ProjectsLocationsRepositoriesFilesGetCall

Get: Gets a file.

- name: The name of the file to retrieve.

func (*ProjectsLocationsRepositoriesFilesService) List ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesFilesService) List(parent string) *ProjectsLocationsRepositoriesFilesListCall

List: Lists files.

parent: The name of the repository whose files will be listed. For example: "projects/p1/locations/us-central1/repositories/repo1.
func (*ProjectsLocationsRepositoriesFilesService) Patch ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesFilesService) Patch(name string, googledevtoolsartifactregistryv1file *GoogleDevtoolsArtifactregistryV1File) *ProjectsLocationsRepositoriesFilesPatchCall

Patch: Updates a file.

name: The name of the file, for example: `projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt`. If the file ID part contains slashes, they are escaped.
func (*ProjectsLocationsRepositoriesFilesService) Upload ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesFilesService) Upload(parent string, uploadfilerequest *UploadFileRequest) *ProjectsLocationsRepositoriesFilesUploadCall

Upload: Directly uploads a file to a repository. The returned Operation will complete once the resources are uploaded.

parent: The resource name of the repository where the file will be uploaded.
type ProjectsLocationsRepositoriesFilesUploadCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesFilesUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesFilesUploadCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesFilesUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesFilesUploadCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Do(opts ...googleapi.CallOption) (*UploadFileMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.files.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadFileMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesFilesUploadCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesFilesUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesFilesUploadCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesFilesUploadCall) Media ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesFilesUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesFilesUploadCall) ProgressUpdater ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesFilesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesFilesUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesFilesUploadCall)
ResumableMedia
DEPRECATED
added in v0.200.0
type ProjectsLocationsRepositoriesGenericArtifactsService ¶
added in v0.178.0
type ProjectsLocationsRepositoriesGenericArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesGenericArtifactsService ¶
added in v0.178.0
func NewProjectsLocationsRepositoriesGenericArtifactsService(s *Service) *ProjectsLocationsRepositoriesGenericArtifactsService
func (*ProjectsLocationsRepositoriesGenericArtifactsService) Upload ¶
added in v0.178.0
func (r *ProjectsLocationsRepositoriesGenericArtifactsService) Upload(parent string, uploadgenericartifactrequest *UploadGenericArtifactRequest) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall

Upload: Directly uploads a Generic artifact. The returned operation will complete once the resources are uploaded. Package, version, and file resources are created based on the uploaded artifact. Uploaded artifacts that conflict with existing resources will raise an `ALREADY_EXISTS` error.

parent: The resource name of the repository where the generic artifact will be uploaded.
type ProjectsLocationsRepositoriesGenericArtifactsUploadCall ¶
added in v0.178.0
type ProjectsLocationsRepositoriesGenericArtifactsUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Context ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Do ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadGenericArtifactMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.genericArtifacts.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadGenericArtifactMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Fields ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Header ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Media ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall) ProgressUpdater ¶
added in v0.178.0
func (c *ProjectsLocationsRepositoriesGenericArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesGenericArtifactsUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesGenericArtifactsUploadCall)
ResumableMedia
DEPRECATED
added in v0.178.0
type ProjectsLocationsRepositoriesGetCall ¶
added in v0.46.0
type ProjectsLocationsRepositoriesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesGetCall) Context ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesGetCall) Do ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesGetCall) Do(opts ...googleapi.CallOption) (*Repository, error)

Do executes the "artifactregistry.projects.locations.repositories.get" call. Any non-2xx status code is an error. Response headers are in either *Repository.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesGetCall) Fields ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesGetCall) Header ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesGetCall) IfNoneMatch ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesGetIamPolicyCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesGetIamPolicyCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesGetIamPolicyCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "artifactregistry.projects.locations.repositories.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesGetIamPolicyCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesGetIamPolicyCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesGetIamPolicyCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsRepositoriesGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsRepositoriesGoModulesService ¶
added in v0.129.0
type ProjectsLocationsRepositoriesGoModulesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesGoModulesService ¶
added in v0.129.0
func NewProjectsLocationsRepositoriesGoModulesService(s *Service) *ProjectsLocationsRepositoriesGoModulesService
func (*ProjectsLocationsRepositoriesGoModulesService) Upload ¶
added in v0.129.0
func (r *ProjectsLocationsRepositoriesGoModulesService) Upload(parent string, uploadgomodulerequest *UploadGoModuleRequest) *ProjectsLocationsRepositoriesGoModulesUploadCall

Upload: Directly uploads a Go module. The returned Operation will complete once the Go module is uploaded. Package, Version, and File resources are created based on the uploaded Go module.

parent: The resource name of the repository where the Go module will be uploaded.
type ProjectsLocationsRepositoriesGoModulesUploadCall ¶
added in v0.129.0
type ProjectsLocationsRepositoriesGoModulesUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesGoModulesUploadCall) Context ¶
added in v0.129.0
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGoModulesUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesGoModulesUploadCall) Do ¶
added in v0.129.0
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Do(opts ...googleapi.CallOption) (*UploadGoModuleMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.goModules.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadGoModuleMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesGoModulesUploadCall) Fields ¶
added in v0.129.0
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGoModulesUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesGoModulesUploadCall) Header ¶
added in v0.129.0
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesGoModulesUploadCall) Media ¶
added in v0.129.0
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesGoModulesUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesGoModulesUploadCall) ProgressUpdater ¶
added in v0.129.0
func (c *ProjectsLocationsRepositoriesGoModulesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesGoModulesUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesGoModulesUploadCall)
ResumableMedia
DEPRECATED
added in v0.129.0
type ProjectsLocationsRepositoriesGoogetArtifactsImportCall ¶
added in v0.122.0
type ProjectsLocationsRepositoriesGoogetArtifactsImportCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Context ¶
added in v0.122.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGoogetArtifactsImportCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Do ¶
added in v0.122.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.googetArtifacts.import" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Fields ¶
added in v0.122.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGoogetArtifactsImportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Header ¶
added in v0.122.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsImportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesGoogetArtifactsService ¶
added in v0.68.0
type ProjectsLocationsRepositoriesGoogetArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesGoogetArtifactsService ¶
added in v0.68.0
func NewProjectsLocationsRepositoriesGoogetArtifactsService(s *Service) *ProjectsLocationsRepositoriesGoogetArtifactsService
func (*ProjectsLocationsRepositoriesGoogetArtifactsService) Import ¶
added in v0.122.0
func (r *ProjectsLocationsRepositoriesGoogetArtifactsService) Import(parent string, importgoogetartifactsrequest *ImportGoogetArtifactsRequest) *ProjectsLocationsRepositoriesGoogetArtifactsImportCall

Import: Imports GooGet artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

parent: The name of the parent resource where the artifacts will be imported.
func (*ProjectsLocationsRepositoriesGoogetArtifactsService) Upload ¶
added in v0.68.0
func (r *ProjectsLocationsRepositoriesGoogetArtifactsService) Upload(parent string, uploadgoogetartifactrequest *UploadGoogetArtifactRequest) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall

Upload: Directly uploads a GooGet artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored.

parent: The name of the parent resource where the artifacts will be uploaded.
type ProjectsLocationsRepositoriesGoogetArtifactsUploadCall ¶
added in v0.68.0
type ProjectsLocationsRepositoriesGoogetArtifactsUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Context ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Do ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadGoogetArtifactMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.googetArtifacts.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadGoogetArtifactMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Fields ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Header ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Media ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) ProgressUpdater ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesGoogetArtifactsUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesGoogetArtifactsUploadCall)
ResumableMedia
DEPRECATED
added in v0.68.0
type ProjectsLocationsRepositoriesKfpArtifactsService ¶
added in v0.98.0
type ProjectsLocationsRepositoriesKfpArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesKfpArtifactsService ¶
added in v0.98.0
func NewProjectsLocationsRepositoriesKfpArtifactsService(s *Service) *ProjectsLocationsRepositoriesKfpArtifactsService
func (*ProjectsLocationsRepositoriesKfpArtifactsService) Upload ¶
added in v0.98.0
func (r *ProjectsLocationsRepositoriesKfpArtifactsService) Upload(parent string, uploadkfpartifactrequest *UploadKfpArtifactRequest) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall

Upload: Directly uploads a KFP artifact. The returned Operation will complete once the resource is uploaded. Package, Version, and File resources will be created based on the uploaded artifact. Uploaded artifacts that conflict with existing resources will be overwritten.

parent: The resource name of the repository where the KFP artifact will be uploaded.
type ProjectsLocationsRepositoriesKfpArtifactsUploadCall ¶
added in v0.98.0
type ProjectsLocationsRepositoriesKfpArtifactsUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Context ¶
added in v0.98.0
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Do ¶
added in v0.98.0
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadKfpArtifactMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.kfpArtifacts.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadKfpArtifactMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Fields ¶
added in v0.98.0
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Header ¶
added in v0.98.0
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Media ¶
added in v0.98.0
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall) ProgressUpdater ¶
added in v0.98.0
func (c *ProjectsLocationsRepositoriesKfpArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesKfpArtifactsUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesKfpArtifactsUploadCall)
ResumableMedia
DEPRECATED
added in v0.98.0
type ProjectsLocationsRepositoriesListCall ¶
added in v0.46.0
type ProjectsLocationsRepositoriesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesListCall) Context ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesListCall) Do ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) Do(opts ...googleapi.CallOption) (*ListRepositoriesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.list" call. Any non-2xx status code is an error. Response headers are in either *ListRepositoriesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesListCall) Fields ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesListCall) Filter ¶
added in v0.195.0
func (c *ProjectsLocationsRepositoriesListCall) Filter(filter string) *ProjectsLocationsRepositoriesListCall

Filter sets the optional parameter "filter": An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * `name` Examples of using a filter: To filter the results of your request to repositories with the name `my-repo` in project `my-project` in the `us-central` region, append the following filter expression to your request: * `name="projects/my-project/locations/us-central1/repositories/my-repo" You can also use wildcards to match any number of characters before or after the value: * `name="projects/my-project/locations/us-central1/repositories/my-*" * `name="projects/my-project/locations/us-central1/repositories/*repo" * `name="projects/my-project/locations/us-central1/repositories/*repo*"

func (*ProjectsLocationsRepositoriesListCall) Header ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesListCall) IfNoneMatch ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesListCall) OrderBy ¶
added in v0.195.0
func (c *ProjectsLocationsRepositoriesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesListCall

OrderBy sets the optional parameter "orderBy": The field to order the results by.

func (*ProjectsLocationsRepositoriesListCall) PageSize ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesListCall

PageSize sets the optional parameter "pageSize": The maximum number of repositories to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesListCall) PageToken ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesListCall) Pages ¶
added in v0.46.0
func (c *ProjectsLocationsRepositoriesListCall) Pages(ctx context.Context, f func(*ListRepositoriesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesMavenArtifactsGetCall ¶
added in v0.86.0
type ProjectsLocationsRepositoriesMavenArtifactsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesMavenArtifactsGetCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesMavenArtifactsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesMavenArtifactsGetCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Do(opts ...googleapi.CallOption) (*MavenArtifact, error)

Do executes the "artifactregistry.projects.locations.repositories.mavenArtifacts.get" call. Any non-2xx status code is an error. Response headers are in either *MavenArtifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesMavenArtifactsGetCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesMavenArtifactsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesMavenArtifactsGetCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesMavenArtifactsGetCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesMavenArtifactsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesMavenArtifactsListCall ¶
added in v0.86.0
type ProjectsLocationsRepositoriesMavenArtifactsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesMavenArtifactsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListMavenArtifactsResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.mavenArtifacts.list" call. Any non-2xx status code is an error. Response headers are in either *ListMavenArtifactsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesMavenArtifactsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesMavenArtifactsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) PageSize ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesMavenArtifactsListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) PageToken ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesMavenArtifactsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesMavenArtifactsListCall) Pages ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesMavenArtifactsListCall) Pages(ctx context.Context, f func(*ListMavenArtifactsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesMavenArtifactsService ¶
added in v0.86.0
type ProjectsLocationsRepositoriesMavenArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesMavenArtifactsService ¶
added in v0.86.0
func NewProjectsLocationsRepositoriesMavenArtifactsService(s *Service) *ProjectsLocationsRepositoriesMavenArtifactsService
func (*ProjectsLocationsRepositoriesMavenArtifactsService) Get ¶
added in v0.86.0
func (r *ProjectsLocationsRepositoriesMavenArtifactsService) Get(name string) *ProjectsLocationsRepositoriesMavenArtifactsGetCall

Get: Gets a maven artifact.

- name: The name of the maven artifact.

func (*ProjectsLocationsRepositoriesMavenArtifactsService) List ¶
added in v0.86.0
func (r *ProjectsLocationsRepositoriesMavenArtifactsService) List(parent string) *ProjectsLocationsRepositoriesMavenArtifactsListCall

List: Lists maven artifacts.

parent: The name of the parent resource whose maven artifacts will be listed.
type ProjectsLocationsRepositoriesNpmPackagesGetCall ¶
added in v0.86.0
type ProjectsLocationsRepositoriesNpmPackagesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesNpmPackagesGetCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesNpmPackagesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesNpmPackagesGetCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Do(opts ...googleapi.CallOption) (*NpmPackage, error)

Do executes the "artifactregistry.projects.locations.repositories.npmPackages.get" call. Any non-2xx status code is an error. Response headers are in either *NpmPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesNpmPackagesGetCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesNpmPackagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesNpmPackagesGetCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesNpmPackagesGetCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesNpmPackagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesNpmPackagesListCall ¶
added in v0.86.0
type ProjectsLocationsRepositoriesNpmPackagesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesNpmPackagesListCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesNpmPackagesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Do(opts ...googleapi.CallOption) (*ListNpmPackagesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.npmPackages.list" call. Any non-2xx status code is an error. Response headers are in either *ListNpmPackagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesNpmPackagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesNpmPackagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) PageSize ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesNpmPackagesListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) PageToken ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesNpmPackagesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesNpmPackagesListCall) Pages ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesNpmPackagesListCall) Pages(ctx context.Context, f func(*ListNpmPackagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesNpmPackagesService ¶
added in v0.86.0
type ProjectsLocationsRepositoriesNpmPackagesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesNpmPackagesService ¶
added in v0.86.0
func NewProjectsLocationsRepositoriesNpmPackagesService(s *Service) *ProjectsLocationsRepositoriesNpmPackagesService
func (*ProjectsLocationsRepositoriesNpmPackagesService) Get ¶
added in v0.86.0
func (r *ProjectsLocationsRepositoriesNpmPackagesService) Get(name string) *ProjectsLocationsRepositoriesNpmPackagesGetCall

Get: Gets a npm package.

- name: The name of the npm package.

func (*ProjectsLocationsRepositoriesNpmPackagesService) List ¶
added in v0.86.0
func (r *ProjectsLocationsRepositoriesNpmPackagesService) List(parent string) *ProjectsLocationsRepositoriesNpmPackagesListCall

List: Lists npm packages.

- parent: The name of the parent resource whose npm packages will be listed.

type ProjectsLocationsRepositoriesPackagesDeleteCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesDeleteCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesDeleteCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesDeleteCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesDeleteCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesPackagesGetCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesGetCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesGetCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Do(opts ...googleapi.CallOption) (*Package, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.get" call. Any non-2xx status code is an error. Response headers are in either *Package.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesGetCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesGetCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesGetCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesPackagesListCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesListCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesListCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) Do(opts ...googleapi.CallOption) (*ListPackagesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.list" call. Any non-2xx status code is an error. Response headers are in either *ListPackagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesListCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesListCall) Filter ¶
added in v0.195.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) Filter(filter string) *ProjectsLocationsRepositoriesPackagesListCall

Filter sets the optional parameter "filter": An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * `name` * `annotations` Examples of using a filter: To filter the results of your request to packages with the name `my-package` in project `my-project` in the `us-central` region, in repository `my-repo`, append the following filter expression to your request: * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package" You can also use wildcards to match any number of characters before or after the value: * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-*" * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/*package" * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/*pack*" To filter the results of your request to packages with the annotation key-value pair [`external_link`: `external_link_value`], append the following filter expression to your request": * "annotations.external_link:external_link_value" To filter the results just for a specific annotation key `external_link`, append the following filter expression to your request: * "annotations.external_link" If the annotation key or value contains special characters, you can escape them by surrounding the value with backticks. For example, to filter the results of your request to packages with the annotation key-value pair [`external.link`:`https://example.com/my-package`], append the following filter expression to your request: * “ "annotations.`external.link`:`https://example.com/my-package" “ You can also filter with annotations with a wildcard to match any number of characters before or after the value: * “ "annotations.*_link:`*example.com*" “

func (*ProjectsLocationsRepositoriesPackagesListCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesListCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesPackagesListCall) OrderBy ¶
added in v0.195.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesPackagesListCall

OrderBy sets the optional parameter "orderBy": The field to order the results by.

func (*ProjectsLocationsRepositoriesPackagesListCall) PageSize ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPackagesListCall

PageSize sets the optional parameter "pageSize": The maximum number of packages to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesPackagesListCall) PageToken ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPackagesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesPackagesListCall) Pages ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesListCall) Pages(ctx context.Context, f func(*ListPackagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesPackagesPatchCall ¶
added in v0.169.0
type ProjectsLocationsRepositoriesPackagesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesPatchCall) Context ¶
added in v0.169.0
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesPatchCall) Do ¶
added in v0.169.0
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Do(opts ...googleapi.CallOption) (*Package, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.patch" call. Any non-2xx status code is an error. Response headers are in either *Package.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesPatchCall) Fields ¶
added in v0.169.0
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesPatchCall) Header ¶
added in v0.169.0
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesPatchCall) UpdateMask ¶
added in v0.169.0
func (c *ProjectsLocationsRepositoriesPackagesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPackagesPatchCall

UpdateMask sets the optional parameter "updateMask": The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

type ProjectsLocationsRepositoriesPackagesService ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesService struct {
	Tags *ProjectsLocationsRepositoriesPackagesTagsService

	Versions *ProjectsLocationsRepositoriesPackagesVersionsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesPackagesService ¶
added in v0.66.0
func NewProjectsLocationsRepositoriesPackagesService(s *Service) *ProjectsLocationsRepositoriesPackagesService
func (*ProjectsLocationsRepositoriesPackagesService) Delete ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesService) Delete(name string) *ProjectsLocationsRepositoriesPackagesDeleteCall

Delete: Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

- name: The name of the package to delete.

func (*ProjectsLocationsRepositoriesPackagesService) Get ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesService) Get(name string) *ProjectsLocationsRepositoriesPackagesGetCall

Get: Gets a package.

- name: The name of the package to retrieve.

func (*ProjectsLocationsRepositoriesPackagesService) List ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesService) List(parent string) *ProjectsLocationsRepositoriesPackagesListCall

List: Lists packages.

- parent: The name of the parent resource whose packages will be listed.

func (*ProjectsLocationsRepositoriesPackagesService) Patch ¶
added in v0.169.0
func (r *ProjectsLocationsRepositoriesPackagesService) Patch(name string, package_ *Package) *ProjectsLocationsRepositoriesPackagesPatchCall

Patch: Updates a package.

name: The name of the package, for example: `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1`. If the package ID part contains slashes, the slashes are escaped.
type ProjectsLocationsRepositoriesPackagesTagsCreateCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesTagsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesTagsCreateCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesTagsCreateCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Do(opts ...googleapi.CallOption) (*Tag, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.tags.create" call. Any non-2xx status code is an error. Response headers are in either *Tag.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesTagsCreateCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesTagsCreateCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesTagsCreateCall) TagId ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsCreateCall) TagId(tagId string) *ProjectsLocationsRepositoriesPackagesTagsCreateCall

TagId sets the optional parameter "tagId": The tag id to use for this repository.

type ProjectsLocationsRepositoriesPackagesTagsDeleteCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesTagsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.tags.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesPackagesTagsGetCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesTagsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesTagsGetCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesTagsGetCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Do(opts ...googleapi.CallOption) (*Tag, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.tags.get" call. Any non-2xx status code is an error. Response headers are in either *Tag.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesTagsGetCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesTagsGetCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesTagsGetCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesTagsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesPackagesTagsListCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesTagsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesTagsListCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Do(opts ...googleapi.CallOption) (*ListTagsResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.tags.list" call. Any non-2xx status code is an error. Response headers are in either *ListTagsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) Filter ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Filter(filter string) *ProjectsLocationsRepositoriesPackagesTagsListCall

Filter sets the optional parameter "filter": An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * `name` * `version` Examples of using a filter: To filter the results of your request to tags with the name `my-tag` in package `my-package` in repository `my-repo` in project "y-project` in the us-central region, append the following filter expression to your request: * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/tags/my-tag" You can also use wildcards to match any number of characters before or after the value: * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/tags/my*" * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/tags/*tag" * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/tags/*tag*" To filter the results of your request to tags applied to the version `1.0` in package `my-package`, append the following filter expression to your request: * `version="projects/my-project/locations/us-central1/repositories/my-repo/pack ages/my-package/versions/1.0"

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesTagsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) PageSize ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPackagesTagsListCall

PageSize sets the optional parameter "pageSize": The maximum number of tags to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) PageToken ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPackagesTagsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesPackagesTagsListCall) Pages ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsListCall) Pages(ctx context.Context, f func(*ListTagsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesPackagesTagsPatchCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesTagsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesTagsPatchCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesTagsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesTagsPatchCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Do(opts ...googleapi.CallOption) (*Tag, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.tags.patch" call. Any non-2xx status code is an error. Response headers are in either *Tag.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesTagsPatchCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesTagsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesTagsPatchCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesTagsPatchCall) UpdateMask ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesTagsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPackagesTagsPatchCall

UpdateMask sets the optional parameter "updateMask": The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

type ProjectsLocationsRepositoriesPackagesTagsService ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesTagsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesPackagesTagsService ¶
added in v0.66.0
func NewProjectsLocationsRepositoriesPackagesTagsService(s *Service) *ProjectsLocationsRepositoriesPackagesTagsService
func (*ProjectsLocationsRepositoriesPackagesTagsService) Create ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Create(parent string, tag *Tag) *ProjectsLocationsRepositoriesPackagesTagsCreateCall

Create: Creates a tag.

- parent: The name of the parent resource where the tag will be created.

func (*ProjectsLocationsRepositoriesPackagesTagsService) Delete ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Delete(name string) *ProjectsLocationsRepositoriesPackagesTagsDeleteCall

Delete: Deletes a tag.

- name: The name of the tag to delete.

func (*ProjectsLocationsRepositoriesPackagesTagsService) Get ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Get(name string) *ProjectsLocationsRepositoriesPackagesTagsGetCall

Get: Gets a tag.

- name: The name of the tag to retrieve.

func (*ProjectsLocationsRepositoriesPackagesTagsService) List ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesTagsService) List(parent string) *ProjectsLocationsRepositoriesPackagesTagsListCall

List: Lists tags.

parent: The name of the parent package whose tags will be listed. For example: `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1`.
func (*ProjectsLocationsRepositoriesPackagesTagsService) Patch ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesTagsService) Patch(name string, tag *Tag) *ProjectsLocationsRepositoriesPackagesTagsPatchCall

Patch: Updates a tag.

name: The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/ta g1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded.
type ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall ¶
added in v0.130.0
type ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Context ¶
added in v0.130.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Do ¶
added in v0.130.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.versions.batchDelete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Fields ¶
added in v0.130.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Header ¶
added in v0.130.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesPackagesVersionsDeleteCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesVersionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.versions.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Force ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Force(force bool) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall

Force sets the optional parameter "force": By default, a version that is tagged may not be deleted. If force=true, the version and any tags pointing to the version are deleted.

func (*ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesPackagesVersionsGetCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesVersionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesVersionsGetCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesVersionsGetCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Do(opts ...googleapi.CallOption) (*Version, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.versions.get" call. Any non-2xx status code is an error. Response headers are in either *Version.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesVersionsGetCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesVersionsGetCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesVersionsGetCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesVersionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesPackagesVersionsGetCall) View ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsGetCall) View(view string) *ProjectsLocationsRepositoriesPackagesVersionsGetCall

View sets the optional parameter "view": The view that should be returned in the response.

Possible values:

"VERSION_VIEW_UNSPECIFIED" - The default / unset value. The API will


default to the BASIC view.

"BASIC" - Includes basic information about the version, but not any


related tags.

"FULL" - Include everything.

type ProjectsLocationsRepositoriesPackagesVersionsListCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesVersionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Do(opts ...googleapi.CallOption) (*ListVersionsResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.versions.list" call. Any non-2xx status code is an error. Response headers are in either *ListVersionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) Filter ¶
added in v0.195.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Filter(filter string) *ProjectsLocationsRepositoriesPackagesVersionsListCall

Filter sets the optional parameter "filter": An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * `name` * `annotations` Examples of using a filter: To filter the results of your request to versions with the name `my-version` in project `my-project` in the `us-central` region, in repository `my-repo`, append the following filter expression to your request: * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/versions/my-version" You can also use wildcards to match any number of characters before or after the value: * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/versions/*version" * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/versions/my*" * `name="projects/my-project/locations/us-central1/repositories/my-repo/package s/my-package/versions/*version*" To filter the results of your request to versions with the annotation key-value pair [`external_link`: `external_link_value`], append the following filter expression to your request: * "annotations.external_link:external_link_value" To filter just for a specific annotation key `external_link`, append the following filter expression to your request: * "annotations.external_link" If the annotation key or value contains special characters, you can escape them by surrounding the value with backticks. For example, to filter the results of your request to versions with the annotation key-value pair [`external.link`:`https://example.com/my-version`], append the following filter expression to your request: * “ "annotations.`external.link`:`https://example.com/my-version" “ You can also filter with annotations with a wildcard to match any number of characters before or after the value: * “ "annotations.*_link:`*example.com*" “

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) IfNoneMatch ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPackagesVersionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) OrderBy ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) OrderBy(orderBy string) *ProjectsLocationsRepositoriesPackagesVersionsListCall

OrderBy sets the optional parameter "orderBy": The field to order the results by.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) PageSize ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPackagesVersionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of versions to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) PageToken ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPackagesVersionsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) Pages ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) Pages(ctx context.Context, f func(*ListVersionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsRepositoriesPackagesVersionsListCall) View ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsListCall) View(view string) *ProjectsLocationsRepositoriesPackagesVersionsListCall

View sets the optional parameter "view": The view that should be returned in the response.

Possible values:

"VERSION_VIEW_UNSPECIFIED" - The default / unset value. The API will


default to the BASIC view.

"BASIC" - Includes basic information about the version, but not any


related tags.

"FULL" - Include everything.

type ProjectsLocationsRepositoriesPackagesVersionsPatchCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesPackagesVersionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Do(opts ...googleapi.CallOption) (*Version, error)

Do executes the "artifactregistry.projects.locations.repositories.packages.versions.patch" call. Any non-2xx status code is an error. Response headers are in either *Version.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPackagesVersionsPatchCall) UpdateMask ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesPackagesVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall

UpdateMask sets the optional parameter "updateMask": The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

type ProjectsLocationsRepositoriesPackagesVersionsService ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPackagesVersionsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesPackagesVersionsService ¶
added in v0.66.0
func NewProjectsLocationsRepositoriesPackagesVersionsService(s *Service) *ProjectsLocationsRepositoriesPackagesVersionsService
func (*ProjectsLocationsRepositoriesPackagesVersionsService) BatchDelete ¶
added in v0.130.0
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) BatchDelete(parent string, batchdeleteversionsrequest *BatchDeleteVersionsRequest) *ProjectsLocationsRepositoriesPackagesVersionsBatchDeleteCall

BatchDelete: Deletes multiple versions across a repository. The returned operation will complete once the versions have been deleted.

- parent: The name of the repository holding all requested versions.

func (*ProjectsLocationsRepositoriesPackagesVersionsService) Delete ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) Delete(name string) *ProjectsLocationsRepositoriesPackagesVersionsDeleteCall

Delete: Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

- name: The name of the version to delete.

func (*ProjectsLocationsRepositoriesPackagesVersionsService) Get ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) Get(name string) *ProjectsLocationsRepositoriesPackagesVersionsGetCall

Get: Gets a version

- name: The name of the version to retrieve.

func (*ProjectsLocationsRepositoriesPackagesVersionsService) List ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) List(parent string) *ProjectsLocationsRepositoriesPackagesVersionsListCall

List: Lists versions.

- parent: The name of the parent resource whose versions will be listed.

func (*ProjectsLocationsRepositoriesPackagesVersionsService) Patch ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesPackagesVersionsService) Patch(name string, version *Version) *ProjectsLocationsRepositoriesPackagesVersionsPatchCall

Patch: Updates a version.

name: The name of the version, for example: `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/version s/art1`. If the package or version ID parts contain slashes, the slashes are escaped.
type ProjectsLocationsRepositoriesPatchCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPatchCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPatchCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPatchCall) Do(opts ...googleapi.CallOption) (*Repository, error)

Do executes the "artifactregistry.projects.locations.repositories.patch" call. Any non-2xx status code is an error. Response headers are in either *Repository.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPatchCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPatchCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPatchCall) UpdateMask ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesPatchCall

UpdateMask sets the optional parameter "updateMask": The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

type ProjectsLocationsRepositoriesPythonPackagesGetCall ¶
added in v0.86.0
type ProjectsLocationsRepositoriesPythonPackagesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPythonPackagesGetCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPythonPackagesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPythonPackagesGetCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Do(opts ...googleapi.CallOption) (*PythonPackage, error)

Do executes the "artifactregistry.projects.locations.repositories.pythonPackages.get" call. Any non-2xx status code is an error. Response headers are in either *PythonPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPythonPackagesGetCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPythonPackagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPythonPackagesGetCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPythonPackagesGetCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPythonPackagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesPythonPackagesListCall ¶
added in v0.86.0
type ProjectsLocationsRepositoriesPythonPackagesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesPythonPackagesListCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesPythonPackagesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Do(opts ...googleapi.CallOption) (*ListPythonPackagesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.pythonPackages.list" call. Any non-2xx status code is an error. Response headers are in either *ListPythonPackagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesPythonPackagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesPythonPackagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) PageSize ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesPythonPackagesListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) PageToken ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesPythonPackagesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesPythonPackagesListCall) Pages ¶
added in v0.86.0
func (c *ProjectsLocationsRepositoriesPythonPackagesListCall) Pages(ctx context.Context, f func(*ListPythonPackagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesPythonPackagesService ¶
added in v0.86.0
type ProjectsLocationsRepositoriesPythonPackagesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesPythonPackagesService ¶
added in v0.86.0
func NewProjectsLocationsRepositoriesPythonPackagesService(s *Service) *ProjectsLocationsRepositoriesPythonPackagesService
func (*ProjectsLocationsRepositoriesPythonPackagesService) Get ¶
added in v0.86.0
func (r *ProjectsLocationsRepositoriesPythonPackagesService) Get(name string) *ProjectsLocationsRepositoriesPythonPackagesGetCall

Get: Gets a python package.

- name: The name of the python package.

func (*ProjectsLocationsRepositoriesPythonPackagesService) List ¶
added in v0.86.0
func (r *ProjectsLocationsRepositoriesPythonPackagesService) List(parent string) *ProjectsLocationsRepositoriesPythonPackagesListCall

List: Lists python packages.

parent: The name of the parent resource whose python packages will be listed.
type ProjectsLocationsRepositoriesRulesCreateCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesRulesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesRulesCreateCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesRulesCreateCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1Rule, error)

Do executes the "artifactregistry.projects.locations.repositories.rules.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleDevtoolsArtifactregistryV1Rule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesRulesCreateCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesRulesCreateCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesRulesCreateCall) RuleId ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesCreateCall) RuleId(ruleId string) *ProjectsLocationsRepositoriesRulesCreateCall

RuleId sets the optional parameter "ruleId": The rule id to use for this repository.

type ProjectsLocationsRepositoriesRulesDeleteCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesRulesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesRulesDeleteCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesRulesDeleteCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "artifactregistry.projects.locations.repositories.rules.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesRulesDeleteCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesRulesDeleteCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesRulesGetCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesRulesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesRulesGetCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesGetCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesRulesGetCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesGetCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1Rule, error)

Do executes the "artifactregistry.projects.locations.repositories.rules.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleDevtoolsArtifactregistryV1Rule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesRulesGetCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesRulesGetCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesRulesGetCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesRulesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRepositoriesRulesListCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesRulesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesRulesListCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesRulesListCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) Do(opts ...googleapi.CallOption) (*ListRulesResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.rules.list" call. Any non-2xx status code is an error. Response headers are in either *ListRulesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesRulesListCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesRulesListCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesRulesListCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRepositoriesRulesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRepositoriesRulesListCall) PageSize ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) PageSize(pageSize int64) *ProjectsLocationsRepositoriesRulesListCall

PageSize sets the optional parameter "pageSize": The maximum number of rules to return. Maximum page size is 1,000.

func (*ProjectsLocationsRepositoriesRulesListCall) PageToken ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) PageToken(pageToken string) *ProjectsLocationsRepositoriesRulesListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous list request, if any.

func (*ProjectsLocationsRepositoriesRulesListCall) Pages ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesListCall) Pages(ctx context.Context, f func(*ListRulesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRepositoriesRulesPatchCall ¶
added in v0.200.0
type ProjectsLocationsRepositoriesRulesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesRulesPatchCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesRulesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesRulesPatchCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleDevtoolsArtifactregistryV1Rule, error)

Do executes the "artifactregistry.projects.locations.repositories.rules.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleDevtoolsArtifactregistryV1Rule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesRulesPatchCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesRulesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesRulesPatchCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesRulesPatchCall) UpdateMask ¶
added in v0.200.0
func (c *ProjectsLocationsRepositoriesRulesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsRepositoriesRulesPatchCall

UpdateMask sets the optional parameter "updateMask": The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

type ProjectsLocationsRepositoriesRulesService ¶
added in v0.200.0
type ProjectsLocationsRepositoriesRulesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesRulesService ¶
added in v0.200.0
func NewProjectsLocationsRepositoriesRulesService(s *Service) *ProjectsLocationsRepositoriesRulesService
func (*ProjectsLocationsRepositoriesRulesService) Create ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesRulesService) Create(parent string, googledevtoolsartifactregistryv1rule *GoogleDevtoolsArtifactregistryV1Rule) *ProjectsLocationsRepositoriesRulesCreateCall

Create: Creates a rule.

- parent: The name of the parent resource where the rule will be created.

func (*ProjectsLocationsRepositoriesRulesService) Delete ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesRulesService) Delete(name string) *ProjectsLocationsRepositoriesRulesDeleteCall

Delete: Deletes a rule.

- name: The name of the rule to delete.

func (*ProjectsLocationsRepositoriesRulesService) Get ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesRulesService) Get(name string) *ProjectsLocationsRepositoriesRulesGetCall

Get: Gets a rule.

- name: The name of the rule to retrieve.

func (*ProjectsLocationsRepositoriesRulesService) List ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesRulesService) List(parent string) *ProjectsLocationsRepositoriesRulesListCall

List: Lists rules.

parent: The name of the parent repository whose rules will be listed. For example: `projects/p1/locations/us-central1/repositories/repo1`.
func (*ProjectsLocationsRepositoriesRulesService) Patch ¶
added in v0.200.0
func (r *ProjectsLocationsRepositoriesRulesService) Patch(name string, googledevtoolsartifactregistryv1rule *GoogleDevtoolsArtifactregistryV1Rule) *ProjectsLocationsRepositoriesRulesPatchCall

Patch: Updates a rule.

name: The name of the rule, for example: `projects/p1/locations/us-central1/repositories/repo1/rules/rule1`.
type ProjectsLocationsRepositoriesService ¶
added in v0.41.0
type ProjectsLocationsRepositoriesService struct {
	AptArtifacts *ProjectsLocationsRepositoriesAptArtifactsService

	Attachments *ProjectsLocationsRepositoriesAttachmentsService

	DockerImages *ProjectsLocationsRepositoriesDockerImagesService

	Files *ProjectsLocationsRepositoriesFilesService

	GenericArtifacts *ProjectsLocationsRepositoriesGenericArtifactsService

	GoModules *ProjectsLocationsRepositoriesGoModulesService

	GoogetArtifacts *ProjectsLocationsRepositoriesGoogetArtifactsService

	KfpArtifacts *ProjectsLocationsRepositoriesKfpArtifactsService

	MavenArtifacts *ProjectsLocationsRepositoriesMavenArtifactsService

	NpmPackages *ProjectsLocationsRepositoriesNpmPackagesService

	Packages *ProjectsLocationsRepositoriesPackagesService

	PythonPackages *ProjectsLocationsRepositoriesPythonPackagesService

	Rules *ProjectsLocationsRepositoriesRulesService

	YumArtifacts *ProjectsLocationsRepositoriesYumArtifactsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesService ¶
added in v0.41.0
func NewProjectsLocationsRepositoriesService(s *Service) *ProjectsLocationsRepositoriesService
func (*ProjectsLocationsRepositoriesService) Create ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesService) Create(parent string, repository *Repository) *ProjectsLocationsRepositoriesCreateCall

Create: Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

parent: The name of the parent resource where the repository will be created.
func (*ProjectsLocationsRepositoriesService) Delete ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesService) Delete(name string) *ProjectsLocationsRepositoriesDeleteCall

Delete: Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

- name: The name of the repository to delete.

func (*ProjectsLocationsRepositoriesService) ExportArtifact ¶
added in v0.255.0
func (r *ProjectsLocationsRepositoriesService) ExportArtifact(repository string, exportartifactrequest *ExportArtifactRequest) *ProjectsLocationsRepositoriesExportArtifactCall

ExportArtifact: Exports an artifact to a Cloud Storage bucket.

repository: The repository of the artifact to export. Format: projects/{project}/locations/{location}/repositories/{repository}.
func (*ProjectsLocationsRepositoriesService) Get ¶
added in v0.46.0
func (r *ProjectsLocationsRepositoriesService) Get(name string) *ProjectsLocationsRepositoriesGetCall

Get: Gets a repository.

- name: The name of the repository to retrieve.

func (*ProjectsLocationsRepositoriesService) GetIamPolicy ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesService) GetIamPolicy(resource string) *ProjectsLocationsRepositoriesGetIamPolicyCall

GetIamPolicy: Gets the IAM policy for a given resource.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsRepositoriesService) List ¶
added in v0.46.0
func (r *ProjectsLocationsRepositoriesService) List(parent string) *ProjectsLocationsRepositoriesListCall

List: Lists repositories.

- parent: The name of the parent resource whose repositories will be listed.

func (*ProjectsLocationsRepositoriesService) Patch ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesService) Patch(name string, repository *Repository) *ProjectsLocationsRepositoriesPatchCall

Patch: Updates a repository.

name: The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`. For each location in a project, repository names must be unique.
func (*ProjectsLocationsRepositoriesService) SetIamPolicy ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsRepositoriesSetIamPolicyCall

SetIamPolicy: Updates the IAM policy for a given resource.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsRepositoriesService) TestIamPermissions ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsRepositoriesTestIamPermissionsCall

TestIamPermissions: Tests if the caller has a list of permissions on a resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsRepositoriesSetIamPolicyCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesSetIamPolicyCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesSetIamPolicyCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "artifactregistry.projects.locations.repositories.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesSetIamPolicyCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesSetIamPolicyCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesTestIamPermissionsCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesTestIamPermissionsCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesTestIamPermissionsCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesTestIamPermissionsCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesTestIamPermissionsCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesYumArtifactsImportCall ¶
added in v0.66.0
type ProjectsLocationsRepositoriesYumArtifactsImportCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesYumArtifactsImportCall) Context ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesYumArtifactsImportCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRepositoriesYumArtifactsImportCall) Do ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "artifactregistry.projects.locations.repositories.yumArtifacts.import" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesYumArtifactsImportCall) Fields ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesYumArtifactsImportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesYumArtifactsImportCall) Header ¶
added in v0.66.0
func (c *ProjectsLocationsRepositoriesYumArtifactsImportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRepositoriesYumArtifactsService ¶
added in v0.66.0
type ProjectsLocationsRepositoriesYumArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRepositoriesYumArtifactsService ¶
added in v0.66.0
func NewProjectsLocationsRepositoriesYumArtifactsService(s *Service) *ProjectsLocationsRepositoriesYumArtifactsService
func (*ProjectsLocationsRepositoriesYumArtifactsService) Import ¶
added in v0.66.0
func (r *ProjectsLocationsRepositoriesYumArtifactsService) Import(parent string, importyumartifactsrequest *ImportYumArtifactsRequest) *ProjectsLocationsRepositoriesYumArtifactsImportCall

Import: Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

parent: The name of the parent resource where the artifacts will be imported.
func (*ProjectsLocationsRepositoriesYumArtifactsService) Upload ¶
added in v0.68.0
func (r *ProjectsLocationsRepositoriesYumArtifactsService) Upload(parent string, uploadyumartifactrequest *UploadYumArtifactRequest) *ProjectsLocationsRepositoriesYumArtifactsUploadCall

Upload: Directly uploads a Yum artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored.

parent: The name of the parent resource where the artifacts will be uploaded.
type ProjectsLocationsRepositoriesYumArtifactsUploadCall ¶
added in v0.68.0
type ProjectsLocationsRepositoriesYumArtifactsUploadCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall) Context ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Context(ctx context.Context) *ProjectsLocationsRepositoriesYumArtifactsUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall) Do ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Do(opts ...googleapi.CallOption) (*UploadYumArtifactMediaResponse, error)

Do executes the "artifactregistry.projects.locations.repositories.yumArtifacts.upload" call. Any non-2xx status code is an error. Response headers are in either *UploadYumArtifactMediaResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall) Fields ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Fields(s ...googleapi.Field) *ProjectsLocationsRepositoriesYumArtifactsUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall) Header ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall) Media ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *ProjectsLocationsRepositoriesYumArtifactsUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall) ProgressUpdater ¶
added in v0.68.0
func (c *ProjectsLocationsRepositoriesYumArtifactsUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ProjectsLocationsRepositoriesYumArtifactsUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ProjectsLocationsRepositoriesYumArtifactsUploadCall)
ResumableMedia
DEPRECATED
added in v0.68.0
type ProjectsLocationsService ¶
added in v0.41.0
type ProjectsLocationsService struct {
	Operations *ProjectsLocationsOperationsService

	Repositories *ProjectsLocationsRepositoriesService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
added in v0.41.0
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (*ProjectsLocationsService) Get ¶
added in v0.74.0
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- name: Resource name for the location.

func (*ProjectsLocationsService) GetVpcscConfig ¶
added in v0.110.0
func (r *ProjectsLocationsService) GetVpcscConfig(name string) *ProjectsLocationsGetVpcscConfigCall

GetVpcscConfig: Retrieves the VPCSC Config for the Project.

- name: The name of the VPCSCConfig resource.

func (*ProjectsLocationsService) List ¶
added in v0.74.0
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

func (*ProjectsLocationsService) UpdateVpcscConfig ¶
added in v0.110.0
func (r *ProjectsLocationsService) UpdateVpcscConfig(name string, vpcscconfig *VPCSCConfig) *ProjectsLocationsUpdateVpcscConfigCall

UpdateVpcscConfig: Updates the VPCSC Config for the Project.

name: The name of the project's VPC SC Config. Always of the form: projects/{projectID}/locations/{location}/vpcscConfig In update request: never set In response: always set.
type ProjectsLocationsUpdateVpcscConfigCall ¶
added in v0.110.0
type ProjectsLocationsUpdateVpcscConfigCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsUpdateVpcscConfigCall) Context ¶
added in v0.110.0
func (c *ProjectsLocationsUpdateVpcscConfigCall) Context(ctx context.Context) *ProjectsLocationsUpdateVpcscConfigCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsUpdateVpcscConfigCall) Do ¶
added in v0.110.0
func (c *ProjectsLocationsUpdateVpcscConfigCall) Do(opts ...googleapi.CallOption) (*VPCSCConfig, error)

Do executes the "artifactregistry.projects.locations.updateVpcscConfig" call. Any non-2xx status code is an error. Response headers are in either *VPCSCConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsUpdateVpcscConfigCall) Fields ¶
added in v0.110.0
func (c *ProjectsLocationsUpdateVpcscConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsUpdateVpcscConfigCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsUpdateVpcscConfigCall) Header ¶
added in v0.110.0
func (c *ProjectsLocationsUpdateVpcscConfigCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsUpdateVpcscConfigCall) UpdateMask ¶
added in v0.110.0
func (c *ProjectsLocationsUpdateVpcscConfigCall) UpdateMask(updateMask string) *ProjectsLocationsUpdateVpcscConfigCall

UpdateMask sets the optional parameter "updateMask": Field mask to support partial updates.

type ProjectsService ¶
added in v0.41.0
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
added in v0.41.0
func NewProjectsService(s *Service) *ProjectsService
func (*ProjectsService) GetProjectSettings ¶
added in v0.66.0
func (r *ProjectsService) GetProjectSettings(name string) *ProjectsGetProjectSettingsCall

GetProjectSettings: Retrieves the Settings for the Project.

- name: The name of the projectSettings resource.

func (*ProjectsService) UpdateProjectSettings ¶
added in v0.66.0
func (r *ProjectsService) UpdateProjectSettings(name string, projectsettings *ProjectSettings) *ProjectsUpdateProjectSettingsCall

UpdateProjectSettings: Updates the Settings for the Project.

name: The name of the project's settings. Always of the form: projects/{project-id}/projectSettings In update request: never set In response: always set.
type ProjectsUpdateProjectSettingsCall ¶
added in v0.66.0
type ProjectsUpdateProjectSettingsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsUpdateProjectSettingsCall) Context ¶
added in v0.66.0
func (c *ProjectsUpdateProjectSettingsCall) Context(ctx context.Context) *ProjectsUpdateProjectSettingsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsUpdateProjectSettingsCall) Do ¶
added in v0.66.0
func (c *ProjectsUpdateProjectSettingsCall) Do(opts ...googleapi.CallOption) (*ProjectSettings, error)

Do executes the "artifactregistry.projects.updateProjectSettings" call. Any non-2xx status code is an error. Response headers are in either *ProjectSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsUpdateProjectSettingsCall) Fields ¶
added in v0.66.0
func (c *ProjectsUpdateProjectSettingsCall) Fields(s ...googleapi.Field) *ProjectsUpdateProjectSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsUpdateProjectSettingsCall) Header ¶
added in v0.66.0
func (c *ProjectsUpdateProjectSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsUpdateProjectSettingsCall) UpdateMask ¶
added in v0.66.0
func (c *ProjectsUpdateProjectSettingsCall) UpdateMask(updateMask string) *ProjectsUpdateProjectSettingsCall

UpdateMask sets the optional parameter "updateMask": Field mask to support partial updates.

type PythonPackage ¶
added in v0.86.0
type PythonPackage struct {
	// CreateTime: Output only. Time the package was created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Required. registry_location, project_id, repository_name and
	// python_package forms a unique package
	// name:`projects//locations//repository//pythonPackages/`. For example,
	// "projects/test-project/locations/us-west4/repositories/test-repo/pythonPackag
	// es/ python_package:1.0.0", where "us-west4" is the registry_location,
	// "test-project" is the project_id, "test-repo" is the repository_name and
	// python_package:1.0.0" is the python package.
	Name string `json:"name,omitempty"`
	// PackageName: Package for the artifact.
	PackageName string `json:"packageName,omitempty"`
	// UpdateTime: Output only. Time the package was updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// Uri: Required. URL to access the package. Example:
	// us-west4-python.pkg.dev/test-project/test-repo/python_package/file-name-1.0.0
	// .tar.gz
	Uri string `json:"uri,omitempty"`
	// Version: Version of this package.
	Version string `json:"version,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PythonPackage: PythonPackage represents a python artifact.

func (PythonPackage) MarshalJSON ¶
added in v0.86.0
func (s PythonPackage) MarshalJSON() ([]byte, error)
type PythonRepository ¶
added in v0.110.0
type PythonRepository struct {
	// CustomRepository: Customer-specified remote repository.
	CustomRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository `json:"customRepository,omitempty"`
	// PublicRepository: One of the publicly available Python repositories
	// supported by Artifact Registry.
	//
	// Possible values:
	//   "PUBLIC_REPOSITORY_UNSPECIFIED" - Unspecified repository.
	//   "PYPI" - PyPI.
	PublicRepository string `json:"publicRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRepository") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PythonRepository: Configuration for a Python remote repository.

func (PythonRepository) MarshalJSON ¶
added in v0.110.0
func (s PythonRepository) MarshalJSON() ([]byte, error)
type RemoteRepositoryConfig ¶
added in v0.110.0
type RemoteRepositoryConfig struct {
	// AptRepository: Specific settings for an Apt remote repository.
	AptRepository *AptRepository `json:"aptRepository,omitempty"`
	// CommonRepository: Common remote repository settings. Used as the remote
	// repository upstream URL.
	CommonRepository *CommonRemoteRepository `json:"commonRepository,omitempty"`
	// Description: The description of the remote source.
	Description string `json:"description,omitempty"`
	// DisableUpstreamValidation: Input only. A create/update remote repo option to
	// avoid making a HEAD/GET request to validate a remote repo and any supplied
	// upstream credentials.
	DisableUpstreamValidation bool `json:"disableUpstreamValidation,omitempty"`
	// DockerRepository: Specific settings for a Docker remote repository.
	DockerRepository *DockerRepository `json:"dockerRepository,omitempty"`
	// MavenRepository: Specific settings for a Maven remote repository.
	MavenRepository *MavenRepository `json:"mavenRepository,omitempty"`
	// NpmRepository: Specific settings for an Npm remote repository.
	NpmRepository *NpmRepository `json:"npmRepository,omitempty"`
	// PythonRepository: Specific settings for a Python remote repository.
	PythonRepository *PythonRepository `json:"pythonRepository,omitempty"`
	// UpstreamCredentials: Optional. The credentials used to access the remote
	// repository.
	UpstreamCredentials *UpstreamCredentials `json:"upstreamCredentials,omitempty"`
	// YumRepository: Specific settings for a Yum remote repository.
	YumRepository *YumRepository `json:"yumRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AptRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AptRepository") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemoteRepositoryConfig: Remote repository configuration.

func (RemoteRepositoryConfig) MarshalJSON ¶
added in v0.110.0
func (s RemoteRepositoryConfig) MarshalJSON() ([]byte, error)
type Repository ¶
added in v0.46.0
type Repository struct {
	// CleanupPolicies: Optional. Cleanup policies for this repository. Cleanup
	// policies indicate when certain package versions can be automatically
	// deleted. Map keys are policy IDs supplied by users during policy creation.
	// They must unique within a repository and be under 128 characters in length.
	CleanupPolicies map[string]CleanupPolicy `json:"cleanupPolicies,omitempty"`
	// CleanupPolicyDryRun: Optional. If true, the cleanup pipeline is prevented
	// from deleting versions in this repository.
	CleanupPolicyDryRun bool `json:"cleanupPolicyDryRun,omitempty"`
	// CreateTime: Output only. The time when the repository was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: The user-provided description of the repository.
	Description string `json:"description,omitempty"`
	// DisallowUnspecifiedMode: Optional. If this is true, an unspecified repo type
	// will be treated as error rather than defaulting to standard.
	DisallowUnspecifiedMode bool `json:"disallowUnspecifiedMode,omitempty"`
	// DockerConfig: Docker repository config contains repository level
	// configuration for the repositories of docker type.
	DockerConfig *DockerRepositoryConfig `json:"dockerConfig,omitempty"`
	// Format: Optional. The format of packages that are stored in the repository.
	//
	// Possible values:
	//   "FORMAT_UNSPECIFIED" - Unspecified package format.
	//   "DOCKER" - Docker package format.
	//   "MAVEN" - Maven package format.
	//   "NPM" - NPM package format.
	//   "APT" - APT package format.
	//   "YUM" - YUM package format.
	//   "GOOGET" - GooGet package format.
	//   "PYTHON" - Python package format.
	//   "KFP" - Kubeflow Pipelines package format.
	//   "GO" - Go package format.
	//   "GENERIC" - Generic package format.
	//   "RUBY" - Ruby package format.
	Format string `json:"format,omitempty"`
	// KmsKeyName: The Cloud KMS resource name of the customer managed encryption
	// key that's used to encrypt the contents of the Repository. Has the form:
	// `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`.
	// This value may not be changed after the Repository has been created.
	KmsKeyName string `json:"kmsKeyName,omitempty"`
	// Labels: Labels with user-defined metadata. This field may contain up to 64
	// entries. Label keys and values may be no longer than 63 characters. Label
	// keys must begin with a lowercase letter and may only contain lowercase
	// letters, numeric characters, underscores, and dashes.
	Labels map[string]string `json:"labels,omitempty"`
	// MavenConfig: Maven repository config contains repository level configuration
	// for the repositories of maven type.
	MavenConfig *MavenRepositoryConfig `json:"mavenConfig,omitempty"`
	// Mode: Optional. The mode of the repository.
	//
	// Possible values:
	//   "MODE_UNSPECIFIED" - Unspecified mode.
	//   "STANDARD_REPOSITORY" - A standard repository storing artifacts.
	//   "VIRTUAL_REPOSITORY" - A virtual repository to serve artifacts from one or
	// more sources.
	//   "REMOTE_REPOSITORY" - A remote repository to serve artifacts from a remote
	// source.
	//   "AOSS_REPOSITORY" - An AOSS repository provides artifacts from AOSS
	// upstreams.
	//   "ASSURED_OSS_REPOSITORY" - Replacement of AOSS_REPOSITORY.
	Mode string `json:"mode,omitempty"`
	// Name: The name of the repository, for example:
	// `projects/p1/locations/us-central1/repositories/repo1`. For each location in
	// a project, repository names must be unique.
	Name string `json:"name,omitempty"`
	// RegistryUri: Output only. The repository endpoint, for example:
	// `us-docker.pkg.dev/my-proj/my-repo`.
	RegistryUri string `json:"registryUri,omitempty"`
	// RemoteRepositoryConfig: Configuration specific for a Remote Repository.
	RemoteRepositoryConfig *RemoteRepositoryConfig `json:"remoteRepositoryConfig,omitempty"`
	// SatisfiesPzi: Output only. Whether or not this repository satisfies PZI.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Whether or not this repository satisfies PZS.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// SizeBytes: Output only. The size, in bytes, of all artifact storage in this
	// repository. Repositories that are generally available or in public preview
	// use this to calculate storage costs.
	SizeBytes int64 `json:"sizeBytes,omitempty,string"`
	// UpdateTime: Output only. The time when the repository was last updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// VirtualRepositoryConfig: Configuration specific for a Virtual Repository.
	VirtualRepositoryConfig *VirtualRepositoryConfig `json:"virtualRepositoryConfig,omitempty"`
	// VulnerabilityScanningConfig: Optional. Config and state for vulnerability
	// scanning of resources within this Repository.
	VulnerabilityScanningConfig *VulnerabilityScanningConfig `json:"vulnerabilityScanningConfig,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CleanupPolicies") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CleanupPolicies") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Repository: A Repository for storing artifacts with a specific format.

func (Repository) MarshalJSON ¶
added in v0.46.0
func (s Repository) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Projects *ProjectsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type SetIamPolicyRequest ¶
added in v0.66.0
type SetIamPolicyRequest struct {
	// Policy: REQUIRED: The complete policy to be applied to the `resource`. The
	// size of the policy is limited to a few 10s of KB. An empty policy is a valid
	// policy but certain Google Cloud services (such as Projects) might reject
	// them.
	Policy *Policy `json:"policy,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Policy") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Policy") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SetIamPolicyRequest: Request message for `SetIamPolicy` method.

func (SetIamPolicyRequest) MarshalJSON ¶
added in v0.66.0
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type Status ¶
type Status struct {
	// Code: The status code, which should be an enum value of google.rpc.Code.
	Code int64 `json:"code,omitempty"`
	// Details: A list of messages that carry the error details. There is a common
	// set of message types for APIs to use.
	Details []googleapi.RawMessage `json:"details,omitempty"`
	// Message: A developer-facing error message, which should be in English. Any
	// user-facing error message should be localized and sent in the
	// google.rpc.Status.details field, or localized by the client.
	Message string `json:"message,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Code") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Code") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Status: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC (https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide (https://cloud.google.com/apis/design/errors).

func (Status) MarshalJSON ¶
func (s Status) MarshalJSON() ([]byte, error)
type Tag ¶
added in v0.66.0
type Tag struct {
	// Name: The name of the tag, for example:
	// "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1
	// ". If the package part contains slashes, the slashes are escaped. The tag
	// part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be
	// URL encoded.
	Name string `json:"name,omitempty"`
	// Version: The name of the version the tag refers to, for example:
	// `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/
	// sha256:5243811` If the package or version ID parts contain slashes, the
	// slashes are escaped.
	Version string `json:"version,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Name") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Name") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Tag: Tags point to a version and represent an alternative name that can be used to access the version.

func (Tag) MarshalJSON ¶
added in v0.66.0
func (s Tag) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest ¶
added in v0.66.0
type TestIamPermissionsRequest struct {
	// Permissions: The set of permissions to check for the `resource`. Permissions
	// with wildcards (such as `*` or `storage.*`) are not allowed. For more
	// information see IAM Overview
	// (https://cloud.google.com/iam/docs/overview#permissions).
	Permissions []string `json:"permissions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Permissions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Permissions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TestIamPermissionsRequest: Request message for `TestIamPermissions` method.

func (TestIamPermissionsRequest) MarshalJSON ¶
added in v0.66.0
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse ¶
added in v0.66.0
type TestIamPermissionsResponse struct {
	// Permissions: A subset of `TestPermissionsRequest.permissions` that the
	// caller is allowed.
	Permissions []string `json:"permissions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Permissions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Permissions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TestIamPermissionsResponse: Response message for `TestIamPermissions` method.

func (TestIamPermissionsResponse) MarshalJSON ¶
added in v0.66.0
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type UploadAptArtifactMediaResponse ¶
added in v0.51.0
type UploadAptArtifactMediaResponse struct {
	// Operation: Operation to be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadAptArtifactMediaResponse: The response to upload an artifact.

func (UploadAptArtifactMediaResponse) MarshalJSON ¶
added in v0.51.0
func (s UploadAptArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadAptArtifactMetadata ¶
added in v0.78.0
type UploadAptArtifactMetadata struct {
}

UploadAptArtifactMetadata: The operation metadata for uploading artifacts.

type UploadAptArtifactRequest ¶
added in v0.66.0
type UploadAptArtifactRequest struct {
}

UploadAptArtifactRequest: The request to upload an artifact.

type UploadAptArtifactResponse ¶
added in v0.51.0
type UploadAptArtifactResponse struct {
	// AptArtifacts: The Apt artifacts updated.
	AptArtifacts []*AptArtifact `json:"aptArtifacts,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AptArtifacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AptArtifacts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadAptArtifactResponse: The response of the completed artifact upload operation. This response is contained in the Operation and available to users.

func (UploadAptArtifactResponse) MarshalJSON ¶
added in v0.51.0
func (s UploadAptArtifactResponse) MarshalJSON() ([]byte, error)
type UploadFileMediaResponse ¶
added in v0.200.0
type UploadFileMediaResponse struct {
	// Operation: Operation that will be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadFileMediaResponse: The response to upload a generic artifact.

func (UploadFileMediaResponse) MarshalJSON ¶
added in v0.200.0
func (s UploadFileMediaResponse) MarshalJSON() ([]byte, error)
type UploadFileRequest ¶
added in v0.200.0
type UploadFileRequest struct {
	// FileId: Optional. The ID of the file. If left empty will default to sha256
	// digest of the content uploaded.
	FileId string `json:"fileId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FileId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FileId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadFileRequest: The request to upload a file.

func (UploadFileRequest) MarshalJSON ¶
added in v0.200.0
func (s UploadFileRequest) MarshalJSON() ([]byte, error)
type UploadGenericArtifactMediaResponse ¶
added in v0.178.0
type UploadGenericArtifactMediaResponse struct {
	// Operation: Operation that will be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadGenericArtifactMediaResponse: The response to upload a generic artifact.

func (UploadGenericArtifactMediaResponse) MarshalJSON ¶
added in v0.178.0
func (s UploadGenericArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadGenericArtifactMetadata ¶
added in v0.178.0
type UploadGenericArtifactMetadata struct {
}

UploadGenericArtifactMetadata: The operation metadata for uploading generic artifacts.

type UploadGenericArtifactRequest ¶
added in v0.178.0
type UploadGenericArtifactRequest struct {
	// Filename: The name of the file of the generic artifact to be uploaded. E.g.
	// `example-file.zip` The filename is limited to letters, numbers, and url safe
	// characters, i.e. [a-zA-Z0-9-_.~@].
	Filename string `json:"filename,omitempty"`
	// PackageId: The ID of the package of the generic artifact. If the package
	// does not exist, a new package will be created. The `package_id` should start
	// and end with a letter or number, only contain letters, numbers, hyphens,
	// underscores, and periods, and not exceed 256 characters.
	PackageId string `json:"packageId,omitempty"`
	// VersionId: The ID of the version of the generic artifact. If the version
	// does not exist, a new version will be created. The version_id must start and
	// end with a letter or number, can only contain lowercase letters, numbers,
	// the following characters [-.+~:], i.e.[a-z0-9-.+~:] and cannot exceed a
	// total of 128 characters. Creating a version called `latest` is not allowed.
	VersionId string `json:"versionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Filename") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Filename") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadGenericArtifactRequest: The request to upload a generic artifact. The created GenericArtifact will have the resource name {parent}/genericArtifacts/package_id:version_id. The created file will have the resource name {parent}/files/package_id:version_id:filename.

func (UploadGenericArtifactRequest) MarshalJSON ¶
added in v0.178.0
func (s UploadGenericArtifactRequest) MarshalJSON() ([]byte, error)
type UploadGoModuleMediaResponse ¶
added in v0.129.0
type UploadGoModuleMediaResponse struct {
	// Operation: Operation to be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadGoModuleMediaResponse: The response to upload a Go module.

func (UploadGoModuleMediaResponse) MarshalJSON ¶
added in v0.129.0
func (s UploadGoModuleMediaResponse) MarshalJSON() ([]byte, error)
type UploadGoModuleMetadata ¶
added in v0.129.0
type UploadGoModuleMetadata struct {
}

UploadGoModuleMetadata: The operation metadata for uploading go modules.

type UploadGoModuleRequest ¶
added in v0.129.0
type UploadGoModuleRequest struct {
}

UploadGoModuleRequest: The request to upload a Go module.

type UploadGoogetArtifactMediaResponse ¶
added in v0.122.0
type UploadGoogetArtifactMediaResponse struct {
	// Operation: Operation to be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadGoogetArtifactMediaResponse: The response to upload an artifact.

func (UploadGoogetArtifactMediaResponse) MarshalJSON ¶
added in v0.122.0
func (s UploadGoogetArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadGoogetArtifactMetadata ¶
added in v0.123.0
type UploadGoogetArtifactMetadata struct {
}

UploadGoogetArtifactMetadata: The operation metadata for uploading artifacts.

type UploadGoogetArtifactRequest ¶
added in v0.122.0
type UploadGoogetArtifactRequest struct {
}

UploadGoogetArtifactRequest: The request to upload an artifact.

type UploadGoogetArtifactResponse ¶
added in v0.123.0
type UploadGoogetArtifactResponse struct {
	// GoogetArtifacts: The GooGet artifacts updated.
	GoogetArtifacts []*GoogetArtifact `json:"googetArtifacts,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GoogetArtifacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GoogetArtifacts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadGoogetArtifactResponse: The response of the completed artifact upload operation. This response is contained in the Operation and available to users.

func (UploadGoogetArtifactResponse) MarshalJSON ¶
added in v0.123.0
func (s UploadGoogetArtifactResponse) MarshalJSON() ([]byte, error)
type UploadKfpArtifactMediaResponse ¶
added in v0.98.0
type UploadKfpArtifactMediaResponse struct {
	// Operation: Operation that will be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadKfpArtifactMediaResponse: The response to upload an artifact.

func (UploadKfpArtifactMediaResponse) MarshalJSON ¶
added in v0.98.0
func (s UploadKfpArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadKfpArtifactMetadata ¶
added in v0.98.0
type UploadKfpArtifactMetadata struct {
}

UploadKfpArtifactMetadata: The operation metadata for uploading KFP artifacts.

type UploadKfpArtifactRequest ¶
added in v0.98.0
type UploadKfpArtifactRequest struct {
	// Description: Description of the package version.
	Description string `json:"description,omitempty"`
	// Tags: Tags to be created with the version.
	Tags []string `json:"tags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Description") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Description") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadKfpArtifactRequest: The request to upload an artifact.

func (UploadKfpArtifactRequest) MarshalJSON ¶
added in v0.98.0
func (s UploadKfpArtifactRequest) MarshalJSON() ([]byte, error)
type UploadYumArtifactMediaResponse ¶
added in v0.51.0
type UploadYumArtifactMediaResponse struct {
	// Operation: Operation to be returned to the user.
	Operation *Operation `json:"operation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadYumArtifactMediaResponse: The response to upload an artifact.

func (UploadYumArtifactMediaResponse) MarshalJSON ¶
added in v0.51.0
func (s UploadYumArtifactMediaResponse) MarshalJSON() ([]byte, error)
type UploadYumArtifactMetadata ¶
added in v0.78.0
type UploadYumArtifactMetadata struct {
}

UploadYumArtifactMetadata: The operation metadata for uploading artifacts.

type UploadYumArtifactRequest ¶
added in v0.66.0
type UploadYumArtifactRequest struct {
}

UploadYumArtifactRequest: The request to upload an artifact.

type UploadYumArtifactResponse ¶
added in v0.51.0
type UploadYumArtifactResponse struct {
	// YumArtifacts: The Yum artifacts updated.
	YumArtifacts []*YumArtifact `json:"yumArtifacts,omitempty"`
	// ForceSendFields is a list of field names (e.g. "YumArtifacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "YumArtifacts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UploadYumArtifactResponse: The response of the completed artifact upload operation. This response is contained in the Operation and available to users.

func (UploadYumArtifactResponse) MarshalJSON ¶
added in v0.51.0
func (s UploadYumArtifactResponse) MarshalJSON() ([]byte, error)
type UpstreamCredentials ¶
added in v0.149.0
type UpstreamCredentials struct {
	// UsernamePasswordCredentials: Use username and password to access the remote
	// repository.
	UsernamePasswordCredentials *UsernamePasswordCredentials `json:"usernamePasswordCredentials,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "UsernamePasswordCredentials") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UsernamePasswordCredentials") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpstreamCredentials: The credentials to access the remote repository.

func (UpstreamCredentials) MarshalJSON ¶
added in v0.149.0
func (s UpstreamCredentials) MarshalJSON() ([]byte, error)
type UpstreamPolicy ¶
added in v0.110.0
type UpstreamPolicy struct {
	// Id: The user-provided ID of the upstream policy.
	Id string `json:"id,omitempty"`
	// Priority: Entries with a greater priority value take precedence in the pull
	// order.
	Priority int64 `json:"priority,omitempty"`
	// Repository: A reference to the repository resource, for example:
	// `projects/p1/locations/us-central1/repositories/repo1`.
	Repository string `json:"repository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Id") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Id") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpstreamPolicy: Artifact policy configuration for the repository contents.

func (UpstreamPolicy) MarshalJSON ¶
added in v0.110.0
func (s UpstreamPolicy) MarshalJSON() ([]byte, error)
type UsernamePasswordCredentials ¶
added in v0.149.0
type UsernamePasswordCredentials struct {
	// PasswordSecretVersion: The Secret Manager key version that holds the
	// password to access the remote repository. Must be in the format of
	// `projects/{project}/secrets/{secret}/versions/{version}`.
	PasswordSecretVersion string `json:"passwordSecretVersion,omitempty"`
	// Username: The username to access the remote repository.
	Username string `json:"username,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PasswordSecretVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PasswordSecretVersion") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UsernamePasswordCredentials: Username and password credentials.

func (UsernamePasswordCredentials) MarshalJSON ¶
added in v0.149.0
func (s UsernamePasswordCredentials) MarshalJSON() ([]byte, error)
type VPCSCConfig ¶
added in v0.110.0
type VPCSCConfig struct {
	// Name: The name of the project's VPC SC Config. Always of the form:
	// projects/{projectID}/locations/{location}/vpcscConfig In update request:
	// never set In response: always set
	Name string `json:"name,omitempty"`
	// VpcscPolicy: The project per location VPC SC policy that defines the VPC SC
	// behavior for the Remote Repository (Allow/Deny).
	//
	// Possible values:
	//   "VPCSC_POLICY_UNSPECIFIED" - VPCSC_POLICY_UNSPECIFIED - the VPS SC policy
	// is not defined. When VPS SC policy is not defined - the Service will use the
	// default behavior (VPCSC_DENY).
	//   "DENY" - VPCSC_DENY - repository will block the requests to the Upstreams
	// for the Remote Repositories if the resource is in the perimeter.
	//   "ALLOW" - VPCSC_ALLOW - repository will allow the requests to the
	// Upstreams for the Remote Repositories if the resource is in the perimeter.
	VpcscPolicy string `json:"vpcscPolicy,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Name") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Name") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VPCSCConfig: The Artifact Registry VPC SC config that apply to a Project.

func (VPCSCConfig) MarshalJSON ¶
added in v0.110.0
func (s VPCSCConfig) MarshalJSON() ([]byte, error)
type Version ¶
added in v0.66.0
type Version struct {
	// Annotations: Optional. Client specified annotations.
	Annotations map[string]string `json:"annotations,omitempty"`
	// CreateTime: The time when the version was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. Description of the version, as specified in its
	// metadata.
	Description string `json:"description,omitempty"`
	// Fingerprints: Output only. Immutable reference for the version, calculated
	// based on the version's content. Currently we only support dirsum_sha256 hash
	// algorithm. Additional hash algorithms may be added in the future.
	Fingerprints []*Hash `json:"fingerprints,omitempty"`
	// Metadata: Output only. Repository-specific Metadata stored against this
	// version. The fields returned are defined by the underlying
	// repository-specific resource. Currently, the resources could be: DockerImage
	// MavenArtifact
	Metadata googleapi.RawMessage `json:"metadata,omitempty"`
	// Name: The name of the version, for example:
	// `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/
	// art1`. If the package or version ID parts contain slashes, the slashes are
	// escaped.
	Name string `json:"name,omitempty"`
	// RelatedTags: Output only. A list of related tags. Will contain up to 100
	// tags that reference this version.
	RelatedTags []*Tag `json:"relatedTags,omitempty"`
	// UpdateTime: The time when the version was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Annotations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Annotations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Version: The body of a version resource. A version resource represents a collection of components, such as files and other data. This may correspond to a version in many package management schemes.

func (Version) MarshalJSON ¶
added in v0.66.0
func (s Version) MarshalJSON() ([]byte, error)
type VirtualRepositoryConfig ¶
added in v0.110.0
type VirtualRepositoryConfig struct {
	// UpstreamPolicies: Policies that configure the upstream artifacts distributed
	// by the Virtual Repository. Upstream policies cannot be set on a standard
	// repository.
	UpstreamPolicies []*UpstreamPolicy `json:"upstreamPolicies,omitempty"`
	// ForceSendFields is a list of field names (e.g. "UpstreamPolicies") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UpstreamPolicies") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VirtualRepositoryConfig: Virtual repository configuration.

func (VirtualRepositoryConfig) MarshalJSON ¶
added in v0.110.0
func (s VirtualRepositoryConfig) MarshalJSON() ([]byte, error)
type VulnerabilityScanningConfig ¶
added in v0.202.0
type VulnerabilityScanningConfig struct {
	// EnablementConfig: Optional. Config for whether this repository has
	// vulnerability scanning disabled.
	//
	// Possible values:
	//   "ENABLEMENT_CONFIG_UNSPECIFIED" - Not set. This will be treated as
	// INHERITED for Docker repositories and DISABLED for non-Docker repositories.
	//   "INHERITED" - Scanning is Enabled, but dependent on API enablement.
	//   "DISABLED" - No automatic vulnerability scanning will be performed for
	// this repository.
	EnablementConfig string `json:"enablementConfig,omitempty"`
	// EnablementState: Output only. State of feature enablement, combining
	// repository enablement config and API enablement state.
	//
	// Possible values:
	//   "ENABLEMENT_STATE_UNSPECIFIED" - Enablement state is unclear.
	//   "SCANNING_UNSUPPORTED" - Repository does not support vulnerability
	// scanning.
	//   "SCANNING_DISABLED" - Vulnerability scanning is disabled for this
	// repository.
	//   "SCANNING_ACTIVE" - Vulnerability scanning is active for this repository.
	EnablementState string `json:"enablementState,omitempty"`
	// EnablementStateReason: Output only. Reason for the repository state.
	EnablementStateReason string `json:"enablementStateReason,omitempty"`
	// LastEnableTime: Output only. The last time this repository config was
	// enabled.
	LastEnableTime string `json:"lastEnableTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnablementConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnablementConfig") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VulnerabilityScanningConfig: Config on whether to perform vulnerability scanning for resources in this repository, as well as output fields describing current state.

func (VulnerabilityScanningConfig) MarshalJSON ¶
added in v0.202.0
func (s VulnerabilityScanningConfig) MarshalJSON() ([]byte, error)
type YumArtifact ¶
added in v0.51.0
type YumArtifact struct {
	// Architecture: Output only. Operating system architecture of the artifact.
	Architecture string `json:"architecture,omitempty"`
	// Name: Output only. The Artifact Registry resource name of the artifact.
	Name string `json:"name,omitempty"`
	// PackageName: Output only. The yum package name of the artifact.
	PackageName string `json:"packageName,omitempty"`
	// PackageType: Output only. An artifact is a binary or source package.
	//
	// Possible values:
	//   "PACKAGE_TYPE_UNSPECIFIED" - Package type is not specified.
	//   "BINARY" - Binary package (.rpm).
	//   "SOURCE" - Source package (.srpm).
	PackageType string `json:"packageType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Architecture") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Architecture") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

YumArtifact: A detailed representation of a Yum artifact.

func (YumArtifact) MarshalJSON ¶
added in v0.51.0
func (s YumArtifact) MarshalJSON() ([]byte, error)
type YumRepository ¶
added in v0.137.0
type YumRepository struct {
	// CustomRepository: Customer-specified remote repository.
	CustomRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository `json:"customRepository,omitempty"`
	// PublicRepository: One of the publicly available Yum repositories supported
	// by Artifact Registry.
	PublicRepository *GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository `json:"publicRepository,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRepository") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRepository") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

YumRepository: Configuration for a Yum remote repository.

func (YumRepository) MarshalJSON ¶
added in v0.137.0
func (s YumRepository) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
artifactregistry-gen.go
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

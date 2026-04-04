# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apigeeregistry/v1

Title: apigeeregistry package - google.golang.org/api/apigeeregistry/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apigeeregistry/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
apigeeregistry
 
v1
apigeeregistry
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 0
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
Source Files
 Documentation ¶
Overview ¶
Library status
Creating a client
Other authentication options

Package apigeeregistry provides access to the Apigee Registry API.

For product documentation, see: https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/apigeeregistry/v1"
...
ctx := context.Background()
apigeeregistryService, err := apigeeregistry.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

apigeeregistryService, err := apigeeregistry.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
apigeeregistryService, err := apigeeregistry.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type Api
func (s Api) MarshalJSON() ([]byte, error)
type ApiDeployment
func (s ApiDeployment) MarshalJSON() ([]byte, error)
type ApiSpec
func (s ApiSpec) MarshalJSON() ([]byte, error)
type ApiVersion
func (s ApiVersion) MarshalJSON() ([]byte, error)
type Artifact
func (s Artifact) MarshalJSON() ([]byte, error)
type Binding
func (s Binding) MarshalJSON() ([]byte, error)
type Build
func (s Build) MarshalJSON() ([]byte, error)
type CancelOperationRequest
type Config
func (s Config) MarshalJSON() ([]byte, error)
type Empty
type Expr
func (s Expr) MarshalJSON() ([]byte, error)
type HttpBody
func (s HttpBody) MarshalJSON() ([]byte, error)
type Instance
func (s Instance) MarshalJSON() ([]byte, error)
type ListApiDeploymentRevisionsResponse
func (s ListApiDeploymentRevisionsResponse) MarshalJSON() ([]byte, error)
type ListApiDeploymentsResponse
func (s ListApiDeploymentsResponse) MarshalJSON() ([]byte, error)
type ListApiSpecRevisionsResponse
func (s ListApiSpecRevisionsResponse) MarshalJSON() ([]byte, error)
type ListApiSpecsResponse
func (s ListApiSpecsResponse) MarshalJSON() ([]byte, error)
type ListApiVersionsResponse
func (s ListApiVersionsResponse) MarshalJSON() ([]byte, error)
type ListApisResponse
func (s ListApisResponse) MarshalJSON() ([]byte, error)
type ListArtifactsResponse
func (s ListArtifactsResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadata
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsLocationsApisArtifactsCreateCall
func (c *ProjectsLocationsApisArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisArtifactsCreateCall
func (c *ProjectsLocationsApisArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsCreateCall
func (c *ProjectsLocationsApisArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsCreateCall
func (c *ProjectsLocationsApisArtifactsCreateCall) Header() http.Header
type ProjectsLocationsApisArtifactsDeleteCall
func (c *ProjectsLocationsApisArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsDeleteCall
func (c *ProjectsLocationsApisArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsDeleteCall
func (c *ProjectsLocationsApisArtifactsDeleteCall) Header() http.Header
type ProjectsLocationsApisArtifactsGetCall
func (c *ProjectsLocationsApisArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsGetCall
func (c *ProjectsLocationsApisArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsGetCall
func (c *ProjectsLocationsApisArtifactsGetCall) Header() http.Header
func (c *ProjectsLocationsApisArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsGetCall
type ProjectsLocationsApisArtifactsGetContentsCall
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsGetContentsCall
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsGetContentsCall
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsApisArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsGetContentsCall
type ProjectsLocationsApisArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisArtifactsGetIamPolicyCall
type ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)
func (c *ProjectsLocationsApisArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) Filter(filter string) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) Header() http.Header
func (c *ProjectsLocationsApisArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisArtifactsListCall
func (c *ProjectsLocationsApisArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error
type ProjectsLocationsApisArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Header() http.Header
type ProjectsLocationsApisArtifactsService
func NewProjectsLocationsApisArtifactsService(s *Service) *ProjectsLocationsApisArtifactsService
func (r *ProjectsLocationsApisArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisArtifactsCreateCall
func (r *ProjectsLocationsApisArtifactsService) Delete(name string) *ProjectsLocationsApisArtifactsDeleteCall
func (r *ProjectsLocationsApisArtifactsService) Get(name string) *ProjectsLocationsApisArtifactsGetCall
func (r *ProjectsLocationsApisArtifactsService) GetContents(name string) *ProjectsLocationsApisArtifactsGetContentsCall
func (r *ProjectsLocationsApisArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsApisArtifactsGetIamPolicyCall
func (r *ProjectsLocationsApisArtifactsService) List(parent string) *ProjectsLocationsApisArtifactsListCall
func (r *ProjectsLocationsApisArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisArtifactsReplaceArtifactCall
func (r *ProjectsLocationsApisArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisArtifactsSetIamPolicyCall
func (r *ProjectsLocationsApisArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisArtifactsTestIamPermissionsCall
type ProjectsLocationsApisArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) ApiId(apiId string) *ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) Context(ctx context.Context) *ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) Do(opts ...googleapi.CallOption) (*Api, error)
func (c *ProjectsLocationsApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) Header() http.Header
type ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Force(force bool) *ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Header() http.Header
type ProjectsLocationsApisDeploymentsArtifactsCreateCall
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisDeploymentsArtifactsCreateCall
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsCreateCall
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsCreateCall
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Header() http.Header
type ProjectsLocationsApisDeploymentsArtifactsDeleteCall
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsDeleteCall
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsDeleteCall
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Header() http.Header
type ProjectsLocationsApisDeploymentsArtifactsGetCall
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsGetCall
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsGetCall
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsArtifactsGetCall
type ProjectsLocationsApisDeploymentsArtifactsGetContentsCall
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall
type ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Filter(filter string) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error
type ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Header() http.Header
type ProjectsLocationsApisDeploymentsArtifactsService
func NewProjectsLocationsApisDeploymentsArtifactsService(s *Service) *ProjectsLocationsApisDeploymentsArtifactsService
func (r *ProjectsLocationsApisDeploymentsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisDeploymentsArtifactsCreateCall
func (r *ProjectsLocationsApisDeploymentsArtifactsService) Delete(name string) *ProjectsLocationsApisDeploymentsArtifactsDeleteCall
func (r *ProjectsLocationsApisDeploymentsArtifactsService) Get(name string) *ProjectsLocationsApisDeploymentsArtifactsGetCall
func (r *ProjectsLocationsApisDeploymentsArtifactsService) GetContents(name string) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall
func (r *ProjectsLocationsApisDeploymentsArtifactsService) List(parent string) *ProjectsLocationsApisDeploymentsArtifactsListCall
func (r *ProjectsLocationsApisDeploymentsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall
type ProjectsLocationsApisDeploymentsCreateCall
func (c *ProjectsLocationsApisDeploymentsCreateCall) ApiDeploymentId(apiDeploymentId string) *ProjectsLocationsApisDeploymentsCreateCall
func (c *ProjectsLocationsApisDeploymentsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsCreateCall
func (c *ProjectsLocationsApisDeploymentsCreateCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)
func (c *ProjectsLocationsApisDeploymentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsCreateCall
func (c *ProjectsLocationsApisDeploymentsCreateCall) Header() http.Header
type ProjectsLocationsApisDeploymentsDeleteCall
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsDeleteCall
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsDeleteCall
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Force(force bool) *ProjectsLocationsApisDeploymentsDeleteCall
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Header() http.Header
type ProjectsLocationsApisDeploymentsDeleteRevisionCall
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsDeleteRevisionCall
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsDeleteRevisionCall
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Header() http.Header
type ProjectsLocationsApisDeploymentsGetCall
func (c *ProjectsLocationsApisDeploymentsGetCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsGetCall
func (c *ProjectsLocationsApisDeploymentsGetCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)
func (c *ProjectsLocationsApisDeploymentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsGetCall
func (c *ProjectsLocationsApisDeploymentsGetCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsGetCall
type ProjectsLocationsApisDeploymentsGetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsGetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsGetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsGetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisDeploymentsGetIamPolicyCall
type ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) Do(opts ...googleapi.CallOption) (*ListApiDeploymentsResponse, error)
func (c *ProjectsLocationsApisDeploymentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) Filter(filter string) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) OrderBy(orderBy string) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) PageSize(pageSize int64) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) PageToken(pageToken string) *ProjectsLocationsApisDeploymentsListCall
func (c *ProjectsLocationsApisDeploymentsListCall) Pages(ctx context.Context, f func(*ListApiDeploymentsResponse) error) error
type ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Do(opts ...googleapi.CallOption) (*ListApiDeploymentRevisionsResponse, error)
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Filter(filter string) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) PageSize(pageSize int64) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) PageToken(pageToken string) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Pages(ctx context.Context, f func(*ListApiDeploymentRevisionsResponse) error) error
type ProjectsLocationsApisDeploymentsPatchCall
func (c *ProjectsLocationsApisDeploymentsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisDeploymentsPatchCall
func (c *ProjectsLocationsApisDeploymentsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsPatchCall
func (c *ProjectsLocationsApisDeploymentsPatchCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)
func (c *ProjectsLocationsApisDeploymentsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsPatchCall
func (c *ProjectsLocationsApisDeploymentsPatchCall) Header() http.Header
func (c *ProjectsLocationsApisDeploymentsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisDeploymentsPatchCall
type ProjectsLocationsApisDeploymentsRollbackCall
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsRollbackCall
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsRollbackCall
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Header() http.Header
type ProjectsLocationsApisDeploymentsService
func NewProjectsLocationsApisDeploymentsService(s *Service) *ProjectsLocationsApisDeploymentsService
func (r *ProjectsLocationsApisDeploymentsService) Create(parent string, apideployment *ApiDeployment) *ProjectsLocationsApisDeploymentsCreateCall
func (r *ProjectsLocationsApisDeploymentsService) Delete(name string) *ProjectsLocationsApisDeploymentsDeleteCall
func (r *ProjectsLocationsApisDeploymentsService) DeleteRevision(name string) *ProjectsLocationsApisDeploymentsDeleteRevisionCall
func (r *ProjectsLocationsApisDeploymentsService) Get(name string) *ProjectsLocationsApisDeploymentsGetCall
func (r *ProjectsLocationsApisDeploymentsService) GetIamPolicy(resource string) *ProjectsLocationsApisDeploymentsGetIamPolicyCall
func (r *ProjectsLocationsApisDeploymentsService) List(parent string) *ProjectsLocationsApisDeploymentsListCall
func (r *ProjectsLocationsApisDeploymentsService) ListRevisions(name string) *ProjectsLocationsApisDeploymentsListRevisionsCall
func (r *ProjectsLocationsApisDeploymentsService) Patch(name string, apideployment *ApiDeployment) *ProjectsLocationsApisDeploymentsPatchCall
func (r *ProjectsLocationsApisDeploymentsService) Rollback(name string, rollbackapideploymentrequest *RollbackApiDeploymentRequest) *ProjectsLocationsApisDeploymentsRollbackCall
func (r *ProjectsLocationsApisDeploymentsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisDeploymentsSetIamPolicyCall
func (r *ProjectsLocationsApisDeploymentsService) TagRevision(name string, tagapideploymentrevisionrequest *TagApiDeploymentRevisionRequest) *ProjectsLocationsApisDeploymentsTagRevisionCall
func (r *ProjectsLocationsApisDeploymentsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisDeploymentsTestIamPermissionsCall
type ProjectsLocationsApisDeploymentsSetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsSetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsSetIamPolicyCall
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisDeploymentsTagRevisionCall
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsTagRevisionCall
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsTagRevisionCall
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Header() http.Header
type ProjectsLocationsApisDeploymentsTestIamPermissionsCall
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsTestIamPermissionsCall
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsTestIamPermissionsCall
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApisGetCall
func (c *ProjectsLocationsApisGetCall) Context(ctx context.Context) *ProjectsLocationsApisGetCall
func (c *ProjectsLocationsApisGetCall) Do(opts ...googleapi.CallOption) (*Api, error)
func (c *ProjectsLocationsApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetCall
func (c *ProjectsLocationsApisGetCall) Header() http.Header
func (c *ProjectsLocationsApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetCall
type ProjectsLocationsApisGetIamPolicyCall
func (c *ProjectsLocationsApisGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisGetIamPolicyCall
func (c *ProjectsLocationsApisGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetIamPolicyCall
func (c *ProjectsLocationsApisGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetIamPolicyCall
func (c *ProjectsLocationsApisGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisGetIamPolicyCall
type ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Context(ctx context.Context) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Do(opts ...googleapi.CallOption) (*ListApisResponse, error)
func (c *ProjectsLocationsApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Filter(filter string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Header() http.Header
func (c *ProjectsLocationsApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) OrderBy(orderBy string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) PageSize(pageSize int64) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) PageToken(pageToken string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Pages(ctx context.Context, f func(*ListApisResponse) error) error
type ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) Context(ctx context.Context) *ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) Do(opts ...googleapi.CallOption) (*Api, error)
func (c *ProjectsLocationsApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) Header() http.Header
func (c *ProjectsLocationsApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisPatchCall
type ProjectsLocationsApisService
func NewProjectsLocationsApisService(s *Service) *ProjectsLocationsApisService
func (r *ProjectsLocationsApisService) Create(parent string, api *Api) *ProjectsLocationsApisCreateCall
func (r *ProjectsLocationsApisService) Delete(name string) *ProjectsLocationsApisDeleteCall
func (r *ProjectsLocationsApisService) Get(name string) *ProjectsLocationsApisGetCall
func (r *ProjectsLocationsApisService) GetIamPolicy(resource string) *ProjectsLocationsApisGetIamPolicyCall
func (r *ProjectsLocationsApisService) List(parent string) *ProjectsLocationsApisListCall
func (r *ProjectsLocationsApisService) Patch(name string, api *Api) *ProjectsLocationsApisPatchCall
func (r *ProjectsLocationsApisService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisSetIamPolicyCall
func (r *ProjectsLocationsApisService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisTestIamPermissionsCall
type ProjectsLocationsApisSetIamPolicyCall
func (c *ProjectsLocationsApisSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisSetIamPolicyCall
func (c *ProjectsLocationsApisSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisSetIamPolicyCall
func (c *ProjectsLocationsApisSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisTestIamPermissionsCall
func (c *ProjectsLocationsApisTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisTestIamPermissionsCall
func (c *ProjectsLocationsApisTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisTestIamPermissionsCall
func (c *ProjectsLocationsApisTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApisVersionsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisVersionsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Header() http.Header
type ProjectsLocationsApisVersionsArtifactsDeleteCall
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsDeleteCall
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsDeleteCall
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsArtifactsGetCall
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsGetCall
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsGetCall
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsGetCall
type ProjectsLocationsApisVersionsArtifactsGetContentsCall
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsGetContentsCall
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsGetContentsCall
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsGetContentsCall
type ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall
type ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Filter(filter string) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsArtifactsListCall
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error
type ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Header() http.Header
type ProjectsLocationsApisVersionsArtifactsService
func NewProjectsLocationsApisVersionsArtifactsService(s *Service) *ProjectsLocationsApisVersionsArtifactsService
func (r *ProjectsLocationsApisVersionsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisVersionsArtifactsCreateCall
func (r *ProjectsLocationsApisVersionsArtifactsService) Delete(name string) *ProjectsLocationsApisVersionsArtifactsDeleteCall
func (r *ProjectsLocationsApisVersionsArtifactsService) Get(name string) *ProjectsLocationsApisVersionsArtifactsGetCall
func (r *ProjectsLocationsApisVersionsArtifactsService) GetContents(name string) *ProjectsLocationsApisVersionsArtifactsGetContentsCall
func (r *ProjectsLocationsApisVersionsArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall
func (r *ProjectsLocationsApisVersionsArtifactsService) List(parent string) *ProjectsLocationsApisVersionsArtifactsListCall
func (r *ProjectsLocationsApisVersionsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall
func (r *ProjectsLocationsApisVersionsArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall
func (r *ProjectsLocationsApisVersionsArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall
type ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) ApiVersionId(apiVersionId string) *ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) Do(opts ...googleapi.CallOption) (*ApiVersion, error)
func (c *ProjectsLocationsApisVersionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) Header() http.Header
type ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Force(force bool) *ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsGetCall
func (c *ProjectsLocationsApisVersionsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsGetCall
func (c *ProjectsLocationsApisVersionsGetCall) Do(opts ...googleapi.CallOption) (*ApiVersion, error)
func (c *ProjectsLocationsApisVersionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsGetCall
func (c *ProjectsLocationsApisVersionsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsGetCall
type ProjectsLocationsApisVersionsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsGetIamPolicyCall
type ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Do(opts ...googleapi.CallOption) (*ListApiVersionsResponse, error)
func (c *ProjectsLocationsApisVersionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Filter(filter string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Pages(ctx context.Context, f func(*ListApiVersionsResponse) error) error
type ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) Do(opts ...googleapi.CallOption) (*ApiVersion, error)
func (c *ProjectsLocationsApisVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsPatchCall
type ProjectsLocationsApisVersionsService
func NewProjectsLocationsApisVersionsService(s *Service) *ProjectsLocationsApisVersionsService
func (r *ProjectsLocationsApisVersionsService) Create(parent string, apiversion *ApiVersion) *ProjectsLocationsApisVersionsCreateCall
func (r *ProjectsLocationsApisVersionsService) Delete(name string) *ProjectsLocationsApisVersionsDeleteCall
func (r *ProjectsLocationsApisVersionsService) Get(name string) *ProjectsLocationsApisVersionsGetCall
func (r *ProjectsLocationsApisVersionsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsGetIamPolicyCall
func (r *ProjectsLocationsApisVersionsService) List(parent string) *ProjectsLocationsApisVersionsListCall
func (r *ProjectsLocationsApisVersionsService) Patch(name string, apiversion *ApiVersion) *ProjectsLocationsApisVersionsPatchCall
func (r *ProjectsLocationsApisVersionsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsSetIamPolicyCall
func (r *ProjectsLocationsApisVersionsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsTestIamPermissionsCall
type ProjectsLocationsApisVersionsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsArtifactsGetCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall
type ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall
type ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall
type ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error
type ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsArtifactsService
func NewProjectsLocationsApisVersionsSpecsArtifactsService(s *Service) *ProjectsLocationsApisVersionsSpecsArtifactsService
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) Delete(name string) *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) Get(name string) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) GetContents(name string) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) List(parent string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall
type ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) ApiSpecId(apiSpecId string) *ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Force(force bool) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsDeleteRevisionCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsGetCall
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetCall
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetCall
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetCall
type ProjectsLocationsApisVersionsSpecsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetContentsCall
type ProjectsLocationsApisVersionsSpecsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall
type ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Do(opts ...googleapi.CallOption) (*ListApiSpecsResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Pages(ctx context.Context, f func(*ListApiSpecsResponse) error) error
type ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Do(opts ...googleapi.CallOption) (*ListApiSpecRevisionsResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Pages(ctx context.Context, f func(*ListApiSpecRevisionsResponse) error) error
type ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsSpecsPatchCall
type ProjectsLocationsApisVersionsSpecsRollbackCall
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsRollbackCall
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsRollbackCall
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsService
func NewProjectsLocationsApisVersionsSpecsService(s *Service) *ProjectsLocationsApisVersionsSpecsService
func (r *ProjectsLocationsApisVersionsSpecsService) Create(parent string, apispec *ApiSpec) *ProjectsLocationsApisVersionsSpecsCreateCall
func (r *ProjectsLocationsApisVersionsSpecsService) Delete(name string) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (r *ProjectsLocationsApisVersionsSpecsService) DeleteRevision(name string) *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall
func (r *ProjectsLocationsApisVersionsSpecsService) Get(name string) *ProjectsLocationsApisVersionsSpecsGetCall
func (r *ProjectsLocationsApisVersionsSpecsService) GetContents(name string) *ProjectsLocationsApisVersionsSpecsGetContentsCall
func (r *ProjectsLocationsApisVersionsSpecsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall
func (r *ProjectsLocationsApisVersionsSpecsService) List(parent string) *ProjectsLocationsApisVersionsSpecsListCall
func (r *ProjectsLocationsApisVersionsSpecsService) ListRevisions(name string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall
func (r *ProjectsLocationsApisVersionsSpecsService) Patch(name string, apispec *ApiSpec) *ProjectsLocationsApisVersionsSpecsPatchCall
func (r *ProjectsLocationsApisVersionsSpecsService) Rollback(name string, rollbackapispecrequest *RollbackApiSpecRequest) *ProjectsLocationsApisVersionsSpecsRollbackCall
func (r *ProjectsLocationsApisVersionsSpecsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall
func (r *ProjectsLocationsApisVersionsSpecsService) TagRevision(name string, tagapispecrevisionrequest *TagApiSpecRevisionRequest) *ProjectsLocationsApisVersionsSpecsTagRevisionCall
func (r *ProjectsLocationsApisVersionsSpecsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall
type ProjectsLocationsApisVersionsSpecsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsTagRevisionCall
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsTagRevisionCall
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsTagRevisionCall
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApisVersionsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsTestIamPermissionsCall
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsArtifactsCreateCall
func (c *ProjectsLocationsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsArtifactsCreateCall
func (c *ProjectsLocationsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsArtifactsCreateCall
func (c *ProjectsLocationsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsCreateCall
func (c *ProjectsLocationsArtifactsCreateCall) Header() http.Header
type ProjectsLocationsArtifactsDeleteCall
func (c *ProjectsLocationsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsArtifactsDeleteCall
func (c *ProjectsLocationsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsDeleteCall
func (c *ProjectsLocationsArtifactsDeleteCall) Header() http.Header
type ProjectsLocationsArtifactsGetCall
func (c *ProjectsLocationsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsArtifactsGetCall
func (c *ProjectsLocationsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsGetCall
func (c *ProjectsLocationsArtifactsGetCall) Header() http.Header
func (c *ProjectsLocationsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsGetCall
type ProjectsLocationsArtifactsGetContentsCall
func (c *ProjectsLocationsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsArtifactsGetContentsCall
func (c *ProjectsLocationsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)
func (c *ProjectsLocationsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsGetContentsCall
func (c *ProjectsLocationsArtifactsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsGetContentsCall
type ProjectsLocationsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsGetIamPolicyCall
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsArtifactsGetIamPolicyCall
type ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)
func (c *ProjectsLocationsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) Filter(filter string) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) Header() http.Header
func (c *ProjectsLocationsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsArtifactsListCall
func (c *ProjectsLocationsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error
type ProjectsLocationsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsReplaceArtifactCall
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Header() http.Header
type ProjectsLocationsArtifactsService
func NewProjectsLocationsArtifactsService(s *Service) *ProjectsLocationsArtifactsService
func (r *ProjectsLocationsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsArtifactsCreateCall
func (r *ProjectsLocationsArtifactsService) Delete(name string) *ProjectsLocationsArtifactsDeleteCall
func (r *ProjectsLocationsArtifactsService) Get(name string) *ProjectsLocationsArtifactsGetCall
func (r *ProjectsLocationsArtifactsService) GetContents(name string) *ProjectsLocationsArtifactsGetContentsCall
func (r *ProjectsLocationsArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsArtifactsGetIamPolicyCall
func (r *ProjectsLocationsArtifactsService) List(parent string) *ProjectsLocationsArtifactsListCall
func (r *ProjectsLocationsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsArtifactsReplaceArtifactCall
func (r *ProjectsLocationsArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsArtifactsSetIamPolicyCall
func (r *ProjectsLocationsArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsArtifactsTestIamPermissionsCall
type ProjectsLocationsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsSetIamPolicyCall
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsTestIamPermissionsCall
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsDocumentsGetIamPolicyCall
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsDocumentsGetIamPolicyCall
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsDocumentsGetIamPolicyCall
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsDocumentsGetIamPolicyCall
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsDocumentsGetIamPolicyCall
type ProjectsLocationsDocumentsService
func NewProjectsLocationsDocumentsService(s *Service) *ProjectsLocationsDocumentsService
func (r *ProjectsLocationsDocumentsService) GetIamPolicy(resource string) *ProjectsLocationsDocumentsGetIamPolicyCall
func (r *ProjectsLocationsDocumentsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsDocumentsSetIamPolicyCall
func (r *ProjectsLocationsDocumentsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsDocumentsTestIamPermissionsCall
type ProjectsLocationsDocumentsSetIamPolicyCall
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsDocumentsSetIamPolicyCall
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsDocumentsSetIamPolicyCall
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsDocumentsTestIamPermissionsCall
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsDocumentsTestIamPermissionsCall
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsDocumentsTestIamPermissionsCall
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsInstancesCreateCall
func (c *ProjectsLocationsInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsInstancesCreateCall
func (c *ProjectsLocationsInstancesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesCreateCall
func (c *ProjectsLocationsInstancesCreateCall) Header() http.Header
func (c *ProjectsLocationsInstancesCreateCall) InstanceId(instanceId string) *ProjectsLocationsInstancesCreateCall
type ProjectsLocationsInstancesDeleteCall
func (c *ProjectsLocationsInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsInstancesDeleteCall
func (c *ProjectsLocationsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDeleteCall
func (c *ProjectsLocationsInstancesDeleteCall) Header() http.Header
type ProjectsLocationsInstancesGetCall
func (c *ProjectsLocationsInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsInstancesGetCall
func (c *ProjectsLocationsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *ProjectsLocationsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesGetCall
func (c *ProjectsLocationsInstancesGetCall) Header() http.Header
func (c *ProjectsLocationsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesGetCall
type ProjectsLocationsInstancesGetIamPolicyCall
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsInstancesGetIamPolicyCall
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesGetIamPolicyCall
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsInstancesGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesGetIamPolicyCall
func (c *ProjectsLocationsInstancesGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsInstancesGetIamPolicyCall
type ProjectsLocationsInstancesService
func NewProjectsLocationsInstancesService(s *Service) *ProjectsLocationsInstancesService
func (r *ProjectsLocationsInstancesService) Create(parent string, instance *Instance) *ProjectsLocationsInstancesCreateCall
func (r *ProjectsLocationsInstancesService) Delete(name string) *ProjectsLocationsInstancesDeleteCall
func (r *ProjectsLocationsInstancesService) Get(name string) *ProjectsLocationsInstancesGetCall
func (r *ProjectsLocationsInstancesService) GetIamPolicy(resource string) *ProjectsLocationsInstancesGetIamPolicyCall
func (r *ProjectsLocationsInstancesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsInstancesSetIamPolicyCall
func (r *ProjectsLocationsInstancesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsInstancesTestIamPermissionsCall
type ProjectsLocationsInstancesSetIamPolicyCall
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsInstancesSetIamPolicyCall
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesSetIamPolicyCall
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Header() http.Header
type ProjectsLocationsInstancesTestIamPermissionsCall
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsInstancesTestIamPermissionsCall
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesTestIamPermissionsCall
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Header() http.Header
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error
type ProjectsLocationsOperationsCancelCall
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall
func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header
type ProjectsLocationsOperationsDeleteCall
func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall
func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall
func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header
type ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)
func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Header() http.Header
func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error
type ProjectsLocationsOperationsService
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall
func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall
func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall
type ProjectsLocationsRuntimeGetIamPolicyCall
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRuntimeGetIamPolicyCall
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeGetIamPolicyCall
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsRuntimeGetIamPolicyCall
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsRuntimeGetIamPolicyCall
type ProjectsLocationsRuntimeService
func NewProjectsLocationsRuntimeService(s *Service) *ProjectsLocationsRuntimeService
func (r *ProjectsLocationsRuntimeService) GetIamPolicy(resource string) *ProjectsLocationsRuntimeGetIamPolicyCall
func (r *ProjectsLocationsRuntimeService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsRuntimeSetIamPolicyCall
func (r *ProjectsLocationsRuntimeService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsRuntimeTestIamPermissionsCall
type ProjectsLocationsRuntimeSetIamPolicyCall
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRuntimeSetIamPolicyCall
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeSetIamPolicyCall
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Header() http.Header
type ProjectsLocationsRuntimeTestIamPermissionsCall
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsRuntimeTestIamPermissionsCall
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeTestIamPermissionsCall
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type RollbackApiDeploymentRequest
func (s RollbackApiDeploymentRequest) MarshalJSON() ([]byte, error)
type RollbackApiSpecRequest
func (s RollbackApiSpecRequest) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SetIamPolicyRequest
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type TagApiDeploymentRevisionRequest
func (s TagApiDeploymentRevisionRequest) MarshalJSON() ([]byte, error)
type TagApiSpecRevisionRequest
func (s TagApiSpecRevisionRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// See, edit, configure, and delete your Google Cloud data and see the email
	// address for your Google Account.
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type Api ¶
type Api struct {
	// Annotations: Annotations attach non-identifying metadata to resources.
	// Annotation keys and values are less restricted than those of labels, but
	// should be generally used for small values of broad interest. Larger, topic-
	// specific metadata should be stored in Artifacts.
	Annotations map[string]string `json:"annotations,omitempty"`
	// Availability: A user-definable description of the availability of this
	// service. Format: free-form, but we expect single words that describe
	// availability, e.g., "NONE", "TESTING", "PREVIEW", "GENERAL", "DEPRECATED",
	// "SHUTDOWN".
	Availability string `json:"availability,omitempty"`
	// CreateTime: Output only. Creation timestamp.
	CreateTime string `json:"createTime,omitempty"`
	// Description: A detailed description.
	Description string `json:"description,omitempty"`
	// DisplayName: Human-meaningful name.
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Labels attach identifying metadata to resources. Identifying
	// metadata can be used to filter list operations. Label keys and values can be
	// no longer than 64 characters (Unicode codepoints), can only contain
	// lowercase letters, numeric characters, underscores, and dashes.
	// International characters are allowed. No more than 64 user labels can be
	// associated with one resource (System labels are excluded). See
	// https://goo.gl/xmQnxf for more information and examples of labels. System
	// reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and
	// cannot be changed.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Resource name.
	Name string `json:"name,omitempty"`
	// RecommendedDeployment: The recommended deployment of the API. Format:
	// `projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}`
	RecommendedDeployment string `json:"recommendedDeployment,omitempty"`
	// RecommendedVersion: The recommended version of the API. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}`
	RecommendedVersion string `json:"recommendedVersion,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
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

Api: A top-level description of an API. Produced by producers and are commitments to provide services.

func (Api) MarshalJSON ¶
func (s Api) MarshalJSON() ([]byte, error)
type ApiDeployment ¶
type ApiDeployment struct {
	// AccessGuidance: Text briefly describing how to access the endpoint. Changes
	// to this value will not affect the revision.
	AccessGuidance string `json:"accessGuidance,omitempty"`
	// Annotations: Annotations attach non-identifying metadata to resources.
	// Annotation keys and values are less restricted than those of labels, but
	// should be generally used for small values of broad interest. Larger, topic-
	// specific metadata should be stored in Artifacts.
	Annotations map[string]string `json:"annotations,omitempty"`
	// ApiSpecRevision: The full resource name (including revision ID) of the spec
	// of the API being served by the deployment. Changes to this value will update
	// the revision. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/
	// {spec@revision}`
	ApiSpecRevision string `json:"apiSpecRevision,omitempty"`
	// CreateTime: Output only. Creation timestamp; when the deployment resource
	// was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: A detailed description.
	Description string `json:"description,omitempty"`
	// DisplayName: Human-meaningful name.
	DisplayName string `json:"displayName,omitempty"`
	// EndpointUri: The address where the deployment is serving. Changes to this
	// value will update the revision.
	EndpointUri string `json:"endpointUri,omitempty"`
	// ExternalChannelUri: The address of the external channel of the API (e.g.,
	// the Developer Portal). Changes to this value will not affect the revision.
	ExternalChannelUri string `json:"externalChannelUri,omitempty"`
	// IntendedAudience: Text briefly identifying the intended audience of the API.
	// Changes to this value will not affect the revision.
	IntendedAudience string `json:"intendedAudience,omitempty"`
	// Labels: Labels attach identifying metadata to resources. Identifying
	// metadata can be used to filter list operations. Label keys and values can be
	// no longer than 64 characters (Unicode codepoints), can only contain
	// lowercase letters, numeric characters, underscores and dashes. International
	// characters are allowed. No more than 64 user labels can be associated with
	// one resource (System labels are excluded). See https://goo.gl/xmQnxf for
	// more information and examples of labels. System reserved label keys are
	// prefixed with `apigeeregistry.googleapis.com/` and cannot be changed.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Resource name.
	Name string `json:"name,omitempty"`
	// RevisionCreateTime: Output only. Revision creation timestamp; when the
	// represented revision was created.
	RevisionCreateTime string `json:"revisionCreateTime,omitempty"`
	// RevisionId: Output only. Immutable. The revision ID of the deployment. A new
	// revision is committed whenever the deployment contents are changed. The
	// format is an 8-character hexadecimal string.
	RevisionId string `json:"revisionId,omitempty"`
	// RevisionUpdateTime: Output only. Last update timestamp: when the represented
	// revision was last modified.
	RevisionUpdateTime string `json:"revisionUpdateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessGuidance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessGuidance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApiDeployment: Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.

func (ApiDeployment) MarshalJSON ¶
func (s ApiDeployment) MarshalJSON() ([]byte, error)
type ApiSpec ¶
type ApiSpec struct {
	// Annotations: Annotations attach non-identifying metadata to resources.
	// Annotation keys and values are less restricted than those of labels, but
	// should be generally used for small values of broad interest. Larger, topic-
	// specific metadata should be stored in Artifacts.
	Annotations map[string]string `json:"annotations,omitempty"`
	// Contents: Input only. The contents of the spec. Provided by API callers when
	// specs are created or updated. To access the contents of a spec, use
	// GetApiSpecContents.
	Contents string `json:"contents,omitempty"`
	// CreateTime: Output only. Creation timestamp; when the spec resource was
	// created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: A detailed description.
	Description string `json:"description,omitempty"`
	// Filename: A possibly-hierarchical name used to refer to the spec from other
	// specs.
	Filename string `json:"filename,omitempty"`
	// Hash: Output only. A SHA-256 hash of the spec's contents. If the spec is
	// gzipped, this is the hash of the uncompressed spec.
	Hash string `json:"hash,omitempty"`
	// Labels: Labels attach identifying metadata to resources. Identifying
	// metadata can be used to filter list operations. Label keys and values can be
	// no longer than 64 characters (Unicode codepoints), can only contain
	// lowercase letters, numeric characters, underscores and dashes. International
	// characters are allowed. No more than 64 user labels can be associated with
	// one resource (System labels are excluded). See https://goo.gl/xmQnxf for
	// more information and examples of labels. System reserved label keys are
	// prefixed with `apigeeregistry.googleapis.com/` and cannot be changed.
	Labels map[string]string `json:"labels,omitempty"`
	// MimeType: A style (format) descriptor for this spec that is specified as a
	// Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values
	// include `application/vnd.apigee.proto`, `application/vnd.apigee.openapi`,
	// and `application/vnd.apigee.graphql`, with possible suffixes representing
	// compression types. These hypothetical names are defined in the vendor tree
	// defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final.
	// Content types can specify compression. Currently only GZip compression is
	// supported (indicated with "+gzip").
	MimeType string `json:"mimeType,omitempty"`
	// Name: Resource name.
	Name string `json:"name,omitempty"`
	// RevisionCreateTime: Output only. Revision creation timestamp; when the
	// represented revision was created.
	RevisionCreateTime string `json:"revisionCreateTime,omitempty"`
	// RevisionId: Output only. Immutable. The revision ID of the spec. A new
	// revision is committed whenever the spec contents are changed. The format is
	// an 8-character hexadecimal string.
	RevisionId string `json:"revisionId,omitempty"`
	// RevisionUpdateTime: Output only. Last update timestamp: when the represented
	// revision was last modified.
	RevisionUpdateTime string `json:"revisionUpdateTime,omitempty"`
	// SizeBytes: Output only. The size of the spec file in bytes. If the spec is
	// gzipped, this is the size of the uncompressed spec.
	SizeBytes int64 `json:"sizeBytes,omitempty"`
	// SourceUri: The original source URI of the spec (if one exists). This is an
	// external location that can be used for reference purposes but which may not
	// be authoritative since this external resource may change after the spec is
	// retrieved.
	SourceUri string `json:"sourceUri,omitempty"`

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

ApiSpec: Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.

func (ApiSpec) MarshalJSON ¶
func (s ApiSpec) MarshalJSON() ([]byte, error)
type ApiVersion ¶
type ApiVersion struct {
	// Annotations: Annotations attach non-identifying metadata to resources.
	// Annotation keys and values are less restricted than those of labels, but
	// should be generally used for small values of broad interest. Larger, topic-
	// specific metadata should be stored in Artifacts.
	Annotations map[string]string `json:"annotations,omitempty"`
	// CreateTime: Output only. Creation timestamp.
	CreateTime string `json:"createTime,omitempty"`
	// Description: A detailed description.
	Description string `json:"description,omitempty"`
	// DisplayName: Human-meaningful name.
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Labels attach identifying metadata to resources. Identifying
	// metadata can be used to filter list operations. Label keys and values can be
	// no longer than 64 characters (Unicode codepoints), can only contain
	// lowercase letters, numeric characters, underscores and dashes. International
	// characters are allowed. No more than 64 user labels can be associated with
	// one resource (System labels are excluded). See https://goo.gl/xmQnxf for
	// more information and examples of labels. System reserved label keys are
	// prefixed with `apigeeregistry.googleapis.com/` and cannot be changed.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Resource name.
	Name string `json:"name,omitempty"`
	// PrimarySpec: The primary spec for this version. Format:
	// projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{
	// spec}
	PrimarySpec string `json:"primarySpec,omitempty"`
	// State: A user-definable description of the lifecycle phase of this API
	// version. Format: free-form, but we expect single words that describe API
	// maturity, e.g., "CONCEPT", "DESIGN", "DEVELOPMENT", "STAGING", "PRODUCTION",
	// "DEPRECATED", "RETIRED".
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
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

ApiVersion: Describes a particular version of an API. ApiVersions are what consumers actually use.

func (ApiVersion) MarshalJSON ¶
func (s ApiVersion) MarshalJSON() ([]byte, error)
type Artifact ¶
type Artifact struct {
	// Annotations: Annotations attach non-identifying metadata to resources.
	// Annotation keys and values are less restricted than those of labels, but
	// should be generally used for small values of broad interest. Larger, topic-
	// specific metadata should be stored in Artifacts.
	Annotations map[string]string `json:"annotations,omitempty"`
	// Contents: Input only. The contents of the artifact. Provided by API callers
	// when artifacts are created or replaced. To access the contents of an
	// artifact, use GetArtifactContents.
	Contents string `json:"contents,omitempty"`
	// CreateTime: Output only. Creation timestamp.
	CreateTime string `json:"createTime,omitempty"`
	// Hash: Output only. A SHA-256 hash of the artifact's contents. If the
	// artifact is gzipped, this is the hash of the uncompressed artifact.
	Hash string `json:"hash,omitempty"`
	// Labels: Labels attach identifying metadata to resources. Identifying
	// metadata can be used to filter list operations. Label keys and values can be
	// no longer than 64 characters (Unicode codepoints), can only contain
	// lowercase letters, numeric characters, underscores and dashes. International
	// characters are allowed. No more than 64 user labels can be associated with
	// one resource (System labels are excluded). See https://goo.gl/xmQnxf for
	// more information and examples of labels. System reserved label keys are
	// prefixed with "registry.googleapis.com/" and cannot be changed.
	Labels map[string]string `json:"labels,omitempty"`
	// MimeType: A content type specifier for the artifact. Content type specifiers
	// are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible
	// "schema" parameter that specifies a schema for the stored information.
	// Content types can specify compression. Currently only GZip compression is
	// supported (indicated with "+gzip").
	MimeType string `json:"mimeType,omitempty"`
	// Name: Resource name.
	Name string `json:"name,omitempty"`
	// SizeBytes: Output only. The size of the artifact in bytes. If the artifact
	// is gzipped, this is the size of the uncompressed artifact.
	SizeBytes int64 `json:"sizeBytes,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
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

Artifact: Artifacts of resources. Artifacts are unique (single-value) per resource and are used to store metadata that is too large or numerous to be stored directly on the resource. Since artifacts are stored separately from parent resources, they should generally be used for metadata that is needed infrequently, i.e., not for display in primary views of the resource but perhaps displayed or downloaded upon request. The `ListArtifacts` method allows artifacts to be quickly enumerated and checked for presence without downloading their (potentially-large) contents.

func (Artifact) MarshalJSON ¶
func (s Artifact) MarshalJSON() ([]byte, error)
type Binding ¶
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
	// `google.com` or `example.com`. * `deleted:user:{emailid}?uid={uniqueid}`: An
	// email address (plus unique identifier) representing a user that has been
	// recently deleted. For example,
	// `alice@example.com?uid=123456789012345678901`. If the user is recovered,
	// this value reverts to `user:{emailid}` and the recovered user retains the
	// role in the binding. * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An
	// email address (plus unique identifier) representing a service account that
	// has been recently deleted. For example,
	// `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the
	// service account is undeleted, this value reverts to
	// `serviceAccount:{emailid}` and the undeleted service account retains the
	// role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An email
	// address (plus unique identifier) representing a Google group that has been
	// recently deleted. For example,
	// `admins@example.com?uid=123456789012345678901`. If the group is recovered,
	// this value reverts to `group:{emailid}` and the recovered group retains the
	// role in the binding.
	Members []string `json:"members,omitempty"`
	// Role: Role that is assigned to the list of `members`, or principals. For
	// example, `roles/viewer`, `roles/editor`, or `roles/owner`.
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
func (s Binding) MarshalJSON() ([]byte, error)
type Build ¶
added in v0.110.0
type Build struct {
	// CommitId: Output only. Commit ID of the latest commit in the build.
	CommitId string `json:"commitId,omitempty"`
	// CommitTime: Output only. Commit time of the latest commit in the build.
	CommitTime string `json:"commitTime,omitempty"`
	// Repo: Output only. Path of the open source repository:
	// github.com/apigee/registry.
	Repo string `json:"repo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CommitId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CommitId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Build: Build information of the Instance if it's in `ACTIVE` state.

func (Build) MarshalJSON ¶
added in v0.110.0
func (s Build) MarshalJSON() ([]byte, error)
type CancelOperationRequest ¶
type CancelOperationRequest struct {
}

CancelOperationRequest: The request message for Operations.CancelOperation.

type Config ¶
type Config struct {
	// CmekKeyName: Required. The Customer Managed Encryption Key (CMEK) used for
	// data encryption. The CMEK name should follow the format of
	// `projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)`,
	// where the `location` must match InstanceConfig.location.
	CmekKeyName string `json:"cmekKeyName,omitempty"`
	// Location: Output only. The GCP location where the Instance resides.
	Location string `json:"location,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CmekKeyName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CmekKeyName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Config: Available configurations to provision an Instance.

func (Config) MarshalJSON ¶
func (s Config) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type Expr ¶
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
func (s Expr) MarshalJSON() ([]byte, error)
type HttpBody ¶
type HttpBody struct {
	// ContentType: The HTTP Content-Type header value specifying the content type
	// of the body.
	ContentType string `json:"contentType,omitempty"`
	// Data: The HTTP request/response body as raw binary.
	Data string `json:"data,omitempty"`
	// Extensions: Application specific response metadata. Must be set in the first
	// response for streaming APIs.
	Extensions []googleapi.RawMessage `json:"extensions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ContentType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ContentType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

HttpBody: Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example: message GetResourceRequest { // A unique request id. string request_id = 1; // The raw HTTP body is bound to this field. google.api.HttpBody http_body = 2; } service ResourceService { rpc GetResource(GetResourceRequest) returns (google.api.HttpBody); rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty); } Example with streaming methods: service CaldavService { rpc GetCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); rpc UpdateCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); } Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

func (HttpBody) MarshalJSON ¶
func (s HttpBody) MarshalJSON() ([]byte, error)
type Instance ¶
type Instance struct {
	// Build: Output only. Build info of the Instance if it's in `ACTIVE` state.
	Build *Build `json:"build,omitempty"`
	// Config: Required. Config of the Instance.
	Config *Config `json:"config,omitempty"`
	// CreateTime: Output only. Creation timestamp.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Format: `projects/*/locations/*/instance`. Currently only
	// `locations/global` is supported.
	Name string `json:"name,omitempty"`
	// State: Output only. The current state of the Instance.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The default value. This value is used if the state
	// is omitted.
	//   "INACTIVE" - The Instance has not been initialized or has been deleted.
	//   "CREATING" - The Instance is being created.
	//   "ACTIVE" - The Instance has been created and is ready for use.
	//   "UPDATING" - The Instance is being updated.
	//   "DELETING" - The Instance is being deleted.
	//   "FAILED" - The Instance encountered an error during a state change.
	State string `json:"state,omitempty"`
	// StateMessage: Output only. Extra information of Instance.State if the state
	// is `FAILED`.
	StateMessage string `json:"stateMessage,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Build") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Build") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Instance: An Instance represents the instance resources of the Registry. Currently, only one instance is allowed for each project.

func (Instance) MarshalJSON ¶
func (s Instance) MarshalJSON() ([]byte, error)
type ListApiDeploymentRevisionsResponse ¶
type ListApiDeploymentRevisionsResponse struct {
	// ApiDeployments: The revisions of the deployment.
	ApiDeployments []*ApiDeployment `json:"apiDeployments,omitempty"`
	// NextPageToken: A token that can be sent as `page_token` to retrieve the next
	// page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiDeployments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiDeployments") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApiDeploymentRevisionsResponse: Response message for ListApiDeploymentRevisionsResponse.

func (ListApiDeploymentRevisionsResponse) MarshalJSON ¶
func (s ListApiDeploymentRevisionsResponse) MarshalJSON() ([]byte, error)
type ListApiDeploymentsResponse ¶
type ListApiDeploymentsResponse struct {
	// ApiDeployments: The deployments from the specified publisher.
	ApiDeployments []*ApiDeployment `json:"apiDeployments,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiDeployments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiDeployments") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApiDeploymentsResponse: Response message for ListApiDeployments.

func (ListApiDeploymentsResponse) MarshalJSON ¶
func (s ListApiDeploymentsResponse) MarshalJSON() ([]byte, error)
type ListApiSpecRevisionsResponse ¶
type ListApiSpecRevisionsResponse struct {
	// ApiSpecs: The revisions of the spec.
	ApiSpecs []*ApiSpec `json:"apiSpecs,omitempty"`
	// NextPageToken: A token that can be sent as `page_token` to retrieve the next
	// page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiSpecs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiSpecs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApiSpecRevisionsResponse: Response message for ListApiSpecRevisionsResponse.

func (ListApiSpecRevisionsResponse) MarshalJSON ¶
func (s ListApiSpecRevisionsResponse) MarshalJSON() ([]byte, error)
type ListApiSpecsResponse ¶
type ListApiSpecsResponse struct {
	// ApiSpecs: The specs from the specified publisher.
	ApiSpecs []*ApiSpec `json:"apiSpecs,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiSpecs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiSpecs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApiSpecsResponse: Response message for ListApiSpecs.

func (ListApiSpecsResponse) MarshalJSON ¶
func (s ListApiSpecsResponse) MarshalJSON() ([]byte, error)
type ListApiVersionsResponse ¶
type ListApiVersionsResponse struct {
	// ApiVersions: The versions from the specified publisher.
	ApiVersions []*ApiVersion `json:"apiVersions,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiVersions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApiVersionsResponse: Response message for ListApiVersions.

func (ListApiVersionsResponse) MarshalJSON ¶
func (s ListApiVersionsResponse) MarshalJSON() ([]byte, error)
type ListApisResponse ¶
type ListApisResponse struct {
	// Apis: The APIs from the specified publisher.
	Apis []*Api `json:"apis,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Apis") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Apis") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApisResponse: Response message for ListApis.

func (ListApisResponse) MarshalJSON ¶
func (s ListApisResponse) MarshalJSON() ([]byte, error)
type ListArtifactsResponse ¶
type ListArtifactsResponse struct {
	// Artifacts: The artifacts from the specified publisher.
	Artifacts []*Artifact `json:"artifacts,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Artifacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Artifacts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListArtifactsResponse: Response message for ListArtifacts.

func (ListArtifactsResponse) MarshalJSON ¶
func (s ListArtifactsResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse ¶
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
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse ¶
type ListOperationsResponse struct {
	// NextPageToken: The standard List next-page token.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Operations: A list of operations that matches the specified filter in the
	// request.
	Operations []*Operation `json:"operations,omitempty"`

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

ListOperationsResponse: The response message for Operations.ListOperations.

func (ListOperationsResponse) MarshalJSON ¶
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type Location ¶
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
func (s Location) MarshalJSON() ([]byte, error)
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
type OperationMetadata struct {
	// ApiVersion: API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CancellationRequested: Identifies whether the user has requested
	// cancellation of the operation. Operations that have successfully been
	// cancelled have Operation.error value with a google.rpc.Status.code of 1,
	// corresponding to `Code.CANCELLED`.
	CancellationRequested bool `json:"cancellationRequested,omitempty"`
	// CreateTime: The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// StatusMessage: Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Server-defined resource path for the target of the operation.
	Target string `json:"target,omitempty"`
	// Verb: Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OperationMetadata: Represents the metadata of the long-running operation.

func (OperationMetadata) MarshalJSON ¶
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type Policy ¶
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
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsLocationsApisArtifactsCreateCall ¶
type ProjectsLocationsApisArtifactsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsCreateCall) ArtifactId ¶
func (c *ProjectsLocationsApisArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisArtifactsCreateCall

ArtifactId sets the optional parameter "artifactId": Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisArtifactsCreateCall) Context ¶
func (c *ProjectsLocationsApisArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsCreateCall) Do ¶
func (c *ProjectsLocationsApisArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.create" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsCreateCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsCreateCall) Header ¶
func (c *ProjectsLocationsApisArtifactsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisArtifactsDeleteCall ¶
type ProjectsLocationsApisArtifactsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsDeleteCall) Context ¶
func (c *ProjectsLocationsApisArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsDeleteCall) Do ¶
func (c *ProjectsLocationsApisArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsDeleteCall) Header ¶
func (c *ProjectsLocationsApisArtifactsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisArtifactsGetCall ¶
type ProjectsLocationsApisArtifactsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsGetCall) Context ¶
func (c *ProjectsLocationsApisArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsGetCall) Do ¶
func (c *ProjectsLocationsApisArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.get" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsGetCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsGetCall) Header ¶
func (c *ProjectsLocationsApisArtifactsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisArtifactsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisArtifactsGetContentsCall ¶
type ProjectsLocationsApisArtifactsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsGetContentsCall) Context ¶
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsGetContentsCall) Do ¶
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.getContents" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsGetContentsCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsGetContentsCall) Header ¶
func (c *ProjectsLocationsApisArtifactsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisArtifactsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisArtifactsGetIamPolicyCall ¶
type ProjectsLocationsApisArtifactsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisArtifactsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisArtifactsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisArtifactsListCall ¶
type ProjectsLocationsApisArtifactsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsListCall) Context ¶
func (c *ProjectsLocationsApisArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsListCall) Do ¶
func (c *ProjectsLocationsApisArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.list" call. Any non-2xx status code is an error. Response headers are in either *ListArtifactsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsListCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsListCall) Filter ¶
func (c *ProjectsLocationsApisArtifactsListCall) Filter(filter string) *ProjectsLocationsApisArtifactsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.

func (*ProjectsLocationsApisArtifactsListCall) Header ¶
func (c *ProjectsLocationsApisArtifactsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisArtifactsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisArtifactsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisArtifactsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisArtifactsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisArtifactsListCall) PageSize ¶
func (c *ProjectsLocationsApisArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisArtifactsListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisArtifactsListCall) PageToken ¶
func (c *ProjectsLocationsApisArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisArtifactsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token.

func (*ProjectsLocationsApisArtifactsListCall) Pages ¶
func (c *ProjectsLocationsApisArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisArtifactsReplaceArtifactCall ¶
type ProjectsLocationsApisArtifactsReplaceArtifactCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsReplaceArtifactCall) Context ¶
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsReplaceArtifactCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsReplaceArtifactCall) Do ¶
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.replaceArtifact" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsReplaceArtifactCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsReplaceArtifactCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsReplaceArtifactCall) Header ¶
func (c *ProjectsLocationsApisArtifactsReplaceArtifactCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisArtifactsService ¶
type ProjectsLocationsApisArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisArtifactsService ¶
func NewProjectsLocationsApisArtifactsService(s *Service) *ProjectsLocationsApisArtifactsService
func (*ProjectsLocationsApisArtifactsService) Create ¶
func (r *ProjectsLocationsApisArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisArtifactsCreateCall

Create: Creates a specified artifact.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisArtifactsService) Delete ¶
func (r *ProjectsLocationsApisArtifactsService) Delete(name string) *ProjectsLocationsApisArtifactsDeleteCall

Delete: Removes a specified artifact.

- name: The name of the artifact to delete. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisArtifactsService) Get ¶
func (r *ProjectsLocationsApisArtifactsService) Get(name string) *ProjectsLocationsApisArtifactsGetCall

Get: Returns a specified artifact.

- name: The name of the artifact to retrieve. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisArtifactsService) GetContents ¶
func (r *ProjectsLocationsApisArtifactsService) GetContents(name string) *ProjectsLocationsApisArtifactsGetContentsCall

GetContents: Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

name: The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*`.
func (*ProjectsLocationsApisArtifactsService) GetIamPolicy ¶
func (r *ProjectsLocationsApisArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsApisArtifactsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisArtifactsService) List ¶
func (r *ProjectsLocationsApisArtifactsService) List(parent string) *ProjectsLocationsApisArtifactsListCall

List: Returns matching artifacts.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisArtifactsService) ReplaceArtifact ¶
func (r *ProjectsLocationsApisArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisArtifactsReplaceArtifactCall

ReplaceArtifact: Used to replace a specified artifact.

- name: Resource name.

func (*ProjectsLocationsApisArtifactsService) SetIamPolicy ¶
func (r *ProjectsLocationsApisArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisArtifactsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisArtifactsService) TestIamPermissions ¶
func (r *ProjectsLocationsApisArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisArtifactsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisArtifactsSetIamPolicyCall ¶
type ProjectsLocationsApisArtifactsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisArtifactsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisArtifactsTestIamPermissionsCall ¶
type ProjectsLocationsApisArtifactsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisArtifactsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisArtifactsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisArtifactsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.artifacts.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisArtifactsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisArtifactsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisArtifactsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisArtifactsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisCreateCall ¶
type ProjectsLocationsApisCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisCreateCall) ApiId ¶
func (c *ProjectsLocationsApisCreateCall) ApiId(apiId string) *ProjectsLocationsApisCreateCall

ApiId sets the optional parameter "apiId": Required. The ID to use for the API, which will become the final component of the API's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisCreateCall) Context ¶
func (c *ProjectsLocationsApisCreateCall) Context(ctx context.Context) *ProjectsLocationsApisCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisCreateCall) Do ¶
func (c *ProjectsLocationsApisCreateCall) Do(opts ...googleapi.CallOption) (*Api, error)

Do executes the "apigeeregistry.projects.locations.apis.create" call. Any non-2xx status code is an error. Response headers are in either *Api.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisCreateCall) Fields ¶
func (c *ProjectsLocationsApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisCreateCall) Header ¶
func (c *ProjectsLocationsApisCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeleteCall ¶
type ProjectsLocationsApisDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeleteCall) Context ¶
func (c *ProjectsLocationsApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeleteCall) Do ¶
func (c *ProjectsLocationsApisDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeleteCall) Fields ¶
func (c *ProjectsLocationsApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeleteCall) Force ¶
added in v0.88.0
func (c *ProjectsLocationsApisDeleteCall) Force(force bool) *ProjectsLocationsApisDeleteCall

Force sets the optional parameter "force": If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)

func (*ProjectsLocationsApisDeleteCall) Header ¶
func (c *ProjectsLocationsApisDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsArtifactsCreateCall ¶
type ProjectsLocationsApisDeploymentsArtifactsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsArtifactsCreateCall) ArtifactId ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisDeploymentsArtifactsCreateCall

ArtifactId sets the optional parameter "artifactId": Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisDeploymentsArtifactsCreateCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsArtifactsCreateCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.artifacts.create" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsArtifactsCreateCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsArtifactsCreateCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsArtifactsDeleteCall ¶
type ProjectsLocationsApisDeploymentsArtifactsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.artifacts.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsArtifactsGetCall ¶
type ProjectsLocationsApisDeploymentsArtifactsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsArtifactsGetCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsArtifactsGetCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.artifacts.get" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsArtifactsGetCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsArtifactsGetCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsArtifactsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsArtifactsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisDeploymentsArtifactsGetContentsCall ¶
type ProjectsLocationsApisDeploymentsArtifactsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.artifacts.getContents" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisDeploymentsArtifactsListCall ¶
type ProjectsLocationsApisDeploymentsArtifactsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsArtifactsListCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.artifacts.list" call. Any non-2xx status code is an error. Response headers are in either *ListArtifactsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) Filter ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Filter(filter string) *ProjectsLocationsApisDeploymentsArtifactsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsArtifactsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisDeploymentsArtifactsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) PageSize ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisDeploymentsArtifactsListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) PageToken ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisDeploymentsArtifactsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token.

func (*ProjectsLocationsApisDeploymentsArtifactsListCall) Pages ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall ¶
type ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.artifacts.replaceArtifact" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsArtifactsService ¶
type ProjectsLocationsApisDeploymentsArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisDeploymentsArtifactsService ¶
func NewProjectsLocationsApisDeploymentsArtifactsService(s *Service) *ProjectsLocationsApisDeploymentsArtifactsService
func (*ProjectsLocationsApisDeploymentsArtifactsService) Create ¶
func (r *ProjectsLocationsApisDeploymentsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisDeploymentsArtifactsCreateCall

Create: Creates a specified artifact.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisDeploymentsArtifactsService) Delete ¶
func (r *ProjectsLocationsApisDeploymentsArtifactsService) Delete(name string) *ProjectsLocationsApisDeploymentsArtifactsDeleteCall

Delete: Removes a specified artifact.

- name: The name of the artifact to delete. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisDeploymentsArtifactsService) Get ¶
func (r *ProjectsLocationsApisDeploymentsArtifactsService) Get(name string) *ProjectsLocationsApisDeploymentsArtifactsGetCall

Get: Returns a specified artifact.

- name: The name of the artifact to retrieve. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisDeploymentsArtifactsService) GetContents ¶
func (r *ProjectsLocationsApisDeploymentsArtifactsService) GetContents(name string) *ProjectsLocationsApisDeploymentsArtifactsGetContentsCall

GetContents: Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

name: The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*`.
func (*ProjectsLocationsApisDeploymentsArtifactsService) List ¶
func (r *ProjectsLocationsApisDeploymentsArtifactsService) List(parent string) *ProjectsLocationsApisDeploymentsArtifactsListCall

List: Returns matching artifacts.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisDeploymentsArtifactsService) ReplaceArtifact ¶
func (r *ProjectsLocationsApisDeploymentsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisDeploymentsArtifactsReplaceArtifactCall

ReplaceArtifact: Used to replace a specified artifact.

- name: Resource name.

type ProjectsLocationsApisDeploymentsCreateCall ¶
type ProjectsLocationsApisDeploymentsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsCreateCall) ApiDeploymentId ¶
func (c *ProjectsLocationsApisDeploymentsCreateCall) ApiDeploymentId(apiDeploymentId string) *ProjectsLocationsApisDeploymentsCreateCall

ApiDeploymentId sets the optional parameter "apiDeploymentId": Required. The ID to use for the deployment, which will become the final component of the deployment's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisDeploymentsCreateCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsCreateCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsCreateCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.create" call. Any non-2xx status code is an error. Response headers are in either *ApiDeployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsCreateCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsCreateCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsDeleteCall ¶
type ProjectsLocationsApisDeploymentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsDeleteCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsDeleteCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsDeleteCall) Force ¶
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Force(force bool) *ProjectsLocationsApisDeploymentsDeleteCall

Force sets the optional parameter "force": If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)

func (*ProjectsLocationsApisDeploymentsDeleteCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsDeleteRevisionCall ¶
type ProjectsLocationsApisDeploymentsDeleteRevisionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsDeleteRevisionCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsDeleteRevisionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsDeleteRevisionCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.deleteRevision" call. Any non-2xx status code is an error. Response headers are in either *ApiDeployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsDeleteRevisionCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsDeleteRevisionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsDeleteRevisionCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsDeleteRevisionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsGetCall ¶
type ProjectsLocationsApisDeploymentsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsGetCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsGetCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsGetCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsGetCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.get" call. Any non-2xx status code is an error. Response headers are in either *ApiDeployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsGetCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsGetCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisDeploymentsGetIamPolicyCall ¶
type ProjectsLocationsApisDeploymentsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisDeploymentsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisDeploymentsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisDeploymentsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisDeploymentsListCall ¶
type ProjectsLocationsApisDeploymentsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsListCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsListCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsListCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsListCall) Do(opts ...googleapi.CallOption) (*ListApiDeploymentsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.list" call. Any non-2xx status code is an error. Response headers are in either *ListApiDeploymentsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsListCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsListCall) Filter ¶
func (c *ProjectsLocationsApisDeploymentsListCall) Filter(filter string) *ProjectsLocationsApisDeploymentsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.

func (*ProjectsLocationsApisDeploymentsListCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisDeploymentsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisDeploymentsListCall) OrderBy(orderBy string) *ProjectsLocationsApisDeploymentsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisDeploymentsListCall) PageSize ¶
func (c *ProjectsLocationsApisDeploymentsListCall) PageSize(pageSize int64) *ProjectsLocationsApisDeploymentsListCall

PageSize sets the optional parameter "pageSize": The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisDeploymentsListCall) PageToken ¶
func (c *ProjectsLocationsApisDeploymentsListCall) PageToken(pageToken string) *ProjectsLocationsApisDeploymentsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiDeployments` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiDeployments` must match the call that provided the page token.

func (*ProjectsLocationsApisDeploymentsListCall) Pages ¶
func (c *ProjectsLocationsApisDeploymentsListCall) Pages(ctx context.Context, f func(*ListApiDeploymentsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisDeploymentsListRevisionsCall ¶
type ProjectsLocationsApisDeploymentsListRevisionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsListRevisionsCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsListRevisionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Do(opts ...googleapi.CallOption) (*ListApiDeploymentRevisionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.listRevisions" call. Any non-2xx status code is an error. Response headers are in either *ListApiDeploymentRevisionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsListRevisionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) Filter ¶
added in v0.109.0
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Filter(filter string) *ProjectsLocationsApisDeploymentsListRevisionsCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisDeploymentsListRevisionsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) PageSize ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) PageSize(pageSize int64) *ProjectsLocationsApisDeploymentsListRevisionsCall

PageSize sets the optional parameter "pageSize": The maximum number of revisions to return per page.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) PageToken ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) PageToken(pageToken string) *ProjectsLocationsApisDeploymentsListRevisionsCall

PageToken sets the optional parameter "pageToken": The page token, received from a previous ListApiDeploymentRevisions call. Provide this to retrieve the subsequent page.

func (*ProjectsLocationsApisDeploymentsListRevisionsCall) Pages ¶
func (c *ProjectsLocationsApisDeploymentsListRevisionsCall) Pages(ctx context.Context, f func(*ListApiDeploymentRevisionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisDeploymentsPatchCall ¶
type ProjectsLocationsApisDeploymentsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsPatchCall) AllowMissing ¶
func (c *ProjectsLocationsApisDeploymentsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisDeploymentsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the deployment is not found, a new deployment will be created. In this situation, `update_mask` is ignored.

func (*ProjectsLocationsApisDeploymentsPatchCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsPatchCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsPatchCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.patch" call. Any non-2xx status code is an error. Response headers are in either *ApiDeployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsPatchCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsPatchCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisDeploymentsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisDeploymentsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisDeploymentsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request.

type ProjectsLocationsApisDeploymentsRollbackCall ¶
type ProjectsLocationsApisDeploymentsRollbackCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsRollbackCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsRollbackCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsRollbackCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.rollback" call. Any non-2xx status code is an error. Response headers are in either *ApiDeployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsRollbackCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsRollbackCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsRollbackCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsRollbackCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsService ¶
type ProjectsLocationsApisDeploymentsService struct {
	Artifacts *ProjectsLocationsApisDeploymentsArtifactsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisDeploymentsService ¶
func NewProjectsLocationsApisDeploymentsService(s *Service) *ProjectsLocationsApisDeploymentsService
func (*ProjectsLocationsApisDeploymentsService) Create ¶
func (r *ProjectsLocationsApisDeploymentsService) Create(parent string, apideployment *ApiDeployment) *ProjectsLocationsApisDeploymentsCreateCall

Create: Creates a specified deployment.

parent: The parent, which owns this collection of deployments. Format: `projects/*/locations/*/apis/*`.
func (*ProjectsLocationsApisDeploymentsService) Delete ¶
func (r *ProjectsLocationsApisDeploymentsService) Delete(name string) *ProjectsLocationsApisDeploymentsDeleteCall

Delete: Removes a specified deployment, all revisions, and all child resources (e.g., artifacts).

name: The name of the deployment to delete. Format: `projects/*/locations/*/apis/*/deployments/*`.
func (*ProjectsLocationsApisDeploymentsService) DeleteRevision ¶
func (r *ProjectsLocationsApisDeploymentsService) DeleteRevision(name string) *ProjectsLocationsApisDeploymentsDeleteRevisionCall

DeleteRevision: Deletes a revision of a deployment.

name: The name of the deployment revision to be deleted, with a revision ID explicitly included. Example: `projects/sample/locations/global/apis/petstore/deployments/prod@c7cfa2a8`.
func (*ProjectsLocationsApisDeploymentsService) Get ¶
func (r *ProjectsLocationsApisDeploymentsService) Get(name string) *ProjectsLocationsApisDeploymentsGetCall

Get: Returns a specified deployment.

name: The name of the deployment to retrieve. Format: `projects/*/locations/*/apis/*/deployments/*`.
func (*ProjectsLocationsApisDeploymentsService) GetIamPolicy ¶
func (r *ProjectsLocationsApisDeploymentsService) GetIamPolicy(resource string) *ProjectsLocationsApisDeploymentsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisDeploymentsService) List ¶
func (r *ProjectsLocationsApisDeploymentsService) List(parent string) *ProjectsLocationsApisDeploymentsListCall

List: Returns matching deployments.

parent: The parent, which owns this collection of deployments. Format: `projects/*/locations/*/apis/*`.
func (*ProjectsLocationsApisDeploymentsService) ListRevisions ¶
func (r *ProjectsLocationsApisDeploymentsService) ListRevisions(name string) *ProjectsLocationsApisDeploymentsListRevisionsCall

ListRevisions: Lists all revisions of a deployment. Revisions are returned in descending order of revision creation time.

- name: The name of the deployment to list revisions for.

func (*ProjectsLocationsApisDeploymentsService) Patch ¶
func (r *ProjectsLocationsApisDeploymentsService) Patch(name string, apideployment *ApiDeployment) *ProjectsLocationsApisDeploymentsPatchCall

Patch: Used to modify a specified deployment.

- name: Resource name.

func (*ProjectsLocationsApisDeploymentsService) Rollback ¶
func (r *ProjectsLocationsApisDeploymentsService) Rollback(name string, rollbackapideploymentrequest *RollbackApiDeploymentRequest) *ProjectsLocationsApisDeploymentsRollbackCall

Rollback: Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID.

- name: The deployment being rolled back.

func (*ProjectsLocationsApisDeploymentsService) SetIamPolicy ¶
func (r *ProjectsLocationsApisDeploymentsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisDeploymentsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisDeploymentsService) TagRevision ¶
func (r *ProjectsLocationsApisDeploymentsService) TagRevision(name string, tagapideploymentrevisionrequest *TagApiDeploymentRevisionRequest) *ProjectsLocationsApisDeploymentsTagRevisionCall

TagRevision: Adds a tag to a specified revision of a deployment.

name: The name of the deployment to be tagged, including the revision ID is optional. If a revision is not specified, it will tag the latest revision.
func (*ProjectsLocationsApisDeploymentsService) TestIamPermissions ¶
func (r *ProjectsLocationsApisDeploymentsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisDeploymentsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisDeploymentsSetIamPolicyCall ¶
type ProjectsLocationsApisDeploymentsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsTagRevisionCall ¶
type ProjectsLocationsApisDeploymentsTagRevisionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsTagRevisionCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsTagRevisionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsTagRevisionCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Do(opts ...googleapi.CallOption) (*ApiDeployment, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.tagRevision" call. Any non-2xx status code is an error. Response headers are in either *ApiDeployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsTagRevisionCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsTagRevisionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsTagRevisionCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsTagRevisionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeploymentsTestIamPermissionsCall ¶
type ProjectsLocationsApisDeploymentsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisDeploymentsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.deployments.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeploymentsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisDeploymentsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisGetCall ¶
type ProjectsLocationsApisGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisGetCall) Context ¶
func (c *ProjectsLocationsApisGetCall) Context(ctx context.Context) *ProjectsLocationsApisGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisGetCall) Do ¶
func (c *ProjectsLocationsApisGetCall) Do(opts ...googleapi.CallOption) (*Api, error)

Do executes the "apigeeregistry.projects.locations.apis.get" call. Any non-2xx status code is an error. Response headers are in either *Api.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisGetCall) Fields ¶
func (c *ProjectsLocationsApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisGetCall) Header ¶
func (c *ProjectsLocationsApisGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisGetIamPolicyCall ¶
type ProjectsLocationsApisGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisListCall ¶
type ProjectsLocationsApisListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisListCall) Context ¶
func (c *ProjectsLocationsApisListCall) Context(ctx context.Context) *ProjectsLocationsApisListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisListCall) Do ¶
func (c *ProjectsLocationsApisListCall) Do(opts ...googleapi.CallOption) (*ListApisResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.list" call. Any non-2xx status code is an error. Response headers are in either *ListApisResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisListCall) Fields ¶
func (c *ProjectsLocationsApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisListCall) Filter ¶
func (c *ProjectsLocationsApisListCall) Filter(filter string) *ProjectsLocationsApisListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.

func (*ProjectsLocationsApisListCall) Header ¶
func (c *ProjectsLocationsApisListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisListCall) OrderBy(orderBy string) *ProjectsLocationsApisListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisListCall) PageSize ¶
func (c *ProjectsLocationsApisListCall) PageSize(pageSize int64) *ProjectsLocationsApisListCall

PageSize sets the optional parameter "pageSize": The maximum number of APIs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisListCall) PageToken ¶
func (c *ProjectsLocationsApisListCall) PageToken(pageToken string) *ProjectsLocationsApisListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApis` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApis` must match the call that provided the page token.

func (*ProjectsLocationsApisListCall) Pages ¶
func (c *ProjectsLocationsApisListCall) Pages(ctx context.Context, f func(*ListApisResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisPatchCall ¶
type ProjectsLocationsApisPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisPatchCall) AllowMissing ¶
func (c *ProjectsLocationsApisPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the API is not found, a new API will be created. In this situation, `update_mask` is ignored.

func (*ProjectsLocationsApisPatchCall) Context ¶
func (c *ProjectsLocationsApisPatchCall) Context(ctx context.Context) *ProjectsLocationsApisPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisPatchCall) Do ¶
func (c *ProjectsLocationsApisPatchCall) Do(opts ...googleapi.CallOption) (*Api, error)

Do executes the "apigeeregistry.projects.locations.apis.patch" call. Any non-2xx status code is an error. Response headers are in either *Api.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisPatchCall) Fields ¶
func (c *ProjectsLocationsApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisPatchCall) Header ¶
func (c *ProjectsLocationsApisPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request.

type ProjectsLocationsApisService ¶
type ProjectsLocationsApisService struct {
	Artifacts *ProjectsLocationsApisArtifactsService

	Deployments *ProjectsLocationsApisDeploymentsService

	Versions *ProjectsLocationsApisVersionsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisService ¶
func NewProjectsLocationsApisService(s *Service) *ProjectsLocationsApisService
func (*ProjectsLocationsApisService) Create ¶
func (r *ProjectsLocationsApisService) Create(parent string, api *Api) *ProjectsLocationsApisCreateCall

Create: Creates a specified API.

parent: The parent, which owns this collection of APIs. Format: `projects/*/locations/*`.
func (*ProjectsLocationsApisService) Delete ¶
func (r *ProjectsLocationsApisService) Delete(name string) *ProjectsLocationsApisDeleteCall

Delete: Removes a specified API and all of the resources that it owns.

name: The name of the API to delete. Format: `projects/*/locations/*/apis/*`.
func (*ProjectsLocationsApisService) Get ¶
func (r *ProjectsLocationsApisService) Get(name string) *ProjectsLocationsApisGetCall

Get: Returns a specified API.

name: The name of the API to retrieve. Format: `projects/*/locations/*/apis/*`.
func (*ProjectsLocationsApisService) GetIamPolicy ¶
func (r *ProjectsLocationsApisService) GetIamPolicy(resource string) *ProjectsLocationsApisGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisService) List ¶
func (r *ProjectsLocationsApisService) List(parent string) *ProjectsLocationsApisListCall

List: Returns matching APIs.

parent: The parent, which owns this collection of APIs. Format: `projects/*/locations/*`.
func (*ProjectsLocationsApisService) Patch ¶
func (r *ProjectsLocationsApisService) Patch(name string, api *Api) *ProjectsLocationsApisPatchCall

Patch: Used to modify a specified API.

- name: Resource name.

func (*ProjectsLocationsApisService) SetIamPolicy ¶
func (r *ProjectsLocationsApisService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisService) TestIamPermissions ¶
func (r *ProjectsLocationsApisService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisSetIamPolicyCall ¶
type ProjectsLocationsApisSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisTestIamPermissionsCall ¶
type ProjectsLocationsApisTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsArtifactsCreateCall ¶
type ProjectsLocationsApisVersionsArtifactsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsCreateCall) ArtifactId ¶
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisVersionsArtifactsCreateCall

ArtifactId sets the optional parameter "artifactId": Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisVersionsArtifactsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.create" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsArtifactsDeleteCall ¶
type ProjectsLocationsApisVersionsArtifactsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsArtifactsGetCall ¶
type ProjectsLocationsApisVersionsArtifactsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.get" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsArtifactsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsArtifactsGetContentsCall ¶
type ProjectsLocationsApisVersionsArtifactsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsGetContentsCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsGetContentsCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.getContents" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsGetContentsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsGetContentsCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsArtifactsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall ¶
type ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisVersionsArtifactsListCall ¶
type ProjectsLocationsApisVersionsArtifactsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.list" call. Any non-2xx status code is an error. Response headers are in either *ListArtifactsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Filter(filter string) *ProjectsLocationsApisVersionsArtifactsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.

func (*ProjectsLocationsApisVersionsArtifactsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsArtifactsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsArtifactsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsArtifactsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisVersionsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsArtifactsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisVersionsArtifactsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsArtifactsListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsArtifactsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsArtifactsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsArtifactsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall ¶
type ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.replaceArtifact" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsArtifactsService ¶
type ProjectsLocationsApisVersionsArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsArtifactsService ¶
func NewProjectsLocationsApisVersionsArtifactsService(s *Service) *ProjectsLocationsApisVersionsArtifactsService
func (*ProjectsLocationsApisVersionsArtifactsService) Create ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisVersionsArtifactsCreateCall

Create: Creates a specified artifact.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisVersionsArtifactsService) Delete ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) Delete(name string) *ProjectsLocationsApisVersionsArtifactsDeleteCall

Delete: Removes a specified artifact.

- name: The name of the artifact to delete. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisVersionsArtifactsService) Get ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) Get(name string) *ProjectsLocationsApisVersionsArtifactsGetCall

Get: Returns a specified artifact.

- name: The name of the artifact to retrieve. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisVersionsArtifactsService) GetContents ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) GetContents(name string) *ProjectsLocationsApisVersionsArtifactsGetContentsCall

GetContents: Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

name: The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*`.
func (*ProjectsLocationsApisVersionsArtifactsService) GetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsArtifactsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsArtifactsService) List ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) List(parent string) *ProjectsLocationsApisVersionsArtifactsListCall

List: Returns matching artifacts.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisVersionsArtifactsService) ReplaceArtifact ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisVersionsArtifactsReplaceArtifactCall

ReplaceArtifact: Used to replace a specified artifact.

- name: Resource name.

func (*ProjectsLocationsApisVersionsArtifactsService) SetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsArtifactsService) TestIamPermissions ¶
func (r *ProjectsLocationsApisVersionsArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall ¶
type ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall ¶
type ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.artifacts.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisVersionsArtifactsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsCreateCall ¶
type ProjectsLocationsApisVersionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsCreateCall) ApiVersionId ¶
func (c *ProjectsLocationsApisVersionsCreateCall) ApiVersionId(apiVersionId string) *ProjectsLocationsApisVersionsCreateCall

ApiVersionId sets the optional parameter "apiVersionId": Required. The ID to use for the version, which will become the final component of the version's resource name. This value should be 1-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisVersionsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Do(opts ...googleapi.CallOption) (*ApiVersion, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.create" call. Any non-2xx status code is an error. Response headers are in either *ApiVersion.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsDeleteCall ¶
type ProjectsLocationsApisVersionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsDeleteCall) Force ¶
added in v0.88.0
func (c *ProjectsLocationsApisVersionsDeleteCall) Force(force bool) *ProjectsLocationsApisVersionsDeleteCall

Force sets the optional parameter "force": If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)

func (*ProjectsLocationsApisVersionsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsGetCall ¶
type ProjectsLocationsApisVersionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsGetCall) Do(opts ...googleapi.CallOption) (*ApiVersion, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.get" call. Any non-2xx status code is an error. Response headers are in either *ApiVersion.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsGetIamPolicyCall ¶
type ProjectsLocationsApisVersionsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisVersionsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisVersionsListCall ¶
type ProjectsLocationsApisVersionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsListCall) Do(opts ...googleapi.CallOption) (*ListApiVersionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.list" call. Any non-2xx status code is an error. Response headers are in either *ListApiVersionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsListCall) Filter(filter string) *ProjectsLocationsApisVersionsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.

func (*ProjectsLocationsApisVersionsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisVersionsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisVersionsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiVersions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiVersions` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsListCall) Pages(ctx context.Context, f func(*ListApiVersionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsPatchCall ¶
type ProjectsLocationsApisVersionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsPatchCall) AllowMissing ¶
func (c *ProjectsLocationsApisVersionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisVersionsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the version is not found, a new version will be created. In this situation, `update_mask` is ignored.

func (*ProjectsLocationsApisVersionsPatchCall) Context ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsPatchCall) Do ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Do(opts ...googleapi.CallOption) (*ApiVersion, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.patch" call. Any non-2xx status code is an error. Response headers are in either *ApiVersion.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsPatchCall) Fields ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsPatchCall) Header ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request.

type ProjectsLocationsApisVersionsService ¶
type ProjectsLocationsApisVersionsService struct {
	Artifacts *ProjectsLocationsApisVersionsArtifactsService

	Specs *ProjectsLocationsApisVersionsSpecsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsService ¶
func NewProjectsLocationsApisVersionsService(s *Service) *ProjectsLocationsApisVersionsService
func (*ProjectsLocationsApisVersionsService) Create ¶
func (r *ProjectsLocationsApisVersionsService) Create(parent string, apiversion *ApiVersion) *ProjectsLocationsApisVersionsCreateCall

Create: Creates a specified version.

parent: The parent, which owns this collection of versions. Format: `projects/*/locations/*/apis/*`.
func (*ProjectsLocationsApisVersionsService) Delete ¶
func (r *ProjectsLocationsApisVersionsService) Delete(name string) *ProjectsLocationsApisVersionsDeleteCall

Delete: Removes a specified version and all of the resources that it owns.

name: The name of the version to delete. Format: `projects/*/locations/*/apis/*/versions/*`.
func (*ProjectsLocationsApisVersionsService) Get ¶
func (r *ProjectsLocationsApisVersionsService) Get(name string) *ProjectsLocationsApisVersionsGetCall

Get: Returns a specified version.

name: The name of the version to retrieve. Format: `projects/*/locations/*/apis/*/versions/*`.
func (*ProjectsLocationsApisVersionsService) GetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsService) List ¶
func (r *ProjectsLocationsApisVersionsService) List(parent string) *ProjectsLocationsApisVersionsListCall

List: Returns matching versions.

parent: The parent, which owns this collection of versions. Format: `projects/*/locations/*/apis/*`.
func (*ProjectsLocationsApisVersionsService) Patch ¶
func (r *ProjectsLocationsApisVersionsService) Patch(name string, apiversion *ApiVersion) *ProjectsLocationsApisVersionsPatchCall

Patch: Used to modify a specified version.

- name: Resource name.

func (*ProjectsLocationsApisVersionsService) SetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsService) TestIamPermissions ¶
func (r *ProjectsLocationsApisVersionsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisVersionsSetIamPolicyCall ¶
type ProjectsLocationsApisVersionsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsArtifactsCreateCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) ArtifactId ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall

ArtifactId sets the optional parameter "artifactId": Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.create" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsArtifactsGetCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.get" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.getContents" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisVersionsSpecsArtifactsListCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.list" call. Any non-2xx status code is an error. Response headers are in either *ListArtifactsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsSpecsArtifactsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.replaceArtifact" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsArtifactsService ¶
type ProjectsLocationsApisVersionsSpecsArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsSpecsArtifactsService ¶
func NewProjectsLocationsApisVersionsSpecsArtifactsService(s *Service) *ProjectsLocationsApisVersionsSpecsArtifactsService
func (*ProjectsLocationsApisVersionsSpecsArtifactsService) Create ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsApisVersionsSpecsArtifactsCreateCall

Create: Creates a specified artifact.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisVersionsSpecsArtifactsService) Delete ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) Delete(name string) *ProjectsLocationsApisVersionsSpecsArtifactsDeleteCall

Delete: Removes a specified artifact.

- name: The name of the artifact to delete. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisVersionsSpecsArtifactsService) Get ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) Get(name string) *ProjectsLocationsApisVersionsSpecsArtifactsGetCall

Get: Returns a specified artifact.

- name: The name of the artifact to retrieve. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsApisVersionsSpecsArtifactsService) GetContents ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) GetContents(name string) *ProjectsLocationsApisVersionsSpecsArtifactsGetContentsCall

GetContents: Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

name: The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*`.
func (*ProjectsLocationsApisVersionsSpecsArtifactsService) GetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsSpecsArtifactsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsSpecsArtifactsService) List ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) List(parent string) *ProjectsLocationsApisVersionsSpecsArtifactsListCall

List: Returns matching artifacts.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsApisVersionsSpecsArtifactsService) ReplaceArtifact ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsApisVersionsSpecsArtifactsReplaceArtifactCall

ReplaceArtifact: Used to replace a specified artifact.

- name: Resource name.

func (*ProjectsLocationsApisVersionsSpecsArtifactsService) SetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsSpecsArtifactsService) TestIamPermissions ¶
func (r *ProjectsLocationsApisVersionsSpecsArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall ¶
type ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.artifacts.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsArtifactsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsCreateCall ¶
type ProjectsLocationsApisVersionsSpecsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsCreateCall) ApiSpecId ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) ApiSpecId(apiSpecId string) *ProjectsLocationsApisVersionsSpecsCreateCall

ApiSpecId sets the optional parameter "apiSpecId": Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.create" call. Any non-2xx status code is an error. Response headers are in either *ApiSpec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsDeleteCall ¶
type ProjectsLocationsApisVersionsSpecsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Force ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Force(force bool) *ProjectsLocationsApisVersionsSpecsDeleteCall

Force sets the optional parameter "force": If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsDeleteRevisionCall ¶
type ProjectsLocationsApisVersionsSpecsDeleteRevisionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.deleteRevision" call. Any non-2xx status code is an error. Response headers are in either *ApiSpec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsGetCall ¶
type ProjectsLocationsApisVersionsSpecsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.get" call. Any non-2xx status code is an error. Response headers are in either *ApiSpec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsSpecsGetContentsCall ¶
type ProjectsLocationsApisVersionsSpecsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.getContents" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsSpecsGetIamPolicyCall ¶
type ProjectsLocationsApisVersionsSpecsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApisVersionsSpecsListCall ¶
type ProjectsLocationsApisVersionsSpecsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Do(opts ...googleapi.CallOption) (*ListApiSpecsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.list" call. Any non-2xx status code is an error. Response headers are in either *ListApiSpecsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.

func (*ProjectsLocationsApisVersionsSpecsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsApisVersionsSpecsListCall) OrderBy(orderBy string) *ProjectsLocationsApisVersionsSpecsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsApisVersionsSpecsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsListCall

PageSize sets the optional parameter "pageSize": The maximum number of specs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsSpecsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiSpecs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiSpecs` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsSpecsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Pages(ctx context.Context, f func(*ListApiSpecsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsSpecsListRevisionsCall ¶
type ProjectsLocationsApisVersionsSpecsListRevisionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Do(opts ...googleapi.CallOption) (*ListApiSpecRevisionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.listRevisions" call. Any non-2xx status code is an error. Response headers are in either *ListApiSpecRevisionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) Filter ¶
added in v0.109.0
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

PageSize sets the optional parameter "pageSize": The maximum number of revisions to return per page.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

PageToken sets the optional parameter "pageToken": The page token, received from a previous ListApiSpecRevisions call. Provide this to retrieve the subsequent page.

func (*ProjectsLocationsApisVersionsSpecsListRevisionsCall) Pages ¶
func (c *ProjectsLocationsApisVersionsSpecsListRevisionsCall) Pages(ctx context.Context, f func(*ListApiSpecRevisionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsSpecsPatchCall ¶
type ProjectsLocationsApisVersionsSpecsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsPatchCall) AllowMissing ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsApisVersionsSpecsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the spec is not found, a new spec will be created. In this situation, `update_mask` is ignored.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.patch" call. Any non-2xx status code is an error. Response headers are in either *ApiSpec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsSpecsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request.

type ProjectsLocationsApisVersionsSpecsRollbackCall ¶
type ProjectsLocationsApisVersionsSpecsRollbackCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsRollbackCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsRollbackCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsRollbackCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.rollback" call. Any non-2xx status code is an error. Response headers are in either *ApiSpec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsRollbackCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsRollbackCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsRollbackCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsRollbackCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsService ¶
type ProjectsLocationsApisVersionsSpecsService struct {
	Artifacts *ProjectsLocationsApisVersionsSpecsArtifactsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsSpecsService ¶
func NewProjectsLocationsApisVersionsSpecsService(s *Service) *ProjectsLocationsApisVersionsSpecsService
func (*ProjectsLocationsApisVersionsSpecsService) Create ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Create(parent string, apispec *ApiSpec) *ProjectsLocationsApisVersionsSpecsCreateCall

Create: Creates a specified spec.

parent: The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`.
func (*ProjectsLocationsApisVersionsSpecsService) Delete ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Delete(name string) *ProjectsLocationsApisVersionsSpecsDeleteCall

Delete: Removes a specified spec, all revisions, and all child resources (e.g., artifacts).

name: The name of the spec to delete. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`.
func (*ProjectsLocationsApisVersionsSpecsService) DeleteRevision ¶
func (r *ProjectsLocationsApisVersionsSpecsService) DeleteRevision(name string) *ProjectsLocationsApisVersionsSpecsDeleteRevisionCall

DeleteRevision: Deletes a revision of a spec.

name: The name of the spec revision to be deleted, with a revision ID explicitly included. Example: `projects/sample/locations/global/apis/petstore/versions/1.0.0/specs/openap i.yaml@c7cfa2a8`.
func (*ProjectsLocationsApisVersionsSpecsService) Get ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Get(name string) *ProjectsLocationsApisVersionsSpecsGetCall

Get: Returns a specified spec.

name: The name of the spec to retrieve. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`.
func (*ProjectsLocationsApisVersionsSpecsService) GetContents ¶
func (r *ProjectsLocationsApisVersionsSpecsService) GetContents(name string) *ProjectsLocationsApisVersionsSpecsGetContentsCall

GetContents: Returns the contents of a specified spec. If specs are stored with GZip compression, the default behavior is to return the spec uncompressed (the mime_type response field indicates the exact format returned).

name: The name of the spec whose contents should be retrieved. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`.
func (*ProjectsLocationsApisVersionsSpecsService) GetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsSpecsService) GetIamPolicy(resource string) *ProjectsLocationsApisVersionsSpecsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsSpecsService) List ¶
func (r *ProjectsLocationsApisVersionsSpecsService) List(parent string) *ProjectsLocationsApisVersionsSpecsListCall

List: Returns matching specs.

parent: The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`.
func (*ProjectsLocationsApisVersionsSpecsService) ListRevisions ¶
func (r *ProjectsLocationsApisVersionsSpecsService) ListRevisions(name string) *ProjectsLocationsApisVersionsSpecsListRevisionsCall

ListRevisions: Lists all revisions of a spec. Revisions are returned in descending order of revision creation time.

- name: The name of the spec to list revisions for.

func (*ProjectsLocationsApisVersionsSpecsService) Patch ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Patch(name string, apispec *ApiSpec) *ProjectsLocationsApisVersionsSpecsPatchCall

Patch: Used to modify a specified spec.

- name: Resource name.

func (*ProjectsLocationsApisVersionsSpecsService) Rollback ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Rollback(name string, rollbackapispecrequest *RollbackApiSpecRequest) *ProjectsLocationsApisVersionsSpecsRollbackCall

Rollback: Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID.

- name: The spec being rolled back.

func (*ProjectsLocationsApisVersionsSpecsService) SetIamPolicy ¶
func (r *ProjectsLocationsApisVersionsSpecsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApisVersionsSpecsService) TagRevision ¶
func (r *ProjectsLocationsApisVersionsSpecsService) TagRevision(name string, tagapispecrevisionrequest *TagApiSpecRevisionRequest) *ProjectsLocationsApisVersionsSpecsTagRevisionCall

TagRevision: Adds a tag to a specified revision of a spec.

name: The name of the spec to be tagged, including the revision ID is optional. If a revision is not specified, it will tag the latest revision.
func (*ProjectsLocationsApisVersionsSpecsService) TestIamPermissions ¶
func (r *ProjectsLocationsApisVersionsSpecsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApisVersionsSpecsSetIamPolicyCall ¶
type ProjectsLocationsApisVersionsSpecsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsTagRevisionCall ¶
type ProjectsLocationsApisVersionsSpecsTagRevisionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsTagRevisionCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsTagRevisionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsTagRevisionCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Do(opts ...googleapi.CallOption) (*ApiSpec, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.tagRevision" call. Any non-2xx status code is an error. Response headers are in either *ApiSpec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsTagRevisionCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsTagRevisionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsTagRevisionCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsTagRevisionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall ¶
type ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.specs.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsTestIamPermissionsCall ¶
type ProjectsLocationsApisVersionsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.apis.versions.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApisVersionsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsArtifactsCreateCall ¶
type ProjectsLocationsArtifactsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsCreateCall) ArtifactId ¶
func (c *ProjectsLocationsArtifactsCreateCall) ArtifactId(artifactId string) *ProjectsLocationsArtifactsCreateCall

ArtifactId sets the optional parameter "artifactId": Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.

func (*ProjectsLocationsArtifactsCreateCall) Context ¶
func (c *ProjectsLocationsArtifactsCreateCall) Context(ctx context.Context) *ProjectsLocationsArtifactsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsCreateCall) Do ¶
func (c *ProjectsLocationsArtifactsCreateCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.artifacts.create" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsCreateCall) Fields ¶
func (c *ProjectsLocationsArtifactsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsCreateCall) Header ¶
func (c *ProjectsLocationsArtifactsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsArtifactsDeleteCall ¶
type ProjectsLocationsArtifactsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsDeleteCall) Context ¶
func (c *ProjectsLocationsArtifactsDeleteCall) Context(ctx context.Context) *ProjectsLocationsArtifactsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsDeleteCall) Do ¶
func (c *ProjectsLocationsArtifactsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.artifacts.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsDeleteCall) Fields ¶
func (c *ProjectsLocationsArtifactsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsDeleteCall) Header ¶
func (c *ProjectsLocationsArtifactsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsArtifactsGetCall ¶
type ProjectsLocationsArtifactsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsGetCall) Context ¶
func (c *ProjectsLocationsArtifactsGetCall) Context(ctx context.Context) *ProjectsLocationsArtifactsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsGetCall) Do ¶
func (c *ProjectsLocationsArtifactsGetCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.artifacts.get" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsGetCall) Fields ¶
func (c *ProjectsLocationsArtifactsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsGetCall) Header ¶
func (c *ProjectsLocationsArtifactsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsArtifactsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsArtifactsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsArtifactsGetContentsCall ¶
type ProjectsLocationsArtifactsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsGetContentsCall) Context ¶
func (c *ProjectsLocationsArtifactsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsArtifactsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsGetContentsCall) Do ¶
func (c *ProjectsLocationsArtifactsGetContentsCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)

Do executes the "apigeeregistry.projects.locations.artifacts.getContents" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsGetContentsCall) Fields ¶
func (c *ProjectsLocationsArtifactsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsGetContentsCall) Header ¶
func (c *ProjectsLocationsArtifactsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsArtifactsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsArtifactsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsArtifactsGetIamPolicyCall ¶
type ProjectsLocationsArtifactsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsArtifactsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.artifacts.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsArtifactsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsArtifactsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsArtifactsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsArtifactsListCall ¶
type ProjectsLocationsArtifactsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsListCall) Context ¶
func (c *ProjectsLocationsArtifactsListCall) Context(ctx context.Context) *ProjectsLocationsArtifactsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsListCall) Do ¶
func (c *ProjectsLocationsArtifactsListCall) Do(opts ...googleapi.CallOption) (*ListArtifactsResponse, error)

Do executes the "apigeeregistry.projects.locations.artifacts.list" call. Any non-2xx status code is an error. Response headers are in either *ListArtifactsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsListCall) Fields ¶
func (c *ProjectsLocationsArtifactsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsListCall) Filter ¶
func (c *ProjectsLocationsArtifactsListCall) Filter(filter string) *ProjectsLocationsArtifactsListCall

Filter sets the optional parameter "filter": An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.

func (*ProjectsLocationsArtifactsListCall) Header ¶
func (c *ProjectsLocationsArtifactsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsArtifactsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsArtifactsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsArtifactsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsArtifactsListCall) OrderBy ¶
added in v0.96.0
func (c *ProjectsLocationsArtifactsListCall) OrderBy(orderBy string) *ProjectsLocationsArtifactsListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields, e.g. "foo,bar" Fields can be sorted in descending order using the "desc" identifier, e.g. "foo desc,bar"

func (*ProjectsLocationsArtifactsListCall) PageSize ¶
func (c *ProjectsLocationsArtifactsListCall) PageSize(pageSize int64) *ProjectsLocationsArtifactsListCall

PageSize sets the optional parameter "pageSize": The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsArtifactsListCall) PageToken ¶
func (c *ProjectsLocationsArtifactsListCall) PageToken(pageToken string) *ProjectsLocationsArtifactsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token.

func (*ProjectsLocationsArtifactsListCall) Pages ¶
func (c *ProjectsLocationsArtifactsListCall) Pages(ctx context.Context, f func(*ListArtifactsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsArtifactsReplaceArtifactCall ¶
type ProjectsLocationsArtifactsReplaceArtifactCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsReplaceArtifactCall) Context ¶
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Context(ctx context.Context) *ProjectsLocationsArtifactsReplaceArtifactCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsReplaceArtifactCall) Do ¶
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Do(opts ...googleapi.CallOption) (*Artifact, error)

Do executes the "apigeeregistry.projects.locations.artifacts.replaceArtifact" call. Any non-2xx status code is an error. Response headers are in either *Artifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsReplaceArtifactCall) Fields ¶
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsReplaceArtifactCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsReplaceArtifactCall) Header ¶
func (c *ProjectsLocationsArtifactsReplaceArtifactCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsArtifactsService ¶
type ProjectsLocationsArtifactsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsArtifactsService ¶
func NewProjectsLocationsArtifactsService(s *Service) *ProjectsLocationsArtifactsService
func (*ProjectsLocationsArtifactsService) Create ¶
func (r *ProjectsLocationsArtifactsService) Create(parent string, artifact *Artifact) *ProjectsLocationsArtifactsCreateCall

Create: Creates a specified artifact.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsArtifactsService) Delete ¶
func (r *ProjectsLocationsArtifactsService) Delete(name string) *ProjectsLocationsArtifactsDeleteCall

Delete: Removes a specified artifact.

- name: The name of the artifact to delete. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsArtifactsService) Get ¶
func (r *ProjectsLocationsArtifactsService) Get(name string) *ProjectsLocationsArtifactsGetCall

Get: Returns a specified artifact.

- name: The name of the artifact to retrieve. Format: `{parent}/artifacts/*`.

func (*ProjectsLocationsArtifactsService) GetContents ¶
func (r *ProjectsLocationsArtifactsService) GetContents(name string) *ProjectsLocationsArtifactsGetContentsCall

GetContents: Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

name: The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*`.
func (*ProjectsLocationsArtifactsService) GetIamPolicy ¶
func (r *ProjectsLocationsArtifactsService) GetIamPolicy(resource string) *ProjectsLocationsArtifactsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsArtifactsService) List ¶
func (r *ProjectsLocationsArtifactsService) List(parent string) *ProjectsLocationsArtifactsListCall

List: Returns matching artifacts.

parent: The parent, which owns this collection of artifacts. Format: `{parent}`.
func (*ProjectsLocationsArtifactsService) ReplaceArtifact ¶
func (r *ProjectsLocationsArtifactsService) ReplaceArtifact(name string, artifact *Artifact) *ProjectsLocationsArtifactsReplaceArtifactCall

ReplaceArtifact: Used to replace a specified artifact.

- name: Resource name.

func (*ProjectsLocationsArtifactsService) SetIamPolicy ¶
func (r *ProjectsLocationsArtifactsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsArtifactsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsArtifactsService) TestIamPermissions ¶
func (r *ProjectsLocationsArtifactsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsArtifactsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsArtifactsSetIamPolicyCall ¶
type ProjectsLocationsArtifactsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsArtifactsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.artifacts.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsArtifactsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsArtifactsTestIamPermissionsCall ¶
type ProjectsLocationsArtifactsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsArtifactsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsArtifactsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsArtifactsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.artifacts.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsArtifactsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsArtifactsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsArtifactsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsArtifactsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDocumentsGetIamPolicyCall ¶
added in v0.144.0
type ProjectsLocationsDocumentsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDocumentsGetIamPolicyCall) Context ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsDocumentsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDocumentsGetIamPolicyCall) Do ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.documents.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDocumentsGetIamPolicyCall) Fields ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsDocumentsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDocumentsGetIamPolicyCall) Header ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDocumentsGetIamPolicyCall) IfNoneMatch ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsDocumentsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDocumentsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsDocumentsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsDocumentsService ¶
added in v0.144.0
type ProjectsLocationsDocumentsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDocumentsService ¶
added in v0.144.0
func NewProjectsLocationsDocumentsService(s *Service) *ProjectsLocationsDocumentsService
func (*ProjectsLocationsDocumentsService) GetIamPolicy ¶
added in v0.144.0
func (r *ProjectsLocationsDocumentsService) GetIamPolicy(resource string) *ProjectsLocationsDocumentsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsDocumentsService) SetIamPolicy ¶
added in v0.144.0
func (r *ProjectsLocationsDocumentsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsDocumentsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsDocumentsService) TestIamPermissions ¶
added in v0.144.0
func (r *ProjectsLocationsDocumentsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsDocumentsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsDocumentsSetIamPolicyCall ¶
added in v0.144.0
type ProjectsLocationsDocumentsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDocumentsSetIamPolicyCall) Context ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsDocumentsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDocumentsSetIamPolicyCall) Do ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.documents.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDocumentsSetIamPolicyCall) Fields ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsDocumentsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDocumentsSetIamPolicyCall) Header ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDocumentsTestIamPermissionsCall ¶
added in v0.144.0
type ProjectsLocationsDocumentsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDocumentsTestIamPermissionsCall) Context ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsDocumentsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDocumentsTestIamPermissionsCall) Do ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.documents.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDocumentsTestIamPermissionsCall) Fields ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsDocumentsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDocumentsTestIamPermissionsCall) Header ¶
added in v0.144.0
func (c *ProjectsLocationsDocumentsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "apigeeregistry.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsInstancesCreateCall ¶
type ProjectsLocationsInstancesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesCreateCall) Context ¶
func (c *ProjectsLocationsInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsInstancesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesCreateCall) Do ¶
func (c *ProjectsLocationsInstancesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apigeeregistry.projects.locations.instances.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesCreateCall) Fields ¶
func (c *ProjectsLocationsInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesCreateCall) Header ¶
func (c *ProjectsLocationsInstancesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesCreateCall) InstanceId ¶
func (c *ProjectsLocationsInstancesCreateCall) InstanceId(instanceId string) *ProjectsLocationsInstancesCreateCall

InstanceId sets the optional parameter "instanceId": Required. Identifier to assign to the Instance. Must be unique within scope of the parent resource.

type ProjectsLocationsInstancesDeleteCall ¶
type ProjectsLocationsInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesDeleteCall) Context ¶
func (c *ProjectsLocationsInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesDeleteCall) Do ¶
func (c *ProjectsLocationsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apigeeregistry.projects.locations.instances.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesDeleteCall) Fields ¶
func (c *ProjectsLocationsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesDeleteCall) Header ¶
func (c *ProjectsLocationsInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesGetCall ¶
type ProjectsLocationsInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesGetCall) Context ¶
func (c *ProjectsLocationsInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesGetCall) Do ¶
func (c *ProjectsLocationsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "apigeeregistry.projects.locations.instances.get" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesGetCall) Fields ¶
func (c *ProjectsLocationsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesGetCall) Header ¶
func (c *ProjectsLocationsInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsInstancesGetIamPolicyCall ¶
type ProjectsLocationsInstancesGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsInstancesGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.instances.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsInstancesGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsInstancesGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsInstancesGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsInstancesGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsInstancesGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsInstancesService ¶
type ProjectsLocationsInstancesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsInstancesService ¶
func NewProjectsLocationsInstancesService(s *Service) *ProjectsLocationsInstancesService
func (*ProjectsLocationsInstancesService) Create ¶
func (r *ProjectsLocationsInstancesService) Create(parent string, instance *Instance) *ProjectsLocationsInstancesCreateCall

Create: Provisions instance resources for the Registry.

parent: Parent resource of the Instance, of the form: `projects/*/locations/*`.
func (*ProjectsLocationsInstancesService) Delete ¶
func (r *ProjectsLocationsInstancesService) Delete(name string) *ProjectsLocationsInstancesDeleteCall

Delete: Deletes the Registry instance.

name: The name of the Instance to delete. Format: `projects/*/locations/*/instances/*`.
func (*ProjectsLocationsInstancesService) Get ¶
func (r *ProjectsLocationsInstancesService) Get(name string) *ProjectsLocationsInstancesGetCall

Get: Gets details of a single Instance.

name: The name of the Instance to retrieve. Format: `projects/*/locations/*/instances/*`.
func (*ProjectsLocationsInstancesService) GetIamPolicy ¶
func (r *ProjectsLocationsInstancesService) GetIamPolicy(resource string) *ProjectsLocationsInstancesGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsInstancesService) SetIamPolicy ¶
func (r *ProjectsLocationsInstancesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsInstancesSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsInstancesService) TestIamPermissions ¶
func (r *ProjectsLocationsInstancesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsInstancesTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsInstancesSetIamPolicyCall ¶
type ProjectsLocationsInstancesSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsInstancesSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.instances.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsInstancesSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesTestIamPermissionsCall ¶
type ProjectsLocationsInstancesTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsInstancesTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.instances.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsInstancesTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsListCall ¶
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "apigeeregistry.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) Fields ¶
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsListCall) Filter ¶
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 (https://google.aip.dev/160).

func (*ProjectsLocationsListCall) Header ¶
func (c *ProjectsLocationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsListCall) PageSize ¶
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

func (*ProjectsLocationsListCall) PageToken ¶
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

func (*ProjectsLocationsListCall) Pages ¶
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsCancelCall ¶
type ProjectsLocationsOperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsCancelCall) Context ¶
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsCancelCall) Do ¶
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsCancelCall) Fields ¶
func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsCancelCall) Header ¶
func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsDeleteCall ¶
type ProjectsLocationsOperationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsDeleteCall) Context ¶
func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsDeleteCall) Do ¶
func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apigeeregistry.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsDeleteCall) Fields ¶
func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsDeleteCall) Header ¶
func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsGetCall ¶
type ProjectsLocationsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsGetCall) Context ¶
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsGetCall) Do ¶
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apigeeregistry.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsGetCall) Fields ¶
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsGetCall) Header ¶
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsListCall ¶
type ProjectsLocationsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsListCall) Context ¶
func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsListCall) Do ¶
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)

Do executes the "apigeeregistry.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsListCall) Fields ¶
func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsListCall) Filter ¶
func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*ProjectsLocationsOperationsListCall) Header ¶
func (c *ProjectsLocationsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsOperationsListCall) PageSize ¶
func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*ProjectsLocationsOperationsListCall) PageToken ¶
func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*ProjectsLocationsOperationsListCall) Pages ¶
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsService ¶
type ProjectsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOperationsService ¶
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (*ProjectsLocationsOperationsService) Cancel ¶
func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

- name: The name of the operation resource to be cancelled.

func (*ProjectsLocationsOperationsService) Delete ¶
func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

- name: The name of the operation resource to be deleted.

func (*ProjectsLocationsOperationsService) Get ¶
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

func (*ProjectsLocationsOperationsService) List ¶
func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type ProjectsLocationsRuntimeGetIamPolicyCall ¶
type ProjectsLocationsRuntimeGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRuntimeGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.runtime.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRuntimeGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsRuntimeGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRuntimeGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsRuntimeGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsRuntimeGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsRuntimeService ¶
type ProjectsLocationsRuntimeService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRuntimeService ¶
func NewProjectsLocationsRuntimeService(s *Service) *ProjectsLocationsRuntimeService
func (*ProjectsLocationsRuntimeService) GetIamPolicy ¶
func (r *ProjectsLocationsRuntimeService) GetIamPolicy(resource string) *ProjectsLocationsRuntimeGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsRuntimeService) SetIamPolicy ¶
func (r *ProjectsLocationsRuntimeService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsRuntimeSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsRuntimeService) TestIamPermissions ¶
func (r *ProjectsLocationsRuntimeService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsRuntimeTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsRuntimeSetIamPolicyCall ¶
type ProjectsLocationsRuntimeSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsRuntimeSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apigeeregistry.projects.locations.runtime.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsRuntimeSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRuntimeTestIamPermissionsCall ¶
type ProjectsLocationsRuntimeTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsRuntimeTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apigeeregistry.projects.locations.runtime.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsRuntimeTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	Apis *ProjectsLocationsApisService

	Artifacts *ProjectsLocationsArtifactsService

	Documents *ProjectsLocationsDocumentsService

	Instances *ProjectsLocationsInstancesService

	Operations *ProjectsLocationsOperationsService

	Runtime *ProjectsLocationsRuntimeService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (*ProjectsLocationsService) Get ¶
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- name: Resource name for the location.

func (*ProjectsLocationsService) List ¶
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service.

- name: The resource that owns the locations collection, if applicable.

type ProjectsService ¶
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *Service) *ProjectsService
type RollbackApiDeploymentRequest ¶
type RollbackApiDeploymentRequest struct {
	// RevisionId: Required. The revision ID to roll back to. It must be a revision
	// of the same deployment. Example: `c7cfa2a8`
	RevisionId string `json:"revisionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RevisionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RevisionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RollbackApiDeploymentRequest: Request message for RollbackApiDeployment.

func (RollbackApiDeploymentRequest) MarshalJSON ¶
func (s RollbackApiDeploymentRequest) MarshalJSON() ([]byte, error)
type RollbackApiSpecRequest ¶
type RollbackApiSpecRequest struct {
	// RevisionId: Required. The revision ID to roll back to. It must be a revision
	// of the same spec. Example: `c7cfa2a8`
	RevisionId string `json:"revisionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RevisionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RevisionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RollbackApiSpecRequest: Request message for RollbackApiSpec.

func (RollbackApiSpecRequest) MarshalJSON ¶
func (s RollbackApiSpecRequest) MarshalJSON() ([]byte, error)
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
type TagApiDeploymentRevisionRequest ¶
type TagApiDeploymentRevisionRequest struct {
	// Tag: Required. The tag to apply. The tag should be at most 40 characters,
	// and match `a-z{3,39}`.
	Tag string `json:"tag,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Tag") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Tag") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TagApiDeploymentRevisionRequest: Request message for TagApiDeploymentRevision.

func (TagApiDeploymentRevisionRequest) MarshalJSON ¶
func (s TagApiDeploymentRevisionRequest) MarshalJSON() ([]byte, error)
type TagApiSpecRevisionRequest ¶
type TagApiSpecRevisionRequest struct {
	// Tag: Required. The tag to apply. The tag should be at most 40 characters,
	// and match `a-z{3,39}`.
	Tag string `json:"tag,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Tag") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Tag") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TagApiSpecRevisionRequest: Request message for TagApiSpecRevision.

func (TagApiSpecRevisionRequest) MarshalJSON ¶
func (s TagApiSpecRevisionRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest ¶
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
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse ¶
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
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
apigeeregistry-gen.go
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

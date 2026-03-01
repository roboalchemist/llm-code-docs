# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apphub/v1alpha

Title: apphub package - google.golang.org/api/apphub/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apphub/v1alpha

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
apphub
 
v1alpha
apphub
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

Package apphub provides access to the App Hub API.

For product documentation, see: https://cloud.google.com/app-hub/docs/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/apphub/v1alpha"
...
ctx := context.Background()
apphubService, err := apphub.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

apphubService, err := apphub.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
apphubService, err := apphub.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type APIService
func New(client *http.Client) (*APIService, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*APIService, error)
type Application
func (s Application) MarshalJSON() ([]byte, error)
type Attributes
func (s Attributes) MarshalJSON() ([]byte, error)
type AuditConfig
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
type Binding
func (s Binding) MarshalJSON() ([]byte, error)
type Boundary
func (s Boundary) MarshalJSON() ([]byte, error)
type CancelOperationRequest
type Channel
func (s Channel) MarshalJSON() ([]byte, error)
type ContactInfo
func (s ContactInfo) MarshalJSON() ([]byte, error)
type Criticality
func (s Criticality) MarshalJSON() ([]byte, error)
type DetachServiceProjectAttachmentRequest
type DetachServiceProjectAttachmentResponse
type DiscoveredService
func (s DiscoveredService) MarshalJSON() ([]byte, error)
type DiscoveredWorkload
func (s DiscoveredWorkload) MarshalJSON() ([]byte, error)
type Empty
type Environment
func (s Environment) MarshalJSON() ([]byte, error)
type Expr
func (s Expr) MarshalJSON() ([]byte, error)
type ExtendedMetadata
func (s ExtendedMetadata) MarshalJSON() ([]byte, error)
type ExtendedMetadataSchema
func (s ExtendedMetadataSchema) MarshalJSON() ([]byte, error)
type FindUnregisteredServicesResponse
func (s FindUnregisteredServicesResponse) MarshalJSON() ([]byte, error)
type FindUnregisteredWorkloadsResponse
func (s FindUnregisteredWorkloadsResponse) MarshalJSON() ([]byte, error)
type FunctionalType
func (s FunctionalType) MarshalJSON() ([]byte, error)
type Identity
func (s Identity) MarshalJSON() ([]byte, error)
type ListApplicationsResponse
func (s ListApplicationsResponse) MarshalJSON() ([]byte, error)
type ListDiscoveredServicesResponse
func (s ListDiscoveredServicesResponse) MarshalJSON() ([]byte, error)
type ListDiscoveredWorkloadsResponse
func (s ListDiscoveredWorkloadsResponse) MarshalJSON() ([]byte, error)
type ListExtendedMetadataSchemasResponse
func (s ListExtendedMetadataSchemasResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListServiceProjectAttachmentsResponse
func (s ListServiceProjectAttachmentsResponse) MarshalJSON() ([]byte, error)
type ListServicesResponse
func (s ListServicesResponse) MarshalJSON() ([]byte, error)
type ListWorkloadsResponse
func (s ListWorkloadsResponse) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type LookupDiscoveredServiceResponse
func (s LookupDiscoveredServiceResponse) MarshalJSON() ([]byte, error)
type LookupDiscoveredWorkloadResponse
func (s LookupDiscoveredWorkloadResponse) MarshalJSON() ([]byte, error)
type LookupServiceProjectAttachmentResponse
func (s LookupServiceProjectAttachmentResponse) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadata
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsLocationsApplicationsCreateCall
func (c *ProjectsLocationsApplicationsCreateCall) ApplicationId(applicationId string) *ProjectsLocationsApplicationsCreateCall
func (c *ProjectsLocationsApplicationsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsCreateCall
func (c *ProjectsLocationsApplicationsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsCreateCall
func (c *ProjectsLocationsApplicationsCreateCall) Header() http.Header
func (c *ProjectsLocationsApplicationsCreateCall) RequestId(requestId string) *ProjectsLocationsApplicationsCreateCall
type ProjectsLocationsApplicationsDeleteCall
func (c *ProjectsLocationsApplicationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDeleteCall
func (c *ProjectsLocationsApplicationsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDeleteCall
func (c *ProjectsLocationsApplicationsDeleteCall) Header() http.Header
func (c *ProjectsLocationsApplicationsDeleteCall) RequestId(requestId string) *ProjectsLocationsApplicationsDeleteCall
type ProjectsLocationsApplicationsGetCall
func (c *ProjectsLocationsApplicationsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsGetCall
func (c *ProjectsLocationsApplicationsGetCall) Do(opts ...googleapi.CallOption) (*Application, error)
func (c *ProjectsLocationsApplicationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsGetCall
func (c *ProjectsLocationsApplicationsGetCall) Header() http.Header
func (c *ProjectsLocationsApplicationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsGetCall
type ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApplicationsGetIamPolicyCall
type ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) Do(opts ...googleapi.CallOption) (*ListApplicationsResponse, error)
func (c *ProjectsLocationsApplicationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) Filter(filter string) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) Header() http.Header
func (c *ProjectsLocationsApplicationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) OrderBy(orderBy string) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsListCall
func (c *ProjectsLocationsApplicationsListCall) Pages(ctx context.Context, f func(*ListApplicationsResponse) error) error
type ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsPatchCall) RequestId(requestId string) *ProjectsLocationsApplicationsPatchCall
func (c *ProjectsLocationsApplicationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsPatchCall
type ProjectsLocationsApplicationsService
func NewProjectsLocationsApplicationsService(s *APIService) *ProjectsLocationsApplicationsService
func (r *ProjectsLocationsApplicationsService) Create(parent string, application *Application) *ProjectsLocationsApplicationsCreateCall
func (r *ProjectsLocationsApplicationsService) Delete(name string) *ProjectsLocationsApplicationsDeleteCall
func (r *ProjectsLocationsApplicationsService) Get(name string) *ProjectsLocationsApplicationsGetCall
func (r *ProjectsLocationsApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsApplicationsGetIamPolicyCall
func (r *ProjectsLocationsApplicationsService) List(parent string) *ProjectsLocationsApplicationsListCall
func (r *ProjectsLocationsApplicationsService) Patch(name string, application *Application) *ProjectsLocationsApplicationsPatchCall
func (r *ProjectsLocationsApplicationsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApplicationsSetIamPolicyCall
func (r *ProjectsLocationsApplicationsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApplicationsTestIamPermissionsCall
type ProjectsLocationsApplicationsServicesCreateCall
func (c *ProjectsLocationsApplicationsServicesCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesCreateCall
func (c *ProjectsLocationsApplicationsServicesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesCreateCall
func (c *ProjectsLocationsApplicationsServicesCreateCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesCreateCall) RequestId(requestId string) *ProjectsLocationsApplicationsServicesCreateCall
func (c *ProjectsLocationsApplicationsServicesCreateCall) ServiceId(serviceId string) *ProjectsLocationsApplicationsServicesCreateCall
type ProjectsLocationsApplicationsServicesDeleteCall
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesDeleteCall
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesDeleteCall
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesDeleteCall) RequestId(requestId string) *ProjectsLocationsApplicationsServicesDeleteCall
type ProjectsLocationsApplicationsServicesGetCall
func (c *ProjectsLocationsApplicationsServicesGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesGetCall
func (c *ProjectsLocationsApplicationsServicesGetCall) Do(opts ...googleapi.CallOption) (*Service, error)
func (c *ProjectsLocationsApplicationsServicesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesGetCall
func (c *ProjectsLocationsApplicationsServicesGetCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsServicesGetCall
type ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) Do(opts ...googleapi.CallOption) (*ListServicesResponse, error)
func (c *ProjectsLocationsApplicationsServicesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) Filter(filter string) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) OrderBy(orderBy string) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsServicesListCall
func (c *ProjectsLocationsApplicationsServicesListCall) Pages(ctx context.Context, f func(*ListServicesResponse) error) error
type ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsServicesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsServicesPatchCall) RequestId(requestId string) *ProjectsLocationsApplicationsServicesPatchCall
func (c *ProjectsLocationsApplicationsServicesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsServicesPatchCall
type ProjectsLocationsApplicationsServicesService
func NewProjectsLocationsApplicationsServicesService(s *APIService) *ProjectsLocationsApplicationsServicesService
func (r *ProjectsLocationsApplicationsServicesService) Create(parent string, service *Service) *ProjectsLocationsApplicationsServicesCreateCall
func (r *ProjectsLocationsApplicationsServicesService) Delete(name string) *ProjectsLocationsApplicationsServicesDeleteCall
func (r *ProjectsLocationsApplicationsServicesService) Get(name string) *ProjectsLocationsApplicationsServicesGetCall
func (r *ProjectsLocationsApplicationsServicesService) List(parent string) *ProjectsLocationsApplicationsServicesListCall
func (r *ProjectsLocationsApplicationsServicesService) Patch(name string, service *Service) *ProjectsLocationsApplicationsServicesPatchCall
type ProjectsLocationsApplicationsSetIamPolicyCall
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsSetIamPolicyCall
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsSetIamPolicyCall
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApplicationsWorkloadsCreateCall
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsCreateCall
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsCreateCall
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Header() http.Header
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) RequestId(requestId string) *ProjectsLocationsApplicationsWorkloadsCreateCall
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) WorkloadId(workloadId string) *ProjectsLocationsApplicationsWorkloadsCreateCall
type ProjectsLocationsApplicationsWorkloadsDeleteCall
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsDeleteCall
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsDeleteCall
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Header() http.Header
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) RequestId(requestId string) *ProjectsLocationsApplicationsWorkloadsDeleteCall
type ProjectsLocationsApplicationsWorkloadsGetCall
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsGetCall
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Do(opts ...googleapi.CallOption) (*Workload, error)
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsGetCall
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Header() http.Header
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsWorkloadsGetCall
type ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Do(opts ...googleapi.CallOption) (*ListWorkloadsResponse, error)
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Filter(filter string) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Header() http.Header
func (c *ProjectsLocationsApplicationsWorkloadsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) OrderBy(orderBy string) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsWorkloadsListCall
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Pages(ctx context.Context, f func(*ListWorkloadsResponse) error) error
type ProjectsLocationsApplicationsWorkloadsPatchCall
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsPatchCall
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsPatchCall
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Header() http.Header
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) RequestId(requestId string) *ProjectsLocationsApplicationsWorkloadsPatchCall
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsWorkloadsPatchCall
type ProjectsLocationsApplicationsWorkloadsService
func NewProjectsLocationsApplicationsWorkloadsService(s *APIService) *ProjectsLocationsApplicationsWorkloadsService
func (r *ProjectsLocationsApplicationsWorkloadsService) Create(parent string, workload *Workload) *ProjectsLocationsApplicationsWorkloadsCreateCall
func (r *ProjectsLocationsApplicationsWorkloadsService) Delete(name string) *ProjectsLocationsApplicationsWorkloadsDeleteCall
func (r *ProjectsLocationsApplicationsWorkloadsService) Get(name string) *ProjectsLocationsApplicationsWorkloadsGetCall
func (r *ProjectsLocationsApplicationsWorkloadsService) List(parent string) *ProjectsLocationsApplicationsWorkloadsListCall
func (r *ProjectsLocationsApplicationsWorkloadsService) Patch(name string, workload *Workload) *ProjectsLocationsApplicationsWorkloadsPatchCall
type ProjectsLocationsDetachServiceProjectAttachmentCall
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Context(ctx context.Context) *ProjectsLocationsDetachServiceProjectAttachmentCall
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Do(opts ...googleapi.CallOption) (*DetachServiceProjectAttachmentResponse, error)
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Fields(s ...googleapi.Field) *ProjectsLocationsDetachServiceProjectAttachmentCall
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Header() http.Header
type ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Do(opts ...googleapi.CallOption) (*FindUnregisteredServicesResponse, error)
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Filter(filter string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Pages(ctx context.Context, f func(*FindUnregisteredServicesResponse) error) error
type ProjectsLocationsDiscoveredServicesGetCall
func (c *ProjectsLocationsDiscoveredServicesGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesGetCall
func (c *ProjectsLocationsDiscoveredServicesGetCall) Do(opts ...googleapi.CallOption) (*DiscoveredService, error)
func (c *ProjectsLocationsDiscoveredServicesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesGetCall
func (c *ProjectsLocationsDiscoveredServicesGetCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredServicesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesGetCall
type ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) Do(opts ...googleapi.CallOption) (*ListDiscoveredServicesResponse, error)
func (c *ProjectsLocationsDiscoveredServicesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) Filter(filter string) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredServicesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredServicesListCall
func (c *ProjectsLocationsDiscoveredServicesListCall) Pages(ctx context.Context, f func(*ListDiscoveredServicesResponse) error) error
type ProjectsLocationsDiscoveredServicesLookupCall
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesLookupCall
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Do(opts ...googleapi.CallOption) (*LookupDiscoveredServiceResponse, error)
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesLookupCall
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredServicesLookupCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesLookupCall
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Uri(uri string) *ProjectsLocationsDiscoveredServicesLookupCall
type ProjectsLocationsDiscoveredServicesService
func NewProjectsLocationsDiscoveredServicesService(s *APIService) *ProjectsLocationsDiscoveredServicesService
func (r *ProjectsLocationsDiscoveredServicesService) FindUnregistered(parent string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall
func (r *ProjectsLocationsDiscoveredServicesService) Get(name string) *ProjectsLocationsDiscoveredServicesGetCall
func (r *ProjectsLocationsDiscoveredServicesService) List(parent string) *ProjectsLocationsDiscoveredServicesListCall
func (r *ProjectsLocationsDiscoveredServicesService) Lookup(parent string) *ProjectsLocationsDiscoveredServicesLookupCall
type ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Do(opts ...googleapi.CallOption) (*FindUnregisteredWorkloadsResponse, error)
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Filter(filter string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Pages(ctx context.Context, f func(*FindUnregisteredWorkloadsResponse) error) error
type ProjectsLocationsDiscoveredWorkloadsGetCall
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsGetCall
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Do(opts ...googleapi.CallOption) (*DiscoveredWorkload, error)
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsGetCall
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsGetCall
type ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Do(opts ...googleapi.CallOption) (*ListDiscoveredWorkloadsResponse, error)
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Filter(filter string) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredWorkloadsListCall
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Pages(ctx context.Context, f func(*ListDiscoveredWorkloadsResponse) error) error
type ProjectsLocationsDiscoveredWorkloadsLookupCall
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsLookupCall
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Do(opts ...googleapi.CallOption) (*LookupDiscoveredWorkloadResponse, error)
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsLookupCall
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsLookupCall
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Uri(uri string) *ProjectsLocationsDiscoveredWorkloadsLookupCall
type ProjectsLocationsDiscoveredWorkloadsService
func NewProjectsLocationsDiscoveredWorkloadsService(s *APIService) *ProjectsLocationsDiscoveredWorkloadsService
func (r *ProjectsLocationsDiscoveredWorkloadsService) FindUnregistered(parent string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall
func (r *ProjectsLocationsDiscoveredWorkloadsService) Get(name string) *ProjectsLocationsDiscoveredWorkloadsGetCall
func (r *ProjectsLocationsDiscoveredWorkloadsService) List(parent string) *ProjectsLocationsDiscoveredWorkloadsListCall
func (r *ProjectsLocationsDiscoveredWorkloadsService) Lookup(parent string) *ProjectsLocationsDiscoveredWorkloadsLookupCall
type ProjectsLocationsExtendedMetadataSchemasGetCall
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Context(ctx context.Context) *ProjectsLocationsExtendedMetadataSchemasGetCall
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Do(opts ...googleapi.CallOption) (*ExtendedMetadataSchema, error)
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsExtendedMetadataSchemasGetCall
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Header() http.Header
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsExtendedMetadataSchemasGetCall
type ProjectsLocationsExtendedMetadataSchemasListCall
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Context(ctx context.Context) *ProjectsLocationsExtendedMetadataSchemasListCall
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Do(opts ...googleapi.CallOption) (*ListExtendedMetadataSchemasResponse, error)
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Fields(s ...googleapi.Field) *ProjectsLocationsExtendedMetadataSchemasListCall
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Header() http.Header
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) IfNoneMatch(entityTag string) *ProjectsLocationsExtendedMetadataSchemasListCall
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) PageSize(pageSize int64) *ProjectsLocationsExtendedMetadataSchemasListCall
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) PageToken(pageToken string) *ProjectsLocationsExtendedMetadataSchemasListCall
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Pages(ctx context.Context, f func(*ListExtendedMetadataSchemasResponse) error) error
type ProjectsLocationsExtendedMetadataSchemasService
func NewProjectsLocationsExtendedMetadataSchemasService(s *APIService) *ProjectsLocationsExtendedMetadataSchemasService
func (r *ProjectsLocationsExtendedMetadataSchemasService) Get(name string) *ProjectsLocationsExtendedMetadataSchemasGetCall
func (r *ProjectsLocationsExtendedMetadataSchemasService) List(parent string) *ProjectsLocationsExtendedMetadataSchemasListCall
type ProjectsLocationsGetBoundaryCall
func (c *ProjectsLocationsGetBoundaryCall) Context(ctx context.Context) *ProjectsLocationsGetBoundaryCall
func (c *ProjectsLocationsGetBoundaryCall) Do(opts ...googleapi.CallOption) (*Boundary, error)
func (c *ProjectsLocationsGetBoundaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetBoundaryCall
func (c *ProjectsLocationsGetBoundaryCall) Header() http.Header
func (c *ProjectsLocationsGetBoundaryCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetBoundaryCall
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
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
type ProjectsLocationsLookupServiceProjectAttachmentCall
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Context(ctx context.Context) *ProjectsLocationsLookupServiceProjectAttachmentCall
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Do(opts ...googleapi.CallOption) (*LookupServiceProjectAttachmentResponse, error)
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Fields(s ...googleapi.Field) *ProjectsLocationsLookupServiceProjectAttachmentCall
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Header() http.Header
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) IfNoneMatch(entityTag string) *ProjectsLocationsLookupServiceProjectAttachmentCall
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
func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall
type ProjectsLocationsOperationsService
func NewProjectsLocationsOperationsService(s *APIService) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall
func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall
func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall
type ProjectsLocationsService
func NewProjectsLocationsService(s *APIService) *ProjectsLocationsService
func (r *ProjectsLocationsService) DetachServiceProjectAttachment(name string, ...) *ProjectsLocationsDetachServiceProjectAttachmentCall
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) GetBoundary(name string) *ProjectsLocationsGetBoundaryCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
func (r *ProjectsLocationsService) LookupServiceProjectAttachment(name string) *ProjectsLocationsLookupServiceProjectAttachmentCall
func (r *ProjectsLocationsService) UpdateBoundary(name string, boundary *Boundary) *ProjectsLocationsUpdateBoundaryCall
type ProjectsLocationsServiceProjectAttachmentsCreateCall
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsCreateCall
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsCreateCall
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Header() http.Header
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) RequestId(requestId string) *ProjectsLocationsServiceProjectAttachmentsCreateCall
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) ServiceProjectAttachmentId(serviceProjectAttachmentId string) *ProjectsLocationsServiceProjectAttachmentsCreateCall
type ProjectsLocationsServiceProjectAttachmentsDeleteCall
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsDeleteCall
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsDeleteCall
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Header() http.Header
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) RequestId(requestId string) *ProjectsLocationsServiceProjectAttachmentsDeleteCall
type ProjectsLocationsServiceProjectAttachmentsGetCall
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsGetCall
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Do(opts ...googleapi.CallOption) (*ServiceProjectAttachment, error)
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsGetCall
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Header() http.Header
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsServiceProjectAttachmentsGetCall
type ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Do(opts ...googleapi.CallOption) (*ListServiceProjectAttachmentsResponse, error)
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Filter(filter string) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Header() http.Header
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) OrderBy(orderBy string) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) PageSize(pageSize int64) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) PageToken(pageToken string) *ProjectsLocationsServiceProjectAttachmentsListCall
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Pages(ctx context.Context, f func(*ListServiceProjectAttachmentsResponse) error) error
type ProjectsLocationsServiceProjectAttachmentsService
func NewProjectsLocationsServiceProjectAttachmentsService(s *APIService) *ProjectsLocationsServiceProjectAttachmentsService
func (r *ProjectsLocationsServiceProjectAttachmentsService) Create(parent string, serviceprojectattachment *ServiceProjectAttachment) *ProjectsLocationsServiceProjectAttachmentsCreateCall
func (r *ProjectsLocationsServiceProjectAttachmentsService) Delete(name string) *ProjectsLocationsServiceProjectAttachmentsDeleteCall
func (r *ProjectsLocationsServiceProjectAttachmentsService) Get(name string) *ProjectsLocationsServiceProjectAttachmentsGetCall
func (r *ProjectsLocationsServiceProjectAttachmentsService) List(parent string) *ProjectsLocationsServiceProjectAttachmentsListCall
type ProjectsLocationsUpdateBoundaryCall
func (c *ProjectsLocationsUpdateBoundaryCall) Context(ctx context.Context) *ProjectsLocationsUpdateBoundaryCall
func (c *ProjectsLocationsUpdateBoundaryCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsUpdateBoundaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsUpdateBoundaryCall
func (c *ProjectsLocationsUpdateBoundaryCall) Header() http.Header
func (c *ProjectsLocationsUpdateBoundaryCall) RequestId(requestId string) *ProjectsLocationsUpdateBoundaryCall
func (c *ProjectsLocationsUpdateBoundaryCall) UpdateMask(updateMask string) *ProjectsLocationsUpdateBoundaryCall
type ProjectsService
func NewProjectsService(s *APIService) *ProjectsService
type RegistrationType
func (s RegistrationType) MarshalJSON() ([]byte, error)
type Scope
func (s Scope) MarshalJSON() ([]byte, error)
type Service
func (s Service) MarshalJSON() ([]byte, error)
type ServiceProjectAttachment
func (s ServiceProjectAttachment) MarshalJSON() ([]byte, error)
type ServiceProperties
func (s ServiceProperties) MarshalJSON() ([]byte, error)
type ServiceReference
func (s ServiceReference) MarshalJSON() ([]byte, error)
type SetIamPolicyRequest
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type Workload
func (s Workload) MarshalJSON() ([]byte, error)
type WorkloadProperties
func (s WorkloadProperties) MarshalJSON() ([]byte, error)
type WorkloadReference
func (s WorkloadReference) MarshalJSON() ([]byte, error)
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
type APIService ¶
type APIService struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Projects *ProjectsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
func NewService(ctx context.Context, opts ...option.ClientOption) (*APIService, error)

NewService creates a new APIService.

type Application ¶
type Application struct {
	// Attributes: Optional. Consumer provided attributes.
	Attributes *Attributes `json:"attributes,omitempty"`
	// CreateTime: Output only. Create time.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. User-defined description of an Application. Can have
	// a maximum length of 2048 characters.
	Description string `json:"description,omitempty"`
	// DisplayName: Optional. User-defined name for the Application. Can have a
	// maximum length of 63 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Identifier. The resource name of an Application. Format:
	// "projects/{host-project-id}/locations/{location}/applications/{application-i
	// d}"
	Name string `json:"name,omitempty"`
	// Scope: Required. Immutable. Defines what data can be included into this
	// Application. Limits which Services and Workloads can be registered.
	Scope *Scope `json:"scope,omitempty"`
	// State: Output only. Application state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified state.
	//   "CREATING" - The Application is being created.
	//   "ACTIVE" - The Application is ready to register Services and Workloads.
	//   "DELETING" - The Application is being deleted.
	State string `json:"state,omitempty"`
	// Uid: Output only. A universally unique identifier (in UUID4 format) for the
	// `Application`.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Update time.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Application: Application defines the governance boundary for App Hub entities that perform a logical end-to-end business function. App Hub supports application level IAM permission to align with governance requirements.

func (Application) MarshalJSON ¶
func (s Application) MarshalJSON() ([]byte, error)
type Attributes ¶
type Attributes struct {
	// BusinessOwners: Optional. Business team that ensures user needs are met and
	// value is delivered
	BusinessOwners []*ContactInfo `json:"businessOwners,omitempty"`
	// Criticality: Optional. User-defined criticality information.
	Criticality *Criticality `json:"criticality,omitempty"`
	// DeveloperOwners: Optional. Developer team that owns development and coding.
	DeveloperOwners []*ContactInfo `json:"developerOwners,omitempty"`
	// Environment: Optional. User-defined environment information.
	Environment *Environment `json:"environment,omitempty"`
	// OperatorOwners: Optional. Operator team that ensures runtime and operations.
	OperatorOwners []*ContactInfo `json:"operatorOwners,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BusinessOwners") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BusinessOwners") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Attributes: Consumer provided attributes.

func (Attributes) MarshalJSON ¶
func (s Attributes) MarshalJSON() ([]byte, error)
type AuditConfig ¶
type AuditConfig struct {
	// AuditLogConfigs: The configuration for logging of each type of permission.
	AuditLogConfigs []*AuditLogConfig `json:"auditLogConfigs,omitempty"`
	// Service: Specifies a service that will be enabled for audit logging. For
	// example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices`
	// is a special value that covers all services.
	Service string `json:"service,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuditLogConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuditLogConfigs") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuditConfig: Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

func (AuditConfig) MarshalJSON ¶
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig ¶
type AuditLogConfig struct {
	// ExemptedMembers: Specifies the identities that do not cause logging for this
	// type of permission. Follows the same format of Binding.members.
	ExemptedMembers []string `json:"exemptedMembers,omitempty"`
	// LogType: The log type that this config enables.
	//
	// Possible values:
	//   "LOG_TYPE_UNSPECIFIED" - Default case. Should never be this.
	//   "ADMIN_READ" - Admin reads. Example: CloudIAM getIamPolicy
	//   "DATA_WRITE" - Data writes. Example: CloudSQL Users create
	//   "DATA_READ" - Data reads. Example: CloudSQL Users list
	LogType string `json:"logType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExemptedMembers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExemptedMembers") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuditLogConfig: Provides the configuration for logging a type of permissions. Example: { "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

func (AuditLogConfig) MarshalJSON ¶
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
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
func (s Binding) MarshalJSON() ([]byte, error)
type Boundary ¶
added in v0.257.0
type Boundary struct {
	// CreateTime: Output only. Create time.
	CreateTime string `json:"createTime,omitempty"`
	// CrmNode: Optional. The resource name of the CRM node being attached to the
	// boundary. Format: `projects/{project-number}` or `projects/{project-id}`
	CrmNode string `json:"crmNode,omitempty"`
	// Name: Identifier. The resource name of the boundary. Format:
	// "projects/{project}/locations/{location}/boundary"
	Name string `json:"name,omitempty"`
	// Type: Output only. Boundary type.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified type.
	//   "AUTOMATIC" - The Boundary automatically includes all descendants of the
	// CRM node.
	//   "MANUAL" - The list of projects within the Boundary is managed by the
	// user.
	//   "MANAGED_AUTOMATIC" - The Boundary automatically includes all descendants
	// of the CRM node, which is set via App Management folder capability.
	Type string `json:"type,omitempty"`
	// UpdateTime: Output only. Update time.
	UpdateTime string `json:"updateTime,omitempty"`

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

Boundary: Application management boundary.

func (Boundary) MarshalJSON ¶
added in v0.257.0
func (s Boundary) MarshalJSON() ([]byte, error)
type CancelOperationRequest ¶
type CancelOperationRequest struct {
}

CancelOperationRequest: The request message for Operations.CancelOperation.

type Channel ¶
type Channel struct {
	// Uri: Required. URI of the channel.
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

Channel: Separate message to accommodate custom formats across IRC and Slack.

func (Channel) MarshalJSON ¶
func (s Channel) MarshalJSON() ([]byte, error)
type ContactInfo ¶
type ContactInfo struct {
	// Channel: Optional. Communication channel of the contacts.
	Channel *Channel `json:"channel,omitempty"`
	// DisplayName: Optional. Contact's name. Can have a maximum length of 63
	// characters.
	DisplayName string `json:"displayName,omitempty"`
	// Email: Required. Email address of the contacts.
	Email string `json:"email,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Channel") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Channel") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ContactInfo: Contact information of stakeholders.

func (ContactInfo) MarshalJSON ¶
func (s ContactInfo) MarshalJSON() ([]byte, error)
type Criticality ¶
type Criticality struct {
	// Level: Optional. Criticality level. Can contain only lowercase letters,
	// numeric characters, underscores, and dashes. Can have a maximum length of 63
	// characters. Deprecated: Please refer to type instead.
	Level string `json:"level,omitempty"`
	// MissionCritical: Optional. Indicates mission-critical Application, Service,
	// or Workload. Deprecated: Please refer to type instead.
	MissionCritical bool `json:"missionCritical,omitempty"`
	// Type: Required. Criticality Type.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified type.
	//   "MISSION_CRITICAL" - Mission critical service, application or workload.
	//   "HIGH" - High impact.
	//   "MEDIUM" - Medium impact.
	//   "LOW" - Low impact.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Level") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Level") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Criticality: Criticality of the Application, Service, or Workload

func (Criticality) MarshalJSON ¶
func (s Criticality) MarshalJSON() ([]byte, error)
type DetachServiceProjectAttachmentRequest ¶
type DetachServiceProjectAttachmentRequest struct {
}

DetachServiceProjectAttachmentRequest: Request for DetachServiceProjectAttachment.

type DetachServiceProjectAttachmentResponse ¶
type DetachServiceProjectAttachmentResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

DetachServiceProjectAttachmentResponse: Response for DetachServiceProjectAttachment.

type DiscoveredService ¶
type DiscoveredService struct {
	// Name: Identifier. The resource name of the discovered service. Format:
	// "projects/{host-project-id}/locations/{location}/discoveredServices/{uuid}"
	Name string `json:"name,omitempty"`
	// ServiceProperties: Output only. Properties of an underlying compute resource
	// that can comprise a Service. These are immutable.
	ServiceProperties *ServiceProperties `json:"serviceProperties,omitempty"`
	// ServiceReference: Output only. Reference to an underlying networking
	// resource that can comprise a Service. These are immutable.
	ServiceReference *ServiceReference `json:"serviceReference,omitempty"`

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

DiscoveredService: DiscoveredService is a network or API interface that exposes some functionality to clients for consumption over the network. A discovered service can be registered to a App Hub service.

func (DiscoveredService) MarshalJSON ¶
func (s DiscoveredService) MarshalJSON() ([]byte, error)
type DiscoveredWorkload ¶
type DiscoveredWorkload struct {
	// Name: Identifier. The resource name of the discovered workload. Format:
	// "projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}"
	// `
	Name string `json:"name,omitempty"`
	// WorkloadProperties: Output only. Properties of an underlying compute
	// resource represented by the Workload. These are immutable.
	WorkloadProperties *WorkloadProperties `json:"workloadProperties,omitempty"`
	// WorkloadReference: Output only. Reference of an underlying compute resource
	// represented by the Workload. These are immutable.
	WorkloadReference *WorkloadReference `json:"workloadReference,omitempty"`

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

DiscoveredWorkload: DiscoveredWorkload is a binary deployment (such as managed instance groups (MIGs) and GKE deployments) that performs the smallest logical subset of business functionality. A discovered workload can be registered to an App Hub Workload.

func (DiscoveredWorkload) MarshalJSON ¶
func (s DiscoveredWorkload) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type Environment ¶
type Environment struct {
	// Environment: Optional. Environment name. Can contain only lowercase letters,
	// numeric characters, underscores, and dashes. Can have a maximum length of 63
	// characters. Deprecated: Please refer to type instead.
	Environment string `json:"environment,omitempty"`
	// Type: Required. Environment Type.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified type.
	//   "PRODUCTION" - Production environment.
	//   "STAGING" - Staging environment.
	//   "TEST" - Test environment.
	//   "DEVELOPMENT" - Development environment.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Environment") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Environment") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Environment: Environment of the Application, Service, or Workload

func (Environment) MarshalJSON ¶
func (s Environment) MarshalJSON() ([]byte, error)
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
type ExtendedMetadata ¶
added in v0.257.0
type ExtendedMetadata struct {
	// MetadataStruct: Output only. The metadata contents.
	MetadataStruct googleapi.RawMessage `json:"metadataStruct,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MetadataStruct") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MetadataStruct") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExtendedMetadata: Additional metadata for a Service or Workload.

func (ExtendedMetadata) MarshalJSON ¶
added in v0.257.0
func (s ExtendedMetadata) MarshalJSON() ([]byte, error)
type ExtendedMetadataSchema ¶
added in v0.258.0
type ExtendedMetadataSchema struct {
	// JsonSchema: Output only. The JSON schema as a string.
	JsonSchema string `json:"jsonSchema,omitempty"`
	// Name: Identifier. Resource name of the schema. Format:
	// projects//locations//extendedMetadataSchemas/
	Name string `json:"name,omitempty"`
	// SchemaVersion: Output only. The version of the schema. New versions are
	// required to be backwards compatible.
	SchemaVersion int64 `json:"schemaVersion,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "JsonSchema") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "JsonSchema") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExtendedMetadataSchema: ExtendedMetadataSchema represents a schema for extended metadata of a service or workload.

func (ExtendedMetadataSchema) MarshalJSON ¶
added in v0.258.0
func (s ExtendedMetadataSchema) MarshalJSON() ([]byte, error)
type FindUnregisteredServicesResponse ¶
type FindUnregisteredServicesResponse struct {
	// DiscoveredServices: List of Discovered Services.
	DiscoveredServices []*DiscoveredService `json:"discoveredServices,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredServices") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredServices") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FindUnregisteredServicesResponse: Response for FindUnregisteredServices.

func (FindUnregisteredServicesResponse) MarshalJSON ¶
func (s FindUnregisteredServicesResponse) MarshalJSON() ([]byte, error)
type FindUnregisteredWorkloadsResponse ¶
type FindUnregisteredWorkloadsResponse struct {
	// DiscoveredWorkloads: List of Discovered Workloads.
	DiscoveredWorkloads []*DiscoveredWorkload `json:"discoveredWorkloads,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredWorkloads") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredWorkloads") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FindUnregisteredWorkloadsResponse: Response for FindUnregisteredWorkloads.

func (FindUnregisteredWorkloadsResponse) MarshalJSON ¶
func (s FindUnregisteredWorkloadsResponse) MarshalJSON() ([]byte, error)
type FunctionalType ¶
added in v0.255.0
type FunctionalType struct {
	// Type: Output only. The functional type of a service or workload.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified type.
	//   "AGENT" - Agent type.
	//   "MCP_SERVER" - MCP Server type.
	Type string `json:"type,omitempty"`
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

FunctionalType: The functional type of a service or workload.

func (FunctionalType) MarshalJSON ¶
added in v0.255.0
func (s FunctionalType) MarshalJSON() ([]byte, error)
type Identity ¶
added in v0.257.0
type Identity struct {
	// Principal: Output only. The principal of the identity. Supported formats: *
	// `sa://my-sa@PROJECT_ID.iam.gserviceaccount.com` for GCP Service Account *
	// `principal://POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/s
	// a/MANAGED_IDENTITY_ID` for Managed Workload Identity
	Principal string `json:"principal,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Principal") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Principal") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Identity: The identity associated with a service or workload.

func (Identity) MarshalJSON ¶
added in v0.257.0
func (s Identity) MarshalJSON() ([]byte, error)
type ListApplicationsResponse ¶
type ListApplicationsResponse struct {
	// Applications: List of Applications.
	Applications []*Application `json:"applications,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Applications") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Applications") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListApplicationsResponse: Response for ListApplications.

func (ListApplicationsResponse) MarshalJSON ¶
func (s ListApplicationsResponse) MarshalJSON() ([]byte, error)
type ListDiscoveredServicesResponse ¶
type ListDiscoveredServicesResponse struct {
	// DiscoveredServices: List of Discovered Services.
	DiscoveredServices []*DiscoveredService `json:"discoveredServices,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredServices") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredServices") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDiscoveredServicesResponse: Response for ListDiscoveredServices.

func (ListDiscoveredServicesResponse) MarshalJSON ¶
func (s ListDiscoveredServicesResponse) MarshalJSON() ([]byte, error)
type ListDiscoveredWorkloadsResponse ¶
type ListDiscoveredWorkloadsResponse struct {
	// DiscoveredWorkloads: List of Discovered Workloads.
	DiscoveredWorkloads []*DiscoveredWorkload `json:"discoveredWorkloads,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredWorkloads") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredWorkloads") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDiscoveredWorkloadsResponse: Response for ListDiscoveredWorkloads.

func (ListDiscoveredWorkloadsResponse) MarshalJSON ¶
func (s ListDiscoveredWorkloadsResponse) MarshalJSON() ([]byte, error)
type ListExtendedMetadataSchemasResponse ¶
added in v0.258.0
type ListExtendedMetadataSchemasResponse struct {
	// ExtendedMetadataSchemas: List of Extended Metadata Schemas.
	ExtendedMetadataSchemas []*ExtendedMetadataSchema `json:"extendedMetadataSchemas,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExtendedMetadataSchemas") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExtendedMetadataSchemas") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListExtendedMetadataSchemasResponse: Response for ListExtendedMetadataSchemas.

func (ListExtendedMetadataSchemasResponse) MarshalJSON ¶
added in v0.258.0
func (s ListExtendedMetadataSchemasResponse) MarshalJSON() ([]byte, error)
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
	// Unreachable: Unordered list. Unreachable resources. Populated when the
	// request sets `ListOperationsRequest.return_partial_success` and reads across
	// collections. For example, when attempting to list all resources across all
	// supported locations.
	Unreachable []string `json:"unreachable,omitempty"`

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
type ListServiceProjectAttachmentsResponse ¶
type ListServiceProjectAttachmentsResponse struct {
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// ServiceProjectAttachments: List of service project attachments.
	ServiceProjectAttachments []*ServiceProjectAttachment `json:"serviceProjectAttachments,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

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

ListServiceProjectAttachmentsResponse: Response for ListServiceProjectAttachments.

func (ListServiceProjectAttachmentsResponse) MarshalJSON ¶
func (s ListServiceProjectAttachmentsResponse) MarshalJSON() ([]byte, error)
type ListServicesResponse ¶
type ListServicesResponse struct {
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Services: List of Services.
	Services []*Service `json:"services,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

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

ListServicesResponse: Response for ListServices.

func (ListServicesResponse) MarshalJSON ¶
func (s ListServicesResponse) MarshalJSON() ([]byte, error)
type ListWorkloadsResponse ¶
type ListWorkloadsResponse struct {
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`
	// Workloads: List of Workloads.
	Workloads []*Workload `json:"workloads,omitempty"`

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

ListWorkloadsResponse: Response for ListWorkloads.

func (ListWorkloadsResponse) MarshalJSON ¶
func (s ListWorkloadsResponse) MarshalJSON() ([]byte, error)
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
type LookupDiscoveredServiceResponse ¶
added in v0.169.0
type LookupDiscoveredServiceResponse struct {
	// DiscoveredService: Discovered Service if exists, empty otherwise.
	DiscoveredService *DiscoveredService `json:"discoveredService,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredService") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredService") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LookupDiscoveredServiceResponse: Response for LookupDiscoveredService.

func (LookupDiscoveredServiceResponse) MarshalJSON ¶
added in v0.169.0
func (s LookupDiscoveredServiceResponse) MarshalJSON() ([]byte, error)
type LookupDiscoveredWorkloadResponse ¶
added in v0.169.0
type LookupDiscoveredWorkloadResponse struct {
	// DiscoveredWorkload: Discovered Workload if exists, empty otherwise.
	DiscoveredWorkload *DiscoveredWorkload `json:"discoveredWorkload,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredWorkload") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredWorkload") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LookupDiscoveredWorkloadResponse: Response for LookupDiscoveredWorkload.

func (LookupDiscoveredWorkloadResponse) MarshalJSON ¶
added in v0.169.0
func (s LookupDiscoveredWorkloadResponse) MarshalJSON() ([]byte, error)
type LookupServiceProjectAttachmentResponse ¶
type LookupServiceProjectAttachmentResponse struct {
	// ServiceProjectAttachment: Service project attachment for a project if
	// exists, empty otherwise.
	ServiceProjectAttachment *ServiceProjectAttachment `json:"serviceProjectAttachment,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ServiceProjectAttachment")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ServiceProjectAttachment") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LookupServiceProjectAttachmentResponse: Response for LookupServiceProjectAttachment.

func (LookupServiceProjectAttachmentResponse) MarshalJSON ¶
func (s LookupServiceProjectAttachmentResponse) MarshalJSON() ([]byte, error)
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
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have been cancelled
	// successfully have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
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
	// AuditConfigs: Specifies cloud audit logging configuration for this policy.
	AuditConfigs []*AuditConfig `json:"auditConfigs,omitempty"`
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
	// ForceSendFields is a list of field names (e.g. "AuditConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuditConfigs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** ``` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } ``` **YAML example:** ``` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 ``` For a description of IAM and its features, see the IAM documentation (https://cloud.google.com/iam/docs/).

func (Policy) MarshalJSON ¶
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsLocationsApplicationsCreateCall ¶
type ProjectsLocationsApplicationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsCreateCall) ApplicationId ¶
func (c *ProjectsLocationsApplicationsCreateCall) ApplicationId(applicationId string) *ProjectsLocationsApplicationsCreateCall

ApplicationId sets the optional parameter "applicationId": Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.

func (*ProjectsLocationsApplicationsCreateCall) Context ¶
func (c *ProjectsLocationsApplicationsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsCreateCall) Do ¶
func (c *ProjectsLocationsApplicationsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsCreateCall) Fields ¶
func (c *ProjectsLocationsApplicationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsCreateCall) Header ¶
func (c *ProjectsLocationsApplicationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsCreateCall) RequestId ¶
func (c *ProjectsLocationsApplicationsCreateCall) RequestId(requestId string) *ProjectsLocationsApplicationsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsApplicationsDeleteCall ¶
type ProjectsLocationsApplicationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsDeleteCall) Context ¶
func (c *ProjectsLocationsApplicationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsDeleteCall) Do ¶
func (c *ProjectsLocationsApplicationsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsDeleteCall) Fields ¶
func (c *ProjectsLocationsApplicationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsDeleteCall) Header ¶
func (c *ProjectsLocationsApplicationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsDeleteCall) RequestId ¶
func (c *ProjectsLocationsApplicationsDeleteCall) RequestId(requestId string) *ProjectsLocationsApplicationsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsApplicationsGetCall ¶
type ProjectsLocationsApplicationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsGetCall) Context ¶
func (c *ProjectsLocationsApplicationsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsGetCall) Do ¶
func (c *ProjectsLocationsApplicationsGetCall) Do(opts ...googleapi.CallOption) (*Application, error)

Do executes the "apphub.projects.locations.applications.get" call. Any non-2xx status code is an error. Response headers are in either *Application.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsGetCall) Fields ¶
func (c *ProjectsLocationsApplicationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsGetCall) Header ¶
func (c *ProjectsLocationsApplicationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApplicationsGetIamPolicyCall ¶
type ProjectsLocationsApplicationsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apphub.projects.locations.applications.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApplicationsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApplicationsListCall ¶
type ProjectsLocationsApplicationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsListCall) Context ¶
func (c *ProjectsLocationsApplicationsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsListCall) Do ¶
func (c *ProjectsLocationsApplicationsListCall) Do(opts ...googleapi.CallOption) (*ListApplicationsResponse, error)

Do executes the "apphub.projects.locations.applications.list" call. Any non-2xx status code is an error. Response headers are in either *ListApplicationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsListCall) Fields ¶
func (c *ProjectsLocationsApplicationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsListCall) Filter ¶
func (c *ProjectsLocationsApplicationsListCall) Filter(filter string) *ProjectsLocationsApplicationsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsApplicationsListCall) Header ¶
func (c *ProjectsLocationsApplicationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsListCall) OrderBy ¶
func (c *ProjectsLocationsApplicationsListCall) OrderBy(orderBy string) *ProjectsLocationsApplicationsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsApplicationsListCall) PageSize ¶
func (c *ProjectsLocationsApplicationsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsApplicationsListCall) PageToken ¶
func (c *ProjectsLocationsApplicationsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsApplicationsListCall) Pages ¶
func (c *ProjectsLocationsApplicationsListCall) Pages(ctx context.Context, f func(*ListApplicationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApplicationsPatchCall ¶
type ProjectsLocationsApplicationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsPatchCall) Context ¶
func (c *ProjectsLocationsApplicationsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsPatchCall) Do ¶
func (c *ProjectsLocationsApplicationsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsPatchCall) Fields ¶
func (c *ProjectsLocationsApplicationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsPatchCall) Header ¶
func (c *ProjectsLocationsApplicationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsPatchCall) RequestId ¶
func (c *ProjectsLocationsApplicationsPatchCall) RequestId(requestId string) *ProjectsLocationsApplicationsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsApplicationsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApplicationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.

type ProjectsLocationsApplicationsService ¶
type ProjectsLocationsApplicationsService struct {
	Services *ProjectsLocationsApplicationsServicesService

	Workloads *ProjectsLocationsApplicationsWorkloadsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsService ¶
func NewProjectsLocationsApplicationsService(s *APIService) *ProjectsLocationsApplicationsService
func (*ProjectsLocationsApplicationsService) Create ¶
func (r *ProjectsLocationsApplicationsService) Create(parent string, application *Application) *ProjectsLocationsApplicationsCreateCall

Create: Creates an Application in a host project and location.

parent: Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsApplicationsService) Delete ¶
func (r *ProjectsLocationsApplicationsService) Delete(name string) *ProjectsLocationsApplicationsDeleteCall

Delete: Deletes an Application in a host project and location.

name: Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.
func (*ProjectsLocationsApplicationsService) Get ¶
func (r *ProjectsLocationsApplicationsService) Get(name string) *ProjectsLocationsApplicationsGetCall

Get: Gets an Application in a host project and location.

name: Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.
func (*ProjectsLocationsApplicationsService) GetIamPolicy ¶
func (r *ProjectsLocationsApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsApplicationsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApplicationsService) List ¶
func (r *ProjectsLocationsApplicationsService) List(parent string) *ProjectsLocationsApplicationsListCall

List: Lists Applications in a host project and location.

parent: Project and location to list Applications on. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsApplicationsService) Patch ¶
func (r *ProjectsLocationsApplicationsService) Patch(name string, application *Application) *ProjectsLocationsApplicationsPatchCall

Patch: Updates an Application in a host project and location.

name: Identifier. The resource name of an Application. Format: "projects/{host-project-id}/locations/{location}/applications/{application -id}".
func (*ProjectsLocationsApplicationsService) SetIamPolicy ¶
func (r *ProjectsLocationsApplicationsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsApplicationsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApplicationsService) TestIamPermissions ¶
func (r *ProjectsLocationsApplicationsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsApplicationsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApplicationsServicesCreateCall ¶
type ProjectsLocationsApplicationsServicesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesCreateCall) Context ¶
func (c *ProjectsLocationsApplicationsServicesCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesCreateCall) Do ¶
func (c *ProjectsLocationsApplicationsServicesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.services.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesCreateCall) Fields ¶
func (c *ProjectsLocationsApplicationsServicesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesCreateCall) Header ¶
func (c *ProjectsLocationsApplicationsServicesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesCreateCall) RequestId ¶
func (c *ProjectsLocationsApplicationsServicesCreateCall) RequestId(requestId string) *ProjectsLocationsApplicationsServicesCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsApplicationsServicesCreateCall) ServiceId ¶
func (c *ProjectsLocationsApplicationsServicesCreateCall) ServiceId(serviceId string) *ProjectsLocationsApplicationsServicesCreateCall

ServiceId sets the optional parameter "serviceId": Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.

type ProjectsLocationsApplicationsServicesDeleteCall ¶
type ProjectsLocationsApplicationsServicesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesDeleteCall) Context ¶
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesDeleteCall) Do ¶
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.services.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesDeleteCall) Fields ¶
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesDeleteCall) Header ¶
func (c *ProjectsLocationsApplicationsServicesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesDeleteCall) RequestId ¶
func (c *ProjectsLocationsApplicationsServicesDeleteCall) RequestId(requestId string) *ProjectsLocationsApplicationsServicesDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsApplicationsServicesGetCall ¶
type ProjectsLocationsApplicationsServicesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesGetCall) Context ¶
func (c *ProjectsLocationsApplicationsServicesGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesGetCall) Do ¶
func (c *ProjectsLocationsApplicationsServicesGetCall) Do(opts ...googleapi.CallOption) (*Service, error)

Do executes the "apphub.projects.locations.applications.services.get" call. Any non-2xx status code is an error. Response headers are in either *Service.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesGetCall) Fields ¶
func (c *ProjectsLocationsApplicationsServicesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesGetCall) Header ¶
func (c *ProjectsLocationsApplicationsServicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsServicesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsServicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApplicationsServicesListCall ¶
type ProjectsLocationsApplicationsServicesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesListCall) Context ¶
func (c *ProjectsLocationsApplicationsServicesListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesListCall) Do ¶
func (c *ProjectsLocationsApplicationsServicesListCall) Do(opts ...googleapi.CallOption) (*ListServicesResponse, error)

Do executes the "apphub.projects.locations.applications.services.list" call. Any non-2xx status code is an error. Response headers are in either *ListServicesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesListCall) Fields ¶
func (c *ProjectsLocationsApplicationsServicesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesListCall) Filter ¶
func (c *ProjectsLocationsApplicationsServicesListCall) Filter(filter string) *ProjectsLocationsApplicationsServicesListCall

Filter sets the optional parameter "filter": Filtering results

func (*ProjectsLocationsApplicationsServicesListCall) Header ¶
func (c *ProjectsLocationsApplicationsServicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsServicesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsServicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsServicesListCall) OrderBy ¶
func (c *ProjectsLocationsApplicationsServicesListCall) OrderBy(orderBy string) *ProjectsLocationsApplicationsServicesListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results

func (*ProjectsLocationsApplicationsServicesListCall) PageSize ¶
func (c *ProjectsLocationsApplicationsServicesListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsServicesListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsApplicationsServicesListCall) PageToken ¶
func (c *ProjectsLocationsApplicationsServicesListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsServicesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsApplicationsServicesListCall) Pages ¶
func (c *ProjectsLocationsApplicationsServicesListCall) Pages(ctx context.Context, f func(*ListServicesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApplicationsServicesPatchCall ¶
type ProjectsLocationsApplicationsServicesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsServicesPatchCall) Context ¶
func (c *ProjectsLocationsApplicationsServicesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsServicesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsServicesPatchCall) Do ¶
func (c *ProjectsLocationsApplicationsServicesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.services.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsServicesPatchCall) Fields ¶
func (c *ProjectsLocationsApplicationsServicesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsServicesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsServicesPatchCall) Header ¶
func (c *ProjectsLocationsApplicationsServicesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsServicesPatchCall) RequestId ¶
func (c *ProjectsLocationsApplicationsServicesPatchCall) RequestId(requestId string) *ProjectsLocationsApplicationsServicesPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsApplicationsServicesPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApplicationsServicesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsServicesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the Service resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.

type ProjectsLocationsApplicationsServicesService ¶
type ProjectsLocationsApplicationsServicesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsServicesService ¶
func NewProjectsLocationsApplicationsServicesService(s *APIService) *ProjectsLocationsApplicationsServicesService
func (*ProjectsLocationsApplicationsServicesService) Create ¶
func (r *ProjectsLocationsApplicationsServicesService) Create(parent string, service *Service) *ProjectsLocationsApplicationsServicesCreateCall

Create: Creates a Service in an Application.

parent: Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.
func (*ProjectsLocationsApplicationsServicesService) Delete ¶
func (r *ProjectsLocationsApplicationsServicesService) Delete(name string) *ProjectsLocationsApplicationsServicesDeleteCall

Delete: Deletes a Service from an Application.

name: Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/service s/{service}`.
func (*ProjectsLocationsApplicationsServicesService) Get ¶
func (r *ProjectsLocationsApplicationsServicesService) Get(name string) *ProjectsLocationsApplicationsServicesGetCall

Get: Gets a Service in an Application.

name: Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/service s/{service}`.
func (*ProjectsLocationsApplicationsServicesService) List ¶
func (r *ProjectsLocationsApplicationsServicesService) List(parent string) *ProjectsLocationsApplicationsServicesListCall

List: Lists Services in an Application.

parent: Fully qualified name of the parent Application to list Services for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.
func (*ProjectsLocationsApplicationsServicesService) Patch ¶
func (r *ProjectsLocationsApplicationsServicesService) Patch(name string, service *Service) *ProjectsLocationsApplicationsServicesPatchCall

Patch: Updates a Service in an Application.

name: Identifier. The resource name of a Service. Format: "projects/{host-project-id}/locations/{location}/applications/{application -id}/services/{service-id}".
type ProjectsLocationsApplicationsSetIamPolicyCall ¶
type ProjectsLocationsApplicationsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "apphub.projects.locations.applications.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsTestIamPermissionsCall ¶
type ProjectsLocationsApplicationsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApplicationsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "apphub.projects.locations.applications.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsWorkloadsCreateCall ¶
type ProjectsLocationsApplicationsWorkloadsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsWorkloadsCreateCall) Context ¶
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsWorkloadsCreateCall) Do ¶
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.workloads.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsWorkloadsCreateCall) Fields ¶
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsWorkloadsCreateCall) Header ¶
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsWorkloadsCreateCall) RequestId ¶
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) RequestId(requestId string) *ProjectsLocationsApplicationsWorkloadsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsApplicationsWorkloadsCreateCall) WorkloadId ¶
func (c *ProjectsLocationsApplicationsWorkloadsCreateCall) WorkloadId(workloadId string) *ProjectsLocationsApplicationsWorkloadsCreateCall

WorkloadId sets the optional parameter "workloadId": Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.

type ProjectsLocationsApplicationsWorkloadsDeleteCall ¶
type ProjectsLocationsApplicationsWorkloadsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsWorkloadsDeleteCall) Context ¶
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsWorkloadsDeleteCall) Do ¶
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.workloads.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsWorkloadsDeleteCall) Fields ¶
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsWorkloadsDeleteCall) Header ¶
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsWorkloadsDeleteCall) RequestId ¶
func (c *ProjectsLocationsApplicationsWorkloadsDeleteCall) RequestId(requestId string) *ProjectsLocationsApplicationsWorkloadsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsApplicationsWorkloadsGetCall ¶
type ProjectsLocationsApplicationsWorkloadsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsWorkloadsGetCall) Context ¶
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsWorkloadsGetCall) Do ¶
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Do(opts ...googleapi.CallOption) (*Workload, error)

Do executes the "apphub.projects.locations.applications.workloads.get" call. Any non-2xx status code is an error. Response headers are in either *Workload.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsWorkloadsGetCall) Fields ¶
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsWorkloadsGetCall) Header ¶
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsWorkloadsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsWorkloadsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsWorkloadsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApplicationsWorkloadsListCall ¶
type ProjectsLocationsApplicationsWorkloadsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsWorkloadsListCall) Context ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsWorkloadsListCall) Do ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Do(opts ...googleapi.CallOption) (*ListWorkloadsResponse, error)

Do executes the "apphub.projects.locations.applications.workloads.list" call. Any non-2xx status code is an error. Response headers are in either *ListWorkloadsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsWorkloadsListCall) Fields ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsWorkloadsListCall) Filter ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Filter(filter string) *ProjectsLocationsApplicationsWorkloadsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsApplicationsWorkloadsListCall) Header ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsWorkloadsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsWorkloadsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsWorkloadsListCall) OrderBy ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) OrderBy(orderBy string) *ProjectsLocationsApplicationsWorkloadsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsApplicationsWorkloadsListCall) PageSize ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsWorkloadsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsApplicationsWorkloadsListCall) PageToken ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsWorkloadsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsApplicationsWorkloadsListCall) Pages ¶
func (c *ProjectsLocationsApplicationsWorkloadsListCall) Pages(ctx context.Context, f func(*ListWorkloadsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApplicationsWorkloadsPatchCall ¶
type ProjectsLocationsApplicationsWorkloadsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsWorkloadsPatchCall) Context ¶
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsWorkloadsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsWorkloadsPatchCall) Do ¶
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.applications.workloads.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsWorkloadsPatchCall) Fields ¶
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsWorkloadsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsWorkloadsPatchCall) Header ¶
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsWorkloadsPatchCall) RequestId ¶
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) RequestId(requestId string) *ProjectsLocationsApplicationsWorkloadsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsApplicationsWorkloadsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApplicationsWorkloadsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsWorkloadsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the Workload resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.

type ProjectsLocationsApplicationsWorkloadsService ¶
type ProjectsLocationsApplicationsWorkloadsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsWorkloadsService ¶
func NewProjectsLocationsApplicationsWorkloadsService(s *APIService) *ProjectsLocationsApplicationsWorkloadsService
func (*ProjectsLocationsApplicationsWorkloadsService) Create ¶
func (r *ProjectsLocationsApplicationsWorkloadsService) Create(parent string, workload *Workload) *ProjectsLocationsApplicationsWorkloadsCreateCall

Create: Creates a Workload in an Application.

parent: Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.
func (*ProjectsLocationsApplicationsWorkloadsService) Delete ¶
func (r *ProjectsLocationsApplicationsWorkloadsService) Delete(name string) *ProjectsLocationsApplicationsWorkloadsDeleteCall

Delete: Deletes a Workload from an Application.

name: Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloa ds/{workload}`.
func (*ProjectsLocationsApplicationsWorkloadsService) Get ¶
func (r *ProjectsLocationsApplicationsWorkloadsService) Get(name string) *ProjectsLocationsApplicationsWorkloadsGetCall

Get: Gets a Workload in an Application.

name: Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloa ds/{workload}`.
func (*ProjectsLocationsApplicationsWorkloadsService) List ¶
func (r *ProjectsLocationsApplicationsWorkloadsService) List(parent string) *ProjectsLocationsApplicationsWorkloadsListCall

List: Lists Workloads in an Application.

parent: Fully qualified name of the parent Application to list Workloads for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.
func (*ProjectsLocationsApplicationsWorkloadsService) Patch ¶
func (r *ProjectsLocationsApplicationsWorkloadsService) Patch(name string, workload *Workload) *ProjectsLocationsApplicationsWorkloadsPatchCall

Patch: Updates a Workload in an Application.

name: Identifier. The resource name of the Workload. Format: "projects/{host-project-id}/locations/{location}/applications/{application -id}/workloads/{workload-id}".
type ProjectsLocationsDetachServiceProjectAttachmentCall ¶
type ProjectsLocationsDetachServiceProjectAttachmentCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDetachServiceProjectAttachmentCall) Context ¶
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Context(ctx context.Context) *ProjectsLocationsDetachServiceProjectAttachmentCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDetachServiceProjectAttachmentCall) Do ¶
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Do(opts ...googleapi.CallOption) (*DetachServiceProjectAttachmentResponse, error)

Do executes the "apphub.projects.locations.detachServiceProjectAttachment" call. Any non-2xx status code is an error. Response headers are in either *DetachServiceProjectAttachmentResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDetachServiceProjectAttachmentCall) Fields ¶
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Fields(s ...googleapi.Field) *ProjectsLocationsDetachServiceProjectAttachmentCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDetachServiceProjectAttachmentCall) Header ¶
func (c *ProjectsLocationsDetachServiceProjectAttachmentCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDiscoveredServicesFindUnregisteredCall ¶
type ProjectsLocationsDiscoveredServicesFindUnregisteredCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Context ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Do ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Do(opts ...googleapi.CallOption) (*FindUnregisteredServicesResponse, error)

Do executes the "apphub.projects.locations.discoveredServices.findUnregistered" call. Any non-2xx status code is an error. Response headers are in either *FindUnregisteredServicesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Fields ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Filter ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Filter(filter string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Header ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) IfNoneMatch ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) OrderBy ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) PageSize ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) PageToken ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Pages ¶
func (c *ProjectsLocationsDiscoveredServicesFindUnregisteredCall) Pages(ctx context.Context, f func(*FindUnregisteredServicesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDiscoveredServicesGetCall ¶
type ProjectsLocationsDiscoveredServicesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredServicesGetCall) Context ¶
func (c *ProjectsLocationsDiscoveredServicesGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredServicesGetCall) Do ¶
func (c *ProjectsLocationsDiscoveredServicesGetCall) Do(opts ...googleapi.CallOption) (*DiscoveredService, error)

Do executes the "apphub.projects.locations.discoveredServices.get" call. Any non-2xx status code is an error. Response headers are in either *DiscoveredService.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredServicesGetCall) Fields ¶
func (c *ProjectsLocationsDiscoveredServicesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredServicesGetCall) Header ¶
func (c *ProjectsLocationsDiscoveredServicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredServicesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsDiscoveredServicesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDiscoveredServicesListCall ¶
type ProjectsLocationsDiscoveredServicesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredServicesListCall) Context ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredServicesListCall) Do ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) Do(opts ...googleapi.CallOption) (*ListDiscoveredServicesResponse, error)

Do executes the "apphub.projects.locations.discoveredServices.list" call. Any non-2xx status code is an error. Response headers are in either *ListDiscoveredServicesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredServicesListCall) Fields ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredServicesListCall) Filter ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) Filter(filter string) *ProjectsLocationsDiscoveredServicesListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsDiscoveredServicesListCall) Header ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredServicesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredServicesListCall) OrderBy ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredServicesListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsDiscoveredServicesListCall) PageSize ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredServicesListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsDiscoveredServicesListCall) PageToken ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredServicesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsDiscoveredServicesListCall) Pages ¶
func (c *ProjectsLocationsDiscoveredServicesListCall) Pages(ctx context.Context, f func(*ListDiscoveredServicesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDiscoveredServicesLookupCall ¶
added in v0.169.0
type ProjectsLocationsDiscoveredServicesLookupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredServicesLookupCall) Context ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredServicesLookupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredServicesLookupCall) Do ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Do(opts ...googleapi.CallOption) (*LookupDiscoveredServiceResponse, error)

Do executes the "apphub.projects.locations.discoveredServices.lookup" call. Any non-2xx status code is an error. Response headers are in either *LookupDiscoveredServiceResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredServicesLookupCall) Fields ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredServicesLookupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredServicesLookupCall) Header ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredServicesLookupCall) IfNoneMatch ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredServicesLookupCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredServicesLookupCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredServicesLookupCall) Uri ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredServicesLookupCall) Uri(uri string) *ProjectsLocationsDiscoveredServicesLookupCall

Uri sets the optional parameter "uri": Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.

type ProjectsLocationsDiscoveredServicesService ¶
type ProjectsLocationsDiscoveredServicesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDiscoveredServicesService ¶
func NewProjectsLocationsDiscoveredServicesService(s *APIService) *ProjectsLocationsDiscoveredServicesService
func (*ProjectsLocationsDiscoveredServicesService) FindUnregistered ¶
func (r *ProjectsLocationsDiscoveredServicesService) FindUnregistered(parent string) *ProjectsLocationsDiscoveredServicesFindUnregisteredCall

FindUnregistered: Finds unregistered services in a host project and location.

parent: Project and location to find unregistered Discovered Services on. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDiscoveredServicesService) Get ¶
func (r *ProjectsLocationsDiscoveredServicesService) Get(name string) *ProjectsLocationsDiscoveredServicesGetCall

Get: Gets a Discovered Service in a host project and location.

name: Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredServ ice}`.
func (*ProjectsLocationsDiscoveredServicesService) List ¶
func (r *ProjectsLocationsDiscoveredServicesService) List(parent string) *ProjectsLocationsDiscoveredServicesListCall

List: Lists Discovered Services that can be added to an Application in a host project and location.

parent: Project and location to list Discovered Services on. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDiscoveredServicesService) Lookup ¶
added in v0.169.0
func (r *ProjectsLocationsDiscoveredServicesService) Lookup(parent string) *ProjectsLocationsDiscoveredServicesLookupCall

Lookup: Lists a Discovered Service in a host project and location, with a given resource URI.

parent: Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.
type ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall ¶
type ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Context ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Do ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Do(opts ...googleapi.CallOption) (*FindUnregisteredWorkloadsResponse, error)

Do executes the "apphub.projects.locations.discoveredWorkloads.findUnregistered" call. Any non-2xx status code is an error. Response headers are in either *FindUnregisteredWorkloadsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Fields ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Filter ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Filter(filter string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Header ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) IfNoneMatch ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) OrderBy ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) PageSize ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) PageToken ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Pages ¶
func (c *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall) Pages(ctx context.Context, f func(*FindUnregisteredWorkloadsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDiscoveredWorkloadsGetCall ¶
type ProjectsLocationsDiscoveredWorkloadsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredWorkloadsGetCall) Context ¶
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredWorkloadsGetCall) Do ¶
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Do(opts ...googleapi.CallOption) (*DiscoveredWorkload, error)

Do executes the "apphub.projects.locations.discoveredWorkloads.get" call. Any non-2xx status code is an error. Response headers are in either *DiscoveredWorkload.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredWorkloadsGetCall) Fields ¶
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredWorkloadsGetCall) Header ¶
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredWorkloadsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsDiscoveredWorkloadsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDiscoveredWorkloadsListCall ¶
type ProjectsLocationsDiscoveredWorkloadsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredWorkloadsListCall) Context ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) Do ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Do(opts ...googleapi.CallOption) (*ListDiscoveredWorkloadsResponse, error)

Do executes the "apphub.projects.locations.discoveredWorkloads.list" call. Any non-2xx status code is an error. Response headers are in either *ListDiscoveredWorkloadsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) Fields ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) Filter ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Filter(filter string) *ProjectsLocationsDiscoveredWorkloadsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) Header ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) OrderBy ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) OrderBy(orderBy string) *ProjectsLocationsDiscoveredWorkloadsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) PageSize ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredWorkloadsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) PageToken ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredWorkloadsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsDiscoveredWorkloadsListCall) Pages ¶
func (c *ProjectsLocationsDiscoveredWorkloadsListCall) Pages(ctx context.Context, f func(*ListDiscoveredWorkloadsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDiscoveredWorkloadsLookupCall ¶
added in v0.169.0
type ProjectsLocationsDiscoveredWorkloadsLookupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredWorkloadsLookupCall) Context ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredWorkloadsLookupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredWorkloadsLookupCall) Do ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Do(opts ...googleapi.CallOption) (*LookupDiscoveredWorkloadResponse, error)

Do executes the "apphub.projects.locations.discoveredWorkloads.lookup" call. Any non-2xx status code is an error. Response headers are in either *LookupDiscoveredWorkloadResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredWorkloadsLookupCall) Fields ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredWorkloadsLookupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredWorkloadsLookupCall) Header ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredWorkloadsLookupCall) IfNoneMatch ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredWorkloadsLookupCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredWorkloadsLookupCall) Uri ¶
added in v0.169.0
func (c *ProjectsLocationsDiscoveredWorkloadsLookupCall) Uri(uri string) *ProjectsLocationsDiscoveredWorkloadsLookupCall

Uri sets the optional parameter "uri": Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.

type ProjectsLocationsDiscoveredWorkloadsService ¶
type ProjectsLocationsDiscoveredWorkloadsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDiscoveredWorkloadsService ¶
func NewProjectsLocationsDiscoveredWorkloadsService(s *APIService) *ProjectsLocationsDiscoveredWorkloadsService
func (*ProjectsLocationsDiscoveredWorkloadsService) FindUnregistered ¶
func (r *ProjectsLocationsDiscoveredWorkloadsService) FindUnregistered(parent string) *ProjectsLocationsDiscoveredWorkloadsFindUnregisteredCall

FindUnregistered: Finds unregistered workloads in a host project and location.

parent: Project and location to find unregistered Discovered Workloads on. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDiscoveredWorkloadsService) Get ¶
func (r *ProjectsLocationsDiscoveredWorkloadsService) Get(name string) *ProjectsLocationsDiscoveredWorkloadsGetCall

Get: Gets a Discovered Workload in a host project and location.

name: Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWor kload}`.
func (*ProjectsLocationsDiscoveredWorkloadsService) List ¶
func (r *ProjectsLocationsDiscoveredWorkloadsService) List(parent string) *ProjectsLocationsDiscoveredWorkloadsListCall

List: Lists Discovered Workloads that can be added to an Application in a host project and location.

parent: Project and location to list Discovered Workloads on. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDiscoveredWorkloadsService) Lookup ¶
added in v0.169.0
func (r *ProjectsLocationsDiscoveredWorkloadsService) Lookup(parent string) *ProjectsLocationsDiscoveredWorkloadsLookupCall

Lookup: Lists a Discovered Workload in a host project and location, with a given resource URI.

parent: Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.
type ProjectsLocationsExtendedMetadataSchemasGetCall ¶
added in v0.258.0
type ProjectsLocationsExtendedMetadataSchemasGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExtendedMetadataSchemasGetCall) Context ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Context(ctx context.Context) *ProjectsLocationsExtendedMetadataSchemasGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExtendedMetadataSchemasGetCall) Do ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Do(opts ...googleapi.CallOption) (*ExtendedMetadataSchema, error)

Do executes the "apphub.projects.locations.extendedMetadataSchemas.get" call. Any non-2xx status code is an error. Response headers are in either *ExtendedMetadataSchema.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExtendedMetadataSchemasGetCall) Fields ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsExtendedMetadataSchemasGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExtendedMetadataSchemasGetCall) Header ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsExtendedMetadataSchemasGetCall) IfNoneMatch ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsExtendedMetadataSchemasGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsExtendedMetadataSchemasListCall ¶
added in v0.258.0
type ProjectsLocationsExtendedMetadataSchemasListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExtendedMetadataSchemasListCall) Context ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Context(ctx context.Context) *ProjectsLocationsExtendedMetadataSchemasListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) Do ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Do(opts ...googleapi.CallOption) (*ListExtendedMetadataSchemasResponse, error)

Do executes the "apphub.projects.locations.extendedMetadataSchemas.list" call. Any non-2xx status code is an error. Response headers are in either *ListExtendedMetadataSchemasResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) Fields ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Fields(s ...googleapi.Field) *ProjectsLocationsExtendedMetadataSchemasListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) Header ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) IfNoneMatch ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) IfNoneMatch(entityTag string) *ProjectsLocationsExtendedMetadataSchemasListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) PageSize ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) PageSize(pageSize int64) *ProjectsLocationsExtendedMetadataSchemasListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) PageToken ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) PageToken(pageToken string) *ProjectsLocationsExtendedMetadataSchemasListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsExtendedMetadataSchemasListCall) Pages ¶
added in v0.258.0
func (c *ProjectsLocationsExtendedMetadataSchemasListCall) Pages(ctx context.Context, f func(*ListExtendedMetadataSchemasResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsExtendedMetadataSchemasService ¶
added in v0.258.0
type ProjectsLocationsExtendedMetadataSchemasService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsExtendedMetadataSchemasService ¶
added in v0.258.0
func NewProjectsLocationsExtendedMetadataSchemasService(s *APIService) *ProjectsLocationsExtendedMetadataSchemasService
func (*ProjectsLocationsExtendedMetadataSchemasService) Get ¶
added in v0.258.0
func (r *ProjectsLocationsExtendedMetadataSchemasService) Get(name string) *ProjectsLocationsExtendedMetadataSchemasGetCall

Get: Gets an Extended Metadata Schema.

name: Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_ metadata_schema}`. `{extended_metadata_schema}` has the format "apphub.googleapis.com/{SchemaName}".
func (*ProjectsLocationsExtendedMetadataSchemasService) List ¶
added in v0.258.0
func (r *ProjectsLocationsExtendedMetadataSchemasService) List(parent string) *ProjectsLocationsExtendedMetadataSchemasListCall

List: Lists Extended Metadata Schemas available in a host project and location.

parent: Project and location to list Extended Metadata Schemas on. Expected format: `projects/{project}/locations/{location}`.
type ProjectsLocationsGetBoundaryCall ¶
added in v0.257.0
type ProjectsLocationsGetBoundaryCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetBoundaryCall) Context ¶
added in v0.257.0
func (c *ProjectsLocationsGetBoundaryCall) Context(ctx context.Context) *ProjectsLocationsGetBoundaryCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetBoundaryCall) Do ¶
added in v0.257.0
func (c *ProjectsLocationsGetBoundaryCall) Do(opts ...googleapi.CallOption) (*Boundary, error)

Do executes the "apphub.projects.locations.getBoundary" call. Any non-2xx status code is an error. Response headers are in either *Boundary.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetBoundaryCall) Fields ¶
added in v0.257.0
func (c *ProjectsLocationsGetBoundaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetBoundaryCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetBoundaryCall) Header ¶
added in v0.257.0
func (c *ProjectsLocationsGetBoundaryCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetBoundaryCall) IfNoneMatch ¶
added in v0.257.0
func (c *ProjectsLocationsGetBoundaryCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetBoundaryCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "apphub.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall ¶
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "apphub.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
added in v0.230.0
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

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

type ProjectsLocationsLookupServiceProjectAttachmentCall ¶
type ProjectsLocationsLookupServiceProjectAttachmentCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsLookupServiceProjectAttachmentCall) Context ¶
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Context(ctx context.Context) *ProjectsLocationsLookupServiceProjectAttachmentCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsLookupServiceProjectAttachmentCall) Do ¶
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Do(opts ...googleapi.CallOption) (*LookupServiceProjectAttachmentResponse, error)

Do executes the "apphub.projects.locations.lookupServiceProjectAttachment" call. Any non-2xx status code is an error. Response headers are in either *LookupServiceProjectAttachmentResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsLookupServiceProjectAttachmentCall) Fields ¶
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Fields(s ...googleapi.Field) *ProjectsLocationsLookupServiceProjectAttachmentCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsLookupServiceProjectAttachmentCall) Header ¶
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsLookupServiceProjectAttachmentCall) IfNoneMatch ¶
func (c *ProjectsLocationsLookupServiceProjectAttachmentCall) IfNoneMatch(entityTag string) *ProjectsLocationsLookupServiceProjectAttachmentCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsCancelCall ¶
type ProjectsLocationsOperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsCancelCall) Context ¶
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsCancelCall) Do ¶
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apphub.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "apphub.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "apphub.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "apphub.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

func (*ProjectsLocationsOperationsListCall) ReturnPartialSuccess ¶
added in v0.253.0
func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type ProjectsLocationsOperationsService ¶
type ProjectsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOperationsService ¶
func NewProjectsLocationsOperationsService(s *APIService) *ProjectsLocationsOperationsService
func (*ProjectsLocationsOperationsService) Cancel ¶
func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

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

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	Applications *ProjectsLocationsApplicationsService

	DiscoveredServices *ProjectsLocationsDiscoveredServicesService

	DiscoveredWorkloads *ProjectsLocationsDiscoveredWorkloadsService

	ExtendedMetadataSchemas *ProjectsLocationsExtendedMetadataSchemasService

	Operations *ProjectsLocationsOperationsService

	ServiceProjectAttachments *ProjectsLocationsServiceProjectAttachmentsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
func NewProjectsLocationsService(s *APIService) *ProjectsLocationsService
func (*ProjectsLocationsService) DetachServiceProjectAttachment ¶
func (r *ProjectsLocationsService) DetachServiceProjectAttachment(name string, detachserviceprojectattachmentrequest *DetachServiceProjectAttachmentRequest) *ProjectsLocationsDetachServiceProjectAttachmentCall

DetachServiceProjectAttachment: Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

name: Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsService) Get ¶
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- name: Resource name for the location.

func (*ProjectsLocationsService) GetBoundary ¶
added in v0.257.0
func (r *ProjectsLocationsService) GetBoundary(name string) *ProjectsLocationsGetBoundaryCall

GetBoundary: Gets a Boundary.

name: The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.
func (*ProjectsLocationsService) List ¶
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

func (*ProjectsLocationsService) LookupServiceProjectAttachment ¶
func (r *ProjectsLocationsService) LookupServiceProjectAttachment(name string) *ProjectsLocationsLookupServiceProjectAttachmentCall

LookupServiceProjectAttachment: Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

name: Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsService) UpdateBoundary ¶
added in v0.257.0
func (r *ProjectsLocationsService) UpdateBoundary(name string, boundary *Boundary) *ProjectsLocationsUpdateBoundaryCall

UpdateBoundary: Updates a Boundary.

name: Identifier. The resource name of the boundary. Format: "projects/{project}/locations/{location}/boundary".
type ProjectsLocationsServiceProjectAttachmentsCreateCall ¶
type ProjectsLocationsServiceProjectAttachmentsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsServiceProjectAttachmentsCreateCall) Context ¶
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsServiceProjectAttachmentsCreateCall) Do ¶
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.serviceProjectAttachments.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsServiceProjectAttachmentsCreateCall) Fields ¶
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsServiceProjectAttachmentsCreateCall) Header ¶
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsServiceProjectAttachmentsCreateCall) RequestId ¶
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) RequestId(requestId string) *ProjectsLocationsServiceProjectAttachmentsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsServiceProjectAttachmentsCreateCall) ServiceProjectAttachmentId ¶
func (c *ProjectsLocationsServiceProjectAttachmentsCreateCall) ServiceProjectAttachmentId(serviceProjectAttachmentId string) *ProjectsLocationsServiceProjectAttachmentsCreateCall

ServiceProjectAttachmentId sets the optional parameter "serviceProjectAttachmentId": Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.

type ProjectsLocationsServiceProjectAttachmentsDeleteCall ¶
type ProjectsLocationsServiceProjectAttachmentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsServiceProjectAttachmentsDeleteCall) Context ¶
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsServiceProjectAttachmentsDeleteCall) Do ¶
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.serviceProjectAttachments.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsServiceProjectAttachmentsDeleteCall) Fields ¶
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsServiceProjectAttachmentsDeleteCall) Header ¶
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsServiceProjectAttachmentsDeleteCall) RequestId ¶
func (c *ProjectsLocationsServiceProjectAttachmentsDeleteCall) RequestId(requestId string) *ProjectsLocationsServiceProjectAttachmentsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsServiceProjectAttachmentsGetCall ¶
type ProjectsLocationsServiceProjectAttachmentsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsServiceProjectAttachmentsGetCall) Context ¶
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsServiceProjectAttachmentsGetCall) Do ¶
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Do(opts ...googleapi.CallOption) (*ServiceProjectAttachment, error)

Do executes the "apphub.projects.locations.serviceProjectAttachments.get" call. Any non-2xx status code is an error. Response headers are in either *ServiceProjectAttachment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsServiceProjectAttachmentsGetCall) Fields ¶
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsServiceProjectAttachmentsGetCall) Header ¶
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsServiceProjectAttachmentsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsServiceProjectAttachmentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsServiceProjectAttachmentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsServiceProjectAttachmentsListCall ¶
type ProjectsLocationsServiceProjectAttachmentsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsServiceProjectAttachmentsListCall) Context ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Context(ctx context.Context) *ProjectsLocationsServiceProjectAttachmentsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) Do ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Do(opts ...googleapi.CallOption) (*ListServiceProjectAttachmentsResponse, error)

Do executes the "apphub.projects.locations.serviceProjectAttachments.list" call. Any non-2xx status code is an error. Response headers are in either *ListServiceProjectAttachmentsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) Fields ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceProjectAttachmentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) Filter ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Filter(filter string) *ProjectsLocationsServiceProjectAttachmentsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) Header ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsServiceProjectAttachmentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) OrderBy ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) OrderBy(orderBy string) *ProjectsLocationsServiceProjectAttachmentsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) PageSize ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) PageSize(pageSize int64) *ProjectsLocationsServiceProjectAttachmentsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) PageToken ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) PageToken(pageToken string) *ProjectsLocationsServiceProjectAttachmentsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsServiceProjectAttachmentsListCall) Pages ¶
func (c *ProjectsLocationsServiceProjectAttachmentsListCall) Pages(ctx context.Context, f func(*ListServiceProjectAttachmentsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsServiceProjectAttachmentsService ¶
type ProjectsLocationsServiceProjectAttachmentsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsServiceProjectAttachmentsService ¶
func NewProjectsLocationsServiceProjectAttachmentsService(s *APIService) *ProjectsLocationsServiceProjectAttachmentsService
func (*ProjectsLocationsServiceProjectAttachmentsService) Create ¶
func (r *ProjectsLocationsServiceProjectAttachmentsService) Create(parent string, serviceprojectattachment *ServiceProjectAttachment) *ProjectsLocationsServiceProjectAttachmentsCreateCall

Create: Attaches a service project to the host project.

parent: Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsServiceProjectAttachmentsService) Delete ¶
func (r *ProjectsLocationsServiceProjectAttachmentsService) Delete(name string) *ProjectsLocationsServiceProjectAttachmentsDeleteCall

Delete: Deletes a service project attachment.

name: Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{service ProjectAttachment}`.
func (*ProjectsLocationsServiceProjectAttachmentsService) Get ¶
func (r *ProjectsLocationsServiceProjectAttachmentsService) Get(name string) *ProjectsLocationsServiceProjectAttachmentsGetCall

Get: Gets a service project attachment.

name: Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{service ProjectAttachment}`.
func (*ProjectsLocationsServiceProjectAttachmentsService) List ¶
func (r *ProjectsLocationsServiceProjectAttachmentsService) List(parent string) *ProjectsLocationsServiceProjectAttachmentsListCall

List: Lists service projects attached to the host project.

parent: Host project ID and location to list service project attachments. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.
type ProjectsLocationsUpdateBoundaryCall ¶
added in v0.257.0
type ProjectsLocationsUpdateBoundaryCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsUpdateBoundaryCall) Context ¶
added in v0.257.0
func (c *ProjectsLocationsUpdateBoundaryCall) Context(ctx context.Context) *ProjectsLocationsUpdateBoundaryCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsUpdateBoundaryCall) Do ¶
added in v0.257.0
func (c *ProjectsLocationsUpdateBoundaryCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "apphub.projects.locations.updateBoundary" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsUpdateBoundaryCall) Fields ¶
added in v0.257.0
func (c *ProjectsLocationsUpdateBoundaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsUpdateBoundaryCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsUpdateBoundaryCall) Header ¶
added in v0.257.0
func (c *ProjectsLocationsUpdateBoundaryCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsUpdateBoundaryCall) RequestId ¶
added in v0.257.0
func (c *ProjectsLocationsUpdateBoundaryCall) RequestId(requestId string) *ProjectsLocationsUpdateBoundaryCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsUpdateBoundaryCall) UpdateMask ¶
added in v0.257.0
func (c *ProjectsLocationsUpdateBoundaryCall) UpdateMask(updateMask string) *ProjectsLocationsUpdateBoundaryCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the Boundary resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

type ProjectsService ¶
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *APIService) *ProjectsService
type RegistrationType ¶
added in v0.257.0
type RegistrationType struct {
	// Type: Output only. The registration type of a service.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified registration type. Defaults to EXCLUSIVE.
	//   "EXCLUSIVE" - The service can only be registered to one application.
	//   "SHARED" - The service can be registered to multiple applications.
	Type string `json:"type,omitempty"`
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

RegistrationType: The registration type of a service.

func (RegistrationType) MarshalJSON ¶
added in v0.257.0
func (s RegistrationType) MarshalJSON() ([]byte, error)
type Scope ¶
type Scope struct {
	// Type: Required. Scope Type.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified type.
	//   "REGIONAL" - Regional type.
	//   "GLOBAL" - Global type.
	Type string `json:"type,omitempty"`
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

Scope: Scope of an application.

func (Scope) MarshalJSON ¶
func (s Scope) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	// Attributes: Optional. Consumer provided attributes.
	Attributes *Attributes `json:"attributes,omitempty"`
	// CreateTime: Output only. Create time.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. User-defined description of a Service. Can have a
	// maximum length of 2048 characters.
	Description string `json:"description,omitempty"`
	// DiscoveredService: Required. Immutable. The resource name of the original
	// discovered service.
	DiscoveredService string `json:"discoveredService,omitempty"`
	// DisplayName: Optional. User-defined name for the Service. Can have a maximum
	// length of 63 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Identifier. The resource name of a Service. Format:
	// "projects/{host-project-id}/locations/{location}/applications/{application-i
	// d}/services/{service-id}"
	Name string `json:"name,omitempty"`
	// ServiceProperties: Output only. Properties of an underlying compute resource
	// that can comprise a Service. These are immutable.
	ServiceProperties *ServiceProperties `json:"serviceProperties,omitempty"`
	// ServiceReference: Output only. Reference to an underlying networking
	// resource that can comprise a Service. These are immutable.
	ServiceReference *ServiceReference `json:"serviceReference,omitempty"`
	// State: Output only. Service state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified state.
	//   "CREATING" - The service is being created.
	//   "ACTIVE" - The service is ready.
	//   "DELETING" - The service is being deleted.
	//   "DETACHED" - The underlying networking resources have been deleted.
	State string `json:"state,omitempty"`
	// Uid: Output only. A universally unique identifier (UUID) for the `Service`
	// in the UUID4 format.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Update time.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Service: Service is an App Hub data model that contains a discovered service, which represents a network or API interface that exposes some functionality to clients for consumption over the network.

func (Service) MarshalJSON ¶
func (s Service) MarshalJSON() ([]byte, error)
type ServiceProjectAttachment ¶
type ServiceProjectAttachment struct {
	// CreateTime: Output only. Create time.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Identifier. The resource name of a ServiceProjectAttachment. Format:
	// "projects/{host-project-id}/locations/global/serviceProjectAttachments/{serv
	// ice-project-id}."
	Name string `json:"name,omitempty"`
	// ServiceProject: Required. Immutable. Service project name in the format:
	// "projects/abc" or "projects/123". As input, project name with either
	// project id or number are accepted. As output, this field will contain
	// project number.
	ServiceProject string `json:"serviceProject,omitempty"`
	// State: Output only. ServiceProjectAttachment state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified state.
	//   "CREATING" - The ServiceProjectAttachment is being created.
	//   "ACTIVE" - The ServiceProjectAttachment is ready. This means Services and
	// Workloads under the corresponding ServiceProjectAttachment is ready for
	// registration.
	//   "DELETING" - The ServiceProjectAttachment is being deleted.
	State string `json:"state,omitempty"`
	// Uid: Output only. A globally unique identifier (in UUID4 format) for the
	// `ServiceProjectAttachment`.
	Uid string `json:"uid,omitempty"`

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

ServiceProjectAttachment: ServiceProjectAttachment represents an attachment from a service project to a host project. Service projects contain the underlying cloud infrastructure resources, and expose these resources to the host project through a ServiceProjectAttachment. With the attachments, the host project can provide an aggregated view of resources across all service projects.

func (ServiceProjectAttachment) MarshalJSON ¶
func (s ServiceProjectAttachment) MarshalJSON() ([]byte, error)
type ServiceProperties ¶
type ServiceProperties struct {
	// ExtendedMetadata: Output only. Additional metadata specific to the resource
	// type. The key is a string that identifies the type of metadata and the value
	// is the metadata contents specific to that type. Key format:
	// `apphub.googleapis.com/{metadataType}`
	ExtendedMetadata map[string]ExtendedMetadata `json:"extendedMetadata,omitempty"`
	// FunctionalType: Output only. The type of the service.
	FunctionalType *FunctionalType `json:"functionalType,omitempty"`
	// GcpProject: Output only. The service project identifier that the underlying
	// cloud resource resides in.
	GcpProject string `json:"gcpProject,omitempty"`
	// Identity: Output only. The identity associated with the service.
	Identity *Identity `json:"identity,omitempty"`
	// Location: Output only. The location that the underlying resource resides in,
	// for example, us-west1.
	Location string `json:"location,omitempty"`
	// RegistrationType: Output only. The registration type of the service.
	RegistrationType *RegistrationType `json:"registrationType,omitempty"`
	// Zone: Output only. The location that the underlying resource resides in if
	// it is zonal, for example, us-west1-a).
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExtendedMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExtendedMetadata") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServiceProperties: Properties of an underlying cloud resource that can comprise a Service.

func (ServiceProperties) MarshalJSON ¶
func (s ServiceProperties) MarshalJSON() ([]byte, error)
type ServiceReference ¶
type ServiceReference struct {
	// Path: Output only. Additional path under the resource URI (demultiplexing
	// one resource URI into multiple entries). Smallest unit a policy can be
	// attached to. Examples: URL Map path entry.
	Path string `json:"path,omitempty"`
	// Uri: Output only. The underlying resource URI. For example, URI of
	// Forwarding Rule, URL Map, and Backend Service.
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Path") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Path") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServiceReference: Reference to an underlying networking resource that can comprise a Service.

func (ServiceReference) MarshalJSON ¶
func (s ServiceReference) MarshalJSON() ([]byte, error)
type SetIamPolicyRequest ¶
type SetIamPolicyRequest struct {
	// Policy: REQUIRED: The complete policy to be applied to the `resource`. The
	// size of the policy is limited to a few 10s of KB. An empty policy is a valid
	// policy but certain Google Cloud services (such as Projects) might reject
	// them.
	Policy *Policy `json:"policy,omitempty"`
	// UpdateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
	// modify. Only the fields in the mask will be modified. If no mask is
	// provided, the following default mask is used: `paths: "bindings, etag"
	UpdateMask string `json:"updateMask,omitempty"`
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
type Workload ¶
type Workload struct {
	// Attributes: Optional. Consumer provided attributes.
	Attributes *Attributes `json:"attributes,omitempty"`
	// CreateTime: Output only. Create time.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. User-defined description of a Workload. Can have a
	// maximum length of 2048 characters.
	Description string `json:"description,omitempty"`
	// DiscoveredWorkload: Required. Immutable. The resource name of the original
	// discovered workload.
	DiscoveredWorkload string `json:"discoveredWorkload,omitempty"`
	// DisplayName: Optional. User-defined name for the Workload. Can have a
	// maximum length of 63 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Identifier. The resource name of the Workload. Format:
	// "projects/{host-project-id}/locations/{location}/applications/{application-i
	// d}/workloads/{workload-id}"
	Name string `json:"name,omitempty"`
	// State: Output only. Workload state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified state.
	//   "CREATING" - The Workload is being created.
	//   "ACTIVE" - The Workload is ready.
	//   "DELETING" - The Workload is being deleted.
	//   "DETACHED" - The underlying compute resources have been deleted.
	State string `json:"state,omitempty"`
	// Uid: Output only. A universally unique identifier (UUID) for the `Workload`
	// in the UUID4 format.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Update time.
	UpdateTime string `json:"updateTime,omitempty"`
	// WorkloadProperties: Output only. Properties of an underlying compute
	// resource represented by the Workload. These are immutable.
	WorkloadProperties *WorkloadProperties `json:"workloadProperties,omitempty"`
	// WorkloadReference: Output only. Reference of an underlying compute resource
	// represented by the Workload. These are immutable.
	WorkloadReference *WorkloadReference `json:"workloadReference,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Workload: Workload is an App Hub data model that contains a discovered workload, which represents a binary deployment (such as managed instance groups (MIGs) and GKE deployments) that performs the smallest logical subset of business functionality.

func (Workload) MarshalJSON ¶
func (s Workload) MarshalJSON() ([]byte, error)
type WorkloadProperties ¶
type WorkloadProperties struct {
	// ExtendedMetadata: Output only. Additional metadata specific to the resource
	// type. The key is a string that identifies the type of metadata and the value
	// is the metadata contents specific to that type. Key format:
	// `apphub.googleapis.com/{metadataType}`
	ExtendedMetadata map[string]ExtendedMetadata `json:"extendedMetadata,omitempty"`
	// FunctionalType: Output only. The type of the workload.
	FunctionalType *FunctionalType `json:"functionalType,omitempty"`
	// GcpProject: Output only. The service project identifier that the underlying
	// cloud resource resides in. Empty for non-cloud resources.
	GcpProject string `json:"gcpProject,omitempty"`
	// Identity: Output only. The identity associated with the workload.
	Identity *Identity `json:"identity,omitempty"`
	// Location: Output only. The location that the underlying compute resource
	// resides in (for example, us-west1).
	Location string `json:"location,omitempty"`
	// Zone: Output only. The location that the underlying compute resource resides
	// in if it is zonal (for example, us-west1-a).
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExtendedMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExtendedMetadata") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WorkloadProperties: Properties of an underlying compute resource represented by the Workload.

func (WorkloadProperties) MarshalJSON ¶
func (s WorkloadProperties) MarshalJSON() ([]byte, error)
type WorkloadReference ¶
type WorkloadReference struct {
	// Uri: Output only. The underlying compute resource uri.
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

WorkloadReference: Reference of an underlying compute resource represented by the Workload.

func (WorkloadReference) MarshalJSON ¶
func (s WorkloadReference) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
apphub-gen.go
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

# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1

Title: advisorynotifications package - google.golang.org/api/advisorynotifications/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1

Markdown Content:
Package advisorynotifications provides access to the Advisory Notifications API.

For product documentation, see: [https://cloud.google.com/advisory-notifications](https://cloud.google.com/advisory-notifications)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/advisorynotifications/v1"
...
ctx := context.Background()
advisorynotificationsService, err := advisorynotifications.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

advisorynotificationsService, err := advisorynotifications.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
advisorynotificationsService, err := advisorynotifications.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#pkg-constants)
*   [type GoogleCloudAdvisorynotificationsV1Attachment](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Attachment)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Attachment) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Attachment.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1Csv](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Csv)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Csv) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Csv.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1CsvCsvRow](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1CsvCsvRow)
*       *   [func (s GoogleCloudAdvisorynotificationsV1CsvCsvRow) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1CsvCsvRow.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1ListNotificationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1ListNotificationsResponse)
*       *   [func (s GoogleCloudAdvisorynotificationsV1ListNotificationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1ListNotificationsResponse.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1Message](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Message)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Message) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Message.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1MessageBody](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1MessageBody)
*       *   [func (s GoogleCloudAdvisorynotificationsV1MessageBody) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1MessageBody.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1Notification](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Notification)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Notification) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Notification.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1NotificationSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1NotificationSettings)
*       *   [func (s GoogleCloudAdvisorynotificationsV1NotificationSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1NotificationSettings.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1Settings](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Settings)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Settings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Settings.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1Subject](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Subject)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Subject) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Subject.MarshalJSON)

*   [type GoogleCloudAdvisorynotificationsV1Text](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Text)
*       *   [func (s GoogleCloudAdvisorynotificationsV1Text) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Text.MarshalJSON)

*   [type OrganizationsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsGetSettingsCall)
*       *   [func (c *OrganizationsLocationsGetSettingsCall) Context(ctx context.Context) *OrganizationsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsGetSettingsCall.Context)
    *   [func (c *OrganizationsLocationsGetSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1Settings, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsGetSettingsCall.Do)
    *   [func (c *OrganizationsLocationsGetSettingsCall) Fields(s ...googleapi.Field) *OrganizationsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsGetSettingsCall.Fields)
    *   [func (c *OrganizationsLocationsGetSettingsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsGetSettingsCall.Header)
    *   [func (c *OrganizationsLocationsGetSettingsCall) IfNoneMatch(entityTag string) *OrganizationsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsGetSettingsCall.IfNoneMatch)

*   [type OrganizationsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall)
*       *   [func (c *OrganizationsLocationsNotificationsGetCall) Context(ctx context.Context) *OrganizationsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall.Context)
    *   [func (c *OrganizationsLocationsNotificationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1Notification, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall.Do)
    *   [func (c *OrganizationsLocationsNotificationsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall.Fields)
    *   [func (c *OrganizationsLocationsNotificationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall.Header)
    *   [func (c *OrganizationsLocationsNotificationsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall.IfNoneMatch)
    *   [func (c *OrganizationsLocationsNotificationsGetCall) LanguageCode(languageCode string) *OrganizationsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsGetCall.LanguageCode)

*   [type OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall)
*       *   [func (c *OrganizationsLocationsNotificationsListCall) Context(ctx context.Context) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.Context)
    *   [func (c *OrganizationsLocationsNotificationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1ListNotificationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.Do)
    *   [func (c *OrganizationsLocationsNotificationsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.Fields)
    *   [func (c *OrganizationsLocationsNotificationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.Header)
    *   [func (c *OrganizationsLocationsNotificationsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.IfNoneMatch)
    *   [func (c *OrganizationsLocationsNotificationsListCall) LanguageCode(languageCode string) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.LanguageCode)
    *   [func (c *OrganizationsLocationsNotificationsListCall) PageSize(pageSize int64) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.PageSize)
    *   [func (c *OrganizationsLocationsNotificationsListCall) PageToken(pageToken string) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.PageToken)
    *   [func (c *OrganizationsLocationsNotificationsListCall) Pages(ctx context.Context, ...) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.Pages)
    *   [func (c *OrganizationsLocationsNotificationsListCall) View(view string) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsListCall.View)

*   [type OrganizationsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsService)
*       *   [func NewOrganizationsLocationsNotificationsService(s *Service) *OrganizationsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewOrganizationsLocationsNotificationsService)

*       *   [func (r *OrganizationsLocationsNotificationsService) Get(name string) *OrganizationsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsService.Get)
    *   [func (r *OrganizationsLocationsNotificationsService) List(parent string) *OrganizationsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsService.List)

*   [type OrganizationsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsService)
*       *   [func NewOrganizationsLocationsService(s *Service) *OrganizationsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewOrganizationsLocationsService)

*       *   [func (r *OrganizationsLocationsService) GetSettings(name string) *OrganizationsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsService.GetSettings)
    *   [func (r *OrganizationsLocationsService) UpdateSettings(name string, ...) *OrganizationsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsService.UpdateSettings)

*   [type OrganizationsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsUpdateSettingsCall)
*       *   [func (c *OrganizationsLocationsUpdateSettingsCall) Context(ctx context.Context) *OrganizationsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsUpdateSettingsCall.Context)
    *   [func (c *OrganizationsLocationsUpdateSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1Settings, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsUpdateSettingsCall.Do)
    *   [func (c *OrganizationsLocationsUpdateSettingsCall) Fields(s ...googleapi.Field) *OrganizationsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsUpdateSettingsCall.Fields)
    *   [func (c *OrganizationsLocationsUpdateSettingsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsUpdateSettingsCall.Header)

*   [type OrganizationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsService)
*       *   [func NewOrganizationsService(s *Service) *OrganizationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewOrganizationsService)

*   [type ProjectsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsGetSettingsCall)
*       *   [func (c *ProjectsLocationsGetSettingsCall) Context(ctx context.Context) *ProjectsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsGetSettingsCall.Context)
    *   [func (c *ProjectsLocationsGetSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1Settings, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsGetSettingsCall.Do)
    *   [func (c *ProjectsLocationsGetSettingsCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsGetSettingsCall.Fields)
    *   [func (c *ProjectsLocationsGetSettingsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsGetSettingsCall.Header)
    *   [func (c *ProjectsLocationsGetSettingsCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsGetSettingsCall.IfNoneMatch)

*   [type ProjectsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall)
*       *   [func (c *ProjectsLocationsNotificationsGetCall) Context(ctx context.Context) *ProjectsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall.Context)
    *   [func (c *ProjectsLocationsNotificationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1Notification, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall.Do)
    *   [func (c *ProjectsLocationsNotificationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall.Fields)
    *   [func (c *ProjectsLocationsNotificationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall.Header)
    *   [func (c *ProjectsLocationsNotificationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsNotificationsGetCall) LanguageCode(languageCode string) *ProjectsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsGetCall.LanguageCode)

*   [type ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall)
*       *   [func (c *ProjectsLocationsNotificationsListCall) Context(ctx context.Context) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.Context)
    *   [func (c *ProjectsLocationsNotificationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1ListNotificationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.Do)
    *   [func (c *ProjectsLocationsNotificationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.Fields)
    *   [func (c *ProjectsLocationsNotificationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.Header)
    *   [func (c *ProjectsLocationsNotificationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsNotificationsListCall) LanguageCode(languageCode string) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.LanguageCode)
    *   [func (c *ProjectsLocationsNotificationsListCall) PageSize(pageSize int64) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.PageSize)
    *   [func (c *ProjectsLocationsNotificationsListCall) PageToken(pageToken string) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.PageToken)
    *   [func (c *ProjectsLocationsNotificationsListCall) Pages(ctx context.Context, ...) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.Pages)
    *   [func (c *ProjectsLocationsNotificationsListCall) View(view string) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsListCall.View)

*   [type ProjectsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsService)
*       *   [func NewProjectsLocationsNotificationsService(s *Service) *ProjectsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewProjectsLocationsNotificationsService)

*       *   [func (r *ProjectsLocationsNotificationsService) Get(name string) *ProjectsLocationsNotificationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsService.Get)
    *   [func (r *ProjectsLocationsNotificationsService) List(parent string) *ProjectsLocationsNotificationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsService.List)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *Service) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewProjectsLocationsService)

*       *   [func (r *ProjectsLocationsService) GetSettings(name string) *ProjectsLocationsGetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsService.GetSettings)
    *   [func (r *ProjectsLocationsService) UpdateSettings(name string, ...) *ProjectsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsService.UpdateSettings)

*   [type ProjectsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsUpdateSettingsCall)
*       *   [func (c *ProjectsLocationsUpdateSettingsCall) Context(ctx context.Context) *ProjectsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsUpdateSettingsCall.Context)
    *   [func (c *ProjectsLocationsUpdateSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudAdvisorynotificationsV1Settings, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsUpdateSettingsCall.Do)
    *   [func (c *ProjectsLocationsUpdateSettingsCall) Fields(s ...googleapi.Field) *ProjectsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsUpdateSettingsCall.Fields)
    *   [func (c *ProjectsLocationsUpdateSettingsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsUpdateSettingsCall.Header)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsService)
*       *   [func NewProjectsService(s *Service) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewProjectsService)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#NewService)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/advisorynotifications/v1/advisorynotifications-gen.go#L100)

const (
	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type GoogleCloudAdvisorynotificationsV1Attachment struct {
	Csv *[GoogleCloudAdvisorynotificationsV1Csv](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Csv) `json:"csv,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Attachment: Attachment with specific information about the issue.

type GoogleCloudAdvisorynotificationsV1Csv struct {
	
	DataRows []*[GoogleCloudAdvisorynotificationsV1CsvCsvRow](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1CsvCsvRow) `json:"dataRows,omitempty"`
	Headers [][string](https://pkg.go.dev/builtin#string) `json:"headers,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Csv: A representation of a CSV file attachment, as a list of column headers and a list of data rows.

type GoogleCloudAdvisorynotificationsV1CsvCsvRow struct {
	
	Entries [][string](https://pkg.go.dev/builtin#string) `json:"entries,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1CsvCsvRow: A representation of a single data row in a CSV file.

type GoogleCloudAdvisorynotificationsV1ListNotificationsResponse struct {
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	Notifications []*[GoogleCloudAdvisorynotificationsV1Notification](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Notification) `json:"notifications,omitempty"`
	TotalSize [int64](https://pkg.go.dev/builtin#int64) `json:"totalSize,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1ListNotificationsResponse: Response of ListNotifications endpoint.

type GoogleCloudAdvisorynotificationsV1Message struct {
	Attachments []*[GoogleCloudAdvisorynotificationsV1Attachment](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Attachment) `json:"attachments,omitempty"`
	Body *[GoogleCloudAdvisorynotificationsV1MessageBody](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1MessageBody) `json:"body,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	LocalizationTime [string](https://pkg.go.dev/builtin#string) `json:"localizationTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Message: A message which contains notification details.

type GoogleCloudAdvisorynotificationsV1Notification struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	Messages []*[GoogleCloudAdvisorynotificationsV1Message](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Message) `json:"messages,omitempty"`
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	
	NotificationType [string](https://pkg.go.dev/builtin#string) `json:"notificationType,omitempty"`
	Subject *[GoogleCloudAdvisorynotificationsV1Subject](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Subject) `json:"subject,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Notification: A notification object for notifying customers about security and privacy issues.

type GoogleCloudAdvisorynotificationsV1NotificationSettings struct {
	Enabled [bool](https://pkg.go.dev/builtin#bool) `json:"enabled,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1NotificationSettings: Settings for each NotificationType.

type GoogleCloudAdvisorynotificationsV1Settings struct {
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	NotificationSettings map[[string](https://pkg.go.dev/builtin#string)][GoogleCloudAdvisorynotificationsV1NotificationSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1NotificationSettings) `json:"notificationSettings,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Settings: Settings for Advisory Notifications.

type GoogleCloudAdvisorynotificationsV1Subject struct {
	Text *[GoogleCloudAdvisorynotificationsV1Text](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Text) `json:"text,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Subject: A subject line of a notification.

type GoogleCloudAdvisorynotificationsV1Text struct {
	EnText [string](https://pkg.go.dev/builtin#string) `json:"enText,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	LocalizationState [string](https://pkg.go.dev/builtin#string) `json:"localizationState,omitempty"`
	LocalizedText [string](https://pkg.go.dev/builtin#string) `json:"localizedText,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleCloudAdvisorynotificationsV1Text: A text object containing the English text and its localized copies.

type OrganizationsLocationsGetSettingsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.organizations.locations.getSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1Settings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OrganizationsLocationsNotificationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.organizations.locations.notifications.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1Notification.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": ISO code for requested localization language. If unset, will be interpereted as "en". If the requested language is valid, but not supported for this notification, English will be returned with an "Not applicable" LocalizationState. If the ISO code is invalid (i.e. not a real language), this RPC will throw an error.

type OrganizationsLocationsNotificationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.organizations.locations.notifications.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1ListNotificationsResponse.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": ISO code for requested localization language. If unset, will be interpereted as "en". If the requested language is valid, but not supported for this notification, English will be returned with an "Not applicable" LocalizationState. If the ISO code is invalid (i.e. not a real language), this RPC will throw an error.

PageSize sets the optional parameter "pageSize": The maximum number of notifications to return. The service may return fewer than this value. If unspecified or equal to 0, at most 50 notifications will be returned. The maximum value is 50; values above 50 will be coerced to 50.

PageToken sets the optional parameter "pageToken": A page token returned from a previous request. When paginating, all other parameters provided in the request must match the call that returned the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

View sets the optional parameter "view": Specifies which parts of the notification resource should be returned in the response.

Possible values:

"NOTIFICATION_VIEW_UNSPECIFIED" - Not specified, equivalent to BASIC.
"BASIC" - Server responses only include title, creation time and

Notification ID. Note: for internal use responses also include the last update time, the latest message text and whether notification has attachments.

"FULL" - Include everything.

type OrganizationsLocationsNotificationsService struct {
	
}

func NewOrganizationsLocationsNotificationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)) *[OrganizationsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsService)

Get: Gets a notification.

*   name: A name of the notification to retrieve. Format: organizations/{organization}/locations/{location}/notifications/{notificati on} or projects/{projects}/locations/{location}/notifications/{notification}.

List: Lists notifications under a given parent.

*   parent: The parent, which owns this collection of notifications. Must be of the form "organizations/{organization}/locations/{location}" or "projects/{project}/locations/{location}".

type OrganizationsLocationsService struct {
 Notifications *[OrganizationsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsNotificationsService)	
}

func NewOrganizationsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)) *[OrganizationsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsService)

GetSettings: Get notification settings.

*   name: The resource name of the settings to retrieve. Format: organizations/{organization}/locations/{location}/settings or projects/{projects}/locations/{location}/settings.

func (r *[OrganizationsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsService)) UpdateSettings(name [string](https://pkg.go.dev/builtin#string), googlecloudadvisorynotificationsv1settings *[GoogleCloudAdvisorynotificationsV1Settings](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Settings)) *[OrganizationsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsUpdateSettingsCall)

UpdateSettings: Update notification settings.

*   name: Identifier. The resource name of the settings to retrieve. Format: organizations/{organization}/locations/{location}/settings or projects/{projects}/locations/{location}/settings.

type OrganizationsLocationsUpdateSettingsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.organizations.locations.updateSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1Settings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrganizationsService struct {
 Locations *[OrganizationsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsLocationsService)	
}

func NewOrganizationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)) *[OrganizationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsService)

type ProjectsLocationsGetSettingsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.projects.locations.getSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1Settings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsNotificationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.projects.locations.notifications.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1Notification.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": ISO code for requested localization language. If unset, will be interpereted as "en". If the requested language is valid, but not supported for this notification, English will be returned with an "Not applicable" LocalizationState. If the ISO code is invalid (i.e. not a real language), this RPC will throw an error.

type ProjectsLocationsNotificationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.projects.locations.notifications.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1ListNotificationsResponse.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": ISO code for requested localization language. If unset, will be interpereted as "en". If the requested language is valid, but not supported for this notification, English will be returned with an "Not applicable" LocalizationState. If the ISO code is invalid (i.e. not a real language), this RPC will throw an error.

PageSize sets the optional parameter "pageSize": The maximum number of notifications to return. The service may return fewer than this value. If unspecified or equal to 0, at most 50 notifications will be returned. The maximum value is 50; values above 50 will be coerced to 50.

PageToken sets the optional parameter "pageToken": A page token returned from a previous request. When paginating, all other parameters provided in the request must match the call that returned the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

View sets the optional parameter "view": Specifies which parts of the notification resource should be returned in the response.

Possible values:

"NOTIFICATION_VIEW_UNSPECIFIED" - Not specified, equivalent to BASIC.
"BASIC" - Server responses only include title, creation time and

Notification ID. Note: for internal use responses also include the last update time, the latest message text and whether notification has attachments.

"FULL" - Include everything.

type ProjectsLocationsNotificationsService struct {
	
}

func NewProjectsLocationsNotificationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)) *[ProjectsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsService)

Get: Gets a notification.

*   name: A name of the notification to retrieve. Format: organizations/{organization}/locations/{location}/notifications/{notificati on} or projects/{projects}/locations/{location}/notifications/{notification}.

List: Lists notifications under a given parent.

*   parent: The parent, which owns this collection of notifications. Must be of the form "organizations/{organization}/locations/{location}" or "projects/{project}/locations/{location}".

type ProjectsLocationsService struct {
 Notifications *[ProjectsLocationsNotificationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsNotificationsService)	
}

func NewProjectsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsService)

GetSettings: Get notification settings.

*   name: The resource name of the settings to retrieve. Format: organizations/{organization}/locations/{location}/settings or projects/{projects}/locations/{location}/settings.

func (r *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsService)) UpdateSettings(name [string](https://pkg.go.dev/builtin#string), googlecloudadvisorynotificationsv1settings *[GoogleCloudAdvisorynotificationsV1Settings](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#GoogleCloudAdvisorynotificationsV1Settings)) *[ProjectsLocationsUpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsUpdateSettingsCall)

UpdateSettings: Update notification settings.

*   name: Identifier. The resource name of the settings to retrieve. Format: organizations/{organization}/locations/{location}/settings or projects/{projects}/locations/{location}/settings.

type ProjectsLocationsUpdateSettingsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "advisorynotifications.projects.locations.updateSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudAdvisorynotificationsV1Settings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsService struct {
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsLocationsService)	
}

func NewProjectsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#Service)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsService)

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Organizations *[OrganizationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#OrganizationsService)
 Projects *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/advisorynotifications/v1#ProjectsService)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

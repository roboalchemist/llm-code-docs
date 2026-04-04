# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1

Title: admin package - google.golang.org/api/admin/reports/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1

Markdown Content:
Package admin provides access to the Admin SDK API.

For product documentation, see: [https://developers.google.com/workspace/admin/](https://developers.google.com/workspace/admin/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/admin/reports/v1"
...
ctx := context.Background()
adminService, err := admin.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use [google.golang.org/api/option.WithScopes](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithScopes):

adminService, err := admin.NewService(ctx, option.WithScopes(admin.AdminReportsUsageReadonlyScope))

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

adminService, err := admin.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adminService, err := admin.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#pkg-constants)
*   [type Activities](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Activities)
*       *   [func (s Activities) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Activities.MarshalJSON)

*   [type ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)
*       *   [func (c *ActivitiesListCall) ActorIpAddress(actorIpAddress string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.ActorIpAddress)
    *   [func (c *ActivitiesListCall) ApplicationInfoFilter(applicationInfoFilter string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.ApplicationInfoFilter)
    *   [func (c *ActivitiesListCall) Context(ctx context.Context) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.Context)
    *   [func (c *ActivitiesListCall) CustomerId(customerId string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.CustomerId)
    *   [func (c *ActivitiesListCall) Do(opts ...googleapi.CallOption) (*Activities, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.Do)
    *   [func (c *ActivitiesListCall) EndTime(endTime string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.EndTime)
    *   [func (c *ActivitiesListCall) EventName(eventName string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.EventName)
    *   [func (c *ActivitiesListCall) Fields(s ...googleapi.Field) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.Fields)
    *   [func (c *ActivitiesListCall) Filters(filters string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.Filters)
    *   [func (c *ActivitiesListCall) GroupIdFilter(groupIdFilter string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.GroupIdFilter)
    *   [func (c *ActivitiesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.Header)
    *   [func (c *ActivitiesListCall) IfNoneMatch(entityTag string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.IfNoneMatch)
    *   [func (c *ActivitiesListCall) MaxResults(maxResults int64) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.MaxResults)
    *   [func (c *ActivitiesListCall) NetworkInfoFilter(networkInfoFilter string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.NetworkInfoFilter)
    *   [func (c *ActivitiesListCall) OrgUnitID(orgUnitID string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.OrgUnitID)
    *   [func (c *ActivitiesListCall) PageToken(pageToken string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.PageToken)
    *   [func (c *ActivitiesListCall) Pages(ctx context.Context, f func(*Activities) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.Pages)
    *   [func (c *ActivitiesListCall) ResourceDetailsFilter(resourceDetailsFilter string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.ResourceDetailsFilter)
    *   [func (c *ActivitiesListCall) StartTime(startTime string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.StartTime)
    *   [func (c *ActivitiesListCall) StatusFilter(statusFilter string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall.StatusFilter)

*   [type ActivitiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesService)
*       *   [func NewActivitiesService(s *Service) *ActivitiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NewActivitiesService)

*       *   [func (r *ActivitiesService) List(userKey string, applicationName string) *ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesService.List)
    *   [func (r *ActivitiesService) Watch(userKey string, applicationName string, channel *Channel) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesService.Watch)

*   [type ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall)
*       *   [func (c *ActivitiesWatchCall) ActorIpAddress(actorIpAddress string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.ActorIpAddress)
    *   [func (c *ActivitiesWatchCall) Context(ctx context.Context) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.Context)
    *   [func (c *ActivitiesWatchCall) CustomerId(customerId string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.CustomerId)
    *   [func (c *ActivitiesWatchCall) Do(opts ...googleapi.CallOption) (*Channel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.Do)
    *   [func (c *ActivitiesWatchCall) EndTime(endTime string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.EndTime)
    *   [func (c *ActivitiesWatchCall) EventName(eventName string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.EventName)
    *   [func (c *ActivitiesWatchCall) Fields(s ...googleapi.Field) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.Fields)
    *   [func (c *ActivitiesWatchCall) Filters(filters string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.Filters)
    *   [func (c *ActivitiesWatchCall) GroupIdFilter(groupIdFilter string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.GroupIdFilter)
    *   [func (c *ActivitiesWatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.Header)
    *   [func (c *ActivitiesWatchCall) MaxResults(maxResults int64) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.MaxResults)
    *   [func (c *ActivitiesWatchCall) OrgUnitID(orgUnitID string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.OrgUnitID)
    *   [func (c *ActivitiesWatchCall) PageToken(pageToken string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.PageToken)
    *   [func (c *ActivitiesWatchCall) StartTime(startTime string) *ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall.StartTime)

*   [type Activity](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Activity)
*       *   [func (s Activity) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Activity.MarshalJSON)

*   [type ActivityActor](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityActor)
*       *   [func (s ActivityActor) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityActor.MarshalJSON)

*   [type ActivityActorApplicationInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityActorApplicationInfo)
*       *   [func (s ActivityActorApplicationInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityActorApplicationInfo.MarshalJSON)

*   [type ActivityEvents](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEvents)
*       *   [func (s ActivityEvents) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEvents.MarshalJSON)

*   [type ActivityEventsParameters](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParameters)
*       *   [func (s ActivityEventsParameters) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParameters.MarshalJSON)

*   [type ActivityEventsParametersMessageValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParametersMessageValue)
*       *   [func (s ActivityEventsParametersMessageValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParametersMessageValue.MarshalJSON)

*   [type ActivityEventsParametersMultiMessageValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParametersMultiMessageValue)
*       *   [func (s ActivityEventsParametersMultiMessageValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParametersMultiMessageValue.MarshalJSON)

*   [type ActivityEventsStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsStatus)
*       *   [func (s ActivityEventsStatus) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsStatus.MarshalJSON)

*   [type ActivityId](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityId)
*       *   [func (s ActivityId) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityId.MarshalJSON)

*   [type ActivityNetworkInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityNetworkInfo)
*       *   [func (s ActivityNetworkInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityNetworkInfo.MarshalJSON)

*   [type AppliedLabel](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#AppliedLabel)
*       *   [func (s AppliedLabel) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#AppliedLabel.MarshalJSON)

*   [type Channel](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Channel)
*       *   [func (s Channel) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Channel.MarshalJSON)

*   [type ChannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsService)
*       *   [func NewChannelsService(s *Service) *ChannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NewChannelsService)

*       *   [func (r *ChannelsService) Stop(channel *Channel) *ChannelsStopCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsService.Stop)

*   [type ChannelsStopCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsStopCall)
*       *   [func (c *ChannelsStopCall) Context(ctx context.Context) *ChannelsStopCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsStopCall.Context)
    *   [func (c *ChannelsStopCall) Do(opts ...googleapi.CallOption) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsStopCall.Do)
    *   [func (c *ChannelsStopCall) Fields(s ...googleapi.Field) *ChannelsStopCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsStopCall.Fields)
    *   [func (c *ChannelsStopCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsStopCall.Header)

*   [type CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall)
*       *   [func (c *CustomerUsageReportsGetCall) Context(ctx context.Context) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.Context)
    *   [func (c *CustomerUsageReportsGetCall) CustomerId(customerId string) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.CustomerId)
    *   [func (c *CustomerUsageReportsGetCall) Do(opts ...googleapi.CallOption) (*UsageReports, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.Do)
    *   [func (c *CustomerUsageReportsGetCall) Fields(s ...googleapi.Field) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.Fields)
    *   [func (c *CustomerUsageReportsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.Header)
    *   [func (c *CustomerUsageReportsGetCall) IfNoneMatch(entityTag string) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.IfNoneMatch)
    *   [func (c *CustomerUsageReportsGetCall) PageToken(pageToken string) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.PageToken)
    *   [func (c *CustomerUsageReportsGetCall) Pages(ctx context.Context, f func(*UsageReports) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.Pages)
    *   [func (c *CustomerUsageReportsGetCall) Parameters(parameters string) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsGetCall.Parameters)

*   [type CustomerUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsService)
*       *   [func NewCustomerUsageReportsService(s *Service) *CustomerUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NewCustomerUsageReportsService)

*       *   [func (r *CustomerUsageReportsService) Get(date string) *CustomerUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsService.Get)

*   [type Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Date)
*       *   [func (s Date) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Date.MarshalJSON)

*   [type EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall)
*       *   [func (c *EntityUsageReportsGetCall) Context(ctx context.Context) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Context)
    *   [func (c *EntityUsageReportsGetCall) CustomerId(customerId string) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.CustomerId)
    *   [func (c *EntityUsageReportsGetCall) Do(opts ...googleapi.CallOption) (*UsageReports, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Do)
    *   [func (c *EntityUsageReportsGetCall) Fields(s ...googleapi.Field) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Fields)
    *   [func (c *EntityUsageReportsGetCall) Filters(filters string) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Filters)
    *   [func (c *EntityUsageReportsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Header)
    *   [func (c *EntityUsageReportsGetCall) IfNoneMatch(entityTag string) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.IfNoneMatch)
    *   [func (c *EntityUsageReportsGetCall) MaxResults(maxResults int64) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.MaxResults)
    *   [func (c *EntityUsageReportsGetCall) PageToken(pageToken string) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.PageToken)
    *   [func (c *EntityUsageReportsGetCall) Pages(ctx context.Context, f func(*UsageReports) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Pages)
    *   [func (c *EntityUsageReportsGetCall) Parameters(parameters string) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsGetCall.Parameters)

*   [type EntityUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsService)
*       *   [func NewEntityUsageReportsService(s *Service) *EntityUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NewEntityUsageReportsService)

*       *   [func (r *EntityUsageReportsService) Get(entityType string, entityKey string, date string) *EntityUsageReportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsService.Get)

*   [type FieldValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValue)
*       *   [func (s FieldValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValue.MarshalJSON)

*   [type FieldValueSelectionListValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionListValue)
*       *   [func (s FieldValueSelectionListValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionListValue.MarshalJSON)

*   [type FieldValueSelectionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionValue)
*       *   [func (s FieldValueSelectionValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionValue.MarshalJSON)

*   [type FieldValueTextListValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueTextListValue)
*       *   [func (s FieldValueTextListValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueTextListValue.MarshalJSON)

*   [type FieldValueUserListValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserListValue)
*       *   [func (s FieldValueUserListValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserListValue.MarshalJSON)

*   [type FieldValueUserValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserValue)
*       *   [func (s FieldValueUserValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserValue.MarshalJSON)

*   [type NestedParameter](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NestedParameter)
*       *   [func (s NestedParameter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NestedParameter.MarshalJSON)

*   [type Reason](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Reason)
*       *   [func (s Reason) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Reason.MarshalJSON)

*   [type ResourceDetails](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ResourceDetails)
*       *   [func (s ResourceDetails) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ResourceDetails.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NewService)

*   [type UsageReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReport)
*       *   [func (s UsageReport) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReport.MarshalJSON)

*   [type UsageReportEntity](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportEntity)
*       *   [func (s UsageReportEntity) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportEntity.MarshalJSON)

*   [type UsageReportParameters](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportParameters)
*       *   [func (s UsageReportParameters) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportParameters.MarshalJSON)

*   [type UsageReports](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReports)
*       *   [func (s UsageReports) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReports.MarshalJSON)

*   [type UsageReportsWarnings](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportsWarnings)
*       *   [func (s UsageReportsWarnings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportsWarnings.MarshalJSON)

*   [type UsageReportsWarningsData](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportsWarningsData)
*       *   [func (s UsageReportsWarningsData) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportsWarningsData.MarshalJSON)

*   [type UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall)
*       *   [func (c *UserUsageReportGetCall) Context(ctx context.Context) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Context)
    *   [func (c *UserUsageReportGetCall) CustomerId(customerId string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.CustomerId)
    *   [func (c *UserUsageReportGetCall) Do(opts ...googleapi.CallOption) (*UsageReports, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Do)
    *   [func (c *UserUsageReportGetCall) Fields(s ...googleapi.Field) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Fields)
    *   [func (c *UserUsageReportGetCall) Filters(filters string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Filters)
    *   [func (c *UserUsageReportGetCall) GroupIdFilter(groupIdFilter string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.GroupIdFilter)
    *   [func (c *UserUsageReportGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Header)
    *   [func (c *UserUsageReportGetCall) IfNoneMatch(entityTag string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.IfNoneMatch)
    *   [func (c *UserUsageReportGetCall) MaxResults(maxResults int64) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.MaxResults)
    *   [func (c *UserUsageReportGetCall) OrgUnitID(orgUnitID string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.OrgUnitID)
    *   [func (c *UserUsageReportGetCall) PageToken(pageToken string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.PageToken)
    *   [func (c *UserUsageReportGetCall) Pages(ctx context.Context, f func(*UsageReports) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Pages)
    *   [func (c *UserUsageReportGetCall) Parameters(parameters string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportGetCall.Parameters)

*   [type UserUsageReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportService)
*       *   [func NewUserUsageReportService(s *Service) *UserUsageReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NewUserUsageReportService)

*       *   [func (r *UserUsageReportService) Get(userKey string, date string) *UserUsageReportGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportService.Get)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/admin/reports/v1/admin-gen.go#L105)

const (
	AdminReportsAuditReadonlyScope = "https://www.googleapis.com/auth/admin.reports.audit.readonly"

	AdminReportsUsageReadonlyScope = "https://www.googleapis.com/auth/admin.reports.usage.readonly"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type Activities struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	Items []*[Activity](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Activity) `json:"items,omitempty"`
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Activities: JSON template for a collection of activities.

type ActivitiesListCall struct {
	
}

func (c *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)) ActorIpAddress(actorIpAddress [string](https://pkg.go.dev/builtin#string)) *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)

ActorIpAddress sets the optional parameter "actorIpAddress": The Internet Protocol (IP) Address of host where the event was performed. This is an additional way to filter a report's summary using the IP address of the user whose activity is being reported. This IP address may or may not reflect the user's physical location. For example, the IP address can be the user's proxy server's address or a virtual private network (VPN) address. This parameter supports both IPv4 and IPv6 address versions.

func (c *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)) ApplicationInfoFilter(applicationInfoFilter [string](https://pkg.go.dev/builtin#string)) *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)

ApplicationInfoFilter sets the optional parameter "applicationInfoFilter": Used to filter on the `oAuthClientId` field present in `ApplicationInfo` (#applicationinfo) message. **Usage** ``` GET...&applicationInfoFilter=oAuthClientId="clientId" GET...&applicationInfoFilter=oAuthClientId=%22clientId%22 ```

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique ID of the customer to retrieve data for.

Do executes the "reports.activities.list" call. Any non-2xx status code is an error. Response headers are in either *Activities.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

EndTime sets the optional parameter "endTime": Sets the end of the range of time shown in the report. The date is in the [RFC 3339](https://rfc-editor.org/rfc/rfc3339.html) format, for example 2010-10-28T10:26:35.000Z. The default value is the approximate time of the API request. An API report has three basic time concepts: - *Date of the API's request for a report*: When the API created and retrieved the report. - *Report's start time*: The beginning of the timespan shown in the report. The `startTime` must be before the `endTime` (if specified) and the current time when the request is made, or the API returns an error. - *Report's end time*: The end of the timespan shown in the report. For example, the timespan of events summarized in a report can start in April and end in May. The report itself can be requested in August. If the `endTime` is not specified, the report returns all activities from the `startTime` until the current time or the most recent 180 days if the `startTime` is more than 180 days in the past. For Gmail requests, `startTime` and `endTime` must be provided and the difference must not be greater than 30 days.

EventName sets the optional parameter "eventName": The name of the event being queried by the API. Each `eventName` is related to a specific Google Workspace service or feature which the API organizes into types of events. An example is the Google Calendar events in the Admin console application's reports. The Calendar Settings `type` structure has all of the Calendar `eventName` activities reported by the API. When an administrator changes a Calendar setting, the API reports this activity in the Calendar Settings `type` and `eventName` parameters. For more information about `eventName` query strings and parameters, see the list of event names for various applications above in `applicationName`.

Filters sets the optional parameter "filters": The `filters` query string is a comma-separated list composed of event parameters manipulated by relational operators. Event parameters are in the form `{parameter1 name}{relational operator}{parameter1 value},{parameter2 name}{relational operator}{parameter2 value},...` These event parameters are associated with a specific `eventName`. An empty report is returned if the request's parameter doesn't belong to the `eventName`. For more information about the available `eventName` fields for each application and their associated parameters, go to the ApplicationName (#applicationname) table, then click through to the Activity Events page in the Appendix for the application you want. In the following Drive activity examples, the returned list consists of all `edit` events where the `doc_id` parameter value matches the conditions defined by the relational operator. In the first example, the request returns all edited documents with a `doc_id` value equal to `12345`. In the second example, the report returns any edited documents where the `doc_id` value is not equal to `98765`. The `<>` operator is URL-encoded in the request's query string (`%3C%3E`): ``` GET...&eventName=edit&filters=doc_id==12345 GET...&eventName=edit&filters=doc_id%3C%3E98765 ``` A `filters` query supports these relational operators: * `==`—'equal to'. * `<>`—'not equal to'. Must be URL-encoded (%3C%3E). * `<`—'less than'. Must be URL-encoded (%3C). * `<=`—'less than or equal to'. Must be URL-encoded (%3C=). * `>`—'greater than'. Must be URL-encoded (%3E). * `>=`—'greater than or equal to'. Must be URL-encoded (%3E=). **Note:** The API doesn't accept multiple values of the same parameter. If a parameter is supplied more than once in the API request, the API only accepts the last value of that parameter. In addition, if an invalid parameter is supplied in the API request, the API ignores that parameter and returns the response corresponding to the remaining valid parameters. If no parameters are requested, all parameters are returned.

func (c *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)) GroupIdFilter(groupIdFilter [string](https://pkg.go.dev/builtin#string)) *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)

GroupIdFilter sets the optional parameter "groupIdFilter": Comma separated group ids (obfuscated) on which user activities are filtered, i.e. the response will contain activities for only those users that are a part of at least one of the group ids mentioned here. Format: "id:abc123,id:xyz456" *Important:* To filter by groups, you must explicitly add the groups to your filtering groups allowlist. For more information about adding groups to filtering groups allowlist, see Filter results by Google Group ([https://support.google.com/a/answer/11482175](https://support.google.com/a/answer/11482175))

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

MaxResults sets the optional parameter "maxResults": Determines how many activity records are shown on each response page. For example, if the request sets `maxResults=1` and the report has two activities, the report has two pages. The response's `nextPageToken` property has the token to the second page. The `maxResults` query string is optional in the request. The default value is 1000.

func (c *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)) NetworkInfoFilter(networkInfoFilter [string](https://pkg.go.dev/builtin#string)) *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)

NetworkInfoFilter sets the optional parameter "networkInfoFilter": Used to filter on the `regionCode` field present in `NetworkInfo` (#networkinfo) message. **Usage** ``` GET...&networkInfoFilter=regionCode="IN" GET...&networkInfoFilter=regionCode=%22IN%22 ```

OrgUnitID sets the optional parameter "orgUnitID": ID of the organizational unit to report on. Activity records will be shown only for users who belong to the specified organizational unit. Data before Dec 17, 2018 doesn't appear in the filtered results.

PageToken sets the optional parameter "pageToken": The token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. In your follow-on request getting the next page of the report, enter the `nextPageToken` value in the `pageToken` query string.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (c *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)) ResourceDetailsFilter(resourceDetailsFilter [string](https://pkg.go.dev/builtin#string)) *[ActivitiesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesListCall)

ResourceDetailsFilter sets the optional parameter "resourceDetailsFilter": The `resourceDetailsFilter` query string is an AND separated list composed of Resource Details (#resourcedetails) fields manipulated by relational operators. Resource Details Filters are in the form `{resourceDetails.field1}{relational operator}{field1 value} AND {resourceDetails.field2}{relational operator}{field2 value}...` All the inner fields are traversed using the `.` operator, as shown in the following example: ``` resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id = "appliedLabelId" AND resourceDetails.appliedLabels.fieldValue.id = "fieldValueId" ``` `resourceDetailsFilter` query supports these relational operators: * `=`—'equal to'. * `!=`—'not equal to'. * `:`—'exists'. This is used for filtering on repeated fields. `FieldValue` (#fieldvalue) types that are repeated in nature uses `exists` operator for filtering. The following `FieldValue` (#fieldvalue) types are repeated: * `TextListValue` (#textlistvalue) * `SelectionListValue` (#selectionlistvalue) * `UserListValue` (#userlistvalue) For example, in the following filter, `SelectionListValue` (#selectionlistvalue), is a repeated field. The filter checks whether `SelectionListValue` (#selectionlistvalue) contains `selection_id`: ``` resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id = "appliedLabelId" AND resourceDetails.appliedLabels.fieldValue.id = "fieldValueId" AND resourceDetails.appliedLabels.fieldValue.type = "SELECTION_LIST_VALUE" AND resourceDetails.appliedLabels.fieldValue.selectionListValue.id: "id" ``` **Usage** ``` GET...&resourceDetailsFilter=resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id = "appliedLabelId" GET...&resourceDetailsFilter=resourceDetails.id=%22resourceId%22%20AND%20reso urceDetails.appliedLabels.id=%22appliedLabelId%22 ``` **Note the following**: * You must URL encode the query string before sending the request. * The API supports a maximum of 5 fields separated by the AND operator. - When filtering on deeper levels (e.g., `AppliedLabel` (#appliedlabel), `FieldValue` (#fieldvalue)), the IDs of all preceding levels in the hierarchy must be included in the filter. For example: Filtering on `FieldValue` (#fieldvalue) requires `AppliedLabel` (#appliedlabel) ID and resourceDetails ID to be present. *Sample Query*: ``` resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id = "appliedLabelId" AND resourceDetails.appliedLabels.fieldValue.id = "fieldValueId" ``` * Filtering on inner `FieldValue` (#fieldvalue) types like `longTextValue` and `textValue` requires `resourceDetails.appliedLabels.fieldValue.type` to be present. * Only Filtering on a single `AppliedLabel` (#appliedlabel) id and `FieldValue` (#fieldvalue) id is supported.

StartTime sets the optional parameter "startTime": Sets the beginning of the range of time shown in the report. The date is in the [RFC 3339](https://rfc-editor.org/rfc/rfc3339.html) format, for example 2010-10-28T10:26:35.000Z. The report returns all activities from `startTime` until `endTime`. The `startTime` must be before the `endTime` (if specified) and the current time when the request is made, or the API returns an error. For Gmail requests, `startTime` and `endTime` must be provided and the difference must not be greater than 30 days.

StatusFilter sets the optional parameter "statusFilter": Used to filter on the `statusCode` field present in `Status` (#status) message. **Usage** ``` GET...&statusFilter=statusCode="200" GET...&statusFilter=statusCode=%22200%22 ```

type ActivitiesService struct {
	
}

func NewActivitiesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Service)) *[ActivitiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesService)

List: Retrieves a list of activities for a specific customer's account and application such as the Admin console application or the Google Drive application. For more information, see the guides for administrator and Google Drive activity reports. For more information about the activity report's parameters, see the activity parameters reference guides.

*   applicationName: Application name for which the events are to be retrieved.
*   userKey: Represents the profile ID or the user email for which the data should be filtered. Can be `all` for all information, or `userKey` for a user's unique Google Workspace profile ID or their primary email address. Must not be a deleted user. For a deleted user, call `users.list` in Directory API with `showDeleted=true`, then use the returned `ID` as the `userKey`.

Watch: Start receiving notifications for account activities. For more information, see Receiving Push Notifications.

*   applicationName: Application name for which the events are to be retrieved.
*   userKey: Represents the profile ID or the user email for which the data should be filtered. Can be `all` for all information, or `userKey` for a user's unique Google Workspace profile ID or their primary email address. Must not be a deleted user. For a deleted user, call `users.list` in Directory API with `showDeleted=true`, then use the returned `ID` as the `userKey`.

type ActivitiesWatchCall struct {
	
}

func (c *[ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall)) ActorIpAddress(actorIpAddress [string](https://pkg.go.dev/builtin#string)) *[ActivitiesWatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesWatchCall)

ActorIpAddress sets the optional parameter "actorIpAddress": The Internet Protocol (IP) Address of host where the event was performed. This is an additional way to filter a report's summary using the IP address of the user whose activity is being reported. This IP address may or may not reflect the user's physical location. For example, the IP address can be the user's proxy server's address or a virtual private network (VPN) address. This parameter supports both IPv4 and IPv6 address versions.

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique ID of the customer to retrieve data for.

Do executes the "reports.activities.watch" call. Any non-2xx status code is an error. Response headers are in either *Channel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

EndTime sets the optional parameter "endTime": Sets the end of the range of time shown in the report. The date is in the [RFC 3339](https://rfc-editor.org/rfc/rfc3339.html) format, for example 2010-10-28T10:26:35.000Z. The default value is the approximate time of the API request. An API report has three basic time concepts: - *Date of the API's request for a report*: When the API created and retrieved the report. - *Report's start time*: The beginning of the timespan shown in the report. The `startTime` must be before the `endTime` (if specified) and the current time when the request is made, or the API returns an error. - *Report's end time*: The end of the timespan shown in the report. For example, the timespan of events summarized in a report can start in April and end in May. The report itself can be requested in August. If the `endTime` is not specified, the report returns all activities from the `startTime` until the current time or the most recent 180 days if the `startTime` is more than 180 days in the past.

EventName sets the optional parameter "eventName": The name of the event being queried by the API. Each `eventName` is related to a specific Google Workspace service or feature which the API organizes into types of events. An example is the Google Calendar events in the Admin console application's reports. The Calendar Settings `type` structure has all of the Calendar `eventName` activities reported by the API. When an administrator changes a Calendar setting, the API reports this activity in the Calendar Settings `type` and `eventName` parameters. For more information about `eventName` query strings and parameters, see the list of event names for various applications above in `applicationName`.

Filters sets the optional parameter "filters": The `filters` query string is a comma-separated list composed of event parameters manipulated by relational operators. Event parameters are in the form `{parameter1 name}{relational operator}{parameter1 value},{parameter2 name}{relational operator}{parameter2 value},...` These event parameters are associated with a specific `eventName`. An empty report is returned if the request's parameter doesn't belong to the `eventName`. For more information about the available `eventName` fields for each application and their associated parameters, go to the ApplicationName (#applicationname) table, then click through to the Activity Events page in the Appendix for the application you want. In the following Drive activity examples, the returned list consists of all `edit` events where the `doc_id` parameter value matches the conditions defined by the relational operator. In the first example, the request returns all edited documents with a `doc_id` value equal to `12345`. In the second example, the report returns any edited documents where the `doc_id` value is not equal to `98765`. The `<>` operator is URL-encoded in the request's query string (`%3C%3E`): ``` GET...&eventName=edit&filters=doc_id==12345 GET...&eventName=edit&filters=doc_id%3C%3E98765 ``` A `filters` query supports these relational operators: * `==`—'equal to'. * `<>`—'not equal to'. Must be URL-encoded (%3C%3E). * `<`—'less than'. Must be URL-encoded (%3C). * `<=`—'less than or equal to'. Must be URL-encoded (%3C=). * `>`—'greater than'. Must be URL-encoded (%3E). * `>=`—'greater than or equal to'. Must be URL-encoded (%3E=). **Note:** The API doesn't accept multiple values of the same parameter. If a parameter is supplied more than once in the API request, the API only accepts the last value of that parameter. In addition, if an invalid parameter is supplied in the API request, the API ignores that parameter and returns the response corresponding to the remaining valid parameters. If no parameters are requested, all parameters are returned.

GroupIdFilter sets the optional parameter "groupIdFilter": `Deprecated`. This field is deprecated and is no longer supported. Comma separated group ids (obfuscated) on which user activities are filtered, i.e. the response will contain activities for only those users that are a part of at least one of the group ids mentioned here. Format: "id:abc123,id:xyz456" *Important:* To filter by groups, you must explicitly add the groups to your filtering groups allowlist. For more information about adding groups to filtering groups allowlist, see Filter results by Google Group ([https://support.google.com/a/answer/11482175](https://support.google.com/a/answer/11482175))

Header returns a http.Header that can be modified by the caller to add headers to the request.

MaxResults sets the optional parameter "maxResults": Determines how many activity records are shown on each response page. For example, if the request sets `maxResults=1` and the report has two activities, the report has two pages. The response's `nextPageToken` property has the token to the second page. The `maxResults` query string is optional in the request. The default value is 1000.

OrgUnitID sets the optional parameter "orgUnitID": `Deprecated`. This field is deprecated and is no longer supported. ID of the organizational unit to report on. Activity records will be shown only for users who belong to the specified organizational unit. Data before Dec 17, 2018 doesn't appear in the filtered results.

PageToken sets the optional parameter "pageToken": The token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. In your follow-on request getting the next page of the report, enter the `nextPageToken` value in the `pageToken` query string.

StartTime sets the optional parameter "startTime": Sets the beginning of the range of time shown in the report. The date is in the [RFC 3339](https://rfc-editor.org/rfc/rfc3339.html) format, for example 2010-10-28T10:26:35.000Z. The report returns all activities from `startTime` until `endTime`. The `startTime` must be before the `endTime` (if specified) and the current time when the request is made, or the API returns an error.

type Activity struct {
	Actor *[ActivityActor](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityActor) `json:"actor,omitempty"`
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	Events []*[ActivityEvents](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEvents) `json:"events,omitempty"`
	Id *[ActivityId](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityId) `json:"id,omitempty"`
	
	
	
	
	IpAddress [string](https://pkg.go.dev/builtin#string) `json:"ipAddress,omitempty"`
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	NetworkInfo *[ActivityNetworkInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityNetworkInfo) `json:"networkInfo,omitempty"`
	
	OwnerDomain [string](https://pkg.go.dev/builtin#string) `json:"ownerDomain,omitempty"`
	ResourceDetails []*[ResourceDetails](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ResourceDetails) `json:"resourceDetails,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Activity: JSON template for the activity resource.

type ActivityActor struct {
	
	ApplicationInfo *[ActivityActorApplicationInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityActorApplicationInfo) `json:"applicationInfo,omitempty"`
	CallerType [string](https://pkg.go.dev/builtin#string) `json:"callerType,omitempty"`
	
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	Key [string](https://pkg.go.dev/builtin#string) `json:"key,omitempty"`
	
	
	ProfileId [string](https://pkg.go.dev/builtin#string) `json:"profileId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityActor: User doing the action.

type ActivityActorApplicationInfo struct {
	ApplicationName [string](https://pkg.go.dev/builtin#string) `json:"applicationName,omitempty"`
	Impersonation [bool](https://pkg.go.dev/builtin#bool) `json:"impersonation,omitempty"`
	
	OauthClientId [string](https://pkg.go.dev/builtin#string) `json:"oauthClientId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityActorApplicationInfo: Details of the application that was the actor for the activity.

type ActivityEvents struct {
	
	
	
	
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	Parameters []*[ActivityEventsParameters](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParameters) `json:"parameters,omitempty"`
	ResourceIds [][string](https://pkg.go.dev/builtin#string) `json:"resourceIds,omitempty"`
	Status *[ActivityEventsStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsStatus) `json:"status,omitempty"`
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type ActivityEventsParameters struct {
	BoolValue [bool](https://pkg.go.dev/builtin#bool) `json:"boolValue,omitempty"`
	IntValue [int64](https://pkg.go.dev/builtin#int64) `json:"intValue,omitempty,string"`
	
	
	
	MessageValue *[ActivityEventsParametersMessageValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParametersMessageValue) `json:"messageValue,omitempty"`
	MultiIntValue [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"multiIntValue,omitempty"`
	MultiMessageValue []*[ActivityEventsParametersMultiMessageValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivityEventsParametersMultiMessageValue) `json:"multiMessageValue,omitempty"`
	MultiValue [][string](https://pkg.go.dev/builtin#string) `json:"multiValue,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type ActivityEventsParametersMessageValue struct {
	Parameter []*[NestedParameter](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NestedParameter) `json:"parameter,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityEventsParametersMessageValue: Nested parameter value pairs associated with this parameter. Complex value type for a parameter are returned as a list of parameter values. For example, the address parameter may have a value as `[{parameter: [{name: city, value: abc}]}]`

type ActivityEventsParametersMultiMessageValue struct {
	Parameter []*[NestedParameter](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#NestedParameter) `json:"parameter,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type ActivityEventsStatus struct {
	ErrorCode [string](https://pkg.go.dev/builtin#string) `json:"errorCode,omitempty"`
	ErrorMessage [string](https://pkg.go.dev/builtin#string) `json:"errorMessage,omitempty"`
	
	
	EventStatus [string](https://pkg.go.dev/builtin#string) `json:"eventStatus,omitempty"`
	HttpStatusCode [int64](https://pkg.go.dev/builtin#int64) `json:"httpStatusCode,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityEventsStatus: Status of the event. Note: Not all events have status.

type ActivityId struct {
	
	ApplicationName [string](https://pkg.go.dev/builtin#string) `json:"applicationName,omitempty"`
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	Time [string](https://pkg.go.dev/builtin#string) `json:"time,omitempty"`
	UniqueQualifier [int64](https://pkg.go.dev/builtin#int64) `json:"uniqueQualifier,omitempty,string"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityId: Unique identifier for each activity record.

type ActivityNetworkInfo struct {
	IpAsn [][int64](https://pkg.go.dev/builtin#int64) `json:"ipAsn,omitempty"`
	RegionCode [string](https://pkg.go.dev/builtin#string) `json:"regionCode,omitempty"`
	
	SubdivisionCode [string](https://pkg.go.dev/builtin#string) `json:"subdivisionCode,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityNetworkInfo: Network information of the user doing the action.

type AppliedLabel struct {
	
	
	FieldValues []*[FieldValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValue) `json:"fieldValues,omitempty"`
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	Reason *[Reason](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Reason) `json:"reason,omitempty"`
	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AppliedLabel: Details of the label applied on the resource.

type Channel struct {
	Address [string](https://pkg.go.dev/builtin#string) `json:"address,omitempty"`
	
	Expiration [int64](https://pkg.go.dev/builtin#int64) `json:"expiration,omitempty,string"`
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	
	Params map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"params,omitempty"`
	
	
	Payload [bool](https://pkg.go.dev/builtin#bool) `json:"payload,omitempty"`
	
	ResourceId [string](https://pkg.go.dev/builtin#string) `json:"resourceId,omitempty"`
	ResourceUri [string](https://pkg.go.dev/builtin#string) `json:"resourceUri,omitempty"`
	
	Token [string](https://pkg.go.dev/builtin#string) `json:"token,omitempty"`
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Channel: A notification channel used to watch for resource changes.

type ChannelsService struct {
	
}

func NewChannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Service)) *[ChannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsService)

func (r *[ChannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsService)) Stop(channel *[Channel](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Channel)) *[ChannelsStopCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsStopCall)

Stop: Stop watching resources through this channel.

type ChannelsStopCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "admin.channels.stop" call.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomerUsageReportsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique ID of the customer to retrieve data for.

Do executes the "reports.customerUsageReports.get" call. Any non-2xx status code is an error. Response headers are in either *UsageReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageToken sets the optional parameter "pageToken": Token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. For your follow-on requests getting all of the report's pages, enter the `nextPageToken` value in the `pageToken` query string.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

Parameters sets the optional parameter "parameters": The `parameters` query string is a comma-separated list of event parameters that refine a report's results. The parameter is associated with a specific application. The application values for the Customers usage report include `accounts`, `app_maker`, `apps_scripts`, `calendar`, `chat`, `classroom`, `cros`, `docs`, `gmail`, `gplus`, `device_management`, `meet`, and `sites`. A `parameters` query string is in the CSV form of `app_name1:param_name1, app_name2:param_name2`. *Note:* The API doesn't accept multiple values of a parameter. If a particular parameter is supplied more than once in the API request, the API only accepts the last value of that request parameter. In addition, if an invalid request parameter is supplied in the API request, the API ignores that request parameter and returns the response corresponding to the remaining valid request parameters. An example of an invalid request parameter is one that does not belong to the application. If no parameters are requested, all parameters are returned.

type CustomerUsageReportsService struct {
	
}

func NewCustomerUsageReportsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Service)) *[CustomerUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsService)

Get: Retrieves a report which is a collection of properties and statistics for a specific customer's account. For more information, see the Customers Usage Report guide. For more information about the customer report's parameters, see the Customers Usage parameters reference guides.

*   date: Represents the date the usage occurred, based on UTC-8:00 (Pacific Standard Time). The timestamp is in the ISO 8601 format ([https://en.wikipedia.org/wiki/ISO_8601](https://en.wikipedia.org/wiki/ISO_8601)), `yyyy-mm-dd`.

type Date struct {
	
	
	Day [int64](https://pkg.go.dev/builtin#int64) `json:"day,omitempty"`
	
	Month [int64](https://pkg.go.dev/builtin#int64) `json:"month,omitempty"`
	
	Year [int64](https://pkg.go.dev/builtin#int64) `json:"year,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Date: Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp

type EntityUsageReportsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique ID of the customer to retrieve data for.

Do executes the "reports.entityUsageReports.get" call. Any non-2xx status code is an error. Response headers are in either *UsageReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filters sets the optional parameter "filters": The `filters` query string is a comma-separated list of an application's event parameters where the parameter's value is manipulated by a relational operator. The `filters` query string includes the name of the application whose usage is returned in the report. The application values for the Entities usage report include `accounts`, `docs`, and `gmail`. Filters are in the form `[application name]:parameter name[parameter value],...`. In this example, the `<>` 'not equal to' operator is URL-encoded in the request's query string (%3C%3E): GET [https://www.googleapis.com/admin/reports/v1/usage/gplus_communities/all/dates/2017-12-01](https://www.googleapis.com/admin/reports/v1/usage/gplus_communities/all/dates/2017-12-01) ?parameters=gplus:community_name,gplus:num_total_members &filters=gplus:num_total_members%3C%3E0 The relational operators include: - `==` - 'equal to'. - `<>` - 'not equal to'. It is URL-encoded (%3C%3E). - `<` - 'less than'. It is URL-encoded (%3C). - `<=` - 'less than or equal to'. It is URL-encoded (%3C=). - `>` - 'greater than'. It is URL-encoded (%3E). - `>=` - 'greater than or equal to'. It is URL-encoded (%3E=). Filters can only be applied to numeric parameters.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

MaxResults sets the optional parameter "maxResults": Determines how many activity records are shown on each response page. For example, if the request sets `maxResults=1` and the report has two activities, the report has two pages. The response's `nextPageToken` property has the token to the second page.

PageToken sets the optional parameter "pageToken": Token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. In your follow-on request getting the next page of the report, enter the `nextPageToken` value in the `pageToken` query string.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

Parameters sets the optional parameter "parameters": The `parameters` query string is a comma-separated list of event parameters that refine a report's results. The parameter is associated with a specific application. The application values for the Entities usage report are only `gplus`. A `parameter` query string is in the CSV form of `[app_name1:param_name1], [app_name2:param_name2]...`. *Note:* The API doesn't accept multiple values of a parameter. If a particular parameter is supplied more than once in the API request, the API only accepts the last value of that request parameter. In addition, if an invalid request parameter is supplied in the API request, the API ignores that request parameter and returns the response corresponding to the remaining valid request parameters. An example of an invalid request parameter is one that does not belong to the application. If no parameters are requested, all parameters are returned.

type EntityUsageReportsService struct {
	
}

func NewEntityUsageReportsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Service)) *[EntityUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsService)

Get: Retrieves a report which is a collection of properties and statistics for entities used by users within the account. For more information, see the Entities Usage Report guide. For more information about the entities report's parameters, see the Entities Usage parameters reference guides.

*   date: Represents the date the usage occurred, based on UTC-8:00 (Pacific Standard Time). The timestamp is in the ISO 8601 format ([https://en.wikipedia.org/wiki/ISO_8601](https://en.wikipedia.org/wiki/ISO_8601)), `yyyy-mm-dd`.
*   entityKey: Represents the key of the object to filter the data with. It is a string which can take the value `all` to get activity events for all users, or any other value for an app-specific entity. For details on how to obtain the `entityKey` for a particular `entityType`, see the Entities Usage parameters reference guides.
*   entityType: Represents the type of entity for the report.

type FieldValue struct {
	DateValue *[Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Date) `json:"dateValue,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	IntegerValue [int64](https://pkg.go.dev/builtin#int64) `json:"integerValue,omitempty,string"`
	LongTextValue [string](https://pkg.go.dev/builtin#string) `json:"longTextValue,omitempty"`
	Reason *[Reason](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Reason) `json:"reason,omitempty"`
	
	SelectionListValue *[FieldValueSelectionListValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionListValue) `json:"selectionListValue,omitempty"`
	
	SelectionValue *[FieldValueSelectionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionValue) `json:"selectionValue,omitempty"`
	TextListValue *[FieldValueTextListValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueTextListValue) `json:"textListValue,omitempty"`
	TextValue [string](https://pkg.go.dev/builtin#string) `json:"textValue,omitempty"`
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	UnsetValue [bool](https://pkg.go.dev/builtin#bool) `json:"unsetValue,omitempty"`
	UserListValue *[FieldValueUserListValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserListValue) `json:"userListValue,omitempty"`
	UserValue *[FieldValueUserValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserValue) `json:"userValue,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FieldValue: Details of the field value set by the user for the particular label.

type FieldValueSelectionListValue struct {
	Values []*[FieldValueSelectionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueSelectionValue) `json:"values,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FieldValueSelectionListValue: Setting a selection list value by selecting multiple values from a dropdown.

type FieldValueSelectionValue struct {
	Badged [bool](https://pkg.go.dev/builtin#bool) `json:"badged,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FieldValueSelectionValue: Setting a selection value by selecting a single value from a dropdown.

type FieldValueTextListValue struct {
	Values [][string](https://pkg.go.dev/builtin#string) `json:"values,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FieldValueTextListValue: Setting a text list value.

type FieldValueUserListValue struct {
	Values []*[FieldValueUserValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#FieldValueUserValue) `json:"values,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FieldValueUserListValue: Setting a user list value by selecting multiple users.

type FieldValueUserValue struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FieldValueUserValue: Setting a user value by selecting a single user.

type NestedParameter struct {
	BoolValue [bool](https://pkg.go.dev/builtin#bool) `json:"boolValue,omitempty"`
	IntValue [int64](https://pkg.go.dev/builtin#int64) `json:"intValue,omitempty,string"`
	MultiBoolValue [][bool](https://pkg.go.dev/builtin#bool) `json:"multiBoolValue,omitempty"`
	MultiIntValue [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"multiIntValue,omitempty"`
	MultiValue [][string](https://pkg.go.dev/builtin#string) `json:"multiValue,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

NestedParameter: JSON template for a parameter used in various reports.

type Reason struct {
	ReasonType [string](https://pkg.go.dev/builtin#string) `json:"reasonType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Reason: The reason why the label/field was applied.

type ResourceDetails struct {
	AppliedLabels []*[AppliedLabel](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#AppliedLabel) `json:"appliedLabels,omitempty"`
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	Relation [string](https://pkg.go.dev/builtin#string) `json:"relation,omitempty"`
	
	
	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ResourceDetails: Details of the resource on which the action was performed.

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Activities *[ActivitiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ActivitiesService)
 Channels *[ChannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#ChannelsService)
 CustomerUsageReports *[CustomerUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#CustomerUsageReportsService)
 EntityUsageReports *[EntityUsageReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#EntityUsageReportsService)
 UserUsageReport *[UserUsageReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportService)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

type UsageReport struct {
	Date [string](https://pkg.go.dev/builtin#string) `json:"date,omitempty"`
	Entity *[UsageReportEntity](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportEntity) `json:"entity,omitempty"`
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	
	
	
	Parameters []*[UsageReportParameters](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportParameters) `json:"parameters,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UsageReport: JSON template for a usage report.

type UsageReportEntity struct {
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	EntityId [string](https://pkg.go.dev/builtin#string) `json:"entityId,omitempty"`
	
	ProfileId [string](https://pkg.go.dev/builtin#string) `json:"profileId,omitempty"`
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	UserEmail [string](https://pkg.go.dev/builtin#string) `json:"userEmail,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UsageReportEntity: Output only. Information about the type of the item.

type UsageReportParameters struct {
	BoolValue [bool](https://pkg.go.dev/builtin#bool) `json:"boolValue,omitempty"`
	
	DatetimeValue [string](https://pkg.go.dev/builtin#string) `json:"datetimeValue,omitempty"`
	IntValue [int64](https://pkg.go.dev/builtin#int64) `json:"intValue,omitempty,string"`
	MsgValue [][googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"msgValue,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	StringValue [string](https://pkg.go.dev/builtin#string) `json:"stringValue,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type UsageReports struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	UsageReports []*[UsageReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReport) `json:"usageReports,omitempty"`
	Warnings []*[UsageReportsWarnings](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportsWarnings) `json:"warnings,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type UsageReportsWarnings struct {
	
	Code [string](https://pkg.go.dev/builtin#string) `json:"code,omitempty"`
	Data []*[UsageReportsWarningsData](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UsageReportsWarningsData) `json:"data,omitempty"`
	
	
	
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type UsageReportsWarningsData struct {
	
	Key [string](https://pkg.go.dev/builtin#string) `json:"key,omitempty"`
	
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type UserUsageReportGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique ID of the customer to retrieve data for.

Do executes the "reports.userUsageReport.get" call. Any non-2xx status code is an error. Response headers are in either *UsageReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filters sets the optional parameter "filters": The `filters` query string is a comma-separated list of an application's event parameters where the parameter's value is manipulated by a relational operator. The `filters` query string includes the name of the application whose usage is returned in the report. The application values for the Users Usage Report include `accounts`, `chat`, `docs`, and `gmail`. Filters are in the form `[application name]:parameter name[parameter value],...`. In this example, the `<>` 'not equal to' operator is URL-encoded in the request's query string (%3C%3E): GET [https://www.googleapis.com/admin/reports/v1/usage/users/all/dates/2013-03-03](https://www.googleapis.com/admin/reports/v1/usage/users/all/dates/2013-03-03) ?parameters=accounts:last_login_time &filters=accounts:last_login_time%3C%3E2010-10-28T10:26:35.000Z The relational operators include: - `==` - 'equal to'. - `<>` - 'not equal to'. It is URL-encoded (%3C%3E). - `<` - 'less than'. It is URL-encoded (%3C). - `<=` - 'less than or equal to'. It is URL-encoded (%3C=). - `>` - 'greater than'. It is URL-encoded (%3E). - `>=` - 'greater than or equal to'. It is URL-encoded (%3E=).

GroupIdFilter sets the optional parameter "groupIdFilter": Comma separated group ids (obfuscated) on which user activities are filtered, i.e. the response will contain activities for only those users that are a part of at least one of the group ids mentioned here. Format: "id:abc123,id:xyz456"

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

MaxResults sets the optional parameter "maxResults": Determines how many activity records are shown on each response page. For example, if the request sets `maxResults=1` and the report has two activities, the report has two pages. The response's `nextPageToken` property has the token to the second page. The `maxResults` query string is optional.

OrgUnitID sets the optional parameter "orgUnitID": ID of the organizational unit to report on. User activity will be shown only for users who belong to the specified organizational unit. Data before Dec 17, 2018 doesn't appear in the filtered results.

PageToken sets the optional parameter "pageToken": Token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. In your follow-on request getting the next page of the report, enter the `nextPageToken` value in the `pageToken` query string.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

Parameters sets the optional parameter "parameters": The `parameters` query string is a comma-separated list of event parameters that refine a report's results. The parameter is associated with a specific application. The application values for the Customers Usage report include `accounts`, `app_maker`, `apps_scripts`, `calendar`, `chat`, `classroom`, `cros`, `docs`, `gmail`, `gplus`, `device_management`, `meet`, and `sites`. A `parameters` query string is in the CSV form of `app_name1:param_name1, app_name2:param_name2`. *Note:* The API doesn't accept multiple values of a parameter. If a particular parameter is supplied more than once in the API request, the API only accepts the last value of that request parameter. In addition, if an invalid request parameter is supplied in the API request, the API ignores that request parameter and returns the response corresponding to the remaining valid request parameters. An example of an invalid request parameter is one that does not belong to the application. If no parameters are requested, all parameters are returned.

type UserUsageReportService struct {
	
}

func NewUserUsageReportService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#Service)) *[UserUsageReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/reports/v1#UserUsageReportService)

Get: Retrieves a report which is a collection of properties and statistics for a set of users with the account. For more information, see the User Usage Report guide. For more information about the user report's parameters, see the Users Usage parameters reference guides.

*   date: Represents the date the usage occurred, based on UTC-8:00 (Pacific Standard Time). The timestamp is in the ISO 8601 format ([https://en.wikipedia.org/wiki/ISO_8601](https://en.wikipedia.org/wiki/ISO_8601)), `yyyy-mm-dd`.
*   userKey: Represents the profile ID or the user email for which the data should be filtered. Can be `all` for all information, or `userKey` for a user's unique Google Workspace profile ID or their primary email address. Must not be a deleted user. For a deleted user, call `users.list` in Directory API with `showDeleted=true`, then use the returned `ID` as the `userKey`.

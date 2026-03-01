# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1

Title: alertcenter package - google.golang.org/api/alertcenter/v1beta1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1

Markdown Content:
Package alertcenter provides access to the Google Workspace Alert Center API.

For product documentation, see: [https://developers.google.com/workspace/admin/alertcenter/](https://developers.google.com/workspace/admin/alertcenter/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/alertcenter/v1beta1"
...
ctx := context.Background()
alertcenterService, err := alertcenter.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

alertcenterService, err := alertcenter.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
alertcenterService, err := alertcenter.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#pkg-constants)
*   [type AbuseDetected](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AbuseDetected)
*       *   [func (s AbuseDetected) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AbuseDetected.MarshalJSON)

*   [type AccessApproval](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccessApproval)
*       *   [func (s AccessApproval) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccessApproval.MarshalJSON)

*   [type AccountSuspensionDetails](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountSuspensionDetails)
*       *   [func (s AccountSuspensionDetails) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountSuspensionDetails.MarshalJSON)

*   [type AccountSuspensionWarning](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountSuspensionWarning)
*       *   [func (s AccountSuspensionWarning) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountSuspensionWarning.MarshalJSON)

*   [type AccountWarning](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountWarning)
*       *   [func (s AccountWarning) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountWarning.MarshalJSON)

*   [type ActionInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ActionInfo)
*   [type ActivityRule](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ActivityRule)
*       *   [func (s ActivityRule) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ActivityRule.MarshalJSON)

*   [type Alert](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Alert)
*       *   [func (s Alert) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Alert.MarshalJSON)

*   [type AlertFeedback](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertFeedback)
*       *   [func (s AlertFeedback) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertFeedback.MarshalJSON)

*   [type AlertMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertMetadata)
*       *   [func (s AlertMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertMetadata.MarshalJSON)

*   [type AlertsBatchDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchDeleteCall)
*       *   [func (c *AlertsBatchDeleteCall) Context(ctx context.Context) *AlertsBatchDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchDeleteCall.Context)
    *   [func (c *AlertsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*BatchDeleteAlertsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchDeleteCall.Do)
    *   [func (c *AlertsBatchDeleteCall) Fields(s ...googleapi.Field) *AlertsBatchDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchDeleteCall.Fields)
    *   [func (c *AlertsBatchDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchDeleteCall.Header)

*   [type AlertsBatchUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchUndeleteCall)
*       *   [func (c *AlertsBatchUndeleteCall) Context(ctx context.Context) *AlertsBatchUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchUndeleteCall.Context)
    *   [func (c *AlertsBatchUndeleteCall) Do(opts ...googleapi.CallOption) (*BatchUndeleteAlertsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchUndeleteCall.Do)
    *   [func (c *AlertsBatchUndeleteCall) Fields(s ...googleapi.Field) *AlertsBatchUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchUndeleteCall.Fields)
    *   [func (c *AlertsBatchUndeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchUndeleteCall.Header)

*   [type AlertsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsDeleteCall)
*       *   [func (c *AlertsDeleteCall) Context(ctx context.Context) *AlertsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsDeleteCall.Context)
    *   [func (c *AlertsDeleteCall) CustomerId(customerId string) *AlertsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsDeleteCall.CustomerId)
    *   [func (c *AlertsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsDeleteCall.Do)
    *   [func (c *AlertsDeleteCall) Fields(s ...googleapi.Field) *AlertsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsDeleteCall.Fields)
    *   [func (c *AlertsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsDeleteCall.Header)

*   [type AlertsFeedbackCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackCreateCall)
*       *   [func (c *AlertsFeedbackCreateCall) Context(ctx context.Context) *AlertsFeedbackCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackCreateCall.Context)
    *   [func (c *AlertsFeedbackCreateCall) CustomerId(customerId string) *AlertsFeedbackCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackCreateCall.CustomerId)
    *   [func (c *AlertsFeedbackCreateCall) Do(opts ...googleapi.CallOption) (*AlertFeedback, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackCreateCall.Do)
    *   [func (c *AlertsFeedbackCreateCall) Fields(s ...googleapi.Field) *AlertsFeedbackCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackCreateCall.Fields)
    *   [func (c *AlertsFeedbackCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackCreateCall.Header)

*   [type AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall)
*       *   [func (c *AlertsFeedbackListCall) Context(ctx context.Context) *AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.Context)
    *   [func (c *AlertsFeedbackListCall) CustomerId(customerId string) *AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.CustomerId)
    *   [func (c *AlertsFeedbackListCall) Do(opts ...googleapi.CallOption) (*ListAlertFeedbackResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.Do)
    *   [func (c *AlertsFeedbackListCall) Fields(s ...googleapi.Field) *AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.Fields)
    *   [func (c *AlertsFeedbackListCall) Filter(filter string) *AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.Filter)
    *   [func (c *AlertsFeedbackListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.Header)
    *   [func (c *AlertsFeedbackListCall) IfNoneMatch(entityTag string) *AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackListCall.IfNoneMatch)

*   [type AlertsFeedbackService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackService)
*       *   [func NewAlertsFeedbackService(s *Service) *AlertsFeedbackService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#NewAlertsFeedbackService)

*       *   [func (r *AlertsFeedbackService) Create(alertId string, alertfeedback *AlertFeedback) *AlertsFeedbackCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackService.Create)
    *   [func (r *AlertsFeedbackService) List(alertId string) *AlertsFeedbackListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackService.List)

*   [type AlertsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall)
*       *   [func (c *AlertsGetCall) Context(ctx context.Context) *AlertsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall.Context)
    *   [func (c *AlertsGetCall) CustomerId(customerId string) *AlertsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall.CustomerId)
    *   [func (c *AlertsGetCall) Do(opts ...googleapi.CallOption) (*Alert, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall.Do)
    *   [func (c *AlertsGetCall) Fields(s ...googleapi.Field) *AlertsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall.Fields)
    *   [func (c *AlertsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall.Header)
    *   [func (c *AlertsGetCall) IfNoneMatch(entityTag string) *AlertsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetCall.IfNoneMatch)

*   [type AlertsGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall)
*       *   [func (c *AlertsGetMetadataCall) Context(ctx context.Context) *AlertsGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall.Context)
    *   [func (c *AlertsGetMetadataCall) CustomerId(customerId string) *AlertsGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall.CustomerId)
    *   [func (c *AlertsGetMetadataCall) Do(opts ...googleapi.CallOption) (*AlertMetadata, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall.Do)
    *   [func (c *AlertsGetMetadataCall) Fields(s ...googleapi.Field) *AlertsGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall.Fields)
    *   [func (c *AlertsGetMetadataCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall.Header)
    *   [func (c *AlertsGetMetadataCall) IfNoneMatch(entityTag string) *AlertsGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsGetMetadataCall.IfNoneMatch)

*   [type AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall)
*       *   [func (c *AlertsListCall) Context(ctx context.Context) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.Context)
    *   [func (c *AlertsListCall) CustomerId(customerId string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.CustomerId)
    *   [func (c *AlertsListCall) Do(opts ...googleapi.CallOption) (*ListAlertsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.Do)
    *   [func (c *AlertsListCall) Fields(s ...googleapi.Field) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.Fields)
    *   [func (c *AlertsListCall) Filter(filter string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.Filter)
    *   [func (c *AlertsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.Header)
    *   [func (c *AlertsListCall) IfNoneMatch(entityTag string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.IfNoneMatch)
    *   [func (c *AlertsListCall) OrderBy(orderBy string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.OrderBy)
    *   [func (c *AlertsListCall) PageSize(pageSize int64) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.PageSize)
    *   [func (c *AlertsListCall) PageToken(pageToken string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.PageToken)
    *   [func (c *AlertsListCall) Pages(ctx context.Context, f func(*ListAlertsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall.Pages)

*   [type AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)
*       *   [func NewAlertsService(s *Service) *AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#NewAlertsService)

*       *   [func (r *AlertsService) BatchDelete(batchdeletealertsrequest *BatchDeleteAlertsRequest) *AlertsBatchDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.BatchDelete)
    *   [func (r *AlertsService) BatchUndelete(batchundeletealertsrequest *BatchUndeleteAlertsRequest) *AlertsBatchUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.BatchUndelete)
    *   [func (r *AlertsService) Delete(alertId string) *AlertsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.Delete)
    *   [func (r *AlertsService) Get(alertId string) *AlertsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.Get)
    *   [func (r *AlertsService) GetMetadata(alertId string) *AlertsGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.GetMetadata)
    *   [func (r *AlertsService) List() *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.List)
    *   [func (r *AlertsService) Undelete(alertId string, undeletealertrequest *UndeleteAlertRequest) *AlertsUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService.Undelete)

*   [type AlertsUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsUndeleteCall)
*       *   [func (c *AlertsUndeleteCall) Context(ctx context.Context) *AlertsUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsUndeleteCall.Context)
    *   [func (c *AlertsUndeleteCall) Do(opts ...googleapi.CallOption) (*Alert, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsUndeleteCall.Do)
    *   [func (c *AlertsUndeleteCall) Fields(s ...googleapi.Field) *AlertsUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsUndeleteCall.Fields)
    *   [func (c *AlertsUndeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsUndeleteCall.Header)

*   [type ApnsCertificateExpirationInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ApnsCertificateExpirationInfo)
*       *   [func (s ApnsCertificateExpirationInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ApnsCertificateExpirationInfo.MarshalJSON)

*   [type AppMakerSqlSetupNotification](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AppMakerSqlSetupNotification)
*       *   [func (s AppMakerSqlSetupNotification) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AppMakerSqlSetupNotification.MarshalJSON)

*   [type AppSettingsChanged](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AppSettingsChanged)
*       *   [func (s AppSettingsChanged) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AppSettingsChanged.MarshalJSON)

*   [type AppsOutage](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AppsOutage)
*       *   [func (s AppsOutage) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AppsOutage.MarshalJSON)

*   [type Attachment](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Attachment)
*       *   [func (s Attachment) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Attachment.MarshalJSON)

*   [type BadWhitelist](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BadWhitelist)
*       *   [func (s BadWhitelist) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BadWhitelist.MarshalJSON)

*   [type BatchDeleteAlertsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchDeleteAlertsRequest)
*       *   [func (s BatchDeleteAlertsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchDeleteAlertsRequest.MarshalJSON)

*   [type BatchDeleteAlertsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchDeleteAlertsResponse)
*       *   [func (s BatchDeleteAlertsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchDeleteAlertsResponse.MarshalJSON)

*   [type BatchUndeleteAlertsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchUndeleteAlertsRequest)
*       *   [func (s BatchUndeleteAlertsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchUndeleteAlertsRequest.MarshalJSON)

*   [type BatchUndeleteAlertsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchUndeleteAlertsResponse)
*       *   [func (s BatchUndeleteAlertsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchUndeleteAlertsResponse.MarshalJSON)

*   [type CloudPubsubTopic](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#CloudPubsubTopic)
*       *   [func (s CloudPubsubTopic) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#CloudPubsubTopic.MarshalJSON)

*   [type Csv](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Csv)
*       *   [func (s Csv) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Csv.MarshalJSON)

*   [type CsvRow](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#CsvRow)
*       *   [func (s CsvRow) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#CsvRow.MarshalJSON)

*   [type DeviceCompromised](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceCompromised)
*       *   [func (s DeviceCompromised) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceCompromised.MarshalJSON)

*   [type DeviceCompromisedSecurityDetail](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceCompromisedSecurityDetail)
*       *   [func (s DeviceCompromisedSecurityDetail) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceCompromisedSecurityDetail.MarshalJSON)

*   [type DeviceManagementRule](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceManagementRule)
*       *   [func (s DeviceManagementRule) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceManagementRule.MarshalJSON)

*   [type DlpRuleViolation](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DlpRuleViolation)
*       *   [func (s DlpRuleViolation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DlpRuleViolation.MarshalJSON)

*   [type DomainId](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainId)
*       *   [func (s DomainId) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainId.MarshalJSON)

*   [type DomainWideTakeoutInitiated](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainWideTakeoutInitiated)
*       *   [func (s DomainWideTakeoutInitiated) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainWideTakeoutInitiated.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Empty)
*   [type Entity](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Entity)
*       *   [func (s Entity) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Entity.MarshalJSON)

*   [type EntityList](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#EntityList)
*       *   [func (s EntityList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#EntityList.MarshalJSON)

*   [type GmailMessageInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#GmailMessageInfo)
*       *   [func (s GmailMessageInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#GmailMessageInfo.MarshalJSON)

*   [type GoogleOperations](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#GoogleOperations)
*       *   [func (s GoogleOperations) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#GoogleOperations.MarshalJSON)

*   [type ListAlertFeedbackResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ListAlertFeedbackResponse)
*       *   [func (s ListAlertFeedbackResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ListAlertFeedbackResponse.MarshalJSON)

*   [type ListAlertsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ListAlertsResponse)
*       *   [func (s ListAlertsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ListAlertsResponse.MarshalJSON)

*   [type LoginDetails](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#LoginDetails)
*       *   [func (s LoginDetails) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#LoginDetails.MarshalJSON)

*   [type MailPhishing](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MailPhishing)
*       *   [func (s MailPhishing) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MailPhishing.MarshalJSON)

*   [type MaliciousEntity](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MaliciousEntity)
*       *   [func (s MaliciousEntity) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MaliciousEntity.MarshalJSON)

*   [type MandatoryServiceAnnouncement](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MandatoryServiceAnnouncement)
*       *   [func (s MandatoryServiceAnnouncement) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MandatoryServiceAnnouncement.MarshalJSON)

*   [type MatchInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MatchInfo)
*       *   [func (s MatchInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MatchInfo.MarshalJSON)

*   [type MergeInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MergeInfo)
*       *   [func (s MergeInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MergeInfo.MarshalJSON)

*   [type Notification](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Notification)
*       *   [func (s Notification) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Notification.MarshalJSON)

*   [type PhishingSpike](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PhishingSpike)
*       *   [func (s PhishingSpike) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PhishingSpike.MarshalJSON)

*   [type PredefinedDetectorInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PredefinedDetectorInfo)
*       *   [func (s PredefinedDetectorInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PredefinedDetectorInfo.MarshalJSON)

*   [type PrimaryAdminChangedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PrimaryAdminChangedEvent)
*       *   [func (s PrimaryAdminChangedEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PrimaryAdminChangedEvent.MarshalJSON)

*   [type ReportingRule](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ReportingRule)
*       *   [func (s ReportingRule) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ReportingRule.MarshalJSON)

*   [type RequestInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RequestInfo)
*       *   [func (s RequestInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RequestInfo.MarshalJSON)

*   [type ResourceInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ResourceInfo)
*       *   [func (s ResourceInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ResourceInfo.MarshalJSON)

*   [type RuleInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RuleInfo)
*       *   [func (s RuleInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RuleInfo.MarshalJSON)

*   [type RuleViolationInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RuleViolationInfo)
*       *   [func (s RuleViolationInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RuleViolationInfo.MarshalJSON)

*   [type SSOProfileCreatedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileCreatedEvent)
*       *   [func (s SSOProfileCreatedEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileCreatedEvent.MarshalJSON)

*   [type SSOProfileDeletedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileDeletedEvent)
*       *   [func (s SSOProfileDeletedEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileDeletedEvent.MarshalJSON)

*   [type SSOProfileUpdatedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileUpdatedEvent)
*       *   [func (s SSOProfileUpdatedEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileUpdatedEvent.MarshalJSON)

*   [type SensitiveAdminAction](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SensitiveAdminAction)
*       *   [func (s SensitiveAdminAction) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SensitiveAdminAction.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#NewService)

*   [type Settings](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Settings)
*       *   [func (s Settings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Settings.MarshalJSON)

*   [type StateSponsoredAttack](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#StateSponsoredAttack)
*       *   [func (s StateSponsoredAttack) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#StateSponsoredAttack.MarshalJSON)

*   [type Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Status)
*       *   [func (s Status) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Status.MarshalJSON)

*   [type SuperAdminPasswordResetEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuperAdminPasswordResetEvent)
*       *   [func (s SuperAdminPasswordResetEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuperAdminPasswordResetEvent.MarshalJSON)

*   [type SupportTicket](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SupportTicket)
*       *   [func (s SupportTicket) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SupportTicket.MarshalJSON)

*   [type SuspiciousActivity](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuspiciousActivity)
*       *   [func (s SuspiciousActivity) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuspiciousActivity.MarshalJSON)

*   [type SuspiciousActivitySecurityDetail](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuspiciousActivitySecurityDetail)
*       *   [func (s SuspiciousActivitySecurityDetail) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuspiciousActivitySecurityDetail.MarshalJSON)

*   [type TransferError](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferError)
*       *   [func (s TransferError) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferError.MarshalJSON)

*   [type TransferMisconfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferMisconfiguration)
*       *   [func (s TransferMisconfiguration) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferMisconfiguration.MarshalJSON)

*   [type UndeleteAlertRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UndeleteAlertRequest)
*       *   [func (s UndeleteAlertRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UndeleteAlertRequest.MarshalJSON)

*   [type User](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#User)
*       *   [func (s User) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#User.MarshalJSON)

*   [type UserChanges](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UserChanges)
*       *   [func (s UserChanges) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UserChanges.MarshalJSON)

*   [type UserDefinedDetectorInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UserDefinedDetectorInfo)
*       *   [func (s UserDefinedDetectorInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UserDefinedDetectorInfo.MarshalJSON)

*   [type V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall)
*       *   [func (c *V1beta1GetSettingsCall) Context(ctx context.Context) *V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall.Context)
    *   [func (c *V1beta1GetSettingsCall) CustomerId(customerId string) *V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall.CustomerId)
    *   [func (c *V1beta1GetSettingsCall) Do(opts ...googleapi.CallOption) (*Settings, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall.Do)
    *   [func (c *V1beta1GetSettingsCall) Fields(s ...googleapi.Field) *V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall.Fields)
    *   [func (c *V1beta1GetSettingsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall.Header)
    *   [func (c *V1beta1GetSettingsCall) IfNoneMatch(entityTag string) *V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall.IfNoneMatch)

*   [type V1beta1Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service)
*       *   [func NewV1beta1Service(s *Service) *V1beta1Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#NewV1beta1Service)

*       *   [func (r *V1beta1Service) GetSettings() *V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service.GetSettings)
    *   [func (r *V1beta1Service) UpdateSettings(settings *Settings) *V1beta1UpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service.UpdateSettings)

*   [type V1beta1UpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall)
*       *   [func (c *V1beta1UpdateSettingsCall) Context(ctx context.Context) *V1beta1UpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall.Context)
    *   [func (c *V1beta1UpdateSettingsCall) CustomerId(customerId string) *V1beta1UpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall.CustomerId)
    *   [func (c *V1beta1UpdateSettingsCall) Do(opts ...googleapi.CallOption) (*Settings, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall.Do)
    *   [func (c *V1beta1UpdateSettingsCall) Fields(s ...googleapi.Field) *V1beta1UpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall.Fields)
    *   [func (c *V1beta1UpdateSettingsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall.Header)

*   [type VaultAcceleratedDeletion](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VaultAcceleratedDeletion)
*       *   [func (s VaultAcceleratedDeletion) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VaultAcceleratedDeletion.MarshalJSON)

*   [type VoiceMisconfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoiceMisconfiguration)
*       *   [func (s VoiceMisconfiguration) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoiceMisconfiguration.MarshalJSON)

*   [type VoicemailMisconfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoicemailMisconfiguration)
*       *   [func (s VoicemailMisconfiguration) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoicemailMisconfiguration.MarshalJSON)

*   [type VoicemailRecipientError](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoicemailRecipientError)
*       *   [func (s VoicemailRecipientError) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoicemailRecipientError.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/alertcenter/v1beta1/alertcenter-gen.go#L100)

const (
	
	AppsAlertsScope = "https://www.googleapis.com/auth/apps.alerts"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type AbuseDetected struct {
	
	AdditionalDetails *[EntityList](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#EntityList) `json:"additionalDetails,omitempty"`
	Product [string](https://pkg.go.dev/builtin#string) `json:"product,omitempty"`
	SubAlertId [string](https://pkg.go.dev/builtin#string) `json:"subAlertId,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	VariationType [string](https://pkg.go.dev/builtin#string) `json:"variationType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AbuseDetected: A generic alert for abusive user activity occurring with a customer.

type AccessApproval struct {
	
	
	
	
	
	
	
	
	
	
	JustificationReason [][string](https://pkg.go.dev/builtin#string) `json:"justificationReason,omitempty"`
	
	OfficeLocation [string](https://pkg.go.dev/builtin#string) `json:"officeLocation,omitempty"`
	Products [][string](https://pkg.go.dev/builtin#string) `json:"products,omitempty"`
	
	RequestId [string](https://pkg.go.dev/builtin#string) `json:"requestId,omitempty"`
	
	Scope [string](https://pkg.go.dev/builtin#string) `json:"scope,omitempty"`
	
	Tickets []*[SupportTicket](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SupportTicket) `json:"tickets,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AccessApproval: Alert that is triggered when Google support requests to access customer data.

type AccountSuspensionDetails struct {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	AbuseReason [string](https://pkg.go.dev/builtin#string) `json:"abuseReason,omitempty"`
	
	
	ProductName [string](https://pkg.go.dev/builtin#string) `json:"productName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AccountSuspensionDetails: Details about why an account is receiving an account suspension warning.

type AccountSuspensionWarning struct {
	
	
	AppealWindow [string](https://pkg.go.dev/builtin#string) `json:"appealWindow,omitempty"`
	
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	SuspensionDetails []*[AccountSuspensionDetails](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AccountSuspensionDetails) `json:"suspensionDetails,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AccountSuspensionWarning: A warning that the customer's account is about to be suspended.

type AccountWarning struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	
	LoginDetails *[LoginDetails](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#LoginDetails) `json:"loginDetails,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AccountWarning: Alerts for user account warning events.

type ActionInfo struct {
}

ActionInfo: Metadata related to the action.

type ActivityRule struct {
	ActionNames [][string](https://pkg.go.dev/builtin#string) `json:"actionNames,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	Query [string](https://pkg.go.dev/builtin#string) `json:"query,omitempty"`
	
	
	SupersededAlerts [][string](https://pkg.go.dev/builtin#string) `json:"supersededAlerts,omitempty"`
	
	
	SupersedingAlert [string](https://pkg.go.dev/builtin#string) `json:"supersedingAlert,omitempty"`
	Threshold [string](https://pkg.go.dev/builtin#string) `json:"threshold,omitempty"`
	
	TriggerSource [string](https://pkg.go.dev/builtin#string) `json:"triggerSource,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`
	WindowSize [string](https://pkg.go.dev/builtin#string) `json:"windowSize,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActivityRule: Alerts from Google Workspace Security Center rules service configured by an admin.

type Alert struct {
	AlertId [string](https://pkg.go.dev/builtin#string) `json:"alertId,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	Data [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"data,omitempty"`
	Deleted [bool](https://pkg.go.dev/builtin#bool) `json:"deleted,omitempty"`
	
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	
	
	
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	Metadata *[AlertMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertMetadata) `json:"metadata,omitempty"`
	
	
	SecurityInvestigationToolLink [string](https://pkg.go.dev/builtin#string) `json:"securityInvestigationToolLink,omitempty"`
	
	
	
	
	Source [string](https://pkg.go.dev/builtin#string) `json:"source,omitempty"`
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Alert: An alert affecting a customer.

type AlertFeedback struct {
	AlertId [string](https://pkg.go.dev/builtin#string) `json:"alertId,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	FeedbackId [string](https://pkg.go.dev/builtin#string) `json:"feedbackId,omitempty"`
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AlertFeedback: A customer feedback about an alert.

type AlertMetadata struct {
	AlertId [string](https://pkg.go.dev/builtin#string) `json:"alertId,omitempty"`
	Assignee [string](https://pkg.go.dev/builtin#string) `json:"assignee,omitempty"`
	
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	
	
	
	
	
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	
	
	Severity [string](https://pkg.go.dev/builtin#string) `json:"severity,omitempty"`
	
	Status [string](https://pkg.go.dev/builtin#string) `json:"status,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AlertMetadata: An alert metadata.

type AlertsBatchDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "alertcenter.alerts.batchDelete" call. Any non-2xx status code is an error. Response headers are in either *BatchDeleteAlertsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AlertsBatchUndeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "alertcenter.alerts.batchUndelete" call. Any non-2xx status code is an error. Response headers are in either *BatchUndeleteAlertsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AlertsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert is associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.alerts.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AlertsFeedbackCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert is associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.alerts.feedback.create" call. Any non-2xx status code is an error. Response headers are in either *AlertFeedback.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AlertsFeedbackListCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert is associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.alerts.feedback.list" call. Any non-2xx status code is an error. Response headers are in either *ListAlertFeedbackResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AlertsFeedbackService struct {
	
}

func NewAlertsFeedbackService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Service)) *[AlertsFeedbackService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackService)

Create: Creates new feedback for an alert. Attempting to create a feedback for a non-existent alert returns `NOT_FOUND` error. Attempting to create a feedback for an alert that is marked for deletion returns `FAILED_PRECONDITION' error.

- alertId: The identifier of the alert this feedback belongs to.

List: Lists all the feedback for an alert. Attempting to list feedbacks for a non-existent alert returns `NOT_FOUND` error.

*   alertId: The alert identifier. The "-" wildcard could be used to represent all alerts.

type AlertsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert is associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.alerts.get" call. Any non-2xx status code is an error. Response headers are in either *Alert.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AlertsGetMetadataCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert metadata is associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.alerts.getMetadata" call. Any non-2xx status code is an error. Response headers are in either *AlertMetadata.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AlertsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alerts are associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.alerts.list" call. Any non-2xx status code is an error. Response headers are in either *ListAlertsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

OrderBy sets the optional parameter "orderBy": The sort order of the list results. If not specified results may be returned in arbitrary order. You can sort the results in descending order based on the creation timestamp using `order_by="create_time desc". Currently, supported sorting are `create_time asc`, `create_time desc`, `update_time desc`

PageSize sets the optional parameter "pageSize": The requested page size. Server may return fewer items than requested. If unspecified, server picks an appropriate default.

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. If empty, a new iteration is started. To continue an iteration, pass in the value from the previous ListAlertsResponse's next_page_token field.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AlertsService struct {
 Feedback *[AlertsFeedbackService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsFeedbackService)	
}

func NewAlertsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Service)) *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)

func (r *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)) BatchDelete(batchdeletealertsrequest *[BatchDeleteAlertsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchDeleteAlertsRequest)) *[AlertsBatchDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchDeleteCall)

BatchDelete: Performs batch delete operation on alerts.

func (r *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)) BatchUndelete(batchundeletealertsrequest *[BatchUndeleteAlertsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#BatchUndeleteAlertsRequest)) *[AlertsBatchUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsBatchUndeleteCall)

BatchUndelete: Performs batch undelete operation on alerts.

Delete: Marks the specified alert for deletion. An alert that has been marked for deletion is removed from Alert Center after 30 days. Marking an alert for deletion has no effect on an alert which has already been marked for deletion. Attempting to mark a nonexistent alert for deletion results in a `NOT_FOUND` error.

- alertId: The identifier of the alert to delete.

Get: Gets the specified alert. Attempting to get a nonexistent alert returns `NOT_FOUND` error.

- alertId: The identifier of the alert to retrieve.

GetMetadata: Returns the metadata of an alert. Attempting to get metadata for a non-existent alert returns `NOT_FOUND` error.

- alertId: The identifier of the alert this metadata belongs to.

func (r *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)) List() *[AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsListCall)

List: Lists the alerts.

func (r *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)) Undelete(alertId [string](https://pkg.go.dev/builtin#string), undeletealertrequest *[UndeleteAlertRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UndeleteAlertRequest)) *[AlertsUndeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsUndeleteCall)

Undelete: Restores, or "undeletes", an alert that was marked for deletion within the past 30 days. Attempting to undelete an alert which was marked for deletion over 30 days ago (which has been removed from the Alert Center database) or a nonexistent alert returns a `NOT_FOUND` error. Attempting to undelete an alert which has not been marked for deletion has no effect.

- alertId: The identifier of the alert to undelete.

type AlertsUndeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "alertcenter.alerts.undelete" call. Any non-2xx status code is an error. Response headers are in either *Alert.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApnsCertificateExpirationInfo struct {
	
	AppleId [string](https://pkg.go.dev/builtin#string) `json:"appleId,omitempty"`
	ExpirationTime [string](https://pkg.go.dev/builtin#string) `json:"expirationTime,omitempty"`
	Uid [string](https://pkg.go.dev/builtin#string) `json:"uid,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApnsCertificateExpirationInfo: The explanation message associated with "APNS certificate is expiring soon" and "APNS certificate has expired" alerts.

type AppMakerSqlSetupNotification struct {
	RequestInfo []*[RequestInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RequestInfo) `json:"requestInfo,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AppMakerSqlSetupNotification: Alerts from App Maker to notify admins to set up default SQL instance.

type AppSettingsChanged struct {
	
	AlertDetails [string](https://pkg.go.dev/builtin#string) `json:"alertDetails,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AppSettingsChanged: Alerts from AppSettingsChanged bucket Rules configured by Admin which contain the following rules: - Calendar settings changed - Drive settings changed - Email settings changed - Mobile settings changed

type AppsOutage struct {
	DashboardUri [string](https://pkg.go.dev/builtin#string) `json:"dashboardUri,omitempty"`
	IncidentTrackingId [string](https://pkg.go.dev/builtin#string) `json:"incidentTrackingId,omitempty"`
	
	MergeInfo *[MergeInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MergeInfo) `json:"mergeInfo,omitempty"`
	NextUpdateTime [string](https://pkg.go.dev/builtin#string) `json:"nextUpdateTime,omitempty"`
	Products [][string](https://pkg.go.dev/builtin#string) `json:"products,omitempty"`
	
	ResolutionTime [string](https://pkg.go.dev/builtin#string) `json:"resolutionTime,omitempty"`
	
	
	
	
	
	
	
	
	
	
	Status [string](https://pkg.go.dev/builtin#string) `json:"status,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AppsOutage: An outage incident reported for a Google Workspace service.

type Attachment struct {
	Csv *[Csv](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Csv) `json:"csv,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Attachment: Attachment with application-specific information about an alert.

type BadWhitelist struct {
	DomainId *[DomainId](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainId) `json:"domainId,omitempty"`
	MaliciousEntity *[MaliciousEntity](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MaliciousEntity) `json:"maliciousEntity,omitempty"`
	Messages []*[GmailMessageInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#GmailMessageInfo) `json:"messages,omitempty"`
	
	SourceIp [string](https://pkg.go.dev/builtin#string) `json:"sourceIp,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BadWhitelist: Alert for setting the domain or IP that malicious email comes from as whitelisted domain or IP in Gmail advanced settings.

type BatchDeleteAlertsRequest struct {
	AlertId [][string](https://pkg.go.dev/builtin#string) `json:"alertId,omitempty"`
	
	
	
	
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchDeleteAlertsRequest: A request to perform batch delete on alerts.

type BatchDeleteAlertsResponse struct {
	FailedAlertStatus map[[string](https://pkg.go.dev/builtin#string)][Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Status) `json:"failedAlertStatus,omitempty"`
	SuccessAlertIds [][string](https://pkg.go.dev/builtin#string) `json:"successAlertIds,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchDeleteAlertsResponse: Response to batch delete operation on alerts.

type BatchUndeleteAlertsRequest struct {
	AlertId [][string](https://pkg.go.dev/builtin#string) `json:"alertId,omitempty"`
	
	
	
	
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchUndeleteAlertsRequest: A request to perform batch undelete on alerts.

type BatchUndeleteAlertsResponse struct {
	FailedAlertStatus map[[string](https://pkg.go.dev/builtin#string)][Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Status) `json:"failedAlertStatus,omitempty"`
	SuccessAlertIds [][string](https://pkg.go.dev/builtin#string) `json:"successAlertIds,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchUndeleteAlertsResponse: Response to batch undelete operation on alerts.

type CloudPubsubTopic struct {
	
	
	
	
	
	
	PayloadFormat [string](https://pkg.go.dev/builtin#string) `json:"payloadFormat,omitempty"`
	
	TopicName [string](https://pkg.go.dev/builtin#string) `json:"topicName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CloudPubsubTopic: A reference to a Cloud Pubsub topic. To register for notifications, the owner of the topic must grant `alerts-api-push-notifications@system.gserviceaccount.com` the `projects.topics.publish` permission.

type Csv struct {
	
	DataRows []*[CsvRow](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#CsvRow) `json:"dataRows,omitempty"`
	Headers [][string](https://pkg.go.dev/builtin#string) `json:"headers,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Csv: A representation of a CSV file attachment, as a list of column headers and a list of data rows.

type CsvRow struct {
	
	Entries [][string](https://pkg.go.dev/builtin#string) `json:"entries,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CsvRow: A representation of a single data row in a CSV file.

type DeviceCompromised struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	Events []*[DeviceCompromisedSecurityDetail](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DeviceCompromisedSecurityDetail) `json:"events,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DeviceCompromised: A mobile device compromised alert. Derived from audit logs.

type DeviceCompromisedSecurityDetail struct {
	
	DeviceCompromisedState [string](https://pkg.go.dev/builtin#string) `json:"deviceCompromisedState,omitempty"`
	DeviceId [string](https://pkg.go.dev/builtin#string) `json:"deviceId,omitempty"`
	DeviceModel [string](https://pkg.go.dev/builtin#string) `json:"deviceModel,omitempty"`
	DeviceType [string](https://pkg.go.dev/builtin#string) `json:"deviceType,omitempty"`
	IosVendorId [string](https://pkg.go.dev/builtin#string) `json:"iosVendorId,omitempty"`
	ResourceId [string](https://pkg.go.dev/builtin#string) `json:"resourceId,omitempty"`
	SerialNumber [string](https://pkg.go.dev/builtin#string) `json:"serialNumber,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DeviceCompromisedSecurityDetail: Detailed information of a single MDM device compromised event.

type DeviceManagementRule struct {
	DeviceId [string](https://pkg.go.dev/builtin#string) `json:"deviceId,omitempty"`
	DeviceModel [string](https://pkg.go.dev/builtin#string) `json:"deviceModel,omitempty"`
	DeviceType [string](https://pkg.go.dev/builtin#string) `json:"deviceType,omitempty"`
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	IosVendorId [string](https://pkg.go.dev/builtin#string) `json:"iosVendorId,omitempty"`
	OwnerId [string](https://pkg.go.dev/builtin#string) `json:"ownerId,omitempty"`
	ResourceId [string](https://pkg.go.dev/builtin#string) `json:"resourceId,omitempty"`
	RuleAction [string](https://pkg.go.dev/builtin#string) `json:"ruleAction,omitempty"`
	SerialNumber [string](https://pkg.go.dev/builtin#string) `json:"serialNumber,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DeviceManagementRule: Alerts from Device Management Rules configured by Admin.

type DlpRuleViolation struct {
	
	
	
	
	RuleViolationInfo *[RuleViolationInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RuleViolationInfo) `json:"ruleViolationInfo,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DlpRuleViolation: Alerts that get triggered on violations of Data Loss Prevention (DLP) rules.

#### type [DomainId](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/alertcenter/v1beta1/alertcenter-gen.go#L1107)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainId "Go to DomainId")

type DomainId struct {
	CustomerPrimaryDomain [string](https://pkg.go.dev/builtin#string) `json:"customerPrimaryDomain,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DomainId: Domain ID of Gmail phishing alerts.

#### type [DomainWideTakeoutInitiated](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/alertcenter/v1beta1/alertcenter-gen.go#L1130)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainWideTakeoutInitiated "Go to DomainWideTakeoutInitiated")

type DomainWideTakeoutInitiated struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	TakeoutRequestId [string](https://pkg.go.dev/builtin#string) `json:"takeoutRequestId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DomainWideTakeoutInitiated: A takeout operation for the entire domain was initiated by an admin. Derived from audit logs.

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type Entity struct {
	
	Link [string](https://pkg.go.dev/builtin#string) `json:"link,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	Values [][string](https://pkg.go.dev/builtin#string) `json:"values,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Entity: Individual entity affected by, or related to, an alert.

type EntityList struct {
	Entities []*[Entity](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Entity) `json:"entities,omitempty"`
	
	Headers [][string](https://pkg.go.dev/builtin#string) `json:"headers,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

EntityList: EntityList stores entities in a format that can be translated to a table in the Alert Center UI.

type GmailMessageInfo struct {
	
	AttachmentsSha256Hash [][string](https://pkg.go.dev/builtin#string) `json:"attachmentsSha256Hash,omitempty"`
	Date [string](https://pkg.go.dev/builtin#string) `json:"date,omitempty"`
	Md5HashMessageBody [string](https://pkg.go.dev/builtin#string) `json:"md5HashMessageBody,omitempty"`
	
	Md5HashSubject [string](https://pkg.go.dev/builtin#string) `json:"md5HashSubject,omitempty"`
	
	MessageBodySnippet [string](https://pkg.go.dev/builtin#string) `json:"messageBodySnippet,omitempty"`
	MessageId [string](https://pkg.go.dev/builtin#string) `json:"messageId,omitempty"`
	Recipient [string](https://pkg.go.dev/builtin#string) `json:"recipient,omitempty"`
	SentTime [string](https://pkg.go.dev/builtin#string) `json:"sentTime,omitempty"`
	SubjectText [string](https://pkg.go.dev/builtin#string) `json:"subjectText,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GmailMessageInfo: Details of a message in phishing spike alert.

type GoogleOperations struct {
	
	AffectedUserEmails [][string](https://pkg.go.dev/builtin#string) `json:"affectedUserEmails,omitempty"`
	
	
	AttachmentData *[Attachment](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Attachment) `json:"attachmentData,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	Domain [string](https://pkg.go.dev/builtin#string) `json:"domain,omitempty"`
	
	Header [string](https://pkg.go.dev/builtin#string) `json:"header,omitempty"`
	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleOperations: An incident reported by Google Operations for a Google Workspace application.

type ListAlertFeedbackResponse struct {
	
	Feedback []*[AlertFeedback](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertFeedback) `json:"feedback,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAlertFeedbackResponse: Response message for an alert feedback listing request.

type ListAlertsResponse struct {
	Alerts []*[Alert](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Alert) `json:"alerts,omitempty"`
	
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAlertsResponse: Response message for an alert listing request.

type LoginDetails struct {
	
	IpAddress [string](https://pkg.go.dev/builtin#string) `json:"ipAddress,omitempty"`
	
	LoginTime [string](https://pkg.go.dev/builtin#string) `json:"loginTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LoginDetails: The details of the login action.

type MailPhishing struct {
	DomainId *[DomainId](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#DomainId) `json:"domainId,omitempty"`
	IsInternal [bool](https://pkg.go.dev/builtin#bool) `json:"isInternal,omitempty"`
	MaliciousEntity *[MaliciousEntity](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MaliciousEntity) `json:"maliciousEntity,omitempty"`
	Messages []*[GmailMessageInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#GmailMessageInfo) `json:"messages,omitempty"`
	
	
	
	
	
	SystemActionType [string](https://pkg.go.dev/builtin#string) `json:"systemActionType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MailPhishing: Proto for all phishing alerts with common payload. Supported types are any of the following: * User reported phishing * User reported spam spike * Suspicious message reported * Phishing reclassification * Malware reclassification * Gmail potential employee spoofing

type MaliciousEntity struct {
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	Entity *[User](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#User) `json:"entity,omitempty"`
	FromHeader [string](https://pkg.go.dev/builtin#string) `json:"fromHeader,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MaliciousEntity: Entity whose actions triggered a Gmail phishing alert.

#### type [MandatoryServiceAnnouncement](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/alertcenter/v1beta1/alertcenter-gen.go#L1446)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MandatoryServiceAnnouncement "Go to MandatoryServiceAnnouncement")added in v0.72.0

type MandatoryServiceAnnouncement struct {
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MandatoryServiceAnnouncement: Alert Created by the MSA team for communications necessary for continued use of Google Workspace Products.

#### func (MandatoryServiceAnnouncement) [MarshalJSON](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/alertcenter/v1beta1/alertcenter-gen.go#L1464)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MandatoryServiceAnnouncement.MarshalJSON "Go to MandatoryServiceAnnouncement.MarshalJSON")added in v0.72.0

type MatchInfo struct {
	PredefinedDetector *[PredefinedDetectorInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PredefinedDetectorInfo) `json:"predefinedDetector,omitempty"`
	UserDefinedDetector *[UserDefinedDetectorInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#UserDefinedDetectorInfo) `json:"userDefinedDetector,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MatchInfo: Proto that contains match information from the condition part of the rule.

type MergeInfo struct {
	
	NewAlertId [string](https://pkg.go.dev/builtin#string) `json:"newAlertId,omitempty"`
	NewIncidentTrackingId [string](https://pkg.go.dev/builtin#string) `json:"newIncidentTrackingId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MergeInfo: New alert tracking numbers.

type PredefinedDetectorInfo struct {
	DetectorName [string](https://pkg.go.dev/builtin#string) `json:"detectorName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PredefinedDetectorInfo: Detector provided by Google.

type PrimaryAdminChangedEvent struct {
	Domain [string](https://pkg.go.dev/builtin#string) `json:"domain,omitempty"`
	
	PreviousAdminEmail [string](https://pkg.go.dev/builtin#string) `json:"previousAdminEmail,omitempty"`
	UpdatedAdminEmail [string](https://pkg.go.dev/builtin#string) `json:"updatedAdminEmail,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PrimaryAdminChangedEvent: Event occurred when primary admin changed in customer's account. The event are being received from insight forwarder

type ReportingRule struct {
	
	AlertDetails [string](https://pkg.go.dev/builtin#string) `json:"alertDetails,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	Query [string](https://pkg.go.dev/builtin#string) `json:"query,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ReportingRule: Alerts from Reporting Rules configured by Admin.

type RequestInfo struct {
	
	AppDeveloperEmail [][string](https://pkg.go.dev/builtin#string) `json:"appDeveloperEmail,omitempty"`
	AppKey [string](https://pkg.go.dev/builtin#string) `json:"appKey,omitempty"`
	
	NumberOfRequests [int64](https://pkg.go.dev/builtin#int64) `json:"numberOfRequests,omitempty,string"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RequestInfo: Requests for one application that needs default SQL setup.

type ResourceInfo struct {
	ChatAttachmentId [string](https://pkg.go.dev/builtin#string) `json:"chatAttachmentId,omitempty"`
	ChatMessageId [string](https://pkg.go.dev/builtin#string) `json:"chatMessageId,omitempty"`
	
	
	DeviceId [string](https://pkg.go.dev/builtin#string) `json:"deviceId,omitempty"`
	DocumentId [string](https://pkg.go.dev/builtin#string) `json:"documentId,omitempty"`
	MessageId [string](https://pkg.go.dev/builtin#string) `json:"messageId,omitempty"`
	
	ResourceTitle [string](https://pkg.go.dev/builtin#string) `json:"resourceTitle,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ResourceInfo: Proto that contains resource information.

type RuleInfo struct {
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	ResourceName [string](https://pkg.go.dev/builtin#string) `json:"resourceName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RuleInfo: Proto that contains rule information.

type RuleViolationInfo struct {
	
	
	
	
	
	
	DataSource [string](https://pkg.go.dev/builtin#string) `json:"dataSource,omitempty"`
	
	
	
	
	
	EventType [string](https://pkg.go.dev/builtin#string) `json:"eventType,omitempty"`
	MatchInfo []*[MatchInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#MatchInfo) `json:"matchInfo,omitempty"`
	
	
	
	
	
	Recipients [][string](https://pkg.go.dev/builtin#string) `json:"recipients,omitempty"`
	ResourceInfo *[ResourceInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ResourceInfo) `json:"resourceInfo,omitempty"`
	RuleInfo *[RuleInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#RuleInfo) `json:"ruleInfo,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	SuppressedActionTypes [][string](https://pkg.go.dev/builtin#string) `json:"suppressedActionTypes,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	Trigger [string](https://pkg.go.dev/builtin#string) `json:"trigger,omitempty"`
	TriggeredActionInfo []*[ActionInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#ActionInfo) `json:"triggeredActionInfo,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	TriggeredActionTypes [][string](https://pkg.go.dev/builtin#string) `json:"triggeredActionTypes,omitempty"`
	
	
	TriggeringUserEmail [string](https://pkg.go.dev/builtin#string) `json:"triggeringUserEmail,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RuleViolationInfo: Common alert information about violated rules that are configured by Google Workspace administrators.

type SSOProfileCreatedEvent struct {
	InboundSsoProfileName [string](https://pkg.go.dev/builtin#string) `json:"inboundSsoProfileName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SSOProfileCreatedEvent: Event occurred when SSO Profile created in customer's account. The event are being received from insight forwarder

type SSOProfileDeletedEvent struct {
	InboundSsoProfileName [string](https://pkg.go.dev/builtin#string) `json:"inboundSsoProfileName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SSOProfileDeletedEvent: Event occurred when SSO Profile deleted in customer's account. The event are being received from insight forwarder

type SSOProfileUpdatedEvent struct {
	InboundSsoProfileChanges [string](https://pkg.go.dev/builtin#string) `json:"inboundSsoProfileChanges,omitempty"`
	InboundSsoProfileName [string](https://pkg.go.dev/builtin#string) `json:"inboundSsoProfileName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SSOProfileUpdatedEvent: Event occurred when SSO Profile updated in customer's account. The event are being received from insight forwarder

type SensitiveAdminAction struct {
	ActorEmail [string](https://pkg.go.dev/builtin#string) `json:"actorEmail,omitempty"`
	EventTime [string](https://pkg.go.dev/builtin#string) `json:"eventTime,omitempty"`
	
	PrimaryAdminChangedEvent *[PrimaryAdminChangedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#PrimaryAdminChangedEvent) `json:"primaryAdminChangedEvent,omitempty"`
	
	SsoProfileCreatedEvent *[SSOProfileCreatedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileCreatedEvent) `json:"ssoProfileCreatedEvent,omitempty"`
	
	SsoProfileDeletedEvent *[SSOProfileDeletedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileDeletedEvent) `json:"ssoProfileDeletedEvent,omitempty"`
	
	SsoProfileUpdatedEvent *[SSOProfileUpdatedEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SSOProfileUpdatedEvent) `json:"ssoProfileUpdatedEvent,omitempty"`
	
	SuperAdminPasswordResetEvent *[SuperAdminPasswordResetEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuperAdminPasswordResetEvent) `json:"superAdminPasswordResetEvent,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SensitiveAdminAction: Alert that is triggered when Sensitive Admin Action occur in customer account.

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Alerts *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#AlertsService)
 V1beta1 *[V1beta1Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

Settings: Customer-level settings.

type StateSponsoredAttack struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

StateSponsoredAttack: A state-sponsored attack alert. Derived from audit logs.

type Status struct {
	Code [int64](https://pkg.go.dev/builtin#int64) `json:"code,omitempty"`
	
	Details [][googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"details,omitempty"`
	
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Status: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC ([https://github.com/grpc](https://github.com/grpc)). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide ([https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)).

type SuperAdminPasswordResetEvent struct {
	UserEmail [string](https://pkg.go.dev/builtin#string) `json:"userEmail,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SuperAdminPasswordResetEvent: Event occurred when password was reset for super admin in customer's account. The event are being received from insight forwarder

type SupportTicket struct {
	TicketId [string](https://pkg.go.dev/builtin#string) `json:"ticketId,omitempty"`
	TicketUrl [string](https://pkg.go.dev/builtin#string) `json:"ticketUrl,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SupportTicket: Support ticket related to Access Approvals request

type SuspiciousActivity struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	Events []*[SuspiciousActivitySecurityDetail](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#SuspiciousActivitySecurityDetail) `json:"events,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SuspiciousActivity: A mobile suspicious activity alert. Derived from audit logs.

type SuspiciousActivitySecurityDetail struct {
	DeviceId [string](https://pkg.go.dev/builtin#string) `json:"deviceId,omitempty"`
	DeviceModel [string](https://pkg.go.dev/builtin#string) `json:"deviceModel,omitempty"`
	DeviceProperty [string](https://pkg.go.dev/builtin#string) `json:"deviceProperty,omitempty"`
	DeviceType [string](https://pkg.go.dev/builtin#string) `json:"deviceType,omitempty"`
	IosVendorId [string](https://pkg.go.dev/builtin#string) `json:"iosVendorId,omitempty"`
	NewValue [string](https://pkg.go.dev/builtin#string) `json:"newValue,omitempty"`
	OldValue [string](https://pkg.go.dev/builtin#string) `json:"oldValue,omitempty"`
	ResourceId [string](https://pkg.go.dev/builtin#string) `json:"resourceId,omitempty"`
	SerialNumber [string](https://pkg.go.dev/builtin#string) `json:"serialNumber,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SuspiciousActivitySecurityDetail: Detailed information of a single MDM suspicious activity event.

type TransferError struct {
	
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	
	
	
	
	
	EntityType [string](https://pkg.go.dev/builtin#string) `json:"entityType,omitempty"`
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	
	
	
	
	
	
	
	
	
	InvalidReason [string](https://pkg.go.dev/builtin#string) `json:"invalidReason,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TransferError: Details for an invalid transfer or forward.

type TransferMisconfiguration struct {
	Errors []*[TransferError](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferError) `json:"errors,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TransferMisconfiguration: Error related to transferring or forwarding a phone call.

type UndeleteAlertRequest struct {
	
	
	
	
	CustomerId [string](https://pkg.go.dev/builtin#string) `json:"customerId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UndeleteAlertRequest: A request to undelete a specific alert that was marked for deletion.

type User struct {
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	EmailAddress [string](https://pkg.go.dev/builtin#string) `json:"emailAddress,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

User: A user.

type UserChanges struct {
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UserChanges: Alerts from UserChanges bucket Rules for predefined rules which contain the following rules: - Suspended user made active - New user added - User suspended (by admin) - User granted admin privileges - User admin privileges revoked - User deleted - Users password changed

type UserDefinedDetectorInfo struct {
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	ResourceName [string](https://pkg.go.dev/builtin#string) `json:"resourceName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UserDefinedDetectorInfo: Detector defined by administrators.

type V1beta1GetSettingsCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert settings are associated with. The `customer_id` must/ have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.getSettings" call. Any non-2xx status code is an error. Response headers are in either *Settings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type V1beta1Service struct {
	
}

func NewV1beta1Service(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Service)) *[V1beta1Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service)

func (r *[V1beta1Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service)) GetSettings() *[V1beta1GetSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1GetSettingsCall)

GetSettings: Returns customer-level settings.

func (r *[V1beta1Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1Service)) UpdateSettings(settings *[Settings](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#Settings)) *[V1beta1UpdateSettingsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#V1beta1UpdateSettingsCall)

UpdateSettings: Updates the customer-level settings.

type V1beta1UpdateSettingsCall struct {
	
}

Context sets the context to be used in this call's Do method.

CustomerId sets the optional parameter "customerId": The unique identifier of the Google Workspace account of the customer the alert settings are associated with. The `customer_id` must have the initial "C" stripped (for example, `046psxkn`). Inferred from the caller identity if not provided. Find your customer ID ([https://support.google.com/cloudidentity/answer/10070793](https://support.google.com/cloudidentity/answer/10070793)).

Do executes the "alertcenter.updateSettings" call. Any non-2xx status code is an error. Response headers are in either *Settings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type VaultAcceleratedDeletion struct {
	
	
	
	
	
	
	ActionType [string](https://pkg.go.dev/builtin#string) `json:"actionType,omitempty"`
	
	
	
	
	AppType [string](https://pkg.go.dev/builtin#string) `json:"appType,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	DeletionRequestId [string](https://pkg.go.dev/builtin#string) `json:"deletionRequestId,omitempty"`
	
	MatterId [string](https://pkg.go.dev/builtin#string) `json:"matterId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

VaultAcceleratedDeletion: Alert that is triggered when a Vault accelerated deletion request is created or canceled.

type VoiceMisconfiguration struct {
	EntityName [string](https://pkg.go.dev/builtin#string) `json:"entityName,omitempty"`
	
	
	
	
	
	EntityType [string](https://pkg.go.dev/builtin#string) `json:"entityType,omitempty"`
	FixUri [string](https://pkg.go.dev/builtin#string) `json:"fixUri,omitempty"`
	MembersMisconfiguration *[TransferMisconfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferMisconfiguration) `json:"membersMisconfiguration,omitempty"`
	
	TransferMisconfiguration *[TransferMisconfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#TransferMisconfiguration) `json:"transferMisconfiguration,omitempty"`
	VoicemailMisconfiguration *[VoicemailMisconfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoicemailMisconfiguration) `json:"voicemailMisconfiguration,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

VoiceMisconfiguration: An alert triggered when Google Voice configuration becomes invalid, generally due to an external entity being modified or deleted.

type VoicemailMisconfiguration struct {
	Errors []*[VoicemailRecipientError](https://pkg.go.dev/google.golang.org/api@v0.269.0/alertcenter/v1beta1#VoicemailRecipientError) `json:"errors,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

VoicemailMisconfiguration: Issue(s) with sending to voicemail.

type VoicemailRecipientError struct {
	
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	
	
	
	InvalidReason [string](https://pkg.go.dev/builtin#string) `json:"invalidReason,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

VoicemailRecipientError: Issue(s) with a voicemail recipient.

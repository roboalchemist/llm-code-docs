Source: https://docs.slack.dev/tools/java-slack-sdk/guides/web-api-for-admins

# Web API for Org Admins

The method names of a portion of [API methods](/reference/methods) start with `admin.`. These APIs are not available for all developers. They are intended to be used by [Enterprise Grid](/enterprise) organization administrators.

* * *

## Call the Web API for org admins {#call-the-web-api-for-org-admins}

There is no difference regarding the ways to use those APIs except for necessary scopes.

```text
String orgAdminToken = System.getenv("SLACK_ORG_ADMIN_TOKEN");Slack slack = Slack.getInstance();// Reset a user sessionAdminUsersSessionResetResponse response = slack.methods(orgAdminToken).adminUsersSessionReset(r -> r  .userId(userId));// Convert a channel to an Org channelAdminConversationsSetTeamsResponse orgChannelResp = slack.methods(orgAdminToken).adminConversationsSetTeams(r -> r  .teamId("T1234567")  .channelId("C12345567")  .orgChannel(true));// Slack App ApprovalsAdminAppsApprovedListResponse response = slack.methods(orgAdminToken).adminAppsApprovedList(r -> r  .limit(1000)  .teamId("T1234567"));// There are more...!
```

You can look up the comprehensive list of admin APIs [here](/admins/). Also, checking [the Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-client/1.48.0/slack-api-client-1.48.0-javadoc.jar/!/com/slack/api/methods/MethodsClient.html) and search by a keyword starting with **`admin`** may be helpful to know methods to use.

Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/classes/WebClient

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WebClient

# Class: WebClient

Defined in: [packages/web-api/src/WebClient.ts:190](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L190)

A client for Slack's Web API

This client provides an alias for each [API method](https://docs.slack.dev/reference/methods%7CWeb). Each method is a convenience wrapper for calling the [WebClient#apiCall](#apicall) method using the method name as the first parameter.

## Extends {#extends}

* [`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods)

## Constructors {#constructors}

### Constructor {#constructor}

```
new WebClient(token?, webClientOptions?): WebClient;
```

Defined in: [packages/web-api/src/WebClient.ts:264](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L264)

#### Parameters {#parameters}

##### token? {#token}

`string`

An API token to authenticate/authorize with Slack (usually start with `xoxp`, `xoxb`)

##### webClientOptions? {#webclientoptions}

[`WebClientOptions`](/tools/node-slack-sdk/reference/web-api/interfaces/WebClientOptions) = `{}`

Configuration options.

#### Returns {#returns}

`WebClient`

#### Overrides {#overrides}

```
Methods.constructor
```

## Properties {#properties}

### admin {#admin}

```
readonly admin: object;
```

Defined in: [packages/web-api/src/methods.ts:612](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L612)

#### analytics {#analytics}

```
analytics: object;
```

##### analytics.getFile {#analyticsgetfile}

```
getFile: MethodWithRequiredArgument<AdminAnalyticsGetFileArguments, AdminAnalyticsGetFileResponse>;
```

###### Description {#description}

Retrieve analytics data for a given date, presented as a compressed JSON file.

###### See {#see}

[\`api.test\` API reference](https://docs.slack.dev/reference/methods/api.test).

#### apps {#apps}

```
apps: object;
```

##### apps.activities {#appsactivities}

```
activities: object;
```

##### apps.activities.list {#appsactivitieslist}

```
list: Method<AdminAppsActivitiesListArguments, AdminAppsActivitiesListResponse>;
```

###### Description {#description-1}

Get logs for a specified team/org.

###### See {#see-1}

[\`admin.apps.activities.list\` API reference](https://docs.slack.dev/reference/methods/admin.apps.activities.list).

##### apps.approve {#appsapprove}

```
approve: MethodWithRequiredArgument<AdminAppsApproveArguments, AdminAppsApproveResponse>;
```

###### Description {#description-2}

Approve an app for installation on a workspace.

###### See {#see-2}

[\`admin.apps.approve\` API reference](https://docs.slack.dev/reference/methods/admin.apps.approve).

##### apps.approved {#appsapproved}

```
approved: object;
```

##### apps.approved.list {#appsapprovedlist}

```
list: MethodWithRequiredArgument<AdminAppsApprovedListArguments, AdminAppsApprovedListResponse>;
```

###### Description {#description-3}

List approved apps for an org or workspace.

###### See {#see-3}

[\`admin.apps.approved.list\` API reference](https://docs.slack.dev/reference/methods/admin.apps.approved.list).

##### apps.clearResolution {#appsclearresolution}

```
clearResolution: MethodWithRequiredArgument<AdminAppsClearResolutionArguments, AdminAppsClearResolutionResponse>;
```

###### Description {#description-4}

Clear an app resolution.

###### See {#see-4}

[\`admin.apps.clearResolution\` API reference](https://docs.slack.dev/reference/methods/admin.apps.clearResolution).

##### apps.config {#appsconfig}

```
config: object;
```

##### apps.config.lookup {#appsconfiglookup}

```
lookup: MethodWithRequiredArgument<AdminAppsConfigLookupArguments, AdminAppsConfigLookupResponse>;
```

###### Description {#description-5}

Look up the app config for connectors by their IDs.

###### See {#see-5}

[\`admin.apps.config.lookup\` API reference](https://docs.slack.dev/reference/methods/admin.apps.config.lookup).

##### apps.config.set {#appsconfigset}

```
set: MethodWithRequiredArgument<AdminAppsConfigSetArguments, AdminAppsConfigSetResponse>;
```

###### Description {#description-6}

Set the app config for a connector.

###### See {#see-6}

[\`admin.apps.config.set\` API reference](https://docs.slack.dev/reference/methods/admin.apps.config.set).

##### apps.requests {#appsrequests}

```
requests: object;
```

##### apps.requests.cancel {#appsrequestscancel}

```
cancel: MethodWithRequiredArgument<AdminAppsRequestsCancelArguments, AdminAppsRequestsCancelResponse>;
```

###### Description {#description-7}

Cancel app request for team.

###### See {#see-7}

[\`admin.apps.requests.cancel\` API reference](https://docs.slack.dev/reference/methods/admin.apps.requests.cancel).

##### apps.requests.list {#appsrequestslist}

```
list: MethodWithRequiredArgument<AdminAppsRequestsListArguments, AdminAppsRequestsListResponse>;
```

###### Description {#description-8}

List app requests for a team/workspace.

###### See {#see-8}

[\`admin.apps.requests.list\` API reference](https://docs.slack.dev/reference/methods/admin.apps.requests.list).

##### apps.restrict {#appsrestrict}

```
restrict: MethodWithRequiredArgument<AdminAppsRestrictArguments, AdminAppsRestrictResponse>;
```

###### Description {#description-9}

Restrict an app for installation on a workspace.

###### See {#see-9}

[\`admin.apps.restrict\` API reference](https://docs.slack.dev/reference/methods/admin.apps.restrict).

##### apps.restricted {#appsrestricted}

```
restricted: object;
```

##### apps.restricted.list {#appsrestrictedlist}

```
list: MethodWithRequiredArgument<AdminAppsRestrictedListArguments, AdminAppsRestrictedListResponse>;
```

###### Description {#description-10}

List restricted apps for an org or workspace.

###### See {#see-10}

[\`admin.apps.restricted.list\` API reference](https://docs.slack.dev/reference/methods/admin.apps.restricted.list).

##### apps.uninstall {#appsuninstall}

```
uninstall: MethodWithRequiredArgument<AdminAppsUninstallArguments, AdminAppsUninstallResponse>;
```

###### Description {#description-11}

Uninstall an app from one or many workspaces, or an entire enterprise organization.

###### See {#see-11}

[\`admin.apps.uninstall\` API reference](https://docs.slack.dev/reference/methods/admin.apps.uninstall).

#### auth {#auth}

```
auth: object;
```

##### auth.policy {#authpolicy}

```
policy: object;
```

##### auth.policy.assignEntities {#authpolicyassignentities}

```
assignEntities: MethodWithRequiredArgument<AdminAuthPolicyAssignEntitiesArguments, AdminAuthPolicyAssignEntitiesResponse>;
```

###### Description {#description-12}

Assign entities to a particular authentication policy.

###### See {#see-12}

[\`admin.auth.policy.assignEntities\` API reference](https://docs.slack.dev/reference/methods/admin.auth.policy.assignEntities).

##### auth.policy.getEntities {#authpolicygetentities}

```
getEntities: MethodWithRequiredArgument<AdminAuthPolicyGetEntitiesArguments, AdminAuthPolicyGetEntitiesResponse>;
```

###### Description {#description-13}

Fetch all the entities assigned to a particular authentication policy by name.

###### See {#see-13}

[\`admin.auth.policy.getEntities\` API reference](https://docs.slack.dev/reference/methods/admin.auth.policy.getEntities).

##### auth.policy.removeEntities {#authpolicyremoveentities}

```
removeEntities: MethodWithRequiredArgument<AdminAuthPolicyRemoveEntitiesArguments, AdminAuthPolicyRemoveEntitiesResponse>;
```

###### Description {#description-14}

Remove specified entities from a specified authentication policy.

###### See {#see-14}

[\`admin.auth.policy.removeEntities\` API reference](https://docs.slack.dev/reference/methods/admin.auth.policy.removeEntities).

#### barriers {#barriers}

```
barriers: object;
```

##### barriers.create {#barrierscreate}

```
create: MethodWithRequiredArgument<AdminBarriersCreateArguments, AdminBarriersCreateResponse>;
```

###### Description {#description-15}

Create an Information Barrier.

###### See {#see-15}

[\`admin.barriers.create\` API reference](https://docs.slack.dev/reference/methods/admin.barriers.create).

##### barriers.delete {#barriersdelete}

```
delete: MethodWithRequiredArgument<AdminBarriersDeleteArguments, AdminBarriersDeleteResponse>;
```

###### Description {#description-16}

Delete an existing Information Barrier.

###### See {#see-16}

[\`admin.barriers.delete\` API reference](https://docs.slack.dev/reference/methods/admin.barriers.delete).

##### barriers.list {#barrierslist}

```
list: Method<AdminBarriersListArguments, AdminBarriersListResponse>;
```

###### Description {#description-17}

Get all Information Barriers for your organization.

###### See {#see-17}

[\`admin.barriers.list\` API reference](https://docs.slack.dev/reference/methods/admin.barriers.list).

##### barriers.update {#barriersupdate}

```
update: MethodWithRequiredArgument<AdminBarriersUpdateArguments, AdminBarriersUpdateResponse>;
```

###### Description {#description-18}

Update an existing Information Barrier.

###### See {#see-18}

[\`admin.barriers.update\` API reference](https://docs.slack.dev/reference/methods/admin.barriers.update).

#### conversations {#conversations}

```
conversations: object;
```

##### conversations.archive {#conversationsarchive}

```
archive: MethodWithRequiredArgument<AdminConversationsArchiveArguments, AdminConversationsArchiveResponse>;
```

###### Description {#description-19}

Archive a public or private channel.

###### See {#see-19}

[\`admin.conversations.archive\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.archive).

##### conversations.bulkArchive {#conversationsbulkarchive}

```
bulkArchive: MethodWithRequiredArgument<AdminConversationsBulkArchiveArguments, AdminConversationsBulkArchiveResponse>;
```

###### Description {#description-20}

Archive public or private channels in bulk.

###### See {#see-20}

[\`admin.conversations.bulkArchive\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.bulkArchive).

##### conversations.bulkDelete {#conversationsbulkdelete}

```
bulkDelete: MethodWithRequiredArgument<AdminConversationsBulkDeleteArguments, AdminConversationsBulkDeleteResponse>;
```

###### Description {#description-21}

Delete public or private channels in bulk.

###### See {#see-21}

[\`admin.conversations.bulkDelete\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.bulkDelete).

##### conversations.bulkMove {#conversationsbulkmove}

```
bulkMove: MethodWithRequiredArgument<AdminConversationsBulkMoveArguments, AdminConversationsBulkMoveResponse>;
```

###### Description {#description-22}

Move public or private channels in bulk.

###### See {#see-22}

[\`admin.conversations.bulkMove\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.bulkMove).

##### conversations.convertToPrivate {#conversationsconverttoprivate}

```
convertToPrivate: MethodWithRequiredArgument<AdminConversationsConvertToPrivateArguments, AdminConversationsConvertToPrivateResponse>;
```

###### Description {#description-23}

Convert a public channel to a private channel.

###### See {#see-23}

[\`admin.conversations.convertToPrivate\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.convertToPrivate).

##### conversations.convertToPublic {#conversationsconverttopublic}

```
convertToPublic: MethodWithRequiredArgument<AdminConversationsConvertToPublicArguments, AdminConversationsConvertToPublicResponse>;
```

###### Description {#description-24}

Convert a private channel to a public channel.

###### See {#see-24}

[\`admin.conversations.convertToPublic\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.convertToPublic).

##### conversations.create {#conversationscreate}

```
create: MethodWithRequiredArgument<AdminConversationsCreateArguments, AdminConversationsCreateResponse>;
```

###### Description {#description-25}

Create a public or private channel-based conversation.

###### See {#see-25}

[\`admin.conversations.create\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.create).

##### conversations.delete {#conversationsdelete}

```
delete: MethodWithRequiredArgument<AdminConversationsDeleteArguments, AdminConversationsDeleteResponse>;
```

###### Description {#description-26}

Delete a public or private channel.

###### See {#see-26}

[\`admin.conversations.delete\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.delete).

##### conversations.disconnectShared {#conversationsdisconnectshared}

```
disconnectShared: MethodWithRequiredArgument<AdminConversationsDisconnectSharedArguments, AdminConversationsDisconnectSharedResponse>;
```

###### Description {#description-27}

Disconnect a connected channel from one or more workspaces.

###### See {#see-27}

[\`admin.conversations.disconnectShared\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.disconnectShared).

##### conversations.ekm {#conversationsekm}

```
ekm: object;
```

##### conversations.ekm.listOriginalConnectedChannelInfo {#conversationsekmlistoriginalconnectedchannelinfo}

```
listOriginalConnectedChannelInfo: Method<AdminConversationsEKMListOriginalConnectedChannelInfoArguments, AdminConversationsEkmListOriginalConnectedChannelInfoResponse>;
```

###### Description {#description-28}

List all disconnected channels — i.e., channels that were once connected to other workspaces and then disconnected — and the corresponding original channel IDs for key revocation with EKM.

###### See {#see-28}

[\`admin.conversations.ekm.listOriginalConnectedChannelInfo\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.ekm.listOriginalConnectedChannelInfo).

##### conversations.getConversationPrefs {#conversationsgetconversationprefs}

```
getConversationPrefs: MethodWithRequiredArgument<AdminConversationsGetConversationPrefsArguments, AdminConversationsGetConversationPrefsResponse>;
```

###### Description {#description-29}

Get conversation preferences for a public or private channel.

###### See {#see-29}

[\`admin.conversations.getConversationPrefs\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.getConversationPrefs).

##### conversations.getCustomRetention {#conversationsgetcustomretention}

```
getCustomRetention: MethodWithRequiredArgument<AdminConversationsGetCustomRetentionArguments, AdminConversationsGetCustomRetentionResponse>;
```

###### Description {#description-30}

Get a conversation's retention policy.

###### See {#see-30}

[\`admin.conversations.getCustomRetention\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.getCustomRetention).

##### conversations.getTeams {#conversationsgetteams}

```
getTeams: MethodWithRequiredArgument<AdminConversationsGetTeamsArguments, AdminConversationsGetTeamsResponse>;
```

###### Description {#description-31}

Get all the workspaces a given public or private channel is connected to within this Enterprise org.

###### See {#see-31}

[\`admin.conversations.getTeams\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.getTeams).

##### conversations.invite {#conversationsinvite}

```
invite: MethodWithRequiredArgument<AdminConversationsInviteArguments, AdminConversationsInviteResponse>;
```

###### Description {#description-32}

Invite a user to a public or private channel.

###### See {#see-32}

[\`admin.conversations.invite\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.invite).

##### conversations.lookup {#conversationslookup}

```
lookup: MethodWithRequiredArgument<AdminConversationsLookupArguments, AdminConversationsLookupResponse>;
```

###### Description {#description-33}

Returns channels on the given team using the filters.

###### See {#see-33}

[\`admin.conversations.lookup\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.lookup).

##### conversations.removeCustomRetention {#conversationsremovecustomretention}

```
removeCustomRetention: MethodWithRequiredArgument<AdminConversationsRemoveCustomRetentionArguments, AdminConversationsRemoveCustomRetentionResponse>;
```

###### Description {#description-34}

Remove a conversation's retention policy.

###### See {#see-34}

[\`admin.conversations.removeCustomRetention\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.removeCustomRetention).

##### conversations.rename {#conversationsrename}

```
rename: MethodWithRequiredArgument<AdminConversationsRenameArguments, AdminConversationsRenameResponse>;
```

###### Description {#description-35}

Rename a public or private channel.

###### See {#see-35}

[\`admin.conversations.rename\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.rename).

##### conversations.restrictAccess {#conversationsrestrictaccess}

```
restrictAccess: object;
```

##### conversations.restrictAccess.addGroup {#conversationsrestrictaccessaddgroup}

```
addGroup: MethodWithRequiredArgument<AdminConversationsRestrictAccessAddGroupArguments, AdminConversationsRestrictAccessAddGroupResponse>;
```

###### Description {#description-36}

Add an allowlist of IDP groups for accessing a channel.

###### See {#see-36}

[\`admin.conversations.restrictAccess.addGroup\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.restrictAccess.addGroup).

##### conversations.restrictAccess.listGroups {#conversationsrestrictaccesslistgroups}

```
listGroups: MethodWithRequiredArgument<AdminConversationsRestrictAccessListGroupsArguments, AdminConversationsRestrictAccessListGroupsResponse>;
```

###### Description {#description-37}

List all IDP Groups linked to a channel.

###### See {#see-37}

[\`admin.conversations.restrictAccess.listGroups\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.restrictAccess.listGroups).

##### conversations.restrictAccess.removeGroup {#conversationsrestrictaccessremovegroup}

```
removeGroup: MethodWithRequiredArgument<AdminConversationsRestrictAccessRemoveGroupArguments, AdminConversationsRestrictAccessRemoveGroupResponse>;
```

###### Description {#description-38}

Remove a linked IDP group linked from a private channel.

###### See {#see-38}

[\`admin.conversations.restrictAccess.removeGroup\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.restrictAccess.removeGroup).

##### conversations.search {#conversationssearch}

```
search: Method<AdminConversationsSearchArguments, AdminConversationsSearchResponse>;
```

###### Description {#description-39}

Search for public or private channels in an Enterprise organization.

###### See {#see-39}

[\`admin.conversations.search\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.search).

##### conversations.setConversationPrefs {#conversationssetconversationprefs}

```
setConversationPrefs: MethodWithRequiredArgument<AdminConversationsSetConversationPrefsArguments, AdminConversationsSetConversationPrefsResponse>;
```

###### Description {#description-40}

Set the posting permissions for a public or private channel.

###### See {#see-40}

[\`admin.conversations.setConversationPrefs\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.setConversationPrefs).

##### conversations.setCustomRetention {#conversationssetcustomretention}

```
setCustomRetention: MethodWithRequiredArgument<AdminConversationsSetCustomRetentionArguments, AdminConversationsSetCustomRetentionResponse>;
```

###### Description {#description-41}

Set a conversation's retention policy.

###### See {#see-41}

[\`admin.conversations.setCustomRetention\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.setCustomRetention).

##### conversations.setTeams {#conversationssetteams}

```
setTeams: MethodWithRequiredArgument<AdminConversationsSetTeamsArguments, AdminConversationsSetTeamsResponse>;
```

###### Description {#description-42}

Set the workspaces in an Enterprise grid org that connect to a public or private channel.

###### See {#see-42}

[\`admin.conversations.setTeams\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.setTeams).

##### conversations.unarchive {#conversationsunarchive}

```
unarchive: MethodWithRequiredArgument<AdminConversationsUnarchiveArguments, AdminConversationsUnarchiveResponse>;
```

###### Description {#description-43}

Unarchive a public or private channel.

###### See {#see-43}

[\`admin.conversations.unarchive\` API reference](https://docs.slack.dev/reference/methods/admin.conversations.unarchive).

#### emoji {#emoji}

```
emoji: object;
```

##### emoji.add {#emojiadd}

```
add: MethodWithRequiredArgument<AdminEmojiAddArguments, AdminEmojiAddResponse>;
```

###### Description {#description-44}

Add an emoji.

###### See {#see-44}

[\`admin.emoji.add\` API reference](https://docs.slack.dev/reference/methods/admin.emoji.add).

##### emoji.addAlias {#emojiaddalias}

```
addAlias: MethodWithRequiredArgument<AdminEmojiAddAliasArguments, AdminEmojiAddAliasResponse>;
```

###### Description {#description-45}

Add an emoji alias.

###### See {#see-45}

[\`admin.emoji.addAlias\` API reference](https://docs.slack.dev/reference/methods/admin.emoji.addAlias).

##### emoji.list {#emojilist}

```
list: Method<AdminEmojiListArguments, AdminEmojiListResponse>;
```

###### Description {#description-46}

List emoji for an Enterprise Grid organization.

###### See {#see-46}

[\`admin.emoji.list\` API reference](https://docs.slack.dev/reference/methods/admin.emoji.list).

##### emoji.remove {#emojiremove}

```
remove: MethodWithRequiredArgument<AdminEmojiRemoveArguments, AdminEmojiRemoveResponse>;
```

###### Description {#description-47}

Remove an emoji across an Enterprise Grid organization.

###### See {#see-47}

[\`admin.emoji.remove\` API reference](https://docs.slack.dev/reference/methods/admin.emoji.remove).

##### emoji.rename {#emojirename}

```
rename: MethodWithRequiredArgument<AdminEmojiRenameArguments, AdminEmojiRenameResponse>;
```

###### Description {#description-48}

Rename an emoji.

###### See {#see-48}

[\`admin.emoji.rename\` API reference](https://docs.slack.dev/reference/methods/admin.emoji.rename).

#### functions {#functions}

```
functions: object;
```

##### functions.list {#functionslist}

```
list: MethodWithRequiredArgument<AdminFunctionsListArguments, AdminFunctionsListResponse>;
```

###### Description {#description-49}

Look up functions by a set of apps.

###### See {#see-49}

[\`admin.functions.list\` API reference](https://docs.slack.dev/reference/methods/admin.functions.list).

##### functions.permissions {#functionspermissions}

```
permissions: object;
```

##### functions.permissions.lookup {#functionspermissionslookup}

```
lookup: MethodWithRequiredArgument<AdminFunctionsPermissionsLookupArguments, AdminFunctionsPermissionsLookupResponse>;
```

###### Description {#description-50}

Lookup the visibility of multiple Slack functions and include the users if it is limited to particular named entities.

###### See {#see-50}

[\`admin.functions.permissions.lookup\` API reference](https://docs.slack.dev/reference/methods/admin.functions.permissions.lookup).

##### functions.permissions.set {#functionspermissionsset}

```
set: MethodWithRequiredArgument<AdminFunctionsPermissionsSetArguments, AdminFunctionsPermissionsSetResponse>;
```

###### Description {#description-51}

Set the visibility of a Slack function and define the users or workspaces if it is set to named\_entities.

###### See {#see-51}

[\`admin.functions.permissions.set\` API reference](https://docs.slack.dev/reference/methods/admin.functions.permissions.set).

#### inviteRequests {#inviterequests}

```
inviteRequests: object;
```

##### inviteRequests.approve {#inviterequestsapprove}

```
approve: MethodWithRequiredArgument<AdminInviteRequestsApproveArguments, AdminInviteRequestsApproveResponse>;
```

###### Description {#description-52}

Approve a workspace invite request.

###### See {#see-52}

[\`admin.inviteRequests.approve\` API reference](https://docs.slack.dev/reference/methods/admin.inviteRequests.approve).

##### inviteRequests.approved {#inviterequestsapproved}

```
approved: object;
```

##### inviteRequests.approved.list {#inviterequestsapprovedlist}

```
list: MethodWithRequiredArgument<AdminInviteRequestsApprovedListArguments, AdminInviteRequestsApprovedListResponse>;
```

###### Description {#description-53}

List all approved workspace invite requests.

###### See {#see-53}

[\`admin.inviteRequests.approved.list\` API reference](https://docs.slack.dev/reference/methods/admin.inviteRequests.approved.list).

##### inviteRequests.denied {#inviterequestsdenied}

```
denied: object;
```

##### inviteRequests.denied.list {#inviterequestsdeniedlist}

```
list: MethodWithRequiredArgument<AdminInviteRequestsDeniedListArguments, AdminInviteRequestsDeniedListResponse>;
```

###### Description {#description-54}

List all denied workspace invite requests.

###### See {#see-54}

[\`admin.inviteRequests.denied.list\` API reference](https://docs.slack.dev/reference/methods/admin.inviteRequests.denied.list).

##### inviteRequests.deny {#inviterequestsdeny}

```
deny: MethodWithRequiredArgument<AdminInviteRequestsDenyArguments, AdminInviteRequestsDenyResponse>;
```

###### Description {#description-55}

Deny a workspace invite request.

###### See {#see-55}

[\`admin.inviteRequests.deny\` API reference](https://docs.slack.dev/reference/methods/admin.inviteRequests.deny).

##### inviteRequests.list {#inviterequestslist}

```
list: MethodWithRequiredArgument<AdminInviteRequestsListArguments, AdminInviteRequestsListResponse>;
```

###### Description {#description-56}

List all pending workspace invite requests.

###### See {#see-56}

[\`admin.inviteRequests.list\` API reference](https://docs.slack.dev/reference/methods/admin.inviteRequests.list).

#### roles {#roles}

```
roles: object;
```

##### roles.addAssignments {#rolesaddassignments}

```
addAssignments: MethodWithRequiredArgument<AdminRolesAddAssignmentsArguments, AdminRolesAddAssignmentsResponse>;
```

###### Description {#description-57}

Adds members to the specified role with the specified scopes.

###### See {#see-57}

[\`admin.roles.addAssignments\` API reference](https://docs.slack.dev/reference/methods/admin.roles.addAssignments).

##### roles.listAssignments {#roleslistassignments}

```
listAssignments: Method<AdminRolesListAssignmentsArguments, AdminRolesListAssignmentsResponse>;
```

###### Description {#description-58}

Lists assignments for all roles across entities. Options to scope results by any combination of roles or entities.

###### See {#see-58}

[\`admin.roles.listAssignments\` API reference](https://docs.slack.dev/reference/methods/admin.roles.listAssignments).

##### roles.removeAssignments {#rolesremoveassignments}

```
removeAssignments: MethodWithRequiredArgument<AdminRolesRemoveAssignmentsArguments, AdminRolesRemoveAssignmentsResponse>;
```

###### Description {#description-59}

Removes a set of users from a role for the given scopes and entities.

###### See {#see-59}

[\`admin.roles.removeAssignments\` API reference](https://docs.slack.dev/reference/methods/admin.roles.removeAssignments).

#### teams {#teams}

```
teams: object;
```

##### teams.admins {#teamsadmins}

```
admins: object;
```

##### teams.admins.list {#teamsadminslist}

```
list: MethodWithRequiredArgument<AdminTeamsAdminsListArguments, AdminTeamsAdminsListResponse>;
```

###### Description {#description-60}

List all of the admins on a given workspace.

###### See {#see-60}

[\`admin.teams.admins.list\` API reference](https://docs.slack.dev/reference/methods/admin.teams.admins.list).

##### teams.create {#teamscreate}

```
create: MethodWithRequiredArgument<AdminTeamsCreateArguments, AdminTeamsCreateResponse>;
```

###### Description {#description-61}

Create an Enterprise team.

###### See {#see-61}

[\`admin.teams.create\` API reference](https://docs.slack.dev/reference/methods/admin.teams.create).

##### teams.list {#teamslist}

```
list: Method<AdminTeamsListArguments, AdminTeamsListResponse>;
```

###### Description {#description-62}

List all teams on an Enterprise organization.

###### See {#see-62}

[\`admin.teams.list\` API reference](https://docs.slack.dev/reference/methods/admin.teams.list).

##### teams.owners {#teamsowners}

```
owners: object;
```

##### teams.owners.list {#teamsownerslist}

```
list: MethodWithRequiredArgument<AdminTeamsOwnersListArguments, AdminTeamsOwnersListResponse>;
```

###### Description {#description-63}

List all of the owners on a given workspace.

###### See {#see-63}

[\`admin.teams.owners.list\` API reference](https://docs.slack.dev/reference/methods/admin.teams.owners.list).

##### teams.settings {#teamssettings}

```
settings: object;
```

##### teams.settings.info {#teamssettingsinfo}

```
info: MethodWithRequiredArgument<AdminTeamsSettingsInfoArguments, AdminTeamsSettingsInfoResponse>;
```

###### Description {#description-64}

Fetch information about settings in a workspace.

###### See {#see-64}

[\`admin.teams.settings.info\` API reference](https://docs.slack.dev/reference/methods/admin.teams.settings.info).

##### teams.settings.setDefaultChannels {#teamssettingssetdefaultchannels}

```
setDefaultChannels: MethodWithRequiredArgument<AdminTeamsSettingsSetDefaultChannelsArguments, AdminTeamsSettingsSetDefaultChannelsResponse>;
```

###### Description {#description-65}

Set the default channels of a workspace.

###### See {#see-65}

[\`admin.teams.settings.setDefaultChannels\` API reference](https://docs.slack.dev/reference/methods/admin.teams.settings.setDefaultChannels).

##### teams.settings.setDescription {#teamssettingssetdescription}

```
setDescription: MethodWithRequiredArgument<AdminTeamsSettingsSetDescriptionArguments, AdminTeamsSettingsSetDescriptionResponse>;
```

###### Description {#description-66}

Set the description of a given workspace.

###### See {#see-66}

[\`admin.teams.settings.setDescription\` API reference](https://docs.slack.dev/reference/methods/admin.teams.settings.setDescription).

##### teams.settings.setDiscoverability {#teamssettingssetdiscoverability}

```
setDiscoverability: MethodWithRequiredArgument<AdminTeamsSettingsSetDiscoverabilityArguments, AdminTeamsSettingsSetDiscoverabilityResponse>;
```

###### Description {#description-67}

Set the discoverability of a given workspace.

###### See {#see-67}

[\`admin.teams.settings.setDiscoverability\` API reference](https://docs.slack.dev/reference/methods/admin.teams.settings.setDiscoverability).

##### teams.settings.setIcon {#teamssettingsseticon}

```
setIcon: MethodWithRequiredArgument<AdminTeamsSettingsSetIconArguments, AdminTeamsSettingsSetIconResponse>;
```

###### Description {#description-68}

Sets the icon of a workspace.

###### See {#see-68}

[\`admin.teams.settings.setIcon\` API reference](https://docs.slack.dev/reference/methods/admin.teams.settings.setIcon).

##### teams.settings.setName {#teamssettingssetname}

```
setName: MethodWithRequiredArgument<AdminTeamsSettingsSetNameArguments, AdminTeamsSettingsSetNameResponse>;
```

###### Description {#description-69}

Set the name of a given workspace.

###### See {#see-69}

[\`admin.teams.settings.setName\` API reference](https://docs.slack.dev/reference/methods/admin.teams.settings.setName).

#### usergroups {#usergroups}

```
usergroups: object;
```

##### usergroups.addChannels {#usergroupsaddchannels}

```
addChannels: MethodWithRequiredArgument<AdminUsergroupsAddChannelsArguments, AdminUsergroupsAddChannelsResponse>;
```

###### Description {#description-70}

Add up to one hundred default channels to an IDP group.

###### See {#see-70}

[\`admin.teams.usergroups.addChannels\` API reference](https://docs.slack.dev/reference/methods/admin.usergroups.addChannels).

##### usergroups.addTeams {#usergroupsaddteams}

```
addTeams: MethodWithRequiredArgument<AdminUsergroupsAddTeamsArguments, AdminUsergroupsAddTeamsResponse>;
```

###### Description {#description-71}

Associate one or more default workspaces with an organization-wide IDP group.

###### See {#see-71}

[\`admin.teams.usergroups.addTeams\` API reference](https://docs.slack.dev/reference/methods/admin.usergroups.addTeams).

##### usergroups.listChannels {#usergroupslistchannels}

```
listChannels: MethodWithRequiredArgument<AdminUsergroupsListChannelsArguments, AdminUsergroupsListChannelsResponse>;
```

###### Description {#description-72}

List the channels linked to an org-level IDP group (user group).

###### See {#see-72}

[\`admin.teams.usergroups.listChannels\` API reference](https://docs.slack.dev/reference/methods/admin.usergroups.listChannels).

##### usergroups.removeChannels {#usergroupsremovechannels}

```
removeChannels: MethodWithRequiredArgument<AdminUsergroupsRemoveChannelsArguments, AdminUsergroupsRemoveChannelsResponse>;
```

###### Description {#description-73}

Remove one or more default channels from an org-level IDP group (user group).

###### See {#see-73}

[\`admin.teams.usergroups.removeChannels\` API reference](https://docs.slack.dev/reference/methods/admin.usergroups.removeChannels).

#### users {#users}

```
users: object;
```

##### users.assign {#usersassign}

```
assign: MethodWithRequiredArgument<AdminUsersAssignArguments, AdminUsersAssignResponse>;
```

###### Description {#description-74}

Add an Enterprise user to a workspace.

###### See {#see-74}

[\`admin.users.assign\` API reference](https://docs.slack.dev/reference/methods/admin.users.assign).

##### users.invite {#usersinvite}

```
invite: MethodWithRequiredArgument<AdminUsersInviteArguments, AdminUsersInviteResponse>;
```

###### Description {#description-75}

Invite a user to a workspace.

###### See {#see-75}

[\`admin.users.invite\` API reference](https://docs.slack.dev/reference/methods/admin.users.invite).

##### users.list {#userslist}

```
list: Method<AdminUsersListArguments, AdminUsersListResponse>;
```

###### Description {#description-76}

List users on a workspace.

###### See {#see-76}

[\`admin.users.list\` API reference](https://docs.slack.dev/reference/methods/admin.users.list).

##### users.remove {#usersremove}

```
remove: MethodWithRequiredArgument<AdminUsersRemoveArguments, AdminUsersRemoveResponse>;
```

###### Description {#description-77}

Remove a user from a workspace.

###### See {#see-77}

[\`admin.users.remove\` API reference](https://docs.slack.dev/reference/methods/admin.users.remove).

##### users.session {#userssession}

```
session: object;
```

##### users.session.clearSettings {#userssessionclearsettings}

```
clearSettings: MethodWithRequiredArgument<AdminUsersSessionClearSettingsArguments, AdminUsersSessionClearSettingsResponse>;
```

###### Description {#description-78}

Clear user-specific session settings—the session duration and what happens when the client closes—for a list of users.

###### See {#see-78}

[\`admin.users.session.clearSettings\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.clearSettings).

##### users.session.getSettings {#userssessiongetsettings}

```
getSettings: MethodWithRequiredArgument<AdminUsersSessionGetSettingsArguments, AdminUsersSessionGetSettingsResponse>;
```

###### Description {#description-79}

Get user-specific session settings—the session duration and what happens when the client closes—given a list of users.

###### See {#see-79}

[\`admin.users.session.getSettings\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.getSettings).

##### users.session.invalidate {#userssessioninvalidate}

```
invalidate: MethodWithRequiredArgument<AdminUsersSessionInvalidateArguments, AdminUsersSessionInvalidateResponse>;
```

###### Description {#description-80}

Revoke a single session for a user. The user will be forced to login to Slack.

###### See {#see-80}

[\`admin.users.session.invalidate\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.invalidate).

##### users.session.list {#userssessionlist}

```
list: Method<AdminUsersSessionListArguments, AdminUsersSessionListResponse>;
```

###### Description {#description-81}

List active user sessions for an organization.

###### See {#see-81}

[\`admin.users.session.list\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.list).

##### users.session.reset {#userssessionreset}

```
reset: MethodWithRequiredArgument<AdminUsersSessionResetArguments, AdminUsersSessionResetResponse>;
```

###### Description {#description-82}

Wipes all valid sessions on all devices for a given user.

###### See {#see-82}

[\`admin.users.session.reset\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.reset).

##### users.session.resetBulk {#userssessionresetbulk}

```
resetBulk: MethodWithRequiredArgument<AdminUsersSessionResetBulkArguments, AdminUsersSessionResetBulkResponse>;
```

###### Description {#description-83}

Enqueues an asynchronous job to wipe all valid sessions on all devices for a given user list.

###### See {#see-83}

[\`admin.users.session.resetBulk\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.resetBulk).

##### users.session.setSettings {#userssessionsetsettings}

```
setSettings: MethodWithRequiredArgument<AdminUsersSessionSetSettingsArguments, AdminUsersSessionSetSettingsResponse>;
```

###### Description {#description-84}

Configure the user-level session settings—the session duration and what happens when the client closes—for one or more users.

###### See {#see-84}

[\`admin.users.session.setSettings\` API reference](https://docs.slack.dev/reference/methods/admin.users.session.setSettings).

##### users.setAdmin {#userssetadmin}

```
setAdmin: MethodWithRequiredArgument<AdminUsersSetAdminArguments, AdminUsersSetAdminResponse>;
```

###### Description {#description-85}

Set an existing guest, regular user, or owner to be an admin user.

###### See {#see-85}

[\`admin.users.setAdmin\` API reference](https://docs.slack.dev/reference/methods/admin.users.setAdmin).

##### users.setExpiration {#userssetexpiration}

```
setExpiration: MethodWithRequiredArgument<AdminUsersSetExpirationArguments, AdminUsersSetExpirationResponse>;
```

###### Description {#description-86}

Set an expiration for a guest user.

###### See {#see-86}

[\`admin.users.setExpiration\` API reference](https://docs.slack.dev/reference/methods/admin.users.setExpiration).

##### users.setOwner {#userssetowner}

```
setOwner: MethodWithRequiredArgument<AdminUsersSetOwnerArguments, AdminUsersSetOwnerResponse>;
```

###### Description {#description-87}

Set an existing guest, regular user, or admin user to be a workspace owner.

###### See {#see-87}

[\`admin.users.setOwner\` API reference](https://docs.slack.dev/reference/methods/admin.users.setOwner).

##### users.setRegular {#userssetregular}

```
setRegular: MethodWithRequiredArgument<AdminUsersSetRegularArguments, AdminUsersSetRegularResponse>;
```

###### Description {#description-88}

Set an existing guest user, admin user, or owner to be a regular user.

###### See {#see-88}

[\`admin.users.setRegular\` API reference](https://docs.slack.dev/reference/methods/admin.users.setRegular).

##### users.unsupportedVersions {#usersunsupportedversions}

```
unsupportedVersions: object;
```

##### users.unsupportedVersions.export {#usersunsupportedversionsexport}

```
export: MethodWithRequiredArgument<AdminUsersUnsupportedVersionsExportArguments, AdminUsersUnsupportedVersionsExportResponse>;
```

###### Description {#description-89}

Ask Slackbot to send you an export listing all workspace members using unsupported software, presented as a zipped CSV file.

###### See {#see-89}

[\`admin.users.unsupportedVersions.export\` API reference](https://docs.slack.dev/reference/methods/admin.users.unsupportedVersions.export).

#### workflows {#workflows}

```
workflows: object;
```

##### workflows.collaborators {#workflowscollaborators}

```
collaborators: object;
```

##### workflows.collaborators.add {#workflowscollaboratorsadd}

```
add: MethodWithRequiredArgument<AdminWorkflowsCollaboratorsAddArguments, AdminWorkflowsCollaboratorsAddResponse>;
```

###### Description {#description-90}

Add collaborators to workflows within the team or enterprise.

###### See {#see-90}

[\`admin.workflows.collaborators.add\` API reference](https://docs.slack.dev/reference/methods/admin.workflows.collaborators.add).

##### workflows.collaborators.remove {#workflowscollaboratorsremove}

```
remove: MethodWithRequiredArgument<AdminWorkflowsCollaboratorsRemoveArguments, AdminWorkflowsCollaboratorsRemoveResponse>;
```

###### Description {#description-91}

Remove collaborators from workflows within the team or enterprise.

###### See {#see-91}

[\`admin.workflows.collaborators.remove\` API reference](https://docs.slack.dev/reference/methods/admin.workflows.collaborators.remove).

##### workflows.permissions {#workflowspermissions}

```
permissions: object;
```

##### workflows.permissions.lookup {#workflowspermissionslookup}

```
lookup: MethodWithRequiredArgument<AdminWorkflowsPermissionsLookupArguments, AdminWorkflowsPermissionsLookupResponse>;
```

###### Description {#description-92}

Look up the permissions for a set of workflows.

###### See {#see-92}

[\`admin.workflows.permissions.lookup\` API reference](https://docs.slack.dev/reference/methods/admin.workflows.permissions.lookup).

##### workflows.search {#workflowssearch}

```
search: Method<AdminWorkflowsSearchArguments, AdminWorkflowsSearchResponse>;
```

###### Description {#description-93}

Search workflows within the team or enterprise.

###### See {#see-93}

[\`admin.workflows.search\` API reference](https://docs.slack.dev/reference/methods/admin.workflows.search).

##### workflows.unpublish {#workflowsunpublish}

```
unpublish: MethodWithRequiredArgument<AdminWorkflowsUnpublishArguments, AdminWorkflowsUnpublishResponse>;
```

###### Description {#description-94}

Unpublish workflows within the team or enterprise.

###### See {#see-94}

[\`admin.workflows.unpublish\` API reference](https://docs.slack.dev/reference/methods/admin.workflows.unpublish).

#### Inherited from {#inherited-from}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`admin`](/tools/node-slack-sdk/reference/web-api/classes/Methods#admin)

* * *

### api {#api}

```
readonly api: object;
```

Defined in: [packages/web-api/src/methods.ts:1377](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1377)

#### test {#test}

```
test: Method<APITestArguments, ApiTestResponse>;
```

##### Description {#description-95}

Checks API calling code.

##### See {#see-95}

[\`api.test\` API reference](https://docs.slack.dev/reference/methods/api.test).

#### Inherited from {#inherited-from-1}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`api`](/tools/node-slack-sdk/reference/web-api/classes/Methods#api)

* * *

### apps {#apps-1}

```
readonly apps: object;
```

Defined in: [packages/web-api/src/methods.ts:1414](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1414)

#### connections {#connections}

```
connections: object;
```

##### connections.open {#connectionsopen}

```
open: Method<AppsConnectionsOpenArguments, AppsConnectionsOpenResponse>;
```

###### Description {#description-96}

Generate a temporary Socket Mode WebSocket URL that your app can connect to in order to receive events and interactive payloads over.

###### See {#see-96}

[\`apps.connections.open\` API reference](https://docs.slack.dev/reference/methods/apps.connections.open).

#### event {#event}

```
event: object;
```

##### event.authorizations {#eventauthorizations}

```
authorizations: object;
```

##### event.authorizations.list {#eventauthorizationslist}

```
list: MethodWithRequiredArgument<AppsEventAuthorizationsListArguments, AppsEventAuthorizationsListResponse>;
```

###### Description {#description-97}

Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

###### See {#see-97}

[\`apps.event.authorizations.list\` API reference](https://docs.slack.dev/reference/methods/apps.event.authorizations.list).

#### manifest {#manifest}

```
manifest: object;
```

##### manifest.create {#manifestcreate}

```
create: MethodWithRequiredArgument<AppsManifestCreateArguments, AppsManifestCreateResponse>;
```

###### Description {#description-98}

Create an app from an app manifest.

###### See {#see-98}

[\`apps.manifest.create\` API reference](https://docs.slack.dev/reference/methods/apps.manifest.create).

##### manifest.delete {#manifestdelete}

```
delete: MethodWithRequiredArgument<AppsManifestDeleteArguments, AppsManifestDeleteResponse>;
```

###### Description {#description-99}

Permanently deletes an app created through app manifests.

###### See {#see-99}

[\`apps.manifest.delete\` API reference](https://docs.slack.dev/reference/methods/apps.manifest.delete).

##### manifest.export {#manifestexport}

```
export: MethodWithRequiredArgument<AppsManifestExportArguments, AppsManifestExportResponse>;
```

###### Description {#description-100}

Export an app manifest from an existing app.

###### See {#see-100}

[\`apps.manifest.export\` API reference](https://docs.slack.dev/reference/methods/apps.manifest.export).

##### manifest.update {#manifestupdate}

```
update: MethodWithRequiredArgument<AppsManifestUpdateArguments, AppsManifestUpdateResponse>;
```

###### Description {#description-101}

Update an app from an app manifest.

###### See {#see-101}

[\`apps.manifest.update\` API reference](https://docs.slack.dev/reference/methods/apps.manifest.update).

##### manifest.validate {#manifestvalidate}

```
validate: MethodWithRequiredArgument<AppsManifestValidateArguments, AppsManifestValidateResponse>;
```

###### Description {#description-102}

Validate an app manifest.

###### See {#see-102}

[\`apps.manifest.validate\` API reference](https://docs.slack.dev/reference/methods/apps.manifest.validate).

#### uninstall {#uninstall}

```
uninstall: MethodWithRequiredArgument<AppsUninstallArguments, AppsUninstallResponse>;
```

##### Description {#description-103}

Uninstalls your app from a workspace.

##### See {#see-103}

[\`apps.uninstall\` API reference](https://docs.slack.dev/reference/methods/apps.uninstall).

#### user {#user}

```
user: object;
```

##### user.connection {#userconnection}

```
connection: object;
```

##### user.connection.update {#userconnectionupdate}

```
update: MethodWithRequiredArgument<AppsUserConnectionUpdateArguments, AppsUserConnectionUpdateResponse>;
```

###### Description {#description-104}

Updates the connection status between a user and an app.

###### See {#see-104}

[\`apps.user.connection.update\` API reference](https://docs.slack.dev/reference/methods/apps.user.connection.update).

#### Inherited from {#inherited-from-2}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`apps`](/tools/node-slack-sdk/reference/web-api/classes/Methods#apps)

* * *

### assistant {#assistant}

```
readonly assistant: object;
```

Defined in: [packages/web-api/src/methods.ts:1385](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1385)

#### threads {#threads}

```
threads: object;
```

##### threads.setStatus {#threadssetstatus}

```
setStatus: MethodWithRequiredArgument<AssistantThreadsSetStatusArguments, AssistantThreadsSetStatusResponse>;
```

###### Description {#description-105}

Set loading status to indicate that the app is building a response.

###### See {#see-105}

[\`assistant.threads.setStatus\` API reference](https://docs.slack.dev/reference/methods/assistant.threads.setStatus).

##### threads.setSuggestedPrompts {#threadssetsuggestedprompts}

```
setSuggestedPrompts: MethodWithRequiredArgument<AssistantThreadsSetSuggestedPromptsArguments, AssistantThreadsSetSuggestedPromptsResponse>;
```

###### Description {#description-106}

Set suggested prompts for the user. Can suggest up to four prompts.

###### See {#see-106}

[\`assistant.threads.setSuggestedPrompts\` API reference](https://docs.slack.dev/reference/methods/assistant.threads.setSuggestedPrompts).

##### threads.setTitle {#threadssettitle}

```
setTitle: MethodWithRequiredArgument<AssistantThreadsSetTitleArguments, AssistantThreadsSetTitleResponse>;
```

###### Description {#description-107}

Set the title of the thread. This is shown when a user views the app's chat history.

###### See {#see-107}

[\`assistant.threads.setTitle\` API reference](https://docs.slack.dev/reference/methods/assistant.threads.setTitle).

#### Inherited from {#inherited-from-3}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`assistant`](/tools/node-slack-sdk/reference/web-api/classes/Methods#assistant)

* * *

### auth {#auth-1}

```
readonly auth: object;
```

Defined in: [packages/web-api/src/methods.ts:1488](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1488)

#### revoke {#revoke}

```
revoke: Method<AuthRevokeArguments, AuthRevokeResponse>;
```

##### Description {#description-108}

Revokes a token.

##### See {#see-108}

[\`auth.revoke\` API reference](https://docs.slack.dev/reference/methods/auth.revoke).

#### teams {#teams-1}

```
teams: object;
```

##### teams.list {#teamslist-1}

```
list: Method<AuthTeamsListArguments, AuthTeamsListResponse>;
```

###### Description {#description-109}

Obtain a full list of workspaces your org-wide app has been approved for.

###### See {#see-109}

[\`auth.teams.list\` API reference](https://docs.slack.dev/reference/methods/auth.teams.list).

#### test {#test-1}

```
test: Method<AuthTestArguments, AuthTestResponse>;
```

#### Inherited from {#inherited-from-4}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`auth`](/tools/node-slack-sdk/reference/web-api/classes/Methods#auth)

* * *

### bookmarks {#bookmarks}

```
readonly bookmarks: object;
```

Defined in: [packages/web-api/src/methods.ts:1504](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1504)

#### add {#add}

```
add: MethodWithRequiredArgument<BookmarksAddArguments, BookmarksAddResponse>;
```

##### Description {#description-110}

Add bookmark to a channel.

##### See {#see-110}

[\`bookmarks.add\` API reference](https://docs.slack.dev/reference/methods/bookmarks.add).

#### edit {#edit}

```
edit: MethodWithRequiredArgument<BookmarksEditArguments, BookmarksEditResponse>;
```

##### Description {#description-111}

Edit bookmark.

##### See {#see-111}

[\`bookmarks.edit\` API reference](https://docs.slack.dev/reference/methods/bookmarks.edit).

#### list {#list}

```
list: MethodWithRequiredArgument<BookmarksListArguments, BookmarksListResponse>;
```

##### Description {#description-112}

List bookmarks for a channel.

##### See {#see-112}

[\`bookmarks.list\` API reference](https://docs.slack.dev/reference/methods/bookmarks.list).

#### remove {#remove}

```
remove: MethodWithRequiredArgument<BookmarksRemoveArguments, BookmarksRemoveResponse>;
```

##### Description {#description-113}

Remove bookmark from a channel.

##### See {#see-113}

[\`bookmarks.remove\` API reference](https://docs.slack.dev/reference/methods/bookmarks.remove).

#### Inherited from {#inherited-from-5}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`bookmarks`](/tools/node-slack-sdk/reference/web-api/classes/Methods#bookmarks)

* * *

### bots {#bots}

```
readonly bots: object;
```

Defined in: [packages/web-api/src/methods.ts:1527](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1527)

#### info {#info}

```
info: Method<BotsInfoArguments, BotsInfoResponse>;
```

##### Description {#description-114}

Gets information about a bot user.

##### See {#see-114}

[\`bots.info\` API reference](https://docs.slack.dev/reference/methods/bots.info).

#### Inherited from {#inherited-from-6}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`bots`](/tools/node-slack-sdk/reference/web-api/classes/Methods#bots)

* * *

### calls {#calls}

```
readonly calls: object;
```

Defined in: [packages/web-api/src/methods.ts:1535](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1535)

#### add {#add-1}

```
add: MethodWithRequiredArgument<CallsAddArguments, CallsAddResponse>;
```

##### Description {#description-115}

Registers a new Call.

##### See {#see-115}

[\`calls.add\` API reference](https://docs.slack.dev/reference/methods/calls.add).

#### end {#end}

```
end: MethodWithRequiredArgument<CallsEndArguments, CallsEndResponse>;
```

##### Description {#description-116}

Ends a Call.

##### See {#see-116}

[\`calls.end\` API reference](https://docs.slack.dev/reference/methods/calls.end).

#### info {#info-1}

```
info: MethodWithRequiredArgument<CallsInfoArguments, CallsInfoResponse>;
```

##### Description {#description-117}

Returns information about a Call.

##### See {#see-117}

[\`calls.info\` API reference](https://docs.slack.dev/reference/methods/calls.info).

#### participants {#participants}

```
participants: object;
```

##### participants.add {#participantsadd}

```
add: MethodWithRequiredArgument<CallsParticipantsAddArguments, CallsParticipantsAddResponse>;
```

###### Description {#description-118}

Registers new participants added to a Call.

###### See {#see-118}

[\`calls.participants.add\` API reference](https://docs.slack.dev/reference/methods/calls.participants.add).

##### participants.remove {#participantsremove}

```
remove: MethodWithRequiredArgument<CallsParticipantsRemoveArguments, CallsParticipantsRemoveResponse>;
```

#### update {#update}

```
update: MethodWithRequiredArgument<CallsUpdateArguments, CallsUpdateResponse>;
```

##### Description {#description-119}

Updates information about a Call.

##### See {#see-119}

[\`calls.update\` API reference](https://docs.slack.dev/reference/methods/calls.update).

#### Inherited from {#inherited-from-7}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`calls`](/tools/node-slack-sdk/reference/web-api/classes/Methods#calls)

* * *

### canvases {#canvases}

```
readonly canvases: object;
```

Defined in: [packages/web-api/src/methods.ts:1569](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1569)

#### access {#access}

```
access: object;
```

##### access.delete {#accessdelete}

```
delete: MethodWithRequiredArgument<CanvasesAccessDeleteArguments, CanvasesAccessDeleteResponse>;
```

###### Description {#description-120}

Remove access to a canvas for specified entities.

###### See {#see-120}

[\`canvases.access.delete\` API reference](https://docs.slack.dev/reference/methods/canvases.access.delete).

##### access.set {#accessset}

```
set: MethodWithRequiredArgument<CanvasesAccessSetArguments, CanvasesAccessSetResponse>;
```

###### Description {#description-121}

Sets the access level to a canvas for specified entities.

###### See {#see-121}

[\`canvases.access.set\` API reference](https://docs.slack.dev/reference/methods/canvases.access.set).

#### create {#create}

```
create: Method<CanvasesCreateArguments, CanvasesCreateResponse>;
```

##### Description {#description-122}

Create Canvas for a user.

##### See {#see-122}

[\`canvases.create\` API reference](https://docs.slack.dev/reference/methods/canvases.create).

#### delete {#delete}

```
delete: MethodWithRequiredArgument<CanvasesDeleteArguments, CanvasesDeleteResponse>;
```

##### Description {#description-123}

Deletes a canvas.

##### See {#see-123}

[\`canvases.delete\` API reference](https://docs.slack.dev/reference/methods/canvases.delete).

#### edit {#edit-1}

```
edit: MethodWithRequiredArgument<CanvasesEditArguments, CanvasesEditResponse>;
```

##### Description {#description-124}

Update an existing canvas.

##### See {#see-124}

[\`canvases.edit\` API reference](https://docs.slack.dev/reference/methods/canvases.edit).

#### sections {#sections}

```
sections: object;
```

##### sections.lookup {#sectionslookup}

```
lookup: MethodWithRequiredArgument<CanvasesSectionsLookupArguments, CanvasesSectionsLookupResponse>;
```

###### Description {#description-125}

Find sections matching the provided criteria.

###### See {#see-125}

[\`canvases.sections.lookup\` API reference](https://docs.slack.dev/reference/methods/canvases.sections.lookup).

#### Inherited from {#inherited-from-8}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`canvases`](/tools/node-slack-sdk/reference/web-api/classes/Methods#canvases)

* * *

### chat {#chat}

```
readonly chat: object;
```

Defined in: [packages/web-api/src/methods.ts:1609](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1609)

#### appendStream {#appendstream}

```
appendStream: MethodWithRequiredArgument<ChatAppendStreamArguments, ChatAppendStreamResponse>;
```

##### Description {#description-126}

Appends text to an existing streaming conversation.

##### See {#see-126}

[\`chat.appendStream\` API reference](https://docs.slack.dev/reference/methods/chat.appendStream).

#### delete {#delete-1}

```
delete: MethodWithRequiredArgument<ChatDeleteArguments, ChatDeleteResponse>;
```

##### Description {#description-127}

Deletes a message.

##### See {#see-127}

[\`chat.delete\` API reference](https://docs.slack.dev/reference/methods/chat.delete).

#### deleteScheduledMessage {#deletescheduledmessage}

```
deleteScheduledMessage: MethodWithRequiredArgument<ChatDeleteScheduledMessageArguments, ChatDeleteScheduledMessageResponse>;
```

##### Description {#description-128}

Deletes a pending scheduled message from the queue.

##### See {#see-128}

[\`chat.deleteScheduledMessage\` API reference](https://docs.slack.dev/reference/methods/chat.deleteScheduledMessage).

#### getPermalink {#getpermalink}

```
getPermalink: MethodWithRequiredArgument<ChatGetPermalinkArguments, ChatGetPermalinkResponse>;
```

##### Description {#description-129}

Retrieve a permalink URL for a specific extant message.

##### See {#see-129}

[\`chat.getPermalink\` API reference](https://docs.slack.dev/reference/methods/chat.getPermalink).

#### meMessage {#memessage}

```
meMessage: MethodWithRequiredArgument<ChatMeMessageArguments, ChatMeMessageResponse>;
```

##### Description {#description-130}

Share a me message into a channel.

##### See {#see-130}

[\`chat.meMessage\` API reference](https://docs.slack.dev/reference/methods/chat.meMessage).

#### postEphemeral {#postephemeral}

```
postEphemeral: MethodWithRequiredArgument<ChatPostEphemeralArguments, ChatPostEphemeralResponse>;
```

##### Description {#description-131}

Sends an ephemeral message to a user in a channel.

##### See {#see-131}

[\`chat.postEphemeral\` API reference](https://docs.slack.dev/reference/methods/chat.postEphemeral).

#### postMessage {#postmessage}

```
postMessage: MethodWithRequiredArgument<ChatPostMessageArguments, ChatPostMessageResponse>;
```

##### Description {#description-132}

Sends a message to a channel.

##### See {#see-132}

[\`chat.postMessage\` API reference](https://docs.slack.dev/reference/methods/chat.postMessage).

#### scheduledMessages {#scheduledmessages}

```
scheduledMessages: object;
```

##### scheduledMessages.list {#scheduledmessageslist}

```
list: Method<ChatScheduledMessagesListArguments, ChatScheduledMessagesListResponse>;
```

###### Description {#description-133}

Returns a list of scheduled messages.

###### See {#see-133}

[\`chat.scheduledMessages.list\` API reference](https://docs.slack.dev/reference/methods/chat.scheduledMessages.list).

#### scheduleMessage {#schedulemessage}

```
scheduleMessage: MethodWithRequiredArgument<ChatScheduleMessageArguments, ChatScheduleMessageResponse>;
```

##### Description {#description-134}

Schedules a message to be sent to a channel.

##### See {#see-134}

[\`chat.scheduleMessage\` API reference](https://docs.slack.dev/reference/methods/chat.scheduleMessage).

#### startStream {#startstream}

```
startStream: MethodWithRequiredArgument<ChatStartStreamArguments, ChatStartStreamResponse>;
```

##### Description {#description-135}

Starts a new streaming conversation.

##### See {#see-135}

[\`chat.startStream\` API reference](https://docs.slack.dev/reference/methods/chat.startStream).

#### stopStream {#stopstream}

```
stopStream: MethodWithRequiredArgument<ChatStopStreamArguments, ChatStopStreamResponse>;
```

##### Description {#description-136}

Stops a streaming conversation.

##### See {#see-136}

[\`chat.stopStream\` API reference](https://docs.slack.dev/reference/methods/chat.stopStream).

#### unfurl {#unfurl}

```
unfurl: MethodWithRequiredArgument<ChatUnfurlArguments, ChatUnfurlResponse>;
```

##### Description {#description-137}

Provide custom unfurl behavior for user-posted URLs.

##### See {#see-137}

[\`chat.unfurl\` API reference](https://docs.slack.dev/reference/methods/chat.unfurl).

#### update {#update-1}

```
update: MethodWithRequiredArgument<ChatUpdateArguments, ChatUpdateResponse>;
```

##### Description {#description-138}

Updates a message.

##### See {#see-138}

[\`chat.update\` API reference](https://docs.slack.dev/reference/methods/chat.update).

#### Inherited from {#inherited-from-9}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`chat`](/tools/node-slack-sdk/reference/web-api/classes/Methods#chat)

* * *

### conversations {#conversations-1}

```
readonly conversations: object;
```

Defined in: [packages/web-api/src/methods.ts:1688](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1688)

#### acceptSharedInvite {#acceptsharedinvite}

```
acceptSharedInvite: MethodWithRequiredArgument<ConversationsAcceptSharedInviteArguments, ConversationsAcceptSharedInviteResponse>;
```

##### Description {#description-139}

Accepts an invitation to a Slack Connect channel.

##### See {#see-139}

[\`conversations.acceptSharedInvite\` API reference](https://docs.slack.dev/reference/methods/conversations.acceptSharedInvite).

#### approveSharedInvite {#approvesharedinvite}

```
approveSharedInvite: MethodWithRequiredArgument<ConversationsApproveSharedInviteArguments, ConversationsApproveSharedInviteResponse>;
```

##### Description {#description-140}

Approves an invitation to a Slack Connect channel.

##### See {#see-140}

[\`conversations.approveSharedInvite\` API reference](https://docs.slack.dev/reference/methods/conversations.approveSharedInvite).

#### archive {#archive}

```
archive: MethodWithRequiredArgument<ConversationsArchiveArguments, ConversationsArchiveResponse>;
```

##### Description {#description-141}

Archives a conversation.

##### See {#see-141}

[\`conversations.archive\` API reference](https://docs.slack.dev/reference/methods/conversations.archive).

#### canvases {#canvases-1}

```
canvases: object;
```

##### canvases.create {#canvasescreate}

```
create: MethodWithRequiredArgument<ConversationsCanvasesCreateArguments, ConversationsCanvasesCreateResponse>;
```

###### Description {#description-142}

Create a Channel Canvas for a channel.

###### See {#see-142}

[\`conversations.canvases.create\` API reference](https://docs.slack.dev/reference/methods/conversations.canvases.create).

#### close {#close}

```
close: MethodWithRequiredArgument<ConversationsCloseArguments, ConversationsCloseResponse>;
```

##### Description {#description-143}

Closes a direct message or multi-person direct message.

##### See {#see-143}

[\`conversations.close\` API reference](https://docs.slack.dev/reference/methods/conversations.close).

#### create {#create-1}

```
create: MethodWithRequiredArgument<ConversationsCreateArguments, ConversationsCreateResponse>;
```

##### Description {#description-144}

Initiates a public or private channel-based conversation.

##### See {#see-144}

[\`conversations.create\` API reference](https://docs.slack.dev/reference/methods/conversations.create).

#### declineSharedInvite {#declinesharedinvite}

```
declineSharedInvite: MethodWithRequiredArgument<ConversationsDeclineSharedInviteArguments, ConversationsDeclineSharedInviteResponse>;
```

##### Description {#description-145}

Declines an invitation to a Slack Connect channel.

##### See {#see-145}

[\`conversations.declineSharedInvite\` API reference](https://docs.slack.dev/reference/methods/conversations.declineSharedInvite).

#### externalInvitePermissions {#externalinvitepermissions}

```
externalInvitePermissions: object;
```

##### externalInvitePermissions.set {#externalinvitepermissionsset}

```
set: MethodWithRequiredArgument<ConversationsExternalInvitePermissionsSetArguments, ConversationsExternalInvitePermissionsSetResponse>;
```

###### Description {#description-146}

Convert a team in a shared channel from an External Limited channel to a fully shared Slack Connect channel or vice versa.

###### See {#see-146}

[\`conversations.externalInvitePermissions.set\` API reference](https://docs.slack.dev/reference/methods/conversations.externalInvitePermissions.set).

#### history {#history}

```
history: MethodWithRequiredArgument<ConversationsHistoryArguments, ConversationsHistoryResponse>;
```

##### Description {#description-147}

Fetches a conversation's history of messages and events.

##### See {#see-147}

[\`conversations.history\` API reference](https://docs.slack.dev/reference/methods/conversations.history).

#### info {#info-2}

```
info: MethodWithRequiredArgument<ConversationsInfoArguments, ConversationsInfoResponse>;
```

##### Description {#description-148}

Retrieve information about a conversation.

##### See {#see-148}

[\`conversations.info\` API reference](https://docs.slack.dev/reference/methods/conversations.info).

#### invite {#invite}

```
invite: MethodWithRequiredArgument<ConversationsInviteArguments, ConversationsInviteResponse>;
```

##### Description {#description-149}

Invites users to a channel.

##### See {#see-149}

[\`conversations.invite\` API reference](https://docs.slack.dev/reference/methods/conversations.invite).

#### inviteShared {#inviteshared}

```
inviteShared: MethodWithRequiredArgument<ConversationsInviteSharedArguments, ConversationsInviteSharedResponse>;
```

##### Description {#description-150}

Sends an invitation to a Slack Connect channel.

##### See {#see-150}

[\`conversations.inviteShared\` API reference](https://docs.slack.dev/reference/methods/conversations.inviteShared).

#### join {#join}

```
join: MethodWithRequiredArgument<ConversationsJoinArguments, ConversationsJoinResponse>;
```

##### Description {#description-151}

Joins an existing conversation.

##### See {#see-151}

[\`conversations.join\` API reference](https://docs.slack.dev/reference/methods/conversations.join).

#### kick {#kick}

```
kick: MethodWithRequiredArgument<ConversationsKickArguments, ConversationsKickResponse>;
```

##### Description {#description-152}

Removes a user from a conversation.

##### See {#see-152}

[\`conversations.kick\` API reference](https://docs.slack.dev/reference/methods/conversations.kick).

#### leave {#leave}

```
leave: MethodWithRequiredArgument<ConversationsLeaveArguments, ConversationsLeaveResponse>;
```

##### Description {#description-153}

Leaves a conversation.

##### See {#see-153}

[\`conversations.leave\` API reference](https://docs.slack.dev/reference/methods/conversations.leave).

#### list {#list-1}

```
list: Method<ConversationsListArguments, ConversationsListResponse>;
```

##### Description {#description-154}

List all channels in a Slack team.

##### See {#see-154}

[\`conversations.list\` API reference](https://docs.slack.dev/reference/methods/conversations.list).

#### listConnectInvites {#listconnectinvites}

```
listConnectInvites: Method<ConversationsListConnectInvitesArguments, ConversationsListConnectInvitesResponse>;
```

##### Description {#description-155}

Lists shared channel invites that have been generated or received but have not been approved by all parties.

##### See {#see-155}

[\`conversations.listConnectInvites\` API reference](https://docs.slack.dev/reference/methods/conversations.listConnectInvites).

#### mark {#mark}

```
mark: MethodWithRequiredArgument<ConversationsMarkArguments, ConversationsMarkResponse>;
```

##### Description {#description-156}

Sets the read cursor in a channel.

##### See {#see-156}

[\`conversations.mark\` API reference](https://docs.slack.dev/reference/methods/conversations.mark).

#### members {#members}

```
members: MethodWithRequiredArgument<ConversationsMembersArguments, ConversationsMembersResponse>;
```

##### Description {#description-157}

Retrieve members of a conversation.

##### See {#see-157}

[\`conversations.members\` API reference](https://docs.slack.dev/reference/methods/conversations.members).

#### open {#open}

```
open: MethodWithRequiredArgument<ConversationsOpenArguments, ConversationsOpenResponse>;
```

##### Description {#description-158}

Opens or resumes a direct message or multi-person direct message.

##### See {#see-158}

[\`conversations.open\` API reference](https://docs.slack.dev/reference/methods/conversations.open).

#### rename {#rename}

```
rename: MethodWithRequiredArgument<ConversationsRenameArguments, ConversationsRenameResponse>;
```

##### Description {#description-159}

Renames a conversation.

##### See {#see-159}

[\`conversations.rename\` API reference](https://docs.slack.dev/reference/methods/conversations.rename).

#### replies {#replies}

```
replies: MethodWithRequiredArgument<ConversationsRepliesArguments, ConversationsRepliesResponse>;
```

##### Description {#description-160}

Retrieve a thread of messages posted to a conversation.

##### See {#see-160}

[\`conversations.replies\` API reference](https://docs.slack.dev/reference/methods/conversations.replies).

#### requestSharedInvite {#requestsharedinvite}

```
requestSharedInvite: object;
```

##### requestSharedInvite.approve {#requestsharedinviteapprove}

```
approve: MethodWithRequiredArgument<ConversationsRequestSharedInviteApproveArguments, ConversationsRequestSharedInviteApproveResponse>;
```

###### Description {#description-161}

Approves a request to add an external user to a channel and sends them a Slack Connect invite.

###### See {#see-161}

[\`conversations.requestSharedInvite.approve\` API reference](https://docs.slack.dev/reference/methods/conversations.requestSharedInvite.approve).

##### requestSharedInvite.deny {#requestsharedinvitedeny}

```
deny: MethodWithRequiredArgument<ConversationsRequestSharedInviteDenyArguments, ConversationsRequestSharedInviteDenyResponse>;
```

###### Description {#description-162}

Denies a request to invite an external user to a channel.

###### See {#see-162}

[\`conversations.requestSharedInvite.deny\` API reference](https://docs.slack.dev/reference/methods/conversations.requestSharedInvite.deny).

##### requestSharedInvite.list {#requestsharedinvitelist}

```
list: Method<ConversationsRequestSharedInviteListArguments, ConversationsRequestSharedInviteListResponse>;
```

###### Description {#description-163}

Lists requests to add external users to channels with ability to filter.

###### See {#see-163}

[\`conversations.requestSharedInvite.list\` API reference](https://docs.slack.dev/reference/methods/conversations.requestSharedInvite.list).

#### setPurpose {#setpurpose}

```
setPurpose: MethodWithRequiredArgument<ConversationsSetPurposeArguments, ConversationsSetPurposeResponse>;
```

##### Description {#description-164}

Sets the purpose for a conversation.

##### See {#see-164}

[\`conversations.setPurpose\` API reference](https://docs.slack.dev/reference/methods/conversations.setPurpose).

#### setTopic {#settopic}

```
setTopic: MethodWithRequiredArgument<ConversationsSetTopicArguments, ConversationsSetTopicResponse>;
```

##### Description {#description-165}

Sets the topic for a conversation.

##### See {#see-165}

[\`conversations.setTopic\` API reference](https://docs.slack.dev/reference/methods/conversations.setTopic).

#### unarchive {#unarchive}

```
unarchive: MethodWithRequiredArgument<ConversationsUnarchiveArguments, ConversationsUnarchiveResponse>;
```

##### Description {#description-166}

Reverses conversation archival.

##### See {#see-166}

[\`conversations.unarchive\` API reference](https://docs.slack.dev/reference/methods/conversations.unarchive).

#### Inherited from {#inherited-from-10}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`conversations`](/tools/node-slack-sdk/reference/web-api/classes/Methods#conversations)

* * *

### dialog {#dialog}

```
readonly dialog: object;
```

Defined in: [packages/web-api/src/methods.ts:1881](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1881)

#### open {#open-1}

```
open: MethodWithRequiredArgument<DialogOpenArguments, DialogOpenResponse>;
```

##### Description {#description-167}

Open a dialog with a user.

##### See {#see-167}

[\`dialog.open\` API reference](https://docs.slack.dev/reference/methods/dialog.open).

#### Inherited from {#inherited-from-11}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`dialog`](/tools/node-slack-sdk/reference/web-api/classes/Methods#dialog)

* * *

### dnd {#dnd}

```
readonly dnd: object;
```

Defined in: [packages/web-api/src/methods.ts:1889](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1889)

#### endDnd {#enddnd}

```
endDnd: Method<DndEndDndArguments, DndEndDndResponse>;
```

##### Description {#description-168}

Ends the current user's Do Not Disturb session immediately.

##### See {#see-168}

[\`dnd.endDnd\` API reference](https://docs.slack.dev/reference/methods/dnd.endDnd).

#### endSnooze {#endsnooze}

```
endSnooze: Method<DndEndSnoozeArguments, DndEndSnoozeResponse>;
```

##### Description {#description-169}

Ends the current user's snooze mode immediately.

##### See {#see-169}

[\`dnd.endSnooze\` API reference](https://docs.slack.dev/reference/methods/dnd.endSnooze).

#### info {#info-3}

```
info: Method<DndInfoArguments, DndInfoResponse>;
```

##### Description {#description-170}

Retrieves a user's current Do Not Disturb status.

##### See {#see-170}

[\`dnd.info\` API reference](https://docs.slack.dev/reference/methods/dnd.info).

#### setSnooze {#setsnooze}

```
setSnooze: MethodWithRequiredArgument<DndSetSnoozeArguments, DndSetSnoozeResponse>;
```

##### Description {#description-171}

Turns on Do Not Disturb mode for the current user, or changes its duration.

##### See {#see-171}

[\`dnd.setSnooze\` API reference](https://docs.slack.dev/reference/methods/dnd.setSnooze).

#### teamInfo {#teaminfo}

```
teamInfo: MethodWithRequiredArgument<DndTeamInfoArguments, DndTeamInfoResponse>;
```

##### Description {#description-172}

Retrieves the Do Not Disturb status for up to 50 users on a team.

##### See {#see-172}

[\`dnd.teamInfo\` API reference](https://docs.slack.dev/reference/methods/dnd.teamInfo).

#### Inherited from {#inherited-from-12}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`dnd`](/tools/node-slack-sdk/reference/web-api/classes/Methods#dnd)

* * *

### emoji {#emoji-1}

```
readonly emoji: object;
```

Defined in: [packages/web-api/src/methods.ts:1917](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1917)

#### list {#list-2}

```
list: Method<EmojiListArguments, EmojiListResponse>;
```

##### Description {#description-173}

Lists custom emoji for a team.

##### See {#see-173}

[\`emoji.list\` API reference](https://docs.slack.dev/reference/methods/emoji.list).

#### Inherited from {#inherited-from-13}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`emoji`](/tools/node-slack-sdk/reference/web-api/classes/Methods#emoji)

* * *

### entity {#entity}

```
readonly entity: object;
```

Defined in: [packages/web-api/src/methods.ts:1925](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1925)

#### presentDetails {#presentdetails}

```
presentDetails: MethodWithRequiredArgument<EntityPresentDetailsArguments, EntityPresentDetailsResponse>;
```

##### Description {#description-174}

Provide information about the entity to be displayed in the flexpane.

##### See {#see-174}

[https://docs.slack.dev/reference/methods/entity.presentDetails](https://docs.slack.dev/reference/methods/entity.presentDetails)

#### Inherited from {#inherited-from-14}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`entity`](/tools/node-slack-sdk/reference/web-api/classes/Methods#entity)

* * *

### files {#files}

```
readonly files: object;
```

Defined in: [packages/web-api/src/methods.ts:1936](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L1936)

#### comments {#comments}

```
comments: object;
```

##### comments.delete {#commentsdelete}

```
delete: MethodWithRequiredArgument<FilesCommentsDeleteArguments, FilesCommentsDeleteResponse>;
```

###### Description {#description-175}

Deletes an existing comment on a file.

###### See {#see-175}

[\`files.comments.delete\` API reference](https://docs.slack.dev/reference/methods/files.comments.delete).

#### completeUploadExternal {#completeuploadexternal}

```
completeUploadExternal: MethodWithRequiredArgument<FilesCompleteUploadExternalArguments, FilesCompleteUploadExternalResponse>;
```

##### Description {#description-176}

Finishes an upload started with [\`files.getUploadURLExternal\`](https://docs.slack.dev/reference/methods/files.getUploadURLExternal).

##### See {#see-176}

[\`files.completeUploadExternal\` API reference](https://docs.slack.dev/reference/methods/files.completeUploadExternal).

#### delete {#delete-2}

```
delete: MethodWithRequiredArgument<FilesDeleteArguments, FilesDeleteResponse>;
```

##### Description {#description-177}

Deletes a file.

##### See {#see-177}

[\`files.delete\` API reference](https://docs.slack.dev/reference/methods/files.delete).

#### getUploadURLExternal {#getuploadurlexternal}

```
getUploadURLExternal: MethodWithRequiredArgument<FilesGetUploadURLExternalArguments, FilesGetUploadURLExternalResponse>;
```

##### Description {#description-178}

Gets a URL for an edge external file upload.

##### See {#see-178}

[\`files.getUploadURLExternal\` API reference](https://docs.slack.dev/reference/methods/files.getUploadURLExternal).

#### info {#info-4}

```
info: MethodWithRequiredArgument<FilesInfoArguments, FilesInfoResponse>;
```

##### Description {#description-179}

Gets information about a file.

##### See {#see-179}

[\`files.info\` API reference](https://docs.slack.dev/reference/methods/files.info).

#### list {#list-3}

```
list: MethodWithRequiredArgument<FilesListArguments, FilesListResponse>;
```

##### Description {#description-180}

List files for a team, in a channel, or from a user with applied filters.

##### See {#see-180}

[\`files.list\` API reference](https://docs.slack.dev/reference/methods/files.list).

#### remote {#remote}

```
remote: object;
```

##### remote.add {#remoteadd}

```
add: MethodWithRequiredArgument<FilesRemoteAddArguments, FilesRemoteAddResponse>;
```

###### Description {#description-181}

Adds a file from a remote service.

###### See {#see-181}

[\`files.remote.add\` API reference](https://docs.slack.dev/reference/methods/files.remote.add).

##### remote.info {#remoteinfo}

```
info: MethodWithRequiredArgument<FilesRemoteInfoArguments, FilesRemoteInfoResponse>;
```

###### Description {#description-182}

Retrieve information about a remote file added to Slack.

###### See {#see-182}

[\`files.remote.info\` API reference](https://docs.slack.dev/reference/methods/files.remote.info).

##### remote.list {#remotelist}

```
list: MethodWithRequiredArgument<FilesRemoteListArguments, FilesRemoteListResponse>;
```

###### Description {#description-183}

List remote files added to Slack.

###### See {#see-183}

[\`files.remote.list\` API reference](https://docs.slack.dev/reference/methods/files.remote.list).

##### remote.remove {#remoteremove}

```
remove: MethodWithRequiredArgument<FilesRemoteRemoveArguments, FilesRemoteRemoveResponse>;
```

###### Description {#description-184}

Remove a remote file.

###### See {#see-184}

[\`files.remote.remove\` API reference](https://docs.slack.dev/reference/methods/files.remote.remove).

##### remote.share {#remoteshare}

```
share: MethodWithRequiredArgument<FilesRemoteShareArguments, FilesRemoteShareResponse>;
```

###### Description {#description-185}

Share a remote file into a channel.

###### See {#see-185}

[\`files.remote.share\` API reference](https://docs.slack.dev/reference/methods/files.remote.share).

##### remote.update {#remoteupdate}

```
update: MethodWithRequiredArgument<FilesRemoteUpdateArguments, FilesRemoteUpdateResponse>;
```

###### Description {#description-186}

Updates an existing remote file.

###### See {#see-186}

[\`files.remote.update\` API reference](https://docs.slack.dev/reference/methods/files.remote.update).

#### revokePublicURL {#revokepublicurl}

```
revokePublicURL: MethodWithRequiredArgument<FilesRevokePublicURLArguments, FilesRevokePublicURLResponse>;
```

##### Description {#description-187}

Revokes public/external sharing access for a file.

##### See {#see-187}

[\`files.revokePublicURL\` API reference](https://docs.slack.dev/reference/methods/files.revokePublicURL).

#### sharedPublicURL {#sharedpublicurl}

```
sharedPublicURL: MethodWithRequiredArgument<FilesSharedPublicURLArguments, FilesSharedPublicURLResponse>;
```

##### Description {#description-188}

Enables a file for public/external sharing.

##### See {#see-188}

[\`files.sharedPublicURL\` API reference](https://docs.slack.dev/reference/methods/files.sharedPublicURL).

#### upload {#upload}

```
upload: MethodWithRequiredArgument<FilesUploadArguments, FilesUploadResponse>;
```

##### Description {#description-189}

Uploads or creates a file.

##### Deprecated {#deprecated}

Use `uploadV2` instead. See [our post on retiring \`files.upload\`](https://docs.slack.dev/changelog/2024-04-a-better-way-to-upload-files-is-here-to-stay).

##### See {#see-189}

[\`files.upload\` API reference](https://docs.slack.dev/reference/methods/files.upload).

#### uploadV2 {#uploadv2}

```
uploadV2: MethodWithRequiredArgument<FilesUploadV2Arguments, WebAPICallResult>;
```

##### Description {#description-190}

Custom method to support a new way of uploading files to Slack. Supports a single file upload Supply:

* (required) single file or content
* (optional) channel, alt\_text, snippet\_type, Supports multiple file uploads Supply:
* multiple upload\_files Will try to honor both single file or content data supplied as well as multiple file uploads property.

##### See {#see-190}

[\`@slack/web-api\` Upload a file documentation](https://docs.slack.dev/tools/node-slack-sdk/web-api/#upload-a-file).

#### Inherited from {#inherited-from-15}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`files`](/tools/node-slack-sdk/reference/web-api/classes/Methods#files)

* * *

### functions {#functions-1}

```
readonly functions: object;
```

Defined in: [packages/web-api/src/methods.ts:2045](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2045)

#### completeError {#completeerror}

```
completeError: MethodWithRequiredArgument<FunctionsCompleteErrorArguments, FunctionsCompleteErrorResponse>;
```

##### Description {#description-191}

Signal the failure to execute a Custom Function.

##### See {#see-191}

[\`functions.completeError\` API reference](https://docs.slack.dev/reference/methods/functions.completeError).

#### completeSuccess {#completesuccess}

```
completeSuccess: MethodWithRequiredArgument<FunctionsCompleteSuccessArguments, FunctionsCompleteSuccessResponse>;
```

##### Description {#description-192}

Signal the successful completion of a Custom Function.

##### See {#see-192}

[\`functions.completeSuccess\` API reference](https://docs.slack.dev/reference/methods/functions.completeSuccess).

#### Inherited from {#inherited-from-16}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`functions`](/tools/node-slack-sdk/reference/web-api/classes/Methods#functions)

* * *

### migration {#migration}

```
readonly migration: object;
```

Defined in: [packages/web-api/src/methods.ts:2064](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2064)

#### exchange {#exchange}

```
exchange: MethodWithRequiredArgument<MigrationExchangeArguments, MigrationExchangeResponse>;
```

##### Description {#description-193}

For Enterprise Grid workspaces, map local user IDs to global user IDs.

##### See {#see-193}

[\`migration.exchange\` API reference](https://docs.slack.dev/reference/methods/migration.exchange).

#### Inherited from {#inherited-from-17}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`migration`](/tools/node-slack-sdk/reference/web-api/classes/Methods#migration)

* * *

### oauth {#oauth}

```
readonly oauth: object;
```

Defined in: [packages/web-api/src/methods.ts:2072](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2072)

#### access {#access-1}

```
access: MethodWithRequiredArgument<OAuthAccessArguments, OauthAccessResponse>;
```

##### Description {#description-194}

Exchanges a temporary OAuth verifier code for an access token.

##### Deprecated {#deprecated-1}

This is a legacy method only used by classic Slack apps. Use `oauth.v2.access` for new Slack apps.

##### See {#see-194}

[\`oauth.access\` API reference](https://docs.slack.dev/reference/methods/oauth.access).

#### v2 {#v2}

```
v2: object;
```

##### v2.access {#v2access}

```
access: MethodWithRequiredArgument<OAuthV2AccessArguments, OauthV2AccessResponse>;
```

###### Description {#description-195}

Exchanges a temporary OAuth verifier code for an access token.

###### See {#see-195}

[\`oauth.v2.access\` API reference](https://docs.slack.dev/reference/methods/oauth.v2.access).

##### v2.exchange {#v2exchange}

```
exchange: MethodWithRequiredArgument<OAuthV2ExchangeArguments, OauthV2ExchangeResponse>;
```

###### Description {#description-196}

Exchanges a legacy access token for a new expiring access token and refresh token.

###### See {#see-196}

[\`oauth.v2.exchange\` API reference](https://docs.slack.dev/reference/methods/oauth.v2.exchange).

#### Inherited from {#inherited-from-18}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`oauth`](/tools/node-slack-sdk/reference/web-api/classes/Methods#oauth)

* * *

### openid {#openid}

```
readonly openid: object;
```

Defined in: [packages/web-api/src/methods.ts:2093](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2093)

#### connect {#connect}

```
connect: object;
```

##### connect.token {#connecttoken}

```
token: MethodWithRequiredArgument<OpenIDConnectTokenArguments, OpenIDConnectTokenResponse>;
```

###### Description {#description-197}

Exchanges a temporary OAuth verifier code for an access token for [Sign in with Slack](https://docs.slack.dev/authentication/sign-in-with-slack).

###### See {#see-197}

[\`openid.connect.token\` API reference](https://docs.slack.dev/reference/methods/openid.connect.token).

##### connect.userInfo {#connectuserinfo}

```
userInfo: Method<OpenIDConnectUserInfoArguments, OpenIDConnectUserInfoResponse>;
```

###### Description {#description-198}

Get the identity of a user who has authorized [Sign in with Slack](https://docs.slack.dev/authentication/sign-in-with-slack).

###### See {#see-198}

[\`openid.connect.userInfo\` API reference](https://docs.slack.dev/reference/methods/openid.connect.userInfo).

#### Inherited from {#inherited-from-19}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`openid`](/tools/node-slack-sdk/reference/web-api/classes/Methods#openid)

* * *

### pins {#pins}

```
readonly pins: object;
```

Defined in: [packages/web-api/src/methods.ts:2111](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2111)

#### add {#add-2}

```
add: MethodWithRequiredArgument<PinsAddArguments, PinsAddResponse>;
```

##### Description {#description-199}

Pins an item to a channel.

##### See {#see-199}

[\`pins.add\` API reference](https://docs.slack.dev/reference/methods/pins.add).

#### list {#list-4}

```
list: MethodWithRequiredArgument<PinsListArguments, PinsListResponse>;
```

##### Description {#description-200}

Lists items pinned to a channel.

##### See {#see-200}

[\`pins.list\` API reference](https://docs.slack.dev/reference/methods/pins.list).

#### remove {#remove-1}

```
remove: MethodWithRequiredArgument<PinsRemoveArguments, PinsRemoveResponse>;
```

##### Description {#description-201}

Un-pins an item from a channel.

##### See {#see-201}

[\`pins.remove\` API reference](https://docs.slack.dev/reference/methods/pins.remove).

#### Inherited from {#inherited-from-20}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`pins`](/tools/node-slack-sdk/reference/web-api/classes/Methods#pins)

* * *

### reactions {#reactions}

```
readonly reactions: object;
```

Defined in: [packages/web-api/src/methods.ts:2129](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2129)

#### add {#add-3}

```
add: MethodWithRequiredArgument<ReactionsAddArguments, ReactionsAddResponse>;
```

##### Description {#description-202}

Adds a reaction to an item.

##### See {#see-202}

[\`reactions.add\` API reference](https://docs.slack.dev/reference/methods/reactions.add).

#### get {#get}

```
get: MethodWithRequiredArgument<ReactionsGetArguments, ReactionsGetResponse>;
```

##### Description {#description-203}

Gets reactions for an item.

##### See {#see-203}

[\`reactions.get\` API reference](https://docs.slack.dev/reference/methods/reactions.get).

#### list {#list-5}

```
list: Method<ReactionsListArguments, ReactionsListResponse>;
```

##### Description {#description-204}

List reactions made by a user.

##### See {#see-204}

[\`reactions.list\` API reference](https://docs.slack.dev/reference/methods/reactions.list).

#### remove {#remove-2}

```
remove: MethodWithRequiredArgument<ReactionsRemoveArguments, ReactionsRemoveResponse>;
```

##### Description {#description-205}

Removes a reaction from an item.

##### See {#see-205}

[\`reactions.remove\` API reference](https://docs.slack.dev/reference/methods/reactions.remove).

#### Inherited from {#inherited-from-21}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`reactions`](/tools/node-slack-sdk/reference/web-api/classes/Methods#reactions)

* * *

### reminders {#reminders}

```
readonly reminders: object;
```

Defined in: [packages/web-api/src/methods.ts:2154](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2154)

#### add {#add-4}

```
add: MethodWithRequiredArgument<RemindersAddArguments, RemindersAddResponse>;
```

##### Description {#description-206}

Creates a reminder.

##### See {#see-206}

[\`reminders.add\` API reference](https://docs.slack.dev/reference/methods/reminders.add).

#### complete {#complete}

```
complete: MethodWithRequiredArgument<RemindersCompleteArguments, RemindersCompleteResponse>;
```

##### Description {#description-207}

Marks a reminder as complete.

##### See {#see-207}

[\`reminders.complete\` API reference](https://docs.slack.dev/reference/methods/reminders.complete).

#### delete {#delete-3}

```
delete: MethodWithRequiredArgument<RemindersDeleteArguments, RemindersDeleteResponse>;
```

##### Description {#description-208}

Deletes a reminder.

##### See {#see-208}

[\`reminders.delete\` API reference](https://docs.slack.dev/reference/methods/reminders.delete).

#### info {#info-5}

```
info: MethodWithRequiredArgument<RemindersInfoArguments, RemindersInfoResponse>;
```

##### Description {#description-209}

Gets information about a reminder.

##### See {#see-209}

[\`reminders.info\` API reference](https://docs.slack.dev/reference/methods/reminders.info).

#### list {#list-6}

```
list: Method<RemindersListArguments, RemindersListResponse>;
```

##### Description {#description-210}

Lists all reminders created by or for a given user.

##### See {#see-210}

[\`reminders.list\` API reference](https://docs.slack.dev/reference/methods/reminders.list).

#### Inherited from {#inherited-from-22}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`reminders`](/tools/node-slack-sdk/reference/web-api/classes/Methods#reminders)

* * *

### rtm {#rtm}

```
readonly rtm: object;
```

Defined in: [packages/web-api/src/methods.ts:2182](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2182)

#### connect {#connect-1}

```
connect: Method<RTMConnectArguments, RtmConnectResponse>;
```

##### Description {#description-211}

Starts a Real Time Messaging session.

##### See {#see-211}

[\`rtm.connect\` API reference](https://docs.slack.dev/reference/methods/rtm.connect).

#### start {#start}

```
start: Method<RTMStartArguments, RtmStartResponse>;
```

##### Description {#description-212}

Starts a Real Time Messaging session.

##### Deprecated {#deprecated-2}

Use `rtm.connect` instead. See [our post on retiring \`rtm.start\`](https://docs.slack.dev/changelog/2021-10-rtm-start-to-stop).

##### See {#see-212}

[\`rtm.start\` API reference](https://docs.slack.dev/reference/methods/rtm.start).

#### Inherited from {#inherited-from-23}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`rtm`](/tools/node-slack-sdk/reference/web-api/classes/Methods#rtm)

* * *

### search {#search}

```
readonly search: object;
```

Defined in: [packages/web-api/src/methods.ts:2196](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2196)

#### all {#all}

```
all: MethodWithRequiredArgument<SearchAllArguments, SearchAllResponse>;
```

##### Description {#description-213}

Searches for messages and files matching a query.

##### See {#see-213}

[search.all\` API reference](https://docs.slack.dev/reference/methods/search.all).

#### files {#files-1}

```
files: MethodWithRequiredArgument<SearchFilesArguments, SearchFilesResponse>;
```

##### Description {#description-214}

Searches for files matching a query.

##### See {#see-214}

[search.files\` API reference](https://docs.slack.dev/reference/methods/search.files).

#### messages {#messages}

```
messages: MethodWithRequiredArgument<SearchMessagesArguments, SearchMessagesResponse>;
```

##### Description {#description-215}

Searches for messages matching a query.

##### See {#see-215}

[search.messages\` API reference](https://docs.slack.dev/reference/methods/search.messages).

#### Inherited from {#inherited-from-24}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`search`](/tools/node-slack-sdk/reference/web-api/classes/Methods#search)

* * *

### slackApiUrl {#slackapiurl}

```
readonly slackApiUrl: string;
```

Defined in: [packages/web-api/src/WebClient.ts:194](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L194)

The base URL for reaching Slack's Web API. Consider changing this value for testing purposes.

* * *

### slackLists {#slacklists}

```
readonly slackLists: object;
```

Defined in: [packages/web-api/src/methods.ts:2214](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2214)

#### access {#access-2}

```
access: object;
```

##### access.delete {#accessdelete-1}

```
delete: MethodWithRequiredArgument<SlackListsAccessDeleteArguments, SlackListsAccessDeleteResponse>;
```

###### Description {#description-216}

Delete access for specified entities.

###### See {#see-216}

[\`slackLists.access.delete\` API reference](https://docs.slack.dev/reference/methods/slackLists.access.delete).

##### access.set {#accessset-1}

```
set: MethodWithRequiredArgument<SlackListsAccessSetArguments, SlackListsAccessSetResponse>;
```

###### Description {#description-217}

Set access level for specified entities.

###### See {#see-217}

[\`slackLists.access.set\` API reference](https://docs.slack.dev/reference/methods/slackLists.access.set).

#### create {#create-2}

```
create: MethodWithRequiredArgument<SlackListsCreateArguments, SlackListsCreateResponse>;
```

##### Description {#description-218}

Create a List.

##### See {#see-218}

[\`slackLists.create\` API reference](https://docs.slack.dev/reference/methods/slackLists.create).

#### download {#download}

```
download: object;
```

##### download.get {#downloadget}

```
get: MethodWithRequiredArgument<SlackListsDownloadGetArguments, SlackListsDownloadGetResponse>;
```

###### Description {#description-219}

Get download job status.

###### See {#see-219}

[\`slackLists.download.get\` API reference](https://docs.slack.dev/reference/methods/slackLists.download.get).

##### download.start {#downloadstart}

```
start: MethodWithRequiredArgument<SlackListsDownloadStartArguments, SlackListsDownloadStartResponse>;
```

###### Description {#description-220}

Start a download job for a list.

###### See {#see-220}

[\`slackLists.download.start\` API reference](https://docs.slack.dev/reference/methods/slackLists.download.start).

#### items {#items}

```
items: object;
```

##### items.create {#itemscreate}

```
create: MethodWithRequiredArgument<SlackListsItemsCreateArguments, SlackListsItemsCreateResponse>;
```

###### Description {#description-221}

Create a list item.

###### See {#see-221}

[\`slackLists.items.create\` API reference](https://docs.slack.dev/reference/methods/slackLists.items.create).

##### items.delete {#itemsdelete}

```
delete: MethodWithRequiredArgument<SlackListsItemsDeleteArguments, SlackListsItemsDeleteResponse>;
```

###### Description {#description-222}

Delete a list item.

###### See {#see-222}

[\`slackLists.items.delete\` API reference](https://docs.slack.dev/reference/methods/slackLists.items.delete).

##### items.deleteMultiple {#itemsdeletemultiple}

```
deleteMultiple: MethodWithRequiredArgument<SlackListsItemsDeleteMultipleArguments, SlackListsItemsDeleteMultipleResponse>;
```

###### Description {#description-223}

Delete multiple list items.

###### See {#see-223}

[\`slackLists.items.deleteMultiple\` API reference](https://docs.slack.dev/reference/methods/slackLists.items.deleteMultiple).

##### items.info {#itemsinfo}

```
info: MethodWithRequiredArgument<SlackListsItemsInfoArguments, SlackListsItemsInfoResponse>;
```

###### Description {#description-224}

Get info about a list item.

###### See {#see-224}

[\`slackLists.items.info\` API reference](https://docs.slack.dev/reference/methods/slackLists.items.info).

##### items.list {#itemslist}

```
list: MethodWithRequiredArgument<SlackListsItemsListArguments, SlackListsItemsListResponse>;
```

###### Description {#description-225}

Get records from a List.

###### See {#see-225}

[\`slackLists.items.list\` API reference](https://docs.slack.dev/reference/methods/slackLists.items.list).

##### items.update {#itemsupdate}

```
update: MethodWithRequiredArgument<SlackListsItemsUpdateArguments, SlackListsItemsUpdateResponse>;
```

###### Description {#description-226}

Update a list item.

###### See {#see-226}

[\`slackLists.items.update\` API reference](https://docs.slack.dev/reference/methods/slackLists.items.update).

#### update {#update-2}

```
update: MethodWithRequiredArgument<SlackListsUpdateArguments, SlackListsUpdateResponse>;
```

##### Description {#description-227}

Update a list.

##### See {#see-227}

[\`slackLists.update\` API reference](https://docs.slack.dev/reference/methods/slackLists.update).

#### Inherited from {#inherited-from-25}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`slackLists`](/tools/node-slack-sdk/reference/web-api/classes/Methods#slacklists)

* * *

### stars {#stars}

```
readonly stars: object;
```

Defined in: [packages/web-api/src/methods.ts:2525](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2525)

#### add {#add-5}

```
add: MethodWithRequiredArgument<StarsAddRemoveArguments, StarsAddResponse>;
```

##### Description {#description-228}

Save an item for later. Formerly known as adding a star.

##### Deprecated {#deprecated-3}

Stars can still be added but they can no longer be viewed or interacted with by end-users. See [our post on stars and the Later list](https://docs.slack.dev/changelog/2023-07-its-later-already-for-stars-and-reminders).

##### See {#see-228}

[\`stars.add\` API reference](https://docs.slack.dev/reference/methods/stars.add).

#### list {#list-7}

```
list: MethodWithRequiredArgument<StarsListArguments, StarsListResponse>;
```

##### Description {#description-229}

List a user's saved items, formerly known as stars.

##### Deprecated {#deprecated-4}

Stars can still be listed but they can no longer be viewed or interacted with by end-users. See [our post on stars and the Later list](https://docs.slack.dev/changelog/2023-07-its-later-already-for-stars-and-reminders).

##### See {#see-229}

[\`stars.list\` API reference](https://docs.slack.dev/reference/methods/stars.list).

#### remove {#remove-3}

```
remove: MethodWithRequiredArgument<StarsAddRemoveArguments, StarsRemoveResponse>;
```

##### Description {#description-230}

Remove a saved item from a user's saved items, formerly known as stars.

##### Deprecated {#deprecated-5}

Stars can still be removed but they can no longer be viewed or interacted with by end-users. See [our post on stars and the Later list](https://docs.slack.dev/changelog/2023-07-its-later-already-for-stars-and-reminders).

##### See {#see-230}

[\`stars.remove\` API reference](https://docs.slack.dev/reference/methods/stars.remove).

#### Inherited from {#inherited-from-26}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`stars`](/tools/node-slack-sdk/reference/web-api/classes/Methods#stars)

* * *

### team {#team}

```
readonly team: object;
```

Defined in: [packages/web-api/src/methods.ts:2301](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2301)

#### accessLogs {#accesslogs}

```
accessLogs: Method<TeamAccessLogsArguments, TeamAccessLogsResponse>;
```

##### Description {#description-231}

Gets the access logs for the current team.

##### See {#see-231}

[\`team.accessLogs\` API reference](https://docs.slack.dev/reference/methods/team.accessLogs).

#### billableInfo {#billableinfo}

```
billableInfo: Method<TeamBillableInfoArguments, TeamBillableInfoResponse>;
```

##### Description {#description-232}

Gets billable users information for the current team.

##### See {#see-232}

[\`team.billableInfo\` API reference](https://docs.slack.dev/reference/methods/team.billableInfo).

#### billing {#billing}

```
billing: object;
```

##### billing.info {#billinginfo}

```
info: MethodWithRequiredArgument<TeamBillingInfoArguments, TeamBillingInfoResponse>;
```

###### Description {#description-233}

Reads a workspace's billing plan information.

###### See {#see-233}

[\`team.billing.info\` API reference](https://docs.slack.dev/reference/methods/team.billing.info).

#### externalTeams {#externalteams}

```
externalTeams: object;
```

##### externalTeams.disconnect {#externalteamsdisconnect}

```
disconnect: MethodWithRequiredArgument<TeamExternalTeamsDisconnectArguments, TeamExternalTeamsDisconnectResponse>;
```

###### Description {#description-234}

Disconnect an external organization.

###### See {#see-234}

[\`team.externalTeams.disconnect\` API reference](https://docs.slack.dev/reference/methods/team.externalTeams.disconnect).

##### externalTeams.list {#externalteamslist}

```
list: MethodWithRequiredArgument<TeamExternalTeamsListArguments, TeamExternalTeamsListResponse>;
```

###### Description {#description-235}

Returns a list of all the external teams connected and details about the connection.

###### See {#see-235}

[\`team.externalTeams.list\` API reference](https://docs.slack.dev/reference/methods/team.externalTeams.list).

#### info {#info-6}

```
info: Method<TeamInfoArguments, TeamInfoResponse>;
```

##### Description {#description-236}

Gets information about the current team.

##### See {#see-236}

[\`team.info\` API reference](https://docs.slack.dev/reference/methods/team.info).

#### integrationLogs {#integrationlogs}

```
integrationLogs: Method<TeamIntegrationLogsArguments, TeamIntegrationLogsResponse>;
```

##### Description {#description-237}

Gets the integration logs for the current team.

##### See {#see-237}

[\`team.integrationLogs\` API reference](https://docs.slack.dev/reference/methods/team.integrationLogs).

#### preferences {#preferences}

```
preferences: object;
```

##### preferences.list {#preferenceslist}

```
list: Method<TeamPreferencesListArguments, TeamPreferencesListResponse>;
```

###### Description {#description-238}

Retrieve a list of a workspace's team preferences.

###### See {#see-238}

[\`team.preferences.list\` API reference](https://docs.slack.dev/reference/methods/team.preferences.list).

#### profile {#profile}

```
profile: object;
```

##### profile.get {#profileget}

```
get: Method<TeamProfileGetArguments, TeamProfileGetResponse>;
```

###### Description {#description-239}

Retrieve a team's profile.

###### See {#see-239}

[\`team.profile.get\` API reference](https://docs.slack.dev/reference/methods/team.profile.get).

#### Inherited from {#inherited-from-27}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`team`](/tools/node-slack-sdk/reference/web-api/classes/Methods#team)

* * *

### token? {#token-1}

```
readonly optional token: string;
```

Defined in: [packages/web-api/src/WebClient.ts:199](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L199)

Authentication and authorization token for accessing Slack Web API (usually begins with `xoxp` or `xoxb`)

* * *

### tooling {#tooling}

```
readonly tooling: object;
```

Defined in: [packages/web-api/src/methods.ts:2372](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2372)

#### tokens {#tokens}

```
tokens: object;
```

##### tokens.rotate {#tokensrotate}

```
rotate: MethodWithRequiredArgument<ToolingTokensRotateArguments, ToolingTokensRotateResponse>;
```

###### Description {#description-240}

Exchanges a refresh token for a new app configuration token.

###### See {#see-240}

[\`tooling.tokens.rotate\` API reference](https://docs.slack.dev/reference/methods/tooling.tokens.rotate).

#### Inherited from {#inherited-from-28}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`tooling`](/tools/node-slack-sdk/reference/web-api/classes/Methods#tooling)

* * *

### usergroups {#usergroups-1}

```
readonly usergroups: object;
```

Defined in: [packages/web-api/src/methods.ts:2382](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2382)

#### create {#create-3}

```
create: MethodWithRequiredArgument<UsergroupsCreateArguments, UsergroupsCreateResponse>;
```

##### Description {#description-241}

Create a User Group.

##### See {#see-241}

[\`usergroups.create\` API reference](https://docs.slack.dev/reference/methods/usergroups.create).

#### disable {#disable}

```
disable: MethodWithRequiredArgument<UsergroupsDisableArguments, UsergroupsDisableResponse>;
```

##### Description {#description-242}

Disable an existing User Group.

##### See {#see-242}

[\`usergroups.disable\` API reference](https://docs.slack.dev/reference/methods/usergroups.disable).

#### enable {#enable}

```
enable: MethodWithRequiredArgument<UsergroupsEnableArguments, UsergroupsEnableResponse>;
```

##### Description {#description-243}

Enable an existing User Group.

##### See {#see-243}

[\`usergroups.enable\` API reference](https://docs.slack.dev/reference/methods/usergroups.enable).

#### list {#list-8}

```
list: Method<UsergroupsListArguments, UsergroupsListResponse>;
```

##### Description {#description-244}

List all User Groups for a team.

##### See {#see-244}

[\`usergroups.list\` API reference](https://docs.slack.dev/reference/methods/usergroups.list).

#### update {#update-3}

```
update: MethodWithRequiredArgument<UsergroupsUpdateArguments, UsergroupsUpdateResponse>;
```

##### Description {#description-245}

Update an existing User Group.

##### See {#see-245}

[\`usergroups.update\` API reference](https://docs.slack.dev/reference/methods/usergroups.update).

#### users {#users-1}

```
users: object;
```

##### users.list {#userslist-1}

```
list: MethodWithRequiredArgument<UsergroupsUsersListArguments, UsergroupsUsersListResponse>;
```

###### Description {#description-246}

List all users in a User Group.

###### See {#see-246}

[\`usergroups.users.list\` API reference](https://docs.slack.dev/reference/methods/usergroups.users.list).

##### users.update {#usersupdate}

```
update: MethodWithRequiredArgument<UsergroupsUsersUpdateArguments, UsergroupsUsersUpdateResponse>;
```

###### Description {#description-247}

Update the list of users in a User Group.

###### See {#see-247}

[\`usergroups.users.update\` API reference](https://docs.slack.dev/reference/methods/usergroups.users.update).

#### Inherited from {#inherited-from-29}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`usergroups`](/tools/node-slack-sdk/reference/web-api/classes/Methods#usergroups)

* * *

### users {#users-2}

```
readonly users: object;
```

Defined in: [packages/web-api/src/methods.ts:2425](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2425)

#### conversations {#conversations-2}

```
conversations: MethodWithRequiredArgument<UsersConversationsArguments, UsersConversationsResponse>;
```

##### Description {#description-248}

List conversations the calling user may access.

##### See {#see-248}

[\`users.conversations\` API reference](https://docs.slack.dev/reference/methods/users.conversations).

#### deletePhoto {#deletephoto}

```
deletePhoto: MethodWithRequiredArgument<UsersDeletePhotoArguments, UsersDeletePhotoResponse>;
```

##### Description {#description-249}

Delete the user profile photo.

##### See {#see-249}

[\`users.deletePhoto\` API reference](https://docs.slack.dev/reference/methods/users.deletePhoto).

#### discoverableContacts {#discoverablecontacts}

```
discoverableContacts: object;
```

##### discoverableContacts.lookup {#discoverablecontactslookup}

```
lookup: MethodWithRequiredArgument<UsersDiscoverableContactsLookupArguments, UsersDiscoverableContactsLookupResponse>;
```

###### Description {#description-250}

Lookup an email address to see if someone is on Slack.

###### See {#see-250}

[\`users.discoverableContacts.lookup\` API reference](https://docs.slack.dev/reference/methods/users.discoverableContacts.lookup).

#### getPresence {#getpresence}

```
getPresence: MethodWithRequiredArgument<UsersGetPresenceArguments, UsersGetPresenceResponse>;
```

##### Description {#description-251}

Gets user presence information.

##### See {#see-251}

[\`users.getPresence\` API reference](https://docs.slack.dev/reference/methods/users.getPresence).

#### identity {#identity}

```
identity: MethodWithRequiredArgument<UsersIdentityArguments, UsersIdentityResponse>;
```

##### Description {#description-252}

Get a user's identity.

##### See {#see-252}

[\`users.identity\` API reference](https://docs.slack.dev/reference/methods/users.identity).

#### info {#info-7}

```
info: MethodWithRequiredArgument<UsersInfoArguments, UsersInfoResponse>;
```

##### Description {#description-253}

Gets information about a user.

##### See {#see-253}

[\`users.info\` API reference](https://docs.slack.dev/reference/methods/users.info).

#### list {#list-9}

```
list: MethodWithRequiredArgument<UsersListArguments, UsersListResponse>;
```

##### Description {#description-254}

Lists all users in a Slack team.

##### See {#see-254}

[\`users.list\` API reference](https://docs.slack.dev/reference/methods/users.list).

#### lookupByEmail {#lookupbyemail}

```
lookupByEmail: MethodWithRequiredArgument<UsersLookupByEmailArguments, UsersLookupByEmailResponse>;
```

##### Description {#description-255}

Find a user with an email address.

##### See {#see-255}

[\`users.lookupByEmail\` API reference](https://docs.slack.dev/reference/methods/users.lookupByEmail).

#### profile {#profile-1}

```
profile: object;
```

##### profile.get {#profileget-1}

```
get: MethodWithRequiredArgument<UsersProfileGetArguments, UsersProfileGetResponse>;
```

###### Description {#description-256}

Retrieve a user's profile information, including their custom status.

###### See {#see-256}

[\`users.profile.get\` API reference](https://docs.slack.dev/reference/methods/users.profile.get).

##### profile.set {#profileset}

```
set: MethodWithRequiredArgument<UsersProfileSetArguments, UsersProfileSetResponse>;
```

###### Description {#description-257}

Set a user's profile information, including custom status.

###### See {#see-257}

[\`users.profile.set\` API reference](https://docs.slack.dev/reference/methods/users.profile.set).

#### setPhoto {#setphoto}

```
setPhoto: MethodWithRequiredArgument<UsersSetPhotoArguments, UsersSetPhotoResponse>;
```

##### Description {#description-258}

Set the user profile photo.

##### See {#see-258}

[\`users.setPhoto\` API reference](https://docs.slack.dev/reference/methods/users.setPhoto).

#### setPresence {#setpresence}

```
setPresence: MethodWithRequiredArgument<UsersSetPresenceArguments, UsersSetPresenceResponse>;
```

##### Description {#description-259}

Manually sets user presence.

##### See {#see-259}

[\`users.setPresence\` API reference](https://docs.slack.dev/reference/methods/users.setPresence).

#### Inherited from {#inherited-from-30}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`users`](/tools/node-slack-sdk/reference/web-api/classes/Methods#users)

* * *

### views {#views}

```
readonly views: object;
```

Defined in: [packages/web-api/src/methods.ts:2495](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2495)

#### open {#open-2}

```
open: MethodWithRequiredArgument<ViewsOpenArguments, ViewsOpenResponse>;
```

##### Description {#description-260}

Open a view for a user.

##### See {#see-260}

[\`views.open\` API reference](https://docs.slack.dev/reference/methods/views.open).

#### publish {#publish}

```
publish: MethodWithRequiredArgument<ViewsPublishArguments, ViewsPublishResponse>;
```

##### Description {#description-261}

Publish a static view for a user.

##### See {#see-261}

[\`views.publish\` API reference](https://docs.slack.dev/reference/methods/views.publish).

#### push {#push}

```
push: MethodWithRequiredArgument<ViewsPushArguments, ViewsPushResponse>;
```

##### Description {#description-262}

Push a view onto the stack of a root view.

##### See {#see-262}

[\`views.push\` API reference](https://docs.slack.dev/reference/methods/views.push).

#### update {#update-4}

```
update: MethodWithRequiredArgument<ViewsUpdateArguments, ViewsUpdateResponse>;
```

##### Description {#description-263}

Update an existing view.

##### See {#see-263}

[\`views.update\` API reference](https://docs.slack.dev/reference/methods/views.update).

#### Inherited from {#inherited-from-31}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`views`](/tools/node-slack-sdk/reference/web-api/classes/Methods#views)

* * *

### workflows {#workflows-1}

```
readonly workflows: object;
```

Defined in: [packages/web-api/src/methods.ts:2549](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L2549)

#### featured {#featured}

```
featured: object;
```

##### featured.add {#featuredadd}

```
add: MethodWithRequiredArgument<WorkflowsFeaturedAddArguments, WebAPICallResult>;
```

###### Description {#description-264}

Add featured workflows to a channel.

###### See {#see-264}

[\`workflows.featured.add\` API reference](https://docs.slack.dev/reference/methods/workflows.featured.add).

##### featured.list {#featuredlist}

```
list: MethodWithRequiredArgument<WorkflowsFeaturedListArguments, WorkflowsFeaturedListResponse>;
```

###### Description {#description-265}

List the featured workflows for specified channels.

###### See {#see-265}

[\`workflows.featured.list\` API reference](https://docs.slack.dev/reference/methods/workflows.featured.list).

##### featured.remove {#featuredremove}

```
remove: MethodWithRequiredArgument<WorkflowsFeaturedRemoveArguments, WebAPICallResult>;
```

###### Description {#description-266}

Remove featured workflows from a channel.

###### See {#see-266}

[\`workflows.featured.remove\` API reference](https://docs.slack.dev/reference/methods/workflows.featured.remove).

##### featured.set {#featuredset}

```
set: MethodWithRequiredArgument<WorkflowsFeaturedSetArguments, WebAPICallResult>;
```

###### Description {#description-267}

Set featured workflows for a channel.

###### See {#see-267}

[\`workflows.featured.set\` API reference](https://docs.slack.dev/reference/methods/workflows.featured.set).

#### stepCompleted {#stepcompleted}

```
stepCompleted: MethodWithRequiredArgument<WorkflowsStepCompletedArguments, WorkflowsStepCompletedResponse>;
```

##### Description {#description-268}

Indicate that an app's step in a workflow completed execution.

##### Deprecated {#deprecated-6}

Steps from Apps is deprecated. We're retiring all Slack app functionality around Steps from Apps in September 2024. See [our post on deprecating Steps from Apps](https://docs.slack.dev/changelog/2023-08-workflow-steps-from-apps-step-back).

##### See {#see-268}

[\`workflows.stepCompleted\` API reference](https://docs.slack.dev/legacy/legacy-steps-from-apps/legacy-steps-from-apps-workflow_step-object).

#### stepFailed {#stepfailed}

```
stepFailed: MethodWithRequiredArgument<WorkflowsStepFailedArguments, WorkflowsStepFailedResponse>;
```

##### Description {#description-269}

Indicate that an app's step in a workflow failed to execute.

##### Deprecated {#deprecated-7}

Steps from Apps is deprecated. We're retiring all Slack app functionality around Steps from Apps in September 2024. See [our post on deprecating Steps from Apps](https://docs.slack.dev/changelog/2023-08-workflow-steps-from-apps-step-back).

##### See {#see-269}

[\`workflows.stepFailed\` API reference](https://docs.slack.dev/legacy/legacy-steps-from-apps/legacy-steps-from-apps-workflow_step-object).

#### updateStep {#updatestep}

```
updateStep: MethodWithRequiredArgument<WorkflowsUpdateStepArguments, WorkflowsUpdateStepResponse>;
```

##### Description {#description-270}

Update the configuration for a workflow step.

##### Deprecated {#deprecated-8}

Steps from Apps is deprecated. We're retiring all Slack app functionality around Steps from Apps in September 2024. See [our post on deprecating Steps from Apps](https://docs.slack.dev/changelog/2023-08-workflow-steps-from-apps-step-back).

##### See {#see-270}

[\`workflows.updateStep\` API reference](https://docs.slack.dev/legacy/legacy-steps-from-apps/legacy-steps-from-apps-workflow_step-object).

#### Inherited from {#inherited-from-32}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`workflows`](/tools/node-slack-sdk/reference/web-api/classes/Methods#workflows)

* * *

### prefixed {#prefixed}

```
static prefixed: string | boolean;
```

Defined in: node\_modules/eventemitter3/index.d.ts:9

#### Inherited from {#inherited-from-33}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`prefixed`](/tools/node-slack-sdk/reference/web-api/classes/Methods#prefixed)

## Methods {#methods}

### addListener() {#addlistener}

```
addListener<T>(   event,    fn,    context?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:45

#### Type Parameters {#type-parameters}

##### T {#t}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-1}

##### event {#event-1}

`T`

##### fn {#fn}

(...`args`) => `void`

##### context? {#context}

`any`

#### Returns {#returns-1}

`this`

#### Inherited from {#inherited-from-34}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`addListener`](/tools/node-slack-sdk/reference/web-api/classes/Methods#addlistener)

* * *

### apiCall() {#apicall}

```
apiCall(method, options?): Promise<WebAPICallResult>;
```

Defined in: [packages/web-api/src/WebClient.ts:346](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L346)

Generic method for calling a Web API method

#### Parameters {#parameters-2}

##### method {#method}

`string`

the Web API method to call [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods)

##### options? {#options}

`Record`<`string`, `unknown`\> = `{}`

options

#### Returns {#returns-2}

`Promise`<[`WebAPICallResult`](/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult)\>

#### Overrides {#overrides-1}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`apiCall`](/tools/node-slack-sdk/reference/web-api/classes/Methods#apicall)

* * *

### chatStream() {#chatstream}

```
chatStream(params): ChatStreamer;
```

Defined in: [packages/web-api/src/WebClient.ts:538](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L538)

Stream markdown text into a conversation.

#### Parameters {#parameters-3}

##### params {#params}

`Omit`<[`ChatStartStreamArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/ChatStartStreamArguments) & [`ChatStreamerOptions`](/tools/node-slack-sdk/reference/web-api/interfaces/ChatStreamerOptions), `"markdown_text"`\>

#### Returns {#returns-3}

[`ChatStreamer`](/tools/node-slack-sdk/reference/web-api/classes/ChatStreamer)

#### Description {#description-271}

The "chatStream" method starts a new chat stream in a conversation that can be appended to. After appending an entire message, the stream can be stopped with concluding arguments such as "blocks" for gathering feedback.

The "markdown\_text" content is appended to a buffer before being sent to the recipient, with a default buffer size of "256" characters. Setting the "buffer\_size" value to a smaller number sends more frequent updates for the same amount of characters, but might reach rate limits more often.

#### Example {#example}

```
const streamer = client.chatStream({  channel: "C0123456789",  thread_ts: "1700000001.123456",  recipient_team_id: "T0123456789",  recipient_user_id: "U0123456789",});await streamer.append({  markdown_text: "**hello wo",});await streamer.append({  markdown_text: "rld!**",});await streamer.stop();
```

#### See {#see-271}

* [https://docs.slack.dev/reference/methods/chat.startStream](https://docs.slack.dev/reference/methods/chat.startStream)
* [https://docs.slack.dev/reference/methods/chat.appendStream](https://docs.slack.dev/reference/methods/chat.appendStream)
* [https://docs.slack.dev/reference/methods/chat.stopStream](https://docs.slack.dev/reference/methods/chat.stopStream)

* * *

### emit() {#emit}

```
emit<T>(event, ...args): boolean;
```

Defined in: node\_modules/eventemitter3/index.d.ts:32

Calls each of the listeners registered for a given event.

#### Type Parameters {#type-parameters-1}

##### T {#t-1}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-4}

##### event {#event-2}

`T`

##### args {#args}

...`any`\[\]

#### Returns {#returns-4}

`boolean`

#### Inherited from {#inherited-from-35}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`emit`](/tools/node-slack-sdk/reference/web-api/classes/Methods#emit)

* * *

### eventNames() {#eventnames}

```
eventNames(): RATE_LIMITED[];
```

Defined in: node\_modules/eventemitter3/index.d.ts:15

Return an array listing the events for which the emitter has registered listeners.

#### Returns {#returns-5}

[`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)\[\]

#### Inherited from {#inherited-from-36}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`eventNames`](/tools/node-slack-sdk/reference/web-api/classes/Methods#eventnames)

* * *

### filesUploadV2() {#filesuploadv2}

```
filesUploadV2(options): Promise<WebAPICallResult & object>;
```

Defined in: [packages/web-api/src/WebClient.ts:559](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L559)

This wrapper method provides an easy way to upload files using the following endpoints:

**#1**: For each file submitted with this method, submit filenames and file metadata to [files.getUploadURLExternal](https://docs.slack.dev/reference/methods/files.getuploadurlexternal) to request a URL to which to send the file data to and an id for the file

**#2**: for each returned file `upload_url`, upload corresponding file to URLs returned from step 1 (e.g. [https://files.slack.com/upload/v1/...\\](https://files.slack.com/upload/v1/...%5C)")

**#3**: Complete uploads [files.completeUploadExternal](https://docs.slack.dev/reference/methods/files.completeuploadexternal)

#### Parameters {#parameters-5}

##### options {#options-1}

[`FilesUploadV2Arguments`](/tools/node-slack-sdk/reference/web-api/type-aliases/FilesUploadV2Arguments)

#### Returns {#returns-6}

`Promise`<[`WebAPICallResult`](/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult) & `object`\>

#### Overrides {#overrides-2}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`filesUploadV2`](/tools/node-slack-sdk/reference/web-api/classes/Methods#filesuploadv2)

* * *

### listenerCount() {#listenercount}

```
listenerCount(event): number;
```

Defined in: node\_modules/eventemitter3/index.d.ts:27

Return the number of listeners listening to a given event.

#### Parameters {#parameters-6}

##### event {#event-3}

[`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Returns {#returns-7}

`number`

#### Inherited from {#inherited-from-37}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`listenerCount`](/tools/node-slack-sdk/reference/web-api/classes/Methods#listenercount)

* * *

### listeners() {#listeners}

```
listeners<T>(event): (...args) => void[];
```

Defined in: node\_modules/eventemitter3/index.d.ts:20

Return the listeners registered for a given event.

#### Type Parameters {#type-parameters-2}

##### T {#t-2}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-7}

##### event {#event-4}

`T`

#### Returns {#returns-8}

(...`args`) => `void`\[\]

#### Inherited from {#inherited-from-38}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`listeners`](/tools/node-slack-sdk/reference/web-api/classes/Methods#listeners)

* * *

### off() {#off}

```
off<T>(   event,    fn?,    context?,    once?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:69

#### Type Parameters {#type-parameters-3}

##### T {#t-3}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-8}

##### event {#event-5}

`T`

##### fn? {#fn-1}

(...`args`) => `void`

##### context? {#context-1}

`any`

##### once? {#once}

`boolean`

#### Returns {#returns-9}

`this`

#### Inherited from {#inherited-from-39}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`off`](/tools/node-slack-sdk/reference/web-api/classes/Methods#off)

* * *

### on() {#on}

```
on<T>(   event,    fn,    context?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:40

Add a listener for a given event.

#### Type Parameters {#type-parameters-4}

##### T {#t-4}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-9}

##### event {#event-6}

`T`

##### fn {#fn-2}

(...`args`) => `void`

##### context? {#context-2}

`any`

#### Returns {#returns-10}

`this`

#### Inherited from {#inherited-from-40}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`on`](/tools/node-slack-sdk/reference/web-api/classes/Methods#on)

* * *

### once() {#once-1}

```
once<T>(   event,    fn,    context?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:54

Add a one-time listener for a given event.

#### Type Parameters {#type-parameters-5}

##### T {#t-5}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-10}

##### event {#event-7}

`T`

##### fn {#fn-3}

(...`args`) => `void`

##### context? {#context-3}

`any`

#### Returns {#returns-11}

`this`

#### Inherited from {#inherited-from-41}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`once`](/tools/node-slack-sdk/reference/web-api/classes/Methods#once)

* * *

### paginate() {#paginate}

#### Call Signature {#call-signature}

```
paginate(method, options?): AsyncIterable<WebAPICallResult>;
```

Defined in: [packages/web-api/src/WebClient.ts:433](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L433)

Iterate over the result pages of a cursor-paginated Web API method. This method can return two types of values, depending on which arguments are used. When up to two parameters are used, the return value is an async iterator which can be used as the iterable in a for-await-of loop. When three or four parameters are used, the return value is a promise that resolves at the end of iteration. The third parameter, `shouldStop`, is a function that is called with each `page` and can end iteration by returning `true`. The fourth parameter, `reduce`, is a function that is called with three arguments: `accumulator`, `page`, and `index`. The `accumulator` is a value of any type you choose, but it will contain `undefined` when `reduce` is called for the first time. The `page` argument and `index` arguments are exactly what they say they are. The `reduce` function's return value will be passed in as `accumulator` the next time it's called, and the returned promise will resolve to the last value of `accumulator`.

The for-await-of syntax is part of ES2018. It is available natively in Node starting with v10.0.0. You may be able to use it in earlier JavaScript runtimes by transpiling your source with a tool like Babel. However, the transpiled code will likely sacrifice performance.

##### Parameters {#parameters-11}

###### method {#method-1}

`string`

the cursor-paginated Web API method to call [https://docs.slack.dev/apis/web-api/paginationn](https://docs.slack.dev/apis/web-api/paginationn)

###### options? {#options-2}

`Record`<`string`, `unknown`\>

options

##### Returns {#returns-12}

`AsyncIterable`<[`WebAPICallResult`](/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult)\>

#### Call Signature {#call-signature-1}

```
paginate(   method,    options, shouldStop): Promise<void>;
```

Defined in: [packages/web-api/src/WebClient.ts:434](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L434)

Iterate over the result pages of a cursor-paginated Web API method. This method can return two types of values, depending on which arguments are used. When up to two parameters are used, the return value is an async iterator which can be used as the iterable in a for-await-of loop. When three or four parameters are used, the return value is a promise that resolves at the end of iteration. The third parameter, `shouldStop`, is a function that is called with each `page` and can end iteration by returning `true`. The fourth parameter, `reduce`, is a function that is called with three arguments: `accumulator`, `page`, and `index`. The `accumulator` is a value of any type you choose, but it will contain `undefined` when `reduce` is called for the first time. The `page` argument and `index` arguments are exactly what they say they are. The `reduce` function's return value will be passed in as `accumulator` the next time it's called, and the returned promise will resolve to the last value of `accumulator`.

The for-await-of syntax is part of ES2018. It is available natively in Node starting with v10.0.0. You may be able to use it in earlier JavaScript runtimes by transpiling your source with a tool like Babel. However, the transpiled code will likely sacrifice performance.

##### Parameters {#parameters-12}

###### method {#method-2}

`string`

the cursor-paginated Web API method to call [https://docs.slack.dev/apis/web-api/paginationn](https://docs.slack.dev/apis/web-api/paginationn)

###### options {#options-3}

`Record`<`string`, `unknown`\>

options

###### shouldStop {#shouldstop}

[`PaginatePredicate`](/tools/node-slack-sdk/reference/web-api/type-aliases/PaginatePredicate)

a predicate that is called with each page, and should return true when pagination can end.

##### Returns {#returns-13}

`Promise`<`void`\>

#### Call Signature {#call-signature-2}

```
paginate<R, A>(   method,    options,    shouldStop, reduce?): Promise<A>;
```

Defined in: [packages/web-api/src/WebClient.ts:435](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L435)

Iterate over the result pages of a cursor-paginated Web API method. This method can return two types of values, depending on which arguments are used. When up to two parameters are used, the return value is an async iterator which can be used as the iterable in a for-await-of loop. When three or four parameters are used, the return value is a promise that resolves at the end of iteration. The third parameter, `shouldStop`, is a function that is called with each `page` and can end iteration by returning `true`. The fourth parameter, `reduce`, is a function that is called with three arguments: `accumulator`, `page`, and `index`. The `accumulator` is a value of any type you choose, but it will contain `undefined` when `reduce` is called for the first time. The `page` argument and `index` arguments are exactly what they say they are. The `reduce` function's return value will be passed in as `accumulator` the next time it's called, and the returned promise will resolve to the last value of `accumulator`.

The for-await-of syntax is part of ES2018. It is available natively in Node starting with v10.0.0. You may be able to use it in earlier JavaScript runtimes by transpiling your source with a tool like Babel. However, the transpiled code will likely sacrifice performance.

##### Type Parameters {#type-parameters-6}

###### R {#r}

`R` _extends_ [`PageReducer`](/tools/node-slack-sdk/reference/web-api/type-aliases/PageReducer)<`any`\>

###### A {#a}

`A` _extends_ `any`

##### Parameters {#parameters-13}

###### method {#method-3}

`string`

the cursor-paginated Web API method to call [https://docs.slack.dev/apis/web-api/paginationn](https://docs.slack.dev/apis/web-api/paginationn)

###### options {#options-4}

`Record`<`string`, `unknown`\>

options

###### shouldStop {#shouldstop-1}

[`PaginatePredicate`](/tools/node-slack-sdk/reference/web-api/type-aliases/PaginatePredicate)

a predicate that is called with each page, and should return true when pagination can end.

###### reduce? {#reduce}

[`PageReducer`](/tools/node-slack-sdk/reference/web-api/type-aliases/PageReducer)<`A`\>

a callback that can be used to accumulate a value that the return promise is resolved to

##### Returns {#returns-14}

`Promise`<`A`\>

* * *

### removeAllListeners() {#removealllisteners}

```
removeAllListeners(event?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:79

Remove all listeners, or those of the specified event.

#### Parameters {#parameters-14}

##### event? {#event-8}

[`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Returns {#returns-15}

`this`

#### Inherited from {#inherited-from-42}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`removeAllListeners`](/tools/node-slack-sdk/reference/web-api/classes/Methods#removealllisteners)

* * *

### removeListener() {#removelistener}

```
removeListener<T>(   event,    fn?,    context?,    once?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:63

Remove the listeners of a given event.

#### Type Parameters {#type-parameters-7}

##### T {#t-6}

`T` _extends_ [`RATE_LIMITED`](/tools/node-slack-sdk/reference/web-api/enumerations/WebClientEvent#rate_limited)

#### Parameters {#parameters-15}

##### event {#event-9}

`T`

##### fn? {#fn-4}

(...`args`) => `void`

##### context? {#context-4}

`any`

##### once? {#once-2}

`boolean`

#### Returns {#returns-16}

`this`

#### Inherited from {#inherited-from-43}

[`Methods`](/tools/node-slack-sdk/reference/web-api/classes/Methods).[`removeListener`](/tools/node-slack-sdk/reference/web-api/classes/Methods#removelistener)

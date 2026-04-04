Source: https://docs.slack.dev/legacy/legacy-authentication/legacy-oauth-scopes

# Legacy OAuth scopes

OAuth scopes let you specify exactly how your app needs to access a Slack user's account. As an app developer, you specify your desired scopes in the initial [OAuth authorization request](/authentication). When a user is responding to your OAuth request, the requested scopes will be displayed to them when they are asked to approve your request.

Slack's system of OAuth permission scopes governs usage of Slack apps and their use of the [Web API](/apis/web-api/), [Events API](/reference/events), [RTM API](/legacy/legacy-rtm-api), [Slash Commands](/interactivity/implementing-slash-commands), and [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).

![A screen showing the requested scopes during an OAuth request](/assets/images/oauth_authorization-b3c235aa09110c5630167fb330555d05.png)

## Types of Scopes {#types}

Slack uses scopes that refer to the object they grant access to, followed by the class of actions on that object they allow (e.g. `file:write`). Additionally, some scopes have an optional perspective which is either `user`, `bot`, or `admin`, which influences how the action appears in Slack (e.g. `chat:write:user` will send a message from the authorizing user as opposed to your app).

The list of objects includes `files`, `search`, `chat`, and `reactions`, along with many other objects in Slack.

There are currently only three classes of action:

* **read**: Reading the full information about a single resource.
* **write**: Modifying the resource in any way e.g. creating, editing, or deleting.
* **history**: Accessing the message archive of channels, DMs, or private channels.

For example, to request access to the list of channels on a workspace and the ability to send messages to those channels as a bot, your app would request `channels:read chat:write:bot`.

## OAuth Scopes to API methods {#oauth-scopes-api-methods}

[`admin.analytics:read`](/reference/scopes/admin.analytics.read)

* [`admin.analytics.getFile`](/reference/methods/admin.analytics.getFile)

* * *

[`admin.app_activities:read`](/reference/scopes/admin.app_activities.read)

* [`admin.apps.activities.list`](/reference/methods/admin.apps.activities.list)

* * *

[`admin.apps:read`](/reference/scopes/admin.apps.read)

* [`admin.apps.approved.list`](/reference/methods/admin.apps.approved.list)
* [`admin.apps.config.lookup`](/reference/methods/admin.apps.config.lookup)
* [`admin.apps.requests.list`](/reference/methods/admin.apps.requests.list)
* [`admin.apps.restricted.list`](/reference/methods/admin.apps.restricted.list)

* * *

[`admin.apps:write`](/reference/scopes/admin.apps.write)

* [`admin.apps.approve`](/reference/methods/admin.apps.approve)
* [`admin.apps.clearResolution`](/reference/methods/admin.apps.clearResolution)
* [`admin.apps.config.set`](/reference/methods/admin.apps.config.set)
* [`admin.apps.requests.cancel`](/reference/methods/admin.apps.requests.cancel)
* [`admin.apps.restrict`](/reference/methods/admin.apps.restrict)
* [`admin.apps.uninstall`](/reference/methods/admin.apps.uninstall)

* * *

[`admin.barriers:read`](/reference/scopes/admin.barriers.read)

* [`admin.barriers.list`](/reference/methods/admin.barriers.list)

* * *

[`admin.barriers:write`](/reference/scopes/admin.barriers.write)

* [`admin.barriers.create`](/reference/methods/admin.barriers.create)
* [`admin.barriers.delete`](/reference/methods/admin.barriers.delete)
* [`admin.barriers.update`](/reference/methods/admin.barriers.update)

* * *

[`admin.conversations:manage_objects`](/reference/scopes/admin.conversations.manage_objects)

* [`admin.conversations.createForObjects`](/reference/methods/admin.conversations.createForObjects)
* [`admin.conversations.linkObjects`](/reference/methods/admin.conversations.linkObjects)
* [`admin.conversations.unlinkObjects`](/reference/methods/admin.conversations.unlinkObjects)

* * *

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

* [`admin.conversations.ekm.listOriginalConnectedChannelInfo`](/reference/methods/admin.conversations.ekm.listOriginalConnectedChannelInfo)
* [`admin.conversations.getConversationPrefs`](/reference/methods/admin.conversations.getConversationPrefs)
* [`admin.conversations.getCustomRetention`](/reference/methods/admin.conversations.getCustomRetention)
* [`admin.conversations.getTeams`](/reference/methods/admin.conversations.getTeams)
* [`admin.conversations.lookup`](/reference/methods/admin.conversations.lookup)
* [`admin.conversations.restrictAccess.listGroups`](/reference/methods/admin.conversations.restrictAccess.listGroups)
* [`admin.conversations.search`](/reference/methods/admin.conversations.search)

* * *

[`admin.conversations:write`](/reference/scopes/admin.conversations.write)

* [`admin.conversations.archive`](/reference/methods/admin.conversations.archive)
* [`admin.conversations.bulkArchive`](/reference/methods/admin.conversations.bulkArchive)
* [`admin.conversations.bulkDelete`](/reference/methods/admin.conversations.bulkDelete)
* [`admin.conversations.bulkMove`](/reference/methods/admin.conversations.bulkMove)
* [`admin.conversations.convertToPrivate`](/reference/methods/admin.conversations.convertToPrivate)
* [`admin.conversations.convertToPublic`](/reference/methods/admin.conversations.convertToPublic)
* [`admin.conversations.create`](/reference/methods/admin.conversations.create)
* [`admin.conversations.delete`](/reference/methods/admin.conversations.delete)
* [`admin.conversations.disconnectShared`](/reference/methods/admin.conversations.disconnectShared)
* [`admin.conversations.invite`](/reference/methods/admin.conversations.invite)
* [`admin.conversations.removeCustomRetention`](/reference/methods/admin.conversations.removeCustomRetention)
* [`admin.conversations.rename`](/reference/methods/admin.conversations.rename)
* [`admin.conversations.restrictAccess.addGroup`](/reference/methods/admin.conversations.restrictAccess.addGroup)
* [`admin.conversations.restrictAccess.removeGroup`](/reference/methods/admin.conversations.restrictAccess.removeGroup)
* [`admin.conversations.setConversationPrefs`](/reference/methods/admin.conversations.setConversationPrefs)
* [`admin.conversations.setCustomRetention`](/reference/methods/admin.conversations.setCustomRetention)
* [`admin.conversations.setTeams`](/reference/methods/admin.conversations.setTeams)
* [`admin.conversations.unarchive`](/reference/methods/admin.conversations.unarchive)

* * *

[`admin.invites:read`](/reference/scopes/admin.invites.read)

* [`admin.inviteRequests.approved.list`](/reference/methods/admin.inviteRequests.approved.list)
* [`admin.inviteRequests.denied.list`](/reference/methods/admin.inviteRequests.denied.list)
* [`admin.inviteRequests.list`](/reference/methods/admin.inviteRequests.list)

* * *

[`admin.invites:write`](/reference/scopes/admin.invites.write)

* [`admin.inviteRequests.approve`](/reference/methods/admin.inviteRequests.approve)
* [`admin.inviteRequests.deny`](/reference/methods/admin.inviteRequests.deny)

* * *

[`admin.roles:read`](/reference/scopes/admin.roles.read)

* [`admin.roles.listAssignments`](/reference/methods/admin.roles.listAssignments)

* * *

[`admin.roles:write`](/reference/scopes/admin.roles.write)

* [`admin.roles.addAssignments`](/reference/methods/admin.roles.addAssignments)
* [`admin.roles.removeAssignments`](/reference/methods/admin.roles.removeAssignments)

* * *

[`admin.teams:read`](/reference/scopes/admin.teams.read)

* [`admin.emoji.list`](/reference/methods/admin.emoji.list)
* [`admin.teams.admins.list`](/reference/methods/admin.teams.admins.list)
* [`admin.teams.list`](/reference/methods/admin.teams.list)
* [`admin.teams.owners.list`](/reference/methods/admin.teams.owners.list)
* [`admin.teams.settings.info`](/reference/methods/admin.teams.settings.info)

* * *

[`admin.teams:write`](/reference/scopes/admin.teams.write)

* [`admin.emoji.add`](/reference/methods/admin.emoji.add)
* [`admin.emoji.addAlias`](/reference/methods/admin.emoji.addAlias)
* [`admin.emoji.remove`](/reference/methods/admin.emoji.remove)
* [`admin.emoji.rename`](/reference/methods/admin.emoji.rename)
* [`admin.teams.create`](/reference/methods/admin.teams.create)
* [`admin.teams.settings.setDefaultChannels`](/reference/methods/admin.teams.settings.setDefaultChannels)
* [`admin.teams.settings.setDescription`](/reference/methods/admin.teams.settings.setDescription)
* [`admin.teams.settings.setDiscoverability`](/reference/methods/admin.teams.settings.setDiscoverability)
* [`admin.teams.settings.setIcon`](/reference/methods/admin.teams.settings.setIcon)
* [`admin.teams.settings.setName`](/reference/methods/admin.teams.settings.setName)
* [`admin.usergroups.addTeams`](/reference/methods/admin.usergroups.addTeams)

* * *

[`admin.usergroups:read`](/reference/scopes/admin.usergroups.read)

* [`admin.usergroups.listChannels`](/reference/methods/admin.usergroups.listChannels)

* * *

[`admin.usergroups:write`](/reference/scopes/admin.usergroups.write)

* [`admin.usergroups.addChannels`](/reference/methods/admin.usergroups.addChannels)
* [`admin.usergroups.removeChannels`](/reference/methods/admin.usergroups.removeChannels)

* * *

[`admin.users:read`](/reference/scopes/admin.users.read)

* [`admin.auth.policy.getEntities`](/reference/methods/admin.auth.policy.getEntities)
* [`admin.users.list`](/reference/methods/admin.users.list)
* [`admin.users.session.getSettings`](/reference/methods/admin.users.session.getSettings)
* [`admin.users.session.list`](/reference/methods/admin.users.session.list)
* [`admin.users.unsupportedVersions.export`](/reference/methods/admin.users.unsupportedVersions.export)

* * *

[`admin.users:write`](/reference/scopes/admin.users.write)

* [`admin.auth.policy.assignEntities`](/reference/methods/admin.auth.policy.assignEntities)
* [`admin.auth.policy.removeEntities`](/reference/methods/admin.auth.policy.removeEntities)
* [`admin.users.assign`](/reference/methods/admin.users.assign)
* [`admin.users.invite`](/reference/methods/admin.users.invite)
* [`admin.users.remove`](/reference/methods/admin.users.remove)
* [`admin.users.session.clearSettings`](/reference/methods/admin.users.session.clearSettings)
* [`admin.users.session.invalidate`](/reference/methods/admin.users.session.invalidate)
* [`admin.users.session.reset`](/reference/methods/admin.users.session.reset)
* [`admin.users.session.resetBulk`](/reference/methods/admin.users.session.resetBulk)
* [`admin.users.session.setSettings`](/reference/methods/admin.users.session.setSettings)
* [`admin.users.setAdmin`](/reference/methods/admin.users.setAdmin)
* [`admin.users.setExpiration`](/reference/methods/admin.users.setExpiration)
* [`admin.users.setOwner`](/reference/methods/admin.users.setOwner)
* [`admin.users.setRegular`](/reference/methods/admin.users.setRegular)

* * *

[`admin.workflows:read`](/reference/scopes/admin.workflows.read)

* [`admin.functions.list`](/reference/methods/admin.functions.list)
* [`admin.functions.permissions.lookup`](/reference/methods/admin.functions.permissions.lookup)
* [`admin.workflows.permissions.lookup`](/reference/methods/admin.workflows.permissions.lookup)
* [`admin.workflows.search`](/reference/methods/admin.workflows.search)

* * *

[`admin.workflows:write`](/reference/scopes/admin.workflows.write)

* [`admin.functions.permissions.set`](/reference/methods/admin.functions.permissions.set)
* [`admin.workflows.collaborators.add`](/reference/methods/admin.workflows.collaborators.add)
* [`admin.workflows.collaborators.remove`](/reference/methods/admin.workflows.collaborators.remove)
* [`admin.workflows.unpublish`](/reference/methods/admin.workflows.unpublish)

* * *

[`app_configurations:read`](/reference/scopes/app_configurations.read)

* [`apps.manifest.export`](/reference/methods/apps.manifest.export)
* [`functions.distributions.permissions.list`](/reference/methods/functions.distributions.permissions.list)

* * *

[`app_configurations:write`](/reference/scopes/app_configurations.write)

* [`apps.manifest.create`](/reference/methods/apps.manifest.create)
* [`apps.manifest.delete`](/reference/methods/apps.manifest.delete)
* [`apps.manifest.update`](/reference/methods/apps.manifest.update)
* [`apps.manifest.validate`](/reference/methods/apps.manifest.validate)
* [`functions.distributions.permissions.add`](/reference/methods/functions.distributions.permissions.add)
* [`functions.distributions.permissions.remove`](/reference/methods/functions.distributions.permissions.remove)
* [`functions.distributions.permissions.set`](/reference/methods/functions.distributions.permissions.set)

* * *

[`assistant:write`](/reference/scopes/assistant.write)

* [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus)
* [`assistant.threads.setSuggestedPrompts`](/reference/methods/assistant.threads.setSuggestedPrompts)
* [`assistant.threads.setTitle`](/reference/methods/assistant.threads.setTitle)

* * *

[`authorizations:read`](/reference/scopes/authorizations.read)

* [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list)

* * *

[`bookmarks:read`](/reference/scopes/bookmarks.read)

* [`bookmarks.list`](/reference/methods/bookmarks.list)
* [`workflows.featured.list`](/reference/methods/workflows.featured.list)

* * *

[`bookmarks:write`](/reference/scopes/bookmarks.write)

* [`bookmarks.add`](/reference/methods/bookmarks.add)
* [`bookmarks.edit`](/reference/methods/bookmarks.edit)
* [`bookmarks.remove`](/reference/methods/bookmarks.remove)
* [`workflows.featured.add`](/reference/methods/workflows.featured.add)
* [`workflows.featured.remove`](/reference/methods/workflows.featured.remove)
* [`workflows.featured.set`](/reference/methods/workflows.featured.set)

* * *

[`calls:read`](/reference/scopes/calls.read)

* [`calls.info`](/reference/methods/calls.info)

* * *

[`calls:write`](/reference/scopes/calls.write)

* [`calls.add`](/reference/methods/calls.add)
* [`calls.end`](/reference/methods/calls.end)
* [`calls.participants.add`](/reference/methods/calls.participants.add)
* [`calls.participants.remove`](/reference/methods/calls.participants.remove)
* [`calls.update`](/reference/methods/calls.update)

* * *

[`canvases:read`](/reference/scopes/canvases.read)

* [`canvases.sections.lookup`](/reference/methods/canvases.sections.lookup)

* * *

[`canvases:write`](/reference/scopes/canvases.write)

* [`canvases.access.delete`](/reference/methods/canvases.access.delete)
* [`canvases.access.set`](/reference/methods/canvases.access.set)
* [`canvases.create`](/reference/methods/canvases.create)
* [`canvases.delete`](/reference/methods/canvases.delete)
* [`canvases.edit`](/reference/methods/canvases.edit)
* [`conversations.canvases.create`](/reference/methods/conversations.canvases.create)

* * *

[`channels:history`](/reference/scopes/channels.history)

* [`conversations.history`](/reference/methods/conversations.history)
* [`conversations.replies`](/reference/methods/conversations.replies)

* * *

[`channels:join`](/reference/scopes/channels.join)

* [`conversations.join`](/reference/methods/conversations.join)

* * *

[`channels:read`](/reference/scopes/channels.read)

* [`conversations.info`](/reference/methods/conversations.info)
* [`conversations.list`](/reference/methods/conversations.list)
* [`conversations.members`](/reference/methods/conversations.members)
* [`users.conversations`](/reference/methods/users.conversations)

* * *

[`channels:write`](/reference/scopes/channels.write)

* [`conversations.archive`](/reference/methods/conversations.archive)
* [`conversations.close`](/reference/methods/conversations.close)
* [`conversations.create`](/reference/methods/conversations.create)
* [`conversations.externalInvitePermissions.set`](/reference/methods/conversations.externalInvitePermissions.set)
* [`conversations.invite`](/reference/methods/conversations.invite)
* [`conversations.join`](/reference/methods/conversations.join)
* [`conversations.kick`](/reference/methods/conversations.kick)
* [`conversations.leave`](/reference/methods/conversations.leave)
* [`conversations.mark`](/reference/methods/conversations.mark)
* [`conversations.open`](/reference/methods/conversations.open)
* [`conversations.rename`](/reference/methods/conversations.rename)
* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)
* [`conversations.unarchive`](/reference/methods/conversations.unarchive)
* [`team.externalTeams.disconnect`](/reference/methods/team.externalTeams.disconnect)

* * *

[`channels:write.invites`](/reference/scopes/channels.write.invites)

* [`conversations.invite`](/reference/methods/conversations.invite)

* * *

[`channels:write.topic`](/reference/scopes/channels.write.topic)

* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)

* * *

[`chat:write`](/reference/scopes/chat.write)

* [`chat.delete`](/reference/methods/chat.delete)
* [`chat.deleteScheduledMessage`](/reference/methods/chat.deleteScheduledMessage)
* [`chat.meMessage`](/reference/methods/chat.meMessage)
* [`chat.postEphemeral`](/reference/methods/chat.postEphemeral)
* [`chat.postMessage`](/reference/methods/chat.postMessage)
* [`chat.scheduleMessage`](/reference/methods/chat.scheduleMessage)
* [`chat.update`](/reference/methods/chat.update)

* * *

[`connections:write`](/reference/scopes/connections.write)

* [`apps.connections.open`](/reference/methods/apps.connections.open)

* * *

[`datastore:read`](/reference/scopes/datastore.read)

* [`apps.datastore.bulkGet`](/reference/methods/apps.datastore.bulkGet)
* [`apps.datastore.count`](/reference/methods/apps.datastore.count)
* [`apps.datastore.get`](/reference/methods/apps.datastore.get)
* [`apps.datastore.query`](/reference/methods/apps.datastore.query)

* * *

[`datastore:write`](/reference/scopes/datastore.write)

* [`apps.datastore.bulkDelete`](/reference/methods/apps.datastore.bulkDelete)
* [`apps.datastore.bulkPut`](/reference/methods/apps.datastore.bulkPut)
* [`apps.datastore.delete`](/reference/methods/apps.datastore.delete)
* [`apps.datastore.put`](/reference/methods/apps.datastore.put)
* [`apps.datastore.update`](/reference/methods/apps.datastore.update)

* * *

[`dnd:read`](/reference/scopes/dnd.read)

* [`dnd.info`](/reference/methods/dnd.info)
* [`dnd.teamInfo`](/reference/methods/dnd.teamInfo)

* * *

[`dnd:write`](/reference/scopes/dnd.write)

* [`dnd.endDnd`](/reference/methods/dnd.endDnd)
* [`dnd.endSnooze`](/reference/methods/dnd.endSnooze)
* [`dnd.setSnooze`](/reference/methods/dnd.setSnooze)

* * *

[`emoji:read`](/reference/scopes/emoji.read)

* [`emoji.list`](/reference/methods/emoji.list)

* * *

[`files:read`](/reference/scopes/files.read)

* [`files.info`](/reference/methods/files.info)
* [`files.list`](/reference/methods/files.list)

* * *

[`files:write`](/reference/scopes/files.write)

* [`files.comments.delete`](/reference/methods/files.comments.delete)
* [`files.completeUploadExternal`](/reference/methods/files.completeUploadExternal)
* [`files.delete`](/reference/methods/files.delete)
* [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal)
* [`files.revokePublicURL`](/reference/methods/files.revokePublicURL)
* [`files.sharedPublicURL`](/reference/methods/files.sharedPublicURL)
* [`files.upload`](/reference/methods/files.upload)

* * *

[`groups:history`](/reference/scopes/groups.history)

* [`conversations.history`](/reference/methods/conversations.history)
* [`conversations.replies`](/reference/methods/conversations.replies)

* * *

[`groups:read`](/reference/scopes/groups.read)

* [`conversations.info`](/reference/methods/conversations.info)
* [`conversations.list`](/reference/methods/conversations.list)
* [`conversations.members`](/reference/methods/conversations.members)
* [`users.conversations`](/reference/methods/users.conversations)

* * *

[`groups:write`](/reference/scopes/groups.write)

* [`conversations.archive`](/reference/methods/conversations.archive)
* [`conversations.close`](/reference/methods/conversations.close)
* [`conversations.create`](/reference/methods/conversations.create)
* [`conversations.externalInvitePermissions.set`](/reference/methods/conversations.externalInvitePermissions.set)
* [`conversations.invite`](/reference/methods/conversations.invite)
* [`conversations.kick`](/reference/methods/conversations.kick)
* [`conversations.leave`](/reference/methods/conversations.leave)
* [`conversations.mark`](/reference/methods/conversations.mark)
* [`conversations.open`](/reference/methods/conversations.open)
* [`conversations.rename`](/reference/methods/conversations.rename)
* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)
* [`conversations.unarchive`](/reference/methods/conversations.unarchive)
* [`team.externalTeams.disconnect`](/reference/methods/team.externalTeams.disconnect)

* * *

[`groups:write.invites`](/reference/scopes/groups.write.invites)

* [`conversations.invite`](/reference/methods/conversations.invite)

* * *

[`groups:write.topic`](/reference/scopes/groups.write.topic)

* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)

* * *

[`hosting:read`](/reference/scopes/hosting.read)

* [`apps.activities.list`](/reference/methods/apps.activities.list)

* * *

[`im:history`](/reference/scopes/im.history)

* [`conversations.history`](/reference/methods/conversations.history)
* [`conversations.replies`](/reference/methods/conversations.replies)

* * *

[`im:read`](/reference/scopes/im.read)

* [`conversations.info`](/reference/methods/conversations.info)
* [`conversations.list`](/reference/methods/conversations.list)
* [`conversations.members`](/reference/methods/conversations.members)
* [`users.conversations`](/reference/methods/users.conversations)

* * *

[`im:write`](/reference/scopes/im.write)

* [`conversations.archive`](/reference/methods/conversations.archive)
* [`conversations.close`](/reference/methods/conversations.close)
* [`conversations.create`](/reference/methods/conversations.create)
* [`conversations.externalInvitePermissions.set`](/reference/methods/conversations.externalInvitePermissions.set)
* [`conversations.invite`](/reference/methods/conversations.invite)
* [`conversations.kick`](/reference/methods/conversations.kick)
* [`conversations.leave`](/reference/methods/conversations.leave)
* [`conversations.mark`](/reference/methods/conversations.mark)
* [`conversations.open`](/reference/methods/conversations.open)
* [`conversations.rename`](/reference/methods/conversations.rename)
* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)
* [`conversations.unarchive`](/reference/methods/conversations.unarchive)
* [`team.externalTeams.disconnect`](/reference/methods/team.externalTeams.disconnect)

* * *

[`im:write.topic`](/reference/scopes/im.write.topic)

* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)

* * *

[`links:write`](/reference/scopes/links.write)

* [`chat.unfurl`](/reference/methods/chat.unfurl)

* * *

[`lists:read`](/reference/scopes/lists.read)

* [`slackLists.download.get`](/reference/methods/slackLists.download.get)
* [`slackLists.download.start`](/reference/methods/slackLists.download.start)
* [`slackLists.items.info`](/reference/methods/slackLists.items.info)
* [`slackLists.items.list`](/reference/methods/slackLists.items.list)

* * *

[`lists:write`](/reference/scopes/lists.write)

* [`slackLists.access.delete`](/reference/methods/slackLists.access.delete)
* [`slackLists.access.set`](/reference/methods/slackLists.access.set)
* [`slackLists.create`](/reference/methods/slackLists.create)
* [`slackLists.items.create`](/reference/methods/slackLists.items.create)
* [`slackLists.items.delete`](/reference/methods/slackLists.items.delete)
* [`slackLists.items.deleteMultiple`](/reference/methods/slackLists.items.deleteMultiple)
* [`slackLists.items.update`](/reference/methods/slackLists.items.update)
* [`slackLists.update`](/reference/methods/slackLists.update)

* * *

[`mpim:history`](/reference/scopes/mpim.history)

* [`conversations.history`](/reference/methods/conversations.history)
* [`conversations.replies`](/reference/methods/conversations.replies)

* * *

[`mpim:read`](/reference/scopes/mpim.read)

* [`conversations.info`](/reference/methods/conversations.info)
* [`conversations.list`](/reference/methods/conversations.list)
* [`conversations.members`](/reference/methods/conversations.members)
* [`users.conversations`](/reference/methods/users.conversations)

* * *

[`mpim:write`](/reference/scopes/mpim.write)

* [`conversations.archive`](/reference/methods/conversations.archive)
* [`conversations.close`](/reference/methods/conversations.close)
* [`conversations.create`](/reference/methods/conversations.create)
* [`conversations.externalInvitePermissions.set`](/reference/methods/conversations.externalInvitePermissions.set)
* [`conversations.invite`](/reference/methods/conversations.invite)
* [`conversations.kick`](/reference/methods/conversations.kick)
* [`conversations.leave`](/reference/methods/conversations.leave)
* [`conversations.mark`](/reference/methods/conversations.mark)
* [`conversations.open`](/reference/methods/conversations.open)
* [`conversations.rename`](/reference/methods/conversations.rename)
* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)
* [`conversations.unarchive`](/reference/methods/conversations.unarchive)
* [`team.externalTeams.disconnect`](/reference/methods/team.externalTeams.disconnect)

* * *

[`mpim:write.topic`](/reference/scopes/mpim.write.topic)

* [`conversations.setPurpose`](/reference/methods/conversations.setPurpose)
* [`conversations.setTopic`](/reference/methods/conversations.setTopic)

* * *

[`pins:read`](/reference/scopes/pins.read)

* [`pins.list`](/reference/methods/pins.list)

* * *

[`pins:write`](/reference/scopes/pins.write)

* [`pins.add`](/reference/methods/pins.add)
* [`pins.remove`](/reference/methods/pins.remove)

* * *

[`reactions:read`](/reference/scopes/reactions.read)

* [`reactions.get`](/reference/methods/reactions.get)
* [`reactions.list`](/reference/methods/reactions.list)

* * *

[`reactions:write`](/reference/scopes/reactions.write)

* [`reactions.add`](/reference/methods/reactions.add)
* [`reactions.remove`](/reference/methods/reactions.remove)

* * *

[`reminders:read`](/reference/scopes/reminders.read)

* [`reminders.info`](/reference/methods/reminders.info)
* [`reminders.list`](/reference/methods/reminders.list)

* * *

[`reminders:write`](/reference/scopes/reminders.write)

* [`reminders.add`](/reference/methods/reminders.add)
* [`reminders.complete`](/reference/methods/reminders.complete)
* [`reminders.delete`](/reference/methods/reminders.delete)

* * *

[`remote_files:read`](/reference/scopes/remote_files.read)

* [`files.remote.info`](/reference/methods/files.remote.info)
* [`files.remote.list`](/reference/methods/files.remote.list)

* * *

[`remote_files:share`](/reference/scopes/remote_files.share)

* [`files.remote.share`](/reference/methods/files.remote.share)

* * *

[`remote_files:write`](/reference/scopes/remote_files.write)

* [`files.remote.add`](/reference/methods/files.remote.add)
* [`files.remote.remove`](/reference/methods/files.remote.remove)
* [`files.remote.update`](/reference/methods/files.remote.update)

* * *

[`search:read`](/reference/scopes/search.read)

* [`assistant.search.context`](/reference/methods/assistant.search.context)
* [`assistant.search.info`](/reference/methods/assistant.search.info)
* [`search.all`](/reference/methods/search.all)
* [`search.files`](/reference/methods/search.files)
* [`search.messages`](/reference/methods/search.messages)

* * *

[`search:read.public`](/reference/scopes/search.read.public)

* [`assistant.search.context`](/reference/methods/assistant.search.context)
* [`assistant.search.info`](/reference/methods/assistant.search.info)

* * *

[`stars:read`](/reference/scopes/stars.read)

* [`stars.list`](/reference/methods/stars.list)

* * *

[`stars:write`](/reference/scopes/stars.write)

* [`stars.add`](/reference/methods/stars.add)
* [`stars.remove`](/reference/methods/stars.remove)

* * *

[`team.billing:read`](/reference/scopes/team.billing.read)

* [`team.billing.info`](/reference/methods/team.billing.info)

* * *

[`team.preferences:read`](/reference/scopes/team.preferences.read)

* [`team.preferences.list`](/reference/methods/team.preferences.list)

* * *

[`team:read`](/reference/scopes/team.read)

* [`team.externalTeams.list`](/reference/methods/team.externalTeams.list)
* [`team.info`](/reference/methods/team.info)
* [`users.discoverableContacts.lookup`](/reference/methods/users.discoverableContacts.lookup)

* * *

[`tokens.basic`](/reference/scopes/tokens.basic)

* [`migration.exchange`](/reference/methods/migration.exchange)

* * *

[`triggers:read`](/reference/scopes/triggers.read)

* [`workflows.triggers.permissions.list`](/reference/methods/workflows.triggers.permissions.list)

* * *

[`triggers:write`](/reference/scopes/triggers.write)

* [`workflows.triggers.permissions.add`](/reference/methods/workflows.triggers.permissions.add)
* [`workflows.triggers.permissions.remove`](/reference/methods/workflows.triggers.permissions.remove)
* [`workflows.triggers.permissions.set`](/reference/methods/workflows.triggers.permissions.set)

* * *

[`usergroups:read`](/reference/scopes/usergroups.read)

* [`usergroups.list`](/reference/methods/usergroups.list)
* [`usergroups.users.list`](/reference/methods/usergroups.users.list)

* * *

[`usergroups:write`](/reference/scopes/usergroups.write)

* [`usergroups.create`](/reference/methods/usergroups.create)
* [`usergroups.disable`](/reference/methods/usergroups.disable)
* [`usergroups.enable`](/reference/methods/usergroups.enable)
* [`usergroups.update`](/reference/methods/usergroups.update)
* [`usergroups.users.update`](/reference/methods/usergroups.users.update)

* * *

[`users.profile:read`](/reference/scopes/users.profile.read)

* [`team.profile.get`](/reference/methods/team.profile.get)
* [`users.profile.get`](/reference/methods/users.profile.get)

* * *

[`users.profile:write`](/reference/scopes/users.profile.write)

* [`users.deletePhoto`](/reference/methods/users.deletePhoto)
* [`users.profile.set`](/reference/methods/users.profile.set)
* [`users.setPhoto`](/reference/methods/users.setPhoto)

* * *

[`users:read`](/reference/scopes/users.read)

* [`bots.info`](/reference/methods/bots.info)
* [`users.getPresence`](/reference/methods/users.getPresence)
* [`users.info`](/reference/methods/users.info)
* [`users.list`](/reference/methods/users.list)

* * *

[`users:read.email`](/reference/scopes/users.read.email)

* [`users.lookupByEmail`](/reference/methods/users.lookupByEmail)

* * *

[`users:write`](/reference/scopes/users.write)

* [`users.setActive`](/reference/methods/users.setActive)
* [`users.setPresence`](/reference/methods/users.setPresence)

[Browse all scopes](/reference/scopes)

## OAuth Scopes to Events API methods {#oauth-scopes-events}

OAuth scopes also govern subscriptions to [event types](/reference/events) in the [Events API](/reference/events).

## Slack app scopes {#slack-app-scopes}

If you're building a Slack app, you will also encounter three other scopes.

* `incoming-webhook` - requesting this scope during the authentication process allows workspaces to easily install an [incoming webhook](/messaging/sending-messages-using-incoming-webhooks) that can post from your app to a single Slack channel.
* `commands` - similarly, requesting this scope allows workspaces to install [slash commands](/interactivity/implementing-slash-commands) bundled in your Slack app.
* `bot` - request this scope when your Slack app includes [bot user](/legacy/legacy-bot-users) functionality. Unlike `incoming-webhook` and `commands`, the `bot` scope grants your bot user access to [a subset of Web API methods](/legacy/legacy-bot-users#api_usage), the [RTM API](/legacy/legacy-rtm-api), and certain [event types](/reference/events) in the [Events API](/apis/events-api/).

## Special scopes {#special-scopes}

Additionally, Slack supports the following special scopes:

* **identify** : Allows applications to confirm your identity.
* **client**: Allows applications to connect to slack as a client, and post messages on behalf of the user.
* **admin**: Allows applications to perform administrative actions, requires the authed user to be an admin.

## Working with Scopes {#working-with-scopes}

When making the initial authorization request, your application can request multiple scopes as a space or comma separated list (e.g. `teams:read users:read`).

```text
https://slack.com/oauth/authorize?    client_id=...&    scope=team%3Aread+users%3Aread
```text

When using the Slack API you can check the HTTP headers to see what OAuth scopes you have, and what the API method accepts.

```bash
curl https://slack.com/api/files.list -H "Authorization: Bearer xoxb-abc-1234" -IHTTP/1.1 200 OKx-oauth-scopes: files:read, chat:write, chat:write.publicx-accepted-oAuth-scopes: files:read
```text

`x-oauth-scopes` lists the scopes your token has authorized. `x-accepted-oAuth-scopes` lists the scopes that the action checks for.

Please note that **certain scopes cannot be asked for in combination with each other**. For instance, you cannot request both the `bot` scope and the `client` scope. When users arrive at an authorization page requesting invalid scope combinations, they'll see an ugly error stating something to this effect:

```text
    "OAuth error: invalid_scope: Cannot request service scope (bot) with deprecated scopes"
```text

## Deprecated Scopes {#deprecated-scopes}

The following scopes are deprecated and their use is strongly discouraged:

* `read`
* `post`
* `client`

### Alternatives to the read scope {#read}

This scope allows apps to read and inspect a wide range of data types.

Analyze which types of data your app needs and locate the accompanying scope in our [scope catalog](/reference/scopes).

For instance, if you need to read public channel history, request [`channels:history`](/reference/scopes/channels.history). If you need to read data _about_ public channels, request \[`channels:read`\].

You'll find a scope corresponding to almost all types of data you'll encounter on the Slack platform.

### Alternatives to the post scope {#post}

This scope allows posting messages into Slack.

Create a [Slack app](https://api.slack.com/apps) and request the [`chat:write`](/reference/scopes/chat.write) scope to use [`chat.postMessage`](/reference/methods/chat.postMessage) to send messages to channels.

### Alternatives to the client scope {#client}

This scope allows an app to retrieve all workspace events in real time.

We recommend using a combination of [relevant scopes](/reference/scopes) with the [Events API](/apis/events-api/) to retrieve just the events your app needs.

If you _must_ use the [RTM API](/legacy/legacy-rtm-api), you must use the [classic bot scope and token model](/reference/scopes/bot) with [`rtm.connect`](/reference/methods/rtm.connect) instead.

* * *

# Stream.io Documentation
# Source: https://getstream.io/chat/docs/moderation/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [React](/chat/docs/react/)

/

  * [Moderation for Chat](/chat/docs/react/moderation/)

# Moderation for Chat

Moderation is essential for a good user experience on chat. There are also
requirements from DSA and the app stores to take into account.

Stream has advanced AI moderation capabilities for text, images, video and
audio. Before we launched moderation, customers often struggled with the cost
and difficulty of integrating external moderation APIs. You can now setup
moderation in minutes at an affordable price point.

There are 4 layers of moderation:

  * **Limits / chat features** : Restrict whatâs allowed. Moderator permissions, disabling links or images, slow mode, enforce_unique_usernames, slash commands etc.
  * **Simple** : Blocklist, regex, domain allow/block, email allow/block
  * **User actions** : Flag, mute, ban etc.
  * **[AI moderation](/moderation/docs/)** : AI on text, images, video, audio

Letâs go over each of these and show whatâs supported.

## Limits & Chat features

### Disabling the permission to post links or add attachments

You can control links and attachments by revoking the relevant permissions for
a role. The permissions to manage are:

  * `add-links` \- ability to post messages containing URLs
  * `create-attachment` \- ability to add attachments to messages
  * `upload-attachment` \- ability to upload files/images

Update the grants for a channel type to remove these permissions from a role:

JavaScriptPythonPHPGo

    
    
    // Remove link and attachment permissions for channel_member role
    await client.updateChannelType("messaging", {
      grants: {
        channel_member: [
          "read-channel",
          "create-message",
          "update-message-owner",
          "delete-message-owner",
          // "add-links" - removed to disable links
          // "create-attachment" - removed to disable attachments
          // "upload-attachment" - removed to disable uploads
        ],
      },
    });
    
    
    # Remove link and attachment permissions for channel_member role
    client.update_channel_type("messaging", grants={
        "channel_member": [
            "read-channel",
            "create-message",
            "update-message-owner",
            "delete-message-owner",
            # "add-links" - removed to disable links
            # "create-attachment" - removed to disable attachments
            # "upload-attachment" - removed to disable uploads
        ],
    })
    
    
    // Remove link and attachment permissions for channel_member role
    $client->updateChannelType('messaging', [
      'grants' => [
        'channel_member' => [
          'read-channel',
          'create-message',
          'update-message-owner',
          'delete-message-owner',
          // 'add-links' - removed to disable links
          // 'create-attachment' - removed to disable attachments
          // 'upload-attachment' - removed to disable uploads
        ],
      ],
    ]);
    
    
    // Remove link and attachment permissions for channel_member role
    client.UpdateChannelType(ctx, "messaging", map[string]interface{}{
      "grants": map[string][]string{
        "channel_member": {
          "read-channel",
          "create-message",
          "update-message-owner",
          "delete-message-owner",
          // "add-links" - removed to disable links
          // "create-attachment" - removed to disable attachments
          // "upload-attachment" - removed to disable uploads
        },
      },
    })

For more details on permissions, see [User
Permissions](/chat/docs/react/chat_permission_policies/).

### Image & Video file types

You can restrict which file types users can upload using `image_upload_config`
and `file_upload_config`. This allows you to set allowed or blocked file
extensions and MIME types, as well as size limits.

Both configs accept the following fields:

Field| Description  
`allowed_file_extensions`| Array of allowed file extensions (e.g., `[".jpg",
".png"]`)  
`blocked_file_extensions`| Array of blocked file extensions  
`allowed_mime_types`| Array of allowed MIME types (e.g., `["image/jpeg",
"image/png"]`)  
`blocked_mime_types`| Array of blocked MIME types  
`size_limit`| Maximum file size in bytes (default allows up to 100MB)  
  
JavaScriptPythonGo

    
    
    // Restrict images to common formats only
    await client.updateAppSettings({
      image_upload_config: {
        allowed_file_extensions: [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        allowed_mime_types: ["image/jpeg", "image/png", "image/gif", "image/webp"],
        size_limit: 5 * 1024 * 1024, // 5MB
      },
      // Restrict file uploads to documents only
      file_upload_config: {
        allowed_file_extensions: [".pdf", ".doc", ".docx"],
        allowed_mime_types: ["application/pdf", "application/msword"],
        size_limit: 10 * 1024 * 1024, // 10MB
      },
    });
    
    
    # Restrict images to common formats only
    client.update_app_settings({
        "image_upload_config": {
            "allowed_file_extensions": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
            "allowed_mime_types": ["image/jpeg", "image/png", "image/gif", "image/webp"],
            "size_limit": 5 * 1024 * 1024,  # 5MB
        },
        # Restrict file uploads to documents only
        "file_upload_config": {
            "allowed_file_extensions": [".pdf", ".doc", ".docx"],
            "allowed_mime_types": ["application/pdf", "application/msword"],
            "size_limit": 10 * 1024 * 1024,  # 10MB
        },
    })
    
    
    // Restrict images to common formats only
    client.UpdateAppSettings(ctx, &UpdateAppSettingsRequest{
        ImageUploadConfig: &FileUploadConfig{
            AllowedFileExtensions: []string{".jpg", ".jpeg", ".png", ".gif", ".webp"},
            AllowedMimeTypes:      []string{"image/jpeg", "image/png", "image/gif", "image/webp"},
            SizeLimit:             5 * 1024 * 1024, // 5MB
        },
        FileUploadConfig: &FileUploadConfig{
            AllowedFileExtensions: []string{".pdf", ".doc", ".docx"},
            AllowedMimeTypes:      []string{"application/pdf", "application/msword"},
            SizeLimit:             10 * 1024 * 1024, // 10MB
        },
    })

For more details, see [App Settings](/chat/docs/react/app_setting_overview/).

### Giving moderators more permissions

Moderators have elevated permissions like the ability to ban users, delete
messages, and more. You can assign moderator roles to users at the channel
level or across all channels.

**Add a Moderator to a Channel:**

JavaScriptPythonRubyPHPGo

    
    
    // Add a member with moderator role
    await channel.addMembers([
      { user_id: "james_bond", channel_role: "channel_moderator" },
    ]);
    
    
    # Add a member with moderator role
    channel.add_members([{"user_id": "james_bond", "channel_role": "channel_moderator"}])
    
    
    # Add a member with moderator role
    channel.add_members([{'user_id' => 'james_bond', 'channel_role' => 'channel_moderator'}])
    
    
    // Add a member with moderator role
    $channel->addMembers([
      ['user_id' => 'james_bond', 'channel_role' => 'channel_moderator'],
    ]);
    
    
    // Assign moderator role
    a := []*RoleAssignment{{ChannelRole: "channel_moderator", UserID: "james_bond"}}
    resp, err = ch.AssignRole(ctx, a, nil)

**Make a User a Moderator Across All Channels:**

To grant a user moderator permissions across all channels in your app, update
their global role:

JavaScriptPythonPHPGo

    
    
    await client.partialUpdateUser({
      id: "james_bond",
      set: { role: "admin" },
    });
    
    
    client.update_user_partial(
      {"id": "james_bond", "set": {"role": "admin"}}
    )
    
    
    $client->partialUpdateUsers([
      'id' => 'james_bond',
      'set' => [
        'role' => 'admin',
      ],
    ]);
    
    
    client.PartialUpdateUser(ctx, &PartialUserUpdate{
      ID: "james_bond",
      Set: map[string]interface{}{
        "role": "admin",
      },
    })

For more details on permissions, see [User
Permissions](/chat/docs/react/chat_permission_policies/).

### Slow mode

Slow mode helps reduce noise on a channel by limiting users to a maximum of 1
message per cooldown interval (1-120 seconds). Moderators, admins, and server-
side API calls are not restricted.

KotlinJavaScriptSwiftPHPPythonJavaGo

    
    
    val channelClient = client.channel("messaging", "general")
    
    // Enable slow mode and set cooldown to 1s
    channelClient.enableSlowMode(cooldownTimeInSeconds = 1).enqueue { /* Result handling */ }
    
    // Increase cooldown to 30s
    channelClient.enableSlowMode(cooldownTimeInSeconds = 30).enqueue { /* Result handling */ }
    
    // Disable slow mode
    channelClient.disableSlowMode().enqueue { /* Result handling */ }
    
    
    // enable slow mode and set cooldown to 1s
    await channel.enableSlowMode(1);
    
    // increase cooldown to 30s
    await channel.enableSlowMode(30);
    
    // disable slow mode
    await channel.disableSlowMode();
    
    
    let channelController = client.channelController(for: .init(type: .messaging, id: "general"))
    
    channelController.enableSlowMode(cooldownDuration: 10)
    
    channelController.disableSlowMode()
    
    
    $update = $channel->update([ 'cooldown' => 30 ]); // 30 sec
    
    
    channel.update({ "cooldown": 30 }) # 30 sec
    
    
    // Enable slow mode and set cooldown to 1s
    channelClient.enableSlowMode(1).enqueue(result -> { /* Result handling */ });
    
    // Disable slow mode
    channelClient.disableSlowMode().enqueue(result -> { /* Result handling */ });
    
    
    channel.Update(ctx, map[string]interface{}{"cooldown": 30}, nil) // 30 sec

For more details, see [Slow Mode & Throttling](/chat/docs/react/slow_mode/).

### Enforce unique usernames

This setting prevents users from using duplicate usernames. When enabled with
`app`, it enforces uniqueness across the entire app. With `team`, it only
enforces within the same team.

JavaScriptPythonRubyPHPJavaGo

    
    
    // Enable uniqueness constraints on App level
    await client.updateAppSettings({
      enforce_unique_usernames: "app",
    });
    
    // Enable uniqueness constraints on Team level
    await client.updateAppSettings({
      enforce_unique_usernames: "team",
    });
    
    
    # Enable uniqueness constraints on App level
    client.update_app_settings(enforce_unique_usernames="app")
    
    # Enable uniqueness constraints on Team level
    client.update_app_settings(enforce_unique_usernames="team")
    
    
    # Enable uniqueness constraints on App level
    client.update_app_settings(enforce_unique_usernames: 'app')
    
    # Enable uniqueness constraints on Team level
    client.update_app_settings(enforce_unique_usernames: 'team')
    
    
    // Enable uniqueness constraints on App level
    $client->updateAppSettings(["enforce_unique_usernames" => "app"]);
    
    // Enable uniqueness constraints on Team level
    $client->updateAppSettings(["enforce_unique_usernames" => "team"]);
    
    
    // Enable uniqueness constraints on App level
    App.update().enforceUniqueUsernames("app").request();
    
    // Enable uniqueness constraints on Team level
    App.update().enforceUniqueUsernames("team").request();
    
    
    // Enable uniqueness constraints on App level
    settings := &AppSettings{EnforceUniqueUsernames: "app"}
    resp, err = client.UpdateAppSettings(ctx, settings)
    
    // Enable uniqueness constraints on Team level
    settings := &AppSettings{EnforceUniqueUsernames: "team"}
    resp, err = client.UpdateAppSettings(ctx, settings)

### Slash commands for banning

Stream Chat supports built-in slash commands like `/ban` and `/unban` for
quick moderation actions. Enable these commands on your channel type:

JavaScriptPythonRubyPHPJavaGo

    
    
    // Enable ban/unban commands for a channel type
    await client.updateChannelType("messaging", {
      commands: ["giphy", "ban", "unban", "mute", "unmute", "flag"],
    });
    
    
    # Enable ban/unban commands for a channel type
    client.update_channel_type(
      "messaging",
      commands=["ban", "unban", "mute", "unmute", "flag"],
    )
    
    
    # Enable ban/unban commands for a channel type
    client.update_channel_type(
      "messaging",
      commands: ["ban", "unban", "mute", "unmute", "flag"]
    )
    
    
    // Enable ban/unban commands for a channel type
    $client->updateChannelType('messaging', [
      'commands' => ['giphy', 'ban', 'unban', 'mute', 'unmute', 'flag']
    ]);
    
    
    // Enable ban/unban commands for a channel type
    ChannelType.update("messaging")
        .commands(List.of("ban", "unban", "mute", "unmute", "flag"))
        .request();
    
    
    // Enable ban/unban commands for a channel type
    client.UpdateChannelType(ctx, "messaging", map[string]interface{}{
      "commands": []interface{}{"ban", "unban", "mute", "unmute", "flag"},
    })

## Simple Moderation features

### Blocklist

A Blocklist is a list of words that you can use to moderate chat messages.
Stream Chat comes with a built-in Blocklist called `profanity_en_2020_v1`
which contains over a thousand of the most common profane words.

You can manage your own blocklists via the Stream dashboard or APIs to a
manage blocklists and configure your channel types to use them. Channel types
can be configured to block or flag messages from your users based on your
blocklists. To do this you need to configure your channel type(s) with these
two configurations: `blocklist` and `blocklist_behavior`. The first one refers
to the name of the blocklist and the second must be set as `block` or `flag` .

  * Applications can have up to 15 blocklists in total alongside advanced filters

  * A Blocklist can contain up to 10,000 words, each word can be up to 40 characters

  * The blocklist words must be in lowercase

  * Text matching is done with case insensitive word match (no prefix, post-fix support)

  * Messages are split into words using white spaces and hyphens (cookie-monster matches both âcookieâ and âmonsterâ)

So for instance, if you have a blocklist with the word âcreamâ these
messages will be blocked or flagged:

  * She jabbed the spoon in the ice cream and sighed

  * Cream is the best

and it will not affect any of these

  * Is creamcheese a word?

  * I did not enjoy watching Scream

The default blocklist contains material that many will find offensive.

#### Setup example

Blocklists can be managed using the APIs like any other Chat feature. Here is
a simple example on how to create a Blocklist and use it for a channel type.

JavaScriptPHPPythonRubyJavaGoC#

    
    
    // add a new blocklist for this app
    await client.createBlockList({
      name: "no-cakes",
      words: ["fudge", "cream", "sugar"],
    });
    
    // use the blocklist for all channels of type messaging
    await client.updateChannelType("messaging", {
      blocklist: "no-cakes",
      blocklist_behavior: "block",
    });
    
    
    // add a new blocklist for this app
    $client->createBlocklist(["no-cakes" => $name, "words" => ["fudge", "cream", "sugar"]]);
    
    
    # add a new blocklist for this app
    client.create_blocklist(name="no-cakes", words=["fudge", "cream", "sugar"])
    
    # use the blocklist for all channels of type messaging
    client.update_channel_type("messaging", blocklist="no-cakes", blocklist_behavior="block")
    
    
    # require 'stream-chat'
    
    # add a new blocklist for this app
    client.create_blocklist("no-cakes", words: ["fudge", "cream", "sugar"])
    
    # use the blocklist for all channels of type messaging
    client.update_channel_type("messaging", blocklist: "no-cakes", blocklist_behavior: "block")
    
    
    // add a new blocklist for this app
    Blocklist.create()
      .name("no-cakes")
      .words(List.of("fudge", "cream", "sugar"))
      .request();
    
    // use the blocklist for all channels of type messaging
    ChannelType.update("messaging")
      .blocklist("no-cakes")
      .blocklistBehavior(ChannelType.BlocklistBehavior.BLOCK)
      .request();
    
    
    // add a new blocklist for this app
    blocklistReq := &BlocklistCreateRequest{BlocklistBase{Name: "no-cakes", Words: []string{"fudge", "cream", "sugar"}}}
    client.CreateBlocklist(ctx, blocklistReq)
    
    // use the blocklist for all channels of type messaging
    client.UpdateChannelType(ctx, "messaging", map[string]interface{}{
     "blocklist": "no-cakes",
     "blocklist_behavior": "block",
    })
    
    
    // add a new blocklist for this app
    await blocklistClient.CreateAsync(new BlocklistCreateRequest
    {
      Name = "no-cakes",
      Words = new[] { "fudge", "cream", "sugar" },
    });
    
    // use the blocklist for all channels of type messaging

#### List available blocklists

All applications have the `profanity_en_2020_v1` blocklist available. This
endpoint returns all blocklists available for this application.

JavaScriptPHPPythonRubyJavaGoC#

    
    
    await client.listBlockLists();
    
    
    $client->listBlocklists();
    
    
    client.list_blocklists()
    
    
    client.list_blocklists()
    
    
    Blocklist.list().request();
    
    
    client.ListBlocklists(ctx)
    
    
    await blocklistClient.ListAsync();

#### Describe a blocklist

JavaScriptPHPPythonRubyJavaGoC#

    
    
    await client.getBlockList("no-cakes");
    
    
    $client->getBlocklist("no-cakes");
    
    
    client.get_blocklist("no-cakes")
    
    
    client.get_blocklist("no-cakes")
    
    
    Blocklist.get("no-cakes").request();
    
    
    c.GetBlocklist(ctx, "no-cakes")
    
    
    await blocklistClient.GetAsync("no-cakes");

#### Create new blocklist

JavaScriptPHPPythonRubyJavaGoC#

    
    
    const words = ["fudge", "cream", "sugar"];
    await client.createBlockList({
      name: "no-cakes",
      words,
    });
    
    
    $client->createBlocklist(["no-cakes" => $name, "words" => ["fudge", "cream", "sugar"]]);
    
    
    client.create_blocklist(name="no-cakes", words=["fudge", "cream", "sugar"])
    
    
    client.create_blocklist("no-cakes", words: ["fudge", "cream", "sugar"])
    
    
    Blocklist.create()
      .name("no-cakes")
      .words(List.of("fudge", "cream", "sugar"))
      .request();
    
    
    blocklistReq := &BlocklistCreateRequest{BlocklistBase{Name: "no-cakes", Words: []string{"fudge", "cream", "sugar"}}}
    client.CreateBlocklist(ctx, blocklistReq)
    
    
    await blocklistClient.CreateAsync(new BlocklistCreateRequest
    {
      Name = "no-cakes",
      Words = new[] { "fudge", "cream", "sugar" },
    });

#### Update a blocklist

JavaScriptPHPPythonRubyJavaGoC#

    
    
    await client.updateBlockList("no-cakes", {
      words: ["fudge", "cream", "sugar", "vanilla"],
    });
    
    
    $client->updateBlocklist("no-cakes", ["words" => ["fudge", "cream", "sugar", "vanilla"]]);
    
    
    client.update_blocklist("no-cakes", words=["fudge", "cream", "sugar", "vanilla"])
    
    
    client.update_blocklist("no-cakes", words: ["fudge", "cream", "sugar", "vanilla"])
    
    
    Blocklist.update("no-cakes")
      .words(List.of("fudge", "cream", "sugar", "vanilla"]))
      .request();
    
    
    client.UpdateBlocklist(ctx, "no-cakes", []string{"fudge", "cream", "sugar", "vanilla"})
    
    
    await blocklistClient.UpdateAsync("no-cakes", new[] { "fudge", "cream", "sugar", "vanilla" });

#### Delete a blocklist

When a blocklist is deleted, it will be automatically removed from all channel
types that were using it.

JavaScriptPHPPythonRubyJavaGoC#

    
    
    await client.deleteBlockList("no-cakes");
    
    
    $client->deleteBlocklist("no-cakes");
    
    
    client.delete_blocklist("no-cakes")
    
    
    client.delete_blocklist("no-cakes")
    
    
    Blocklist.delete("no-cakes").request();
    
    
    client.DeleteBlocklist(ctx, "no-cakes")
    
    
    await _blocklistClient.DeleteAsync("no-cakes");

### Regex

Regex filters allow you to match and moderate messages using regular
expressions. This is useful for filtering patterns like phone numbers, URLs,
or complex word variations. Configure regex filters via the Stream dashboard
under âBlocklist & Regex Filtersâ.

For detailed configuration, see [Regex, Email, and Domain
Filters](/moderation/docs/engines/blocklists-and-regex-filters/).

### Email/domain allow or block

You can configure domain and email filters to control what URLs and email
addresses can be shared in messages. Set up allowlists or blocklists for
specific domains via the Stream dashboard.

For detailed configuration, see [Regex, Email, and Domain
Filters](/moderation/docs/engines/blocklists-and-regex-filters/).

## User Actions

### Flag

Any user can flag a message or user. Flagged content is added to your
moderation review queue on the Stream Dashboard.

KotlinJavaScriptSwiftPythonRubyGoUnity

    
    
    client.flagMessage(
      messageId = "message-id",
      reason = "This message is inappropriate",
      customData = mapOf("extra_info" to "more details"),
    ).enqueue { result ->
      if (result.isSuccess) {
        val flag: Flag = result.data()
      } else {
        // Handle result.error()
      }
    }
    
    client.flagUser(
      userId = "user-id",
      reason = "This user is a spammer",
      customData = mapOf("extra_info" to "more details"),
    ).enqueue { result ->
      if (result.isSuccess) {
        val flag: Flag = result.data()
      } else {
        // Handle result.error()
      }
    }
    
    
    // Flag a message
    const flag = await client.flagMessage(messageId);
    
    // Flag with a reason and custom data
    const flag = await client.flagMessage(messageId, {
      reason: "spammy_user",
      custom: {
        user_comment: "This user is spamming.",
      },
    });
    
    
    import StreamChat
    
    let messageController = chatClient.messageController(cid: channelId, messageId: messageId)
    
    messageController.flag { error in
      print(error ?? "message flagged")
    }
    
    // Flag a user
    let userController = chatClient.userController(userId: "another_user")
    userController.flag { error in
      print(error ?? "user flagged")
    }
    
    
    client.flag_message(msg["id"], user_id=server_user["id"])
    
    
    @client.flag_message(msg_id, user_id: server_user[:id])
    
    
    client.FlagMessage(ctx, msg.ID, user.ID)
    
    
    // Flag a message
    await message.FlagAsync();
    
    // Flag a user
    await channelMember.User.FlagAsync();

#### Reasons & custom data

You can enhance flags by associating them with a specific reason and custom
data. It is advisable to utilise a slug or keyword as a designated reason for
easy translation or other forms of display customisation.

The custom data can encompass any object, offering supplementary metadata to
the flag.

The Query Message Flags endpoint retrieves both reasons and custom data, and
the reason can also be utilised for filtering these flags.

JavaScriptSwift

    
    
    // flag with a reason
    let flag = await client.flagMessage(messageID, {
      reason: "spammy_user",
    });
    
    // flag with a reason and additional custom data
    flag = await client.flagMessage(messageID, {
      reason: "spammy_user",
      custom: {
        user_comment: "This user is spamming the homepage.",
        page: "homepage",
      },
    });
    
    // flag with only custom data
    flag = await client.flagMessage(messageID, {
      custom: {
        page: "homepage",
      },
    });
    
    
    // flag with a reason
    messageController.flag(reason: "spammy_user")

#### Query Flagged Messages

If you prefer to build your own in-app moderation dashboard, rather than use
the Stream dashboard, you can query flagged messages using the
`QueryReviewQueue` API endpoint.

Both server-authenticated and user-authenticated clients can use this method.
For client-side requests, the user needs moderator or admin permissions.

JavaScript

    
    
    const response = await client.moderation.queryReviewQueue(
      { entity_type: "stream:chat:v1:message" },
      [{ field: "created_at", direction: -1 }],
      { next: null },
    );
    
    for (const item of response.items) {
      console.log(item.message.id);
      console.log(item.message.text);
      console.log(item.message.type);
      console.log(item.message.created_at);
    }
    
    console.log(next); // <-- next cursor for pagination

Please refer to the [Moderation API](/moderation/docs/api/#query-review-queue)
documentation for more details.

### Mute

Users can mute other users. Mutes are stored at the user level and returned
when `connectUser` is called. Messages from muted users are still delivered
via websocket but not via push notifications.

See [Mute in the Moderation API](/moderation/docs/api/flag-mute-ban/#mute) for
full documentation and SDK examples.

### Block

The user block feature allows users to control their 1-on-1 interactions
within the chat application by blocking other users.

    
    
    await client.blockUser("user-to-block");

#### How blocking impacts chat

When a user is blocked, several changes occur:

  * **Direct Communication Termination** : When a user blocks another user, communication in all 1-on-1 channels are hidden for the blocking user.
  * **Adding to Channels** : If a blocked user tries to add the blocking user to a channel as a member, the action is ignored. The channel will not include the blocking user but will have the remaining members.
  * **Push Notifications** : The blocking user will not receive push notifications from blocked users for 1-on-1 channels.
  * **Channel Events** : The blocking user will not receive any events from blocked users in 1-on-1 channels (e.g., message.new).
  * **Group Channels** : Group channels are unaffected by the block. Both the blocking and blocked users can participate, receive push notifications, and events in group channels.
  * **Query Channels** : When hidden channels are requested, 1-on-1 channels with blocked users will be returned with a `blocked:true` flag and all the messages.
  * **Active Chats and Unread Counts** : Blocked users will not appear in the blocking userâs list of active chats. Messages from blocked users will not contribute to unread counts.
  * **Unblocking Users** : After unblocking, all previous messages in 1-on-1 channels become visible again, including those sent during the block period.
  * **Hidden Channels** : Channels with only the blocked and blocking users are marked as hidden for the blocking user by default. If a blocked user sends a message in a hidden channel, the channel remains hidden for the blocking user.
  * **Group Channel Messages** : Messages from blocked users will still appear when retrieving messages from a group channel.
  * **WebSocket Connection** : When connecting to the WebSocket, the blocking user receives a list of users they have blocked (user.blocked_users). This is only available for the blocking userâs own account.
  * **Message Actions** : Actions such as sending, updating, reacting to, and deleting messages will still work in blocked channels. However, since the channels are hidden, these actions will not be visible to the blocking user.

#### Block User

Any user is allowed to block another user. Blocked users are stored at the
user level and returned with the rest of the user information when connectUser
is called. A user will be blocked until the user is unblocked.

JavaScriptKotlinSwift

    
    
    await client.blockUser("user-to-block");
    
    
    client.blockUser("user-to-block-id").enqueue { /* ... */ }
    
    
    chatClient.userController(userId: userToBlock.id).block { error in ... }

#### Unblock user

JavaScriptKotlinSwift

    
    
    await client.unBlockUser(blockedUser);
    
    
    client.unblockUser("user-to-unblock-id").enqueue { /* ... */ }
    
    
    chatClient.userController(userId: userToUnblock.id).unblock { error in ... }

#### List of Blocked Users

JavaScriptKotlinSwift

    
    
    const resp = await client.getBlockedUsers();
    
    
    client.queryBlockedUsers().enqueue { result ->
        if (result is Result.Success) {
            val blockedUsers: List<UserBlock> = result.value
        } else {
            // Handle Result.Failure
        }
    }
    
    
    chatClient.currentUserController().loadBlockedUsers { result in
      switch result {
      case .success(let blockedUsers):
        // Handle success
      case .failure(let error):
        // Handle error
      }
    }

#### Server Side

**Block User:**

JavaScriptGoC#Java

    
    
    const blockingUser = "user1";
    const blockedUser = "user2";
    await ctx.createUsers([blockingUser, blockedUser]);
    const serverClient = await ctx.serverClient();
    
    await serverClient.blockUser(blockedUser, blockingUser);
    const resp = await serverClient.getBlockedUsers(blockingUser);
    
    
    resp, err := client.BlockUser(ctx, blockedUserID, blockingUserID)
    
    
    await userClient.BlockUserAsync(user2.Id, user1.Id);
    
    
    BlockUser.BlockUserResponse blockResponse = BlockUser.blockUser()
      .blockedUserID(blockedUserId)
      .userID(blockingUserId)
      .request();

**Unblock user:**

JavaScriptGoC#Java

    
    
    await serverClient.unBlockUser(blockedUser, blockingUser);
    
    
    resp, err := client.UnblockUser(ctx, blockedUserID, blockingUserID)
    
    
    await userClient.UnblockUserAsync(user2.Id, user1.Id);
    
    
    BlockUser.UnblockUserResponse unblockResponse = BlockUser.unblockUser()
      .blockedUserID(blockedUserId)
      .userID(blockingUserId)
      .request();

**Get List of Blocked Users:**

JavaScriptGoC#Java

    
    
    const resp = await client.getBlockedUsers(blockingUser);
    
    
    getRes, err := client.GetBlockedUser(ctx, blockingUserID)
    for _, blockedUser := getRes.BlockedUsers{
    	fmt.Println(blockedUser.BlockedUserID)
    }
    
    
    await userClient.GetBlockedUsersAsync(user1.Id);
    
    
    BlockUser.GetBlockedUsersResponse getBlockedUsersResponse = BlockUser.getBlockedUsers(blockingUserId).request();

## AI moderation

AI moderation can detect over 40 harms in 50+ different languages. In addition
to these classification models LLM based moderation is also supported.
Moderation APIs are available at additional costs. Itâs priced to be cost-
effective and typically is a fraction of the cost of other moderation APIs.

[Read the full AI moderation docs](/moderation/docs/).

## Ban

Users can be banned from an app entirely or from a channel. When banned, they
cannot post messages until the ban is removed or expires. You can also apply
IP bans and optionally delete the userâs messages.

See [Ban in the Moderation API](/moderation/docs/api/flag-mute-ban/#ban) for
full documentation, including shadow bans, query endpoints, and SDK examples.

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousOverview](/chat/docs/react/best_practices/)[NextMarketplace
Apps](/chat/docs/react/marketplace_best_practices/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/react/moderation.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/moderation.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/moderation.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/moderation.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/moderation.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/moderation.md)

On this page:

  * Limits & Chat features

    * Disabling the permission to post links or add attachments
    * Image & Video file types
    * Giving moderators more permissions
    * Slow mode
    * Enforce unique usernames
    * Slash commands for banning

  * Simple Moderation features

    * Blocklist
    * Regex
    * Email/domain allow or block

  * User Actions

    * Flag
    * Mute
    * Block

  * AI moderation
  * Ban

Is this helpful?

Thank you .

An error has occurred.
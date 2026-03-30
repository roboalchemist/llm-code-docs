# Source: https://developers.buffer.com/reference.md

# Buffer GraphQL API Reference

> Complete API reference documentation

API Endpoint: https://api.buffer.com
Authentication: Bearer token via Authorization header

## Queries

#### account

Retrieves the authenticated user's account information

**Returns:** `Account!`

#### channel

Fetches a single channel using the provided ID

**Returns:** `Channel!`

**Arguments:**
- `input`: `ChannelInput!` - Query's input.

#### channels

Fetch all channels for the organization taking into account the current's user permissions

**Returns:** `[Channel!]!`

**Arguments:**
- `input`: `ChannelsInput!` - Query's input.

#### post

Fetches a post by PostID for the given organization: first and last can be set for forward pagination using Relay convention

**Returns:** `Post!`

**Arguments:**
- `input`: `PostInput!` - Query's input.

#### posts

Fetches posts for the given organization: first and last can be set for forward pagination using Relay convention

**Returns:** `PostsResults!`

**Arguments:**
- `input`: `PostsInput!` - Query's input.
- `first`: `Int` - The number of posts to return
- `after`: `String` - The cursor of the post to start fetching from

## Mutations

#### createIdea

Create a new idea with the given content and metadata

**Returns:** `CreateIdeaPayload!`

**Arguments:**
- `input`: `CreateIdeaInput!` - Input to create an idea

#### createPost

Create post for channel

**Returns:** `PostActionPayload!`

**Arguments:**
- `input`: `CreatePostInput!` - The mutation's input

## Object Types

#### Account

Account is a representation of a Buffer user.

**Fields:**
- `id`: `ID!` - Unique identifier for the account
- `email`: `String!` - Primary email address for the account
- `backupEmail`: `String` - Backup email address for account recovery
- `avatar`: `String!` - URL to the account's avatar image
- `createdAt`: `DateTime` - Date the account was created in the Core DB. For older customers, it's possible a Publish account existed in the Publish DB for this customer before this date
- `organizations`: `[Organization!]!`
  - Arg `filter`: `OrganizationFilterInput`
- `timezone`: `String` - The account-level timezone - this is used as a default input for streaks, posting plans, and new channel channel connections.
- `name`: `String` - The account name, different from the organization name
- `preferences`: `Preferences` - The accounts preferences
- `connectedApps`: `[ConnectedApp!]` - The connected apps for the account

#### Annotation

Annotation representing all the entities in the text

**Fields:**
- `type`: `AnnotationType!` - The type of the annotation
- `indices`: `[Int!]!` - The indices of the annotation in the text
- `content`: `String!` - The content of the annotation. Annotations can sometimes be different from the actual text content.
E.g., Mastodon mentions have 'text: @buffer', but includes the server name in the content, 'content: @buffer@threads.net'
- `text`: `String!` - The text representation of the annotation, eg '@buffer'
- `url`: `String!` - The URL the annotation points to

#### Author

Represent the author of a post or note.

**Fields:**
- `id`: `AccountId!` - The unique identifier of the author.
- `email`: `String!` - The email address of the author.
- `avatar`: `String!` - The avatar URL of the author.
- `isDeleted`: `Boolean!` - Indicates whether the author is a deleted.
- `name`: `String` - The name of the author. Null if the user has not yet set a name.

#### BlueskyMetadata

Bluesky metadata

**Fields:**
- `serverUrl`: `String!` - The instance of bluesky of the channel

#### BlueskyPostMetadata

Bluesky post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts
- `linkAttachment`: `LinkAttachment` - Link attachment

#### Channel

Channel entity

**Fields:**
- `id`: `ChannelId!` - The ID of the channel
Source: mapper from channel collection - channel._id
Defined in: both proposals
- `allowedActions`: `[ChannelAction!]!` - The allowed actions for the current user
Source: field resolver
Defined in: new proposal
- `scopes`: `[String]!` - Scopes requested for a given channel - empty array if we don't have them tracked
Source: mapper from channel collection - channel.credentials.scopes
Defined in: current implementation
- `avatar`: `String!` - The avatar URL of the channel
Source: mapper from channel collection - channel.avatar
Defined in: both proposals
- `createdAt`: `DateTime!` - The creation date of the channel
Source: mapper from channel collection - channel.createdAt
Defined in: both proposals
- `descriptor`: `String!` - Formatted name of the channel service and type: e.g. 'Twitter Profile' or 'Facebook Page'
Source: mapper from channel collection - channel.service and channel.type
Defined in: current implementation
- `displayName`: `String` - The display name of the channel - nullable (reason?)
Source: mapper from channel collection - channel.displayName
Defined in: current implementation
- `isDisconnected`: `Boolean!` - Indicates if the channel is properly connected to Buffer
Source: mapper from channel collection - channel.credentials.invalid
Defined in: both proposals
- `isLocked`: `Boolean!` - Indicates if the channel is locked - Locked channels can't be used for posting.
A channel can be locked when the organization downgrades and reduces the channel quantity of their plan.
Source: mapper from channel collection - channel.isLocked
Defined in: both proposals
- `isNew`: `Boolean!` - Indicates if the channel was recently created (in less than 10 seconds). This is used to determine the redirect modal after channel authorization
Source: mapper from channel collection - channel.createdAt comparison with current time
Defined in: current implementation
- `postingSchedule`: `[ScheduleV2!]!` - Provides the posting slots for each day of the week
Source: field resolver based on profiles collection - getPostingSchedule
- `isQueuePaused`: `Boolean!` - Indicates is the queue is paused for the channel. A paused queue means schedules posts won't be published.
Source: Field resolver - From profiles collection - profile.paused
Defined in: new proposal
- `showTrendingTopicSuggestions`: `Boolean!` - Indicates if trending topic suggestions should be shown in the composer.
When false, users can still access trends via the trending icon button.
Defaults to true for backward compatibility.
Source: Field resolver - From profiles collection - profile.show_trending_topic_suggestions
- `metadata`: `ChannelMetadata` - Metadata or settings depending on the service type - such as the server URL for Mastodon or Location data for Facebook/GPB
Source: Field resolver - From channel collection: channel.locationData + channel.serverURL | profile collection: profile.default_to_reminder
Defined in: new proposal
- `name`: `String!` - The name of the channel - the handle name, username, etc.
Source: mapper from channel collection - channel.name
Defined in: both proposals
- `organizationId`: `OrganizationId!` - The organization ID of the channel
Source: mapper from channel collection - channel.organizationId
Defined in: both proposals
- `products`: `[Product!]` - Products that support a given channel
- `service`: `Service!` - Represents the social network
Source: mapper from channel collection - channel.serviceType
Defined in: both proposals
- `serviceId`: `String!` - Represents the external ID of the channel on social network API
Source: mapper from channel collection - channel.serviceId
Defined in: both proposals
- `timezone`: `String!` - The timezone of the channel - Default if not set is Europe/London
Source: field resolver based on profiles collection - timezone
Defined in: both proposals
- `type`: `ChannelType!` - The type of the channel - Page, Profile, Business, Group, Account, etc.
Source: mapper from channel collection - channel.type
Defined in: both proposals
- `updatedAt`: `DateTime!` - The last time the channel was updated
Source: mapper from channel collection - channel.updatedAt
Defined in: both proposals
- `hasActiveMemberDevice`: `Boolean!` - Whether at least one member of the orginization who have access to this channel
also has a user device registered for push notifications
- `postingGoal`: `PostingGoal` - The posting goal for the channel
- `externalLink`: `String` - The channel's URL on the social network (e.g. instagram.com/username or facebook.com/page)
Source: field resolver
Returns null if the channel is not supported
- `linkShortening`: `ChannelLinkShortening!` - Link Shortening settings for the channel
- `weeklyPostingLimit`: `WeeklyPostingLimit` - Weekly posting limit for the channel *(Deprecated: This field is not used anymore)*

#### ChannelLinkShortening

Settings for link shortening

**Fields:**
- `config`: `LinkShorteningConfig` - Configuration of link shortening integration. Null if disabled.
- `isEnabled`: `Boolean!` - If link shortening is enabled for the channel

#### ConnectedApp

Connected App

**Fields:**
- `clientId`: `ID!` - The id of the connectedApp.
- `userId`: `ID!` - The id of the user that has granted access to the app.
- `name`: `String!` - The name of the connected app.
- `description`: `String!` - A brief description of the connected app.
- `website`: `String!` - The website URL of the connected app.
- `createdAt`: `DateTime!` - The date and time when the connected app was created.

#### DocumentAsset

Document asset

**Implements:** Asset

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset
- `document`: `DocumentMetadata!` - Document specific metadata

#### DocumentMetadata

Document metadata

**Fields:**
- `filesize`: `Int` - Document fileSize in bytes
- `numPages`: `Int!` - Number of pages in the document
- `thumbnails`: `[String!]!` - URLs to the static thumbnails of the document pages

#### FacebookMetadata

Facebook metadata

**Fields:**
- `locationData`: `LocationData` - Metadata about the location of the business associated with the channel. Only available for Facebook and GPB

#### FacebookPostMetadata

Facebook post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `linkAttachment`: `LinkAttachment` - Link attachment
- `title`: `String` - Title of Facebook reel
- `firstComment`: `String` - Facebook post's first comment

#### GoogleBusinessEventMetaData

Metadata for a GBP post that is an event

**Fields:**
- `title`: `String!` - Title of the event
- `startDate`: `DateTime!` - Start date of the event
- `endDate`: `DateTime!` - End date of the event
- `startTime`: `String` - Start time of the event *(Deprecated: get time from the startDate)*
- `endTime`: `String` - End time of the event *(Deprecated: get time from the endDate)*
- `isFullDayEvent`: `Boolean!` - Indicate whether the event has a start or end time.
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### GoogleBusinessMetadata

Google Business metadata

**Fields:**
- `locationData`: `LocationData` - Metadata about the location of the business associated with the channel. Only available for Facebook and GPB

#### GoogleBusinessOfferMetaData

Metadata for a GBP post that is an offer

**Fields:**
- `title`: `String!` - Title of the offer
- `startDate`: `DateTime!` - Start date of the offer
- `endDate`: `DateTime!` - End date of the offer
- `code`: `String` - Coupon code for the offer
- `link`: `String` - Link to the offer
- `terms`: `String` - Terms and Conditions

#### GoogleBusinessPostMetadata

Google Business Profile post metadata
@deprecated: pending proposal for specific GBP post types: update, offer and event metadata types

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `title`: `String` - Title if available in the given GBP post type: event and offer
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `details`: `GoogleBusinessPostDetails` - Details of the metadata

#### GoogleBusinessWhatsNewMetaData

Metadata for a GBP post of type Whats new

**Fields:**
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### Idea

Ideas are the main entity in the create space

**Fields:**
- `id`: `ID!` - Unique identifier for the idea
- `organizationId`: `ID!` - ID of the organization that owns this idea
- `content`: `IdeaContent!` - The actual content and metadata of the idea
- `groupId`: `ID` - ID of the group this idea belongs to (if any)
- `position`: `Float` - Numerical position for ordering within a group
- `createdAt`: `Int!` - Unix timestamp of when the idea was created
- `updatedAt`: `Int!` - Unix timestamp of when the idea was last modified

#### IdeaContent

Content of an idea

**Fields:**
- `title`: `String` - Title or headline of the idea
- `text`: `String` - Main body text or description of the idea
- `media`: `[IdeaMedia!]` - List of media items attached to the idea
- `tags`: `[PublishingTag!]!` - Tags used to categorize and organize the idea
- `aiAssisted`: `Boolean!` - Indicates whether AI tools were used in creating this idea
- `services`: `[Service!]!` - Services tagged by the user - this is typically used to annotate ideas with their target services
- `date`: `DateTime` - DateTime set by user associated with the idea - this often reflects a target publish date.

#### IdeaMedia

Media attached to an idea

**Fields:**
- `id`: `ID!` - Unique identifier for the media in Buffer's upload system
- `url`: `String!` - Direct URL to access the media file
- `alt`: `String` - Alternative text description for accessibility
- `thumbnailUrl`: `String` - URL to a smaller version of the media for preview purposes
- `type`: `MediaType!` - Type of media (e.g., image, video, gif)
- `size`: `Int` - File size in bytes
- `source`: `IdeaMediaSource` - Source platform information for the media

#### IdeaMediaSource

Media source for the idea, e.g. Unsplash, Gifphy, etc.

**Fields:**
- `name`: `String!` - Name of the media source platform (e.g., 'Unsplash', 'Giphy')
- `id`: `String` - Unique identifier from the source platform
- `author`: `String` - Name of the content creator/author
- `authorUrl`: `String` - URL to the author's profile on the source platform

#### IdeaResponse

createIdea response type

**Fields:**
- `idea`: `Idea` - The affected idea
- `refreshIdeas`: `Boolean!` - If true, the client should refresh the ideas list because other ideas might have been moved

#### ImageAsset

Image asset

**Implements:** Asset

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset
- `image`: `ImageMetadata!` - Image specific metadata

#### ImageMetadata

Image metadata

**Fields:**
- `altText`: `String!` - Alternative text for accessibility
- `width`: `Int!` - Image width in pixels
- `height`: `Int!` - Image height in pixels
- `isAnimated`: `Boolean!` - Is the image animated?
- `animatedThumbnail`: `String` - Animated thumbnail URL
- `userTags`: `[UserTag!]` - User tags in the image

#### InstagramGeolocation

Instagram Geolocation

**Fields:**
- `id`: `String` - The id of this location
- `text`: `String` - The name of this location

#### InstagramMetadata

Instagram metadata

**Fields:**
- `defaultToReminders`: `Boolean!` - Indicates if we should default to reminder for Instagram
Source: field resolver: profile.default_to_reminders

#### InstagramPostMetadata

Instagram post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `firstComment`: `String` - Instagram post's first comment
- `link`: `String` - Shop Grid link for the post
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `geolocation`: `InstagramGeolocation` - Geolocation of the post
- `shouldShareToFeed`: `Boolean!` - Indicates whether post should be shared to feed
- `stickerFields`: `InstagramStickerFields` - Sticker fields for reminder-based publishing

#### InstagramStickerFields

Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user
is prompted to copy and paste these fields into the Instagram app to complete the post.

**Fields:**
- `text`: `String` - Text for the Story or Reel
- `music`: `String` - Placeholder text for the post's music
- `products`: `String` - Placeholder text for the post's linked products
- `topics`: `String` - Placeholder text for the post's topics (Reels only)
- `other`: `String` - Additional field for any other post content

#### InvalidInputError

Error returned when the input is invalid

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### LimitReachedError

Error returned when the limit is reached

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### LinkAttachment

Link attachment

**Implements:** ScrapedLink

**Fields:**
- `url`: `String!` - URL that the link asset has been built from
- `expandedUrl`: `String` - Full URL that the link asset has been built from
- `text`: `String!` - Description for the scraped link
- `thumbnails`: `[String!]!` - Thumbnails of media available in the link
- `thumbnail`: `String` - Selected thumbnail for this link preview
- `title`: `String!` - Title for the link attachment

#### LinkedInMetadata

LinkedIn metadata

**Fields:**
- `shouldShowLinkedinAnalyticsRefreshBanner`: `Boolean!` - Property parsed from scopes indicating whether the client should show the LinkedIn analytics refresh banner

#### LinkedInPostMetadata

LinkedIn post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `firstComment`: `String` - LinkedIn post's first comment
- `linkAttachment`: `LinkAttachment` - Link attachment

#### LinkShorteningConfig

Link Shortening Configuration

**Fields:**
- `domain`: `String!` - Domain of the link shortener - eg buff.ly, dub.co,
or the user's custom domain.
- `name`: `String!` - Human readable string to describe the link shortening
service.

#### LocationData

Location data about the channel

**Fields:**
- `location`: `String` - Location of the business associated with the channel
- `mapsLink`: `String` - Link to the map
- `googleAccountId`: `String` - Google Account Id of the business

#### MastodonMetadata

Mastodon metadata

**Fields:**
- `serverUrl`: `String!` - The instance of mastodon of the channel

#### MastodonPostMetadata

Mastodon post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts
- `spoilerText`: `String` - Spoiler text hiding the root text of this post

#### MemberConnection

Represents the members connection edge. Later, we can add the list of members with the page info to follow our connection edge pattern.

**Fields:**
- `totalCount`: `Int!` - The total count of team members counting the org owner and team members from the Publish DB.

#### Note

Note entity

**Fields:**
- `id`: `NoteId!` - The unique identifier of the note.
- `text`: `String!` - The content of the note.
- `type`: `NoteType!` - The type of the note.
- `author`: `Author!` - The author of the note - null if the user is deleted or left the organization.
- `createdAt`: `DateTime!` - The date and time when the note was created.
- `updatedAt`: `DateTime` - The date and time when the note was last edited.
- `allowedActions`: `[NoteAction!]!` - The allowed actions a user can perform on the note.

#### NotFoundError

Error returned when the resource is not found

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### Organization

Organization is a representation of a Buffer Organization.

**Fields:**
- `id`: `OrganizationId!` - The ID of the organization.
- `channelCount`: `Int!` - The total number of channels connected to the organization.
- `limits`: `OrganizationLimits!` - The limits of the organization. Can be used to check if the organization has reached the limit of channels, members, etc.
- `members`: `MemberConnection!` - The members of the organization. Can be used to check the total number of members in the organization. In the future, it might contain more information about the members.
- `name`: `String!` - The name of the organization.
- `ownerEmail`: `String!` - The owner email of the organization.

#### OrganizationLimits

Resource limits for an organization including channels, members, and content limits

**Fields:**
- `channels`: `Int!`
- `members`: `Int!`
- `scheduledPosts`: `Int!`
- `scheduledThreadsPerChannel`: `Int!`
- `scheduledStoriesPerChannel`: `Int!`
- `generateContent`: `Int!`
- `tags`: `Int!`
- `ideas`: `Int!`
- `ideaGroups`: `Int!`
- `savedReplies`: `Int!`

#### PaginationPageInfo

Information to aid in pagination.

**Fields:**
- `startCursor`: `String` - The first cursor in the list. It can be used to fetch the previous page.
- `endCursor`: `String` - The last cursor in the list. It can be used to fetch the next page.
- `hasPreviousPage`: `Boolean!` - When set to true, it means there is a previous page available. Will always return false for now as we only support forward pagination.
- `hasNextPage`: `Boolean!` - When set to true, it means there is a next page available.

#### PinterestBoard

A Pinterest board

**Fields:**
- `id`: `String!` - The ID of the board
- `serviceId`: `String!` - The ID of the service
- `name`: `String!` - The board name
- `url`: `String!` - The board URL
- `description`: `String` - The board description
- `avatar`: `String` - The board avatar

#### PinterestMetadata

Pinterest metadata

**Fields:**
- `boards`: `[PinterestBoard!]!` - The list of boards the user has on Pinterest

#### PinterestPostMetadata

Pinterest post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `title`: `String` - The title of the Pin
- `url`: `String` - The Pin destination link
- `board`: `PinterestBoard` - The board the Pin is saved to
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text

#### Post

Post entity

**Fields:**
- `id`: `PostId!` - ObjectId of the post
- `ideaId`: `IdeaId` - Is set when the Post is generated from an Idea
- `status`: `PostStatus!` - status
- `via`: `PostVia!` - Indicates if the post is created from Buffer or the API
- `schedulingType`: `SchedulingType` - Scheduling type can be null if the post was created natively on the social network without using notification publishing or automatic publishing
- `author`: `Author` - Represents the user who created the post
- `isCustomScheduled`: `Boolean!` - Indicates whether time to publish was manually selected by the user
- `createdAt`: `DateTime!` - Date when the post was created
- `updatedAt`: `DateTime!` - Date when the post was updated
- `dueAt`: `DateTime` - Date when the post is scheduled to be published
- `sentAt`: `DateTime` - Date when the post is published
- `text`: `String!` - Text content of the Post
- `externalLink`: `String` - The external URL of the post at the destination service
- `metadata`: `PostMetadata` - Metadata of the post which differs based on the social network/service
@see post.metadata.graphql
- `channelId`: `ChannelId!` - channel ID (faster than resolving the channnel.id)
- `channelService`: `Service!` - channel service (faster than resolving the channnel.service)
- `channel`: `Channel!` - channel
- `tags`: `[Tag!]!` - tags - sorted by name in ascending order
- `notes`: `[Note!]!` - notes
- `notificationStatus`: `NotificationStatus` - notificationStatus: notified or markedAsPublished
- `error`: `PostPublishingError` - error
- `assets`: `[Asset!]!` - assets
- `allowedActions`: `[PostAction!]!` - Indicates what actions the current account can perform on the post
- `sharedNow`: `Boolean!` - Indicates whether the post was shared via publish now action
- `shareMode`: `ShareMode!` - Indicates the share mode of the post (e.g., addToQueue, shareNext, shareNow, customScheduled)

#### PostActionSuccess

Success response returns the full up-to-date post from after the action was performed.

**Fields:**
- `post`: `Post!` - Post on which the action was successfully performed.

#### PostingGoal

Represents a posting goal for a channel, including target, progress, and status information.

**Fields:**
- `goal`: `Int!` - The target number of posts for this goal.
- `sentCount`: `Int!` - The number of posts that have been sent (published or ingested) for this goal.
- `scheduledCount`: `Int!` - The number of posts that are scheduled to be sent for this goal.
- `status`: `PostingGoalStatus!` - The current status of the posting goal.
- `periodStart`: `DateTime!` - The start date of the period for this posting goal.
- `periodEnd`: `DateTime!` - The end date of the period for this posting goal.

#### PostPublishingError

Post publishing error

**Fields:**
- `message`: `String!` - Error message to display
- `supportUrl`: `String` - Link to a help center article to help resolve the error
- `rawError`: `String` - The original error from the publishing service (internal use only)

#### PostsEdge

Represent a node in the pagination result using the Connect Relay convention.

**Fields:**
- `node`: `Post!` - Represents the current post in the list.
- `cursor`: `String!` - Opaque cursor to be used in pagination to fetch from current node.

#### PostsResults

Results for the posts query.

**Fields:**
- `edges`: `[PostsEdge!]` - The list of posts that match the query.
- `pageInfo`: `PaginationPageInfo!` - Information to aid in pagination.

#### Preferences

Account preferences

**Fields:**
- `timeFormat`: `String`
- `startOfWeek`: `String`
- `defaultScheduleOption`: `ScheduleOption!`

#### PublishingTag

Tag associated with a post

**Fields:**
- `id`: `ID!`
- `color`: `String!` - Hex color for tag e.g #F523F1
- `name`: `String!`

#### RestProxyError

Error proxied from the REST API response

**Implements:** MutationError

**Fields:**
- `message`: `String!` - An error message from the REST API response that we proxied here
- `link`: `String` - Link to our Help center from the REST API response
- `code`: `Int` - Error code from the REST API response - https://buffer.com/developers/api/errors

#### RetweetMetadata

Information about the initial Tweet that was retweeted

**Implements:** ScrapedLink

**Fields:**
- `id`: `String!` - Retweet ID
- `url`: `String!` - Link to original tweet
- `text`: `String!` - Text of the original tweet
- `createdAt`: `DateTime!` - Date when the original tweet was created
- `user`: `RetweetUserMetadata!` - User who created the original tweet
- `thumbnails`: `[String!]!` - Thumbnails to media available in the link

#### RetweetUserMetadata

Information about the initial author of the Tweet that was retweeted

**Fields:**
- `name`: `String!` - Name of the user who created the original Tweet
- `username`: `String!` - Username of the user who created the original Tweet
- `avatar`: `String!` - Avatar of the user who created the original Tweet

#### ScheduleV2

Posting schedule for a specific day of the week

**Fields:**
- `day`: `DayOfWeek!` - The day of the week: mon, tue, wed, thu, fri, sat, sun
- `times`: `[String!]!` - The times the channel is scheduled to post on the day: HH:MM
- `paused`: `Boolean!` - Indicates if this day is paused in the posting schedule.

#### StartPagePostMetadata

Start Page post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `link`: `String` - Optional link in post

#### Tag

Tag entity

**Fields:**
- `id`: `TagId!` - ObjectId of the tag
- `color`: `String!` - Hex color for tag e.g '#F523F1'
- `name`: `String!` - Name of the tag e.g 'Summer sales'
- `isLocked`: `Boolean!` - Locked tag cannot be assigned to new items in the UI.
A Tag is locked after a customer downgrades and has more tags than the free plan limit allows

#### ThreadedPost

A post authored by the user which is posted to a thread.
This is commonly used for long-format twitter and meta threads posts to
allow authored content to span multiple threads.
Threads are represented as a list of replies, each replying to the previous one.

**Fields:**
- `text`: `String!` - The text body content of the threaded post
- `assets`: `[Asset!]!` - Media assets of the threaded post
- `linkAttachment`: `LinkAttachment` - Link attachment for the threaded post

#### ThreadsPostMetadata

Threads post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts
- `linkAttachment`: `LinkAttachment` - Link attachment
- `topic`: `String` - Topic associated with the post
- `locationId`: `String` - LocationId associated with the post
- `locationName`: `String` - Location name associated with the post

#### TiktokMetadata

Tiktok metadata

**Fields:**
- `defaultToReminders`: `Boolean!` - Indicates if we should default to reminder for Tiktok
Source: field resolver: profile.default_to_reminders

#### TiktokPostMetadata

Tiktok post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `title`: `String` - The title of the TikTok post (for photo posts)

#### TwitterMetadata

Twitter metadata

**Fields:**
- `subscriptionType`: `String` - Indicates the type of subscription the user has on Twitter

#### TwitterPostMetadata

Twitter post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `retweet`: `RetweetMetadata` - The details of the tweet being retweeted
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts

#### UnauthorizedError

Error returned when the user is not authorized to perform the action

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### UnexpectedError

Error returned when unexpected error occurs

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### UserTag

User tag in the image

**Fields:**
- `handle`: `String!` - The handle of the user
- `x`: `Float!` - The x coordinate of the user tag
- `y`: `Float!` - The y coordinate of the user tag

#### VideoAsset

Video asset

**Implements:** Asset

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset
- `video`: `VideoMetadata!` - Video specific metadata

#### VideoMetadata

Video metadata

**Fields:**
- `durationMs`: `Int!` - Video duration in seconds
- `containerFormat`: `String` - Video container format
- `videoCodec`: `String` - Video codec
- `frameRate`: `Int` - Video framerate
- `videoBitRate`: `Int` - Video bitrate in kbps
- `audioCodec`: `String` - Audio codec
- `rotationDegree`: `Int` - Rotation degree
- `isTranscodingRequired`: `Boolean!` - Whether the video needs to be transcoded before it can be broadcasted
- `isVideoProcessing`: `Boolean!` - Whether the video is currently being processed (transcoding in progress)
- `width`: `Int!` - Video width in pixels
- `height`: `Int!` - Video height in pixels
- `fileSize`: `Int` - Video fileSize in bytes

#### VoidMutationError

Error implementation that allows clients to resolve the MutationError on mutations that do not currently have typed errors.
This allows clients to automatically handle errors that may be added to a mutation in future.

Do not directly throw this error, use a custom typed error instead

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### WeeklyPostingLimit

Weekly posting limit for a channel

**Fields:**
- `sent`: `Int!` - The number of posts the channel has sent this week
- `scheduled`: `Int!` - The number of posts the channel has scheduled for this week
- `limit`: `Int!` - The weekly posting limit for the channel

#### YoutubeCategory

**Fields:**
- `categoryId`: `String!`
- `title`: `String!`

#### YoutubeMetadata

Youtube metadata

**Fields:**
- `defaultToReminders`: `Boolean!` - Indicates if we should default to reminder for Youtube
Source: field resolver: profile.default_to_reminders

#### YoutubePostMetadata

Youtube post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Youtube
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `title`: `String` - Title of the Youtube post
- `privacy`: `YoutubePrivacy` - Privacy setting for post
- `category`: `YoutubeCategory` - Post category
- `license`: `YoutubeLicense` - Video license
- `notifySubscribers`: `Boolean!` - Indicates whether to notify subscribers on publish video
- `embeddable`: `Boolean!` - Indicates whether the video allows embedding
- `madeForKids`: `Boolean!` - Indicates whether the video is suitable for kids

## Input Types

#### AnnotationInputFacebook

Annotation representing all the entities in the text

**Fields:**
- `content`: `String!` - The content of the annotation, e.g. '107509875938399'
- `indices`: `[Int!]!` - The indices of the annotation in the text, e.g. [6, 9] (from 6 to 9 characters in the text)
- `text`: `String!` - The text representation of the annotation, eg 'Buffer'
- `url`: `String!` - The URL the annotation points to, e.g. https://www.facebook.com/107509875938399

#### AnnotationInputLinkedIn

Annotation representing all the entities in the text

**Fields:**
- `id`: `String!` - The id of the annotation, e.g. 1521226
- `link`: `String!` - The link of the annotation, e.g. https://www.linkedin.com/company/bufferapp
- `entity`: `String!` - The entity of the annotation, e.g. urn:li:organization:1521226
- `vanityName`: `String!` - The vanity name of the annotation, e.g. bufferapp
- `localizedName`: `String!` - The localized name of the annotation, e.g. Buffer
- `start`: `Int!` - The start of the annotation, e.g. 5
- `length`: `Int!` - The length of the annotation, e.g. 6

#### AssetsInput

Asset interface with common fields

**Fields:**
- `images`: `[ImageAssetInput!]` - Images to be attached to the post
- `videos`: `[VideoAssetInput!]` - Videos to be attached to the post
- `documents`: `[DocumentAssetInput!]` - Documents to be attached to the post
- `link`: `LinkAssetInput` - Link to be attached to the post

#### BlueskyPostMetadataInput

Bluesky post metadata

**Fields:**
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)
- `linkAttachment`: `LinkAttachmentInput` - Link attachment

#### ChannelInput

Input for the channel query

**Fields:**
- `id`: `ChannelId!` - The ID of the channel to be retrieved

#### ChannelsFiltersInput

Filter to pass when fetching channels.

**Fields:**
- `isLocked`: `Boolean` - If not defined, it returns all channels
Else,
  if true, it only returns locked channels
  if false, it only returns not locked channels
- `product`: `Product` - If not passed, it return all channels
Else, it filters the channels based on what the product supports.

#### ChannelsInput

Input to pass when fetching channels.

**Fields:**
- `organizationId`: `OrganizationId!` - The Organization id to fetch channels for
- `filter`: `ChannelsFiltersInput` - A list of option filters - passing null means we don't want to filter

#### CreateIdeaInput

createIdea input type

**Fields:**
- `organizationId`: `ID!` - Organization ID that will own the idea
- `content`: `IdeaContentInput!` - Content and metadata for the new idea
- `cta`: `String` - Call-to-action identifier for analytics tracking
- `group`: `IdeaGroupInput` - Group placement (null for unassigned group)
- `templateId`: `String` - Template ID used to create the idea

#### CreatePostInput

Create post's request input.

**Fields:**
- `ideaId`: `IdeaId` - Is set when the Post is generated from an Idea
- `draftId`: `DraftId` - Is set when the Post is generated from a Draft
- `schedulingType`: `SchedulingType!` - Scheduling type to indicate notification publishing or automatic publishing
- `dueAt`: `DateTime` - Date when the post is scheduled to be published
- `text`: `String` - Text content of the Post
- `metadata`: `PostInputMetaData` - Metadata of the post which differs based on the social network/service
- `channelId`: `ChannelId!` - Channel's Id for which we want to create the post
- `tagIds`: `[TagId!]` - List of tag IDs
- `assets`: `AssetsInput` - assets
- `mode`: `ShareMode!` - How the post is being scheduled.
- `source`: `String` - source where the composer was initiated from, used for tracking.
- `aiAssisted`: `Boolean` - If this post was created with the help of AI
- `saveToDraft`: `Boolean` - If true, saves the post as a draft instead of scheduling it.
When saving as draft:
- Post status will be 'draft' instead of 'buffer'
- Posting limits are not checked
- The post will not be published until explicitly scheduled

#### DateTimeComparator

Comparator for filtering by date

**Fields:**
- `start`: `DateTime` - Include results with dates equal to or after
the specified date
- `end`: `DateTime` - Include results with dates equal to or before
the specified date

#### DocumentAssetInput

Document asset

**Fields:**
- `url`: `String!` - Document URL
- `title`: `String!` - Document title
- `thumbnailUrl`: `String!` - Document thumbnail URL

#### FacebookPostMetadataInput

Facebook post metadata

**Fields:**
- `type`: `PostTypeFacebook!` - The channel-specific type of the post, eg, post, story, reel for Facebook
- `annotations`: `[AnnotationInputFacebook!]` - Annotations representing entities in the text
- `linkAttachment`: `LinkAttachmentInput` - Link attachment
- `firstComment`: `String` - Facebook post's first comment

#### GoogleBusinessEventMetaDataInput

Metadata for a GBP post that is an event

**Fields:**
- `title`: `String!` - Title of the event
- `startDate`: `DateTime!` - Start date of the event
- `endDate`: `DateTime!` - End date of the event
- `isFullDayEvent`: `Boolean!` - Indicate whether the event has a start or end time.
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### GoogleBusinessOfferMetaDataInput

Metadata for a GBP post that is an offer

**Fields:**
- `title`: `String!` - Title of the offer
- `startDate`: `DateTime!` - Start date of the offer
- `endDate`: `DateTime!` - End date of the offer
- `code`: `String` - Coupon code for the offer
- `link`: `String` - Link to the offer
- `terms`: `String` - Terms and Conditions

#### GoogleBusinessPostMetadataInput

Google Business Profile post metadata
@deprecated: pending proposal for specific GBP post types: update, offer and event metadata types

**Fields:**
- `type`: `PostTypeGoogleBusiness!` - The channel-specific type of the post, eg, post, offer, event for Google Business Profile
- `title`: `String` - Title if available in the given GBP post type: event and offer
- `detailsOffer`: `GoogleBusinessOfferMetaDataInput` - Details of the Offer metadata
- `detailsEvent`: `GoogleBusinessEventMetaDataInput` - Details of the Event metadata
- `detailsWhatsNew`: `GoogleBusinessWhatsNewMetaDataInput` - Details of the Whats new metadata

#### GoogleBusinessWhatsNewMetaDataInput

Metadata for a GBP post of type Whats new

**Fields:**
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### IdeaContentInput

content input for creating/updating an idea

**Fields:**
- `title`: `String` - Title or headline of the idea
- `text`: `String` - Main body text or description
- `media`: `[IdeaMediaInput!]` - List of media items to attach
- `tags`: `[TagInput!]` - Tags to categorize the idea
- `aiAssisted`: `Boolean` - Whether AI tools were used in creation
- `services`: `[Service!]` - Services associated with the idea for targeting specific platforms
- `date`: `DateTime` - Target date for the idea, often used for planning publish schedules

#### IdeaGroupInput

idea group input for create/update

**Fields:**
- `groupId`: `ID` - Target group ID (null for unassigned group)
- `placeAfterId`: `ID` - ID of idea to place after (null for top position)

#### IdeaMediaInput

**Fields:**
- `url`: `String!` - The URL of the media
- `alt`: `String` - Alternative text for the media
- `thumbnailUrl`: `String` - Thumbnail URL for the media
- `type`: `MediaType!` - The type of media (image, gif, video, link, document, unsupported). Note: 'video' is not supported via public API
- `size`: `Int` - The size of the media in bytes
- `source`: `IdeaMediaSourceInput` - Source information for the media

#### IdeaMediaSourceInput

Input type for the source information of media attached to an idea

**Fields:**
- `name`: `String!`
- `id`: `String`
- `trigger`: `String`
- `author`: `String` - for unsplash only
- `authorUrl`: `String`

#### ImageAssetInput

Image asset

**Fields:**
- `url`: `String!` - URL to the file source
- `thumbnailUrl`: `String` - URL to the static thumbnail of the asset
- `metadata`: `ImageMetadataInput` - Image specific metadata

#### ImageDimensionsInput

Image dimensions

**Fields:**
- `width`: `Int!` - Image width in pixels
- `height`: `Int!` - Image height in pixels

#### ImageMetadataInput

Image metadata

**Fields:**
- `altText`: `String!` - Alternative text for accessibility
- `animatedThumbnail`: `String` - Animated thumbnail URL
- `userTags`: `[UserTagInput!]` - User tags in the image
- `dimensions`: `ImageDimensionsInput` - Image dimensions

#### InstagramGeolocationInput

Instagram Geolocation

**Fields:**
- `id`: `String` - The id of this location
- `text`: `String` - The name of this location

#### InstagramPostMetadataInput

Instagram post metadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `firstComment`: `String` - Instagram post's first comment
- `link`: `String` - Shop Grid link for the post
- `geolocation`: `InstagramGeolocationInput` - Geolocation of the post
- `shouldShareToFeed`: `Boolean!` - Indicates whether post should be shared to feed
- `stickerFields`: `InstagramStickerFieldsInput` - Sticker fields for reminder-based publishing

#### InstagramStickerFieldsInput

Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user
is prompted to copy and paste these fields into the Instagram app to complete the post.

**Fields:**
- `text`: `String` - Text for the Story or Reel
- `music`: `String` - Placeholder text for the post's music
- `products`: `String` - Placeholder text for the post's linked products
- `topics`: `String` - Placeholder text for the post's topics (Reels only)
- `other`: `String` - Additional field for any other post content

#### LinkAssetInput

Link attached to the post

**Fields:**
- `url`: `String!` - URL to the link
- `title`: `String` - Title of the link
- `description`: `String` - Description of the link
- `thumbnailUrl`: `String` - Thumbnail URL of the link

#### LinkAttachmentInput

Link attachment

**Fields:**
- `url`: `String!` - URL that the link asset has been built from

#### LinkedInPostMetadataInput

LinkedIn post metadata

**Fields:**
- `annotations`: `[AnnotationInputLinkedIn!]` - Annotations representing entities in the text
- `firstComment`: `String` - LinkedIn post's first comment
- `linkAttachment`: `LinkAttachmentInput` - Link attachment

#### MastodonPostMetadataInput

Mastodon post metadata

**Fields:**
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)
- `spoilerText`: `String` - Spoiler text hiding the root text of this post

#### OrganizationFilterInput

Allow retrieving a specific Organization

**Fields:**
- `organizationId`: `String!`

#### PinterestPostMetadataInput

Pinterest post metadata

**Fields:**
- `title`: `String` - The title of the Pin
- `url`: `String` - The Pin destination link
- `boardServiceId`: `String!` - The board ID of the Pin, can be obtained when fetching the channel details with the following query:
```
query GetChannelWithSubprofiles {
  channel(input: { id: "[CHANNEL_ID_HERE]" }) {
    metadata {
      ... on PinterestMetadata {
        boards {
          serviceId
        }
      }
    }
  }
}
```

#### PostInput

Input for the post query

**Fields:**
- `id`: `PostId!` - The ID of the post to be retrieved

#### PostInputMetaData

Metadata of the post which differs based on the social network/service

**Fields:**
- `instagram`: `InstagramPostMetadataInput` - Metadata for Instagram post
- `facebook`: `FacebookPostMetadataInput` - Metadata for Facebook post
- `linkedin`: `LinkedInPostMetadataInput` - Metadata for LinkedIn post
- `twitter`: `TwitterPostMetadataInput` - Metadata for Twitter post
- `pinterest`: `PinterestPostMetadataInput` - Metadata for Pinterest post
- `google`: `GoogleBusinessPostMetadataInput` - Metadata for Google Business Profile post
- `youtube`: `YoutubePostMetadataInput` - Metadata for Youtube post
- `mastodon`: `MastodonPostMetadataInput` - Metadata for Mastodon post
- `startPage`: `StartPagePostMetadataInput` - Metadata for Start Page post
- `threads`: `ThreadsPostMetadataInput` - Metadata for Threads post
- `bluesky`: `BlueskyPostMetadataInput` - Metadata for Bluesky post
- `tiktok`: `TikTokPostMetadataInput` - Metadata for TikTok post

#### PostsFiltersInput

Filter to apply to the posts query

**Fields:**
- `channelIds`: `[ChannelId!]` - When set, it will filter posts by channel
- `startDate`: `DateTime` - When set, it will return posts with createdAt or dueAt date after startDate
- `endDate`: `DateTime` - When set, it will return posts with createdAt or dueAt date before endDate
- `status`: `[PostStatus!]` - When set, it will filter posts by status
- `tags`: `TagComparator` - Filter posts by tags. Supports specific tags, untagged posts, or union of both.
- `tagIds`: `[TagId!]` - When set, it will filter posts by tag
- `dueAt`: `DateTimeComparator` - When set, it will filter posts by their scheduled posting date
- `createdAt`: `DateTimeComparator` - When set, it will filter posts by the date they were created

#### PostsInput

Input for the posts query

**Fields:**
- `organizationId`: `OrganizationId!` - The Organization id to fetch posts for
- `filter`: `PostsFiltersInput` - The filters to apply to the posts query
- `sort`: `[PostSortInput!]` - The sort to apply to the posts results

#### PostSortInput

Sort order of post results. List multiple to create tie-breaking order.

**Fields:**
- `field`: `PostSortableKey!` - The field to sort by.
- `direction`: `SortDirection!` - The direction to sort by.

#### RetweetMetadataInput

Information about the initial Tweet that was retweeted

**Fields:**
- `id`: `String!` - Retweet ID

#### StartPagePostMetadataInput

Start Page post metadata

**Fields:**
- `link`: `String` - Optional link in post

#### TagComparator

Comparator for filtering by tags

**Fields:**
- `in`: `[TagId!]!` - Include results that have any of the specified tags (union/OR).
- `isEmpty`: `Boolean!` (default: false) - When true, include results that have no tags assigned.
Can be combined with 'in' for union filtering.
Defaults to false if not specified.

#### TagInput

Input type for tag information used in idea creation

**Fields:**
- `id`: `ID!`
- `name`: `String!`
- `color`: `String!`

#### ThreadedPostInput

A post authored by the user which is posted to a thread.
This is commonly used for long-format twitter and meta threads posts to
allow authored content to span multiple threads.
Threads are represented as a list of replies, each replying to the previous one.

**Fields:**
- `text`: `String` - The text body content of the threaded post
- `assets`: `AssetsInput` - Media assets of the threaded post

#### ThreadsPostMetadataInput

Threads post metadata

**Fields:**
- `type`: `PostType` - The type of the post
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)
- `linkAttachment`: `LinkAttachmentInput` - Link attachment
- `topic`: `String` - Topic associated with the post
- `locationId`: `String` - LocationId associated with the post
- `locationName`: `String` - Location name associated with the post

#### TikTokPostMetadataInput

TikTok post metadata

**Fields:**
- `title`: `String` - The title of the TikTok post (for photo posts)

#### TwitterPostMetadataInput

Twitter post metadata

**Fields:**
- `retweet`: `RetweetMetadataInput` - The details of the tweet being retweeted
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)

#### UserTagInput

User tag in the image

**Fields:**
- `handle`: `String!` - The handle of the user
- `x`: `Float!` - The x coordinate of the user tag
- `y`: `Float!` - The y coordinate of the user tag

#### VideoAssetInput

Video asset

**Fields:**
- `url`: `String!` - URL to the file source
- `thumbnailUrl`: `String` - URL to the thumbnail of the video
- `metadata`: `VideoMetadataInput` - Video specific metadata

#### VideoMetadataInput

Video metadata

**Fields:**
- `thumbnailOffset`: `Int` - Offset of the thumbnail chosen for the video, in ms
- `title`: `String` - Video title

#### YoutubePostMetadataInput

Youtube post metadata

**Fields:**
- `title`: `String!` - Title of the Youtube post
- `privacy`: `YoutubePrivacy` - Privacy setting for post (default: public)
- `categoryId`: `String!` - Youtube Category ID, one ID of this list:
ID: 1 -> Film & Animation
ID: 2 -> Autos & Vehicles
ID: 10 -> Music
ID: 15 -> Pets & Animals
ID: 17 -> Sports
ID: 19 -> Travel & Events
ID: 20 -> Gaming
ID: 22 -> People & Blogs
ID: 23 -> Comedy
ID: 24 -> Entertainment
ID: 25 -> News & Politics
ID: 26 -> Howto & Style
ID: 27 -> Education
ID: 28 -> Science & Technology
ID: 29 -> Nonprofits & Activism
- `license`: `YoutubeLicense` - Video license (default: youtube)
- `notifySubscribers`: `Boolean` - Indicates whether to notify subscribers on publish video (default: true)
- `embeddable`: `Boolean` - Indicates whether the video allows embedding (default: true)
- `madeForKids`: `Boolean` - Indicates whether the video is suitable for kids (default: false)

## Interfaces

#### Asset

Asset interface with common fields

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset

#### CommonPostMetadata

Common properties for all post metadata types

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text

#### MutationError

Base Mutation Error type

**Fields:**
- `message`: `String!` - Error message

#### ScrapedLink

Link data for link preview

**Fields:**
- `url`: `String!` - URL that the link asset has been built from
- `text`: `String!` - Description for the scraped link
- `thumbnails`: `[String!]!` - Thumbnails of media available in the link

#### ThreadedPostMetadata

Common properties for all posts that support threaded replies.
See ThreadedPost for more details.

**Fields:**
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts

## Unions

#### ChannelMetadata

Metadata or settings about the channel depending on the service type

**Possible types:** InstagramMetadata | TiktokMetadata | YoutubeMetadata | PinterestMetadata | MastodonMetadata | BlueskyMetadata | GoogleBusinessMetadata | FacebookMetadata | TwitterMetadata | LinkedInMetadata

#### CreateIdeaPayload

createIdea response (including errors)

**Possible types:** Idea | IdeaResponse | InvalidInputError | UnauthorizedError | UnexpectedError | LimitReachedError

#### GoogleBusinessPostDetails

GoogleBusiness Metadata details

**Possible types:** GoogleBusinessWhatsNewMetaData | GoogleBusinessOfferMetaData | GoogleBusinessEventMetaData

#### PostActionPayload

Create post's request response payload.

**Possible types:** PostActionSuccess | NotFoundError | UnauthorizedError | UnexpectedError | RestProxyError | LimitReachedError | InvalidInputError

#### PostMetadata

Post metadata union type. Contains all possible types of post metadata.

**Possible types:** InstagramPostMetadata | FacebookPostMetadata | LinkedInPostMetadata | TwitterPostMetadata | PinterestPostMetadata | GoogleBusinessPostMetadata | YoutubePostMetadata | MastodonPostMetadata | StartPagePostMetadata | TiktokPostMetadata | ThreadsPostMetadata | BlueskyPostMetadata

## Enums

#### AnnotationType

List of possible types for an annotation

**Values:**
- `hashtag`
- `mention`
- `url`
- `annotation`
- `cashtag`

#### AssetType

Asset types

**Values:**
- `image`
- `video`
- `document`

#### ChannelAction

List of possible actions that can be performed on a Channel

**Values:**
- `publishStartPage`

#### ChannelType

Channel is a representation of a social media account or page that can be connected to Buffer.

**Values:**
- `page`
- `profile`
- `business`
- `group`
- `account`
- `channel`

#### DayOfWeek

**Values:**
- `mon`
- `tue`
- `wed`
- `thu`
- `fri`
- `sat`
- `sun`

#### GoogleBusinessPostActionType

List of possible types for GBP cta

**Values:**
- `none`
- `book`
- `order`
- `shop`
- `learn_more`
- `signup`
- `call`

#### MediaType

The type of media attached to a post

**Values:**
- `image`
- `gif`
- `video`
- `link`
- `document`
- `unsupported`

#### NoteAction

List of possible actions that can be performed on a note

**Values:**
- `updateNote` - The user can update the note.
- `deleteNote` - The user can delete the note.

#### NoteType

The type of a note.

**Values:**
- `userGenerated` - A note that was manually written by a user.
- `bufferGenerated` - A note that was generated by our internal system. Can be used for approval flows notifications or other automated processes.
- `aiGenerated` - A note that was generated by our AI system.

#### NotificationStatus

List of possible statuses for a notification

**Values:**
- `notified`
- `markedAsPublished`

#### OrganizationAction

List of possible actions that can be performed on a Organization

**Values:**
- `view`
- `edit`
- `manageBilling`
- `manageTeamMembers`
- `publishStartPages`
- `manageAllNotes`
- `manageChannels`
- `transferOwnership`
- `receiveOrganizationOwnership`

#### PostAction

List of possible actions that can be performed on a Post

**Values:**
- `updatePost`
- `deletePost`
- `viewPost`
- `sharePostLink`
- `copyPostLink`
- `movePostToDraft`
- `publishPostNow`
- `publishPostNext`
- `addPostToQueue`
- `updatePostSchedule`
- `removePostScheduledTime`
- `requestPostApproval`
- `revertPostApprovalRequest`
- `approvePost`
- `rejectPost`
- `duplicatePost`
- `updatePostTags`
- `addPostNote`
- `updateShopGridLink`

#### PostingGoalStatus

PostingGoalStatus is used to track the status of a posting goal.

**Values:**
- `OnTrack`
- `AtRisk`
- `Hit`

#### PostSortableKey

Key of collection to use for sorting

**Values:**
- `dueAt` - Sort by the post's dueAt field.
Due at is the date when the post is scheduled to be published.
- `createdAt` - Sort by the post's createdAt field.
Created at is the date when the post was created.

#### PostStatus

List of possible statuses for a Post

**Values:**
- `draft`
- `needs_approval`
- `scheduled`
- `sending`
- `sent`
- `error`

#### PostType

List of possible types for a Post. Some services may have different types (e.g., Instagram has story, reel, post but Twitter has only post)

**Values:**
- `post`
- `reel`
- `story`
- `short`
- `whats_new`
- `offer`
- `event`
- `carousel`
- `ghost_post`
- `thread`

#### PostTypeFacebook

List of specific post types available for Facebook

**Values:**
- `post`
- `story`
- `reel`

#### PostTypeGoogleBusiness

List of specific post types available for Google Business profiles

**Values:**
- `event`
- `whats_new`
- `offer`

#### PostVia

List of possible ways to create a Post

**Values:**
- `buffer`
- `network`
- `api`

#### Product

Buffer products, buffer is used as all products

**Values:**
- `analyze`
- `engage`
- `publish`
- `buffer`
- `startPage`
- `comments`

#### ScheduleOption

**Values:**
- `Queue`
- `Prioritize`
- `FixedTime`
- `Now`

#### SchedulingType

Indicates whether the post was scheduled for notification publishing or automatic publishing

**Values:**
- `notification` - The post was created natively on the social network using notification publishing
- `automatic` - The post was created natively on the social network using automatic publishing

#### Service

The list of services that can be authorized.

**Values:**
- `instagram`
- `facebook`
- `twitter`
- `linkedin`
- `pinterest`
- `tiktok`
- `googlebusiness`
- `startPage`
- `mastodon`
- `youtube`
- `threads`
- `bluesky`

#### ShareMode

How the post is being scheduled.

**Values:**
- `addToQueue`
- `shareNow`
- `shareNext`
- `customScheduled`
- `recommendedTime`

#### SortDirection

Direction to sort the results by.

**Values:**
- `asc` - Sort records in ascending order.
- `desc` - Sort records in descending order.

#### YoutubeLicense

List of license types

**Values:**
- `youtube`
- `creativeCommon`

#### YoutubePrivacy

List of privacy types

**Values:**
- `public`
- `unlisted`
- `private`

## Scalars

#### AccountId

The `AccountId` scalar represents the MongoDB ObjectId of a Buffer Account

#### ChannelId

The `ChannelId` scalar represents the MongoDB ObjectId of a Buffer Channel

#### DateTime

The `DateTime` scalar represents a date and time following the ISO 8601 standard.

#### DraftId

The `DraftId` scalar represents the MongoDB ObjectId of a Buffer Draft

#### IdeaId

The `IdeaId` scalar represents the MongoDB ObjectId of a Buffer Idea

#### NoteId

The `NoteId` scalar represents the MongoDB ObjectId of a Buffer Note

#### OrganizationId

The `OrganizationId` scalar represents the MongoDB ObjectId of a Buffer Organization

#### PostId

The `PostId` scalar represents the MongoDB ObjectId of a Buffer Post

#### TagId

The `TagId` scalar represents the MongoDB ObjectId of a Buffer Tag

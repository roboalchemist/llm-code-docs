# Source: https://docs.fireflies.ai/additional-info/change-log.md

# Changelog

> Recent updates to the Fireflies API

## Overview

This document maintains a chronologically ordered list of notable changes for each version of the Fireflies API. It's designed to make it easier for you to keep track of new features, improvements, and bug fixes.

### 2.15.0

<Card>
  Added `updateMeetingChannel` mutation to set the channel for one or more meetings. Supports batch updates of 1–5 transcripts to a single channel and requires meeting owner or team admin privileges. See [Update Meeting Channel](/graphql-api/mutation/update-meeting-channel).
</Card>

### 2.14.0

<Card>
  Added `active_meetings` query to retrieve meetings currently in progress. Allows fetching active meetings for users in your team with role-based access control. See [Active Meetings](/graphql-api/query/active-meetings).
</Card>

### 2.13.0

<Card>
  Added rate limiting to the `deleteTranscript` mutation. It is limited to 10 requests per minute across all user tiers. When exceeded, the API returns HTTP 429 `too_many_requests`. See [Delete Transcript](/graphql-api/mutation/delete-transcript).
</Card>

### 2.12.0

<Card>
  Added `updateMeetingPrivacy` mutation to update meeting privacy settings. Allows meeting owners and team admins to change privacy levels between link, owner, participants, teammatesandparticipants, and teammates. See [Update Meeting Privacy](/graphql-api/mutation/update-meeting-privacy).
</Card>

### 2.11.0

<Card>
  Added `channels` field to [Transcript](/schema/transcript) schema. Returns an array of [Channel](/schema/channel) objects containing channel IDs associated with the meeting.
</Card>

### 2.10.0

<Card>
  Added new `meeting_attendance` field to [Transcript](/schema/transcript) schema providing participant join and leave times from meeting events data.
</Card>

<Card>
  Added new [MeetingAttendance](/schema/meeting-attendance) schema with `name`, `join_time`, and `leave_time` fields for tracking participant attendance.
</Card>

### 2.9.0

<Card>
  Added `channel_id` parameter to [Transcripts](/graphql-api/query/transcripts) query to filter meetings by specific channel. Accepts a single channel ID string.
</Card>

### 2.8.0

<Card>
  Added array fields `organizers` and `participants` to [Transcripts](/graphql-api/query/transcripts) query for filtering by multiple email addresses. Previous single email fields `organizer_email` and `participant_email` are now deprecated.
</Card>

### 2.7.1

<Card>
  Added validation for [Add to Live](/graphql-api/mutation/add-to-live) to only allow supported meeting platforms as `meeting_link`.

  Added new error type [UnsupportedPlatform](/miscellaneous/error-codes#unsupported-platform) that is thrown when an unsupported `meeting_link` is provided to `Add to Live`.
</Card>

### 2.7.0

<Card>Added new `user_groups` query to fetch user groups with optional `mine` filter. See [User Groups](/graphql-api/query/user-groups)</Card>

<Card>Enhanced [UserGroup](/schema/user-groups) schema with `members` field</Card>

<Card>Added new [UserGroupMember](/schema/user-group-member) schema for user group member details</Card>

### 2.6.3

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.6.2

<Card>
  Updated `transcripts` query to allow text search within meeting transcript (/query/transcripts)\[Transcripts]
</Card>

### 2.6.1

<Card>
  Updated `uploadAudio` mutation to include `bypass_size_check` boolean, allowing processing of
  audio files smaller than the standard 50kb minimum size.
</Card>

### 2.6.0

<Card>Added [Realtime API](/realtime-api/overview) support.</Card>

### 2.5.1

<Card>Added `user_groups` field to [User](/schema/user) query.</Card>

### 2.5.0

<Card>
  Added query `analytics` to query team and user analytics for meetings and conversations. See
  [Analytics](/graphql-api/analytics)
</Card>

<Card>
  Added query `transcript.analytics` to query analytics per meeting. See
  [Transcript](/graphql-api/transcript) or [Transcripts](/graphql-api/transcripts)
</Card>

### 2.4.6

<Card>Fixed bug in `transcripts.title` query not returning correct results</Card>

### 2.4.5

<Card>Reduced the minimum file size for `uploadAudio` mutation to 50kb.</Card>

### 2.4.4

<Card>
  Field `client_reference_id` in [AudioUpload](/graphql-api/mutation/upload-audio) was limited to 32
  characters as part of input validation. It has now been increased to 128 characters.
</Card>

### 2.4.3

<Card>Added length validation for all input fields.</Card>

### 2.4.2

<Card>
  Added `updateMeetingTitle` mutation to update meeting titles. For more details, view [Update
  Meeting Title](/graphql-api/mutation/update-meeting-title)
</Card>

### 2.4.1

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.4.0

<Card>Added `mine` field to [Transcripts](/graphql-api/query/transcripts) query</Card>

<Card>
  Added breaking changes to [Transcripts](/graphql-api/query/transcripts) query that allows you to
  only use one of the following fields: `organizer_email`, `participant_email`, `user_id`, `mine` at
  a time
</Card>

### 2.3.17

<Card>Added `meeting_link` field to [Transcript](/schema/transcript) schema</Card>

### 2.3.16

<Card>
  Added `apps` query to fetch AI App Outputs. For more details, view [Apps](/graphql-api/query/apps)
</Card>

### 2.3.15

<Card>Fixed bug in `transcripts` query where it was not returning the correct match.</Card>

### 2.3.14

<Card>
  Added support for webhook auth. For more details, view the [Webhooks](/graphql-api/webhooks) page
</Card>

### 2.3.13

<Card>Added new fields to summary to [Summary](/schema/summary) schema</Card>

### 2.3.12

<Card>Added fields `cal_id` and `calendar_type` to [Transcript](/schema/transcript) schema</Card>

### 2.3.11

<Card>Fixed bug in `transcript.sentences` query where it was incorrectly returning null</Card>

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.3.10

<Card>Added field `attendees` to [addToLive](/graphql-api/mutation/add-to-live) mutation</Card>

### 2.3.9

<Card>Added field `meeting_info` for meeting metadata.</Card>

<Card>Updated `uploadAudio` mutation to allow saving video</Card>

### 2.3.8

<Card>Added field `speakers` in transcript.</Card>

<Card>
  Updated docs to include error codes and their explanations. View details
  [here](/miscellaneous/error-codes)
</Card>

### 2.3.7

<Card>
  Added new fields for `transcript.summary`. View details on the [Summary](/schema/summary) schema
  page
</Card>

### 2.3.6

<Card>Updated docs for webhooks to include webhook schema</Card>

<Card>Added `client_reference_id` field for audio upload</Card>

### 2.3.5

<Card>Added argument `custom_language` for `uploadAudio`.</Card>

### 2.3.4

<Card>
  Added query argument `fromDate` and `toDate` for `transcripts`. View more details
  [here](/graphql-api/query/transcripts). Field `date` has been deprecated in favor of these
  arguments
</Card>

### 2.3.3

<Card>
  Added mutation for `addToLiveMeeting`. View more details [here](/graphql-api/mutation/add-to-live)
</Card>

### 2.3.2

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.3.1

<Card>
  Added field `calendar_id`. This field represents calId for google calendar and iCalUID for outlook
  calendar. For more details, view [Transcript](/schema/transcript)
</Card>

### 2.3.0

<Card>
  Added queries for [Transcript Summary](/schema/summary). For more details, view
  [Summary](/schema/summary) schema and [Transcript](/schema/transcript) schema
</Card>

### 2.2.0

<Card>
  Added queries for [bites](/graphql-api/query/bites) and [bite](/graphql-api/query/bite). For more
  details, view [Bites](/schema/bite) schema
</Card>

<Card>
  Added mutation for Create Bite that allows you to progmatically create bites. For more details,
  view [CreateBite](/graphql-api/mutation/create-bite) mutation
</Card>

### 2.1.1

<Card>Fixed bugs in [Transcripts](/graphql-api/query/transcripts) query</Card>

### 2.1.0

<Card>Added `video_url` field for [Transcript](schema/transcript) schema</Card>

### 2.0.7

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.0.6

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.0.5

<Card>
  Fixed bug in in [Transcripts](graphql-api/query/transcripts) query for `fireflies_users` field
</Card>

### 2.0.4

<Card>
  Fixed bug in in [Transcripts](graphql-api/query/transcripts) query for `audio_url` field
</Card>

### 2.0.3

<Card>Made improvements to the performance and stability of the Fireflies API.</Card>

### 2.0.2

<Card>Fixed bug in [Transcripts](/graphql-api/query/transcripts) query arguments</Card>

### 2.0.1

<Card>
  Fixed schema inconsistency in [AudioUpload](/graphql-api/mutation/upload-audio) mutation.
</Card>

<Card>
  Fixed schema inconsistency in [SetUserRole](/graphql-api/mutation/set-user-role) mutation
</Card>

### 2.0.0

<Card>
  Field `transcript/host_email` has been deprecated. More details in
  [Transcript](/schema/transcript)
</Card>

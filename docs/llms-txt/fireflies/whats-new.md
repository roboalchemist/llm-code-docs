# Source: https://docs.fireflies.ai/getting-started/whats-new.md

# What's New

> Latest updates to the Fireflies API

Take a look at our latest updates, features, and improvements for the Fireflies API.

<Update label="2.15.0" description="Set Meeting Channels">
  ### Set Meeting Channels

  The new [Update Meeting Channel](/graphql-api/mutation/update-meeting-channel) mutation allows meeting owners and team administrators to set the channel for one or more meetings. You can update 1–5 transcripts to a single channel in one API call with all-or-nothing semantics.

  This mutation requires either meeting ownership or team admin privileges for all specified transcripts. If any transcript fails validation, none of the transcripts will be updated, ensuring data consistency across your channel organization.
</Update>

<Update label="2.14.0" description="Active Meetings Fetching">
  ### Active Meetings Fetching

  The new [Active Meetings](/graphql-api/query/active-meetings) query allows you to fetch meetings currently in progress. This query returns real-time information about active meetings including meeting details, start time, organizer, and meeting link.
</Update>

<Update label="2.13.0" description="Rate Limiting for Delete Transcript">
  ### Rate Limiting for Delete Transcript

  The [Delete Transcript](/graphql-api/mutation/delete-transcript) mutation now includes rate limiting protection to prevent abuse. The mutation is limited to 10 requests per minute across all user tiers.

  If you exceed this limit, the API will return a `too_many_requests` error (HTTP 429) with a `retryAfter` timestamp indicating when you can make requests again.
</Update>

<Update label="2.12.0" description="Meeting Privacy Control">
  ### Meeting Privacy Control

  The new [Update Meeting Privacy](/graphql-api/mutation/update-meeting-privacy) mutation allows meeting owners and team administrators to programmatically update meeting privacy settings. You can now change privacy levels between `link`, `owner`, `participants`, `teammatesandparticipants`, and `teammates` to control who can access meeting transcripts.

  This mutation follows the same authorization pattern as other meeting management operations, requiring either meeting ownership or team admin privileges.
</Update>

<Update label="2.10.0" description="Meeting Attendance Tracking">
  ### Meeting Attendance Tracking

  The [Transcript](/schema/transcript) schema now includes a new `meeting_attendance` field that provides detailed participant attendance information. This field returns an array of [MeetingAttendance](/schema/meeting-attendance) records showing when participants joined and left the meeting.

  Each attendance record includes the participant's name, join time (ISO 8601 format), and leave time (if they left during the meeting). This feature enables better meeting analytics and participation tracking by leveraging meeting events data.

  The attendance data is available in both [Transcript](/graphql-api/query/transcript) and [Transcripts](/graphql-api/query/transcripts) queries.
</Update>

<Update label="2.9.0" description="Channel Filtering">
  ### Channel Filtering

  The [Transcripts](/graphql-api/query/transcripts) query now supports filtering by channel using the new `channel_id` parameter. This allows you to retrieve transcripts from specific channels by providing a single channel ID.

  The `channel_id` parameter accepts a string value and enables more targeted querying of meeting transcripts within your organization's channels.
</Update>

<Update label="2.8.0" description="Array Fields for Organizers and Participants">
  ### Array Fields for Organizers and Participants

  The [Transcripts](/graphql-api/query/transcripts) query now supports array fields `organizers` and `participants` that allow filtering by multiple email addresses. These new array fields provide more flexible querying capabilities while maintaining backward compatibility.

  The previous single email fields `organizer_email` and `participant_email` are now deprecated but continue to work. Using both old and new fields simultaneously will result in a validation error.
</Update>

<Update label="2.7.0" description="User Groups">
  ### User Groups

  The Fireflies API now includes comprehensive support for user groups. The new [User Groups](/graphql-api/query/user-groups) query allows you to fetch all user groups within your team or filter to only show groups you belong to using the `mine` parameter.

  Additionally, the [User](/schema/user) and [Users](/graphql-api/query/users) queries now include enhanced `user_groups` fields with detailed member information, providing better visibility into team organization and collaboration.
</Update>

<Update label="2.6.2" description="Keyword search">
  ### Keyword Search

  The [Transcripts](/graphql-api/query/transcripts) query has been enhanced to include keyword search functionality. By utilizing the `keyword` and `scope` parameters, you can now perform advanced searches within both the title and the transcript text, offering more precise retrieval.

  The `title` parameter has been deprecated in favor of `keyword`
</Update>

<Update label="2.6.1" description="Upload audio">
  ### Enhancements to Audio Upload

  The [Upload Audio](/graphql-api/mutation/upload-audio) function now includes a `bypass_size_check` flag. This enhancement provides greater control over filtering unwanted uploads, such as voicemails from dialers.
</Update>

<Update label="2.6.0" description="Realtime API">
  ### Realtime API

  The Fireflies.ai [Realtime API](/realtime-api/overview) allows your application to receive live transcription events over WebSockets. This enables building interactive features such as live captioning, transcription overlays, and real-time analysis as users speak.
</Update>

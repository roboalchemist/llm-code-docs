# Stream.io Documentation
# Source: https://getstream.io/chat/docs/permissions/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [React](/chat/docs/react/)

/

  * [Reference](/chat/docs/react/permissions_reference/)

# Reference

This reference contains some useful information about permission system,
applicable to both versions.

## Actions

In the table below you will find all available actions of Stream Chat
permission system

Action| Resource Type| Description  
AddLinks| Channel| Allows user to add URLs into messages  
AddOwnChannelMembership| Channel| Allows user to add own channel membership
(join channel)  
BanChannelMember| Channel| Allows user to ban channel members  
CreateChannel| Channel| Allows user to create a new channel  
CreateDistinctChannelForOthers| Channel| Allows user to create new distinct
channel for other users (e.g. user A creates channel for users B and C)  
CreateMessage| Channel| Allows user to send a new message  
CreateAttachment| Channel| Allows user to send a new message with attachments  
CreateMention| Channel| Allows user to send a new message with mentions  
CreateReaction| Channel| Allows user to add a reaction to a message  
CreateSystemMessage| Channel| Allows user to send a new system message  
DeleteChannel| Channel| Allows user to delete a channel  
DeleteReaction| Channel| Allows user to delete a reaction  
FlagMessage| Channel| Allows user to flag messages  
MuteChannel| Channel| Allows user to mute and unmute channel  
PinMessage| Channel| Allows user to pin a message  
ReadChannel| Channel| Allows user to read messages from the channel  
ReadChannelMembers| Channel| Allows user to read channel members  
ReadDisabledChannel| User| Allows user to read disabled channels (regardless
of channel membership)  
ReadMessageFlags| Channel| Allows user to access messages that have been
flagged  
RecreateChannel| Channel| Allows user to recreate a channel when it got
deleted  
RemoveOwnChannelMembership| Channel| Allows user to leave the channel (remove
own channel membership)  
SendCustomEvent| Channel| Allows user to send custom events to a channel  
SkipChannelCooldown| Channel| Allows user to bypass existing cooldown in a
channel  
SkipMessageModeration| Channel| Allows user to bypass automatic message
moderation  
TruncateChannel| Channel| Allows user to truncate a channel  
UpdateChannel| Channel| Allows user to update channel data  
UpdateChannelCooldown| Channel| Allows user to set and unset cooldown time for
a channel (slow mode)  
UpdateChannelFrozen| Channel| Allows user to freeze and unfreeze a channel  
UpdateChannelMembers| Channel| Allows user to add, modify and remove channel
members  
UploadAttachment| Channel| Allows user to upload files and images  
UseFrozenChannel| Channel| Allows user to send messages and reactions to a
frozen channels  
DeleteMessage| Message| Allows user to delete a message  
RunMessageAction| Message| Allows user to run an action against a message  
UnblockMessage| Message| Allows user to unblock message blocked by automatic
moderation  
UpdateMessage| Message| Allows user to update a message  
DeleteAttachment| Attachment| Allows user to delete uploaded files and images  
BanUser| User| Allows user to ban users  
FlagUser| User| Allows user to flag users  
MuteUser| User| Allows user to mute and unmute users  
SearchUser| User| Allows user to search for other users  
UpdateUser| User| Allows user to update users  
UpdateUserRole| User| Allows user to update user roles  
UpdateUserTeams| User| Allows user to update user teams  
CreateRestrictedVisibilityMessage| User| Allows user to create restricted
visibility messages  
ReadRestrictedVisibilityMessage| User| Allows user to read restricted
visibility messages  
BlockUser| Call| Allows user to Block and unblock users on calls  
CreateCall| Call| Allows user to creates a call  
CreateCallReaction| Call| Allows user to Add a reaction to a call  
DeleteRecording| Call| Allows user to Delete recording  
EndCall| Call| Allows user to terminates a call  
JoinBackstage| Call| Allows user to joins a call backstage  
JoinCall| Call| Allows user to joins a call  
JoinEndedCall| Call| Allows user to joins a call that was marked as ended  
ListRecordings| Call| Allows user to List recordings  
MuteUsers| Call| Allows user to MuteUsers  
PinCallTrack| Call| Allows user to Pin/Unpin a track for everyone in the call  
ReadCall| Call| Allows user to read a call  
ReadFlagReports| FlagReport| Allows user to read flag reports  
RemoveCallMember| Call| Allows user to Remove a participant  
Screenshare| Call| Allows user to Screenshare  
SendAudio| Call| Allows user to Send audio  
SendEvent| Call| Allows user to SendEvent  
SendVideo| Call| Allows user to Send video  
StartBroadcasting| Call| Allows user to Start broadcasting  
StartRecording| Call| Allows user to Start recording  
StartTranscription| Call| Allows user to Start transcription  
StopBroadcasting| Call| Allows user to Stop broadcasting  
StopRecording| Call| Allows user to Stop recording  
StopTranscription| Call| Allows user to Stop transcription  
UpdateCall| Call| Allows user to update the data for a call  
UpdateCallMember| Call| Allows user to Update a participant  
UpdateCallMemberRole| Call| Allows user to Update role for participants  
UpdateCallPermissions| Call| Allows user to UpdateCallPermissions  
UpdateCallSettings| Call| Allows user to updates settings of a call  
UpdateFlagReport| FlagReport| Allows user to update flag report  
  
## Default Grants

In tables below you will find default permission grants for each builtin
channel type as well as `.app` permission scope.

For each of of the above actions, there are different built in permissions
depending on whether the object was created by the user or not. For example,
users can be given permissions to `delete-attachment` which allows for
deleting any message attachments, or they can be given permissions to `delete-
attachment-owned` to restrict this to only attachments added by the current
user.

Every custom channel type that you create using CreateChannelType API
endpoint, will have `messaging` scope grants by default.

### Scope `video:development`

Permission ID| admin| user| guest| anonymous  
block-user| â | â | âï¸| âï¸  
create-call| â | â | âï¸| âï¸  
create-call-reaction| â | â | âï¸| âï¸  
end-call| â | â | âï¸| âï¸  
join-backstage| â | â | âï¸| âï¸  
join-call| â | â | â | â   
join-ended-call| â | â | âï¸| âï¸  
list-recordings| â | â | âï¸| âï¸  
mute-users| â | â | âï¸| âï¸  
pin-call-track| â | â | âï¸| âï¸  
read-call| â | â | â | â   
remove-call-member| â | â | âï¸| âï¸  
screenshare| â | â | âï¸| âï¸  
send-audio| â | â | â | âï¸  
send-event| â | â | â | âï¸  
send-video| â | â | â | âï¸  
start-broadcasting| â | â | âï¸| âï¸  
start-recording| â | â | âï¸| âï¸  
start-transcription| â | â | âï¸| âï¸  
stop-broadcasting| â | â | âï¸| âï¸  
stop-recording| â | â | âï¸| âï¸  
stop-transcription| â | â | âï¸| âï¸  
update-call| â | â | âï¸| âï¸  
update-call-member| â | â | âï¸| âï¸  
update-call-member-role| â | â | âï¸| âï¸  
update-call-permissions| â | â | âï¸| âï¸  
update-call-settings| â | â | âï¸| âï¸  
  
### Scope `video:livestream`

Permission ID| admin| user| anonymous  
block-user| â | âï¸| âï¸  
block-user-owner| âï¸| â | âï¸  
create-call| â | â | âï¸  
create-call-reaction| â | â | âï¸  
end-call| â | âï¸| âï¸  
end-call-owner| âï¸| â | âï¸  
join-backstage| â | âï¸| âï¸  
join-backstage-owner| âï¸| â | âï¸  
join-call| â | â | â   
join-ended-call| â | âï¸| âï¸  
join-ended-call-owner| âï¸| â | âï¸  
mute-users| â | âï¸| âï¸  
mute-users-owner| âï¸| â | âï¸  
pin-call-track| â | âï¸| âï¸  
pin-call-track-owner| âï¸| â | âï¸  
read-call| â | â | â   
remove-call-member| â | âï¸| âï¸  
remove-call-member-owner| âï¸| â | âï¸  
screenshare| â | âï¸| âï¸  
screenshare-owner| âï¸| â | âï¸  
send-audio| â | âï¸| âï¸  
send-audio-owner| âï¸| â | âï¸  
send-event| â | â | âï¸  
send-video| â | âï¸| âï¸  
send-video-owner| âï¸| â | âï¸  
start-broadcasting| â | âï¸| âï¸  
start-broadcasting-owner| âï¸| â | âï¸  
start-recording| â | âï¸| âï¸  
start-recording-owner| âï¸| â | âï¸  
stop-broadcasting| â | âï¸| âï¸  
stop-broadcasting-owner| âï¸| â | âï¸  
stop-recording| â | âï¸| âï¸  
stop-recording-owner| âï¸| â | âï¸  
update-call| â | âï¸| âï¸  
update-call-member| â | âï¸| âï¸  
update-call-member-owner| âï¸| â | âï¸  
update-call-member-role| â | âï¸| âï¸  
update-call-member-role-owner| âï¸| â | âï¸  
update-call-owner| âï¸| â | âï¸  
update-call-permissions| â | âï¸| âï¸  
update-call-permissions-owner| âï¸| â | âï¸  
update-call-settings| â | âï¸| âï¸  
  
### Scope `video:audio_room`

Permission ID| admin| user| anonymous  
block-user| â | âï¸| âï¸  
block-user-owner| âï¸| â | âï¸  
create-call| â | â | âï¸  
create-call-reaction| â | â | âï¸  
end-call| â | âï¸| âï¸  
end-call-owner| âï¸| â | âï¸  
join-backstage| â | âï¸| âï¸  
join-backstage-owner| âï¸| â | âï¸  
join-call| â | â | â   
join-ended-call| â | âï¸| âï¸  
join-ended-call-owner| âï¸| â | âï¸  
mute-users| â | âï¸| âï¸  
mute-users-owner| âï¸| â | âï¸  
read-call| â | â | â   
remove-call-member| â | âï¸| âï¸  
remove-call-member-owner| âï¸| â | âï¸  
screenshare| â | âï¸| âï¸  
send-audio| â | âï¸| âï¸  
send-audio-owner| âï¸| â | âï¸  
send-event| â | â | âï¸  
start-broadcasting| â | âï¸| âï¸  
start-broadcasting-owner| âï¸| â | âï¸  
start-recording| â | âï¸| âï¸  
start-recording-owner| âï¸| â | âï¸  
start-transcription| â | âï¸| âï¸  
start-transcription-owner| âï¸| â | âï¸  
stop-broadcasting| â | âï¸| âï¸  
stop-broadcasting-owner| âï¸| â | âï¸  
stop-recording| â | âï¸| âï¸  
stop-recording-owner| âï¸| â | âï¸  
stop-transcription| â | âï¸| âï¸  
stop-transcription-owner| âï¸| â | âï¸  
update-call| â | âï¸| âï¸  
update-call-member| â | âï¸| âï¸  
update-call-member-owner| âï¸| â | âï¸  
update-call-member-role| â | âï¸| âï¸  
update-call-member-role-owner| âï¸| â | âï¸  
update-call-owner| âï¸| â | âï¸  
update-call-permissions| â | âï¸| âï¸  
update-call-permissions-owner| âï¸| â | âï¸  
update-call-settings| â | âï¸| âï¸  
update-call-settings-owner| âï¸| â | âï¸  
  
### Scope `.app`

Permission ID| admin| moderator| user| guest  
flag-user| â | â | â | â   
mute-user| â | â | â | â   
read-flag-reports| â | â | âï¸| âï¸  
search-user| â | â | â | â   
update-flag-report| â | â | âï¸| âï¸  
update-user-owner| â | â | â | â   
  
### Scope `video:default`

Permission ID| admin| user| guest  
block-user| â | âï¸| âï¸  
block-user-owner| âï¸| â | âï¸  
create-call| â | â | âï¸  
create-call-reaction| â | â | âï¸  
delete-recording| â | âï¸| âï¸  
end-call| â | â | âï¸  
join-backstage| â | âï¸| âï¸  
join-call| â | â | â   
join-ended-call| â | â | âï¸  
list-recordings| â | â | âï¸  
mute-users| â | âï¸| âï¸  
mute-users-owner| âï¸| â | âï¸  
pin-call-track| â | âï¸| âï¸  
pin-call-track-owner| âï¸| â | âï¸  
read-call| â | â | â   
remove-call-member| â | â | âï¸  
screenshare| â | â | âï¸  
send-audio| â | â | â   
send-event| â | â | â   
send-video| â | â | â   
start-broadcasting| â | â | âï¸  
start-recording| â | â | âï¸  
start-transcription| â | â | âï¸  
stop-broadcasting| â | â | âï¸  
stop-recording| â | â | âï¸  
stop-transcription| â | â | âï¸  
update-call| â | âï¸| âï¸  
update-call-member| â | â | âï¸  
update-call-member-role| â | âï¸| âï¸  
update-call-owner| âï¸| â | âï¸  
update-call-permissions| â | âï¸| âï¸  
update-call-permissions-owner| âï¸| â | âï¸  
update-call-settings| â | âï¸| âï¸  
update-call-settings-owner| âï¸| â | âï¸  
  
### Scope `messaging`

Permission ID| admin| moderator| user| channel_member| channel_moderator  
add-links| â | â | âï¸| â | â   
add-links-owner| âï¸| âï¸| â | âï¸| âï¸  
ban-channel-member| â | â | âï¸| âï¸| â   
ban-user| â | â | âï¸| âï¸| âï¸  
create-call| â | â | âï¸| â | â   
create-channel| â | â | â | âï¸| âï¸  
create-message| â | â | âï¸| â | â   
create-message-owner| âï¸| âï¸| â | âï¸| âï¸  
create-attachment| â | â | âï¸| â | â   
create-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
create-mention| â | â | âï¸| â | â   
create-mention-owner| âï¸| âï¸| â | âï¸| âï¸  
create-reaction| â | â | âï¸| â | â   
create-reaction-owner| âï¸| âï¸| â | âï¸| âï¸  
create-system-message| â | â | âï¸| âï¸| â   
delete-attachment| â | â | âï¸| âï¸| â   
delete-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
delete-channel| â | âï¸| âï¸| âï¸| âï¸  
delete-channel-owner| âï¸| â | â | âï¸| âï¸  
delete-message| â | â | âï¸| âï¸| â   
delete-message-owner| âï¸| âï¸| â | âï¸| âï¸  
delete-reaction| â | â | âï¸| âï¸| â   
delete-reaction-owner| âï¸| âï¸| â | âï¸| âï¸  
flag-message| â | â | âï¸| â | â   
flag-message-owner| âï¸| âï¸| â | âï¸| âï¸  
join-call| â | â | âï¸| â | â   
mute-channel| â | â | âï¸| â | â   
mute-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
pin-message| â | â | âï¸| â | â   
pin-message-owner| âï¸| âï¸| â | âï¸| âï¸  
read-channel| â | â | âï¸| â | â   
read-channel-members| â | â | âï¸| â | â   
read-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸  
read-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
read-message-flags| â | â | âï¸| âï¸| â   
recreate-channel| â | âï¸| âï¸| âï¸| âï¸  
recreate-channel-owner| âï¸| â | â | âï¸| âï¸  
remove-own-channel-membership| â | â | âï¸| â | â   
remove-own-channel-membership-owner| âï¸| âï¸| â | âï¸| âï¸  
run-message-action| â | â | âï¸| â | â   
run-message-action-owner| âï¸| âï¸| â | âï¸| âï¸  
send-custom-event| â | â | âï¸| â | â   
send-custom-event-owner| âï¸| âï¸| â | âï¸| âï¸  
skip-channel-cooldown| â | â | âï¸| âï¸| â   
skip-message-moderation| â | â | âï¸| âï¸| â   
truncate-channel| â | âï¸| âï¸| âï¸| âï¸  
truncate-channel-owner| âï¸| â | â | âï¸| âï¸  
unblock-message| â | â | âï¸| âï¸| â   
update-channel| â | â | âï¸| âï¸| â   
update-channel-cooldown| â | â | âï¸| âï¸| â   
update-channel-frozen| â | â | âï¸| âï¸| â   
update-channel-members| â | â | âï¸| âï¸| â   
update-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸  
update-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
update-message| â | â | âï¸| âï¸| â   
update-message-owner| âï¸| âï¸| â | âï¸| âï¸  
upload-attachment| â | â | âï¸| â | â   
upload-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
  
### Scope `livestream`

Permission ID| admin| moderator| user| channel_moderator| guest| anonymous  
add-links| â | â | â | âï¸| âï¸| âï¸  
ban-channel-member| â | â | âï¸| â | âï¸| âï¸  
ban-user| â | â | âï¸| âï¸| âï¸| âï¸  
create-call| â | â | âï¸| â | âï¸| âï¸  
create-channel| â | â | â | âï¸| âï¸| âï¸  
create-message| â | â | â | âï¸| âï¸| âï¸  
create-attachment| â | â | â | âï¸| âï¸| âï¸  
create-mention| â | â | â | âï¸| âï¸| âï¸  
create-reaction| â | â | â | âï¸| âï¸| âï¸  
create-system-message| â | â | âï¸| â | âï¸| âï¸  
delete-attachment| â | â | âï¸| â | âï¸| âï¸  
delete-attachment-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
delete-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
delete-message| â | â | âï¸| â | âï¸| âï¸  
delete-message-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
delete-reaction| â | â | âï¸| â | âï¸| âï¸  
delete-reaction-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
flag-message| â | â | â | âï¸| â | âï¸  
join-call| â | â | â | âï¸| â | â   
mute-channel| â | â | â | âï¸| â | âï¸  
pin-message| â | â | âï¸| â | âï¸| âï¸  
pin-message-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
read-channel| â | â | â | âï¸| â | â   
read-channel-members| â | â | â | âï¸| â | â   
read-message-flags| â | â | âï¸| â | âï¸| âï¸  
recreate-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
remove-own-channel-membership| â | âï¸| âï¸| âï¸| âï¸| âï¸  
run-message-action| â | â | â | âï¸| âï¸| âï¸  
send-custom-event| â | â | â | âï¸| âï¸| âï¸  
skip-channel-cooldown| â | â | âï¸| â | âï¸| âï¸  
skip-message-moderation| â | â | âï¸| â | âï¸| âï¸  
truncate-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
unblock-message| â | â | âï¸| â | âï¸| âï¸  
update-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
update-channel-cooldown| â | â | âï¸| â | âï¸| âï¸  
update-channel-frozen| â | â | âï¸| â | âï¸| âï¸  
update-channel-members| â | âï¸| âï¸| âï¸| âï¸| âï¸  
update-message| â | â | âï¸| â | âï¸| âï¸  
update-message-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
upload-attachment| â | â | â | âï¸| âï¸| âï¸  
  
### Scope `team`

Permission ID| admin| moderator| user| channel_member| channel_moderator  
add-links| â | â | âï¸| â | â   
add-links-owner| âï¸| âï¸| â | âï¸| âï¸  
ban-channel-member| â | â | âï¸| âï¸| â   
ban-user| â | â | âï¸| âï¸| âï¸  
create-call| â | â | âï¸| â | â   
create-channel| â | â | â | âï¸| âï¸  
create-message| â | â | âï¸| â | â   
create-message-owner| âï¸| âï¸| â | âï¸| âï¸  
create-attachment| â | â | âï¸| â | â   
create-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
create-mention| â | â | âï¸| â | â   
create-mention-owner| âï¸| âï¸| â | âï¸| âï¸  
create-reaction| â | â | âï¸| â | â   
create-reaction-owner| âï¸| âï¸| â | âï¸| âï¸  
create-system-message| â | â | âï¸| âï¸| â   
delete-attachment| â | â | âï¸| âï¸| â   
delete-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
delete-channel| â | âï¸| âï¸| âï¸| âï¸  
delete-channel-owner| âï¸| â | â | âï¸| âï¸  
delete-message| â | â | âï¸| âï¸| â   
delete-message-owner| âï¸| âï¸| â | âï¸| âï¸  
delete-reaction| â | â | âï¸| âï¸| â   
delete-reaction-owner| âï¸| âï¸| â | âï¸| âï¸  
flag-message| â | â | âï¸| â | â   
flag-message-owner| âï¸| âï¸| â | âï¸| âï¸  
join-call| â | â | âï¸| â | â   
mute-channel| â | â | âï¸| â | â   
mute-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
pin-message| â | â | âï¸| â | â   
pin-message-owner| âï¸| âï¸| â | âï¸| âï¸  
read-channel| â | â | âï¸| â | â   
read-channel-members| â | â | âï¸| â | â   
read-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸  
read-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
read-message-flags| â | â | âï¸| âï¸| â   
recreate-channel| â | âï¸| âï¸| âï¸| âï¸  
recreate-channel-owner| âï¸| â | â | âï¸| âï¸  
remove-own-channel-membership| â | â | âï¸| â | â   
remove-own-channel-membership-owner| âï¸| âï¸| â | âï¸| âï¸  
run-message-action| â | â | âï¸| â | â   
run-message-action-owner| âï¸| âï¸| â | âï¸| âï¸  
send-custom-event| â | â | âï¸| â | â   
send-custom-event-owner| âï¸| âï¸| â | âï¸| âï¸  
skip-channel-cooldown| â | â | âï¸| âï¸| â   
skip-message-moderation| â | â | âï¸| âï¸| â   
truncate-channel| â | âï¸| âï¸| âï¸| âï¸  
truncate-channel-owner| âï¸| â | â | âï¸| âï¸  
unblock-message| â | â | âï¸| âï¸| â   
update-channel| â | â | âï¸| âï¸| â   
update-channel-cooldown| â | â | âï¸| âï¸| â   
update-channel-frozen| â | â | âï¸| âï¸| â   
update-channel-members| â | â | âï¸| âï¸| â   
update-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸  
update-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
update-message| â | â | âï¸| âï¸| â   
update-message-owner| âï¸| âï¸| â | âï¸| âï¸  
upload-attachment| â | â | âï¸| â | â   
upload-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
  
### Scope `commerce`

Permission ID| admin| moderator| user| channel_member| channel_moderator|
guest  
add-links| â | â | âï¸| â | â | â   
add-links-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
ban-channel-member| â | â | âï¸| âï¸| â | âï¸  
ban-user| â | â | âï¸| âï¸| âï¸| âï¸  
create-call| â | â | âï¸| âï¸| â | âï¸  
create-channel| â | â | âï¸| âï¸| âï¸| â   
create-message| â | â | âï¸| â | â | âï¸  
create-message-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
create-attachment| â | â | âï¸| â | â | âï¸  
create-attachment-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
create-mention| â | â | âï¸| â | â | âï¸  
create-mention-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
create-reaction| â | â | âï¸| â | â | âï¸  
create-reaction-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
create-system-message| â | â | âï¸| âï¸| â | âï¸  
delete-attachment| â | â | âï¸| âï¸| â | âï¸  
delete-attachment-owner| âï¸| âï¸| â | âï¸| âï¸| â   
delete-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
delete-message| â | â | âï¸| âï¸| â | âï¸  
delete-message-owner| âï¸| âï¸| â | âï¸| âï¸| â   
delete-reaction| â | â | âï¸| âï¸| â | âï¸  
delete-reaction-owner| âï¸| âï¸| â | âï¸| âï¸| â   
flag-message| â | â | âï¸| â | â | âï¸  
flag-message-owner| âï¸| âï¸| â | âï¸| âï¸| â   
join-call| â | â | âï¸| â | â | âï¸  
mute-channel| â | â | âï¸| â | â | âï¸  
mute-channel-owner| âï¸| âï¸| â | âï¸| âï¸| â   
pin-message| â | â | âï¸| âï¸| â | âï¸  
pin-message-owner| âï¸| âï¸| â | âï¸| âï¸| â   
read-channel| â | â | âï¸| â | â | âï¸  
read-channel-members| â | â | âï¸| â | â | âï¸  
read-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸| â   
read-channel-owner| âï¸| âï¸| â | âï¸| âï¸| â   
read-message-flags| â | â | âï¸| âï¸| â | âï¸  
recreate-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
remove-own-channel-membership| â | â | âï¸| â | â | âï¸  
remove-own-channel-membership-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
run-message-action| â | â | âï¸| â | â | âï¸  
run-message-action-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
send-custom-event| â | â | âï¸| â | â | âï¸  
send-custom-event-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
skip-channel-cooldown| â | â | âï¸| âï¸| â | âï¸  
skip-message-moderation| â | â | âï¸| âï¸| â | âï¸  
truncate-channel| â | âï¸| âï¸| âï¸| âï¸| âï¸  
unblock-message| â | â | âï¸| âï¸| â | âï¸  
update-channel| â | â | âï¸| âï¸| â | âï¸  
update-channel-cooldown| â | â | âï¸| âï¸| â | âï¸  
update-channel-frozen| â | â | âï¸| âï¸| â | âï¸  
update-channel-members| â | â | âï¸| âï¸| â | âï¸  
update-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸| â   
update-message| â | â | âï¸| âï¸| â | âï¸  
update-message-owner| âï¸| âï¸| â | âï¸| âï¸| â   
upload-attachment| â | â | âï¸| â | â | â   
upload-attachment-owner| âï¸| âï¸| â | âï¸| âï¸| âï¸  
  
### Scope `gaming`

Permission ID| admin| moderator| user| channel_member| channel_moderator  
add-links| â | â | âï¸| â | â   
add-links-owner| âï¸| âï¸| â | âï¸| âï¸  
ban-channel-member| â | â | âï¸| âï¸| â   
ban-user| â | â | âï¸| âï¸| âï¸  
create-call| â | â | âï¸| â | â   
create-channel| â | âï¸| âï¸| âï¸| âï¸  
create-message| â | â | âï¸| â | â   
create-message-owner| âï¸| âï¸| â | âï¸| âï¸  
create-attachment| â | â | âï¸| â | â   
create-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
create-mention| â | â | âï¸| â | â   
create-mention-owner| âï¸| âï¸| â | âï¸| âï¸  
create-reaction| â | â | âï¸| â | â   
create-reaction-owner| âï¸| âï¸| â | âï¸| âï¸  
create-system-message| â | â | âï¸| âï¸| â   
delete-attachment| â | â | âï¸| âï¸| â   
delete-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
delete-channel| â | âï¸| âï¸| âï¸| âï¸  
delete-message| â | â | âï¸| âï¸| â   
delete-message-owner| âï¸| âï¸| â | âï¸| âï¸  
delete-reaction| â | â | âï¸| âï¸| â   
delete-reaction-owner| âï¸| âï¸| â | âï¸| âï¸  
flag-message| â | â | âï¸| â | â   
flag-message-owner| âï¸| âï¸| â | âï¸| âï¸  
join-call| â | â | âï¸| â | â   
mute-channel| â | â | âï¸| â | â   
mute-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
pin-message| â | â | âï¸| âï¸| â   
read-channel| â | â | âï¸| â | â   
read-channel-members| â | â | âï¸| â | â   
read-channel-members-owner| âï¸| âï¸| â | âï¸| âï¸  
read-channel-owner| âï¸| âï¸| â | âï¸| âï¸  
read-message-flags| â | â | âï¸| âï¸| â   
recreate-channel| â | âï¸| âï¸| âï¸| âï¸  
remove-own-channel-membership| â | â | âï¸| â | â   
remove-own-channel-membership-owner| âï¸| âï¸| â | âï¸| âï¸  
run-message-action| â | â | âï¸| â | â   
run-message-action-owner| âï¸| âï¸| â | âï¸| âï¸  
send-custom-event| â | â | âï¸| â | â   
send-custom-event-owner| âï¸| âï¸| â | âï¸| âï¸  
skip-channel-cooldown| â | â | âï¸| âï¸| â   
skip-message-moderation| â | â | âï¸| âï¸| â   
truncate-channel| â | âï¸| âï¸| âï¸| âï¸  
unblock-message| â | â | âï¸| âï¸| â   
update-channel| â | âï¸| âï¸| âï¸| âï¸  
update-channel-cooldown| â | â | âï¸| âï¸| â   
update-channel-frozen| â | â | âï¸| âï¸| â   
update-channel-members| â | âï¸| âï¸| âï¸| âï¸  
update-message| â | â | âï¸| âï¸| â   
update-message-owner| âï¸| âï¸| â | âï¸| âï¸  
upload-attachment| â | â | âï¸| â | â   
upload-attachment-owner| âï¸| âï¸| â | âï¸| âï¸  
  
## Multi-Tenant Default Grants

In tables below you will find default permission grants for builtin roles that
designed for multi-tenant applications. They are useful for [multi-tenant
applications](/chat/docs/react/multi_tenant_chat/) only.

By default, for multi-tenant applications, all objects (users, channels, and
messages) must belong to the same team to be able to interact. These multi-
tenant permissions enable overriding that behavior, so that certain users can
have permissions to interact with objects on any team

### Scope `video:livestream`

Permission ID  
  
### Scope `video:development`

Permission ID  
  
### Scope `.app`

Permission ID| global_moderator| global_admin  
flag-user-any-team| â | â   
mute-user-any-team| â | â   
read-flag-reports-any-team| â | â   
search-user-any-team| â | â   
update-flag-report-any-team| â | â   
update-user-owner| â | â   
  
### Scope `video:audio_room`

Permission ID  
  
### Scope `video:default`

Permission ID  
  
### Scope `messaging`

Permission ID| global_moderator| global_admin  
add-links-any-team| â | â   
ban-channel-member-any-team| â | â   
ban-user-any-team| â | â   
create-call-any-team| â | â   
create-channel-any-team| â | â   
create-message-any-team| â | â   
create-attachment-any-team| â | â   
create-mention-any-team| â | â   
create-reaction-any-team| â | â   
create-system-message-any-team| â | â   
delete-attachment-any-team| â | â   
delete-channel-any-team| âï¸| â  
delete-channel-owner-any-team| â | âï¸  
delete-message-any-team| â | â   
delete-reaction-any-team| â | â   
flag-message-any-team| â | â   
join-call-any-team| â | â   
mute-channel-any-team| â | â   
pin-message-any-team| â | â   
read-channel-any-team| â | â   
read-channel-members-any-team| â | â   
read-message-flags-any-team| â | â   
recreate-channel-any-team| âï¸| â  
recreate-channel-owner-any-team| â | âï¸  
remove-own-channel-membership-any-team| â | â   
run-message-action-any-team| â | â   
send-custom-event-any-team| â | â   
skip-channel-cooldown-any-team| â | â   
skip-message-moderation-any-team| â | â   
truncate-channel-any-team| âï¸| â  
truncate-channel-owner-any-team| â | âï¸  
unblock-message-any-team| â | â   
update-channel-any-team| â | â   
update-channel-cooldown-any-team| â | â   
update-channel-frozen-any-team| â | â   
update-channel-members-any-team| â | â   
update-message-any-team| â | â   
upload-attachment-any-team| â | â   
  
### Scope `livestream`

Permission ID| global_moderator| global_admin  
add-links-any-team| â | â   
ban-channel-member-any-team| â | â   
ban-user-any-team| â | â   
create-call-any-team| â | â   
create-channel-any-team| â | â   
create-message-any-team| â | â   
create-attachment-any-team| â | â   
create-mention-any-team| â | â   
create-reaction-any-team| â | â   
create-system-message-any-team| â | â   
delete-attachment-any-team| â | â   
delete-channel-any-team| âï¸| â  
delete-message-any-team| â | â   
delete-reaction-any-team| â | â   
flag-message-any-team| â | â   
join-call-any-team| â | â   
mute-channel-any-team| â | â   
pin-message-any-team| â | â   
read-channel-any-team| â | â   
read-channel-members-any-team| â | â   
read-message-flags-any-team| â | â   
recreate-channel-any-team| âï¸| â  
remove-own-channel-membership-any-team| âï¸| â  
run-message-action-any-team| â | â   
send-custom-event-any-team| â | â   
skip-channel-cooldown-any-team| â | â   
skip-message-moderation-any-team| â | â   
truncate-channel-any-team| âï¸| â  
unblock-message-any-team| â | â   
update-channel-any-team| âï¸| â  
update-channel-cooldown-any-team| â | â   
update-channel-frozen-any-team| â | â   
update-channel-members-any-team| âï¸| â  
update-message-any-team| â | â   
upload-attachment-any-team| â | â   
  
### Scope `team`

Permission ID| global_moderator| global_admin  
add-links-any-team| â | â   
ban-channel-member-any-team| â | â   
ban-user-any-team| â | â   
create-call-any-team| â | â   
create-channel-any-team| â | â   
create-message-any-team| â | â   
create-attachment-any-team| â | â   
create-mention-any-team| â | â   
create-reaction-any-team| â | â   
create-system-message-any-team| â | â   
delete-attachment-any-team| â | â   
delete-channel-any-team| âï¸| â  
delete-channel-owner-any-team| â | âï¸  
delete-message-any-team| â | â   
delete-reaction-any-team| â | â   
flag-message-any-team| â | â   
join-call-any-team| â | â   
mute-channel-any-team| â | â   
pin-message-any-team| â | â   
read-channel-any-team| â | â   
read-channel-members-any-team| â | â   
read-message-flags-any-team| â | â   
recreate-channel-any-team| âï¸| â  
recreate-channel-owner-any-team| â | âï¸  
remove-own-channel-membership-any-team| â | â   
run-message-action-any-team| â | â   
send-custom-event-any-team| â | â   
skip-channel-cooldown-any-team| â | â   
skip-message-moderation-any-team| â | â   
truncate-channel-any-team| âï¸| â  
truncate-channel-owner-any-team| â | âï¸  
unblock-message-any-team| â | â   
update-channel-any-team| â | â   
update-channel-cooldown-any-team| â | â   
update-channel-frozen-any-team| â | â   
update-channel-members-any-team| â | â   
update-message-any-team| â | â   
upload-attachment-any-team| â | â   
  
### Scope `commerce`

Permission ID| global_moderator| global_admin  
add-links-any-team| â | â   
ban-channel-member-any-team| â | â   
ban-user-any-team| â | â   
create-call-any-team| â | â   
create-channel-any-team| â | â   
create-message-any-team| â | â   
create-attachment-any-team| â | â   
create-mention-any-team| â | â   
create-reaction-any-team| â | â   
create-system-message-any-team| â | â   
delete-attachment-any-team| â | â   
delete-channel-any-team| âï¸| â  
delete-message-any-team| â | â   
delete-reaction-any-team| â | â   
flag-message-any-team| â | â   
join-call-any-team| â | â   
mute-channel-any-team| â | â   
pin-message-any-team| â | â   
read-channel-any-team| â | â   
read-channel-members-any-team| â | â   
read-message-flags-any-team| â | â   
recreate-channel-any-team| âï¸| â  
remove-own-channel-membership-any-team| â | â   
run-message-action-any-team| â | â   
send-custom-event-any-team| â | â   
skip-channel-cooldown-any-team| â | â   
skip-message-moderation-any-team| â | â   
truncate-channel-any-team| âï¸| â  
unblock-message-any-team| â | â   
update-channel-any-team| â | â   
update-channel-cooldown-any-team| â | â   
update-channel-frozen-any-team| â | â   
update-channel-members-any-team| â | â   
update-message-any-team| â | â   
upload-attachment-any-team| â | â   
  
### Scope `gaming`

Permission ID| global_moderator| global_admin  
add-links-any-team| â | â   
ban-channel-member-any-team| â | â   
ban-user-any-team| â | â   
create-call-any-team| â | â   
create-channel-any-team| âï¸| â  
create-message-any-team| â | â   
create-attachment-any-team| â | â   
create-mention-any-team| â | â   
create-reaction-any-team| â | â   
create-system-message-any-team| â | â   
delete-attachment-any-team| â | â   
delete-channel-any-team| âï¸| â  
delete-message-any-team| â | â   
delete-reaction-any-team| â | â   
flag-message-any-team| â | â   
join-call-any-team| â | â   
mute-channel-any-team| â | â   
pin-message-any-team| â | â   
read-channel-any-team| â | â   
read-channel-members-any-team| â | â   
read-message-flags-any-team| â | â   
recreate-channel-any-team| âï¸| â  
remove-own-channel-membership-any-team| â | â   
run-message-action-any-team| â | â   
send-custom-event-any-team| â | â   
skip-channel-cooldown-any-team| â | â   
skip-message-moderation-any-team| â | â   
truncate-channel-any-team| âï¸| â  
unblock-message-any-team| â | â   
update-channel-any-team| âï¸| â  
update-channel-cooldown-any-team| â | â   
update-channel-frozen-any-team| â | â   
update-channel-members-any-team| âï¸| â  
update-message-any-team| â | â   
upload-attachment-any-team| â | â   
  
Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousMulti-Tenant &
Teams](/chat/docs/react/multi_tenant_chat/)[NextChannel Setting
Overwrites](/chat/docs/react/channel-level_settings/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/react/permissions_reference.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/permissions_reference.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/permissions_reference.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/permissions_reference.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/permissions_reference.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/permissions_reference.md)

On this page:

  * Actions
  * Default Grants

    * Scope video:development
    * Scope video:livestream
    * Scope video:audio_room
    * Scope .app
    * Scope video:default
    * Scope messaging
    * Scope livestream
    * Scope team
    * Scope commerce
    * Scope gaming

  * Multi-Tenant Default Grants

    * Scope video:livestream
    * Scope video:development
    * Scope .app
    * Scope video:audio_room
    * Scope video:default
    * Scope messaging
    * Scope livestream
    * Scope team
    * Scope commerce
    * Scope gaming

Is this helpful?

Thank you .

An error has occurred.
# Source: https://docs.aws.amazon.com/chime/latest/APIReference/llms.txt

# Amazon Chime API Reference

> The Amazon Chime application programming interface (API) is designed so administrators can perform key tasks, such as creating and managing Amazon Chime accounts, users, and Voice Connectors. This guide provides detailed information about the Amazon Chime API, including operations, types, inputs and outputs, and error codes.

- [Welcome](https://docs.aws.amazon.com/chime/latest/APIReference/welcome.html)
- [Common Errors](https://docs.aws.amazon.com/chime/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/chime/latest/APIReference/API_Operations.html)

- [AssociatePhoneNumberWithUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumberWithUser.html): Associates a phone number with the specified Amazon Chime user.
- [AssociateSigninDelegateGroupsWithAccount](https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociateSigninDelegateGroupsWithAccount.html): Associates the specified sign-in delegate groups with the specified Amazon Chime account.
- [BatchCreateRoomMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateRoomMembership.html): Adds up to 50 members to a chat room in an Amazon Chime Enterprise account.
- [BatchDeletePhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchDeletePhoneNumber.html): Moves phone numbers into the Deletion queue.
- [BatchSuspendUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchSuspendUser.html): Suspends up to 50 users from a Team or EnterpriseLWA Amazon Chime account.
- [BatchUnsuspendUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchUnsuspendUser.html): Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime EnterpriseLWA account.
- [BatchUpdatePhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchUpdatePhoneNumber.html): Updates phone number product types or calling names.
- [BatchUpdateUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchUpdateUser.html): Updates user details within the object for up to 20 users for the specified Amazon Chime account.
- [CreateAccount](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAccount.html): Creates an Amazon Chime account under the administrator's AWS account.
- [CreateBot](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateBot.html): Creates a bot for an Amazon Chime Enterprise account.
- [CreateMeetingDialOut](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingDialOut.html): Uses the join token and call metadata in a meeting request (From number, To number, and so forth) to initiate an outbound call to a public switched telephone network (PSTN) and join them into a Chime meeting.
- [CreatePhoneNumberOrder](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreatePhoneNumberOrder.html): Creates an order for phone numbers to be provisioned.
- [CreateRoom](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateRoom.html): Creates a chat room for the specified Amazon Chime Enterprise account.
- [CreateRoomMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateRoomMembership.html): Adds a member to a chat room in an Amazon Chime Enterprise account.
- [CreateUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateUser.html): Creates a user under the specified Amazon Chime account.
- [DeleteAccount](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAccount.html): Deletes the specified Amazon Chime account.
- [DeleteEventsConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteEventsConfiguration.html): Deletes the events configuration that allows a bot to receive outgoing events.
- [DeletePhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeletePhoneNumber.html): Moves the specified phone number into the Deletion queue.
- [DeleteRoom](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteRoom.html): Deletes a chat room in an Amazon Chime Enterprise account.
- [DeleteRoomMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteRoomMembership.html): Removes a member from a chat room in an Amazon Chime Enterprise account.
- [DisassociatePhoneNumberFromUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumberFromUser.html): Disassociates the primary provisioned phone number from the specified Amazon Chime user.
- [DisassociateSigninDelegateGroupsFromAccount](https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociateSigninDelegateGroupsFromAccount.html): Disassociates the specified sign-in delegate groups from the specified Amazon Chime account.
- [GetAccount](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAccount.html): Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.
- [GetAccountSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAccountSettings.html): Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dialout settings.
- [GetBot](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetBot.html): Retrieves details for the specified bot, such as bot email address, bot type, status, and display name.
- [GetEventsConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetEventsConfiguration.html): Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.
- [GetGlobalSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetGlobalSettings.html): Retrieves global settings for the administrator's AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.
- [GetPhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetPhoneNumber.html): Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.
- [GetPhoneNumberOrder](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetPhoneNumberOrder.html): Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.
- [GetPhoneNumberSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetPhoneNumberSettings.html): Retrieves the phone number settings for the administrator's AWS account, such as the default outbound calling name.
- [GetRetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetRetentionSettings.html): Gets the retention settings for the specified Amazon Chime Enterprise account.
- [GetRoom](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetRoom.html): Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.
- [GetUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetUser.html): Retrieves details for the specified user ID, such as primary email address, license type,and personal meeting PIN.
- [GetUserSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetUserSettings.html): Retrieves settings for the specified user ID, such as any associated phone number settings.
- [InviteUsers](https://docs.aws.amazon.com/chime/latest/APIReference/API_InviteUsers.html): Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime Team account.
- [ListAccounts](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAccounts.html): Lists the Amazon Chime accounts under the administrator's AWS account.
- [ListBots](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListBots.html): Lists the bots associated with the administrator's Amazon Chime Enterprise account ID.
- [ListPhoneNumberOrders](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListPhoneNumberOrders.html): Lists the phone number orders for the administrator's Amazon Chime account.
- [ListPhoneNumbers](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListPhoneNumbers.html): Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.
- [ListRoomMemberships](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListRoomMemberships.html): Lists the membership details for the specified room in an Amazon Chime Enterprise account, such as the members' IDs, email addresses, and names.
- [ListRooms](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListRooms.html): Lists the room details for the specified Amazon Chime Enterprise account.
- [ListSupportedPhoneNumberCountries](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSupportedPhoneNumberCountries.html): Lists supported phone number countries.
- [ListUsers](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListUsers.html): Lists the users that belong to the specified Amazon Chime account.
- [LogoutUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_LogoutUser.html): Logs out the specified user from all of the devices they are currently logged into.
- [PutEventsConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutEventsConfiguration.html): Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime.
- [PutRetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutRetentionSettings.html): Puts retention settings for the specified Amazon Chime Enterprise account.
- [RedactConversationMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactConversationMessage.html): Redacts the specified message from the specified Amazon Chime conversation.
- [RedactRoomMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactRoomMessage.html): Redacts the specified message from the specified Amazon Chime channel.
- [RegenerateSecurityToken](https://docs.aws.amazon.com/chime/latest/APIReference/API_RegenerateSecurityToken.html): Regenerates the security token for a bot.
- [ResetPersonalPIN](https://docs.aws.amazon.com/chime/latest/APIReference/API_ResetPersonalPIN.html): Resets the personal meeting PIN for the specified user on an Amazon Chime account.
- [RestorePhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_RestorePhoneNumber.html): Moves a phone number from the Deletion queue back into the phone number Inventory.
- [SearchAvailablePhoneNumbers](https://docs.aws.amazon.com/chime/latest/APIReference/API_SearchAvailablePhoneNumbers.html): Searches for phone numbers that can be ordered.
- [UpdateAccount](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAccount.html): Updates account details for the specified Amazon Chime account.
- [UpdateAccountSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAccountSettings.html): Updates the settings for the specified Amazon Chime account.
- [UpdateBot](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateBot.html): Updates the status of the specified bot, such as starting or stopping the bot from running in your Amazon Chime Enterprise account.
- [UpdateGlobalSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateGlobalSettings.html): Updates global settings for the administrator's AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.
- [UpdatePhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdatePhoneNumber.html): Updates phone number details, such as product type or calling name, for the specified phone number ID.
- [UpdatePhoneNumberSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdatePhoneNumberSettings.html): Updates the phone number settings for the administrator's AWS account, such as the default outbound calling name.
- [UpdateRoom](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateRoom.html): Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.
- [UpdateRoomMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateRoomMembership.html): Updates room membership details, such as the member role, for a room in an Amazon Chime Enterprise account.
- [UpdateUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateUser.html): Updates user details for a specified user ID.
- [UpdateUserSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateUserSettings.html): Updates the settings for the specified user, such as phone number settings.


## [Data Types](https://docs.aws.amazon.com/chime/latest/APIReference/API_Types.html)

- [Account](https://docs.aws.amazon.com/chime/latest/APIReference/API_Account.html): The Amazon Chime account details.
- [AccountSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_AccountSettings.html): Settings related to the Amazon Chime account.
- [AlexaForBusinessMetadata](https://docs.aws.amazon.com/chime/latest/APIReference/API_AlexaForBusinessMetadata.html): The Alexa for Business metadata associated with an Amazon Chime user, used to integrate Alexa for Business with a device.
- [Bot](https://docs.aws.amazon.com/chime/latest/APIReference/API_Bot.html): A resource that allows Enterprise account administrators to configure an interface to receive events from Amazon Chime.
- [BusinessCallingSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_BusinessCallingSettings.html): The Amazon Chime Business Calling settings for the administrator's AWS account.
- [ConversationRetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_ConversationRetentionSettings.html): The retention settings that determine how long to retain conversation messages for an Amazon Chime Enterprise account.
- [EventsConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_EventsConfiguration.html): The configuration that allows a bot to receive outgoing events.
- [Invite](https://docs.aws.amazon.com/chime/latest/APIReference/API_Invite.html): Invitation object returned after emailing users to invite them to join the Amazon Chime Team account.
- [Member](https://docs.aws.amazon.com/chime/latest/APIReference/API_Member.html): The member details, such as email address, name, member ID, and member type.
- [MemberError](https://docs.aws.amazon.com/chime/latest/APIReference/API_MemberError.html): The list of errors returned when a member action results in an error.
- [MembershipItem](https://docs.aws.amazon.com/chime/latest/APIReference/API_MembershipItem.html): Membership details, such as member ID and member role.
- [OrderedPhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_OrderedPhoneNumber.html): A phone number for which an order has been placed.
- [PhoneNumber](https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumber.html): A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.
- [PhoneNumberAssociation](https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberAssociation.html): The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.
- [PhoneNumberCapabilities](https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberCapabilities.html): The phone number capabilities for Amazon Chime Business Calling phone numbers, such as enabled inbound and outbound calling and text messaging.
- [PhoneNumberCountry](https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberCountry.html): The phone number country.
- [PhoneNumberError](https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberError.html): If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
- [PhoneNumberOrder](https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberOrder.html): The details of a phone number order created for Amazon Chime.
- [RetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_RetentionSettings.html): The retention settings for an Amazon Chime Enterprise account that determine how long to retain items such as chat-room messages and chat-conversation messages.
- [Room](https://docs.aws.amazon.com/chime/latest/APIReference/API_Room.html): The Amazon Chime chat room details.
- [RoomMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_RoomMembership.html): The room membership details.
- [RoomRetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_RoomRetentionSettings.html): The retention settings that determine how long to retain chat-room messages for an Amazon Chime Enterprise account.
- [SigninDelegateGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_SigninDelegateGroup.html): An Active Directory (AD) group whose members are granted permission to act as delegates.
- [TelephonySettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_TelephonySettings.html): Settings that allow management of telephony permissions for an Amazon Chime user, such as inbound and outbound calling and text messaging.
- [UpdatePhoneNumberRequestItem](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdatePhoneNumberRequestItem.html): The phone number ID, product type, or calling name fields to update, used with the and actions.
- [UpdateUserRequestItem](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateUserRequestItem.html): The user ID and user fields to update, used with the action.
- [User](https://docs.aws.amazon.com/chime/latest/APIReference/API_User.html): The user on the Amazon Chime account.
- [UserError](https://docs.aws.amazon.com/chime/latest/APIReference/API_UserError.html): The list of errors returned when errors are encountered during the , , or actions.
- [UserSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_UserSettings.html): Settings associated with an Amazon Chime user, including inbound and outbound calling and text messaging.
- [VoiceConnectorSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_VoiceConnectorSettings.html): The Amazon Chime Voice Connector settings.

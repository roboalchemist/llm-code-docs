# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/index.md

---

title: RTKChat · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/index.md
---

[]()

This is the chat module, which can be used to send and receive messages from the meeting.

* [RTKChat](#module_RTKChat)

  * [module.exports](#exp_module_RTKChat--module.exports) ⏏

    * [new module.exports(context, chatSocketHandler, self, participants)](#new_module_RTKChat--module.exports_new)
    *
    * [.telemetry](#module_RTKChat--module.exports+telemetry)
    * [.pinned](#module_RTKChat--module.exports+pinned)
    * [.setMaxTextLimit(limit)](#module_RTKChat--module.exports+setMaxTextLimit)
    * [.sendMessageInternal(message, \[participantIds\])](#module_RTKChat--module.exports+sendMessageInternal)
    * [.sendTextMessageInternal(message, \[peerIds\])](#module_RTKChat--module.exports+sendTextMessageInternal)
    * [.sendImageMessageInternal(image, \[peerIds\])](#module_RTKChat--module.exports+sendImageMessageInternal)
    * [.sendFileMessageInternal(file, \[peerIds\])](#module_RTKChat--module.exports+sendFileMessageInternal)
    * [.updateRateLimits(num, period)](#module_RTKChat--module.exports+updateRateLimits)
    * [.sendTextMessage(message, \[peerIds\])](#module_RTKChat--module.exports+sendTextMessage)
    * [.sendCustomMessage(message, \[peerIds\])](#module_RTKChat--module.exports+sendCustomMessage)
    * [.sendImageMessage(image, \[peerIds\])](#module_RTKChat--module.exports+sendImageMessage)
    * [.sendFileMessage(file, \[peerIds\])](#module_RTKChat--module.exports+sendFileMessage)
    * [.sendMessage(message, \[participantIds\])](#module_RTKChat--module.exports+sendMessage)
    * [.editTextMessage(messageId, message)](#module_RTKChat--module.exports+editTextMessage)
    * [.editImageMessage(messageId, image)](#module_RTKChat--module.exports+editImageMessage)
    * [.editFileMessage(messageId, file)](#module_RTKChat--module.exports+editFileMessage)
    * [.editMessage(messageId, message)](#module_RTKChat--module.exports+editMessage)
    * [.deleteMessage(messageId)](#module_RTKChat--module.exports+deleteMessage)
    *
    *
    * [.pin(id)](#module_RTKChat--module.exports+pin)
    * [.unpin(id)](#module_RTKChat--module.exports+unpin)
    * [.fetchPublicMessages(options)](#module_RTKChat--module.exports+fetchPublicMessages)
    * [.fetchPrivateMessages(options)](#module_RTKChat--module.exports+fetchPrivateMessages)
    * [.fetchPinnedMessages(options)](#module_RTKChat--module.exports+fetchPinnedMessages)
    *
    *

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, chatSocketHandler, self, participants)

| Param | Type |
| - | - |
| context | `Context` |
| chatSocketHandler | `RTKChatSocketHandler` |
| self | `Self` |
| participants | `Participants` |

[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKChat--module.exports)\
[]()

#### module.exports.telemetry

**Kind**: instance property of [`module.exports`](#exp_module_RTKChat--module.exports)\
[]()

#### module.exports.pinned

**Kind**: instance property of [`module.exports`](#exp_module_RTKChat--module.exports)\
**Deprecated.**: This property is deprectated. Please use `fetchPinnedMessages()` instead. Returns an array of pinned messages.\
[]()

#### module.exports.setMaxTextLimit(limit)

Set the max character limit of a text message

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| limit | `number` | Max character limit for a text message. |

[]()

#### module.exports.sendMessageInternal(message, \[participantIds])

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| message | `MessagePayload` | Message payload to send. |
| \[participantIds] | `Array.<string>` | Participant ids to send the message to. |

[]()

#### module.exports.sendTextMessageInternal(message, \[peerIds])

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| message | `string` | Text message to send. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.sendImageMessageInternal(image, \[peerIds])

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| image | `File` \| `ReactNativeFile` | Image file to send. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.sendFileMessageInternal(file, \[peerIds])

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| file | `File` \| `ReactNativeFile` | File to send. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.updateRateLimits(num, period)

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type |
| - | - |
| num | `number` |
| period | `number` |

[]()

#### module.exports.sendTextMessage(message, \[peerIds])

Sends a chat text message to the room.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| message | `string` | The message that must be sent to the room. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.sendCustomMessage(message, \[peerIds])

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| message | `CustomMessagePayload` | Custom message payload. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.sendImageMessage(image, \[peerIds])

Sends an image message to the meeting.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| image | `File` \| `ReactNativeFile` | The image that is to be sent. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.sendFileMessage(file, \[peerIds])

Sends a file to the meeting.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| file | `File` \| `ReactNativeFile` | A File object. |
| \[peerIds] | `Array.<string>` | Peer ids to send the message to. |

[]()

#### module.exports.sendMessage(message, \[participantIds])

Sends a message to the meeting. This method can be used to send text, image, or file messages. The message type is determined by the key 'type' in `message` object.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| message | `MessagePayload` | An object including the type and content of the message. |
| \[participantIds] | `Array.<string>` | An array including the userIds of the participants. |

[]()

#### module.exports.editTextMessage(messageId, message)

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| messageId | `string` | Id of the message to edit. |
| message | `string` | Updated text message. |

[]()

#### module.exports.editImageMessage(messageId, image)

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| messageId | `string` | Id of the message to edit. |
| image | `File` \| `ReactNativeFile` | Updated image file. |

[]()

#### module.exports.editFileMessage(messageId, file)

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| messageId | `string` | Id of the message to edit. |
| file | `File` \| `ReactNativeFile` | Updated file. |

[]()

#### module.exports.editMessage(messageId, message)

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| messageId | `string` | Id of the message to edit. |
| message | `MessagePayload` | Updated message payload. |

[]()

#### module.exports.deleteMessage(messageId)

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| messageId | `string` | Id of the message to delete. |

[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| userId | `string` | The user id of the user that sent the message. |

[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| type | `'text'` \| `'image'` \| `'file'` \| `'custom'` \| `'poll'` | 'text', 'image', 'file', 'custom', or 'poll'. |

[]()

#### module.exports.pin(id)

Pins a chat message

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| id | `string` | ID of the message to be pinned |

[]()

#### module.exports.unpin(id)

Unpins a chat message

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| id | `string` | ID of the message to be unpinned |

[]()

#### module.exports.fetchPublicMessages(options)

Fetches messages from the chat with pagination.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| options | `FetchMessageOptions` | Configuration options for fetching messages, including timestamp, limit, and direction for pagination. |

[]()

#### module.exports.fetchPrivateMessages(options)

Fetches private messages between the current user and another participant with pagination.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| options | `FetchPrivateMessagesOptions` | Configuration options for fetching private messages, including private RTKChat ID (User ID of the participant) and pagination settings. |

[]()

#### module.exports.fetchPinnedMessages(options)

Fetches pinned messages with pagination.

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Description |
| - | - | - |
| options | `FetchMessageOptions` | Configuration options for fetching pinned messages, including timestamp, limit, and direction. |

[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type | Default |
| - | - | - |
| timeStamp | `number` | |
| size | `number` | |
| reversed | `boolean` | |
| \[offset] | `number` | `0` |

[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RTKChat--module.exports)

| Param | Type |
| - | - |
| query | `string` |
| \[filters] | `SearchFilters` |

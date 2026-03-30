# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/index.md

---

title: RTKPolls · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/index.md
---

[]()

The RTKPolls module consists of the polls that have been created in the meeting.

* [RTKPolls](#module_RTKPolls)

  * [.items](#module_RTKPolls+items)
  * [.create(question, options, anonymous, hideVotes)](#module_RTKPolls+create)
  * [.vote(pollId, index)](#module_RTKPolls+vote)

[]()

### meeting.polls.items

An array of poll items.

**Kind**: instance property of [`RTKPolls`](#module_RTKPolls)\
[]()

### meeting.polls.create(question, options, anonymous, hideVotes)

Creates a poll in the meeting.

**Kind**: instance method of [`RTKPolls`](#module_RTKPolls)

| Param | Default | Description |
| - | - | - |
| question | | The question that is to be voted for. |
| options | | The options of the poll. |
| anonymous | `false` | If true, the poll votes are anonymous. |
| hideVotes | `false` | If true, the votes on the poll are hidden. |

[]()

### meeting.polls.vote(pollId, index)

Casts a vote on an existing poll.

**Kind**: instance method of [`RTKPolls`](#module_RTKPolls)

| Param | Description |
| - | - |
| pollId | The ID of the poll that is to be voted on. |
| index | The index of the option. |

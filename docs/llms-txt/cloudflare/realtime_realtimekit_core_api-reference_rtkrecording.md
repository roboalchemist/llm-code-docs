# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/index.md

---

title: RTKRecording · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/index.md
---

[]()

The RTKRecording module represents the state of the current recording, and allows to start/stop recordings and check if there's a recording in progress.

* [RTKRecording](#module_RTKRecording)

  * [.telemetry](#module_RTKRecording+telemetry)
  * [.start()](#module_RTKRecording+start)
  * [.stop()](#module_RTKRecording+stop)
  * [.pause()](#module_RTKRecording+pause)
  * [.resume()](#module_RTKRecording+resume)

[]()

### meeting.recording.telemetry

**Kind**: instance property of [`RTKRecording`](#module_RTKRecording)\
[]()

### meeting.recording.start()

Starts recording the meeting.

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)\
[]()

### meeting.recording.stop()

Stops all recording currently in 'RECORDING' state

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)\
[]()

### meeting.recording.pause()

Pauses all recording currently in 'RECORDING' state

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)\
[]()

### meeting.recording.resume()

Resumes all recording currently in 'PAUSED' state

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)

# Source: https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-ui-kit/index.md

---

title: Android UI Kit SDK · Cloudflare Realtime docs
description: Subscribe to RSS
lastUpdated: 2026-01-16T11:57:12.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-ui-kit/
  md: https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-ui-kit/index.md
---

[Subscribe to RSS](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-ui-kit/index.xml)

## 2026-02-06

**RealtimeKit Android UI Kit 0.3.4**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.6.1](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2026-02-06)

## 2026-01-14

**RealtimeKit Android UI Kit 0.3.3**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.6.0](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2026-01-14)

## 2025-12-16

**RealtimeKit Android UI Kit 0.3.2**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.7](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-12-16)

## 2025-12-12

**RealtimeKit Android UI Kit 0.3.1**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.6](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-12-12)

**Fixes**

* Fixed crash when screenshare is disabled for a participant
* Fixed screenshare disappearing when video is disabled for a screensharing participant

## 2025-12-04

**RealtimeKit Android UI Kit 0.3.0**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.5](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-12-04)

## 2025-11-06

**RealtimeKit Android UI Kit 0.2.12**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.4](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-11-06)

**Fixes**

* Fixed an issue with camera video not rendering in the settings UI

## 2025-10-23

**RealtimeKit Android UI Kit 0.2.11**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.3](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-10-23)

**Fixes**

* Fixed a regression that caused self video to not render if meeting was joined with camera disabled

## 2025-10-23

**RealtimeKit Android UI Kit 0.2.10**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.2](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-10-23)

**Fixes**

* Fixed an issue where pinning yourself in the participant view didn't update correctly

## 2025-10-08

**RealtimeKit Android UI Kit 0.2.9**

**Fixes**

* Fixed an issue where the last video frame remained stuck on participant tile

## 2025-10-06

**RealtimeKit Android UI Kit 0.2.8**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.1](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-10-06)

## 2025-09-23

**RealtimeKit Android UI Kit 0.2.7**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.5.0](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-09-23)

## 2025-09-18

**RealtimeKit Android UI Kit 0.2.6**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.4.1](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-09-18)

**Fixes**

* Audio device selector now dynamically updates the options list when devices are removed or added
* Fixed crash when a host turns off video for an active screenshare user

## 2025-09-12

**RealtimeKit Android UI Kit 0.2.5**

**Fixes**

* Fixed pinned peers not being removed from the stage when kicked
* Media consumers are now created in parallel, which significantly improved the speed of when users start seeing other people's audio/video after joining a meeting
* Fixed "Ghost"/Invalid peers that would sometimes show up in long-running meetings
* Fixed an issue in webinar meetings where the SDK would fail to produce media after being removed from the stage once
* Fixed a rare crash during meeting joins in poor network scenarios

## 2025-08-13

**RealtimeKit Android UI Kit 0.2.4**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.3.2](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-08-13)

## 2025-08-13

**RealtimeKit Android UI Kit 0.2.3**

**Enhancements**

* Upgraded to [RealtimeKit Core v1.3.1](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-08-13)

## 2025-08-12

**RealtimeKit Android UI Kit 0.2.2**

**Breaking changes**

* `RtkParticipantTileView#activateForSelfPreview` was removed, you can now call `RtkParticipantTileView#activate` for all participants and we take care of the self preview case internally

**Features**

* Upgraded to [RealtimeKit Core v1.3.0](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-08-12)

## 2025-08-05

**RealtimeKit Android UI Kit 0.2.1**

**Features**

* Upgraded to [RealtimeKit Core v1.2.0](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-08-05)

## 2025-07-02

**RealtimeKit Android UI Kit 0.2.0**

**Features**

* Upgraded to [RealtimeKit Core v1.1.0](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-core/#2025-07-02)

# Source: https://developers.cloudflare.com/realtime/realtimekit/release-notes/react-native-core/index.md

---

title: React Native Core SDK · Cloudflare Realtime docs
description: Subscribe to RSS
lastUpdated: 2026-01-16T11:57:12.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/release-notes/react-native-core/
  md: https://developers.cloudflare.com/realtime/realtimekit/release-notes/react-native-core/index.md
---

[Subscribe to RSS](https://developers.cloudflare.com/realtime/realtimekit/release-notes/react-native-core/index.xml)

## 2025-11-20

**RealtimeKit React Native Core 0.3.1**

**Fixes**

* Fixed bluetooth not showing in list/dropdown after rejoining meeting
* Fixed mobile active speaker not working after rejoining meeting

## 2025-11-02

**RealtimeKit React Native Core 0.3.0**

**Breaking changes**

* Starting from version v0.3.0, SDK now supports only React Native 0.77 and above.

**Fixes**

* Fixed 16KB page support in Android >=15
* Fixed foreground service failed to stop errors in Android
* Fixed bluetooth issues in iOS Devices
* Fixed android build issues due to deprecated jCenter in React Native 0.80 or higher

## 2025-10-06

**RealtimeKit React Native Core 0.2.1**

**Fixes**

* Fixed can't install multiple apps with expo sdk
* Fixed screenshare for Android in Expo with New Architecture enabled
* Fixed remote audio/video not working in group calls

## 2025-09-14

**RealtimeKit React Native Core 0.2.0**

**Breaking changes**

* Adding a `blob_provider_authority` string resource is now mandatory. Refer to the installation instructions for more details.

**Fixes**

* Fixed audio switch to earpiece when leaving stage in Webinar
* Fixed types for useRealtimeKitClient options
* Fixed screenshare for Android in Expo

## 2025-08-05

**RealtimeKit React Native Core 0.1.3**

**Fixes**

* Fixed active speaker not working

## 2025-07-08

**RealtimeKit React Native Core 0.1.2**

**Fixes**

* Fixed screenshare not working for Android 13 and later
* Fixed audio device switching not working
* Minor performance improvements

## 2025-06-05

**RealtimeKit React Native Core 0.1.1**

**Fixes**

* Documentation improvements

## 2025-05-29

**RealtimeKit React Native Core 0.1.0**

**Features**

* Initial release

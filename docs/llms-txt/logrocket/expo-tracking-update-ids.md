# Source: https://docs.logrocket.com/reference/expo-tracking-update-ids.md

# Tracking Update IDs

Instructions for associating Expo Update IDs to LogRocket session replays.

If you are utilizing's Expo's EAS Update service then you can follow these instructions to be able to view and filter by  the specific Expo Update version used in session recordings.

> NOTE: Update ID tracking using the LogRocket mobile SDK requires using a version of 1.42.2 or higher.

# Configure Update ID and Channel

When initializing the LogRocket SDK pass the current Update ID and channel via the appropriate config settings:

```typescript
import * as Updates from 'expo-updates';
import LogRocket from '@logrocket/react-native';
...
LogRocket.init('<APP_SLUG>', {
  // Other config options ...
  updateId: Updates.isEmbeddedLaunch ? null : Updates.updateId,
  expoChannel: Updates.channel
});
```

> ⚠️ Impact to App Version Blocking
>
> If you configure the LogRocket SDK to set `updateId`,  then be aware when blocking specific app versions from recording sessions (under Project Settings -> Block App Versions in your LogRocket project dashboard) that the release value will change with every Expo update due to update IDs being appended to the end of the release.

# View Update ID and channel

If the `updateId` and `expoChannel` config settings are set to a non-empty value in the LogRocket SDK then the Release version associated with recordings will be a concatenation of the native app version, Expo Update ID and channel. For example, if the native app version is `1.0.0` and the Expo Update ID being used is `c4eb13d7-d50e-4d80-b2ac-943d25a4c3b4` and the channel name is `dev` then the Release version will display as `1.0.0#dev:c4eb13d7-d50e-4d80-b2ac-943d25a4c3b4` in session replays.

<Image align="center" width="250px" src="https://files.readme.io/aabfaae7f19a3022d1085895c4894830d16293b63d97df5c2a4779406384f5fa-Screenshot_2024-10-09_at_1.46.27_PM.png" />

# Filter by Update ID

You can find sessions that use a specific Update ID by using the **Release** filter when searching for sessions. Enter the release version as seen in the session replay (ex. `1.0.0#dev:c4eb13d7-d50e-4d80-b2ac-943d25a4c3b4`) to filter down sessions with that specific Update ID:

<Image align="center" src="https://files.readme.io/61c819a84574090938ae25c86bee778625229ff18e82f630763f1c6cf93530af-Screenshot_2024-10-11_at_12.12.46_PM.png" />

## Determine the Release Version from the Expo Dashboard

Within your Expo dashboard on [expo.dev](https://expo.dev/), select the Project that you are working on. Then in the Project navigation menu, expand the Updates section and select the Update Groups page. On the Update Groups page select the update that you are interested in and on the page for that Update Group you will be able to find the Runtime Version and the platform-specific Update ID.

<Image align="center" width="400px" src="https://files.readme.io/847f2bade919bbb3e549a4368cfde9663451a496f895152b36e757842e1bb37b-Screenshot_2024-10-11_at_11.54.04_AM.png" />

Then if you go to the Channels page you can find the Channel that is linked to the branch that your update is on. If you have configured the LogRocket SDK with both the `expoChannel` and `updateId` then the Release version recorded in LogRocket is in the format of `RUNTIME_VERSION#CHANNEL_NAME:UPDATE_ID`.

## Link to a list of all sessions for an Update ID

If you'd like to a link to a list of all sessions for a specific Update ID from within another tool, then determine the corresponding Release Version value using the directions in the previous section and then construct a URL like this and embed it into your other platforms:

`https://app.logrocket.com/YOUR_ORG/YOUR_APP/sessions?r=RELEASE_VERSION`

If you want to link to a list of all sessions for multiple Update IDs (for example if you want a list of sessions for a single Update Group on both iOS and Android) then set the `r` query parameter to a comma-separated list of the specific release versions:

`https://app.logrocket.com/YOUR_ORG/YOUR_APP/sessions?r=RELEASE_VERSION_1,RELEASE_VERSION_2`

> NOTE: Since the Release Version values are being passed as query string parameters in a URL, it is important to URL encode those values before using or embedding the link to ensure the filters are pre-populated correctly.
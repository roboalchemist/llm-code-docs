# Source: https://docs.mage.ai/data-integrations/sources/youtube_analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# YouTube Analytics API Source

> This guide explains how to configure the YouTube Analytics API as a data source in Mage. Learn how to authenticate with Google Cloud, request the necessary OAuth scopes, and sync data from specific channels.


export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="data-integration" />

Mage supports ingesting data from YouTube Analytics by connecting to the YouTube Analytics API and YouTube Data API v3 using OAuth 2.0 credentials.

This integration allows you to extract rich channel analytics, video performance, and viewer engagement metrics directly into your Mage pipelines.

***

## 🔧 Configuration

To connect to the YouTube Analytics API, provide the following parameters in your source configuration:

| Key             | Description                                                   | Sample Value                                  | Required |
| --------------- | ------------------------------------------------------------- | --------------------------------------------- | -------- |
| `client_id`     | OAuth 2.0 Client ID from Google Cloud Console                 | `123456789-abcdef.apps.googleusercontent.com` | ✅        |
| `client_secret` | OAuth 2.0 Client Secret from Google Cloud Console             | `abcdefghijklmnopqrstuvwxyz`                  | ✅        |
| `refresh_token` | OAuth 2.0 refresh token for authenticating requests           | `1//abcdefghijklmnopqrstuvwxyz`               | ✅        |
| `start_date`    | Start date for pulling analytics data                         | `2021-01-01T00:00:00Z`                        | ✅        |
| `user_agent`    | User agent string identifying the integration                 | `example@example.com`                         | ✅        |
| `channel_ids`   | Comma-separated list of channel IDs to retrieve analytics for | `UC1234..., UC5678...`                        | ✅        |

***

## 🔐 How to Generate Credentials

Follow these steps to generate the required credentials from the Google Cloud Console:

### 1. Set Up OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the following APIs:
   * **YouTube Data API v3**
   * **YouTube Analytics API v2**
4. Navigate to “APIs & Services > Credentials”
5. Create a new **OAuth 2.0 Client ID** (select "Web application" or "Desktop app")

### 2. Generate a Refresh Token

Use [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/) to get a `refresh_token`:

* Click the gear icon and check **"Use your own OAuth credentials"**, then enter your Client ID and Secret.
* Select the following scopes:
  * `https://www.googleapis.com/auth/youtube.readonly`
  * `https://www.googleapis.com/auth/yt-analytics.readonly`
* Follow the steps to **authorize**, **exchange code for tokens**, and **copy the refresh token**.

## How It Works

This integration connects to two key Google APIs to extract YouTube Analytics data and video metadata:

### APIs Used

* **[YouTube Reporting API](https://developers.google.com/youtube/reporting/v1/reports)**\
  Used to retrieve bulk analytics reports for YouTube channels and content owners.

  * [Jobs](https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list): List available report jobs
  * [Reports](https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports/list): Retrieve generated reports
  * [Report Types](https://developers.google.com/youtube/reporting/v1/reference/rest/v1/reportTypes/list): View available report categories
  * Report examples:
    * [Channel Reports](https://developers.google.com/youtube/reporting/v1/reports/channel_reports)
    * [Content Owner Reports](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports)

* **[YouTube Data API v3](https://developers.google.com/youtube/v3/docs)**\
  Used to fetch real-time metadata and performance metrics for channels, videos, and playlists.

  * [Channels](https://developers.google.com/youtube/v3/docs/channels/list)
  * [Playlists](https://developers.google.com/youtube/v3/docs/playlists/list)
  * [Playlist Items](https://developers.google.com/youtube/v3/docs/playlistItems/list)
  * [Videos](https://developers.google.com/youtube/v3/docs/videos/list)

## Supported Streams

The following streams are available in the YouTube Analytics integration:

| Stream           | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| `channels`       | Metadata and statistics for authenticated YouTube channels |
| `playlist_items` | Videos and items within playlists                          |
| `playlists`      | Metadata about playlists created by the authenticated user |
| `reports`        | Bulk analytics data from YouTube Reporting API             |
| `videos`         | Video metadata, engagement, and performance statistics     |

## Sync Behavior

* **Incremental Syncs**\
  The integration supports stateful incremental loading, so only new or modified records are fetched during each sync run.

* **Schema Output**\
  Mage automatically generates the output schema for each stream, making it easier to understand and work with the resulting data.


Built with [Mintlify](https://mintlify.com).
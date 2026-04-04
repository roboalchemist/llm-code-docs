# Source: https://docs.mage.ai/data-integrations/sources/instagram.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Instagram

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

<img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" width="300" />

## Configuration

Connect to **Instagram Graph API** to sync media, stories, and insights for business accounts. Provide the following configuration parameters:

| Key                            | Description                                                             | Sample Value                   | Required |
| ------------------------------ | ----------------------------------------------------------------------- | ------------------------------ | -------- |
| `access_token`                 | OAuth access token with Instagram Graph API permissions.                | `EAAGm0PX4ZCpsBA...`           | ✅        |
| `ig_user_ids`                  | List of Instagram Business Account IDs to fetch data for.               | `["1234567890", "9876543210"]` | ✅        |
| `media_insights_lookback_days` | Number of days to look back for media insights.                         | `60`                           | Optional |
| `start_date`                   | Start date (ISO 8601 format) to begin fetching media and insights data. | `2025-01-01T00:00:00Z`         | ✅        |
| `metrics_log_level`            | Log level for API metrics (e.g., `INFO`, `DEBUG`, `WARNING`).           | `INFO`                         | Optional |

<br />

## How to Get Your `access_token`

You have two options to generate an access token:

### 1. Use the OAuth Button (Recommended)

* Click the **OAuth login** button in your Mage workspace.
* Approve the required permissions for Instagram:
  * `instagram_basic`
  * `instagram_manage_insights`
  * `pages_show_list`
* The access token will be securely generated and automatically populated in the configuration.

> **Tip**: Use the OAuth flow for a smoother and safer authentication process without manually handling tokens.

### 2. Manually Generate Access Token

* Create a Facebook App via [Facebook Developer Portal](https://developers.facebook.com/).
* Add Instagram Basic Display API and Instagram Graph API products to your app.
* Generate a **User Access Token** via [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
* Make sure to select the correct Instagram-related permissions.
* Convert the short-lived token to a **long-lived token** for production use.

<br />

## What is Instagram Graph API?

The [Instagram Graph API](https://developers.facebook.com/docs/instagram-api) is designed for businesses and creators to access media, insights, and metrics on Instagram accounts. It enables data-driven marketing and content analysis.

<br />

## Why Integrate Instagram with Mage?

* **Automate content extraction**: Sync media posts and stories.
* **Measure engagement**: Track likes, comments, saves, impressions, and reach.
* **Audience insights**: Understand follower growth and demographics.
* **Marketing analytics**: Integrate with other platforms for a 360-degree marketing view.

<br />

## Supported Streams

The Instagram source extracts the following resources:

* **media**: All published media objects (images, videos, carousels).
* **media\_children**: Children of carousel media posts.
* **media\_insights**: Metrics like reach, impressions, engagement for each media post.
* **stories**: Instagram Stories posted by the account.
* **story\_insights**: Insights for each Story, including taps forward, exits, impressions.
* **user\_insights\_28day**: Aggregated user insights over a 28-day window.
* **user\_insights\_daily**: Daily user insights.
* **user\_insights\_followers**: Follower count and demographic data.
* **user\_insights\_online\_followers**: Times of day when followers are online.
* **user\_insights\_weekly**: Weekly user insights.
* **users**: Profile data of the Instagram Business accounts.

<br />


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.mage.ai/data-integrations/sources/facebook_pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Facebook Pages

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

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Facebook_Logo_%282019%29.svg/2560px-Facebook_Logo_%282019%29.svg.png" alt="Facebook Pages" width="300" />

## Configuration

Connect to **Facebook Pages** and sync posts, insights, and engagement metrics. Provide the following configuration parameters:

| Key            | Description                                                                                                                   | Sample Value                   | Required |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | -------- |
| `access_token` | OAuth access token for Facebook Graph API with the required permissions (`pages_read_engagement`, `pages_read_user_content`). | `EAABsbCS1i...`                | ✅        |
| `page_ids`     | List of Facebook Page IDs you want to extract data from.                                                                      | `["1234567890", "9876543210"]` | ✅        |
| `start_date`   | Start date (ISO 8601 format) to begin fetching posts and engagement data.                                                     | `2025-01-01T00:00:00Z`         | ✅        |

<br />

## How to Get Your `access_token`

You have two options to generate an access token:

### 1. Use the OAuth Button (Recommended)

* Click the **OAuth Authorize** button in your Mage workspace.
* Approve the required Facebook permissions:
  * `pages_show_list`
  * `pages_read_engagement`
  * `pages_read_user_content`
  * `read_insights`
* The access token will be securely generated and auto-filled in the configuration.

> **Tip**: Use the OAuth flow for a smoother, safer authentication process without manually handling tokens.

### 2. Manually Generate Access Token

* Create a Facebook App via [Facebook Developer Portal](https://developers.facebook.com/).
* Configure the app and get the permissions listed above.
* Generate a **User Access Token** or **Page Access Token** via [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
* (Optional) Exchange for a **long-lived token** for production environments.

<br />

## What is Facebook Pages API?

The [Facebook Pages API](https://developers.facebook.com/docs/pages) allows programmatic access to posts, insights, page metadata, and engagement data for Facebook Pages. Businesses use it to monitor social presence, measure engagement, and automate reporting workflows.

<br />

## Why Integrate Facebook Pages with Mage?

* **Automate data extraction**: Fetch page posts, reactions, and comments for analysis.
* **Engagement tracking**: Monitor likes, shares, comments, and post performance.
* **Insights at scale**: Integrate page metrics into BI dashboards for better reporting.
* **Marketing analytics**: Correlate Facebook engagement with other marketing activities.

<br />

## Supported Streams

The Facebook Pages source extracts the following resources:

* **page**: Basic page details like name, ID, and metadata.
* **page\_insights**: Aggregated metrics like page impressions, engagement, and follower growth.
* **post\_attachments**: Media and links attached to posts.
* **post\_insights**: Detailed insights for each post, including reach and engagement breakdown.
* **post\_tagged\_profile**: Profiles tagged in the posts.
* **posts**: Content posted on the page — text, images, videos, and links.

<br />


Built with [Mintlify](https://mintlify.com).
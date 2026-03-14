# Source: https://docs.mage.ai/data-integrations/sources/quickbooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# QuickBooks

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

## Configuration

To set up the QuickBooks source, provide the following configuration parameters:

| Key             | Description                                                                                      | Sample Value           | Required |
| --------------- | ------------------------------------------------------------------------------------------------ | ---------------------- | -------- |
| `client_id`     | Client ID associated with your QuickBooks app.                                                   | `123456`               | ✅        |
| `client_secret` | Client secret generated when you create your QuickBooks app.                                     | `abcdefg`              | ✅        |
| `start_date`    | The start date for syncing data. Format: `YYYY-MM-DDTHH:MM:SSZ`.                                 | `2021-01-01T00:00:00Z` | ✅        |
| `user_agent`    | User agent name registered for your QuickBooks app.                                              | `agent_name`           | ✅        |
| `realm_id`      | Realm ID associated with your QuickBooks company account.                                        | `123456`               | ✅        |
| `refresh_token` | Refresh token used to renew the access token after expiration (requires `offline_access` scope). | `abcdefg`              | ✅        |

<br />

## How to Generate Credentials

Follow QuickBooks' [OAuth 2.0 Authentication Playground guide](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0-playground) to generate the required credentials:

1. Register a new QuickBooks app to get your `client_id` and `client_secret`.
2. Configure the OAuth scopes required by your app.
3. Use the OAuth 2.0 playground to complete authentication and retrieve your `refresh_token` and `realm_id`.

<br />

## Additional Notes

* The `start_date` determines how far back data will be synced.
* Ensure that the `offline_access` scope is enabled to obtain a `refresh_token`.
* Tokens expire after a set period; use the `refresh_token` to obtain new access credentials automatically.


Built with [Mintlify](https://mintlify.com).
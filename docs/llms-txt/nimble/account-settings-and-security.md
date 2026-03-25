# Source: https://docs.nimbleway.io/general/faqs/account-settings-and-security.md

# Account Settings and Security

<details>

<summary>How can I open a Nimble account?</summary>

To open an account, please send us an email at <sales@nimbleway.com>

</details>

<details>

<summary>Is there an unlimited bandwidth plan?</summary>

While we don’t currently offer an unlimited plan, all of our plans have an auto-recharge option that triggers a new billing cycle if your quota runs out, and ensures your account will run continuously without billing-related limitations.

Optional: If your use case entails special data requirements, contact your account manager / sales at <sales@nimbleway.com>

</details>

<details>

<summary>Does Nimble have a user dashboard?</summary>

Yes! We have a full [User Dashboard](https://app.nimbleway.com/login) where users can access usage reports and statistics, perform account functions, manage their pipelines, and more!

All of the same functionality and reports are available programmatically through our [Admin API.](https://docs.nimbleway.com/management-tools/nimble-admin-api)

</details>

<details>

<summary>Can I check my bandwidth usage in real-time?</summary>

Nimble measures bandwidth usage in two ways:

1. Total bandwidth per pipeline
2. Daily bandwidth

You can view your total bandwidth usage, usage per pipeline, and view daily reports via the [User Dashboard](https://app.nimbleway.com/login), or using the [Admin API](https://docs.nimbleway.com/management-tools/nimble-admin-api).

To see your total bandwidth usage per pipeline, send a GET request to the Admin API at this endpoint:

`https://api.nimbleway.com/api/v1/account/pipeline`

You will receive a list of pipelines, each of which has a property titled “spent\_gb” which represents that pipeline’s total bandwidth usage.

To get a daily usage report, send a GET request to:

`https://api.nimbleway.com/api/v1/account/reports/daily-usage?fromDate=`**`<startDate>`**`&toDate=`**`<EndDate>`**

You can also see this report on a pipeline level using: `https://api.nimbleway.com/api/v1/account/pipeline/`**`<pipelineName>`**`/reports/daily-usage?fromDate=`**`<startDate>`**`&toDate=`**`<EndDate>`**

</details>

<details>

<summary>What timezone do Nimble’s reports use?</summary>

All of our reports are set to UTC.

</details>

<details>

<summary>How do I manage my Nimble account?</summary>

Both our [User Dashboard](https://app.nimbleway.com/login) and [Admin API](https://docs.nimbleway.com/management-tools/nimble-admin-api) allow users to view account information, create and manage pipelines, access usage statistics, and more!&#x20;

</details>

<details>

<summary>How can I see my remaining credits?</summary>

To view your account’s remaining credits, send a GET request to `https://api.nimbleway.com/api/v1/account/remaining-credits`

In the resulting list, your remaining credits will be available under “remaining\_budget\_usd”.

</details>

<details>

<summary>How do I change my Admin API password?</summary>

You can generate a new Admin API password by sending a PUT request to: `https://api.nimbleway.com/api/v1/account/users/support%40nimbleway.com/password`

For example:

*curl -X PUT “<https://api.nimbleway.com/api/v1/account/users/**\\><UserName>\*\*/password” -H “accept: application/json” -H “Authorization: bearer **\<token>”***

</details>

<details>

<summary>How do pipelines work?</summary>

Pipelines are Nimble’s solution for a more streamlined approach to managing business use cases. With pipelines, you can configure default session settings such as target country and IP rotation once, and all requests made through a particular pipeline automatically inherit those parameters. You can always override the default settings by adding the settings parameters to your request.

**Pipeline Advantages**:

1. Set your country and IP rotation once.
2. Monitor performance and statistics per pipeline.
3. Optimized IP selection according to the pipeline’s session profile and targeted sites.
4. Set budget caps per pipeline.
5. Coming soon: permission control per pipeline.

</details>

<details>

<summary>How do I add a new pipeline?</summary>

New pipelines can be created through the [User Dashboard](https://app.nimbleway.com/login), or by using the /account/pipelines endpoint of our Admin API. When creating a new pipeline, you can set the name, proxy type, and geotargeting settings of the pipeline (these can always be changed later!).&#x20;

For a full walkthrough, see our [Admin API Documentation](https://docs.nimbleway.com/management-tools/nimble-admin-api).

</details>

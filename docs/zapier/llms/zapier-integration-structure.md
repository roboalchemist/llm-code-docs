# Source: https://docs.zapier.com/platform/quickstart/zapier-integration-structure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zapier integration structure

> [Zapier's Developer Platform](https://developer.zapier.com/) includes everything needed to build and manage a new Zapier integration. When you access your integration project by name, you'll see the left sidebar outlines the core project structure.

### Dashboard

*Dashboard* tab is used to see your Partnership level, active user total count, overall embed status and [integration health score](/platform/publish/partner-program#integration-health-score). You **must** be an [admin or collaborator](/platform/manage/add-team) to view an integration's dashboard.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=5626c8e6b6776e53a0f7c1ce973ced46" data-og-width="1811" width="1811" data-og-height="1033" height="1033" data-path="images/3b26f7098360a25ec055ab9be6713e9d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=93c9793f217d5439dda6d89f531128a7 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a849b13b6388a7ad13674fa76eadb189 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=75f498f9c3235395da34de9ce7e57bdf 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3dea9faca122f1166e0e78739096576c 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ba928a1f805296a5ce55063d7ea85b0c 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3b26f7098360a25ec055ab9be6713e9d.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=bcd7122edb2eec9bfe81431f71f93136 2500w" />
</Frame>

### Insights

*Insights* tab is used to monitor and analyze your integration's growth, usage, and detailed embed metrics. You **must** be an [admin or collaborator](/platform/manage/add-team) to view an integration's insights.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=07d95a36ae2c851fbd46de99cf665b3e" data-og-width="1814" width="1814" data-og-height="1020" height="1020" data-path="images/81930868f966d933d1edb90cc61623bc.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=0bc9801dd66df92f4818d24d9798359f 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=06b2b5d8e6dd8af34e72c85124046d30 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3009b62b505a4385b56606299320be48 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=c7f5334026b19fd5f9680da47f585eb8 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=bca2aa794d191a0fea8693d8a0d09b06 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81930868f966d933d1edb90cc61623bc.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f3e2341e785d59207aa5651082731331 2500w" />
</Frame>

### Build

*Build* tab defines your integration:

* *Version Overview* shows the outline of the version selected in the [dropdown](https://cdn.zappy.app/ca49500dc40cd1986693223661ab22b2.png)
* *Authentication* sets how users authenticate with your API; using basic, API key, digest, session, or OAuth v2 authentication.
* *Triggers* control how Zapier gets data from your API into a Zap, with `GET` HTTP calls or REST Hooks.
* *Actions* control how Zapier sends data to your API, including:
  * *Create Actions* to send new data from a Zap to your API, with `POST` or `PUT` HTTP calls to create or update items.
  * *Search Actions* to perform lookups through your API using `GET` calls.
* *Advanced* manages environment variables to store secret values your integration needs to communicate with your API, such as API keys or client IDs and secrets, or manage switching between staging and production environments in a version.

When planning your integration build, think through your integration and what features from your app your users might find the most valuable. Review [integration design examples](/platform/quickstart/must-have-triggers-and-actions) by app category for inspiration.

Walk through building an integration with the [UI tutorial](/platform/quickstart/ui-tutorial) or the [CLI tutorial](/platform/quickstart/cli-tutorial).

### Manage

*Manage* tab is where you access tools to maintain your integration:

* *Versions* gives an [overview of each version's status](/platform/manage/versions), user activity and for published apps; the changelog included in a promotion
* *Sharing* is where you [give users access](/platform/manage/sharing) to private versions via an invite link to all versions or an email invite to a specific version
* *Manage Team* is used to [add team members](/platform/manage/add-team) to manage your integration
* *Monitoring* gives access to [logs for requests](/platform/build/test-monitoring#steps) made to your API by your Zapier integration
* *History* shows the 50 most recent audit logs for changes to your integration
* *Bugs & Feature Requests* are reported by users for published apps and should be used to communicate on these issues with Zapier Developer Support

### Embed

*Embed* tab shows for [public integrations](/platform/quickstart/private-vs-public-integrations) only and describes a [variety of ways](https://platform.zapier.com/embed/full-zapier-experience) to surface your Zapier integration directly within your own product. It allows your users to search for apps that connect with yours, see popular workflows used with your app, and (most importantly) enables them to sign up for Zapier, build Zaps and edit them, too — without leaving your product.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

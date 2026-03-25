# Source: https://help.aikido.dev/zen-firewall/zen-features/understanding-your-zen-statistics.md

# Understanding Your Zen Statistics

Zen gather statistics to offer a clear, at-a-glance view of your application's traffic and Zen's protective actions.

### Stats tab <a href="#stats-tab" id="stats-tab"></a>

At the top of the page, you'll find two key graphs. The **Requests** graph shows the "Amount requests seen" by your application over time, helping you understand typical traffic patterns and spot unusual spikes. Below it, the **Attacks** graph displays the number of "Attacks blocked" and "Attacks detected" by Zen, visually confirming active protection and showing when attacks occur.

![App statistics dashboard showing request volume and detected attacks over time.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fi33swEgmbUinGDOyDNY6%2FScreenshot%202025-10-30%20at%2012.09.14.png?alt=media\&token=ad413876-e750-457e-9187-4b8cf6b7532d)

### Invocation Details: Understanding Attack Paths (Sinks) <a href="#invocation-details-understanding-attack-paths-sinks" id="invocation-details-understanding-attack-paths-sinks"></a>

The **Invocation Details** section, also known as "Sinks," provides a detailed breakdown of the different attack vectors Zen monitors within your application. Use this to identify frequently targeted or potentially vulnerable parts of your application. These differ per language.

![Invocation statistics for HTTP, SQL, shell, and I/O operations over the past week.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-04932512f9391d7a2efb5d5e07890fb07032d75d%2Funderstanding-your-zen-statistics_b219f4b1-5b25-435d-95fd-43be3d6cc8fd.png?alt=media)

### Route-Specific Statistics <a href="#route-specific-statistics" id="route-specific-statistics"></a>

For granular insights, the **Routes** table details traffic and protection for each of your application's paths.

![API routes dashboard showing request rates, rate limits, and detection status for each endpoint.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4bded267a9a0a48c7093918a22f785168152d681%2Funderstanding-your-zen-statistics_913f50b7-85c2-4457-8087-8f37c36cd060.png?alt=media)

### Outbound-Specific Statistics <a href="#outbound-specific-statistics" id="outbound-specific-statistics"></a>

Finally, the **Outbound** section summarises all outbound calls & services Zen is currently monitoring. This view helps you quickly verify that all intended services are monitored and check their recent activity.

![Outbound network activity summary for My App, showing requests by hostname and last seen times.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cd99ed3cb046b562a5747cd2feadc1ee3915b7c0%2Funderstanding-your-zen-statistics_33bc48f6-a234-4475-b25b-6b9cc1255437.png?alt=media)

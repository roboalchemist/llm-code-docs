# Source: https://help.aikido.dev/zen-firewall/disable-attack-protection-for-specific-path-or-url.md

# Disable Attack Protection for Specific Path or URL

Disable Attack Protection lets you mark a route as safe if Zen is incorrectly blocking legitimate traffic. This is the recommended way to handle false positives. Once disabled, Zen stops blocking requests on that route (or group of routes)

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FFH6RR2jJdryDGf2to3iO%2FScreenshot%202025-09-02%20at%2017.46.05.png?alt=media&#x26;token=4f6b5cd5-30a8-499f-a3e9-5fff1522de5c" alt=""><figcaption></figcaption></figure>

## Use Cases

* Database tools, for example PHPMyAdmin: Routes where raw SQL queries are expected. Zen would normally block these, but here they’re legitimate.
* Search APIs with custom query syntax: For example, an API that accepts filter expressions (field:value) that look like injection attempts.
* Developer / debug endpoints: Internal tools that accept large or unusual payloads.
* Custom applications: Endpoints intentionally designed to accept input patterns that resemble attacks.

{% hint style="warning" %}
Only disable protection if you are sure the behavior is expected and safe. For real attacks, Zen should stay enabled.
{% endhint %}

## How to Disable Protection

### Disable for a Single Route

1. Open the Routes view in your Zen dashboard.
2. Locate the route that triggered the false positive.
3. Click the action menu (⋮).
4. Select **Disable Protection** for this route.
5. Confirm your choice.

Zen will now no longer block attacks on this specific route.

### Disable for Multiple Routes (Wildcard)

1. Open the Routes view in your Zen dashboard.
2. Add a new route with wildcard `*` <br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FMvszdz630IqcS1fVqAjk%2FScreenshot%202025-09-02%20at%2017.50.37.png?alt=media&#x26;token=114ee8ca-6a11-43ef-a874-28591d2272a0" alt=""><figcaption></figcaption></figure>
3. Click the action menu (⋮)
4. Select Disable protection for route wildcard.
5. Confirm your choice.

All routes that match the wildcard will bypass attack blocking.

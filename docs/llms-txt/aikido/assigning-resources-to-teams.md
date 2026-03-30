# Source: https://help.aikido.dev/getting-started/manage-teams-and-applications/assigning-resources-to-teams.md

# Assigning Resources to Teams

Assigning resources to teams defines ownership inside Aikido. It ensures that findings are routed to the right people, dashboards stay relevant, and teams only see what they are responsible for.

This page explains all available ways to assign resources, including individual and bulk options.

### Assign from the Team Page

1. Go to [Settings → Teams](https://app.aikido.dev/settings/teams)
2. Select a team
3. Open the Responsibility tab

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZu4AiAtPf48AR1Rwf1LA%2FScreenshot%202026-02-23%20at%2011.45.39.png?alt=media&#x26;token=255dde11-a62d-4e75-9028-2ece67f08e5a" alt=""><figcaption></figcaption></figure>
4. Click "Link Resource"
5. Select resource type, and search and add resources<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6lBS6KejQUT885j598Jm%2FScreenshot%202026-03-10%20at%2011.38.31.png?alt=media&#x26;token=4fd2e7c3-c13d-4475-ba7f-49493d856939" alt="" width="563"><figcaption></figcaption></figure>

### Assign from the Resource Page

You can also assign a team while viewing the resource itself.

#### Repositories

Open a Repository → Configure → Teams responsible

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FIBphGT7Vm07ANtO9GsAJ%2FLanguageTool_Overlay.png?alt=media&#x26;token=65470eba-cd61-4fdc-aa0d-a4900aa73f97" alt=""><figcaption></figcaption></figure>

#### Cloud Accounts

Open a Cloud Connection → Configure → Teams responsible

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F5bW7TDTZNYNeWS31ZkKS%2FLanguageTool_Overlay.png?alt=media&#x26;token=7251d5fd-e33a-496e-a809-5c06b5854607" alt=""><figcaption></figcaption></figure>

### Domains & API's

Open the Front-end, REST, or GraphQL scan configuration from the Settings page (or the action menu in the list view) and link the domain to an asset.

You can link it to either a repository or a container. Once linked, the scan inherits the team permissions from that asset.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FLUDN9XokEfkVrdqOJOIe%2FScreenshot%202026-02-25%20at%2019.05.11.png?alt=media&#x26;token=5a95e5c3-45f3-4a0f-90c2-a9300bda6bc3" alt=""><figcaption></figcaption></figure>

### Bulk Assignment

Bulk actions are available on resource list pages in [settings](https://app.aikido.dev/settings/account).

{% hint style="info" %}
If bulk actions are not visible, assignment must be done individually.
{% endhint %}

**Repositories**

[Settings → Repositories](https://app.aikido.dev/settings/integrations/repositories) → Select multiple → Bulk Actions → Assign to team

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FI5Rav0nqk14UtdB1Qz5K%2FLanguageTool_Overlay.png?alt=media&#x26;token=db3bd019-72cd-432f-846a-408c0be4d8b5" alt=""><figcaption></figcaption></figure>

**Containers**

[Settings → Containers](https://app.aikido.dev/settings/container-image-registry) → Select multiple → Bulk Actions → Assign to team

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1jltOtRF87i8totb0kgy%2FScreenshot_23_02_2026__11_57.png?alt=media&#x26;token=6cebb8f3-ab14-43cc-b39c-0eabd7bc1ed7" alt=""><figcaption></figcaption></figure>

# Source: https://developers.make.com/custom-apps-documentation/component-blocks/scopes.md

# Scope List

## Specification

The scopes object contains all available scopes used within Make with their human-readable description.

{% tabs %}
{% tab title="Code" %}

```json
{
	"identify": "Allow application to confirm your identity.",
	"groups:read": "Access information about user's private channels.",
	"channels:read": "Access information about user's public channels.",
	"users:read": "Access the team member's profile information.",
	"im:read": "Access information about user's direct messages.",
	"files:write:user": "Upload and modify files as user.",
	"chat:write:bot": "Send messages as user.",
	"channels:history": "Access user's public channels.",
	"im:history": "Access user's direct messages.",
	"groups:history": "Access user's private channels.",
	"team:read": "Access basic information about the team."
}
```

{% endtab %}
{% endtabs %}

## View granted scopes in a connection

You can view the scopes granted in a connection:

{% stepper %}
{% step %}
Click **Connections** in the left menu.
{% endstep %}

{% step %}
Find the connection you want to review. If you have many connections, you can use the Search feature in the upper-right corner to find the connection.
{% endstep %}

{% step %}
Every row with a connection has a lock icon with a number. If there are scopes available in the connection, the number is larger than 0.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e389d53a896f71829cf53c1510f2318cfa966b20%2Fconnection_listscopes.png?alt=media" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click on the lock icon to view the list of granted scopes in the connection.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-77f68a52b0d48ca973e38354fc60c0c2b1599f7d%2Fscopes_details.png?alt=media" alt="" width="430"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

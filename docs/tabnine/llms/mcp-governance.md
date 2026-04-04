# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/mcp-governance.md

# MCP Governance

### Admin-Enforced MCP Server Whitelisting

As of [5.26.3](https://docs.tabnine.com/main/release-notes#v5.26.3), admins have the ability to limit what kind of MCP servers are permitted in the organization.

Beneath the <mark style="color:red;">**//**</mark>**&#x20;MCP Governance&#x20;**<mark style="color:red;">**//**</mark> title of the page, Admins will be able to see a menu of control options will appear that include:

* **Allow all** – No restrictions
* **Allow only remote** – Only StreamableHTTP/SSE transports will be permitted
* **Allow-list only** – Only MCP servers in the allow list can be used
* **Block all** – Admins can disallow any MCP servers

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fb8SP7IVQmRXOTtSE0VT4%2Fnew%20screenshot.png?alt=media&#x26;token=f336d9ce-2ce9-4628-86fd-88e6c0c53ba5" alt=""><figcaption></figcaption></figure>

### Adding an MCP Server

Under MCP Governance, you have the option to catalog MCP servers for use in an **Allow List** ([5.26.3](https://docs.tabnine.com/main/release-notes#v5.26.3)).&#x20;

Simply go to the blue <mark style="background-color:blue;">**+ Add MCP**</mark> button in the upper righthand corner of the screen and select.

A window will appear where you must input the server’s information.

If it is a remote MCP server, it must include the following:

* Server location (local or remote)
* The MCP server name\*\*
* The MCP server URL

{% hint style="info" %}
\*\*If the user specifies this server name in the `mcp_servers.json` file, then the associated configuration must be remote and have this URL.
{% endhint %}

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fp8FrCxlw7vrVIK6w1PyK%2Funknown.png?alt=media&#x26;token=ee839051-484f-41d1-a572-54fce37755b8" alt=""><figcaption></figcaption></figure>

If from a local (i.e. STDIO) server, it must **also** include:

* Command Regex
* `args`
  * ‘Exact match’ toggle (Default is "no")\*\*\*

{% hint style="info" %}
\*\*\*

* "No" args in `mcp_servers.json` *must* contain those that occur in the **Allow List**.&#x20;
* "Yes" means that those `args` must be used in the `mcp_servers.json` file.
  {% endhint %}

Once you do that, hit <mark style="background-color:blue;">**Save**</mark>.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FLawk1DxALT7p44dIgXDy%2Funknown.png?alt=media&#x26;token=61bc17a9-3fa3-4618-af9d-ef4542df9409" alt=""><figcaption></figcaption></figure>

<br>

# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens.md

# Personal Access Tokens

Tabnine supports Personal Access Tokens (PATs) for non-interactive authentication for APIs, scripts and integrations that call Tabnine services.

### **Generating a PAT**

In the Admin Console, go to **Settings** on the lefthand-side menu and select **Access Tokens**. Then click **Generate Token**.

{% hint style="info" %}
Personal Access Token generation is not admin-only. Any user with a Tabnine account can create PATs by navigating to `[TABNINE_URL]/app/settings/access-tokens`.
{% endhint %}

Next, type in the name or purpose of the token, then select an expiration date option from the dropdown menu.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FazDol1ZyFrf2zeo8g4aW%2FCreate%20PAT.gif?alt=media&#x26;token=6a0049e8-935a-45e6-a0d1-3db053843c7c" alt=""><figcaption></figcaption></figure>

***Copy the token value*** and store it securely. Tabnine will not display it again. Then press **Close**.

## **Using a PAT in API calls**

Include the PAT as a bearer token in the Authorization header of your HTTP requests.

#### Example: cURL

```bash
#cURL example

curl -X GET "https://<tabnine-server>/api/v1/health" \
  -H "Authorization: Bearer <TABNINE_PAT>" \
  -H "Content-Type: application/json"
```

#### Example: Node.js

```javascript
import fetch from "node-fetch";
const TABNINE_PAT = process.env.TABNINE_PAT;
const res = await fetch("https://<tabnine-server>/api/v1/health", {
  headers: {
    Authorization: `Bearer ${TABNINE_PAT}`,
    "Content-Type": "application/json",
  },
});

```

#### Example: Tabnine CLI (headless / non-interactive mode)

Set your PAT as `TABNINE_TOKEN`, then run prompts with `-p`:

{% tabs %}
{% tab title="macOS / Linux" %}

```bash
export TABNINE_TOKEN="<TABNINE_PAT>"

# Simple text output
tabnine -p "Summarize the repo and list key entry points"

# JSON output (for automation)
tabnine -p "Extract a dependency list from package.json" --output-format json
```

{% endtab %}

{% tab title="Windows (PowerShell)" %}

```powershell
$env:TABNINE_TOKEN = "<TABNINE_PAT>"

tabnine -p "Summarize the repo and list key entry points"
tabnine -p "Extract a dependency list from package.json" --output-format json
```

{% endtab %}
{% endtabs %}

For more automation patterns, see [Non-Interactive Mode](https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started/quickstart#non-interactive-mode).

Use the same pattern for any internal Tabnine API endpoint (admin automation, reporting, or integration scripts).

### Access Token List

A list of all active tokens will display on the Access Tokens page, noting:

* Status
* Creation Date
* Expiration Date
* The last time it was used (including noting if it is still “Never Used”)

### Revoking Tokens

In the final column on the same list, you have the option to revoke the token’s access by pressing <mark style="color:$primary;background-color:$info;">**`Revoke`**</mark>. This will also eliminate it from the list of tokens.

<br>

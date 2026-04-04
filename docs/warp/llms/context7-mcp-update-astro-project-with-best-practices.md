# Source: https://docs.warp.dev/university/mcp-servers/context7-mcp-update-astro-project-with-best-practices.md

# Context7 MCP: Update Astro Project with Best Practices

{% hint style="info" %}
This tutorial shows how the **Context7 MCP Server** gives Warp agents real‑time access to documentation for upgrading frameworks and codebases automatically.
{% endhint %}

{% embed url="<https://youtu.be/rrxfS9u1XRA?si=X2CBWW1PD3M8IuFr&t=369>" %}

***

## 🧠 Overview

The **Context7 MCP Server** lets Warp fetch live documentation from across the web.\
\
In the example, the agent updates an older **Astro** project to align with the latest version (Astro 5).

***

{% stepper %}
{% step %}
**Add the Context7 Server**

* Open Warp’s **MCP Panel** via the Command Palette.
* Add the **Context7 JSON config** and click **Save**.

```json
{
  "Context7": {
    "command": "npx",
    "args": [
      "-y",
      "@upstash/context7-mcp"
    ],
    "env": {},
    "working_directory": null
  }
}
```

* This enables the endpoint `getLibraryDocs`, which retrieves live documentation directly from the official sources.
  {% endstep %}

{% step %}
**Run the Update Prompt**

The developer issues this prompt:

{% code title="prompt.txt" overflow="wrap" fullWidth="true" %}

```
Create a new git branch called update and in that branch update this Astro project to follow all the latest best practices based on all Astro and developer documentation.
```

{% endcode %}
{% endstep %}

{% step %}
**Review the Automatic Code Changes**

The transcript shows that Warp automatically:

* Updates Tailwind import syntax
* Improves TypeScript configuration
* Optimizes build settings
* Enhances accessibility rules

These edits happen across multiple files — without manually searching docs or changelogs.
{% endstep %}

{% step %}
**Best Use Cases**

* Migrating old Astro, React, or Vue projects
* Refreshing codebases to reflect recent standards
* Saving time otherwise spent reading version notes
  {% endstep %}
  {% endstepper %}

{% hint style="success" %}
Context7 MCP automates documentation lookups — letting Warp update your project intelligently based on live references.
{% endhint %}

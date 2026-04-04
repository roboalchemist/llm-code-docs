# Source: https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/urls-as-context.md

# URLs as Context

## Referencing websites via URLs

You can attach a public URL to any prompt to provide page content as context. Warp will scrape the page and surface the extracted text directly to the model.

* Only publicly accessible pages are supported.
* The full page is added to the model’s context, which may increase credit usage for long documents.
* Only the specific URL you provide is processed. The agent won’t explore the site, follow links, or crawl beyond that page.

{% hint style="info" %}
**Important**: URL attachments are different from web search. If you need the agent to look something up, gather real-time information, or pull in multiple sources, use [Web Search](https://docs.warp.dev/agent-platform/agent/using-agents/web-search) instead.
{% endhint %}

<figure><img src="https://769506432-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAULCelT4yIUOcSwWWvPk%2Fuploads%2Fgit-blob-176c44d1b3c99c2e2f5dbc7b87ff754a9fa38c26%2Furl-as-context.png?alt=media" alt=""><figcaption><p>Example of referencing docs via a URL</p></figcaption></figure>

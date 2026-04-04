# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/workspace-settings.md

# Personalization

## Enabling local workspace awareness (context through local code awareness) in Tabnine Enterprise

[Context through local code awareness](https://docs.tabnine.com/main/welcome/readme/personalization) using RAG **for code completions** is enabled for all users, and cannot be turned off.

However, context through local code awareness using RAG **for Tabnine Chat** for all users is controlled by the team admin:

1. Sign in to the Tabnine Console as an admin.
2. Go to the **Personalization** page (formerly "**Workspace**"), under **Settings.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-17f2e549c1a9b11adec60d319ed884c23189729e%2FSH%20settings%20workspace.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Turn on (or off) the **Enable Tabnine Context** toggle button to enable (or disable) this feature for all the users in the organization.

{% hint style="info" %}
**Note**: It can take up to one hour to populate the end users' IDEs.
{% endhint %}

### Local Indexing

Tabnine supports any SCM for local indexing. If you have cloned your git, Tabnine will automatically create a .git root folder and parse it to create a .tabnine\_root file and .gitignore from a clone of your git.

Restart your IDE to affect this change.

*Learn more about* [*Context Scoping*](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping)*.*

####

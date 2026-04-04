# Source: https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/autofix-suggestions-and-inline-commenting-for-pr-checks.md

# AutoFix Suggestions and Inline Commenting for PR Checks

Aikido supports inline comments directly in your SCM software. This feature allows developers to receive feedback on specific lines of code, helping them resolve issues faster. Configuration is available per repository, so teams can enable it only where needed.

Moreover we can also make AutoFix suggestions to fix issues instantly when they arise, we continuously enable more and more rules to have autofixes available.

### Prerequisities <a href="#prerequisities" id="prerequisities"></a>

* Make sure to have your CI Checks enabled (via the Aikido Dashboard)
* You are an admin within Aikido

## Enabling Inline Commenting <a href="#enabling-inline-commenting" id="enabling-inline-commenting"></a>

**Step 1:** Go to the settings page via **Repositories > Pull/Merge Requests > Manage PR/MR Checks**

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FofWwMYxuKZ3EpHVvwBGd%2FScreenshot%202026-01-14%20at%2017.37.08.png?alt=media&#x26;token=f8257b50-ccd9-43d8-9c83-20620db83982" alt=""><figcaption></figcaption></figure></div>

**Step 2:** **Select the repo(s)** for which you want to enable it and click **Setup PR Scans**

**Step 3:** **Enable the toggle for&#x20;**<mark style="color:purple;">**Add comments**</mark>. Make sure at least SAST or Secrets scan is enabled.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FGqhErGzH2fVXKbWtpiP2%2FScreenshot%202026-03-04%20at%2011.50.00.png?alt=media&#x26;token=e100dcf5-6e8d-42bf-af17-5f2de6ecffb3" alt=""><figcaption></figcaption></figure></div>

**Step 4:** When a new issue is introduced (based on the scan failure severity), a new comment will be added in your SCM.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-90f716535082dcceb5e48577dc7b6c4c1f3d80ba%2Fautofix-suggestions-and-inline-commenting-for-pr-checks_c879fc1f-6a0b-4142-ade4-9c6e0bc8f952.png?alt=media" alt="Security bot flags script from malicious domain, recommends its immediate removal from code." width="563"></div>

**Step 5.** When available, Aikido will make AutoFix suggestions. Review the diff and commit the suggestion to fix the newly introduced vulnerability all at once.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-45c89e4bfcd11b9442b1849378751ce8f178e464%2Fautofix-suggestions-and-inline-commenting-for-pr-checks_d5405ee7-a7ec-4996-be54-b6e3577304ee.png?alt=media" alt="Suggested code change to add &#x22;drop_invalid_header_fields&#x22; to AWS ALB resource configuration." width="563"></div>

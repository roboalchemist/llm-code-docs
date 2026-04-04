# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/release-agent/pr-review.md

# PR Review

### Overview

AI PR Review helps engineering teams ship higher-quality code by analyzing pull requests using Luciq’s agents.\
It detects bugs, flags anti-patterns, identifies performance and security risks, and summarizes the PR - before your team spends time reviewing.

The result: fewer regressions, fewer production crashes and bugs, and faster review cycles.

### How It Works

Each PR triggers Luciq’s multi-stage review pipeline:

1. GitHub event received via the Luciq GitHub App
2. Luciq agent start analyse the PR
3. The agent generates summary & explanations
4. Results posted back to GitHub as review comments + PR summary

This creates a review experience that is fast, actionable, and grounded in real production intelligence.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FJYsQJVXfgZfYgKkIDmMT%2FPR%20Review%20%2346.gif?alt=media&#x26;token=b0543ef2-3bcd-4eb1-b690-1763b0769b40" alt=""><figcaption></figcaption></figure>

### Installation

#### 1. Install the Luciq GitHub App

Navigate to:\
**Settings** → **Source Code Management** → I**nstall GitHub App**

Grant repository access to the repos you want reviewed.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FkghqiUe8gAGdz7ZM6ILR%2Fimage.png?alt=media&#x26;token=4f15f5d5-c9dc-4bc3-9b9c-f686509911a9" alt=""><figcaption></figcaption></figure>

#### 2. Enable AI PR Review

Once the GitHub App is connected, you can enable or disable AI PR Review per application from the Settings page.

#### 3. Create or update a Pull Request

Mention Luciq inside the PR by commenting:

```
@luciq review
```

Luciq will immediately react to your comment with a thumbs up :thumbsup:  to confirm that the review has started.\
Once the analysis is complete, Luciq will post the PR summary and risk assessment as a new comment.

{% hint style="info" %}
The thumbs up :thumbsup:  reaction helps your team know that the AI review is in progress.
{% endhint %}

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FFUtwovbstZumS4wWbTh7%2Fimage.png?alt=media&#x26;token=9ab72dbe-c498-4ea4-8a3a-06e1a9311214" alt=""><figcaption></figcaption></figure>

### Security & Permissions

All AI processing happens within secure, isolated environments deployed inside Luciq’s infrastructure.\
Luciq only requests the minimum GitHub permissions required to:

* Read pull requests and diffs
* Write review comments
* Access relevant repository metadata

No code is stored, and no data leaves Luciq’s secure environment.

### Best Practices

* Enable Luciq PR Review on your core repositories first
* Use AI findings as a first pass before the developer do a deeper review
* Pay attention to high-risk flags - they often correlate with production issues

### FAQ

**Does Luciq modify my code?**\
No. Luciq only comments and recommends improvements.

**Can I disable the AI reviewer on certain repos?**\
Yes - permissions and enablement are per-application, also review added only when you mention luciq reviewer.

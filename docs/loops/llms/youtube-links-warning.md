# Source: https://loops.so/docs/deliverability/youtube-links-warning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Shortened YouTube links warning

> Information about shortened YouTube links being flagged in Gmail

We are currently flagging shortened YouTube links (youtu.be) in emails because Gmail is incorrectly identifying them as phishing links.

## What's happening

Gmail's spam filters are flagging emails containing shortened YouTube links as potential phishing attempts. To protect your deliverability, our [Guardian](/creating-emails/guardian) feature will warn you if your email contains these links.

## Recommendation

Use full YouTube URLs instead of shortened links:

* **Avoid:** `youtu.be/abc123`
* **Use:** `youtube.com/watch?v=abc123`

## Status

We are actively monitoring this situation and will retire this warning once Gmail resolves the issue.

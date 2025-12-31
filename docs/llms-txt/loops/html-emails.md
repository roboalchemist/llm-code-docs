# Source: https://loops.so/docs/guides/html-emails.md

# Why we don't support HTML emails

> Understanding why Loops doesn't support HTML email content and the benefits of our approach.

This guide explains why Loops doesn't support HTML email content in your requests, and how this approach benefits your team in the long run. We'll cover the common questions we receive and explain our philosophy on email management.

## The multi-provider problem

In our experience working with hundreds of software companies, we've noticed a pattern: by the Series B stage, most companies are using 3-6 different email sending providers. This fragmentation happens because different teams have different needs:

* Growth teams need advanced automation tools
* Marketing teams focus on promotional content
* Product teams send surveys and feature-specific emails
* Sales teams need targeted outreach
* Customer success teams handle support emails
* Engineering teams want simple, maintainable solutions

Each department gets its own tool, requiring coordination between design, marketing, legal, and engineering to keep everything working together.

**We believe there's a better way.**

## Why we don't support HTML content

We intentionally don't support HTML content in your requests because we don't believe emails belong in your codebase. Here's why:

### Branding management

When you need to update your brand colors, footer copy, or logo, you shouldn't need to:

1. Open a pull request
2. Update code
3. Deploy changes
4. Test across all email types

In Loops, these changes are a single click away and apply instantly across all your emails, whether they're transactional, marketing, or product updates. Even better, non-technical team members can make these changes without involving engineering.

### Email client compatibility

Email clients are notoriously inconsistent in how they render HTML. We maintain daily updates to our email rendering system to handle things like:

* New email client versions
* Dark mode changes
* Mobile rendering quirks
* Legacy client support

By handling this complexity for you, we ensure your emails look great everywhere, from the latest iPhone to that ancient Outlook version your biggest client refuses to update.

### Long-term support

Email clients evolve slowly but constantly. Keeping up with that is literally our full-time job. By taking HTML out of your codebase, we're basically giving you a free email-compatibility team that monitors email client changes, updates, tests across all major clients, and handles edge cases.

### Security and deliverability

When major email providers like Gmail and Yahoo update their guidelines, we catch changes early and update our system proactively, ensuring your emails remain compliant and maintain high deliverability rates.

### Team collaboration

Keeping your emails out of your codebase means any member of your team can make changes without engineering involvement.

It's also possible to preview new content or designs without affecting live emails, and make changes instantly without deployment.

## Summary

You probably have better things to do than manage email templates. Our approach means:

* Your team can update emails without engineering
* Changes are instant and safe
* Emails look great everywhere
* You maintain consistent branding
* We handle all the technical complexity

## Read more

<CardGroup>
  <Card title="Improve your inbox placement" icon="inbox" href="/deliverability/improving-inbox-placement" />

  <Card title="Understanding email open rates" icon="envelope-open-text" href="/deliverability/understanding-email-open-rates" />

  <Card title="Delivery optimization" icon="chart-line" href="/deliverability/optimization" />
</CardGroup>

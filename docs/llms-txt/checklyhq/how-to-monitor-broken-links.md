# Source: https://checklyhq.com/docs/guides/how-to-monitor-broken-links.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring for Broken Links with Playwright & Checkly

> Learn how to check for broken links on your webpages with Playwright.

## Why you should monitor for broken links.

If your content lives in markdown and is only updated on deployments, checking for broken links in CICD will work out
fine. But in my experience, this is rarely the case.

Website content often comes from a CMS or results from data stored in a database so that people can change content
without relying on a developer. And that's great for the team, but it also means that links can change at any time.
Your site can and will include broken links at any time.

Will this be a big deal? It depends. But if you consider being in charge of a popular newspaper website, a broken top
story link on the home page will get someone into trouble.

In this case, you can adopt [synthetic monitoring](https://www.checklyhq.com/product/synthetic-monitoring/), constantly run your Playwright scripts on a schedule, and
receive alerts when your tests fail. When then someone typoed a broken link into your site, you'll be the first to know about it because you received a timely alert.

<img src="https://mintcdn.com/checkly-422f444a/VAj__e35Pt2i8_lu/images/guides/images/checkly-links.png?fit=max&auto=format&n=VAj__e35Pt2i8_lu&q=85&s=901a8e8e4d1e5a7b0e1aaf6bbbc9effc" alt="Run playwright tests on a Schedule with Checkly" width="803" height="606" data-path="images/guides/images/checkly-links.png" />


Built with [Mintlify](https://mintlify.com).
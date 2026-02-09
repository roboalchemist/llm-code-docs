# Source: https://www.mintlify.com/docs/create/changelogs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelogs

> Create product changelogs with RSS feed support for subscribers.

Create a changelog for your docs by adding [Update components](/components/update) to a page.

Check out the [Mintlify changelog](/changelog) as an example: you can include links, images, text, and demos of your new features in each update.

## Setting up your changelog

<Steps>
  <Step title="Create a page for your changelog">
    1. Create a new page in your docs such as `changelog.mdx` or `updates.mdx`.
    2. Add your changelog page to your navigation scheme in your `docs.json`.
  </Step>

  <Step title="Add Update components to your changelog">
    Add an `Update` for each changelog entry.

    Include relevant information like feature releases, bug fixes, or other announcements.
  </Step>
</Steps>

```mdx Example changelog.mdx theme={null}
---
title: "Changelog"
description: "Product updates and announcements"
---
<Update label="March 2025" description="v0.0.10">
  Added a new Wintergreen flavor.

  Released a new version of the Spearmint flavor, now with 10% more mint.
</Update>

<Update label="February 2025" description="v0.0.09">
  Released a new version of the Spearmint flavor.
</Update>
```

## Customizing your changelog

Control how people navigate your changelog and stay up to date with your product information.

### Table of contents

Each `label` property for an `Update` automatically creates an entry in the right sidebar's table of contents. This is the default navigation for your changelog.

<Frame>
  <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3f3018782389da4ccab476fbecfaa84b" alt="Changelog with table of contents displayed in light mode." className="block dark:hidden" data-og-width="2632" width="2632" data-og-height="1502" height="1502" data-path="images/changelog-toc-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b647661dfd9106e29447eff40aa8ecab 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5a46b78addb99d0d7efa5c95ad4d3336 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=ba41c6d011be619589f8fded5c8da51b 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8c4968ea5bb462f0353b24389f77b5ea 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8c201e27bfaff95dfb2c8d014fe34cd4 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-light.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=476a2f448ecfee904efcb687cbc58f77 2500w" />

  <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d8e69af3525f597335e5d2dcb6ec8192" alt="Changelog with table of contents displayed in dark mode." className="hidden dark:block" data-og-width="2590" width="2590" data-og-height="1432" height="1432" data-path="images/changelog-toc-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=ccee9015dcedba719ffd954c12576caf 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b5731bdffd2be18d3684cff4e44bc17e 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=765b9b8785ed54cb6583b79db4e68b87 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d2f285e83185bc5705aa242dd7fbcd12 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=6ea107d1ab6df90a20484eb05342205e 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-toc-dark.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d313d4d719dd23b48381e88f84ef4acb 2500w" />
</Frame>

### Tag filters

Add `tags` to your `Update` components to replace the table of contents with tag filters. Users can filter the changelog by selecting one or more tags:

```mdx Tag filters example wrap theme={null}
<Update label="March 2025" description="v0.0.10" tags={["Wintergreen", "Spearmint"]}>
  Added a new Wintergreen flavor.

  Released a new version of the Spearmint flavor, now with 10% more mint.
</Update>

<Update label="February 2025" description="v0.0.09" tags={["Spearmint"]}>
  Released a new version of the Spearmint flavor.
</Update>

<Update label="January 2025" description="v0.0.08" tags={["Peppermint", "Spearmint"]}>
  Deprecated the Peppermint flavor.

  Released a new version of the Spearmint flavor.
</Update>
```

<Frame>
  <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1c6e5fc5902e27e520fa217924871589" alt="Changelog in light mode with the Peppermint tag filter selected." className="block dark:hidden" data-og-width="2170" width="2170" data-og-height="582" height="582" data-path="images/changelog-filters-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=46da93d58b3f4390b49fe7966cf17343 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=48c59b235ea462ba5dc5b87db9baf41e 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=492638ba7e2bd9d00a78220dddc93003 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=40eceaf16f1b96f419c5c14608647052 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=36b62b16258b9013ea38eeb1afee99a1 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-light.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=fef0c4b81fa215680d41998c39b23bc6 2500w" />

  <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5aad3dbe45acd21db99dfae04b4846f7" alt="Changelog in dark mode with the Peppermint tag filter selected." className="hidden dark:block" data-og-width="2172" width="2172" data-og-height="584" height="584" data-path="images/changelog-filters-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1bb5fe9face10a4b88ea85a80d334ab1 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=547f7a95b8b0b5f2a1f706a7799daedc 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f2c13f0e8c1aa9a7e4dbc2915b8e415f 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e8cb5cc1567b6bd4f5f51ff33dd317da 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=6010f30b249bc7ec4535adddb16fda10 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-filters-dark.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=334968478cd2351ee0a241b6c6726a4e 2500w" />
</Frame>

<Tip>
  The table of contents and changelog filters are hidden when using `custom`, `center`, or `wide` page modes. Learn more about [page modes](/organize/pages#page-mode).
</Tip>

### Subscribable changelogs

<Note>RSS feeds are only available on public documentation.</Note>

Use `Update` components to create a subscribable RSS feed at your page URL with `/rss.xml` appended. For example, `mintlify.com/docs/changelog/rss.xml`.

The RSS feed publishes entries when you add new `Update` components and when modify headings inside of existing `Update` components.

RSS feed entries contain pure Markdown only. Components, code, and HTML elements are excluded. Use the `rss` property to provide alternative text descriptions for RSS subscribers when your updates include content that is excluded.

```xml Example RSS feed theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <title><![CDATA[Product updates]]></title>
    <description><![CDATA[New updates and improvements]]></description>
    <link>https://mintlify.com/docs</link>
    <generator>RSS for Node</generator>
    <lastBuildDate>Mon, 21 Jul 2025 21:21:47 GMT</lastBuildDate>
    <atom:link href="https://mintlify.com/docs/changelog/rss.xml" rel="self" type="application/rss+xml"/>
    <copyright><![CDATA[Mintlify]]></copyright>
    <docs>https://mintlify.com/docs</docs>
    <item>
      <title><![CDATA[June 2025]]></title>
      <link>https://mintlify.com/docs/changelog#june-2025</link>
      <guid isPermaLink="true">https://mintlify.com/docs/changelog#june-2025</guid>
      <pubDate>Mon, 23 Jun 2025 16:54:22 GMT</pubDate>
    </item>
  </channel>
</rss>
```

RSS feeds can integrate with Slack, email, or other subscription tools to notify users of product changes. Some options include:

* [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack)
* [Email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email) via Zapier
* Discord bots like [Readybot](https://readybot.io) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot)

To make the RSS feed discoverable, you can display an RSS icon button that links to the feed at the top of the page. Add `rss: true` to the page frontmatter:

```mdx  theme={null}
---
rss: true
---
```

<Frame>
  <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=088f41b7cdb5f701909d2c5cea5e52fd" alt="Changelog page in light mode with RSS feed button enabled." className="block dark:hidden" data-og-width="1486" width="1486" data-og-height="388" height="388" data-path="images/changelog-rss-button-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b0c9bfd4e52fe19bfa9d4411e1b12860 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5857160d39488b2d392dafc0eac4560f 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=49b2dcee13ef1f3945da2ae88a3521ec 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a941b884376e2a88fcefe85d0d63f1e9 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=793c7d07b06a87765c0cebf53ce8d530 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-light.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=af09f50b2f217bef9578b1cc6ad36002 2500w" />

  <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=67b22fea2a8411fe4c38caf569a8bf5f" alt="Changelog page in dark mode with RSS feed button enabled." className="hidden dark:block" data-og-width="1486" width="1486" data-og-height="388" height="388" data-path="images/changelog-rss-button-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0424eced2ece3e7d4854cfa8b344177d 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=80f4792d7179990e14dcc329007cfbc6 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c5b8d99afd8bc61e7526bea024ec6778 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=eb7dfdc0d700d97f7cc3f5c44e756286 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=18bf3c4cf2489d3eb996c3d6ffb54df7 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/changelog-rss-button-dark.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3252c4ade1cee20cef3fcb163a908af6 2500w" />
</Frame>

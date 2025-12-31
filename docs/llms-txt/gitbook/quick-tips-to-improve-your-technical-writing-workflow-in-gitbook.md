# Source: https://gitbook.com/docs/guides/docs-workflow-optimization/quick-tips-to-improve-your-technical-writing-workflow-in-gitbook.md

# Quick tips to improve your technical writing workflow in GitBook

Your technical documentation probably already contains all the important information you need to give to your readers. Nice work! But could you make any changes to make it easier to understand, or more accessible?

There are a few simple ways to improve your work (and your workflow) in GitBook. From adding relevant links to setting up a two-way sync with GitHub or GitLab. In this post we’ll share some of those tips — as well as advice on the fastest way to edit your content in GitBook to make it look it’s best.

### Use Markdown to write faster <a href="#use-markdown-to-write-faster" id="use-markdown-to-write-faster"></a>

Yes, you can certainly write into the GitBook editor in plain text. But it also supports Markdown as a keyboard-friendly way to format your content and add blocks fast.

GitBook supports basic formatting, including **bold** and *italic*. But you can also add H1, H2 and H3 titles using hashes (`#`) at the start of a new block, add code and quote blocks, and create lists with a few keystrokes.

*New to Markdown? We’ve got your back. Many other tools outside GitBook support it — so learning it now will likely prove useful in other places. You can learn more about our Markdown support* [*in our documentation*](https://app.gitbook.com/s/NkEGS7hzeqa35sMXQZ4X/creating-content/formatting/markdown)*, and explore Markdown itself in more detail over at* [*CommonMark*](https://commonmark.org/)*.*

### Learn some handy keyboard shortcuts <a href="#learn-some-handy-keyboard-shortcuts" id="learn-some-handy-keyboard-shortcuts"></a>

Okay, so you’re a Markdown master. In that case, here are some quick keyboard shortcuts that will speed up the tiny tasks you carry out multiple times every day. Below, we’ve chosen a few of our most-used shortcuts to get you started. You can head [to our documentation](https://app.gitbook.com/s/NkEGS7hzeqa35sMXQZ4X/resources/keyboard-shortcuts) to explore the full list.

**⌘ + K** (Mac) or **Ctrl + K** (Windows) — Open the **Ask or search** panel

**⌘ + Enter** (Mac) or **Ctrl + Enter** (Windows) — Exit from content block (code, tabs, table, quote, etc)

**Esc** — Select the entire active block (or multiple active blocks)

### Add and change blocks fast <a href="#add-and-change-blocks-fast" id="add-and-change-blocks-fast"></a>

There’s one keyboard shortcut we didn’t list above, because we think it’s important enough to deserve its own section. Hitting `/` opens the block-insert palette — and unlocks a whole selection of possibilities for your content.

Use it on a new, empty block and you can select from the full list of blocks in GitBook, plus any integrations you’ve added. You can scroll through the list, or type to narrow it down.

Alternatively, you can use **⌘ + /** or **Ctrl + /** on a block you’re already editing — whatever it’s type — to open up a context menu with options for that current block. In a text block that means you can switch between paragraph and heading blocks. In a code block, you can set the syntax, add line numbers, and more.

{% embed url="<https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLBGJKQic7BQYBXmVSjy0%2Fuploads%2F4Jiwi9cm2XZEvFLJtulz%2Fcode-block.mp4?alt=media&token=72bd7161-c0f0-4511-8334-d398336fa1d4?autoplay=1>" %}
Add and update blocks using the block insert menu.
{% endembed %}

See what we mean? Super powerful — give it a try on different blocks to see what it can do!

### Add inline content <a href="#add-inline-content" id="add-inline-content"></a>

Using the block-insert palette isn’t the only way to add content to your pages fast, though. When typing in a text block, you can hit `/` at any time to open the inline palette.

The inline palette lets you add an image, emoji, link or math & TeX system. It’s a fast way to access common inputs without lifting your fingers from the keyboard — handy when you need to add diagram images or link to another part of your documentation.

<figure><img src="https://1940848424-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLBGJKQic7BQYBXmVSjy0%2Fuploads%2FZ2NuonVJtgYYmOL6t1cN%2Finline-menu.jpg?alt=media&#x26;token=c41216e9-d5cc-4ef9-82f7-3c7e574080b6" alt=""><figcaption><p>Add inline content directly in your content.</p></figcaption></figure>

{% hint style="info" %}
**Tip:** Alternatively, you can add emoji by typing `:` followed by the name of the emoji you want to add 👍
{% endhint %}

### Select and move blocks <a href="#select-and-move-blocks" id="select-and-move-blocks"></a>

One shortcut we did list above, but bears repeating, is the option to select a whole block or blocks — simply by hitting the `Esc` key. This is great for reorganizing content within your page, as you can drag multiple blocks around at once, or use commands like cut, copy, paste and delete to manage your content.

{% embed url="<https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLBGJKQic7BQYBXmVSjy0%2Fuploads%2FASqYAgNxI2JT1EnRmC6k%2Fblock-selection.mp4?alt=media&token=1fb80dc2-688b-4148-b95c-fe550d0369c6?autoplay=1>" %}
Select and move blocks.
{% endembed %}

### Add email address links using mailto: <a href="#add-email-address-links-using-mailto" id="add-email-address-links-using-mailto"></a>

You want people to be able to get in touch with you if they have questions about your docs, right? Well the best way is to use a hyperlink with a `mailto:` prefix!

If you need to add contact information into a GitBook page, highlight the words you want to add it to, add a link using the context menu, then simply add `mailto:` before the email address when you type it in.

Now people can drop you a line with a click&#x20;

### Use relative links <a href="#use-relative-links" id="use-relative-links"></a>

Relative links in GitBook are the best way to link to other parts of your documentation. Why? Because if someone changes the URL, name, or location of the linked content, GitBook will still keep its reference up to date. And that means fewer broken links.

If your technical documentation is part of your team’s internal knowledge base, you can link to other anchors, pages, or spaces within your internal content. If it’s public, you can link to anchors or other pages in your published space.

You add them just like you add any other link. Highlight the text you want to use as a link, hit the link button of hit ⌘+K or Ctrl+K, then simply type in the name of the anchor, page or space you want to link to.

<figure><img src="https://1940848424-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLBGJKQic7BQYBXmVSjy0%2Fuploads%2FT1YSM45UO3HYdTBM8Ca2%2Frelative-links.jpg?alt=media&#x26;token=5be87bf8-0798-4e70-a645-0abd65e2f327" alt=""><figcaption><p>Add relative links to other pages in your documentation.</p></figcaption></figure>

### Change the hint color and icon with a click <a href="#change-the-hint-color-and-icon-with-a-click" id="change-the-hint-color-and-icon-with-a-click"></a>

We’re sure you know that hint blocks have four different colors and styles that you can choose from, to match the kind of content inside. What you may not know is that you can quickly cycle through the different styles simply by clicking the icon in the block itself. There are four to choose from — and it saves you opening the menu to change it!

### Add integrations <a href="#add-integrations" id="add-integrations"></a>

While there are plenty of built-in tools that will make your life with GitBook easier, you shouldn’t stop there. We have a whole host of integrations that you can add to improve your workflows — and your technical documentation.

From adding extra [analytics tools](https://www.gitbook.com/integrations/googleanalytics) to embedding [Linear issues](https://www.gitbook.com/integrations/linear), [Mermaid diagrams](https://www.gitbook.com/integrations/mermaid) and [RunKit notebooks](https://www.gitbook.com/integrations/runkit), you’ll find plenty of ways to supercharge your technical docs and get extra features with just a few clicks.

Take a look at [all our integrations](https://www.gitbook.com/integrations), and find out how soon, you’ll be able to [build your own](https://gitbook.com/docs/guides/docs-workflow-optimization/broken-reference).

### Set up Git Sync <a href="#set-up-git-sync" id="set-up-git-sync"></a>

This last entry is a big one — and if you haven‘t set it up already, it could save you hours of work in the long-run.

Git Sync lets technical teams synchronize GitHub or GitLab repositories with GitBook — and turn existing Markdown files into beautiful, user-friendly technical documentation. And when you edit that content in GitBook, Git Sync will automatically update your codebase in GitHub or GitLab to keep everything in sync.

Best of all, Git Sync is two-way — so if you make a commit in GitHub or GitLab, that change will also appear automatically in GitBook. How handy is that?

Once you’ve set up the sync, your whole team can contribute to your technical documentation — and your wider knowledge base — no matter which tool they prefer to use.

Find out how to get set up [in our documentation](https://app.gitbook.com/s/NkEGS7hzeqa35sMXQZ4X/getting-started/git-sync).

***

[**→ 7 tips to improve your public docs**](https://gitbook.com/docs/guides/docs-workflow-optimization/7-ways-to-make-your-public-documentation-more-useful-for-users)

[**→ Advice on writing great documentation**](https://steves-space.gitbook.io/how-to-write-great-documentation/?utm_source=marketing_site\&utm_medium=referral\&utm_campaign=gitbook_library)

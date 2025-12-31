# Source: https://docs.warp.dev/terminal/blocks/block-sharing.md

# Block Sharing

{% hint style="info" %}
This action sends command information to our server and is explicitly opt-in. Read more about privacy at Warp on [our privacy page](https://www.warp.dev/privacy).
{% endhint %}

Share your blocks with a permalink or HTML embed. You can get started with shared blocks by opening the context menu and copying the command, output, or prompt.

## How to Share Blocks

{% tabs %}
{% tab title="macOS" %}
To share your blocks, follow these steps:

1. On a finished block, click the context menu and select `Share...` or select the block and hit `CMD-SHIFT-S`.
2. A modal will pop up that lets you title your block and customize it by selecting which parts of the block you want to share (e.g. command, output, prompt, etc.).
3. Click either "Create link" or "Get embed" depending on how you want to share your block.
4. The link or embed snippet will be copied to your clipboard.
   {% endtab %}

{% tab title="Windows" %}
To share your blocks, follow these steps:

1. On a finished block, click the context menu and select `Share...` or by setting up a key bind for Share Block in `Settings > Keyboard Shortcuts`.
2. A modal will pop up that lets you title your block and customize it by selecting which parts of the block you want to share (e.g. command, output, prompt, etc.).
3. Click either "Create link" or "Get embed" depending on how you want to share your block.
4. The link or embed snippet will be copied to your clipboard.
   {% endtab %}

{% tab title="Linux" %}
To share your blocks, follow these steps:

1. On a finished block, click the context menu and select `Share...` or by setting up a key bind for Share Block in `Settings > Keyboard Shortcuts`.
2. A modal will pop up that lets you title your block and customize it by selecting which parts of the block you want to share (e.g. command, output, prompt, etc.).
3. Click either "Create link" or "Get embed" depending on how you want to share your block.
4. The link or embed snippet will be copied to your clipboard.
   {% endtab %}
   {% endtabs %}

{% hint style="info" %}
If you experience any issues with block sharing, please see our known issues for [troubleshooting steps](https://docs.warp.dev/support-and-billing/known-issues#online-features-dont-work).
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a4fd4b700beedbbec7864cd4c309b53ff75461cb%2Fblock-sharing-embed.gif?alt=media&#x26;token=02f237e8-061c-42ee-93ae-cb6b1da9fdc6" alt=""><figcaption><p>Block Sharing &#x26; Embed Demo</p></figcaption></figure>

## Permalink

Create and share a permalink to your blocks to collaborate with teammates. Here is the [web permalink](https://app.warp.dev/block/vzFATak939iqGWfNh7wsAP) of the block depicted below.

![Shared Block](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-221d43e8629ad806343376b4647d9d7188c8ca86%2Fshared_block.png?alt=media\&token=8f429a14-bdaf-4e2e-8e19-92525657252b)

## Embedded Blocks

Create and embed your blocks on web pages to help your readers follow along with technical writing. Readers can interact with an embedded block as they would with a block in Warp, with a context menu and styling. When you click "Get embed", Warp will copy an `iframe` to your clipboard. Here's an example `iframe`:

```html
<iframe src="https://app.warp.dev/block/embed/qn0g1CqQnkYjEafPH5HCVT"
title="server script error" style="width: 712px; height: 397px; border:0;
overflow:hidden;" allow="clipboard-read; clipboard-write"></iframe>
```

#### Embedded Block Example on Web Page

![Embedded Block Example](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-d9229fcb56841824629e982884ea5bb8aee0781f%2Fembed.png?alt=media\&token=15202210-1745-45a1-9b41-3a7244b0dfc4)

## Managing Shared Blocks

You can unshare a block by navigating to `Settings > Shared blocks`. Currently, shared blocks are accessible to anyone with the link.

## Link Previews

Shared permalinks will also display a preview of your code for quick context on each link.

{% hint style="info" %}
Compatible with any platform that supports Open Graph or Twitter meta tags. For example Slack, Twitter, Facebook, Telegram, Notion, and more ...
{% endhint %}

{% embed url="<https://www.loom.com/share/a78147fee8804c00b08a1decbc0d4e72?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Share and Unfurl a Block Preview
{% endembed %}

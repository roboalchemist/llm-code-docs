# Source: https://docs.warp.dev/terminal/blocks/block-actions.md

# Block Actions

## Accessing Block Actions

There are 2 ways you can access Block actions.

1. Hover over a Block and click the kebab (three dots) button on the right-hand side.
2. Right-click a Block.

{% embed url="<https://www.loom.com/share/3dec25e548d4484aa3dd6437869e2bbf?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Accessing Block Actions
{% endembed %}

## Copy Input / Output of Block

For command blocks, you can `RIGHT-CLICK` on a Block or click the context menu and copy the Block command, output, or both.

For AI blocks, you can `RIGHT-CLICK` to copy the prompt, output, both or the entire conversation.

{% embed url="<https://www.loom.com/share/9ad67eca0a8d47afb82cc1acba617f3c?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Copy Block Actions
{% endembed %}

## Sharing a Block

Share a block easily with coworkers or teammates by creating a web permalink. This preserves formatting and makes debugging and sharing output easy. [See Block Sharing Page.](https://docs.warp.dev/terminal/blocks/block-sharing)

## Bookmarking a Block

Quickly navigate to important Blocks despite where they are in the terminal history.

{% tabs %}
{% tab title="macOS" %}
Ways to bookmark a Block:

1. Select `Toggle bookmark` in the block context menu
2. Use `CMD-B` keybinding to bookmark a selected block

Navigate to a bookmarked Block, by:

* Clicking on the indicator.\
  The indicator position reflects the approximate position of the Block in the Block history. Hovering over the indicator will give a snapshot of the Block including its prompt, command, and the last two lines of output.
* Pressing `OPTION-UP` and `OPTION-DOWN`
  {% endtab %}

{% tab title="Windows" %}
There are Ways to bookmark a Block:

1. Select `Toggle bookmark` in the block context menu
2. Use `CTRL-SHIFT-B` keybinding to bookmark a selected block

Navigate to a bookmarked Block, by:

* Clicking on the indicator.\
  The indicator position reflects the approximate position of the Block in the Block history. Hovering over the indicator will give a snapshot of the Block including its prompt, command, and the last two lines of output.
* Pressing `ALT-UP` and `ALT-DOWN`
  {% endtab %}

{% tab title="Linux" %}
Ways to bookmark a Block:

1. Click on the bookmark icon in the top right corner of a Block
2. Select `Toggle bookmark` in the block context menu
3. Use `CTRL-SHIFT-B` keybinding to bookmark a selected block

Navigate to a bookmarked Block, by:

* Clicking on the indicator.\
  The indicator position reflects the approximate position of the Block in the Block history. Hovering over the indicator will give a snapshot of the Block including its prompt, command, and the last two lines of output.
* Pressing `ALT-UP` and `ALT-DOWN`
  {% endtab %}
  {% endtabs %}

{% hint style="info" %}
Bookmarks only persist while the session is open, once you close the session they are lost. If you want to save the command and output for later use, [Share the Block](https://docs.warp.dev/terminal/blocks/block-sharing).
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ce03da65a5db101052441f0d7e2c54cd71439e4c%2Fblock-bookmarks.gif?alt=media" alt=""><figcaption><p>Bookmarking a Block</p></figcaption></figure>

## Search Within A Block

Quickly find important information within a Block. [See Find page](https://docs.warp.dev/terminal/blocks/find)

{% tabs %}
{% tab title="macOS" %}
With a Block selected, press "Find Within Block" or use `CMD-F` to search within a Block.
{% endtab %}

{% tab title="Windows" %}
With a Block selected, Press "Find Within Block" or use `CTRL-SHIFT-F` to search within a Block.
{% endtab %}

{% tab title="Linux" %}
With a Block selected, Press "Find Within Block" or use `CTRL-SHIFT-F` to search within a Block.
{% endtab %}
{% endtabs %}

{% embed url="<https://www.loom.com/share/7dda0e7a6ec144cfb6410d29a586ddd0?hide_owner=true&hide_share=true&hide_title=true&hideEmbedTopBar=true>" %}
Search within a Block
{% endembed %}

## Filtering a Block

Filter the output lines of a block natively in Warp to quickly focus on a subset of the block. [See Block Filtering Page](https://docs.warp.dev/terminal/blocks/block-filtering).

{% tabs %}
{% tab title="macOS" %}

* Using the keybinding `OPT-SHIFT-F` by default to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}

{% tab title="Windows" %}

* Using the keybinding `ALT-SHIFT-F` to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}

{% tab title="Linux" %}

* Using the keybinding `ALT-SHIFT-F` to toggle filtering on the selected or latest block
* Selecting `Toggle Block Filter` in the block context menu
  {% endtab %}
  {% endtabs %}

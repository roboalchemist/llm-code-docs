# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/creating-content/blocks/hint.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/blocks/hint.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/blocks/hint.md

# Source: https://gitbook.com/docs/creating-content/blocks/hint.md

# Hints

Hints, or callouts, are a great way to bring the reader’s attention to specific elements in your documentation, such as tips, warnings, and other important information.

There are four different hint styles — you can change the style by clicking the colored icon, or by opening the block’s **Options menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> and selecting the style you want.

Hint blocks support [inline content](https://gitbook.com/docs/creating-content/formatting/inline) and [formatting](https://gitbook.com/docs/creating-content/formatting), as well some specific block types. To see which block types you can use in a hint, hit `/` on an empty line and check the [insert palette](https://gitbook.com/docs/creating-content/blocks/..#inserting-a-new-content-block).

### Examples of hint blocks <a href="#example-of-a-hint" id="example-of-a-hint"></a>

{% hint style="info" %}
**Info hints** are great for showing general information, or providing tips and tricks.
{% endhint %}

{% hint style="success" %}
**Success hints** are good for showing positive actions or achievements.
{% endhint %}

{% hint style="warning" %}
**Warning hints** are good for showing important information or non-critical warnings.
{% endhint %}

{% hint style="danger" %}
**Danger hints** are good for highlighting destructive actions or raising attention to critical information.
{% endhint %}

{% hint style="info" %}
**This is a H2 heading**

This is a line

This is an inline <img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F0FzoF68PAY3Rv297meNB%2Fcommand.svg?alt=media&#x26;token=b07ff261-6e28-4879-8ab1-039a49f6ab41" alt="The Apple computer command icon" data-size="line"> image

* This is a second <mark style="color:orange;background-color:purple;">line using an unordered list and color</mark>
  {% endhint %}

To add a heading to your hint, you need to create a heading block as the the first block in the hint.

### Representation in Markdown

```markdown
{% hint style="info" %}
**Info hints** are great for showing general information, or providing tips and tricks.
{% endhint %}

{% hint style="success" %}
**Success hints** are good for showing positive actions or achievements.
{% endhint %}

{% hint style="warning" %}
**Warning hints** are good for showing important information or non-critical warnings.
{% endhint %}

{% hint style="danger" %}
**Danger hints** are good for highlighting destructive actions or raising attention to critical information.
{% endhint %}

{% hint style="info" %}

## This is a H2 heading

This is a line

This is an inline <img src="../../.gitbook/assets/25_01_10_command_icon_light.svg" alt="The Apple computer command icon" data-size="line"> image

- This is a second <mark style="color:orange;background-color:purple;">line using an unordered list and color</mark>
{% endhint %}
```

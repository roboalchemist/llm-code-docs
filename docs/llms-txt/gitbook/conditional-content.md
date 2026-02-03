# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/creating-content/blocks/conditional-content.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/blocks/conditional-content.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/blocks/conditional-content.md

# Source: https://gitbook.com/docs/creating-content/blocks/conditional-content.md

# Conditional content

Conditional content blocks let you control who can see a given block of content on your page based on user data and variables. These variables can be passed in via cookies, feature flags, authenticated access, or URL parameters.

### Create conditional content

To add a conditional block, begin a new line in the editor, type <kbd>/</kbd>, then select <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> **Conditional content**.

After inserting the block, click the red condition badge in the top right of the block.

Clicking this will allow you to add a condition through the [condition editor](https://gitbook.com/docs/publishing-documentation/adaptive-content/adapting-your-content#working-with-the-condition-editor). You’ll be able to write your condition as an [expression](https://gitbook.com/docs/creating-content/variables-and-expressions) that will run against data defined in your site. You can reference data from [variables](https://gitbook.com/docs/creating-content/variables-and-expressions), or data coming from visitors through their [claims](https://gitbook.com/docs/publishing-documentation/adaptive-content/enabling-adaptive-content#set-your-visitor-schema).

See [adaptive content](https://gitbook.com/docs/publishing-documentation/adaptive-content) for more details.

### Example

The examples below use a URL parameter linked from the button to control which conditional content block is visible.

{% if visitor.claims.unsigned.example\_attribute\_A %}
This block is only visible to users **with** attribute A.

<a href="https://gitbook.com/docs/creating-content/blocks/conditional-content?visitor.example_attribute_A=false" class="button primary">View without attribute A</a>
{% endif %}

{% if !visitor.claims.unsigned.example\_attribute\_A %}
This block is only visible to users **without** attribute A.

<a href="https://gitbook.com/docs/creating-content/blocks/conditional-content?visitor.example_attribute_A=true" class="button primary">View with attribute A</a>
{% endif %}

## Representation in Markdown

```markdown
## Example

{% if visitor.claims.unsigned.example_attribute_A %}
This block is only visible to users **with** attribute A.
<a href="https://gitbook.com/docs/creating-content/blocks/conditional-content?visitor.example_attribute_A=false" class="button primary">View without attribute A</a>
{% endif %}

{% if !visitor.claims.unsigned.example_attribute_A %}
This block is only visible to users **without** attribute A.
<a href="https://gitbook.com/docs/creating-content/blocks/conditional-content?visitor.example_attribute_A=true" class="button primary">View with attribute A</a>
{% endif %}
```

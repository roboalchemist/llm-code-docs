# Source: https://redocly.com/docs/realm/customization/react-components/list/admonition.md

# Source: https://redocly.com/docs/realm/content/markdoc-tags/admonition.md

# Source: https://redocly.com/learn/markdoc/tags/admonition.md

# Admonition Tag [](/learn/markdoc/tags/tag-library#redocly-tag-badge)

The admonition tag calls your users' attention to a specific piece of information by placing it inside a pre-styled banner, separate from the main content.

Use admonitions to **add clarity** to your content or *communicate important information*.

## Syntax and usage

Use the admonition tag to wrap content. Choose between the pre-built styles using `type`. Optionally add a header with `name`.

Important warning
Stop! **Read me** before moving on.


```md
{% admonition type="warning" name="Important warning" %}
  Stop! **Read me** before moving on.
{% /admonition %}
```

## Attributes

| Attribute | Type | Description |
|  --- | --- | --- |
| `type` | String | **Required.**
Sets the type of admonition to info, warning, success, or danger. Examples below. |
| `name` | String | Adds a header to the admonition. Transforms to ALL CAPS. |


### Admonition types

Type `info` creates an **Info** admonition.

Type `warning` creates a **Warning** admonition.

Type `success` creates a **Success** admonition.

Type `danger` creates a **Danger** admonition.

## Examples

### Add relevant information

Admonitions can be *distracting*. Consider how they **help users** before adding them.


```md
  {% admonition type="info" %}
    Admonitions can be _distracting_. Consider how they **help users** before adding them.
  {% /admonition %}
```

### Highlight something important

Read this!
Users read admonitions *before* content. They can communicate essential information.


```md
  {% admonition type="warning" name="Read this!" %}
    Users read admonitions _before_ content. They can communicate essential information.
  {% /admonition %}
```

### Communicate urgency

Careful
Don't abuse admonitions or readers will ignore them. You might need them to communicate something before a user makes an irreversible decision.


```md
  {% admonition type="danger" name="Careful" %}
    Don't abuse admonitions or readers will ignore them. You might need them to communicate something before a user makes an irreversible decision.
  {% /admonition %}
```

### Celebrate wins

Success
You made it to the **last admonition example**. Hooray ð¥³!


```md
  {% admonition type="success" name="Success" %}
    You made it to the **last admonition example**. Hooray ð¥³!
  {% /admonition %}
```

## Best practices

**Use in moderation**
Overuse of admonitions will reduce their effectiveness and users will learn to ignore them.

**Don't use for page content**
Carefully consider the information you put in your admonitions. They should add value and clarity or communicate something important. If readers don't know what to expect, then admonitions won't draw their attention effectively.

**Use clear headers**
Use short, impactful headers that reflect the content to set the tone and encourage users to pay attention to the message.

**Choose the right type**
Select the admonition type that aligns with the nature of the content. This helps users understand *intent* and recognize the level of urgency. For example, you should use `warning` for cautionary information and `success` for confirmation or positive feedback.

**Admonitions *after* content**
Avoid using admonitions as the first element below headers or section headers. Giving readers information to consider *before* content adds to their cognitive load and reduces comprehension.
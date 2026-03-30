# Localization

> Learn how to add localization, or i18n, by using the Variants Block.

Localization in BaseHub is enabled by the Variant Block.

### Create the Variants Block

Somewhere in the Editor, press “/variants” and add the block. Name it “Language“. Make sure you create this block below a Document block.

### Add some langauges inside

Add some variants for the languages you’ll support.

![](https://assets.basehub.com/7b31fb4b/a3fad3704809acb484a47b3307083922/cleanshot-2024-11-25-at-21.32.282x.png?width=3840&quality=90&format=auto)

Something like this

### Enable the set on a Document or a Collection

Take a look at this short video to see how we do it.

### Query by variants on GraphQL

After committing your changes, you will be able to apply variants arguments on the blocks that you enabled it, check it out:

```
{
  # from this point on, the schema will inherit the variant selected
  posts(variants: { language: es }) {
    items {
      _title
      excerpt
      coverImage {
        url
      }
      body {
        json {
          content
        }
      }
    }
  }
}
```

info:

Note that variant sets can only live inside Documents. Because of their unique nature, they cannot be replicated by Components and instances behaviors.

## Full Example

*   GitHub: [https://github.com/basehub-ai/localized-blog](https://github.com/basehub-ai/localized-blog)
    
*   BaseHub: [https://basehub.com/basehub/localized-blog](https://basehub.com/basehub/localized-blog/explore)
    
*   Demo: [https://localized-blog-basehub.vercel.app/en](https://localized-blog-basehub.vercel.app/en)
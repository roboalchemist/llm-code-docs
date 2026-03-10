# Query API Guidelines

> Master GraphQL querying in BaseHub with comprehensive examples for layout and primitive blocks, filtering, ordering, and variants.

The Query API is GraphQL-based, allowing you to fetch content from your BaseHub repository using GraphQL queries.

## Layout Blocks

These blocks typically contain other nested blocks. They're key to giving the repository a tree-like structure. They're all objects and share some common GraphQL keys:

*   **\_title**: string
    
*   **\_slug**: string, auto generated based on the title
    
*   **\_sys**: object containing system fields like apiNamePath, createdAt, hash, id, idPath, lastModifiedAt, slug, slugPath, title
    

### Document

A single document/page, for example "homepage", or "about page", or something more generic like "globals" or "settings".

### Component

Like a document, but used to reutilize structures/schemas, like a "CTA", or even a section like "Features Grid Section", or a "Callout" to be used within a Rich Text block. It's quite flexible.

### Instance

Which practically targets a Component and sticks to its structure.

### List

Meant to be used for listing things. Gets its columns by targeting a Component and using it as "template". Has rows (instances), which are the actual items in the list. Useful for things like "Blog Posts", "Authors", "Categories", "Testimonials", etc.

List blocks have a GraphQL object with the following keys:

*   **items**: array of rows returned after applying sorts, filters, and pagination
    
*   **item**: grabs the first item from the items array
    
*   **\_meta**: contains totalCount and filteredCount
    

List blocks receive optional arguments:

*   **orderBy**: enum for sorting (e.g., `createdAt__DESC`)
    
*   **filter**: object for filtering based on field types
    
*   **first**: number, takes the first N items
    
*   **skip**: number, skips N items
    

## Query Examples

### Get the first 10 posts

```
{
  posts(first: 10) {
    items {
      _id
      _title
      date
      excerpt
      body {
        json {
          content
        }
      }
    }
  }
}
```

### Get a specific post by slug

```
{
  posts(filter: { _sys_slug: { eq: "my-blog-post-slug" } }) {
    items {
      _id
      _title
      date
      excerpt
      body {
        json {
          content
        }
      }
    }
  }
}
```

## Reference Blocks

Can target an Instance or a Component. Reference blocks take the structure of the component(s) they target:

1.  If `acceptedTypes` has just one component id, it takes that component's structure
    
2.  If `acceptedTypes` has multiple component ids, it becomes a union
    

### Single Reference Type

```
{
  demo {
    author {
      _title
      xUsername
      bio {
        json {
          content
        }
      }
    }
  }
}
```

### Multiple Reference Types (Union)

```
{
  demo {
    author {
      ... on Author {
        _title
        xUsername
        bio {
          json {
            content
          }
        }
      }
      ... on ExternalPerson {
        _title
        linkedinUrl
        company
        role
      }
    }
  }
}
```

## Primitive Blocks

These blocks typically contain the largest parts of the content. An important prop is the `isRequired` prop, which makes the field nullable or non-nullable accordingly.

### Text, Number, Boolean

Self explanatory primitive types.

### Date

ISO date string.

### Select

If `multiple={true}`, it returns an array of strings. Else, it returns a single string.

### Media

An object with the following properties:

*   **url**: string (can receive args: width, height, format, quality, blur)
    
*   **alt**: string (nullable)
    
*   **width**, **height**: number (nullable)
    
*   **blurDataURL**: string (nullable)
    
*   **mimeType**, **fileName**: string
    

### Rich Text

Rich text blocks have a GraphQL object with the following keys:

*   **json**: contains `content` (JSON definition) and optional `blocks` array
    
*   **markdown**: string representation
    
*   **html**: HTML representation
    
*   **plainText**: plain text representation
    
*   **readingTime**: number in minutes
    

### Rich Text Examples

```
{
  about {
    subtitle {
      json {
        content
      }
    }
  }
}
```

### Code Snippet

An object with `code` and `language` string properties.

### Color

An object with `hex`, `rgb`, and `hsl` string properties.

## Variant Sets

The variant set block is used to have different values for the same block. Different variants are defined inside a variant set block.

### Get variant set information

```
{
  settings {
    languages {
      variants {
        id
        isDefault
        label
        apiName
      }
    }
  }
}
```

### Query specific variant

```
{
  chapters {
    items {
      lessons(variants: { languages: es }) {
        items {
          transcription {
            plainText
          }
          video {
            url
          }
        }
      }
    }
  }
}
```

## Common Errors

### Missing items wrapper

❌ **Incorrect**:

```
{
  posts(filter: { _sys_slug: { eq: "my-blog-post-slug" } }) {
    _id
    _title
    date
  }
}
```

✅ **Correct**:

```
{
  posts(filter: { _sys_slug: { eq: "my-blog-post-slug" } }) {
    items {
      _id
      _title
      date
    }
  }
}
```

### Missing content in rich text

❌ **Incorrect**:

```
{
  about {
    subtitle {
      json
    }
  }
}
```

✅ **Correct**:

```
{
  about {
    subtitle {
      json {
        content
      }
    }
  }
}
```

### Incorrect variant placement

❌ **Incorrect** (variants on primitive blocks):

```
{
  chapters {
    items {
      lessons {
        items {
          transcription(variants: { languages: es }) {
            plainText
          }
        }
      }
    }
  }
}
```

✅ **Correct** (variants on layout blocks):

```
{
  chapters {
    items {
      lessons(variants: { languages: es }) {
        items {
          transcription {
            plainText
          }
        }
      }
    }
  }
}
```
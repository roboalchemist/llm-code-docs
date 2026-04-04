# Source: https://flatfile.com/docs/guides/utilizing-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Metadata

> Store descriptive information or data that provides additional context

Metadata allows you to store and retrieve additional data about any Flatfile resource without exposing it to end users. This key-value object provides a flexible way to attach custom information, track state, store references, or add contextual data to your resources.

## Universal Usage

Metadata can be added during resource creation or updated later using the Flatfile API. The metadata object accepts any valid JSON data and is accessible in all listeners and webhooks.

```javascript  theme={null}
await api.spaces.update(spaceId, {
  metadata: {
    userId: "user123",
    companyId: "company456",
    customField: "any value"
  }
});
```

## Resource Types

**Environment** - Store deployment details, version info, or environment state\
**Space** - Track user IDs, company information, or session data\
**Workbook** - Add expiration dates, processing flags, or workflow state\
**Record** - Store computed values, external IDs, or transformation flags\
**Field** - Define formatting rules, validation context, or display preferences

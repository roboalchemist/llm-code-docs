# Source: https://exa.ai/docs/changelog/highlights-restored-js-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JS SDK: highlights restored

> The highlights feature has been reintroduced in the JavaScript SDK (exa-js) as of version 2.0.11.

***

**Date: November 26, 2025**

The highlights feature is back in the JavaScript SDK. Following user feedback, we've reintroduced highlights in `exa-js` v2.0.11, allowing you to extract key sentences from search results with relevance scores.

## What's Back

The `highlights` option is now available in search and contents operations:

* `highlights: true` - Returns highlighted sentences with default settings
* `highlights: { maxCharacters, query }` - Customize extraction behavior

Results include:

* `highlights: string[]` - Array of extracted key sentences
* `highlightScores: number[]` - Relevance scores for each highlight

## Usage Examples

**Basic highlights:**

```javascript  theme={null}
const results = await exa.searchAndContents("latest AI research", {
  highlights: true
});

console.log(results.results[0].highlights);
// ["Key sentence from the article...", "Another relevant excerpt..."]
```

**With options:**

```javascript  theme={null}
const results = await exa.searchAndContents("machine learning tutorials", {
  highlights: {
    maxCharacters: 2000,
    query: "beginner friendly"
  }
});
```

**Combined with text:**

```javascript  theme={null}
const results = await exa.searchAndContents("climate news", {
  text: true,
  highlights: true
});
// Returns both full text and highlighted excerpts
```

## Scope

This update applies only to the JavaScript SDK (`exa-js`). Other SDKs can access highlights via direct API calls.

## Installation

```bash  theme={null}
npm install exa-js@latest
```

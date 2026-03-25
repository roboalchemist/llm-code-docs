# Source: https://crawlee.dev/js/api/core/class/PseudoUrl.md

# externalPseudoUrl<!-- -->

Represents a pseudo-URL (PURL) - a URL pattern used to find the matching URLs on a page or html document.

A PURL is simply a URL with special directives enclosed in `[]` brackets. Currently, the only supported directive is `[RegExp]`, which defines a JavaScript-style regular expression to match against the URL.

The `PseudoUrl` class can be constructed either using a pseudo-URL string or a regular expression (an instance of the `RegExp` object). With a pseudo-URL string, the matching is always case-insensitive. If you need case-sensitive matching, use an appropriate `RegExp` object.

Internally, `PseudoUrl` class is using `purlToRegExp` function which parses the provided PURL and converts it to an instance of the `RegExp` object (in case it's not).

For example, a PURL `http://www.example.com/pages/[(\w|-)*]` will match all of the following URLs:

* `http://www.example.com/pages/`
* `http://www.example.com/pages/my-awesome-page`
* `http://www.example.com/pages/something`

Be careful to correctly escape special characters in the pseudo-URL string. If either `[` or `]` is part of the normal query string, it must be encoded as `[\x5B]` or `[\x5D]`, respectively. For example, the following PURL:

```
http://www.example.com/search?do[\x5B]load[\x5D]=1
```

will match the URL:

```
http://www.example.com/search?do[load]=1
```

If the regular expression in the pseudo-URL contains a backslash character (), you need to escape it with another back backslash, as shown in the example below.

**Example usage:**

```
// Using a pseudo-URL string
const purl = new PseudoUrl('http://www.example.com/pages/[(\\w|-)+]');

// Using a regular expression
const purl2 = new PseudoUrl(/http://www\.example\.com/pages/(\w|-)+/);

if (purl.matches('http://www.example.com/pages/my-awesome-page')) console.log('Match!');
```

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**regex](#regex)

### Methods

* [**matches](#matches)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/pseudo_url/src/index.d.ts#L58)externalconstructor

* ****new PseudoUrl**(purl): [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md)

- #### Parameters

  * ##### externalpurl: string | RegExp

    A pseudo-URL string or a regular expression object. Using a `RegExp` instance enables more granular control, such as making the matching case-sensitive.

  #### Returns [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md)

## Properties<!-- -->[**](#Properties)

### [**](#regex)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/pseudo_url/src/index.d.ts#L51)externalreadonlyregex

**regex: RegExp

## Methods<!-- -->[**](#Methods)

### [**](#matches)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/pseudo_url/src/index.d.ts#L62)externalmatches

* ****matches**(url): boolean

- Determines whether a URL matches this pseudo-URL pattern.

  ***

  #### Parameters

  * ##### externalurl: string

  #### Returns boolean

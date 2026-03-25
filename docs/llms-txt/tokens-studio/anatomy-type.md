# Source: https://docs.tokens.studio/fundamentals/design-tokens/anatomy-type.md

# Token Anatomy - Type

## Token Anatomy - Type

The `type` of Design Token defines which category of design property this decision belongs to, or ***when*** it can be applied.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FmObosUuw4StzoO7T9rZE%2Fcode-tokenAnat-type.png?alt=media&#x26;token=2e245ed2-fa7c-4f80-aa8a-15a0d3177cb6" alt=""><figcaption><p>In this infographic, the Token examples on the right side highlight the Type. Both code blocks have <code>color</code>as the Token Type.</p></figcaption></figure>

### Type = Design property

For example, the system could interpret a Token with a Value of `#22c55e` applied to a text layer as a string property to create a text element or a color hex code.

When we define a Token Type of `color` alongside the Value, it's much easier to communicate that this design decision is to be applied *when* the **color** of a text element should be green.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FRQTHgvjERLOu5DfyHZWJ%2Ftoken-intro-example-type.png?alt=media&#x26;token=ac03c9f8-0607-4025-9b63-42d7556311a6" alt=""><figcaption><p>An infographic example of documenting a Token with a value of <code>#b1f1cb</code> with a different application depending on the Token Type that is defined. </p></figcaption></figure>

### Token Types for design properties

There are many 'Official' Token Types are listed in the [W3C Design Tokens Community Group (DTCG) Specifications for Design Tokens](https://tr.designtokens.org/format/#types).

Most often, `type`matches a design property. For example, the `type` of Color can be applied to any design element requiring color.

The DTCG Specifications define how the Token is written depending on its `type`. For example, a Typography Token requires several design decisions to be composed into a single token, whereas a Color Token does not.

Tokens Studio supports 24 unique Token Types, and the DTCG is constantly adding new Token Types to the specification. &#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FaRZaJgTzIJZttAGAla5S%2FtokenType-overview-all.png?alt=media&#x26;token=120dbaf9-052c-4346-83c4-d6a381213422" alt=""><figcaption><p>The Tokens page of the Tokens Studio Plugin shows all Token Types supported. The list is quite long, so the page is scrolled and shown side-by-side to capture them all. </p></figcaption></figure>

*If you are ready to jump into Tokens Studio, this guide will walk you through the nuances of each Token Type.*&#x20;

{% content-ref url="../../manage-tokens/token-types" %}
[token-types](https://docs.tokens.studio/manage-tokens/token-types)
{% endcontent-ref %}

***

### Up next - Value

Next, let's explore the `value` of a Design Token as this anatomic property depends on the Token's Type.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FqfnfWWz8bti3BjVUzhw8%2Ftoken-anatomy-value.png?alt=media&#x26;token=1f20de93-c969-4564-bc53-fe22b81c5c4b" alt=""><figcaption><p>In this infographic, the Token examples on the right side highlight the Value. The top code block shows a hard-coded value. The bottom code block has a value that references another Token. </p></figcaption></figure>

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>

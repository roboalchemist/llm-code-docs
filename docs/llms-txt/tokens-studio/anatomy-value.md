# Source: https://docs.tokens.studio/fundamentals/design-tokens/anatomy-value.md

# Token Anatomy - Value

## Token Anatomy - Value

The `value` of a Design Token defines ***what*** the design decision is and, in some cases, ***where*** the decision came from.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FIBYtR1L9F1lIwgfR96Rf%2Ftoken-anatomy-value.png?alt=media&#x26;token=b0ae649a-de5d-46d6-a5e4-44e480a14ebf" alt=""><figcaption><p>In this infographic, the Token examples on the right side highlight the Value. The top code block shows a hard-coded value. The bottom code block has a value that references another Token. </p></figcaption></figure>

### Value = What was decided

The **Values** that are possible for a Token are determined by its`type`.

For example, a hard-coded Value of `#22c55e` is possible when the **Token Type** is `color`, but not when it is `fontFamily`.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FKjHeWjGqRBcPjXTUXOB6%2Ftoken-intro-example-value.png?alt=media&#x26;token=4e642e3a-4cd3-44d9-be84-9fba0e769e6f" alt=""><figcaption><p>An infographic example of documenting a Token applied to the text layer of a button label with different values depending on the defined Token Type. </p></figcaption></figure>

The hard-coded values define ***what*** the design decision is, and the specifications for what values are accepted for each Token Type is defined by the [Design Tokens Community Group](https://tr.designtokens.org/format/#types).&#x20;

### Values that reference another Token

While it's helpful to give a human-readable name to a hard-coded value, the real power of Design Tokens comes from referencing another Token.&#x20;

If you write the Value of a Token as the name of an existing Token in the system wrapped in curly brackets, it will inherit its value from the referenced Token.&#x20;

For example, looking at the value of a Color Token applied to the label of a button component, you can see it has a value of `{brand.colors.success.on-success}`and same value of `#b1f1cb.`

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXCQycYs1Aj9L4uhD7BNx%2Ftoken-intro-example-value-references.png?alt=media&#x26;token=ef194b8f-d5fa-461c-adf2-2510f3682f14" alt=""><figcaption><p>An infographic example of documenting a Color Token applied to the text layer of a button label. The Value of the Token directly applied is referencing another Token. Following the pathway of referenced Tokens as Values shows where the Color comes from in the system. </p></figcaption></figure>

So if you were to ask yourself, "where did the label color decision for the button come from?" the answer is, "it's coming from my band decisions for success colors".

Values that reference another Token define ***where*** the design decision came from.

### Scaling systems with thoughtful references

The ability to reference another Token as a value creates a flexible and dynamic system which scales very quickly.

For example, if you decide that the text for success elements should be white instead of a light green, you only need to change the value of one Token (the `{brand.colors.success.on-success}` Token), and all components referencing it will change.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F4MmQIsV8E5QZKJO0nzo7%2Ftoken-intro-example-value-references-changeToken.png?alt=media&#x26;token=9bfd4a91-bd3b-4a70-bd27-4dd83597b2b1" alt=""><figcaption><p>An infographic example of documenting a Color Token applied to the text layer of a button label. The difference between the two buttons is the color of the label text which is controlled by the value of the middle Token. On the left side, it is referencing a Token from a <code>green</code>scale. On the right right, it is referencing a Token from a <code>grey</code>scale. </p></figcaption></figure>

### Scaling systems with math

In addition to hard-coded and references to other Tokens, Tokens Studio also supports math equations as the Value in compatible Token Types.

For example, you can create a Typography scale which is customized for different view-port sizes using a math equation.

### Summary

To sum it all up, the power of a Design Token lies in the flexibility of its Value.&#x20;

For design systems that support multiple themes, products, brands, or clients, using Token Values effectively means managing more design assets with the same components and minimal effort.

If you are ready to jump into Tokens Studio, this guide will through the more technical nuances of each Token Value you can work with in the Plugin for Figma.

{% content-ref url="../../manage-tokens/token-values" %}
[token-values](https://docs.tokens.studio/manage-tokens/token-values)
{% endcontent-ref %}

***

### Up next - Description

Next, let's explore the `description` of a Design Token as this anatomic property can help provide additional context about your design decisions.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPVOhLCiPqVNKvjFibqWO%2Ftoken-anatomy-card-description%402x.png?alt=media&#x26;token=e21ac8d1-5da1-4a73-9163-6bd558796266" alt=""><figcaption><p>In this infographic, the Token examples on the right side highlight the Description. </p></figcaption></figure>

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>

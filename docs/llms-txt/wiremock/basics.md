# Source: https://docs.wiremock.io/response-templating/basics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Responses with Templates

> Returning dynamic responses using Handlebars templates

Some elements of WireMock Cloud stub responses can be configured generated dynamically, via the use of [Handlebars templates](https://github.com/jknack/handlebars.java).

Most commonly this is used in the response body but response header values can also
be templated. For proxy responses, the target URL can be a template.

## Enabling templating

Enable templating for a stub by ticking the "Enable templating" box in the Response section:

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=bae55be65820726bc7837793e8daa8e1" title="Enable templating" height="70px" data-og-width="297" data-og-height="46" data-path="images/screenshots/enable-response-templating-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=acd3e5eabefc2b5c3e63cf922c57a9a7 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=8225c084606b02d44339dfe8352d78bc 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7f389217563396c7851e25fd2eb8a104 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=8f8b40c4b2fa385d246131c20028c285 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=461e650183f07389afc2a0a1950d01cc 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-response-templating-screenshot.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=5552fe8bf90ca2554798fb6602447016 2500w" />

Ticking this box means that header values can be templated e.g.

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=0d2aa3cd58a20127705c301effa9dc61" title="Header template" height="70px" data-og-width="1482" data-og-height="128" data-path="images/screenshots/header-template-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=9b6072a7654f890462236a2ee8d018ce 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=3db1487d1eff5dead5e6146f3e00845b 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=ef56db899f77ac87f09c5d0df422894c 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=fb13dc62a994128fcacf8b21bda69bfe 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=d6723423dee436ac525b107c35eec81d 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/header-template-screenshot.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=2fa71b5f690c2160362357f04e7495f3 2500w" />

And also the response body e.g.

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=76f15e19820495604e4b7be651b33c2e" title="Body template" height="130px" data-og-width="588" data-og-height="236" data-path="images/screenshots/body-template-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a0cfd969fa3aeafb43dc16a29cd971dc 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=c1c5348383fa0d54c3645b31dc92f737 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ad187a3cbe2dee1e4fead111d04c051e 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=cdea6771b2e8bca6cb98bdcab3967292 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=b1a9a17476307faa5280f0ee380dbd6d 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/body-template-screenshot.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7fc8509b0567753908e3e4109ea74865 2500w" />

## Handlebars overview

A complete description of the Handlebars syntax and core helpers can be found on the [Handlebars JS](https://handlebarsjs.com/guide/), but we'll cover the essentials here.

Handlebars works like many other template languages - a template is provided a data model
and uses a special tag syntax to denote dynamic elements, referred to as a "helper" in this case.

Helpers are always delimited by double or triple curly braces (`{` and `}`). In the simplest case a helper can
simply output the value of a variable in the model:

```handlebars  theme={null}
{{myVariable}}        // Top-level model variable
{{outerVar.innerVar}} // Nested model variable
```

### Helper parameters

Helpers can take both positional and named parameters. In both cases they are delimited by spaces.

The following helper takes three positional parameters -
the string in which the replacement should take place, the substring to find and the
replacement value:

```handlebars  theme={null}
{{replace myString 'foo' 'bar'}}
```

Named values are of the form `name=value`. The following helper has a single
positional parameter followed by a parameter named `format`:

```handlebars  theme={null}
{{dateFormat myDate format='yyyy-MM-dd'}}
```

### Nesting helpers

Sometimes it's necessary to apply a helper to the result of another one. This can
be achieved by nesting helpers using bracket syntax. For example, this template
will truncate the input string, then capitalise the first letter:

```handlebars  theme={null}
{{capitalize (substring myString 0 4)}}
```

### Blocks

Blocks can be used to apply processing to an inner piece of content.

```handlebars  theme={null}
{{#if productExists}}
  // do something with the product
{{else}}
  // product not found
{{/if}}
```

Blocks form the foundation of logical and looping structures in Handlebars and are [described here in more detail](/response-templating/conditional-logic-and-iteration/).

### HTML escaping

We mentioned earlier that double or triple curly braces are used to delimit helpers.
The difference between these two forms is that with double braces, Handlebars will
automatically HTML escape the output of the helper, whereas with triple braces no escaping will be
applied.

For instance, suppose we have a data model where the variable `tag` has the value `<html>`.

The template

```handlebars  theme={null}
{{tag}}
```

will output

```
&lt;html&gt;
```

whereas the template

```handlebars  theme={null}
{{{tag}}}
```

will output

```
<html>
```

## The request model

When templates are evaluated, they have access to a data model containing information about the incoming request. For a complete reference of all available request attributes and how to access them, see the [Request Model Reference](/response-templating/request-model).

## Handlebars helpers

WireMock Cloud provides a set of Handlebars helpers that perform a variety of logical functions and transformations inside templates. These include all of the standard helpers from the [Java Handlebars implementation by jknack](https://github.com/jknack/handlebars.java).

All of the available helpers are described in detail in these articles:

* [Conditional Logic and Iteration](./conditional-logic-and-iteration/)
* [Strings](./string-helpers/)
* [String Encodings](./string-encodings/)
* [Dates & Times](./dates-and-times/)
* [Random Values](./random-values/)
* [Random Faker](./random-faker/)
* [XML](./xml/)
* [JSON](./json/)
* [JSON Web Tokens](./jwt/)
* [Miscellaneous Helpers](./misc-helpers/)

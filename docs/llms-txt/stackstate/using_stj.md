# Source: https://archivedocs.stackstate.com/5.1/develop/reference/stj/using_stj.md

# Using STJ

## Overview

StackState's graph is entirely configured using JSON. To make it easy to work with large quantities of (often repetitive) JSON, StackState comes with the StackState Template JSON format (STJ).

STJ is based on [handlebars (handlebarsjs.com)](https://handlebarsjs.com/) and comes with a number of [StackState functions](https://archivedocs.stackstate.com/5.1/develop/reference/stj/stj_reference).

## Handlebars syntax

StackState template files use handlebars. Content that is placed between double curly brackets `{{ some content }}` is included in the output. The example below shows handlebars used in a component template:

{% code lineNumbers="true" %}

```
[{
  "_type": "Component",
  "checks": [],
  "streams": [],
  "labels": [],
  "name": "{{ name }}",
  "description": "{{ description }}",
  "type" : {{ componentTypeId }},
  "layer": {{ layerId }},
  "domain": {{ domainId }},
  "environments": [{{ environmentId }}]
}]
```

{% endcode %}

### Conditionals: #if / else

Run some template code conditionally if a variable has a value.

{% tabs %}
{% tab title="Template" %}

```
{{# if description }}
"description": "{{ description }}",
{{else}}
"description": "noop",
{{/ if }}
```

{% endtab %}

{% tab title="Data" %}

```
[ description: "hello world" ]
```

{% endtab %}

{% tab title="Result" %}

```
"description": "hello world"
```

{% endtab %}
{% endtabs %}

### Looping: #each

Loop over an array or map of data.

{% tabs %}
{% tab title="Template" %}

```
[
  {{# each names }}
  "hello {{this}}",
  {{/ each }}
  "bye y'all!"
]
```

{% endtab %}

{% tab title="Data" %}

```
[ names: [ "stackstate", "handlebars" ]]
```

{% endtab %}

{% tab title="Result" %}

```
[
  "hello stackstate",
  "hello handlebars",
  "bye y'all!"
]
```

{% endtab %}
{% endtabs %}

## StackState handlebars functions

StackState adds a number of function to the handlebars syntax. You can use these to create complex JSON results.

➡️ [Learn more about the available handlebars functions](https://archivedocs.stackstate.com/5.1/develop/reference/stj/stj_reference)

## Component and relation templates

Templates are used to create topology.

➡️ [Learn more about component and relation templates](https://archivedocs.stackstate.com/5.1/configure/topology/sync#template-functions)

## See also

* [StackState Template Language Functions](https://archivedocs.stackstate.com/5.1/develop/reference/stj/stj_reference)

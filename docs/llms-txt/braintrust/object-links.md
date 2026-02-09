# Source: https://braintrust.dev/docs/reference/object-links.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Share via URL

Braintrust supports a convenient method for generating permanent links (permalinks) to experiment and dataset objects in your workspace by using their unique object IDs. This allows you to share, bookmark, or automate navigation to specific resources.

When you access a URL in this format, Braintrust automatically redirects you to the canonical page for the object, regardless of its organization or project.

```
https://www.braintrust.dev/app/braintrustdata.com/object?object_type=<object_type>&object_id=<object_id>
```

* **object\_type**: The type of object (`experiment` or `dataset`).
* **object\_id**: The unique identifier for the object.

For example, if you have an experiment with the ID `dc877d29-fc32-438f-bd62-169967c817f0`, use:

```
https://www.braintrust.dev/app/braintrustdata.com/object?object_type=experiment&object_id=dc877d29-fc32-438f-bd62-169967c817f0
```

### Redirection behavior

When you visit the above URL, you are automatically redirected to the standard page for the object, following the canonical URL structure for that object type.

```
https://www.braintrust.dev/app/<your org>/p/<your project>/<object_collection>/<object_slug>
```

For the experiment example above, the redirect might look like:

```
https://www.braintrust.dev/app/braintrustdata.com/p/pedro-project1/experiments/dc877d29-fc32-438f-bd62-169967c817f0
```

### Supported object types

This method works for any object type that has a unique ID. Set the `object_type` parameter to one of the supported types:

* `experiment`
* `dataset`

## Generate links via SDK

The SDK also supports methods for generating permalinks in both [TypeScript](/reference/sdks/typescript) and [Python](/reference/sdks/python).

## Use cases

You can use object permalinks to:

* Bookmark important experiments or datasets
* Automate navigation in documentation or scripts
* Share direct links with collaborators

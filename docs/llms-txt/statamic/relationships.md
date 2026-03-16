# Source: https://statamic.dev/content-modeling/relationships.md

# Relationships

Content is often related to other content and bits of data. A blog post may have an author and 3 other recommended posts. A product may have a brand and a category. A hot dog may have a bun and some mustard. This page covers ways to create and take advantage of these types of relationships.

## Overview

Statamic relationships are defined by storing an `id` or `handle` of one piece of content (an entry, term, or user for example) in a variable on another piece of content. Once linked in this simple-but-specific manner, you can fetch and display the related content by using the variable in your templates.

## Fieldtypes

There are 13 fieldtypes that manage relationships in one fashion or another. When you use these fieldtypes in your [blueprint](/blueprints.md), the relationships are automatically resolved on the front-end of your site and you can work directly with the data it references.

- [Assets](/fieldtypes/assets.md)
- [Collections](/fieldtypes/collections.md)
- [Entries](/fieldtypes/entries.md)
- [Form](/fieldtypes/form.md)
- [Link](/fieldtypes/link.md)
- [Navs](/fieldtypes/navs.md)
- [Sites](/fieldtypes/sites.md)
- [Structures](/fieldtypes/structures.md)
- [Taxonomies](/fieldtypes/taxonomies.md)
- [Taxonomy Terms](/fieldtypes/terms.md)
- [User Groups](/fieldtypes/user-groups.md)
- [User Roles](/fieldtypes/user-roles.md)
- [Users](/fieldtypes/users.md)


## Example

Let's use this example product entry to walk through displaying data from the three relationships: photo, author, and related products.

``` yaml
# /content/products/wayne-gretzky-pog-collection.md
title: Wayne Gretzky Pog Collection
price: 2495.00
template: products.show
id: 123-1234-12-4321
photo: products/gretzky-pogs-FINAL-(2).jpg
author: abc-abcd-ab-dcba
related_products:
  - 789-7890-78-0987
  - abc-1234-bc-4eba
```

### Field breakdown
- `id` is the unique identifier given to this particular entry
- `photo` is a reference to an asset image of the product (why didn't they clean up the filename?)
- `author` is the id of the user who created this entry
- `related_products` is an array of other product entry ids

### Templating

In this following template example you can see how easy it is to use the data from related entries, assets, and users. You don't need to write queries, request data filter results, or anything complicated. As long as you've used the appropriate [fieldtypes](#fieldtypes.md) in your [blueprint](/blueprints.md), the data will be ready and waiting for you to use in your view template.

::tabs

::tab antlers
```antlers
<!-- resources/views/products/show.antlers.html -->

<div class="product">
  <div class="flex justify-between">
    <h1>{{ title }}</h1>
    <h2 class="text-green">${{ price }}</h2>
  </div>
  <img src="{{ photo:url }}" alt="{{ alt }}">
  <p>Listed by: {{ author:name }}</p>
</div>

<div class="mt-8">
  <h3>Related Products</h3>
  <div class="flex flex-wrap -mx-2">
    {{ related_products }}
    <div class="w-1/2 p-4 border m-2">
      <div class="font-bold">{{ title }}</div>
      <div class="text-green">{{ price }}</div>
      <img src="{{ photo }}" alt="{{ alt }}">
    </div>
    {{ /related_products }}
  </div>
</div>
```
::tab blade
```blade
<!-- resources/views/products/show.blade.php -->

<div class="product">
  <div class="flex justify-between">
    <h1>{{ $title }}</h1>
    <h2 class="text-green">${{ $price }}</h2>
  </div>
  <img src="{{ $photo->url }}" alt="{{ $photo->alt }}">
  <p>Listed by: {{ $author->name }}</p>
</div>

<div class="mt-8">
  <h3>Related Products</h3>
  <div class="flex flex-wrap -mx-2">
    @foreach ($related_products as $product)
    <div class="w-1/2 p-4 border m-2">
      <div class="font-bold">{{ $product->title }}</div>
      <div class="text-green">{{ $product->price }}</div>
      <img src="{{ $product->photo->url }}" alt="{{ $product->photo->alt }}">
    </div>
    @endforeach
  </div>
</div>
```
::

## Manual fetching

If you _aren't_ using a relationship fieldtype but _do_ have an `id` or `handle` to fetch data from you can use the [get_content tag](/tags/get_content.md).

::tabs

::tab antlers
```antlers
<!-- You can hardcode the ID -->
{{ get_content from="123-1234-12-4321" }}
  <a href="{{ url }}">{{ title }}</a>
{{ /get_content }}

<!-- Or pass the variable holding it -->
{{ get_content :from="related_id" }}
  <a href="{{ url }}">{{ title }}</a>
{{ /get_content }}
```
::tab blade
```blade
<!-- You can hardcode the ID -->
<s:get_content from="123-1234-12-4321">
  <a href="{{ $url }}">{{ $title }}</a>
</s:get_content>

<!-- Or pass the variable holding it -->
<s:get_content :from="related_id">
  <a href="{{ $url }}">{{ $title }}</a>
</s:get_content>
```
::

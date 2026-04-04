# Source: https://docs.xano.com/xano-features/metadata-api/search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

This section is broken down into Browse Content and Search. [Browse Content](/xano-features/metadata-api/search#browse-content) is a simple method of getting or reading the content of a database table. It can be optionally combined with paging.

[Search](/xano-features/metadata-api/search#search) is an advanced method of filtering, sorting, and paging database content. It is flexible and powerful and enables you to return content based on the parameters you define.

<Info>
  Please note that the Metadata APIs for browsing content do not react to API Access settings. All fields will be returned regardless of this setting.
</Info>

## Browse Content

Browse table content is a simple method of getting content (database records) in a database table. It requires a workspace ID and table ID, while paging is optional.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b2bed4f6-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=4e100c9d7bc0824b4df6fc2b4a4afd59" width="2304" height="1108" data-path="images/b2bed4f6-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "round ball to shoot hoops",
      "category_id": 1
    },
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2
    },
    {
      "id": 3,
      "created_at": 1681336868658,
      "name": "Bluetooth Speaker",
      "description": "Portable music player",
      "category_id": 3
    },
    {
      "id": 4,
      "created_at": 1681336868931,
      "name": "Camera",
      "description": "Take photos with this",
      "category_id": 3
    }
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}
```

## Search

Search via the Metadata API is powerful and flexible to return the exact database content you are searching for.

#### Search where ID = 10

In this example, we will search the Items table where ID = 10

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d579df83-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=4a040c39e61af61babc1d2b495b7a13c" width="2304" height="1122" data-path="images/d579df83-image.jpeg" />
</Frame>

<Info>
  Search can be done as a single object or array if there is only one search parameter. If there are multiple parameters then it must be an array.

  You can pass just what you want in the request body. For example, if all we want to do is search then we just need to pass search to the body.
</Info>

With paging, sort, and search as an array.

```json  theme={null}
{
  "page": 1,
  "per_page": 50,
  "sort": {
    "id": "desc"
  },
  "search": [{
   "id": 10
}]
}
```

With paging, sort, and search as a single object.

```json  theme={null}
{
  "page": 1,
  "per_page": 50,
  "sort": {
    "id": "desc"
  },
  "search": {
   "id": 10
}
}
```

With just search, as an array.

```json  theme={null}
{
  "search": [{
   "id": 10
}]
}
```

With just search, as a single object.

```json  theme={null}
{
  "search": {
   "id": 10
}
}
```

For this example, all of the above are acceptable for the request body.

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 10,
      "created_at": 1681346185431,
      "name": "Air Fryer",
      "description": "A new way to fry food without all the grease and oil",
      "category_id": 2,
      "price": 75
    }
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 1,
  "pageTotal": 1
}
```

#### Search where Price > 30 and Price \< 70

In this example, we are searching for content where price is > 30 and price is \< 70.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/476525f1-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=e16be6e228a62f0a2330fc68cca0e27a" width="2304" height="1089" data-path="images/476525f1-image.jpeg" />
</Frame>

Example request body:

```json  theme={null}
{
  "search": [{
   "price|>": 30
},
{
   "price|<": 70
}]
}
```

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 5,
      "created_at": 1681346183608,
      "name": "Microwave",
      "description": "Reheat leftovers quickly",
      "category_id": 2,
      "price": 40
    },
    {
      "id": 8,
      "created_at": 1681346184305,
      "name": "Blender",
      "description": "Make smoothies and more",
      "category_id": 2,
      "price": 65
    },
    {
      "id": 9,
      "created_at": 1681346184508,
      "name": "Running Shoes",
      "description": "Comfy footwear for long runs",
      "category_id": 1,
      "price": 45
    }
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}
```

#### Search where Price \< 30 or Price > 70

In this example, we will search for where the price is \< 30 or the price is > 70

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/bb32e78c-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=b4f68038bba0bd767f00b92f089c4c88" width="2304" height="1137" data-path="images/bb32e78c-image.jpeg" />
</Frame>

Example request body:

```json  theme={null}
{
  "search": [
{
   "price|<": 30
},
{
   "price|>|or": 70
}
]
}
```

<Info>
  Notice how the or is formatted after the Price is > 70 expression.
</Info>

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "round ball to shoot hoops",
      "category_id": 1,
      "price": 10
    },
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2,
      "price": 5
    },
    {
      "id": 4,
      "created_at": 1681336868931,
      "name": "Camera",
      "description": "Take photos with this",
      "category_id": 3,
      "price": 80
    },
    {
      "id": 6,
      "created_at": 1681346183823,
      "name": "Resistance Bands",
      "description": "Stretchy bands for working out",
      "category_id": 1,
      "price": 15
    },
    {
      "id": 7,
      "created_at": 1681346184107,
      "name": "Tablet",
      "description": "Browse, stream, and more with a portable tablet",
      "category_id": 3,
      "price": 120
    },
    {
      "id": 10,
      "created_at": 1681346185431,
      "name": "Air Fryer",
      "description": "A new way to fry food without all the grease and oil",
      "category_id": 2,
      "price": 75
    }
  ],
  "itemsReceived": 6,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 6,
  "pageTotal": 1
}
```

#### In and Not In

The IN and NOT IN operators are great for working with lists and can also be thought of as another version of "or" operators. In the first example, we will search where the ID is IN \[2,3,7].

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8f5a4254-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=edcbdc65df614a335b7069e4b7f6f8c7" width="2304" height="1082" data-path="images/8f5a4254-image.jpeg" />
</Frame>

Example request body:

```json  theme={null}
{

  "search": {
  "id|in": [2,3,7]
}
}
```

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2,
      "price": 5
    },
    {
      "id": 3,
      "created_at": 1681336868658,
      "name": "Bluetooth Speaker",
      "description": "Portable music player",
      "category_id": 3,
      "price": 30
    },
    {
      "id": 7,
      "created_at": 1681346184107,
      "name": "Tablet",
      "description": "Browse, stream, and more with a portable tablet",
      "category_id": 3,
      "price": 120
    }
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}
```

In the second example, we will search where ID is NOT IN \[1,2,3,4,6,7,8,9]

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/292bef33-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=40d980c89b51d7cd186d89f27d0b0a7c" width="2304" height="1065" data-path="images/292bef33-image.jpeg" />
</Frame>

Example request body:

```json  theme={null}
{

  "search": {
  "id|not in": [1,2,3,4,6,7,8,9]
}
}
```

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 5,
      "created_at": 1681346183608,
      "name": "Microwave",
      "description": "Reheat leftovers quickly",
      "category_id": 2,
      "price": 40
    },
    {
      "id": 10,
      "created_at": 1681346185431,
      "name": "Air Fryer",
      "description": "A new way to fry food without all the grease and oil",
      "category_id": 2,
      "price": 75
    }
  ],
  "itemsReceived": 2,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 2,
  "pageTotal": 1
}
```

### Sort

Sort is flexible, like search, in the sense that it accepts a single object or an array for a single sort parameter. It also supports multiple sorts, which require an array format.

#### Single Sort

In this example, we will sort the category table by the name in ascending order.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8e2e447c-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=f3b28ae14f18af05179532d2877e154f" width="2304" height="1062" data-path="images/8e2e447c-image.jpeg" />
</Frame>

Example request body:

```json  theme={null}
{

  "sort": {
    "name": "asc"
  }
}
```

Also acceptable:

```json  theme={null}
{

  "sort": [{
    "name": "asc"
  }]
}
```

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 5,
      "created_at": 1681350452709,
      "name": "Decor",
      "rating": 3
    },
    {
      "id": 3,
      "created_at": 1681337773911,
      "name": "Electronics",
      "rating": 5
    },
    {
      "id": 2,
      "created_at": 1681337772998,
      "name": "Kitchen",
      "rating": 4
    },
    {
      "id": 4,
      "created_at": 1681350451208,
      "name": "Outdoor",
      "rating": 4
    },
    {
      "id": 1,
      "created_at": 1681337772458,
      "name": "Sports equipment",
      "rating": 4
    }
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}
```

#### Multi-Sort

In this example, we will first sort the content by rating in descending order, then the name in ascending order.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4eace699-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=042e128d3b532f30f1366906eb81a9c6" width="2304" height="1137" data-path="images/4eace699-image.jpeg" />
</Frame>

Example request body:

```json  theme={null}
{

  "sort": [{
    "rating": "desc"
  },
  {
    "name": "asc"
  }
]
}
```

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 3,
      "created_at": 1681337773911,
      "name": "Electronics",
      "rating": 5
    },
    {
      "id": 2,
      "created_at": 1681337772998,
      "name": "Kitchen",
      "rating": 4
    },
    {
      "id": 4,
      "created_at": 1681350451208,
      "name": "Outdoor",
      "rating": 4
    },
    {
      "id": 1,
      "created_at": 1681337772458,
      "name": "Sports equipment",
      "rating": 4
    },
    {
      "id": 5,
      "created_at": 1681350452709,
      "name": "Decor",
      "rating": 3
    }
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}
```


Built with [Mintlify](https://mintlify.com).
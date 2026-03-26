# Source: https://www.cosmicjs.com/docs/api/queries.md

# Queries

Learn about queries; the way to fetch content from your Cosmic Bucket.

### Prerequisite

The following references assume you have already reviewed the methods for fetching [Objects](/docs/api/objects) and [media](/docs/api/media) from your Bucket.

### Queries in the browser URL

If accessing the endpoint via browser address bar, open and closed curly
braces will need to be encoded: `%7B` and `%7D` respectively. [This encoder
tool may help](https://meyerweb.com/eric/tools/dencoder/).

## Object properties

You can compose queries to search by the following Object properties.

| Parameter       | Description                |
| :-------------- | :------------------------- |
| `id`            | Object id                  |
| `title`         | Object title               |
| `slug`          | Object slug                |
| `type`          | Object type Slug           |
| `locale`        | Object locale              |
| `created_at`    | Object created at date     |
| `published_at`  | Object published at date   |
| `modified_at`   | Object modified at date    |
| `created_by`    | Object created by user id  |
| `modified_by`   | Object modified by user id |
| `metadata.$key` | Metadata value(s)          |

## Media properties

Construct queries to search by the following media properties.

| Parameter       | Description           |
| :-------------- | :-------------------- |
| `id`            | Media id              |
| `name`          | Media name            |
| `original_name` | Media original name   |
| `size`          | Media size            |
| `type`          | Media type            |
| `created`       | Media created date    |
| `folder`        | Media folder          |
| `metadata`      | Media metadata (JSON) |

## Selectors

Use the following selectors to build your queries.

| Parameter | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| `$eq`     | Matches values that are equal to a specified value. Default key/value query. |
| `$gt`     | Matches values that are greater than a specified value.                      |
| `$gte`    | Matches values that are greater than or equal to a specified value.          |
| `$lt`     | Matches values that are less than a specified value.                         |
| `$lte`    | Matches values that are less than or equal to a specified value.             |
| `$in`     | Matches **any** of the values specified in an array.                         |
| `$all`    | Matches **all** of the values specified in an array.                         |
| `$ne`     | Matches all values that are not equal to a specified value.                  |
| `$nin`    | Matches none of the values specified in an array.                            |

## Evaluation

| Parameter            | Description                                                          |
| -------------------- | -------------------------------------------------------------------- |
| `$regex`, `$options` | Search for string, use `$options: "i"` for case insensitive matches. |

## Logic Operators

| Parameter | Description                                                         |
| --------- | ------------------------------------------------------------------- |
| `$and`    | Returns results that match all of the query conditions.             |
| `$not`    | Returns results that do not match the query expression.             |
| `$or`     | Returns results that match any of the specified conditions.         |
| `$nor`    | Returns results that fail to match any of the specified conditions. |

## Basic examples

The following examples use the NPM module and assume you have an understaning of [authentication](/docs/api/authentication).

A basic query may be when you want to fetch Objects in a certain type. For example, blog posts:
```js
const query = {
  type: 'posts',
};
await cosmic.objects.find(query);

```
You can also use queries to fetch media.
```js
const query = {
  type: 'video/mp4', // fetch all video files
};
await cosmic.media.find(query);

```
## Advanced examples

Let's say you want to fetch only blog posts with a certain text metafield by a key and value:
```js
const query = {
  type: 'posts',
  'metadata.some_unique_key': 'some-unique-value',
};
await cosmic.objects.find(query);

```
Let's say you want to fetch only blog posts from a certain category set by a single Object relationship metafield:
```js
const query = {
  type: 'posts',
  'metadata.category': 'category-object-id', // The category Object id
};
await cosmic.objects.find(query);

```
When querying using an Object Metafield, make sure you query by the Object
`id` not the `slug`.

Let's say you want to fetch products that have a `price` (Number Metafield) less than `100`:
```js
const query = {
  type: 'products',
  'metadata.price': {
    $lt: 100,
  },
};
await cosmic.objects.find(query);

```
Let's say you want to fetch products that have any of a certain set of `tags` (select dropdown Metafield):
```js
const query = {
  type: 'products',
  'metadata.tags': {
    $in: ['Clothing', 'Menswear'],
  },
};
await cosmic.objects.find(query);

```
Let's say you want to fetch products that match a combination of values using the `$and` logic operator.
```js
const query = {
  type: 'products',
  $and: [
    {
      'metadata.category': 'Tshirt',
    },
    {
      'metadata.price': {
        $lte: 29,
      },
    },
  ],
};
await cosmic.objects.find(query);

```
Using the `$regex` method we can create a search feature that searches Objects by `title`.
```js
const query = {
  type: 'products',
  title: {
    $regex: 'Hoodie',
    $options: 'i', // case insensitive
  },
};
await cosmic.objects.find(query);

```
### More query info

**Want more information?** Cosmic queries follow MongoDB methods of comparison
and logical operators. See further documentation and more examples in the
[MongoDB
docs](https://docs.mongodb.com/manual/reference/operator/query/index.html).
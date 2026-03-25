# Source: https://developers-classic.mailerlite.com/docs/parameters.md

# Using parameters

[block:api-header]
{
  "type": "basic",
  "title": "Limit & Offset"
}
[/block]

You can provide `limit` and `offset` parameters chaining corresponding methods to your API query. These methods are useful if you want to use pagination.

> `limit(int $limit)`
> `offset(int $offset)`

[block:code]
{
  "codes": [
    {
      "code": "<?php\n\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$items = $groupsApi->limit(10)->get(); // the first ten items (page one)\n$items = $groupsApi->limit(10)->offset(10)->get(); // page two\n$items = $groupsApi->limit(10)->offset(20)->get(); // page three\n",
      "language": "php"
    }
  ]
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Order by"
}
[/block]

You can order data by selected column using this method:

> `orderBy(string $column, string $order)`

[block:code]
{
  "codes": [
    {
      "code": "<?php\n\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$items = $groupsApi->orderBy('name', 'DESC')->get(); // order by name descending\n$items = $groupsApi->orderBy('name', 'ASC')->get(); // order by name ascending",
      "language": "php"
    }
  ]
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Where"
}
[/block]

Also, you can find items using criteria by any other field value using where method.

> `where(array $filters)`

When you want to get items by exact value of field, `$filters` are should look like this:

```
$filters = ['column_title' => $value];
```

[block:code]
{
  "codes": [
    {
      "code": "<?php\n\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$items = $groupsApi->where(['date_created' => '2016-01-01'])->get(); // get groups which have 4 active subscribers",
      "language": "text"
    }
  ]
}
[/block]

## Operators

There is an ability to use operators when you want to get items:

* `$gt` (greater than)
* `$gte` (greater than or equal)
* `$lt` (less than)
* `$lte` (less than or equal)
* `$ne` (not equal)
* `$like` (like)

In that case, `$filters` array should look like this:

```
$filters = [
  'column_title' => [
    'operator' => $value
  ]
];
```

[block:code]
{
  "codes": [
    {
      "code": "<?php\n\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$items = $groupsApi->where([\n  \t'active' => [\n    \t'$gte' => 4\n    ]\n  ])->get(); // get groups which have 4 or more active subscribers",
      "language": "php"
    }
  ]
}
[/block]
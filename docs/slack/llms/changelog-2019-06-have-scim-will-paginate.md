Source: https://docs.slack.dev/changelog/2019-06-have-scim-will-paginate

# Have SCIM, will paginate

June 1, 2019

We're modernizing the [GET /Users](/reference/scim-api#get_users) and [GET /Groups](/reference/scim-api#get_groups) methods of our [SCIM user management API](/admins/scim-api) by putting a more reasonable upper bound on results served per page.

The [SCIM spec](http://www.simplecloud.info/specs/draft-scim-api-01.html#query-resources) allows for pagination and these methods have long supported it, but we've accepted higher `count` values in the past.

The changes described below are effective July 8th, 2019 **August 30th, 2019**.

## What's changing? {#what}

The `count` parameter in [GET /Users](/reference/scim-api#get_users) and [GET /Groups](/reference/scim-api#get_groups) will no longer accept values greater than `1000`.

HTTP requests with `count` parameter values of `1001` and above will automatically be evaluated as if `1000` were provided and only the first 1,000 results will be returned. The remainder can be fetched by adjusting the `startIndex` parameter.

## What isn't changing? {#not_changing}

The default page size remains `10` results when no `count` parameter is presented.

No other methods have changed.

## How do I prepare? {#how}

If you don't use the SCIM API or don't use these two data retrieval methods, there's no action needed, regardless of workspace size.

If you use the SCIM API and provide `count` values greater than `1000` to these two SCIM methods, you'll need to paginate through the lists provided by GET /Users and GET /Groups using both the `count` and `startIndex` parameters.

### Example adaptation {#example}

You currently use a `count` value of `100000` (_one hundred thousand_) to retrieve all possible provisioned Users by making a HTTP call like the following.

```text
GET /scim/v1/Users?count=100000
```text

Instead of receiving all possible results in a single API call, you must now break your calls up into groups of `count` values set to `1000` or less. In your very first request you can find out how large the result set is.

```text
GET /scim/v1/Users?count=1000
```text

In response you receive the first 1,000 results, including a top-level `totalResults` field. If this number is less than `1000`, you don't need to perform any other requests. If it's greater than `1000`, then you'll need to set `startIndex` to the _nth_ result, or the numbered result you're looking for just after the last one you collected.

When working with a pagesize of `1000`, your second request will always begin with a `startIndex` of `1001`. If there were `1000` more after that, you'd next ask for `2001`.

Assuming there were 2,225 results to retrieve, your sequence of requests may look like:

```text
GET /scim/v1/Users?count=1000GET /scim/v1/Users?count=1000&startIndex=1001GET /scim/v1/Users?count=1000&startindex=2001
```text

Stop issuing paginated requests when you've collected an equal number of results to the `totalResults` field found in each response. In this example, the third request would have included the final 223 results.

If you require an exact set of current users, avoid using this paginated API call while the current roster of users in your organization is changing.

## When is this happening? {#when}

This change to `count` parameters in the SCIM API takes effect on July 8th, 2019 **August 30, 2019**.

We don't anticipate this change to negatively effect a large number of workspaces or applications. [Talk to us](https://slack.com/help/requests/new) if you have concerns or questions.

## Tags:

* [New feature](/changelog/tags/new-feature)
* [Breaking change](/changelog/tags/breaking-change)

# Source: https://docs.xano.com/troubleshooting-and-support/troubleshooting-performance/function-stack-performance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Function Stack Performance

Xano does a lot of work behind the scenes to ensure your API response time is as fast as possible. That said, there are best practices that should be followed when you're building your API endpoints to avoid slowing down your server.

## What is "good" performance?

The performance of your API endpoint depends on a number of different variables which include:

* The complexity of your function stack and the number of statements that execute

* How much data is being processed

* How your Database is set up/indexed (if you're querying the Database)

* Server location and resources

**Examples below are using a Xano paid plan (Dedicated resources) with a local server:**

<Warning>
  The below response times will change depending on your Xano plan and load on your Xano Instance.
</Warning>

| Task                                               | Statements | Median Response  |
| -------------------------------------------------- | ---------- | ---------------- |
| Get 100 Records                                    | 1          | **\< 1 second**  |
| Filter 100,000 records by one field                | 1          | **\< 1 second**  |
| Bulk Add 10k records                               | 1          | **\< 1 second**  |
| Transform 100k records (Change field to uppercase) | 3          | **\< 1 second**  |
| Bulk Delete (Recursive)                            | 502        | **\< 5 seconds** |

*\*\< 1 second = under 1 second*

*\*\*The results are the median response times between Launch, Scale, and Scale-2x.*

## How to improve your API response times

1. **Get a dedicated instance in a region that's closest to your customers**<br />The Free plan is on a shared resource. When you upgrade, each paid Xano instance is on dedicated resources and allows you to deploy in the region of your choice. The closer the server is to your users, the faster the response time will be. Xano uses Google Cloud under the hood so if you don't see a region that is listed on their [supported regions page](https://cloud.google.com/about/locations), please contact support. If there is enough demand, we will open a new region.

2. **Optimize Database Performance**<br />There are many ways to set up the Database for your application. Unfortunately, there are inefficient ways to set this up that can slow your app down. You'll have to go through a few iterations to find the most efficient way for your use case.

3. **Simplify your Function Stack**<br />This may seem obvious, but producing a response in ten (10) functions is slower than doing it in three (3). It's also important to remember that the number of functions in the function stack could be different than the statements that get executed (for example, if you have a loop).

4. [**Use Addons when requesting related data**](/the-function-stack/functions/database-requests/query-all-records#using-addons)<br />Addons are Xano's way of enriching the response of a Database query without a heavy volume of requests. As a simple example, let's say you want to get 100 unique books and their associated 100 unique authors. Normally that would be 101 requests (1 request for all books, and a request to retrieve each author). With the magic of Addons, it's only 2 requests (1 to get the books, 1 to enrich the authors).

5. [**Use Data Caching**](/the-function-stack/additional-features/response-caching)<br />When working with large datasets or external API endpoints that have a rate limit/cost associated with them. (request caching, function caching, redis caching).

6. [**Use the Stream return type**](/the-function-stack/functions/database-requests/query-all-records#output)<br />when looping through large sets of data. This will retrieve your records in a memory-efficient way.


Built with [Mintlify](https://mintlify.com).
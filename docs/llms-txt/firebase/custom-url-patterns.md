# Source: https://firebase.google.com/docs/perf-mon/custom-url-patterns.md.txt

<br />

Firebase Performance Monitoringautomatically aggregates data for similar network requests to help you understand trends in your network request performance.

Sometimes, though, you need to customize how Firebase aggregates specific network request data to better support your app's use cases. We provide two ways that you customize data aggregation for network requests:[aggregate data under custom URL patterns](https://firebase.google.com/docs/perf-mon/custom-url-patterns#custom-url-patterns)and[customize how success rate is calculated](https://firebase.google.com/docs/perf-mon/custom-url-patterns#customize-success-rate-calculation).

## Aggregate data under custom URL patterns

For each request, Firebase checks if the network request's URL matches a[URL pattern](https://firebase.google.com/docs/perf-mon/network-traces#url-patterns). If the request URL matches a URL pattern, Firebase automatically aggregates the request's data under the URL pattern.

You can create***custom URL patterns*** to monitor specific URL patterns that Firebase isn't capturing with its derived[automatic URL pattern matching](https://firebase.google.com/docs/perf-mon/network-traces#automatic-url-patterns). For example, you can use a custom URL pattern to troubleshoot a specific URL or to monitor a specific set of URLs over time.

Firebase displays all URL patterns (including custom URL patterns) and their aggregated data in the*Network requests* subtab of the traces table, which is at the bottom of the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole.

### How does custom URL pattern matching work?

Firebase attempts to match request URLs to any configured custom URL patterns before falling back to automatic URL pattern matching. For any matching requests to a custom URL pattern, Firebase aggregates the requests' data under the custom URL pattern.

If a request's URL matches more than one custom URL pattern, Firebase maps the request to the*most specific* custom URL pattern only, according to the following specificity order:**plain text \>`*`\>`**`*from left to right in the path*** . For example, a request to`example.com/books/dog`matches two custom URL patterns:

- `example.com/books/*`
- `example.com/*/dog`

However, the pattern`example.com/books/*`is the*most specific* matching URL pattern because the leftmost segment`books`in`example.com/books/*`takes precedence over the leftmost segment`*`in`example.com/*/dog`.

When you create a new custom URL pattern, be aware of the following:

- Matches and aggregated data from*previous*requests aren't affected by creating a new custom URL pattern. Firebase does not retroactively re-aggregate request data.

- Only*future* requests are affected by creating a new custom URL pattern. You might need to wait up to 12 hours forPerformance Monitoringto collect and aggregate data under a new custom URL pattern.

### Create a custom URL pattern

You can create a custom URL pattern from the*Network requests* subtab in the traces table, which is at the bottom of the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole.

A project member must be an[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic)to create a new custom URL pattern; however, all project members can view custom URL patterns and their aggregated data.

You can create up to 400 total custom URL patterns per app and up to 100 custom URL patterns per domain for that app.

To create a custom URL pattern, start with a hostname, followed by path segments. The hostname must include a valid domain, and can optionally include the subdomain. Use the following path segment syntax to create a pattern that can match URLs.

- plain text --- matches an exact string
- `*`--- matches the first subdomain segment, or any string in a single path segment
- `**`--- matches an arbitrary path suffix

The following table describes some potential custom URL pattern matching.

|          **To match...**          | **Create a custom URL pattern like...** |                                        **Example matches to this URL pattern**                                        |
|-----------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| An exact URL                      | `example.com/foo/baz`                   | `example.com/foo/baz`                                                                                                 |
| Any single path segment (`*`)     | `example.com/*/baz`                     | `example.com/foo/baz` `example.com/bar/baz`                                                                           |
| Any single path segment (`*`)     | `example.com/*/*/baz`                   | `example.com/foo/bar/baz` `example.com/bah/qux/baz`                                                                   |
| Any single path segment (`*`)     | `example.com/foo/*`                     | `example.com/foo/baz` `example.com/foo/bar` **Note:** This pattern will not match`example.com/foo`.                   |
| An arbitrary path suffix (`**`)   | `example.com/foo/**`                    | `example.com/foo` `example.com/foo/baz` `example.com/foo/baz/more/segments`                                           |
| An arbitrary path suffix (`**`)   | `subdomain.example.com/foo.bar/**`      | `subdomain.example.com/foo.bar` `subdomain.example.com/foo.bar/baz` `subdomain.example.com/foo.bar/baz/more/segments` |
| The first subdomain segment (`*`) | `*.example.com/foo`                     | `bar.example.com/foo` `baz.example.com/foo`                                                                           |

| **Note:** For custom URL patterns, Firebase does not support the syntax of`*.`<var translate="no">file-extension</var>, like`*.png`or`*.css`.

### View custom URL patterns and their data

Firebase displays all URL patterns (including custom URL patterns) and their aggregated data in the*Network requests* subtab of the traces table, which is at the bottom of the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole.

To view*only* custom URL patterns, select*Custom patterns* from the dropdown menu in the*Network requests*subtab of the traces table. Note that if a custom URL pattern doesn't have any aggregated data, then it only appears in this list.

When the[data retention period](https://firebase.google.com/support/privacy#data_processing_information)ends for the data aggregated under a URL pattern, Firebase deletes that data from the URL pattern. If all the data aggregated under a custom URL pattern expires, then Firebase does*not* delete the custom URL pattern from theFirebaseconsole. Instead, Firebase continues to list "empty" custom URL patterns in the*Custom patterns* list of the*Network requests*subtab of the traces table.

### Remove a custom URL pattern

You can remove custom URL patterns from your project. Note that you cannot remove an automatic URL pattern.

1. From the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance), scroll down to the traces table, then select the*Network requests*subtab.

2. Select*Custom patterns* from the dropdown menu in the*Network requests*subtab.

3. Hover over the row of the custom URL pattern that you want to remove.

4. Clickmore_vertat the far right of the row, select*Remove custom pattern*, then confirm the removal in the dialog.

When you remove a custom URL pattern, be aware of the following:

- Any*future* requests are mapped to the*next most specific* matching custom URL pattern. If Firebase finds no matching custom URL patterns, then it falls back to[automatic URL pattern matching](https://firebase.google.com/docs/perf-mon/custom-url-patterns#automatic-url-patterns).

- Matches and aggregated data from*previous*requests aren't affected by removing a custom URL pattern.

  You can still access a removed custom URL pattern and its aggregated data in the*Network requests* subtab (with*All network requests*selected) until the end of the applicable data retention period. When all the aggregated data under the removed custom URL pattern expires, Firebase deletes the custom URL pattern.
- The*Network requests* subtab (with*Custom patterns*selected) does not list any removed custom URL patterns.

### Next steps

- [Set up alerts](https://firebase.google.com/docs/perf-mon/alerts)for network requests that are degrading the performance of your app. For example, you can configure an email alert for your team if the*response time*for a specific URL pattern exceeds a threshold that you set.

## Customize how success rate is calculated

One of the metrics that Firebase monitors for each network request is the request's success rate. Success rate is the percentage of successful responses compared to total responses. This metric helps you to measure network and server failures.

Specifically, Firebase automatically counts network requests with a response code in the range of 100 - 399 as successful responses.

You can customize the success rate calculation by counting certain error codes as "successful responses" in addition to the response codes that Firebase automatically counts as successful.

For example, if your app has a search endpoint API, you can count 404 responses as "successful" because 404 responses are expected for a search endpoint. Suppose there are 100 samples for this search endpoint every hour, and 60 of them are 200-responses and 40 of them are 404-responses. Before you configure the success rate, the success rate will be 60%. After you configure the success rate calculation to count 404 responses as successful, the success rate will be 100%.
| **Note:** New success rate configurations only apply to data collected after the configuration is created.

### Configure success rate calculation

To configure the success rate calculation for a network URL pattern, you must have the`firebaseperformance.config.update`permission. The following roles include this required permission by default:[Firebase Performance Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#performance),[Firebase Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles),[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), and project[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

1. Go to thePerformance Monitoring[*Dashboard*tab](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole, then select the app for which you want to configure a success rate calculation.
2. Scroll down to the traces table at the bottom of the screen and select the**Network requests**tab.
3. Find the URL pattern for which you want to configure the success rate calculation.
4. At the far right of the row, open the overflow menu (more_vert) and select**Configure success rate**.
5. Follow the on-screen instructions to select response codes that you want to count as successful response codes.

| **Note:** You can configure success rate for both automatic and custom URL patterns. It is recommended that you only configure success rate for custom URL patterns because automatic URL patterns can change over time as your data changes.
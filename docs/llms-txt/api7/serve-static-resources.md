# Source: https://docs.api7.ai/apisix/production/serve-static-resources.md

# Serve Static Resources

Static resources are files that are served directly to clients without any modification or processing at runtime. These files are typically intended to remain unchanged and are commonly used to deliver assets such as HTML, CSS, JavaScript, images, fonts, and other media files. Unlike dynamic resources that are generated or processed dynamically on the server, static resources are pre-existing files that are served as-is to the client.

In this guide, you will learn how to configure APISIX to cache and serve static resources.

## Create a Route[â](#create-a-route "Direct link to Create a Route")

For demonstration, the example below will use APISIX to reverse proxy static content from the Web Hypertext Application Technology Working Group (WHATWG) public GitHub repository.

Create a route to the WHATWG GitHub repository, configure it to match the desired static resource extensions, and enable [`proxy-cache`](https://docs.api7.ai/hub/proxy-cache.md) plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "static-src-route",
    "uri": "/whatwg/*",
    "vars": [["uri", "~~", "(.jpeg|.html)$"]],
    "plugins": {
      "proxy-cache": {}
    },
    "upstream": {
      "type": "roundrobin",
      "scheme": "https",
      "pass_host": "node",
      "nodes": {
        "raw.githubusercontent.com": 1
      }
    }
  }'
```

â¶ Match requests looking for files with `.jpeg` and `.html` extensions.

â· Enable [`proxy-cache`](https://docs.api7.ai/hub/proxy-cache.md) on the route.

### Verify[â](#verify "Direct link to Verify")

Send a request to the route for an HTML file:

```
curl -i "http://127.0.0.1:9080/whatwg/html/main/404.html"
```

You should receive an `HTTP/1.1 200 OK` response and see the following file content:

```
<!DOCTYPE html>
<script src="/link-fixup.js" defer></script>
<title>404 Not Found</title>
<style>
 body.loading div.failed, body.failed div.loading, div.failed { display: none; }
 body.loading div.loading, body.failed div.failed, div.loading { display: block; }
</style>
<body onload="document.body.className = 'failed'">
<script>document.body.className = 'loading'</script>
<div class="loading">
 <p>Loading...</p>
</div>
<div class="failed">
 <h1>Not Found</h1>
 <p>The page you are looking for is no longer available at this URL.</p>
 <p>Links to the multipage version of the specification are
 unfortunately likely to break over time. You might be able to find
 what you want from <a href="/multipage/">the contents page</a>.</p>
 <p>If you have found a broken link on the WHATWG site itself, please
 <a href="https://github.com/whatwg/html/issues/new">file an issue</a>.
 If you found a broken link from another site pointing to the WHATWG site,
 please let that site know of the problem instead. Thanks!</p>
</div>
```

Similarly, you could also send a request to the route to download a JPEG image:

```
curl -Ov "http://127.0.0.1:9080/whatwg/html/main/images/abstract.jpeg"
```

You should receive an `HTTP/1.1 200 OK` response and see the image saved in the current directory.

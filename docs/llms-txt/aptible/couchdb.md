# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/couchdb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CouchDB

> Learn about running secure, Managed CouchDB Databases on Aptible

# Available Versions

<Warning>
  As of October 31, 2024, CouchDB is no longer offered on Aptible.
</Warning>

# Logging in to the CouchDB interface (Fauxton)

To maximize security, Aptible enables authentication in CouchDB, and requires valid users. While this is unquestionably a security best practice, a side effect of requiring authentication in CouchDB is that you can't access the management interface.

Indeed, if you navigate to the management interface on a CouchDB Database where authentication is enabled, you won't be served login form... because any request, including one for the login form, requires authentication! (more on the [CouchDB Blog](https://blog.couchdb.org/2018/02/03/couchdb-authentication-without-server-side-code/)).

That said, you can easily work around this. Here's how. When you access your CouchDB Database (either through a [Database Endpoint](/core-concepts/managed-databases/connecting-databases/database-endpoints) or through a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels)), open your browser's console, and run the following code. Make sure to replace `USERNAME` and `PASSWORD` on the last line with the actual username and password from your [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials).

This code will log you in, then redirect you to Fauxton, the CouchDB management interface.

```javascript  theme={null}
(function (name, password) {
  // Don't use a relative URL in fetch: if the user accessed the page by
  // setting a username and password in the URL, that would fail (in fact, it
  // will break Fauxton as well).
  var rootUrl = window.location.href.split("/").slice(0, 3).join("/");
  var basic = btoa(`${name}:${password}`);

  window
    .fetch(rootUrl + "/_session", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Basic ${basic}`,
      },
      body: JSON.stringify({ name, password }),
    })
    .then((r) => {
      if (r.status === 200) {
        return (window.location.href = rootUrl + "/_utils/");
      }
      return r.text().then((t) => {
        throw new Error(t);
      });
    })
    .catch((e) => {
      console.log(`login failed: ${e}`);
    });
})("USERNAME", "PASSWORD");
```

# Configuration

CouchDB Databases can be configured with the [CouchDB HTTP API](http://docs.couchdb.org/en/stable/config/intro.html#setting-parameters-via-the-http-api). Changes made this way will persist across Database restarts.

# Connection Security

Aptible CouchDB Databases support connections via the following protocol:

* For CouchDB version 2.1: `TLSv1.2`

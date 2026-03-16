# Download handlers

Download handlers are Scrapy components used to
download requests and produce responses from
them.

## Using download handlers

The `DOWNLOAD_HANDLERS_BASE` and `DOWNLOAD_HANDLERS` settings
tell Scrapy which handler is responsible for a given URL scheme. Their values
are merged into a mapping from scheme names to handler classes. When Scrapy
initializes it creates instances of all configured download handlers (except
for lazy ones) and stores them in a similar
mapping. When Scrapy needs to download a request it extracts the scheme from
its URL, finds the handler for this scheme, passes the request to it and gets a
response from it.  If there is no handler for the scheme, the request is not
downloaded and a `NotSupported` exception is raised.

The `DOWNLOAD_HANDLERS_BASE` setting contains the default mapping of
handlers. You can use the `DOWNLOAD_HANDLERS` setting to add handlers
for additional schemes and to replace or disable default ones:

```
DOWNLOAD_HANDLERS = {
    # disable support for ftp:// requests
    "ftp": None,
    # replace the default one for http://
    "http": "my.download_handlers.HttpHandler",
    # http:// and https:// are different schemes,
    # even though they may use the same handler
    "https": "my.download_handlers.HttpHandler",
    # support for any custom scheme can be added
    "sftp": "my.download_handlers.SftpHandler",
}

```
# Source: https://docs.logrocket.com/reference/javascript-stack-traces.md

# JavaScript Stack Traces

How to upload source maps to decode stack traces for JavaScript

LogRocket interprets your JavaScript source maps so you can see your original, non-minified code in stack traces. This lets you view the source context of errors, logs, network requests and redux actions to understand where in your code logs were generated. These are also used in Error Reporting pages.

## Making source maps accessible to LogRocket

There are two ways to make source maps accessible to LogRocket:

1. Host source maps publicly over `http`/`https`.
2. Upload source maps to LogRocket for each version of your application.

### Hosting source map files

LogRocket searches for source map directives in your minified JavaScript files with the following format:

```
//# sourceMappingURL=<url>
```

When LogRocket encounters such a directive, it will resolve the source map URL relative to the source file in which it is found, and make an HTTP request to fetch it.

> 🚧 Hidden source maps
>
> Please note that hidden source maps are **not supported** by LogRocket.  The sourceMappingURL noted above is required.

> 🚧 Upload sourcemaps prior to an error occurring
>
> Please note that source maps must be uploaded to LogRocket before use.  They will not be applied to existing errors.

Many developers choose not to publicly host their source maps. In this case, we recommend uploading your source maps directly to LogRocket.

### Uploading source maps to LogRocket

To upload source maps you will need to install the LogRocket command line tool:

```shell
npm install -g logrocket-cli
```

#### Creating a Release

All source maps you upload must be associated with a release. This keeps the correct sources associated with older videos. A release can be any version string, such as `2.4.6` or a commit hash such as `b620fm`.

There are two parts to creating a release. First, tell LogRocket about the release you're currently recording. This is done in the script tag that you added as part of the quickstart:

```javascript
LogRocket.init('yourorg/yourapp', {
  release: 'b620fm'
});
```

Next, use the command line to create the release. You will need an API key. It can be found in your app settings. Make sure to copy it in its entirety.

```shell
logrocket release b620fm --apikey="your:api:key"
```

#### Uploading Source Maps for a Release

Lastly, it's time to upload the source maps for this release. You can point the upload script at any number of files or directories. If you do upload a directory be aware that it will recursively upload everything in it. You should upload the source maps as well as the compressed JavaScript files, so that they can be matched up.

```javascript
logrocket upload my_directory/ 
  --release=b620fm
  --apikey="your:api:key"
  --url-prefix="~/public/"  # optional
```

> 🚧 URL Prefix (--url-prefix) option
>
> If your assets are hosted in a subfolder, then provide a url-prefix option to the upload command matching the path relative to the hostname (you may replace the hostname with `~`). If you don't provide this option we won't be able to correctly link your source map files.
>
> **For example:**
>
> Asset URL: [https://example.com/public/main.js](https://example.com/public/main.js)\
> URL prefix provided to LogRocket CLI: `~/public` or `https://example.com/public/`
# Source: https://docs.socket.dev/reference/socket-package-urls-purl.md

# Socket Package URLs (purl)

This page describes how Socket purls work

# What is a Socket purl?

A Socket purl is based on the standard as documented [here](https://spdx.github.io/spdx-spec/v3.0/model/Software/Properties/packageUrl/#:~:text=A%20packageUrl%20\(commonly%20pronounced%20and,identify%20and%20locate%20software%20packages.\)). There is a good description from that page:

A packageUrl (commonly pronounced and referred to as "purl") is an attempt to standardize package representations in order to reliably identify and locate software packages. A purl is a URL string which represents a package in a mostly universal and uniform way across programming languages, package managers, packaging conventions, tools, APIs and databases.

A Socket purl as used with the [packages](https://docs.socket.dev/reference/batchpackagefetch) API and the specific definition for the format can be found at the [Github Spec](https://github.com/package-url/purl-spec).

# Constructing a Socket purl

The format for a purl is like the following:

```
scheme:type/namespace/name@version
```

In the case of the Socket Packages endpoint the scheme is always going to be `pkg`. Here are some examples for different eccosystems:

**npm**

```
pkg:npm/browserlist@1.0.0
```

**Python**

```
pkg:pypi/light-s3-client@0.0.20
```

**Maven**

```
pkg:maven/log4j/log4j@1.2.17
```
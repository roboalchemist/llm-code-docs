# Source: https://redocly.com/learn/openapi/multi-file-definitions.md

# Multi-file OpenAPI definitions

We recommend a multi-file OpenAPI definition.

Skills you will need:

- General knowledge of the OpenAPI Specification 3.0.3.
- How to [use $refs](/learn/openapi/ref-guide).


## Why

Be able to explain the reasons for using a multi-file format:

1. Easier to contribute.
2. Easier to review contributions.
3. Better supports a docs-like-code workflow.
4. Enforces better re-use of objects to avoid duplication and divergence issues.
5. Supported by Redocly toolchain including the free open-source [Redocly CLI](https://github.com/redocly/redocly-cli).


Be able to explain the drawbacks of a multi-file approach:

1. Some tools don't support `$ref`s in other files. Mitigation: Redocly CLI has a `bundle` command, and Redocly has a free API Registry to build a bundled file which can be useful for others.


Tip
Use Redocly's [VS Code plugin](https://marketplace.visualstudio.com/items?itemName=Redocly.openapi-vs-code) to lint as you type. Navigate to `$ref`s with a click or keystroke.

## Folder structure

We have built a free tool, Redocly CLI [split command](/docs/cli/commands/split), that can take an OpenAPI 3 definition and convert it to a multi-file format. If you are starting from scratch without any definition, you can use our template [OpenAPI starter repo](https://github.com/Redocly/openapi-starter).

You'll end up with files structured like this inside of the `openapi` folder:


```shell
âââ README.md
âââ code_samples
âÂ Â  âââ C#
âÂ Â  âÂ Â  âââ echo
âÂ Â  âÂ Â      âââ post.cs
âÂ Â  âââ PHP
âÂ Â  âÂ Â  âââ echo
âÂ Â  âÂ Â      âââ post.php
âÂ Â  âââ README.md
âââ components
âÂ Â  âââ README.md
âÂ Â  âââ headers
âÂ Â  âÂ Â  âââ ExpiresAfter.yaml
âÂ Â  âââ schemas
âÂ Â  âÂ Â  âââ Email.yaml
âÂ Â  âÂ Â  âââ User.yaml
âÂ Â  âââ securitySchemes
âÂ Â      âââ api_key.yaml
âÂ Â      âââ basic_auth.yaml
âÂ Â      âââ main_auth.yaml
âââ openapi.yaml
âââ paths
    âââ README.md
    âââ echo.yaml
    âââ users@{username}.yaml
```

There is a `README.md` in each directory with further instructions and suggestions.

You'll notice the main `openapi.yaml` file which we call the root document of the OpenAPI definition.

Keep in mind, this is just one possible structure. Structure the files however you want, and you will still benefit from Redocly's CLI tool.

Inspect the `package.json` file to learn more about these scripts.

## Root file

The `openapi.yaml` file referred to above is what we call the root file.
This file can be named anything, but you may need to adjust the [Redocly configuration file](/docs/cli/configuration) if you rename it.

In this example, we rename the file from `openapi.yaml` to `foo.yaml` and also rename the within the configuration file the corresponding `apis` object's properties.
The `foo@v1` could be renamed to any unique alias.
The alias can be useful when you have multiple definitions, you can refer to them on the command line like: `redocly lint foo@v1`.


```yaml
# See https://redocly.com/docs/cli/configuration/ for more information.
apis:
  foo@v1:
    root: "openapi/foo.yaml"
rules:
  no-unused-schemas: warning
theme:
  openapi:
    htmlTemplate: ./docs/index.html
    theme:
      colors:
        primary: "#32329f"
```

The root `openapi.yaml` file looks like this:


```yaml
openapi: 3.0.3
info:
  version: 1.0.0
  title: Example.com
  termsOfService: 'https://example.com/terms/'
  contact:
    email: contact@example.com
    url: 'http://example.com/contact'
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
  x-logo:
    url: 'https://apis.guru/openapi-template/logo.png'
  description: >
    This is an **example** API to demonstrate features of OpenAPI specification.

    # Introduction

    Truncated intentionally...

externalDocs:
  description: Find out how to create a GitHub repo for your OpenAPI definition.
  url: 'https://github.com/Rebilly/generator-openapi-repo'
tags:
  - name: Echo
    description: Example echo operations
  - name: User
    description: Operations about user
servers:
  - url: 'http://example.com/api/v1'
  - url: 'https://example.com/api/v1'
paths:
  '/users/{username}':
    $ref: 'paths/users@{username}.yaml'
  /echo:
    $ref: paths/echo.yaml
components:
  securitySchemes:
    main_auth:
      type: oauth2
      flows:
        implicit:
          authorizationUrl: 'http://example.com/api/oauth/dialog'
          scopes:
            'read:users': read users info
            'write:users': modify or remove users
    api_key:
      type: apiKey
      in: header
      name: api_key
    basic_auth:
      type: http
      scheme: basic
```

This file is intentionally short.
Most of the content is organized in the `paths` and `components` folders.

### Lint

npm

```shell
npm test
```

yarn

```shell
yarn test
```

### Bundle

npm

```shell
npm build
```

yarn

```shell
yarn build
```

### Preview-docs

If you subscribe to our commercial offering, generate an API key under **My profile**, and your previews will be using Redocly API docs (or it will fallback to Redoc community edition).
Read more about [preview-docs](/docs/cli/v1/commands/preview-docs).

npm

```shell
npm start
```

yarn

```shell
yarn start
```
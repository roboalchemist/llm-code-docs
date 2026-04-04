# Source: https://upstash.com/docs/workflow/agents/overview.md

# Source: https://upstash.com/docs/redis/sdks/ts/overview.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/overview.md

# Source: https://upstash.com/docs/redis/sdks/ratelimit-ts/overview.md

# Source: https://upstash.com/docs/redis/sdks/ratelimit-py/overview.md

# Source: https://upstash.com/docs/redis/sdks/py/overview.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/overview.md

# Source: https://upstash.com/docs/qstash/sdks/ts/overview.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/overview.md

# Source: https://upstash.com/docs/qstash/sdks/py/overview.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/overview.md

# Source: https://upstash.com/docs/devops/terraform/overview.md

# Source: https://upstash.com/docs/devops/pulumi/overview.md

# Source: https://upstash.com/docs/devops/cli/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Manage Upstash resources in your terminal or CI.

You can find the Github Repository [here](https://github.com/upstash/cli).

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=937abb7a6ac182220417755140c1a552" data-og-width="2048" width="2048" data-og-height="1414" height="1414" data-path="img/oss/cli/banner.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=539308726a2f9892a345d9b706b944ff 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2ff1ff319b6f77b3b994b2dab8a2dd49 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=69085bd86ca2af13ac25016635e09bb4 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=121513fcc45c291dc2f68217900ad93b 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=0a8989255b1e309d60414658a3a68bba 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/oss/cli/banner.svg?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=249344a05e443b79f630cf8f022dc3ce 2500w" />
</Frame>

<br />

# Installation

## npm

You can install upstash's cli directly from npm

```bash  theme={"system"}
npm i -g @upstash/cli
```

It will be added as `upstash` to your system's path.

## Compiled binaries:

`upstash` is also available from the
[releases page](https://github.com/upstash/cli/releases/latest) compiled
for windows, linux and mac (both intel and m1).

# Usage

```bash  theme={"system"}
> upstash

  Usage:   upstash
  Version: development

  Description:

    Official cli for Upstash products

  Options:

    -h, --help               - Show this help.
    -V, --version            - Show the version number for this program.
    -c, --config   <string>  - Path to .upstash.json file

  Commands:

    auth   - Login and logout
    redis  - Manage redis database instances
    team   - Manage your teams and their members

  Environment variables:

    UPSTASH_EMAIL    <string>  - The email you use on upstash
    UPSTASH_API_KEY  <string>  - The api key from upstash
```

## Authentication

When running `upstash` for the first time, you should log in using
`upstash auth login`. Provide your email and an api key.
[See here for how to get a key.](https://docs.upstash.com/redis/howto/developerapi#api-development)

As an alternative to logging in, you can provide `UPSTASH_EMAIL` and
`UPSTASH_API_KEY` as environment variables.

## Usage

Let's create a new redis database:

```
> upstash redis create --name=my-db --region=eu-west-1
  Database has been created

  database_id          a3e25299-132a-45b9-b026-c73f5a807859
  database_name        my-db
  database_type        Pay as You Go
  region               eu-west-1
  type                 paid
  port                 37090
  creation_time        1652687630
  state                active
  password             88ae6392a1084d1186a3da37fb5f5a30
  user_email           andreas@upstash.com
  endpoint             eu1-magnetic-lacewing-37090.upstash.io
  edge                 false
  multizone            false
  rest_token           AZDiASQgYTNlMjUyOTktMTMyYS00NWI5LWIwMjYtYzczZjVhODA3ODU5ODhhZTYzOTJhMTA4NGQxMTg2YTNkYTM3ZmI1ZjVhMzA=
  read_only_rest_token ApDiASQgYTNlMjUyOTktMTMyYS00NWI5LWIwMjYtYzczZjVhODA3ODU5O_InFjRVX1XHsaSjq1wSerFCugZ8t8O1aTfbF6Jhq1I=


  You can visit your database details page: https://console.upstash.com/redis/a3e25299-132a-45b9-b026-c73f5a807859

  Connect to your database with redis-cli: redis-cli -u redis://88ae6392a1084d1186a3da37fb5f5a30@eu1-magnetic-lacewing-37090.upstash.io:37090
```

## Output

Most commands support the `--json` flag to return the raw api response as json,
which you can parse and automate your system.

```bash  theme={"system"}
> upstash  redis create --name=test2113 --region=us-central1 --json | jq '.endpoint'

 "gusc1-clean-gelding-30208.upstash.io"
```

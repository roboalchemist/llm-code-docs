# Source: https://docs.socket.dev/docs/socket-analytics.md

# socket analytics

Get analytics data at the organization and repository level

```
$ socket analytics --help

  Look up analytics data

  Usage
    $ socket analytics [options] [ "org" | "repo" <reponame>] [TIME]

  API Token Requirements
    - Quota: 1 unit
    - Permissions: report:write

  The scope is either org or repo level, defaults to org.

  When scope is repo, a repo slug must be given as well.

  The TIME argument must be number 7, 30, or 90 and defaults to 30.

  Options
    --file            Path to store result, only valid with --json/--markdown
    --json            Output result as json
    --markdown        Output result as markdown

  Examples
    $ socket analytics org 7
    $ socket analytics repo test-repo 30
    $ socket analytics 90
```

<br />

Example of what the dashboard looks like:

![](https://files.readme.io/4198b08d713fd8d06e5d5fb434659f11e660b15dba25e0772ac2339ab6bf62f7-image.png)
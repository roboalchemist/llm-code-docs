# Source: https://docs.socket.dev/docs/socketjson.md

# socket.json

A file containing local project settings to be used by the CLI

The `socket.json` file is a local configuration file to be consumed by the CLI.

The file contains project/repository level default override for flags and args.

For example, if you do `socket scan create --branch=foo`, you can instead also run `socket scan setup`, set a default for the `--branch` flag to `foo`, and next time you run `socket scan create` it will automatically set `--branch=foo`. And if you use `--branch=xyz` instead then it will happily use `xyz`.

Each project root dir needs its own `socket.json`. There is no inheritance or anything fancy. Many things here are specific to a project, anyways. Repo name, branch name, manifest configuration, etc.

This file is meant to make your life easier when using the Socket CLI. You can do whatever you want with it:

* Commit it to repo to ease collaboration
* Ignore it in your `.gitignore` because you don't like the clutter
* Delete it because you don't need this
* Edit it because you're curious
* Do nothing
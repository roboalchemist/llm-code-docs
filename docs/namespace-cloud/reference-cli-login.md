<!-- Source: https://namespace.so/docs/reference/cli/login -->

# nsc login

Login to Namespace to access Namespace Instances, Remote Builders, etc.

`login` authenticates the `nsc` CLI to use Namespace products. The CLI opens
a browser where you need to select a [workspace](/docs/workspaces) to
complete the login flow.

## Usage

```
nsc login [--session]
```

### Example

```
$ nsc login
Login to Namespace
Please complete the login flow in your browser.
 
  https://cloud.namespace.so/login/workspace?id=<id>
 
You are now logged in, have a nice day.
```

Afterward you can start using the `nsc` CLI to create ephemeral instances, build
container images, run containers or previews.

## Options

### --session

If set, creates a long-lived, revocable session. Sessions can be managed under [cloud.namespace.so/user/sessions](https://cloud.namespace.so/user/sessions).

Last updated July 4, 2025

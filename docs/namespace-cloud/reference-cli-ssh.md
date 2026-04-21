<!-- Source: https://namespace.so/docs/reference/cli/ssh -->

# nsc ssh

Connect to ephemeral environments.

`ssh` connects to a previously created ephemeral environment. It establishes a
`ssh` connection to the target environment, over Namespace's networking, in a
way that end-to-end encryption is retained, but the target host is not exposed
directly to the Internet.

To enable experimentation, `ssh` also has a "quick create" mode built-in,
allowing you to quickly create a named environment (a sandbox), or get back to a
previously created sandbox.

This allows you to jump into a container-enabled terminal in a few seconds.

## Usage

```
nsc ssh [--tag <name>] [-A] [<id>] [command]
```

### Example

Create an ephemeral instance:

```
$ nsc create
  Created new ephemeral environment! ID: 85a32emcg99ii
```

SSH into the created instance:

```
$ nsc ssh 85a32emcg99ii
85a32emcg99ii:~#
```

You can also omit the environment id, and a list of your environments will be presented to you.

```
$ nsc ssh
┌─────────────────────────────────────────────────────────────────────────────────┐
│ Instance ID    CPU  Memory   Arch   Created       Time to live         Purpose  │
│─────────────────────────────────────────────────────────────────────────────────│
│ 85a32emcg99ii  4    4.0 GiB  amd64  10 hours ago  29 minutes from now  ...      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

Finally, you can also issue commands to the ssh sessions directly from `nsc`.

```
$ nsc ssh 85a32emcg99ii ls /
bin         etc         lib         media       nsc         proc        run         srv         tmp         var
dev         home        lost+found  mnt         opt         root        sbin        sys         usr         vendor
```

## Options

### --tag <name>

If specified, connects to an existing environment named `name`; and if one
doesn't exit, creates a new one.

### -A

Forward your local SSH agent connection, to the remote environment.

Last updated July 4, 2025

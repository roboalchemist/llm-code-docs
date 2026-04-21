<!-- Source: https://namespace.so/docs/reference/cli/rdp -->

# nsc rdp

Start an RDP session.

`rdp` connects to a previously created instance via RDP (Remote Desktop Protocol), allowing you to
gain interactive, visual access to your [Windows runners](/docs/architecture/compute/windows).

## Usage

```
nsc rdp [instance-id]
```

### Example

Start an RDP session to a Windows instance:

```
$ nsc rdp 85a32emcg99ii
```

RDP credentials are printed on the CLI and currently need to be entered in the RDP client manually.

![Windows RDP](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwindows-demo.338ac8f5.png&w=1200&q=75)

You can also omit the instance id, and a list of your instances will be presented to you.

## Options

`nsc rdp` has no options.

Last updated February 13, 2026

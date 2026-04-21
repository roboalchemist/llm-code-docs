<!-- Source: https://namespace.so/docs/reference/cli/ingress-list -->

# nsc ingress list

Lists the registered ingresses on the specified instance.

`ingress list` lists all the registered ingresses for an instance.
To expose an application in a preview, see our guides on [Container Previews](/docs/solutions/previews) and [Kubernetes Previews](/docs/solutions/previews/kubernetes).

## Usage

```
nsc ingress list <instance-id> [--output <plain|json>]
```

### Example

In the example below, we first create an ephemeral instance, start nginx with `kubectl run`, create a Load Balancer with `kubectl expose` and then expose it
using `nsc expose kubernetes`.

Create an ephemeral instance:

```
$ nsc create
  Created new ephemeral environment! ID: hk99v6hn1tk9m
```

Start nginx within the created instance:

```
nsc kubectl hk99v6hn1tk9m run nginx --image=nginx
pod/nginx created
```

And create a Load Balancer:

```
nsc kubectl hk99v6hn1tk9m expose pod nginx --type=LoadBalancer --port=80
service/nginx exposed
```

Then, expose port 80 using the `nsc expose kubernetes` command:

```
$ nsc expose kubernetes hk99v6hn1tk9m --namespace=default --service=nginx --name=nginx-foobar
Exported port 80 from default/nginx:
  https://nginx-foobar-hk99v6hn1tk9m.fra1.namespaced.app
```

From now own, `nsc ingress list` will inform you about this exposed ingress.

```
% nsc ingress list hk99v6hn1tk9m
https://nginx-foobar-hk99v6hn1tk9m.fra1.namespaced.app (port: 80)
```

## Options

### -o <type>

Specifies the output format. Supported options are `json` and
`plain`. By default, plain output format is used.

Last updated July 4, 2025

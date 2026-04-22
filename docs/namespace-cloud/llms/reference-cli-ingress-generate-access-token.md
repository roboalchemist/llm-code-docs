<!-- Source: https://namespace.so/docs/reference/cli/ingress-generate-access-token -->

# nsc ingress generate-access-token

Generate a scoped access token that can be used to access a preview programmatically.

`ingress generate-access-token` generates an access token. Using this token, you can access your Namespace previews programmatically.
By default, the token is scoped to the entire workspace. You can restrict the token to only grant access to a single instance though.

## Usage

```
nsc ingress generate-access-token [--instance <instance-id>]
```

### Example

The following example starts a new ephemeral environment, running nginx. The `nginx`
container image has nginx, an http reverse proxy, listening on port 80. We
export that port to a public endpoint, using `-p 80`.

Then, we generate an access token and query the exposed application with `curl`.

```
$ nsc run --image nginx -p 80
  Created new ephemeral environment! (id: 85a32emcg99ii).
  More at: https://cloud.namespace.so/01gr490qvbntkjn9jwypnd4g04/instance/85a32emcg99ii
  Running "nginx-t082s"
    Exported 80/tcp as https://4bi2reg-85a32emcg99ii.fra1.namespaced.app
```

Let's generate an access token for this instance and `curl` the exposed application:

```
$ export TOKEN=`nsc ingress generate-access-token --instance=85a32emcg99ii`
 
$ curl -H "x-nsc-ingress-auth: Bearer $TOKEN" 'https://4bi2reg-85a32emcg99ii.fra1.namespaced.app'
 
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

## Options

### --instance <instance-id>

If set, the generated access token will be limited to this instance.

### --output\_to <path>

Write the generated access token to this path. If file already exists, it will get overwritten.

Last updated July 4, 2025

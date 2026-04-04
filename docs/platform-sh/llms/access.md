# Source: https://docs.upsun.com/create-apps/image-properties/access.md

# access


An access dictionary that defines the access control for roles accessing app environments.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images. 

The `access` dictionary has one allowed key:

| Name  | Allowed values                      | Default       | Description                                                           |
|-------|-------------------------------------|---------------|-----------------------------------------------------------------------|
| `ssh` | `admin`, `contributor`, or `viewer` | `contributor` | Defines the minimum role required to access app environments via SSH. |

In the following example, only users with `admin` permissions for the
given [environment type](https://docs.upsun.com/administration/users.md#environment-type-roles)
can access the deployed environment via SSH:

```yaml {}
applications:
  <APP_NAME>:
    type: "python:3.14"
    source:
      root: "/"
    access:
      ssh: admin
```

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    type: "composable:25.11"
    stack: 
      runtimes: [ "python@3.14" ]
    source:
      root: "/"
    access:
      ssh: admin
```



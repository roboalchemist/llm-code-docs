# Source: https://docs.upsun.com/environments/http-access-control.md

# Configure HTTP access control

When developing your site, you might want to hide your preview environments from outside viewers.
Or you may find you have performance issues from [excessive bot access](https://support.platform.sh/hc/en-us/community/posts/16439634723858).
You can control access with a username and password **or** by allowing/denying specific IP addresses or networks.
This setting applies to the entire environment.

The settings for a specific environment are inherited by all of its children.
So if you have a `staging` environment and you [branch environments from it](https://docs.upsun.com/glossary.md#branch),
all of the environments branched from it inherit the same authentication information.

Changing access control triggers a new deploy of the current environment.
The changes don't propagate to child environments until they're [redeployed manually](https://docs.upsun.com../development/troubleshoot.md#force-a-redeploy).

## Use a username and password

You can set up one or more combinations of a username and password.
To add a username and password, follow these steps:

Run the following command:

```bash {}
upsun environment:http-access -e <ENVIRONMENT_NAME> --auth <USERNAME>:<PASSWORD>
```

For example, to add the username ``name`` with the password ``12321`` to the ``test`` environment, run:

```bash {}
upsun environment:http-access -e test --auth name:12321
```

## Filter IP addresses

Alternatively, you can control access to environments by allowing or denying specific IP addresses or ranges of IP addresses.
The addresses should be in the [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
Both`4.5.6.7` and `4.5.6.0/8` are accepted formats.

Note that `allow` entries should come before `deny` entries in case they both match.

For example, the following configuration allows only the IP `198.51.100.0` to access your website.

```txt
198.51.100.0 allow
0.0.0.0/0 deny
```

**Pick your authentication method**: 

When you set up IP filtering authentication,
make sure no [username and password are defined](#use-a-username-and-password) for your environment.

Otherwise, your environment will remain accessible through the defined username and password combination,
regardless of your IP filtering settings.

To control access based on IP address, follow these steps:

Run the following command:

```bash {}
upsun environment:http-access -e <ENVIRONMENT_NAME> --access allow:<IPS_TO_ALLOW> --access deny:<IPS_TO_DENY>
```



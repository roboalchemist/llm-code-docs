# User-Password authentication · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/manual/user-password

# Source: https://zenoh.io/docs/manual/user-password

# User-Password authentication
Zenoh supports basicuser-password authentication.
Clients and peers can useuserandpasswordfor authentication against a router or a peer.
Similarly, peers and routers can useuserandpasswordfor authentication among themselves.
The configuration of credentials is done via aconfiguration file.

## Client configuration
The required configuration fields for aclientwould hence be:
```
{
  /// The node's mode (router, peer or client)
  mode: "client",
  transport: {
    auth: {
      /// The configuration of authentication.
      /// A password implies a username is required.
      usrpwd: {
        user: "clientusername",
        password: "clientpassword",
      },
    },
  },
}
```

When using such configuration, the client will use the provideduserandpasswordto authenticate against any peer or router.
Let’s assume the above configuration is then saved with the nameclient.json5.

## Router or peer configuration
The required configuration fields for arouteror apeerwould hence be:
```
{
  /// The node's mode (router, peer or client)
  mode: "router",
  transport: {
    auth: {
      /// The configuration of authentication.
      usrpwd: {
        user: "routerusername",
        password: "routerpassword",
        /// The path to a file containing the user password dictionary
        dictionary_file: "credentials.txt",
      },
    },
  },
}
```

Thedictionary_fileindicates the path of a text file containing the full list of authorized credentials for connection.
The authorized credentials text file would hence be:
```
clientusername:clientpassword
```

Each line of the file represents the one single authorized credential in the form ofuser:password.
The authorized credentials text file can contain any number of lines.
When using such configuration, the router or peer will use the provideduserandpasswordto authenticate against any other peer or router.
At the same time, it will use the file containing the authorized credentials to authenticate incoming connections.
Let’s assume that the above configurations are then saved with the namerouter.json5andcredentials.txt.

## Testing the user-password authentication
Let’s assume a scenario with one Zenoh router and two clients connected to it: one publisher and one subscriber.
The first thing to do is to run the router passing its configuration, i.e.router.json5:
```
$ zenohd -c router.json5
```

Make sure that the path indicated in theuser_password_dictionaryproperty points to a valid credentials file.
Then, let’s start the subscriber in client mode passing its configuration, i.e.client.json5:
```
$ z_sub -c client.json5
```

Lastly, let’s start the publisher in client mode passing its configuration, i.e.client.json5:
```
$ z_pub -c client.json5
```

As it can be noticed, the sameclient.json5is used forz_subandz_put.
Both are using the same credentials and are authenticated accordingly by therouter.
Nevertheless, different configuration files and credentials could be used.

## Final remark
Consider to not store clear text password in the configuration files. Before creating the configuration files, a hashing function should be used to hash the password.
For example, let’s compute the hash for theclientandrouterpasswords:
```
$ echo clientpassword | sha256sum
92df0d4f39c218607e3200bf93ccac87a80cb910e811d84b286bebe0a8860724

$ echo routerpassword | sha256sum
2ce01a11893f276a4064f586f24b8f1868008e2e623f6c4e74ef381247e49df1
```

Therefore, theclient.json5would become:
```
{
  /// The node's mode (router, peer or client)
  mode: "client",
  transport: {
    auth: {
      /// The configuration of authentication.
      /// A password implies a username is required.
      usrpwd: {
        user: "clientusername",
        password: "92df0d4f39c218607e3200bf93ccac87a80cb910e811d84b286bebe0a8860724",
      },
    },
  },
}
```

And therouter.json5file would become:
```
{
  /// The node's mode (router, peer or client)
  mode: "router",
  transport: {
    auth: {
      /// The configuration of authentication.
      usrpwd: {
        user: "routerusername",
        password: "2ce01a11893f276a4064f586f24b8f1868008e2e623f6c4e74ef381247e49df1",
        /// The path to a file containing the user password dictionary
        dictionary_file: "credentials.txt",
      },
    },
  },
}
```

Finally, thecredentials.txtfile would become:
```
clientusername:92df0d4f39c218607e3200bf93ccac87a80cb910e811d84b286bebe0a8860724
```
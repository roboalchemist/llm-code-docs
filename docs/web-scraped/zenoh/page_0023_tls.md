# TLS authentication · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/manual/tls

# Source: https://zenoh.io/docs/manual/tls

# TLS authentication
Zenoh supports TLS as a transport protocol.
TLS can be configured in two ways:
- server side authentication: clients validate the server TLS certificate but not the other way around, that is, the same way of operating on the web where the web browsers validate the identity of the server via means of the TLS certificate.
- mutual authentication (mTLS): where both server-side and client-side authentication is required.
The configuration of TLS certificates is done via aconfiguration file.

## Client configuration
The fieldroot_ca_certificateis used to specify the path to the certificate used to authenticate theTLS server.
It’s important to note that if the field is not specified then the default behaviour is to load the root certificates provided byMozilla’s CA for use with webpki.
However, if we manage our own certificates, we need to specify the root certificate.
Suppose we generated the certificate usingMiniCA as explained below, then the configuration file for aclientwould be:
```
{
  /// The node's mode (router, peer or client)
  "mode": "client",
  "connect": {
    "endpoints": ["tls/localhost:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/tls/minica.pem"
      }
    }
  }
}
```

When using such configuration, the client will use the providedminica.pemcertificate to authenticate theTLS server certificate.
Let’s assume the above configuration is then saved with the nameclient.json5.

## Router configuration
The requiredtlsfields for configuring aTLS certificatefor a router arelisten_private_keyandlisten_certificate.
A configuration file for arouterwould be:
```
{
  /// The node's mode (router, peer or client)
  "mode": "router",
  "listen": {
    "endpoints": ["tls/localhost:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_private_key": "/home/user/tls/localhost/key.pem",
        "listen_certificate": "/home/user/tls/localhost/cert.pem"
      }
    }
  }
}
```

When using such configuration, the router will use the providedlisten_private_keyandlisten_certificatefor establishing a TLS session with any client.
Let’s assume that the above configurations are then saved with the nameserver.json5.

## Peer configuration
The requiredtlsfields for configuring aTLS certificatefor a peer areroot_ca_certificate,listen_private_keyandlisten_certificate.
A configuration file for apeerwould be:
```
{
  /// The node's mode (router, peer or client)
  "mode": "peer",
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/tls/minica.pem",
        "listen_private_key": "/home/user/tls/localhost/key.pem",
        "listen_certificate": "/home/user/tls/localhost/cert.pem"
      }
    }
  }
}
```

When using such configuration, the peer will use the providedroot_ca_certificateto authenticate theTLS certificateof thepeerit is connecting to.
At the same time, the peer will use the providedlisten_private_keyandlisten_certificatefor initiating incoming TLS sessions from other peers.
Let’s assume that the above configurations are then saved with the namepeer.json5.

## TLS with Scouting ⚠️
Zenoh provides ascouting mechanismthat allows peers to discover other neighboring peers automatically.
By default, this feature is enabled and attempts to establish connections with other peersusing all Zenoh-supported protocols(not just TLS).
To ensure that all connections are established using TLS, you can configure the protocols filter as shown below:
```
{
  "transport": {
    "link": {
      "protocols": ["tls"]
    }
  }
}
```

Theprotocolsconfiguration field specifies which protocols Zenoh should whitelist for accepting and opening sessions. If this field is not configured, Zenoh will automatically whitelist all supported protocols.

## Mutual authentication (mTLS)
In order to enable mutual authentication, we’ll need two sets of keys and certificates, one for the “server” and one for the “client”. These sets of keys and certificates can be generated as explainedin the appendix section below.
Let’s suppose we are storing them under$home/user/with the following files and folders structure:
```
user
├── client
│   ├── localhost
│   │   ├── cert.pem
│   │   └── key.pem
│   ├── minica-key.pem
│   └── minica.pem
└── server
    ├── localhost
    │   ├── cert.pem
    │   └── key.pem
    ├── minica-key.pem
    └── minica.pem
```

### Router configuration
The filedenable_mtlsneeds to be set totrueand we must provide the router (acting as server) the certificate authority to validate the client’s keys and certificates under the fieldroot_ca_certificate. Thelisten_private_keyandlisten_certificatefields are also required in order to authenticate the router in front of the client.
```
{
  "mode": "router",
  "listen": {
    "endpoints": ["tls/localhost:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/client/minica.pem",
        "enable_mtls": true,
        "listen_private_key": "/home/user/server/localhost/key.pem",
        "listen_certificate": "/home/user/server/localhost/cert.pem"
      }
    }
  }
}
```

### Client configuration
Again, the fieldenable_mtlsneeds to be set totrueand we must provide the certificate authority to validate the server keys and certificates. Similarly, we need to provide the client keys and certificates for the server to authenticate our connection.
```
{
  "mode": "client",
  "connect": {
    "endpoints": ["tls/localhost:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/server/minica.pem",
        "enable_mtls": true,
        "connect_private_key": "/home/user/client/localhost/key.pem",
        "connect_certificate": "/home/user/client/localhost/cert.pem"
      }
    }
  }
}
```

## Close on certificate expiration
Starting with Zenoh v1.0.3, TLS and QUIC links can be closed when the remote certificate chain expires: the configured local instance will monitor the expiration time of the first expiring certificate in the remote instance’s certificate chain, and will disconnect the link when said time is reached.
This behavior can be enabled via the zenoh config file, by setting the fieldclose_link_on_expirationtotrue. This is valid for both TLS clients and servers.

### Client configuration
Below is an example config for a TLS client with certificate expiration monitoring.mTLS-related config fields can also be added if required.
```
{
  "mode": "client",
  "connect": {
    "endpoints": ["tls/localhost:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/server/minica.pem",
        "close_link_on_expiration": true
      }
    }
  }
}
```

### Listener configuration
Note that certificate expiration can only be monitored by a TLS listener whenmTLSis enabled, since withoutmTLSa client does not need certificates to connect. Below is an example config for a router acting as TLS server with certificate expiration monitoring.
```
{
  "mode": "router",
  "listen": {
    "endpoints": ["tls/localhost:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/client/minica.pem",
        "listen_private_key": "/home/user/server/localhost/key.pem",
        "listen_certificate": "/home/user/server/localhost/cert.pem",
        "enable_mtls": true,
        "close_link_on_expiration": true
      }
    }
  }
}
```

## Testing the TLS transport
Let’s assume a scenario with one Zenoh router and two clients connected to it: one publisher and one subscriber.
The first thing to do is to run the router passing its configuration, i.e.router.json5:
```
$ zenohd -c router.json5
```

Then, let’s start the subscriber in client mode passing its configuration, i.e.client.json5:
```
$ z_sub -c client.json5
```

Lastly, let’s start the publisher in client mode passing its configuration, i.e.client.json5:
```
$ z_pub -c client.json5
```

As it can be noticed, the sameclient.json5is used forz_subandz_pub.

### Peer-to-peer scenario
Let’s assume a scenario with two peers.
First, let’s start the first peer in peer mode passing its configuration, i.e.peer.json5:
```
$ z_sub -c peer.json5 -l tls/localhost:7447
```

Next, let’s start the second peer in peer mode passing its configuration, i.e.peer.json5:
```
$ z_pub -c peer.json5 -l tls/localhost:7448 -e tls/localhost:7447
```

As it can be noticed, the samepeer.json5is used forz_subandz_pub.

## Appendix: TLS certificates creation
In order to use TLS as a transport protocol, we need first to create the TLS certificates.
While multiple ways of creating TLS certificates exist, in this guide we are going to useminicafor simplicity:
> Minica is a simple CA intended for use in situations where the CA operator also operates each host where a certificate will be used. It automatically generates both a key and a certificate when asked to produce a certificate. It does not offer OCSP or CRL services. Minica is appropriate, for instance, for generating certificates for RPC systems or microservices.
Minica is a simple CA intended for use in situations where the CA operator also operates each host where a certificate will be used. It automatically generates both a key and a certificate when asked to produce a certificate. It does not offer OCSP or CRL services. Minica is appropriate, for instance, for generating certificates for RPC systems or microservices.
First, you need to install minica by following theseinstructions.
Once you have successfully installed on your machine, let’s create the certificates as follows assuming that we will test Zenoh over TLS onlocalhost.
First let’s create a folder to store our certificates:
```
$/home/user: mkdir tls
$/home/user: cd tls
$/home/user/tls: pwd
/home/user/tls
```

Then, let’s generate the TLS certificate for thelocalhostdomain:
```
$/home/user/tls: minica --domains localhost
```

This should create the following files:
```
$/home/user/tls: ls
localhost   minica-key.pem  minica.pem
```

minica.pemis the root CA certificate that will be used by the client to validate the server certificate.
The server certificatecert.pemand private keykey.pemcan be found inside thelocalhostfolder.
```
$/home/user/tls: ls localhost
cert.pem    key.pem
```

Once the above certificates have been correctly generated, we can proceed to configure Zenoh to use TLS as explained.
Since version 0.7.1-rc from Zenoh, we can generate certificates associated not only to dns domains but also to ip addresses as well. For instance, we can generate them as follows with minica:
```
$/home/user/server/tls: minica --ip-addresses 127.0.0.1
```

```
$/home/user/server/tls: ls
127.0.0.1   minica-key.pem  minica.pem
```

Then on the Zenoh configuration file we’ll be able to set up the TLS configuration specifying the ip address, for instance for a server and a client with tls:
```
{
  "mode": "router",
  "listen": {
    "endpoints": ["tls/127.0.0.1:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_private_key": "/home/user/server/127.0.0.1/key.pem",
        "listen_certificate": "/home/user/server/127.0.0.1/cert.pem"
      }
    }
  }
}
```

```
{
  "mode": "client",
  "connect": {
    "endpoints": ["tls/127.0.0.1:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/home/user/server/minica.pem"
      }
    }
  }
}
```
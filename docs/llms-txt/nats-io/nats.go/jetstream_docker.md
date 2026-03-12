# Source: https://docs.nats.io/running-a-nats-service/nats_docker/jetstream_docker.md

# JetStream

This mini-tutorial shows how to run a NATS server with JetStream enabled in a local Docker container. This enables quick and consequence-free experimentation with the many features of JetStream.

Using the official `nats` image, start a server. The `-js` option is passed to the server to enable JetStream. The `-p` option forwards your local 4222 port to the server inside the container, 4222 is the default client connection port.

```shell
docker run -p 4222:4222 nats -js
```

To persist JetStream data to a volume, you can use the `-v` option in combination with `-sd`:

```shell
docker run -p 4222:4222 -v nats:/data nats -js -sd /data
```

With the server running, use `nats bench` to create a stream and publish some messages to it.

```shell
nats bench -s localhost:4222 benchsubject --js --pub 1 --msgs=100000
```

JetStream persists the messages (on disk by default). Now consume them with:

```shell
nats bench -s localhost:4222 benchsubject --js --sub 3 --msgs=100000
```

You can use `nats` to inspect various aspects of the stream, for example:

```shell
nats -s localhost:4222 stream list
╭────────────────────────────────────────────────────────────────────────────────────╮
│                                       Streams                                      │
├─────────────┬─────────────┬─────────────────────┬──────────┬────────┬──────────────┤
│ Name        │ Description │ Created             │ Messages │ Size   │ Last Message │
├─────────────┼─────────────┼─────────────────────┼──────────┼────────┼──────────────┤
│ benchstream │             │ 2024-06-07 20:26:38 │ 100,000  │ 16 MiB │ 35s          │
╰─────────────┴─────────────┴─────────────────────┴──────────┴────────┴──────────────╯
```

### Related and useful:

* Official [Docker image for the NATS server on GitHub](https://github.com/nats-io/nats-docker) and [issues](https://github.com/nats-io/nats-docker/issues)
* [`nats` images on DockerHub](https://hub.docker.com/_/nats)
* [`nats` CLI tool](https://docs.nats.io/using-nats/nats-tools/nats_cli) and [`nats bench`](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/nats_cli/natsbench/README.md)
* [`Administer JetStream`](https://github.com/nats-io/nats.docs/blob/master/nats_admin/jetstream_admin/README.md)

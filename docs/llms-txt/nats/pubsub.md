# Source: https://docs.nats.io/nats-concepts/core-nats/pubsub.md

# Publish-Subscribe

## Publish-Subscribe

NATS implements a publish-subscribe message distribution model for one-to-many communication. A publisher sends a message on a subject and any active subscriber listening on that subject receives the message. Subscribers can also register interest in wildcard subjects that work a bit like a regular expression (but only a bit). This one-to-many pattern is sometimes called a fan-out.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-22d59af386038cc2717176561ffc95c63c295926%2Fpubsub.svg?alt=media\&token=cc54babb-76c4-4389-87fc-11e63429b341)

## Messages

Messages are composed of:

1. A subject.
2. A payload in the form of a byte array.
3. Any number of header fields.
4. An optional 'reply' address field.

Messages have a maximum size (which is set in the server configuration with `max_payload`). The size is set to 1 MB by default, but can be increased up to 64 MB if needed (though we recommend keeping the max message size to something more reasonable like 8 MB).

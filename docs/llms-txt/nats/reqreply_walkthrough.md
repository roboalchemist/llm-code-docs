# Source: https://docs.nats.io/nats-concepts/core-nats/reqreply/reqreply_walkthrough.md

# Request-Reply Walkthrough

NATS supports [request-reply](https://docs.nats.io/nats-concepts/core-nats/reqreply) messaging. In this tutorial you explore how to exchange point-to-point messages using NATS.

## Prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) the `nats` CLI Tool and optionally, the nats-server on your machine.

## Walkthrough

Start two terminal sessions. These will be used to run the NATS request and reply clients.

### In one terminal, run the reply client listener

```bash
nats reply help.please 'OK, I CAN HELP!!!'
```

You should see the message: *Listening on \[help.please]*

This means that the NATS receiver client is listening for request messages on the "help.please" subject. In NATS, the receiver is a subscriber.

### In the other terminal, run the request client

```bash
nats request help.please 'I need help!'
```

The NATS requestor client makes a request by sending the message "I need help!" on the “help.please” subject.

The NATS receiver client receives the message, formulates the reply ("OK, I CAN HELP!!!"), and sends it to the inbox of the requester.

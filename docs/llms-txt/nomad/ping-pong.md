# Source: https://docs.nomad.xyz/developers/application-developers/examples/ping-pong.md

# Ping Pong

{% hint style="warning" %}
The Ping Pong xApp is for reference only. Please do not deploy!
{% endhint %}

[The PingPong xApp](https://github.com/nomad-xyz/nomad-monorepo/tree/main/solidity/nomad-xapps/contracts/ping-pong) is capable of initiating PingPong "matches" between two chains. A match consists of "volleys" sent back-and-forth between the two chains via Nomad.

The first volley in a match is always a Ping volley.

* When a Router receives a Ping volley, it returns a Pong.
* When a Router receives a Pong volley, it returns a Ping.

The Routers keep track of the number of volleys in a given match, and emit events for each Sent and Received volley so that spectators can watch.

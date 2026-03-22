# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/events-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/events-api.md

# Events API

This API allows a client, not participating in consensus, to follow along with consensus in a trustless manner, by streaming and verifying events produced by consensus. It is especially useful for block builders, who need to maintain their own view of the internal consensus state at all times, so that they can intelligently propose blocks on top of not-yet-finalized proposed parent blocks.

{% hint style="warning" %}
This API is often served on a different port than other APIs, for reasons that will be resolved in future releases.
{% endhint %}

## Types

### `LeafInfo`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`LeafInfo`](https://hotshot.docs.espressosys.com/hotshot_types/event/struct.LeafInfo.html) type.

### `DAProposal`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`Proposal`](https://hotshot.docs.espressosys.com/hotshot_types/message/struct.Proposal.html) type.

### `QuorumProposal`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`Proposal`](https://hotshot.docs.espressosys.com/hotshot_types/message/struct.Proposal.html) type.

## Endpoints

### GET `/hotshot-events/events`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to consensus events.

#### Yields

```json
{
    "view_number": integer,
    "event":
        {
            "StartupInfo": {
                "known_node_with_stake": [
                    {
                    }
                ]
            }
        }
      | { "HotshotError": { "error": ... } }
      | { "HotshotTransactions": { "transactions": [Transaction] } }
      | {
            "HotshotDecide": {
                "leaf_chain": [LeafInfo],
                "block_size": null | integer
            }
        }
      | {
            "HotshotDAProposal": {
                "proposal": DAProposal,
                "sender": tagged<BLS_VER_KEY>
            }
        }
      | {
            "HotshotQuorumProposal": {
                "proposal": QuorumProposal,
                "sender": tagged<BLS_VER_KEY>
            }
        }
      | "Unknown"
}
```

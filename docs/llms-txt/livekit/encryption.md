# Source: https://docs.livekit.io/transport/encryption.md

LiveKit docs › Encryption › Overview

---

# Encryption overview

> Secure your realtime media and data with end-to-end encryption.

## Overview

LiveKit includes built-in support for end-to-end encryption (E2EE) for both realtime media tracks (audio and video) and data channels (text and byte streams). With E2EE enabled, content remains fully encrypted from sender to receiver, ensuring that no intermediaries (including LiveKit servers) can access or modify the content. This feature is:

- Available for both self-hosted and LiveKit Cloud customers at no additional cost.
- Ideal for regulated industries and security-critical applications.
- Designed to provide an additional layer of protection beyond standard transport encryption.

> ℹ️ **Security is our highest priority**
> 
> Learn more about [our comprehensive approach to security](https://livekit.io/security).

## Encryption components

LiveKit provides end-to-end encryption for both media and data:

| Component | Description | Use cases |
| **Media encryption** | Encrypts all audio and video tracks from all participants in a room, ensuring no intermediaries can access the content. | Regulated industries, security-critical applications, and privacy-focused use cases. |
| **Data channel encryption** | Encrypts all text messages, byte streams, and data packets sent between participants. | Secure chat applications, private file sharing, and encrypted data exchange. |

## How E2EE works

E2EE is enabled at the room level and automatically applied to all media tracks and data channels from all participants in that room. You must enable it within the LiveKit SDK for each participant. In many cases you can use a built-in key provider with a single shared key for the whole room. If you require unique keys for each participant, or key rotation during the lifetime of a single room, you can implement your own key provider.

## Key distribution

It is your responsibility to securely generate, store, and distribute encryption keys to your application at runtime. LiveKit does not (and cannot) store or transport encryption keys for you.

If using a shared key, you would typically generate it on your server at the same time that you create a room and distribute it securely to participants alongside their access token for the room. When using unique keys per participant, you may need a more sophisticated method for distributing keys as new participants join the room. Remember that the key is needed for both encryption and decryption, so even when using per-participant keys, you must ensure that all participants have all keys.

## Media encryption

E2EE is enabled at the room level and automatically applied to all media tracks from all participants in that room. You must enable it within the LiveKit SDK for each participant.

## Data channel encryption

Realtime data and text are encrypted using the `encryption` field for `RoomOptions` when you create a room. When the `encryption` field is set, all outgoing data messages (including text and byte streams) are end-to-end encrypted.

End-to-end encryption for data channel messages is the default. However, for backwards compatibility, the `e2ee` field is still supported. If `encryption` is not set, data channel messages are _not_ encrypted.

> ℹ️ **e2ee field is deprecated**
> 
> The `e2ee` field is deprecated and will be removed in the next major version of each client SDK. Use the `encryption` field instead.

> ❗ **Signaling messages and APIs**
> 
> Signaling messages (control messages used to coordinate a WebRTC session) and API calls are _not_ end-to-end encrypted—they're encrypted in transit using TLS, but the LiveKit server can still read them.

## In this section

Learn how to implement end-to-end encryption in your applications.

- **[Get started](https://docs.livekit.io/transport/encryption/start.md)**: Learn how to implement E2EE with step-by-step guides and code examples for all platforms.

---

This document was rendered at 2026-02-03T03:25:19.828Z.
For the latest version of this document, see [https://docs.livekit.io/transport/encryption.md](https://docs.livekit.io/transport/encryption.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).
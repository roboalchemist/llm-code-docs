# Source: https://io.net/docs/guides/confidential-inference/confidential-chat.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Confidential Chat

> io.net provides a web-based confidential chat interface where you can interact with AI models securely, with full privacy guarantees and verifiable attestation.

## Getting Started

### Step 1: Select a Secure Model

1. Navigate to [ai.io.net/ai/models](https://ai.io.net/ai/models)
2. Look for models with the **SECURE AI** badge
3. Click on a secure model to start a confidential chat session

<img src="https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=e8c2b9aa7c006109aa073937bf72372e" alt="Image" data-og-width="2434" width="2434" data-og-height="468" height="468" data-path="images/image-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?w=280&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=3260440435628cfee49cdc3d19ce7c10 280w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?w=560&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=3296946f2961024561fff86d090c434a 560w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?w=840&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=951135fc86be01ca36a6ddf72f1d7d6f 840w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?w=1100&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=23268cb44c085dbfd4a5bb110958c5a7 1100w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?w=1650&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=ee3f2c98f6925226912efbb1b38cbea6 1650w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-5.png?w=2500&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=69e395bd2e9aad6e63dfc4e96142f698 2500w" />

### Step 2: Start Chatting Privately

Once you select a secure model, you enter a private chat session with the following guarantees:

* **Messages are never saved** - your conversation is not stored on any server
* **No observation** - io.net staff cannot see your prompts or responses
* **Session-only context** - only the current chat is passed to the LLM for context
* **End-to-end verification** - every response is cryptographically signed

## Privacy Guarantees

| Feature           | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| Zero storage      | Messages exist only in your browser and the TEE during processing |
| No logging        | Conversation content is never written to logs                     |
| Session isolation | Each chat session is independent and ephemeral                    |
| Signed responses  | Every AI response includes a cryptographic signature              |

## Verifying Attestation and Signatures

Every message in a confidential chat can be verified. Click the **Secure AI** label under any AI response to open the verification panel.

<img src="https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=650d955fbe5e63ae9c10f210b6db6f1b" alt="Image" data-og-width="960" width="960" data-og-height="2238" height="2238" data-path="images/image-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?w=280&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=b9c37a2c7e1cbf11c4d76008755d2fd6 280w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?w=560&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=79bda202342dba11b61c611640119bf5 560w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?w=840&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=41bd009bd942d83138fa0aa8ceb7bd0c 840w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?w=1100&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=22af150b10836ac51aa4fdab7304ede2 1100w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?w=1650&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=62e75a61993f188691fef386af9d1e92 1650w, https://mintcdn.com/ionet-cca8037f/MQC9Ah7E57sayqgo/images/image-6.png?w=2500&fit=max&auto=format&n=MQC9Ah7E57sayqgo&q=85&s=36f660eb9863b01346e594fcd0335640 2500w" />

### Attestation Report

The verification panel displays the full attestation report, proving:

* The response came from a genuine NVIDIA GPU running in TEE mode
* The specific hardware configuration and firmware version
* The container image hash (`image_digest`) running inside the secure enclave - compare with the expected digest from the [latest official release](https://github.com/ionet-official/attestation-agent/releases) to confirm the container hasn't been tampered with

### Message Signatures

For each AI response, you can view:

| Field               | Description                                           |
| ------------------- | ----------------------------------------------------- |
| **Signed Text**     | The exact content that was signed                     |
| **Signature**       | The cryptographic signature proving authenticity      |
| **Signing Address** | The public key that signed (matches attestation)      |
| **Algorithm**       | The signing algorithm used (e.g., ecdsa)              |
| **Image digest**    | SHA256 hash of the container image running in the TEE |

This allows you to independently verify that:

1. The response was generated by the attested hardware
2. The content was not modified after generation
3. The signing key matches the attestation report

## Best Practices

### For Maximum Privacy

* **Start fresh sessions** for sensitive topics
* **Verify signatures** for critical responses
* **Check attestation** to confirm hardware authenticity
* **Clear your browser** after sensitive sessions

### Understanding Session Context

Since messages are not saved:

* The AI only has context from the current session
* New chat starts a new session with no history
* You cannot retrieve previous confidential conversations

This is by design - true privacy means no persistent storage.

## What's Next

* [Quick Start API](./quick-start) - For developers building integrations
* [Verification Guide](./verification-guide) - Deep dive into verifying attestation and signatures

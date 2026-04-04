# Source: https://docs.meshconnect.com/advanced/customer-managed-tokens.md

# Client Managed Tokens (CMT)

> This guide explains how to implement Client Managed Tokens (CMT), our recommended approach for handling user authentication to create a secure and seamless return user experience.

## **What are Client Managed Tokens?**

Client Managed Tokens is the model where **your application** takes responsibility for securely storing and managing the `auth_token` and `refreshToken` that are returned after a user connects their account through Mesh Link.

This is the key to enabling the "Seamless Return Experience," where a user who has connected their account once does not need to log in again for future transactions.

## **Why is CMT the Recommended Approach?**

We strongly recommend that clients manage their own tokens for a crucial reason: **security**. By storing the tokens on your own secure backend, you maintain full control over your users' data and connections. This aligns with security best practices and prevents Mesh from becoming a "honeypot," which would be a centralized target for potential attacks.

## **How to Implement Client Managed Tokens: A Step-by-Step Guide**

Implementing CMT involves a five-step process that covers capturing, storing, and utilizing the tokens.

### **Step 1: Get Tokens from the SDK**

Use the `onIntegrationConnected()` SDK callback function to capture the `accessTokenPayload` after the user successfully connects their account. You will need to capture and store the following key fields:

* `accessToken`
* `refreshToken`
* `expiresInSeconds`
* `refreshTokenExpiresInSeconds`
* `brokerType`
* `brokerName`

### **Step 2: Associate Tokens with a User**

On your backend, you must associate the set of tokens you just received with a unique identifier for that specific user in your system. This is a critical step to ensure that you only ever use a token for the correct user and do not mix up account data.

### **Step 3: Store Tokens Securely**

It is essential to store the tokens with the utmost security. The tokens should be stored in a secure and encrypted storage layer on your backend, such as a key management system (KMS) or an encrypted database.

> 🔒 Security First
>
> Never store auth\_token or refreshToken in an insecure location, especially on the client side (e.g., in browser local storage) for production applications.

### **Step 4: Implement Token Refresh Logic**

Some tokens, particularly from OAuth integrations like Coinbase, will expire. To maintain a persistent connection, you must implement logic on your backend to refresh them.

1. Check if the `expiresInSeconds` value is present. If it is, you need to refresh the `accessToken` before it expires.
2. Record the timestamp when the token was obtained.
3. Before that timestamp plus `expiresInSeconds` occurs, make a `POST` request to the `/api/v1/token/refresh` endpoint, including the `refreshToken`, to get a new `accessToken`.
4. If a `refreshTokenExpiresInSeconds` is also provided, implement the same logic for the `refreshToken` itself.

> **Note:** It is considered bad practice to wait for a `401 Unauthorized` error before refreshing a token. Proactive refreshing provides a much better user experience.

### **Step 5: Pass Tokens to the SDK for Return Users**

The next time the same user initiates a transaction, you will pass their stored and valid `accessToken` in the `accessTokens` parameter when you initialize the Link SDK. This will bypass the authentication step and take the user directly to the transfer flow, creating a seamless, one-click experience.

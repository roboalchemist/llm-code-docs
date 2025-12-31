# Source: https://docs.venice.ai/overview/guides/generating-api-key-agent.md

# Autonomous Agent API Key Creation

Autonomous AI Agents can programmatically access Venice.ai's APIs without any human interaction using the "api\_keys" endpoint. AI Agents are now able to manage their own wallets on the BASE blockchain, allowing them to programmatically acquire and stake VVV token to earn a daily Diem inference allocation. Venice's new API endpoint allows them to automate further by generating their own API key.&#x20;

To autonomously generate an API key within an agent, you must:

<Steps>
  <Step title="Acquire VVV">
    The agent will need VVV token to complete this process. This can be achieved by sending tokens directly to the agent wallet, or having the agent swap on a Decentralized Exchange (DEX), like [Aerodrome](https://aerodrome.finance/swap?from=eth\&to=0xacfe6019ed1a7dc6f7b508c02d1b04ec88cc21bf\&chain0=8453\&chain1=8453) or [Uniswap](https://app.uniswap.org/swap?chain=base\&inputCurrency=NATIVE\&outputCurrency=0xacfe6019ed1a7dc6f7b508c02d1b04ec88cc21bf).
  </Step>

  <Step title="Stake VVV with Venice">
    Once funded, the agent will need to stake the VVV tokens within the [Venice Staking Smart Contract](https://basescan.org/address/0x321b7ff75154472b18edb199033ff4d116f340ff#code). To accomplish this you first must approve VVV tokens for staking, then execute a "stake" transaction.&#x20;

    <Frame as="div">
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6a2180bbdc58f95990e99568d7015bbc" alt="Smart Contract Staking" data-og-width="812" width="812" data-og-height="324" height="324" data-path="images/guides/SC-Stake.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=64d66069edc7f3060c1046bef50a2a18 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=b8e22d317889626cf500e3355e1b2b45 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=131a37bcfb65773721f179340ce2a390 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6b6c2ffa9d7d32c41b4e389f7b4747b3 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=91c6003ebbce068d5724090802f5be30 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6c46ebbf0b5bc252ede57a11b096c71d 2500w" />
    </Frame>

    When the transaction is complete, you will see the VVV tokens exit the wallet and sVVV tokens returned to your wallet. This indicates a successful stake.&#x20;
  </Step>

  <Step title="Obtain Validation Token">
    To generate an API key, you need to first obtain your validation token. You can get this by calling this [API endpoint ](https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get)`https://api.venice.ai/api/v1/api_keys/generate_web3_key` . The API response will provide you with a "token".&#x20;

    Here is an example request:

    ```
    curl --request GET \
      --url https://api.venice.ai/api/v1/api_keys/generate_web3_key
    ```
  </Step>

  <Step title="Sign for Wallet Validation">
    Sign the token with the wallet holding VVV to complete the association between the wallet and token.&#x20;
  </Step>

  <Step title="Generate API Key">
    Now you can call this same [API endpoint](https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get) `https://api.venice.ai/api/v1/api_keys/generate_web3_key` to create your API key.&#x20;

    You will need the following information to proceed, which is described further within the "[Generating API Key Guide](https://docs.venice.ai/overview/guides/generating-api-key)":

    * API Key Type: Inference or Admin

    * ConsumptionLimit: To be used if you want to limit the API key usage

    * Signature: The signed token from step 4

    * Token: The unsigned token from step 3

    * Address: The agent's wallet address

    * Description: String to describe your API Key

    * ExpiresAt: Option to set an expiration date for the API key (empty for no expiration)

    Here is an example request:

    ```
    curl --request POST \
      --url https://api.venice.ai/api/v1/api_keys/generate_web3_key \
      --header 'Authorization: Bearer ' \
      --header 'Content-Type: application/json' \
      --data '{
      "description": "Web3 API Key",
      "apiKeyType": "INFERENCE",
      "signature": "<signed token>",
      "token": "<unsigned token>",
      "address": "<wallet address>",
      "consumptionLimit": {
        "diem": 1
      }
    }'
    ```
  </Step>
</Steps>

Example code to interact with this API can be found below:

```
import { ethers } from "ethers";

// NOTE: This is an example. To successfully generate a key, your address must be holding
// and staking VVV.
const wallet = ethers.Wallet.createRandom()
const address = wallet.address
console.log("Created address:", address)

// Request a JWT from Venice's API
const response = await fetch('https://api.venice.ai/api/v1/api_keys/generate_web3_key')
const token = (await response.json()).data.token
console.log("Validation Token:", token)

// Sign the token with your wallet and pass that back to the API to generate an API key
const signature = await wallet.signMessage(token)
const postResponse = await fetch('https://api.venice.ai/api/v1/api_keys/generate_web3_key', {
  method: 'POST',
  body: JSON.stringify({
    address,
    signature,
    token,
    apiKeyType: 'ADMIN'
  })
})

await postResponse.json()
```

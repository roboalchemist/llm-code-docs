<!--
source: https://desearch.ai/docs/guide/integrations/numinous-sn6
title: Numinous SN6 × Desearch Integration - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# Numinous SN6 × Desearch Integration - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/numinous-sn6

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
Numinous SN6 × Desearch Integration

Secure Miner → Account Linking & Request Authentication

This guide explains how Subnet-6 miners and validators authenticate with Desearch APIs using cryptographic signatures.
🔐 Miners
Connect a Miner’s Coldkey to a Desearch Account

Before a Subnet-6 miner can use Desearch APIs, their coldkey must be cryptographically linked to their DeSearch account.
This proves ownership and authorizes all miners (hotkeys) that belong to that coldkey.

Prerequisites
Register at: https://console.desearch.ai
Generate a Desearch API Key
Have your Bittensor coldkey wallet available
How It Works
You sign your Desearch API key using your coldkey
Desearch verifies this signature against the coldkey’s public SS58 address
This establishes a coldkey → account link
After linking, you may generate new API keys — the coldkey stays attached to the account
You can update coldkey to new account by running with new API key.
🧩 Linking Miner's Coldkey to Desearch (One-time)

PYTHON
import requests
from bittensor_wallet import Wallet

API_KEY = "DESEARCH_API_KEY"
WALLET_NAME = "my_wallet"
WALLET_PASSWORD = "my_password"

# Load Bittensor wallet and coldkey
wallet = Wallet(name=WALLET_NAME)
keypair = wallet.get_coldkey(WALLET_PASSWORD)

coldkey_ss58 = keypair.ss58_address
print(f"Using coldkey: {coldkey_ss58}")

# Sign the Desearch API key with your coldkey private key
signature_bytes = keypair.sign(API_KEY.encode("utf-8"))
signature_hex = signature_bytes.hex()

# Prepare request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "coldkey_ss58": coldkey_ss58,
    "signature_hex": signature_hex,
}

# Call Desearch API
url = "https://api.desearch.ai/bt/miner/link"
print("Linking miner to Desearch account...")

response = requests.post(url, json=payload, headers=headers)

print(f"\nResponse from /bt/miner/link [{response.status_code}]:")
print(response.text)

🔑 Authenticating Requests as a Subnet-6 Miner

Miners should sign code with their hotkey and send signature back to validator.

PYTHON
from bittensor_wallet import Wallet

# Load bittensor wallet
wallet = Wallet(name="my_wallet", hotkey="default")

CODE = "SIGNING_CODE_HERE"

# Sign code with hotkey
keypair = wallet.get_hotkey()
signature_bytes = keypair.sign(CODE.encode("utf-8"))
signature_hex = signature_bytes.hex()

print(f"Signature (hex): {signature_hex}\n")

Along with the code, send signature back to the validator.

🛡️ Validators
Authenticating Desearch Requests as a Validator

Validators must authenticate both themselves and forward miner credentials when calling Desearch APIs.

To authenticate as a validator, sign the current timestamp with your validator hotkey and include it in the request headers.

PYTHON
from datetime import datetime, timezone
from bittensor_wallet import Wallet

# Sign timestamp with validator hotkey
wallet = Wallet(name="validator", hotkey="default")
keypair = wallet.get_hotkey()
validator_timestamp = datetime.now(timezone.utc).isoformat()
validator_signature = keypair.sign(validator_timestamp.encode("utf-8")).hex()
validator_hotkey = keypair.ss58_address

# Replace Desearch headers with miner + validator info
headers = {
    "X-Validator-Hotkey": validator_hotkey,
    "X-Validator-Signature": validator_signature,
    "X-Validator-Timestamp": validator_timestamp,

    # Forward miner signature info
    "X-Miner-Signature": 'signature',
    "X-Miner-Code": 'code',
    "X-Miner-Hotkey": 'hotkey',
    "X-Miner-Coldkey": 'coldkey',
}

response = requests.get(
    "https://api.desearch.ai/twitter",
    headers=headers,
    params={"query": "crypto", "sort": "Top", "count": 20},
)

print(response.status_code, response.text)

Timestamp Validation

Validator timestamps must be:

In ISO 8601 format with timezone (UTC)
Within ±5 minutes of time
Unique per request
What Desearch Verifies

For every API request, Desearch validates:

Validator Authentication

✅ Validator hotkey is whitelisted in the subnet
✅ Validator signature matches the timestamp
✅ Timestamp is within 5 minutes

Miner Authentication

✅ Miner signature is valid for the provided code
✅ Miner's coldkey is linked to a Desearch account
✅ Miner's hotkey belongs to the linked coldkey
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All

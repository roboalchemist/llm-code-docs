# Source: https://docs.drip.re/developer/credentials.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Ghost Credentials

> Pre-credit users before they connect with ghost credentials

Ghost credentials allow you to create identity records and assign points to users before they've connected to your realm. This is powerful for pre-seeding rewards, running off-platform campaigns, or migrating users from external systems.

## Overview

A **ghost credential** is a non-verified identity record (Twitter ID, wallet address, email, etc.) that can accumulate point balances independently. When the user eventually connects that identity to your realm, the ghost credential is linked to their account and all accumulated balances are transferred.

<Info>
  Ghost credentials are realm-specific. The same Twitter ID can exist as separate ghost credentials in different realms, each with their own point balances.
</Info>

### Use Cases

<CardGroup cols={2}>
  <Card title="Pre-Credit Campaigns" icon="bullhorn">
    Award points to Twitter followers or wallet holders before they join your community
  </Card>

  <Card title="Off-Platform Activity" icon="arrow-up-right-from-square">
    Track and reward activity that happens outside your realm (external events, partnerships)
  </Card>

  <Card title="User Migration" icon="arrows-rotate">
    Import users from external systems with their pre-existing point balances
  </Card>

  <Card title="Email Onboarding" icon="envelope">
    Assign welcome bonuses to email addresses before users complete signup
  </Card>
</CardGroup>

## Credential Types

Ghost credentials support multiple identity formats:

| Type         | Description                           | Example Value                                |
| ------------ | ------------------------------------- | -------------------------------------------- |
| `twitter-id` | Twitter/X user ID                     | `1234567890`                                 |
| `discord-id` | Discord user ID                       | `123456789012345678`                         |
| `wallet`     | Blockchain wallet address             | `0x742d35Cc6634C0532925a3b844Bc454e4438f44e` |
| `email`      | Email address                         | `user@example.com`                           |
| `custom`     | Custom identifier (requires `source`) | `customer_12345`                             |

## Creating Credentials

### Social Credentials

Create credentials for social platform identities like Twitter or Discord:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function createTwitterCredential(realmId, twitterId, username) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/social`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          provider: 'twitter',
          providerId: twitterId,
          username: username
        })
      }
    );

    return response.json();
  }

  // Create a ghost credential for a Twitter user
  const credential = await createTwitterCredential(
    'YOUR_REALM_ID',
    '1234567890',
    'twitter_handle'
  );

  ```

  ```python Python theme={"dark"}
  import requests
  import os

  def create_twitter_credential(realm_id, twitter_id, username):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/social"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {
          'provider': 'twitter',
          'providerId': twitter_id,
          'username': username
      }
      
      response = requests.post(url, headers=headers, json=data)
      return response.json()

  # Create a ghost credential for a Twitter user
  credential = create_twitter_credential(
      'YOUR_REALM_ID',
      '1234567890',
      'twitter_handle'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X POST "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/social" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "provider": "twitter",
      "providerId": "1234567890",
      "username": "twitter_handle"
    }'
  ```

</CodeGroup>

### Wallet Credentials

Create credentials for blockchain wallet addresses:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function createWalletCredential(realmId, address, chain) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/wallet`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          address: address,
          chain: chain
        })
      }
    );

    return response.json();
  }

  // Create a ghost credential for an Ethereum wallet
  const credential = await createWalletCredential(
    'YOUR_REALM_ID',
    '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
    'ethereum'
  );

  ```

  ```python Python theme={"dark"}
  def create_wallet_credential(realm_id, address, chain):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/wallet"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {
          'address': address,
          'chain': chain
      }
      
      response = requests.post(url, headers=headers, json=data)
      return response.json()

  # Create a ghost credential for an Ethereum wallet
  credential = create_wallet_credential(
      'YOUR_REALM_ID',
      '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
      'ethereum'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X POST "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/wallet" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
      "chain": "ethereum"
    }'
  ```

</CodeGroup>

## Finding Credentials

Look up existing ghost credentials by their identifier:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function findCredential(realmId, type, value) {
    const params = new URLSearchParams({ type, value });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/find?${params}`,
      {
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`
        }
      }
    );
    
    if (response.status === 404) {
      return null; // Credential doesn't exist
    }
    
    return response.json();
  }

  // Find by Twitter ID
  const twitterCred = await findCredential('YOUR_REALM_ID', 'twitter-id', '1234567890');

  // Find by wallet address
  const walletCred = await findCredential('YOUR_REALM_ID', 'wallet', '0x742d35Cc...');

  // Find by email
  const emailCred = await findCredential('YOUR_REALM_ID', 'email', 'user@example.com');

  ```

  ```python Python theme={"dark"}
  def find_credential(realm_id, cred_type, value):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/find"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}'
      }
      
      params = {
          'type': cred_type,
          'value': value
      }
      
      response = requests.get(url, headers=headers, params=params)
      
      if response.status_code == 404:
          return None
      
      return response.json()

  # Find by Twitter ID
  twitter_cred = find_credential('YOUR_REALM_ID', 'twitter-id', '1234567890')
  ```

  ```bash cURL theme={"dark"}
  # Find by Twitter ID
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/find?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY"

  # Find by wallet
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/find?type=wallet&value=0x742d35Cc..." \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

## Managing Balances

### Update Balance

Award or deduct points from a ghost credential:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function updateCredentialBalance(realmId, type, value, amount, realmPointId = null) {
    const params = new URLSearchParams({ type, value });

    const body = { amount };
    if (realmPointId) {
      body.realmPointId = realmPointId;
    }
    
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/balance?${params}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      }
    );
    
    return response.json();
  }

  // Award 100 points to a Twitter user (uses default currency)
  await updateCredentialBalance('YOUR_REALM_ID', 'twitter-id', '1234567890', 100);

  // Deduct 50 points from a wallet
  await updateCredentialBalance('YOUR_REALM_ID', 'wallet', '0x742d35Cc...', -50);

  // Award 200 of a specific currency
  await updateCredentialBalance('YOUR_REALM_ID', 'email', 'user@example.com', 200, 'CURRENCY_ID');

  ```

  ```python Python theme={"dark"}
  def update_credential_balance(realm_id, cred_type, value, amount, realm_point_id=None):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/balance"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      params = {
          'type': cred_type,
          'value': value
      }
      
      data = {'amount': amount}
      if realm_point_id:
          data['realmPointId'] = realm_point_id
      
      response = requests.patch(url, headers=headers, params=params, json=data)
      return response.json()

  # Award 100 points to a Twitter user
  update_credential_balance('YOUR_REALM_ID', 'twitter-id', '1234567890', 100)
  ```

  ```bash cURL theme={"dark"}
  # Award 100 points to a Twitter user
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/balance?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"amount": 100}'
  ```

</CodeGroup>

<Info>
  If `realmPointId` is not specified, the realm's default currency is used.
</Info>

### Batch Updates

Update multiple credentials in a single request:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function batchUpdateBalances(realmId, updates) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/transaction`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ updates })
      }
    );

    return response.json();
  }

  // Batch award points to multiple credentials
  const result = await batchUpdateBalances('YOUR_REALM_ID', [
    { type: 'twitter-id', value: '1234567890', amount: 100 },
    { type: 'twitter-id', value: '9876543210', amount: 150 },
    { type: 'wallet', value: '0x742d35Cc...', amount: 200 },
    { type: 'email', value: 'user@example.com', amount: 75 }
  ]);

  console.log(`Success: ${result.results.length}, Errors: ${result.errors.length}`);

  ```

  ```python Python theme={"dark"}
  def batch_update_balances(realm_id, updates):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/transaction"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {'updates': updates}
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Batch award points
  result = batch_update_balances('YOUR_REALM_ID', [
      {'type': 'twitter-id', 'value': '1234567890', 'amount': 100},
      {'type': 'twitter-id', 'value': '9876543210', 'amount': 150},
      {'type': 'wallet', 'value': '0x742d35Cc...', 'amount': 200}
  ])
  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/transaction" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "updates": [
        {"type": "twitter-id", "value": "1234567890", "amount": 100},
        {"type": "twitter-id", "value": "9876543210", "amount": 150},
        {"type": "wallet", "value": "0x742d35Cc...", "amount": 200}
      ]
    }'
  ```

</CodeGroup>

### Transfer Points

Transfer points between two credentials:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function transferPoints(realmId, from, to, amount, realmPointId = null) {
    const params = new URLSearchParams({
      fromType: from.type,
      fromValue: from.value,
      toType: to.type,
      toValue: to.value
    });

    const body = { amount };
    if (realmPointId) {
      body.realmPointId = realmPointId;
    }
    
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/transfer?${params}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      }
    );
    
    return response.json();
  }

  // Transfer 50 points from one Twitter user to another
  await transferPoints(
    'YOUR_REALM_ID',
    { type: 'twitter-id', value: '1234567890' },
    { type: 'twitter-id', value: '9876543210' },
    50
  );

  // Transfer points from a wallet to an email
  await transferPoints(
    'YOUR_REALM_ID',
    { type: 'wallet', value: '0x742d35Cc...' },
    { type: 'email', value: 'user@example.com' },
    100
  );

  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/transfer?fromType=twitter-id&fromValue=1234567890&toType=twitter-id&toValue=9876543210" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"amount": 50}'
  ```

</CodeGroup>

## Linking to Accounts

When a user connects their identity to your realm, you can link the ghost credential to their account. This transfers all accumulated balances to their account.

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function linkCredentialToAccount(realmId, type, value, accountId) {
    const params = new URLSearchParams({ type, value, accountId });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/link?${params}`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`
        }
      }
    );
    
    if (response.status === 204) {
      return { success: true };
    }
    
    return response.json();
  }

  // Link a Twitter credential to a user's account
  await linkCredentialToAccount(
    'YOUR_REALM_ID',
    'twitter-id',
    '1234567890',
    'ACCOUNT_ID'
  );

  ```

  ```python Python theme={"dark"}
  def link_credential_to_account(realm_id, cred_type, value, account_id):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/link"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}'
      }
      
      params = {
          'type': cred_type,
          'value': value,
          'accountId': account_id
      }
      
      response = requests.post(url, headers=headers, params=params)
      return response.status_code == 204

  # Link a Twitter credential to a user's account
  link_credential_to_account(
      'YOUR_REALM_ID',
      'twitter-id',
      '1234567890',
      'ACCOUNT_ID'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X POST "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/link?type=twitter-id&value=1234567890&accountId=ACCOUNT_ID" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

<Warning>
  Linking is a one-way operation. Once linked, ghost balances are transferred to the account and the credential cannot be unlinked. The credential will still exist but future balance updates will go directly to the account.
</Warning>

### What Happens When Linking

1. Ghost credential is found by identifier
2. All `GhostCredentialPointBalance` records are transferred to `AccountPointBalance`
3. Ghost balance records are deleted
4. Credential gets `accountId` set
5. If the account has a verified credential with the same identity, the ghost credential can auto-upgrade to verified

## Metadata

Store custom data on credentials for your application's needs:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function updateCredentialMetadata(realmId, type, value, metadata) {
    const params = new URLSearchParams({ type, value });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/metadata?${params}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ metadata })
      }
    );
    
    return response.status === 204;
  }

  // Store custom metadata
  await updateCredentialMetadata(
    'YOUR_REALM_ID',
    'twitter-id',
    '1234567890',
    {
      source: 'airdrop_campaign_2024',
      tier: 'gold',
      referredBy: 'partner_xyz'
    }
  );

  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/metadata?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "metadata": {
        "source": "airdrop_campaign_2024",
        "tier": "gold",
        "referredBy": "partner_xyz"
      }
    }'
  ```

</CodeGroup>

<Info>
  Metadata is returned when finding credentials and can be used to track campaign attribution, user segments, or any custom data your application needs.
</Info>

## Deleting Credentials

Remove ghost credentials that are no longer needed:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function deleteCredential(realmId, type, value) {
    const params = new URLSearchParams({ type, value });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials?${params}`,
      {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`
        }
      }
    );
    
    return response.status === 204;
  }

  // Delete a ghost credential
  await deleteCredential('YOUR_REALM_ID', 'twitter-id', '1234567890');

  ```

  ```bash cURL theme={"dark"}
  curl -X DELETE "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

<Warning>
  You cannot delete credentials that have non-zero point balances. Zero out the balance first or link the credential to transfer the balance.
</Warning>

## Custom Credential Types

For identifiers that don't fit the standard types, use the `custom` type with a `source` parameter:

```javascript  theme={"dark"}
// Create a custom credential (e.g., Shopify customer ID)
const response = await fetch(
  `https://api.drip.re/api/v1/realms/${realmId}/credentials/social`,
  {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      provider: 'shopify',  // Your custom source
      providerId: 'customer_12345',
      username: 'Customer Name'
    })
  }
);

// Find by custom type
const credential = await findCredential('YOUR_REALM_ID', 'custom', 'customer_12345');
// Note: For custom types, include source parameter:
// ?type=custom&value=customer_12345&source=shopify
```

## Best Practices

<CardGroup cols={2}>
  <Card title="Batch Operations" icon="layer-group">
    Use batch endpoints when updating multiple credentials to reduce API calls and improve performance
  </Card>

  <Card title="Idempotent Creates" icon="repeat">
    Creating a credential that already exists returns a 409 Conflict - check first or handle the error
  </Card>

  <Card title="Track Attribution" icon="tag">
    Use metadata to track where credentials came from (campaigns, partners, events)
  </Card>

  <Card title="Clean Up" icon="broom">
    Periodically review and delete unused credentials with zero balances
  </Card>
</CardGroup>

## Error Handling

Common errors and how to handle them:

| Error                             | Cause                                | Solution                                     |
| --------------------------------- | ------------------------------------ | -------------------------------------------- |
| `409 Conflict`                    | Credential already exists            | Find existing credential instead of creating |
| `404 Not Found`                   | Credential doesn't exist             | Create the credential first                  |
| `400 INSUFFICIENT_BALANCE`        | Trying to deduct more than available | Check balance before deducting               |
| `400 CANNOT_DELETE_WITH_BALANCES` | Credential has non-zero balance      | Zero out balance or link first               |

## Next Steps

<CardGroup cols={3}>
  <Card title="Member Management" icon="users" href="/developer/managing-members">
    Learn how to manage verified realm members
  </Card>

  <Card title="Point Systems" icon="coins" href="/developer/point-systems">
    Design effective point economies
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Explore the complete API documentation
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).

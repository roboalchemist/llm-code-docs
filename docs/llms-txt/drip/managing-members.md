# Source: https://docs.drip.re/developer/managing-members.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Member Management

> Search, update, and manage community members like a pro 👥

This guide covers everything you need to know about managing members in your DRIP realm, from searching and retrieving member data to updating balances and transferring points.

## Overview

Member management is one of the most common use cases for the DRIP API. You can:

* Search for members using various identifiers
* Retrieve detailed member information and balances
* Update individual or multiple member point balances
* Transfer points between members
* Track member activity and engagement

## Searching Members

### Search by Different Identifiers

The member search endpoint allows you to find members using various identifiers:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function searchMembers(realmId, searchType, values) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/search?type=${searchType}&values=${values}`,
      {
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        }
      }
    );

    return response.json();
  }

  // Search by Discord ID
  const discordMembers = await searchMembers('YOUR_REALM_ID', 'discord-id', '123456789012345678');

  // Search by multiple wallet addresses
  const walletMembers = await searchMembers(
    'YOUR_REALM_ID',
    'wallet',
    '0x742d35Cc6634C0532925a3b8D23,0x8ba1f109551bD432803012645Hac136c'
  );

  ```

  ```python Python theme={"dark"}
  import requests

  def search_members(realm_id, search_type, values):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/search"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      params = {
          'type': search_type,
          'values': values
      }
      
      response = requests.get(url, headers=headers, params=params)
      return response.json()

  # Search by email
  email_members = search_members('YOUR_REALM_ID', 'email', 'user@example.com')

  # Search by multiple usernames
  username_members = search_members('YOUR_REALM_ID', 'username', 'gamer1,gamer2,gamer3')
  ```

  ```bash cURL theme={"dark"}
  # Search by Discord ID
  curl -X GET "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/search?type=discord-id&values=123456789012345678" \
    -H "Authorization: Bearer YOUR_API_KEY"

  # Search by multiple DRIP IDs
  curl -X GET "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/search?type=drip-id&values=507f1f77bcf86cd799439013,507f1f77bcf86cd799439014" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

### Search Types and Examples

| Search Type  | Description             | Value Format                    |
| ------------ | ----------------------- | ------------------------------- |
| `drip-id`    | Internal DRIP member ID | `507f1f77bcf86cd799439013`      |
| `discord-id` | Discord user ID         | `123456789012345678`            |
| `twitter-id` | Twitter/X user ID       | `987654321`                     |
| `wallet`     | Crypto wallet address   | `0x742d35Cc6634C0532925a3b8D23` |
| `email`      | Email address           | `user@example.com`              |
| `username`   | Display username        | `gamerpro123`                   |

<Info>
  You can search for multiple values at once by separating them with commas. For example: `values=user1,user2,user3`
</Info>

## Updating Member Balances

### Single Member Balance Update

Update a specific member's point balance:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function updateMemberBalance(realmId, memberId, tokens, realmPointId = null) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/${memberId}/point-balance`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tokens: tokens,
          ...(realmPointId && { realmPointId })
        })
      }
    );

    return response.json();
  }

  // Award 100 points to a member
  const result = await updateMemberBalance('YOUR_REALM_ID', 'MEMBER_ID', 100);

  // Award 50 points of a specific currency
  const specificResult = await updateMemberBalance(
    'YOUR_REALM_ID',
    'MEMBER_ID',
    50,
    'REALM_POINT_ID'
  );

  ```

  ```python Python theme={"dark"}
  def update_member_balance(realm_id, member_id, tokens, realm_point_id=None):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/{member_id}/point-balance"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {'tokens': tokens}
      if realm_point_id:
          data['realmPointId'] = realm_point_id
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Deduct 25 points from a member
  result = update_member_balance('YOUR_REALM_ID', 'MEMBER_ID', -25)
  ```

  ```bash cURL theme={"dark"}
  # Award 100 points
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/MEMBER_ID/point-balance" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"tokens": 100}'

  # Deduct 50 points of specific currency
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/MEMBER_ID/point-balance" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"tokens": -50, "realmPointId": "REALM_POINT_ID"}'
  ```

</CodeGroup>

### Batch Balance Updates

Update multiple members' balances in a single API call:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function batchUpdateBalances(realmId, updates) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/transaction`,
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

  // Update multiple members at once
  const updates = [
    { memberId: 'MEMBER_ID_1', tokens: 100 },
    { memberId: 'MEMBER_ID_2', tokens: 150, realmPointId: 'SPECIFIC_POINT_ID' },
    { memberId: 'MEMBER_ID_3', tokens: -25 } // Deduct points
  ];

  const batchResult = await batchUpdateBalances('YOUR_REALM_ID', updates);

  ```

  ```python Python theme={"dark"}
  def batch_update_balances(realm_id, updates):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/transaction"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {'updates': updates}
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Batch update example
  updates = [
      {'memberId': 'MEMBER_ID_1', 'tokens': 200},
      {'memberId': 'MEMBER_ID_2', 'tokens': 100, 'realmPointId': 'SPECIFIC_POINT_ID'},
      {'memberId': 'MEMBER_ID_3', 'tokens': 75}
  ]

  batch_result = batch_update_balances('YOUR_REALM_ID', updates)
  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/transaction" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "updates": [
        {"memberId": "MEMBER_ID_1", "tokens": 100},
        {"memberId": "MEMBER_ID_2", "tokens": 150, "realmPointId": "SPECIFIC_POINT_ID"},
        {"memberId": "MEMBER_ID_3", "tokens": -25}
      ]
    }'
  ```

</CodeGroup>

<Warning>
  Batch updates are atomic - if any single update fails, the entire batch is rolled back. This ensures data consistency.
</Warning>

## Transferring Points Between Members

Transfer points directly from one member to another:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function transferPoints(realmId, senderId, recipientId, tokens, realmPointId) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/${senderId}/transfer`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tokens,
          recipientId,
          realmPointId
        })
      }
    );

    return response.json();
  }

  // Transfer 50 points from one member to another
  const transfer = await transferPoints(
    'YOUR_REALM_ID',
    'SENDER_MEMBER_ID',
    'RECIPIENT_MEMBER_ID',
    50,
    'REALM_POINT_ID'
  );

  ```

  ```python Python theme={"dark"}
  def transfer_points(realm_id, sender_id, recipient_id, tokens, realm_point_id):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/{sender_id}/transfer"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {
          'tokens': tokens,
          'recipientId': recipient_id,
          'realmPointId': realm_point_id
      }
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Transfer example
  transfer = transfer_points(
      'YOUR_REALM_ID',
      'SENDER_MEMBER_ID',
      'RECIPIENT_MEMBER_ID',
      100,
      'REALM_POINT_ID'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/SENDER_MEMBER_ID/transfer" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "tokens": 50,
      "recipientId": "RECIPIENT_MEMBER_ID",
      "realmPointId": "REALM_POINT_ID"
    }'
  ```

</CodeGroup>

## Common Use Cases

### Activity-Based Rewards

Automatically reward members for various activities:

```javascript  theme={"dark"}
// Reward system for different activities
const ACTIVITY_REWARDS = {
  'message_sent': 5,
  'reaction_added': 2,
  'voice_join': 10,
  'quest_completed': 100,
  'referral_successful': 250
};

async function rewardActivity(realmId, memberId, activityType) {
  const points = ACTIVITY_REWARDS[activityType];
  if (!points) return null;
  
  return updateMemberBalance(realmId, memberId, points);
}

// Usage in Discord bot or webhook handler
await rewardActivity('YOUR_REALM_ID', 'MEMBER_ID', 'message_sent');
```

### Leaderboard Generation

Create leaderboards by fetching and sorting member data:

```javascript  theme={"dark"}
async function generateLeaderboard(realmId, limit = 10) {
  // This would typically involve fetching multiple members
  // and sorting by their point balances
  const members = await searchMembers(realmId, 'drip-id', 'all'); // Pseudo-code
  
  return members
    .sort((a, b) => b.pointBalances[0].balance - a.pointBalances[0].balance)
    .slice(0, limit)
    .map((member, index) => ({
      rank: index + 1,
      username: member.username,
      points: member.pointBalances[0].balance
    }));
}
```

### Member Onboarding

Set up new members with welcome bonuses:

```javascript  theme={"dark"}
async function onboardNewMember(realmId, memberId) {
  const welcomeBonus = 100;
  const result = await updateMemberBalance(realmId, memberId, welcomeBonus);
  
  console.log(`Welcomed new member with ${welcomeBonus} points!`);
  return result;
}
```

## Error Handling

Handle common errors when managing members:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function safeUpdateBalance(realmId, memberId, tokens) {
    try {
      const result = await updateMemberBalance(realmId, memberId, tokens);
      return { success: true, data: result };
    } catch (error) {
      if (error.status === 404) {
        return { success: false, error: 'Member not found' };
      } else if (error.status === 400) {
        return { success: false, error: 'Invalid request data' };
      } else if (error.status === 403) {
        return { success: false, error: 'Insufficient permissions' };
      }

      return { success: false, error: 'Unknown error occurred' };
    }
  }

  ```

  ```python Python theme={"dark"}
  def safe_update_balance(realm_id, member_id, tokens):
      try:
          result = update_member_balance(realm_id, member_id, tokens)
          return {'success': True, 'data': result}
      except requests.exceptions.HTTPError as e:
          if e.response.status_code == 404:
              return {'success': False, 'error': 'Member not found'}
          elif e.response.status_code == 400:
              return {'success': False, 'error': 'Invalid request data'}
          elif e.response.status_code == 403:
              return {'success': False, 'error': 'Insufficient permissions'}
          else:
              return {'success': False, 'error': 'Unknown error occurred'}
  ```

</CodeGroup>

## Best Practices

<CardGroup cols={2}>
  <Card title="Efficient Searching" icon="magnifying-glass">
    * Use specific search types when possible
    * Batch multiple searches together
    * Cache frequently accessed member data
    * Implement pagination for large result sets
  </Card>

  <Card title="Balance Management" icon="scale-balanced">
    * Always validate point amounts before updates
    * Use batch operations for multiple updates
    * Implement transaction logs for audit trails
    * Handle insufficient balance scenarios gracefully
  </Card>

  <Card title="Performance" icon="gauge-high">
    * Use batch endpoints for bulk operations
    * Implement rate limiting in your application
    * Cache member data to reduce API calls
    * Monitor API response times
  </Card>

  <Card title="Security" icon="shield-check">
    * Validate all input parameters
    * Implement proper error handling
    * Log all balance changes for auditing
    * Use least-privilege API keys
  </Card>
</CardGroup>

## Next Steps

<CardGroup cols={2}>
  <Card title="Point Systems" icon="coins" href="/developer/point-systems">
    Learn advanced point management and currency systems
  </Card>

  <Card title="Ghost Credentials" icon="ghost" href="/developer/credentials">
    Manage points for users before they become members
  </Card>

  <Card title="Quest Management" icon="map" href="/developer/quest-integration">
    Create engaging gamified experiences for members
  </Card>

  <Card title="Webhooks" icon="webhook" href="/developer/webhooks">
    Set up real-time notifications for member activities
  </Card>
</CardGroup>

<Info>
  **Need to manage users who haven't joined yet?** Use [Ghost Credentials](/developer/credentials) to pre-credit points to Twitter followers, wallet holders, or email addresses before they connect to your realm.
</Info>

Built with [Mintlify](https://mintlify.com).

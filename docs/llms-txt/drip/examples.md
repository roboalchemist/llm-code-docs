# Source: https://docs.drip.re/developer/examples.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Code Examples

> Copy-paste code for common DRIP API tasks 📋

Ready-to-use code snippets for the most common DRIP API tasks. Just copy, paste, and customize! 🚀

<Info>
  **New to APIs?** Each example includes error handling and comments explaining what's happening. Perfect for learning!
</Info>

## Setup & Authentication

### Basic API Client Setup

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    class DripClient {
      constructor(apiKey, realmId) {
        this.apiKey = apiKey;
        this.realmId = realmId;
        this.baseUrl = 'https://api.drip.re/api/v1';
      }

      async request(method, endpoint, data = null) {
        const url = `${this.baseUrl}${endpoint}`;
        const options = {
          method,
          headers: {
            'Authorization': `Bearer ${this.apiKey}`,
            'Content-Type': 'application/json'
          }
        };

        if (data) {
          options.body = JSON.stringify(data);
        }

        try {
          const response = await fetch(url, options);
          
          if (!response.ok) {
            const error = await response.json();
            throw new Error(`API Error: ${response.status} - ${error.message || 'Unknown error'}`);
          }

          return response.json();
        } catch (error) {
          console.error('DRIP API Error:', error);
          throw error;
        }
      }
    }

    // Usage
    const client = new DripClient('your_api_key', 'your_realm_id');
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    import requests
    import json

    class DripClient:
        def __init__(self, api_key, realm_id):
            self.api_key = api_key
            self.realm_id = realm_id
            self.base_url = 'https://api.drip.re/api/v1'
            self.session = requests.Session()
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            })

        def request(self, method, endpoint, data=None):
            url = f"{self.base_url}{endpoint}"
            
            try:
                response = self.session.request(method, url, json=data)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                print(f'DRIP API Error: {e}')
                raise
            except Exception as e:
                print(f'Request failed: {e}')
                raise

    # Usage
    client = DripClient('your_api_key', 'your_realm_id')
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"dark"}
    # Set your variables
    DRIP_API_KEY="your_api_key_here"
    REALM_ID="your_realm_id_here"
    BASE_URL="https://api.drip.re/api/v1"

    # Function to make API calls
    drip_api() {
      local method=$1
      local endpoint=$2
      local data=$3
      
      if [ -n "$data" ]; then
        curl -s -X "$method" "$BASE_URL$endpoint" \
          -H "Authorization: Bearer $DRIP_API_KEY" \
          -H "Content-Type: application/json" \
          -d "$data"
      else
        curl -s -X "$method" "$BASE_URL$endpoint" \
          -H "Authorization: Bearer $DRIP_API_KEY"
      fi
    }

    # Usage
    # drip_api GET "/realms/$REALM_ID"
    ```
  </Tab>
</Tabs>

## Member Management

### Search for Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    // Search by different identifiers
    async function searchMembers(client, searchType, values) {
      const endpoint = `/realm/${client.realmId}/members/search?type=${searchType}&values=${values}`;
      return await client.request('GET', endpoint);
    }

    // Examples
    const client = new DripClient('your_api_key', 'your_realm_id');

    // Search by Discord ID
    const discordMembers = await searchMembers(client, 'discord-id', '123456789012345678');

    // Search by multiple usernames
    const usernameMembers = await searchMembers(client, 'username', 'user1,user2,user3');

    // Search by wallet address
    const walletMembers = await searchMembers(client, 'wallet', '0x742d35Cc6634C0532925a3b8D23');

    // Search by email
    const emailMembers = await searchMembers(client, 'email', 'user@example.com');

    console.log('Found members:', discordMembers.data);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def search_members(client, search_type, values):
        endpoint = f'/realm/{client.realm_id}/members/search?type={search_type}&values={values}'
        return client.request('GET', endpoint)

    # Examples
    client = DripClient('your_api_key', 'your_realm_id')

    # Search by Discord ID
    discord_members = search_members(client, 'discord-id', '123456789012345678')

    # Search by multiple usernames
    username_members = search_members(client, 'username', 'user1,user2,user3')

    # Search by wallet address
    wallet_members = search_members(client, 'wallet', '0x742d35Cc6634C0532925a3b8D23')

    print(f"Found {len(discord_members.get('data', []))} members")
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"dark"}
    # Search by Discord ID
    drip_api GET "/realm/$REALM_ID/members/search?type=discord-id&values=123456789012345678"

    # Search by multiple usernames
    drip_api GET "/realm/$REALM_ID/members/search?type=username&values=user1,user2,user3"

    # Search by wallet
    drip_api GET "/realm/$REALM_ID/members/search?type=wallet&values=0x742d35Cc6634C0532925a3b8D23"
    ```
  </Tab>
</Tabs>

### Get Member Details

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function getMemberDetails(client, memberId) {
      // First search for the member to get their full details
      const members = await searchMembers(client, 'drip-id', memberId);

      if (members.data && members.data.length > 0) {
        const member = members.data[0];
        
        return {
          id: member.id,
          name: member.displayName || member.username,
          joinedAt: member.joinedAt,
          lastVisit: member.lastVisit,
          points: member.pointBalances || [],
          credentials: member.credentials || []
        };
      }
      
      throw new Error('Member not found');
    }

    // Usage
    try {
      const member = await getMemberDetails(client, 'member_id_here');
      console.log(`${member.name} has ${member.points[0]?.balance || 0} points`);
    } catch (error) {
      console.error('Member not found:', error.message);
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def get_member_details(client, member_id):
        members = search_members(client, 'drip-id', member_id)

        if members.get('data') and len(members['data']) > 0:
            member = members['data'][0]
            
            return {
                'id': member['id'],
                'name': member.get('displayName') or member.get('username'),
                'joined_at': member.get('joinedAt'),
                'last_visit': member.get('lastVisit'),
                'points': member.get('pointBalances', []),
                'credentials': member.get('credentials', [])
            }
        
        raise Exception('Member not found')

    # Usage
    try:
        member = get_member_details(client, 'member_id_here')
        points = member['points'][0]['balance'] if member['points'] else 0
        print(f"{member['name']} has {points} points")
    except Exception as e:
        print(f"Member not found: {e}")
    ```
  </Tab>
</Tabs>

## Points Management

### Award Points to a Member

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function awardPoints(client, memberId, points, realmPointId = null) {
      const endpoint = `/realm/${client.realmId}/members/${memberId}/point-balance`;
      const data = { tokens: points };

      if (realmPointId) {
        data.realmPointId = realmPointId;
      }
      
      return await client.request('PATCH', endpoint, data);
    }

    // Examples
    const client = new DripClient('your_api_key', 'your_realm_id');

    // Award 100 points (default currency)
    const result = await awardPoints(client, 'member_id', 100);
    console.log('Points awarded:', result);

    // Award points to specific currency
    const specificResult = await awardPoints(client, 'member_id', 50, 'specific_point_id');

    // Deduct points (negative number)
    const deductResult = await awardPoints(client, 'member_id', -25);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def award_points(client, member_id, points, realm_point_id=None):
        endpoint = f'/realm/{client.realm_id}/members/{member_id}/point-balance'
        data = {'tokens': points}

        if realm_point_id:
            data['realmPointId'] = realm_point_id
        
        return client.request('PATCH', endpoint, data)

    # Examples
    client = DripClient('your_api_key', 'your_realm_id')

    # Award 100 points
    result = award_points(client, 'member_id', 100)
    print('Points awarded:', result)

    # Deduct 25 points
    deduct_result = award_points(client, 'member_id', -25)
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"dark"}
    # Award 100 points
    drip_api PATCH "/realm/$REALM_ID/members/MEMBER_ID/point-balance" '{"tokens": 100}'

    # Award points to specific currency
    drip_api PATCH "/realm/$REALM_ID/members/MEMBER_ID/point-balance" '{"tokens": 50, "realmPointId": "POINT_ID"}'

    # Deduct points
    drip_api PATCH "/realm/$REALM_ID/members/MEMBER_ID/point-balance" '{"tokens": -25}'
    ```
  </Tab>
</Tabs>

### Batch Update Multiple Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function batchUpdatePoints(client, updates) {
      const endpoint = `/realm/${client.realmId}/members/transaction`;
      return await client.request('PATCH', endpoint, { updates });
    }

    // Example: Award points to multiple members
    const updates = [
      { memberId: 'member_1', tokens: 100 },
      { memberId: 'member_2', tokens: 150 },
      { memberId: 'member_3', tokens: 75, realmPointId: 'specific_point_id' }
    ];

    const batchResult = await batchUpdatePoints(client, updates);
    console.log('Batch update result:', batchResult);

    // Example: Weekly point distribution
    async function weeklyPointDistribution(client, memberIds, basePoints = 50) {
      const updates = memberIds.map(memberId => ({
        memberId,
        tokens: basePoints + Math.floor(Math.random() * 50) // 50-100 points
      }));
      
      return await batchUpdatePoints(client, updates);
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def batch_update_points(client, updates):
        endpoint = f'/realm/{client.realm_id}/members/transaction'
        return client.request('PATCH', endpoint, {'updates': updates})

    # Example: Award points to multiple members
    updates = [
        {'memberId': 'member_1', 'tokens': 100},
        {'memberId': 'member_2', 'tokens': 150},
        {'memberId': 'member_3', 'tokens': 75, 'realmPointId': 'specific_point_id'}
    ]

    batch_result = batch_update_points(client, updates)
    print('Batch update result:', batch_result)

    # Weekly distribution function
    def weekly_point_distribution(client, member_ids, base_points=50):
        import random
        updates = [
            {
                'memberId': member_id,
                'tokens': base_points + random.randint(0, 50)
            }
            for member_id in member_ids
        ]
        return batch_update_points(client, updates)
    ```
  </Tab>
</Tabs>

### Transfer Points Between Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function transferPoints(client, senderId, recipientId, amount, realmPointId) {
      const endpoint = `/realm/${client.realmId}/members/${senderId}/transfer`;
      const data = {
        tokens: amount,
        recipientId: recipientId,
        realmPointId: realmPointId
      };

      return await client.request('PATCH', endpoint, data);
    }

    // Example: Transfer 100 points from one member to another
    const transfer = await transferPoints(
      client,
      'sender_member_id',
      'recipient_member_id', 
      100,
      'realm_point_id'
    );

    console.log('Transfer successful:', transfer);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def transfer_points(client, sender_id, recipient_id, amount, realm_point_id):
        endpoint = f'/realm/{client.realm_id}/members/{sender_id}/transfer'
        data = {
            'tokens': amount,
            'recipientId': recipient_id,
            'realmPointId': realm_point_id
        }
        return client.request('PATCH', endpoint, data)

    # Example usage
    transfer = transfer_points(
        client,
        'sender_member_id',
        'recipient_member_id',
        100,
        'realm_point_id'
    )
    print('Transfer successful:', transfer)
    ```
  </Tab>
</Tabs>

## Common Patterns

### Find and Reward Active Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function rewardActiveMembers(client, minPoints = 0, reward = 50) {
      // Get all members
      const allMembers = await searchMembers(client, 'drip-id', 'all');

      // Filter active members (you can customize this logic)
      const activeMembers = allMembers.data.filter(member => {
        const points = member.pointBalances[0]?.balance || 0;
        const lastVisit = new Date(member.lastVisit);
        const weekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
        
        return points >= minPoints && lastVisit > weekAgo;
      });

      // Prepare batch update
      const updates = activeMembers.map(member => ({
        memberId: member.id,
        tokens: reward
      }));

      if (updates.length > 0) {
        const result = await batchUpdatePoints(client, updates);
        console.log(`Rewarded ${updates.length} active members with ${reward} points each`);
        return result;
      } else {
        console.log('No active members found to reward');
        return null;
      }
    }

    // Usage
    await rewardActiveMembers(client, 100, 75); // Reward members with 100+ points who visited in last week
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    from datetime import datetime, timedelta

    def reward_active_members(client, min_points=0, reward=50):
        # Get all members
        all_members = search_members(client, 'drip-id', 'all')
        
        # Filter active members
        active_members = []
        week_ago = datetime.now() - timedelta(days=7)
        
        for member in all_members.get('data', []):
            points = member.get('pointBalances', [{}])[0].get('balance', 0)
            last_visit = datetime.fromisoformat(member.get('lastVisit', '').replace('Z', '+00:00'))
            
            if points >= min_points and last_visit > week_ago:
                active_members.append(member)

        # Prepare batch update
        updates = [
            {'memberId': member['id'], 'tokens': reward}
            for member in active_members
        ]

        if updates:
            result = batch_update_points(client, updates)
            print(f"Rewarded {len(updates)} active members with {reward} points each")
            return result
        else:
            print("No active members found to reward")
            return None

    # Usage
    reward_active_members(client, 100, 75)
    ```
  </Tab>
</Tabs>

### Create a Leaderboard

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function getLeaderboard(client, limit = 10) {
      // Get all members
      const allMembers = await searchMembers(client, 'drip-id', 'all');

      // Filter members with points and sort
      const leaderboard = allMembers.data
        .filter(member => member.pointBalances && member.pointBalances.length > 0)
        .map(member => ({
          id: member.id,
          name: member.displayName || member.username || 'Anonymous',
          points: member.pointBalances[0]?.balance || 0,
          joinedAt: member.joinedAt,
          lastVisit: member.lastVisit
        }))
        .sort((a, b) => b.points - a.points)
        .slice(0, limit)
        .map((member, index) => ({
          ...member,
          rank: index + 1
        }));

      return leaderboard;
    }

    // Usage
    const topMembers = await getLeaderboard(client, 10);
    console.log('Top 10 Members:');
    topMembers.forEach(member => {
      console.log(`${member.rank}. ${member.name}: ${member.points} points`);
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def get_leaderboard(client, limit=10):
        # Get all members
        all_members = search_members(client, 'drip-id', 'all')

        # Filter and sort members
        leaderboard = []
        for member in all_members.get('data', []):
            if member.get('pointBalances') and len(member['pointBalances']) > 0:
                leaderboard.append({
                    'id': member['id'],
                    'name': member.get('displayName') or member.get('username') or 'Anonymous',
                    'points': member['pointBalances'][0].get('balance', 0),
                    'joined_at': member.get('joinedAt'),
                    'last_visit': member.get('lastVisit')
                })
        
        # Sort by points and add ranks
        leaderboard = sorted(leaderboard, key=lambda x: x['points'], reverse=True)[:limit]
        for i, member in enumerate(leaderboard):
            member['rank'] = i + 1
        
        return leaderboard

    # Usage
    top_members = get_leaderboard(client, 10)
    print("Top 10 Members:")
    for member in top_members:
        print(f"{member['rank']}. {member['name']}: {member['points']} points")
    ```
  </Tab>
</Tabs>

### Discord Bot Integration

<Tabs>
  <Tab title="JavaScript (Discord.js)">
    ```javascript  theme={"dark"}
    const { Client, GatewayIntentBits } = require('discord.js');

    const bot = new Client({
      intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent]
    });

    const dripClient = new DripClient('your_drip_api_key', 'your_realm_id');

    // Award points for messages
    bot.on('messageCreate', async (message) => {
      if (message.author.bot) return;

      try {
        // Find member by Discord ID
        const members = await searchMembers(dripClient, 'discord-id', message.author.id);
        
        if (members.data && members.data.length > 0) {
          const memberId = members.data[0].id;
          
          // Award 5 points per message
          await awardPoints(dripClient, memberId, 5);
          
          // Optional: React to show points were awarded
          await message.react('⭐');
        }
      } catch (error) {
        console.error('Error awarding points:', error);
      }
    });

    // Leaderboard command
    bot.on('messageCreate', async (message) => {
      if (message.content === '!leaderboard') {
        try {
          const leaderboard = await getLeaderboard(dripClient, 5);
          
          const leaderboardText = leaderboard
            .map(member => `${member.rank}. ${member.name}: ${member.points} points`)
            .join('\n');
          
          await message.reply(`🏆 **Top 5 Members:**\n\`\`\`\n${leaderboardText}\n\`\`\``);
        } catch (error) {
          await message.reply('Sorry, I couldn\'t fetch the leaderboard right now.');
        }
      }
    });

    bot.login('your_discord_bot_token');
    ```
  </Tab>

  <Tab title="Python (discord.py)">
    ````python  theme={"dark"}
    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    drip_client = DripClient('your_drip_api_key', 'your_realm_id')

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        try:
            # Find member by Discord ID
            members = search_members(drip_client, 'discord-id', str(message.author.id))
            
            if members.get('data') and len(members['data']) > 0:
                member_id = members['data'][0]['id']
                
                # Award 5 points per message
                award_points(drip_client, member_id, 5)
                
                # React to show points were awarded
                await message.add_reaction('⭐')
        except Exception as e:
            print(f'Error awarding points: {e}')

        await bot.process_commands(message)

    @bot.command()
    async def leaderboard(ctx):
        try:
            top_members = get_leaderboard(drip_client, 5)
            
            leaderboard_text = '\n'.join([
                f"{member['rank']}. {member['name']}: {member['points']} points"
                for member in top_members
            ])
            
            await ctx.send(f"🏆 **Top 5 Members:**\n```\n{leaderboard_text}\n```")
        except Exception as e:
            await ctx.send("Sorry, I couldn't fetch the leaderboard right now.")

    bot.run('your_discord_bot_token')
    ````
  </Tab>
</Tabs>

## Error Handling Patterns

### Robust Error Handling

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function safeApiCall(apiCall, fallbackValue = null) {
      try {
        return await apiCall();
      } catch (error) {
        console.error('API call failed:', error.message);

        // Handle specific error types
        if (error.message.includes('401')) {
          console.error('Authentication failed - check your API key');
        } else if (error.message.includes('403')) {
          console.error('Permission denied - check your scopes');
        } else if (error.message.includes('404')) {
          console.error('Resource not found');
        } else if (error.message.includes('429')) {
          console.error('Rate limited - slow down your requests');
        }
        
        return fallbackValue;
      }
    }

    // Usage
    const members = await safeApiCall(
      () => searchMembers(client, 'discord-id', 'invalid_id'),
      { data: [] }
    );
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def safe_api_call(api_call, fallback_value=None):
        try:
            return api_call()
        except Exception as e:
            print(f'API call failed: {e}')

            # Handle specific error types
            error_str = str(e).lower()
            if '401' in error_str:
                print('Authentication failed - check your API key')
            elif '403' in error_str:
                print('Permission denied - check your scopes')
            elif '404' in error_str:
                print('Resource not found')
            elif '429' in error_str:
                print('Rate limited - slow down your requests')
            
            return fallback_value

    # Usage
    members = safe_api_call(
        lambda: search_members(client, 'discord-id', 'invalid_id'),
        {'data': []}
    )
    ```
  </Tab>
</Tabs>

## Quick Reference

### Most Common API Calls

```javascript  theme={"dark"}
// Authentication & Setup
const client = new DripClient('api_key', 'realm_id');

// Get realm info
const realm = await client.request('GET', `/realms/${client.realmId}`);

// Search members
const members = await searchMembers(client, 'discord-id', 'user_id');

// Award points
await awardPoints(client, 'member_id', 100);

// Get leaderboard
const top10 = await getLeaderboard(client, 10);

// Batch update
await batchUpdatePoints(client, [
  { memberId: 'id1', tokens: 50 },
  { memberId: 'id2', tokens: 75 }
]);
```

### Common Search Types

| Type         | Use Case             | Example Value                   |
| ------------ | -------------------- | ------------------------------- |
| `discord-id` | Find Discord users   | `123456789012345678`            |
| `username`   | Find by display name | `cooluser123`                   |
| `email`      | Find by email        | `user@example.com`              |
| `wallet`     | Find crypto users    | `0x742d35Cc6634C0532925a3b8D23` |
| `twitter-id` | Find Twitter users   | `987654321`                     |
| `drip-id`    | Find by DRIP ID      | `507f1f77bcf86cd799439013`      |

<Info>
  **Need more examples?** Check out our [First App tutorial](/developer/first-app) for a complete working project, or browse the [API Reference](/api-reference) for detailed endpoint documentation.
</Info>

Built with [Mintlify](https://mintlify.com).

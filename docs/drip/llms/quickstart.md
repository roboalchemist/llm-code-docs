# Source: https://docs.drip.re/developer/quickstart.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# 5-Minute Quickstart

> Get your first DRIP API call working in 5 minutes ⚡

Ready to start building with DRIP? Let's get you up and running in 5 minutes! 🚀

## TL;DR - Just Want to Code?

<CodeGroup>
  ```bash Copy & Run This theme={"dark"}
  # 1. Get your API key from Admin > Developer > Project API
  # 2. Replace YOUR_API_KEY and YOUR_REALM_ID below
  # 3. Run this command

  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
    -H "Authorization: Bearer YOUR_API_KEY"

  ```

  ```javascript Node.js One-Liner theme={"dark"}
  // npm install node-fetch
  const response = await fetch('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', {
    headers: { 'Authorization': 'Bearer YOUR_API_KEY' }
  });
  console.log(await response.json());
  ```

  ```python Python One-Liner   theme={"dark"}
  # pip install requests
  import requests
  r = requests.get('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', 
                   headers={'Authorization': 'Bearer YOUR_API_KEY'})
  print(r.json())
  ```

</CodeGroup>

## Step-by-Step (For Real This Time)

### 1. Get Your API Key (30 seconds)

<Steps>
  <Step title="Open DRIP Dashboard">
    Go to [app.drip.re](https://app.drip.re) and log in
  </Step>

  <Step title="Navigate to Developer Portal">
    Click **Admin** → **Developer** in the sidebar
  </Step>

  <Step title="Create API Client">
    * Click **Project API** tab
    * Click **Create API Client**
    * Give it a name like "My First App"
    * Select some scopes (start with `realm:read` and `members:read`)
    * Click **Create**
  </Step>

  <Step title="Copy Your Keys">
    Copy both the **Client ID** and **Client Secret** (you'll need the secret)
  </Step>
</Steps>

### 2. Find Your Realm (Project) ID (15 seconds)

Your Realm ID is displayed in the dashboard header when you select your project:

<Steps>
  <Step title="Select Your Project">
    In the DRIP dashboard, make sure your project is selected from the project switcher
  </Step>

  <Step title="Copy Realm ID">
    Look at the dashboard header - your Realm ID is displayed there and can be copied directly
  </Step>
</Steps>

### 3. Make Your First Call (1 minute)

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    const DRIP_API_KEY = 'your_client_secret_here';
    const REALM_ID = 'your_realm_id_here';

    async function getDripData() {
      try {
        // Get your realm info
        const realm = await fetch(`https://api.drip.re/api/v1/realms/${REALM_ID}`, {
          headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
        }).then(r => r.json());
        
        console.log('🎉 Your realm:', realm.name);
        
        // Get some members
        const members = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=drip-id&values=all`, {
          headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
        }).then(r => r.json());
        
        console.log('👥 Member count:', members.data?.length || 0);
        
      } catch (error) {
        console.error('❌ Error:', error.message);
      }
    }

    getDripData();
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    import requests

    DRIP_API_KEY = 'your_client_secret_here'
    REALM_ID = 'your_realm_id_here'

    headers = {'Authorization': f'Bearer {DRIP_API_KEY}'}

    try:
        # Get your realm info
        realm = requests.get(f'https://api.drip.re/api/v1/realms/{REALM_ID}', headers=headers).json()
        print(f'🎉 Your realm: {realm["name"]}')
        
        # Get some members  
        members = requests.get(f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search?type=drip-id&values=all', headers=headers).json()
        print(f'👥 Member count: {len(members.get("data", []))}')
        
    except Exception as error:
        print(f'❌ Error: {error}')
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"dark"}
    # Set your variables
    DRIP_API_KEY="your_client_secret_here"
    REALM_ID="your_realm_id_here"

    # Get realm info
    echo "🎉 Your realm:"
    curl -s "https://api.drip.re/api/v1/realms/$REALM_ID" \
      -H "Authorization: Bearer $DRIP_API_KEY" | jq '.name'

    # Get member count
    echo "👥 Member count:"
    curl -s "https://api.drip.re/api/v1/realm/$REALM_ID/members/search?type=drip-id&values=all" \
      -H "Authorization: Bearer $DRIP_API_KEY" | jq '.data | length'
    ```
  </Tab>
</Tabs>

## What Just Happened? 🤔

You just:

1. ✅ **Authenticated** with the DRIP API
2. ✅ **Retrieved** your realm information
3. ✅ **Searched** for members in your community

Not bad for 5 minutes! 🎉

## What Can You Do Next?

<CardGroup cols={2}>
  <Card title="Award Points to Members" icon="coins" href="#award-points-to-a-member">
    Give your community members some points for being awesome
  </Card>

  <Card title="Search for Specific Members" icon="user" href="#search-members-by-discord-id">
    Find members by Discord ID, wallet address, or username
  </Card>

  <Card title="Build a Simple Dashboard" icon="chart-bar" href="/developer/first-app">
    Create your first DRIP-powered app
  </Card>

  <Card title="Member Management" icon="users" href="/developer/managing-members">
    Search, update, and manage community members effectively
  </Card>
</CardGroup>

## Quick Examples for Vibe Coders

### Award Points to a Member

<CodeGroup>
  ```javascript Give 100 Points theme={"dark"}
  // Find a member first
  const members = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=username&values=cool_member`, {
    headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
  }).then(r => r.json());

  if (members.data?.length > 0) {
    const memberId = members.data[0].id;

    // Give them 100 points
    const result = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/${memberId}/point-balance`, {
      method: 'PATCH',
      headers: { 
        'Authorization': `Bearer ${DRIP_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ tokens: 100 })
    }).then(r => r.json());
    
    console.log('💰 Points awarded!', result);
  }

  ```

  ```python Award Points theme={"dark"}
  import requests

  # Find a member
  members = requests.get(
      f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search?type=username&values=cool_member',
      headers={'Authorization': f'Bearer {DRIP_API_KEY}'}
  ).json()

  if members.get('data'):
      member_id = members['data'][0]['id']
      
      # Award 100 points
      result = requests.patch(
          f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/{member_id}/point-balance',
          headers={'Authorization': f'Bearer {DRIP_API_KEY}', 'Content-Type': 'application/json'},
          json={'tokens': 100}
      ).json()
      
      print('💰 Points awarded!', result)
  ```

</CodeGroup>

### Search Members by Discord ID

<CodeGroup>
  ```javascript Find Discord User theme={"dark"}
  const discordId = '123456789012345678'; // Their Discord user ID

  const members = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=discord-id&values=${discordId}`, {
    headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
  }).then(r => r.json());

  if (members.data?.length > 0) {
    const member = members.data[0];
    console.log(`Found: ${member.displayName} with ${member.pointBalances[0]?.balance || 0} points`);
  } else {
    console.log('Member not found 😢');
  }

  ```

  ```python Find by Wallet theme={"dark"}
  wallet_address = '0x742d35Cc6634C0532925a3b8D23'

  members = requests.get(
      f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search?type=wallet&values={wallet_address}',
      headers={'Authorization': f'Bearer {DRIP_API_KEY}'}
  ).json()

  if members.get('data'):
      member = members['data'][0]
      points = member['pointBalances'][0]['balance'] if member['pointBalances'] else 0
      print(f"Found: {member['displayName']} with {points} points")
  else:
      print('Member not found 😢')
  ```

</CodeGroup>

## Common "Oops" Moments 🤦‍♂️

<AccordionGroup>
  <Accordion title="❌ 401 Unauthorized">
    **Problem**: Your API key is wrong or missing

    **Fix**: Double-check you're using the **Client Secret** (not Client ID) from the developer portal

    ```bash  theme={"dark"}
    # Wrong ❌
    Authorization: Bearer your_client_id_here

    # Right ✅  
    Authorization: Bearer your_client_secret_here
    ```
  </Accordion>

  <Accordion title="❌ 403 Forbidden">
    **Problem**: Your API client doesn't have the right scopes

    **Fix**: Go back to **Admin > Developer > Project API** and add more scopes to your client

    Common scopes you might need:

    * `realm:read` - Read realm info
    * `members:read` - Read member data
    * `members:write` - Update member points
    * `points:write` - Award/deduct points
  </Accordion>

  <Accordion title="❌ 404 Not Found">
    **Problem**: Wrong Realm ID or member doesn't exist

    **Fix**: Check your realm ID in the dashboard URL. For members, try searching first before updating.
  </Accordion>

  <Accordion title="❌ 429 Too Many Requests">
    **Problem**: You're making requests too fast

    **Fix**: Add a small delay between requests or use batch endpoints

    ```javascript  theme={"dark"}
    // Add delay
    await new Promise(resolve => setTimeout(resolve, 100));
    ```
  </Accordion>
</AccordionGroup>

## You're Ready! 🎯

That's it! You now know enough to be dangerous with the DRIP API. Here's what to explore next:

<CardGroup cols={3}>
  <Card title="Build Your First App" icon="rocket" href="/developer/first-app">
    Create a simple DRIP-powered application
  </Card>

  <Card title="Learn the Fundamentals" icon="book" href="/developer/core-concepts">
    Understand DRIP's data model and concepts
  </Card>

  <Card title="See More Examples" icon="code" href="/developer/examples">
    Copy-paste code for common tasks
  </Card>
</CardGroup>

<Info>
  **Pro tip**: Join our [Discord community](https://discord.gg/dripchain) for help, tips, and to show off what you're building! 🚀
</Info>

Built with [Mintlify](https://mintlify.com).

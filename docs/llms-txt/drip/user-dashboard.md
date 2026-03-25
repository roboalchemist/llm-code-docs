# Source: https://docs.drip.re/bot-documentation/drip-features/user-dashboard.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# User Dashboard

> The Dashboard is a central place for your community to manage points.

Creating the Dashboard

<Info>Only an administrator can create the dashboard</Info>

1. **Creating the Dashboard:** Visit the `#🛠┆admin` channel and click `Create Channels > Create Specific` and select "Dashboard".

<Frame caption="Preview of  channel.">
  <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_9ec59e.png?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=fba440fd625f4d2c9d44e9ce8d39c15f" width="498" height="342" data-path="images/drip-features/img_9ec59e.png" />

  `#🛠┆admin`
</Frame>

<Frame caption="Step by step">
  <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_249ad1.gif?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=9a180fc20c7afaadc7d73d4651e405bf" width="509" height="399" data-path="images/drip-features/img_249ad1.gif" />
</Frame>

1. You can create the dashboard Magic Embed in a channel directly by using the command `/dashboard ChannelName` - This can also be used to reset the Dashboard embed.

<Frame caption="Dashboard directly to a specific channel.">
  <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_a6f26f.png?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=7e00ff4a5c71533b2ac3a295657f71bf" width="551" height="170" data-path="images/drip-features/img_a6f26f.png" />
</Frame>

### Using the Dashboard

<Frame caption="Preview of the dashboard">
  <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_40dfaf.png?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=d006c8d82f3a0cae8131a2d68932d191" width="495" height="339" data-path="images/drip-features/img_40dfaf.png" />
</Frame>

#### Buttons on the Main Embed

* **⚡My Dashboard:** Navigate to your dashboard with details about points, NFTs, and more.

* **🏆 Leaderboard:** See other community members with the highest point counts.

* **🔎 Check NFT Balance:** Check the balance of specific NFTs from activated collections.

* **Support:** Join the Drip Discord for support and follow us on Twitter for the latest updates

<Info>
  **Pro Feature:** Right-click the embed then use `App > Edit` to change various features of your community dashboard including image, embed title, description, and color.

  ![](https://docs.drip.re/~gitbook/image?url=https%3A%2F%2F2728597434-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxUaE8LDXTeS85PkKxJJa%252Fuploads%252F33dxKeYBDYc3Zr0KLKOx%252F%2523%25E3%2580%258C%25E2%259A%25A1%25E3%2580%258Ddashboard%2520%2524WOJAK%2520x%2520Anonthology%2520-%2520Discord%25202024-02-24%2520at%25203.06.43%2520PM.jpg%3Falt%3Dmedia%26token%3D1a495dcc-d879-44e5-85ec-7104cb79db1d\&width=300\&dpr=4\&quality=100\&sign=be15c07d\&sv=1)
</Info>

### Detailed Features

<Tabs>
  <Tab title="⚡️ My Dashboard">
    Displays an overview of your account:

    * Points balance
    * Daily points generation (yield)
    * Time remaining until your next claim
    * The number of NFTs you own from the server's activated collection(s).

    <Frame caption="My Dashboard Embed">
      <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_c0a3f1.jpg?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=3f20881a5bab703f96b7ae02f7d4ae57" width="988" height="994" data-path="images/drip-features/img_c0a3f1.jpg" />
    </Frame>

    **Dashboard Buttons:**

    1. **Claim Tokens:** Harvest all the Points from your NFTs.
    2. **🔗 Pair/Unpair NFTs:** These buttons are visible only when the server has a multiplier. Use them to pair or unpair NFTs.
    3. **🔎 Browse NFTs:** Navigate through your NFTs from activated collections. Check details and harvest tokens from generator NFTs. [Read More](/drip-features/user-dashboard/browse-nfts)
    4. **⚙️ Settings:** Manage your Twitter account and Web3 Wallets – adding or removing them. [Read More](/drip-features/user-dashboard/user-settings/wallet-settings)
  </Tab>

  <Tab title="🏆 Leaderboard">
    Displays community members with the highest point counts:

    <Frame caption="Community Leaderboard">
      <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_717015.png?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=59c47ce64253fa1935c0ae1650f9cc55" width="866" height="526" data-path="images/drip-features/img_717015.png" />
    </Frame>

    You can exclude certain roles from appearing in the Leaderboard. [Read more](/admin-settings/admin-dashboard/admin-settings/member-roles)

    Admins can enable/disable the Leaderboard. [Read more](/admin-settings/admin-dashboard/admin-settings/points-settings)
  </Tab>

  <Tab title="🔎 Check NFT Balance">
    Enter the NFT ID of your choice from an activated collection to see how many points it holds.

    <Frame caption="Lookup NFT">
      <img src="https://mintcdn.com/driprewards/Xh33JGW0jVY0ds3p/images/drip-features/img_a955c9.jpg?fit=max&auto=format&n=Xh33JGW0jVY0ds3p&q=85&s=e8dfac20b0dca53964bc50f9ea0313a3" width="874" height="558" data-path="images/drip-features/img_a955c9.jpg" />
    </Frame>
  </Tab>
</Tabs>

### Learn More About

<CardGroup>
  <Card title="🔎" href="/drip-features/user-dashboard/browse-nfts">
    The browse NFTs is the way for users to check their NFTs from imported collections and harvest generators.
  </Card>

  <Card title="💰" href="/drip-features/user-dashboard/user-settings/wallet-settings">
    The wallets section in the dashboard is the place to manage all of your wallets.
  </Card>
</CardGroup>

*Keywords: dashboard, leaderboard, points balance, claim points, pair/unpair NFTs, browse NFTs*

Built with [Mintlify](https://mintlify.com).

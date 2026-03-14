# Source: https://docs.drip.re/bot-documentation/faq/how-do-i-whitelist-drip-with-wick-bot.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# How do I whitelist Drip with Wick Bot?

> How to prevent Drip Rewards from being kicked by Wick Bot

The Wick Bot is a great tool for Discord security and is notorious for "wrongfully" kicking verified members/bots from servers if whitelist roles are not properly configured. Here is how you can set the Wick Bot to work together with Drip Rewards:

<Info>
  This is not a tutorial for the entire setup of the Wick Bot. If you have not
  properly set up certain components, the whitelist may not work. Please refer
  to Wick Bot documentation/support for initial setup and any ongoing issues.
</Info>

### Types of Whitelist

The Wick Bot has 4 different types of whitelists, each allowing different members/roles to do different things without risk of consequence. It is your choice to whitelist Drip Rewards for the various categories that fit your needs best.

* **Spam Whitelist:** Allows members/roles to send multiple messages at a time and walls of text

* **Mentions Whitelist:** Allows members/roles to repeatedly mention other members and roles

* **Invite Links Whitelist:** Allows members/roles to post invite links to other Discord servers

* **@Everyone Whitelist:** Allows members/roles to mention @everyone and other public roles

The process for whitelisting a member/role with the Wick Bot is the same for all 4 types. For this example, we will be showing you how to give Drip Reward the Mentions Whitelist.

### How to Whitelist Drip Rewards

<Warning>
  If using Wick Premium, you must ensure Anti-Nuke Protection is disabled before
  installing or setting up Drip Rewards
</Warning>

Navigate to your server's Wick Dashboard and click on Whitelist in the Auto Mod category. Ensure Auto Mod is properly set up beforehand.

<Frame caption="Click on Whitelist in the Auto Mod category">
  <img src="https://mintcdn.com/driprewards/ug46C-MqFjUqOXfE/images/faq/img_f709ab.png?fit=max&auto=format&n=ug46C-MqFjUqOXfE&q=85&s=4555bc7ea847624fd39199c8af4a4ca0" width="618" height="588" data-path="images/faq/img_f709ab.png" />
</Frame>

Click on the Mention tab to modify whitelist permissions

<Frame caption="Click on Mentions to modify whitelist permissions">
  <img src="https://mintcdn.com/driprewards/ug46C-MqFjUqOXfE/images/faq/img_60ede9.png?fit=max&auto=format&n=ug46C-MqFjUqOXfE&q=85&s=86aa73505978e2c78468837f8ebb0684" width="1200" height="508" data-path="images/faq/img_60ede9.png" />
</Frame>

Click on the dropdown menu under Roles and select the Drip role to whitelist Drip Rewards

<Frame caption="Choose the role you have assigned to Drip Rewards">
  <img src="https://mintcdn.com/driprewards/ug46C-MqFjUqOXfE/images/faq/img_506b75.png?fit=max&auto=format&n=ug46C-MqFjUqOXfE&q=85&s=05ee538ff5d40ab3d4d88631bd7b78b5" width="1936" height="696" data-path="images/faq/img_506b75.png" />
</Frame>

<Frame caption="The role will now show up as whitelisted">
  <img src="https://mintcdn.com/driprewards/ug46C-MqFjUqOXfE/images/faq/img_1096e4.png?fit=max&auto=format&n=ug46C-MqFjUqOXfE&q=85&s=6025c78f9f7960a8ffd72c9733125989" width="1904" height="240" data-path="images/faq/img_1096e4.png" />
</Frame>

Be sure to save your changes!

Drip Rewards should now be able to mention members without consequence from the Wick Bot. The process is the same for the other 3 categories.

Built with [Mintlify](https://mintlify.com).

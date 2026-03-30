# Source: https://docs.vast.ai/documentation/teams/teams-quickstart.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Teams Quickstart

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Get Started with Vast.ai Teams",
  "description": "A quickstart guide to creating a team, inviting team members, assigning roles, and using SSH keys with team instances on Vast.ai.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Create Your Team",
      "text": "There are two ways to create a team: Click on your profile name in the Context Switcher and click the Create Team button, or navigate to the Members section in the Sidebar and click Create Team. Enter your Team Name and optionally transfer some credit to your team during creation by selecting the 'Transfer my personal credits' checkbox. Click Create to finish."
    },
    {
      "@type": "HowToStep",
      "name": "Understand Default Team Roles",
      "text": "Every team comes with two default roles: Manager (full access to team resources) and Member (limited read access to most resources while still being able to rent instances). You can view and manage these roles from the Members Page."
    },
    {
      "@type": "HowToStep",
      "name": "Create Custom Roles (Optional)",
      "text": "To create a new role with custom permissions, navigate to the Roles tab of the Members Page. Name the role and choose the permission groups that the new role will have access to. Once satisfied, click Generate to create the new role."
    },
    {
      "@type": "HowToStep",
      "name": "Invite Team Members",
      "text": "Go to the Members Page and click the Invite button. Enter the email and team role for the person you want to invite, then click Invite to send the invitation email. The invitee will receive an email with a link to join your team. Note: If the recipient does not have a Vast account, they will need to create one before being added to your team."
    },
    {
      "@type": "HowToStep",
      "name": "Set Up SSH Keys for Team Instances",
      "text": "For VM Instances: Add your SSH key to your personal account before the VM is created. For Non-VM Instances: Either add your SSH key directly to the instance or add your key to your personal account, and it will be automatically applied to the team instance."
    }
  ]
})
}}
/>

## Introduction

This quickstart guide will walk you through how to create a team, invite new team members and assign them to different roles.

## Creating the Team

There are two ways to create a team:

1. Click on your profile name (or email address) in the Context Switcher and then click the **Create Team** button
2. Or you can navigate to the **Members** section in the Sidebar and click **Create Team**

<Frame caption="Create Team">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=be252d285d1d7a76a287d5033bf7f2b9" alt="" data-og-width="800" width="800" data-og-height="464" height="464" data-path="images/teams-quickstart.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=bf1b4c8550ebd50ca11ff29e3ed16695 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d9a36c15849bae48e8223f1ce2bf722b 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=f99bdd7bb037572f53dc5af00afcbc5e 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=acfb606715fb038075e0a74b2c39fbfa 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=132eb07867f6cffc1324c8f41c55fd0a 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=a5ccdb036013cc4d6c6a9202db1e4506 2500w" />
</Frame>

<Frame caption="Members Page">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=52c71e6f8be73e535c8775759d419e77" alt="" data-og-width="800" width="800" data-og-height="379" height="379" data-path="images/teams-quickstart-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=53dc890e68c9c58a23ff6f4aa0dc0164 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=808ac838a29ed95b051bc0d88ba0b44a 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=aca3a4bd0c23c526a370c98b0ac0549f 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d66325b15f0fb0577d5bc9cbc435e050 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=4630a59c795b4e8892140883ed71e8d5 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-2.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=9ad36fbc3768102f6eb54fe0c144b82b 2500w" />
</Frame>

Once there, you can create your **Team Name** and transfer some credit to your team during creation. You can also skip the credit transfer step and do it later from the [**Billing Page**](/documentation/reference/billing#a6bsE).

To add credit during team creation, select **Transfer my personal credits** checkbox, enter an amount, and then click **Create**.

<Frame caption="Team Creation">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=08f15631ba03184c7bd98478fee0f96b" alt="" data-og-width="800" width="800" data-og-height="720" height="720" data-path="images/teams-quickstart-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=639b487b13c0d85d58a73abc695ed559 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=7b057c718c5f07ba0879f6382531d8d8 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=8533b1a8dbdfcd1886555eb6295bb1db 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d2c701d2c4668a8e5455ec515c3c6b81 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=5bdcc5a205ba71100a7bfc3945329a7f 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-3.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=f327bfe8ab36765542b29a96a1561d22 2500w" />
</Frame>

After successfully creating the team you should see your Team Name and role in the Context Switcher in the upper left corner and the Team Dashboard on the **Members** page.

<Frame caption="Members Page">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=1ee87edcfb1cda108a11959a325145de" alt="" data-og-width="1079" width="1079" data-og-height="419" height="419" data-path="images/teams-quickstart-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d078db8a60c90961286acac7f83d608a 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=05aa2b9be5a402673e4e82540fe3fe2f 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d4b20ca15f2b8d3590842709093782de 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=26f8a436865186780b6c81e99c9ebdd4 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=60e1144bc564629701cd658960bead22 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-4.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=ee5fcc9e4b3e2966af9755e941b80534 2500w" />
</Frame>

The **Members** section is the main way that team owners and managers can interact with the Teams ecosystem. From here you can invite team members, create/manage team roles, remove team members, etc.

## Managing Team Roles

Every team comes with two default roles: manager and member.

Managers have full access to team resources, while members have limited read access to most resources while still being able to rent instances. [Learn more.](/documentation/teams/teams-roles)

To create a new role with your desired permissions, navigate to the **Roles** tab of the **Members** **Page**. Then you can name the role and choose the permission groups that the new role will have access to. Once you are satisfied, click **Generate** to create the new role.

<Frame caption="Create Role with custom permissions">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=eb3adf6615921db1e9390af9b72344be" alt="" data-og-width="953" width="953" data-og-height="801" height="801" data-path="images/teams-quickstart-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=de8df1404d7e00c10e081c6f6e4a9d8e 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=2b7ed8c100580079daf0a6aea8748391 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=17b42a318365894a924521d201d5e3a3 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=e8f58d3d6db735cca2d661f8f6d7fe00 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=7b2c804d1835d6f4c1ed56fc08b33889 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-5.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d95a7559c72420c9397528e0a7ed7356 2500w" />
</Frame>

For more information on Permission Groups and what they allow access to, [click here](/api-reference/permissions-and-authorization).

## Inviting Team Members

To invite a team member, go to the **Members Page** and click on the **Invite** button.

This will bring up a quick popup where you can enter the email and team role for the person you want to invite. Once complete, click **Invite** to send the invitation email.

<Frame caption="Invite Member">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d963643955c5f12551d9173709c8f40b" alt="" data-og-width="800" width="800" data-og-height="605" height="605" data-path="images/teams-quickstart-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d25cd9cdaef7868d03026a1d2b0f9ddf 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=fcee46502ca03df6b1d1f629e92cdefc 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=0752c21e714cc0c5f5e8dbbf20f958c2 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=c7383bba2988ebdc45f96e8959be43e6 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=6434c18c1da509e41797e94bbccc41d9 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=6fab82b602917714b5432cb727d3892d 2500w" />
</Frame>

Once you send the invitation, the user should get an email asking them to join your team. Upon clicking the link in the email they will be added as a member of your team.

**Note:** if the recipient of the invitation does not have a Vast account, they will need to create one before being added to your Team.

Once the invitee has joined your team, you should see them listed in the **Members** section.

<Frame caption="Team Members">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=2a94f40a9320dbd81ce43cfeaa13c028" alt="" data-og-width="1171" width="1171" data-og-height="512" height="512" data-path="images/teams-quickstart-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=c564195ec6bc86800650f23865a1721f 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=5bfe04b4e0bec34e724b298450e1b958 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=1a2baf736ff5b39c377de1d15c715a1b 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=1046029b36e2b000a99e3b0ed5c359f2 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=13cf6e41d3c518787f094648bf4a332a 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-7.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=cd47702b3b116d64614b372f0732e54b 2500w" />
</Frame>

## Using SSH Keys with Team Instances

If you are part of a **team** and want to connect to a **team’s instance** using SSH, simply add your key to your individual account keys. Here’s how it works depending on the type of instance:

🔹 VM Instances

* Your SSH key **must be added to your personal account before the VM is created**.
* When the VM is launched, all SSH keys in your account are automatically included for access a team instance.

🔹 Non-VM Instances

* You can either:
  * **Add your SSH key directly to the instance**, or
  * **Add your key to your personal account**, in which case it will be automatically applied to the team instance as well.

<img src="https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=06bf91354f63ee759ee43d76b83a201b" alt="Screenshot2025 09 08171421 Pn" data-og-width="1016" width="1016" data-og-height="249" height="249" data-path="images/Screenshot2025-09-08171421.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?w=280&fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=4bfdd66394655ae9dff88ccae48bd548 280w, https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?w=560&fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=419842cd19411b071737de500e84aa4e 560w, https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?w=840&fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=dfc022c871b67fb4f257de16f4f5a275 840w, https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?w=1100&fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=eac559ba1163621bab1e234a7fd7029d 1100w, https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?w=1650&fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=5fb15162d5b4ff15371268e09372decf 1650w, https://mintcdn.com/vastai-80aa3a82/QCY8wvX6GFpUG_n2/images/Screenshot2025-09-08171421.png?w=2500&fit=max&auto=format&n=QCY8wvX6GFpUG_n2&q=85&s=947f12c38900b6f47360d2874f8eadf6 2500w" />

## Conclusion

You have now successfully created a team!

From this point, you can add any Billing information the same way as a regular account and invite as many of your teammates as you like so you can collaborate together with ease.

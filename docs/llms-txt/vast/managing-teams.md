# Source: https://docs.vast.ai/documentation/teams/managing-teams.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Your Team

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Manage Your Vast.ai Team",
  "description": "A comprehensive guide covering all operations needed to manage your team including inviting members, managing roles, editing settings, transferring ownership, and deleting teams.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Navigate to the Members Page",
      "text": "The Members page is the main hub for managing your team. From this page, you can view all team members and their assigned roles, change member roles, remove team members, invite new members, and access team settings through the three-dot menu."
    },
    {
      "@type": "HowToStep",
      "name": "Invite Team Members",
      "text": "Go to the Members Page and click the Invite button. Enter the email and team role for the person you want to invite, then click Invite to send the invitation email. Anyone with team_write permissions can send invitations. Invitees will receive an email with a unique team invitation link. Note that team invitations expire after 4 hours."
    },
    {
      "@type": "HowToStep",
      "name": "Manage Member Roles",
      "text": "Change a member's role by clicking on the directional arrow next to their name and selecting a new role. Every team comes with two default roles: Manager (full access to team resources) and Member (limited read access while still being able to rent instances). You can also create custom roles with specific permissions."
    },
    {
      "@type": "HowToStep",
      "name": "Edit Team Settings",
      "text": "To change the team name, switch to Team Context, select the team you want to manage, open the Members Page, and click the three-dot menu to select 'Edit Team Name'. You must be a team owner or team manager to update the team name."
    },
    {
      "@type": "HowToStep",
      "name": "Transfer Team Ownership (Optional)",
      "text": "Navigate to the Members page and click the three-dot menu. Select Transfer Team Ownership, choose a new owner (who must already be a member of the team), and confirm the transfer. Once confirmed, ownership will be reassigned and your role will be changed to a manager."
    },
    {
      "@type": "HowToStep",
      "name": "Remove Team Members or Delete Team",
      "text": "To remove a team member, click Delete next to their name and confirm. To delete a team (owner only), open the three-dot menu on the Members page and select 'Delete team'. Make sure you have deleted all instances and machines before proceeding. Warning: This action is permanent and cannot be undone."
    }
  ]
})
}}
/>

This guide covers all the operations you'll need to manage your team after creation, including inviting members, managing roles, editing settings, and more.

## The Members Page

The Members page is the main hub for managing your team. Here you can view team members, assign roles, invite new members, and access team settings.

Here's an example of what a Members page looks like in the console:

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=edeb6ce87327da1cedb9d4ef60b575d3" alt="Members Page" data-og-width="1280" width="1280" data-og-height="890" height="890" data-path="images/console-members.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ec90f977173d2e2ffeec6807662b6006 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=67258ded6ffe21e36b52b4d4af04c908 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c076832c401edb7a63c1df12f5740ccf 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b3e67253ae07ccce43752d86a8ac3c6f 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c11f38b0d060d9fad853d2dc290e2a26 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9f32a8fe79c0fae48f657e9f0a779eae 2500w" />

From this page, you can:

* View all team members and their assigned roles
* Change member roles by clicking the directional arrow
* Remove team members
* Invite new members
* Access team settings (three-dot menu)

## Inviting Team Members

To invite a team member, go to the **Members Page** and click on the **Invite** button.

This will bring up a popup where you can enter the email and team role for the person you want to invite. Once complete, click **Invite** to send the invitation email.

<Frame caption="Invite Member">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d963643955c5f12551d9173709c8f40b" alt="" data-og-width="800" width="800" data-og-height="605" height="605" data-path="images/teams-quickstart-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=d25cd9cdaef7868d03026a1d2b0f9ddf 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=fcee46502ca03df6b1d1f629e92cdefc 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=0752c21e714cc0c5f5e8dbbf20f958c2 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=c7383bba2988ebdc45f96e8959be43e6 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=6434c18c1da509e41797e94bbccc41d9 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-6.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=6fab82b602917714b5432cb727d3892d 2500w" />
</Frame>

Anyone with the proper permissions (currently **team\_write**) can send invitations to invite team members at any role level.

### Accepting Team Invitations

1. **Receiving the Invitation Email**: Invitees will receive an email containing a unique team invitation link.
2. **Completing the Joining Process**: Clicking the link will initiate a set of operations to add the invitee to the team. This may involve signing into the Vast.ai platform or creating an account if necessary.
3. **Confirmation of Membership**: Once the process is complete, the new member will be officially added to the team and will have access based on their role.

**Note:** If the recipient of the invitation does not have a Vast account, they will need to create one before being added to your Team.

### Best Practices for Invitations

* **Ensure Accurate Email Address**: Double-check the email address before sending invitations to avoid any miscommunication.
* **Communicate with Invitees**: Inform potential team members that they will be receiving an invitation and what steps they need to follow.
* **Follow-up on Pending Invitations**: Keep track of sent invitations and follow up with invitees who haven't joined yet. **Note:** Team Invitations will expire after **4 hours.**

## Managing Member Roles

You can change a member's role by clicking on the directional arrow next to their name and selecting a new role.

<Frame caption="Change Roles">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7ada3883d8d900c0e13a8ac61247dcb7" alt="Roles" data-og-width="800" width="800" data-og-height="504" height="504" data-path="images/console-members-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=675c85fcfea338af3daeef4760191134 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=eb5fa74f98de477f4319ca8f940677f7 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7be3927548afc1f0909670315a790bb2 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9262e7d6f131fabb4ec99d1868f5dece 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c1e2f5ee67175c760ea62d75d1a43c18 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-2.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b3640bc05790cb394d928cf13dec1434 2500w" />
</Frame>

Every team comes with two default roles:

* **Manager**: Full access to team resources
* **Member**: Limited read access to most resources while still being able to rent instances

For detailed information about creating custom roles with specific permissions, see the [Teams Roles](/documentation/teams/teams-roles) documentation.

## Editing Team Settings

### Change Team Name

You must be a team owner or team manager to update the team name. Here is how to do it:

1. Switch to Team Context by clicking your profile in the top-left corner
2. Select the team you want to manage
3. Open the Members Page
4. Click the three-dot menu and select 'Edit Team Name'

<img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=bded8efb6d77674e88fa02ef994231c8" alt="" data-og-width="800" width="800" data-og-height="594" height="594" data-path="images/teams-quickstart-edit.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=f80fd939b41a3f0a884f731e54a40490 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=30775ee141d730928c322c778b5f911e 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=cb675fca342dfbdd825997583de6eb44 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=95e98a500e898fd58e8da6e36ef56ca6 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=7835a63598ddd3db83bbfbb87b89c3d8 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=8d8f4fd5fb8c72e00d4bb1976821c07e 2500w" />

The 'Edit team name' option opens a pop-up that allows you to enter and save a new team name.

<Frame caption="Edit team">
    <img src="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=85f59f8ffc1030e23f2300ef9a7bc095" alt="" data-og-width="800" width="800" data-og-height="461" height="461" data-path="images/teams-quickstart-edit-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?w=280&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=e040d1550deebf937df5fc8fca6dfa3a 280w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?w=560&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=4503b496387cf1076e06e28e3db2b5f7 560w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?w=840&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=b0d7245a03f78b741c494dd4d1e4590b 840w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?w=1100&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=79085810584e011d740546be4e97aede 1100w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?w=1650&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=91822825a8790a951aff0216670f8351 1650w, https://mintcdn.com/vastai-80aa3a82/KWV1TCiq0zjC57hU/images/teams-quickstart-edit-2.webp?w=2500&fit=max&auto=format&n=KWV1TCiq0zjC57hU&q=85&s=ddce522916ca71dce8a48941eef9fb3b 2500w" />
</Frame>

## Transferring Team Ownership

The Transfer Team Ownership feature allows an owner to seamlessly reassign the team to another member within it. To do so, navigate to the **Members** page and click the three-dot menu in the upper right corner.

<Frame caption="Three-dot menu">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=e26c429a692c1d77c0784e307f44a644" alt="" data-og-width="800" width="800" data-og-height="283" height="283" data-path="images/teams-transfer.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=bdf7af9a917ba99ba5a383638b873330 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=fd50661113710f6bb42db746dd3bb582 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=85dce935b3192a1b4200ee53def8aca4 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=3c6a5d73b2ee83934a4cd865b62f9109 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1ae3c868c72514d6d9231ff7da02bc73 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=7535241576ae2b5099d23452d94c40c2 2500w" />
</Frame>

From there, you can click **Transfer Team Ownership** and open a pop-up, select a new owner (who must already be a member of the team), and confirm the transfer. Once confirmed, ownership will be reassigned, and your role will be changed to a manager.

<Frame caption="Transfer Team Ownership pop-up">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5a1a23db2fc0e7a9c46465f9a088ed37" alt="" data-og-width="800" width="800" data-og-height="758" height="758" data-path="images/teams-transfer-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=d9db044f06fee4be475ac0acb0ff79df 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=b6cdf947b6406487910c24c974ec5407 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=cc55f9656901a2565f15bdbb1bfefe69 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=7a262c6a3349154982c76b24ec3c4bac 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=08ec086a8b613051702021fe17975826 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-transfer-2.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=ccd4e3d7bfc02a0de839ab1ae48ce395 2500w" />
</Frame>

## Removing Team Members

You can remove a team member by clicking on 'Delete' next to their name, which will trigger a confirmation pop-up.

<Frame caption="Remove Member">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=62e936356bfb9e79c866e6ba78c0c261" alt="Remove Member" data-og-width="800" width="800" data-og-height="353" height="353" data-path="images/console-members-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=f39bb79dea3afed7645d948be9d22048 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ebf88fdc789be8722708df287af7c9c2 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=df58eac23d32d907a62456ab204290da 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=1a15f18efd9f80c03e819bb6c543711e 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e6b20decae72863108efeeee3e2c2599 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-members-3.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=1e52fd3d3622404878290d1074eb6177 2500w" />
</Frame>

## Deleting a Team

Only the Team Owner can delete a team.

To delete a team, open the three-dot menu on the Members page and select 'Delete team'. Make sure you have deleted all instances from the Instances page, or all machines from the Machines page (if you are a host), before proceeding.

⚠ **Warning**: This action is permanent and cannot be undone. All team members will be removed and any remaining credits will be returned to your personal account.

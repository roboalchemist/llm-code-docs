# Source: https://docs.zapier.com/platform/build/reorder-action.md

# Reorder or remove action

> Whenever a user selects your app's integration in a Zapier action step, they'll see every _create_ and _search_ action in your integration. 

## Reordering actions

Zapier shows *create* actions first, followed by *search* actions. Within the Create and Search sections, actions are listed in alphabetical order and this order cannot be changed.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=1488bfcd2c6f77cbceb30ae769ca41ab" alt="Actions inside Zapier" data-og-width="1552" width="1552" data-og-height="884" height="884" data-path="images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=2c014d2852fd99c0f37f5e0359d55dd7 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=23372baffbf682a32b40cd064f0405bf 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9f01a35a4757845a0b5a5fdfbc6a374d 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=76e5fe5877bb3900c2872a1de2f0a7d0 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a4b1244f6632921a1875c1f9c3ec4f87 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5d3c2e8f9f6cf0f6daadd3ee97fa5e80.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=8eec3464f406c03bfc5fb049e110508d 2500w" />
</Frame>

If you don't want an action to be shown, you can change the action's visibility at any time.

To change an actions's visibility:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section on the left sidebar, click **Actions**.
4. Click on the action whose visibility you wish to change.
5. Scroll to the bottom of the page to the **Visibility in Editor** and select `Hidden` if you want to keep users from being able to select the action
6. Users with that action selected in their existing Zaps would continue to be able to use it, but if they edit the Zap and select a different action, they will not be able to select the `Hidden` action again.

## Removing actions

You may want to remove an action your app no longer supports. Deleted actions cannot be restored.

If you remove an action from a live Zapier integration, this will break existing Zaps. As such, before removing an action, always [create a new major version](/platform/manage/versions) of your integration, hide the action in the new version, to allow users to [manually switch to a new action](/platform/manage/change-keys) without breaking their Zaps. Monitor integration usage by action from the Dashboard to only remove actions with no usage.

To remove an action:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section on the left sidebar, click **Actions**.
4. Click on the ellipses for the action you wish to remove, and click **Delete**.
5. On the confirmation prompt, click **Delete**
   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=56d28c6094e1c5658e8bd80caf255562" alt="Remove Zapier action" data-og-width="1507" width="1507" data-og-height="873" height="873" data-path="images/809321da0cd78edef6f464eb1f803855.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=75ff126afb9f45c8817dd0110b59d5be 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=6e1745dd7dffd8423e43e379efb8cfcd 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=fc79226c8a2b29ef34104aae124ad2ae 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9dd131c5fe6418ee672d86eef8556eae 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=8ef68dc2fbb2f6246adaf489b60fe277 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/809321da0cd78edef6f464eb1f803855.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a81cbe86b4823b06b7957b39c378812d 2500w" />
   </Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

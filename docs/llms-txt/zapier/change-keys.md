# Source: https://docs.zapier.com/platform/manage/change-keys.md

# Change trigger or action key

## Change scenario

In cases where a trigger/action/search's custom code needs to be rewritten or a new v2 is replacing an older v1.

## Impact to users

Deleting a trigger/action/search in a new version is a breaking change - which would prevent migration of your users to the new version. Updating an existing trigger/action/search's custom code would allow for migration but break users' Zaps if the output changes.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b7073d22f1f7e8c5609ca814fef723d7" data-og-width="960" width="960" data-og-height="131" height="131" data-path="images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7220216e5e90bbcd8a1fb00af5431e67 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=2771b32bc9959d31c131351ae33a420e 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3b8651ca7ddecb8e50bb829f3a7f1432 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=955848a1e0f9de7452d0a233d0d3c2ee 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5b7924dc33b3beeccf5a5cda341cc330 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/65326a8f5fff0f9640c0d6fdc59dfa3b.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=fc551f3ad010fdf20edd99019c7a7a21 2500w" />
</Frame>

The triggers, actions, and searches are identified by their **key**, such as `new_contact` or `create_post`, so if you remove that key from the app's definition, or change it (possible in CLI apps only), this message appears when you attempt to migrate.

## Best practices

* If you have already renamed the **key** (possible in CLI apps only) for a trigger/action/search, you'll need to switch it back to the previous **key** to proceed with migrating users.
* If you need to remove a trigger/action/search, change its visibility to **hidden** instead. Use the Visibility Options dropdown in the [UI](https://platform.zapier.com/polling-trigger#1-add-the-trigger-settings), or the `hidden` key in the [CLI](https://github.com/zapier/zapier-platform/blob/main/packages/schema/docs/build/schema.md#basicdisplayschema).
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=0d2ce685b278df28cb54fd170d49f81a" data-og-width="1794" width="1794" data-og-height="157" height="157" data-path="images/73990d8049572347aea87fc304173ecc.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3fe3aea82bb491faba7fe3c7287c1365 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=31eaec17b9dbf467aa48f9603fe4a798 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=1ad6f7891fa906803462c350e9bc1fbf 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5b4de0e650746d0dddd88ea199863b47 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=52081dd1441bf88bab059a82c7eb4f22 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/73990d8049572347aea87fc304173ecc.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=bd7ce7f955135ddfe78b3ff306d97414 2500w" />
  </Frame>

Migrated Zaps that used the hidden trigger/action/search will now show it as Deprecated in the Zap editor, but will continue to function as long as the endpoints remain valid.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b7258386513897200439dfde2ca147b8" data-og-width="942" width="942" data-og-height="388" height="388" data-path="images/61a2ac6095433d278bc412c2e59408fc.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=e895226795e7689e29321fb76c02fe51 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=4a47a8b136c53ac24f2d00a779f89ef5 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d4fc25d039ae01310597a31ba0c49754 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a7a866a3183db7c53ac2a506730a2f10 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=2114650e4c0e74fd118516ed65d8ebb8 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/61a2ac6095433d278bc412c2e59408fc.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=78d41a01ebadcd48905be2253e715452 2500w" />
</Frame>

Once a user selects a different trigger/action/search when editing their Zap, they will not be able to retrieve the hidden one. New users will not see any `hidden` trigger/action/search as available for selection.

* If you need to add a new trigger/action/search that replaces the hidden one, create a duplicate and give it a new **key** (such as appending `_v2` on the end), and keep the Name and Description the same if the functionality for a user is the same.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a1d9ea12d1b7bcaa6c9aba9c31298b31" data-og-width="1889" width="1889" data-og-height="995" height="995" data-path="images/6231ec2b53271c7d83672f6ed232d0e3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d04be1b34a08735270295e939bef154a 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5fcead4c66b3f0dc4f0759a61ece3210 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=12876c0ee37625aee27d75d5c3bf93a7 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3ca9cea171c022477dccb201202cf586 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a76cb87b4c2882c071c55422ce91df05 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6231ec2b53271c7d83672f6ed232d0e3.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f45f40d674cf946848a9cf512d9b0a28 2500w" />
  </Frame>

* This way existing Zaps continue to work once migrated with the previous (and now hidden) definition, and new Zaps will only be able to select the new definition.

* In cases where the endpoint in the hidden trigger/action/search will be sunset and begin to return errors in the future, the impact to users would be as follows:

Once the API has been sunset, active Zaps (turned on) using the impacted trigger/action/search will produce errors when they run. Depending on [user's email notification settings](https://help.zapier.com/hc/en-us/articles/8496289225229), owners of these Zaps will be sent email notifications about these errors.

If those Zaps exceed the error ratio **and** users have not [overridden related settings in their Zaps](https://help.zapier.com/hc/en-us/articles/8496037690637-Troubleshoot-errors-in-Zapier#i-want-my-zap-to-continue-running-even-when-there-are-errors--0-6), those Zaps will be automatically turned off.

* If you'd like to add custom errors within Zapier for the hidden trigger/action/search at the time of the endpoint sunset, you could consider the following:

Create a new version of the integration that immediately throws a `z.errors.Error` exception in the `perform` method of the impacted trigger/action/search. Learn more for apps maintained in the [UI](/platform/manage/planning-changes#custom-error-handling-in-the-ui) or the [CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#zerrors).

*Promote* and then *migrate* users to this new version as close to the sunset date as possible.

The benefits of this approach are:

* Throwing an explicit exception will ensure impacted Zaps will hit the error ratio (and be turned off) at the earliest possible time.
* You can add a user-friendly message to the exception that users will see in both Zaps Runs on the [Zap History](https://help.zapier.com/hc/en-us/articles/8496291148685-View-and-manage-your-Zap-history) and also in email error notifications, e.g. *This function has been deprecated and is no longer available.*
* Here's an example of how a custom error message would be displayed on an action in the Zap History:
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4688d76ee858a965b34bf1664dce444c" data-og-width="1014" width="1014" data-og-height="445" height="445" data-path="images/50807aad2a2e2ecda9044a524dafba8c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9f2e5eba0253d986e2316f94d8c4b8bc 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=f3dc11366123bb9f743bea3550f70fc8 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=932cec23d9788de600aecaf34a34cc38 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=e21500def9c6491b6ec0a35de9d7a4cc 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ebe17ed39a4cb6ca912fcb55308cad36 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50807aad2a2e2ecda9044a524dafba8c.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=42d74d0cef7c8585778000b659b83958 2500w" />
  </Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

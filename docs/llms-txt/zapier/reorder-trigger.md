# Source: https://docs.zapier.com/platform/build/reorder-trigger.md

# Reorder or remove triggers

> Triggers are listed in alphabetical order in the Zap editor and this order cannot be changed.

## Reordering triggers

You can, however, change a trigger's visibility to control if it is shown to users or not.

To change a trigger's visibility:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section on the left sidebar, click **Triggers**.
4. Click on the trigger whose visibility you wish to change.
5. Scroll to the bottom of the page to the **Visibility in Editor** and select `Hidden` if you want to keep users from being able to select the trigger.
6. Users with that trigger selected in their existing Zaps would continue to be able to use it, but if they edit the Zap and select a different trigger, they will not be able to select the `Hidden` trigger again.
   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=09d0e1802fc6f6c6b050164b676af8be" data-og-width="1110" width="1110" data-og-height="151" height="151" data-path="images/51c3b8911b5384ddf03b9dbfffd40050.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4f7edd81515b34de3b04617d5f593573 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4371328bf9764b089c8831eacc678020 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=5be24525eb9ebe7914828afba0857af5 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=64378966277429eac07adc91e78e89ab 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7d04150d484097aefb61d79fbba98e0d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51c3b8911b5384ddf03b9dbfffd40050.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=20de795110c752ff086aeede809bfbb8 2500w" />
   </Frame>

## Removing triggers

You may want to remove a trigger that your app no longer supports, or fully rebuild a new one in place of the previous one.

> Note: It is best practice to not remove a trigger that has been used in a live integration version. If a trigger is in use, it is recommended to [hide it rather than deleting it](/platform/manage/planning-changes#updates-to-triggeractionsearch-keys). Only remove unused triggers from staging or development versions.

To remove a trigger:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section on the left sidebar, click **Triggers**.
4. Click on the ellipses for the trigger you wish to remove, and click **Delete**.
5. On the confirmation prompt, click **Delete**
   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=e89f8cb3e55bdaf517e8c145fe58156d" data-og-width="1025" width="1025" data-og-height="395" height="395" data-path="images/fc65459abad8ac60504f6085078bb361.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=bfa9be40075af761912fcbe136f5ca77 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=30ac31bccdc39c543a79a42fc0b22675 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=9f92cc3b3aa686f490f6648ba46c9604 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=3f2febb29d93735de5d1a7c26cc988d8 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f65497ed924e62cc45993b5578480fdd 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fc65459abad8ac60504f6085078bb361.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=786367a012852e00758026bc8bf84cb4 2500w" />
   </Frame>

Deleted triggers cannot be restored.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

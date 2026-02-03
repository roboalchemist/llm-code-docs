# Source: https://docs.unifygtm.com/reference/integrations/segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment Integration Guide

> This guide outlines how to connect your Segment workspace to Unify.

# Overview

If you use Segment to collect website analytics, Unify can be connected to your
Segment workspace as a destination in order to reveal web traffic data. This
will also let you build audiences and Plays using Segment analytics data.

# Steps

<Note>
  If you’re also using the Unify Tag, ensure it isn’t running on the same
  pages as Segment. Otherwise, events may be double counted.
</Note>

### Generate a key in Unify

1. Log in to Unify

2. Navigate to [Settings -> Integrations -> Segment](https://app.unifygtm.com/dashboard/settings/integrations/segment) and click **Setup**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f629a09a07d5de67bc7cbfa456108893" alt="Setup.png" data-og-width="2000" width="2000" data-og-height="1329" height="1329" data-path="images/53.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=df996a278fe7bd9ae993f35780797dc5 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=460fdebb6b407f278bffa52ef1aa5624 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=55881c3b33f35f9ec8be5e8293fa13c3 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7ad5962d63f510fbca3e80ca216dc15b 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=721faed7d996038e4515e7886fd6de9c 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4ed1cc879e75b33b65a3b4eebb2007c1 2500w" /></Frame>

3. Click the **Copy** button to copy the write key to your clipboard

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b6ebe5630f7cd5731f7ffa0c68fcc759" alt="Write Key.png" data-og-width="2000" width="2000" data-og-height="1329" height="1329" data-path="images/54.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=051960a213222d78a1bbc24adb42ae39 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7af6a399973b52c9d015e21e9e244aba 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=88994a08664d2f936bdc8274d3b37014 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=d5ea57830aaa2426ad56c68b39df57d4 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4f206ace2ab585e04dbf7807ed103f68 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=2061f372489e7fd25cab0b4294728822 2500w" /></Frame>

### Add Segment destination

1. Log in to Segment and click on the **Destinations** tab in the sidebar

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=24da26163177fb33eb7f27f3048593c5" alt="Screenshot 2023-08-23 at 8.02.29 PM.png" data-og-width="480" width="480" data-og-height="552" height="552" data-path="images/55.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=903d9a4ca167b7dfdf1846c14e462506 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=87e929c2527e6479b59e82217559f811 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=0fc3fef80ce1d2a65b73e338a7b1a9b5 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=1e68cb077b4e6aec0db132411dfacb15 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=2796809dccaf120c041a7d55c3f8cccd 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=36352931288f3de9495d6a7174d938eb 2500w" /></Frame>

2. Click **Add destination** in the top right corner

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=379089fb5a0816300977290b6eecabc1" alt="Screenshot 2023-08-23 at 7.02.47 PM.png" data-og-width="580" width="580" data-og-height="182" height="182" data-path="images/56.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=9f51ea710e307ecede0eb15d5beef26f 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=92612ad8420c65a3ccde3ebe6b4683e3 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4ae695279918da1d3473cfe6aaf25ae6 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=29185cd2a81369f8e9cdaa3342f877fc 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4c0e3ba3db82d2dbdcfbca2fe5a4c1f7 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=8485091e69083893699e4e23f26d56d5 2500w" /></Frame>

3. Search for “webhook” and select the **Webhook (actions)** destination

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f8ba7a4e1baf18efd52cbf086b547005" alt="Screenshot 2023-08-23 at 7.03.49 PM.png" data-og-width="580" width="580" data-og-height="249" height="249" data-path="images/57.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=68f29c8e08f364eef17c56b44b5cf576 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=816b8af70354f3441a0cf05d68e22044 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=63dff82e4b70f8678c7620e5412f4d26 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=39e4535796122ff4299829f543900608 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=3f761fd4eed74e78047039e38d848b28 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=77a1ad489eb49239bf848f5c264e36ed 2500w" /></Frame>

4. Click **Add destination** again in the top right corner

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=0fce45f6e023787737ffed8968e51334" alt="Screenshot 2023-08-23 at 7.05.58 PM.png" data-og-width="2000" width="2000" data-og-height="1312" height="1312" data-path="images/58.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c3d22724ff84a83d37a4077b046084f1 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=39e0963f822234738226b961b55d876a 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=86e55370218185b24b4269595a6796a6 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b9c41bcea18b3d377a12aa51971fb56e 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=33f49d17295bf03dd94f360e7a2a4d1e 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=044acf50e506e11435a28d93733ca14f 2500w" /></Frame>

5. Select website source whose data you want to send to Unify and then click **Next**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=badeaf966f78d2bb57e6452001d0a48d" alt="Screenshot 2023-08-23 at 7.08.02 PM.png" data-og-width="2000" width="2000" data-og-height="1120" height="1120" data-path="images/59.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7344ef79d7bac6547c260dede4a1322d 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f274de83c1bfca90d590578e6f0efd7a 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=445ca7982a838f1163e5d1ca1c6e2802 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=bc64cb5cb7a7cca808b646ae06037c7a 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=8db1a2de1c86f509985172609516fa95 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f50d6224f19d759cbbc4a8896906a4b0 2500w" /></Frame>

6. Give this destination a name, make sure **Fill in settings manually** is selected, and click **Create destination**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=1f16e50997242eb3c75af440f8b96feb" alt="Screenshot 2023-08-23 at 7.13.50 PM.png" data-og-width="2000" width="2000" data-og-height="1120" height="1120" data-path="images/60.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=eb06f0bbd5228f79397104352c41f7ed 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=e82434032dc43ee20b0117d7eb911ed0 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c4728f13d0048aa42303e5f3144513bf 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=54ee9da16309fc3f112a3e05fb67fef5 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c9f8649fefda99a749c62ea883b1fa6a 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=86c8c1eaadd34156c989f25dd33d6d7e 2500w" /></Frame>

7. Click on the **Mappings** tab on the top and then select **New Mapping**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=34ea46b0bb84ce018cf2bd321eaa3288" alt="Screenshot 2023-08-23 at 7.18.04 PM.png" data-og-width="2000" width="2000" data-og-height="1310" height="1310" data-path="images/61.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4dde078bba98b1d36f3ff77b76466926 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b0bbe6d0ac6cce785cd3bc79e8ef2ace 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4b06672b3614d60b8467d73d22db348d 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=afab0babd9b0b89eab4de08cffac14ed 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=a4994b3f9951d31561a34bbafd2af4a7 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7babc6451378736091e701bd763580c2 2500w" /></Frame>

8. Choose the **Send** option

   <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=aede00c7fb3b01a961e528900005836d" alt="Screenshot 2023-08-23 at 7.21.39 PM.png" data-og-width="2000" width="2000" data-og-height="1088" height="1088" data-path="images/62.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0137248863ca94ea854f665e31e09b8e 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e41b2a8f493610ac760ca4811ba4ee21 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=a715159b20ff9ac79a518fc990820919 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=95969236fcd55764bbb1d1e3deb7ebcc 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=69f7095e1194c2436e7495cebed5a79b 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5b392ba5bd79571ae6537163d759c260 2500w" /></Frame>

9. Fill in the following mapping values…
   1. Under **Section 1**:

      1. Unify currently supports Page and Identify event types. Track events will be supported soon. You should select **any** and then list these types.
      2. If there are specific event types that you know you do not want to forward to Unify, you can safely omit them.

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=73ac92bbf6a4be152a5e8cc90c8e29fd" alt="Screenshot 2023-08-23 at 7.24.38 PM.png" data-og-width="2000" width="2000" data-og-height="770" height="770" data-path="images/63.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1fd08bb01166d9d00ececb25f203fd2d 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b6f5d3acb29214a1de41160c87a091c6 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b1f099a33604e4199cf4825315660b01 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2f9b6cc35a9495c7e36c29f13dab3e4d 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f873ee61649448e7e32df139d6508537 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=11f13b569280066e1f497bffe5c8051b 2500w" /></Frame>

   2. Under **Section 2**:

      1. Click **Load Sample Event** to populate the box with an example Segment event

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=97aeeeb9d9239342b59fa624be477b28" alt="Screenshot 2023-08-23 at 7.29.31 PM.png" data-og-width="2000" width="2000" data-og-height="1229" height="1229" data-path="images/64.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=81d78da8d0865250989de7e96a3c1448 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9d0e8040457c36e729f9252a06ea325e 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=98aca53d6acb54c5625b28ba9d1fd869 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=22493118e21a01cca5ec65d9764c57c4 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=8b1fb6dd06fb22965c4a3605751af2c0 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=912abd28e8120e3b5a7457495e12ebc8 2500w" /></Frame>

   3. Under **Section 3**:

      1. Next to **URL**, fill in the following value:

         ```
         https://analytics.unifygtm.com/api/v1/webhooks/segment
         ```

      2. List two values under **Headers** (click **Add Mapping Field** to add more boxes):
         1. `<YOUR WRITE KEY` → `X-Write-Key`
         2. `application-json` → `Content-Type`

      3. Be sure to replace `<YOUR WRITE KEY>` with the key you copied earlier

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=de35b4f8dea4d7a97e2bfbb61a1ca79c" alt="Screenshot 2023-08-23 at 7.42.22 PM.png" data-og-width="2000" width="2000" data-og-height="2301" height="2301" data-path="images/65.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=49a6ec26e80401583ae06bcc5422358c 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=25efd4b9f56dfad01aad5b17aa86b8db 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1537dd8e39a5ba93a76cc8f87fbff6f3 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=138fb67fbb5d8b4ec17df2f1729fe309 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2970d25e9d0e022efc297418af84039f 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4a328474d5343b557237d99e68ebde65 2500w" /></Frame>

   4. Under **Section 4**:

      1. Send a test event to verify that it’s working

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c089096e1eec784eaa551bdbdf25295d" alt="Screenshot 2023-08-23 at 7.44.09 PM.png" data-og-width="2000" width="2000" data-og-height="1031" height="1031" data-path="images/66.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2adc82442b01ead8e7b964be5532ed1a 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ca4b43b72136f15dc0a077dfc5f85150 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5f6203f0d8e24933f07dff91086c7097 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3983840d43a682d8efe0b0687f18e400 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5b9735e08fb4047af8d4ce3e94d0936e 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b2406d656da98b8fd4192db87f03bb0b 2500w" /></Frame>

That’s it! If you see **Test succeeded**, you’re all set. Traffic should now be flowing into Unify.

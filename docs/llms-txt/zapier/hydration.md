# Source: https://docs.zapier.com/platform/build-cli/hydration.md

# Hydration

> The best answer to this lives in our [CLI docs](https://docs.zapier.com/platform/reference/cli-docs#dehydration):

## What is dehydration & hydration?

<Info>
  Dehydration, and its counterpart hydration, is a tool that can lazily load
  data that might be otherwise expensive to retrieve aggressively.
</Info>

From a developer's perspective, you only need to worry about dehydration—Zapier will cover the hydration side of things.

## When to use dehydration?

The two most common times you should use dehydration in a Zapier integration are when:

1. You need to retrieve extra information from an API (e.g. a resource's list endpoint only returns IDs, but content must be retrieved per ID)
2. You need to provide access to a file (or files)

## Why use dehydration?

The core reason is reducing load to your API in case #1 above, where Zapier could fetch a list of known IDs of resources every 1-15 minutes per Zap, instead of the full definition of each of those resources. Putting any secondary requests behind a dehydration pointer means the request is made only once, although a Zap might see the same records again and again based on its polling cycle.

Dehydration saves even more bandwidth with files. No polling trigger should return files without dehydration, because otherwise, your app will send that file to Zapier around 100-300 times per day. For file outputs, implementing dehydration means the file will only be accessed and downloaded when a later Zap step asks for it.

The second reason is time. Your integration gets [30 seconds to run its API calls and any additional code](/platform/build/troubleshoot-trigger-timeouts#trigger-runs-in-a-zap) each time a Zap step runs before the step would time out. If you are running into that time limit, consider if work could be offloaded to dehydration and hydration.

## How to use dehydration?

Check out our [example "files" app](https://github.com/zapier/zapier-platform/tree/main/example-apps/files) for an example of file dehydration in action with a working Zapier demo integration. You can even initialize a Zapier app based on that repo by entering `zapier-platform init . --template=files` (or deprecated `zapier init . --template=files`) in Terminal to see it in your local code editor.

## Hydration in action

Some key areas include `index.js`, `hydrators.js`, `triggers/newFile.js`, and `creates/uploadFile.js`.

When building your integration, you'll likely be retrieving file info from a remote server. Instead, this example integration hard codes file urls to demonstrate.

The `New File` Trigger returns those file urls. The method [`z.dehydrateFile`](https://github.com/zapier/zapier-platform/blob/master/packages/cli/README.md#zdehydratefilefunc-inputdata) is used to create a pointer to the `downloadFile` function. In order to pass those files to other apps in actions, we reference `hydrators.downloadFile`, our hydrating function given a file url.

If you look at the `hydrators.js` file, you can see the `downloadFile` function. `downloadFile` calls the method[`z.stashFile`](https://github.com/zapier/zapier-platform/blob/master/packages/cli/README.md#zstashfilebufferstringstream-knownlength-filename-contenttype) to return a URL file pointer.

All of these will work together to lazily fetch the trigger data only when needed, avoiding API calls during polling or for reuse.

The only Action for this app is to upload the file, given a `bundle.inputData.file`.

### Setup

First, install the sample Zapier app `zapier-platform init . --template=files` (or deprecated `zapier init . --template=files`) and `zapier-platform push` (or deprecated `zapier push`) it to Zapier. If you've not worked with the CLI before, start by checking out the [tutorial](/platform/quickstart/cli-tutorial).

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=10d35a904ff0f4836b4e445a619df79d" data-og-width="1071" width="1071" data-og-height="479" height="479" data-path="images/c3e87ca1ba18ce915d23dedf055e61af.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=4135cbfedbf6a9aaefcab2d067491f3d 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=73e08f93aed1d523b9d6da06ef99d713 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=89e584e85cb5423476b2bf9798c617f4 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=261c5a722f5c14b0963dcba1abacc090 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=e7cea3b885e0a5bceb3fbcee0ec13c8c 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c3e87ca1ba18ce915d23dedf055e61af.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=93274d6e080e731523551de2176a6b3f 2500w" />

  {" "}
</Frame>

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=83472d9bfe96a547cad21c61653cdbce" data-og-width="1080" width="1080" data-og-height="701" height="701" data-path="images/914893706d089af76bb445b3d885908d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=1ed23bdcaf4f6dc0613128ecf8ac772f 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=bff25734ecfcfedd3807944c9a3ca367 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=53bf9878deeac4ef6a07a2631166a10b 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=69c70898db5c7f666655964c8d414dc1 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5dfe4033d37254bbd79cdffecbe1eae1 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/914893706d089af76bb445b3d885908d.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=922365f8e5df329e7c5769f30a014cba 2500w" />

  {" "}
</Frame>

Here's how the integration looks in [Zapier's developer dashboard](https://developer.zapier.com/). Add an optional icon to it if you like.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=0cc2ce559e3906821574c90b478b53a1" data-og-width="1692" width="1692" data-og-height="1137" height="1137" data-path="images/13df6356d05b5bb3e4533666bbfcc680.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3b4bf4b3388c20e82c63516e8cc65e2a 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=247a1360aabe87444ca8d1ea92bb57aa 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f0ad1fa14c6346ec611a7d40d30ac87b 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=0c0c75e95cbf66f7038371dfeca51bb3 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8c1778ceaa98dbc754b29298d5aa6a9b 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/13df6356d05b5bb3e4533666bbfcc680.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=338816d2d19b58af940f5ec3793b4b3f 2500w" />

  {" "}
</Frame>

Next, we'll want to add a Zap. Open the [Zap editor](https://zapier.com/editor), and select your integration's trigger.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ad94a5d340972a980db194ffd993dedf" data-og-width="1573" width="1573" data-og-height="1121" height="1121" data-path="images/50a4c0399eef2728b1f3e2b67f7fb916.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9682569fb026f203e97b8425ba4ed089 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8f4da6aa16f6c0e3164f010c4e5701b4 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b840edca5a60c09200fb340a3b3e4451 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9d02fc1430b91379f2ee122de2601495 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a033cc77ec3e3d8879f9238b250d5a8f 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/50a4c0399eef2728b1f3e2b67f7fb916.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ce12bcff6a58215fb4fdf086b8f6bad2 2500w" />

  {" "}
</Frame>

Select continue - you'll notice this app has no authentication, as the file urls are accessible without it. Select `Test trigger` to see the three sample urls pulled in and hydrated pointer for each.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=dedd6fb4edb2061c445fcabed545aa23" data-og-width="970" width="970" data-og-height="772" height="772" data-path="images/c68b2539d72c6c72da2ba3c35c9cef8d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=ba515ed83ab0cda6f498f34df780c118 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=101251b05381b92bb939c47f6e5ecdcf 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=fb704998935e56923ed8670132db62ed 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=07a1a4d79812468decf4cc564561a936 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3790217c4cbb8000c6dcc7df23b3e9f2 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c68b2539d72c6c72da2ba3c35c9cef8d.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=7005f5f2a3b0507dcb8f257d1179b3c4 2500w" />

  {" "}
</Frame>

Now let's add the `Upload File` action to the Zap. Normally, we wouldn't want a setup like this (trigger off of new file / create a new file), because it would result in a [Zap loop](https://help.zapier.com/hc/en-us/articles/8496232045453-Zap-is-stuck-in-a-loop). But this is just a test—and be sure to turn the Zap off shortly after it's turned on.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=c76608ff473d956595054f6719156bac" data-og-width="1695" width="1695" data-og-height="1043" height="1043" data-path="images/28ed4762db06d0dd95563a4480a8dc36.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=df80c5d936777979014ede3646007da4 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=eff7ed0aa924138d8ffcf160ac8af6c0 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f7ced1fe6d4b3388bd7f1672ddaa247b 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=743e7232dcef5feac04738200a800400 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=075d483c30e6791a98e4c63a831336c2 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/28ed4762db06d0dd95563a4480a8dc36.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=27b247a53ce6bb1e6d2595d1fabde7bb 2500w" />

  {" "}
</Frame>

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3a16e4f5f30cb955af593c47a4ee0dca" data-og-width="1719" width="1719" data-og-height="891" height="891" data-path="images/dd56ad225973829fbdc9fa1bcec5a2da.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=9050a94b080e92a9b23bd58fc259d34b 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=ccfc37d05711284e847622fb7efad98f 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8fabf0b73700cc335dfd1c6e4cf5e8c3 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=5d2c678eb06c097400a1b21ac636bcc6 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=c95109a2eef0868a1cd822400360d83b 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dd56ad225973829fbdc9fa1bcec5a2da.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=33d2a6285a57c48e2d62cc9b94e9b043 2500w" />

  {" "}
</Frame>

Above, you'll see the string that prompts Zapier to hydrate a file. When the Zap runner encounters a string like this, Zapier will call the defined hydration function with the proper arguments.

After selecting `Test step`, you will see three new requests show in the `Monitoring` [tab of your integration](/platform/build/test-monitoring):

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e084b9bc3a34e78973ceb97756f4f9c7" data-og-width="1711" width="1711" data-og-height="1014" height="1014" data-path="images/97152cd0012be0e7c35385a4f4b3f50a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=48a2cd0b6dd14759e3aeeefc1f91fd56 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=0f986f6d9c081b8dc72db24a9f3c6468 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=30292addeccb46d7d023e6f2f74c3cec 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=145d824f440c6f9928d407971ace7aa9 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=7535af80f727cf9b510ddd78512d7835 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/97152cd0012be0e7c35385a4f4b3f50a.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9190ab40e96e10c36b36bb355eccc152 2500w" />

  {" "}
</Frame>

The POST at the top was from the upload itself. The GET requests retrieve the file from the pointer provided by the trigger.

Now the Zap is ready to be turned on!

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=261a8ce8336471b12eaf6b3ca2e52db6" data-og-width="1660" width="1660" data-og-height="1156" height="1156" data-path="images/81cac4d9b52b6a76194d5af91949bfef.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7baf5c609075011af57b7855265c5309 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5e7c122d839f8abcd1c32d2f37066a2c 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f58284babd57e3a10befc5c63089fcae 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=73af5c56b7f9eae5ebda04ceca16cc2d 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=983e90d7e4f67ba72c63ecc5ee2283d4 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81cac4d9b52b6a76194d5af91949bfef.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b891ad3408f6138eac0cb63cfd837740 2500w" />

  {" "}
</Frame>

In this example app integration, the trigger will not run automatically due to the hard coded file urls used for illustrative purposes. Once you replace the `fileURLs` in the trigger `perform`, with a request to your API that returns the triggering file, you'll be able to test this out fully.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

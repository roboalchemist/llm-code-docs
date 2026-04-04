# Source: https://docs.zapier.com/platform/build/error-array-expected.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Error: An array is expected

> When you add a polling trigger or search action to your integration, the Zapier platform [expects a bare array of new or found items returned](/platform/build/response-types), sorted in reverse chronological order. An API may instead return a result _object_ that contains the array of items the trigger/search needs.

## Error shown

For example, for a “Find Issue” search action with GitHub's API, we might start with a `https://api.github.com/repos/{{bundle.inputData.owner}}/ {{bundle.inputData.repo}}/issues/{{bundle.inputData.issue_number}}` request:

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=ac6fb4a8108d66b02e9f5eb3f1108b79" data-og-width="1229" width="1229" data-og-height="401" height="401" data-path="images/a5516cc30abee4f84a58ac5b7b3dfc76.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=181d5f8ed1a4834f42aecb516dd28bad 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=fb3de565cad30d410cf9f1e381a0cfff 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=4fd59ea13e4912aff678fdfaab7d8d2e 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=56667e8d7c3e6730035590e1ec536249 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=72d88c1658d8e0d9e4801471d239a4f4 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a5516cc30abee4f84a58ac5b7b3dfc76.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9aa8fada58471e9535482c0c12639091 2500w" />

  {" "}
</Frame>

When tested, Zapier will show an error message `Results must be an array, got: object,`

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=06cde1cd6e874a8c397be273e4f0dfba" data-og-width="1215" width="1215" data-og-height="925" height="925" data-path="images/2461b0e7f49ecf5aed90d429a59ad2bf.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=e56c0570cef6f1b0e2d2ad4fa95c959a 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=2e4888ce1fe6516daffbc6df96be8c6a 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3c277e1c029c7d274f3546b4b16b559b 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=b530f7cd65b30cdb9b4f41adeaa7c631 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=2ab85cf67b5dd6564c46e3b3a3cc04b1 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2461b0e7f49ecf5aed90d429a59ad2bf.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=50b740fe11f5f3765c00cb09d7056873 2500w" />

  {" "}
</Frame>

Check the API response in the HTTP tab of the *[Test your API Request](/platform/build/test-triggers-actions)* section, and you'll see an *object* that contains the array of items we need was returned, not the array itself:

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a3f9044ec76524e9aaf2e40b1106610f" data-og-width="1144" width="1144" data-og-height="961" height="961" data-path="images/d569e3a05f643a9a199b5d85dc4a4fc2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3dbcbe9acffc6ed09b31dcc65c326b6a 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=bf6111bb07423dd66b4e3421e06eebf6 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=1b20e4de819e2dfb7b053e99640e3434 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=dfb1b4e46acaabdf7bf02cc0002c6c41 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=649b5c26cab3cbf716a9637e838f9726 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d569e3a05f643a9a199b5d85dc4a4fc2.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=cc14b95e01cb623287fb4be973d40add 2500w" />

  {" "}
</Frame>

## Solution

Instead, return that array of channels to Zapier. To do that switch to [Code Mode](/platform/build/code-mode) in your request. That will allow you to provide a JavaScript function to handle the request, and make needed changes to the structure or content of the result before returning data to the Zapier platform.

For this request, wrap the response with an array instead of the default `return results`, to have Zapier return an array of issues.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=2f57c7632c52f98e5e00237ebda532b9" data-og-width="1223" width="1223" data-og-height="705" height="705" data-path="images/3bec13fa502f47ff1e5f9bfded052b4d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=00e639fe1a1d8ae563102ecb4921957a 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9d819cd03d78c743906ebb7d10acc66b 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=54be3c08c0e669f357783b15bab9e9c7 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=21ad460a9aad3defa1a0946a97724f96 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d2e3256d2d558a840e490dbc6f96d82d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3bec13fa502f47ff1e5f9bfded052b4d.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=df7f3fbb6a1bac8cc4851b105c6189f0 2500w" />

  {" "}
</Frame>

> Remember: [Code Mode](/platform/build/code-mode) is a toggle; if you switch back to Form Mode your code will be ignored!

Now, retest the request and it should run successfully.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a1dd806729d99a6828aabf6bca218018" data-og-width="1226" width="1226" data-og-height="644" height="644" data-path="images/af56c7fed5183aed462d2e7efbf78f8c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=6b67a4d1a22e1a4351b03423e17d40a5 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b43498ac63db770042f47fc7a38519ad 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=33d35366fa066fc7c8ba28603b6ed7f8 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=bc5159e0c2b2aea78cc7be9220cc633d 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5263dc5241ae18f299c629c6cf1bb121 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/af56c7fed5183aed462d2e7efbf78f8c.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=4ebafdd3d5cb9d3e5820a22bb8c7f030 2500w" />

  {" "}
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

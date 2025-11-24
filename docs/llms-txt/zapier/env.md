# Source: https://docs.zapier.com/platform/build/env.md

# Use environment variables in your API call

> Integrations can define environment variables that are available when the app's code executes. They are useful when you have data like an OAuth client ID and secret that you don't want to commit to source control. Environment variables can also be used as a way to toggle between a staging and production environment during app development and this would be recommended instead of the use of an independent integration for staging purposes.

Environment variables are defined on a per-version basis. Much like in local development environments such as the one in the [Platform CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#environment), environment variables store key and value pairs outside of your app's API calls. Instead of hardcoding critical, secret values into your API authentication, trigger, and action calls, it's best to add them as environment variables in your integration, then reference the environment variable in your API calls.

If using OAuth v2 Authentication, the client ID and client secret fields are reserved environment variables. You'll need to use custom variable names for any other variables.

## 1. Add environment variables

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3d1885847d0989a8bacd244426d21ed5" alt="Add Zapier environment variables" data-og-width="1641" width="1641" data-og-height="874" height="874" data-path="images/52c80699c321084eaaf7b387c47bd438.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d15fbd8a9f678e429ea1dc5502154dfe 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=de9e68d1d66c25cadc0bdb4d16147cf1 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=707d7bb84ae1a5684a82ed2f55ca6b8a 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c0ff7b42ac17c49db240c47c83df4adb 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=1fd93c9d3493b4d3c0709e4dbd062780 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/52c80699c321084eaaf7b387c47bd438.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=2144865b685e6d5f138b0e9d84996b49 2500w" />
</Frame>

To add environment variables:

* Log into the [Platform UI](https://zapier.com/app/developer).
* Select your **integration**.
* In the *Build* section in the left sidebar, click **Advanced** . There you can add your environment variables including a key and a value for each.
* Click **Add** to include additional environment variables, or click the `x` icon to remove variables if needed.
* Once you've completed adding a key and value, click **Save**.

## 2. Reference environment variables

<Frame caption="Use environment variables in Zapier's API call forms or in custom code">
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f47960e259bbcdfe9dcfe3df90703c15" alt="Use Zapier environment variable" data-og-width="1643" width="1643" data-og-height="1089" height="1089" data-path="images/226591ede97cbcde75481b38fa0cd64f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=81a0d315ea86367ff2b2619f351643da 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=4a6fe7d7331901da3e0f26ac4bd957ed 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=a364ffe0a4ad654b3f1efc28573de09d 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=2f047e1c1b69ede585a65b7249d64668 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=6a65e0356c5f63b91807826d06798e3b 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/226591ede97cbcde75481b38fa0cd64f.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=748ca48dabb268a42e914860a4dc9539 2500w" />
</Frame>

Use environment variables in any Zapier integration API call through the form's *Show Options* link, selecting *Request Body*, *URL Params* or *HTTP Headers* as your API expects. Reference the environment variable you've configured under *Advanced*, in the form with the following text, replacing `YOUR_KEY` with your actual key: `{{process.env.YOUR_KEY}}` Zapier will then replace that variable with the value for that key from your *Advanced* settings and will use the correct value every time if you change it in the future. You can also reference environment variables in custom code if you switch your API call to code mode.

## 3. Change environment variables

<Frame caption="You can change environment variable values, but not the original keys">
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=84c082c98087567732feb2b9dc2c1585" alt="Edit Zapier Environment Variables" data-og-width="1009" width="1009" data-og-height="759" height="759" data-path="images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=6d351a3e662b2da17c426df9e60c92dc 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d23f9da6d284c4c055fdb6e03b12d8d3 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=1a9c18c6799e40b41616d48f289ac18b 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=240df58b331015bc70039f49f8456c3b 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=0be7cf8d1b26e2344ecb03a890794a1b 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2bbe32e1bcfd77c62a75fce5be6eb03a.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d21c83ce223ff1e286a4dab611dc66c3 2500w" />
</Frame>

It is possible to change your environment variables in a new version of your integration, or when switching from dev to production endpoints for the release of your integration to the public.

To change an environment variable:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section in the left sidebar, click **Advanced**.
4. Edit the text in the **Values** column with the new variable values. You cannot edit the *Key*. If you need to change a key and its value, first delete the old key, then add a new one instead.

## 4. Use environment variables for staging and production versions

We strongly recommend against the use of an independent integration for staging purposes. By utilising [version control](/platform/manage/versions) and environment variables instead, the deployment, integration and user management processes (eg. migration) will be significantly improved for your integration. It also helps [Developer Support](https://developer.zapier.com/contact) establish exactly what you're working on and identifying relevant logs.

It is conventional to reserve one version for testing/staging and one version for production, setting the applicable environment variables under *Advanced* in each.

If you want to be able to work with both environments in development in one version, one approach is the following:

* Set environment variables for both domains you want to call

* Set another environment variable for the domain you want to work with. For example, `key: ENVFLAG / value: staging`

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a097f2fd4a6a5b1ec79a0109c0fd44f9" data-og-width="826" width="826" data-og-height="209" height="209" data-path="images/e2820a532b072401560d6c6afd7c90f8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a6585c241ab879073698238cfde3d4c6 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8f6f8ea7d548f797dee14661b0731d88 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=785b1a822ae7f44ad7f65e94f9a0a4ad 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=7f1dcdd77f57ac353c8ca069bff8e681 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8afdb744ea8ebb50b1750b2beb456c8d 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e2820a532b072401560d6c6afd7c90f8.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=c786cc66c878b5d0d2f04994ca71aa54 2500w" />
  </Frame>

* Throughout the app, in [Code Mode](/platform/build/code-mode), check the value of the latter variable and conditionally reference the corresponding domain environment variable.

For example:

```js  theme={null}
let domain;

if (process.env.ENVFLAG === "staging") {
  domain = process.env.STAGING
} else {
  domain = process.env.PRODUCTION
}

const options = {
  url: domain // conditional, depending on envFlag
  method: 'POST',
  headers: {
    // headers
  },
  body: {
    // body
  }
}
```

Thus, during development, you can toggle the value of one environment variable to conditionally call the corresponding domain.

However, once a version is pushed to production, the variables are fixed, so in the case of a [public app](/platform/quickstart/private-vs-public-integrations) make sure to set the flag environment variable accordingly before promoting.

## 5. Allow users to select an environment

Certain apps need to allow users to select the domain during authentication. To do so, create an [input field in the authentication form](/platform/build/oauth#optional-input-form), allowing the user to pick which domain they want their connection to interact with.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5647ba840162768dd95a9d4a5617a0e2" data-og-width="1100" width="1100" data-og-height="576" height="576" data-path="images/8da73bce1eb9f7b20c018be357c765b1.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=107df914bfc07e66a0641bde93112cb1 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2b7a2550d14adff94f7afe70b59a8eb8 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3d1b6803b1493b8382b63acf2dc3f193 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e8df3764645defa8da3cf7d728d2951a 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=bda08c6d6ed1d3559ba2d961d50b03ea 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8da73bce1eb9f7b20c018be357c765b1.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e78616f1f59145b65cfd09ccefcb4c9c 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=d94fce1fb66f4f52ab80f66acf544187" data-og-width="1068" width="1068" data-og-height="345" height="345" data-path="images/10bd5195508ba9d9cc43e711504f96be.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=bd8ffbc3783409a6462aadcc018cc826 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=c211d3b69e6d7563d121aed47cd3f98f 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=56a9284af8fb6dacad4019af0edcbb39 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=cd8397ff5eb9bdd78034eb2348a94422 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=91836b910099077385025874ab3146ac 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/10bd5195508ba9d9cc43e711504f96be.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=6ead9a4adb6daf758a88e88dc454a078 2500w" />
</Frame>

Reference the user's selection with `{{bundle.authData.env_url}}` throughout the integration to conditionally call the corresponding domain.

## Video Tutorial

You can refer to this video on using environment variables:

<video controls src="https://cdn.zappy.app/cb768909f391c96e8814d77c2eece503.mp4" />

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

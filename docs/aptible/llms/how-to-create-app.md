# Source: https://www.aptible.com/docs/how-to-guides/app-guides/how-to-create-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to create an app

Learn how to create an [app](/core-concepts/apps/overview)

> ❗️Apps handles cannot start with "internal-" because applications with that prefix cannot have [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview)

## Using the Dashboard

Apps can be created/provisioned within the Dashboard the following ways:

* Using the [**Deploy**](https://app.aptible.com/create) tool will automatically create a new app in a new environment as you deploy your code <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c3ec85cf5e8ec92a87df551f13bfdcfa" alt="" data-og-width="2560" width="2560" data-og-height="1280" height="1280" data-path="images/create-app1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=165e5282966f3f0fa2a7df8f945de1ff 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=934174730afdec35bb07d274807fc18d 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=4df0a5ea3a68fb733636643542a9b4ae 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a4d343b491ab0b1f74e913ca1c7cd27f 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=4d911a7137da038eba5b32476f9230ac 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app1.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d0a021ccafed4697a90ab1d27c21deb3 2500w" />

* From the Environment by:

  * Navigating to the respective Environment

  * Selecting the **Apps** tab

  * Selecting **Create App**

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=75af2b31fe3d8e99dcbb24510aba1e02" alt="" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/create-app2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=8619d5fdb8fd0629596f46eeb598bc14 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=7126123f76743a0ecebf982447825eeb 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=6ce04c6e4055ac2099bd3beef9b8dcb0 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3b889e79e8de759ac2155d2edf9a1484 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=359335d4dce072e92807d49a6c5764f4 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/create-app2.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=bc20a35b56bddc1756e9dee86724b5e1 2500w" />

## Using the CLI

Apps can be created/provsioned via the Aptible CLI by using the [`aptible apps:create`](/reference/aptible-cli/cli-commands/cli-apps-create) command.

```js  theme={null}
aptible apps:create HANDLE
```

## Using Terraform

Apps can be created/provsioned via the [Aptible Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs) by using the terraform\_aptible\_app resource.

```js  theme={null}
data "aptible_app" "APP" {
    handle = "APP_HANDLE"
}
```

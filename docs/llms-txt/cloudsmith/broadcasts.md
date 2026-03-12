# Source: https://help.cloudsmith.io/docs/broadcasts.md

# Broadcasts

Share branded public repositories via a public facing URL.

> 📘 Early Access
>
> Broadcasts are in Early Access. If you would like to try this feature, please [Contact us](https://help.cloudsmith.io/docs/contact-us).

One of the many challenges companies face today is publicly distributing software to users. This is essential for open source projects, public SDKs, developer tools, or package ecosystems where ease of access matters.

Cloudsmith Broadcasts lets you securely share a repository using a public-facing URL with a few clicks, offering an enterprise-level range of controls:

* Publish your software to a **customized web portal**.
* Use your own domain for the Broadcast URL.
* **Monitor** usage and gain valuable insights into usage.
* **Control** what is available to users.

Users can browse and discover software artifacts from this public Broadcast page, and download artifacts via the browser, or pull them using native tooling such as their IDE or CI/CD build systems.

<Image align="center" src="https://files.readme.io/a5a471ee8bae4784ac0a26f3bdd75dcd8390c78c115788e6611d02208d98af56-Group_3_1.png" />

## Creating a broadcast

Any public repository can be turned into a Broadcast. To create a Broadcast, navigate to the required repository and click the “Broadcast” button.

<Image align="center" src="https://files.readme.io/32ff78dbf8e86fded0ebc1417ce5d082838f90d4b7925c6818b6c18208a210e6-Screenshot_2025-02-21_at_13.20.48.png" />

While a repository has a Broadcast active, the Broadcast button will read “Broadcasting”:

<Image align="center" src="https://files.readme.io/82db4db3b3e028f20847b0a5eaca65d3eb24358532c51b1511b05acd5dfe65a2-Screenshot_2025-02-21_at_13.31.18.png" />

You can view the public Broadcast page via your organization’s broadcast URL:

```text
https://broadcasts.cloudsmith.com/{organization-name}/{repository-name}
```

## Disabling a Broadcast

> 🚧 Disabling a Broadcast
>
> When a Broadcast is disabled, its public Broadcast URL will not be accessible.

To disable a Broadcast, press the “Broadcasting” button. Please note if a Broadcast is disabled, the URL associated with it will not be accessible.

<Image align="center" src="https://files.readme.io/14e82d13fab5ccbe1ed7233812a68423bf6eed0f6d085ad804d1660bcd2664d5-Screenshot_2025-02-21_at_13.25.50.png" />

## Broadcasts view

The Broadcasts view can be selected from the top left corner of the UI. This view provides an overview of all your Broadcasts and other Broadcast functionality available to you based on your customer pricing tier.

<Image align="center" src="https://files.readme.io/b5d121722ab295a5addae07ddc041c3a241903a1e1c3c5d5edc5097f2ee6d77b-Screenshot_2025-02-20_at_17.05.10.png" />

## Broadcast Analytics

> 📘 Broadcast Analytics
>
> Broadcast analytics are only available for Ultra customers.

The Broadcast Overview displays analytics for all Broadcasts in your Workspace. Broadcast analytics allow you to keep track of the following:

* The number of downloads across all of your Broadcasts in the last 30 days
* The most popular/downloaded broadcasts.
* The most popular/downloaded packages.

<Image align="center" src="https://files.readme.io/8b98ea7775c802b498da3e5c651c371ebfca344eedba6ad3914bb793391fed04-Screenshot_2025-02-20_at_17.08.46.png" />

### Analytics for a specific Broadcast

To view analytics specific to a given Broadcast, select that Broadcast. The Overview page for the Broadcast will include total downloads over the last 30 days and the most popular packages downloaded.

## Customizing a Broadcast

> 📘 Broadcast Theme Customization
>
> Broadcast customization is only available for Ultra customers.

The default Broadcast color scheme can be customized to allow your public broadcasts to match your organization's brand colors. To customize the appearance of your Broadcasts, click the **Theme Tab**.

<Image align="center" src="https://files.readme.io/cf047228716e5362113f2e7b783acebbb0ba719dd81d9dad001e1eee7655e92a-Screenshot_2025-02-17_at_15.15.15.png" />

From this view, you will be able to customize:

* The background, text and accent color used.
* The logo displayed.

## Custom domains

> 📘 Custom Domains
>
> Custom domains are only available for Ultra customers.

Broadcasts can be displayed on a custom domain. To do so, please contact Cloudsmith via support. You will need to provide your chosen custom domain, and Cloudsmith will provide you a `CNAME` to add to this domain. Cloudsmith will then let you know when your domain is published and available to use.

## Legacy public and open source repositories

> 🚧 Legacy Repository URLs
>
> It is advised to update any references to existing public repositories hosted on the legacy web app to reflect their respective Broadcast URL.

Broadcasts replace what were previously called public and open-source repositories in Cloudsmith. Public and open source repositories currently hosted on the legacy Cloudsmith web app will automatically have a corresponding Broadcast created on the new web app. As the legacy web app is [moved towards sunsetting](https://cloudsmith.com/blog/launching-the-new-cloudsmith-web-app), Cloudsmith will set up redirects for repositories on the legacy application to their corresponding Broadcasts. Although existing legacy URLs will still work as expected with redirects in place, Cloudsmith advises customers who have referenced any public repositories in their documentation etc., to change the respective URLs ahead of the legacy web app sunsetting.

For example, the legacy URL structure of:

```
https://cloudsmith.io/~{organization-name}/repos/{repository-name}/packages/
```

Should be updated to the new Broadcast URL structure of:

```
https://broadcasts.cloudsmith.com/{organization-name}/{repository-name}
```
# Source: https://mintlify.com/docs/deploy/route53-cloudfront.md

# AWS Route 53 and CloudFront

> Deploy documentation on AWS with Route 53 DNS and CloudFront CDN.

To host your documentation at a custom subpath such as `yoursite.com/docs` using AWS Route 53 and CloudFront, you need to configure your DNS provider to point to your CloudFront distribution.

## Repository structure

Your documentation files must be organized within your repository to match your chosen subpath structure. For example, if you want your documentation at `yoursite.com/docs`, you would create a `docs/` directory with all of your documentation files.

## High-level overview

Route traffic to these paths with a Cache Policy of **CachingDisabled**:

* `/.well-known/acme-challenge/*` - Required for Let's Encrypt certificate verification
* `/.well-known/vercel/*` - Required for domain verification
* `/docs/*` - Required for subpath routing
* `/docs/` - Required for subpath routing

Route traffic to this path with a Cache Policy of **CachingEnabled**:

* `/mintlify-assets/_next/static/*`
* `Default (*)`	- Your websites landing page

All Behaviors must have the an **origin request policy** of `AllViewerExceptHostHeader`.

<img src="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=666a7c785bcc7f6b2aa23424f8c1c668" alt="CloudFront &#x22;Behaviors&#x22; page with 4 behaviors: /docs/*, /docs, Default, and /.well-known/*." data-og-width="1603" width="1603" data-og-height="365" height="365" data-path="images/cloudfront/all-behaviors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=280&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=71017f7f8adb9707c30a4af5f18466c1 280w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=560&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b3d0b64d01d3d9405b3237ffe99e8b9f 560w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=840&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=97dd0acfd49dfd2f345f2fd3018e9db0 840w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1100&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b5f9cdf34197e6b4d86e36980d6a000f 1100w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1650&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=c4a30fd51baf478014221afc66c7ac2a 1650w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=2500&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b10b0389187a79b2367074200a34dc17 2500w" />

## Create CloudFront distribution

1. Navigate to [CloudFront](https://aws.amazon.com/cloudfront) inside the AWS console.
2. Select **Create distribution**.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=cd402e36a077943e5de51319a2fba9c3" alt="CloudFront Distributions page with the &#x22;Create distribution&#x22; button emphasized." data-og-width="3024" width="3024" data-og-height="922" height="922" data-path="images/cloudfront/create-distribution.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a14e9b98b0a52b5506139de3990ed56c 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=fff44181d05af6479ebf8f71793a9df2 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7f1bd8301e645206bd75dd4a00b39bb7 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=652ccfcf0b02689df1303e036689f30a 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=77d0f33cd3538e0945e392e3a7347aa3 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b3857c3316d9018af53d363296f156c1 2500w" />
</Frame>

3. For the Origin domain, input `[SUBDOMAIN].mintlify.dev` where `[SUBDOMAIN]` is your project's unique subdomain.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3bccb966a96cba7ec83364dabf5ba788" alt="CloudFront &#x22;Create distribution&#x22; page showing &#x22;acme.mintlify.dev&#x22; as the origin domain." data-og-width="1495" width="1495" data-og-height="1036" height="1036" data-path="images/cloudfront/origin-name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5f80b263a9f29ec240019d96d9edaf6d 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7746f61d09fcd8d68c2b82eedeba4a83 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5c4db2ba59e618dcb16f7219fa1d5c67 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f2adcb53996e6ba67072e566563a4b0e 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e1c482ddd1688c0b7b35f08a05ad8801 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3486245acffbe7d9eff91e179eb64dba 2500w" />
</Frame>

4. For "Web Application Firewall (WAF)," enable security protections.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=73a02de58bfbce884656443bb5d1ec42" alt="Web Application Firewall (WAF) options with &#x22;Enable security protections&#x22; selected." data-og-width="1482" width="1482" data-og-height="877" height="877" data-path="images/cloudfront/enable-security-protections.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8ad5bdde51829e1972c399de3d8806bf 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1d9535dfc44839225a3ac3b578a91f7a 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=13bccc1bd18c1e493697f946c42c99b0 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5b4d95a51ca31be7a27a651e149c11a8 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f859c34c5c459da088e65cf9d41fda5f 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=9b7a10b459e612101c36a21cc24b2c2e 2500w" />
</Frame>

5. The remaining settings should be default.
6. Select **Create distribution**.

## Add default origin

1. After creating the distribution, navigate to the "Origins" tab.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=bbf7cd128d5fa29b2d957e224757d90c" alt="A CloudFront distribution with the &#x22;Origins&#x22; tab highlighted." data-og-width="3024" width="3024" data-og-height="1466" height="1466" data-path="images/cloudfront/origins.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=aa7bae4c10cf41533acabddcfc54f568 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7d703fcc13c4526c48b3e82fce390324 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f0f0120635fd5452703f78e3db14f60c 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f26e5b8f578123e38f8b235252658b52 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b3949751be07019ea134de611921bf8e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9d8272f1f9a9066b3166330b8a707a69 2500w" />
</Frame>

2. Find your staging URL that mirrors the main domain. This is highly variant depending on how your landing page is hosted. For example, the Mintlify staging URL is [mintlify-landing-page.vercel.app](https://mintlify-landing-page.vercel.app).

<Info>
  If your landing page is hosted on Webflow, use Webflow's staging URL. It would look like `.webflow.io`.

  If you use Vercel, use the `.vercel.app` domain available for every project.
</Info>

3. Create a new Origin and add your staging URL as the "Origin domain."

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c67257bc20e907ea4da1a8719fae0543" alt="CloudFront &#x22;Create origin&#x22; page with a &#x22;Origin domain&#x22; input field highlighted." data-og-width="3024" width="3024" data-og-height="1332" height="1332" data-path="images/cloudfront/default-origin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=be2c93bed56c831d4f0328f913365927 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=762bf1eca446eeec28749e6d031b42fc 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=36f2f39ecd5607134cb037f3366de8a9 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5c0bf927f10b494efbe4860c3c0cc674 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8edb7f1a41443eda7cf820cabd9d9eb1 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c91110942758408e864542c42a152d04 2500w" />
</Frame>

By this point, you should have two Origins: one with `[SUBDOMAIN].mintlify.app` and another with your staging URL.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c1fdd6d6e346e0e7b3a669daba284fba" alt="CloudFront &#x22;Origins&#x22; page with two origins: One for mintlify and another for mintlify-landing-page." data-og-width="1230" width="1230" data-og-height="690" height="690" data-path="images/cloudfront/final-origins.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d6f49353d428a3918a50019415f3b332 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=dd47af40f1a0f2b3a293603a8996d94f 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=779c21e2440c9a67ab4f6c2868f21e11 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a4fb662350e37ebb0e890069d711ded7 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=bf9804c4703342bc0de775f27ff55494 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3ade799350b7e7ee33ccec38a974ed38 2500w" />
</Frame>

## Set behaviors

Behaviors in CloudFront enable control over the subpath logic. At a high level, we're looking to create the following logic:

* **If a user lands on your custom subpath**, go to `[SUBDOMAIN].mintlify.dev`.
* **If a user lands on any other page**, go the current landing page.

1. Navigate to the "Behaviors" tab of your CloudFront distribution.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=6ab02a43a5427d2d1306dfd6d313bc49" alt="CloudFront &#x22;Behaviors&#x22; tab highlighted." data-og-width="3024" width="3024" data-og-height="1384" height="1384" data-path="images/cloudfront/behaviors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f5cf4e6e79ea2cb17f57668d938b6d42 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b1657d38c9cdfbf180c746cf0bbab348 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=605f1ee4a420dd549a5feb4fe186063b 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=ca4656368268c50468cc87261d17092e 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7ad8b32781d0e8cdb8c7d2fc7b7b6691 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=19d0067d18ab1c69d03168c82be480ff 2500w" />
</Frame>

2. Select the **Create behavior** button and create the following behaviors.

### `/.well-known/*`

Create behaviors for Vercel domain verification paths with a **Path pattern** of `/.well-known/*` and set **Origin and origin groups** to your docs URL.

For "Cache policy," select **CachingDisabled** to ensure these verification requests pass through without caching.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=374fd2e53349cc9796515cda82a9b165" alt="CloudFront &#x22;Create behavior&#x22; page with a &#x22;Path pattern&#x22; of &#x22;/.well-known/*&#x22; and &#x22;Origin and origin groups&#x22; pointing to the staging URL." data-og-width="1413" width="1413" data-og-height="1098" height="1098" data-path="images/cloudfront/well-known-policy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=8ecced93fe28b40cbf6be37c834c6a8c 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a500a1b484f3251724a470987e156f43 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=be86e4de31b968087c11e4c780ab1e5d 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0889bd6abd0faa4f6eb972c62839e45c 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3659464f1ce1e75c49c2add0cc7c91ef 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ffc102f5136367e16b0cb21322be97b7 2500w" />
</Frame>

<Info>
  If `.well-known/*` is too generic, it can be narrowed down to 2 behaviors at a minimum for Vercel:

  * `/.well-known/vercel/*` - Required for Vercel domain verification
  * `/.well-known/acme-challenge/*` - Required for Let's Encrypt certificate verification
</Info>

### Your custom subpath

Create a behavior with a **Path pattern** of your chosen subpath, for example `/docs`, with **Origin and origin groups** pointing to the `.mintlify.dev` URL (in our case `acme.mintlify.dev`).

* Set "Cache policy" to **CachingOptimized**.
* Set "Origin request policy" to **AllViewerExceptHostHeader**.
* Set Viewer Protocol Policy to **Redirect HTTP to HTTPS**

<Frame>
    <img src="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=0ce9e6db0d16c0c095abf1bc44e68833" alt="CloudFront &#x22;Create behavior&#x22; page with a &#x22;Path pattern&#x22; of &#x22;/docs/*&#x22; and &#x22;Origin and origin groups&#x22; pointing to the acme.mintlify.dev URL." data-og-width="1520" width="1520" data-og-height="1117" height="1117" data-path="images/cloudfront/behavior-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=280&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=7ab1bb41895bb54e7e6aa14f6f83ac50 280w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=560&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=bb5384522a0a391acc94fd837abd4351 560w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=840&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=d56f68b911e11ce2a022e5740f80a7fe 840w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=1100&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=51107e34efbe3a0724823989b7c19221 1100w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=1650&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=17211bee07269e1ca4e013a7e8414b8c 1650w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=2500&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=275446c0ebfc6ad984632f2071291185 2500w" />
</Frame>

### Your custom subpath with wildcard

Create a behavior with a **Path pattern** of your chosen subpath followed by `/*`, for example `/docs/*`, and **Origin and origin groups** pointing to the same `.mintlify.dev` URL.

These settings should exactly match your base subpath behavior. With the exception of the **Path pattern**.

* Set "Cache policy" to **CachingOptimized**.
* Set "Origin request policy" to **AllViewerExceptHostHeader**.
* Set "Viewer protocol policy" to **Redirect HTTP to HTTPS**

### `/mintlify-assets/_next/static/*`

* Set "Cache policy" to **CachingOptimized**
* Set "Origin request policy" to **AllViewerExceptHostHeader**
* Set "Viewer protocol policy" to **Redirect HTTP to HTTPS**

### `Default (*)`

Lastly, we're going to edit the `Default (*)` behavior.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d1404011b4a312d88c7e523bbcf94316" alt="A CloudFront distribution with the &#x22;Default (*)&#x22; behavior selected and the Edit button emphasized." data-og-width="3024" width="3024" data-og-height="1406" height="1406" data-path="images/cloudfront/default-behavior-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a667557538a05b428b88de0860055fdc 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0ef97f41ff4722b83ada48dcfe4a6fb3 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=477ee3b3ff613ff0db18da30685a66e7 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0293e235eeaa0b07d06d5aa1b237154d 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e049af02765251c8dc70f75871ce8646 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=420d002f4dd0a5d33b6f3939ccba08f8 2500w" />
</Frame>

1. Change the default behavior's **Origin and origin groups** to the staging URL (in our case `mintlify-landing-page.vercel.app`).

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3c81d60889bc1157954524865a0bde14" alt="CloudFront &#x22;Edit behavior&#x22; page with the &#x22;Origin and origin groups&#x22; input field highlighted." data-og-width="3024" width="3024" data-og-height="1298" height="1298" data-path="images/cloudfront/default-behavior-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=978b2b690638bffc0b4d8a042c38496b 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=163f9ce0d805d64936d0ad3d0f1e95b8 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=79132725b4b9360f74098fb37d8aa39f 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8254ab4be3bb28a5a8eb6ac56cac4c04 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=2b75a3d1bd5e7f728e6fc98dec394abd 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=21d56c18cbd73f2e0939ac52805c9517 2500w" />
</Frame>

2. Select **Save changes**.

### Check behaviors are set up correctly

If you follow the above steps, your behaviors should look like this:

<Frame>
    <img src="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=666a7c785bcc7f6b2aa23424f8c1c668" alt="CloudFront &#x22;Behaviors&#x22; page with 4 behaviors: /docs/*, /docs, Default, and /.well-known/*." data-og-width="1603" width="1603" data-og-height="365" height="365" data-path="images/cloudfront/all-behaviors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=280&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=71017f7f8adb9707c30a4af5f18466c1 280w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=560&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b3d0b64d01d3d9405b3237ffe99e8b9f 560w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=840&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=97dd0acfd49dfd2f345f2fd3018e9db0 840w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1100&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b5f9cdf34197e6b4d86e36980d6a000f 1100w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1650&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=c4a30fd51baf478014221afc66c7ac2a 1650w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=2500&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b10b0389187a79b2367074200a34dc17 2500w" />
</Frame>

## Preview distribution

You can now test if your distribution is set up properly by going to the "General" tab and visiting the **Distribution domain name** URL.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b7f0582640bb6650054c7b40ee9bdd57" alt="CloudFront &#x22;General&#x22; tab with the &#x22;Distribution domain name&#x22; URL highlighted." data-og-width="3024" width="3024" data-og-height="1394" height="1394" data-path="images/cloudfront/preview-distribution.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=88578895d491f6405b39aa52d91123ec 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0c07a7178b43c2d4d2011fafc34bef59 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7ba052eb7683b44ebf829a0806ba0aa0 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9fe004b5b8c70190e09a51478b05b9f6 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c0e9bf74112262191fd0c053f3a42a74 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cf41b0e9aeedefab2e2f8dba02f43460 2500w" />
</Frame>

All pages should be directing to your main landing page, but if you append your chosen subpath, for example `/docs`, to the URL, you should see it going to your Mintlify documentation instance.

## Connect with Route53

Now, we're going to bring the functionality of the CloudFront distribution into your primary domain.

<Note>
  For this section, you can also refer to AWS's official guide on [Configuring
  Amazon Route 53 to route traffic to a CloudFront
  distribution](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html#routing-to-cloudfront-distribution-config)
</Note>

1. Navigate to [Route53](https://aws.amazon.com/route53) inside the AWS console.
2. Navigate to the "Hosted zone" for your primary domain.
3. Select **Create record**.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=27a00457e2401c2d55262291dda15579" alt="Route 53 &#x22;Records&#x22; page with the &#x22;Create record&#x22; button emphasized." data-og-width="1540" width="1540" data-og-height="1238" height="1238" data-path="images/cloudfront/route53-create-record.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a89b265f8944bd325f6422ae0532aa7b 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=71b98a1b9face10930f59047e6b06da8 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c05ef2f2a52142c2a5c5588ae458302c 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a3ff847c7cd962bff070660ac65e6cab 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7257b0f07303f69ad65e2af26ae20937 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=44902e21c0e9ed907d1ef95a81f98a8c 2500w" />
</Frame>

4. Toggle `Alias` and then **Route traffic to** the `Alias to CloudFront distribution` option.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=cb7dbe0320f3f73233ed6452ac3b0372" alt="Route 53 &#x22;Create record&#x22; page with the &#x22;Alias&#x22; toggle and the &#x22;Route traffic to&#x22; menu highlighted." data-og-width="3024" width="3024" data-og-height="1494" height="1494" data-path="images/cloudfront/create-record-alias.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7e6a7c98c6385b708c13a4ba97e7be28 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d3585515b33059d1c2796651fd4e3747 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e8d6264e546b432c60ee555c4d188cb3 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=4fc4e520251cf12caff27666ea2ccdc5 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=233ca4593b197c489cada291613333a3 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1561e423e0702a1cac1d3c4fbdd4dca9 2500w" />
</Frame>

5. Select **Create records**.

<Note>
  You may need to remove the existing A record if one currently exists.
</Note>

Your documentation is now live at your chosen subpath for your primary domain.

<Note>
  After configuring your DNS, custom subdomains are usually available within a few minutes. DNS propagation can sometimes take 1-4 hours, and in rare cases up to 48 hours. If your subdomain is not immediately available, please wait before troubleshooting.
</Note>

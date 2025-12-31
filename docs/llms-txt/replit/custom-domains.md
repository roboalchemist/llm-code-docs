# Source: https://docs.replit.com/cloud-services/deployments/custom-domains.md

# Custom Domains

> Use your domain name for your Replit published apps to showcase your app from a professional, branded web address.

Custom domains let you assign your domain name, such as `www.my-incredible-app.com` to your Replit published app.
While Replit provides a free subdomain in the format `<your-live-app-subdomain-name>.replit.app`, using
a custom domain lets you create a more memorable address.

A custom domain name can help brand recognition and trust with your app's users.

Watch the following video for a quick overview of setting up Custom Domains:

<Frame>
  <iframe src="https://www.youtube.com/embed/rGYdyb58wJY" title="Custom Domains with Publishing" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</Frame>

## Features

Custom Domains are available for the following Deployment types:

* [Autoscale](/cloud-services/deployments/autoscale-deployments/)
* [Reserved VM](/cloud-services/deployments/reserved-vm-deployments/)
* [Static](/cloud-services/deployments/static-deployments/)

The following table compares Replit's subdomains with custom domains:

| Feature                         | Replit Subdomain   | Custom Domain            |
| :------------------------------ | :----------------- | :----------------------- |
| Hostname customization          | Subdomain only     | Any domain that you own  |
| DNS update time                 | Instant            | Up to 48 hours           |
| Security Certificates (TLS/SSL) | Provided by Replit | Provided by Replit       |
| Price                           | Free               | Pay your domain provider |

## Usage

<Accordion title="How to access Custom Domains">
  1. After publishing your app, navigate to the <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=df3fa2573b451c54591523c9d9111db1" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/deploy-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=115e9383e0350a6ef201a41f78f8a19a 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=667b93ae66d0b69569409fb90d9fc280 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ae927e5aadcb7a470ad726f0acb0f782 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=16ee8f7b3d9db6b4f74ea8c2ebb6730f 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ad04a5984543c13895fd30182294ec0a 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=2449268bce371256727b17027eb180f3 2500w" /> **Deployments** tab.
  2. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/settings-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0a36e6a9a2078c02467d2abf0b8ba9e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3be97f139b63f478d536ccaa51518c9a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4eba230fefbe9836ffd37672275aa7d1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97e5099639faf4a5490d8e000c00149a 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4d9552209cee3306d2bc2a02e747ecb6 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d84a81284c0c9af295e0b86273d5c291 2500w" /> **Settings** tab.
  3. Select **Link a domain** or **Manually connect from another registrar** as shown in the following screenshot.

  <Frame>
    <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5dc58a0cab37877093e55c9a2b3b1367" alt="Settings tab" data-og-width="2422" width="2422" data-og-height="1130" height="1130" data-path="images/deployments/custom-domains/01.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=10f132a7d6791c3af72d31dc029cd93f 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=1dbe5628fda2b7b946042ee17e9f288f 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=7760f5013d03731317c10bf03d65496c 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5b2abbed7188c8ba42a7f87ab02133d2 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=cee6473a18de9d60f10947f6c0ae5afe 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/01.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=61f98d8d242b29b636b120b1fe8cb1f0 2500w" />
  </Frame>
</Accordion>

Follow the steps below to set up your custom domain:

<Warning>
  You might experience setup issues if you have one of the following: - Multiple
  `A` records for the same domain name that point to different servers. - `A`
  and `AAAA` records co-exist for the same domain since Replit only supports `A`
  records. - Cloudflare proxied domain records since Replit cannot automatically
  renew security certificates for that type.
</Warning>

<Steps>
  <Step title="Add your custom domain">
    Enter your custom domain name in the text field. You can use a registered domain or include a subdomain.

    For example, `hat-tip.cc` is the registered domain and `my.hat-tip.cc` includes subdomain `my`.

    <Frame>
      <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=38485a8680fe6ae256ec2d7b0665a784" alt="screenshot of the DNS settings" data-og-width="1940" width="1940" data-og-height="718" height="718" data-path="images/deployments/custom-domains/02.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=be47f14bdc89fe81c5becdcf3ab01325 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5a814a5e18c23d480e6c8673ff516980 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b76930fbcf7e2633878b04618f382540 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=7ba829c2d528f1c8ac44466a787a41ff 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=d35706627d73554723d15e43f905124f 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/02.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=d6b10b8b3b5be300bbfdfa326dd10031 2500w" />
    </Frame>
  </Step>

  <Step title="Add the DNS records to your domain registrar">
    Replit generates DNS records that you must provide to your **domain registrar**.
    A domain registrar is the service that manages your domain name, such as GoDaddy or Namecheap.

    Copy the `A` and `TXT` record values from Replit and paste them into your domain registrar's
    DNS management section. If your domain registrar does not support `@` as a hostname, use your registered domain name.
  </Step>

  <Step title="Optional: Add a subdomain">
    To add a subdomain to your published app, add a new `A` record with the same IP address
    in your provider's DNS management section.
    For example, if you want to add `my-subdomain.hat-tip.cc`, you must:

    * Copy the `A` and `TXT` record values from Replit to your registrar
    * Add a new `A` record with a hostname value of `my-subdomain` using the same IP address as your primary domain
  </Step>

  <Step title="Wait for DNS propagation to complete">
    After adding the records, you must wait for them to propagate online.
    This can take between a few minutes and 48 hours.

    When the propagation completes, your Domains tab should show the "Verified" status next to the domain name as shown below:

    <Frame>
      <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=fe5c99d84ff0334119d2e94b2f07c99a" alt="screenshot of the verified domain status" data-og-width="1866" width="1866" data-og-height="890" height="890" data-path="images/deployments/custom-domains/domain-verified.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=752f7faae26878667764b8a9551c16ed 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=9e581b4ad44577b7e93acbabc3da023e 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=275716ee7684a2b41831bff11d72d127 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5696d155898b7329963510e5ae966aec 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=72a3c969086037d2c28d3a2795ed6e22 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/custom-domains/domain-verified.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=3c3d0ad18418a3e6e2a20fe102b533e4 2500w" />
    </Frame>

    Load the domain in your browser to verify that it works.
  </Step>
</Steps>

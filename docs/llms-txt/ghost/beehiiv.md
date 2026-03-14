# Source: https://docs.ghost.org/migration/beehiiv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from BeeHiiv

> Migrate from BeeHiiv and import your content to Ghost with this guide

<Note>
  If you're a Ghost(Pro) customer, our team may be able to help you migrate your content and subscribers. Learn more about our [Concierge service](https://ghost.org/concierge/).
</Note>

## Exporting your subscribers

To get started, [download your full subscriber list](https://support.beehiiv.com/hc/en-us/articles/12234988536215-How-to-export-subscribers) (**Export Subscribers (Full)**) from BeeHiiv.

<Frame>
  <img src="https://mintcdn.com/ghost/ZMdvGdmwew7ypzvu/images/5830e1b4-beehiiv-subscriber-exports_huae1d966f695844077fd5c2e1914a81b1_25651_2148x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=ZMdvGdmwew7ypzvu&q=85&s=a1d79abf14c646779ef52793a5dc9c4e" width="2148" height="576" data-path="images/5830e1b4-beehiiv-subscriber-exports_huae1d966f695844077fd5c2e1914a81b1_25651_2148x0_resize_q100_h2_box_3.webp" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/ghost/KePyCzI5-bxtjueF/images/cbffd4f4-beehiiv-subscriber-download_huff7cd490bded2324dbd2f44e962cade4_16919_2148x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=KePyCzI5-bxtjueF&q=85&s=2ee3c63a68e22be7c63a7fac1b44f0d0" width="2148" height="602" data-path="images/cbffd4f4-beehiiv-subscriber-download_huff7cd490bded2324dbd2f44e962cade4_16919_2148x0_resize_q100_h2_box_3.webp" />
</Frame>

## Import subscribers to Ghost

If all of your subscribers are free, you can import this into Ghost directly.

<Frame>
  <img src="https://mintcdn.com/ghost/5_xpDDjqLTzEezAK/images/2f96f746-import-members-1_huc3d26abd3bec140dac4d1e5fd61f2b53_17353_1000x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=5_xpDDjqLTzEezAK&q=85&s=1f2f8d5b608e1dd8e7ac1b58960fc752" width="1000" height="167" data-path="images/2f96f746-import-members-1_huc3d26abd3bec140dac4d1e5fd61f2b53_17353_1000x0_resize_q100_h2_box_3.webp" />
</Frame>

If you have paid subscribers, you need to relate Stripe Customer IDs with your subscribers emails.

<Frame>
  <img src="https://mintcdn.com/ghost/5_xpDDjqLTzEezAK/images/19216f0e-import-members-2_hu4666f031efd860d74fa4f40b2a587fd0_130604_1000x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=5_xpDDjqLTzEezAK&q=85&s=6d35692e55955554d4cb0ec7505539d8" width="1000" height="1022" data-path="images/19216f0e-import-members-2_hu4666f031efd860d74fa4f40b2a587fd0_130604_1000x0_resize_q100_h2_box_3.webp" />
</Frame>

If you cannot connect your Ghost site to the same Stripe account you used with BeeHiiv, you may need to migrate customer data, products, prices, coupons to a new Stripe account, and then recreate the subscriptions before importing into your Ghost site. The [Ghost Concierge](https://ghost.org/concierge/) team can help with this.

## Migrating Content

Developers can migrate content from BeeHiiv to Ghost using our [migration CLI tools](https://github.com/TryGhost/migrate/tree/main/packages/mg-beehiiv).

You will first need to [export your posts](https://support.beehiiv.com/hc/en-us/articles/12258595483543-How-to-export-your-post-content) from BeeHiiv. This will be a CSV file which includes all post content, titles, dates, etc.

<Frame>
  <img src="https://mintcdn.com/ghost/5_xpDDjqLTzEezAK/images/0e894c9e-beehiiv-content-export_hu692b89da164ad0d3b6abc7f18ee87332_11063_2148x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=5_xpDDjqLTzEezAK&q=85&s=4e0a182891d2557c2d181ecc3f6679fe" width="2148" height="432" data-path="images/0e894c9e-beehiiv-content-export_hu692b89da164ad0d3b6abc7f18ee87332_11063_2148x0_resize_q100_h2_box_3.webp" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/ghost/5_xpDDjqLTzEezAK/images/1c0d9391-beehiiv-content-download_hu2bc2e7c63f879a9affdf18f111de440a_16136_2148x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=5_xpDDjqLTzEezAK&q=85&s=2694d106c8ab147cdd43e05e1ecb02d0" width="2148" height="602" data-path="images/1c0d9391-beehiiv-content-download_hu2bc2e7c63f879a9affdf18f111de440a_16136_2148x0_resize_q100_h2_box_3.webp" />
</Frame>

First, make sure the CLI is installed.

```sh  theme={"dark"}
# Install CLI
npm install --global @tryghost/migrate

# Verify it's installed
migrate
```

To run a basic migration with the default commands:

```sh  theme={"dark"}
# Basic migration
migrate beehiiv --posts /path/to/posts.csv --url https://example.com
```

There are [more options](https://github.com/TryGhost/migrate/tree/main/packages/mg-beehiiv#usage), such as the ability define a default author name and choose where `/subscribe` links go to.

Once the CLI task has finished, it creates a new ZIP file which you can [import into Ghost](https://ghost.org/help/imports/).

### Using custom domains

If you’re using a custom domain on BeeHiiv, you’ll need to implement redirects in Ghost to prevent broken links.

BeeHiiv uses `/p/` as part of the public post URL, where as Ghost uses it in the URL for post previews. This means the redirect regular expression is quite complex, but necessary so that post previews in Ghost function correctly.

```yaml  theme={"dark"}
# redirects.yaml
301:
  ^\/p\/(?![0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})(.*): /$1
  ^\/polls\/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}(.*): /
  ^\/t\/(.*): /tag/$1

302:
```

This means that if a visitor or crawler goes to `https://mysite.com/p/awesome-post`, they will automatically be redirected to `https://mysite.com/awesome-post`.

***

## Summary

Congratulations on your migration to Ghost 🙌. All that’s left to do is check over your content to ensure the migration has worked as expected. We also have a guide on [how to implement redirects](https://ghost.org/tutorials/implementing-redirects/) to make your transition smoother.


Built with [Mintlify](https://mintlify.com).
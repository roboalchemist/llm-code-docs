# Source: https://firebase.google.com/docs/test-lab/usage-quotas-pricing.md.txt

# Source: https://firebase.google.com/docs/hosting/usage-quotas-pricing.md.txt

<br />

The pricing forFirebase Hostingis based upon your project's usage of the following:

- [Hostingstorage](https://firebase.google.com/docs/hosting/usage-quotas-pricing#hosting-storage)(GB) --- The amount of storage space required to store the content of yourHostingsites (your static files and your configuration files).

- [Data transfer](https://firebase.google.com/docs/hosting/usage-quotas-pricing#hosting-data-transfer)(GB/month) --- The amount of data transferred to end users from our CDN. EveryHostingsite is automatically backed by our global CDN at no charge.

YourHostingquota is project-level, not site-level or channel-level. You can upgrade your project to the Blaze billing plan to unlock additional paid storage and data transfer levels. Learn more about[quotas and pricing forFirebase Hosting](https://firebase.google.com/pricing#hosting).

We recommend setting up[budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)for your project in theGoogle Cloudconsole.

Monitor both yourHostingstorage level and data transfer level in theFirebaseconsole:

- Visit the[*Usage*](https://console.firebase.google.com/project/_/hosting/usage)dashboard in the*Hosting* section of the console.  
  You can view the usage levels for different billing periods as well as for all yourHostingsites or for each site.

- Visit your project's[*Usage and billing*dashboard](https://console.firebase.google.com/project/_/usage)in the console.

| When your project is on the Blaze pricing plan,[**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)using the console. You can use the[Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator)to estimate your monthly costs.
|
| Be aware that**budget alerts do*not*cap your usage or charges** --- they are*alerts* about your costs so that you can take action, if needed. For example, you might consider[using budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

## UnderstandHostingstorage

When you deploy new content to your site, you create a "release" that points to a specific version of content and configuration for your site. The files associated with each release (both new releases and any retained previous releases) are stored by Firebase. These files make up your project'sHostingstorage usage level.

ThisHostingstorage is independent and unrelated to any other storage for your Firebase project (likeCloud Storage for Firebaseor database storage).

Note thatHostinghas a maximum size limit of 2 GB for individual files.

### Quota forHostingstorage

Storage for yourHostingcontent is at no cost up to 10 GB.

- If you are*not* on the Blaze plan, and you reach the 10 GB limit of no-costHostingstorage, you won't be able to deploy new content to your sites. You'll need to[delete older releases](https://firebase.google.com/docs/hosting/manage-hosting-resources#delete-release)or[upgrade to the Blaze plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

- If you are on the Blaze plan, and you reach the 10 GB limit of no-costHostingstorage, you'll be billed $0.026 for each additional GB ofHostingstorage.

### Control usage ofHostingstorage

To control yourHostingstorage usage, here are some things you can do:

- [Set a limit](https://firebase.google.com/docs/hosting/manage-hosting-resources#release-storage-settings)for the number of releases to keep.

- [Manually delete](https://firebase.google.com/docs/hosting/manage-hosting-resources#delete-release)specific releases.

- Store larger files using[Cloud Storage for Firebase](https://firebase.google.com/docs/storage), which offers a maximum size limit in the terabyte range for individual objects.

## UnderstandHostingdata transfer

WhenHostingserves one of your site's resources, data transfers from our CDN to your end user. The requested resource might already be available in our CDN cache (a cache hit) or it might need to come from theHostingbackend (a cache miss). If the requested content can be cached in the CDN, it will be. Both cache hits and misses count toward your project'sHostingdata transfer usage.

### Quota forHostingdata transfer

EveryHostingsite is automatically backed by our global CDN at no charge. Data transfer from the CDN to your end users is at no cost up to 10 GB/month.

- If you are*not* on the Blaze plan, and you reach the 10 GB/month limit of no-cost data transfer, we offer a short grace period but then your sites will be disabled. Your sites will remain disabled until the start of the next month because data transfer billing is based on*monthly* usage levels. You can reenable your sites immediately by[upgrading to the Blaze plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

- If you are on the Blaze plan, and you reach the 10 GB/month limit of no-cost data transfer, you'll be billed $0.15 for each additional GB of data transferred that month.

### Control usage ofHostingdata transfer

To control yourHostingdata transfer usage, here are some things you can do:

- Fine-tune the client-side caching of your content so that browsers don't need to request a resource from the CDN. Learn more about caching in the[web developer documentation](https://web.dev/http-cache/#cache-control).

- Avoid loading images and videos that you don't actually need to display.

- Create service workers to handle certain requests.  
  If you load Firebase SDKs via reservedHostingURLs, make sure to read important information about the[reserved namespace for these URLs](https://firebase.google.com/docs/hosting/reserved-urls#reserved_urls_and_service_workers).

  Here are some resources to help you set up service workers, especially with a PWA:
  - Codelab:[Caching files with the service worker](https://codelabs.developers.google.com/codelabs/pwa-caching-service-worker/index.html)

  - Documentation:[Service Worker Mindset](https://web.dev/service-worker-mindset/#powerful-but-limited)
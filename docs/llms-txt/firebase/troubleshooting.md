# Source: https://firebase.google.com/docs/test-lab/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/studio/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/perf-mon/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/crashlytics/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/app-distribution/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/app-hosting/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/crashlytics/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/app-distribution/troubleshooting.md.txt

# Source: https://firebase.google.com/docs/app-hosting/troubleshooting.md.txt

<br />

This page provides answers to frequently asked questions (FAQs) aboutApp Hosting.

## App HostingFAQ

#### DoesApp Hostingsupport frameworks other than Next.js and Angular?

App Hostingprovides preconfigured build and deploy support for Next.js and Angular, where we've committed to understanding those frameworks and interpreting their native configurations. For a number of[other frameworks](https://firebase.google.com/docs/app-hosting/about-app-hosting#other-frameworks), the developer community supportsApp Hostingframework adapters. Additionally, for any Node.js application with a build and start script,App Hostingwill attempt builds, but cannot dependably guarantee success. See[Framework integration](https://firebase.google.com/docs/app-hosting/about-app-hosting#frameworks).  

#### Which regions doesFirebase App Hostingsupport?

The regions forApp Hostingare likely to expand over time. See[App Hostinglocations](https://firebase.google.com/docs/app-hosting/about-app-hosting#locations)for the most up-to-date information.  

#### Can I use GitLab or other Git providers besides GitHub for deployments?

Currently you can't, but support for other providers is in the long term roadmap forApp Hosting.  

#### Why can't I find my repository in the Firebase console UI?

If your repository does not appear in the list of options when you are creating a new backend in the Firebase console, first try selecting**Refresh list** . If the preferred repository is still not available, you may need to add it using the option to**Grant access to a new repository in GitHub**.

Additionally, you can manage repositories with theFirebase App HostingGitHub application. To do this, go to your GitHub profile, and select**Settings** and then**Applications** . In the table row for theFirebase App Hostingapplication, click**Configure**to manage repositories.  

#### Why won't my site display normally in Android mobile app WebView?

Apps that configured a custom domain with the Firebase console prior to Q3 2025 may find that the site does not display properly in Android WebView. This occurs because CNAME records used during that period were not compatible with Android WebView.

To resolve this issue, remove the custom domain from theApp Hostingbackend and re-add it. The updated console UI will provide 3 new records, an A and a TXT record for the domain, and a CNAME for the ACME challenge subdomain (for certs); use these records in place of the previous CNAME record.  

#### How do I change the repository associated with myApp Hostingproject?

Currently, changing the repository isn't possible. However, you can create a new backend associated with the preferred repository within the same project, or create a new backend in a separate project.  

#### How can I set headers for myApp Hostingsite?

Headers are framework-dependent. Do whatever you would normally do for your framework.  

#### Is there an emulator for local development withApp Hosting?

Yes, you can perform local tests of your app prior toApp Hostingdeployment using theApp Hostingemulator, which is part of the Firebase Local Emulator Suite. See[Locally test your app deployment](https://firebase.google.com/docs/app-hosting/emulate).  

#### Why do I see errors inApp Hostingbut not in Cloud Build?

In such cases, it's possible that your error may have come from Cloud Run. Check the status of the rollout to be sure.  

#### How do I change or remove a linked GitHub account?

To remove the linked GitHub account, open[Developer Connect](https://console.cloud.google.com/developer-connect/connections), ensure your project is selected, and delete the`firebase-app-hosting-github-oath`connection and the connection that starts with`apphosting-github-conn-`. When you openApp Hostingin theFirebaseconsole, you should now be able to set up a new GitHub connection.  

#### How can I set cookies for myApp Hostingsite?

Though it was not available at the launch of theApp Hostingpreview, the`Set-Cookie`HTTP response header now works as expected.

## GeneralApp Hostinglimitations and troubleshooting

- App Hosting's CDN can only include a specific set of request headers in its cache keys. That list includes NextJS's`RSC`,`Next-Router-State-Tree`,`Next-Router-Prefetch`,`Next-Router-Segment-Prefetch`, and`Next-Url`headers, as well as Cloud CDN's standard`Accept`,`Accept-Encoding`,`Access-Control-Request-Headers`,`Access-Control-Request-Method`,`Origin`,`Sec-Fetch-Dest`,`Sec-Fetch-Mode`,`Sec-Fetch-Site`,`X-Goog-Allowed-Resources`, and`X-Origin`. If a response contains a`Vary`header with a value not listed here, our CDN won't cache it.
- Uncached static files are served out ofCloud Run; in a later release, they'll be stored and served from theApp Hostingorigin for better performance.
- TheFirebaseconsole may intermittently show a "build was not found and is invalid" error on backend creation.
- All backends in the same project share a GitHub org/account. They can be connected to different repositories under that org/account. To create backends that are connected to different GitHub accounts, put them in separate projects.

## Angular app limitations and troubleshooting

ThoughApp Hostingsupport for Angular is actively in development and expanding, it has the following limitations:

- **I18n**: While core I18n functionality works, direct navigation to SSR pages can result in errors.
- **Localization**: Building versions for different locales isn't supported.
- **Builders**: Only the Application builder is currently supported.
- **Environments and Monorepo Tooling**: Angular projects that have more than a single application target will fail. For more complete monorepo support, use Nx.

## Next.js limitations and troubleshooting

- By default, the[built-in NextJS image optimization](https://nextjs.org/.docs/app/building-your-application/optimizing/images)is disabled on App Hosting unless you explicitly set[`images.unoptimized`](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized)to false or use a custom[Image Loader.](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#example-loader-configuration)See[Optimize image loading on Next.js](https://firebase.google.com/docs/app-hosting/optimize-image-loading).
- URL paths containing percent-encoded characters are decoded byCloud Run. This may cause issues with features that expect only encoded URL paths, such as Next.js parallel routing.
- Currently,App Hostinglimits the caching for NextJS apps using[middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware). Over time, cache hit rates should improve.
- URL paths containing percent-encoded characters are decoded by Cloud Run. This may cause issues with features that expect only encoded URL paths, such as[Next.js parallel routing](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes)
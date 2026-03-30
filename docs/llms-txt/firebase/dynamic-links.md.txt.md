# Source: https://firebase.google.com/docs/dynamic-links.md.txt

# Firebase Dynamic Links

# Firebase Dynamic Links


Firebase Dynamic Links are links that work the way you want, on multiple
platforms, and whether or not your app is already installed.
[Video](https://www.youtube.com/watch?v=LvY1JMcrPF8)

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

With Dynamic Links, your users get the best available experience for the
platform they open your link on. If a user opens a Dynamic Link on iOS or Android,
they can be taken directly to the linked content in your native app. If a user
opens the same Dynamic Link in a desktop browser, they can be taken to the equivalent
content on your website.

In addition, Dynamic Links work across app installs: if a user opens a Dynamic Link on
iOS or Android and doesn't have your app installed, the user can be prompted to
install it; then, after installation, your app starts and can access the link.

## How does it work?

You create a Dynamic Link either by using the Firebase console, using a REST
API, iOS or Android Builder API, or by forming a URL by adding Dynamic Link parameters to a domain
specific to your app. These parameters specify the links you want to open, depending on the
user's platform and whether your app is installed.

When a user opens one of your Dynamic Links, if your app isn't yet installed, the
user is sent to the Play Store or App Store to install your app (unless you
specify otherwise), and your app opens. You can then retrieve the link that
was passed to your app and handle the deep link as appropriate for your app.

## Custom link domains

You can [create Dynamic Links using
your own domain name](https://firebase.google.com/docs/dynamic-links/custom-domains):

```
https://example.com/summer-sale
https://example.com/links/promos/summer-sale
https://links.example.com/summer-sale
https://ex.amp.le/summer-sale
```

Or, if you don't have a domain for your app, you can use a no-cost custom
page.link subdomain:

```
https://example.page.link/summer-sale
```

Create your subdomain at no charge in the Firebase console.

All Dynamic Links features, including analytics, post-install attributions, and
SDK integrations, work with both custom page.link domains and your own
domain.

## Implementation path

|---|---|---|
|   | **Set up Firebase and the Dynamic Links SDK** | Enable Firebase Dynamic Links for your Firebase project in the Firebase console. Then, include the Dynamic Links SDK in your app. |
|   | **Create Dynamic Links** | You can create Dynamic Links programmatically or by using the Firebase console. |
|   | **Handle Dynamic Links in your app** | When your app opens, use the Dynamic Links SDK to check if a Dynamic Link was passed to it. If so, get the deep link from the Dynamic Link data and handle the deep link as necessary. |
|   | **View analytics data** | Track the performance of your Dynamic Links in the Firebase console. |

## Next steps

- Learn about some of Firebase Dynamic Links' most common [use cases](https://firebase.google.com/docs/dynamic-links/use-cases) and how to implement them.
- Learn how to [create
  Dynamic Links](https://firebase.google.com/docs/dynamic-links/create-links) and then receive them in your [iOS](https://firebase.google.com/docs/dynamic-links/ios/receive), [Android](https://firebase.google.com/docs/dynamic-links/android/receive), [Flutter](https://firebase.google.com/docs/dynamic-links/flutter/receive), [Unity](https://firebase.google.com/docs/dynamic-links/unity/receive), and [C++](https://firebase.google.com/docs/dynamic-links/cpp/receive) apps.
- Use your own [custom
  domain](https://firebase.google.com/docs/dynamic-links/custom-domains) for Dynamic Links.
- Understand your Dynamic Links's performance with two [analytics](https://firebase.google.com/docs/dynamic-links/analytics) tools.
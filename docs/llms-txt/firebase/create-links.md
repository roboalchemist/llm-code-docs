# Source: https://firebase.google.com/docs/dynamic-links/create-links.md.txt

<br />

| **Note:** Firebase Dynamic Links is*deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the[migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service)and see the[Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq)for more information.

There are four ways you can create aDynamic Link:

- Using the[Firebaseconsole](https://console.firebase.google.com/project/_/durablelinks/links/). This is useful if you're creating promo links to share on social media. This way you can select a custom suffix and a name for the link in the[Firebaseconsole](https://console.firebase.google.com/project/_/durablelinks/links/). You can track the performance of theseDynamic Linksin the[Firebaseconsole](https://console.firebase.google.com/project/_/durablelinks/links/)or via the[Analytics REST API](https://firebase.google.com/docs/reference/dynamic-links/analytics).
- Using theDynamic LinkBuilder API on[iOS](https://firebase.google.com/docs/dynamic-links/ios/create),[Android](https://firebase.google.com/docs/dynamic-links/android/create), and[Flutter](https://firebase.google.com/docs/dynamic-links/flutter/create). This is the preferred way to dynamically create links in your app for user-to-user sharing or in any situation that requires many links. You can track the performance ofDynamic Linkscreated with the Builder API using theDynamic Links[Analytics API](https://firebase.google.com/docs/reference/dynamic-links/analytics).
- Using the[REST API](https://firebase.google.com/docs/dynamic-links/rest). This is the preferred way to dynamically create links on platforms that don't have a Builder API. The[Analytics REST API](https://firebase.google.com/docs/reference/dynamic-links/analytics)can be used to track the performance of promo campaigns created in the console.
- [Manually](https://firebase.google.com/docs/dynamic-links/create-manually). If you don't need to track click data and you don't care if the links are long, you can manually constructDynamic Linksusing URL parameters, and by doing so, avoid an extra network round trip.

#### Next steps

After you createDynamic Links, you need to set up your app to receiveDynamic Linksand send users to the right place in your app after a user opens them.

To receiveDynamic Linksin your app, see the documentation for[iOS](https://firebase.google.com/docs/dynamic-links/ios/receive),[Android](https://firebase.google.com/docs/dynamic-links/android/receive),[Flutter](https://firebase.google.com/docs/dynamic-links/flutter/receive),[C++](https://firebase.google.com/docs/dynamic-links/cpp/receive), and[Unity](https://firebase.google.com/docs/dynamic-links/unity/receive).
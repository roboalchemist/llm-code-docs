# Source: https://firebase.google.com/docs/dynamic-links/link-previews.md.txt

<br />

| **Note:** Firebase Dynamic Links is*deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the[migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service)and see the[Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq)for more information.

You can improve the way apps and sites display yourDynamic Linksby specifying social metadata when you[create yourDynamic Links](https://firebase.google.com/docs/dynamic-links/create-links). This metadata is passed on to supported services in the form of social meta tags, which the services use to generate a rich presentation of the link.

For example, social apps can use the metadata to present sharedDynamic Linksas cards with a title, a description of the linked content, and a preview image.

Also, the app preview page that is displayed when you open aDynamic Linkon iOS will use the metadata, if provided, to display a preview of the link's content.

## Social sharing previews

Social apps can use the data specified by social metadata to generate rich previews of sharedDynamic Links. For example:

![](https://firebase.google.com/static/docs/dynamic-links/images/social-share.png)

The above example is a preview of aDynamic Linkwith the following metadata specified:

- Title (`st`): Reticulated Giraffes

- Description (`sd`): The reticulated giraffe, also known as the Somali giraffe, is a subspecies of giraffe native to the Horn of Africa.

- Image (`si`): (URL to image)

  The image should be at least 300x200 px, and less than 300 KB.

Social metadata is passed to Twitter, Facebook, Facebook Messenger, iMessage, WhatsApp, Google+, and other services.

## App preview pages

When a user opens aDynamic Linkon iOS, they will see an app preview page that shows them which app will be used to open the link. The app preview page more reliably sends users to the most appropriate destination (such as your app) by minimizing unnecessary system dialogs and enabling users to navigate out of in-app browsers. As a result, the app preview page increases the click-to-install rate of yourDynamic Links.

The app preview page also enablesDynamic Linksto be received as unique matches on iOS. When a user selects**Save my place in the app** and then clicks**Open** , theDynamic Linkis copied to the iOS clipboard; then, when your app opens, theDynamic LinksSDK an receive the link with 100% confidence that the app's current user is the user who clicked the link.

If you don't specify social metadata in yourDynamic Link, the app preview page displays your app's name, icon, and description, based on your app's information in the App Store. For example:

![](https://firebase.google.com/static/docs/dynamic-links/images/app-preview-plain.png)

When you provide social metadata in yourDynamic Link, the app preview page displays the title, description, and image you specified instead, as well as your app's name and icon. For example:

![](https://firebase.google.com/static/docs/dynamic-links/images/app-preview-metadata.png)

You can bypass the app preview page by specifying the dynamic link parameter`efr=1`. Note that without the app preview page,Dynamic Linkscannot be received as unique matches on iOS.
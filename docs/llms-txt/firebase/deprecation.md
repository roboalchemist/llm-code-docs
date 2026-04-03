# Source: https://firebase.google.com/docs/invites/deprecation.md.txt

<br />

| Firebase Invites is deprecated. On**January 24th, 2020** , we will discontinue support for Firebase Invites. You will be able to use[Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links)with a custom sharing solution.

Firebase Invitesprovided both a mechanism for receiving[Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links)in your app, as well as a feature to share that link via SMS or email. We developedFirebase Invitesto help you grow your app users through word of mouth, but over time, we learned that you found better ways to encourage users to share their favorite apps with their friends, beyond whatFirebase Invitesdoes today.

We also saw that while usage ofFirebase Invitesdropped, many of you were still usingFirebase Dynamic Linksas the key ingredient of your user-to-user sharing solution. So, we're strengthening our focus and increasing our effort to makeFirebase Dynamic Linksthe best way to build user-to-user sharing capabilities into your app. As part of this shift, we have deprecated theFirebase Invitesfeature, and will discontinue support starting on**January 24th, 2020**.

### What does this mean and how does it impact me?

Starting on January 24th, 2020, your users will no longer be able to send or receiveFirebase Invites, and the invites backend service will start returning error responses when making calls to send and receive an invite link. The current SDKs include error handling to help ensure graceful failure cases for these server responses, so your users will be able to continue using your app without crashing, but we recommend that you no longer useFirebase Invites, and switch to an alternative solution usingFirebase Dynamic Linkswith a custom sharing solution.

Here is how to do that!

## Create invitation links withFirebase Dynamic Links

First,[Create aDynamic Link](https://firebase.google.com/docs/dynamic-links/create-links)that your users can share with their friends. The good news is that you're likely familiar with this step already because it's similar to how you set upFirebase Invites. But you can also add specific parameters to your Dynamic Link, such as[adding social metadata to your links](https://firebase.google.com/docs/dynamic-links/link-previews)if your users share your app via a social network to customize the appearance of the URL that gets shared.

## Build a sharing solution

Next, build your sharing solution for your users to be able to share that link with their friends. What you will want to build here will vary depending on how you want to provide the sharing feature that will replace the previous one inFirebase Invites, but for most mobile apps you can take advantage of features already built into the platform.

For Android, one simple solution that covers both SMS and email sharing, as well as other popular social network and messaging apps, is to use a generic intent with an action set as`Intent.ACTION_SEND`. This provides a convenient way to share data from your app to any app the user has installed that can handle a share intent.

Something similar to the following example should work here (recommending that you use constant string resources in your own code):  

```css+lasso
Intent sendIntent = new Intent();
sendIntent.setAction(Intent.ACTION_SEND);
sendIntent.putExtra(Intent.EXTRA_TEXT, "Here's a new lesson for" +
        " learning more Miwok vocabulary:\n\n" + dynamicLink);
sendIntent.putExtra(Intent.EXTRA_SUBJECT, "Let's Learn Miwok!");
sendIntent.setType("text/plain");
startActivity(Intent.createChooser(sendIntent,
        getResources().getText(R.string.send_to)));
```

For a fuller example and more details, check out this guide for[sending simple data to other apps](https://developer.android.com/training/sharing/send).

The code snippet above will generate something like invitation flow shown in the screens below:

![Sharing on Android](https://firebase.google.com/static/docs/invites/images/android-share.png)

For iOS developers, you can use a`UIActivityViewController`, passing in the link created as part of the data to the custom VC. This method would provide a sharing flow similar to the screens below:

![Sharing on iOS](https://firebase.google.com/static/docs/invites/images/ios-share.png)

## Receive aDynamic Linkin your app

Finally, the last step to provide user-to-user sharing for your app after the sunset is in receiving aDynamic Linkin your app.

For Android, this process remains the same so you won't need to change much here. The only difference is that withoutFirebase Invites, there will no longer be an invitation ID, and so you would need to remove the call to extract the invite ID via`FirebaseAppInvite invite = FirebaseAppInvite.getInvitation(data)`, if your app is making that call. For more details on this piece, please see the guide on[Receiving Dynamic Links in your Android app](https://firebase.google.com/docs/dynamic-links/android/receive).

For iOS, this would require changing from the[FIRReceivedInvite](https://firebase.google.com/docs/reference/ios/firebaseinvites/api/reference/Classes/FIRReceivedInvite)object to the[FIRDynamicLink](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink)object, which both contain similar data. Please see the guide on[Receiving Dynamic Links in your iOS app](https://firebase.google.com/docs/dynamic-links/ios/receive)for more details.

For Unity developers, there are a number of open-source libraries and equivalent solutions as those described above to migrate your user-to-user sharing functionality. If you need any assistance on providing a suitable solution, please reach out to the support resources linked further below.

Firebase Inviteshas been a great tool that we're proud to have built. As we look towards the future, we're excited to double down on makingFirebase Dynamic Linkseven better so you have more flexibility and control over how you encourage users to invite others to your app. If you have any questions about setting up yourFirebase Dynamic Linksand custom sharing solutions, please reach out on[StackOverflow](https://stackoverflow.com/questions/tagged/firebase-dynamic-links), or any of our[additional support forums](https://firebase.google.com/support/).
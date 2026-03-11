# Source: https://docs.buildnatively.com/natively-platform/features/photo-library.md

# Photo Library

This feature enables broad, persistent access to the user's entire Photo Library on their device.

When to Enable (Broad Access):

* Enable this feature only if your app has a core function that requires broad, continuous access to the entire photo collection (e.g., photo editors, gallery management apps).

When to Disable (Limited Access):

* If your app only requires one-time or limited access to a single photo or video (e.g., for uploading a profile photo or attaching an image to a message), you should disable this feature.
* For limited access, you must use the system picker (which is accessed via your website's standard file uploader input). This fulfills the requirement without needing broad permissions, ensuring compliance with Google and Apple security policies.

Sometimes Apple may reject your app and require a more detailed explanation on how to use photo library.

* **Permission description** - The permission description text should explain to the user why your app needs that permission. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)to avoid potential **rejection**.

### Rejection example:

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FhNLjcMZ81S0sQDUAUfwg%2Fimage.png?alt=media&#x26;token=968272d9-f2ee-4d90-a524-1ce5f61746e1" alt=""><figcaption></figcaption></figure>

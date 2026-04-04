# Source: https://docs.buildnatively.com/natively-platform/app-info/android-build.md

# Android App

## Bundle Identifier

{% hint style="warning" %}
The Bundle Identifier is a unique identifier for your app. Once set, it can only be changed if your app or developer account is suspended. Please find more details in our [FAQ](https://docs.buildnatively.com/getting-started/faq#how-do-i-change-my-app-ios-or-android-bundle-id-bundle-identifier)
{% endhint %}

### Generate Bundle ID

Natively will automatically generate a bundle identifier for your app, otherwise, you can create your own.

### Create Own Bundle ID

A bundle ID, otherwise, known as a **package name** in Android, is the unique identifier for all Android apps. Choose it carefully - once set, it is permanent.

Android uses a Reverse-DNS naming convention. This ensures that your app is unique by basing the ID on a domain name you control.

* Format: `com.companyname.appname`
* Hierarchy: It starts with the top-level domain (`com`, `io`, `net`), followed by your brand/organization name, and finally the specific app name.

To pass the Google Play Console validation and our native build engine, your Package Name must adhere to these strict rules:

* Format: Must follow the Reverse-DNS convention (e.g., `com.yourcompany.appname`).
* Segments: It must contain at least two segments (one or more periods).
* Characters: Only alphanumeric characters (A-Z, a-z, 0-9), underscores (\_), and periods (.) are allowed.
* Starting Characters: Each segment must start with a letter, not a number.
* No Hyphens: Android Package Names cannot contain hyphens (`-`).
* No Java Keywords: Avoid using reserved Java keywords like `abstract, assert, boolean, break, byte, case, catch, char, class, const, continue, default, do, double, else, enum, extends, final, finally, float, for, goto, if, implements, import, instanceof, int, interface, long, native, new, package, private, protected, public, return, short, static, strictfp, super, switch, synchronized, this, throw, throws, transient, try, void, volatile, while`.
* No Spaces.
* Uniqueness: Your Package Name must be unique across the entire Google Play Store. If another developer has used `com.myapp.test`, you will not be able to upload your build.

The most direct way to check uniqueness is to manually construct the URL that Google Play uses for every app.

The Formula: `https://play.google.com/store/apps/details?id=YOUR_PACKAGE_NAME`

How to Read the Results:

* Not Found: This is actually a good sign! It means no public app is currently using that ID. It is likely available for your app.
* An App Page Appears: The ID is taken. You must choose a different Package Name (even if the app you see is old or unrelated).

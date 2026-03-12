# Source: https://developers.make.com/custom-apps-documentation/app-components/iml-functions/handling-of-full-update-approach-in-update-modules.md

# Handling of PUT requests in action modules

Some APIs use full updates instead of partial updates. This is usually seen when the endpoint uses the `PUT` method instead of `PATCH`.

While `PATCH` allows you to provide just a few values and it will update only those, `PUT` generally requires you to send the entire object being updated. If you don't provide all values, missing fields may become empty or be changed to the default values.

For more information, see the best practices on [updating modules with the PUT request](https://developers.make.com/custom-apps-documentation/best-practices/modules/batch-actions#put-vs-patch-behavior-in-update-modules).

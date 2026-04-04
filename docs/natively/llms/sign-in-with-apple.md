# Source: https://docs.buildnatively.com/natively-platform/features/social_auth/sign-in-with-apple.md

# Sign In with Apple

### What is Sign In with Apple?

The Sign In with Apple feature empowers Natively to seamlessly integrate Apple's own authentication system within the application, enhancing user trust and convenience. To align with Apple's stringent privacy and security policies, which are designed to protect users from potential phishing and fraudulent activities, Natively channels users directly through the secure and native authentication flow provided by Apple.

### How to set up Sign In with Apple?

1. Go to the Natively app dashboard.
2. Navigate to Features -> Social Auth
3. Turn on the **Sign In with Apple** feature
4. Open the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) (left menu)
5. Click on the [Identifiers](https://developer.apple.com/account/resources/identifiers/list)
6. Select the previously [created Bundle Identifier](https://docs.buildnatively.com/natively-platform/features/social_auth/broken-reference)
7. Scroll down and enable **Sign In with Apple**
8. Click **Save & Confirm**
9. Rebuild your app
10. Test

### How to use it?

{% content-ref url="../../../guides/integration/apple-sign-in" %}
[apple-sign-in](https://docs.buildnatively.com/guides/integration/apple-sign-in)
{% endcontent-ref %}

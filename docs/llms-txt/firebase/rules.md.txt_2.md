# Source: https://firebase.google.com/docs/rules.md.txt

# Firebase Security Rules

# Firebase Security Rules

Use our flexible, extensible Firebase Security Rules to
secure your data in Cloud Firestore, Firebase Realtime Database, and
Cloud Storage.

> [!NOTE]
> **Note:** Many AI assistants, such as [Gemini CLI](https://cloud.google.com/gemini/docs/codeassist/gemini-cli), can help generate Firebase Security Rules for Cloud Firestore and Cloud Storage for Firebase. For a detailed, pre-written prompt you can use with your AI assistant, refer to [AI Prompt: Write Firebase Security Rules](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules).

Firebase Security Rules stand between your data and malicious users. You can write simple or
complex rules that protect your app's data to the level of granularity that
your specific app requires.

Firebase Security Rules leverage
extensible, flexible configuration languages to define what data your users
can access for Realtime Database, Cloud Firestore, and Cloud Storage.
Firebase Realtime Database Security Rules leverage JSON in rule definitions, while
Cloud Firestore Security Rules and Firebase Security Rules for Cloud Storage leverage a unique
language built to accommodate more complex rules-specific structures.

Learn more about how to set up Security Rules for the specific Firebase products
you use in your app, and how Security Rules behavior differs across Firebase
products.

[Get started](https://firebase.google.com/docs/rules/get-started)

## Key capabilities

|---|---|
| Flexibility | Write custom rules that make sense for your app's structure and behavior. Security Rules use languages that allow you to leverage your own data to authorize access. |
| Granularity | Your rules can be as broad or as narrow as you need. |
| Independent security | Because Security Rules are defined outside of your app (in the Firebase console or Firebase CLI), clients aren't responsible for enforcing security, bugs don't compromise data, and your data is always protected. |

## How do they work?

Firebase Security Rules work by matching a pattern against database paths, and then applying
custom conditions to allow access to data at those paths. All Security Rules
across Firebase products have a path-matching component and a conditional
statement allowing read or write access. You must define Security Rules for
each Firebase product you use in your app.

For Cloud Firestore and Cloud Storage, Security Rules use the following
syntax:

    service <<name>> {
      // Match the resource path.
      match <<path>> {
        // Allow the request if the following conditions are true.
        allow <<methods>> : if <<condition>>
      }
    }

For Realtime Database, JSON-based Security Rules use the following syntax:

    {
      "rules": {
        "<<path>>": {
        // Allow the request if the condition for each method is true.
          ".read": <<condition>>,
          ".write": <<condition>>
        }
      }
    }

Security Rules are applied as `OR` statements, not `AND` statements.
Consequently, if multiple rules match a path, and any of the matched
conditions grants access, Security Rules grant access to the data at that
path. Therefore, if a broad rule grants access to data, you can't restrict with
a more specific rule. You can, however, avoid this problem by making sure your
Security Rules don't overlap too much. Firebase Security Rules flag overlaps in your
matched paths as compiler warnings.

Firebase Security Rules can also leverage Authentication to grant user-based permissions, and the
conditions you set can be very basic or incredibly complex. Learn more
about Security Rules [language](https://firebase.google.com/docs/rules/rules-language) and [behavior](https://firebase.google.com/docs/rules/rules-behavior)
before you start writing Security Rules.

## Implementation path

|---|---|---|
|   | Integrate the product SDKs | Set up [Cloud Firestore](https://firebase.google.com/docs/firestore), [Cloud Storage](https://firebase.google.com/docs/storage), or [Realtime Database](https://firebase.google.com/docs/database) for your app. |
|   | Write your Firebase Security Rules | Learn more about [how Security Rules work](https://firebase.google.com/docs/rules/rules-behavior) and [set up some basic Security Rules](https://firebase.google.com/docs/rules/basics) |
|   | Test your Firebase Security Rules | Use the Realtime Database and Cloud Firestore emulators to test your app's behavior and validate your rules before you deploy them to production. |
|   | Deploy your Firebase Security Rules | Use the Firebase console or the Firebase CLI to deploy your rules to production. |

## Next steps

- [Understand the Firebase Security Rules language](https://firebase.google.com/docs/rules/rules-language).
- Learn more about [how Firebase Security Rules work](https://firebase.google.com/docs/rules/rules-behavior).
- Explore the [common mistakes you should avoid](https://firebase.google.com/docs/rules/insecure-rules).
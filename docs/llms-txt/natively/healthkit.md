# Source: https://docs.buildnatively.com/guides/integration/healthkit.md

# Source: https://docs.buildnatively.com/natively-platform/features/healthkit.md

# HealthKit

{% hint style="danger" %}
HealthKit is an Apple Framework that is available only on iPhones. No iPads or Android devices.
{% endhint %}

### How to set up HealthKit?

1. **Enable HealthKit for your Bundle ID on** [**https://developer.apple.com**](https://developer.apple.com)

   \
   a) Go to [Bundle IDs page](https://developer.apple.com/account/resources/identifiers/bundleId)

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FQF75RUQiKpKmbrxCsxt3%2Fimage.png?alt=media&#x26;token=8773f809-24dc-4c3b-a005-a2b4f418ade3" alt=""><figcaption></figcaption></figure>

   \
   b) Find your Bundle ID in a list and click on it

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FWxPaxqgEIzYVvY1WdAph%2Fimage.png?alt=media&#x26;token=21046c8d-7c3c-4747-bb47-cd70bea498c1" alt=""><figcaption></figcaption></figure>

   \
   c) Scroll down, enable HealthKit, and click Save

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FEdvIYw1C8dDT77w1vG2E%2Fimage.png?alt=media&#x26;token=13f2f455-f999-4aac-822d-d18978912478" alt=""><figcaption></figcaption></figure>

   <br>
2. **Enable HealthKit in Natively**

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FmuXyaXicZj75HJ7iBxrG%2Fimage.png?alt=media&#x26;token=66d6a3af-2e05-42c7-a395-6d45798babb3" alt=""><figcaption></figcaption></figure>

   Turn on the HealthKit feature and fill out the following information:

   * **Read permission description** - A message to the user that explains why the app requested permission to read samples from the HealthKit store. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)to avoid potential **rejection**.
   * **Write permission description** - A message to the user that explains why the app requested permission to save samples to the HealthKit store. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)to avoid potential **rejection**.

{% hint style="warning" %}
For now, Natively **supports only reading data** from HealthKit (We plan to add writing soon). But **Apple requires** apps that only read data to provide **both Read/Write permission text**. You can **use Read text for both Read & Write**.
{% endhint %}

3. **Go to Natively and rebuild your app**

### How to use HealthKit?

{% content-ref url="../../guides/integration/healthkit" %}
[healthkit](https://docs.buildnatively.com/guides/integration/healthkit)
{% endcontent-ref %}

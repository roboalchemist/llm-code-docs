# Source: https://docs.buildnatively.com/guides/integration/nfc.md

# Source: https://docs.buildnatively.com/natively-platform/features/nfc.md

# NFC

### How to set up NFC?

### For iOS

1. **Go to** the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) \*\*\*\* (left menu)
2. Click on the [Identifiers](https://developer.apple.com/account/resources/identifiers/list)
3. Select previously [created Bundle Identifier](https://docs.buildnatively.com/natively-platform/features/broken-reference)
4. Scroll down and enable **NFC Tag Reading**
5. Click **Save & Confirm**
6. On Natively app dashboard, turn on the **NFC** feature and fill out the **Permission description** - The permission description text should explain to the user why your app needs that permission. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)to avoid potential **rejection**.
7. Rebuild your app

### For Android

1. On Natively app dashboard, turn on the **NFC** feature
2. Rebuild your app

{% hint style="warning" %}
For now, Natively supports only NTAG213,215,216 (MiFare Ultralight). All other cards/tags haven't been tested yet.
{% endhint %}

### How to use NFC?

{% content-ref url="../../guides/integration/nfc" %}
[nfc](https://docs.buildnatively.com/guides/integration/nfc)
{% endcontent-ref %}

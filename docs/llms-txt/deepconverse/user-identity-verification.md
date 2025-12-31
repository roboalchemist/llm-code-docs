# Source: https://docs.deepconverse.com/product-docs/chatbots/advanced-functionality/user-identity-verification.md

# User Identity Verification

Identity verification allows the chatbot to verify that your users are not being impersonated. It ensures that conversations are private and all user metadata is verified before being put to use.&#x20;

### How does Identity Verification work?

Identity verification makes use of a shared secret that is known to the chatbot and your server. Using this shared secret we generate a hash of the user metadata json. When the chatbot is started this user hash is verified with the shared secret and if the hash matches our computed hash we add the user metadata into the chatbot flow context.

After verification the user metadata is available to use throughout the flow.

### How to use Identity Verification in the flow?

To use identity verification there are two components:

* Identity Verification in Conversation Flow
* Identity Hash Generation&#x20;

#### Identity Verification in Conversation Flow

* Get started by going to your greet flow and adding the Identity Verification module. \ <br>

  <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FntDIGx0uFfMdgZkai45T%2Fimage.png?alt=media&#x26;token=ceff785a-5a0f-45bf-a897-19b357c814b3" alt=""><figcaption></figcaption></figure>
* In the Identity Verification module settings set the shared secret value. (This shared secret is what you will be using on your server for hash generation)\ <br>

  <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2F8Ou8jxPRE9QQaQngPvi8%2Fimage.png?alt=media&#x26;token=815feae2-457f-4fb8-9f6e-730962e23808" alt=""><figcaption></figcaption></figure>
* The identity verification module will use the shared secret and generate the hash of the incoming data and compare that with the hash that you provide.
* *If the values match the user metadata will become available in the flow context*.

#### Identity Hash Generation

* To use identity verification you will need to pass in browser\_userHash variable when you invoke the chatbot.
* Identity Verification works by using a server side generated [HMAC (hash based message authentication code)](http://en.wikipedia.org/wiki/Hash-based_message_authentication_code), using SHA256, on either the user’s *metadata.*
* *Note: Metadata keys should be sorted when generating the HMAC*
* Here is an example of how to invoke the chatbot with the metadata.

<pre><code><strong>document.dispatchEvent(new CustomEvent("botWidgetInit", {"detail": {
</strong><strong>  'browser_userHash': '7a0d22dc447aea49f2b27bc20fabf1c2311bf7feb6bb15c2508149089c524fbf',
</strong><strong>  'browser_userMeta': {
</strong><strong>    'email': 'robin@apple.com' 
</strong><strong>  }
</strong><strong>}}));
</strong></code></pre>

&#x20;

# Source: https://dev.writer.com/api-reference/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Secure your integration

Ensure compliance and secure communications between Writer and your server.

Writer API supports TLS 1.3 by default and TLS 1.2+ in other cases

## Using TLS and HTTPS

TLS refers to the process of securely transmitting data between the client—the app or browser that your customer is using—and your server. This was originally performed using the SSL (Secure Sockets Layer) protocol. However, this is outdated and no longer secure, and has been replaced by TLS. The term “SSL” continues to be used colloquially when referring to TLS and its function to protect transmitted data.

Payment pages must make use of a modern version of TLS (for example, TLS 1.2) as it significantly reduces the risk of you or your customers being exposed to a man-in-the-middle attack. TLS attempts to accomplish the following:

* Encrypt and verify the integrity of traffic between the client and your server
* Verify that the client is communicating with the correct server. In practice, this usually means verifying that the owner of the domain and the owner of the server are the same entity. This helps prevent man-in-the-middle attacks. Without it, there’s no guarantee that you’re encrypting traffic to the right recipient.

Additionally, your customers are more comfortable sharing sensitive information on pages visibly served over HTTPS, which can help increase your customer conversion rate.

If need be, you can test your integration without using HTTPS, and enable it once you’re ready to accept live charges. However, all interactions between your server and Writer must use TLS 1.2 (i.e, when using our libraries).

## Setting up TLS

SERVING RESOURCES SECURELY\
You should make sure that any resources (JavaScript, CSS, images, etc.) are also served over TLS to avoid a mixed content warning being shown to your customers in their browser.

A digital certificate—a file issued by a certification authority (CA)—is needed in order to use TLS. When installed, this certificate assures the client that it’s really communicating with the server it expects to be talking to, not an impostor. You should get a digital certificate from a reputable certificate provider, such as:

* Let’s Encrypt
* DigiCert
* NameCheap\
  Certificates can vary in cost, depending on the type of certificate and provider. Let’s Encrypt is a certificate authority that provides certificates for free.

Conceptually, setting up TLS is very straightforward: a certificate is purchased from a suitable provider, and then your server is configured to use it. The actual process does tend to be somewhat complex, and we recommend you follow the installation guide of the provider you use.

As TLS is a complex suite of cryptographic tools, it's easy to miss a few details. We recommend using the SSL Server Test by Qualys SSL Labs to make sure you have everything set up in a secure way.

## Additional security considerations

It can be a security risk to include JavaScript from other sites as your security becomes dependent on theirs. If they’re ever compromised, an attacker may be able to execute arbitrary code on your page. In practice, many sites make use of JavaScript for services like Google Analytics, even on secure pages. Nonetheless, it’s something to be aware of, and ideally minimize.

If you’re making use of webhooks, we recommend using TLS for the endpoint to avoid traffic being intercepted and the notifications altered (sensitive information is never included in a webhook event).

While complying with the Data Security Standards is important, it shouldn’t be where you stop thinking about security. Some good resources to learn about web security are:

* OWASP
* SANS
* NIST\
  Out-of-scope card data that you can safely store\
  Writer returns non-sensitive card information in the response to a charge request. This includes the card type, the last four digits of the card, and the expiration date. This information is not subject to PCI compliance, so you are able to store any of these properties in your database.

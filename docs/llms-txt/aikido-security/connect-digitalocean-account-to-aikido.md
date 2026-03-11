# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/digital-ocean/connect-digitalocean-account-to-aikido.md

# Connect DigitalOcean Account

### Why connect my DigitalOcean cloud? <a href="#why-connect-my-digitalocean-cloud" id="why-connect-my-digitalocean-cloud"></a>

Securing your cloud infrastructure is crucial to protecting your user data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

**Main Use Cases**

* Aikido surfaces critical cloud misconfigurations that allow hackers to get into your DigitalOcean cloud, such as the risk highlighted in [this blog post](https://www.aikido.dev/blog/how-a-startups-cloud-got-taken-over-by-a-simple-form-that-sends-an-email). All configuration checks can be found [here (filter on DigitalOcean)](https://app.aikido.dev/clouds/checks)
* If you store Docker images in repo, Aikido looks for most known vulnerabilities in Apache, Nginx etc.

Aikido performs a daily compliancy scans on the above.

### Getting started <a href="#getting-started" id="getting-started"></a>

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your DigitalOcean account to Aikido.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeEBzlm2HJVD9MfI70Tsz%2Fimage.png?alt=media&#x26;token=4ba4bf2e-e3d8-472e-a1c4-9ccd5ee61897" alt=""><figcaption></figcaption></figure>

To connect your account, you will need to create an access token that Aikido can use in DigitalOcean. Click on "API" in the left-hand navigation to go to the following screen.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9ae42b55d37202db44df62c49e889085d1e01015%2Fconnect-digitalocean-account-to-aikido_4996db5b-f814-410c-a88e-77ed990b0114.png?alt=media)

On this page, click on "Generate New Token" to create a new token.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61d6afb9852c1462aad6818536352ba3f05707f0%2Fconnect-digitalocean-account-to-aikido_44e23ed1-bfe4-4e94-853b-68f78eac4440.png?alt=media)

Enter a descriptive name for your token, and set the expiration to "No expire". Aikido only needs 'Read' access. Click on "Generate Token".

Once your token is created in DigitalOcean, you can copy it and enter it in Aikido's setup wizard, together with the token name you chose.

Finally, you can name your connected project in Aikido and specify the environment it operates in. This information helps Aikido prioritize findings based on the severity and impact to your business.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5a150e43145ee0115fe707e10aefed6b77d30fa1%2Fconnect-digitalocean-account-to-aikido_09b2e048-f427-40c2-9b47-e8ae568b3e92.png?alt=media)

Within 1-2 minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

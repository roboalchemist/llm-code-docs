# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/allow-listing-in-other-security-solutions.md

# Allow Listing in Other Security Solutions

## Allow Listing in Content Filtering (Proxy)

### Allow Listing Platform Addresses

Platform administrators must allow list **dash.keepnetlabs.com** and **api.keepnetlabs.com** on content filtering proxy solutions to use the products successfully.

{% hint style="warning" %}
If you have completed white labeling, it is sufficient to allow list the platform domain name that will be used to access to platform and api.keepnetlabs.com address.
{% endhint %}

### Allow Listing Phishing Simulation Domain Addresses

The domain names of the [Phishing Simulator](https://keepnetlabs.com/products/phishing-simulator) should be allow listed with content filtering (proxy) solutions to make sure that the domains can be accessed by the target users. If the target users can't access the phishing link in the network, the simulated phishing campaign might not be successful.

You can find the phishing simulation domains by logging into the platform and then go to **Phishing Simulator > Settings > Domains** page.

### Allow Listing in Data Loss Prevention (DLP)

System administrators may upload the target users' first name, last name, email address, department, or such other information to the platform; however, because [DLP](https://digitalguardian.com/blog/what-data-loss-prevention-dlp-definition-data-loss-prevention) can be very sensitive, the platform domain information should be allow listed to ensure DLP allows you to upload these pieces of information to the platform.

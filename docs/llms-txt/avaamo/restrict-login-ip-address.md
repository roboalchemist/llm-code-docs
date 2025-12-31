# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/restrict-login-ip-address.md

# Restrict login IP address

By default, Avaamo Platform Dashboard does not restrict login access based on IP addresses. However, for added security, you can control login access to the Avaamo Platform dashboard at the company level by specifying a range of allowed IP addresses on the company's profile. This feature helps in providing better overall security, remote access, and anonymity.&#x20;

{% hint style="info" %}
**Note**: When you define IP address restrictions for a profile, a login from any other IP address to the Avaamo Platform is denied. Dashboard users of the company can log in only through allowed or restricted IP addresses. This also restricts the integration of any [public APIs](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation) that use the user access token on your client-side dashboard, since the dashboard is accessible only through allowed or restricted IP addresses.
{% endhint %}

This article explains the process of setting up allowed IP addresses at the company level within the Avaamo Conversational AI system for restricted access.

### Set up allowed IP addresses

Contact Avaamo Support with the following details:

* Company for which you wish to set up the allowed IP addresses
* List or range of allowed IP addresses in the IPv4 format. Supported examples: 49.14.176.91, 49.37.165.0/16.

The Avaamo support configures the list of allowed IP addresses for your company as per the details received.

### Test restricted access

After the configuration is completed, Dashboard users of the company can log in only through allowed or restricted IP addresses. With valid login credentials to the Avaamo Platform Dashboard,&#x20;

* Login to the Avaamo Platform after connecting to IP address that is not in the allowed range. Access is denied and the following error message is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTnsBAX4Z1PEBQ24FRG%2F-MTnyS5MQT5LRN-SCL7T%2F5.6.1-invalid%20email-pin.png?alt=media\&token=2660e770-dc04-4122-8d2d-ecde4648bb5c)

* Login to the Avaamo Platform after connecting to IP address that is in the allowed range. You can log in successfully and access the Avaamo Platform dashboard.

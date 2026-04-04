# Source: https://help.aikido.dev/pentests/safety-measures.md

# Safety Measures

To minimise the impact the pentest can have on your environment, the following safety mechanisms are in place.&#x20;

{% hint style="success" %}
We strongly recommend to launch the pentest in staging, test or isolated environments
{% endhint %}

## Preventing pentests outside of intended scope

By design, the pentesting agents cannot reach domains that have not been explicitly approved during the setup of the pentest. Two security boundaries are in place:&#x20;

1. **Attackable domains**: Domains that can be actively attacked during the pentest
2. **Reachable domains:** Domains that should not be actively attacked but are allowed to reach.&#x20;

In the example configuration below, the pentesting agents can reach  "portal.attack-me.com",  "api.attack-me.com" and "login.attack-me.com" but are not going to attack "login.attack-me.com". All other domains are blocked.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F40YXmy9uGn9xJokSGuZp%2Fimage.png?alt=media&#x26;token=ff7cd138-9341-4556-989f-6447cf889d41" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Requests containing static files or that are part of developer tool platforms are automatically marked Allowed (but will not be attacked)
{% endhint %}

## Cancel pentest any time

In case anything goes wrong during the pentest, the pentest can be cancelled at any time.  This will terminate all ongoing actions and stop the pentest fully.&#x20;

## Mitigating high server load

To minimize potential impact due to server load, the setup allows the configuration of the maximum requests per second that the pentest generates and the option to execute it in our outside of business hours.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FQOf4KM49xajq22OKrLec%2Fimage.png?alt=media&#x26;token=f859bf06-6021-43dd-ae3b-0f9b657f7197" alt=""><figcaption></figcaption></figure>

# Source: https://docs.portainer.io/2.33-lts/faqs/known-issues/hardware-acceleration-gpu-button-is-missing.md

# Source: https://docs.portainer.io/sts/faqs/known-issues/hardware-acceleration-gpu-button-is-missing.md

# Source: https://docs.portainer.io/faqs/known-issues/hardware-acceleration-gpu-button-is-missing.md

# Hardware Acceleration GPU button is missing

{% hint style="info" %}
**Affected versions:** 2.15.0, 2.16.0, 2.17.0

**Fixed in:** 2.18.0 and above
{% endhint %}

#### Issue Description

After upgrading a Portainer installation from 2.14.2 to a newer version, the Hardware Acceleration GPU button is missing.

#### Cause

This issue is the result of a bug in the upgrade process of Portainer where a value is set incorrectly.

#### Workaround

You can manually resolve this issue in your configuration through the Portainer API by setting the Gpus option to the correct value of \[].  Here is an example API command:

```
http --verify=no PUT https://localhost:9443/api/endpoints/1 X-API-Key:my-api-key Gpus:='[]'
```

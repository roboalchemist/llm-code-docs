# Source: https://docs.portainer.io/2.33-lts/faqs/known-issues/groups-info-issue-with-oauth-using-microsoft-ad.md

# Source: https://docs.portainer.io/sts/faqs/known-issues/groups-info-issue-with-oauth-using-microsoft-ad.md

# Source: https://docs.portainer.io/faqs/known-issues/groups-info-issue-with-oauth-using-microsoft-ad.md

# Groups info issue with OAuth using Microsoft AD

{% hint style="info" %}
**Affected versions:** 2.14.2 and previous

**Fixed in:** 2.15.0 and above
{% endhint %}

#### Issue Description

If you have configured OAuth using Microsoft AD in Portainer and trying to use Automatic Team membership you may run into an issue where group membership information is not returned correctly and users are not populated into the correct teams in Portainer.

#### Fix

Update Portainer to 2.15.0 or above.

#### Workaround

In OAuth Config, use the following URL for Resource URL (replace the existing graph.windows.net URL)

```
https://login.microsoftonline.com/<tenant ID>/openid/userinfo
```

User Identifier: unique\_name\
Scopes: openid profile

You will also need to have following permissions on your App Registration in Azure:

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7ffQ4DIuSIW9Dne9HRFk/image.png" alt=""><figcaption></figcaption></figure>

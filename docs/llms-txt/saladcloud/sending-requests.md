# Source: https://docs.salad.com/container-engine/how-to-guides/gateway/sending-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticated Requests

*Last Updated: October 15, 2024*

If you have selected authentication for the Container Gateway, the access domain name will indicated it is "Protected"
and a lock icon will be shown. You will need to provide your API key in the header of requests.

First, you'll need the domain name of your container group and your API key. You can view and copy your API key at
[portal](https://portal.salad.com/api-key).

Obtain the domain name in the details of your deployment, e.g.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d158f3a5bd0dde1aa361cba1575364bc" data-og-width="725" width="725" data-og-height="111" height="111" data-path="container-engine/images/portal-access-domain-name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=1611f4fc178857612425bbfe0bc50349 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=94515bad6d40253ebee509c437951b99 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=f9aaa8a68244f2dc3a3fcd43c5a9950a 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=db8bcbcb0679bce6ade1f39771d41056 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0497722b9b9d7042e5d35ea1c60f2d1b 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-access-domain-name.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=1701c5c221e5068416977a8b0d5b3a2e 2500w" />

You can Copy the domain name by clicking the copy icon on the right.

Send a request to the access domain name with your API key included in the header as `Salad-Api-Key` however you'd like,
e.g.

```
curl --location '[YOUR ACCESS DOMAIN NAME HERE]'
  --header 'Content-Type: application/json'
    --header 'Salad-Api-Key: [YOUR API KEY HERE]'
      --data '{
 								...
              }'
```

# Optional Container Gateway Authentication

Please note that requiring authenticated networking to the containers is optional, You can choose whether to enable or
disable authentication for your containers. However, we recommend implementing your own authentication if you plan not
to use ours.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9ef70617ece084810431ebe61228d4cb" data-og-width="530" width="530" data-og-height="520" height="520" data-path="container-engine/images/portal-enable-authentication.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4ead57795cf28d209e709ef78307bca2 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5a551b1f382b0190cd23454f78104de8 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8d1693dc8ae58fdf130ace6aefade75e 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3ed52815d2b28f95c8a0046baa6b4cfd 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ce6f4fc570b1b006717cc4f7cf625f5b 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-enable-authentication.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=d6cc80b3d59b2b3ef42421f50aa56943 2500w" />

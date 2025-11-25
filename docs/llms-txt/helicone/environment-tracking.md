# Source: https://docs.helicone.ai/guides/cookbooks/environment-tracking.md

# Environment Tracking

> Effortlessly track and manage your development, staging, and production environments with Helicone.

Many organizations operate across multiple environments, such as development, staging, and production. To differentiate these environments, you can establish a `Helicone-Property-Environment` property. In the example below, we assign the "development" property to the environment:

```python  theme={null}
client.chat.completions.create(
    # ...
    extra_headers={
        "Helicone-Property-Environment": "development",
    }
)
```

If you are utilizing any other libraries or packages, please refer to our [Custom Properties](/features/advanced-usage/custom-properties) documentation for guidance.

### Viewing Environments

On the [request page](https://www.helicone.ai/requests), you can conveniently view all the environments that your organization has employed.

<Frame>
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ba613389f4e6b9f9e2a1d5c35298d5c2" alt="View environments tracked by Helicone on the Requests page." data-og-width="2530" width="2530" data-og-height="1222" height="1222" data-path="images/environment-cp/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=fb85e384f29dc7674ffec819d1b4eea3 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=999f192e424691e8e913b26e4bf0a6e3 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=72b344842702c1bb5e953ae23c0c00b8 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=5eecc006177c09440911330ac56d9fca 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=823819236e7dcda62e23368e86cb391f 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/1.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=d454c4114ce66c26a10aabc704e3d61f 2500w" />
</Frame>

Additionally, you can filter by environment to view all the requests made within that specific environment.

<Frame>
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=8a762f18db68944d70bf2ef6d8af9bb8" alt="Filter requests by specific environments on the Requests page." data-og-width="2598" width="2598" data-og-height="862" height="862" data-path="images/environment-cp/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=2223fa76b0c0fb032caebedb1190beee 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=f9e33a1a2ce602a8c731924802c400d2 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=fd9dcd5e3d14211cf21def0c87aba218 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=1e4784b6db03855f7c05d6c931d3f3b8 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=3a8579eb1ae3bfeaf2a58faba3415945 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=056b94d029197cca86503910d6cc5d67 2500w" />
</Frame>

Efficiently add filters to your requests to view all the requests made in a particular environment.

<Frame>
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=137cefc38e64e27126e6c33a5a4c7352" alt="Add filters to specify environment within Helicone." data-og-width="1546" width="1546" data-og-height="474" height="474" data-path="images/environment-cp/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=26b31ee1d9553c8910a8daf987c82b32 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=d9770e7f00692812bc1fb3dce0fc9a33 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=295e2ada0498e1398cb397f6d1a4cfe9 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=0a952d942a427921a708016a274d4649 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=98791d485c4edf9d5b8c9adad866bd27 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=767d985acf021dd295a3d37a57f4877b 2500w" />
</Frame>

Helicone also offers a dedicated page to view all the environments that your organization has utilized. You can also view the number of requests made in each environment.

Visit the [properties page](https://www.helicone.ai/properties) to view all the environments that your organization has employed.

<Frame>
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=31e2f7b213b75f908695dd9628e89333" alt="View cost, usage and latency associated with a custom property on the Properties page." data-og-width="3376" width="3376" data-og-height="1892" height="1892" data-path="images/environment-cp/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=73490a478531298182421677f24c0155 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=e37bc957589f08da5cb243e9ad4456ff 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=dbb0bd048d78c0c191fbb42129c6493a 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ec6064884c98de67fa18af59eda8d083 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=6f2534ceebf0461b1dbdc20adbef3755 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=013ae787139437345709918a137c28a3 2500w" />
</Frame>

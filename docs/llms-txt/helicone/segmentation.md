# Source: https://docs.helicone.ai/guides/cookbooks/segmentation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Custom Properties to Segment Data

> Derive powerful insights into costs and user behaviors using custom properties in Helicone. Learn to track environments, user types, and more.

Use [Custom Properties](features/advanced-usage/custom-properties) to segment your data and derive meaningful insights. This feature can help you understand the costs and behavior of different user groups, and gain other insights to help inform strategic decisions and optimizations.

Here are some methods that we recommend for data segmentation:

<CardGroup cols={3}>
  <Card title="Use Case 1" href="/use-cases/segmentation#use-case-1-tracking-environments">
    Tracking Environments
  </Card>

  <Card title="Use Case 2" href="/use-cases/segmentation#use-case-2-user-segmentation">
    User Segmentation
  </Card>

  <Card title="Use Case 3" href="/use-cases/segmentation#use-case-3-advanced-segmentation">
    Advanced Segmentation
  </Card>
</CardGroup>

<Note>
  If you have other use cases, we'd love to know! Send us an
  [email](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.{" "}
</Note>

## Use Case 1: Tracking Environments

Organizations use **Custom Properties** to track different environments (i.e. development, staging, and production). To distinguish between these environments, you can create a `Helicone-Property-Environment` property.

### Quick Start

<Steps>
  <Step title="Add the 'Environment' property and assign a value.">
    ```python  theme={null}
    client.chat.completions.create(
        # ...
        extra_headers={
            "Helicone-Property-Environment": "development",
        }
    )
    ```
  </Step>

  <Step title="Send a request.">
    You will then see the `Environment` property appear in the Requests page.

    <Frame caption="In this example, we now have a property called 'environment'.">
      <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=8a762f18db68944d70bf2ef6d8af9bb8" alt="Example of the Helicone Requests page showing a custom property named 'environment'." data-og-width="2598" width="2598" data-og-height="862" height="862" data-path="images/environment-cp/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=2223fa76b0c0fb032caebedb1190beee 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=f9e33a1a2ce602a8c731924802c400d2 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=fd9dcd5e3d14211cf21def0c87aba218 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=1e4784b6db03855f7c05d6c931d3f3b8 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=3a8579eb1ae3bfeaf2a58faba3415945 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/2.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=056b94d029197cca86503910d6cc5d67 2500w" />
    </Frame>

    You can choose to hide the custom property by deselecting it under `Columns`.

    <Frame caption="You can modify other properties in a similar manner.">
      <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=a1ced5a9e3122ec2fcc8398311459064" alt="Example of modifying Helicone's interface to show or hide a custom property." data-og-width="940" width="940" data-og-height="602" height="602" data-path="images/environment-cp/cp-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=83c0a178c7de3d7cd271906623a95697 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=789935870afe4334810c53c868f13834 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=18ce3b910f1ebcbd3ad0a4b91451cf36 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=92c466e9778edc22073d0cbbfdb0108f 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ab4d78d6dcd15b5e2e281e3deed6049c 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/cp-1.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=38c6d97246dbae89eacca8d742df54c1 2500w" />
    </Frame>
  </Step>

  <Step title="Filter by custom properties">
    <Frame caption="Filter all requests labelled as 'development'.">
      <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=137cefc38e64e27126e6c33a5a4c7352" alt="Example of filtering requests labeled 'development' in Helicone." data-og-width="1546" width="1546" data-og-height="474" height="474" data-path="images/environment-cp/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=26b31ee1d9553c8910a8daf987c82b32 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=d9770e7f00692812bc1fb3dce0fc9a33 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=295e2ada0498e1398cb397f6d1a4cfe9 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=0a952d942a427921a708016a274d4649 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=98791d485c4edf9d5b8c9adad866bd27 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/3.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=767d985acf021dd295a3d37a57f4877b 2500w" />
    </Frame>
  </Step>

  <Step title="View metrics associated with a custom property. ">
    Go to the `Properties` page, and select `Environment`. You will see metrics associated with this custom property.

    <Frame caption="View total costs, requests and average latency for `Environment'.">
      <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=31e2f7b213b75f908695dd9628e89333" alt="Viewing metrics associated with the 'Environment' custom property on Helicone's Properties page." data-og-width="3376" width="3376" data-og-height="1892" height="1892" data-path="images/environment-cp/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=73490a478531298182421677f24c0155 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=e37bc957589f08da5cb243e9ad4456ff 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=dbb0bd048d78c0c191fbb42129c6493a 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ec6064884c98de67fa18af59eda8d083 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=6f2534ceebf0461b1dbdc20adbef3755 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/environment-cp/4.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=013ae787139437345709918a137c28a3 2500w" />
    </Frame>
  </Step>
</Steps>

## Use Case 2: User Segmentation

A common method of data segmentation is by `user type`. For example, you might want to distinguish between **paying** and **free** users to understand their behaviors and costs.

### Quick Start

To do this, create a `user_type` custom property and assign either **"paid"** or **"free"**.

```python  theme={null}
client.chat.completions.create(
    # ...
    extra_headers={
        "Helicone-Property-User-Type": "free",
    }
)
```

Then, you can filter by paid/free users, or view associated metrics in the same way.

<Tip>
  Data segmentation can become powerful when you combine it with other
  properties.{" "}
</Tip>

### Further Segmentation

Suppose you want to understand the behavior of paying users when they use a specific feature (i.e. spellcheck). You can add a `Feature` custom property.

```python  theme={null}
client.chat.completions.create(
    # ...
    extra_headers={
        "Helicone-Property-User-Type": "paid",
        "Helicone-Property-Feature": "spellcheck",
    }
)
```

You can create highly detailed segment by adding even more custom properties. For example, you may segment users further by `plan` and `Job ID`. There are no limits on the number of custom properties you can add.

```python  theme={null}
client.chat.completions.create(
    # ...
    extra_headers={
        "Helicone-Property-User-Type": "paid",
        "Helicone-Property-Feature": "spellcheck",
        "Helicone-Property-Plan": "enterprise",
        "Helicone-Property-Job-UUID": "1234-5678-9012-3456",
    }
)
```

### Analyzing Segmented Data

Segmented data can provide you with invaluable insights. For example, you might discover that your free users are using the spellcheck feature more than your paid users. This could signal an opportunity to market this feature more aggressively within your premium plans.

## Use Case 3: Advanced Segmentation

You can refine your segments further by incorporating other properties. The more detailed your segments, the more accurate insights you can derive. Here are some examples:

* Location: `Helicone-Property-Location`
* Device type: `Helicone-Property-Device-Type`
* Use activity level: `Helicone-Property-Activity-Level`

Remember, the key is to select properties that best align with your objectives and that will yield valuable insights upon analysis.

***

<Accordion title="Need more help?">
  Additional questions or feedback? Reach out to
  [help@helicone.ai](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.
</Accordion>

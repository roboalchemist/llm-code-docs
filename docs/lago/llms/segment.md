# Source: https://getlago.com/docs/templates/hybrid/segment.md

# Source: https://getlago.com/docs/integrations/usage/segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment

> Segment is a powerful tool that allows you to track the usage of your customers, providing valuable insights that can help you make  data-driven decisions. This data can be sent to Lago, our usage-based billing platform, to automate your billing process and ensure  accurate invoicing for your customers.

Here's a step-by-step guide to help you get started:

## Prerequisites

**In Lago:**

1. Create a Lago organization to manage your billing and invoicing;
2. Create a Billable metric to track the usage of your customers;
3. Create a Plan and price the above billable metric to determine the billing rates for your customers; and
4. Create a Customer and assign the Plan.

**In Segment:**

1. Create a Segment account;
2. Create a data source (ideally, product usage of your customer);

## Send usage from Segment to Lago

### Create a function

To accomplish this, you'll need to create a custom **Function** in Segment. This can be done by following these simple steps:

1. Navigate to the **Catalog** in Segment;
2. Click the **Functions** tab to access the custom Functions feature;
3. Choose to create your first function and follow the prompts to set it up.

<Frame caption="Segment Functions">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=ff517969f241be63547b33ea49004bbe" data-og-width="2996" width="2996" data-og-height="1100" height="1100" data-path="integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c9c9ac87dfceb4f493fda384c89912ac 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=95d6a434fe5779dbeefeb446317b341a 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=f6be2cfb16a1fba4bec287e1906072a0 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=a0d45aa8c4c78c9e43ea19efe71a368a 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5a7277f21ebd155d00a9b09f7907d0fd 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-catalog-1a7de549eb06d94a6a8ce92565e957a8.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=0d507105ef6bda9fbf0d6257b6adb1c2 2500w" />
</Frame>

### Use the Destination function

Make sure to select the **Destination function**, as you want to send data from Segment to Lago.

<Frame caption="Destinations function">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=d374f48ed23590453a0e515f59ee209f" data-og-width="2972" width="2972" data-og-height="1336" height="1336" data-path="integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=ef7ae616454308379a8bc75b0ad6b300 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c233d58c76bb7408188eab4b4e049f7f 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5078d8c77475a801dee20929b82fb165 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=aa499ae038ee9e5ff5fd1a50e6ea8b80 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=25614259cc3e0557685d8663b15ed2c3 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/destination-function-segment-6131770a6f0e5b7c8e7bf694ca6339b3.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=dd07ee38e7fa913c00a72112d196f572 2500w" />
</Frame>

### Post Request to Lago events

To successfully integrate Lago with Segment, you'll need to replace the pre-written functions in the code editor with the following code. This example function, written by the Lago team, will catch a **Track** event from Segment, define the targeted endpoint (events) in Lago, build the body of the request, and finally post the event.

```javascript  theme={"dark"}
// Running everytime a Track call is made on Segment
async function onTrack(event, settings) {

  // events endpoint to reach
  const endpoint = 'https://api.getlago.com/api/v1/events';

  // body of the event following Lago documentation
    const body = {
      event: {
        transactionId: event.messageId,
        externalCustomerId: event.userId,
        code: event.event,
        properties: {
          invoiceId: event.properties.invoice_id
        }
      }
    };

    // Post event
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${settings.api}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    });

    return response.json();

  }
```

<Info>
  This function can be adapted with Identify, Group or Page events. Please, refer to [Segment's documentation](https://segment.com/docs/connections/functions/destination-functions/) for all available actions.
</Info>

<Info>
  The `body` structure of the event depends on your use case. Please adapt it if needed (*ie: remove or add properties*). You can also add conditions if you want to send data to Lago only on specific events.
</Info>

### Use the test mode editor

By using a sample event, you can preview the incoming data fetched from a Segment event. This will help you post a request for existing data or debug.

<Frame caption="Segment Sample Events">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=d6cf9c31c718cd2644b9e31a1a3582c4" data-og-width="2980" width="2980" data-og-height="1252" height="1252" data-path="integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=30d89efe853a39f71efb95b90eab037c 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e71ec951a2779657a34f1e68ee5c438d 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=47d88945009ac8abd815cab4b37d7ab3 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=55465e35c97b49ba1a81ce0cc32acf7a 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=6d3653d73bef718a49be200b996cb0fe 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/test-mode-segment-747eee5ec2ff46a349064e3dbbf4a758.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=35c7df486902438b18e0f8bed5578f77 2500w" />
</Frame>

### Hide sensitive data

Let's take back the example from the code written above. We decided to hide the **API Key** and mark it as sensitive information. By setting this as a variable, you make sure not to hard code your private key in the function.

To create **Settings** variables:

1. Go to the **Settings** tab;
2. **Add** a new Setting;
3. Define a **Name** and a **Label** for this Settings;
4. Define it as **Required** or **Optional**; and
5. Mark is as **Sensitive** or not.

<Frame caption="Hide sensitive data with settings variables">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2326eb0d7eb514d91a0450674b69723b" data-og-width="2972" width="2972" data-og-height="884" height="884" data-path="integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=f21e012320118d00552fd16448dd54fe 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e0cbd6961c1c0367e25ab8c1a7c9de2b 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=3609285441cd9ae6d3fff1f24d10df98 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=72d1e99a079233d5a9b4d5d59935b6f7 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=09e1278d6def1abfb87f5023bbb6c281 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/segment-settings-variable-c19b5f3de23eec11ffe475e8272dc5ff.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=10d5439ddb668f44296f5101ef95009a 2500w" />
</Frame>

### Send usage events to Lago

By running the function in Segment, this will send a test usage to Lago events. You can retrieve this event in the events list. By finalizing the setup in Segment, the function will be automatically triggered based on your defined behavior

## Segment to Lago - demo video

If easier, please find a demo video explaining the full setup of custom functions to send event from Segment.com to Lago.

<iframe width="700" height="500" src="https://www.youtube.com/embed/lyJmdh47JTE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

# Source: https://docs.frigade.com/integrations/heap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Heap

Frigade supports bidirectional reads and writes from Heap. This guide shows you how to get started in a few minutes.

## Sending Frigade data to Heap

The following steps will help you send data from Frigade to Heap. For instance, when a user completes a Survey or a step in a Checklist, Frigade can send this data to Heap.

<Steps>
  <Step title="Get your Heap Environment ID">
    From the Heap dashboard, navigate to **Settings** and open **Projects**.
    Click the appropriate project and environment and copy the numeric **Environment ID**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=c9aaf64c9e9d33f7ee678558d91ef958" className="rounded" data-og-width="1493" width="1493" data-og-height="875" height="875" data-path="images/integrations/heap/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9a8954b0fc9aceac40c834c4b694b02a 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=50b597f97779b8f87c156b3805901071 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fb36214f35cec377737735bca99c3721 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=19b91f54245e189366973a1d59f85c89 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6535c18c36c879714861e0d17ab09f5f 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a81aaffc595f4dc4e820d9f0ab641c0d 2500w" />
  </Step>

  <Step title="Add Heap in Frigade">
    Next, go to your Frigade dashboard and select **Integrations**. Click **Add Integration** and select **Heap**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6bcc9086b2808f9d596ddaed04bb449d" className="rounded" data-og-width="1395" width="1395" data-og-height="825" height="825" data-path="images/integrations/heap/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7c05651a411f06d612188cc9541becfc 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=75aa5121e93c01f767dc8e1971062d93 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5eab8efc716d0cc25c1c3e9c868ad0d4 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=83eb8ed9df03c08be2fe24b218e8e04e 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=97165363154e329c233d6a314e5c2307 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1b4060a4e52646d0ec8f58b59edb48c5 2500w" />

    You will be asked to enter your Heap Environment ID. Click **Connect** to save and activate the integration. Shortly after, events will start streaming from Frigade in real-time.
  </Step>

  <Step title="See Frigade events in Heap">
    You should now see events from Frigade in your Heap dashboard. You can test the integration by completing a Flow and checking the **Live data feed** page in Heap:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ca238de01f7f28293ffb7f95c2a2edbb" className="rounded" data-og-width="1380" width="1380" data-og-height="812" height="812" data-path="images/integrations/heap/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6e2fded11031ee5879b1f029fb7264dc 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=df5336e86ec739e01384c3e2b66203be 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=cb616c9898e02d0f5fa57e0d64d638f8 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=45a3454dd05a44db6208e0821407d2a6 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3e5ab8a811fc3c7a13cd3828c7bc1386 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3ddaeec8d7a8593b426dd9eac505f1f2 2500w" />
  </Step>
</Steps>

## Sending Heap segments to Frigade

<Note>This feature is in early preview. <a href="mailto:support@frigade.com">Reach out</a> to get early access.</Note>

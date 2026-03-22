# Source: https://docs.brightdata.com/api-reference/scraper-studio-api/Choose_a_delivery_type_on_request_level.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose a delivery type on request level

Instead of creating duplicate scrapers for each delivery type, you can choose a delivery type per job using API.

<Frame>
    <img src="https://mintcdn.com/brightdata/a-wmt8sZJyXzLgP2/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/hero-image.png?fit=max&auto=format&n=a-wmt8sZJyXzLgP2&q=85&s=c32b69390ddfb19a5e2166aef7be490c" alt="hero-image.png" width="1308" height="371" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/hero-image.png" />
</Frame>

<Steps>
  <Step title="Update your scraper">
    Ensure that your scraper is updated to the latest version to improve success rate

    <Frame>
            <img src="https://mintcdn.com/brightdata/2-G3wocTpDaL5JJE/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/update-available.png?fit=max&auto=format&n=2-G3wocTpDaL5JJE&q=85&s=7c9c23bebc7b6c2d2893f5b7f1eb7c32" alt="update-available.png" width="1624" height="354" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/update-available.png" />
    </Frame>
  </Step>

  <Step title="Set a delivery type to Batch">
    <Frame>
      <img src="https://mintcdn.com/brightdata/a-wmt8sZJyXzLgP2/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/type-batch.png?fit=max&auto=format&n=a-wmt8sZJyXzLgP2&q=85&s=6e44615cc0a94f9c5a2b42f6a30002c6" alt="type-batch.png" width="1613" height="353" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/type-batch.png" />
      <img src="https://mintcdn.com/brightdata/a-wmt8sZJyXzLgP2/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/on-completion.png?fit=max&auto=format&n=a-wmt8sZJyXzLgP2&q=85&s=33e70e9e3450d65d969514ac133035a7" alt="on-completion.png" width="940" height="287" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/on-completion.png" />
    </Frame>

    Following error message will be returned from Batch API when delivery type is set to Realtime.

    ```json Error theme={null}
    "error": "Cannot trigger a batch job with a real-time scraper. Use /trigger_immediate endpoint instead"
    ```
  </Step>

  <Step title="Trigger the scraper using a preferred API">
    <Tabs>
      <Tab title="Initiate a Batch job">
        `dca/trigger`

        [Trigger a scraper for batch collection method](/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)

        <CodeGroup>
          ```sh Shell theme={null}
          curl "https://api.brightdata.com/dca/trigger?collector=ID_COLLECTOR&queue_next=1" -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '[{"url":"https://targetwebsite.com/product_id/"}]'
          ```

          ```json Sample Response theme={null}
          {
              "collection_id":"j_l3daejgw1wnpjxxxxx",
              "start_eta":"2022-05-19T17:28:48.056Z"
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Initiate a Realtime job">
        `dca/trigger_immediate`

        [Trigger a scraper for real-time collection](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)

        <CodeGroup>
          ```sh Shell theme={null}
          curl "https://api.brightdata.com/dca/trigger_immediate?collector=ID_COLLECTOR" -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"url":"https://targetwebsite.com/product_id/"}'
          ```

          ```json Sample Response theme={null}
          {
              "response_id":"z2805t1652973963340rg6252xxxxxx"
          }
          ```
        </CodeGroup>
      </Tab>
    </Tabs>

    <Note>
      Batch responses begin with `j_****` and real-time responses begin with `z****`
    </Note>
  </Step>

  <Step title="Receive data">
    * [Receive batch data](/api-reference/scraper-studio-api/Receive_batch_data)
    * [Receive data from real-time work scraper](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)
  </Step>
</Steps>

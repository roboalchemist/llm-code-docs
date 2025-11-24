# Source: https://docs.zapier.com/powered-by-zapier/ai-workflows/zap-guesser.md

# Zap Guesser

> Quickly generate intelligent Zap suggestions from natural language prompts.

The Zap Guesser lets you generate a suggested Zap and a pre-filled URL to the Zapier editor by submitting a simple description of the workflow you want to automate. This is ideal for building AI-driven Zap recommendations based on user input.

<Note>
  You can leverage the Workflow Element for a no-code, visual experience that
  integrates directly into your app or site, or you can use the API to
  programmatically generate Zap suggestions based on a user's prompts or prompts
  generated from a user's activity.
</Note>

## Workflow Element Usage

You can view our [Workflow Element Documentation](/powered-by-zapier/embedding-zapier/workflow-element) and then visit the [Workflow Element Builder](https://zapier.com/partner/embed/workflow) if you'd like to embed the Workflow Element.

<Frame caption="Leverage the Workflow Element for a no-code, visual experience that integrates directly into your app or site.">
  <video controls className="w-full aspect-video" src="https://cdn.zappy.app/75e9d02f52b27dad2eb383d190236eac.mov" />
</Frame>

## API Usage

To generate a Zap suggestion, send a POST request to the [/v2/guess](/powered-by-zapier/api-reference/zaps/guess-a-zap) endpoint with a client\_id as a query parameter and a description in the JSON body.

### Example Request

Content-Type: application/json

```json  theme={null}
{
  "description": "Save new leads from Facebook Lead Ads to Google Sheets, and email me the lead in Gmail"
}
```

Example Response

```json  theme={null}
{
  "title": "Save Facebook Lead Ads leads to Google Sheets and send an email",
  "steps": [
    {
      "step": {
        "title": "Trigger when a new lead is created in Facebook Lead Ads",
        "app": "Facebook Lead Ads",
        "api": "FacebookLeadsAPI"
      },
      "alternatives": [
        {
          "title": null,
          "app": "LinkedIn Ads",
          "api": "LinkedInLeadGenFormsCLIAPI@2.7.1"
        }
      ]
    },
    {
      "step": {
        "title": "Save the lead information to a Google Sheet",
        "app": "Google Sheets",
        "api": "GoogleSheetsV2API"
      },
      "alternatives": []
    }
  ],
  "prefilled_url": "https://api.zapier.com/v1/embed/my-app/create?steps%5B0%5D%5Bapp%5D=FacebookLeadsAPI&steps%5B0%5D%5Baction%5D=lead&steps%5B0%5D%5Btype%5D=read&steps%5B1%5D%5Bapp%5D=GoogleSheetsV2API&steps%5B1%5D%5Baction%5D=add_row&steps%5B1%5D%5Btype%5D=write&utm_campaign=partner_zap_guesser&copilot_prompt=Save+new+leads+from+Facebook+Lead+Ads+to+Google+Sheets%2C+and+email+me+the+lead+in+Gmail&partner_zap_guesser_attempt_id=22f44602-db8f-4a2a-8b09-420b0d277b5f"
}
```

The prefilled\_url directs users to the Zap editor with high-confidence steps already filled in. Users can fine-tune the automation or activate the Zap from there.

Usage Notes

* **client\_id** is required as a query parameter and must be valid. See [authentication](/powered-by-zapier/authentication/methods/client-id) documentation to locate your client ID.
* **description** should be a short, clear sentence describing the automation you want to build.
* The returned **steps** include the best match and potential alternatives for each step.
* Use the **prefilled\_url** in your application to guide users directly into a personalized Zap-building experience.
* This API is [rate limited](/powered-by-zapier/api-reference/rate-limiting).

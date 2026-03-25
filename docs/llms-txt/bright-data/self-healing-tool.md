# Source: https://docs.brightdata.com/datasets/scraper-studio/self-healing-tool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Fix and Modify Your Scraper Using the Self Healing Tool

This guide shows you how to use the Self Healing Tool to automatically update your scraper's code - adding or removing output fields and resolving broken code - without needing to manually edit the underlying script.

## What Is the Self Healing Tool?

The Self Healing Tool is an AI-powered code refactor assistant built into Scraper Studio. When your scraper breaks due to a site structure change, or when you need to add or remove output fields, the tool rewrites the relevant parts of your collector's code based on a plain-language prompt - so you don't need to dig into the code manually.

<Tip>
  ### When to use it:

  Use the Self Healing Tool when a collector stops returning expected data, or when you need to quickly add/remove fields like `price`, `image`, or `rating` without deep coding knowledge.
</Tip>

<Accordion title="Prerequisites" icon="list-check" iconType="duotone">
  * An active [Bright Data account](https://brightdata.com/)
  * An existing scraper in Scraper Studio (Development mode saved version)
  * Access to the Scraper Studio IDE
</Accordion>

<Steps>
  <Step title="Open the Self Healing Tool">
    In your Scraper Studio IDE, locate the Self Healing Tool

    <Frame>
            <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/self-healing-tool-location.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=e0c198d40b13e3e6af91d062010d5339" alt="self-healing-tool-location.png" width="2598" height="1902" data-path="images/datasets/scraper-studio/self-healing-tool/self-healing-tool-location.png" />
    </Frame>

    > ***Expected result**: You should see a text input field, ready to accept your instruction.*

    <Frame>
            <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/refactor-collector.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=06a4618922395e07c1ed0bacb2a534ca" alt="refactor-collector.png" width="1324" height="646" data-path="images/datasets/scraper-studio/self-healing-tool/refactor-collector.png" />
    </Frame>
  </Step>

  <Step title="Describe the Fix or Change You Need">
    Type your request in plain language into the prompt field. Be specific about what is broken or what you want to add.

    ```txt Example prompts: wrap theme={null}
    Add 'price' and 'image' fields to the output

    The 'price' value is returning 'undefined', please fix  
    The 'price' field is returning incorrect data from HTML, switch to using tag_response() to capture '/api/price' instead  
    ```

    > ***Expected result**: The AI processes your prompt and generates a proposed code change, highlighted as a diff in the editor.*

    <Note>
      You don't have to stay on the page while the Self Healing Tool processes your request, it can take up to 15 mins. Once the AI refactoring is complete, you'll receive an email notification so you can come back and review the proposed changes at your convenience.

      <Frame>
                <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/email.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=8aa0325cc5814f108443476457b538d5" alt="email.png" width="1582" height="1252" data-path="images/datasets/scraper-studio/self-healing-tool/email.png" />
      </Frame>
    </Note>
  </Step>

  <Step title="Review the Proposed Changes">
    Examine the AI-generated diff in the code template. Verify the changes match your intent before accepting.

    * ✅ Accept - Saves the changes to a draft
    * ❌ Decline - Discards the suggestion; your original code remains unchanged

    > ***Expected result**: If accepted, the editor reflects the updated code and saves it to the draft*
  </Step>

  <Step title="Run a Preview">
    After accepting the changes, run a Preview to validate that the scraper is returning the expected data correctly.

    <Frame>
            <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/run-a-preview.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=4114785ce0dce9532380cbc52cdca947" alt="run-a-preview.png" width="3158" height="924" data-path="images/datasets/scraper-studio/self-healing-tool/run-a-preview.png" />
    </Frame>

    > ***Expected result**: Your output file includes the newly added/fixed fields with valid, non-undefined values.*

    <Frame>
            <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/view-download.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=238a2dd5ec17e0b7a9e4416d0d0d5b76" alt="view-download.png" width="1457" height="1091" data-path="images/datasets/scraper-studio/self-healing-tool/view-download.png" />
    </Frame>
  </Step>

  <Step title="Save to Production">
    Once the Preview confirms the data is correct, save the scraper to Production.

    <Frame>
            <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/save-to-production.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=89456f88669516dd669724929def0d5b" alt="save-to-production.png" width="550" height="301" data-path="images/datasets/scraper-studio/self-healing-tool/save-to-production.png" />
    </Frame>

    <Note>
      If you added/renamed fields, you will be prompted to update the schema. Click <Badge color="blue">Update Schema</Badge>, then click <Badge color="blue">Save to Production</Badge>.
    </Note>

    <Frame>
            <img src="https://mintcdn.com/brightdata/U8muwkGHc7tnC6aA/images/datasets/scraper-studio/self-healing-tool/update-schema.png?fit=max&auto=format&n=U8muwkGHc7tnC6aA&q=85&s=5b92a37e8279e08f267e21083f6797a2" alt="update-schema.png" width="982" height="535" data-path="images/datasets/scraper-studio/self-healing-tool/update-schema.png" />
    </Frame>

    > ***Expected result**: The refactored/fixed scraper is live and ready to collect data with the new configuration.*
  </Step>
</Steps>

## Troubleshooting

| Problem                                 | Likely Cause                  | Resolution                                                                      |
| --------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------- |
| AI-generated code doesn't fix the issue | Prompt was too vague          | Re-prompt with more specific field names or error descriptions                  |
| Preview still returns undefined values  | Target site structure changed | Inspect the live page and include the expected HTML element hint in your prompt |
| Changes not reflected after accepting   | Browser cache issue           | Refresh the IDE and re-check Development mode                                   |

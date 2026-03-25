# Source: https://docs.linkup.so/pages/documentation/tutorials/linkedin-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Find LinkedIn Profiles

> A practical guide to quickly locate official LinkedIn home‑page URLs for companies or people

This tutorial will show you how to build find the LinkedIn profile of a company or an individual using Linkup.

## What We'll Build

This tutorial will show you how to build find the LinkedIn profile of a company or an individual using Linkup.

* **Input**: Any text prompt that describes the profile you're after (company, school, person, etc.).
* **Process**:
  1. Send the prompt to the **Linkup API** with `depth="standard"`.
  2. Ask for **sourcedAnswer** output so we can inspect citations.
  3. Decide whether we're ≥ 99 % sure.
* **Output**: A single LinkedIn URL or `undefined`.

This pattern is perfect for enriching CRMs, onboarding forms, or internal tools where you need fast links with a very low false‑positive rate.

## How To Build

<Steps>
  <Step title="Install the SDK">
    <CodeGroup>
      ```python python theme={null}
      pip install linkup-sdk
      ```

      ```javascript js theme={null}
      npm i linkup-sdk
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up the Client">
    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
      ```

      ```javascript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: '<YOUR_LINKUP_API_KEY>',
      });
      ```
    </CodeGroup>

    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Make the API Call">
    <CodeGroup>
      ```python python theme={null}
      # 🔎  Example
      response = client.search(
          query="Please locate the official LinkedIn page for Linkup (their website is linkup.so).\nReturn only the LinkedIn home‑page URL.\nIf you're not at least 99 % sure the link is accurate, answer with undefined.",
          depth="standard",          # fast yet accurate
          output_type="sourcedAnswer",
          include_images=False,
      )
      print(response.answer)  # either the URL or 'undefined'
      ```

      ```javascript js theme={null}
      // 🔎  Example
      const response = await client.search({
        query: `Please locate the official LinkedIn page for Linkup (their website is linkup.so).
        Return only the LinkedIn home‑page URL.
        If you're not at least 99 % sure the link is accurate, answer with undefined.`,
        depth: 'standard', // fast yet accurate
        outputType: 'sourcedAnswer',
        includeImages: false,
      });
      console.log(response.answer); // either the URL or 'undefined'
      ```
    </CodeGroup>
  </Step>

  <Step title="Craft Better Prompts">
    For best accuracy, include **at least two unique signals**:

    | ✅ Good signal         | 📝 Example                         |
    | --------------------- | ---------------------------------- |
    | Official domain       | "(their website is acme.com)"      |
    | City or region        | "based in Berlin, Germany"         |
    | Stock ticker          | "listed on NASDAQ : ACME"          |
    | Unique slogan/tagline | "company slogan 'Think tangerine'" |

    > **Tip:** Keep the "Return only the LinkedIn home‑page URL…" and the 99 % clause; it gives the model explicit, measurable instructions.
  </Step>

  <Step title="Batch Lookup">
    Need to process a list of companies? Here's a tiny batch helper:

    <CodeGroup>
      ```python python theme={null}
      companies = [
          ("Stripe", "stripe.com"),
          ("Intercom", "intercom.com"),
          ("Monzo", "monzo.com"),
      ]

      for name, domain in companies:
          q = (
              f"Locate the official LinkedIn page for {name} (their website is {domain}). "
              "Return only the LinkedIn home‑page URL. If you're not at least 99 % sure, answer with undefined."
          )
          response = client.search(
              query=q,
              depth="standard",
              output_type="sourcedAnswer",
              include_images=False,
          )
          print(name, "→", response.answer)
      ```

      ```javascript js theme={null}
      const companies = [
        ['Stripe', 'stripe.com'],
        ['Intercom', 'intercom.com'],
        ['Monzo', 'monzo.com'],
      ];

      for (const [name, domain] of companies) {
        const q = `Locate the official LinkedIn page for ${name} (their website is ${domain}). ` +
                  `Return only the LinkedIn home‑page URL. If you're not at least 99 % sure, answer with undefined.`;
        const response = await client.search({
          query: q,
          depth: 'standard',
          outputType: 'sourcedAnswer',
          includeImages: false,
        });
        console.log(name, '→', response.answer);
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Advanced Enhancements

* **Fallback to Deep Search**: Retry with `depth="deep"` when standard depth yields `undefined`.
* **Multiple Entities**: Adjust the prompt to return an *array* of URLs when searching generic terms like "Acme Inc".
* **Integrate with CRMs**: Enrich company records automatically, then store URL + confidence + timestamp.
* **Rate Limiting**: Use `asyncio` / `Promise.allSettled` with a limiter when batch‑processing thousands.

## Conclusion

With fewer than 20 lines of code you now have a **LinkedIn‑URL resolver** that's fast, accurate, and completely configurable. Plug it into sign‑up flows, prospecting pipelines, or internal dashboards—and never copy‑paste a LinkedIn link again.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.mage.ai/development/updating-mage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating Mage

> How to get the latest and greatest from the Mage team.

<AccordionGroup>
  <Accordion title="Docker" icon="Docker">
    ```bash  theme={"system"}
    docker pull mageai/mageai:latest
    ```

    <Check>
      1. Are you a technologist? *Yes, you are from the future*
      2. Do you live on the edge of the galaxy? *Yes you do Sith Lord of the Empire*

      If you said `Yes`, `No`, or didn’t reply to any of these,
      you should download the `alpha` build instead:

      ```bash  theme={"system"}
      docker pull mageai/mageai:alpha
      ```
    </Check>
  </Accordion>

  <Accordion title="pip/conda" icon="python">
    <CodeGroup>
      ```bash pip theme={"system"}
      pip install -U mage-ai
      ```

      ```bash conda theme={"system"}
      conda update mage-ai
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).
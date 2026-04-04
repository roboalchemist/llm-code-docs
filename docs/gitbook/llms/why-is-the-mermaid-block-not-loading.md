# Source: https://gitbook.com/docs/help-center/integrations/integrations-troubleshooting/why-is-the-mermaid-block-not-loading.md

# Why is the Mermaid block not loading?

Mermaid lets you create diagrams and visualizations using text and code. Learning Mermaid's syntax should not be a problem if you are already familiar with Markdown.

If you are struggling to load your Mermaid diagram, we recommend following these troubleshooting steps:

### Ensure the Mermaid integration is installed in your organization and enabled for your space

To ensure Mermaid is displayed correctly in your space, it is essential to confirm that the Mermaid integration is correctly installed in your organization and enabled in your specific space. This is a critical step because, without integration, Mermaid diagrams will not render.

1. Go to your **organization's settings.**
2. Click on the **integrations** section
3. Find Mermaid on the list of available integrations
4. If the integration is not already installed, please install it by following the instructions, which will appear on the screen.
5. If the integration is already installed, ensure it has been enabled in your space by clicking Configure and then Manage Spaces.

### **Ensure your Mermaid code is correctly formatted.**

Incorrect syntax or formatting errors in your Mermaid code can prevent your diagram from loading correctly.

1. Please carefully review your Mermaid code.
2. Compare your syntax with examples in the Mermaid documentation to ensure it is correct.
3. Use a Mermaid live editor to test your code before embedding it into GitBook.

### Ensure that you are using a Mermaid block (and not a code block)

Mermaid blocks and code blocks have different functions in the GitBook editor. Your Mermaid code will not render if pasted into our standard code block.&#x20;

To add a Mermaid block, hit the `/` key and select the **Mermaid diagram** block

<figure><img src="https://content.gitbook.com/content/Ua3kTfM3iWAoECzM0u90/blobs/tLjFPntA6jpnubSonf1x/image.png" alt=""><figcaption><p>Mermaid block selection in the GitBook editor</p></figcaption></figure>

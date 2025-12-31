# Source: https://dev.writer.com/no-code/introduction.md

# Source: https://dev.writer.com/home/introduction.md

# Source: https://dev.writer.com/framework/introduction.md

# Source: https://dev.writer.com/no-code/introduction.md

# Source: https://dev.writer.com/home/introduction.md

# Source: https://dev.writer.com/framework/introduction.md

# Source: https://dev.writer.com/no-code/introduction.md

# Source: https://dev.writer.com/home/introduction.md

# Source: https://dev.writer.com/framework/introduction.md

# Source: https://dev.writer.com/no-code/introduction.md

# Source: https://dev.writer.com/home/introduction.md

# Source: https://dev.writer.com/framework/introduction.md

# Writer Framework

The Writer Framework lets you build feature-rich apps by using a drag-and-drop visual editor called **the Builder** and writing the back-end code in Python. It's fast and flexible, with clean, easy-to-test syntax. It provides separation of concerns between UI and business logic, enabling more complex apps.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9ad9be8f3da7b87fca947402b68986b7" alt="Framework Builder screenshot" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="framework/public/builder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=77bad05f5c56eab560a011477d04f5f1 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e8f39be618c1774bea7784ac483ba770 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=b3f9e5150fb2a181b8faa4dd5fedd555 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=682fe8d8c2d5035b6b9c2b1f2fc3d53b 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=741f7e0a41b473e3653991a7ac23cd56 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/builder.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=766af15e70dd4f8a6045662b7957d17c 2500w" />

Build AI apps with the Writer Framework when:

1. You need to incorporate external data sources, such as external APIs
2. You have complex user input that requires custom logic, such as conditions that trigger the use of different prompts
3. You want to quickly analyze and visualize data using an LLM

The Writer Framework offers:

<AccordionGroup>
  <Accordion title="Easily-testable Python functions">
    Define event handlers as plain Python functions.

    ```python  theme={null}
    def handle_text_update(state):
        state["text"] = "Updated text"

    writer.init_state({
        "text": "Initial text"
    })
    ```
  </Accordion>

  <Accordion title="Visual editor">
    Link the event handler and state to the UI seamlessly.
  </Accordion>

  <Accordion title="Standard Python packages">
    Install with a simple pip command.
  </Accordion>

  <Accordion title="Version control">
    Save user interfaces as JSON to be version controlled with the rest of the app.
  </Accordion>

  <Accordion title="Flexible editing">
    Use your local code editor with instant refreshes or the provided web-based editor. Edit the UI while your app is running without needing to click “Preview.”
  </Accordion>

  <Accordion title="Minimal overhead">
    Event handling adds only 1-2ms to your Python code.
  </Accordion>

  <Accordion title="Real-time synchronization">
    Use WebSockets to synchronize front-end and back-end states.
  </Accordion>

  <Accordion title="Efficient execution">
    Non-blocking by default, with asynchronous event handling in a dedicated thread pool.
  </Accordion>

  <Accordion title="Customizable elements">
    No CSS required for customization like shadows, button icons, and background colors.
  </Accordion>

  <Accordion title="HTML integration">
    Include HTML elements with custom CSS using the HTML Element component, which can serve as containers for built-in components.
  </Accordion>
</AccordionGroup>

To get started, head to [Quickstart](/framework/quickstart) or our tutorials:

<CardGroup cols={3}>
  <Card title="Social post generator" icon="megaphone" href="/framework/social-post-generator" color="currentColor">
    Generate multiple social media posts in a click of button using our social media generator.
  </Card>

  <Card title="Chat assistant" icon="comment" href="/framework/chat-assistant" color="currentColor">
    Using Knowledge Graph, our graph-based RAG solution, you can build chat assistants to quickly ask questions using your data sources.
  </Card>

  <Card title="Product description generator" icon="page" href="/framework/product-description-generator" color="currentColor">
    Build real-time digital shelves for hundreds of products that are automatically customized for different e-retailers.
  </Card>
</CardGroup>

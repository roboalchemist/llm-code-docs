# Source: https://developers.webflow.com/code-components/faqs.mdx

***

title: FAQs and troubleshooting
slug: faqs
description: Frequently asked questions about code components
hidden: false
subtitle: Common questions and solutions for code components
canonical-url: '[https://developers.webflow.com/code-components/faqs](https://developers.webflow.com/code-components/faqs)'
---------------------------------------------------------------------------------------------------------------------------

Find answers to common questions about code components, from setup to troubleshooting.

## Getting started

<Accordion title="How do I create my first code component?">
  <Steps>
    <Step title="Install the Webflow CLI and dependencies">
      ```bash
      npm i --save-dev @webflow/webflow-cli @webflow/react @webflow/data-types
      ```

      <Note title="Install the Webflow CLI locally">
        Install the Webflow CLI locally to your project to use the `npx webflow library share` command.
      </Note>
    </Step>

    <Step title="Declare your Webflow component">
      [Declare your code component](/code-components/define-code-component) to map your React component to Webflow
    </Step>

    <Step title="Import">
      ```bash
      npx webflow library share
      ```
    </Step>
  </Steps>

  See the [getting started guide](/code-components/introduction/quick-start) for detailed steps.
</Accordion>

<Accordion title="Which frameworks can I use?">
  Imported components support React with TypeScript. You can use:

  * React hooks and functional components
  * TypeScript for type safety
  * Popular React libraries (with some limitations)
  * CSS-in-JS solutions (with configuration)
</Accordion>

<Accordion title="How many components can I share in a library?">
  There's no strict limit on the number of components per library, but keep your bundle size under 50MB for optimal performance.
</Accordion>

## Development and styling

<Accordion title="Why can't I see my component styles?">
  Code components render in Shadow DOM, which isolates styles. Common issues:

  * **Site classes don't work** - Use component-specific CSS classes
  * **CSS-in-JS libraries need configuration** - See [bundling guide](/code-components/bundling-and-import)
</Accordion>

<Accordion title="How do I use my site variables?">
  Reference site variables in your component CSS:

  ```css
  .my-component {
    color: var(--background-primary, #000);
  }
  ```

  Get the exact variable name from the Variables panel in Webflow Designer.
</Accordion>

<Accordion title="Can I use external APIs in my components?">
  Yes, but with important limitations:

  * **Client-side requests only** - All API requests are executed in the browser
  * **Public APIs only** - Don't include auth tokens or secrets
  * **CORS considerations** - APIs must allow cross-origin requests

  Example of safe API usage:

  ```tsx
  useEffect(() => {
    fetch('/api/public-data')
      .then(response => response.json())
      .then(setData);
  }, []);
  ```
</Accordion>

## Imports and updates

<Accordion title="How do I update a component in my library?">
  1. Make your changes locally
  2. Run `npx webflow library share` to deploy
  3. The updated component replaces the previous version

  **Note:** You can't update individual components - the entire library is deployed as one unit.
</Accordion>

<Accordion title="Can I test components locally before importing?">
  Yes, use the local bundling feature:

  ```bash
  npx webflow library bundle --public-path http://localhost:4000/ --dev
  ```

  This creates a `dist` folder you can serve locally for testing.
</Accordion>

<Accordion title="How do I handle component versioning?">
  Currently, code components don't support versioning. Each import replaces the previous version. Consider:

  * Using Git for version control
  * Testing thoroughly before import
  * Keeping import logs for rollback reference
</Accordion>

## Troubleshooting

<Accordion title="My component isn't rendering">
  Check these common issues:

  1. **Build errors** - Check your terminal for compilation errors
  2. **Missing dependencies** - Ensure all imports are available
  3. **Bundle size** - Keep under 50MB limit
  4. **Single root element** - Components must have one root element (no fragments)
</Accordion>

<Accordion title="Styles aren't applying correctly">
  Shadow DOM limitations can cause styling issues:

  * **Site classes** - Use component-specific classes instead
  * **CSS-in-JS** - Configure for Shadow DOM (see [bundling guide](/code-components/bundling-and-import))
  * **Inheritance** - Use `inherit` values for cross-boundary styling
</Accordion>

<Accordion title="Component state isn't persisting">
  Each code component runs in its own React root, so:

  * **React Context doesn't work** across components
  * **Redux/global state** isn't shared between components
  * **Use alternatives** like URL parameters, `localStorage`, or external state management

  Learn more about [component architecture](/code-components/component-architecture) and [state management](/code-components/component-architecture#state-management) when building React components for import into Webflow.
</Accordion>

<Accordion title="Library import fails">
  Common import issues:

  * **Authentication** - Ensure your Workspace token is valid in your `.env` file
  * **Bundle size** - Check if you're under the 50MB limit
  * **Build errors** - Fix any compilation issues first
  * **Network issues** - Check your internet connection
</Accordion>

## Performance and limitations

<Accordion title="What's the bundle size limit?">
  Maximum bundle size is 50MB. To optimize:

  * Use tree shaking
  * Minimize dependencies
  * Remove unused code
  * Optimize images and assets
</Accordion>

<Accordion title="How do I share state between components?">
  Since each component has its own React root, use:

  * **URL parameters** for simple state
  * **`localStorage`/`sessionStorage`** for persistent data
  * **External state management** libraries compatible with isolated roots
  * **Custom events** for component communication

  Learn more about [component architecture](/code-components/component-architecture) and [state management](/code-components/component-architecture#state-management) when building React components for import into Webflow.
</Accordion>

<Accordion title="Can I use third-party libraries?">
  Most React libraries work, but some have limitations:

  * **Multiple entry points** - Libraries with ESM + CJS may not work
  * **Style injection** - CSS-in-JS libraries need Shadow DOM configuration
  * **Global dependencies** - Libraries that modify `window` or `document` may conflict

  Learn more about [styling components](/code-components/styling-components) when building React components for import into Webflow.
</Accordion>

## Advanced topics

<Accordion title="How do I debug my components?">
  1. **Browser developer tools** - Inspect the Shadow DOM
  2. **Console logging** - Add `console.log` statements
  3. **Local bundling** - Use `--dev` flag for better error messages
  4. **Source maps** - Enable for easier debugging
</Accordion>

<Accordion title="Can I use TypeScript?">
  Yes, TypeScript is fully supported. Use `.tsx` files for your components and configure `tsconfig.json` for your project.
</Accordion>

<Accordion title="How do I handle responsive design?">
  Use standard CSS media queries within your component:

  ```css
  .my-component {
    width: 100%;
  }

  @media (min-width: 768px) {
    .my-component {
      width: 50%;
    }
  }
  ```
</Accordion>

<Accordion title="Can I use animations and transitions?">
  Yes, CSS animations and transitions work normally within the Shadow DOM boundary. Use standard CSS animation properties and `@keyframes`.
</Accordion>

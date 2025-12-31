# Source: https://mintlify.com/docs/components/tiles.md

# Tiles

> Display visual previews with titles and descriptions in a grid layout.

Use tiles to create visual showcase elements with a patterned background, title, and description. Tiles are ideal for displaying component previews, feature highlights, or navigation items in a grid layout.

<Tile href="/components/accordions" title="Accordion" description="Two variants">
  <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=17321f69398df3418c75ab1cf5b87471" alt="Accordion component preview" className="block dark:hidden" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-light.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=3030fc2ea71a74c175c39b4d9de97344 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=b84dd3e40ed00c752382e2b92ba470ea 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=46761268bbe6ccc822ead12d3c568d09 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=30ce55ea79d2e7f4bf4edebc2a7c2ebf 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8f4d3ecc8c8698652762f483afec953e 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=dc9e8c4184756cf3c342a9e987abbb77 2500w" />

  <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8257dfcdda4630dd41f4a69d60063f53" alt="Accordion component preview (dark mode)" className="hidden dark:block" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=74b6315a7278cbe217cbf39dbf68a2d3 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=06689063fcd2049dcff35d41721f000e 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=893a0cf3725775ce4359b3698feed766 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=de9131cc8e187f3ff3c2d7c0618b83e4 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=e0df364488bb0980515cb9d0bd659d6c 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=685ea3999b55d0a234a4638fcf3d29b5 2500w" />
</Tile>

```mdx Tile example theme={null}
<Tile href="/components/accordions" title="Accordion" description="Two variants">
  <img src="/images/tiles/accordion-light.svg" alt="Accordion component preview" className="block dark:hidden" />
  <img src="/images/tiles/accordion-dark.svg" alt="Accordion component preview (dark mode)" className="hidden dark:block" />
</Tile>
```

## Grid layout

Combine tiles with the [columns component](/components/columns) to create a responsive grid of visual previews.

<Columns cols={3}>
  <Tile href="/components/accordions" title="Accordion" description="Two variants">
    <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=17321f69398df3418c75ab1cf5b87471" alt="Accordion component preview" className="block dark:hidden" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-light.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=3030fc2ea71a74c175c39b4d9de97344 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=b84dd3e40ed00c752382e2b92ba470ea 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=46761268bbe6ccc822ead12d3c568d09 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=30ce55ea79d2e7f4bf4edebc2a7c2ebf 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8f4d3ecc8c8698652762f483afec953e 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=dc9e8c4184756cf3c342a9e987abbb77 2500w" />

    <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8257dfcdda4630dd41f4a69d60063f53" alt="Accordion component preview (dark mode)" className="hidden dark:block" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=74b6315a7278cbe217cbf39dbf68a2d3 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=06689063fcd2049dcff35d41721f000e 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=893a0cf3725775ce4359b3698feed766 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=de9131cc8e187f3ff3c2d7c0618b83e4 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=e0df364488bb0980515cb9d0bd659d6c 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=685ea3999b55d0a234a4638fcf3d29b5 2500w" />
  </Tile>

  <Tile href="/components/accordions" title="Accordion" description="Two variants">
    <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=17321f69398df3418c75ab1cf5b87471" alt="Accordion component preview" className="block dark:hidden" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-light.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=3030fc2ea71a74c175c39b4d9de97344 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=b84dd3e40ed00c752382e2b92ba470ea 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=46761268bbe6ccc822ead12d3c568d09 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=30ce55ea79d2e7f4bf4edebc2a7c2ebf 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8f4d3ecc8c8698652762f483afec953e 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=dc9e8c4184756cf3c342a9e987abbb77 2500w" />

    <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8257dfcdda4630dd41f4a69d60063f53" alt="Accordion component preview (dark mode)" className="hidden dark:block" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=74b6315a7278cbe217cbf39dbf68a2d3 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=06689063fcd2049dcff35d41721f000e 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=893a0cf3725775ce4359b3698feed766 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=de9131cc8e187f3ff3c2d7c0618b83e4 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=e0df364488bb0980515cb9d0bd659d6c 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=685ea3999b55d0a234a4638fcf3d29b5 2500w" />
  </Tile>

  <Tile href="/components/accordions" title="Accordion" description="Two variants">
    <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=17321f69398df3418c75ab1cf5b87471" alt="Accordion component preview" className="block dark:hidden" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-light.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=3030fc2ea71a74c175c39b4d9de97344 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=b84dd3e40ed00c752382e2b92ba470ea 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=46761268bbe6ccc822ead12d3c568d09 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=30ce55ea79d2e7f4bf4edebc2a7c2ebf 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8f4d3ecc8c8698652762f483afec953e 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-light.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=dc9e8c4184756cf3c342a9e987abbb77 2500w" />

    <img src="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=8257dfcdda4630dd41f4a69d60063f53" alt="Accordion component preview (dark mode)" className="hidden dark:block" data-og-width="184" width="184" data-og-height="100" height="100" data-path="images/tiles/accordion-dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=280&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=74b6315a7278cbe217cbf39dbf68a2d3 280w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=560&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=06689063fcd2049dcff35d41721f000e 560w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=840&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=893a0cf3725775ce4359b3698feed766 840w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1100&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=de9131cc8e187f3ff3c2d7c0618b83e4 1100w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=1650&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=e0df364488bb0980515cb9d0bd659d6c 1650w, https://mintcdn.com/mintlify/5zb00FEo6Z8cj3rs/images/tiles/accordion-dark.svg?w=2500&fit=max&auto=format&n=5zb00FEo6Z8cj3rs&q=85&s=685ea3999b55d0a234a4638fcf3d29b5 2500w" />
  </Tile>
</Columns>

```mdx Grid layout example theme={null}
<Columns cols={3}>
  <Tile href="/components/accordions" title="Accordion" description="Two variants">
    <img src="/images/tiles/accordion-light.svg" alt="Accordion component preview" className="block dark:hidden" />
    <img src="/images/tiles/accordion-dark.svg" alt="Accordion component preview (dark mode)" className="hidden dark:block" />
  </Tile>
  <Tile href="/components/accordions" title="Accordion" description="Two variants">
    <img src="/images/tiles/accordion-light.svg" alt="Accordion component preview" className="block dark:hidden" />
    <img src="/images/tiles/accordion-dark.svg" alt="Accordion component preview (dark mode)" className="hidden dark:block" />
  </Tile>
  <Tile href="/components/accordions" title="Accordion" description="Two variants">
    <img src="/images/tiles/accordion-light.svg" alt="Accordion component preview" className="block dark:hidden" />
    <img src="/images/tiles/accordion-dark.svg" alt="Accordion component preview (dark mode)" className="hidden dark:block" />
  </Tile>
</Columns>
```

## Properties

<ResponseField name="href" type="string" required>
  URL to navigate to when the tile is clicked.
</ResponseField>

<ResponseField name="title" type="string">
  The title displayed below the tile preview.
</ResponseField>

<ResponseField name="description" type="string">
  A short description displayed below the title.
</ResponseField>

<ResponseField name="children" type="React.ReactNode" required>
  Content displayed inside the tile preview area, typically images or SVGs.
</ResponseField>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://mintlify.com/docs/llms.txt
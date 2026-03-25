# Source: https://vueform.com/news/20260108-announcing-vueform-2-0

Title: Announcing Vueform 2.0

URL Source: https://vueform.com/news/20260108-announcing-vueform-2-0

Markdown Content:
08 January, 2026

[![Image 1](https://vueform.com/images/adam-berecz.webp) Adam Berecz github.com/adamberecz](https://github.com/adamberecz)
Today I’d like to share an early look at the next major version of Vueform.

Vueform 2.0 is a ground-up rethinking of how form frameworks should integrate into modern Vue applications. It is not a replacement for Vueform 1, but a parallel effort aimed at addressing long-standing limitations, informed directly by real-world usage and community feedback.

This post explains why Vueform 2 exists, what problems it aims to solve, and what you can expect over the coming year.

A look back at 2025 [​](https://vueform.com/news/20260108-announcing-vueform-2-0#a-look-back-at-2025)
-----------------------------------------------------------------------------------------------------

2025 turned out to be a defining year for Vueform.

In March, I had the opportunity to introduce Vueform [live on stage](https://www.youtube.com/live/fB3j5cQyOB8?t=27639s) in front of over 1,000 developers at [Vue.js Amsterdam](https://vuejs.amsterdam/) – the largest Vue.js conference in the world. Over the course of the year, I also presented Vueform at several meetups and conferences including [MadVue](https://madvue.es/), [PragVue](https://pragvue.com/) and [ZurichJS](https://zurichjs.com/).

More important than the talks themselves were the conversations around them.

I had long, honest discussions with developers who were using Vueform in production, as well as those who had chosen other solutions. We talked about what worked well, what felt limiting, and what started to break down at scale. These conversations continued online through GitHub issues, discussions, and direct messages.

**Taken together, this feedback made one thing clear: many of the improvements people were asking for could not be delivered incrementally without rethinking some of the core assumptions of Vueform.**

That realization led to the decision to start Vueform 2.0.

Why Vueform 2? [​](https://vueform.com/news/20260108-announcing-vueform-2-0#why-vueform-2)
------------------------------------------------------------------------------------------

Today, form tooling in the Vue ecosystem largely falls into two categories.

The first is the “monolithic” approach: full form frameworks that ship their own component libraries along with validation, data handling, conditional logic, steps, and submission workflows in a single opinionated package. Vueform and FormKit are examples of this approach.

The second is the “modular” approach: smaller, focused tools that integrate into an existing setup and handle specific concerns like validation or state management. VeeValidate and Vuelidate fall into this category.

Both approaches have clear strengths and tradeoffs.

Monolithic frameworks are convenient and powerful, but they often require adopting an entire component system. This can feel restrictive if you already use a UI library or have a mature design system. Modular solutions offer much more freedom, but that freedom comes with added wiring, duplication, and long-term maintenance costs.

Vueform 2 is an attempt to combine the strengths of both.

**Instead of shipping a fixed component library, Vueform 2 is designed as a framework for building form frameworks. It provides a headless core that handles data, validation, conditions, expressions, and structure, while allowing UI libraries to plug in naturally.**

The goal is simple: Vueform should adapt to your component system, not the other way around.

Architectural overview [​](https://vueform.com/news/20260108-announcing-vueform-2-0#architectural-overview)
-----------------------------------------------------------------------------------------------------------

### Headless core with UI library integrations [​](https://vueform.com/news/20260108-announcing-vueform-2-0#headless-core-with-ui-library-integrations)

Most Vue projects today rely on a UI library. Vueform 2 embraces that reality.

Rather than asking you to restyle Vueform components to match your design system, Vueform 2 will provide official integrations for major UI libraries. For example, instead of installing Vueform and PrimeVue separately, you’ll be able to install `@vueform/primevue` and get form elements rendered using PrimeVue components directly.

Vueform still adds its own thin layer for layout, structure, containers, lists, and advanced behaviors, but core inputs like text fields, selects, or checkboxes will come from your chosen UI library. This means you get native styling, existing theming, and full access to both Vueform features and the underlying component API.

In addition to UI integrations, Vueform 2 will ship with a headless HTML-based setup and a set of optional advanced elements such as phone inputs, signatures, and captchas. These can be used with any design system on demand.

### TypeScript as a first-class feature [​](https://vueform.com/news/20260108-announcing-vueform-2-0#typescript-as-a-first-class-feature)

Vueform 2 is written entirely in TypeScript, and TypeScript support goes far beyond basic prop typing.

*   All public APIs are fully typed, including component props, events, slots, and element instance methods
*   Core APIs use generics instead of broad types, enabling precise inference
*   Schema-driven forms provide typed access paths to elements
*   Element instances retrieved via `ref` or `el$()` expose strongly typed APIs

For example, accessing `form$.el$('list.0.birthday')` can return a properly typed date element instance, with full method and event type support.

Complex schemas can be defined using helpers like `defineSchema()`, which provide autocomplete for element types even in deeply nested structures. Event callbacks receive fully typed element instances, making API exploration faster and reducing the need to constantly reference documentation.

TypeScript in Vueform 2 is meant to actively guide development, not just validate it.

### Dependencies and bundle size [​](https://vueform.com/news/20260108-announcing-vueform-2-0#dependencies-and-bundle-size)

Vueform 2 significantly reduces its dependency footprint.

Large dependencies such as lodash are removed entirely. Others, like HTTP and date handling, are optional and loaded only when needed. As part of this effort, existing dependencies are being revisited and updated where better alternatives exist, such as replacing Moment with date-fns.

The core will be available as a minimal bundle, with optional services and element packs layered on top. This allows applications to include only what they actually use.

### SSR support [​](https://vueform.com/news/20260108-announcing-vueform-2-0#ssr-support)

Vueform 2 is designed with server-side rendering in mind from the start.

The core avoids browser-only assumptions, supports deterministic rendering, and is compatible with modern SSR setups such as Nuxt. This applies equally to headless usage and UI library integrations.

### Performance at scale [​](https://vueform.com/news/20260108-announcing-vueform-2-0#performance-at-scale)

Vueform 1 performs well for small and medium forms, but real-world usage has shown that large enterprise forms often go far beyond that – dozens of steps and even thousands of elements.

Supporting those cases required architectural changes that could not be backported.

#### Fewer components [​](https://vueform.com/news/20260108-announcing-vueform-2-0#fewer-components)

Vueform 1 relied heavily on small, composable components for labels, descriptions, hints, and layout. While intuitive, this resulted in significant overhead when rendering large forms.

Vueform 2 reduces component depth, especially in hot paths like element layout, to minimize rendering cost and memory usage.

#### Fewer computed values [​](https://vueform.com/news/20260108-announcing-vueform-2-0#fewer-computed-values)

Computed properties are powerful, but they come with memory and tracking overhead. Vueform 2 minimizes computed usage where possible, favoring direct refs, unwrapped values, and targeted reactivity.

#### Virtualized pages [​](https://vueform.com/news/20260108-announcing-vueform-2-0#virtualized-pages)

In multi-step or tabbed forms, only the currently active page is rendered. All other elements exist purely at the data level until needed. This drastically reduces initial render time and memory usage for large forms.

Benchmarks will be shared closer to release.

Feature-level improvements [​](https://vueform.com/news/20260108-announcing-vueform-2-0#feature-level-improvements)
-------------------------------------------------------------------------------------------------------------------

### A new data engine [​](https://vueform.com/news/20260108-announcing-vueform-2-0#a-new-data-engine)

Vueform 1 uses a top-down data flow, where each element owns its value and parents aggregate state through child refs. This guarantees consistency but becomes expensive in deeply nested structures.

Vueform 2 switches to a bottom-up model. A single data repository lives at the highest relevant level, and elements write directly into it. This minimizes recomputation and avoids unnecessary updates to unrelated parts of the tree.

### Standalone elements [​](https://vueform.com/news/20260108-announcing-vueform-2-0#standalone-elements)

Elements in Vueform 2 can be used without a wrapping form.

This makes it possible to reuse Vueform inputs in parts of your UI where you don’t need validation, conditions, or submission logic. Elements support v-model where applicable, making standalone usage feel natural and lightweight.

### A simpler class system [​](https://vueform.com/news/20260108-announcing-vueform-2-0#a-simpler-class-system)

The existing class engine is powerful but difficult to reason about. Vueform 2 replaces it with a system that mirrors standard Vue class bindings.

Classes are defined using reactive objects and arrays, with conditional logic expressed directly where it belongs. Overrides and extensions use a single, consistent API instead of multiple specialized helpers.

Class keys are fully typed, so editors can provide autocomplete and validation when customizing styles.

Ecosystem and tooling [​](https://vueform.com/news/20260108-announcing-vueform-2-0#ecosystem-and-tooling)
---------------------------------------------------------------------------------------------------------

### Schema-based integrations [​](https://vueform.com/news/20260108-announcing-vueform-2-0#schema-based-integrations)

Support for rendering forms from JSON Schema, Zod, or similar formats is planned after the initial release, once the core architecture is stable.

### Debugging tools [​](https://vueform.com/news/20260108-announcing-vueform-2-0#debugging-tools)

A dedicated Vue Devtools extension is planned to help inspect form state, data flow, and validation more easily, especially in complex forms.

Vueform 2 is an opportunity to make the project more open to contributions. The contribution process will be documented more clearly, with better development tooling and guidance for contributors.

Planned timeline [​](https://vueform.com/news/20260108-announcing-vueform-2-0#planned-timeline)
-----------------------------------------------------------------------------------------------

*   **2026 Q2** – Alpha release with headless UI and one UI library integration
*   **2026 Q3** – Beta phase, expanding UI library support
*   **2026 Q4** – Stable release

Q&A [​](https://vueform.com/news/20260108-announcing-vueform-2-0#q-a)
---------------------------------------------------------------------

### Does this affect Vueform 1 or Vueform Builder? [​](https://vueform.com/news/20260108-announcing-vueform-2-0#does-this-affect-vueform-1-or-vueform-builder)

No. Vueform 2 is a separate codebase. Vueform 1 and Vueform Builder will continue to receive updates and support, with no announced end-of-life.

### Will there be a migration path? [​](https://vueform.com/news/20260108-announcing-vueform-2-0#will-there-be-a-migration-path)

Yes. A migration guide will be provided once Vueform 2 stabilizes.

### Will there be a Vueform Builder 2? [​](https://vueform.com/news/20260108-announcing-vueform-2-0#will-there-be-a-vueform-builder-2)

Yes, but later. The priority is to release Vueform 2 as a stable foundation with solid UI library support. Vueform Builder 2 will be announced separately once that milestone is reached.

Questions and feedback [​](https://vueform.com/news/20260108-announcing-vueform-2-0#questions-and-feedback)
-----------------------------------------------------------------------------------------------------------

If you have ideas, questions, or concerns, feel free to join the discussion on [GitHub](https://github.com/vueform/vueform/discussions/505) or email me directly at **[adam@vueform.com](mailto:adam@vueform.com)**.

More updates soon.

[![Image 2](https://vueform.com/images/adam-berecz.webp) Adam Berecz github.com/adamberecz](https://github.com/adamberecz)

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)

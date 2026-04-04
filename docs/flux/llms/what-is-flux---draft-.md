# Source: https://docs.flux.ai/Introduction/what-is-flux---draft-.md

# What is Flux Editor? A Modern Browser-Based PCB Design Tool


Go 10x faster from idea to PCB by reducing busy work, never starting from scratch, and keeping your team in sync.




Flux Editor is a fully browser-based tool, so all you need to access the full development environment is a computer and an internet connection. This makes it easier than ever to build parts, projects, and ideas with others. Additionally, with Flux Editor's built-in version control, you can embrace the rapid development process without worrying about lost work.

## The Flux Method

Flux Editor is based on three core principles: promoting re-usability, fostering collaboration, and keeping you focused.

**Reusability can amplify the impact of individuals and organizations**. Leverage the work of others in the community by using templates, modules or example projects.

**Building hardware often requires collaboration** with teammates, clients, manufacturers, and other stakeholders. Flux Editor facilitates seamless, browser-based collaboration with controlled permissions and automated version control.

**Reducing distractions and repetitive tasks can keep you in the flow** and help you achieve better results. Flux Editor integrates key workflows into one app to keep you in the flow and reduce distractions. Including schematic and PCB editors, an AI assistant, and a built-in SPICE simulator.

Read our [Flux Method](https://docs.flux.ai/flux/Introduction/the-flux-method) page to learn more about how Flux Editor can improve your PCB design workflow.

## The Flux Model

Understand how Flux is set up so you can get started quickly.

### Basic Model


#### Projects

Projects are where all design work happens in Flux Editor. Projects bundle together a schematic and a PCB layout, along with all relevant files and information. There's also a place to write code, and chat with Flux, your AI assistant.

Projects have an owner – you, another user, or an organization. The owner controls who can edit, comment on, or view the project. Collaboration is easy: grant permissions for anyone on the internet, individuals, or members of an organization.

Basically everything in Flux Editor is a project. Components, modules, simulations, etc – at their core, they're just projects.


#### Components

Components serve as the primary building block for PCB designs. Generally, a component is a part – a resistor, capacitor, or integrated circuit (IC) with a manufacturer part number (MPN). This should feel familiar from other EDA tools, but there are some key differences.

- Components can contain many things. Remember, components are just projects. So they bundle together the schematic, symbols, footprints, and more into a single unit.
- There's lots of flexibility. For example, a component can contain an internal schematic _and_ a symbol.
- Functional blocks – like an entire buck converter – can be a component in Flux Editor we call a module.


#### Modules

Modules are kind of component that contain a complete section of a design, including components, traces, vias, etc. Some EDA tools call these sub-layouts, hierarchical designs, or functional blocks.

Modules can be placed into existing projects to reuse previous designs with minimal effort. This strategy of reuse will help you build things more quickly.

Learn more about modules in this [tutorial](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts).

{% image url="https://uploads.developerhub.io/prod/86Yw/jfmkgkdtq34d75yx1ufdi8tbkd7spu94iya5b4s4o0zfap3g7vh1fbqi0uqr9xci.png" mode="600" height="2054" width="600" %}
{% /image %}


#### Library

Flux Editor has a single, unified library of components. It contains hundreds of thousands of components, all made by the community. This removes the hassle of having to create your own components. Permissions govern who can see what, so it's easy to keep your personal or organization's sensitive components private – or to give back to the community.

In case you do need to create a component, just follow this [tutorial.](https://docs.flux.ai/flux/tutorials/tutorial-add-part-library)

{% image url="https://uploads.developerhub.io/prod/86Yw/ubvo4v3r33g9yesqe9o3lrwjn6gpda75rglzli5fv1ky1trxune96zb1zow8gqyr.png" mode="600" height="1499" width="600" %}
{% /image %}


#### Layout Rules

Layout rules configure your layout and routing tools. In fact, rules _drive_ the design. Unlike in legacy tools, which check to ensure your design adheres to manufacturability standards after it's completed, Flux Editor enforces layout rules automatically as they're created. That means less mistakes in the first place.

Most of the time, you won't need to get into rules. We've designed Flux Editor so you can accomplish almost everything from the canvas just by pointing and clicking. Rules get written for you when you do that. And when you're ready to go deeper, it's easy to edit the rules directly.

Learn to design with layout rules in this [tutorial.](https://docs.flux.ai/flux/tutorials/tutorial-layout-rules-deep-dive)

### AI Hardware Assistant – Flux

Flux is a natively integrated AI assistant. Think of it like a teammate who can speed you up, double check your work, and unlock more complex projects.

Flux knows your project deeply: the components, their datasheets, connections, prices, etc. So it can answer complex questions, brainstorm block diagrams, search the library, create connections, and more.

Under the hood, Flux uses cutting edge AI technology. Agentic, large language models (LLM) are trained by Flux to plan, coordinate tools, ingest context, and take action.

Read more about how Flux can improve your design process in this [tutorial.](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design)

{% image url="https://uploads.developerhub.io/prod/86Yw/ktnmeg2dqz7qgv24k1pd3ymns6bw2y71xcrhdtofml5zythfyq0bbrqgh1n75asz.png" mode="600" height="1787" width="600" %}
{% /image %}

## Best Practices for Getting Started with Flux

1. **Start with templates.** Use existing templates for common platforms like Arduino, ESP32, or Raspberry Pi.
2. **Leverage the community library.** Take advantage of pre-built components rather than creating everything from scratch.
3. **Use modules for common circuits.** Implement reusable modules for standard circuit blocks like power supplies or USB interfaces.
4. **Collaborate early and often**. Share your designs with teammates or the community for feedback throughout the process.
5. **Utilize Flux for assistance.** Ask the AI assistant for help with component selection, design reviews, and troubleshooting.

## Troubleshooting Common Issues

### Browser Compatibility

- Ensure you're using a supported browser (Chrome, Firefox, Edge).
- Clear your browser cache if you experience display issues.
- Check that your browser is up to date.

### Performance Concerns

- Close unnecessary browser tabs to free up memory.
- For complex designs, consider breaking them into modules.
- Use the object tree to hide layers or components not currently being worked on.

### Connectivity Problems

- Verify that your internet connection is stable.
- If you experience disconnections, Flux automatically saves your work.
- Use the version control system to recover any lost changes.

## Help and Tutorials

These are some tips for how to navigate our documentation page and access other resources:

- [First project in Flux](https://docs.flux.ai/flux/Introduction/flux-walkthrough-project) – The quickest way to jump into Flux and get started on a project.
- [Tutorials](https://docs.flux.ai/flux/tutorials/flux-tutorials) – In-depth tutorials about how to use Flux.
- [Reference](https://docs.flux.ai/flux/reference/api-overview) – Find detailed information about the elements of Flux.
- [YouTube](https://www.youtube.com/channel/UC5CsglCHQBd4-WFrZmqzVyw) – Video example projects and tutorials all in Flux.
- [Slack](https://join.slack.com/t/fluxcommunity/shared_invite/zt-2hi664box-TNSNJ_~nUkNHkxeULXkSog) – Join our community of engineers, contractors, and hobbyists using Flux.

## What's Next

Now that you understand what Flux is, you might want to explore:

- [The Flux Method](https://docs.flux.ai/flux/Introduction/the-flux-method)[https://join.slack.com/t/fluxcommunity/shared_invite/zt-2hi664box-TNSNJ_~nUkNHkxeULXkSog](https://join.slack.com/t/fluxcommunity/shared_invite/zt-2hi664box-TNSNJ_~nUkNHkxeULXkSog) – Learn more about Flux's design philosophy.
- [Creating an Account](https://docs.flux.ai/flux/Introduction/creating-an-account) – Get started with your own Flux account.
- [First Project in Flux](https://docs.flux.ai/flux/Introduction/flux-walkthrough-project) – Follow a step-by-step guide to create your first project.
- [Set Up Your Browser](https://docs.flux.ai/flux/Introduction/set-up-your-browser) – Optimize your browser for the best Flux experience.

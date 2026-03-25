# Source: https://unovis.dev/docs/intro

Title: Introduction | Unovis

URL Source: https://unovis.dev/docs/intro

Markdown Content:
👋 Welcome to Unovis[​](https://unovis.dev/docs/intro#-welcome-to-unovis "Direct link to 👋 Welcome to Unovis")
---------------------------------------------------------------------------------------------------------------

This documentation will help you to get comfortable with _Unovis_ — a modular and framework-independent library for charts, maps and network graphs.

🏗 Install[​](https://unovis.dev/docs/intro#-install "Direct link to 🏗 Install")
---------------------------------------------------------------------------------

Unovis is available on NPM in several packages, each for the UI framework of your choice (_React_, _Angular_, _Svelte_ or _Vue_). The core package `@unovis/ts` can be used without a UI framework, and if you use one you'll need to install `@unovis/ts` along with the framework specific package:

*   React
*   Angular
*   Svelte
*   Vue
*   Solid
*   TypeScript

`npm install -P @unovis/ts @unovis/react`

info

If you use TypeScript, you'll need to enable the [`allowSyntheticDefaultImports`](https://www.typescriptlang.org/tsconfig#allowSyntheticDefaultImports) option in the `compilerOptions` section of your `tsconfig.json`, because some of _Unovis_'s dependencies need it.

Also if you have [`types`](https://www.typescriptlang.org/tsconfig#types) specified in `tsconfig.json` explicitly, you might need to add `"topojson-client"` to the list. Otherwise, the TypeScript compiler won't find the required TopoJSON types.

🧑‍💻 Create your first chart[​](https://unovis.dev/docs/intro#-create-your-first-chart "Direct link to 🧑‍💻 Create your first chart")
---------------------------------------------------------------------------------------------------------------------------------------

Most of _Unovis_ components require a _Container_ to get rendered. There are two types of containers available:

*   [_XY Container_](https://unovis.dev/docs/containers/XY_Container). Designed to manage multiple _XY Components_ (e.g. [_Line_](https://unovis.dev/docs/xy-charts/Line), [_GroupedBar_](https://unovis.dev/docs/xy-charts/GroupedBar), [_Scatter_](https://unovis.dev/docs/xy-charts/Scatter), ...), along with optional [_Axes_](https://unovis.dev/docs/auxiliary/Axis), [_Tooltip_](https://unovis.dev/docs/auxiliary/Tooltip) and [_Crosshair_](https://unovis.dev/docs/auxiliary/Crosshair);

*   [_Single Container_](https://unovis.dev/docs/containers/Single_Container). Works only with a single components, like [_Graph_](https://unovis.dev/docs/networks-and-flows/Graph), [_Sankey_](https://unovis.dev/docs/networks-and-flows/Sankey), or [_TopoJSONMap_](https://unovis.dev/docs/maps/TopoJSONMap). It also supports [_Tooltip_](https://unovis.dev/docs/auxiliary/Tooltip).

Some of the components are stand-alone and don't need a container: [_LeafletMap_](https://unovis.dev/docs/maps/LeafletMap), [_LeafletFlowMap_](https://unovis.dev/docs/maps/LeafletFlowMap) and legends.

Go to the 👟 [Quick Start](https://unovis.dev/docs/quick-start) section to learn how to quickly build a simple Line Chart.

🔭 Explore the docs[​](https://unovis.dev/docs/intro#-explore-the-docs "Direct link to 🔭 Explore the docs")
------------------------------------------------------------------------------------------------------------

Pick a component from the sidebar to learn how to configure it. Start with 📈 [_Line_](https://unovis.dev/docs/xy-charts/Line) or 📊 [_Bar_](https://unovis.dev/docs/xy-charts/GroupedBar) if you want something simple. Don't forget to check out our 🖼 [Gallery](https://unovis.dev/gallery) to see what the library is capable of!

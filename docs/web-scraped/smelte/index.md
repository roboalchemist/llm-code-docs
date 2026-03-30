# Source: https://smeltejs.com/

Title: Material design using Tailwind CSS for Svelte

URL Source: https://smeltejs.com/

Markdown Content:
Hi
--

Smelte is a UI framework built on top of Svelte and [Tailwind CSS](https://tailwindcss.com/) using Material Design spec. It comes with many components and utility functions making it easy to build beautiful responsive layouts while keeping bundle size and performance at check all thanks to Svelte. The project was initially inspired by [Vuetify,](https://vuetifyjs.com/) but comes at much lower price. The website you're viewing is only a fraction of both JS (670 vs 40 Kb) and CSS (110 vs 10 Kb) payloads of even the most [basic Vuetify example layout)](https://vuetifyjs.com/en/examples/layouts/baseline) , and of course has [dark mode.](https://smeltejs.com/dark-mode)

Tailwind resets much of CSS whereas Smelte tries to bring sensible Material design defaults in [typography](https://smeltejs.com/typography) and [color.](https://smeltejs.com/color)

Hit up the components [introduction](https://smeltejs.com/components) or please join our [Discord chat](https://discord.com/invite/nZc64MMdkU) for a lovely chat!

#### Installation

 To get you started you need to add Smelte to your dependencies with your favorite package manager. `$ npm install smelte or yarn add smelte` Then add the Smelte Rollup plugin (after svelte but before css). Webpack support coming soon. 
```
const smelte=require("smelte/rollup-plugin-smelte");

plugins=[ 
  ...your plugins, 
  smelte({ 
    purge: production,
    output: "public/global.css", // it defaults to static/global.css which is probably what you expect in Sapper 
    postcss: [], // Your PostCSS plugins
    whitelist: [], // Array of classnames whitelisted from purging
    whitelistPatterns: [], // Same as above, but list of regexes
    tailwind: { 
      colors: { 
        primary: "#b027b0",
        secondary: "#009688",
        error: "#f44336",
        success: "#4caf50",
        alert: "#ff9800",
        blue: "#2196f3",
        dark: "#212121" 
      }, // Object of colors to generate a palette from, and then all the utility classes
      darkMode: true, 
    }, 
    // Any other props will be applied on top of default Smelte tailwind.config.js
  }),
]
```
 Then you should add Tailwind utilites CSS in your app component. `import "smelte/src/tailwind.css" ;` You might also need to include material icons in your template's if you use any: `<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">` Or ship them along with Roboto if you would like to use default material font: 
```
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500|Material+Icons&display=swap"
    rel="stylesheet" />
```
 And you're good to go and have all the Tailwind CSS power all to yourself! For treeshaking to work it is recommended to import each component on its own like this: 
```
import Button from "smelte/src/components/Button";
import Treeview from "smelte/src/components/Treeview";
```

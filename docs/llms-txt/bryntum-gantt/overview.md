# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/revisions/overview.md

# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/overview.md

[//]: # (Links in this document only works when viewed in the documentation browser, surf to ./docs)

# Bryntum Gantt

## What is Bryntum Gantt?

Welcome to Bryntum Gantt - the most **reliable** and **feature-complete** JavaScript Gantt chart component.

Bryntum Gantt is a full-featured gantt component with a rich, clean and comprehensively documented API and many
ways to customize and extend it. It is accessible, responsive and supports touch devices.

Bryntum Gantt is built using modern web techniques on a well documented, comprehensive set of core UI components.
It is designed from the ground up to be responsive and mobile-friendly, while still being a powerful tool for desktop users.

It is internationalized with support for 45 locales out of the box, and this can be easily extended.

It is themed using modern CSS techniques and includes a number of preconfigured themes, each of which may be switched
between light and dark mode. All aspects of the appearance may be customized using CSS variables.

For more general information on our Gantt product, please read on. This documentation provides you with everything you
need to get started.

If you are excited to have a go now, we suggest you to start with one of our **quick start guides** below:

<div class="framework-logos">
<a href="#Gantt/guides/quick-start/react.md"><img src="Core/logo/react.svg" alt="React"><span>React</span></a>
<a href="#Gantt/guides/quick-start/angular.md"><img src="Core/logo/angular.svg" alt="Angular"><span>Angular</span></a>
<a href="#Gantt/guides/quick-start/vue-3.md"><img src="Core/logo/vue.svg" alt="Vue"><span>Vue</span></a>
<a href="#Gantt/guides/quick-start/javascript.md"><img src="Core/logo/js.svg" alt="Vanilla JS"><span>Vanilla JS</span></a>
<a href="#Gantt/guides/quick-start/salesforce.md"><img src="Core/logo/salesforce.svg" alt="Salesforce"><span>Salesforce</span></a>
</div>

## Features

Bryntum Gantt chart offers a wide range of features, such as:

* <a target="_blank" href="#Gantt/guides/data/project_data.md">Scheduling tasks using dependencies and constraints</a>
* <a target="_blank"  href="#Gantt/guides/basics/calendars.md">Leveraging calendars for projects, tasks, and resources</a>
* <a target="_blank" href="#../engine/gantt_tasks_scheduling.md">Using recurrent and fixed time intervals</a>
* <a target="_blank" href="#Gantt/guides/customization/styling.md">Customizing rendering and styling</a>
* <a target="_blank" href="#Grid/guides/basics/columns.md">Customizing user Experience through many different column types</a> & <a target="_blank" href="#Gantt/guides/customization/taskedit.md">task editors</a>
* <a target="_blank" href="../examples/bigdataset/">Dealing with extensive data sets</a> and <a target="_blank" href="#Gantt/guides/build-production.md#performance-optimization">performance tuning</a>
* and more...

## Live demo

Try out some of the Bryntum Gantt features with the live demo below.

<div class="external-example" data-file="Gantt/guides/readme/intro.js"></div>

For a complete overview of Bryntum Gantt capabilities, explore the topic-specific guides in the menu, visit our [API documentation](#Gantt/view/Gantt), and browse [Bryntum Gantt examples](../examples/).

## Continuous evolution and improvement

Maintenance releases with bug fixes are released on average every two weeks, with minor releases every quarter. See
[the public change log](https://bryntum.com/products/gantt/changelog/)

Keep up to date with developments on [our blog](https://bryntum.com/blog/)

## Integration

Bryntum Gantt runs in all modern browsers (Chrome, Firefox, Safari, and modern Edge), regardless of your target technology.

Before integrating Bryntum Gantt with any framework, ensure that your environment meets the following version requirements:

* [NodeJS](https://nodejs.org/en): `>= 20.0.0`
* [TypeScript](https://www.typescriptlang.org/): `>= 3.6.0`
* [Angular](https://angularjs.org/): `>= 9.0.0`
* [React](https://react.dev/): `>= 16.0.0`
* [Vue](https://vuejs.org/): `>= 3.0.0`
* [Ionic](https://ionicframework.com/): `>= 5.0.0`
* [Vite](https://vite.dev/): `>= 4.0.0`
* [Webpack](https://webpack.js.org/): `>= 4.0.0`

You can use Bryntum Gantt out of the box or integrate it with the framework of your choice and many third-party solutions. Visit the integration section of our documentation for further details:

* <a href="#Gantt/guides/integration/react/guide.md">React <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/react.svg" alt="React"></a>
* <a href="#Gantt/guides/integration/angular/guide.md">Angular <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/angular.svg" alt="Angular"></a>
* <a href="#Gantt/guides/integration/vue/guide.md">Vue <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/vue.svg" alt="Vue"></a>
* <a href="#Gantt/guides/integration/ionic/guide.md">Ionic <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/ionic.svg" alt="Ionic"></a>
* <a href="#Gantt/guides/integration/salesforce/readme.md">Salesforce <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/salesforce.svg" alt="Salesforce"></a>

* <a href="#Gantt/guides/integration/nodejs.md">Node.JS <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/nodejs.svg" alt="Node.js"></a>

* <a href="#Gantt/guides/integration/sharepoint.md">Sharepoint <img style="height: 1em;width: 1em;margin-top:0;" src="Core/logo/sharepoint.svg" alt="Sharepoint"></a>

<div class="note">
If you have already downloaded Bryntum Gantt, you'll find framework examples in the <code>examples/frameworks</code>
folder. If you haven't downloaded Bryntum Gantt yet, you can get a free trial
<a href="https://bryntum.com/download/">here</a>.
</div>

## How does it work?

The Bryntum Gantt consists of two parts.
The first part is the project data, consisting of tasks, dependencies, resources, assignments, and calendars.
The second part is the visualization, the **User Interface** for the **project data**.

### Project Data

Gantt is one of a kind. Its scheduling engine matches Microsoft Project logic and supports projects of any size. It is
built on top of [ChronoGraph](https://github.com/bryntum/chronograph) - an open-source reactive computational engine
also developed by Bryntum.

<img src="Gantt/chronograph.png" class="b-screenshot" alt="Scheduling engine">

The component will perform everything under the hood for you. Defaults suit most situations, but you can also customize
the scheduling rules with specific business logic if needed!

The scheduling engine is self-contained/headless, designed to be compatible with a server-side Node.js environment. It
is a built-in dependency and should require no additional installation or configuration.
The documentation for this part of the codebase is available in [Bryntum Scheduling Engine API Docs](engine).

### Visualisation and UI

The visualisation and user interface part of the Gantt is based on [Bryntum Grid](https://bryntum.com/products/grid)
and is written in plain JavaScript. So you can use most Grid features like for instance filtering, sorting or
summarizing in the Gantt too. For more information about Grid capabilities, please visit
the [Grid Component documentation](https://bryntum.com/products/grid/docs/).

In a traditional setup, you will want to use **frozen grid** columns to the left and let the **Gantt Timeline** (which
is a specialised grid) occupy the rest of the available space with a horizontal scrollbar to scroll the timeline. You
can also associate as many extra grids as needed to improve even more the user experience.

<img src="Gantt/gantt-layout.png" class="b-screenshot" alt="Gantt layout">

[//]: # (do not change the title of the last section unless you adapt GA Tag tutorial_complete)

## Next steps

The best way to get started with Gantt is by following our quick start guide, which provides step-by-step
instructions. Once you're familiar with the basics, continue with our in-depth tutorial to explore advanced features.
Choose your preferred technology below to begin:

<div class="framework-logos">
<a href="#Gantt/guides/quick-start/react.md"><img src="Core/logo/react.svg" alt="React"><span>React</span></a>
<a href="#Gantt/guides/quick-start/angular.md"><img src="Core/logo/angular.svg" alt="Angular"><span>Angular</span></a>
<a href="#Gantt/guides/quick-start/vue-3.md"><img src="Core/logo/vue.svg" alt="Vue"><span>Vue</span></a>
<a href="#Gantt/guides/quick-start/javascript.md"><img src="Core/logo/js.svg" alt="Vanilla JS"><span>Vanilla JS</span></a>
</div>

## Professional Services

Need help implementing or customizing Bryntum Gantt? Don’t hesitate to request support from our
[Professional Services team](https://bryntum.com/services/).

## Copyright and license

Copyright © 2009 - 2026, Bryntum

All rights reserved.

[License](https://bryntum.com/products/gantt/license/)

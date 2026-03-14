# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/npm/repository/components.md

﻿# Components and wrappers

## Components

Bryntum components (libraries) for web applications are built using pure JavaScript and can be used in any modern web
application without requiring any special JS framework. These components are packaged as follows:

| _Component_                | _Package_                     | Description                          |
|----------------------------|-------------------------------|--------------------------------------|
| Bryntum Gantt            | `@bryntum/gantt`            | Full licensed component version      |
| Bryntum Gantt Trial      | `@bryntum/gantt-trial`      | Trial limited component version      |
| Bryntum Gantt Thin       | `@bryntum/gantt-thin`       | Thin licensed component version      |
| Bryntum Gantt Thin Trial | `@bryntum/gantt-thin-trial` | Thin trial limited component version |

## Frameworks wrappers

To integrate Bryntum components with all major frameworks including Angular, Ionic, React and Vue, we provide
framework specific wrappers in the following packages:

| _Framework_           | _Package_                       | Integration guide                                                                           |
|-----------------------|---------------------------------|---------------------------------------------------------------------------------------------|
| Angular (IVY)         | `@bryntum/gantt-angular`      | [Angular integration guide](#Gantt/guides/integration/angular/guide.md)                   |
| Angular (View Engine) | `@bryntum/gantt-angular-view` | [Angular integration guide](#Gantt/guides/integration/angular/guide.md)                   |
| Angular (Thin)        | `@bryntum/gantt-angular-thin` | [Angular multiple products guide](#Gantt/guides/integration/angular/multiple-products.md) |
| Ionic with Angular    | `@bryntum/gantt-angular`      | [Ionic integration guide](#Gantt/guides/integration/ionic/guide.md)                       |
| React                 | `@bryntum/gantt-react`        | [React integration guide](#Gantt/guides/integration/react/guide.md)                       |
| React (Thin)          | `@bryntum/gantt-react-thin`   | [React multiple products guide](#Gantt/guides/integration/react/multiple-products.md)     |
| Vue 2.x               | `@bryntum/gantt-vue`          | [Vue integration guide](#Gantt/guides/integration/vue/guide.md)                           |
| Vue 3.x               | `@bryntum/gantt-vue-3`        | [Vue integration guide](#Gantt/guides/integration/vue/guide.md)                           |
| Vue 3.x (Thin)        | `@bryntum/gantt-vue-3-thin`   | [Vue multiple products guide](#Gantt/guides/integration/vue/multiple-products.md)         |

<div class="note">

Wrapper packages require installing <strong>@bryntum/gantt</strong> but it is not listed in the package dependencies.
This was done to support trial package aliasing. You have to manually add the <strong>@bryntum/gantt</strong> dependency to the
application's <strong>package.json</strong> file to use the wrapper packages.

</div>

## Demo resources

Bryntum demo applications use resources such as images, fonts and styling from the **demo-resources** npm package.
This package is **optional** and it is not necessary to add it in your application.

| _Description_  | _Package_                 |
|----------------|---------------------------|
| Demo Resources | `@bryntum/demo-resources` |

<div class="note">

Demo Resources package does not contain framework demos and they are bundled within distribution zip.

</div>

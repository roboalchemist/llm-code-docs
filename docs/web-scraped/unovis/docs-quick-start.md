# Source: https://unovis.dev/docs/quick-start

Title: Quick Start | Unovis

URL Source: https://unovis.dev/docs/quick-start

Published Time: Sat, 31 Jan 2026 00:56:51 GMT

Markdown Content:
Quick Start | Unovis
===============

[Skip to main content](https://unovis.dev/docs/quick-start#__docusaurus_skipToContent_fallback)

⚠️ Important: Angular version support changes in [Unovis 1.7](https://unovis.dev/releases/1.7-angular)

[![Image 1: Unovis](https://unovis.dev/img/unovis-logo.svg)](https://unovis.dev/)[Docs](https://unovis.dev/docs/intro)[Gallery](https://unovis.dev/gallery)[Releases](https://unovis.dev/releases)[Contributing](https://unovis.dev/contributing/intro)

[](https://github.com/f5/unovis)[](https://discord.gg/5hnmashSaN)

Search Ctrl K

*   [Introduction](https://unovis.dev/docs/intro)
*   [Quick Start](https://unovis.dev/docs/quick-start)
*   [Component Reference](https://unovis.dev/docs/category/component-reference) 
    *   [Containers](https://unovis.dev/docs/quick-start#) 
    *   [XY Components](https://unovis.dev/docs/quick-start#) 
    *   [Networks and Flows](https://unovis.dev/docs/quick-start#) 
    *   [Maps](https://unovis.dev/docs/quick-start#) 
    *   [Misc](https://unovis.dev/docs/quick-start#) 
    *   [Auxiliary](https://unovis.dev/docs/quick-start#) 

*   [Guides](https://unovis.dev/docs/quick-start) 
    *   [JavaScript Usage](https://unovis.dev/docs/guides/js-usage)
    *   [Theming](https://unovis.dev/docs/guides/theming)
    *   [Tips and Tricks](https://unovis.dev/docs/guides/tips-and-tricks)

*   [](https://unovis.dev/)
*   Quick Start

On this page

Quick Start
===========

### Component import[​](https://unovis.dev/docs/quick-start#component-import "Direct link to Component import")

_Unovis_ is distributed in the format of [ES modules](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/). After the library is [installed](https://unovis.dev/docs/intro#-install) you can simply import _Unovis_ components from `@unovis/...` packages:

*   React
*   Angular
*   Svelte
*   Vue
*   Solid
*   TypeScript

`import { VisXYContainer, VisLine, VisAxis } from '@unovis/react'`

`import { VisXYContainerModule, VisLineModule, VisAxisModule } from '@unovis/angular'`

`import { VisXYContainer, VisLine, VisAxis } from '@unovis/svelte'`

`import { VisXYContainer, VisLine, VisAxis } from '@unovis/vue'`

`import { VisXYContainer, VisLine, VisAxis } from '@unovis/solid'`

`import { XYContainer, Line, Axis } from '@unovis/ts'`

You can import components individually as well:

*   React
*   Angular
*   Svelte
*   Vue
*   Solid
*   TypeScript

`import { VisXYContainer } from '@unovis/react/containers/xy-container'import { VisLine } from '@unovis/react/components/line'import { VisAxis } from '@unovis/react/components/axis'`

`import { VisXYContainerModule } from '@unovis/angular/esm2015/containers/xy-container'import { VisLineModule } from '@unovis/angular/esm2015/components/line'import { VisAxisModule } from '@unovis/angular/esm2015/components/axis'`

`import { VisXYContainer } from '@unovis/svelte/containers/xy-container'import { VisLine } from '@unovis/svelte/components/line'import { VisAxis } from '@unovis/svelte/components/axis'`

`import { VisXYContainer } from '@unovis/vue/containers/xy-container'import { VisLine } from '@unovis/vue/components/line'import { VisAxis } from '@unovis/vue/components/axis'`

`import { VisXYContainer } from '@unovis/solid/containers/xy-container'import { VisLine } from '@unovis/solid/components/line'import { VisAxis } from '@unovis/solid/components/axis'`

`import { XYContainer } from '@unovis/ts/containers/xy-container'import { Line } from '@unovis/ts/components/line'import { Axis } from '@unovis/ts/components/axis'`

info

_Unovis_ is tree-shakable! Based on our preliminary tests, regular package imports work as good as individual imports. Unused components won't be included into your app's bundle!

Furthermore, heavy parts of the library like _Graph_ layouts or _LeafletMap_ dependencies support dynamic imports and will be loaded on-the-fly after component initialization.

### Line Chart with Axes[​](https://unovis.dev/docs/quick-start#line-chart-with-axes "Direct link to Line Chart with Axes")

*   React
*   Angular
*   Svelte
*   Vue
*   Solid
*   TypeScript

info

We'll use the [useCallback](https://reactjs.org/docs/hooks-reference.html#usecallback) and [useMemo](https://reactjs.org/docs/hooks-reference.html#usememo) hooks throughout the documentation and examples extensively because that improves the performance of the library by avoiding unnecessary rerenders.

`import React, { useCallback } from 'react'import { VisXYContainer, VisLine, VisAxis } from '@unovis/react'type DataRecord = { x: number; y: number }const data: DataRecord[] = [  { x: 0, y: 0 },  { x: 1, y: 2 },  { x: 2, y: 1 },]export function BasicLineChart (): JSX.Element {  return (    <VisXYContainer data={data}>      <VisLine<DataRecord>        x={useCallback(d => d.x, [])}        y={useCallback(d => d.y, [])}      ></VisLine>      <VisAxis type="x"></VisAxis>      <VisAxis type="y"></VisAxis>    </VisXYContainer>  )}`

basic-line-chart.html

`<vis-xy-container>    <vis-line [data]="data" [x]="x" [y]="y"></vis-line>    <vis-axis type="x"></vis-axis>    <vis-axis type="y"></vis-axis></vis-xy-container>`

basic-line-chart.component.ts

`import { Component } from '@angular/core'type DataRecord = { x: number; y: number }@Component({  selector: 'basic-line-chart',  templateUrl: './basic-line-chart.component.html'})export class BasicLineChartComponent {  x = (d: DataRecord): number => d.x  y = (d: DataRecord): number => d.y  data: DataRecord[] = [    { x: 0, y: 0 },    { x: 1, y: 2 },    { x: 2, y: 1 },  ]}`

basic-line-chart.module.ts

`import { NgModule } from '@angular/core'import { VisXYContainerModule, VisLineModule, VisAxisModule } from '@unovis/angular'import { BasicLineChartComponent } from './basic-line-chart.component'@NgModule({  imports: [VisXYContainerModule, VisLineModule, VisAxisModule],  declarations: [BasicLineChartComponent],  exports: [BasicLineChartComponent],})export class BasicLineChartModule { }`

`<script lang="ts">  import { VisXYContainer, VisLine, VisAxis } from '@unovis/svelte'  type DataRecord = { x: number, y: number }  export let data: DataRecord[] = [    { x: 0, y: 0 },    { x: 1, y: 2 },    { x: 2, y: 1 },  ]</script><VisXYContainer>  <VisLine {data} x={d => d.x} y={d => d.y}/>  <VisAxis type="x"/>  <VisAxis type="y"/></VisXYContainer>`

`<script setup lang="ts">  import { VisXYContainer, VisLine, VisAxis } from '@unovis/vue'  import { ref } from 'vue'  type DataRecord = { x: number, y: number }  const data = ref<DataRecord[]>([    { x: 0, y: 0 },    { x: 1, y: 2 },    { x: 2, y: 1 },  ])</script><VisXYContainer>  <VisLine :data="data" :x="d => d.x" :y="d => d.y" />  <VisAxis type="x" />  <VisAxis type="y" /></VisXYContainer>`

`import { VisXYContainer, VisLine, VisAxis } from '@unovis/solid'type DataRecord = { x: number; y: number }const data: DataRecord[] = [  { x: 0, y: 0 },  { x: 1, y: 2 },  { x: 2, y: 1 },]const BasicLineChart = () => {  return (    <VisXYContainer height='50dvh'>      <VisLine data={data} x={(d) => d.x} y={(d) => d.y} />      <VisAxis type='x' />      <VisAxis type='y' />    </VisXYContainer>  )}export default BasicLineChart`

`import { Axis, Line, XYContainer } from '@unovis/ts'type DataRecord = { x: number; y: number }const data: DataRecord[] = [  { x: 0, y: 0 },  { x: 1, y: 2 },  { x: 2, y: 1 },]const line = new Line<DataRecord>({  x: d => d.x,  y: d => d.y,})const container = document.getElementById('vis-container')const chart = new XYContainer(container, {  components: [line],  xAxis: new Axis(),  yAxis: new Axis(),}, data)`

[Edit this page](https://github.com/f5/unovis/tree/main/packages/website/docs/quick-start.mdx)

[Previous Introduction](https://unovis.dev/docs/intro)[Next Component Reference](https://unovis.dev/docs/category/component-reference)

*   [Component import](https://unovis.dev/docs/quick-start#component-import)
*   [Line Chart with Axes](https://unovis.dev/docs/quick-start#line-chart-with-axes)

Learn

*   [Quick Start](https://unovis.dev/docs/quick-start)
*   [Gallery](https://unovis.dev/gallery)

Community

*   [Discord](https://discord.gg/5hnmashSaN)
*   [GitHub Discussions](https://github.com/f5/unovis/discussions)
*   [StackOverflow](https://stackoverflow.com/questions/tagged/unovis)
*   [Twitter](https://twitter.com/unovisdev)

More

*   [Source Code](https://github.com/f5/unovis)
*   [npm](https://www.npmjs.com/package/@unovis/ts)

Copyright © 2026 F5, Inc.

# Source: https://echarts.apache.org/en/faq.html

Title: FAQ - Apache ECharts

URL Source: https://echarts.apache.org/en/faq.html

Markdown Content:
General Questions
-----------------

### What to do if you have technical problem?

1) It is recommended that you read the navigation on the left side of the [option manual](https://echarts.apache.org/en/option.html) before you ask questions. In the option manual, you can find out what configuration items does ECharts have. And you can find under the relevant components whether there are configuration items that can implement the functions you need.

2) Browse FAQ questions on this page.

3) Create a simple example to reproduce your problem on [Official Editor](https://echarts.apache.org/examples/en/editor.html), [CodePen](https://codepen.io/Ovilia/pen/dyYWXWM), [CodeSandbox](https://codesandbox.io/s/echarts-basic-example-template-mpfz1s) or [JSFiddle](https://jsfiddle.net/plainheart/e46ozpqj/7/). If you can't use the code to describe the requirements, you can try to provide a design draft or draw a sketch.

4) Ask questions on [stackoverflow](https://stackoverflow.com/) and attach the example link.

### Is ECharts free to use?

Yes, ECharts is open-sourced under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Axis
----

### What should I do if the axis label doesn't have enough space?

You can use [interval](https://echarts.apache.org/en/option.html#xAxis.interval) to control how many labels are displayed, set it to `0` to display all labels.

Or you can set [axisLabel.rotate](https://echarts.apache.org/en/option.html#yAxis.axisLabel.rotate) to rotate the label a certain angle.

### Why does it not work when you want to put the axis on the right side?

You need to set [onZero](https://echarts.apache.org/en/option.html#yAxis.axisLine.onZero) to `false`.

### How do I force the first / last label of the axis to be displayed?

Both [axisLabel.showMinLabel](https://echarts.apache.org/en/option.html#xAxis.axisLabel.showMinLabel) and [axisLabel.showMaxLabel](https://echarts.apache.org/en/option.html#xAxis.axisLabel.showMaxLabel) are supported since ECharts version 3.5.2. It can be used to control whether the first / last tags are forced to display.

legend
------

### What should I do if the legend area overlapped on the chart?

You can set the [grid](https://echarts.apache.org/en/option.html#grid) to control the position of the chart area. For example, Set a larger `grid.top` to move drawing area down.

We are planning to make the layout smarter in the future versions.

line-chart
----------

### The ticks on the coordinate axis seems different with the data?

Check if you set the `stack`. You should remove it if you don't want to make a stack line chart.

bar-chart
---------

### Why does the y-axis scale disappear when the values are small?

Version 3.5 of ECharts has been fixed this issue.

map-chart
---------

### Province names overlap on the chart. How to modify the location of the names?

You can modify the `cp` coordinates of the corresponding province in the map file (JS or JSON), or modify the map data that has been loaded by `echarts.getMap('china')`.

For more details, please refer to [GitHub](https://github.com/apache/echarts/issues/4379#issuecomment-257765948).

### Where can I download maps from other countries?

Map information for other countries can be downloaded from [here](https://github.com/echarts-maps/echarts-countries-js).

### How can I get the zoom event of a map?

First, you need to set the series's [roam](https://echarts.apache.org/en/option.html#series-map.roam) to `true` and then listen for the `'georoam'` event. Such as:

```
myChart.on('georoam', function (params) {
   console.log(params);
});
```

### How to make my custom map?

The ECharts map is [additionally encoded](https://github.com/apache/echarts/blob/8eeb7e5abe207d0536c62ce1f4ddecc6adfdf85e/src/util/mapData/rawData/encode.js) from original coordinates. You can use the [mapshaper-plus tool](https://github.com/giscafer/mapshaper-plus) to upload a custom geojson file and then generate a map file that can be used in Echarts.

baidu-map
---------

### How to use ECharts with Baidu Map?

1. Include `echarts.js`, `bmap.js` and `https://api.map.baidu.com/api?v=3.0&ak=Here is the access key you obtained on the Baidu development platform`.
2. Set `bmap` in `option`，You can refer to this [example](https://echarts.apache.org/examples/en/editor.html?c=effectScatter-bmap).
3. If you need to get a Baidu map instance, you can use `chart.getModel().getComponent('bmap').getBMap()`，and then make do settings based on [Baidu Maps API](https://lbsyun.baidu.com/cms/jsapi/reference/jsapi_reference.html) .

gauge-chart
-----------

### How to set the dashboard color?

You can use [axisLine.lineStyle.color](https://echarts.apache.org/en/option.html#series-gauge.axisLine.lineStyle.color).

Event processing
----------------

### How do I get events such as chart clicks?

Read the [official tutorial](https://echarts.apache.org/handbook/en/concepts/event). The types of events supported by ECharts can be found in the [related API](https://echarts.apache.org/en/api.html#events).

others
------

### Why is the chart not displayed?

You can check the following situations：

* Whether `echarts.js` is loaded normally.
* Whether`echarts` variable exists.
* Whether the DOM container has a width or height when calling `echarts.init`.

### Why does the chart not work correctly when using ECharts in Vue?

* If you are using Vue 3, avoid using `reactive` and `ref`.
* If you are using Vue 2, avoid declaring the ECharts instance object in the `data` function or using the `Vue.observable` API.

All of the above will cause the ECharts instance object to be proxied as a reactive object, which may affect the access to the properties of inner models of ECharts and bring some unexpected issues and lousy performance.

The suggestion is to declare the ECharts instance object as a normal variable, or use `shallowRef` / `shallowReactive` / `markRaw` API to prevent the instance object from being proxied.

See also [#17723](https://github.com/apache/echarts/issues/17723#issuecomment-1268311307) and [the usage caution from Vue documentation](https://vuejs.org/api/reactivity-advanced.html#markraw).

### Are there more resources for learning ECharts?

Please refer to [awesome-echarts](https://github.com/ecomfe/awesome-echarts) for more related projects and resources.

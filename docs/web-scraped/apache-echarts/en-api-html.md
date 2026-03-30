# Source: https://echarts.apache.org/en/api.html

Title: Documentation - Apache ECharts

URL Source: https://echarts.apache.org/en/api.html

Markdown Content:
Global echarts object, which can be accessed after including `echarts.js` in script tag or through `require('echarts')` in AMD environment.

### Properties

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[init](https://echarts.apache.org/en/api.html#echarts.init)

Function

```
(dom: HTMLDivElement|HTMLCanvasElement, theme?: Object|string, opts?: {
    devicePixelRatio?: number,
    renderer?: string,
    useDirtyRect?: boolean,     // Since `5.0.0`
    useCoarsePointer?: boolean, // Since `5.4.0`
    pointerSize?: number,       // Since `5.4.0`
    ssr?: boolean,              // Since `5.3.0`
    width?: number|string,
    height?: number|string,
    locale?: string             // Since `5.0.0`
}) => ECharts
```

Creates an ECharts instance, and returns an [echartsInstance](https://echarts.apache.org/en/api.html#echartsInstance). You shall not initialize multiple ECharts instances on a single container.

**Parameters**

* `dom`

Instance container, usually is a DIV element with height and width defined. It's only optional when `opts.ssr` is enabled for server-side rendering.

It can also be a `canvas` element. thus the canvas can be used somewhere else as image directly after rendering the chart. For example, canvas can be used as a texture in WebGL, which enables updating charts in real-time, as compared to using images generated with [echartsInstance.getDataURL](https://echarts.apache.org/en/api.html#echartsInstance.getDataURL).

* `theme`

Theme to be applied. This can be a configuring object of a theme, or a theme name registered through [echarts.registerTheme](https://echarts.apache.org/en/api.html#echarts.registerTheme). See [Overview of Style Customization](https://echarts.apache.org/handbook/en/concepts/style).

* `opts`

Optional chart configurations; which may contain:

    *   `devicePixelRatio` Ratio of one physical pixel to the size of one device independent pixels. Browser's `window.devicePixelRatio` is used by default.
    *   `renderer` Supports `'canvas'` or `'svg'`. See [Render by Canvas or SVG](https://echarts.apache.org/handbook/en/best-practices/canvas-vs-svg).
    *   `ssr` Whether to use server-side rendering. Only available in SVG rendering mode. When enabled, it will no longer render automatically every frame, you have to use the [renderToSVGString](https://echarts.apache.org/en/api.html#echartsInstance.renderToSVGString) method to get the rendered SVG string. See [Server Side Rendering](https://echarts.apache.org/handbook/en/how-to/cross-platform/server).
    *   `useDirtyRect` Enable dirty rectangle rendering or not, `false` by default. See [New features in ECharts 5](https://echarts.apache.org/handbook/en/basics/release-note/v5-feature).
    *   `useCoarsePointer` Whether to expand the response area when interacting with elements. `null` means enabling for mobile devices; `true` means always enabling; `false` means always disabling. See [Coarse Pointer](https://echarts.apache.org/handbook/en/how-to/interaction/coarse-pointer) for more information.
    *   `pointerSize` Size of expanded interaction size in pixels. It should be used along with `opts.useCoarsePointer`.
    *   `width` Specify width explicitly, in pixel. If setting to `null`/`undefined`/`'auto'`, width of `dom` (instance container) will be used.
    *   `height` Specify height explicitly, in pixel. If setting to `null`/`undefined`/`'auto'`, height of `dom` (instance container) will be used.
    *   `locale` Specify the locale. There are two builtins: `'ZH'` and `'EN'`. Or you can use [echarts.registerLocale](https://echarts.apache.org/en/api.html#echarts.registerLocale) to register a new locale. Or supported locales can be referenced in [src/i18n](https://github.com/apache/echarts/tree/release/src/i18n).

If no need to specify a theme, a `null` should be passed before `opts` . Example:

```
const chart = echarts.init(dom, null, {renderer: 'svg'});
```

**Note**

If DIV is hidden, ECharts initialization tends to fail due to the lack of width and height information. In this case, you can explicitly specify `style.width` and `style.height` of DIV, or manually call [echartsInstance.resize](https://echarts.apache.org/en/api.html#echartsInstance.resize) after showing DIV.

The height and width must be set via `opts.width` and `opts.height` in the server side rendering.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[connect](https://echarts.apache.org/en/api.html#echarts.connect)

Function

```
(group:string|Array)
```

Connects interaction of multiple chart series.

**Parameters**

* `group` Group id, or array of chart instance.

**For example:**

```
// set group id of each instance respectively.
chart1.group = 'group1';
chart2.group = 'group1';
echarts.connect('group1');
// or incoming instance array that need to be linked.
echarts.connect([chart1, chart2]);
```

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[disconnect](https://echarts.apache.org/en/api.html#echarts.disconnect)

Function

```
(group:string)
```

Disconnects interaction of multiple chart series. To have one single instance to be removed, you can set `group` of chart instance to be null.

**Parameters**

* `group`

group id.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[dispose](https://echarts.apache.org/en/api.html#echarts.dispose)

Function

```
(target: ECharts|HTMLDivElement|HTMLCanvasElement)
```

Destroys chart instance, after which the instance cannot be used any more.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[getInstanceByDom](https://echarts.apache.org/en/api.html#echarts.getInstanceByDom)

Function

```
(target: HTMLDivElement|HTMLCanvasElement) => ECharts
```

Returns chart instance of dom container.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[use](https://echarts.apache.org/en/api.html#echarts.use)

Function

Since `v5.0.1`

Use components. Used with the new tree-shaking API.

NOTE: `echarts.use` must be used before `eharts.init`

```
// Import the echarts core module, which provides the necessary interfaces for using echarts.
import * as echarts from 'echarts/core';
// Import bar charts, all with Chart suffix
import {
    BarChart
} from 'echarts/charts';
// import rectangular coordinate system component, all suffixed with Component
import {
    GridComponent
} from 'echarts/components';
// Import the Canvas renderer, note that introducing the CanvasRenderer or SVGRenderer is a required step
import {
    CanvasRenderer
} from 'echarts/renderers';

// Register the required components
echarts.use(
    [GridComponent, BarChart, CanvasRenderer]
);
```

See [Use ECharts with bundler and NPM](https://echarts.apache.org/handbook/en/basics/import) for more detailed explanation.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[registerMap](https://echarts.apache.org/en/api.html#echarts.registerMap)

Function

```
(
    mapName: string,
    opt: {
        geoJSON: Object | string;
        specialAreas?: Object;
    }
)
| (
    mapName: string,
    opt: {
        svg: Object | string;
    }
)
| (
    mapName: string,
    geoJSON: Object | string,
    specialAreas?: Object
)
```

Registers available maps. This can only be used after including [geo](https://echarts.apache.org/en/option.html#geo) component or chart series of [map](https://echarts.apache.org/en/option.html#series-map).

Please refer to [option.geo](https://echarts.apache.org/en/option.html#geo.map) for usage.

**Parameters:**

* **@param `mapName`:**

Map name, referring to `map` value set in [geo](https://echarts.apache.org/en/option.html#geo) component or [map](https://echarts.apache.org/en/option.html#series-map).

* **@param `opt.geoJSON`:**

Optional. Data in GeoJSON format. See [https://geojson.org/](https://geojson.org/) for more format information. Can be a JSON string or a parsed object. This key can also be `geoJson`.

For example, A minimal geoJSON:

```
const geoJSONSample = {
      "type": "FeatureCollection",
      "features": [
          {
              "type": "Feature",
              "geometry": {
                  "type": "Polygon",
                  "coordinates": [
                      [[200, 3000], [500, 3000], [500, 5000], [200, 5000]]
                  ]
              },
              "properties": {
                  "name": "Some Place",
                  "cp": [220, 2100]
              }
          }
      ]
  };
  echarts.registerMap('my_geo_sample', {geoJSON: geoJSONSample});
```

Note:

    *   `features[i].properties.name` in GeoJSON is required by ECharts to query the corresponding region, or display the label. Property `name` is used by default, but can also be other properties, see [geo.nameProperty](https://echarts.apache.org/en/option.html#geo.nameProperty).
    *   `features[i].properties.cp` is an optional property that ECharts can recoganize. It provides coordinates on which the label can be displayed. If not provided, the label will be displayed at the center of the region.

* **@param `opt.svg`:**

Optional. Data in SVG format. Can be a SVG string or a parsed SVG DOM object. See more info in [SVG Base Map](https://echarts.apache.org/handbook/en/how-to/component-types/geo/svg-base-map). Introduced in `v5.1.0`.

For example, A minimal SVG:

```
const mySVG = `<?xml version="1.0" encoding="utf-8"?>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:ooo="http://xml.openoffice.org/svg/export" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.2" fill-rule="evenodd" xml:space="preserve">
  <path name="left_rect" d="M 0,0 L 0,100 100,100 100,0 Z" fill="#765" stroke="rgb(56,93,138)" stroke-width="0" stroke-linecap="square" stroke-linejoin="miter"/>
  </svg>`;
  echarts.registerMap('my_geo_sample', {svg: mySVG});
```

* **@param `opt.specialAreas`:**

Optional. zoomed part of a specific area in the map for better visual effect. Only work for `geoJSON`.

**[An example of specialAreas](https://echarts.apache.org/examples/en/editor.html?c=map-usa):**

```
echarts.registerMap('USA', usaJson, {
      // Move Alaska to the bottom left of United States
      Alaska: {
          // Upper left longitude
          left: -131,
          // Upper left latitude
          top: 25,
          // Range of longitude
          width: 15
      },
      // Hawaii
      Hawaii: {
          left: -110,
          top: 28,
          width: 5
      },
      // Puerto Rico
      'Puerto Rico': {
          left: -76,
          top: 26,
          width: 2
      }
  });
```

Note: If you only import the required components in your project, starting from v5.3.0 `registerMap` cannot be called unless `MapChart` or `GeoComponent` is imported (ES module import).

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[getMap](https://echarts.apache.org/en/api.html#echarts.getMap)

Function

```
(mapName: string)
```

Get a registered map in the following format:

```
{
    // geoJSON data of the map
    geoJSON: Object,
    // special area, see registerMap() for more information
    specialAreas: Object
}
```

Note:

* `geoJSON` can also be `geoJson`, they have the same reference.
* SVG registered by `registerMap` can not be obtained by this method yet.
* If you only import the required components in your project, starting from v5.3.0 `getMap` has to be used after the `MapChart` or `GeoComponent` is imported.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[registerTheme](https://echarts.apache.org/en/api.html#echarts.registerTheme)

Function

Since `v6.0.0`

```
(themeName: string, theme: Object)
```

Registers a theme, should be specified when [initialize the chart instance](https://echarts.apache.org/en/api.html#echarts.init).

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[registerCustomSeries](https://echarts.apache.org/en/api.html#echarts.registerCustomSeries)

Function

Since `v6.0.0`

```
(type: string, renderItem: Function)
```

Register a custom series. After registration, it can be used in [setOption](https://echarts.apache.org/en/api.html#api.html#echartsInstance.setOption).

* `type` is the type of the chart to be registered, that is, the `series.renderItem` written later in `setOption`.
* `renderItem` is the graphic rendering logic of the custom series. For details, see [series-custom.renderItem](https://echarts.apache.org/en/option.html#series-custom.renderItem).

Example:

```
const renderItem = (params, api) => {
    return {
        type: 'circle',
        shape: {
            cx: api.coord([api.value(0), api.value(1)])[0],
            cy: api.coord([api.value(0), api.value(1)])[1],
            r: api.value(2) * (params.itemPayload.scale || 1)
        },
        style: {
            fill: api.visual('color'),
            opacity: params.itemPayload.opacity() || 1,
        }
    }
};
echarts.registerCustomSeries('bubble', renderItem);

const option = {
    xAxis: {},
    yAxis: {},
    series: {
        type: 'custom',
        renderItem: 'bubble',
        itemPayload: {
            scale: 2,
            opacity: () => Math.random() * 0.5 + 0.5
        },
        data: [[11, 22, 20], [33, 44, 40], [18, 24, 10]]
    }
};
chart.setOption(option);
```

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[registerLocale](https://echarts.apache.org/en/api.html#echarts.registerLocale)

Function

Since `v5.0.0`

```
(locale: string, localeCfg: Object)
```

Registers a locale, should be specified when [initialize the chart instance](https://echarts.apache.org/en/api.html#echarts.init). See the format in [src/i18n/langEN.ts](https://github.com/apache/echarts/blob/release/src/i18n/langEN.ts)

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[setPlatformAPI](https://echarts.apache.org/en/api.html#echarts.setPlatformAPI)

Function

Since `v5.3.0`

```
(platformAPI?: {
    createCanvas(): HTMLCanvasElement
    measureText(text: string, font?: string): { width: number }
    loadImage(
        src: string,
        onload: () => void,
        onerror: () => void
    ): HTMLImageElement
}) => void
```

Sets the platform-related API, which may need to be provided when non-browser platforms such as NodeJS.

* `createCanvas` Creates a Canvas element, mainly used for measuring text width, which is required when `measureText` is not provided.
* `measureText` measures the width of the text. By default will use the interface provided by the Canvas element to measure the width of the text. It can be replaced with a lighter implementation.
* `loadImage` Load image, required when using Canvas rendering mode and using URLs as images.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[graphic](https://echarts.apache.org/en/api.html#echarts.graphic)

any

Util methods about graphics.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[graphic.](https://echarts.apache.org/en/api.html#echarts.graphic)[extendShape](https://echarts.apache.org/en/api.html#echarts.graphic.extendShape)

Function

Create a new shape class.

```
(
    opts: Object
) => zrender.graphic.Path
```

The details of the parameter `opts` can be checked in [zrender.graphic.Path](https://ecomfe.github.io/zrender-doc/public/api.html#zrenderpath)

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[graphic.](https://echarts.apache.org/en/api.html#echarts.graphic)[registerShape](https://echarts.apache.org/en/api.html#echarts.graphic.registerShape)

Function

Register a user defined shape.

```
(
    name: string,
    ShapeClass: zrender.graphic.Path
)
```

The `ShapeClass` should be generated by [echarts.graphic.extendShape](https://echarts.apache.org/en/api.html#echarts.graphic.extendShape). Then the shape class can be fetched by [echarts.graphic.getShapeClass](https://echarts.apache.org/en/api.html#echarts.graphic.getShapeClass)`registerShape` will overwrite the registered shapes, including the registered built-in shapes, if using the same `name`. The registered shapes can be used in [custom series](https://echarts.apache.org/en/option.html#series-custom) and [graphic component](https://echarts.apache.org/en/option.html#graphic) by declaring `{type: name}`.

For example:

```
var MyShape = echarts.graphic.extendShape({
    shape: {
        x: 0,
        y: 0,
        width: 0,
        height: 0
    },
    buildPath: function (ctx, shape) {
        ctx.moveTo(shape.x, shape.y);
        ctx.lineTo(shape.x + shape.width, shape.y);
        ctx.lineTo(shape.x, shape.y + shape.height);
        ctx.lineTo(shape.x + shape.width, shape.y + shape.height);
        ctx.closePath();
    }
});
echarts.graphic.registerShape('myCustomShape', MyShape);

var option = {
    series: {
        type: 'custom',
        coordinateSystem: 'none',
        renderItem: function (params, api) {
            return {
                type: 'myCustomShape',
                shape: {
                    x: api.value(0),
                    y: api.value(1),
                    width: api.value(2),
                    height: api.value(3)
                },
                style: {
                    fill: 'red'
                }
            };
        },
        data: [[10, 20, 30, 40]]
    }
};
```

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[graphic.](https://echarts.apache.org/en/api.html#echarts.graphic)[getShapeClass](https://echarts.apache.org/en/api.html#echarts.graphic.getShapeClass)

Function

Get the [registered](https://echarts.apache.org/en/api.html#echarts.graphic.registerShape) shape class.

```
(
    name: String
) => zrender.graphic.Path
```

Some built-in shapes are registered by default: `'circle'`, `'sector'`, `'ring'`, `'polygon'`, `'polyline'`, `'rect'`, `'line'`, `'bezierCurve'`, `'arc'`.

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[graphic.](https://echarts.apache.org/en/api.html#echarts.graphic)[clipPointsByRect](https://echarts.apache.org/en/api.html#echarts.graphic.clipPointsByRect)

Function

Clip the given points by the given rectangular.

```
(
    // The points to be clipped, like [[23, 44], [12, 15], ...].
    points: Array.<Array.<number>>,
    // The rectangular that is used to clip points.
    rect: {
        x: number,
        y: number,
        width: number,
        height: number
    }
) => Array.<Array.<number>> // The result Points.
```

#### [echarts.](https://echarts.apache.org/en/api.html#echarts)[graphic.](https://echarts.apache.org/en/api.html#echarts.graphic)[clipRectByRect](https://echarts.apache.org/en/api.html#echarts.graphic.clipRectByRect)

Function

Clip the first input rectangular by the second input rectangular.

```
(
    // The rectangular to be clipped.
    targetRect: {
        x: number,
        y: number,
        width: number,
        height: number
    },
    // The rectangular that is used to clip the first  rectangular.
    rect: {
        x: number,
        y: number,
        width: number,
        height: number
    }
) => { // The result rectangular.
    x: number,
    y: number,
    width: number,
    height: number
}
```

Notice: if the rect is totally clipped, returns `undefined`.

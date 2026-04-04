# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/customization/styling.md

# Styling

The Bryntum Gantt is rendered in the DOM using regular HTML and CSS, and can be completely styled using CSS. It ships
with both pre-compiled CSS bundles, and the original CSS files. The CSS includes different themes and colors,
which can be used to alter how the Gantt and its contents look.

You can also programmatically modify the appearance of cells, headers and events using renderers (depending on product).

## <img src="Gantt/figma.svg"> Figma templates

Designers looking for Figma templates can find them over at [figma.com/@bryntum](https://www.figma.com/@bryntum)

![Figma screenshot](Gantt/gantt-figma.png "Figma screenshot")

## Styling the left grid / table tree section

The left section of the Gantt is inherited from the [Bryntum Grid](https://bryntum.com/products/grid). Any styling
you want to perform on columns, cells or rows is described
[here](https://bryntum.com/products/grid/docs/guide/Grid/customization/styling#using-renderers-and-css).

## Styling task bars

### Styling using predefined colors

Bryntum Gantt ships with 17 predefined task colors. Task color can be specified for the entire Gantt or per task. Task
settings overrides the Gantt setting. The following snippet shows how to assign colors:

```javascript
// Make all tasks orange by default
gantt.eventColor = 'orange';
// Make a single task violet:
task.eventColor = 'violet';
```

This demo has one task per available color:

<div class="external-example" data-file="Gantt/guides/customization/colors.js"></div>

Give the <a href="../examples/taskstyles" target="_blank">Task styles</a> demo a shot if you want to try different
colors.

<div class="note">
If you want to control the appearance of tasks using custom CSS we recommend setting <code>eventColor</code> to
<code>null</code>. This applies very basic styling that is easier to override using CSS.
</div>

### Styling using task data fields

Tasks can be styled in a few different ways. The easiest way is by applying a CSS class using
the [cls](#Gantt/model/TaskModel#field-cls)
data field in the `TaskModel`. You can also apply inline styles through the data using
the [style](#Gantt/model/TaskModel#field-style)
field. See example data below setting background to **red** and adding a myClass CSS class to the task bar element:

```json
{
    "id"          : 13,
    "name"        : "Setup load balancer",
    "percentDone" : 50,
    "style"       : "background:red",
    "cls"         : "myClass",
    "startDate"   : "2022-01-14",
    "duration"    : 3,
    "endDate"     : "2019-01-17"
}
```

### Styling at runtime using the `taskRenderer`

You can also use the [taskRenderer](#Gantt/view/GanttBase#config-taskRenderer) method to apply styles at runtime. This
method receives a `renderData` parameter which you can use to set:

- `cls` - A CSS class to add to the task bar element
- `wrapperCls` - A CSS class to add to the outer task wrapping element
- `iconCls` - A CSS class representing a task icon element
- `style` - An inline style string (or object) to add to the task bar element
- `indicators` - An array that can be populated with TimeSpan records or their config objects to have them rendered in the
  task row (See the [indicators](../examples/indicators) demo for more information)

The function return value can be any markup to render inside the task bar.

```javascript
new Gantt({
    taskRenderer({ taskRecord, renderData }) {
        if (taskRecord.endDate < Date.now()) {
            // fade out tasks in the past
            renderData.style = "opacity:0.5";
        }

        // Skip showing names for parent task bars
        return taskRecord.isParent ? '' : taskRecord.name;
    }
});
```

### Styling task bars using predefined colors

Bryntum Gantt ships with a bunch of pre-defined colors. Color can be specified for the entire Gantt or per task. Task
settings overrides Gantt setting. The following snippet shows how to assign colors:

```javascript
// Make all tasks blue by default
gantt.eventColor = 'blue';
// Make a single task violet:
task.eventColor = 'violet';
```

**Note:** If you want to control the appearance of events using custom CSS we recommend setting `eventColor` to `null`.
This applies very basic styling that is easier to override using CSS.

## Rendering custom HTML content inside a task bar

You can fully control the markup of the task bar using the [taskRenderer](#Gantt/view/GanttBase#config-taskRenderer)
method. Below is a demo showing the initials of the assigned resources rendered inside the task bar.

<div class="external-example" data-file="Gantt/guides/customization/taskRenderer.js"></div>

If you instead want to output some data about each time axis tick (like hours worked on a task per day), you can look at
the [custom task bar example](../examples/custom-taskbar) for inspiration:

![Custom task bar](Gantt/custom-taskbar.png "Custom task bar")

## Rendering custom indicator icons inside a task row

You can render icons inside a task row to indicate things like deadline or other important task dates using the
[indicators](#Gantt/feature/Indicators) feature. Try a live demo of it [here](../examples/indicators)

![Indicators](Gantt/indicators.png "Indicators")

## Styling dependency lines

The inter-task dependencies are rendered as SVG lines which you can easily customize using regular CSS. To change
the appearance of all dependency lines globally, simply do:

```css
/* Lines */
.b-sch-dependency {
  stroke       : #000; /* Black lines */
  stroke-width : 2;    /* Slightly thicker */
}

/* Arrow markers */
.b-sch-dependency-arrow {
  fill : #000; /* Black arrows too */
}
```

<div class="external-example" data-file="Gantt/guides/customization/stylingDependencies.js"></div>

To modify individual dependencies, you can use the [cls](#Gantt/model/DependencyModel#field-cls) data field to add a CSS
class to the SVG element representing the dependency:

```json
{
  "id"       : 1,
  "fromTask" : 11,
  "toTask"   : 15,
  "lag"      : 2,
  "cls"      : "important"
}
```

And here is the CSS to change the appearance:

```css
.b-sch-dependency.important {
  stroke       : #e44b4b;
  marker-start : url(#arrowEndCritical);
}

.b-sch-dependency-arrow#arrowEndCritical {
  fill : #e44b4b;
}
```

## Using a theme

Bryntum products have their "structural" CSS and themes separated. The structural CSS contains the basic layout and
styling shared between all themes for the product. It defines a lot of CSS variables (CSS custom properties), that the
themes then set to specific values to create the visual appearance.

The theme CSS files set CSS variables for all Bryntum products, so you can use the same theme file for all Bryntum
products.

The Gantt ships with four themes, each available in light and dark variants:

- Stockholm (`stockholm-light.css` & `stockholm-dark.css`)
- Svalbard (`svalbard-light.css` & `svalbard-dark.css`)
- Visby (`visby-light.css` & `visby-dark.css`)
- Material3 (`material3-light.css` & `material3-dark.css`)
- Fluent2 (`fluent2-light.css` & `fluent2-dark.css`)

The CSS is located in the `/build` folder of the Bryntum distribution. You can include it in your project by for example
using link tags:

```html
<!-- Structural CSS -->
<link rel="stylesheet" href="build/gantt.css">
<!-- Bryntum theme -->
<link rel="stylesheet" href="build/svalbard-light.css" data-bryntum-theme>
```

<div class="note">

The <code>data-bryntum-theme</code> attribute on the link tag is not strictly required, but it allows you to programmatically
switch the theme at runtime using <code>DomHelper.setTheme()</code>.

</div>

### Comparison of themes

#### Svalbard

Our default theme, very light and minimalistic. It is designed to be easy on the eyes and to not distract from the data.

![Svalbard Light theme](Gantt/themes/thumb.svalbard-light.png "Svalbard Light theme")
![Svalbard Dark theme](Gantt/themes/thumb.svalbard-dark.png "Svalbard Dark theme")

#### Stockholm

The Stockholm theme was our default theme prior to v7.0. It has been updated with a more modern look and feel.

![Stockholm Light theme](Gantt/themes/thumb.stockholm-light.png "Stockholm Light theme")
![Stockholm Dark theme](Gantt/themes/thumb.stockholm-dark.png "Stockholm Dark theme")

#### Visby

The city of Visby is famous for its medieval city wall, and the Visby theme embraces that by using more borders than our
other themes.

![Visby Light theme](Gantt/themes/thumb.visby-light.png "Visby Light theme")
![Visby Dark theme](Gantt/themes/thumb.visby-dark.png "Visby Dark theme")

#### Material3

The Material3 theme is based on Google's Material Design. It is a modern and clean theme that is slightly more colorful
than our Svalbard theme.

![Material3 Light theme](Gantt/themes/thumb.material3-light.png "Material Light theme")
![Material3 Dark theme](Gantt/themes/thumb.material3-dark.png "Material Dark theme")

In most of the included examples you can switch theme on the fly by clicking on the gear icon found in the header and
then picking a theme in the dropdown.

![Change theme](Gantt/changing-theme.png "Change theme")

### Combining products

The structural CSS described above include all the CSS you need to use Gantt and its helper widgets such as Popups,
TextFields and so on. When combining multiple different Bryntum products on a single page using normal structural CSS,
the shared styling will be included multiple times.

To avoid this, each product's structural CSS is available in a version that only contains the CSS specific for that
product. These are called `thin` CSS bundles (e.g. `gantt.thin.css`).

When using them you will need to include one for each used level in the Bryntum product hierarchy
(Gantt -> `Core + Grid + Scheduler + Scheduler Pro + Gantt`).

For example to combine Gantt and Calendar using the Svalbard Light theme, you would include:

- `core.thin.css`
- `grid.thin.css`
- `scheduler.thin.css`
- `schedulerpro.thin.css`
- `gantt.thin.css`
- `calendar.thin.css`
- `svalbard-light.css`

Which in your html file might look something like this:

```html
<link rel="stylesheet" href="core.thin.css" >
<link rel="stylesheet" href="grid.thin.css">
<link rel="stylesheet" href="scheduler.thin.css">
<link rel="stylesheet" href="schedulerpro.thin.css">
<link rel="stylesheet" href="gantt.thin.css">
<link rel="stylesheet" href="calendar.thin.css">
<link rel="stylesheet" href="svalbard-light.css" data-bryntum-theme>
```

<div class="note">

Nothing prevents you from always using thin CSS bundles, but please note that there might be a slight network overhead
from pulling in multiple CSS files as opposed to a single one with the normal CSS.

</div>

## Creating a custom theme

To create your own theme, get the [distribution bundle](#Gantt/guides/download.md) or install the NPM package as usual and follow these steps:

- (Optional) Make a copy of an existing theme found under `build/` (either in package under the `node_modules` folder or
  in the extracted zip), for example the `svalbard-light.css` file. If you pick the theme that is closest to what you
  want, you will have to change less. You can also start from scratch, but it will be more work.
- Edit the variables in it to suit your needs, and add any additional variables you want to tweak. You can reference all
  the available variables in the API documentation for each widget, or by looking at the CSS files in the `lib` folder.
- Include your theme on page (and remove any default theme you where using).

Depending on the import order of your CSS files, you might need to make the theme's variables more specific than the
structural CSS. If for example this does not alter the variables as you would expect:

```css
:root {
    --b-button-outlined-border-color : lightsalmon;
}
```

It might be because the structural CSS is included after your theme, and it sets the variable to a different value. In
that case, you can either alter the inclusion order (if you have control over the build process), or make your variables
more specific:

```css
/* The :not rule can contain anything, its purpose is only to make this rule */ 
/* more specific */
:root:not(.b-nothing) {
  --b-button-outlined-border-color : lightsalmon;
}

/* Another (less flexible) option is to scope it to a specific selector */
.b-button {
  --b-button-outlined-border-color : lightsalmon;
}
```

Gantt also uses variables from `grid-sass`, `scheduler-sass` and `schedulerpro-sass`, found at `node_modules/@bryntum/gantt/source/resources/[grid/scheduler/schedulerpro]-sass/variables.scss`

Please see the <a href="../examples/custom-theme/" target="_blank">
Custom theme example</a> for a custom theme in action:

![Custom theme](Gantt/themes/thumb.custom.png "Custom theme")

## Overriding an existing theme

As an alternative to creating a full custom theme, you can also just override a few variables in an existing theme.
To do so, include the structural CSS and the theme you want to use, and then add your own CSS file that overrides
the variables you want to change.

```html
<!-- Structural CSS -->
<link rel="stylesheet" href="build/gantt.css">
<!-- Bryntum theme -->
<link rel="stylesheet" href="build/svalbard-light.css" data-bryntum-theme>
<!-- Your customizations -->
<link rel="stylesheet" href="path/to/your/customizations.css">
```

In `customizations.css`, you can then override any variables you want to change:

```css
:root {
    /* Everything looks good in lightsalmon */
    --b-button-outlined-border-color : lightsalmon;
}
```

## Switching theme at runtime

You can also add a combo box (or other UI) that lets you change the theme at run-time, similar to the examples we have.
To do so, ensure you have multiple themes in a folder (e.g. `/themes`).

<div class="note">

If you're using custom themes, ensure that you change their names in the <code>.b-theme-info</code> block in the CSS file to avoid
collisions.

</div>

Next, you need to add a combo box using `tbar`.

```javascript
import { Gantt, DomHelper } from '@bryntum/gantt';
const gantt = new Gantt({
    // ...gantt data
    tbar : [
        {
            type  : 'combo',
            // list of themes shown in the drop down (combo box)
            items : [
                { text : 'Svalbard Light', value : 'svalbard-light' },
                { text : 'Svalbard Dark', value : 'svalbard-dark' },
                { text : 'Visby-Light', value : 'visby-light' },
                { text : 'Visby-Dark', value : 'visby-dark' }
                // More themes...
            ],
            label : 'Theme',
            // default theme
            value : 'svalbard-light',
            // change theme on selection
            onAction(props) {
                DomHelper.setTheme(props.value);
            }
        }
    ]
});
```

With that being set up, you can switch themes within your application.

## Using renderers and CSS

For performance reasons, scheduled task elements are reused when scrolling, meaning that you should not manipulate them
directly. Instead the contents of cells, headers and tasks can be customized using renderers. Renderers are functions
with access to a cell/header/tasks data (such as style and CSS classes, and in some cases elements). They can
manipulate the data to alter appearances or return a value to have it displayed.

For more information, see the [theme](../examples/theme) demo or check API docs for:
- [Cell renderer](#Grid/column/Column#config-renderer)
- [Column header renderer](#Grid/column/Column#config-headerRenderer)
- [Task renderer](#Gantt/view/Gantt#config-taskRenderer)

## Troubleshooting

### CSS mismatched version

If you've encountered a CSS error:

```plaintext
CSS version 7.0.0 doesn't match bundle version 7.2.1!
Make sure you have imported css from the appropriate product version.
```

That means you're using a wrong version of Bryntum theme file. Following are some of the ways to check and fix the issue:

#### Verify CSS version

Ensure that the CSS file being used matches the version of the Bryntum API. For example, if you're using version
`7.2.1` of Gantt, you need to have the CSS files of version `7.2.1`.

#### Clear Cache

Ensure the mismatched CSS file is not cached on your web server to prevent outdated files from being served.
Clear the browser cache to ensure the latest CSS file is loaded.

#### Cache Busting

Cache busting is a technique used to force browsers to load the most recent versions of files. If the CSS file is
imported in `index.html`, then it should have cache busting by specifying the version
(`gantt.css?v=7.2.1`) or use timestamps (`gantt.css?1704085200`).

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Gantt App</title>
    <link rel="stylesheet" href="path/to/stylesheet.css?v=1.2.3"> <!-- Cache busting by specifying version -->
</head>
<body>
    <!-- Your content here -->
</body>
</html>
```

Modern frameworks apply this by default to the production code, but it needs to be manually implemented in vanilla
JavaScript projects.

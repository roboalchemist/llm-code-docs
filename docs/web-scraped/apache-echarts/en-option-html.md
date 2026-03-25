# Source: https://echarts.apache.org/en/option.html

Title: Documentation - Apache ECharts

URL Source: https://echarts.apache.org/en/option.html

Markdown Content:
title
-----

Title component, including main title and subtitle.

In ECharts 2.x, a single instance of ECharts could contains one title component at most. However, in ECharts 3, there could be one or more than one title components. It is more useful when multiple diagrams in one instance all need titles.

**Here are some instances of different animation easing functions, among which every instance has a title component:**

### Properties

#### [title.](https://echarts.apache.org/en/option.html#title)[id](https://echarts.apache.org/en/option.html#title.id)

string

Component ID, not specified by default. If specified, it can be used to refer the component in option or API.

#### [title.](https://echarts.apache.org/en/option.html#title)[show](https://echarts.apache.org/en/option.html#title.show) = true __ Try It

boolean

Set this to `false` to prevent the title from showing

#### [title.](https://echarts.apache.org/en/option.html#title)[text](https://echarts.apache.org/en/option.html#title.text) = ''__ Try It

string

The main title text, supporting for `\n` for newlines.

[WARNING]: When enabling [toolbox.feature.saveAsImage](https://echarts.apache.org/en/option.html#toolbox.feature.saveAsImage), and [toolbox.feature.saveAsImage.name](https://echarts.apache.org/en/option.html#toolbox.feature.saveAsImage.name) is not provided, it has historically been using `title[0].text` instead. This usage is not recommended -- [toolbox.feature.saveAsImage.name](https://echarts.apache.org/en/option.html#toolbox.feature.saveAsImage.name) should always be specified explicitly; otherwise, **correctness** and **security risks** for a filename have to be considered in this `title.text` option. See document ["Security Guidelines"](https://echarts.apache.org/handbook/en/best-practices/security) for recommendations on safe usage.

#### [title.](https://echarts.apache.org/en/option.html#title)[link](https://echarts.apache.org/en/option.html#title.link) = ''

string

The hyper link of main title text.

[WARNING]: This URL string is accepted directly without any internal sanitization. **Security risks** must be considered if it comes from untrusted sources. See document ["Security Guidelines"](https://echarts.apache.org/handbook/en/best-practices/security) for recommendations on safe usage.

#### [title.](https://echarts.apache.org/en/option.html#title)[target](https://echarts.apache.org/en/option.html#title.target) = 'blank'

string

Open the hyper link of main title in specified tab.

**options:**

* `'self'` opening it in current tab

* `'blank'` opening it in a new tab

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle](https://echarts.apache.org/en/option.html#title.textStyle)

Object

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[color](https://echarts.apache.org/en/option.html#title.textStyle.color) = '#333'__ Try It

Color

main title text color.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[fontStyle](https://echarts.apache.org/en/option.html#title.textStyle.fontStyle) = 'normal'__ Try It

string

main title font style.

Options are:

* `'normal'`
* `'italic'`
* `'oblique'`

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[fontWeight](https://echarts.apache.org/en/option.html#title.textStyle.fontWeight) = 'bolder'__ Try It

string number

main title font thick weight.

Options are:

* `'normal'`
* `'bold'`
* `'bolder'`
* `'lighter'`
* 100 | 200 | 300 | 400...

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[fontFamily](https://echarts.apache.org/en/option.html#title.textStyle.fontFamily) = 'sans-serif'__ Try It

string

main title font family.

Can also be 'serif' , 'monospace', ...

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[fontSize](https://echarts.apache.org/en/option.html#title.textStyle.fontSize) = 18 __ Try It

number

main title font size.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[lineHeight](https://echarts.apache.org/en/option.html#title.textStyle.lineHeight)__ Try It

number

Line height of the text fragment.

If `lineHeight` is not set in `rich`, `lineHeight` in parent level will be used. For example:

```
{
    lineHeight: 56,
    rich: {
        a: {
            // `lineHeight` is not set, then it will be 56
        }
    }
}
```

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[width](https://echarts.apache.org/en/option.html#title.textStyle.width)__ Try It

number

Width of text block.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[height](https://echarts.apache.org/en/option.html#title.textStyle.height)__ Try It

number

Height of text block.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textBorderColor](https://echarts.apache.org/en/option.html#title.textStyle.textBorderColor)__ Try It

Color

Stroke color of the text.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textBorderWidth](https://echarts.apache.org/en/option.html#title.textStyle.textBorderWidth)__ Try It

number

Stroke line width of the text.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textBorderType](https://echarts.apache.org/en/option.html#title.textStyle.textBorderType) = 'solid'__ Try It

string number Array

Stroke line type of the text.

Possible values are:

* `'solid'`
* `'dashed'`
* `'dotted'`

Since `v5.0.0`, it can also be a number or a number array to specify the [dash array](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dasharray) of the line. With `textBorderDashOffset` , we can make the line style more flexible.

For example：

```
{

textBorderType: [5, 10],

textBorderDashOffset: 5
}
```

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textBorderDashOffset](https://echarts.apache.org/en/option.html#title.textStyle.textBorderDashOffset)__ Try It

number

Since `v5.0.0`

To set the line dash offset. With `textBorderType` , we can make the line style more flexible.

Refer to MDN [lineDashOffset](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineDashOffset) for more details.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textShadowColor](https://echarts.apache.org/en/option.html#title.textStyle.textShadowColor) = 'transparent'__ Try It

Color

Shadow color of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textShadowBlur](https://echarts.apache.org/en/option.html#title.textStyle.textShadowBlur)__ Try It

number

Shadow blue of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textShadowOffsetX](https://echarts.apache.org/en/option.html#title.textStyle.textShadowOffsetX)__ Try It

number

Shadow X offset of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[textShadowOffsetY](https://echarts.apache.org/en/option.html#title.textStyle.textShadowOffsetY)__ Try It

number

Shadow Y offset of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[overflow](https://echarts.apache.org/en/option.html#title.textStyle.overflow) = 'none'__ Try It

string

Determine how to display the text when it's overflow. Available when `width` is set.

* `'truncate'` Truncate the text and trailing with `ellipsis`.
* `'break'` Break by word
* `'breakAll'` Break by character.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[ellipsis](https://echarts.apache.org/en/option.html#title.textStyle.ellipsis) = '...'

string

Ellipsis to be displayed when `overflow` is set to `truncate`.

* `'truncate'` Truncate the overflow lines.

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[rich](https://echarts.apache.org/en/option.html#title.textStyle.rich)

Object

"Rich text styles" can be defined in this `rich` property. For example:

```
label: {
    // Styles defined in 'rich' can be applied to some fragments
    // of text by adding some markers to those fragment, like
    // `{styleName|text content text content}`.
    // `'\n'` is the newline character.
    formatter: [
        '{a|Style "a" is applied to this snippet}'
        '{b|Style "b" is applied to this snippet}This snippet use default style{x|use style "x"}'
    ].join('\n'),

    rich: {
        a: {
            color: 'red',
            lineHeight: 10
        },
        b: {
            backgroundColor: {
                image: 'xxx/xxx.jpg'
            },
            height: 40
        },
        x: {
            fontSize: 18,
            fontFamily: 'Microsoft YaHei',
            borderColor: '#449933',
            borderRadius: 4
        },
        ...
    }
}
```

For more details, see [Rich Text](https://echarts.apache.org/en/tutorial.html#Rich%20Text) please.

##### Properties

{ [<style_name>](https://echarts.apache.org/en/option.html#title.textStyle.rich.%3Cstyle_name%3E) }

#### [title.](https://echarts.apache.org/en/option.html#title)[textStyle.](https://echarts.apache.org/en/option.html#title.textStyle)[richInheritPlainLabel](https://echarts.apache.org/en/option.html#title.textStyle.richInheritPlainLabel) = true

boolean

Since `v6.0.0`

Whether rich text inherits plain text style.

This option is just for backward compatibility.

> The [label.rich / textStyle.rich](https://echarts.apache.org/en/option.html#series-scatter.label.rich)`fontStyle`, `fontWeight`, `fontSize`, `fontFamily`, `textShadowColor`, `textShadowBlur`, `textShadowOffsetX`, `textShadowOffsetY` are changed to inherit the corresponding [plain label styles](https://echarts.apache.org/en/option.html#series-scatter.label) since echarts v6. You can use `richInheritPlainLabel: false` to restore it. For example,
>
>
> ```
> option = {
>     richInheritPlainLabel: false, // In most cases, this is enough.
>     xxx1: {
>         // Can also set it here to only control this label.
>         label: {
>             richInheritPlainLabel: false,
>             rich: {/* ... */},
>         }
>     },
>     xxx2: {
>         textStyle: {
>             richInheritPlainLabel: false,
>             rich: {/* ... */},
>         }
>     }
> }
> ```

#### [title.](https://echarts.apache.org/en/option.html#title)[subtext](https://echarts.apache.org/en/option.html#title.subtext) = ''__ Try It

string

Subtitle text, supporting for `\n` for newlines.

#### [title.](https://echarts.apache.org/en/option.html#title)[sublink](https://echarts.apache.org/en/option.html#title.sublink) = ''

string

The hyper link of subtitle text.

[WARNING]: This URL string is accepted directly without any internal sanitization. **Security risks** must be considered if it comes from untrusted sources. See document ["Security Guidelines"](https://echarts.apache.org/handbook/en/best-practices/security) for recommendations on safe usage.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtarget](https://echarts.apache.org/en/option.html#title.subtarget) = 'blank'

string

Open the hyper link of subtitle in specified tab, options:

* `'self'` opening it in current tab

* `'blank'` opening it in a new tab

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle](https://echarts.apache.org/en/option.html#title.subtextStyle)

Object

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[color](https://echarts.apache.org/en/option.html#title.subtextStyle.color) = '#aaa'__ Try It

Color

subtitle text color.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[fontStyle](https://echarts.apache.org/en/option.html#title.subtextStyle.fontStyle) = 'normal'__ Try It

string

subtitle font style.

Options are:

* `'normal'`
* `'italic'`
* `'oblique'`

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[fontWeight](https://echarts.apache.org/en/option.html#title.subtextStyle.fontWeight) = 'normal'__ Try It

string number

subtitle font thick weight.

Options are:

* `'normal'`
* `'bold'`
* `'bolder'`
* `'lighter'`
* 100 | 200 | 300 | 400...

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[fontFamily](https://echarts.apache.org/en/option.html#title.subtextStyle.fontFamily) = 'sans-serif'__ Try It

string

subtitle font family.

Can also be 'serif' , 'monospace', ...

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[fontSize](https://echarts.apache.org/en/option.html#title.subtextStyle.fontSize) = 12 __ Try It

number

subtitle font size.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[align](https://echarts.apache.org/en/option.html#title.subtextStyle.align)__ Try It

string

Horizontal alignment of text, automatic by default.

Options are:

* `'left'`
* `'center'`
* `'right'`

If `align` is not set in `rich`, `align` in parent level will be used. For example:

```
{
    align: right,
    rich: {
        a: {
            // `align` is not set, then it will be right
        }
    }
}
```

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[verticalAlign](https://echarts.apache.org/en/option.html#title.subtextStyle.verticalAlign)__ Try It

string

Vertical alignment of text, automatic by default.

Options are:

* `'top'`
* `'middle'`
* `'bottom'`

If `verticalAlign` is not set in `rich`, `verticalAlign` in parent level will be used. For example:

```
{
    verticalAlign: bottom,
    rich: {
        a: {
            // `verticalAlign` is not set, then it will be bottom
        }
    }
}
```

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[lineHeight](https://echarts.apache.org/en/option.html#title.subtextStyle.lineHeight)__ Try It

number

Line height of the text fragment.

If `lineHeight` is not set in `rich`, `lineHeight` in parent level will be used. For example:

```
{
    lineHeight: 56,
    rich: {
        a: {
            // `lineHeight` is not set, then it will be 56
        }
    }
}
```

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[width](https://echarts.apache.org/en/option.html#title.subtextStyle.width)__ Try It

number

Width of text block.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[height](https://echarts.apache.org/en/option.html#title.subtextStyle.height)__ Try It

number

Height of text block.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textBorderColor](https://echarts.apache.org/en/option.html#title.subtextStyle.textBorderColor)__ Try It

Color

Stroke color of the text.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textBorderWidth](https://echarts.apache.org/en/option.html#title.subtextStyle.textBorderWidth)__ Try It

number

Stroke line width of the text.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textBorderType](https://echarts.apache.org/en/option.html#title.subtextStyle.textBorderType) = 'solid'__ Try It

string number Array

Stroke line type of the text.

Possible values are:

* `'solid'`
* `'dashed'`
* `'dotted'`

Since `v5.0.0`, it can also be a number or a number array to specify the [dash array](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dasharray) of the line. With `textBorderDashOffset` , we can make the line style more flexible.

For example：

```
{

textBorderType: [5, 10],

textBorderDashOffset: 5
}
```

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textBorderDashOffset](https://echarts.apache.org/en/option.html#title.subtextStyle.textBorderDashOffset)__ Try It

number

Since `v5.0.0`

To set the line dash offset. With `textBorderType` , we can make the line style more flexible.

Refer to MDN [lineDashOffset](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineDashOffset) for more details.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textShadowColor](https://echarts.apache.org/en/option.html#title.subtextStyle.textShadowColor) = 'transparent'__ Try It

Color

Shadow color of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textShadowBlur](https://echarts.apache.org/en/option.html#title.subtextStyle.textShadowBlur)__ Try It

number

Shadow blue of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textShadowOffsetX](https://echarts.apache.org/en/option.html#title.subtextStyle.textShadowOffsetX)__ Try It

number

Shadow X offset of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[textShadowOffsetY](https://echarts.apache.org/en/option.html#title.subtextStyle.textShadowOffsetY)__ Try It

number

Shadow Y offset of the text itself.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[overflow](https://echarts.apache.org/en/option.html#title.subtextStyle.overflow) = 'none'__ Try It

string

Determine how to display the text when it's overflow. Available when `width` is set.

* `'truncate'` Truncate the text and trailing with `ellipsis`.
* `'break'` Break by word
* `'breakAll'` Break by character.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[ellipsis](https://echarts.apache.org/en/option.html#title.subtextStyle.ellipsis) = '...'

string

Ellipsis to be displayed when `overflow` is set to `truncate`.

* `'truncate'` Truncate the overflow lines.

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[rich](https://echarts.apache.org/en/option.html#title.subtextStyle.rich)

Object

"Rich text styles" can be defined in this `rich` property. For example:

```
label: {
    // Styles defined in 'rich' can be applied to some fragments
    // of text by adding some markers to those fragment, like
    // `{styleName|text content text content}`.
    // `'\n'` is the newline character.
    formatter: [
        '{a|Style "a" is applied to this snippet}'
        '{b|Style "b" is applied to this snippet}This snippet use default style{x|use style "x"}'
    ].join('\n'),

    rich: {
        a: {
            color: 'red',
            lineHeight: 10
        },
        b: {
            backgroundColor: {
                image: 'xxx/xxx.jpg'
            },
            height: 40
        },
        x: {
            fontSize: 18,
            fontFamily: 'Microsoft YaHei',
            borderColor: '#449933',
            borderRadius: 4
        },
        ...
    }
}
```

For more details, see [Rich Text](https://echarts.apache.org/en/tutorial.html#Rich%20Text) please.

##### Properties

{ [<style_name>](https://echarts.apache.org/en/option.html#title.subtextStyle.rich.%3Cstyle_name%3E) }

#### [title.](https://echarts.apache.org/en/option.html#title)[subtextStyle.](https://echarts.apache.org/en/option.html#title.subtextStyle)[richInheritPlainLabel](https://echarts.apache.org/en/option.html#title.subtextStyle.richInheritPlainLabel) = true

boolean

Since `v6.0.0`

Whether rich text inherits plain text style.

This option is just for backward compatibility.

> The [label.rich / textStyle.rich](https://echarts.apache.org/en/option.html#series-scatter.label.rich)`fontStyle`, `fontWeight`, `fontSize`, `fontFamily`, `textShadowColor`, `textShadowBlur`, `textShadowOffsetX`, `textShadowOffsetY` are changed to inherit the corresponding [plain label styles](https://echarts.apache.org/en/option.html#series-scatter.label) since echarts v6. You can use `richInheritPlainLabel: false` to restore it. For example,
>
>
> ```
> option = {
>     richInheritPlainLabel: false, // In most cases, this is enough.
>     xxx1: {
>         // Can also set it here to only control this label.
>         label: {
>             richInheritPlainLabel: false,
>             rich: {/* ... */},
>         }
>     },
>     xxx2: {
>         textStyle: {
>             richInheritPlainLabel: false,
>             rich: {/* ... */},
>         }
>     }
> }
> ```

#### [title.](https://echarts.apache.org/en/option.html#title)[textAlign](https://echarts.apache.org/en/option.html#title.textAlign) = 'auto'__ Try It

string

The horizontal align of the component (including "text" and "subtext").

Optional values: `'auto'`, `'left'`, `'right'`, `'center'`.

#### [title.](https://echarts.apache.org/en/option.html#title)[textVerticalAlign](https://echarts.apache.org/en/option.html#title.textVerticalAlign) = 'auto'__ Try It

string

The vertical align of the component (including "text" and "subtext").

Optional values: `'auto'`, `'top'`, `'bottom'`, `'middle'`.

#### [title.](https://echarts.apache.org/en/option.html#title)[triggerEvent](https://echarts.apache.org/en/option.html#title.triggerEvent)

boolean

Set this to `true` to enable triggering events

#### [title.](https://echarts.apache.org/en/option.html#title)[padding](https://echarts.apache.org/en/option.html#title.padding) = 5 __ Try It

number Array

title space around content. The unit is px. Default values for each position are 5. And they can be set to different values with left, right, top, and bottom.

Examples:

```
// Set padding to be 5
padding: 5
// Set the top and bottom paddings to be 5, and left and right paddings to be 10
padding: [5, 10]
// Set each of the four paddings separately
padding: [
    5,  // up
    10, // right
    5,  // down
    10, // left
]
```

#### [title.](https://echarts.apache.org/en/option.html#title)[itemGap](https://echarts.apache.org/en/option.html#title.itemGap) = 10 __ Try It

number

The gap between the main title and subtitle.

#### [title.](https://echarts.apache.org/en/option.html#title)[zlevel](https://echarts.apache.org/en/option.html#title.zlevel)

number

`zlevel` value of all graphical elements in .

`zlevel` is used to make layers with Canvas. Graphical elements with different `zlevel` values will be placed in different Canvases, which is a common optimization technique. We can put those frequently changed elements (like those with animations) to a separate `zlevel`. Notice that too many Canvases will increase memory cost, and should be used carefully on mobile phones to avoid crash.

Canvases with bigger `zlevel` will be placed on Canvases with smaller `zlevel`.

#### [title.](https://echarts.apache.org/en/option.html#title)[z](https://echarts.apache.org/en/option.html#title.z) = 2

number

`z` value of all graphical elements in , which controls order of drawing graphical components. Components with smaller `z` values may be overwritten by those with larger `z` values.

`z` has a lower priority to `zlevel`, and will not create new Canvas.

#### [title.](https://echarts.apache.org/en/option.html#title)[left](https://echarts.apache.org/en/option.html#title.left) = 'auto'__ Try It

string number

Distance between title component and the left side of the container.

`left` can be a pixel value like `20`; it can also be a percentage value relative to the container width like `'20%'`; and it can also be `'left'`, `'center'`, or `'right'`.

If the `left` value is set to be `'left'`, `'center'`, or `'right'`, then the component will be aligned automatically based on position.

#### [title.](https://echarts.apache.org/en/option.html#title)[top](https://echarts.apache.org/en/option.html#title.top) = 'auto'__ Try It

string number

Distance between title component and the top side of the container.

`top` can be a pixel value like `20`; it can also be a percentage value relative to the container height like `'20%'`; and it can also be `'top'`, `'middle'`, or `'bottom'`.

If the `top` value is set to be `'top'`, `'middle'`, or `'bottom'`, then the component will be aligned automatically based on position.

#### [title.](https://echarts.apache.org/en/option.html#title)[right](https://echarts.apache.org/en/option.html#title.right) = 'auto'__ Try It

string number

Distance between title component and the right side of the container.

`right` can be a pixel value like `20`; it can also be a percentage value relative to the container width like `'20%'`.

Adaptive by default.

#### [title.](https://echarts.apache.org/en/option.html#title)[bottom](https://echarts.apache.org/en/option.html#title.bottom) = 'auto'__ Try It

string number

Distance between title component and the bottom side of the container.

`bottom` can be a pixel value like `20`; it can also be a percentage value relative to the container height like `'20%'`.

Adaptive by default.

#### [title.](https://echarts.apache.org/en/option.html#title)[coordinateSystem](https://echarts.apache.org/en/option.html#title.coordinateSystem) = 'none'

string

Since `v6.0.0`

Specifies another coordinate system component on which this `title` is laid out.

Options:

* `null`/`undefined`/`'none'`

Not laid out in any coordinate system; instead, laid out independently.

* `'calendar'`

Lay out based on a [calendar coordinate system](https://echarts.apache.org/en/option.html#calendar). When multiple calendar coordinate systems exist within an ECharts instance, the corresponding system should be specified using [calendarIndex](https://echarts.apache.org/en/option.html#title.calendarIndex) or [calendarId](https://echarts.apache.org/en/option.html#title.calendarId).

* `'matrix'`

Lay out based on a [matrix coordinate system](https://echarts.apache.org/en/option.html#matrix). When multiple matrix coordinate systems exist within an ECharts instance, the corresponding system should be specified using [matrixIndex](https://echarts.apache.org/en/option.html#title.matrixIndex) or [matrixId](https://echarts.apache.org/en/option.html#title.matrixId).

**Support for series and component layout on coordinate systems:**

The leftmost column lists the series and components that will be laid out (coordinate systems themselves are also components), and the topmost row lists the coordinate systems that can be laid out on.

|  | no coord sys | [grid](https://echarts.apache.org/en/option.html#grid) (cartesian2d) | [polar](https://echarts.apache.org/en/option.html#polar) | [geo](https://echarts.apache.org/en/option.html#geo) | [singleAxis](https://echarts.apache.org/en/option.html#singleAxis) | [radar](https://echarts.apache.org/en/option.html#radar) | [parallel](https://echarts.apache.org/en/option.html#parallel) | [calendar](https://echarts.apache.org/en/option.html#calendar) | [matrix](https://echarts.apache.org/en/option.html#matrix) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [grid](https://echarts.apache.org/en/option.html#grid) (cartesian2d) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [polar](https://echarts.apache.org/en/option.html#polar) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [geo](https://echarts.apache.org/en/option.html#geo) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [singleAxis](https://echarts.apache.org/en/option.html#singleAxis) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [calendar](https://echarts.apache.org/en/option.html#calendar) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [matrix](https://echarts.apache.org/en/option.html#matrix) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [series-line](https://echarts.apache.org/en/option.html#series-line) | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) |
| [series-bar](https://echarts.apache.org/en/option.html#series-bar) | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) |
| [series-pie](https://echarts.apache.org/en/option.html#series-pie) | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| [series-scatter](https://echarts.apache.org/en/option.html#series-scatter) | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| [series-effectScatter](https://echarts.apache.org/en/option.html#series-effectScatter) | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| [series-radar](https://echarts.apache.org/en/option.html#series-radar) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ (✅ if via [radar](https://echarts.apache.org/en/option.html#radar) coord sys) | ❌ (✅ if via [radar](https://echarts.apache.org/en/option.html#radar) coord sys) |
| [series-tree](https://echarts.apache.org/en/option.html#series-tree) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-treemap](https://echarts.apache.org/en/option.html#series-treemap) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-sunburst](https://echarts.apache.org/en/option.html#series-sunburst) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-boxplot](https://echarts.apache.org/en/option.html#series-boxplot) | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) |
| [series-candlestick](https://echarts.apache.org/en/option.html#series-candlestick) | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) |
| [series-heatmap](https://echarts.apache.org/en/option.html#series-heatmap) | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-map](https://echarts.apache.org/en/option.html#series-map) | ✅ (create a geo coord sys exclusively) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-parallel](https://echarts.apache.org/en/option.html#series-parallel) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ (✅ if via [parallel](https://echarts.apache.org/en/option.html#parallel) coord sys) | ❌ (✅ if via [parallel](https://echarts.apache.org/en/option.html#parallel) coord sys) |
| [series-lines](https://echarts.apache.org/en/option.html#series-lines) | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ (✅ if via another coord sys like [geo](https://echarts.apache.org/en/option.html#geo)) | ❌ (✅ if via another coord sys like [geo](https://echarts.apache.org/en/option.html#geo)) |
| [series-graph](https://echarts.apache.org/en/option.html#series-graph) | ✅ (create a "view" coord sys exclusively) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-sankey](https://echarts.apache.org/en/option.html#series-sankey) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-funnel](https://echarts.apache.org/en/option.html#series-funnel) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-gauge](https://echarts.apache.org/en/option.html#series-gauge) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [series-pictorialBar](https://echarts.apache.org/en/option.html#series-pictorialBar) | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) | ❌ (✅ if via another coord sys like [grid](https://echarts.apache.org/en/option.html#grid)) |
| [series-themeRiver](https://echarts.apache.org/en/option.html#series-themeRiver) | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ (✅ if via another coord sys like [singleAxis](https://echarts.apache.org/en/option.html#singleAxis)) | ❌ (✅ if via another coord sys like [singleAxis](https://echarts.apache.org/en/option.html#singleAxis)) |
| [series-chord](https://echarts.apache.org/en/option.html#series-chord) | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| [title](https://echarts.apache.org/en/option.html#title) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [legend](https://echarts.apache.org/en/option.html#legend) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [dataZoom](https://echarts.apache.org/en/option.html#dataZoom) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [visualMap](https://echarts.apache.org/en/option.html#visualMap) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [toolbox](https://echarts.apache.org/en/option.html#toolbox) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [timeline](https://echarts.apache.org/en/option.html#timeline) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| [thumbnail](https://echarts.apache.org/en/option.html#thumbnail) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |

See also [title.coordinateSystemUsage](https://echarts.apache.org/en/option.html#title.coordinateSystemUsage).

#### [title.](https://echarts.apache.org/en/option.html#title)[coordinateSystemUsage](https://echarts.apache.org/en/option.html#title.coordinateSystemUsage) = 'box'

string

Since `v6.0.0`

Specify how to lay out this `title` based on the specified [coordinateSystem](https://echarts.apache.org/en/option.html#title.coordinateSystem).

In most cases, there is no need to specify `coordinateSystemUsage`, unless the default behavior is unexpected.

Options:

* `'data'`: **(Not applicable in [title](https://echarts.apache.org/en/option.html#title))**

Each data item of a series (e.g., each `series.data[i]`) is laid out separately based on the specified coordinate system. Currently no non-series component supports `coordinateSystemUsage: 'data'`.

* `'box'`:

The entire series or component is laid out as a whole based on the specified coordinate system - that is, the overall bounding rect or basic anchor point is calculated relative to the system.

    *   For example, a [grid component](https://echarts.apache.org/en/option.html#grid) can be laid out in a [matrix coordinate system](https://echarts.apache.org/en/option.html#matrix) or a [calendar coordinate system](https://echarts.apache.org/en/option.html#calendar), where its layout rectangle is calculated by the specified [title.coords](https://echarts.apache.org/en/option.html#title.coords) in that system. See example [sparkline in matrix](https://echarts.apache.org/examples/en/editor.html?c=matrix-sparkline&edit=1&reset=1).
    *   For example, a [pie series](https://echarts.apache.org/en/option.html#series-pie) or a [chord series](https://echarts.apache.org/en/option.html#series-chord) can be laid out in a [geo coordinate system](https://echarts.apache.org/en/option.html#geo) or a [cartesian2d coordinate system](https://echarts.apache.org/en/option.html#grid), where the center is calculated by the specified [series-pie.coords](https://echarts.apache.org/en/option.html#series-pie.coords) or [series-pie.center](https://echarts.apache.org/en/option.html#series-pie.center) in that system. See example [pie in geo](https://echarts.apache.org/examples/en/editor.html?c=map-iceland-pie&edit=1&reset=1).

See also [title.coordinateSystem](https://echarts.apache.org/en/option.html#title.coordinateSystem).

#### [title.](https://echarts.apache.org/en/option.html#title)[coord](https://echarts.apache.org/en/option.html#title.coord)

Array number string

Since `v6.0.0`

When [coordinateSystemUsage](https://echarts.apache.org/en/option.html#title.coordinateSystemUsage) is `'box'`, `coord` is used as the input to the coordinate system and calculate the layout rectangle or anchor point.

Examples: [sparkline in matrix](https://echarts.apache.org/examples/en/editor.html?c=matrix-sparkline&edit=1&reset=1), [grpah in matrix](https://echarts.apache.org/examples/en/editor.html?c=doc-example/matrix-graph-box&edit=1&reset=1).

> Note: when [coordinateSystemUsage](https://echarts.apache.org/en/option.html#title.coordinateSystemUsage) is `'data'`, the input of coordinate system is `series.data[i]` rather than this `coord`.

The format this `coord` is defined by each coordinate system, and it's the same as the second parameter of [chart.convertToPixel](https://echarts.apache.org/en/api.html#echartsInstance.convertToPixel).

#### [title.](https://echarts.apache.org/en/option.html#title)[calendarIndex](https://echarts.apache.org/en/option.html#title.calendarIndex)

number

Since `v6.0.0`

The index of the [calendar coordinate system](https://echarts.apache.org/en/option.html#calendar) to base on. When mutiple `calendar` exist within an ECharts instance, use this to specify the corresponding `calendar`.

#### [title.](https://echarts.apache.org/en/option.html#title)[calendarId](https://echarts.apache.org/en/option.html#title.calendarId) = undefined

number

Since `v6.0.0`

The id of the [calendar coordinate system](https://echarts.apache.org/en/option.html#calendar) to base on. When mutiple `calendar` exist within an ECharts instance, use this to specify the corresponding `calendar`.

#### [title.](https://echarts.apache.org/en/option.html#title)[matrixIndex](https://echarts.apache.org/en/option.html#title.matrixIndex)

number

Since `v6.0.0`

The index of the [matrix coordinate system](https://echarts.apache.org/en/option.html#matrix) to base on. When mutiple `matrix` exist within an ECharts instance, use this to specify the corresponding `matrix`.

#### [title.](https://echarts.apache.org/en/option.html#title)[matrixId](https://echarts.apache.org/en/option.html#title.matrixId) = undefined

number

Since `v6.0.0`

The id of the [matrix coordinate system](https://echarts.apache.org/en/option.html#matrix) to base on. When mutiple `matrix` exist within an ECharts instance, use this to specify the corresponding `matrix`.

#### [title.](https://echarts.apache.org/en/option.html#title)[backgroundColor](https://echarts.apache.org/en/option.html#title.backgroundColor) = 'transparent'__ Try It

Color

Background color of title, which is transparent by default.

> Color can be represented in RGB, for example `'rgb(128, 128, 128)'`. RGBA can be used when you need alpha channel, for example `'rgba(128, 128, 128, 0.5)'`. You may also use hexadecimal format, for example `'#ccc'`.

#### [title.](https://echarts.apache.org/en/option.html#title)[borderColor](https://echarts.apache.org/en/option.html#title.borderColor) = '#ccc'__ Try It

Color

Border color of title. Support the same color format as backgroundColor.

#### [title.](https://echarts.apache.org/en/option.html#title)[borderWidth](https://echarts.apache.org/en/option.html#title.borderWidth) = 1 __ Try It

number

Border width of title.

#### [title.](https://echarts.apache.org/en/option.html#title)[borderRadius](https://echarts.apache.org/en/option.html#title.borderRadius)__ Try It

number Array

The radius of rounded corner. Its unit is px. And it supports use array to respectively specify the 4 corner radiuses.

For example:

```
borderRadius: 5, // consistently set the size of 4 rounded corners
borderRadius: [5, 5, 0, 0] // (clockwise upper left, upper right, bottom right and bottom left)
```

#### [title.](https://echarts.apache.org/en/option.html#title)[shadowBlur](https://echarts.apache.org/en/option.html#title.shadowBlur)__ Try It

number

Size of shadow blur. This attribute should be used along with `shadowColor`,`shadowOffsetX`, `shadowOffsetY` to set shadow to component.

For example:

```
{
    shadowColor: 'rgba(0, 0, 0, 0.5)',
    shadowBlur: 10
}
```

**Attention**: This property works only if `show: true` is configured and `backgroundColor` is defined other than `transparent`.

#### [title.](https://echarts.apache.org/en/option.html#title)[shadowColor](https://echarts.apache.org/en/option.html#title.shadowColor)__ Try It

Color

Shadow color. Support same format as `color`.

**Attention**: This property works only if `show: true` configured.

#### [title.](https://echarts.apache.org/en/option.html#title)[shadowOffsetX](https://echarts.apache.org/en/option.html#title.shadowOffsetX)__ Try It

number

Offset distance on the horizontal direction of shadow.

**Attention**: This property works only if `show: true` configured.

#### [title.](https://echarts.apache.org/en/option.html#title)[shadowOffsetY](https://echarts.apache.org/en/option.html#title.shadowOffsetY)__ Try It

number

Offset distance on the vertical direction of shadow.

**Attention**: This property works only if `show: true` configured.

Preview

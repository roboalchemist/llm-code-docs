# Source: https://recharts.github.io/en-US/guide/barAlignment/

# Aligning Bars in a BarChart

BarChart comes with some default settings for aligning bars within their categories. You can use the following props to customize the alignment:

- **barSize**: Controls the width of each Bar. This can be defined in pixels or in percent. If undefined, it\'s computed based on the available space and number of bars.
- **barGap**: Controls the distance between Bars in the same category. Increasing this gap will shrink the Bar rectangles. This can be defined in pixels or in percent.
- **barCategoryGap**: This prop controls the gap between categories. It can be specified as a percentage of the category width or as a fixed pixel value. This is a shortcut for setting the inner and outer padding of the band scale used for the XAxis. Notice how changing this value affects the alignment of the bars and XAxis ticks below. This can be defined in pixels or in percent.
- **scale**: You can provide a custom band scale to the XAxis component to have more control over the alignment of bars within their categories. This allows you to set properties like `paddingInner`, `paddingOuter`, and `align` on the scale itself. See [d3-scale/band docs![Link opens in new tab](data:image/svg+xml,%3c!--%20SVG%20Icon:%20Open%20in%20New%20Window%20/%20External%20Link%20-%20This%20SVG%20is%20designed%20to%20be%20placed%20next%20to%20a%20link.%20-%20The%20color%20will%20be%20inherited%20from%20the%20parent%20text%20element's%20color%20(e.g.,%20the%20link's%20color)%20because%20%60stroke%60%20is%20set%20to%20'currentColor'.%20--%3e%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='16'%20height='16'%20viewBox='0%200%2032%2024'%20fill='none'%20stroke='currentColor'%20stroke-width='2.5'%20stroke-linecap='round'%20stroke-linejoin='round'%20style='display:%20inline-block;%20vertical-align:%20middle;%20margin-left:%204px;'%20%3e%3cpath%20d='M18%2013v6a2%202%200%200%201-2%202H5a2%202%200%200%201-2-2V8a2%202%200%200%201%202-2h6'/%3e%3cpolyline%20points='15%203%2021%203%2021%209'/%3e%3cline%20x1='10'%20y1='14'%20x2='21'%20y2='3'/%3e%3c/svg%3e)](https://d3js.org/d3-scale/band) and [d3-scaleband notebook![Link opens in new tab](data:image/svg+xml,%3c!--%20SVG%20Icon:%20Open%20in%20New%20Window%20/%20External%20Link%20-%20This%20SVG%20is%20designed%20to%20be%20placed%20next%20to%20a%20link.%20-%20The%20color%20will%20be%20inherited%20from%20the%20parent%20text%20element's%20color%20(e.g.,%20the%20link's%20color)%20because%20%60stroke%60%20is%20set%20to%20'currentColor'.%20--%3e%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='16'%20height='16'%20viewBox='0%200%2032%2024'%20fill='none'%20stroke='currentColor'%20stroke-width='2.5'%20stroke-linecap='round'%20stroke-linejoin='round'%20style='display:%20inline-block;%20vertical-align:%20middle;%20margin-left:%204px;'%20%3e%3cpath%20d='M18%2013v6a2%202%200%200%201-2%202H5a2%202%200%200%201-2-2V8a2%202%200%200%201%202-2h6'/%3e%3cpolyline%20points='15%203%2021%203%2021%209'/%3e%3cline%20x1='10'%20y1='14'%20x2='21'%20y2='3'/%3e%3c/svg%3e)](https://observablehq.com/@d3/d3-scaleband) for more information on band scales.

## Bar alignment playground

Source codeHook inspectorControls

  ------------------------- -- -----
  BarChart.barGap              10%
  BarChart.barCategoryGap      10%
  bandScale.paddingInner       0
  bandScale.paddingOuter       0.8
  bandScale.align              0.7
  ------------------------- -- -----
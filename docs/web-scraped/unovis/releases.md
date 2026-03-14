# Source: https://unovis.dev/releases

Title: Blog | Unovis

URL Source: https://unovis.dev/releases

Markdown Content:
[Angular LTS Support](https://unovis.dev/releases/1.7-angular)
--------------------------------------------------------------

January 23, 2026 ·

2 min read

[![Image 1: Surya Hanumandla](https://avatars.githubusercontent.com/u/7765847)](https://github.com/suryahanumandla)

Maintainer, Key Contributor

[![Image 2: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

Overview[​](https://unovis.dev/releases#overview "Direct link to Overview")
---------------------------------------------------------------------------

Effective with the next major release (1.7) of Unovis, we will only support Angular versions that are currently in Long-Term Support (LTS) as defined by [Angular's version support policy](https://angular.dev/reference/versions).

What This Means[​](https://unovis.dev/releases#what-this-means "Direct link to What This Means")
------------------------------------------------------------------------------------------------

Angular follows a predictable release cycle where each major version receives:

*   **6 months** of active support (regular updates and patches)
*   **12 months** of long-term support (critical fixes and security patches)
*   After 18 months, versions reach end-of-life

Unovis will support all Angular versions currently in their LTS window. As Angular versions reach end-of-life, Unovis will drop support for those versions in our next minor release.

Current Status[​](https://unovis.dev/releases#current-status "Direct link to Current Status")
---------------------------------------------------------------------------------------------

Currently, Unovis supports Angular versions **12 through 19** (`"@angular/common": "12 - 19"` in our peer dependencies). Moving forward, we will only support Angular versions that are in active support or LTS.

Why This Change?[​](https://unovis.dev/releases#why-this-change "Direct link to Why This Change?")
--------------------------------------------------------------------------------------------------

1.   **Security**: Unsupported Angular versions no longer receive security updates, which can pose risks to applications
2.   **Modern Features**: Allows us to leverage newer Angular features and APIs (standalone components, signals, improved TypeScript support, etc.)
3.   **Maintenance Efficiency**: Reduces the testing matrix and allows our team to focus on supporting current Angular versions with better quality
4.   **Industry Standard**: This aligns with how other major Angular libraries (Angular Material, NgRx, etc.) manage version support

Timeline[​](https://unovis.dev/releases#timeline "Direct link to Timeline")
---------------------------------------------------------------------------

*   **Effective Date**: Next major version release of Unovis
*   **Transition Period**: Current versions of Unovis will continue to support the existing range until the next major release

What You Should Do[​](https://unovis.dev/releases#what-you-should-do "Direct link to What You Should Do")
---------------------------------------------------------------------------------------------------------

1.   **Check Your Angular Version**: Run `ng version` to see which Angular version you're using
2.   **Plan Your Upgrade**: If you're using an Angular version that's approaching end-of-life, plan to upgrade
3.   **Stay Informed**: Follow [Angular's release schedule](https://angular.dev/reference/versions) to know when versions enter and exit LTS

References[​](https://unovis.dev/releases#references "Direct link to References")
---------------------------------------------------------------------------------

*   [Angular Version Support Policy](https://angular.dev/reference/versions)
*   [Angular Material Version Support](https://github.com/angular/components)
*   [Unovis Documentation](https://unovis.dev/)

Feedback[​](https://unovis.dev/releases#feedback "Direct link to Feedback")
---------------------------------------------------------------------------

We value your input! If you have concerns or questions about this policy change, please:

*   Open an issue on [GitHub](https://github.com/f5/unovis/issues)
*   Join the discussion in our community channels
*   Reach out to the maintainers

* * *

**The Unovis Team**

[Release 1.6](https://unovis.dev/releases/1.6)
----------------------------------------------

August 14, 2025 ·

5 min read

[![Image 3: Qian Liu](https://avatars.githubusercontent.com/u/5026041)](https://github.com/lee00678)

Maintainer, Key Contributor

[![Image 4: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

[![Image 5: Surya Hanumandla](https://avatars.githubusercontent.com/u/7765847)](https://github.com/suryahanumandla)

Maintainer, Key Contributor

Version `1.6` of _Unovis_ is here! This is one of our most feature-packed releases yet, bringing exciting new components, enhanced graph functionality, improved axis customization, and numerous quality of life improvements.

We're excited to welcome our new first-time contributors to the Unovis community: [@dennisadriaans](https://github.com/dennisadriaans), [@curran](https://github.com/curran), [@50rayn](https://github.com/50rayn), and [@devgru](https://github.com/devgru). Thank you for your valuable contributions! 🎉

Release Highlights[​](https://unovis.dev/releases#release-highlights "Direct link to Release Highlights")
---------------------------------------------------------------------------------------------------------

### 📊 New Components: Treemap, Plotline, Plotband & Rolling Pin Legend[​](https://unovis.dev/releases#-new-components-treemap-plotline-plotband--rolling-pin-legend "Direct link to 📊 New Components: Treemap, Plotline, Plotband & Rolling Pin Legend")

Introducing four new components:

**_Treemap_**

*   Hierarchical data visualization with customizable layers
*   Rich styling options including `tileColor`, `tilePadding`, `tileBorderRadius` and `lightnessVariationAmount`
*   Interactive features with hover states: `--vis-treemap-tile-hover-stroke-color`, `--vis-treemap-tile-hover-stroke-opacity`

**_Plotline_** - Draw precise reference lines across your charts:

![Image 6: image](https://github.com/user-attachments/assets/b5fa5b43-fbc4-4485-aa85-504009f90e77)

*   Support for both X and Y axis orientation
*   Customizable line styles (solid, dashed, dotted)
*   Configurable colors, widths, and positioning
*   Works with all XY components

**_Plotband_** - Highlight ranges and areas in your visualizations:

![Image 7: image](https://github.com/user-attachments/assets/ceec5a52-2dfc-457b-a829-764b95e7f319)

*   Create horizontal or vertical bands across chart areas
*   Customizable colors with transparency support
*   Flexible labeling with multiple positioning options

**_Rolling Pin Legend_** - Compact legend for displaying color scales:

![Image 8: image](https://github.com/user-attachments/assets/53823036-8260-4d8a-a5b6-0c85555443a7)

*   Displays color gradients in a horizontal rolling pin format
*   Left and right label support for scale endpoints
*   Customizable font sizes and styling

Check out _Plotline_'s [documentation](https://unovis.dev/docs/auxiliary/Plotline), _Plotband_'s [documentation](https://unovis.dev/docs/auxiliary/Plotband), _Treemap_'s [documentation](https://unovis.dev/docs/misc/Treemap), and _Rolling Pin Legend_'s [documentation](https://unovis.dev/docs/auxiliary/RollingPinLegend) with examples to learn how to use them.

### 🎯 Enhanced Crosshair Component[​](https://unovis.dev/releases#-enhanced-crosshair-component "Direct link to 🎯 Enhanced Crosshair Component")

Allow enforcement of crosshair display at certain position, this can be used to enable synchronized crosshair display

### 📈 Line Chart Interpolation[​](https://unovis.dev/releases#-line-chart-interpolation "Direct link to 📈 Line Chart Interpolation")

New interpolation feature for handling missing data in line charts:

*   `interpolateMissingData` property fills data gaps with dashed lines
*   Customizable appearance with CSS variables

`--vis-line-gapfill-stroke-dasharray: 2 3;    --vis-line-gapfill-stroke-opacity: 0.8;    --vis-line-gapfill-stroke-dashoffset: 0;`

*   Works seamlessly with fallback values for better data visualization

### 🔘 Bullet Legend Enhancements[​](https://unovis.dev/releases#-bullet-legend-enhancements "Direct link to 🔘 Bullet Legend Enhancements")

_Bullet Legend_ now supports multiple colors per item, enabling more sophisticated legend designs:

![Image 9: image](https://github.com/user-attachments/assets/4a08a5c6-dd59-4744-b0a6-03f4bd4e0e3f)

*   Multiple color arrays for complex legend items

### 📏 Axis Customization[​](https://unovis.dev/releases#-axis-customization "Direct link to 📏 Axis Customization")

New CSS variables for greater axis styling control:

*   `--vis-axis-line-stroke-color`: Customize axis line color
*   `--vis-axis-line-stroke-width`: Control axis line thickness
*   Better separation between domain line and tick styling
*   **Label Trim and Wrap**: Add trim and wrap functionality to axis labels for better text handling

![Image 10: Screenshot 2025-08-13 at 12 36 45 PM](https://github.com/user-attachments/assets/49ad7935-0f24-4081-95a3-259ca06a1e3c)

### ⏱️ Timeline Component Enhancements[​](https://unovis.dev/releases#%EF%B8%8F-timeline-component-enhancements "Direct link to ⏱️ Timeline Component Enhancements")

Major updates to the Timeline component with new features and improved functionality:

*   **Row Icons**: Support for enhanced visual categorization with icons alongside row labels
*   **Line Icons**: Add start and end icons to timeline lines with configurable positioning
*   **Arrow Support**: Connect related timeline entries with customizable arrows allowing user to create Gantt Charts
*   **Hover Styles**: Better visual feedback with configurable hover states
*   **Animation Control**: Configurable animation positions for line enter/exit transitions
*   **Label Positioning**: Improved label positioning and clipping behavior with dedicated clipPath
*   `labelTextAlign`: Adds `labelTextAlign` config option to Timeline component to control label alignment

### 🔗 Graph Component Updates[​](https://unovis.dev/releases#-graph-component-updates "Direct link to 🔗 Graph Component Updates")

Continued improvements to the Graph component:

*   Enhanced panel documentation and examples
*   Configurable node and group spacing in Parallel layouts ([doc](https://unovis.dev/docs/networks-and-flows/Graph#fine-tuning-node-and-sub-group-spacing))

Other Changes[​](https://unovis.dev/releases#other-changes "Direct link to Other Changes")
------------------------------------------------------------------------------------------

### Enhancements[​](https://unovis.dev/releases#enhancements "Direct link to Enhancements")

*   Component | Graph: Enhanced panel documentation and examples [#616](https://github.com/f5/unovis/pull/616)
*   Container | XY: Handle edge cases when `scaleByDomain` is `true`[#588](https://github.com/f5/unovis/pull/588)
*   Website | Gallery: New custom nodes graph with tooltips example [#603](https://github.com/f5/unovis/pull/603)
*   Website | Gallery: New patchy line chart gallery example [#558](https://github.com/f5/unovis/pull/558)
*   Website | Gallery: New stacked area chart with attributes example [#597](https://github.com/f5/unovis/pull/597)
*   Website | Docs: Enhanced documentation for multiple components

### Bug Fixes[​](https://unovis.dev/releases#bug-fixes "Direct link to Bug Fixes")

*   Component | Tooltip: Fix dynamic config retrieval for mousemove handler [#606](https://github.com/f5/unovis/pull/606)
*   Component | Graph: Fix link flow group dot issue [#575](https://github.com/f5/unovis/pull/575)
*   Component | Graph: Fix link flow animation update [#577](https://github.com/f5/unovis/pull/577)
*   Component | Timeline: Fix icon data binding, ordinal scale domain, and arrow exit transition [#536](https://github.com/f5/unovis/pull/536)
*   Solid | Bug: Component destroy method [#602](https://github.com/f5/unovis/pull/602)
*   Core | Types: Making `fontSize` optional in `UnovisText`[#585](https://github.com/f5/unovis/pull/585)

### Quality of Life Improvements[​](https://unovis.dev/releases#quality-of-life-improvements "Direct link to Quality of Life Improvements")

*   TS: Replace deprecated JSX.Element with React.ReactNode [#545](https://github.com/f5/unovis/pull/545)
*   Testing: Continued improvements to visual testing infrastructure

[Release 1.5](https://unovis.dev/releases/1.5)
----------------------------------------------

December 4, 2024 ·

3 min read

[![Image 11: Qian Liu](https://avatars.githubusercontent.com/u/5026041)](https://github.com/lee00678)

Maintainer, Key Contributor

[![Image 12: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

[![Image 13: Rebecca Bol](https://avatars.githubusercontent.com/u/52078477)](https://github.com/reb-dev)

Maintainer, Key Contributor

Version `1.5` of _Unovis_ has arrived! This release is packed with enhancements, including full support for Solid; compatibility with React 19 and Angular 19; many Graph component tweaks; exciting new features; and numerous bug fixes.

Release Highlights[​](https://unovis.dev/releases#release-highlights "Direct link to Release Highlights")
---------------------------------------------------------------------------------------------------------

### 🎉 Solid Support[​](https://unovis.dev/releases#-solid-support "Direct link to 🎉 Solid Support")

_Unovis_ now works with Solid — one of the most performant JSX frameworks. Thanks to [@hngngn](https://github.com/hngngn) for this amazing [contribution](https://github.com/f5/unovis/pull/469)!

### 🎊 React 19 and Angular 19[​](https://unovis.dev/releases#--react-19-and-angular-19 "Direct link to 🎊  React 19 and Angular 19")

_Unovis_ now also support Angular 19 and React 19. 

 Calling for Svelte 5 support contribution ([discussion](https://github.com/f5/unovis/issues/500))! Huge thanks to [@pingu-codes](https://github.com/pingu-codes) for your incredible help with Svelte support! 🚀.

### 🔗 Graph[​](https://unovis.dev/releases#-graph "Direct link to 🔗 Graph")

A ton of new features were added to _Graph_:

*   Provide your own functions to render nodes allowing you to highly customize how the graph looks ([docs](https://unovis.dev/docs/networks-and-flows/Graph#custom-rendering-15)).

*   Post-Layout ([docs](https://unovis.dev/docs/networks-and-flows/Graph#post-layout-customization-15)) and Post-Render Customization ([docs](https://unovis.dev/docs/networks-and-flows/Graph#post-render-customization-15)) allowing you to modify the layout of the graph on the fly and render additional layers with D3.

*   Provide custom SVG icon to link labels ([docs](https://unovis.dev/docs/networks-and-flows/Graph#labels-updated-in-15)).

*   Zoom start/end and node dragging callbacks ([docs](https://unovis.dev/docs/networks-and-flows/Graph#pan--zoom--drag)).

*   Fit view to specific nodes by providing an array of node ids.

*   Multiple node selection ([docs](https://unovis.dev/docs/networks-and-flows/Graph#multiple-node-drag)).

*   Enable _Graph_ nodes to accept precalculated layout data ([docs](https://unovis.dev/docs/networks-and-flows/Graph#precalculated)).

### 🪧 Tooltip[​](https://unovis.dev/releases#-tooltip "Direct link to 🪧 Tooltip")

_Tooltip_ now can be anchored to the target element, can be hovered over, and supports dynamic content (updates if the content changes) ([docs](https://unovis.dev/docs/auxiliary/Tooltip#follow-cursor)).

### 📏 Axis[​](https://unovis.dev/releases#-axis "Direct link to 📏 Axis")

Axis now automatically hides overlapping labels ([docs](https://unovis.dev/docs/auxiliary/Axis#hide-overlapping-ticks-15)) and supports label rotation ([docs](https://unovis.dev/docs/auxiliary/Axis#label-rotation)).

### 🔵 Bullet Legend[​](https://unovis.dev/releases#-bullet-legend "Direct link to 🔵 Bullet Legend")

You can set the orientation of _Bullet Legend_ to `'vertical'` ([docs](https://unovis.dev/docs/auxiliary/BulletLegend#orientation)).

![Image 14](https://github.com/user-attachments/assets/3e0edcb5-42ae-41da-ac11-83c1488d70c5)

### 💬 Discord[​](https://unovis.dev/releases#-discord "Direct link to 💬 Discord")

_Unovis_ now has a [Discord](https://discord.com/invite/5hnmashSaN) channel! Join us to say hi, ask questions, and stay updated with the latest news.

Other changes[​](https://unovis.dev/releases#other-changes "Direct link to Other changes")
------------------------------------------------------------------------------------------

### Enhancements[​](https://unovis.dev/releases#enhancements "Direct link to Enhancements")

*   Testing | Add Cypress and Percy for visual testing [#419](https://github.com/f5/unovis/pull/419)
*   Component | Brush: Additional styling options via CSS variables [#392](https://github.com/f5/unovis/pull/392)
*   Website | Upgrade to Docusaurus V3 [#486](https://github.com/f5/unovis/pull/486)
*   Website | Gallery: Range plot [#390](https://github.com/f5/unovis/pull/390)
*   Website | Gallery: Scatter Plot with Varied Shape [#370](https://github.com/f5/unovis/pull/370)
*   Website | Gallery: Donut Example [#367](https://github.com/f5/unovis/pull/367)
*   Website | Add new composite chart section and dual axis chart [#383](https://github.com/f5/unovis/pull/383)

### Bug Fixes[​](https://unovis.dev/releases#bug-fixes "Direct link to Bug Fixes")

*   Component | Scatter: MakesizeScale immutable to prevent sizeRange collisions [#411](https://github.com/f5/unovis/pull/411)
*   Component | Scatter: Label rendering fixes [#413](https://github.com/f5/unovis/pull/413)
*   Component | TopoJSON Map: Various fixes [#425](https://github.com/f5/unovis/pull/425)
*   Core | Bug: XY-container size rendering fix [#431](https://github.com/f5/unovis/pull/431)

[Release 1.4](https://unovis.dev/releases/1.4)
----------------------------------------------

April 2, 2024 ·

3 min read

[![Image 15: Rebecca Bol](https://avatars.githubusercontent.com/u/52078477)](https://github.com/reb-dev)

Maintainer, Key Contributor

Version `1.4.0` of _Unovis_ is finally here! This update is packed full with enhancements including the new Annotations component, expanded Graph features, and a number of bug fixes to improve overall stability of the library.

Release Highlights[​](https://unovis.dev/releases#release-highlights "Direct link to Release Highlights")
---------------------------------------------------------------------------------------------------------

### 📝 New component: Annotations[​](https://unovis.dev/releases#-new-component-annotations "Direct link to 📝 New component: Annotations")

Introducing _Annotations_, a versatile new component that enables you to overlay customized, stylized text on top of your visualizations. Whether you want to highlight points of interest, annotate trends, or simply add text labels to your charts or graphs, _Annotations_ is designed to integrate smoothly with any Unovis component.

Check out _Annotations_'s [documentation](https://unovis.dev/docs/auxiliary/Annotations) and [gallery example](https://unovis.dev/gallery/view?collection=Auxiliary%20Components&title=Chart%20Annotations) to learn how to use it.

![Image 16: annotations](https://github.com/f5/unovis/assets/755708/e2d63880-5e65-406f-b7de-9a5f893b8608)

### 🔗 Graph Link Curvature and SVG Icons[​](https://unovis.dev/releases#-graph-link-curvature-and-svg-icons "Direct link to 🔗 Graph Link Curvature and SVG Icons")

A number of features were added to _Graph_ in this [PR](https://github.com/f5/unovis/pull/322), including link curvature configuration, the ability to use custom SVGs as node icons, and support for longer link labels. Check out the [docs](https://unovis.dev/docs/networks-and-flows/Graph) for a deep dive into the latest enhancements or to explore the breadth of features Graph has to offer.

![Image 17: SCR-20240105-motu](https://github.com/f5/unovis/assets/755708/43473502-0be0-4627-885f-c2820badfd12)

### 🧩 Bullet Legend Shapes[​](https://unovis.dev/releases#-bullet-legend-shapes "Direct link to 🧩 Bullet Legend Shapes")

_Bullet Legend_ now supports a variety of shapes on the component level and for individual legend items. Perfect for when you want to pair a legend with a combination chart or shaped scatter plot.

![Image 18](https://github.com/f5/unovis/assets/52078477/78054126-72ff-4035-97f6-5ab3af202d80)

Other changes[​](https://unovis.dev/releases#other-changes "Direct link to Other changes")
------------------------------------------------------------------------------------------

### Enhancements[​](https://unovis.dev/releases#enhancements "Direct link to Enhancements")

*   React: Exporting component selectors to allow for easier import [#325](https://github.com/f5/unovis/pull/325)
*   Component | Crosshair | Configurable stroke and strokeWidth [#353](https://github.com/f5/unovis/pull/353)
*   Vue | export selector, docs: update [#358](https://github.com/f5/unovis/pull/358)

### Bug Fixes[​](https://unovis.dev/releases#bug-fixes "Direct link to Bug Fixes")

*   Component | Donut | Fix: sortFunction type error [#308](https://github.com/f5/unovis/pull/308)
*   XYContainer | Fix: Crosshair accessors [#309](https://github.com/f5/unovis/pull/309)
*   Component | Timeline | Fix: Color rendering on enter [#310](https://github.com/f5/unovis/pull/310)
*   Component | Chord Diagram | Fixes, enhancements, and refactoring [#318](https://github.com/f5/unovis/pull/318)
*   Website | Releases: Fix url image preview [#323](https://github.com/f5/unovis/pull/323)
*   Core Component and Tooltip event handling tweaks [#330](https://github.com/f5/unovis/pull/330)
*   Svelte | Package: Add missing exports condition for Svelte [#334](https://github.com/f5/unovis/pull/334)
*   Angular | Build: Removing shared from peer dependencies [#349](https://github.com/f5/unovis/pull/349)
*   React | Fixing ref initialization [#344](https://github.com/f5/unovis/pull/344)
*   XY Container | Fix: scaleByDomain produces inconsistent behavior among XY charts [#348](https://github.com/f5/unovis/pull/308)
*   Component | XYLabels | Fix clustering config not taking effect [#351](https://github.com/f5/unovis/pull/308)
*   Component | Crosshair | Fix: crosshair with multiple area issue [#356](https://github.com/f5/unovis/pull/356)

[Release 1.3](https://unovis.dev/releases/1.3)
----------------------------------------------

November 8, 2023 ·

2 min read

[![Image 19: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

[![Image 20: Rebecca Bol](https://avatars.githubusercontent.com/u/52078477)](https://github.com/reb-dev)

Maintainer, Key Contributor

Unovis 1.3 introduces [Vue](http://vuejs.org/) support and a new pattern theme to further improve our support for accessibility features.

Release Highlights[​](https://unovis.dev/releases#release-highlights "Direct link to Release Highlights")
---------------------------------------------------------------------------------------------------------

### 🎉 Vue 3 support[​](https://unovis.dev/releases#-vue-3-support "Direct link to 🎉 Vue 3 support")

Long-awaited support for Vue, the third most popular front-end UI framework. Kudos to our community member [@zernonia](https://github.com/zernonia) for this amazing [contribution](https://github.com/f5/unovis/pull/272)!

### 👨‍🎨 Patterns[​](https://unovis.dev/releases#-patterns "Direct link to 👨‍🎨 Patterns")

A new theme with pattern fills that can be enabled by adding the `theme-patterns` class to the `body` element of your document. See the [documentation](https://unovis.dev/docs/guides/theming#applying-patterns) and [this pull request](https://github.com/f5/unovis/pull/275) for more details.

![Image 21: unovis-patterns](https://github.com/f5/unovis/assets/52078477/6450b1ac-f95d-4fcf-bf30-fe87a8a375e8)![Image 22: unovis-patterns](https://github.com/f5/unovis/assets/52078477/8a0b8f8d-9a28-4352-8b3b-918928241841)

Other changes[​](https://unovis.dev/releases#other-changes "Direct link to Other changes")
------------------------------------------------------------------------------------------

Other changes were aimed at improving the overall stability of the library making the codebase more robust to future changes

*   Refactoring: From Config Classes to Objects [#279](https://github.com/f5/unovis/pull/279)
*   Refactoring: No Implicit Any [#290](https://github.com/f5/unovis/pull/290)
*   Component | Tooltip | Fix: Prevent container overflow when viewport size is reduced [#292](https://github.com/f5/unovis/pull/292)
*   Component | NestedDonut | Fix: TS errors [#296](https://github.com/f5/unovis/pull/296)
*   Svelte: Fixing SingleContainer props and adding support for `class` property [#294](https://github.com/f5/unovis/pull/294)
*   Theme | Patterns: Adjust injected SVG style [#298](https://github.com/f5/unovis/pull/298)

[Release 1.2](https://unovis.dev/releases/1.2)
----------------------------------------------

June 27, 2023 ·

3 min read

[![Image 23: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

[![Image 24: Rebecca Bol](https://avatars.githubusercontent.com/u/52078477)](https://github.com/reb-dev)

Maintainer, Key Contributor

A new version of _Unovis_ is waiting for you on NPM! This update introduces a new component: Nested Donut (aka Sunburst). It also adds better support for accessibility features, allows you to apply additional styles to axes, and much more.

Release Highlights[​](https://unovis.dev/releases#release-highlights "Direct link to Release Highlights")
---------------------------------------------------------------------------------------------------------

### 🍩 New component: _Nested Donut_[​](https://unovis.dev/releases#--new-component-nested-donut "Direct link to --new-component-nested-donut")

_Nested Donut_ is a captivating graphical representation that displays hierarchical data in a circular format. Its nested design allows for multiple concentric rings, each representing a different level of data, enabling users to explore relationships and proportions effortlessly.

Check out _Nested Donut_'s [documentation](https://unovis.dev/docs/misc/NestedDonut) and [example](https://unovis.dev/gallery/view?collection=Networks%20and%20Flows&title=Sunburst%20Nested%20Donut) to learn how to use it.

![Image 25: SCR-20230616-iwvk](https://github.com/f5/unovis/assets/755708/4903488a-275a-4595-9dbf-de9d6ff918eb)![Image 26: nested-donut-2](https://github.com/f5/unovis/assets/755708/cd1d2119-e789-44a3-a673-d9fdc23f767d)

### 👓 Accessibility: Supporting ARIA tags[​](https://unovis.dev/releases#--accessibility-supporting-aria-tags "Direct link to 👓  Accessibility: Supporting ARIA tags")

You can now set the `aria-label` attribute for your visualization by providing the `ariaLabel` config property to the container you use. Unovis will automatically apply `role="figure"` attribute to the container element, making it accessible to assistive technologies.

![Image 27: Image showing aria-label support in Unovis](https://github.com/f5/unovis/assets/755708/028ea127-899c-455e-ad23-e02121019440)

### 🔠 New CSS variables for styling Axis[​](https://unovis.dev/releases#--new-css-variables-for-styling-axis "Direct link to 🔠  New CSS variables for styling Axis")

If you want to customize the width of your tick and grid lines, you can do so using the new `--vis-axis-tick-line-width` and `--vis-axis-grid-line-width` variables.

The color of the domain line by default equals the tick color (that can be specified with `--vis-axis-tick-color`), but _Unovis 1.2_ allows you to explicitly set it via `--vis-axis-domain-color`.

Additionally you can apply custom `cursor` and `text-decoration` to your tick labels with `--vis-axis-tick-label-cursor` and `--vis-axis-tick-label-text-decoration` variables.

![Image 28: image](https://github.com/f5/unovis/assets/755708/8bce43b1-d955-4683-a55a-6596da9b2bf0)

Other changes[​](https://unovis.dev/releases#other-changes "Direct link to Other changes")
------------------------------------------------------------------------------------------

### Enhancements[​](https://unovis.dev/releases#enhancements "Direct link to Enhancements")

*   Component | LeafletMap: Adding `getExpandedCluster` public method [#205](https://github.com/f5/unovis/pull/205)
*   Component | Line: Better enter transition for broken lines [#227](https://github.com/f5/unovis/pull/227)
*   Component | Scatter: Fixing the missing points issue [#227](https://github.com/f5/unovis/pull/227)
*   Component | Scatter: Stroke color and width support [#232](https://github.com/f5/unovis/pull/232)

### Bug Fixes[​](https://unovis.dev/releases#bug-fixes "Direct link to Bug Fixes")

*   Container | XY: Calling render right after initialization if there are axes or components with data [#212](https://github.com/f5/unovis/pull/212)
*   @unovis/svelte: Updating component lifecycles to prevent DOM related errors with SvelteKt (SSR) [#216](https://github.com/f5/unovis/pull/216)

### Other[​](https://unovis.dev/releases#other "Direct link to Other")

*   Core: Using native ResizeObserver when available [#209](https://github.com/f5/unovis/pull/209)
*   Dependencies: Updating Dagre packages to work with Angular 16 [#210](https://github.com/f5/unovis/pull/210)

[Release 1.1](https://unovis.dev/releases/1.1)
----------------------------------------------

April 20, 2023 ·

3 min read

[![Image 29: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

[![Image 30: Rebecca Bol](https://avatars.githubusercontent.com/u/52078477)](https://github.com/reb-dev)

Maintainer, Key Contributor

We're excited to announce the release of _Unovis_`1.1.0`! This update brings new features, enhancements, and bug fixes that improve the overall user experience and stability of the library.

Release Highlights[​](https://unovis.dev/releases#release-highlights "Direct link to Release Highlights")
---------------------------------------------------------------------------------------------------------

### 🦌 [ELK](https://www.eclipse.org/elk/) support for Graph[​](https://unovis.dev/releases#-elk-support-for-graph "Direct link to -elk-support-for-graph")

We've added ELK integration to our Graph component. Now you can render complex hierarchical graphs ELK is famous for! ![Image 31: SCR-20230405-ngtd](https://user-images.githubusercontent.com/755708/230221102-7d798ed0-d587-4c81-b374-e1cc8d582b73.png)

### 🥨 New component: Multi-Level Chord Diagram[​](https://unovis.dev/releases#--new-component-multi-level-chord-diagram "Direct link to 🥨  New component: Multi-Level Chord Diagram")

_Multi-Level Chord Diagram_ can display hierarchical relationships and interactions between multiple entities, often used to visualize complex systems or networks. It showcases the flow of data or connections between different levels, allowing users to understand the intricacies of interconnected components and their relative importance within the system. ![Image 32: SCR-20230419-lhbu](https://user-images.githubusercontent.com/755708/233187237-22c5d229-a8a7-4631-8584-a84db7e20ea9.png)

### 👋 Goodbye `lodash`[​](https://unovis.dev/releases#-goodbye-lodash "Direct link to -goodbye-lodash")

_Unovis_ doesn't have `lodash` as it's dependency anymore saving precious 90KB (unzipped) of your app bundle! ![Image 33: SCR-20230419-llma](https://user-images.githubusercontent.com/755708/233184570-84a1e9cd-fa99-40b0-b4c3-856a20d3ba68.png)

Changelog[​](https://unovis.dev/releases#changelog "Direct link to Changelog")
------------------------------------------------------------------------------

### New Features[​](https://unovis.dev/releases#new-features "Direct link to New Features")

*   Component | Graph: ELK Support by @rokotyan [#161](https://github.com/f5/unovis/pull/161)
*   Chord Diagram: Refactoring, Docs, Examples by @reb-dev [#105](https://github.com/f5/unovis/pull/105)

### Enhancements[​](https://unovis.dev/releases#enhancements "Direct link to Enhancements")

*   Goodbye lodash by @rokotyan [#100](https://github.com/f5/unovis/pull/100)
*   Component | Timeline: Fixing odd rows fill color by @rokotyan [#145](https://github.com/f5/unovis/pull/145)
*   Component | LeafletMap: Calling fitView and fitToPoints in the next frame by @rokotyan [#148](https://github.com/f5/unovis/pull/148)
*   Code Quality: Enabling strictFunctionTypes by @rokotyan [#158](https://github.com/f5/unovis/pull/158)
*   React | Tweaks: Supporting style and className; Removing @emotion/css dependency by @rokotyan [#162](https://github.com/f5/unovis/pull/162)
*   Component | LeafletMap | Styles: Updating MapLibreArcticLight style by @rokotyan [#165](https://github.com/f5/unovis/pull/165)
*   Component | LeafletMap: Configurable inner label color by @rokotyan [#156](https://github.com/f5/unovis/pull/156)
*   Component | Chord Diagram: Better accessor support for non-leaf nodes by @reb-dev [#160](https://github.com/f5/unovis/pull/160)
*   Website: Updating Docusaurus and fixing editUrl by @rokotyan [#175](https://github.com/f5/unovis/pull/175)
*   Container | Core, Single: Setting SVG size in render() by @rokotyan [#174](https://github.com/f5/unovis/pull/174)

### Bug Fixes[​](https://unovis.dev/releases#bug-fixes "Direct link to Bug Fixes")

*   Component | Graph | Link fixes by @reb-dev [#151](https://github.com/f5/unovis/pull/151)
*   React: Fixing double-render on component initialization by @rokotyan [#154](https://github.com/f5/unovis/pull/154)
*   React: Fixing component initialization flow by @rokotyan [#164](https://github.com/f5/unovis/pull/164)
*   Component | Chord Diagram: Fixing invisible nodes by @reb-dev [#169](https://github.com/f5/unovis/pull/169)

### Other[​](https://unovis.dev/releases#other "Direct link to Other")

*   Misc tweaks and fixes by @rokotyan [#168](https://github.com/f5/unovis/pull/168)

[Announcing Unovis 1.0](https://unovis.dev/releases/1)
------------------------------------------------------

December 12, 2022 ·

One min read

[![Image 34: Nikita Rokotyan](https://avatars.githubusercontent.com/u/755708)](https://rokotyan.com/)

Creator, Key Contributor

[![Image 35: Rebecca Bol](https://avatars.githubusercontent.com/u/52078477)](https://github.com/reb-dev)

Maintainer, Key Contributor

![Image 36](https://unovis.dev/assets/images/unovis-banner-fbb7148d5264a219add7228af05d9a93.png)

### We’re excited to announce Unovis 1.0 - a modular data visualization framework for React, Angular, Svelte, and vanilla TypeScript or JavaScript![​](https://unovis.dev/releases#were-excited-to-announce-unovis-10---a-modular-data-visualization-framework-for-react-angular-svelte-and-vanilla-typescript-or-javascript "Direct link to We’re excited to announce Unovis 1.0 - a modular data visualization framework for React, Angular, Svelte, and vanilla TypeScript or JavaScript!")

After more than 3 years in development, _Unovis_ finally goes open source. _Unovis_ can draw charts, maps and network graphs, no matter what UI framework you use. We’ve been using it extensively at [F5](https://f5.com/) with Angular and React apps, and it now empowers user interfaces of F5 Distributed Cloud console and NGINX Controller.

### Why Unovis?[​](https://unovis.dev/releases#why-unovis "Direct link to Why Unovis?")

*   🏗 Integrates nicely with the UI framework of your choice, making it very easy to use;
*   🗺 Supports various charts, simple and detailed maps, network graphs and diagrams;
*   💇 Highly customizable, thanks to the extensive use of CSS variables;
*   📖 Extensive documentation and growing gallery of examples.

### Want to give it try?[​](https://unovis.dev/releases#want-to-give-it-try "Direct link to Want to give it try?")

Go to [unovis.dev](https://unovis.dev/), check out the [docs](https://unovis.dev/docs/intro), explore the [gallery](https://unovis.dev/gallery), or jump right into development with our [Quick Start guide](https://unovis.dev/docs/quick-start/).

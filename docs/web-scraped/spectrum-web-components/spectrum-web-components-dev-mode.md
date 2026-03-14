# Source: https://opensource.adobe.com/spectrum-web-components/dev-mode

Title: Dev mode: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/dev-mode

Markdown Content:
Dev mode: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

Dev mode
========

Spectrum Web Components aims to support developers in making high quality applications by taking into account features of our components--accessibility, connectivity, interactivity, etc.--that would otherwise distract. While many of these capabilities can exist wholey at runtime in their encapsulated custom element delivery, some require development time considerations to ensure they are surfaced correctly. Code checks can be costly and require KBs of Javascript that aren't needed in production. With this in mind, we package these extended capbilities into a dev mode. With the dev mode activated, you can be assured that your consumption of Spectrum Web Components is adhering to best practices for accessibility, API-usage, code deprecation, performance, and more.

Activation
----------

#Section titled Activation

Dev mode can be accessed via the `development`export condition. Each tooling pipeline allows for this condition to be applied in its own way. With Rollup, for example, use the `nodeResolve()` plugin to make choices about what export conditions to follow, like so:

import { nodeResolve } from '@rollup/plugin-node-resolve';

export default {
  // ...
  plugins: [
    nodeResolve({
      // Add this line for development config, omit for production config
      exportConditions: ['development'],
    }),
  ],
};
Assuming you're already consuming Spectrum Web Components perfectly, you'll be greeted with the following message to announce that dev mode has been activated:

Spectrum Web Components is in dev mode. Not recommended for production!

https://opensource.adobe.com/spectrum-web-components/dev-mode/
{
    warningData: { localName: 'base', type: 'default', level: 'default' }
}

Configuration
-------------

#Section titled Configuration

You can customize the messages that you receive by turning off warnings that you no longer believe apply, or allowing warnings to be published verbosely. This can be done by element "localName", warning "type", warning "level" or with the `verbose` property on the `window.__swc` object. To configure this, apply a value for `window.__swc` in your JS at any point that you'd like to control future warning messages. The following is an example of doing this before you import any of the rest of your application:

<script>
window.__swc = {
    ignoreWarningTypes: { api: true },
    ignoreWarningLevels: { deprecation: true },
    ignoreWarningLocalNames: { 'sp-button': true },
    verbose: true
}
</script>

<script
    src="./path/to/app.js"
    type="module"
></script>
The above code turn warnings off for `sp-button`, `api`s, and `deprecation`s while receiving `verbose` messages outside of those.

The config is typed as follows:

type ElementLocalName = string;

type WarningType = 'default' | 'accessibility' | 'api';

type WarningLevel = 'default' | 'low' | 'medium' | 'high' | 'deprecation';

type SWCWarningData = {
  localName: string;
  type: WarningType;
  level: WarningLevel;
};

type BrandedSWCWarningID = `${ElementLocalName}:${WarningType}:${WarningLevel}`;

interface Window {
  __swc: {
    ignoreWarningTypes: Record<WarningType, boolean>;
    ignoreWarningLevels: Record<WarningLevel, boolean>;
    ignoreWarningLocalNames: Record<ElementLocalName, boolean>;
    verbose?: boolean;
  };
}

Future
------

#Section titled Future

While there are currently only a handful of warnings that will be published from the library in this way, look for usage of this feature to expand in the coming months and years. As you consume Spectrum Web Components, if you find concepts or features that you feel could be clarified or enhanced by dev mode, please join the discussion and support us in making the library as productive for you as possible.

Dev mode should not be delivered to your users in production. This is why it has been added as an opt-in feature of the Spectrum Web Components library. With this in mind, there is the possibility that breaking changes to the dev mode API could occur outside of breaking changes in semver for the library or its packages. To avoid potential breaks affecting your code, do NOT leverage the API beyond the `ignoreWarningTypes`, `ignoreWarningLevels`, `ignoreWarningLocalNames`, and `verbose` properties on the `__swc` object listed above.

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)

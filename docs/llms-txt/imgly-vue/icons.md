# Icons

Customize the editor’s icons by registering custom SVG icon sets and using them in dock entries, custom components, and other UI elements.

![Icons example showing the CE.SDK editor with custom icons in the dock and canvas menu](/docs/cesdk/_astro/browser.hero.rQnJB7Ts_Zcq5PY.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-appearance-icons-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-appearance-icons-browser)

CE.SDK uses SVG sprites for icons throughout the editor interface. Each icon is referenced by a symbol ID that starts with `@`. You can register custom icon sets to replace built-in icons or add new ones for your own custom UI components.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';
class Example implements EditorPlugin {  name = 'guides-user-interface-appearance-icons-browser';  version = '1.0.0';
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });
    // Set the editor view    cesdk.ui.setView('advanced');
    // Create a design scene    await cesdk.createDesignScene();
    const engine = cesdk.engine;
    // Register a custom SVG icon set with multiple symbols    cesdk.ui.addIconSet(      '@custom/icons',      `      <svg xmlns="http://www.w3.org/2000/svg">        <symbol id="@custom/icon/star" viewBox="0 0 24 24" fill="none">          <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>        </symbol>        <symbol id="@custom/icon/heart" viewBox="0 0 24 24" fill="none">          <path d="M20.84 4.61C20.3292 4.099 19.7228 3.69365 19.0554 3.41708C18.3879 3.14052 17.6725 2.99817 16.95 2.99817C16.2275 2.99817 15.5121 3.14052 14.8446 3.41708C14.1772 3.69365 13.5708 4.099 13.06 4.61L12 5.67L10.94 4.61C9.9083 3.57831 8.50903 2.99871 7.05 2.99871C5.59096 2.99871 4.19169 3.57831 3.16 4.61C2.12831 5.64169 1.54871 7.04097 1.54871 8.5C1.54871 9.95903 2.12831 11.3583 3.16 12.39L4.22 13.45L12 21.23L19.78 13.45L20.84 12.39C21.351 11.8792 21.7563 11.2728 22.0329 10.6054C22.3095 9.93789 22.4518 9.22249 22.4518 8.5C22.4518 7.77751 22.3095 7.0621 22.0329 6.39464C21.7563 5.72718 21.351 5.12075 20.84 4.61Z" fill="currentColor"/>        </symbol>        <symbol id="@custom/icon/diamond" viewBox="0 0 24 24" fill="none">          <path d="M6 3H18L22 9L12 21L2 9L6 3Z" fill="currentColor"/>        </symbol>      </svg>    `    );
    // Get the current dock order and replace the Images dock icon    const dockOrder = cesdk.ui.getDockOrder();    cesdk.ui.setDockOrder(      dockOrder.map((entry) => {        if (entry.key === 'ly.img.image') {          return { ...entry, icon: '@custom/icon/star' };        }        return entry;      })    );
    // Register a custom component that uses a custom icon    cesdk.ui.registerComponent(      'CustomIconButton',      ({ builder: { Button } }) => {        Button('heartButton', {          label: 'Heart',          icon: '@custom/icon/heart',          onClick: () => {            console.log('Heart icon button clicked');          }        });        Button('diamondButton', {          label: 'Diamond',          icon: '@custom/icon/diamond',          onClick: () => {            console.log('Diamond icon button clicked');          }        });      }    );
    // Add the custom component to the canvas menu    cesdk.ui.setCanvasMenuOrder([      ...cesdk.ui.getCanvasMenuOrder(),      'CustomIconButton'    ]);
    // Add an image block to the scene so the canvas menu is visible when selected    const page = engine.block.findByType('page')[0];    if (page !== undefined) {      const imageBlock = await engine.block.addImage(        'https://img.ly/static/ubq_samples/sample_1.jpg',        {          x: 50,          y: 50,          size: { width: 400, height: 300 }        }      );      engine.block.appendChild(page, imageBlock);      engine.block.select(imageBlock);    }  }}
export default Example;
```

This guide covers how to register custom SVG icon sets, replace dock entry icons with custom icons, and use custom icons in custom UI components.

## Registering Custom Icon Sets[#](#registering-custom-icon-sets)

We add custom icons to CE.SDK using the `cesdk.ui.addIconSet()` method. The method takes two parameters: a unique identifier for the icon set and an SVG sprite string containing symbol definitions.

```
// Register a custom SVG icon set with multiple symbolscesdk.ui.addIconSet(  '@custom/icons',  `  <svg xmlns="http://www.w3.org/2000/svg">    <symbol id="@custom/icon/star" viewBox="0 0 24 24" fill="none">      <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="currentColor"/>    </symbol>    <symbol id="@custom/icon/heart" viewBox="0 0 24 24" fill="none">      <path d="M20.84 4.61C20.3292 4.099 19.7228 3.69365 19.0554 3.41708C18.3879 3.14052 17.6725 2.99817 16.95 2.99817C16.2275 2.99817 15.5121 3.14052 14.8446 3.41708C14.1772 3.69365 13.5708 4.099 13.06 4.61L12 5.67L10.94 4.61C9.9083 3.57831 8.50903 2.99871 7.05 2.99871C5.59096 2.99871 4.19169 3.57831 3.16 4.61C2.12831 5.64169 1.54871 7.04097 1.54871 8.5C1.54871 9.95903 2.12831 11.3583 3.16 12.39L4.22 13.45L12 21.23L19.78 13.45L20.84 12.39C21.351 11.8792 21.7563 11.2728 22.0329 10.6054C22.3095 9.93789 22.4518 9.22249 22.4518 8.5C22.4518 7.77751 22.3095 7.0621 22.0329 6.39464C21.7563 5.72718 21.351 5.12075 20.84 4.61Z" fill="currentColor"/>    </symbol>    <symbol id="@custom/icon/diamond" viewBox="0 0 24 24" fill="none">      <path d="M6 3H18L22 9L12 21L2 9L6 3Z" fill="currentColor"/>    </symbol>  </svg>`);
```

Each symbol in the SVG sprite must have an `id` attribute that starts with `@`. This ID is how you reference the icon throughout CE.SDK. In this example, we register three custom icons: `@custom/icon/star`, `@custom/icon/heart`, and `@custom/icon/diamond`.

### SVG Sprite Format Requirements[#](#svg-sprite-format-requirements)

When creating custom icon SVG sprites, follow these requirements for proper rendering:

*   Wrap all symbols in an `<svg>` element with the `xmlns` attribute
*   Each `<symbol>` must have a unique `id` starting with `@`
*   Include a `viewBox` attribute on each symbol for proper scaling
*   Use `currentColor` for `fill` and `stroke` values to inherit the current theme color
*   Avoid hardcoded width/height attributes on symbols—let CE.SDK handle sizing

### Security Considerations[#](#security-considerations)

SVG content passed to `addIconSet()` is injected into the DOM without sanitization. Only use trusted SVG sources. If you need to load icons from untrusted sources, consider sanitizing the content with a library like DOMPurify before registration.

## Replacing Dock Entry Icons[#](#replacing-dock-entry-icons)

Once you’ve registered a custom icon set, you can replace the icons of existing dock entries. We retrieve the current dock order using `cesdk.ui.getDockOrder()`, modify the entries we want to change, and apply the updated order with `cesdk.ui.setDockOrder()`.

```
// Get the current dock order and replace the Images dock iconconst dockOrder = cesdk.ui.getDockOrder();cesdk.ui.setDockOrder(  dockOrder.map((entry) => {    if (entry.key === 'ly.img.image') {      return { ...entry, icon: '@custom/icon/star' };    }    return entry;  }));
```

This example replaces the Images dock entry icon with our custom star icon. The `key` property identifies the dock entry, and we update the `icon` property to reference our custom icon by its symbol ID.

## Using Icons in Custom Components[#](#using-icons-in-custom-components)

You can use custom icons in your own UI components by referencing the icon’s symbol ID in the component builder. When registering a custom component with `cesdk.ui.registerComponent()`, buttons and other elements accept an `icon` property.

```
// Register a custom component that uses a custom iconcesdk.ui.registerComponent(  'CustomIconButton',  ({ builder: { Button } }) => {    Button('heartButton', {      label: 'Heart',      icon: '@custom/icon/heart',      onClick: () => {        console.log('Heart icon button clicked');      }    });    Button('diamondButton', {      label: 'Diamond',      icon: '@custom/icon/diamond',      onClick: () => {        console.log('Diamond icon button clicked');      }    });  });
// Add the custom component to the canvas menucesdk.ui.setCanvasMenuOrder([  ...cesdk.ui.getCanvasMenuOrder(),  'CustomIconButton']);
```

We register a custom component containing two buttons, each using a different custom icon. We then add this component to the canvas menu so the buttons appear when users select elements on the canvas.

## Built-In Icons[#](#built-in-icons)

CE.SDK includes a built-in icon set named ‘Essentials’ with icons for common editor actions. Each icon is referenced by its symbol ID following the pattern `@imgly/IconName`. You can use these icons directly in your custom components or as references when replacing dock icons.

### Set ‘Essentials’[#](#set-essentials)

| Name | Icon |
| --- | --- |
| 
`@imgly/Adjustments`

 | 

![Adjustments Icon](/docs/cesdk/_astro/Adjustments.CMpGLfUm_68cTD.svg)

 |
| 

`@imgly/Animation`

 | 

![Animation Icon](/docs/cesdk/_astro/Animation.B2rhC3jX_68cTD.svg)

 |
| 

`@imgly/Appearance`

 | 

![Appearance Icon](/docs/cesdk/_astro/Appearance.DNDO2WuP_68cTD.svg)

 |
| 

`@imgly/Apps`

 | 

![Apps Icon](/docs/cesdk/_astro/Apps.DznTjKmh_68cTD.svg)

 |
| 

`@imgly/ArrowDown`

 | 

![ArrowDown Icon](/docs/cesdk/_astro/ArrowDown.DF55uy6X_68cTD.svg)

 |
| 

`@imgly/ArrowLeft`

 | 

![ArrowLeft Icon](/docs/cesdk/_astro/ArrowLeft.rNR_kJjE_68cTD.svg)

 |
| 

`@imgly/ArrowRight`

 | 

![ArrowRight Icon](/docs/cesdk/_astro/ArrowRight.9eua18dC_68cTD.svg)

 |
| 

`@imgly/ArrowUp`

 | 

![ArrowUp Icon](/docs/cesdk/_astro/ArrowUp.CVAHSy6F_68cTD.svg)

 |
| 

`@imgly/ArrowsDirectionHorizontal`

 | 

![ArrowsDirectionHorizontal Icon](/docs/cesdk/_astro/ArrowsDirectionHorizontal.B0bUSo3k_68cTD.svg)

 |
| 

`@imgly/ArrowsDirectionVertical`

 | 

![ArrowsDirectionVertical Icon](/docs/cesdk/_astro/ArrowsDirectionVertical.BpuSfMrI_68cTD.svg)

 |
| 

`@imgly/AsClip`

 | 

![AsClip Icon](/docs/cesdk/_astro/AsClip.CVGpviFn_68cTD.svg)

 |
| 

`@imgly/AsOverlay`

 | 

![AsOverlay Icon](/docs/cesdk/_astro/AsOverlay.5eEK9ZPF_68cTD.svg)

 |
| 

`@imgly/Audio`

 | 

![Audio Icon](/docs/cesdk/_astro/Audio.uOK5I2sE_68cTD.svg)

 |
| 

`@imgly/AudioAdd`

 | 

![AudioAdd Icon](/docs/cesdk/_astro/AudioAdd.B-ssll_o_68cTD.svg)

 |
| 

`@imgly/Backward`

 | 

![Backward Icon](/docs/cesdk/_astro/Backward.C2BFbDeQ_68cTD.svg)

 |
| 

`@imgly/Blendmode`

 | 

![Blendmode Icon](/docs/cesdk/_astro/Blendmode.z9rB9rxU_68cTD.svg)

 |
| 

`@imgly/Blur`

 | 

![Blur Icon](/docs/cesdk/_astro/Blur.DgAVmk6g_68cTD.svg)

 |
| 

`@imgly/BooleanExclude`

 | 

![BooleanExclude Icon](/docs/cesdk/_astro/BooleanExclude.By40Ey3m_68cTD.svg)

 |
| 

`@imgly/BooleanIntersect`

 | 

![BooleanIntersect Icon](/docs/cesdk/_astro/BooleanIntersect.CY4HM50Y_68cTD.svg)

 |
| 

`@imgly/BooleanSubstract`

 | 

![BooleanSubstract Icon](/docs/cesdk/_astro/BooleanSubstract.CwYzfMbe_68cTD.svg)

 |
| 

`@imgly/BooleanUnion`

 | 

![BooleanUnion Icon](/docs/cesdk/_astro/BooleanUnion.C-xUCyCc_68cTD.svg)

 |
| 

`@imgly/CaseAsTyped`

 | 

![CaseAsTyped Icon](/docs/cesdk/_astro/CaseAsTyped.l6bSq4oc_68cTD.svg)

 |
| 

`@imgly/CaseLowercase`

 | 

![CaseLowercase Icon](/docs/cesdk/_astro/CaseLowercase.BEN90R29_68cTD.svg)

 |
| 

`@imgly/CaseSmallCaps`

 | 

![CaseSmallCaps Icon](/docs/cesdk/_astro/CaseSmallCaps.BTdtiBHa_68cTD.svg)

 |
| 

`@imgly/CaseTitleCase`

 | 

![CaseTitleCase Icon](/docs/cesdk/_astro/CaseTitleCase.6GhYywMm_68cTD.svg)

 |
| 

`@imgly/CaseUppercase`

 | 

![CaseUppercase Icon](/docs/cesdk/_astro/CaseUppercase.B4vfd36q_68cTD.svg)

 |
| 

`@imgly/CheckboxCheckmark`

 | 

![CheckboxCheckmark Icon](/docs/cesdk/_astro/CheckboxCheckmark.pMjPiK5g_68cTD.svg)

 |
| 

`@imgly/CheckboxMixed`

 | 

![CheckboxMixed Icon](/docs/cesdk/_astro/CheckboxMixed.DOxJYYWZ_68cTD.svg)

 |
| 

`@imgly/Checkmark`

 | 

![Checkmark Icon](/docs/cesdk/_astro/Checkmark.CP0StQxb_68cTD.svg)

 |
| 

`@imgly/ChevronDown`

 | 

![ChevronDown Icon](/docs/cesdk/_astro/ChevronDown.f4OqdrJU_68cTD.svg)

 |
| 

`@imgly/ChevronLeft`

 | 

![ChevronLeft Icon](/docs/cesdk/_astro/ChevronLeft.BU6Cbcnc_68cTD.svg)

 |
| 

`@imgly/ChevronRight`

 | 

![ChevronRight Icon](/docs/cesdk/_astro/ChevronRight.DaVhuEy-_68cTD.svg)

 |
| 

`@imgly/ChevronUp`

 | 

![ChevronUp Icon](/docs/cesdk/_astro/ChevronUp.BcBhYGEB_68cTD.svg)

 |
| 

`@imgly/Collage`

 | 

![Collage Icon](/docs/cesdk/_astro/Collage.C9m_-pZR_68cTD.svg)

 |
| 

`@imgly/ColorFill`

 | 

![ColorFill Icon](/docs/cesdk/_astro/ColorFill.Due-2va6_68cTD.svg)

 |
| 

`@imgly/ColorGradientAngular`

 | 

![ColorGradientAngular Icon](/docs/cesdk/_astro/ColorGradientAngular.CWntlp_d_68cTD.svg)

 |
| 

`@imgly/ColorGradientLinear`

 | 

![ColorGradientLinear Icon](/docs/cesdk/_astro/ColorGradientLinear.DmT3R1oC_68cTD.svg)

 |
| 

`@imgly/ColorGradientRadial`

 | 

![ColorGradientRadial Icon](/docs/cesdk/_astro/ColorGradientRadial.DzApV2NU_68cTD.svg)

 |
| 

`@imgly/ColorOpacity`

 | 

![ColorOpacity Icon](/docs/cesdk/_astro/ColorOpacity.DMNZ-UhH_68cTD.svg)

 |
| 

`@imgly/ColorSolid`

 | 

![ColorSolid Icon](/docs/cesdk/_astro/ColorSolid.DVTQ0W3Q_68cTD.svg)

 |
| 

`@imgly/ConnectionLostSlash`

 | 

![ConnectionLostSlash Icon](/docs/cesdk/_astro/ConnectionLostSlash.DTcmxMhK_68cTD.svg)

 |
| 

`@imgly/Copy`

 | 

![Copy Icon](/docs/cesdk/_astro/Copy.BmABgrWc_68cTD.svg)

 |
| 

`@imgly/CornerJoinBevel`

 | 

![CornerJoinBevel Icon](/docs/cesdk/_astro/CornerJoinBevel.DqlY245R_68cTD.svg)

 |
| 

`@imgly/CornerJoinMiter`

 | 

![CornerJoinMiter Icon](/docs/cesdk/_astro/CornerJoinMiter.D3jd16NL_68cTD.svg)

 |
| 

`@imgly/CornerJoinRound`

 | 

![CornerJoinRound Icon](/docs/cesdk/_astro/CornerJoinRound.BwcufozW_68cTD.svg)

 |
| 

`@imgly/Crop`

 | 

![Crop Icon](/docs/cesdk/_astro/Crop.DYPLk0m-_68cTD.svg)

 |
| 

`@imgly/CropCoverMode`

 | 

![CropCoverMode Icon](/docs/cesdk/_astro/CropCoverMode.CGAJdwRR_68cTD.svg)

 |
| 

`@imgly/CropCropMode`

 | 

![CropCropMode Icon](/docs/cesdk/_astro/CropCropMode.DkkLoYje_68cTD.svg)

 |
| 

`@imgly/CropFitMode`

 | 

![CropFitMode Icon](/docs/cesdk/_astro/CropFitMode.BO_JImlA_68cTD.svg)

 |
| 

`@imgly/CropFreefromMode`

 | 

![CropFreefromMode Icon](/docs/cesdk/_astro/CropFreefromMode.BnRsz2W6_68cTD.svg)

 |
| 

`@imgly/Cross`

 | 

![Cross Icon](/docs/cesdk/_astro/Cross.txikJ9io_68cTD.svg)

 |
| 

`@imgly/CrossRoundSolid`

 | 

![CrossRoundSolid Icon](/docs/cesdk/_astro/CrossRoundSolid.BOTrEi6a_68cTD.svg)

 |
| 

`@imgly/CustomLibrary`

 | 

![CustomLibrary Icon](/docs/cesdk/_astro/CustomLibrary.CI29Obfk_68cTD.svg)

 |
| 

`@imgly/Download`

 | 

![Download Icon](/docs/cesdk/_astro/Download.CZGsxZgt_68cTD.svg)

 |
| 

`@imgly/DropShadow`

 | 

![DropShadow Icon](/docs/cesdk/_astro/DropShadow.C4Pf5WpM_68cTD.svg)

 |
| 

`@imgly/Duplicate`

 | 

![Duplicate Icon](/docs/cesdk/_astro/Duplicate.DrdC6vQb_68cTD.svg)

 |
| 

`@imgly/Edit`

 | 

![Edit Icon](/docs/cesdk/_astro/Edit.CUHjt2nS_68cTD.svg)

 |
| 

`@imgly/Effects`

 | 

![Effects Icon](/docs/cesdk/_astro/Effects.DRlbFdXp_68cTD.svg)

 |
| 

`@imgly/ExternalLink`

 | 

![ExternalLink Icon](/docs/cesdk/_astro/ExternalLink.25xxhZJX_68cTD.svg)

 |
| 

`@imgly/EyeClosed`

 | 

![EyeClosed Icon](/docs/cesdk/_astro/EyeClosed.Cu1m0jfI_68cTD.svg)

 |
| 

`@imgly/EyeOpen`

 | 

![EyeOpen Icon](/docs/cesdk/_astro/EyeOpen.Ds3PBojz_68cTD.svg)

 |
| 

`@imgly/Filter`

 | 

![Filter Icon](/docs/cesdk/_astro/Filter.O79QRETm_68cTD.svg)

 |
| 

`@imgly/FlipHorizontal`

 | 

![FlipHorizontal Icon](/docs/cesdk/_astro/FlipHorizontal.Ei-fC6h9_68cTD.svg)

 |
| 

`@imgly/FlipVertical`

 | 

![FlipVertical Icon](/docs/cesdk/_astro/FlipVertical.M9ofU4J4_68cTD.svg)

 |
| 

`@imgly/FontAutoSizing`

 | 

![FontAutoSizing Icon](/docs/cesdk/_astro/FontAutoSizing.DexdGxcq_68cTD.svg)

 |
| 

`@imgly/FontSize`

 | 

![FontSize Icon](/docs/cesdk/_astro/FontSize.S7lZw5Ga_68cTD.svg)

 |
| 

`@imgly/Forward`

 | 

![Forward Icon](/docs/cesdk/_astro/Forward.BcuMexaI_68cTD.svg)

 |
| 

`@imgly/FullscreenEnter`

 | 

![FullscreenEnter Icon](/docs/cesdk/_astro/FullscreenEnter.kF_8SSV7_68cTD.svg)

 |
| 

`@imgly/FullscreenLeave`

 | 

![FullscreenLeave Icon](/docs/cesdk/_astro/FullscreenLeave.DzxL3476_68cTD.svg)

 |
| 

`@imgly/Group`

 | 

![Group Icon](/docs/cesdk/_astro/Group.DAQiJIa__68cTD.svg)

 |
| 

`@imgly/GroupEnter`

 | 

![GroupEnter Icon](/docs/cesdk/_astro/GroupEnter.H1qCSB2q_68cTD.svg)

 |
| 

`@imgly/GroupExit`

 | 

![GroupExit Icon](/docs/cesdk/_astro/GroupExit.Cxgs51O9_68cTD.svg)

 |
| 

`@imgly/Home`

 | 

![Home Icon](/docs/cesdk/_astro/Home.DATK_4gX_68cTD.svg)

 |
| 

`@imgly/Image`

 | 

![Image Icon](/docs/cesdk/_astro/Image.D2nUt11G_68cTD.svg)

 |
| 

`@imgly/Info`

 | 

![Info Icon](/docs/cesdk/_astro/Info.DNnpRpS4_68cTD.svg)

 |
| 

`@imgly/LayerBringForward`

 | 

![LayerBringForward Icon](/docs/cesdk/_astro/LayerBringForward.CTq67SoU_68cTD.svg)

 |
| 

`@imgly/LayerBringForwardArrow`

 | 

![LayerBringForwardArrow Icon](/docs/cesdk/_astro/LayerBringForwardArrow.BcT_xGMM_68cTD.svg)

 |
| 

`@imgly/LayerBringToFront`

 | 

![LayerBringToFront Icon](/docs/cesdk/_astro/LayerBringToFront.BeM-z2uF_68cTD.svg)

 |
| 

`@imgly/LayerBringToFrontArrow`

 | 

![LayerBringToFrontArrow Icon](/docs/cesdk/_astro/LayerBringToFrontArrow.CnSyUJQI_68cTD.svg)

 |
| 

`@imgly/LayerOpacity`

 | 

![LayerOpacity Icon](/docs/cesdk/_astro/LayerOpacity.OWYnyPUZ_68cTD.svg)

 |
| 

`@imgly/LayerSendBackward`

 | 

![LayerSendBackward Icon](/docs/cesdk/_astro/LayerSendBackward.CFC8GyHY_68cTD.svg)

 |
| 

`@imgly/LayerSendBackwardArrow`

 | 

![LayerSendBackwardArrow Icon](/docs/cesdk/_astro/LayerSendBackwardArrow.5_XvmVuj_68cTD.svg)

 |
| 

`@imgly/LayerSendToBack`

 | 

![LayerSendToBack Icon](/docs/cesdk/_astro/LayerSendToBack.BvPugqHt_68cTD.svg)

 |
| 

`@imgly/LayerSendToBackArrow`

 | 

![LayerSendToBackArrow Icon](/docs/cesdk/_astro/LayerSendToBackArrow.YfQYh_l3_68cTD.svg)

 |
| 

`@imgly/LayoutHorizontal`

 | 

![LayoutHorizontal Icon](/docs/cesdk/_astro/LayoutHorizontal.CePOuWsz_68cTD.svg)

 |
| 

`@imgly/LayoutVertical`

 | 

![LayoutVertical Icon](/docs/cesdk/_astro/LayoutVertical.DxgvBSD0_68cTD.svg)

 |
| 

`@imgly/Library`

 | 

![Library Icon](/docs/cesdk/_astro/Library.xdK4TnnL_68cTD.svg)

 |
| 

`@imgly/LineHeight`

 | 

![LineHeight Icon](/docs/cesdk/_astro/LineHeight.CVWOG1lW_68cTD.svg)

 |
| 

`@imgly/LinkClosed`

 | 

![LinkClosed Icon](/docs/cesdk/_astro/LinkClosed.DSl2uQyi_68cTD.svg)

 |
| 

`@imgly/LinkOpen`

 | 

![LinkOpen Icon](/docs/cesdk/_astro/LinkOpen.DofM8u7F_68cTD.svg)

 |
| 

`@imgly/LoopClip`

 | 

![LoopClip Icon](/docs/cesdk/_astro/LoopClip.ClOhgNoV_68cTD.svg)

 |
| 

`@imgly/LoadingSpinner`

 | 

![LoadingSpinner Icon](/docs/cesdk/_astro/LoadingSpinner.DVqX5QnF_68cTD.svg)

 |
| 

`@imgly/LockClosed`

 | 

![LockClosed Icon](/docs/cesdk/_astro/LockClosed.CNalJFXd_68cTD.svg)

 |
| 

`@imgly/LockOpen`

 | 

![LockOpen Icon](/docs/cesdk/_astro/LockOpen.TJhEPjeL_68cTD.svg)

 |
| 

`@imgly/Minus`

 | 

![Minus Icon](/docs/cesdk/_astro/Minus.CqBSW4Hh_68cTD.svg)

 |
| 

`@imgly/MoreOptionsHorizontal`

 | 

![MoreOptionsHorizontal Icon](/docs/cesdk/_astro/MoreOptionsHorizontal.L63utfkH_68cTD.svg)

 |
| 

`@imgly/MoreOptionsVertical`

 | 

![MoreOptionsVertical Icon](/docs/cesdk/_astro/MoreOptionsVertical.CuZa1NAq_68cTD.svg)

 |
| 

`@imgly/Move`

 | 

![Move Icon](/docs/cesdk/_astro/Move.BcjZGlar_68cTD.svg)

 |
| 

`@imgly/Next`

 | 

![Next Icon](/docs/cesdk/_astro/Next.D6AnK3jG_68cTD.svg)

 |
| 

`@imgly/None`

 | 

![None Icon](/docs/cesdk/_astro/None.94s_6ShU_68cTD.svg)

 |
| 

`@imgly/ObjectAlignBottom`

 | 

![ObjectAlignBottom Icon](/docs/cesdk/_astro/ObjectAlignBottom.Q-hKPxE5_68cTD.svg)

 |
| 

`@imgly/ObjectAlignDistributedHorizontal`

 | 

![ObjectAlignDistributedHorizontal Icon](/docs/cesdk/_astro/ObjectAlignDistributedHorizontal.X0A9Wwpy_68cTD.svg)

 |
| 

`@imgly/ObjectAlignDistributedVertical`

 | 

![ObjectAlignDistributedVertical Icon](/docs/cesdk/_astro/ObjectAlignDistributedVertical.CNGw3lI8_68cTD.svg)

 |
| 

`@imgly/ObjectAlignHorizontalCenter`

 | 

![ObjectAlignHorizontalCenter Icon](/docs/cesdk/_astro/ObjectAlignHorizontalCenter.DYUFnb31_68cTD.svg)

 |
| 

`@imgly/ObjectAlignLeft`

 | 

![ObjectAlignLeft Icon](/docs/cesdk/_astro/ObjectAlignLeft.esiSYWS7_68cTD.svg)

 |
| 

`@imgly/ObjectAlignRight`

 | 

![ObjectAlignRight Icon](/docs/cesdk/_astro/ObjectAlignRight.GPKDNQHR_68cTD.svg)

 |
| 

`@imgly/ObjectAlignTop`

 | 

![ObjectAlignTop Icon](/docs/cesdk/_astro/ObjectAlignTop.l_WErmNU_68cTD.svg)

 |
| 

`@imgly/ObjectAlignVerticalCenter`

 | 

![ObjectAlignVerticalCenter Icon](/docs/cesdk/_astro/ObjectAlignVerticalCenter.8hE0T5x6_68cTD.svg)

 |
| 

`@imgly/OrientationToggleLandscape`

 | 

![OrientationToggleLandscape Icon](/docs/cesdk/_astro/OrientationToggleLandscape.CSDa8O0M_68cTD.svg)

 |
| 

`@imgly/OrientationTogglePortrait`

 | 

![OrientationTogglePortrait Icon](/docs/cesdk/_astro/OrientationTogglePortrait.DxVF38g4_68cTD.svg)

 |
| 

`@imgly/PageResize`

 | 

![PageResize Icon](/docs/cesdk/_astro/PageResize.Cu1xAsRj_68cTD.svg)

 |
| 

`@imgly/Paste`

 | 

![Paste Icon](/docs/cesdk/_astro/Paste.BuMonsY9_68cTD.svg)

 |
| 

`@imgly/Pause`

 | 

![Pause Icon](/docs/cesdk/_astro/Pause.DDGCVnKM_68cTD.svg)

 |
| 

`@imgly/PlaceholderConnected`

 | 

![PlaceholderConnected Icon](/docs/cesdk/_astro/PlaceholderConnected.BkUyWaQ7_68cTD.svg)

 |
| 

`@imgly/PlaceholderStripes`

 | 

![PlaceholderStripes Icon](/docs/cesdk/_astro/PlaceholderStripes.BFineOwo_68cTD.svg)

 |
| 

`@imgly/Play`

 | 

![Play Icon](/docs/cesdk/_astro/Play.DSpjfhWu_68cTD.svg)

 |
| 

`@imgly/Plus`

 | 

![Plus Icon](/docs/cesdk/_astro/Plus.D3IdVb1T_68cTD.svg)

 |
| 

`@imgly/Position`

 | 

![Position Icon](/docs/cesdk/_astro/Position.DhnoEfwQ_68cTD.svg)

 |
| 

`@imgly/Previous`

 | 

![Previous Icon](/docs/cesdk/_astro/Previous.CCrN_eRf_68cTD.svg)

 |
| 

`@imgly/Redo`

 | 

![Redo Icon](/docs/cesdk/_astro/Redo.CfjN5TI8_68cTD.svg)

 |
| 

`@imgly/Rename`

 | 

![Rename Icon](/docs/cesdk/_astro/Rename.CxI-t7Fn_68cTD.svg)

 |
| 

`@imgly/Reorder`

 | 

![Reorder Icon](/docs/cesdk/_astro/Reorder.CzUg_r09_68cTD.svg)

 |
| 

`@imgly/Repeat`

 | 

![Repeat Icon](/docs/cesdk/_astro/Repeat.B2e75pG7_68cTD.svg)

 |
| 

`@imgly/RepeatOff`

 | 

![RepeatOff Icon](/docs/cesdk/_astro/RepeatOff.B29qufK8_68cTD.svg)

 |
| 

`@imgly/Replace`

 | 

![Replace Icon](/docs/cesdk/_astro/Replace.B7aKEXkR_68cTD.svg)

 |
| 

`@imgly/Reset`

 | 

![Reset Icon](/docs/cesdk/_astro/Reset.Cxse5Eti_68cTD.svg)

 |
| 

`@imgly/RotateCCW90`

 | 

![RotateCCW90 Icon](/docs/cesdk/_astro/RotateCCW90.BIw29FPG_68cTD.svg)

 |
| 

`@imgly/RotateCW`

 | 

![RotateCW Icon](/docs/cesdk/_astro/RotateCW.BdtOYcHi_68cTD.svg)

 |
| 

`@imgly/RotateCW90`

 | 

![RotateCW90 Icon](/docs/cesdk/_astro/RotateCW90.Dr3zp4wc_68cTD.svg)

 |
| 

`@imgly/Save`

 | 

![Save Icon](/docs/cesdk/_astro/Save.C0V1utdu_68cTD.svg)

 |
| 

`@imgly/Scale`

 | 

![Scale Icon](/docs/cesdk/_astro/Scale.Ap3A7VA6_68cTD.svg)

 |
| 

`@imgly/Search`

 | 

![Search Icon](/docs/cesdk/_astro/Search.OK9LIXmS_68cTD.svg)

 |
| 

`@imgly/Settings`

 | 

![Settings Icon](/docs/cesdk/_astro/Settings.VScoKX0i_68cTD.svg)

 |
| 

`@imgly/SettingsCog`

 | 

![SettingsCog Icon](/docs/cesdk/_astro/SettingsCog.CHzkR7oC_68cTD.svg)

 |
| 

`@imgly/ShapeOval`

 | 

![ShapeOval Icon](/docs/cesdk/_astro/ShapeOval.CJRIxxg5_68cTD.svg)

 |
| 

`@imgly/ShapePolygon`

 | 

![ShapePolygon Icon](/docs/cesdk/_astro/ShapePolygon.BAIvfUsG_68cTD.svg)

 |
| 

`@imgly/ShapeRectangle`

 | 

![ShapeRectangle Icon](/docs/cesdk/_astro/ShapeRectangle.D_GcPdj4_68cTD.svg)

 |
| 

`@imgly/ShapeStar`

 | 

![ShapeStar Icon](/docs/cesdk/_astro/ShapeStar.ChTrfgau_68cTD.svg)

 |
| 

`@imgly/Shapes`

 | 

![Shapes Icon](/docs/cesdk/_astro/Shapes.bR8cU9cb_68cTD.svg)

 |
| 

`@imgly/Share`

 | 

![Share Icon](/docs/cesdk/_astro/Share.CxVmAh-Q_68cTD.svg)

 |
| 

`@imgly/SidebarOpen`

 | 

![SidebarOpen Icon](/docs/cesdk/_astro/SidebarOpen.DP_Nkz_M_68cTD.svg)

 |
| 

`@imgly/Split`

 | 

![Split Icon](/docs/cesdk/_astro/Split.CtHPO2rr_68cTD.svg)

 |
| 

`@imgly/Sticker`

 | 

![Sticker Icon](/docs/cesdk/_astro/Sticker.giyPqv3w_68cTD.svg)

 |
| 

`@imgly/Stop`

 | 

![Stop Icon](/docs/cesdk/_astro/Stop.Dk91ehJn_68cTD.svg)

 |
| 

`@imgly/Straighten`

 | 

![Straighten Icon](/docs/cesdk/_astro/Straighten.QTpTGn7c_68cTD.svg)

 |
| 

`@imgly/StrokeDash`

 | 

![StrokeDash Icon](/docs/cesdk/_astro/StrokeDash.G2iLl7Ql_68cTD.svg)

 |
| 

`@imgly/StrokeDotted`

 | 

![StrokeDotted Icon](/docs/cesdk/_astro/StrokeDotted.BNij6pGg_68cTD.svg)

 |
| 

`@imgly/StrokePositionCenter`

 | 

![StrokePositionCenter Icon](/docs/cesdk/_astro/StrokePositionCenter.DLGkhfZI_68cTD.svg)

 |
| 

`@imgly/StrokePositionInside`

 | 

![StrokePositionInside Icon](/docs/cesdk/_astro/StrokePositionInside.YLPd54Fr_68cTD.svg)

 |
| 

`@imgly/StrokePositionOutside`

 | 

![StrokePositionOutside Icon](/docs/cesdk/_astro/StrokePositionOutside.BToQBEp3_68cTD.svg)

 |
| 

`@imgly/StrokeSolid`

 | 

![StrokeSolid Icon](/docs/cesdk/_astro/StrokeSolid.BbQK_ttd_68cTD.svg)

 |
| 

`@imgly/StrokeWeight`

 | 

![StrokeWeight Icon](/docs/cesdk/_astro/StrokeWeight.p9i4NW18_68cTD.svg)

 |
| 

`@imgly/Template`

 | 

![Template Icon](/docs/cesdk/_astro/Template.DiqM4ifM_68cTD.svg)

 |
| 

`@imgly/Text`

 | 

![Text Icon](/docs/cesdk/_astro/Text.D20mu4op_68cTD.svg)

 |
| 

`@imgly/TextAlignBottom`

 | 

![TextAlignBottom Icon](/docs/cesdk/_astro/TextAlignBottom.Lrl-KvaG_68cTD.svg)

 |
| 

`@imgly/TextAlignCenter`

 | 

![TextAlignCenter Icon](/docs/cesdk/_astro/TextAlignCenter.GaFLxW6o_68cTD.svg)

 |
| 

`@imgly/TextAlignLeft`

 | 

![TextAlignLeft Icon](/docs/cesdk/_astro/TextAlignLeft.JPvbI_Iv_68cTD.svg)

 |
| 

`@imgly/TextAlignMiddle`

 | 

![TextAlignMiddle Icon](/docs/cesdk/_astro/TextAlignMiddle.Cc4CeA8h_68cTD.svg)

 |
| 

`@imgly/TextAlignRight`

 | 

![TextAlignRight Icon](/docs/cesdk/_astro/TextAlignRight.DtFvwWBW_68cTD.svg)

 |
| 

`@imgly/TextAlignTop`

 | 

![TextAlignTop Icon](/docs/cesdk/_astro/TextAlignTop.BlMx73E2_68cTD.svg)

 |
| 

`@imgly/TextAutoHeight`

 | 

![TextAutoHeight Icon](/docs/cesdk/_astro/TextAutoHeight.fSi8isZl_68cTD.svg)

 |
| 

`@imgly/TextAutoSize`

 | 

![TextAutoSize Icon](/docs/cesdk/_astro/TextAutoSize.Bp4copWt_68cTD.svg)

 |
| 

`@imgly/TextBold`

 | 

![TextBold Icon](/docs/cesdk/_astro/TextBold.DQnuwuNI_68cTD.svg)

 |
| 

`@imgly/TextFixedSize`

 | 

![TextFixedSize Icon](/docs/cesdk/_astro/TextFixedSize.8ULsWSkZ_68cTD.svg)

 |
| 

`@imgly/TextItalic`

 | 

![TextItalic Icon](/docs/cesdk/_astro/TextItalic.vCylf_bp_68cTD.svg)

 |
| 

`@imgly/Timeline`

 | 

![Timeline Icon](/docs/cesdk/_astro/Timeline.BZOGSaoW_68cTD.svg)

 |
| 

`@imgly/ToggleIconOff`

 | 

![ToggleIconOff Icon](/docs/cesdk/_astro/ToggleIconOff.tOLH9iio_68cTD.svg)

 |
| 

`@imgly/ToggleIconOn`

 | 

![ToggleIconOn Icon](/docs/cesdk/_astro/ToggleIconOn.C1vynusd_68cTD.svg)

 |
| 

`@imgly/TransformSection`

 | 

![TransformSection Icon](/docs/cesdk/_astro/TransformSection.Cd_1rtk4_68cTD.svg)

 |
| 

`@imgly/TrashBin`

 | 

![TrashBin Icon](/docs/cesdk/_astro/TrashBin.DIRoLX4y_68cTD.svg)

 |
| 

`@imgly/TriangleDown`

 | 

![TriangleDown Icon](/docs/cesdk/_astro/TriangleDown.qVuJ48qB_68cTD.svg)

 |
| 

`@imgly/TriangleUp`

 | 

![TriangleUp Icon](/docs/cesdk/_astro/TriangleUp.BZYFGYKM_68cTD.svg)

 |
| 

`@imgly/TrimMedia`

 | 

![TrimMedia Icon](/docs/cesdk/_astro/TrimMedia.BgO_0rmP_68cTD.svg)

 |
| 

`@imgly/Typeface`

 | 

![Typeface Icon](/docs/cesdk/_astro/Typeface.DqVOeIHT_68cTD.svg)

 |
| 

`@imgly/Undo`

 | 

![Undo Icon](/docs/cesdk/_astro/Undo.CPyRKh4X_68cTD.svg)

 |
| 

`@imgly/Ungroup`

 | 

![Ungroup Icon](/docs/cesdk/_astro/Ungroup.CFB9nh2f_68cTD.svg)

 |
| 

`@imgly/Upload`

 | 

![Upload Icon](/docs/cesdk/_astro/Upload.DXKuDONZ_68cTD.svg)

 |
| 

`@imgly/Video`

 | 

![Video Icon](/docs/cesdk/_astro/Video.DY9tRwlD_68cTD.svg)

 |
| 

`@imgly/VideoCamera`

 | 

![VideoCamera Icon](/docs/cesdk/_astro/VideoCamera.Dlw252lj_68cTD.svg)

 |
| 

`@imgly/Volume`

 | 

![Volume Icon](/docs/cesdk/_astro/Volume.DyYIA3JG_68cTD.svg)

 |
| 

`@imgly/VolumeMute`

 | 

![VolumeMute Icon](/docs/cesdk/_astro/VolumeMute.BPyJ4_Sl_68cTD.svg)

 |
| 

`@imgly/ZoomIn`

 | 

![ZoomIn Icon](/docs/cesdk/_astro/ZoomIn.BldHnJXW_68cTD.svg)

 |
| 

`@imgly/ZoomOut`

 | 

![ZoomOut Icon](/docs/cesdk/_astro/ZoomOut.CC-7T1Td_68cTD.svg)

 |

## Troubleshooting[#](#troubleshooting)

### Custom Icon Not Appearing[#](#custom-icon-not-appearing)

If your custom icon doesn’t display:

*   Verify the symbol ID starts with `@`
*   Check that the SVG sprite syntax is valid XML
*   Confirm `addIconSet()` was called before using the icon
*   Inspect the browser console for SVG parsing errors

### Icon Not Scaling Correctly[#](#icon-not-scaling-correctly)

If your icon renders at the wrong size:

*   Ensure the `viewBox` attribute is set on the symbol
*   Avoid hardcoding `width` and `height` attributes on the symbol
*   Verify the symbol uses relative coordinates within the viewBox

### Icon Color Not Matching Theme[#](#icon-color-not-matching-theme)

If your icon doesn’t change color with the theme:

*   Use `currentColor` for `fill` and `stroke` values in SVG paths
*   Avoid hardcoded color values like `#000000` or `rgb()`
*   Check that `fillOpacity` and `strokeOpacity` use appropriate values for theme compatibility

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `cesdk.ui.addIconSet(id, svgSprite)` | Registers a custom SVG sprite icon set with the given identifier. The sprite should contain `<symbol>` elements with IDs starting with `@`. |
| `cesdk.ui.getDockOrder()` | Returns the current array of dock entries, each containing `id`, `key`, `label`, and `icon` properties. |
| `cesdk.ui.setDockOrder(entries)` | Sets the dock order with the provided array of entries. Use this to modify icons or reorder dock items. |
| `cesdk.ui.registerComponent(id, builder)` | Registers a custom UI component that can be used in menus, panels, and other UI locations. |
| `cesdk.ui.setCanvasMenuOrder(entries)` | Sets the canvas menu entries that appear when users select elements on the canvas. |

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/appearance/custom-labels-7794f7)
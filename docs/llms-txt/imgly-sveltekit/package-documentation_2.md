# Package: documentation

## Classes[#](#classes)

| Class | Description |
| --- | --- |
| [AssetAPI](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/assetapi/) | Manage asset sources and apply assets to scenes. |
| [BlockAPI](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/blockapi/) | Create, manipulate, and query the building blocks of your design. |
| [CreativeEngine](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/creativeengine/) | The CreativeEngine is the core processing unit of CE.SDK and handles state management, rendering, input handling, and much more. It provides APIs to directly interact with assets, blocks, scenes, and variables. These APIs can be used in a headless environment to build and manipulate designs programmatically, or in a browser to create interactive applications. |
| [EditorAPI](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/editorapi/) | Control the design editor’s behavior and settings. |
| [EventAPI](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/eventapi/) | Subscribe to block lifecycle events in the design engine. |
| [SceneAPI](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/sceneapi/) | Create, load, save, and manipulate scenes. |
| [VariableAPI](https://img.ly/docs/cesdk/sveltekit/api/engine/classes/variableapi/) | Manage text variables within design templates. |

## Functions[#](#functions)

| Function | Description |
| --- | --- |
| [checkVideoExportSupport](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/checkvideoexportsupport/) | Throws an error if the current browser does not support video exporting. |
| [checkVideoSupport](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/checkvideosupport/) | Throws an error if the current browser does not support video editing. |
| [\_combineProperties](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/combineproperties/) | Combines multiple reactive properties into a single reactive property. |
| [\_createDerivedProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/createderivedproperty/) | Creates a derived reactive property from one or more sources. |
| [\_createReactiveProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/createreactiveproperty/) | Creates a reactive property with subscribe, value, and update methods. |
| [\_createTrackedProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/createtrackedproperty/) | Creates a reactive property that tracks a source and updates based on a getter/setter. |
| [defaultLogger](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/defaultlogger/) | \- |
| [isCMYKColor](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/iscmykcolor/) | Type guard for [CMYKColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/cmykcolor/). |
| [isRGBAColor](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/isrgbacolor/) | Type guard for [RGBAColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/rgbacolor/). |
| [isSpotColor](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/isspotcolor/) | Type guard for [SpotColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/spotcolor/). |
| [\_makeSource](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/makesource/) | Creates a simple event source that can emit values to subscribed listeners. |
| [\_mergeSources](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/mergesources/) | Merges multiple event sources into a single source that emits when any source emits. |
| [supportsBrowser](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/supportsbrowser/) | Checks if the current browser supports necessary technologies to match our supported browsers |
| [supportsVideo](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/supportsvideo/) | Checks if the current browser supports video editing. |
| [supportsVideoExport](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/supportsvideoexport/) | Checks if the current browser supports video exporting. |
| [supportsWasm](https://img.ly/docs/cesdk/sveltekit/api/engine/functions/supportswasm/) | Checks if the current browser supports web assembly |

## Type Aliases[#](#type-aliases)

| Type Alias | Description |
| --- | --- |
| [AddImageOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/addimageoptions/) | Options for adding images to the scene. |
| [AnimationBaselineDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationbaselinedirection/) | \- |
| [AnimationBlockSwipeTextDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationblockswipetextdirection/) | \- |
| [AnimationEasing](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationeasing/) | \- |
| [AnimationEntry](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationentry/) | Configuration options for animations. |
| [AnimationGrowDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationgrowdirection/) | \- |
| [AnimationJumpLoopDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationjumploopdirection/) | \- |
| [AnimationKenBurnsDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationkenburnsdirection/) | \- |
| [AnimationMergeTextDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationmergetextdirection/) | \- |
| [AnimationOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationoptions/) | Options for configuring animations (in, loop, out animations). |
| [AnimationSpinDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationspindirection/) | \- |
| [AnimationSpinLoopDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationspinloopdirection/) | \- |
| [AnimationType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationtype/) | The block type IDs for the animation blocks. These are the IDs used to create new animations using `cesdk.engine.block.createAnimation(id)`. Refer to [AnimationTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationtypeshorthand/) and [AnimationTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationtypelonghand/) for more details. |
| [AnimationTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationtypelonghand/) | The longhand block type IDs for the animation blocks. These are the IDs used to create new animations using `cesdk.engine.block.createAnimation(id)`. |
| [AnimationTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationtypeshorthand/) | \- |
| [AnimationTypewriterTextWritingStyle](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationtypewritertextwritingstyle/) | \- |
| [AnimationWipeDirection](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationwipedirection/) | \- |
| [ApplicationMimeType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/applicationmimetype/) | Represents the application MIME types used in the editor. |
| [AssetColor](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assetcolor/) | Asset Color payload |
| [AssetGroups](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assetgroups/) | An asset can be member of multiple groups. Groups have a semantic meaning used to build and group UIs exploring the assets, e.g.sections in the content library, or for things like topics in Unsplash for instance. |
| [AssetMetaData](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assetmetadata/) | Generic asset information |
| [AssetProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assetproperty/) | Asset property for payload |
| [AssetTransformPreset](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assettransformpreset/) | Transform preset payload |
| [AudioExportOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/audioexportoptions/) | Represents the options for exporting audio. |
| [AudioFromVideoOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/audiofromvideooptions/) | Options for configuring audio extraction from video operations. |
| [AudioMimeType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/audiomimetype/) | Represents the audio MIME types used in the editor. |
| [BlendMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blendmode/) | \- |
| [BlockEnumType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blockenumtype/) | \- |
| [BlockState](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blockstate/) | Represents the state of a design block. |
| [BlurType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blurtype/) | The block type IDs for the blur blocks. These are the IDs used to create new blurs using `cesdk.engine.block.createBlur(id)`. Refer to [BlurTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blurtypeshorthand/) and [BlurTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blurtypelonghand/) for more details. |
| [BlurTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blurtypelonghand/) | The longhand block type IDs for the blur blocks. These are the IDs used to create new blurs using `cesdk.engine.block.createBlur(id)`. |
| [BlurTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/blurtypeshorthand/) | \- |
| [BooleanOperation](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/booleanoperation/) | Represents the names of boolean operations. |
| [BoolPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/boolpropertyname/) | \- |
| [CameraClampingOvershootMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/cameraclampingovershootmode/) | \- |
| [Canvas](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/canvas/) | An HTML Canvas or an Offscreen Canvas |
| [CaptionHorizontalAlignment](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/captionhorizontalalignment/) | \- |
| [CaptionVerticalAlignment](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/captionverticalalignment/) | \- |
| [CMYK](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/cmyk/) | Represents a color in the CMYK color space. |
| [Color](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) | Represents all color types supported by the engine. |
| [ColorPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/colorpropertyname/) | \- |
| [ColorSpace](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/colorspace/) | Represents the color space used in the editor. |
| [ContentFillMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/contentfillmode/) | \- |
| [CreateSceneOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/createsceneoptions/) | Options for creating a video scene. |
| [CutoutOperation](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/cutoutoperation/) | Represents the type of a cutout. |
| [CutoutType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/cutouttype/) | \- |
| [DefaultAssetSourceId](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/defaultassetsourceid/) | Represents the default asset source IDs used in the editor. |
| [DemoAssetSourceId](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/demoassetsourceid/) | Represents the default demo asset source IDs used in the editor. |
| [DesignBlockId](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designblockid/) | A numerical identifier for a design block |
| [DesignBlockType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designblocktype/) | The block type IDs for the top-level design blocks. These are the IDs used to create new blocks using `cesdk.engine.block.create(id)`. Refer to [DesignBlockTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designblocktypeshorthand/) and [DesignBlockTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designblocktypelonghand/) for more details. |
| [DesignBlockTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designblocktypelonghand/) | The longhand block type IDs for the top-level design blocks. These are the IDs used to create new blocks using `cesdk.engine.block.create(id)`. |
| [DesignBlockTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designblocktypeshorthand/) | \- |
| [DoubleClickSelectionMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/doubleclickselectionmode/) | \- |
| [DoublePropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/doublepropertyname/) | \- |
| [DropShadowOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/dropshadowoptions/) | Options for configuring drop shadow effects on blocks. |
| [EditMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/editmode/) | Represents the current edit mode of the editor. |
| [EffectType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/effecttype/) | The block type IDs for the effect blocks. These are the IDs used to create new effects using `cesdk.engine.block.createEffect(id)`. Refer to [EffectTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/effecttypeshorthand/) and [EffectTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/effecttypelonghand/) for more details. |
| [EffectTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/effecttypelonghand/) | The longhand block type IDs for the effect blocks. These are the IDs used to create new effects using `cesdk.engine.block.createEffect(id)`. |
| [EffectTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/effecttypeshorthand/) | \- |
| [EnginePluginContext](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/engineplugincontext/) | Represents the context for an engine plugin. |
| [EnumPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/enumpropertyname/) | \- |
| [EnumValues](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/enumvalues/) | \- |
| [\_EqualsFn](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/equalsfn/) | A function that compares two values for equality |
| [ExportOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/exportoptions/) | Represents the options for exporting a design block. |
| [FillPixelStreamOrientation](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/fillpixelstreamorientation/) | \- |
| [FillType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/filltype/) | The block type IDs for the fill blocks. These are the IDs used to create new fills using `cesdk.engine.block.createFill(id)`. Refer to [FillTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/filltypeshorthand/) and [FillTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/filltypelonghand/) for more details. |
| [FillTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/filltypelonghand/) | The longhand block type IDs for the fill blocks. These are the IDs used to create new fills using `cesdk.engine.block.createFill(id)`. |
| [FillTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/filltypeshorthand/) | \- |
| [FloatPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/floatpropertyname/) | \- |
| [FontSizeUnit](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/fontsizeunit/) | Extended design unit type that includes Point for font size operations. Maintains consistency with SceneDesignUnit’s capitalized naming convention. |
| [FontStyle](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/fontstyle/) | Represents the style of a font. |
| [FontWeight](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/fontweight/) | Represents the weight of a font. |
| [GradientstopRGBA](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/gradientstoprgba/) | Represents a gradient stop in the RGBA color space. |
| [HeightMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/heightmode/) | \- |
| [HexColorString](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/hexcolorstring/) | Represents a hexadecimal color value (RGB or RGBA) that starts with a ’#’. |
| [HistoryId](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/historyid/) | A numerical identifier for a history stack |
| [HorizontalBlockAlignment](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/horizontalblockalignment/) | \- |
| [ImageMimeType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/imagemimetype/) | Represents the image MIME types used in the editor. |
| [IntPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/intpropertyname/) | \- |
| [\_LegacySource](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/legacysource/) | A simplified source type for legacy API streams |
| [\_Listener](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/listener/) | A listener function that receives value updates |
| [Locale](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/locale/) | e.g. `en`, `de`, etc. |
| [LogLevel](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/loglevel/) | Provides logging functionality for the Creative Editor SDK. |
| [MimeType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/mimetype/) | Represents the MIME types used in the editor. |
| [ObjectType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/objecttype/) | The block type IDs for all blocks types in the Creative Engine. Those are the types that can be passed to `cesdk.engine.block.findByType(type)` for example. Refer to [ObjectTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/objecttypeshorthand/) and [ObjectTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/objecttypelonghand/) for more details. |
| [ObjectTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/objecttypelonghand/) | The longhand block type IDs for all blocks types in the Creative Engine. Those are the Types returned by the engine when calling `cesdk.engine.block.getType(blockId)` for example. |
| [ObjectTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/objecttypeshorthand/) | The shorthand block type IDs for all blocks types in the Creative Engine. Those are the types that can be passed to `cesdk.engine.block.findByType(type)` for example. |
| [OffscreenCanvas](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/offscreencanvas/) | A simplified placeholder type for `OffscreenCanvas`, to avoid a dependency on `@types/offscreencanvas` |
| [OptionalPrefix](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/optionalprefix/) | \- |
| [PaletteColor](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/palettecolor/) | Represents a color definition for the custom color palette. |
| [PositionMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/positionmode/) | \- |
| [PositionXMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/positionxmode/) | \- |
| [PositionYMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/positionymode/) | \- |
| [PropertyType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/propertytype/) | Represents the various types of properties that can be associated with design blocks. Each type corresponds to a different kind of data that can be used to define the properties of a design block within the system. |
| [RGBA](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rgba/) | Represents a color in the RGBA color space. |
| [RoleString](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rolestring/) | Represents a role string. |
| [DesignUnit](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/designunit/) | \- |
| [SceneLayout](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/scenelayout/) | \- |
| [SceneMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/scenemode/) | \- |
| [Scope](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/scope/) | Represents the various scopes that define the capabilities and permissions within the Creative Editor SDK. Each scope corresponds to a specific functionality or action that can be performed within the editor. |
| [SettingBoolPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingboolpropertyname/) | \- |
| [SettingColorPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingcolorpropertyname/) | \- |
| [SettingEnumPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumpropertyname/) | \- |
| [SettingEnumType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/) | \- |
| [SettingEnumValues](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumvalues/) | \- |
| [SettingFloatPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingfloatpropertyname/) | \- |
| [SettingIntPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingintpropertyname/) | \- |
| [SettingKey](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingkey/) | Union type of all valid setting keys. |
| [SettingsBool](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingsbool/) | \- |
| [SettingsColor](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingscolor/) | Represents the color settings available in the editor. |
| [~SettingsColorRGBA~](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingscolorrgba/) | Represents the color settings available in the editor. |
| [SettingsEnum](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingsenum/) | \- |
| [SettingsFloat](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingsfloat/) | \- |
| [SettingsInt](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingsint/) | \- |
| [SettingsString](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingsstring/) | \- |
| [SettingStringPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingstringpropertyname/) | \- |
| [SettingType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingtype/) | Represents the type of a setting. |
| [SettingValueType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingvaluetype/) | Gets the value type for a specific setting key. |
| [ShapeType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/shapetype/) | The block type IDs for the shape blocks. These are the IDs used to create new shapes using `cesdk.engine.block.createShape(id)`. Refer to [ShapeTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/shapetypeshorthand/) and [ShapeTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/shapetypelonghand/) for more details. |
| [ShapeTypeLonghand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/shapetypelonghand/) | The longhand block type IDs for the blocks. These are the IDs used to create new shapes using `cesdk.engine.block.createShape(id)`. |
| [ShapeTypeShorthand](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/shapetypeshorthand/) | \- |
| [SizeMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/sizemode/) | \- |
| [SortingOrder](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/sortingorder/) | The order to sort by if the asset source supports sorting. If set to None, the order is the same as the assets were added to the source. |
| [SourceSetPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/sourcesetpropertyname/) | \- |
| [SplitOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/splitoptions/) | Options for configuring block split operations. |
| [StringPropertyName](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/stringpropertyname/) | \- |
| [StrokeCornerGeometry](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/strokecornergeometry/) | \- |
| [StrokePosition](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/strokeposition/) | \- |
| [StrokeStyle](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/strokestyle/) | \- |
| [\_Subscription](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/subscription/) | Represents a subscription to an event. |
| [TextAnimationWritingStyle](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/textanimationwritingstyle/) | \- |
| [TextCase](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/textcase/) | Represents the text case of a text block. |
| [HorizontalTextAlignment](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/horizontaltextalignment/) | \- |
| [TextVerticalAlignment](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/textverticalalignment/) | \- |
| [TouchPinchAction](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/touchpinchaction/) | \- |
| [TouchRotateAction](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/touchrotateaction/) | \- |
| [~TypefaceDefinition~](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/typefacedefinition/) | Represents a typeface definition used in the editor. |
| [\_Unsubscribe](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/unsubscribe/) | An unsubscribe function that removes a listener |
| [VerticalBlockAlignment](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/verticalblockalignment/) | \- |
| [VideoExportOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/videoexportoptions/) | Represents the options for exporting a video. |
| [VideoMimeType](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/videomimetype/) | Represents the video MIME types used in the editor. |
| [WidthMode](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/widthmode/) | \- |
| [XYWH](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/xywh/) | Describes a rectangle on the screen. |
| [ZoomAutoFitAxis](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/zoomautofitaxis/) | The axis(es) for which to auto-fit. |
| [ZoomOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/zoomoptions/) | Options for zooming to a block with optional animation. |

## Interfaces[#](#interfaces)

| Interface | Description |
| --- | --- |
| [AddVideoOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/addvideooptions/) | Options for adding videos to the scene. |
| [ApplyAssetOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/applyassetoptions/) | Options for applying an asset to the scene. |
| [Asset](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/asset/) | Generic asset information |
| [AssetBooleanProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetbooleanproperty/) | Asset boolean property definition |
| [AssetCMYKColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetcmykcolor/) | Asset Color payload CMYK representation |
| [AssetColorProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetcolorproperty/) | Asset color property definition |
| [AssetDefinition](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetdefinition/) | Definition of an asset used if an asset is added to an asset source. |
| [AssetEnumProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetenumproperty/) | Asset enum property definition |
| [AssetFixedAspectRatio](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetfixedaspectratio/) | Asset transform preset payload fixed aspect ratio |
| [AssetFixedSize](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetfixedsize/) | Asset transform preset payload fixed size |
| [AssetFreeAspectRatio](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetfreeaspectratio/) | Asset transform preset payload free aspect ratio |
| [AssetNumberProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetnumberproperty/) | Asset number property definition |
| [AssetPayload](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetpayload/) | Asset payload |
| [AssetQueryData](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetquerydata/) | Defines a request for querying assets |
| [AssetResult](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) | Single asset result of a query from the engine. |
| [\_AssetResultCredits](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresultcredits/) | Represents the credits for an asset result. |
| [\_AssetResultLicense](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresultlicense/) | Represents the license for an asset result. |
| [AssetRGBColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetrgbcolor/) | Asset Color payload RGB representation |
| [AssetSource](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetsource/) | A source of assets |
| [AssetSpotColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetspotcolor/) | Asset Color payload SpotColor representation |
| [AssetsQueryResult](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetsqueryresult/) | Return type of a `findAssets` query. |
| [AssetStringProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetstringproperty/) | Asset string property definition |
| [AudioTrackInfo](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/audiotrackinfo/) | Information about a single audio track from a video. This interface provides comprehensive metadata about audio tracks, including codec information, technical specifications, and track details. |
| [BlockEvent](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/blockevent/) | Represents an event related to a design block. |
| [BlockStateError](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/blockstateerror/) | Represents an error state for a design block. |
| [BlockStatePending](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/blockstatepending/) | Represents a pending state for a design block. |
| [BlockStateReady](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/blockstateready/) | Represents a ready state for a design block. |
| [BlurEvent](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/blurevent/) | Dispatched on the engine canvas when the text input has been blurred. Call `preventDefault()` to disallow this and refocus the engine text input. |
| [Buffer](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/buffer/) | Represents a buffer of data. |
| [CMYKColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/cmykcolor/) | Represents a CMYK color value. |
| [CompleteAssetResult](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/completeassetresult/) | Asset results that are returned from the engine. |
| [Configuration](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/configuration/) | Specifies the configuration for the Creative Editor SDK. |
| [CursorEvent](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/cursorevent/) | Dispatched on the engine canvas when the text input has been blurred. Call `preventDefault()` to disallow this and refocus the engine text input. |
| [EnginePlugin](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/engineplugin/) | Represents an engine plugin. |
| [\_FindAssetsQuery](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/findassetsquery/) | Represents a query for finding assets. |
| [\_Flip](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/flip/) | Specifies the horizontal and vertical flip states of a design block. |
| [Font](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/font/) | Represents a font. |
| [GradientColorStop](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/gradientcolorstop/) | Represents a gradient color stop. |
| [HTMLCreativeEngineCanvasElement](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/htmlcreativeenginecanvaselement/) | A wrapper around a plain canvas |
| [Logger](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/logger/) | Represents a logger function. |
| [PageDuration](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/pageduration/) | \- |
| [Range](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/range/) | An open range. |
| [Reaction](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reaction/) | Reactions track read calls and provide a way to react if they change. |
| [\_ReactiveProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactiveproperty/) | A reactive property with subscribe, value, and update methods |
| [\_ReactivePropertyOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactivepropertyoptions/) | Options for creating a reactive property |
| [Reactor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactor/) | The reactor coordinates the update of registered _Reactions_. |
| [\_ReadonlyReactiveProperty](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/readonlyreactiveproperty/) | A read-only reactive property with subscribe and value methods |
| [RefocusEvent](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/refocusevent/) | Dispatched on the engine canvas right before the engine will refocus its text input after a blur. Call `preventDefault()` to prevent the refocusing. |
| [RGBAColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/rgbacolor/) | Represents an RGBA color value. |
| [RGBColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/rgbcolor/) | Represents an RGB color value. |
| [Settings](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/settings/) | Map of all available settings with their types. This provides type-safe access to all editor settings. |
| [Size2](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/size2/) | \- |
| [Source](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/source/) | A single source width an intrinsic width & height. |
| [\_Source](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/source-1/) | A source that can emit values to subscribed listeners |
| [SpotColor](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/spotcolor/) | Represents a spot color value. |
| [TextFontSizeOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/textfontsizeoptions/) | Options for text font size operations with unit support. |
| [TransientResource](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/transientresource/) | Represents a transient resource. |
| [Typeface](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/typeface/) | Represents a typeface. |
| [\_UBQAudioFromVideoOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/ubqaudiofromvideooptions/) | Specifies options for configuring audio extraction from video operations. |
| [\_UBQExportAudioOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/ubqexportaudiooptions/) | Specifies options for exporting audio design blocks to various formats. |
| [\_UBQExportOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/ubqexportoptions/) | Specifies options for exporting design blocks to various formats. |
| [\_UBQExportVideoOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/ubqexportvideooptions/) | Specifies options for exporting video design blocks to various formats. |
| [\_UBQSplitOptions](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/ubqsplitoptions/) | Specifies options for configuring block split operations. |
| [Vec2](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/vec2/) | \- |
| [Vec3](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/vec3/) | \- |

## Variables[#](#variables)

| Variable | Description |
| --- | --- |
| [ANIMATION\_TYPES](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animation_types/) | The shorthand block type IDs for the animation blocks. These are the IDs used to create new animations using `cesdk.engine.block.createAnimation(id)`. |
| [AnimationBaselineDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationbaselinedirectionvalues/) | \- |
| [AnimationBlockSwipeTextDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationblockswipetextdirectionvalues/) | \- |
| [AnimationEasingValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationeasingvalues/) | \- |
| [AnimationGrowDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationgrowdirectionvalues/) | \- |
| [AnimationJumpLoopDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationjumploopdirectionvalues/) | \- |
| [AnimationKenBurnsDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationkenburnsdirectionvalues/) | \- |
| [AnimationMergeTextDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationmergetextdirectionvalues/) | \- |
| [AnimationSpinDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationspindirectionvalues/) | \- |
| [AnimationSpinLoopDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationspinloopdirectionvalues/) | \- |
| [AnimationTypewriterTextWritingStyleValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationtypewritertextwritingstylevalues/) | \- |
| [AnimationWipeDirectionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/animationwipedirectionvalues/) | \- |
| [BlendModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/blendmodevalues/) | \- |
| [BLUR\_TYPES](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/blur_types/) | The shorthand block type IDs for the blur blocks. These are the IDs used to create new blurs using `cesdk.engine.block.createBlur(id)`. |
| [CameraClampingOvershootModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/cameraclampingovershootmodevalues/) | \- |
| [CaptionHorizontalAlignmentValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/captionhorizontalalignmentvalues/) | \- |
| [CaptionVerticalAlignmentValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/captionverticalalignmentvalues/) | \- |
| [ContentFillModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/contentfillmodevalues/) | \- |
| [CutoutTypeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/cutouttypevalues/) | \- |
| [DESIGN\_BLOCK\_TYPES](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/design_block_types/) | The shorthand block type IDs for the top-level design blocks. These are the IDs used to create new blocks using `cesdk.engine.block.create(id)`. |
| [DoubleClickSelectionModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/doubleclickselectionmodevalues/) | \- |
| [EFFECT\_TYPES](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/effect_types/) | The shorthand block type IDs for the effect blocks. These are the IDs used to create new effects using `cesdk.engine.block.createEffect(id)`. |
| [FILL\_TYPES](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/fill_types/) | The shorthand block type IDs for the fill blocks. These are the IDs used to create new fills using `cesdk.engine.block.createFill(id)`. |
| [FillPixelStreamOrientationValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/fillpixelstreamorientationvalues/) | \- |
| [HeightModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/heightmodevalues/) | \- |
| [~LogLevel~](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/loglevel/) | Provides a set of predefined log levels for the Creative Editor SDK. |
| [~MimeType~](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/mimetype/) | Represents the MIME types used in the editor. |
| [PositionXModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/positionxmodevalues/) | \- |
| [PositionYModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/positionymodevalues/) | \- |
| [SceneDesignUnitValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/scenedesignunitvalues/) | \- |
| [SceneLayoutValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/scenelayoutvalues/) | \- |
| [SceneModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/scenemodevalues/) | \- |
| [SHAPE\_TYPES](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/shape_types/) | The shorthand block type IDs for the shape blocks. These are the IDs used to create new shapes using `cesdk.engine.block.createShape(id)`. |
| [StrokeCornerGeometryValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/strokecornergeometryvalues/) | \- |
| [StrokePositionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/strokepositionvalues/) | \- |
| [StrokeStyleValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/strokestylevalues/) | \- |
| [TextAnimationWritingStyleValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/textanimationwritingstylevalues/) | \- |
| [TextHorizontalAlignmentValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/texthorizontalalignmentvalues/) | \- |
| [TextVerticalAlignmentValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/textverticalalignmentvalues/) | \- |
| [TouchPinchActionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/touchpinchactionvalues/) | \- |
| [TouchRotateActionValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/touchrotateactionvalues/) | \- |
| [WidthModeValues](https://img.ly/docs/cesdk/sveltekit/api/engine/variables/widthmodevalues/) | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api-reference/overview-8f24e1)
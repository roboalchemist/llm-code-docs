# Package: documentation

## Classes[#](#classes)

| Class | Description |
| --- | --- |
| [AssetAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/assetapi/) | Manage asset sources and apply assets to scenes. |
| [BlockAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/blockapi/) | Create, manipulate, and query the building blocks of your design. |
| [CreativeEngine](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/creativeengine/) | The CreativeEngine is the core processing unit of CE.SDK and handles state management, rendering, input handling, and much more. It provides APIs to directly interact with assets, blocks, scenes, and variables. These APIs can be used in a headless environment to build and manipulate designs programmatically, or in a browser to create interactive applications. |
| [EditorAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/editorapi/) | Control the design editor’s behavior and settings. |
| [EventAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/eventapi/) | Subscribe to block lifecycle events in the design engine. |
| [SceneAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/sceneapi/) | Create, load, save, and manipulate scenes. |
| [VariableAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/variableapi/) | Manage text variables within design templates. |
| [ActionsAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/actionsapi/) | ActionsAPI provides a centralized way to manage and customize actions for various user interactions in the Creative Engine SDK. |
| [CreativeEditorSDK](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/creativeeditorsdk/) | The main entry point for the Creative Editor SDK. |
| [FeatureAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/featureapi/) | Controls the availability of features within the Creative Editor SDK. |
| [InternationalizationAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/internationalizationapi/) | Manages localization and internationalization settings for the Creative Editor SDK. |
| [UserInterfaceAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/userinterfaceapi/) | Control the user interface and behavior of the Creative Editor SDK. |
| [UtilsAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/classes/utilsapi/) | UtilsAPI provides utility functions for common operations in the Creative Engine SDK. |

## Functions[#](#functions)

| Function | Description |
| --- | --- |
| [supportsBrowser](https://img.ly/docs/cesdk/vue/api/cesdk-js/functions/supportsbrowser/) | Checks if the current browser supports necessary technologies to match our supported browsers |
| [checkVideoSupport](https://img.ly/docs/cesdk/vue/api/cesdk-js/functions/checkvideosupport/) | Throws an error if the current browser does not support video editing. |
| [supportsVideo](https://img.ly/docs/cesdk/vue/api/cesdk-js/functions/supportsvideo/) | Checks if the current browser supports video editing. |
| [checkVideoExportSupport](https://img.ly/docs/cesdk/vue/api/cesdk-js/functions/checkvideoexportsupport/) | Throws an error if the current browser does not support video exporting. |
| [supportsVideoExport](https://img.ly/docs/cesdk/vue/api/cesdk-js/functions/supportsvideoexport/) | Checks if the current browser supports video exporting. |
| [supportsWasm](https://img.ly/docs/cesdk/vue/api/cesdk-js/functions/supportswasm/) | Checks if the current browser supports web assembly |

## Type Aliases[#](#type-aliases)

| Type Alias | Description |
| --- | --- |
| [SizeMode](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sizemode/) | \- |
| [PositionMode](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/positionmode/) | \- |
| [VerticalBlockAlignment](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/verticalblockalignment/) | \- |
| [HorizontalBlockAlignment](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/horizontalblockalignment/) | \- |
| [PropertyType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/propertytype/) | Represents the various types of properties that can be associated with design blocks. Each type corresponds to a different kind of data that can be used to define the properties of a design block within the system. |
| [TextCase](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/textcase/) | Represents the text case of a text block. |
| [BooleanOperation](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/booleanoperation/) | Represents the names of boolean operations. |
| [EngineExportOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/engineexportoptions/) | Represents the options for exporting a design block. |
| [VideoExportOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videoexportoptions/) | Represents the options for exporting a video. |
| [AudioExportOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/audioexportoptions/) | Represents the options for exporting audio. |
| [SplitOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/splitoptions/) | Options for configuring block split operations. |
| [DropShadowOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dropshadowoptions/) | Options for configuring drop shadow effects on blocks. |
| [AnimationEntry](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationentry/) | Configuration options for animations. |
| [AnimationOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationoptions/) | Options for configuring animations (in, loop, out animations). |
| [AddImageOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/addimageoptions/) | Options for adding images to the scene. |
| [SettingType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingtype/) | Represents the type of a setting. |
| [SettingsBool](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingsbool/) | \- |
| [SettingsString](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingsstring/) | \- |
| [SettingsFloat](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingsfloat/) | \- |
| [SettingsColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingscolor/) | Represents the color settings available in the editor. |
| [~SettingsColorRGBA~](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingscolorrgba/) | Represents the color settings available in the editor. |
| [SettingsEnum](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/settingsenum/) | \- |
| [ZoomOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomoptions/) | Options for zooming to a block with optional animation. |
| [CreateSceneOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/createsceneoptions/) | Options for creating a video scene. |
| [DefaultAssetSourceId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/defaultassetsourceid/) | Represents the default asset source IDs used in the editor. |
| [DemoAssetSourceId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/demoassetsourceid/) | Represents the default demo asset source IDs used in the editor. |
| [~TypefaceDefinition~](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/typefacedefinition/) | Represents a typeface definition used in the editor. |
| [EnginePluginContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/engineplugincontext/) | Represents the context for an engine plugin. |
| [LogLevel](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/loglevel/) | Provides logging functionality for the Creative Editor SDK. |
| [MimeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/mimetype/) | Represents the MIME types used in the editor. |
| [ImageMimeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/imagemimetype/) | Represents the image MIME types used in the editor. |
| [AudioMimeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/audiomimetype/) | Represents the audio MIME types used in the editor. |
| [VideoMimeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videomimetype/) | Represents the video MIME types used in the editor. |
| [ApplicationMimeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/applicationmimetype/) | Represents the application MIME types used in the editor. |
| [AssetGroups](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetgroups/) | An asset can be member of multiple groups. Groups have a semantic meaning used to build and group UIs exploring the assets, e.g.sections in the content library, or for things like topics in Unsplash for instance. |
| [SortingOrder](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sortingorder/) | The order to sort by if the asset source supports sorting. If set to None, the order is the same as the assets were added to the source. |
| [AssetMetaData](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetmetadata/) | Generic asset information |
| [AssetColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetcolor/) | Asset Color payload |
| [AssetTransformPreset](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assettransformpreset/) | Transform preset payload |
| [AssetProperty](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetproperty/) | Asset property for payload |
| [DesignBlockTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblocktypeshorthand/) | \- |
| [DesignBlockTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblocktypelonghand/) | The longhand block type IDs for the top-level design blocks. These are the IDs used to create new blocks using `cesdk.engine.block.create(id)`. |
| [DesignBlockType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblocktype/) | The block type IDs for the top-level design blocks. These are the IDs used to create new blocks using `cesdk.engine.block.create(id)`. Refer to [DesignBlockTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblocktypeshorthand/) and [DesignBlockTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblocktypelonghand/) for more details. |
| [ShapeTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/shapetypeshorthand/) | \- |
| [ShapeTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/shapetypelonghand/) | The longhand block type IDs for the blocks. These are the IDs used to create new shapes using `cesdk.engine.block.createShape(id)`. |
| [ShapeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/shapetype/) | The block type IDs for the shape blocks. These are the IDs used to create new shapes using `cesdk.engine.block.createShape(id)`. Refer to [ShapeTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/shapetypeshorthand/) and [ShapeTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/shapetypelonghand/) for more details. |
| [FillTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filltypeshorthand/) | \- |
| [FillTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filltypelonghand/) | The longhand block type IDs for the fill blocks. These are the IDs used to create new fills using `cesdk.engine.block.createFill(id)`. |
| [FillType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filltype/) | The block type IDs for the fill blocks. These are the IDs used to create new fills using `cesdk.engine.block.createFill(id)`. Refer to [FillTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filltypeshorthand/) and [FillTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filltypelonghand/) for more details. |
| [EffectTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/effecttypeshorthand/) | \- |
| [EffectTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/effecttypelonghand/) | The longhand block type IDs for the effect blocks. These are the IDs used to create new effects using `cesdk.engine.block.createEffect(id)`. |
| [EffectType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/effecttype/) | The block type IDs for the effect blocks. These are the IDs used to create new effects using `cesdk.engine.block.createEffect(id)`. Refer to [EffectTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/effecttypeshorthand/) and [EffectTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/effecttypelonghand/) for more details. |
| [BlurTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blurtypeshorthand/) | \- |
| [BlurTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blurtypelonghand/) | The longhand block type IDs for the blur blocks. These are the IDs used to create new blurs using `cesdk.engine.block.createBlur(id)`. |
| [BlurType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blurtype/) | The block type IDs for the blur blocks. These are the IDs used to create new blurs using `cesdk.engine.block.createBlur(id)`. Refer to [BlurTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blurtypeshorthand/) and [BlurTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blurtypelonghand/) for more details. |
| [AnimationTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationtypeshorthand/) | \- |
| [AnimationTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationtypelonghand/) | The longhand block type IDs for the animation blocks. These are the IDs used to create new animations using `cesdk.engine.block.createAnimation(id)`. |
| [AnimationType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationtype/) | The block type IDs for the animation blocks. These are the IDs used to create new animations using `cesdk.engine.block.createAnimation(id)`. Refer to [AnimationTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationtypeshorthand/) and [AnimationTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationtypelonghand/) for more details. |
| [ObjectTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttypeshorthand/) | The shorthand block type IDs for all blocks types in the Creative Engine. Those are the types that can be passed to `cesdk.engine.block.findByType(type)` for example. |
| [ObjectTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttypelonghand/) | The longhand block type IDs for all blocks types in the Creative Engine. Those are the Types returned by the engine when calling `cesdk.engine.block.getType(blockId)` for example. |
| [ObjectType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttype/) | The block type IDs for all blocks types in the Creative Engine. Those are the types that can be passed to `cesdk.engine.block.findByType(type)` for example. Refer to [ObjectTypeShorthand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttypeshorthand/) and [ObjectTypeLonghand](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttypelonghand/) for more details. |
| [OffscreenCanvas](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/offscreencanvas/) | A simplified placeholder type for `OffscreenCanvas`, to avoid a dependency on `@types/offscreencanvas` |
| [Canvas](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvas/) | An HTML Canvas or an Offscreen Canvas |
| [HexColorString](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/hexcolorstring/) | Represents a hexadecimal color value (RGB or RGBA) that starts with a ’#’. |
| [PaletteColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/palettecolor/) | Represents a color definition for the custom color palette. |
| [ColorSpace](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/colorspace/) | Represents the color space used in the editor. |
| [CutoutOperation](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/cutoutoperation/) | Represents the type of a cutout. |
| [DesignBlockId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblockid/) | A numerical identifier for a design block |
| [HistoryId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/historyid/) | A numerical identifier for a history stack |
| [ZoomAutoFitAxis](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomautofitaxis/) | The axis(es) for which to auto-fit. |
| [EditMode](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/editmode/) | Represents the current edit mode of the editor. |
| [FontWeight](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/fontweight/) | Represents the weight of a font. |
| [FontStyle](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/fontstyle/) | Represents the style of a font. |
| [BlendMode](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blendmode/) | \- |
| [ContentFillMode](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/contentfillmode/) | \- |
| [DesignUnit](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designunit/) | \- |
| [SceneLayout](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scenelayout/) | \- |
| [SceneMode](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scenemode/) | \- |
| [StrokeCornerGeometry](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/strokecornergeometry/) | \- |
| [StrokePosition](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/strokeposition/) | \- |
| [StrokeStyle](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/strokestyle/) | \- |
| [CutoutType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/cutouttype/) | \- |
| [AnimationEasing](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationeasing/) | \- |
| [RoleString](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rolestring/) | Represents a role string. |
| [Scope](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scope/) | Represents the various scopes that define the capabilities and permissions within the Creative Editor SDK. Each scope corresponds to a specific functionality or action that can be performed within the editor. |
| [RGBA](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/) | Represents a color in the RGBA color space. |
| [CMYK](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/cmyk/) | Represents a color in the CMYK color space. |
| [XYWH](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/xywh/) | Describes a rectangle on the screen. |
| [GradientstopRGBA](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/gradientstoprgba/) | Represents a gradient stop in the RGBA color space. |
| [BlockState](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blockstate/) | Represents the state of a design block. |
| [ActionFunction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/actionfunction/) | Type helper for retrieving the correct action function type based on the action ID. Returns the strongly-typed action for known actions, or a custom action type for unknown IDs. |
| [ActionId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/actionid/) | Available action event types that can be registered with the ActionsAPI. These correspond to different UI actions that can be customized. Supports both predefined action types from the Actions interface and custom string identifiers. |
| [AssetEntryId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/) | Asset library entry IDs that can be used with asset library APIs. Includes built-in entry IDs registered by the SDK, and allows custom entry IDs. |
| [AssetLibraryDockComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetlibrarydockcomponent/) | Represents an asset library dock component. |
| [AssetLibraryPanelPayload](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetlibrarypanelpayload/) | Represents the payload for the asset library panel in the Creative Editor SDK. This interface defines the title, entries, and placement options for the asset library panel. |
| [BuilderRenderFunction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/builderrenderfunction/) | Function that defines a component with the help of the passed builder object. |
| [CanvasBarComponentId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/) | Represents the ID of a canvas bar component. |
| [CanvasMenuComponentId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/) | A list of the component IDs that can be used in the canvas menu. |
| [CanvasMenuComponents](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponents/) | \- |
| [CanvasMenuOrderComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenuordercomponent/) | \- |
| [ChildrenOrder](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/childrenorder/) | Represents the order of children components in a dropdown. |
| [ComponentId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/componentid/) | Represents the ID of a component. |
| [Configuration](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/configuration/) | Represents the user-provided configuration for the Creative Editor SDK. This type allows for partial configuration settings, making all properties optional. |
| [CopyAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/copyaction/) | Action function for copying selected blocks to the clipboard |
| [CustomActionFunction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/customactionfunction/) | A generic action function type for custom actions. Supports both synchronous and asynchronous implementations with flexible parameters. |
| [CustomPanelMountFunction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/custompanelmountfunction/) | Represents a function that mounts a custom panel. |
| [DialogAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogaction/) | Represents an action in the dialog. |
| [DialogContent](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogcontent/) | Represents the content of the dialog. |
| [DialogProgress](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogprogress/) | Represents the progress of the dialog. |
| [DialogSize](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogsize/) | Represents the size of the dialog. |
| [DialogType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogtype/) | Represents the type of dialog. |
| [DockOrderComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponent/) | Represents a dock order component. |
| [DockOrderComponentId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/) | Represents the ID of a dock order component. |
| [EditorPluginContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/editorplugincontext/) | Represents the context for an editor plugin. This type extends the `EnginePluginContext` with an optional `cesdk` property. |
| [ExportAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/exportaction/) | Action function for handling export operations. Can be called with or without options to customize the export behavior. Supports both standard and video export workflows through a generic type parameter. The return type is automatically inferred based on the input options type. |
| [ExportSceneAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/exportsceneaction/) | Action function for handling scene export operations. |
| [FeatureId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) | All built-in CE.SDK Feature Ids. |
| [FeaturePredicate](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featurepredicate/) | The feature predicate is used to enable or disable a feature based on the boolean or the return value of the function. |
| [FeaturePredicateContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featurepredicatecontext/) | Represents the context for enabling a feature. This type extends `IsEnabledFeatureContext` and includes a function to check the previous enable state and a function to get the default predicate. |
| [FileMimeType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filemimetype/) | Represents the MIME types for files supported by the file operations in UtilsAPI. |
| [ImportSceneAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/importsceneaction/) | Action function for handling scene import operations. |
| [InsertOrderComponentLocation](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/insertordercomponentlocation/) | Represents the location for inserting an order component. |
| [InspectorBarComponentId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/) | Represents the ID of an inspector bar component. |
| [IsEnabledFeatureContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/isenabledfeaturecontext/) | Represents the context for determining if a feature is enabled. This type includes the `CreativeEngine` instance. |
| [LocaleKey](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/localekey/) | Represents the supported locale keys for the Creative Editor SDK. |
| [NavigationBarComponentId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/) | A list of the component IDs that can be used in the navigation bar. |
| [NavigationBarComponents](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponents/) | \- |
| [NavigationBarOrderComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarordercomponent/) | \- |
| [NotificationDuration](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/notificationduration/) | Represents the duration of the notification. |
| [NotificationType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/notificationtype/) | Represents the type of notification. |
| [OnExportOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onexportoptions/) | This interface extends the base ExportOptions with additional information about the export, including which design blocks were exported and the mimeType. |
| [OnExportVideoOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onexportvideooptions/) | This interface extends the base VideoExportOptions with additional information about the export, including which design blocks were exported and the mimeType. |
| [OnUnsupportedBrowserAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onunsupportedbrowseraction/) | Action function that is invoked when an unsupported browser is detected. This allows custom handling of unsupported browser scenarios. |
| [Optional](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/optional/) | Turn value at K of T into a Partial |
| [OrderComponentMatcher](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/) | Represents a matcher for order components. |
| [PageFormatDefinition](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/pageformatdefinition/) | Represents the definition of a page format in the Creative Editor SDK. This interface defines the width, height, unit, and optional fixed orientation for a page format. |
| [PanelDisposer](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/paneldisposer/) | Represents a function that disposes of a panel. |
| [PanelId](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelid/) | Represents a unique identifier for a panel in the Creative Editor SDK. This type defines specific panel IDs and allows for custom panel IDs. |
| [PanelOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/paneloptions/) | Represents the options for a panel in the Creative Editor SDK. This interface defines the options for a panel, including whether it is closable by the user, its position, whether it is floating, and its payload. |
| [PanelPayload](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelpayload/) | Represents the payload for a panel in the Creative Editor SDK. This type defines the payload based on the panel ID. |
| [PasteAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/pasteaction/) | Action function for pasting blocks from the clipboard |
| [PreviewType](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/previewtype/) | Represents a preview, which can be either an image or a color. |
| [PreviewTypeColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/previewtypecolor/) | Represents a color preview. |
| [PreviewTypeImage](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/previewtypeimage/) | Represents an image preview. |
| [SaveSceneAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/savesceneaction/) | Action function for handling scene saving operations. |
| [ScrollToBlockAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scrolltoblockaction/) | Action function for scrolling to a specific block |
| [ScrollToPageAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scrolltopageaction/) | Action function for scrolling to a specific page |
| [ShareSceneAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sharesceneaction/) | Action function for handling scene sharing operations. |
| [Suffix](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/suffix/) | Represents additional options for a button, which can be used as a suffix. |
| [TimelineCollapseAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelinecollapseaction/) | Action function for collapsing the video timeline |
| [TimelineExpandAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelineexpandaction/) | Action function for expanding the video timeline |
| [TimelineZoomInAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelinezoominaction/) | Action function for zooming in the video timeline by one step |
| [TimelineZoomOutAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelinezoomoutaction/) | Action function for zooming out the video timeline by one step |
| [TimelineZoomResetAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelinezoomresetaction/) | Action function for resetting the video timeline zoom to default level (1.0) |
| [TimelineZoomToFitAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelinezoomtofitaction/) | Action function for fitting the video timeline to show all content |
| [TimelineZoomToLevelAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/timelinezoomtolevelaction/) | Action function for setting the video timeline zoom to a specific level |
| [UnknownPanelPayload](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/unknownpanelpayload/) | Represents an unknown payload for a panel in the Creative Editor SDK. This type defines a generic payload with unknown keys and values. |
| [UnknownTranslations](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/unknowntranslations/) | Allows for custom translation keys beyond the built-in ones. |
| [UploadAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/uploadaction/) | Action function for uploading files to asset sources. |
| [ViewStyle](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/viewstyle/) | Represents the view style options in the Creative Editor SDK. This type defines the possible view styles, which are ‘advanced’ and ‘default’. |
| [ZoomInAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoominaction/) | Action function for zooming in by one step |
| [ZoomOutAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomoutaction/) | Action function for zooming out by one step |
| [ZoomToBlockAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomtoblockaction/) | Action function for zooming to a specific block |
| [ZoomToLevelAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomtolevelaction/) | Action function for setting zoom to a specific level |
| [ZoomToPageAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomtopageaction/) | Action function for zooming to a page with optional padding |
| [ZoomToSelectionAction](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomtoselectionaction/) | Action function for zooming to the current selection |

## Enumerations[#](#enumerations)

| Enumeration | Description |
| --- | --- |
| [PanelPosition](https://img.ly/docs/cesdk/vue/api/cesdk-js/enumerations/panelposition/) | This enum is used to specify the position of various panels within the user interface, such as the inspector, settings, and asset library panels. |

## Interfaces[#](#interfaces)

| Interface | Description |
| --- | --- |
| [ApplyAssetOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/applyassetoptions/) | Options for applying an asset to the scene. |
| [AddVideoOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/addvideooptions/) | Options for adding videos to the scene. |
| [HTMLCreativeEngineCanvasElement](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/htmlcreativeenginecanvaselement/) | A wrapper around a plain canvas |
| [\_EngineConfiguration](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/engineconfiguration/) | Specifies the configuration for the Creative Editor SDK. |
| [EnginePlugin](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/engineplugin/) | Represents an engine plugin. |
| [Logger](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/logger/) | Represents a logger function. |
| [Source](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/source/) | A single source width an intrinsic width & height. |
| [AssetRGBColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetrgbcolor/) | Asset Color payload RGB representation |
| [AssetCMYKColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetcmykcolor/) | Asset Color payload CMYK representation |
| [AssetSpotColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetspotcolor/) | Asset Color payload SpotColor representation |
| [AssetFixedAspectRatio](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetfixedaspectratio/) | Asset transform preset payload fixed aspect ratio |
| [AssetFreeAspectRatio](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetfreeaspectratio/) | Asset transform preset payload free aspect ratio |
| [AssetFixedSize](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetfixedsize/) | Asset transform preset payload fixed size |
| [AssetStringProperty](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetstringproperty/) | Asset string property definition |
| [AssetNumberProperty](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetnumberproperty/) | Asset number property definition |
| [AssetBooleanProperty](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetbooleanproperty/) | Asset boolean property definition |
| [AssetEnumProperty](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetenumproperty/) | Asset enum property definition |
| [AssetColorProperty](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetcolorproperty/) | Asset color property definition |
| [AssetPayload](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetpayload/) | Asset payload |
| [Asset](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/asset/) | Generic asset information |
| [AssetDefinition](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetdefinition/) | Definition of an asset used if an asset is added to an asset source. |
| [AssetResult](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetresult/) | Single asset result of a query from the engine. |
| [CompleteAssetResult](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/completeassetresult/) | Asset results that are returned from the engine. |
| [AssetQueryData](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetquerydata/) | Defines a request for querying assets |
| [AssetsQueryResult](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetsqueryresult/) | Return type of a `findAssets` query. |
| [AssetSource](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetsource/) | A source of assets |
| [RGBColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/rgbcolor/) | Represents an RGB color value. |
| [RGBAColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/rgbacolor/) | Represents an RGBA color value. |
| [CMYKColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/cmykcolor/) | Represents a CMYK color value. |
| [SpotColor](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/spotcolor/) | Represents a spot color value. |
| [GradientColorStop](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/gradientcolorstop/) | Represents a gradient color stop. |
| [Range](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/range/) | An open range. |
| [Font](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/font/) | Represents a font. |
| [Typeface](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/typeface/) | Represents a typeface. |
| [Buffer](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/buffer/) | Represents a buffer of data. |
| [TransientResource](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/transientresource/) | Represents a transient resource. |
| [BlockEvent](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/blockevent/) | Represents an event related to a design block. |
| [AssetLibraryEntry](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetlibraryentry/) | Represents an entry in the asset library, combining data and view configurations. |
| [Builder](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/builder/) | Interface for all available builder. Depending on the context different implementation might be used. A “Button” in the canvas menu might render different component than a button in the topbar or a panel. |
| [BuilderRenderFunctionContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/builderrenderfunctioncontext/) | Represents the context for rendering a builder function. |
| [BuiltinTranslations](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/builtintranslations/) | Built-in translation keys provided by the Creative Editor SDK. |
| [ButtonGroupOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/buttongroupoptions/) | Represents options for a button group. |
| [ButtonOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/buttonoptions/) | Represents options for a button. |
| [CanvasMenuActionButton](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenuactionbutton/) | Base interface for action buttons in the canvas menu. Contains common properties shared across all canvas menu button types. |
| [CanvasMenuCustomActionButton](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenucustomactionbutton/) | Interface representing a custom canvas menu action button. Note: This component requires a key and has a required label, unlike other action buttons. |
| [CanvasMenuOptionsComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenuoptionscomponent/) | Interface representing the canvas menu options dropdown component. This component can contain children components that are rendered in a dropdown menu. |
| [CESDKConfiguration](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/cesdkconfiguration/) | Represents the configuration settings for the Creative Editor SDK. This interface defines various settings such as locale, theme, development mode, user interface, internationalization, accessibility, callbacks, feature flags, and logger. |
| [CheckboxOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/checkboxoptions/) | Represents options for a checkbox. |
| [ColorInputOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/colorinputoptions/) | Represents options for a color input. |
| [ComponentOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentoptions/) | Represents options for a component. |
| [ComponentPayload](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) | Represents the payload of a component. |
| [CustomDockComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/customdockcomponent/) | Represents a custom dock component. |
| [Dialog](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/dialog/) | Represents a dialog configuration. |
| [DropdownChildrenContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/dropdownchildrencontext/) | Represents the context for the children of a dropdown. |
| [DropdownOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/dropdownoptions/) | Represents options for a dropdown. |
| [EditorPlugin](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/editorplugin/) | Represents an editor plugin. This interface defines the structure of an editor plugin, including its name, version, and initialization function. |
| [ExportOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/exportoptions/) | Specifies options for exporting design blocks to various formats. |
| [HeadingOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/headingoptions/) | Represents options for a heading. |
| [InputOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) | Represents options for an input. |
| [LibraryOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/libraryoptions/) | Represents options for a library. |
| [MediaPreviewOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/mediapreviewoptions/) | Represents options for a media preview. |
| [NavigationBarActionButton](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/navigationbaractionbutton/) | Base interface for action buttons in the navigation bar. Contains common properties shared across all action button types. |
| [NavigationBarCustomActionButton](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/navigationbarcustomactionbutton/) | Interface representing a generic Action Button in the navigation bar component. Note: This component requires a key and has a required label, unlike other action buttons. |
| [Notification](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/notification/) | Represents a notification configuration. |
| [NumberInputOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/numberinputoptions/) | Represents options for a number input. |
| [OrderComponent](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/) | Represents an order component. |
| [OrderComponentWithChildren](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/) | Represents a custom dock component. |
| [OrderContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Interface representing the context for ordering components. |
| [RegisteredActions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/registeredactions/) | Represents a collection of action functions used throughout the application. Each property corresponds to a specific UI action or event that can be customized. |
| [ReplaceAssetLibraryEntriesContext](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/replaceassetlibraryentriescontext/) | Provides context for replacing asset library entries, including selected blocks and default entry IDs. |
| [SectionOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/sectionoptions/) | Represents options for a section. |
| [SelectOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/selectoptions/) | Represents options for a select input. |
| [SelectValue](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/selectvalue/) | Represents a value for a select input. |
| [SliderOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/slideroptions/) | Represents options for a slider. |
| [TextAreaOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/textareaoptions/) | Represents options for a text area. |
| [TextInputOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/textinputoptions/) | Represents options for a text input. |
| [TextOptions](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/textoptions/) | Represents options for text. |
| [Translations](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/translations/) | Complete translation type that includes both built-in and custom translations. |
| [UserInterface](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/userinterface/) | Specifies the configuration for the user interface of the Creative Editor SDK. |

## Namespaces[#](#namespaces)

| Namespace | Description |
| --- | --- |
| [CESDKConfiguration](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/cesdkconfiguration/) | Namespace for `CESDKConfiguration` to include deprecated keys. This namespace includes deprecated keys that are part of the public API via the `CombinedConfiguration` type. These keys are used in the ConfigMigrations but are not used internally. |
| [ConfigTypes](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/) | \- |
| [ExperimentalBuilder](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/experimentalbuilder/) | Namespace containing experimental features for the builder. These features are subject to change and may not be stable for production use. |
| [ExperimentalUserInterfaceAPI](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/experimentaluserinterfaceapi/) | Provides experimental methods for controlling the UI of the Creative Editor SDK. |
| [UserInterfaceElements](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/) | \- |

## Variables[#](#variables)

| Variable | Description |
| --- | --- |
| [~LogLevel~](https://img.ly/docs/cesdk/vue/api/cesdk-js/variables/loglevel/) | Provides a set of predefined log levels for the Creative Editor SDK. |
| [~MimeType~](https://img.ly/docs/cesdk/vue/api/cesdk-js/variables/mimetype/) | Represents the MIME types used in the editor. |

---



[Source](https:/img.ly/docs/cesdk/vue/animation/types-4e5f41)
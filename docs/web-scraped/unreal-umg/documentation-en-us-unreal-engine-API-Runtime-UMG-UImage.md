# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UImage

Title: UImage | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UImage

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The image widget allows you to display a Slate Brush, or texture or material in the UI.

* No Children

|  |  |
| --- | --- |
| _Name_ | UImage |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/Image.h |
| _Include Path_ | #include "Components/Image.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UImage : public UWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → **UImage**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UCommonLazyImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/UCommonLazyImage)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UImage ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/Image.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bFlipForRightToLeftFlowDirection | bool | Flips the image if the localization's flow direction is RightToLeft | Components/Image.h | *EditAnywhere* BlueprintReadWrite *Getter="ShouldFlipForRightToLeftFlowDirection"* Setter="SetFlipForRightToLeftFlowDirection" * Category="Localization" |
| Brush | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) | Image to draw | Components/Image.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetBrush"* FieldNotify * Category=Appearance |
| BrushDelegate | [FGetSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetSlateBrush) | A bindable delegate for the Image. | Components/Image.h |  |
| ColorAndOpacity | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | Color and opacity | Components/Image.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetColorAndOpacity"* Category=Appearance * Meta=(sRGB="true") |
| ColorAndOpacityDelegate | [FGetLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetLinearColor) | A bindable delegate for the ColorAndOpacity. | Components/Image.h |  |
| OnMouseButtonDownEvent | [FOnPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FOnPointerEvent) |  | Components/Image.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& GetBrush() |  | Components/Image.h |  |
| const [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)& GetColorAndOpacity() |  | Components/Image.h |  |
| [UMaterialInstanceDynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInstanceDynamic) * GetDynamicMaterial() |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrush ( const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& InBrush ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromAsset ( [USlateBrushAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USlateBrushAsset)* Asset ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromAtlasInterface ( [TScriptInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TScriptInterface)<[ISlateTextureAtlasInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ISlateTextureAtlasInterface)> AtlasRegion, bool bMatchSize ) | Sets the Brush to the specified Atlas Region. | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromMaterial ( [UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)* Material ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromSoftMaterial ( [TSoftObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSoftObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> SoftMaterial ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromSoftTexture ( [TSoftObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSoftObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> SoftTexture, bool bMatchSize ) | Sets the Brush to the specified Soft Texture. | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromTexture ( [UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)* Texture, bool bMatchSize ) | Sets the Brush to the specified Texture. | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBrushFromTextureDynamic ( [UTexture2DDynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2DDynamic)* Texture, bool bMatchSize ) | Sets the Brush to the specified Dynamic Texture. | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| void SetBrushResourceObject ( [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)* ResourceObject ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| void SetBrushSize ( FVector2D DesiredSize ) |  | Components/Image.h |  |
| void SetBrushTintColor ( [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) TintColor ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| void SetColorAndOpacity ( [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) InColorAndOpacity ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| void SetDesiredSizeOverride ( FVector2D DesiredSize ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| void SetFlipForRightToLeftFlowDirection ( bool InbFlipForRightToLeftFlowDirection ) |  | Components/Image.h |  |
| void SetOpacity ( float InOpacity ) |  | Components/Image.h | *BlueprintCallable* Category="Appearance" |
| bool ShouldFlipForRightToLeftFlowDirection() |  | Components/Image.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/Image.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UImage/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/Image.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/Image.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void CancelImageStreaming() | Called when we need to abort the texture being streamed in. | Components/Image.h |  |
| const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) * ConvertImage ( [TAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TAttribute)<[FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)> InImageAsset ) const | Translates the bound brush data and assigns it to the cached brush used by this widget. | Components/Image.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) HandleMouseButtonDown ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& Geometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Components/Image.h |  |
| [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) K2_Gate_ColorAndOpacity() |  | Components/Image.h |  |
| virtual void OnImageStreamingComplete ( [TSoftObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSoftObjectPtr)<[UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)> LoadedSoftObject ) | Called when the image streaming completes. | Components/Image.h |  |
| virtual void OnImageStreamingStarted ( [TSoftObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSoftObjectPtr)<[UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)> SoftObject ) | Called when the image streaming starts, after the other one was cancelled. | Components/Image.h |  |
| void [RequestAsyncLoad](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UImage/RequestAsyncLoad) ( [TSoftObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSoftObjectPtr)<[UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)> SoftObject, [TFunction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TFunction)< void()>&& Callback ) | Called when we need to stream in content. | Components/Image.h |  |
| virtual void [RequestAsyncLoad](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UImage/RequestAsyncLoad) ( [TSoftObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSoftObjectPtr)<[UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)> SoftObject, FStreamableDelegate DelegateToCall ) |  | Components/Image.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> GetAccessibleWidget() | Gets the widget that accessibility properties should synchronize to. | Components/Image.h |  |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/Image.h |  |

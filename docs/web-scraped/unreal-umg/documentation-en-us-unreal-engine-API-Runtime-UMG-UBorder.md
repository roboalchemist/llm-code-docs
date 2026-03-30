# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBorder

Title: UBorder | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBorder

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

A border is a container widget that can contain one child widget, providing an opportunity to surround it with a background image and adjustable padding.

* Single Child
* Image

|  |  |
| --- | --- |
| _Name_ | UBorder |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/Border.h |
| _Include Path_ | #include "Components/Border.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UBorder : public UContentWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → [UContentWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget) → **UBorder**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UCommonBorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/UCommonBorder)
* [UCommonCustomNavigation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/UCommonCustomNavigation)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UBorder ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/Border.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| Background | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) | Brush to drag as the background | Components/Border.h | *EditAnywhere* BlueprintReadOnly *Category=Appearance* Meta=(DisplayName="Brush") |
| BackgroundDelegate | [FGetSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetSlateBrush) | A bindable delegate for the Brush. | Components/Border.h |  |
| bFlipForRightToLeftFlowDirection | bool | Flips the background image if the localization's flow direction is RightToLeft | Components/Border.h | *EditAnywhere* Category="Localization" |
| BrushColor | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | Color and opacity of the actual border image | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetBrushColor"* Category="Appearance" * Meta=(sRGB="true") |
| BrushColorDelegate | [FGetLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetLinearColor) | A bindable delegate for the BrushColor. | Components/Border.h |  |
| bShowEffectWhenDisabled | uint8 | Whether or not to show the disabled effect when this border is disabled | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter="GetShowEffectWhenDisabled"* Setter="SetShowEffectWhenDisabled" *BlueprintSetter="SetShowEffectWhenDisabled"* Category="Appearance" * AdvancedDisplay |
| ContentColorAndOpacity | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | Color and opacity multiplier of content in the border | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetContentColorAndOpacity"* Category="Content" * Meta=(sRGB="true") |
| ContentColorAndOpacityDelegate | [FGetLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetLinearColor) | A bindable delegate for the ContentColorAndOpacity. | Components/Border.h |  |
| DesiredSizeScale | FVector2D | Scales the computed desired size of this border and its contents. | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetDesiredSizeScale"* Category="Appearance" |
| HorizontalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment)> | The alignment of the content horizontally. | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetHorizontalAlignment"* Category="Content" |
| OnMouseButtonDownEvent | [FOnPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FOnPointerEvent) |  | Components/Border.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |
| OnMouseButtonUpEvent | [FOnPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FOnPointerEvent) |  | Components/Border.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |
| OnMouseDoubleClickEvent | [FOnPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FOnPointerEvent) |  | Components/Border.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |
| OnMouseMoveEvent | [FOnPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FOnPointerEvent) |  | Components/Border.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |
| Padding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) | The padding area between the slot and the content it contains. | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetPadding"* Category="Content" |
| VerticalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment)> | The alignment of the content vertically. | Components/Border.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetVerticalAlignment"* Category="Content" |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) GetBrushColor() |  | Components/Border.h |  |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) GetContentColorAndOpacity() |  | Components/Border.h |  |
| FVector2D GetDesiredSizeScale() | Gets the DesiredSizeScale of this border. | Components/Border.h |  |
| [UMaterialInstanceDynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInstanceDynamic) * GetDynamicMaterial() |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) GetHorizontalAlignment() |  | Components/Border.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetPadding() |  | Components/Border.h |  |
| bool GetShowEffectWhenDisabled() |  | Components/Border.h |  |
| [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) GetVerticalAlignment() |  | Components/Border.h |  |
| void SetBrush ( const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& InBrush ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetBrushColor ( [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) InBrushColor ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetBrushFromAsset ( [USlateBrushAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USlateBrushAsset)* Asset ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetBrushFromMaterial ( [UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)* Material ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetBrushFromTexture ( [UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)* Texture ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetContentColorAndOpacity ( [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) InContentColorAndOpacity ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetDesiredSizeScale ( FVector2D InScale ) | Sets the DesiredSizeScale of this border. | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetHorizontalAlignment ( [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) InHorizontalAlignment ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InPadding ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetShowEffectWhenDisabled ( bool bInShowEffectWhenDisabled ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |
| void SetVerticalAlignment ( [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) InVerticalAlignment ) |  | Components/Border.h | *BlueprintCallable* Category="Appearance" |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/Border.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBorder/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/Border.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/Border.h |  |

#### Overridden from [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void PostEditChangeProperty ( [FPropertyChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FPropertyChangedEvent)& PropertyChangedEvent ) |  | Components/Border.h |  |
| virtual void PostLoad() | Begin [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject). | Components/Border.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) * ConvertImage ( [TAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TAttribute)<[FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)> InImageAsset ) const | Translates the bound brush data and assigns it to the cached brush used by this widget. | Components/Border.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) HandleMouseButtonDown ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& Geometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Components/Border.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) HandleMouseButtonUp ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& Geometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Components/Border.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) HandleMouseDoubleClick ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& Geometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Components/Border.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) HandleMouseMove ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& Geometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Components/Border.h |  |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) K2_Gate_ContentColorAndOpacity() |  | Components/Border.h |  |

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [UClass](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UClass) * GetSlotClass() | [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget). | Components/Border.h |  |
| virtual void OnSlotAdded ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/Border.h |  |
| virtual void OnSlotRemoved ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/Border.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/Border.h |  |

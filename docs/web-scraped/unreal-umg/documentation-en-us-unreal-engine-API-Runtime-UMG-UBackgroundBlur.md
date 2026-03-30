# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlur

Title: UBackgroundBlur | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlur

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

A background blur is a container widget that can contain one child widget, providing an opportunity to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.

* Single Child
* Blur Effect

|  |  |
| --- | --- |
| _Name_ | UBackgroundBlur |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/BackgroundBlur.h |
| _Include Path_ | #include "Components/BackgroundBlur.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UBackgroundBlur : public UContentWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → [UContentWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget) → **UBackgroundBlur**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UBackgroundBlur ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/BackgroundBlur.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bApplyAlphaToBlur | bool | True to modulate the strength of the blur based on the widget alpha. | Components/BackgroundBlur.h | *EditAnywhere* BlueprintReadWrite *Getter=GetApplyAlphaToBlur* Setter=SetApplyAlphaToBlur *BlueprintSetter=SetApplyAlphaToBlur* Category=Content |
| BlurRadius | int32 | This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur A larger value is more costly but allows for stronger blurs. | Components/BackgroundBlur.h | *EditAnywhere* AdvancedDisplay *BlueprintReadWrite* Getter *Setter* BlueprintSetter=SetBlurRadius *Category=Appearance* Meta=(ClampMin=0, ClampMax=255, EditCondition="bOverrideAutoRadiusCalculation") |
| BlurStrength | float | How blurry the background is. | Components/BackgroundBlur.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter=SetBlurStrength* Category=Appearance * Meta=(ClampMin=0, ClampMax=100) |
| bOverrideAutoRadiusCalculation | bool | When OverrideAutoRadiusCalculation is set to true, BlurRadius is used for the radius of the blur. | Components/BackgroundBlur.h | *Getter=GetOverrideAutoRadiusCalculation* Setter=SetOverrideAutoRadiusCalculation |
| CornerRadius | FVector4 | Radius in Slate Units applied to the blur widget at each corner. | Components/BackgroundBlur.h | *EditAnywhere* AdvancedDisplay *BlueprintReadWrite* Getter *Setter* BlueprintSetter=SetCornerRadius * Category=Appearance |
| HorizontalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment)> | The alignment of the content horizontally. | Components/BackgroundBlur.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter=SetHorizontalAlignment* Category=Content |
| LowQualityFallbackBrush | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) | An image to draw instead of applying a blur when low quality override mode is enabled. | Components/BackgroundBlur.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter=SetLowQualityFallbackBrush* Category=Appearance |
| Padding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) | The padding area between the slot and the content it contains. | Components/BackgroundBlur.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter=SetPadding* Category=Content |
| VerticalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment)> | The alignment of the content vertically. | Components/BackgroundBlur.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter=SetVerticalAlignment* Category=Content |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| bool GetApplyAlphaToBlur() |  | Components/BackgroundBlur.h |  |
| int32 GetBlurRadius() |  | Components/BackgroundBlur.h |  |
| float GetBlurStrength() |  | Components/BackgroundBlur.h |  |
| FVector4 GetCornerRadius() |  | Components/BackgroundBlur.h |  |
| [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) GetHorizontalAlignment() |  | Components/BackgroundBlur.h |  |
| [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) GetLowQualityFallbackBrush() |  | Components/BackgroundBlur.h |  |
| bool GetOverrideAutoRadiusCalculation() |  | Components/BackgroundBlur.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetPadding() |  | Components/BackgroundBlur.h |  |
| [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) GetVerticalAlignment() |  | Components/BackgroundBlur.h |  |
| void SetApplyAlphaToBlur ( bool bInApplyAlphaToBlur ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| void SetBlurRadius ( int32 InBlurRadius ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetBlurStrength ( float InStrength ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| virtual void SetCornerRadius ( FVector4 InCornerRadius ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| void SetHorizontalAlignment ( [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) InHorizontalAlignment ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| void SetLowQualityFallbackBrush ( const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& InBrush ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| void SetOverrideAutoRadiusCalculation ( bool InOverrideAutoRadiusCalculation ) |  | Components/BackgroundBlur.h |  |
| void SetPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InPadding ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |
| void SetVerticalAlignment ( [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) InVerticalAlignment ) |  | Components/BackgroundBlur.h | *BlueprintCallable* Category="Appearance" |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/BackgroundBlur.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/BackgroundBlur.h |  |

#### Overridden from [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void PostEditChangeProperty ( [FPropertyChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FPropertyChangedEvent)& PropertyChangedEvent ) |  | Components/BackgroundBlur.h |  |
| virtual void PostLoad() | Begin [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject). | Components/BackgroundBlur.h |  |
| virtual void Serialize ( [FArchive](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FArchive)& Ar ) | [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) interface | Components/BackgroundBlur.h |  |

### Protected

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [UClass](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UClass) * GetSlotClass() | [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) interface | Components/BackgroundBlur.h |  |
| virtual void OnSlotAdded ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) | [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) interface | Components/BackgroundBlur.h |  |
| virtual void OnSlotRemoved ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/BackgroundBlur.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/BackgroundBlur.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlur/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/BackgroundBlur.h |  |

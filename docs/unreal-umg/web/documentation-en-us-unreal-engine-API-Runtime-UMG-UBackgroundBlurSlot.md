# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlurSlot

Title: UBackgroundBlurSlot | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlurSlot

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The Slot for the [UBackgroundBlurSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlurSlot), contains the widget displayed in a BackgroundBlur's single slot

|  |  |
| --- | --- |
| _Name_ | UBackgroundBlurSlot |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/BackgroundBlurSlot.h |
| _Include Path_ | #include "Components/BackgroundBlurSlot.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UBackgroundBlurSlot : public UPanelSlot
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot) → **UBackgroundBlurSlot**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UBackgroundBlurSlot ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/BackgroundBlurSlot.h |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| BackgroundBlur | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SBackgroundBlur](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SBackgroundBlur)> | A pointer to the BackgroundBlur to allow us to adjust the size, padding...etc at runtime. | Components/BackgroundBlurSlot.h |  |
| UBackgroundBlur | friend |  | Components/BackgroundBlurSlot.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void BuildSlot ( [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SBackgroundBlur](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SBackgroundBlur)> InBackgroundBlur ) | Builds the underlying slot for the slate BackgroundBlur. | Components/BackgroundBlurSlot.h |  |
| [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) GetHorizontalAlignment() |  | Components/BackgroundBlurSlot.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetPadding() |  | Components/BackgroundBlurSlot.h |  |
| [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) GetVerticalAlignment() |  | Components/BackgroundBlurSlot.h |  |
| void SetHorizontalAlignment ( [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) InHorizontalAlignment ) |  | Components/BackgroundBlurSlot.h | *BlueprintCallable* Category="Layout|Background Blur Slot" |
| void SetPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InPadding ) |  | Components/BackgroundBlurSlot.h | *BlueprintCallable* Category="Layout|Background Blur Slot" |
| void SetVerticalAlignment ( [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) InVerticalAlignment ) |  | Components/BackgroundBlurSlot.h | *BlueprintCallable* Category="Layout|Background Blur Slot" |

#### Overridden from [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void SynchronizeProperties() | Applies all properties to the live slot if possible. | Components/BackgroundBlurSlot.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/BackgroundBlurSlot.h |  |

#### Overridden from [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void PostEditChangeProperty ( [FPropertyChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FPropertyChangedEvent)& PropertyChangedEvent ) |  | Components/BackgroundBlurSlot.h |  |

# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButtonSlot

Title: UButtonSlot | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButtonSlot

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The Slot for the [UButtonSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButtonSlot), contains the widget displayed in a button's single slot

|  |  |
| --- | --- |
| _Name_ | UButtonSlot |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/ButtonSlot.h |
| _Include Path_ | #include "Components/ButtonSlot.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UButtonSlot : public UPanelSlot
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot) → **UButtonSlot**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UButtonSlot ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/ButtonSlot.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| HorizontalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment)> | The alignment of the object horizontally. | Components/ButtonSlot.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetHorizontalAlignment"* Category="Layout|Button Slot" |
| Padding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) | The padding area between the slot and the content it contains. | Components/ButtonSlot.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetPadding"* Category="Layout|Button Slot" |
| VerticalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment)> | The alignment of the object vertically. | Components/ButtonSlot.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetVerticalAlignment"* Category="Layout|Button Slot" |

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| Button | [TWeakPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TWeakPtr)<[SButton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SButton)> | A pointer to the button to allow us to adjust the size, padding...etc at runtime. | Components/ButtonSlot.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void BuildSlot ( [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SButton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SButton)> InButton ) | Builds the underlying slot for the slate button. | Components/ButtonSlot.h |  |
| [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) GetHorizontalAlignment() |  | Components/ButtonSlot.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetPadding() |  | Components/ButtonSlot.h |  |
| [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) GetVerticalAlignment() |  | Components/ButtonSlot.h |  |
| void SetHorizontalAlignment ( [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) InHorizontalAlignment ) |  | Components/ButtonSlot.h | *BlueprintCallable* Category="Layout|Button Slot" |
| void SetPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InPadding ) |  | Components/ButtonSlot.h | *BlueprintCallable* Category="Layout|Button Slot" |
| void SetVerticalAlignment ( [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) InVerticalAlignment ) |  | Components/ButtonSlot.h | *BlueprintCallable* Category="Layout|Button Slot" |

#### Overridden from [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void SynchronizeProperties() | Applies all properties to the live slot if possible. | Components/ButtonSlot.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/ButtonSlot.h |  |

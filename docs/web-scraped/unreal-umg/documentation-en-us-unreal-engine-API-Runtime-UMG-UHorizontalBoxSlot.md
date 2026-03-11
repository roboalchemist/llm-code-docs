# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UHorizontalBoxSlot

Title: UHorizontalBoxSlot | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UHorizontalBoxSlot

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | UHorizontalBoxSlot |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/HorizontalBoxSlot.h |
| _Include Path_ | #include "Components/HorizontalBoxSlot.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UHorizontalBoxSlot : public UPanelSlot
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot) → **UHorizontalBoxSlot**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UHorizontalBoxSlot ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/HorizontalBoxSlot.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| HorizontalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment)> |  | Components/HorizontalBoxSlot.h | *EditAnywhere* BlueprintReadWrite *Setter* BlueprintSetter="SetHorizontalAlignment" * Category="Layout|Horizontal Box Slot" |
| Padding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) | The amount of padding between the slots parent and the content. | Components/HorizontalBoxSlot.h | *EditAnywhere* BlueprintReadWrite *Setter* BlueprintSetter="SetPadding" * Category="Layout|Horizontal Box Slot" |
| Size | [FSlateChildSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FSlateChildSize) | How much space this slot should occupy in the direction of the panel. | Components/HorizontalBoxSlot.h | *EditAnywhere* BlueprintReadWrite *Setter* BlueprintSetter="SetSize" * Category="Layout|Horizontal Box Slot" |
| VerticalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment)> |  | Components/HorizontalBoxSlot.h | *EditAnywhere* BlueprintReadWrite *Setter* BlueprintSetter="SetVerticalAlignment" * Category="Layout|Horizontal Box Slot" |

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| Slot | [SHorizontalBox::FSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SHorizontalBox/FSlot) * |  | Components/HorizontalBoxSlot.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void BuildSlot ( [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SHorizontalBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SHorizontalBox)> HorizontalBox ) |  | Components/HorizontalBoxSlot.h |  |
| [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) GetHorizontalAlignment() |  | Components/HorizontalBoxSlot.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetPadding() |  | Components/HorizontalBoxSlot.h |  |
| [FSlateChildSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FSlateChildSize) GetSize() |  | Components/HorizontalBoxSlot.h |  |
| [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) GetVerticalAlignment() |  | Components/HorizontalBoxSlot.h |  |
| void SetHorizontalAlignment ( [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) InHorizontalAlignment ) |  | Components/HorizontalBoxSlot.h | *BlueprintCallable* Category="Layout|Horizontal Box Slot" |
| void SetPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InPadding ) |  | Components/HorizontalBoxSlot.h | *BlueprintCallable* Category="Layout|Horizontal Box Slot" |
| void SetSize ( [FSlateChildSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FSlateChildSize) InSize ) |  | Components/HorizontalBoxSlot.h | *BlueprintCallable* Category="Layout|Horizontal Box Slot" |
| void SetVerticalAlignment ( [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) InVerticalAlignment ) |  | Components/HorizontalBoxSlot.h | *BlueprintCallable* Category="Layout|Horizontal Box Slot" |

#### Overridden from [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual bool [NudgeByDesigner](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UHorizontalBoxSlot/NudgeByDesigner) ( const FVector2D& NudgeDirection, const [TOptional](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TOptional)< int32 >& GridSnapSize ) | Called by the designer to "nudge" a widget in a direction. | Components/HorizontalBoxSlot.h |  |
| virtual void SynchronizeFromTemplate ( const [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)*const TemplateSlot ) | Called by the designer when a design-time widget needs to have changes to its associated template synchronized. | Components/HorizontalBoxSlot.h |  |
| virtual void SynchronizeProperties() | Applies all properties to the live slot if possible. | Components/HorizontalBoxSlot.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/HorizontalBoxSlot.h |  |

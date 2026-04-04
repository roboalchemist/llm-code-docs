# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UExpandableArea

Title: UExpandableArea | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UExpandableArea

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | UExpandableArea |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/ExpandableArea.h |
| _Include Path_ | #include "Components/ExpandableArea.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UExpandableArea :  
    public UWidget ,  
    public INamedSlotInterface
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → **UExpandableArea**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)
* [INamedSlotInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/INamedSlotInterface)

Derived Classes
---------------

* [UEditorUtilityExpandableArea](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Editor/Blutility/UEditorUtilityExpandableArea)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UExpandableArea ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/ExpandableArea.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| AreaPadding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) |  | Components/ExpandableArea.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category="Expansion" |
| bIsExpanded | bool |  | Components/ExpandableArea.h | *EditAnywhere* BlueprintReadWrite *Getter="GetIsExpanded"* Setter="SetIsExpanded" *BlueprintGetter="GetIsExpanded"* BlueprintSetter="SetIsExpanded" *FieldNotify* Category="Expansion" |
| BorderBrush | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) |  | Components/ExpandableArea.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category="Style" |
| BorderColor | [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) |  | Components/ExpandableArea.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category="Style" |
| HeaderPadding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) |  | Components/ExpandableArea.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category="Expansion" |
| MaxHeight | float | The maximum height of the area | Components/ExpandableArea.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category="Expansion" |
| OnExpansionChanged | [FOnExpandableAreaExpansionChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnExpandableAreaExpansionChange-) | A bindable delegate for the IsChecked. | Components/ExpandableArea.h | *BlueprintAssignable* Category="ExpandableArea|Event" |
| Style | [FExpandableAreaStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FExpandableAreaStyle) |  | Components/ExpandableArea.h | *EditAnywhere* Category="Style" |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetAreaPadding() |  | Components/ExpandableArea.h |  |
| const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& GetBorderBrush() |  | Components/ExpandableArea.h |  |
| const [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor)& GetBorderColor() |  | Components/ExpandableArea.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetHeaderPadding() |  | Components/ExpandableArea.h |  |
| bool GetIsExpanded() |  | Components/ExpandableArea.h | *BlueprintCallable* Category="Expansion" |
| float GetMaxHeight() |  | Components/ExpandableArea.h |  |
| const [FExpandableAreaStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FExpandableAreaStyle)& GetStyle() |  | Components/ExpandableArea.h |  |
| void SetAreaPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InAreaPadding ) |  | Components/ExpandableArea.h |  |
| void SetBorderBrush ( const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& InBorderBrush ) |  | Components/ExpandableArea.h |  |
| void SetBorderColor ( const [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor)& InBorderColor ) |  | Components/ExpandableArea.h |  |
| void SetHeaderPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InHeaderPadding ) |  | Components/ExpandableArea.h |  |
| void SetIsExpanded ( bool IsExpanded ) |  | Components/ExpandableArea.h | *BlueprintCallable* Category="Expansion" |
| void SetIsExpanded_Animated ( bool IsExpanded ) |  | Components/ExpandableArea.h | *BlueprintCallable* Category="Expansion" |
| void SetMaxHeight ( float InMaxHeight ) |  | Components/ExpandableArea.h |  |
| void SetStyle ( const [FExpandableAreaStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FExpandableAreaStyle)& InStyle ) |  | Components/ExpandableArea.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/ExpandableArea.h |  |
| virtual void OnDescendantDeselectedByDesigner ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* DescendantWidget ) |  | Components/ExpandableArea.h |  |
| virtual void OnDescendantSelectedByDesigner ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* DescendantWidget ) |  | Components/ExpandableArea.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UExpandableArea/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/ExpandableArea.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/ExpandableArea.h |  |

#### Overridden from [INamedSlotInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/INamedSlotInterface)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) * GetContentForSlot ( [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) SlotName ) const | Gets the widget for a given slot by name, will return nullptr if no widget is in the slot. | Components/ExpandableArea.h |  |
| virtual void GetSlotNames ( [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)>& SlotNames ) const | Gets the names for slots that we can store widgets into. | Components/ExpandableArea.h |  |
| virtual void SetContentForSlot ( [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) SlotName, [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Content ) | Sets the widget for a given slot by name. | Components/ExpandableArea.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void SlateExpansionChanged ( bool NewState ) |  | Components/ExpandableArea.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/ExpandableArea.h |  |

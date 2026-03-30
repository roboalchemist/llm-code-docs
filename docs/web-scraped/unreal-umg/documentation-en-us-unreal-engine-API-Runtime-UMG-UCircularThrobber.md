# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCircularThrobber

Title: UCircularThrobber | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCircularThrobber

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

A throbber widget that orients images in a spinning circle.

* No Children
* Spinner Progress

|  |  |
| --- | --- |
| _Name_ | UCircularThrobber |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/CircularThrobber.h |
| _Include Path_ | #include "Components/CircularThrobber.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UCircularThrobber : public UWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → **UCircularThrobber**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UEditorUtilityCircularThrobber](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Editor/Blutility/UEditorUtilityCircularThrobber)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UCircularThrobber ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/CircularThrobber.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| Image | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) | The throbber image. | Components/CircularThrobber.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category=Appearance |
| NumberOfPieces | int32 | How many pieces there are | Components/CircularThrobber.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetNumberOfPieces"* Category=Appearance * Meta=(ClampMin="1", ClampMax="25", UIMin="1", UIMax="25") |
| Period | float | The amount of time for a full circle (in seconds) | Components/CircularThrobber.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetPeriod"* Category=Appearance * Meta=(ClampMin="0", UIMin="0") |
| Radius | float | The radius of the circle. | Components/CircularThrobber.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetRadius"* Category=Appearance * Meta=(EditCondition="bEnableRadius") |

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bEnableRadius | bool |  | Components/CircularThrobber.h | *Transient* EditAnywhere *Category="Appearance"* Meta=(InlineEditConditionToggle) |
| MyCircularThrobber | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SCircularThrobber](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SCircularThrobber)> | The CircularThrobber widget managed by this object. | Components/CircularThrobber.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& GetImage() |  | Components/CircularThrobber.h |  |
| int32 GetNumberOfPieces() |  | Components/CircularThrobber.h | *BlueprintCallable* Category="Appearance" |
| float GetPeriod() |  | Components/CircularThrobber.h | *BlueprintCallable* Category="Appearance" |
| float GetRadius() |  | Components/CircularThrobber.h | *BlueprintCallable* Category="Appearance" |
| void SetImage ( const [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush)& InRadius ) | Sets the throbber image. | Components/CircularThrobber.h |  |
| void SetNumberOfPieces ( int32 InNumberOfPieces ) | Sets how many pieces there are. | Components/CircularThrobber.h | *BlueprintCallable* Category="Appearance" |
| void SetPeriod ( float InPeriod ) | Sets the amount of time for a full circle (in seconds). | Components/CircularThrobber.h | *BlueprintCallable* Category="Appearance" |
| void SetRadius ( float InRadius ) | Sets the radius of the circle. | Components/CircularThrobber.h | *BlueprintCallable* Category="Appearance" |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/CircularThrobber.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCircularThrobber/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/CircularThrobber.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/CircularThrobber.h |  |

### Protected

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/CircularThrobber.h |  |

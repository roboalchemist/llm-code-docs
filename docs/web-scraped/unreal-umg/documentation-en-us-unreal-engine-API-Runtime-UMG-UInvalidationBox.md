# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UInvalidationBox

Title: UInvalidationBox | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UInvalidationBox

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

Invalidate

* Single Child
* Caching / Performance

|  |  |
| --- | --- |
| _Name_ | UInvalidationBox |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/InvalidationBox.h |
| _Include Path_ | #include "Components/InvalidationBox.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UInvalidationBox : public UContentWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → [UContentWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget) → **UInvalidationBox**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UInvalidationBox ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/InvalidationBox.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| bool GetCanCache() |  | Components/InvalidationBox.h | *BlueprintCallable* Category="Invalidation Box" |
| void InvalidateCache() |  | Components/InvalidationBox.h | *BlueprintCallable* Category="Invalidation Box" * Meta=(DeprecatedFunction) |
| void [SetCanCache](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UInvalidationBox/SetCanCache) ( bool CanCache ) | Tell the InvalidationBox to use the invalidation process. | Components/InvalidationBox.h | *BlueprintCallable* Category="Invalidation Box" |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/InvalidationBox.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/InvalidationBox.h |  |

### Protected

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void OnSlotAdded ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/InvalidationBox.h |  |
| virtual void OnSlotRemoved ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/InvalidationBox.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/InvalidationBox.h |  |

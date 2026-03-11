# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget

Title: UContentWidget | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | UContentWidget |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/ContentWidget.h |
| _Include Path_ | #include "Components/ContentWidget.h" |

Syntax
------

```
UCLASS (Abstract, MinimalAPI)  
class UContentWidget : public UPanelWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → **UContentWidget**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

UContentWidget derived class hierarchy

* [UBackgroundBlur](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBackgroundBlur)
* [UBorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UBorder)
* [UButton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButton)
* [UCheckBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCheckBox)
* [UCommonLoadGuard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/UCommonLoadGuard)
* [UInvalidationBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UInvalidationBox)
* [UMenuAnchor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UMenuAnchor)
* [UNamedSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UNamedSlot)
* [URetainerBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/URetainerBox)
* [USafeZone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/USafeZone)
* [UScaleBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UScaleBox)
* [USizeBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/USizeBox)
* [UViewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UViewport)
* [UWindowTitleBarArea](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWindowTitleBarArea)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UContentWidget ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/ContentWidget.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) * GetContent() |  | Components/ContentWidget.h | *BlueprintCallable* Category="Widget|Panel" |
| [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot) * GetContentSlot() |  | Components/ContentWidget.h | *BlueprintCallable* Category="Widget|Panel" |
| [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot) *SetContent ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Content ) |  | Components/ContentWidget.h | *BlueprintCallable* Category="Widget|Panel" |

### Protected

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [UClass](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UClass) * GetSlotClass() | [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget). | Components/ContentWidget.h |  |

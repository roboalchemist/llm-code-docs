# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SWorldWidgetScreenLayer

Title: SWorldWidgetScreenLayer | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SWorldWidgetScreenLayer

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | SWorldWidgetScreenLayer |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Slate/SWorldWidgetScreenLayer.h |
| _Include Path_ | #include "Slate/SWorldWidgetScreenLayer.h" |

Syntax
------

```
class SWorldWidgetScreenLayer : public SCompoundWidget
```

Inheritance Hierarchy
---------------------

* [FSharedFromThisBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FSharedFromThisBase) → [TSharedFromThis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedFromThis) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) → **SWorldWidgetScreenLayer**
* [FSlateControlledConstruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateControlledConstruction) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) → **SWorldWidgetScreenLayer**

Classes
-------

| Name | Remarks |
| --- | --- |
| [FComponentEntry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SWorldWidgetScreenLayer/FComponentEntry) |  |

Structs
-------

| Name | Remarks |
| --- | --- |
| [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SWorldWidgetScreenLayer/FArguments) |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| Canvas | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SConstraintCanvas](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SConstraintCanvas)> |  | Slate/SWorldWidgetScreenLayer.h |  |
| ComponentMap | [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TMap)<[FObjectKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectKey), FComponentEntry > |  | Slate/SWorldWidgetScreenLayer.h |  |
| DrawSize | FVector2D |  | Slate/SWorldWidgetScreenLayer.h |  |
| Pivot | FVector2D |  | Slate/SWorldWidgetScreenLayer.h |  |
| PlayerContext | [FLocalPlayerContext](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FLocalPlayerContext) |  | Slate/SWorldWidgetScreenLayer.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void AddComponent ( [USceneComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USceneComponent)* Component, [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> Widget ) |  | Slate/SWorldWidgetScreenLayer.h |  |
| void Construct ( const [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SWorldWidgetScreenLayer/FArguments)& InArgs, const [FLocalPlayerContext](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FLocalPlayerContext)& InPlayerContext ) |  | Slate/SWorldWidgetScreenLayer.h |  |
| void RemoveComponent ( [USceneComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USceneComponent)* Component ) |  | Slate/SWorldWidgetScreenLayer.h |  |
| void SetWidgetDrawSize ( FVector2D DrawSize ) |  | Slate/SWorldWidgetScreenLayer.h |  |
| void SetWidgetPivot ( FVector2D Pivot ) |  | Slate/SWorldWidgetScreenLayer.h |  |

#### Overridden from [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual FVector2D ComputeDesiredSize ( float ) const |  | Slate/SWorldWidgetScreenLayer.h |  |
| virtual void Tick ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& AllottedGeometry, const double InCurrentTime, const float InDeltaTime ) |  | Slate/SWorldWidgetScreenLayer.h |  |

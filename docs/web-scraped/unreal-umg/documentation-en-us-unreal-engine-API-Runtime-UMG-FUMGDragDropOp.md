# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGDragDropOp

Title: FUMGDragDropOp | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGDragDropOp

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

This is the drag/drop class used for UMG, all UMG drag drop operations utilize this operation. It supports moving a [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) payload and using a [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) decorator.

|  |  |
| --- | --- |
| _Name_ | FUMGDragDropOp |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Slate/UMGDragDropOp.h |
| _Include Path_ | #include "Slate/UMGDragDropOp.h" |

Syntax
------

```
class FUMGDragDropOp :  
    public FGameDragDropOperation ,  
    public FGCObject
```

Inheritance Hierarchy
---------------------

* [FSharedFromThisBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FSharedFromThisBase) → [TSharedFromThis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedFromThis) → [FDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropOperation) → [FGameDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGameDragDropOperation) → **FUMGDragDropOp**
* [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject) → **FUMGDragDropOp**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| FUMGDragDropOp() |  | Slate/UMGDragDropOp.h |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| DecoratorWidget | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> | The widget used during the drag/drop action to show something being dragged. | Slate/UMGDragDropOp.h |  |
| DragOperation | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation)> | Raw pointer to the drag operation, kept alive by AddReferencedObjects. | Slate/UMGDragDropOp.h |  |
| GameViewport | [TWeakObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TWeakObjectPtr)<[UGameViewportClient](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UGameViewportClient)> | The viewport this drag/drop operation is associated with. | Slate/UMGDragDropOp.h |  |
| MouseDownOffset | FVector2D | The offset to use when dragging the object so that it says the same distance away from the mouse. | Slate/UMGDragDropOp.h |  |
| PointerIndex | int32 |  | Slate/UMGDragDropOp.h |  |
| SourceUserWidget | [TWeakPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TWeakPtr)<[SObjectWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectWidget)> | Source User Widget | Slate/UMGDragDropOp.h |  |
| StartingScreenPos | FVector2D | The starting screen location where the drag operation started. | Slate/UMGDragDropOp.h |  |
| StartTime | double | Allows smooth interpolation of the dragged visual over a few frames. | Slate/UMGDragDropOp.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [UDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation) * GetOperation() |  | Slate/UMGDragDropOp.h |  |

#### Overridden from [FDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropOperation)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual bool AffectedByPointerEvent ( const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& PointerEvent ) |  | Slate/UMGDragDropOp.h |  |
| virtual [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> GetDefaultDecorator() |  | Slate/UMGDragDropOp.h |  |
| virtual bool IsOfTypeImpl ( const [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)& Type ) const |  | Slate/UMGDragDropOp.h |  |
| virtual [FCursorReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FCursorReply) OnCursorQuery() |  | Slate/UMGDragDropOp.h |  |
| virtual void OnDragged ( const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Slate/UMGDragDropOp.h |  |
| virtual void OnDrop ( bool bDropWasHandled, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Slate/UMGDragDropOp.h |  |

#### Overridden from [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void AddReferencedObjects ( [FReferenceCollector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FReferenceCollector)& Collector ) | Begin [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject). | Slate/UMGDragDropOp.h |  |
| virtual [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) GetReferencerName() |  | Slate/UMGDragDropOp.h |  |

### Protected

#### Overridden from [FDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropOperation)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void Construct() |  | Slate/UMGDragDropOp.h |  |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static const [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)& GetTypeId() |  | Slate/UMGDragDropOp.h |  |
| static [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[FUMGDragDropOp](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGDragDropOp)> New ( [UDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation)* Operation, const int32 PointerIndex, const FVector2D& CursorPosition, const FVector2D& ScreenPositionOfNode, float DPIScale, [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SObjectWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectWidget)> SourceUserWidget ) |  | Slate/UMGDragDropOp.h |  |

# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation

Title: UDragDropOperation | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

This class is the base drag drop operation for UMG, extend it to add additional data and add new functionality.

|  |  |
| --- | --- |
| _Name_ | UDragDropOperation |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Blueprint/DragDropOperation.h |
| _Include Path_ | #include "Blueprint/DragDropOperation.h" |

Syntax
------

```
UCLASS (BlueprintType, Blueprintable, Meta=(DontUseGenericSpawnObject="True"), MinimalAPI)  
class UDragDropOperation : public UObject
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → **UDragDropOperation**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UDragDropOperation ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Blueprint/DragDropOperation.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| DefaultDragVisual | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)< class [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)> | The Drag Visual is the widget to display when dragging the item. | Blueprint/DragDropOperation.h | *EditAnywhere* BlueprintReadOnly *Category="Drag and Drop"* Meta=(ExposeOnSpawn="true", DisplayName="Drag Visual") |
| Offset | FVector2D | A percentage offset (-1..+1) from the Pivot location, the percentage is of the desired size of the dragged visual. | Blueprint/DragDropOperation.h | *EditAnywhere* BlueprintReadWrite *Category="Drag and Drop"* AdvancedDisplay * Meta=(ExposeOnSpawn="true") |
| OnDragCancelled | [FOnDragDropMulticast](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnDragDropMulticast) |  | Blueprint/DragDropOperation.h | * BlueprintAssignable |
| OnDragged | [FOnDragDropMulticast](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnDragDropMulticast) |  | Blueprint/DragDropOperation.h | * BlueprintAssignable |
| OnDrop | [FOnDragDropMulticast](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnDragDropMulticast) |  | Blueprint/DragDropOperation.h | * BlueprintAssignable |
| Payload | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)> | The payload of the drag operation. | Blueprint/DragDropOperation.h | *EditAnywhere* BlueprintReadWrite *Category="Drag and Drop"* Meta=(ExposeOnSpawn="true") |
| Pivot | [EDragPivot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/EDragPivot) | Controls where the drag widget visual will appear when dragged relative to the pointer performing the drag operation. | Blueprint/DragDropOperation.h | *EditAnywhere* BlueprintReadWrite *Category="Drag and Drop"* Meta=(ExposeOnSpawn="true") |
| Tag | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | A simple string tag you can optionally use to provide extra metadata about the operation. | Blueprint/DragDropOperation.h | *EditAnywhere* BlueprintReadWrite *Category="Drag and Drop"* Meta=(ExposeOnSpawn="true") |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void DragCancelled ( const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& PointerEvent ) |  | Blueprint/DragDropOperation.h | *BlueprintNativeEvent* Category="Drag and Drop" |
| void Dragged ( const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& PointerEvent ) |  | Blueprint/DragDropOperation.h | *BlueprintNativeEvent* Category="Drag and Drop" |
| void Drop ( const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& PointerEvent ) |  | Blueprint/DragDropOperation.h | *BlueprintNativeEvent* Category="Drag and Drop" |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static [EUMGItemDropZone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/EUMGItemDropZone) ConvertSlateDropZoneToUMG ( [TOptional](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TOptional)<[EItemDropZone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/EItemDropZone)> DropZone ) |  | Blueprint/DragDropOperation.h |  |

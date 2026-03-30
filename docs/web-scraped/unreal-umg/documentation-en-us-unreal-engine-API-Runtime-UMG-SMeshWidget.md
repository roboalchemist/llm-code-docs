# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget

Title: SMeshWidget | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

A widget that draws vertexes provided by a 2.5D StaticMesh. The Mesh's material is used. Hardware instancing is supported.

|  |  |
| --- | --- |
| _Name_ | SMeshWidget |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Slate/SMeshWidget.h |
| _Include Path_ | #include "Slate/SMeshWidget.h" |

Syntax
------

```
class SMeshWidget :  
    public SLeafWidget ,  
    public FGCObject
```

Inheritance Hierarchy
---------------------

* [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject) → **SMeshWidget**
* [FSharedFromThisBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FSharedFromThisBase) → [TSharedFromThis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedFromThis) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SLeafWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SLeafWidget) → **SMeshWidget**
* [FSlateControlledConstruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateControlledConstruction) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SLeafWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SLeafWidget) → **SMeshWidget**

Classes
-------

| Name | Remarks |
| --- | --- |
| [FRenderRun](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/FRenderRun) | Which mesh to draw, starting with which instance offset and how many instances to draw in this run/batch. |

Structs
-------

| Name | Remarks |
| --- | --- |
| [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/FArguments) |  |
| [FRenderData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/FRenderData) |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| RenderRuns | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)< FRenderRun > |  | Slate/SMeshWidget.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| uint32 [AddMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/AddMesh) ( [USlateVectorArtData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/USlateVectorArtData)& InMeshData ) | Draw the InStaticMesh when this widget paints. | Slate/SMeshWidget.h |  |
| uint32 AddMeshWithInstancing ( [USlateVectorArtData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/USlateVectorArtData)& InMeshData, int32 InitialBufferSize ) | Much like AddMesh, but also enables instancing support for this MeshId. | Slate/SMeshWidget.h |  |
| void [AddRenderRun](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/AddRenderRun) ( uint32 InMeshIndex, uint32 InInstanceOffset, uint32 InNumInstances ) | Tell the widget to draw instances of a mesh a given number of times starting at a given offset. | Slate/SMeshWidget.h |  |
| void ClearRuns ( int32 NumRuns ) | Discard any previous runs and reserve space for new render runs if needed. | Slate/SMeshWidget.h |  |
| void Construct ( const [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/FArguments)& Args ) |  | Slate/SMeshWidget.h |  |
| [UMaterialInstanceDynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInstanceDynamic) * ConvertToMID ( uint32 MeshId ) | Switch from static material to material instance dynamic. | Slate/SMeshWidget.h |  |
| void EnableInstancing ( uint32 MeshId, int32 InitialSize ) | Enable hardware instancing | Slate/SMeshWidget.h |  |
| void UpdatePerInstanceBuffer ( uint32 MeshId, FSlateInstanceBufferData& Data ) | Updates the per instance buffer. Automatically enables hardware instancing. | Slate/SMeshWidget.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual int32 OnPaint ( const [FPaintArgs](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPaintArgs)& Args, const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& AllottedGeometry, const [FSlateRect](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateRect)& MyCullingRect, [FSlateWindowElementList](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateWindowElementList)& OutDrawElements, int32 LayerId, const [FWidgetStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FWidgetStyle)& InWidgetStyle, bool bParentEnabled ) const |  | Slate/SMeshWidget.h |  |

#### Overridden from [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual FVector2D ComputeDesiredSize ( float ) const |  | Slate/SMeshWidget.h |  |

#### Overridden from [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void AddReferencedObjects ( [FReferenceCollector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FReferenceCollector)& Collector ) | ~ [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject) | Slate/SMeshWidget.h |  |
| virtual [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) GetReferencerName() |  | Slate/SMeshWidget.h |  |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static void [PushUpdate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/PushUpdate) ( uint32 VectorArtId, [SMeshWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget)& Widget, const FVector2D& Position, float Scale, uint32 BaseAddress ) |  | Slate/SMeshWidget.h |  |
| static void [PushUpdate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget/PushUpdate) ( uint32 VectorArtId, [SMeshWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SMeshWidget)& Widget, const FVector2D& Position, float Scale, float OptionalFloat ) |  | Slate/SMeshWidget.h |  |

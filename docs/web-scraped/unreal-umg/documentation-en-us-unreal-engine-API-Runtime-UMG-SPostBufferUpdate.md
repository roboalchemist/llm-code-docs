# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate

Title: SPostBufferUpdate | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

Implements a widget that triggers a post buffer update on draw

|  |  |
| --- | --- |
| _Name_ | SPostBufferUpdate |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Slate/SPostBufferUpdate.h |
| _Include Path_ | #include "Slate/SPostBufferUpdate.h" |

Syntax
------

```
class SPostBufferUpdate : public SLeafWidget
```

Inheritance Hierarchy
---------------------

* [FSharedFromThisBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FSharedFromThisBase) → [TSharedFromThis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedFromThis) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SLeafWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SLeafWidget) → **SPostBufferUpdate**
* [FSlateControlledConstruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateControlledConstruction) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SLeafWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SLeafWidget) → **SPostBufferUpdate**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| SPostBufferUpdate() | Constructor | Slate/SPostBufferUpdate.h |  |

Structs
-------

| Name | Remarks |
| --- | --- |
| [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate/FArguments) |  |

Typedefs
--------

| Name | Type | Remarks | Include Path |
| --- | --- | --- | --- |
| PrivateParentType | [SLeafWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SLeafWidget) |  | Slate/SPostBufferUpdate.h |
| PrivateThisType | [SPostBufferUpdate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate) |  | Slate/SPostBufferUpdate.h |
| Super | [SLeafWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SLeafWidget) |  | Slate/SPostBufferUpdate.h |
| ThisClass | [SPostBufferUpdate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate) |  | Slate/SPostBufferUpdate.h |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| BuffersToUpdate | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[ESlatePostRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ESlatePostRT)> | Buffers that we should update, all of these buffers will be affected by 'bPerformDefaultPostBufferUpdate' if disabled | Slate/SPostBufferUpdate.h |  |
| bUsePaintGeometry | bool | True if we should limit processing to our paint geometry | Slate/SPostBufferUpdate.h |  |
| PostBufferUpdater | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)< FPostBufferUpdater > | Custom drawer used to trigger a post buffer update | Slate/SPostBufferUpdate.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void Construct ( const [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate/FArguments)& InArgs ) | Construct this widget | Slate/SPostBufferUpdate.h |  |
| const [TArrayView](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArrayView)< const [ESlatePostRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ESlatePostRT)> GetBuffersToUpdate() | Get buffers to update | Slate/SPostBufferUpdate.h |  |
| virtual int32 OnPaint ( const [FPaintArgs](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPaintArgs)& Args, const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& AllottedGeometry, const [FSlateRect](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateRect)& MyCullingRect, [FSlateWindowElementList](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateWindowElementList)& OutDrawElements, int32 LayerId, const [FWidgetStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FWidgetStyle)& InWidgetStyle, bool bParentEnabled ) const |  | Slate/SPostBufferUpdate.h |  |
| void ReleasePostBufferUpdater() | Release Post Buffer Updater, called out of caution in case of reuse during 'ReleaseSlateResources' in [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) | Slate/SPostBufferUpdate.h |  |
| void [SetBuffersToUpdate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SPostBufferUpdate/SetBuffersToUpdate) ( const [TArrayView](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArrayView)<[ESlatePostRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ESlatePostRT)> InBuffersToUpdate ) | Set buffers to, this method only affects the 'FPostBufferUpdater' custom drawer once during initialization. | Slate/SPostBufferUpdate.h |  |
| void SetProcessorUpdaters ( [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TMap)<[ESlatePostRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ESlatePostRT), [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[FSlatePostProcessorUpdaterProxy](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FSlatePostProcessorUpdaterProxy)>> InProcessorUpdaters ) | Set processsor updaters for the given buffers by index. | Slate/SPostBufferUpdate.h |  |
| void SetUsePaintGeometry ( bool bInUsePaintGeometry ) | Set if we should use paint geometry | Slate/SPostBufferUpdate.h |  |

#### Overridden from [FSlateControlledConstruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateControlledConstruction)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FSlateWidgetClassData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateWidgetClassData)& GetWidgetClass() |  | Slate/SPostBufferUpdate.h |  |

### Protected

#### Overridden from [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual FVector2D ComputeDesiredSize ( float LayoutScaleMultiplier ) const |  | Slate/SPostBufferUpdate.h |  |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static const [FSlateWidgetClassData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateWidgetClassData)& GetPrivateWidgetClass() |  | Slate/SPostBufferUpdate.h |  |
| static UMG_API void PrivateRegisterAttributes ( FSlateAttributeInitializer& ) |  | Slate/SPostBufferUpdate.h |  |
| static const [FSlateWidgetClassData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateWidgetClassData)& StaticWidgetClass() |  | Slate/SPostBufferUpdate.h |  |

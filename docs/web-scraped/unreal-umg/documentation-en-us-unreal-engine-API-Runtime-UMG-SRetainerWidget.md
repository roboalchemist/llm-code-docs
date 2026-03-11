# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget

Title: SRetainerWidget | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The [SRetainerWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget) renders children widgets to a render target first before later rendering that render target to the screen. This allows both frequency and phase to be controlled so that the UI can actually render less often than the frequency of the main game render. It also has the side benefit of allow materials to be applied to the render target after drawing the widgets to apply a simple post process.

|  |  |
| --- | --- |
| _Name_ | SRetainerWidget |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Slate/SRetainerWidget.h |
| _Include Path_ | #include "Slate/SRetainerWidget.h" |

Syntax
------

```
class SRetainerWidget :  
    public SCompoundWidget ,  
    public FSlateInvalidationRoot
```

Inheritance Hierarchy
---------------------

* [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject) → [FSlateInvalidationRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateInvalidationRoot) → **SRetainerWidget**
* [FNoncopyable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FNoncopyable) → [FSlateInvalidationRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateInvalidationRoot) → **SRetainerWidget**
* [FSharedFromThisBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FSharedFromThisBase) → [TSharedFromThis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedFromThis) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) → **SRetainerWidget**
* [FSlateControlledConstruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateControlledConstruction) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) → **SRetainerWidget**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| SRetainerWidget() |  | Slate/SRetainerWidget.h |  |

Destructors
-----------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| ~SRetainerWidget() |  | Slate/SRetainerWidget.h |  |

Structs
-------

| Name | Remarks |
| --- | --- |
| [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget/FArguments) |  |

Enums
-----

### Protected

| Name | Remarks |
| --- | --- |
| [EPaintRetainedContentResult](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget/EPaintRetainedContentResult) |  |

Constants
---------

| Name | Type | Remarks | Include Path |
| --- | --- | --- | --- |
| OnRetainerModeChangedDelegate | FOnRetainedModeChanged |  | Slate/SRetainerWidget.h |
| Shared_MaxRetainerWorkPerFrame | int32 |  | Slate/SRetainerWidget.h |
| Shared_RetainerWorkThisFrame | [TFrameValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TFrameValue)< int32 > |  | Slate/SRetainerWidget.h |
| Shared_WaitingToRender | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[SRetainerWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget) *, TInlineAllocator< 3 >> |  | Slate/SRetainerWidget.h |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bEnableRetainedRendering | bool |  | Slate/SRetainerWidget.h |  |
| bEnableRetainedRenderingDesire | bool |  | Slate/SRetainerWidget.h |  |
| bInvalidSizeLogged | bool |  | Slate/SRetainerWidget.h |  |
| bIsDesignTime | bool | True if widget is used in design time | Slate/SRetainerWidget.h |  |
| bRenderRequested | bool |  | Slate/SRetainerWidget.h |  |
| bShowEffectsInDesigner | bool | True if we should retain rendering in designer | Slate/SRetainerWidget.h |  |
| bWarnOnInvalidSize | bool | True if we should warn when the requested size for the retainer is 0 or too large | Slate/SRetainerWidget.h |  |
| DynamicBrush | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) |  | Slate/SRetainerWidget.h |  |
| DynamicEffectTextureParameter | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) |  | Slate/SRetainerWidget.h |  |
| HittestGrid | [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[FHittestGrid](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FHittestGrid)> |  | Slate/SRetainerWidget.h |  |
| LastDrawTime | double |  | Slate/SRetainerWidget.h |  |
| LastIncomingLayerId | int32 |  | Slate/SRetainerWidget.h |  |
| LastTickedFrame | int64 |  | Slate/SRetainerWidget.h |  |
| MyWidget | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> |  | Slate/SRetainerWidget.h |  |
| OuterWorld | [TWeakObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TWeakObjectPtr)<[UWorld](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UWorld)> |  | Slate/SRetainerWidget.h |  |
| Phase | int32 |  | Slate/SRetainerWidget.h |  |
| PhaseCount | int32 |  | Slate/SRetainerWidget.h |  |
| PreviousAllottedGeometry | [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry) |  | Slate/SRetainerWidget.h |  |
| PreviousClippingState | [TOptional](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TOptional)<[FSlateClippingState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateClippingState)> |  | Slate/SRetainerWidget.h |  |
| PreviousClipRectSize | FIntPoint |  | Slate/SRetainerWidget.h |  |
| PreviousColorAndOpacity | [FColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FColor) |  | Slate/SRetainerWidget.h |  |
| PreviousRenderSize | FIntPoint |  | Slate/SRetainerWidget.h |  |
| RenderingResources | FRetainerWidgetRenderingResources * |  | Slate/SRetainerWidget.h |  |
| RenderOnInvalidation | bool |  | Slate/SRetainerWidget.h |  |
| RenderOnPhase | bool |  | Slate/SRetainerWidget.h |  |
| SurfaceBrush | [FSlateBrush](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateBrush) |  | Slate/SRetainerWidget.h |  |
| VirtualWindow | [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SVirtualWindow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SVirtualWindow)> |  | Slate/SRetainerWidget.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void Construct ( const [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget/FArguments)& Args ) | Constructor | Slate/SRetainerWidget.h |  |
| [UMaterialInstanceDynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInstanceDynamic) * GetEffectMaterial() |  | Slate/SRetainerWidget.h |  |
| void RequestRender() | Requests that the retainer redraw the hosted content next time it's painted. | Slate/SRetainerWidget.h |  |
| void SetContent ( const [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)>& InContent ) |  | Slate/SRetainerWidget.h |  |
| void SetEffectMaterial ( [UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)* EffectMaterial ) |  | Slate/SRetainerWidget.h |  |
| void SetIsDesignTime ( bool bInIsDesignTime ) |  | Slate/SRetainerWidget.h |  |
| void SetRenderingPhase ( int32 Phase, int32 PhaseCount ) |  | Slate/SRetainerWidget.h |  |
| void SetRetainedRendering ( bool bRetainRendering ) |  | Slate/SRetainerWidget.h |  |
| void SetShowEffectsInDesigner ( bool bInShowEffectsInDesigner ) |  | Slate/SRetainerWidget.h |  |
| void SetTextureParameter ( [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) TextureParameter ) |  | Slate/SRetainerWidget.h |  |
| void SetWorld ( [UWorld](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UWorld)* World ) |  | Slate/SRetainerWidget.h |  |

#### Overridden from [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [FChildren](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FChildren) * Debug_GetChildrenForReflector() |  | Slate/SRetainerWidget.h |  |
| virtual [FChildren](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FChildren) * GetChildren() |  | Slate/SRetainerWidget.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| bool IsAnythingVisibleToRender() |  | Slate/SRetainerWidget.h |  |
| void OnRetainerModeChanged() |  | Slate/SRetainerWidget.h |  |
| [EPaintRetainedContentResult](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SRetainerWidget/EPaintRetainedContentResult) PaintRetainedContentImpl ( const [FSlateInvalidationContext](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateInvalidationContext)& Context, const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& AllottedGeometry, int32 LayerId ) |  | Slate/SRetainerWidget.h |  |
| void RefreshRenderingMode() |  | Slate/SRetainerWidget.h |  |
| bool ShouldBeRenderingOffscreen() |  | Slate/SRetainerWidget.h |  |

#### Overridden from [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FSlateInvalidationRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateInvalidationRoot) * Advanced_AsInvalidationRoot() |  | Slate/SRetainerWidget.h |  |
| virtual bool Advanced_IsInvalidationRoot() |  | Slate/SRetainerWidget.h |  |
| virtual FVector2D ComputeDesiredSize ( float Scale ) const |  | Slate/SRetainerWidget.h |  |
| virtual bool CustomPrepass ( float LayoutScaleMultiplier ) |  | Slate/SRetainerWidget.h |  |
| virtual int32 OnPaint ( const [FPaintArgs](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPaintArgs)& Args, const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& AllottedGeometry, const [FSlateRect](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateRect)& MyCullingRect, [FSlateWindowElementList](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateWindowElementList)& OutDrawElements, int32 LayerId, const [FWidgetStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FWidgetStyle)& InWidgetStyle, bool bParentEnabled ) const | [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) interface | Slate/SRetainerWidget.h |  |

#### Overridden from [FSlateInvalidationRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateInvalidationRoot)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> GetRootWidget() |  | Slate/SRetainerWidget.h |  |
| virtual void OnRootInvalidated() |  | Slate/SRetainerWidget.h |  |
| virtual int32 PaintSlowPath ( const [FSlateInvalidationContext](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateInvalidationContext)& Context ) |  | Slate/SRetainerWidget.h |  |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static void OnRetainerModeCVarChanged ( [IConsoleVariable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/IConsoleVariable)* CVar ) |  | Slate/SRetainerWidget.h |  |

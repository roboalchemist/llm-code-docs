# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGViewportClient

Title: FUMGViewportClient | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGViewportClient

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | FUMGViewportClient |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/Viewport.h |
| _Include Path_ | #include "Components/Viewport.h" |

Syntax
------

```
class FUMGViewportClient :  
    public FCommonViewportClient ,  
    public FViewElementDrawer
```

Inheritance Hierarchy
---------------------

* [FViewportClient](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FViewportClient) → [FCommonViewportClient](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FCommonViewportClient) → **FUMGViewportClient**
* [FViewElementDrawer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FViewElementDrawer) → **FUMGViewportClient**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| FUMGViewportClient ( [FPreviewScene](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FPreviewScene)* InPreviewScene ) |  | Components/Viewport.h |  |

Destructors
-----------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual ~FUMGViewportClient() |  | Components/Viewport.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [FSceneView](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FSceneView) *CalcSceneView ( [FSceneViewFamily](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FSceneViewFamily)* ViewFamily ) |  | Components/Viewport.h |  |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) GetBackgroundColor() |  | Components/Viewport.h |  |
| const FVector & GetLookAtLocation() |  | Components/Viewport.h |  |
| float GetOrthoUnitsPerPixel ( const [FViewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FViewport)* Viewport ) const |  | Components/Viewport.h |  |
| float GetOrthoZoom() |  | Components/Viewport.h |  |
| virtual [FSceneInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FSceneInterface) * GetScene() |  | Components/Viewport.h |  |
| const FVector & GetViewLocation() |  | Components/Viewport.h |  |
| FMatrix GetViewProjectionMatrix() |  | Components/Viewport.h |  |
| const FRotator & GetViewRotation() |  | Components/Viewport.h |  |
| bool IsAspectRatioConstrained() |  | Components/Viewport.h |  |
| void SetBackgroundColor ( [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) InBackgroundColor ) |  | Components/Viewport.h |  |
| void SetEngineShowFlags ( [FEngineShowFlags](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FEngineShowFlags) InEngineShowFlags ) |  | Components/Viewport.h |  |
| void SetLookAtLocation ( const FVector& LookAt, bool bRecalculateView ) | Sets the look at location of the viewports camera for orbit * | Components/Viewport.h |  |
| void SetOrthoZoom ( float InOrthoZoom ) | Sets ortho zoom amount | Components/Viewport.h |  |
| void SetViewLocation ( const FVector& NewLocation ) | Sets the location of the viewport's camera | Components/Viewport.h |  |
| void SetViewRotation ( const FRotator& NewRotation ) | Sets the location of the viewport's camera | Components/Viewport.h |  |
| virtual void Tick ( float InDeltaTime ) |  | Components/Viewport.h |  |

#### Overridden from [FViewportClient](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FViewportClient)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void [Draw](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGViewportClient/Draw) ( [FViewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FViewport)*InViewport, [FCanvas](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FCanvas)* Canvas ) |  | Components/Viewport.h |  |
| virtual [UWorld](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UWorld) * GetWorld() |  | Components/Viewport.h |  |

#### Overridden from [FViewElementDrawer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FViewElementDrawer)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void [Draw](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUMGViewportClient/Draw) ( const [FSceneView](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FSceneView)*View, [FPrimitiveDrawInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FPrimitiveDrawInterface)* PDI ) |  | Components/Viewport.h |  |

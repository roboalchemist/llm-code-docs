# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UColorBinding

Title: UColorBinding | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UColorBinding

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | UColorBinding |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Binding/ColorBinding.h |
| _Include Path_ | #include "Binding/ColorBinding.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UColorBinding : public UPropertyBinding
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UPropertyBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPropertyBinding) → **UColorBinding**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UColorBinding() |  | Binding/ColorBinding.h |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bNeedsConversion | [TOptional](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TOptional)< bool > |  | Binding/ColorBinding.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) GetLinearValue() |  | Binding/ColorBinding.h |  |
| [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) GetSlateValue() |  | Binding/ColorBinding.h |  |

#### Overridden from [UPropertyBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPropertyBinding)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void Bind ( [FProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FProperty)*Property, FScriptDelegate* Delegate ) |  | Binding/ColorBinding.h |  |
| virtual bool IsSupportedDestination ( [FProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FProperty)* Property ) const |  | Binding/ColorBinding.h |  |
| virtual bool IsSupportedSource ( [FProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FProperty)* Property ) const |  | Binding/ColorBinding.h |  |

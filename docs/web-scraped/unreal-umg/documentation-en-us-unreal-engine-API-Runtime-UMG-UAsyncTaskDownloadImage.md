# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UAsyncTaskDownloadImage

Title: UAsyncTaskDownloadImage | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UAsyncTaskDownloadImage

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | UAsyncTaskDownloadImage |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Blueprint/AsyncTaskDownloadImage.h |
| _Include Path_ | #include "Blueprint/AsyncTaskDownloadImage.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UAsyncTaskDownloadImage : public UBlueprintAsyncActionBase
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UBlueprintAsyncActionBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UBlueprintAsyncActionBase) → **UAsyncTaskDownloadImage**

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UAsyncTaskDownloadImage ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Blueprint/AsyncTaskDownloadImage.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| OnFail | [FDownloadImageDelegate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FDownloadImageDelegate) |  | Blueprint/AsyncTaskDownloadImage.h | * BlueprintAssignable |
| OnSuccess | [FDownloadImageDelegate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FDownloadImageDelegate) |  | Blueprint/AsyncTaskDownloadImage.h | * BlueprintAssignable |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void Start ( [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) URL ) |  | Blueprint/AsyncTaskDownloadImage.h |  |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static [UAsyncTaskDownloadImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UAsyncTaskDownloadImage) * DownloadImage ( [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) URL ) |  | Blueprint/AsyncTaskDownloadImage.h | *BlueprintCallable* Meta=(BlueprintInternalUseOnly="true") |

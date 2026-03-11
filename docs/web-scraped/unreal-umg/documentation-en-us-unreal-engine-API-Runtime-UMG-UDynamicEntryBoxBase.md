# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBoxBase

Title: UDynamicEntryBoxBase | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBoxBase

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

Base for widgets that support a dynamic number of auto-generated entries at both design- and run-time. Contains all functionality needed to create, construct, and cache an arbitrary number of entry widgets, but exposes no means of entry creation or removal It's up to child classes to decide how they want to perform the population (some may do so entirely on their own without exposing a thing)

|  |  |
| --- | --- |
| _Name_ | UDynamicEntryBoxBase |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/DynamicEntryBoxBase.h |
| _Include Path_ | #include "Components/DynamicEntryBoxBase.h" |

Syntax
------

```
UCLASS (Abstract, MinimalAPI)  
class UDynamicEntryBoxBase : public UWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → **UDynamicEntryBoxBase**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UCommonBoundActionBar](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/UCommonBoundActionBar)
* [UDynamicEntryBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBox)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UDynamicEntryBoxBase ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& Initializer ) |  | Components/DynamicEntryBoxBase.h |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| EntryWidgetPool | [FUserWidgetPool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FUserWidgetPool) |  | Components/DynamicEntryBoxBase.h | * Transient |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| const [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget) * >& GetAllEntries() |  | Components/DynamicEntryBoxBase.h | *BlueprintCallable* Category=DynamicEntryBox |
| [EDynamicBoxType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/EDynamicBoxType) GetBoxType() |  | Components/DynamicEntryBoxBase.h |  |
| [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) GetEntryHorizontalAlignment() |  | Components/DynamicEntryBoxBase.h |  |
| const [FSlateChildSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FSlateChildSize)& GetEntrySizeRule() |  | Components/DynamicEntryBoxBase.h |  |
| const FVector2D & GetEntrySpacing() |  | Components/DynamicEntryBoxBase.h |  |
| [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) GetEntryVerticalAlignment() |  | Components/DynamicEntryBoxBase.h |  |
| int32 GetMaxElementSize() |  | Components/DynamicEntryBoxBase.h |  |
| int32 GetNumEntries() |  | Components/DynamicEntryBoxBase.h | *BlueprintCallable* Category=DynamicEntryBox |
| const [FRadialBoxSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FRadialBoxSettings)& GetRadialBoxSettings() |  | Components/DynamicEntryBoxBase.h |  |
| [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)< EntryWidgetT * > GetTypedEntries() |  | Components/DynamicEntryBoxBase.h |  |
| void SetEntrySpacing ( const FVector2D& InEntrySpacing ) |  | Components/DynamicEntryBoxBase.h | *BlueprintCallable* Category=DynamicEntryBox |
| void SetRadialSettings ( const [FRadialBoxSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FRadialBoxSettings)& InSettings ) |  | Components/DynamicEntryBoxBase.h | *BlueprintCallable* Category=DynamicEntryBox |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/DynamicEntryBoxBase.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void AddEntryChild ( [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)& ChildWidget ) |  | Components/DynamicEntryBoxBase.h |  |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) BuildEntryPadding ( const FVector2D& DesiredSpacing ) |  | Components/DynamicEntryBoxBase.h |  |
| [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget) * CreateEntryInternal ( [TSubclassOf](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSubclassOf)<[UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)> InEntryClass ) |  | Components/DynamicEntryBoxBase.h |  |
| void InitEntryBoxType ( [EDynamicBoxType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/EDynamicBoxType) InEntryBoxType ) | Initialize EntryBoxType in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/DynamicEntryBoxBase.h |  |
| void InitEntryHorizontalAlignment ( [EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment) InEntryHorizontalAlignment ) | Initialize EntryHorizontalAlignment in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/DynamicEntryBoxBase.h |  |
| void InitEntrySizeRule ( [FSlateChildSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FSlateChildSize) InEntrySizeRule ) | Initialize EntrySizeRule in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/DynamicEntryBoxBase.h |  |
| void InitEntryVerticalAlignment ( [EVerticalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EVerticalAlignment) InEntryVerticalAlignment ) | Initialize EntryVerticalAlignment in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/DynamicEntryBoxBase.h |  |
| void InitMaxElementSize ( int32 InMaxElementSize ) | Initialize MaxElementSize in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/DynamicEntryBoxBase.h |  |
| bool IsEntryClassValid ( [TSubclassOf](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSubclassOf)<[UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)> InEntryClass ) const |  | Components/DynamicEntryBoxBase.h |  |
| void RemoveEntryInternal ( [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)* EntryWidget, bool bReleaseSlate ) |  | Components/DynamicEntryBoxBase.h |  |
| void [ResetInternal](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBoxBase/ResetInternal) ( bool bDeleteWidgets ) | Clear out the box entries, optionally deleting the underlying Slate widgets entirely as well. | Components/DynamicEntryBoxBase.h |  |
| void [ResetInternal](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBoxBase/ResetInternal) ( [TFunctionRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TFunctionRef)< void(WidgetT&)> ResetEntryFunc, bool bDeleteWidgets ) | Clear out the box entries, executing the provided reset function for each and optionally deleting the underlying Slate widgets entirely as well. | Components/DynamicEntryBoxBase.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/DynamicEntryBoxBase.h |  |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/DynamicEntryBoxBase.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBoxBase/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/DynamicEntryBoxBase.h |  |

#### Overridden from [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void PostEditChangeProperty ( [FPropertyChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FPropertyChangedEvent)& PropertyChangedEvent ) |  | Components/DynamicEntryBoxBase.h |  |

See Also
--------

* [UDynamicEntryBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDynamicEntryBox) for a ready-to-use version

# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem

Title: UGameViewportSubsystem | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | UGameViewportSubsystem |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Blueprint/GameViewportSubsystem.h |
| _Include Path_ | #include "Blueprint/GameViewportSubsystem.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UGameViewportSubsystem : public UEngineSubsystem
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [USubsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USubsystem) → [UDynamicSubsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UDynamicSubsystem) → [UEngineSubsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UEngineSubsystem) → **UGameViewportSubsystem**

Classes
-------

| Name | Remarks |
| --- | --- |
| [FWidgetAddedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/FWidgetAddedEvent) |  |
| [FWidgetRemovedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/FWidgetRemovedEvent) |  |

Structs
-------

| Name | Remarks |
| --- | --- |
| [FSlotInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/FSlotInfo) |  |

Typedefs
--------

| Name | Type | Remarks | Include Path |
| --- | --- | --- | --- |
| FViewportWidgetList | [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TMap)<[TObjectKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TObjectKey)<[UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)>, FSlotInfo > |  | Blueprint/GameViewportSubsystem.h |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| OnWidgetAdded | [FWidgetAddedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/FWidgetAddedEvent) |  | Blueprint/GameViewportSubsystem.h |  |
| OnWidgetRemoved | [FWidgetRemovedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/FWidgetRemovedEvent) |  | Blueprint/GameViewportSubsystem.h |  |

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| ViewportWidgets | [FViewportWidgetList](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TMap) |  | Blueprint/GameViewportSubsystem.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| bool AddWidget ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Widget, [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) Slot ) | Adds it to the game's viewport. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* BlueprintCosmetic * Category="User Interface" |
| bool [AddWidgetForPlayer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/AddWidgetForPlayer) ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)*Widget, [ULocalPlayer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ULocalPlayer)* Player, [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) Slot ) | Adds the widget to the game's viewport in the section dedicated to the player. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* BlueprintCosmetic * Category="User Interface" |
| [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) GetWidgetSlot ( const [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Widget ) const | The slot info from previously added widget or info that is store for later. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* BlueprintCosmetic * Category="User Interface" |
| bool IsWidgetAdded ( const [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Widget ) const |  | Blueprint/GameViewportSubsystem.h | *BlueprintPure* BlueprintCosmetic * Category="User Interface" |
| void RemoveWidget ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Widget ) | Removes the widget from the viewport. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* BlueprintCosmetic * Category="User Interface" |
| void SetWidgetSlot ( [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Widget, [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) Slot ) | Update the slot info of a previously added widget or Store the slot info for later use. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* BlueprintCosmetic * Category="User Interface" |

#### Overridden from [USubsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USubsystem)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void Deinitialize() |  | Blueprint/GameViewportSubsystem.h |  |
| virtual void Initialize ( [FSubsystemCollectionBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FSubsystemCollectionBase)& Collection ) |  | Blueprint/GameViewportSubsystem.h |  |

### Static

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| static [UGameViewportSubsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem) * [Get](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/Get) () |  | Blueprint/GameViewportSubsystem.h |  |
| static [UGameViewportSubsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem) *[Get](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UGameViewportSubsystem/Get) ( [UWorld](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UWorld)* World ) |  | Blueprint/GameViewportSubsystem.h |  |
| static [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) SetWidgetSlotDesiredSize ( [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) Slot, FVector2D Size ) | Helper function to set the desired size in the viewport for the Slot. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* Category="GameViewportWidgetSlot" |
| static [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) SetWidgetSlotPosition ( [FGameViewportWidgetSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FGameViewportWidgetSlot) Slot, const [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)* Widget, FVector2D Position, bool bRemoveDPIScale ) | Helper function to set the position in the viewport for the Slot. | Blueprint/GameViewportSubsystem.h | *BlueprintCallable* Category="GameViewportWidgetSlot" |

# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UMenuAnchor

Title: UMenuAnchor | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UMenuAnchor

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The Menu Anchor allows you to specify an location that a popup menu should be anchored to, and should be summoned from.

* Single Child
* Popup

|  |  |
| --- | --- |
| _Name_ | UMenuAnchor |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/MenuAnchor.h |
| _Include Path_ | #include "Components/MenuAnchor.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UMenuAnchor : public UContentWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → [UContentWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget) → **UMenuAnchor**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UMenuAnchor ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/MenuAnchor.h |  |

Classes
-------

| Name | Remarks |
| --- | --- |
| [FGetUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UMenuAnchor/FGetUserWidget) |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bFitInWindow | bool | Should the menu anchor attempt to fit the menu inside the window. | Components/MenuAnchor.h | *EditAnywhere* BlueprintReadWrite *Setter="FitInWindow"* Getter="IsFitInWindow" *BlueprintSetter="FitInWindow"* Category="Menu Anchor" * Meta=(ScriptName="ShouldFitInWindow") |
| MenuClass | [TSubclassOf](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/TSubclassOf)< class [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)> | The widget class to spawn when the menu is required. | Components/MenuAnchor.h | *EditAnywhere* BlueprintReadOnly * Category="Menu Anchor" |
| OnGetMenuContentEvent | [FGetWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetWidget) | Deprecated. | Components/MenuAnchor.h | *EditAnywhere* Category="Events" * Meta=(DeprecationMessage="4.26. Use OnGetUserMenuContentEvent instead, you may need to make the previous binding return an User Widget.") |
| OnGetUserMenuContentEvent | [FGetUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UMenuAnchor/FGetUserWidget) | Called when the menu content is requested to allow a more customized handling over what to display | Components/MenuAnchor.h | *EditAnywhere* Category="Events" |
| OnMenuOpenChanged | [FOnMenuOpenChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnMenuOpenChangedEvent) | Called when the opened state of the menu changes | Components/MenuAnchor.h | *BlueprintAssignable* Category="Menu Anchor|Event" |
| Placement | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EMenuPlacement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EMenuPlacement)> | The placement location of the summoned widget. | Components/MenuAnchor.h | *EditAnywhere* BlueprintReadWrite *Setter* Getter *BlueprintSetter="SetPlacement"* Category="Menu Anchor" |
| ShouldDeferPaintingAfterWindowContent | bool |  | Components/MenuAnchor.h | *EditAnywhere* BlueprintReadOnly *Getter="IsDeferPaintingAfterWindowContent"* AdvancedDisplay * Category="Menu Anchor" |
| ShowMenuBackground | bool | For menus using the application menu stack, should the window background be visible? | Components/MenuAnchor.h | *EditAnywhere* BlueprintReadOnly *Getter="IsShowMenuBackground"* AdvancedDisplay *Category="Menu Anchor"* Meta=(EditCondition="UseApplicationMenuStack", EditConditionHides, AllowPrivateAccess="true", DisplayAfter="UseApplicationMenuStack") |
| UseApplicationMenuStack | bool | Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself. | Components/MenuAnchor.h | *EditAnywhere* BlueprintReadOnly *Getter="IsUseApplicationMenuStack"* AdvancedDisplay * Category="Menu Anchor" |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void Close() | Closes the menu if it is currently open. | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| void FitInWindow ( bool bFit ) |  | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| FVector2D GetMenuPosition() | Returns the current menu position | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| [EMenuPlacement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EMenuPlacement) GetPlacement() |  | Components/MenuAnchor.h |  |
| bool HasOpenSubMenus() | Returns whether this menu has open submenus | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| bool IsDeferPaintingAfterWindowContent() |  | Components/MenuAnchor.h |  |
| bool IsFitInWindow() |  | Components/MenuAnchor.h |  |
| bool IsOpen() | Returns true if the popup is open; false otherwise. | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| bool IsShowMenuBackground() |  | Components/MenuAnchor.h |  |
| bool IsUseApplicationMenuStack() |  | Components/MenuAnchor.h |  |
| void Open ( bool bFocusMenu ) | Opens the menu if it is not already open | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| void SetPlacement ( [EMenuPlacement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EMenuPlacement) InPlacement ) |  | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| bool [ShouldOpenDueToClick](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UMenuAnchor/ShouldOpenDueToClick) () | Returns true if we should open the menu due to a click. | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |
| void ToggleOpen ( bool bFocusOnOpen ) | Toggles the menus open state. | Components/MenuAnchor.h | *BlueprintCallable* Category="Menu Anchor" |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/MenuAnchor.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/MenuAnchor.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> HandleGetMenuContent() |  | Components/MenuAnchor.h |  |
| void HandleMenuOpenChanged ( bool bIsOpen ) |  | Components/MenuAnchor.h |  |
| void InitShouldDeferPaintingAfterWindowContent ( bool InShouldDeferPaintingAfterWindowContent ) | Initialize ShouldDeferPaintingAfterWindowContent in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/MenuAnchor.h |  |
| void InitShowMenuBackground ( bool InShowMenuBackground ) | Initialize ShowMenuBackground in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/MenuAnchor.h |  |
| void InitUseApplicationMenuStack ( bool InUseApplicationMenuStack ) | Initialize UseApplicationMenuStack in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/MenuAnchor.h |  |

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void OnSlotAdded ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) | [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget). | Components/MenuAnchor.h |  |
| virtual void OnSlotRemoved ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/MenuAnchor.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/MenuAnchor.h |  |

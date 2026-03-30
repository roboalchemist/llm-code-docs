# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButton

Title: UButton | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButton

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The button is a click-able primitive widget to enable basic interaction, you can place any other widget inside a button to make a more complex and interesting click-able element in your UI.

* Single Child
* Clickable

|  |  |
| --- | --- |
| _Name_ | UButton |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/Button.h |
| _Include Path_ | #include "Components/Button.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UButton : public UContentWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → [UContentWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget) → **UButton**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UCommonButtonInternalBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/UCommonButtonInternalBase)
* [UUIFrameworkButtonWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/UIFramework/UUIFrameworkButtonWidget)
* [UEditorUtilityButton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Editor/Blutility/UEditorUtilityButton)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UButton ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/Button.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| BackgroundColor | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | The color multiplier for the button background | Components/Button.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetBackgroundColor"* Category="Appearance" * Meta=(sRGB="true") |
| ClickMethod | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EButtonClickMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonClickMethod__Type)> | The type of mouse action required by the user to trigger the buttons 'Click' | Components/Button.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetClickMethod"* Category="Interaction" * AdvancedDisplay |
| ColorAndOpacity | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | The color multiplier for the button content | Components/Button.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetColorAndOpacity"* Category="Appearance" * Meta=(sRGB="true") |
| IsFocusable | bool | Sometimes a button should only be mouse-clickable and never keyboard focusable. | Components/Button.h | *EditAnywhere* BlueprintReadOnly *Getter* Category="Interaction" |
| OnButtonDragDetected | FOnDragDetected | Delegate triggered when a user starts to drag a button | Components/Button.h |  |
| OnButtonDragEnter | FOnDragEnter | Delegate triggered when a user's drag enters the bounds of this button | Components/Button.h |  |
| OnButtonDragLeave | FOnDragLeave | Delegate triggered when a user's drag leaves the bounds of this button | Components/Button.h |  |
| OnButtonDragOver | FOnDragOver | Delegate triggered when a user's drag leaves the bounds of this button | Components/Button.h |  |
| OnButtonDrop | FOnDrop | Delegate triggered when a user's drag is dropped in the bounds of this button | Components/Button.h |  |
| OnClicked | [FOnButtonClickedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnButtonClickedEvent) | Called when the button is clicked | Components/Button.h | *BlueprintAssignable* Category="Button|Event" |
| OnHovered | [FOnButtonHoverEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnButtonHoverEvent) |  | Components/Button.h | *BlueprintAssignable* Category="Button|Event" |
| OnLostFocus | FSimpleDelegate | Called when the button loses focus | Components/Button.h |  |
| OnPressed | [FOnButtonPressedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnButtonPressedEvent) | Called when the button is pressed | Components/Button.h | *BlueprintAssignable* Category="Button|Event" |
| OnReceivedFocus | FSimpleDelegate | Called when the button receives focus | Components/Button.h |  |
| OnReleased | [FOnButtonReleasedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnButtonReleasedEvent) | Called when the button is released | Components/Button.h | *BlueprintAssignable* Category="Button|Event" |
| OnUnhovered | [FOnButtonHoverEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnButtonHoverEvent) |  | Components/Button.h | *BlueprintAssignable* Category="Button|Event" |
| PressMethod | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EButtonPressMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonPressMethod__Type)> | The type of keyboard/gamepad button press action required by the user to trigger the buttons 'Click' | Components/Button.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetPressMethod"* Category="Interaction" * AdvancedDisplay |
| TouchMethod | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EButtonTouchMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonTouchMethod__Type)> | The type of touch action required by the user to trigger the buttons 'Click' | Components/Button.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetTouchMethod"* Category="Interaction" * AdvancedDisplay |
| WidgetStyle | [FButtonStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FButtonStyle) | The button style used at runtime | Components/Button.h | *EditAnywhere* BlueprintReadWrite *Getter="GetStyle"* Setter="SetStyle" *BlueprintSetter="SetStyle"* Category="Appearance" * Meta=(DisplayName="Style") |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) GetBackgroundColor() |  | Components/Button.h |  |
| [EButtonClickMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonClickMethod__Type) GetClickMethod() |  | Components/Button.h |  |
| [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) GetColorAndOpacity() |  | Components/Button.h |  |
| bool GetIsFocusable() |  | Components/Button.h |  |
| [EButtonPressMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonPressMethod__Type) GetPressMethod() |  | Components/Button.h |  |
| const [FButtonStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FButtonStyle)& GetStyle() |  | Components/Button.h |  |
| [EButtonTouchMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonTouchMethod__Type) GetTouchMethod() |  | Components/Button.h |  |
| bool [IsPressed](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButton/IsPressed) () | Returns true if the user is actively pressing the button. | Components/Button.h | *BlueprintCallable* Category="Button" |
| void SetAllowDragDrop ( bool bInAllowDragDrop ) |  | Components/Button.h | *BlueprintCallable* Category="Button" |
| void SetBackgroundColor ( [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) InBackgroundColor ) | Sets the color multiplier for the button background | Components/Button.h | *BlueprintCallable* Category="Button|Appearance" |
| void SetClickMethod ( [EButtonClickMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonClickMethod__Type) InClickMethod ) |  | Components/Button.h | *BlueprintCallable* Category="Button" |
| void SetColorAndOpacity ( [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) InColorAndOpacity ) | Sets the color multiplier for the button content | Components/Button.h | *BlueprintCallable* Category="Button|Appearance" |
| void SetPressMethod ( [EButtonPressMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonPressMethod__Type) InPressMethod ) |  | Components/Button.h | *BlueprintCallable* Category="Button" |
| void SetStyle ( const [FButtonStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FButtonStyle)& InStyle ) | Sets the color multiplier for the button background | Components/Button.h | *BlueprintCallable* Category="Button|Appearance" |
| void SetTouchMethod ( [EButtonTouchMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonTouchMethod__Type) InTouchMethod ) |  | Components/Button.h | *BlueprintCallable* Category="Button" |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/Button.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UButton/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/Button.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/Button.h |  |

#### Overridden from [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void PostLoad() | Begin [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject). | Components/Button.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void InitIsFocusable ( bool InIsFocusable ) | Initialize IsFocusable in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/Button.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) SlateHandleClicked() | Handle the actual click event from slate and forward it on | Components/Button.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) SlateHandleDragDetected ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) | Drag and Drop. | Components/Button.h |  |
| void SlateHandleDragEnter ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Components/Button.h |  |
| void SlateHandleDragLeave ( const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Components/Button.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) SlateHandleDragOver ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Components/Button.h |  |
| [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) SlateHandleDrop ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Components/Button.h |  |
| void SlateHandleHovered() |  | Components/Button.h |  |
| void SlateHandleOnLostFocus() |  | Components/Button.h |  |
| void SlateHandleOnReceivedFocus() |  | Components/Button.h |  |
| void SlateHandlePressed() |  | Components/Button.h |  |
| void SlateHandleReleased() |  | Components/Button.h |  |
| void SlateHandleUnhovered() |  | Components/Button.h |  |

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [UClass](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UClass) * GetSlotClass() | [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget). | Components/Button.h |  |
| virtual void OnSlotAdded ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/Button.h |  |
| virtual void OnSlotRemoved ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/Button.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> GetAccessibleWidget() | Gets the widget that accessibility properties should synchronize to. | Components/Button.h |  |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildDesignWidget ( [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> Content ) |  | Components/Button.h |  |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/Button.h |  |

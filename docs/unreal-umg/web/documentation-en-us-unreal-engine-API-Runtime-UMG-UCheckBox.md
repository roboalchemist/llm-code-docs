# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCheckBox

Title: UCheckBox | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCheckBox

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and 'indeterminable. You can use the checkbox for a classic checkbox, or as a toggle button, or as radio buttons.

* Single Child
* Toggle

|  |  |
| --- | --- |
| _Name_ | UCheckBox |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/CheckBox.h |
| _Include Path_ | #include "Components/CheckBox.h" |

Syntax
------

```
UCLASS (MinimalAPI)  
class UCheckBox : public UContentWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget) → [UContentWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UContentWidget) → **UCheckBox**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UEditorUtilityCheckBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Editor/Blutility/UEditorUtilityCheckBox)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UCheckBox ( const [FObjectInitializer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FObjectInitializer)& ObjectInitializer ) |  | Components/CheckBox.h |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| CheckedState | [ECheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ECheckBoxState) | Whether the check box is currently in a checked state | Components/CheckBox.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintGetter="GetCheckedState"* BlueprintSetter="SetCheckedState" *FieldNotify* Category="Appearance" |
| CheckedStateDelegate | [FGetCheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetCheckBoxState) | A bindable delegate for the IsChecked. | Components/CheckBox.h |  |
| ClickMethod | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EButtonClickMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonClickMethod__Type)> | The type of mouse action required by the user to trigger the buttons 'Click' | Components/CheckBox.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetClickMethod"* Category="Interaction" * AdvancedDisplay |
| HorizontalAlignment | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EHorizontalAlignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EHorizontalAlignment)> | How the content of the toggle button should align within the given space | Components/CheckBox.h | *EditAnywhere* BlueprintReadOnly * Category="Appearance" |
| IsFocusable | bool | Sometimes a button should only be mouse-clickable and never keyboard focusable. | Components/CheckBox.h | *EditAnywhere* BlueprintReadOnly *Getter* Category="Interaction" |
| OnCheckStateChanged | [FOnCheckBoxComponentStateChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FOnCheckBoxComponentStateChanged) | Called when the checked state has changed | Components/CheckBox.h | *BlueprintAssignable* Category="CheckBox|Event" |
| PressMethod | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EButtonPressMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonPressMethod__Type)> | The type of keyboard/gamepad button press action required by the user to trigger the buttons 'Click' | Components/CheckBox.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetPressMethod"* Category="Interaction" * AdvancedDisplay |
| TouchMethod | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EButtonTouchMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonTouchMethod__Type)> | The type of touch action required by the user to trigger the buttons 'Click' | Components/CheckBox.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *BlueprintSetter="SetTouchMethod"* Category="Interaction" * AdvancedDisplay |
| WidgetStyle | [FCheckBoxStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FCheckBoxStyle) | The checkbox bar style | Components/CheckBox.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *Category="Style"* Meta=(DisplayName="Style") |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| [ECheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ECheckBoxState) GetCheckedState() | Returns the full current checked state. | Components/CheckBox.h | *BlueprintCallable* Category="Widget" |
| [EButtonClickMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonClickMethod__Type) GetClickMethod() | Returns the click method. | Components/CheckBox.h |  |
| bool GetIsFocusable() | Is the checkbox focusable. | Components/CheckBox.h |  |
| [EButtonPressMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonPressMethod__Type) GetPressMethod() | Returns the press method. | Components/CheckBox.h |  |
| [EButtonTouchMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonTouchMethod__Type) GetTouchMethod() | Returns the touch method. | Components/CheckBox.h |  |
| const [FCheckBoxStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FCheckBoxStyle)& GetWidgetStyle() | Returns the local style. | Components/CheckBox.h |  |
| bool IsChecked() | Returns true if the checkbox is currently checked | Components/CheckBox.h | *BlueprintCallable* Category="Widget" |
| bool IsPressed() | Returns true if this button is currently pressed | Components/CheckBox.h | *BlueprintCallable* Category="Widget" |
| void SetCheckedState ( [ECheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ECheckBoxState) InCheckedState ) | Sets the checked state. | Components/CheckBox.h | *BlueprintCallable* Category="Widget" |
| void SetClickMethod ( [EButtonClickMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonClickMethod__Type) InClickMethod ) | Sets the click method. | Components/CheckBox.h | *BlueprintCallable* Category="Button" |
| void SetIsChecked ( bool InIsChecked ) | Sets the checked state. | Components/CheckBox.h | *BlueprintCallable* Category="Widget" |
| void SetPressMethod ( [EButtonPressMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonPressMethod__Type) InPressMethod ) | Sets the press method. | Components/CheckBox.h | *BlueprintCallable* Category="Button" |
| void SetTouchMethod ( [EButtonTouchMethod::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EButtonTouchMethod__Type) InTouchMethod ) | Sets the touch method. | Components/CheckBox.h | *BlueprintCallable* Category="Button" |
| void SetWidgetStyle ( const [FCheckBoxStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FCheckBoxStyle)& InStyle ) | Sets the style. | Components/CheckBox.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/CheckBox.h |  |
| virtual void [SynchronizeProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UCheckBox/SynchronizeProperties) () | Applies all properties to the native widget if possible. | Components/CheckBox.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/CheckBox.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void InitCheckedStateDelegate ( [FGetCheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget/FGetCheckBoxState) InCheckedStateDelegate ) |  | Components/CheckBox.h |  |
| void InitIsFocusable ( bool InIsFocusable ) | Initialize IsFocusable in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/CheckBox.h |  |
| [ECheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ECheckBoxState) K2_Gate_CheckedState() |  | Components/CheckBox.h |  |
| void SlateOnCheckStateChangedCallback ( [ECheckBoxState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ECheckBoxState) NewState ) |  | Components/CheckBox.h |  |

#### Overridden from [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void OnSlotAdded ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) | [UPanelWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelWidget). | Components/CheckBox.h |  |
| virtual void OnSlotRemoved ( [UPanelSlot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UPanelSlot)* Slot ) |  | Components/CheckBox.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> GetAccessibleWidget() | Gets the widget that accessibility properties should synchronize to. | Components/CheckBox.h |  |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildDesignWidget ( [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> Content ) |  | Components/CheckBox.h |  |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> RebuildWidget() | Function implemented by all subclasses of [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) is called when the underlying [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) needs to be constructed. | Components/CheckBox.h |  |

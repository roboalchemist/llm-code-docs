# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey

Title: UComboBoxKey | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one. Use OnGenerateConentWidgetEvent to return a custom built widget.

|  |  |
| --- | --- |
| _Name_ | UComboBoxKey |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/ComboBoxKey.h |
| _Include Path_ | #include "Components/ComboBoxKey.h" |

Syntax
------

```
UCLASS (Meta=(DisplayName="ComboBox (Key)"), MinimalAPI)  
class UComboBoxKey : public UWidget
```

Inheritance Hierarchy
---------------------

* [UObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBase) → [UObjectBaseUtility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObjectBaseUtility) → [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) → [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual) → [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget) → **UComboBoxKey**

Implements Interfaces
---------------------

* [INotifyFieldValueChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/FieldNotification/INotifyFieldValueChanged)
* [IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/IInterface)

Derived Classes
---------------

* [UEditorUtilityComboBoxKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Editor/Blutility/UEditorUtilityComboBoxKey)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| UComboBoxKey() |  | Components/ComboBoxKey.h |  |

Classes
-------

| Name | Remarks |
| --- | --- |
| [FGenerateWidgetEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FGenerateWidgetEvent) |  |
| [FOnOpeningEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FOnOpeningEvent) |  |
| [FOnSelectionChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FOnSelectionChangedEvent) |  |

Variables
---------

### Public

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bEnableGamepadNavigationMode | bool | When false, directional keys will change the selection. | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadWrite *Getter="IsEnableGamepadNavigationMode"* Setter="SetEnableGamepadNavigationMode" *Category=Style* AdvancedDisplay |
| bHasDownArrow | bool | When false, the down arrow is not generated and it is up to the API consumer to make their own visual hint that this is a drop down. | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadWrite *Getter="IsHasDownArrow"* Setter="SetHasDownArrow" *Category=Style* AdvancedDisplay |
| bIsFocusable | bool | When true, allows the combo box to receive keyboard focus | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadOnly *Getter="IsFocusable"* Category=Style |
| ContentPadding | [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) |  | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category=Style |
| ForegroundColor | [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) | The foreground color to pass through the hierarchy. | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadOnly *Getter* Category=Style * Meta=(DesignerRebuild) |
| ItemStyle | [FTableRowStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FTableRowStyle) | The item row style. | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter * Category=Style |
| MaxListHeight | float | The max height of the combobox list that opens | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *Category=Style* AdvancedDisplay |
| OnGenerateContentWidget | [FGenerateWidgetEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FGenerateWidgetEvent) | Called when the widget is needed for the content. | Components/ComboBoxKey.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |
| OnGenerateItemWidget | [FGenerateWidgetEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FGenerateWidgetEvent) | Called when the widget is needed for the item. | Components/ComboBoxKey.h | *EditAnywhere* Category=Events * Meta=(IsBindableEvent="True") |
| OnOpening | [FOnOpeningEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FOnOpeningEvent) | Called when the combobox is opening | Components/ComboBoxKey.h | *BlueprintAssignable* Category=Events |
| OnSelectionChanged | [FOnSelectionChangedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UComboBoxKey/FOnSelectionChangedEvent) | Called when a new item is selected in the combobox. | Components/ComboBoxKey.h | *BlueprintAssignable* Category=Events |
| ScrollBarStyle | [FScrollBarStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FScrollBarStyle) | The scroll bar style. | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadOnly *Getter* Category="Style" |
| WidgetStyle | [FComboBoxStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FComboBoxStyle) | The combobox style. | Components/ComboBoxKey.h | *EditAnywhere* BlueprintReadWrite *Getter* Setter *Category=Style* Meta=(DisplayName="Style") |

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| ComboBoxContent | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SBox)> | A shared pointer to a container that holds the combobox content that is selected | Components/ComboBoxKey.h |  |
| MyComboBox | [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SComboBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/SComboBox)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)>> | A shared pointer to the underlying slate combobox | Components/ComboBoxKey.h |  |
| Options | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> |  | Components/ComboBoxKey.h | *EditAnywhere* Category=Content |
| SelectedOption | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) |  | Components/ComboBoxKey.h | *EditAnywhere* FieldNotify * Category=Content |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void AddOption ( [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) Option ) | Add an element to the option list. | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" |
| void ClearOptions() | Remove all the elements of the option list. | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" |
| void ClearSelection() | Clear the current selection. | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" |
| [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) GetContentPadding() | Get the padding for content. | Components/ComboBoxKey.h |  |
| [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) GetForegroundColor() | Get the foreground color of the button. | Components/ComboBoxKey.h |  |
| const [FTableRowStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FTableRowStyle)& GetItemStyle() | Get the style of the items. | Components/ComboBoxKey.h |  |
| float GetMaxListHeight() | Get the maximum height of the combobox list. | Components/ComboBoxKey.h |  |
| const [FScrollBarStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FScrollBarStyle)& GetScrollBarStyle() | Get the style of the scrollbar. | Components/ComboBoxKey.h |  |
| [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) GetSelectedOption() | Get the current selected option | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" |
| const [FComboBoxStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FComboBoxStyle)& GetWidgetStyle() | Get the style of the combobox. | Components/ComboBoxKey.h |  |
| bool IsEnableGamepadNavigationMode() | Is the combobox navigated by gamepad. | Components/ComboBoxKey.h |  |
| bool IsFocusable() | Is the combobox focusable. | Components/ComboBoxKey.h |  |
| bool IsHasDownArrow() | Is the combobox arrow showing. | Components/ComboBoxKey.h |  |
| bool IsOpen() | Is the combobox menu opened. | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" * Meta=(ReturnDisplayName="bOpen") |
| bool RemoveOption ( [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) Option ) | Remove an element to the option list. | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" |
| void SetContentPadding ( [FMargin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FMargin) InPadding ) | Set the padding for content. | Components/ComboBoxKey.h |  |
| void SetEnableGamepadNavigationMode ( bool InEnableGamepadNavigationMode ) | Set whether the combobox is navigated by gamepad. | Components/ComboBoxKey.h |  |
| void SetHasDownArrow ( bool InHasDownArrow ) | Set whether the combobox arrow is showing. | Components/ComboBoxKey.h |  |
| void SetItemStyle ( const [FTableRowStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FTableRowStyle)& InItemStyle ) | Set the style of the items. | Components/ComboBoxKey.h |  |
| void SetMaxListHeight ( float InMaxHeight ) | Set the maximum height of the combobox list. | Components/ComboBoxKey.h |  |
| void SetSelectedOption ( [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) Option ) | Set the current selected option. | Components/ComboBoxKey.h | *BlueprintCallable* Category="ComboBox" |
| void SetWidgetStyle ( const [FComboBoxStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FComboBoxStyle)& InWidgetStyle ) | Set the style of the combobox. | Components/ComboBoxKey.h |  |

#### Overridden from [UWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual const [FText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FText) GetPaletteCategory() | Gets the palette category of the widget | Components/ComboBoxKey.h |  |

#### Overridden from [UVisual](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UVisual)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void ReleaseSlateResources ( bool bReleaseChildren ) |  | Components/ComboBoxKey.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void InitForegroundColor ( [FSlateColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateColor) InForegroundColor ) | Initialize ForegroundColor in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/ComboBoxKey.h |  |
| void InitIsFocusable ( bool InIsFocusable ) | Initialize IsFocusable in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/ComboBoxKey.h |  |
| void InitScrollBarStyle ( const [FScrollBarStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FScrollBarStyle)& InScrollBarStyle ) | Initialize the scrollbar style in the constructor before the [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) is constructed. | Components/ComboBoxKey.h |  |

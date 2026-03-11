# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectTableRow

Title: SObjectTableRow | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectTableRow

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

It's an SObjectWidget! It's an ITableRow! It does it all!

By using UUserWidget::TakeDerivedWidget(), this class allows UMG to fully leverage the robust Slate list view widgets. The major gain from this is item virtualization, which is an even bigger deal when unnecessary widgets come with a boatload of additional [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject) allocations.

The owning [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget) is expected to implement the [IUserListEntry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/IUserListEntry)[UInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UInterface), which allows the row widget to respond to various list-related events.

Note: Much of the implementation here matches STableRow exactly, so refer there if looking for additional information.

|  |  |
| --- | --- |
| _Name_ | SObjectTableRow |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Slate/SObjectTableRow.h |
| _Include Path_ | #include "Slate/SObjectTableRow.h" |

Syntax
------

```
template<typename ItemType>  
class SObjectTableRow :  
    public SObjectWidget ,  
    public IObjectTableRow
```

Inheritance Hierarchy
---------------------

* [FGCObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject) → [SObjectWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectWidget) → **SObjectTableRow**
* [FSharedFromThisBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FSharedFromThisBase) → [TSharedFromThis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedFromThis) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) → [SObjectWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectWidget) → **SObjectTableRow**
* [FSlateControlledConstruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FSlateControlledConstruction) → [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget) → [SCompoundWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SCompoundWidget) → [SObjectWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectWidget) → **SObjectTableRow**

Implements Interfaces
---------------------

* [IObjectTableRow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/IObjectTableRow)
* [ITableRow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ITableRow)

Derived Classes
---------------

* [SCommonButtonTableRow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/CommonUI/SCommonButtonTableRow)

Destructors
-----------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual ~SObjectTableRow() |  | Slate/SObjectTableRow.h |  |

Structs
-------

| Name | Remarks |
| --- | --- |
| [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectTableRow/FArguments) |  |

Variables
---------

### Protected

| Name | Type | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperties#propertyspecifiers) |
| --- | --- | --- | --- | --- |
| bAllowDragDrop | bool | Whether to allow drag drop operations to be performed on the list | Slate/SObjectTableRow.h |  |
| bAllowDragging | bool | Whether to allow dragging of this item | Slate/SObjectTableRow.h |  |
| bAllowKeepPreselectedItems | bool | If true, when selecting an item via mouse button, we allow pre-selected items to remain selected | Slate/SObjectTableRow.h |  |
| bChangedSelectionOnMouseDown | bool |  | Slate/SObjectTableRow.h |  |
| bDragWasDetected | bool | Whether or not drag was detected | Slate/SObjectTableRow.h |  |
| bIsAppearingSelected | bool |  | Slate/SObjectTableRow.h |  |
| bProcessingSelectionTouch | bool |  | Slate/SObjectTableRow.h |  |
| IndexInList | int32 |  | Slate/SObjectTableRow.h |  |
| ItemDropZone | [TOptional](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TOptional)<[EItemDropZone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/EItemDropZone)> | Are we currently dragging/dropping over this item? | Slate/SObjectTableRow.h |  |

Functions
---------

### Public

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| void Construct ( const [FArguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectTableRow/FArguments)& InArgs, const [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[STableViewBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/STableViewBase)>& InOwnerTableView, [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)& InWidgetObject, [UListViewBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UListViewBase)* InOwnerListView ) |  | Slate/SObjectTableRow.h |  |
| [EActiveTimerReturnType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EActiveTimerReturnType)[DetectItemSelectionChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectTableRow/DetectItemSelectionChanged) ( double InCurrentTime, float InDeltaTime ) |  | Slate/SObjectTableRow.h |  |
| bool GetAllowDragDrop() |  | Slate/SObjectTableRow.h |  |
| virtual void HandleEntryDragged ( [UDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation)* Operation ) |  | Slate/SObjectTableRow.h |  |
| virtual void HandleEntryDropped ( [UDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation)* Operation ) |  | Slate/SObjectTableRow.h |  |
| virtual void NotifyItemExpansionChanged ( bool bIsExpanded ) |  | Slate/SObjectTableRow.h |  |
| [EItemDropZone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/EItemDropZone) ZoneFromPointerPosition ( UE::Slate::FDeprecateVector2DParameter LocalPointerPos, UE::Slate::FDeprecateVector2DParameter LocalSize, [EOrientation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/EOrientation) Orientation ) |  | Slate/SObjectTableRow.h |  |

#### Overridden from [SObjectWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void OnDragCancelled ( const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent, [UDragDropOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UDragDropOperation)* Operation ) |  | Slate/SObjectTableRow.h |  |

#### Overridden from [SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnDragDetected ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual void OnDragEnter ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual void OnDragLeave ( [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent) const& DragDropEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnDragOver ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnDrop ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FDragDropEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FDragDropEvent)& DragDropEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnMouseButtonDoubleClick ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& InMyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& InMouseEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnMouseButtonDown ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnMouseButtonUp ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual void OnMouseEnter ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual void OnMouseLeave ( const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& MouseEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnTouchEnded ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& InTouchEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual [FReply](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FReply) OnTouchStarted ( const [FGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FGeometry)& MyGeometry, const [FPointerEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FPointerEvent)& InTouchEvent ) |  | Slate/SObjectTableRow.h |  |
| virtual bool SupportsKeyboardFocus() |  | Slate/SObjectTableRow.h |  |

#### Overridden from [IObjectTableRow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/IObjectTableRow)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [UListViewBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UListViewBase) * GetOwningListView() |  | Slate/SObjectTableRow.h |  |
| virtual [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget) * GetUserWidget() |  | Slate/SObjectTableRow.h |  |

#### Overridden from [ITableRow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ITableRow)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> AsWidget() |  | Slate/SObjectTableRow.h |  |
| virtual int32 DoesItemHaveChildren() |  | Slate/SObjectTableRow.h |  |
| virtual [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> GetContent() |  | Slate/SObjectTableRow.h |  |
| virtual int32 GetIndentLevel() |  | Slate/SObjectTableRow.h |  |
| virtual int32 GetIndexInList() |  | Slate/SObjectTableRow.h |  |
| virtual FVector2D GetRowSizeForColumn ( const [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)& InColumnName ) const |  | Slate/SObjectTableRow.h |  |
| virtual [ESelectionMode::Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ESelectionMode__Type) GetSelectionMode() |  | Slate/SObjectTableRow.h |  |
| virtual [TBitArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TBitArray) GetWiresNeededByDepth() |  | Slate/SObjectTableRow.h |  |
| virtual void InitializeRow() |  | Slate/SObjectTableRow.h |  |
| virtual bool IsItemExpanded() |  | Slate/SObjectTableRow.h |  |
| virtual bool IsItemSelected() |  | Slate/SObjectTableRow.h |  |
| virtual bool IsLastChild() |  | Slate/SObjectTableRow.h |  |
| virtual void Private_OnExpanderArrowShiftClicked() |  | Slate/SObjectTableRow.h |  |
| virtual void ResetRow() |  | Slate/SObjectTableRow.h |  |
| virtual void SetIndexInList ( int32 InIndexInList ) |  | Slate/SObjectTableRow.h |  |
| virtual void ToggleExpansion() |  | Slate/SObjectTableRow.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void [DetectItemSelectionChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/SObjectTableRow/DetectItemSelectionChanged) () |  | Slate/SObjectTableRow.h |  |
| const TObjectPtrWrapTypeOf< ItemType > * GetItemForThis ( const [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[ITypedTableView](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ITypedTableView)< ItemType >>& OwnerTable ) const |  | Slate/SObjectTableRow.h |  |
| virtual void InitializeObjectRow() |  | Slate/SObjectTableRow.h |  |
| bool IsItemSelectable() |  | Slate/SObjectTableRow.h |  |
| virtual void OnItemSelectionChanged ( bool bIsItemSelected ) |  | Slate/SObjectTableRow.h |  |
| virtual void ResetObjectRow() |  | Slate/SObjectTableRow.h |  |

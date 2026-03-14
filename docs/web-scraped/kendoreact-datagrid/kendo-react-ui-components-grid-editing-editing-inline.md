# Source: https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-inline

Title: React Data Grid Editing Inline Editing - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-inline

Markdown Content:
[Inline Editing in KendoReact Data Grid Premium](https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-inline#inline-editing-in-kendoreact-data-grid)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 19, 2025

The KendoReact Data Grid enables you to create, update, and delete data records inline.

![Image 1: ninja-icon](https://www.telerik.com/kendo-react-ui/components/static/d2ecd6c1a01f6b1598a481623b8f4389/start-free-trial-icon.inline.svg)The Inline Editing feature of the Grid is part of [KendoReact](https://www.telerik.com/kendo-react-ui) premium, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components for building polished, performant apps. Test-drive all features with a free 30-day trial.[Start Free Trial](https://www.telerik.com/try/kendo-react-ui)

The following example demonstrates how to implement the inline editing.

[Setup](https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-inline#setup)
--------------------------------------------------------------------------------------------

1.   Set the `editable` prop of the Grid to true and configure its [`edit`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops) property to manage the built-in edit state and track which rows are being edited.

jsx `const [edit, setEdit] = React.useState<EditDescriptor>({});` jsx 
```
<Grid
    edit={edit}
    editable={true}
>
``` 
2.   Configure the command column by defining the command buttons inside the [GridCellProps](https://www.telerik.com/kendo-react-ui/components/grid/api/gridcellprops) component. In the example below, we use a function which receives all functions that will be executed from the command buttons and passes them to the command cell component.

jsx 
```
const CommandCell = (props) => {
    const { edit, enterEdit, remove, add, discard, update, cancel } = props;
    return (
        <MyCommandCell
            {...props}
            edit={edit}
            enterEdit={enterEdit}
            remove={remove}
            add={add}
            discard={discard}
            update={update}
            cancel={cancel}
        />
    );
};
``` jsx 
```
export const MyCommandCell = (props) => {
    const { dataItem, edit, remove, add, update, enterEdit, discard, cancel } = props;

    const [visible, setVisible] = React.useState(false);

    const inEdit = edit[dataItem.ProductID];
    const isNewItem = dataItem.new === true;

    const onDeleteData = () => {
        remove(dataItem);
        setVisible(!visible);
    };

    const toggleDialog = () => {
        setVisible(!visible);
    };

    let commandLabel = 'Edit';
    if (inEdit) {
        commandLabel = isNewItem ? 'Add' : 'Update';
    }

    // Extract the nested ternary operation into a variable
    let secondaryCommandLabel = 'Remove';
    if (inEdit) {
        secondaryCommandLabel = isNewItem ? 'Discard' : 'Cancel';
    }

    return (
        <td className="k-command-cell">
            <Button
                themeColor={'primary'}
                onClick={() => {
                    if (inEdit) {
                        if (isNewItem) {
                            add(dataItem);
                        } else {
                            update(dataItem);
                        }
                    } else {
                        enterEdit(dataItem);
                    }
                }}
            >
                {commandLabel}
            </Button>
            <Button
                themeColor={'primary'}
                onClick={() => {
                    if (inEdit) {
                        if (isNewItem) {
                            discard(dataItem);
                        } else {
                            cancel(dataItem);
                        }
                    } else {
                        toggleDialog();
                    }
                }}
            >
                {secondaryCommandLabel}
            </Button>
            {visible && (
                <Dialog title={'Delete Data'} onClose={toggleDialog} width={350}>
                    <div>Are you sure you want to delete item with ID {dataItem.ProductID}?</div>
                    <DialogActionsBar>
                        <Button onClick={onDeleteData}>Delete</Button>
                        <Button onClick={toggleDialog}>Cancel</Button>
                    </DialogActionsBar>
                </Dialog>
            )}
        </td>
    );
};
``` 
3.   Define the `enterEdit`, `remove`, `add`, `update`, `discard` and `cancel` functions needed by the command cell.

jsx 
```
const enterEdit = (dataItem: Product) => {
    setEdit((edit) => ({ ...edit, [dataItem.ProductID]: true }));
};
``` jsx 
```
const remove = (dataItem: Product) => {
    deleteItem(dataItem);
    setData((prevData) => prevData.filter((item) => item.ProductID !== dataItem.ProductID));
};
``` jsx 
```
const add = (dataItem: Product) => {
    dataItem.new = false;
    insertItem(dataItem);
    setEdit((edit) => ({ ...edit, [dataItem.ProductID]: false }));
};
``` jsx 
```
const discard = (dataItem: Product) => {
    const newData = [...data.filter((item) => item.ProductID !== dataItem.ProductID)];
    setData(newData);
};
``` jsx 
```
const update = (dataItem: Product) => {
    updateItem(dataItem);
    setEdit((edit) => ({ ...edit, [dataItem.ProductID]: false }));
};
``` jsx 
```
const cancel = (dataItem: Product) => {
    const originalItem = getItems().find((p) => p.ProductID === dataItem.ProductID);

    if (originalItem) {
        const newData = data.map((item) => (item.ProductID === originalItem.ProductID ? originalItem : item));
        setData(newData);
        setEdit((edit) => ({ ...edit, [dataItem.ProductID]: false }));
    }
};
``` 
4.   Define a function for the [`onItemChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onitemchange) event which will handle the data changes during editing. The event provides the edited data item, the field being changed, and the new value available as [`onItemChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/griditemchangeevent) parameters.

jsx `<Grid onItemChange={itemChange}>` jsx 
```
const itemChange = (event: GridItemChangeEvent) => {
    const newData = data.map((item) =>
        item.ProductID === event.dataItem.ProductID
            ? {
                  ...item,
                  [event.field || '']: event.value
              }
            : item
    );
    setData(newData);
};
``` 
5.   Per column, set the options that are related to row editing:

*   [`editable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridcolumnprops#editable) — Determines if the column is editable.
*   [`editor`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridcolumnprops#editor) — Specifies the data type of the column and, based on that, sets the appropriate editor.

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-inline#suggested-links)
----------------------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [Data Query Overview](https://www.telerik.com/kendo-react-ui/components/dataquery)
*   [API Reference of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops)
*   [API Reference of the GridToolbar](https://www.telerik.com/kendo-react-ui/components/grid/api/gridtoolbar)
*   [API Index of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/api)

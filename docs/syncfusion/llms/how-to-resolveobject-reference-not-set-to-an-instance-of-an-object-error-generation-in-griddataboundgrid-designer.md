# Source: https://docs.syncfusion.com/windowsforms/classic/databoundgrid/how-to/how-to-resolveobject-reference-not-set-to-an-instance-of-an-object-error-generation-in-griddataboundgrid-designer.md

# How to resolveObject reference in Windows Forms DataBoundGrid

GridDataBoundGrid is a grid that is bound to data sources such as Data Tables, String Collections, Data Sets, and Data Views. The Hidden, Position and Width properties of GridDataBoundColumn generate the âObject reference not set to an instance of an objectâ error on designer code generation. This issue has been resolved for version 10.1.0.44 and following versions by setting DesignerSerializationVisibility for these codes to Hidden. However, if the application is migrated from version 9.4.0.62 or earlier versions to the latest version, the designer code throws this exception. This can be fixed by removing the âDesignerSerializationVisibilityâ part of code from the designer.


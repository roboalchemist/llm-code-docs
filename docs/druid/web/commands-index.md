druid

# Module commands

Source

## Constants§

CLOSE_ALL_WINDOWSClose all windows.CLOSE_WINDOWThe selector for a command to close a window.CONFIGURE_WINDOWApply the configuration payload to an existing window. The target should be a WindowId.COPYCopy the current selection.CUTCut the current selection.HIDE_APPLICATIONDeprecatedHide the application. (mac only)HIDE_OTHERSDeprecatedHide all other applications. (mac only)HIDE_WINDOWThe selector for a command to hide a specific windowNEW_FILEShow the new file dialog.OPEN_FILEOpen a path, must be handled by the application.OPEN_FILESOpen a set of paths, must be handled by the application.OPEN_PANEL_CANCELLEDSent when the user cancels an open file panel.PASTEPaste.PRINTShow the print dialog.PRINT_PREVIEWShow the print preview.PRINT_SETUPShow the print-setup window.QUIT_APPQuit the running application. This command is handled by the Druid library.REDORedo.SAVE_FILESave the current path.SAVE_FILE_ASSave to a given location.SAVE_PANEL_CANCELLEDSent when the user cancels a save file panel.SCROLL_TO_VIEWInforms this widget that a child wants a specific region to be shown. The payload is the
requested region in global coordinates.SELECT_ALLSelect all.SHOW_ABOUTShow the application’s “about” window.SHOW_ALLShow all applications.SHOW_OPEN_PANELWhen submitted by the application, a file picker dialog will be shown to the user,
and an `OPEN_FILE` command will be sent if a path is chosen.SHOW_PREFERENCESShow the application preferences.SHOW_SAVE_PANELWhen submitted by the application, the system will show the ‘save as’ panel,
and if a path is selected the system will issue a `SAVE_FILE` command
with the selected path as the payload.SHOW_WINDOWThe selector for a command to bring a window to the front, and give it focus.UNDOUndo.

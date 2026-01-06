# Source: https://docs.helix-editor.com/keymap.html

## Keymap

- Normal modeMovementChangesShellSelection manipulationSearchMinor modesView modeGoto modeMatch modeWindow modeSpace modePopupCompletion MenuSignature-help PopupUnimpaired
- Insert mode
- Select / extend mode
- Picker
- Prompt
> 💡 Mappings marked (LSP) require an active language server for the file.
> 💡 Mappings marked (TS) require a tree-sitter grammar for the file type.
> ⚠️ Some terminals' default key mappings conflict with Helix's. If any of the mappings described on this page do not work as expected, check your terminal's mappings to ensure they do not conflict. See thewikifor known conflicts.

## Normal mode

Normal mode is the default mode when you launch helix. You can return to it from other modes by pressing theEscapekey.

### Movement

> NOTE: Unlike Vim,f,F,tandTare not confined to the current line.
KeyDescriptionCommandh,LeftMove leftmove_char_leftj,DownMove downmove_visual_line_downk,UpMove upmove_visual_line_upl,RightMove rightmove_char_rightwMove next word startmove_next_word_startbMove previous word startmove_prev_word_starteMove next word endmove_next_word_endWMove next WORD startmove_next_long_word_startBMove previous WORD startmove_prev_long_word_startEMove next WORD endmove_next_long_word_endtFind till next charfind_till_charfFind next charfind_next_charTFind till previous chartill_prev_charFFind previous charfind_prev_charGGo to line number<n>goto_lineAlt-.Repeat last motion (f,t,m,[or])repeat_last_motionHomeMove to the start of the linegoto_line_startEndMove to the end of the linegoto_line_endCtrl-b,PageUpMove page uppage_upCtrl-f,PageDownMove page downpage_downCtrl-uMove cursor and page half page uppage_cursor_half_upCtrl-dMove cursor and page half page downpage_cursor_half_downCtrl-iJump forward on the jumplistjump_forwardCtrl-oJump backward on the jumplistjump_backwardCtrl-sSave the current selection to the jumplistsave_selection

### Changes

KeyDescriptionCommandrReplace with a characterreplaceRReplace with yanked textreplace_with_yanked~Switch case of the selected textswitch_case`Set the selected text to lower caseswitch_to_lowercaseAlt-`Set the selected text to upper caseswitch_to_uppercaseiInsert before selectioninsert_modeaInsert after selection (append)append_modeIInsert at the start of the lineinsert_at_line_startAInsert at the end of the lineinsert_at_line_endoOpen new line below selectionopen_belowOOpen new line above selectionopen_above.Repeat last insertN/AuUndo changeundoURedo changeredoAlt-uMove backward in historyearlierAlt-UMove forward in historylateryYank selectionyankpPaste after selectionpaste_afterPPaste before selectionpaste_before"<reg>Select a register to yank to or paste fromselect_register>Indent selectionindent<Unindent selectionunindent=Format selection (LSP)format_selectionsdDelete selectiondelete_selectionAlt-dDelete selection, without yankingdelete_selection_noyankcChange selection (delete and enter insert mode)change_selectionAlt-cChange selection (delete and enter insert mode, without yanking)change_selection_noyankCtrl-aIncrement object (number) under cursorincrementCtrl-xDecrement object (number) under cursordecrementQStart/stop macro recording to the selected register (experimental)record_macroqPlay back a recorded macro from the selected register (experimental)replay_macro

#### Shell

KeyDescriptionCommand|Pipe each selection through shell command, replacing with outputshell_pipeAlt-|Pipe each selection into shell command, ignoring outputshell_pipe_to!Run shell command, inserting output before each selectionshell_insert_outputAlt-!Run shell command, appending output after each selectionshell_append_output$Pipe each selection into shell command, keep selections where command returned 0shell_keep_pipe

### Selection manipulation

KeyDescriptionCommandsSelect all regex matches inside selectionsselect_regexSSplit selection into sub selections on regex matchessplit_selectionAlt-sSplit selection on newlinessplit_selection_on_newlineAlt-minusMerge selectionsmerge_selectionsAlt-_Merge consecutive selectionsmerge_consecutive_selections&Align selection in columnsalign_selections_Trim whitespace from the selectiontrim_selections;Collapse selection onto a single cursorcollapse_selectionAlt-;Flip selection cursor and anchorflip_selectionsAlt-:Ensures the selection is in forward directionensure_selections_forward,Keep only the primary selectionkeep_primary_selectionAlt-,Remove the primary selectionremove_primary_selectionCCopy selection onto the next line (Add cursor below)copy_selection_on_next_lineAlt-CCopy selection onto the previous line (Add cursor above)copy_selection_on_prev_line(Rotate main selection backwardrotate_selections_backward)Rotate main selection forwardrotate_selections_forwardAlt-(Rotate selection contents backwardrotate_selection_contents_backwardAlt-)Rotate selection contents forwardrotate_selection_contents_forward%Select entire fileselect_allxSelect current line, if already selected, extend to next lineextend_line_belowXExtend selection to line bounds (line-wise selection)extend_to_line_boundsAlt-xShrink selection to line bounds (line-wise selection)shrink_to_line_boundsJJoin lines inside selectionjoin_selectionsAlt-JJoin lines inside selection and select the inserted spacejoin_selections_spaceKKeep selections matching the regexkeep_selectionsAlt-KRemove selections matching the regexremove_selectionsCtrl-cComment/uncomment the selectionstoggle_commentsAlt-o,Alt-upExpand selection to parent syntax node (TS)expand_selectionAlt-i,Alt-downShrink syntax tree object selection (TS)shrink_selectionAlt-p,Alt-leftSelect previous sibling node in syntax tree (TS)select_prev_siblingAlt-n,Alt-rightSelect next sibling node in syntax tree (TS)select_next_siblingAlt-aSelect all sibling nodes in syntax tree (TS)select_all_siblingsAlt-I,Alt-Shift-downSelect all children nodes in syntax tree (TS)select_all_childrenAlt-eMove to end of parent node in syntax tree (TS)move_parent_node_endAlt-bMove to start of parent node in syntax tree (TS)move_parent_node_start

### Search

Search commands all operate on the/register by default. To use a different register, use"<char>.
KeyDescriptionCommand/Search for regex patternsearch?Search for previous patternrsearchnSelect next search matchsearch_nextNSelect previous search matchsearch_prev*Use current selection as the search pattern, automatically wrapping with\bon word boundariessearch_selection_detect_word_boundariesAlt-*Use current selection as the search patternsearch_selection

### Minor modes

These sub-modes are accessible from normal mode and typically switch back to normal mode after a command.
KeyDescriptionCommandvEnterselect (extend) modeselect_modegEntergoto modeN/AmEntermatch modeN/A:Enter command modecommand_modezEnterview modeN/AZEnter stickyview modeN/ACtrl-wEnterwindow modeN/ASpaceEnterspace modeN/A
These modes (except command mode) can be configured byremapping keys.

#### View mode

Accessed by typingzinnormal mode.
View mode is intended for scrolling and manipulating the view without changing
the selection. The "sticky" variant of this mode (accessed by typingZin
normal mode) is persistent and can be exited using the escape key. This is
useful when you're simply looking over text and not actively editing it.
KeyDescriptionCommandz,cVertically center the linealign_view_centertAlign the line to the top of the screenalign_view_topbAlign the line to the bottom of the screenalign_view_bottommAlign the line to the middle of the screen (horizontally)align_view_middlej,downScroll the view downwardsscroll_downk,upScroll the view upwardsscroll_upCtrl-f,PageDownMove page downpage_downCtrl-b,PageUpMove page uppage_upCtrl-uMove cursor and page half page uppage_cursor_half_upCtrl-dMove cursor and page half page downpage_cursor_half_down

#### Goto mode

Accessed by typingginnormal mode.
Jumps to various locations.
KeyDescriptionCommandgGo to line number<n>else start of filegoto_file_start|Go to column number<n>else start of linegoto_columneGo to the end of the filegoto_last_linefGo to files in the selectionsgoto_filehGo to the start of the linegoto_line_startlGo to the end of the linegoto_line_endsGo to first non-whitespace character of the linegoto_first_nonwhitespacetGo to the top of the screengoto_window_topcGo to the middle of the screengoto_window_centerbGo to the bottom of the screengoto_window_bottomdGo to definition (LSP)goto_definitionyGo to type definition (LSP)goto_type_definitionrGo to references (LSP)goto_referenceiGo to implementation (LSP)goto_implementationaGo to the last accessed/alternate filegoto_last_accessed_filemGo to the last modified/alternate filegoto_last_modified_filenGo to next buffergoto_next_bufferpGo to previous buffergoto_previous_buffer.Go to last modification in current filegoto_last_modificationjMove down textual (instead of visual) linemove_line_downkMove up textual (instead of visual) linemove_line_upwShow labels at each word and select the word that belongs to the entered labelsgoto_word

#### Match mode

Accessed by typingminnormal mode.
Please refer to the relevant sections for detailed explanations aboutsurroundandtextobjects.
KeyDescriptionCommandmGoto matching bracket (TS)match_bracketss<char>Surround current selection with<char>surround_addr<from><to>Replace surround character<from>with<to>surround_replaced<char>Delete surround character<char>surround_deletea<object>Select around textobjectselect_textobject_aroundi<object>Select inside textobjectselect_textobject_inner
TODO: Mappings for selecting syntax nodes (a superset of[).

#### Window mode

Accessed by typingCtrl-winnormal mode.
This layer is similar to Vim keybindings as Kakoune does not support windows.
KeyDescriptionCommandw,Ctrl-wSwitch to next windowrotate_viewv,Ctrl-vVertical right splitvsplits,Ctrl-sHorizontal bottom splithsplitfGo to files in the selections in horizontal splitsgoto_fileFGo to files in the selections in vertical splitsgoto_fileh,Ctrl-h,LeftMove to left splitjump_view_leftj,Ctrl-j,DownMove to split belowjump_view_downk,Ctrl-k,UpMove to split abovejump_view_upl,Ctrl-l,RightMove to right splitjump_view_rightq,Ctrl-qClose current windowwcloseo,Ctrl-oOnly keep the current window, closing all the otherswonlyHSwap window to the leftswap_view_leftJSwap window downwardsswap_view_downKSwap window upwardsswap_view_upLSwap window to the rightswap_view_right

#### Space mode

Accessed by typingSpaceinnormal mode.
This layer is a kludge of mappings, mostly pickers.
KeyDescriptionCommandfOpen file picker at LSP workspace rootfile_pickerFOpen file picker at current working directoryfile_picker_in_current_directorybOpen buffer pickerbuffer_pickerjOpen jumplist pickerjumplist_pickergOpen changed file pickerchanged_file_pickerGDebug (experimental)N/AkShow documentation for item under cursor in apopup(LSP)hoversOpen document symbol picker (LSP)symbol_pickerSOpen workspace symbol picker (LSP)workspace_symbol_pickerdOpen document diagnostics picker (LSP)diagnostics_pickerDOpen workspace diagnostics picker (LSP)workspace_diagnostics_pickerrRename symbol (LSP)rename_symbolaApply code action (LSP)code_actionhSelect symbol references (LSP)select_references_to_symbol_under_cursor'Open last fuzzy pickerlast_pickerwEnterwindow modeN/AcComment/uncomment selectionstoggle_commentsCBlock comment/uncomment selectionstoggle_block_commentsAlt-cLine comment/uncomment selectionstoggle_line_commentspPaste system clipboard after selectionspaste_clipboard_afterPPaste system clipboard before selectionspaste_clipboard_beforeyYank selections to clipboardyank_to_clipboardYYank main selection to clipboardyank_main_selection_to_clipboardRReplace selections by clipboard contentsreplace_selections_with_clipboard/Global search in workspace folderglobal_search?Open command palettecommand_palette
> 💡 Global search displays results in a fuzzy picker, useSpace + 'to bring it back up after opening a file.

##### Popup

Displays documentation for item under cursor. Remapping currently not supported.
KeyDescriptionCtrl-uScroll upCtrl-dScroll down

##### Completion Menu

Displays documentation for the selected completion item. Remapping currently not supported.
KeyDescriptionShift-Tab,Ctrl-p,UpPrevious entryTab,Ctrl-n,DownNext entryEnterClose menu and accept completionCtrl-cClose menu and reject completion
Any other keypresses result in the completion being accepted.

##### Signature-help Popup

Displays the signature of the selected completion item. Remapping currently not supported.
KeyDescriptionAlt-pPrevious signatureAlt-nNext signature

#### Unimpaired

These mappings are in the style ofvim-unimpaired.
KeyDescriptionCommand]dGo to next diagnostic (LSP)goto_next_diag[dGo to previous diagnostic (LSP)goto_prev_diag]DGo to last diagnostic in document (LSP)goto_last_diag[DGo to first diagnostic in document (LSP)goto_first_diag]fGo to next function (TS)goto_next_function[fGo to previous function (TS)goto_prev_function]tGo to next type definition (TS)goto_next_class[tGo to previous type definition (TS)goto_prev_class]aGo to next argument/parameter (TS)goto_next_parameter[aGo to previous argument/parameter (TS)goto_prev_parameter]cGo to next comment (TS)goto_next_comment[cGo to previous comment (TS)goto_prev_comment]TGo to next test (TS)goto_next_test[TGo to previous test (TS)goto_prev_test]pGo to next paragraphgoto_next_paragraph[pGo to previous paragraphgoto_prev_paragraph]gGo to next changegoto_next_change[gGo to previous changegoto_prev_change]GGo to last changegoto_last_change[GGo to first changegoto_first_change]SpaceAdd newline belowadd_newline_below[SpaceAdd newline aboveadd_newline_above

## Insert mode

Accessed by typingiinnormal mode.
Insert mode bindings are minimal by default. Helix is designed to
be a modal editor, and this is reflected in the user experience and internal
mechanics. Changes to the text are only saved for undos when
escaping from insert mode to normal mode.
> 💡 New users are strongly encouraged to learn the modal editing paradigm
to get the smoothest experience.
KeyDescriptionCommandEscapeSwitch to normal modenormal_modeCtrl-sCommit undo checkpointcommit_undo_checkpointCtrl-xAutocompletecompletionCtrl-rInsert a register contentinsert_registerCtrl-w,Alt-BackspaceDelete previous worddelete_word_backwardAlt-d,Alt-DeleteDelete next worddelete_word_forwardCtrl-uDelete to start of linekill_to_line_startCtrl-kDelete to end of linekill_to_line_endCtrl-h,Backspace,Shift-BackspaceDelete previous chardelete_char_backwardCtrl-d,DeleteDelete next chardelete_char_forwardCtrl-j,EnterInsert new lineinsert_newline
These keys are not recommended, but are included for new users less familiar
with modal editors.
KeyDescriptionCommandUpMove to previous linemove_line_upDownMove to next linemove_line_downLeftBackward a charmove_char_leftRightForward a charmove_char_rightPageUpMove one page uppage_upPageDownMove one page downpage_downHomeMove to line startgoto_line_startEndMove to line endgoto_line_end_newline
As you become more comfortable with modal editing, you may want to disable some
insert mode bindings. You can do this by editing yourconfig.tomlfile.

```
[keys.insert]
up = "no_op"
down = "no_op"
left = "no_op"
right = "no_op"
pageup = "no_op"
pagedown = "no_op"
home = "no_op"
end = "no_op"
```

## Select / extend mode

Accessed by typingvinnormal mode.
Select mode echoes Normal mode, but changes any movements to extend
selections rather than replace them. Goto motions are also changed to
extend, so thatvgl, for example, extends the selection to the end of
the line.
Search is also affected. By default,nandNwill remove the current
selection and select the next instance of the search term. Toggling this
mode before pressingnorNmakes it possible to keep the current
selection. Toggling it on and off during your iterative searching allows
you to selectively add search terms to your selections.

## Picker

Keys to use within picker. Remapping currently not supported.
See the documentation page onpickersfor more info.Promptkeybinds also work in pickers, except where they conflict with picker keybinds.
KeyDescriptionShift-Tab,Up,Ctrl-pPrevious entryTab,Down,Ctrl-nNext entryPageUp,Ctrl-uPage upPageDown,Ctrl-dPage downHomeGo to first entryEndGo to last entryEnterOpen selectedAlt-EnterOpen selected in the background without closing the pickerCtrl-sOpen horizontallyCtrl-vOpen verticallyCtrl-tToggle previewEscape,Ctrl-cClose picker

## Prompt

Keys to use within prompt, Remapping currently not supported.
KeyDescriptionEscape,Ctrl-cClose promptAlt-b,Ctrl-LeftBackward a wordCtrl-b,LeftBackward a charAlt-f,Ctrl-RightForward a wordCtrl-f,RightForward a charCtrl-e,EndMove prompt endCtrl-a,HomeMove prompt startCtrl-w,Alt-Backspace,Ctrl-BackspaceDelete previous wordAlt-d,Alt-Delete,Ctrl-DeleteDelete next wordCtrl-uDelete to start of lineCtrl-kDelete to end of lineBackspace,Ctrl-h,Shift-BackspaceDelete previous charDelete,Ctrl-dDelete next charCtrl-sInsert a word under doc cursor, may be changed to Ctrl-r Ctrl-w laterCtrl-p,UpSelect previous historyCtrl-n,DownSelect next historyCtrl-rInsert the content of the register selected by following input charTabSelect next completion itemBackTabSelect previous completion itemEnterOpen selected
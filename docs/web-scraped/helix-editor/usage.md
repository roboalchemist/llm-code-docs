# Source: https://docs.helix-editor.com/usage.html

# Using Helix

For a full interactive introduction to Helix, refer to thetutorwhich
can be accessed via the commandhx --tutoror:tutor.
> 💡 Currently, not all functionality is fully documented, please refer to thekey mappingslist.

## Modes

Helix is a modal editor, meaning it has different modes for different tasks. The main modes are:
- Normal mode: For navigation and editing commands. This is the default mode.
- Insert mode: For typing text directly into the document. Access by typingiin normal mode.
- Select/extend mode: For making selections and performing operations on them. Access by typingvin normal mode.

## Buffers

Buffers are in-memory representations of files. You can have multiple buffers open at once. Usepickersor commands like:buffer-nextand:buffer-previousto open buffers or switch between them.

## Selection-first editing

Inspired byKakoune, Helix follows theselection → actionmodel. This means that whatever you are going to act on (a word, a paragraph, a line, etc.) is selected first and the action itself (delete, change, yank, etc.) comes second. A cursor is simply a single width selection.

## Multiple selections

Also inspired by Kakoune, multiple selections are a core mode of interaction in Helix. For example, the standard way of replacing multiple instances of a word is to first select all instances (so there is one selection per instance) and then use the change action (c) to edit them all at the same time.

## Motions

Motions are commands that move the cursor or modify selections. They're used for navigation and text manipulation. Examples includewto move to the next word, orfto find a character. See theMovementsection of the keymap for more motions.
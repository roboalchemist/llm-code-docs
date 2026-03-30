### Overview ¶

Package histutil provides utilities for working with command history.

### Index ¶

- Variables

-
          type Cursor

-

-
            func NewDedupCursor(c Cursor) Cursor

-
          type DB

-
          type FaultyInMemoryDB

-

-
            func NewFaultyInMemoryDB(cmds ...string) FaultyInMemoryDB

-
          type Store

-

-
            func NewDBStore(db DB) (Store, error)

-
            func NewHybridStore(db DB) (Store, error)

-
            func NewMemStore(texts ...string) Store

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var ErrEndOfHistory = errors.New("end of history")
```

ErrEndOfHistory is returned by Cursor.Get if the cursor is currently over the
edge.

### Functions ¶

This section is empty.

### Types ¶

####

      type Cursor ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
type Cursor interface {
 // Prev moves the cursor to the previous command.
 Prev()
 // Next moves the cursor to the next command.
 Next()
 // Get returns the command the cursor is currently at, or any error if the
 // cursor is in an invalid state. If the cursor is "over the edge", the
 // error is ErrEndOfHistory.
 Get() (store.Cmd, error)
}
```

Cursor is used to navigate a Store.

####

      func NewDedupCursor ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func NewDedupCursor(c Cursor) Cursor
```

NewDedupCursor returns a cursor that skips over all duplicate entries.

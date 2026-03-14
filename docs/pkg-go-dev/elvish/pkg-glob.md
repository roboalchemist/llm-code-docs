### Overview ¶

Package glob implements globbing for elvish.

### Index ¶

- Constants

-
        func Glob(p string, cb func(PathInfo) bool) bool

-
        func IsLiteral(seg Segment) bool

-
        func IsSlash(seg Segment) bool

-
        func IsWild(seg Segment) bool

-
        func IsWild1(seg Segment, t WildType) bool

-
        func IsWild2(seg Segment, t1, t2 WildType) bool

-
          type Literal

-
          type PathInfo

-
          type Pattern

-

-
            func Parse(s string) Pattern

-

-
            func (p Pattern) Glob(cb func(PathInfo) bool) bool

-
          type Segment

-
          type Slash

-
          type Wild

-

-
            func (w Wild) Match(r rune) bool

-
          type WildType

### Constants ¶

      View Source
      

```
const (
 Question = iota
 Star
 StarStar
)
```

Values for WildType.

### Variables ¶

This section is empty.

### Functions ¶

####

      func Glob ¶
  
    
  

    
    
      

```
func Glob(p string, cb func(PathInfo) bool) bool
```

Glob returns a list of file names satisfying the given pattern.

####

      func IsLiteral ¶
  
    
  

    
    
      

```
func IsLiteral(seg Segment) bool
```

IsLiteral returns whether a Segment is a Literal.

####

      func IsSlash ¶
  
    
  

    
    
      

```
func IsSlash(seg Segment) bool
```

IsSlash returns whether a Segment is a Slash.

####

      func IsWild ¶
  
    
  

    
    
      

```
func IsWild(seg Segment) bool
```

IsWild returns whether a Segment is a Wild.

####

      func IsWild1 ¶
  
    
  

    
    
      

```
func IsWild1(seg Segment, t WildType) bool
```

IsWild1 returns whether a Segment is a Wild and has the specified type.

####

      func IsWild2 ¶
  
    
  

    
    
      

```
func IsWild2(seg Segment, t1, t2 WildType) bool
```

IsWild2 returns whether a Segment is a Wild and has one of the two specified
types.

### Types ¶

####

      type Literal ¶
  
    
  

    
    
      

```
type Literal struct {
 Data string
}
```

Literal is a series of non-slash, non-wildcard characters, that is to be
matched literally.

####

      type PathInfo ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
type PathInfo struct {
 // The generated path, consistent with the original glob pattern. It cannot
 // be replaced by Info.Name(), which is just the final path component.
 Path string
 Info os.FileInfo
}
```

PathInfo keeps a path resulting from glob expansion and its FileInfo. The
FileInfo is useful for efficiently determining if a given pathname satisfies
a particular constraint without doing an extra stat.

####

      type Pattern ¶
  
    
  

    
    
      

```
type Pattern struct {
 Segments    []Segment
 DirOverride string
}
```

Pattern is a glob pattern.

####

      func Parse ¶
  
    
  

    
    
      

```
func Parse(s string) Pattern
```

Parse parses a pattern.

####

      func (Pattern) Glob ¶
  
    
  

    
    
      

```
func (p Pattern) Glob(cb func(PathInfo) bool) bool
```

Glob returns a list of file names satisfying the Pattern.

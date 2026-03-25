spdx::lexer
# Struct LexerToken 
Source 

```
pub struct LexerToken<'a> {
    pub token: Token<'a>,
    pub span: Range<usize>,
}
```

## Fields§
§`token: Token<'a>`

The token that was lexed
§`span: Range<usize>`

The range of the token characters in the original license expression

## Trait Implementations§
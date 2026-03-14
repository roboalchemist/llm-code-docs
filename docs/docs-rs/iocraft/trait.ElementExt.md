iocraft
# Trait ElementExt 
Source 

```
pub trait ElementExt: Sealed + Sized {
    // Required methods
    fn key(&self) -> &ElementKey;
    fn render(&mut self, max_width: Option<usize>) -> Canvas;

    // Provided methods
    fn to_string(&mut self) -> String { ... }
    fn print(&mut self) { ... }
    fn eprint(&mut self) { ... }
    fn write<W: Write>(&mut self, w: W) -> Result<()> { ... }
    fn write_to_raw_fd<F: Write + AsRawFd>(&mut self, fd: F) -> Result<()> { ... }
    fn write_to_is_terminal<W: Write + IsTerminal>(
        &mut self,
        w: W,
    ) -> Result<()> { ... }
    fn render_loop(&mut self) -> RenderLoopFuture<'_, Self> ⓘ { ... }
    fn mock_terminal_render_loop(
        &mut self,
        config: MockTerminalConfig,
    ) -> impl Stream<Item = Canvas> { ... }
    fn fullscreen(&mut self) -> RenderLoopFuture<'_, Self> ⓘ { ... }
}
```

## Required Methods§
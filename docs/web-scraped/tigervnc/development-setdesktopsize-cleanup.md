# Source: https://github.com/TigerVNC/tigervnc/wiki/Development:-SetDesktopSize-Cleanup

Right now the SetDesktopSize call (and equivalents from X11) are causing multiple ExtendedDesktopSize to be emitted to the client, even though one would be sufficient. This is not currently a practical problem, but it is inefficient and might cause problems down the road.

The call chain shown below describes the flow of calls when we get either a SetDesktopSize from a VNC client, or when a X11 client uses RandR. If you follow the calls, you\'ll notice that we end up in writeExtendedDesktopSize() multiple times. We need to figure out an architecture that avoids this problem.

|   |                                  /|
|   | 1                               / |
|   |                                 | |
|   \\-> setScreenLayout()             | \\-> ??()
|       |     |                       |     |
| 2     | 1   \\-----------------------+-----\\-> setScreenLayout()
|       |                             |         |
|       \\-> RRSetConfig()             |         \\-> screenLayoutChanged()
|           |                         |                       |
|           \\-> vncRandRSetConfig() <-/                       |
|               |                                             |
|               \\-> setFrameBuffer()                          |
|                   |                                         |
|                   \\-> setPB()                               |
|                       |                                     |
|                       \\-> pixelBufferChanged()              |
|                           |                                 |
\\---------------------------\\-> writeExtendedDesktopSize()<---/"}
``` notranslate
SetDesktopSize                          X11
|   |                                  /|
|   | 1                               / |
|   |                                 | |
|   \-> setScreenLayout()             | \-> ??()
|       |     |                       |     |
| 2     | 1   \-----------------------+-----\-> setScreenLayout()
|       |                             |         |
|       \-> RRSetConfig()             |         \-> screenLayoutChanged()
|           |                         |                       |
|           \-> vncRandRSetConfig() <-/                       |
|               |                                             |
|               \-> setFrameBuffer()                          |
|                   |                                         |
|                   \-> setPB()                               |
|                       |                                     |
|                       \-> pixelBufferChanged()              |
|                           |                                 |
\---------------------------\-> writeExtendedDesktopSize()<---/
```

The wiki is read-only because of malware spam that GitHub refuses to provide protection agains. Contact the maintainers directly with changes you\'d like to make.
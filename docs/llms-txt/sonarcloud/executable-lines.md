# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/developing-a-plugin/executable-lines.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/executable-lines.md

# Executable lines

These are the guidelines that Sonar uses internally when defining executable lines for a language. Community plugins are not required to adhere to these guidelines. They are provided here only in case they are useful.

### Things that are executable <a href="#things-that-are-executable" id="things-that-are-executable"></a>

Executable lines data is used to calculate missing test coverage for files that are not included in coverage reports. Ideally, executable line counts will be at or just under what coverage engines would calculate.

Generally, each line containing a statement should count as an executable line, with the exception that compound statements ({}) are ignored, although their contents are not. So, for example:

```css-79elbk
void doTheThing ()        // +0
{                         // +0
  String fname="Finn";    // +1
  etc();                  // +1
}                         // +0
```

### Things that are ignored <a href="#things-that-are-ignored" id="things-that-are-ignored"></a>

#### !Statement: +0 <a href="#statement-0" id="statement-0"></a>

Since some coverage engines mark these things as executable, it’s worth stating explicitly that we will ignore them:

* lines containing only punctuation.
* the method signature of a method definition.

#### Imports, Declarations: +0 <a href="#imports-declarations-0" id="imports-declarations-0"></a>

Imports, package and namespace statements, declarations, and a few other things demonstrated below are ignored.

```css-79elbk
package foo;     // +0
namespace bar {  // +0
  ...
}
  
import java.util.ArrayList;  // +0
#include <stdio>             // +0
  
public interface FooFace {  // +0
  void doFoo();             // +0
}
public class Foo1 implements FooFace {  // +0
  private String name;                  // +0
}
struct PairWithOperator { // +0
  int x;                  // +0
  int y;                  // +0
  
  bool operator==(PairWithOperator rhs) const {  // +0
    return x == rhs.x && y == rhs.y;             // +1
  }
}
  
class C {
  C(const C&) =default;  // +0 (explicit inheritance of parent method)
}
 
using Vec = std::vector<T,MyAllocator<T>>;       // +0
  
static {                 // +0
  ...
}
 
01  ERROR-MESSAGE.                                      *> +0
        02  ERROR-TEXT  PIC X(132) OCCURS 10 TIMES      *> +0
                                   INDEXED BY ERROR-INDEX.
77  ERROR-TEXT-LEN      PIC S9(9)  COMP VALUE +132.     *> +0
```

#### Location <a href="#location" id="location"></a>

The presence of executable code on a line makes the entire line executable. If a statement is split over multiple lines, the line to be marked executable is the first one with executable code. Given that, a `for` loop is considered executable:

```css-79elbk
for         // +1
  (         // +0
   int i=0; // +0
   i < 10;  // +0
   i++      // +0
  )         // +0
{           // +0
}
```

Regardless of the number of lines across which nested statements are spread, the executable line count should only be incremented by one, since typically the execution of one naturally follows from the other.

```css-79elbk
foo(1, bar());  // +1
foo(1,          // +1
    bar());     // +0
```

We ignore here the possibility that `bar()` could throw an exception, preventing `foo` from being executed.

### Exceptions <a href="#exceptions" id="exceptions"></a>

#### Python <a href="#python" id="python"></a>

`# pragma: no cover` exempts a block from coverage. For example:

![Exempt a block of Python code from coverage](https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/kvatwdMvm6wnwmwgfXwo/9801c7fc496d5d2181ecff3ec24703b0685513dd.png)

Exempt a block of Python code from coverage

#### JavaScript <a href="#javascript" id="javascript"></a>

We mark variable declarations as executable. For example:

```css-79elbk
var a;  // +1
```

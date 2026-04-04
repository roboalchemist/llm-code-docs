# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/clean-code/definition.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/clean-code/definition.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/clean-code/definition.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-code/definition.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/definition.md

# Clean Code definition

We define Clean Code as code that has the following attributes: consistency, intentionality, adaptability, and responsibility.

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-0e61ea1b649a8f4c8e5bc09da7604737e61a5a17%2Fb7517b3ce586e9cba105b12a5726c14dccf82bda.png?alt=media)

### Consistency <a href="#consistency" id="consistency"></a>

The code is written in a uniform and conventional way. All the code looks similar and follows a regular pattern, even with multiple contributors at different times.

Consistent code is formatted, conventional, and identifiable.

#### Formatted <a href="#formatted" id="formatted"></a>

The code presentation is systematic and regular. Non-semantic choices, such as spacing, indentation, and character placement, remain consistent throughout the codebase, maintaining uniformity across files and authors.

<details>

<summary>Example</summary>

The example below shows inconsistent indentation in Java code. It’s not about tabs versus spaces, it’s about consistency.

**Non-compliant code**

```css-79elbk
class Foo {

  public int a;

    public int b;

  public void doSomething() {

    if(something) {

          doSomethingElse();

  }

  }

}
```

**Compliant code**

```css-79elbk
class Foo {

  public int a;

  public int b;

  public void doSomething() {

    if(something) {

      doSomethingElse();

    }

  }

}
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/java/RSPEC-1120).

</details>

#### Conventional <a href="#conventional" id="conventional"></a>

The code performs tasks with expected instructions. Faced with equally good options, the code adheres to a single choice across all instances, preferring language conventions. This includes using the appropriate programming interfaces and language features.

<details>

<summary>Example</summary>

In C++ from version 11, ​​type aliases can be declared via either **`typedef`** or **`using`**, however, you should prefer the latter for modern code.

**Non-compliant code**

```css-79elbk
typedef void (*FunctionPointerType)(int);
```

**Compliant code**

```css-79elbk
using FunctionPointerType = void (*)(int);
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/cpp/RSPEC-5416/).

</details>

#### Identifiable <a href="#identifiable" id="identifiable"></a>

The names follow a regular structure based on language conventions. The casing, word separators, suffixes, and prefixes used in the identifiers have purpose, without arbitrary differences.

<details>

<summary>Example</summary>

Consider code written in C#, where PascalCase is used for all identifiers except parameter names. In this context, using underscores or other casing styles to differentiate words in an identifier is unacceptable.

**Non-compliant code**

```css-79elbk
class my_class {...}
class SOMEName {...}
```

**Compliant code**

```css-79elbk
class MyClass {...}
class SomeName {...}
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/csharp/RSPEC-101/).

</details>

### Intentionality <a href="#intentionality" id="intentionality"></a>

The code is precise and purposeful. Every instruction makes sense, is adequately formed, and clearly communicates its behavior.

Intentional code is clear, logical, complete, and efficient.

#### Clear <a href="#clear" id="clear"></a>

The code is self-explanatory, transparently communicating its functionality. It is written in a straightforward way that minimizes ambiguity, avoiding unnecessary clever or intricate solutions.

<details>

<summary>Example</summary>

In the non-compliant example of Python code below, and you’ll notice that variables **`message`** and **`i`** are defined but never used. When readers encounter such cases, they might wonder if it’s a coding error that was supposed to do something else or if it’s just leftover code that can be safely deleted.

**Non-compliant code**

```css-79elbk
def hello(name):
    message = "Hello " + name
    print(name)
for i in range(10):
    foo()
```

**Compliant code**

```css-79elbk
def hello(name):
    message = "Hello " + name
    print(message)
for _ in range(10):
    foo()
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/python/RSPEC-1481/).

</details>

#### Logical <a href="#logical" id="logical"></a>

The code has well-formed and sound instructions that work together. It is free of explicit errors, contradictions, and commands that could be unpredictable or objectionable.

<details>

<summary>Example</summary>

In JavaScript, there’s **`NaN`**, which stands for Not-a-Number. It represents a numeric data type that isn’t a valid number. **`NaN`** is not equal to any value, even itself, and this behavior can lead to unexpected results.

**Non-compliant code**

```css-79elbk
if (a !== NaN) {

  console.log("this is always logged");

}
```

**Compliant code**

```css-79elbk
if (!isNaN(a)) {

  console.log("a is not NaN");

}
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/javascript/RSPEC-2688/).

</details>

#### Complete <a href="#complete" id="complete"></a>

The code constructs are comprehensive and used adequately and thoroughly. The code is functional and achieves its implied goals. There are no obviously incomplete or lacking solutions.

<details>

<summary>Example</summary>

An example in PHP is the use of secure cookies. The method **`setcookie`** allows you to create cookies that can be transmitted via HTTP by default, making their contents readable. Since cookies often carry sensitive data, it’s important to ensure they are transferred securely to fulfill their intended purpose. You need to pass a last argument to enable HTTPS only.

**Non-compliant code**

```css-79elbk
$value = "sensitive data";

setcookie($name, $value, $expire, $path, $domain);
```

**Compliant code**

```css-79elbk
$value = "sensitive data";

setcookie($name, $value, $expire, $path, $domain, true);
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/php/RSPEC-2092).

</details>

#### Efficient <a href="#efficient" id="efficient"></a>

The code uses resources without needless waste. It prioritizes economical options when available, avoiding unnecessary consumption of memory, processor, disk, or network resources.

<details>

<summary>Example</summary>

Most Linux package managers create a cache by default when working with Docker. Unless you remember to remove these files in your Dockerfile, they will increase the size of your image without providing any additional value.

**Non-compliant code**

```css-79elbk
RUN apt-get update \
  && apt-get install nginx
```

**Compliant code**

```css-79elbk
RUN apt-get update \
  && apt-get install nginx \
  && apt-get clean
```

</details>

### Adaptability <a href="#adaptability" id="adaptability"></a>

The code is structured to be easy to evolve and develop with confidence. It makes extending or repurposing its parts easy and promotes localized changes without undesirable side-effects.

Adaptable code is focused, distinct, modular, and tested.

#### Focused <a href="#focused" id="focused"></a>

The code has a single, narrow, and specific scope. Each unit should have only one concise purpose, without an overwhelming accumulation of instructions or excessive amounts of complexity.

<details>

<summary>Example</summary>

In Swift, it’s best practice to keep types, such as classes, in separate files. This helps prevent an excessive accumulation of instructions or an overwhelming amount of complexity within a single file.

**Non-compliant code**

```css-79elbk
class MyViewController: UIViewController {
  // …
}
extension MyViewController: UIScrollViewDelegate {
  // …
}
class UnrelatedController: UIViewController {
  // …
}
```

**Compliant code**

```css-79elbk
class MyViewController: UIViewController {
  // …
}
extension MyViewController: UIScrollViewDelegate {
  // …
}
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/swift/RSPEC-1996).

</details>

#### Distinct <a href="#distinct" id="distinct"></a>

The code procedures and data are unique and distinctive, without undue duplication. The codebase has no significant repetition where it could be decomposed into smaller shared segments.

<details>

<summary>Example</summary>

Duplicating string literals raises the risk of errors when making updates since each occurrence must be changed separately. A better approach is to use constants that can be referenced from multiple places, allowing updates to be made in a single location. Here’s an example using Ruby.

**Non-compliant code**

```css-79elbk
def foo()
  prepare('action random1')
  execute('action random1')
  release('action random1')
end
```

**Compliant code**

```css-79elbk
def foo()
  action1 = 'action random1'
  prepare(action1)
  execute(action1)
  release(action1)
end
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/ruby/RSPEC-1192).

</details>

#### Modular <a href="#modular" id="modular"></a>

The code has been organized and distributed to emphasize the separation between its parts. The relationships within the code are carefully managed, ensuring they are minimal and clearly defined.

<details>

<summary>Example</summary>

A key aspect of this is encapsulation. In Object-Oriented languages, encapsulation often involves making fields private. This way, the class retains control over the details of its internal representation and prevents other parts of the code from having too much knowledge about its inner workings.

However, there are multiple levels of encapsulation, and even minor improvements can make a difference. For example, if you’re working with VB.Net, which allows publicly accessible fields, it’s better to avoid using them and instead use properties. Properties work similarly to fields but are part of the interface and can be overridden by getters and setters.

**Non-compliant code**

```css-79elbk
Class Foo
    Public Bar = 42
End Class
```

**Compliant code**

```css-79elbk
Class Foo
    Public Property Bar = 42
End Class
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/vbnet/RSPEC-2357).

</details>

#### Tested <a href="#tested" id="tested"></a>

The code has automated checks that provide confidence in the functionality. It has enough test coverage which enables changes in implementation without the risk of functional regressions.

<details>

<summary>Examples</summary>

There are odd examples, where you have a test folder or test files, without actual test cases inside, which can mislead other developers. See the corresponding [Sonar rule](https://rules.sonarsource.com/csharp/RSPEC-2187/).

There are also cases where tests are skipped and accidentally committed like that, which might go unnoticed if not tracked in any way. See the corresponding [Sonar rule](https://rules.sonarsource.com/csharp/RSPEC-1607).

</details>

### Responsibility <a href="#responsibility" id="responsibility"></a>

The code takes into account its ethical obligations on data, as well as societal norms.

Responsible code is lawful, trustworthy, and respectful.

#### Lawful <a href="#lawful" id="lawful"></a>

The code respects licensing and copyright regulation. It exercises the creator’s rights and honors other’s rights to license their own code.

<details>

<summary>Example</summary>

One common example is companies enforcing copyright headers in their code files:

```css-79elbk
/*
 * SonarQube, open source software for clean code.
 * Copyright (C) 2008-2024 SonarSource
 * mailto:contact AT sonarsource DOT com
 *
 * SonarQube is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or (at your option) any later version.
 *
 * SonarQube is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/csharp/RSPEC-1451).

</details>

#### Trustworthy <a href="#trustworthy" id="trustworthy"></a>

The code abstains from revealing or hard-coding private information. It preserves sensitive private information such as credentials and personally identifying information.

<details>

<summary>Example</summary>

Below is a simplified example using Go.

**Non-compliant code**

```css-79elbk
func connect()  {
  user := "root"
  password:= "supersecret"

  url := "login=" + user + "&passwd=" + password
}
```

**Compliant code**

```css-79elbk
func connect()  {
  user := getEncryptedUser()
  password:= getEncryptedPass()

  url := "login=" + user + "&passwd=" + password
}
```

For more information, see the corresponding [Sonar rule](https://rules.sonarsource.com/go/RSPEC-2068).

</details>

#### Respectful <a href="#respectful" id="respectful"></a>

The code refrains from using discriminatory and offensive language. It chooses to prioritize inclusive terminology whenever an alternative exists that conveys the same meaning.

<details>

<summary>Example</summary>

**Non-compliant code**

```css-79elbk
Master / Slave
Blacklist / Whitelist
```

**Compliant code**

```css-79elbk
Primary / Secondary
Denylist / Allowlist
```

</details>

### Learn more <a href="#learn-more" id="learn-more"></a>

Check the [software-qualities](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/software-qualities "mention") page to better understand software qualities. On the [code-analysis](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/code-analysis "mention") page you can learn how Clean Code attributes and software qualities are impacted by your code issue.

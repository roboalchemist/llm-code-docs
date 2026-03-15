# Source: https://logbackcn.gitbook.io/logback/06-di-liu-zhang-layouts.md

# 第六章：Layouts

### 什么是 layout？

layout 是 logback 的组件，负责将日志事件转换为字符串。[`Layout`](https://logback.qos.ch/xref/ch/qos/logback/core/Layout.html) 接口中的 `format()` 方法接受一个表示日志事件的对象 (任何类型) 并返回一个字符串。`Layout` 接口的概要如下：

```java
public interface Layout<E> extends ContextAware, LifeCycle {

  String doLayout(E event);
  String getFileHeader();
  String getPresentationHeader();
  String getFileFooter();
  String getPresentationFooter();
  String getContentType();
}
```

这个接口相对简单，但是它可以满足大部分的格式化需求。

### Logback-classic

logback-classic 仅仅用来处理 [`ch.qos.logback.classic.spi.ILoggingEvent`](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/ILoggingEvent.html) 类型的日志事件。我们将在这个部分说明这个事实。

### 定制 Layout

让我们为 logback-classic 模块实现一个简单但是实用的功能，打印应用启动所耗费的时间，日志事件的级别，被综括号包裹的调用者线程，logger 名，破折号后面跟日志信息，以及新起一行。

类似下面的输出：

```java
10489 DEBUG [main] com.marsupial.Pouch - Hello world.
```

下面是一种可能的实现：

> Example: MySampleLayout.java

```java
package chapters.layouts;

import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.LayoutBase;

public class MySampleLayout extends LayoutBase<ILoggingEvent> {

  public String doLayout(ILoggingEvent event) {
    StringBuffer sbuf = new StringBuffer(128);
    sbuf.append(event.getTimeStamp() - event.getLoggingContextVO.getBirthTime());
    sbuf.append(" ");
    sbuf.append(event.getLevel());
    sbuf.append(" [");
    sbuf.append(event.getThreadName());
    sbuf.append("] ");
    sbuf.append(event.getLoggerName();
    sbuf.append(" - ");
    sbuf.append(event.getFormattedMessage());
    sbuf.append(CoreConstants.LINE_SEP);
    return sbuf.toString();
  }
}
```

`MySampleLayout` 继承自 [`LayoutBase`](https://logback.qos.ch/xref/ch/qos/logback/core/LayoutBase.html)。这个类管理所有 layout 实例的状态信息，例如：layout 是否启动或者停止，头部，尾部以及内容类型数据。它让开发者通过自己 `Layout` 集中在日志具体的格式化上。`LayoutBase` 类是通用的。在它的类声明上，`MySampleLayout` 继承 `LayoutBase<ILoggingEvent>`。

在上面这个例子中，`doLayout` 方法忽略了日志事件中任何可能的异常。在实际应用中，你可能需要打印异常信息。

#### 配置自定义的 layout

配置自定义的 layout 跟其它的组件一样的配置。根据之前提到的，`FileAppender` 及其子类期望一个 encoder。为了去满足这个需求，我们将一个包裹了我们自己定义的 `MySampleLayout` 的 `LayoutWrappingEncoder` 的实例传递给 `FileAppender`。下面是配置示例：

> Example: *sampleLayoutConfig.xml*

```markup
<configuration>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
      <layout class="chapters.layouts.MySampleLayout" />
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

[`chapters.layouts.SampleLogging`](https://logback.qos.ch/xref/chapters/layouts/SampleLogging.html) 这个简单的应用通过第一个参数接收配置文件，然后打印了一个 debug 信息，接着打印了 error 信息。

在 *logback-examples* 文件夹下通过以下命令来运行：

```bash
java chapters.layouts.SampleLogging src/main/java/chapters/layouts/sampleLayoutConfig.xml
```

将会输出：

```java
0 DEBUG [main] chapters.layouts.SampleLogging - Everything's going well
0 ERROR [main] chapters.layouts.SampleLogging - maybe not quite...
```

这种足够简单。读者应该会发现，在 [`MySampleLayout2.java`](https://logback.qos.ch/xref/chapters/layouts/MySampleLayout2.html) 中，我们自定义的 layout 做了一点点的修改。正如本手册一直提到的，为 layout 或者其它 logback 的组件添加一个属性，跟为这个属性添加一个 set 方法一样简单。

[`MySampleLayout2`](https://logback.qos.ch/xref/chapters/layouts/MySampleLayout2.html) 类包含了两个属性。第一个是可以将一个前缀添加到输出的日志中。第二个属性可以用来选择是否展示发送日志请求的线程名。

下面是 [`MySampleLayout2`](https://logback.qos.ch/xref/chapters/layouts/MySampleLayout2.html) 类：

```java
package chapters.layouts;

import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.LayoutBase;

public class MySampleLayout2 extends LayoutBase<ILoggingEvent> {

  String prefix = null;
  boolean printThreadName = true;

  public void setPrefix(String prefix) {
    this.prefix = prefix;
  }

  public void setPrintThreadName(boolean printThreadName) {
    this.printThreadName = printThreadName;
  }

  public String doLayout(ILoggingEvent event) {
    StringBuffer sbuf = new StringBuffer(128);
    if (prefix != null) {
      sbuf.append(prefix + ": ");
    }
    sbuf.append(event.getTimeStamp() - event.getLoggerContextVO().getBirthTime());
    sbuf.append(" ");
    sbuf.append(event.getLevel());
    if (printThreadName) {
      sbuf.append(" [");
      sbuf.append(event.getThreadName());
      sbuf.append("] ");
    } else {
      sbuf.append(" ");
    }
    sbuf.append(event.getLoggerName());
    sbuf.append(" - ");
    sbuf.append(event.getFormattedMessage());
    sbuf.append(LINE_SEP);
    return sbuf.toString();
  }
}
```

添加相应的 set 方法就可以开启属性的配置。`PrintThreadName` 属性是 `boolean` 而不是 `String` 类型。关于配置 logback 的详细信息请参见[第三章：logback 的配置](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md)。[第十一章](https://logback.qos.ch/manual/onJoran.html)将会提供更详细的内容。下面是关于 `MySampleLayout2` 的相关配置：

```markup
<configuration>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
      <layout class="chapters.layouts.MySampleLayout2"> 
        <prefix>MyPrefix</prefix>
        <printThreadName>false</printThreadName>
      </layout>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

### PatternLayout

logback 配备了一个更加灵活的 layout 叫做 [`PatternLayout`](https://logback.qos.ch/xref/ch/qos/logback/classic/PatternLayout.html)。跟所有的 layout 一样，`PatternLayout` 接收一个日志事件并返回一个字符串。但是，可以通过调整 `PatternLayout` 的转换模式来进行定制。

`PatternLayout` 中的转换模式与 C 语言中 `printf()` 方法中的转换模式密切相关。转换模式由字面量与格式控制表达式也叫*转换说明符*组成。你可以在转换模式中自由的插入字面量。每一个转换说明符由一个百分号开始 '%'，后面跟随可选的*格式修改器*，以及用综括号括起来的转换字符与可选的参数。转换字符需要转换的字段。如：logger 的名字，日志级别，日期以及线程名。格式修改器控制字段的宽度，间距以及左右对齐。

正如我们已经在其它地方提到过的，`FileAppender` 及其子类需要一个 encoder。因为，当将 `FileAppender` 及其子类与 `PatternLayout` 结合使用时，`PatternLayout` 必须用 encoder 包裹起来。鉴于 `FileAppender/PatternLayout` 结合使用很常见，因此 logback 单独设计了一个名叫 `PatternLayoutEncoder` 的 encoder，包裹了一个 `PatternLayout`，因此它可以被当作一个 encoder。下面是通过代码配置 `ConsoleAppender` 与 `PatternLayoutEncoder` 使用的例子：

> Example: [PatternSample.java](https://logback.qos.ch/xref/chapters/layouts/PatternSample.html)

```java
package chapters.layouts;

import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.Logger;
import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.classic.encoder.PatternLayoutEncoder;
import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.ConsoleAppender;

public class PatternSample {

  static public void main(String[] args) throws Exception {
    Logger rootLogger = (Logger)LoggerFactory.getLogger(Logger.ROOT_LOGGER_NAME);
    LoggerContext loggerContext = rootLogger.getLoggerContext();
    // we are not interested in auto-configuration
    loggerContext.reset();

    PatternLayoutEncoder encoder = new PatternLayoutEncoder();
    encoder.setContext(loggerContext);
    encoder.setPattern("%-5level [%thread]: %message%n");
    encoder.start();

    ConsoleAppender<ILoggingEvent> appender = new ConsoleAppender<ILoggingEvent>();
    appender.setContext(loggerContext);
    appender.setEncoder(encoder); 
    appender.start();

    rootLogger.addAppender(appender);

    rootLogger.debug("Message 1"); 
    rootLogger.warn("Message 2");
  } 
}
```

在上面这个例子中，转换模式被设置为 "**%-5level \[%thread]: %message%n** "，关于 logback 中简短的转换字符将会很快给出。运行 `PatternSample`：

```bash
java java chapters.layouts.PatternSample
```

将会输出如下信息：

```java
DEBUG [main]: Message 1 
WARN  [main]: Message 2
```

在转换模式 **"%-5level \[%thread]: %message%n"** 中，字面量与转换说明符之间没有明显的分隔符。当对转换模式进行解析的时候，`PatternLayout` 有能力对字面量 (空格符，方括号，冒号) 和 转换说明符进行区分。在上面的例子中，转换说明符 %-5level 表示日志事件的级别的字符应该向左对齐，保持五个字符的宽度。具体的转换格式将会在下面介绍。

在 `PatternLayout` 中，括号用于对转换模式进行分组。**'(' 与 ')' 有特殊的含义，因此如果想用作字面量，需要进行特殊的转义**。圆括号的特殊含义将在[下面](https://logback.qos.ch/manual/layouts.html#Parentheses) 进行详细的介绍。

之前提到过，特定的转换模式可以通过花括号指定可选的参数。一个简单的可选转换模式可以是 %logger{10}。在这里 "logger" 就是转换字符，10 就是可选参数。可选参将在[下面](https://logback.qos.ch/manual/layouts.html#cwOptions)详细介绍。

转换字符与它们的可选参数在下面的表格中进行详细叙述。当多个转换字符在同一个单元格中被列出来，它们被当作别名来考虑。

| 转换字符                                                                                                                                                                                                                                                                                                                                                                              | 效果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>c</strong>{<em>length</em>}<br><strong>lo</strong>{<em>length</em>}<br><strong>logger</strong>{<em>length</em>}</p>                                                                                                                                                                                                                                                    | <p>输出 logger 的名字作为日志事件的来源。转换字符接收一个作为它的第一个也是为一个参数。转换器的简写算法将会缩短 logger 的名字，但是通过不会丢失重要的信息。设置 length 的值为 0 是一个例外。它将会导致转换字符返回 logger 名字中最右边的点右边的字符。下面的表格提供了一个示例：<br>logger 名字最右边的部分永远不会被简写，即使它的长度比 <em>length</em> 的值要大。其它的部分可能会被缩短为一个字符，但是永不会被移除。<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <p><strong>C</strong>{<em>length</em>}  <br><strong>class</strong>{<em>length</em>}</p>                                                                                                                                                                                                                                                                                           | <p>输出发出日志请求的类的全限定名称。<br>跟 <em>%logger%</em> 转换符一样，它也可以接收一个整型的可选参数去缩短类名。0 表示特殊含义，在打印类名时将不会输出包的前缀名。默认表示打印类的全限定名。<br>生成调用者类的信息并不是特别快。因此，应该避免使用，除非执行速度不是问题。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <p><strong>contextName</strong><br><strong>cn</strong></p>                                                                                                                                                                                                                                                                                                                        | 输出日志事件附加到的 logger 上下文的名字。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **d**{*pattern*}  **date**{*pattern*}  **d**{*pattern*, *timezone*}  **date**{*pattern*, *timezone*}                                                                                                                                                                                                                                                                              | <p>用于输出日志事件的日期。日期转换符允许接收一个字符串作为参数。字符串的语法与 <a href="https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html">SimpleDateFormat</a> 中的格式完全兼容。<br>你可以指定 "ISO8601" 来表示将日期格式为 ISO8601 类型。如果没有指定日期格式，那么 %date 转换字符默认为 <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO860 类型</a>。<br>这里有一个例子。它假设当前时间为 2006.10.20 星期五，作者刚刚吃完饭准备写这篇文档。<br><br>第二个参数用于指定时区。例如， '%date{HH:mm:ss.SSS, Australia/Perth}' 将会打印世界上最孤立的城市，澳大利亚佩斯所在时区的日期。如果没有指定时区参数，则默认使用 Java 平台所在主机的时区。如果指定的时区不能识别或者拼写错误，则 \[TimeZone.getTimeZone(String)]\(<a href="http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html#getTimeZone(java.lang.String"><http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html#getTimeZone(java.lang.String></a>)) 方法会指定时区为 GMT。<br><code>常见错误：</code> 对于 <code>HH:mm:ss,SSS</code> 模式，逗号会被解析为分隔符，所以最终会被解析为 <code>HH:mm:ss</code>，<code>SSS</code> 会被当作时区。如果你想在日期模式中使用逗号，那么你可以这样使用，%date{<strong>"</strong>HH:mm:ss,SSS<strong>"</strong>}  用双引号将日期模式包裹起来。</p> |
| **F / file**                                                                                                                                                                                                                                                                                                                                                                      | <p>输出发出日志请求的 Java 源文件名。<br>由于生成文件的信息不是特别快，因此，应该避免使用，除非速度不是问题。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <p><strong>caller{depth}</strong><br><strong>caller{depthStart..depthEnd}</strong><br><strong>caller{depth, evaluator-1, ... evaluator-n}</strong><br><strong>caller{depthStart..depthEnd, evaluator-1, ... evaluator-n}</strong></p>                                                                                                                                             | <p>输出生成日志的调用者所在的位置信息。<br>位置信息依赖 JVM 的实现，但是通常由调用方法的全限定名以及调用者的来源组成。以及由圆括号括起来的文件名与行号。<br><em>caller</em> 转换符还可以接收一个整形的参数，用来配置展示信息的深度。<br>例如，<strong>%caller{2}</strong> 会展示如下的信息：<br> <strong>%caller{3}</strong>  会展示如下信息：<br><br><em>caller</em> 转换符还可以接收一个范围用来展示深度在这个范围内的信息。<br>例如，<strong>%caller{1..2}</strong> 会展示如下信息：<br><br>转换字符还可以接收一个 evaluator，在计算调用者数据之前通过指定的标准对日志事件进行测验。例如，<strong>%caller{3, CALLER\_DISPLAY\_EVAL}</strong> 会在 <em>CALLER\_DISPLAY\_EVAL</em> 返回一个肯定的答案，才会显示三行堆栈信息。<br>将在下面详细叙述 evaluator。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **L / line**                                                                                                                                                                                                                                                                                                                                                                      | <p>输出发出日志请求所在的行号。<br>生成行号不是特别快。因此，不建议使用，除非生成速度不是问题。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **m / msg / message**                                                                                                                                                                                                                                                                                                                                                             | 输出与日志事件相关联的，由应用程序提供的日志信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **M / method**                                                                                                                                                                                                                                                                                                                                                                    | <p>输出发出日志请求的方法名。<br>生成方法名不是特别快，因此，应该避免使用，除非生成速度不是问题。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **n**                                                                                                                                                                                                                                                                                                                                                                             | <p>输出平台所依赖的行分割字符。<br>转换字符提供了像 "\n" 或 "\r\n" 一样的转换效果。因此指定行分隔符它是首选的指定方式。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **p / le / level**                                                                                                                                                                                                                                                                                                                                                                | 输出日志事件的级别。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **r / relative**                                                                                                                                                                                                                                                                                                                                                                  | 输出应用程序启动到创建日志事件所花费的毫秒数                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **t / thread**                                                                                                                                                                                                                                                                                                                                                                    | 输出生成日志事件的线程名。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <p><strong>X</strong>{<em>key:-defaultVal</em>}<br>  <strong>mdc</strong>{<em>key:-defaultVal</em>}</p>                                                                                                                                                                                                                                                                           | <p>输出生成日志事件的线程的 MDC (mapped diagnostic context)。<br>如果 <strong>MDC</strong> 转换字符后面跟着用花括号括起来的 kye，例 <strong>%MDC{userid}</strong>，那么 'userid' 所对应 MDC 的值将会输出。如果该值为 null，那么通过 :- 指定的<a href="https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%8F%98%E9%87%8F%E7%9A%84%E9%BB%98%E8%AE%A4%E5%80%BC">默认值</a> 将会输出。如果没有指定默认值，那么将会输出空字符串。<br>如果没有指定的 key，那么 MDC 的整个内容将会以 "key1=val1, key2=val2" 的格式输出。<br>查详情请见 <a href="https://logback.qos.ch/manual/mdc.html">第八章</a></p>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **ex**{*depth*}  **exception**{*depth*}  **throwable**{*depth*}   **ex**{depth, evaluator-1, ..., evaluator-n}  **exception**{depth, evaluator-1, ..., evaluator-n}  **throwable**{depth, evaluator-1, ..., evaluator-n}                                                                                                                                                          | <p>输出日志事件相关的堆栈信息，默认情况下会输出全部的堆栈信息。<br> <em>throwable</em> 转换词可以接收如下的参数：<br><br>下面是一些示例：<br><br>在输出前，转换字符还可以使用给定的标准再次检验日志事件。例如，使用 <strong>%ex{full, EX\_DISPLAY\_EVAL}</strong>，只有 <em>EX\_DISPLAY\_EVAL</em> 返回一个否定的答案，才会输出全部的堆栈信息。evaluator 在接下来的文档中将会进一步叙述。<br>如果你没有指定 %throwable 或者其它跟 throwable 相关的转换字符，那么 <code>PatternLayout</code> 会在最后一个转换字符加上这个。因为堆栈信息非常的重要。如果你不想展示堆栈信息，那么可以使用 %nopex (作者原文为 $nopex) 可以替代 %throwable。详情见 %nopex。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <p><a href="#xThrowable"><strong>xEx</strong>{<em>depth</em>}</a>  <br><strong>xException</strong>{<em>depth</em>}  <strong>xThrowable</strong>{<em>depth</em>}   <br><strong>xEx</strong>{depth, evaluator-1, ..., evaluator-n}  <br><strong>xException</strong>{depth, evaluator-1, ..., evaluator-n} <br><strong>xThrowable</strong>{depth, evaluator-1, ..., evaluator-n}</p> | <p>跟 %throwable 类似，只不过多了类的包信息。<br>在每个堆栈信息的末尾，多了包含 jar 文件的字符串，后面再加上具体的实现版本。这项创造性的技术是来自 <a href="http://macstrac.blogspot.com/2008/09/better-stack-traces-in-java-with-log4j.html">James Strachan</a> 的建议。如果该信息不确定，那么类的包信息前面会有一个波浪号 (~~)。<br>下面是一个例子：<br>logback 努力的去确保类的包信息正确的展示，即使是在复杂的类加载层次中。但是，一个不能保证信息的绝对正确，那么在这些数据的前面将会多一个波浪符 (~~)。因此，从理论上来说，打印的类的包信息跟真实的类的包信息是有区别的。在上面的例子中，类 Wombat 的包信息前面有一个波浪符，在实际的情况中，它真实包可能为  \[wombat.jar:1.7]。<br>但是请注意潜在的性能损耗，计算<a href="https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%9C%A8%E5%A0%86%E6%A0%88%E4%B8%AD%E5%B1%95%E7%A4%BA%E5%8C%85%E6%95%B0%E6%8D%AE">包信息默认是禁止的</a>。当启用了计算包信息，那么 <code>PatternLayout</code> 将会自动认为在字符串模式的末尾 %xThrowable 替代了 %throwable。<br>根据用户的<a href="https://jira.qos.ch/browse/LOGBACK-324">反馈</a>，Netbeans 会阻止包信息的打印。</p>                                                                                                |
| <p><strong>nopex</strong><br><strong>nopexception</strong></p>                                                                                                                                                                                                                                                                                                                    | <p>这个转换字符不会输出任何数据，因此，它可以用来有效忽略异常信息。<br>%nopex 转换字符允许用户重写 <code>PatternLayout</code> 内部的安全机制，该机制将会在没有指定其它处理异常的转换字符时，默认添加 %xThrowable。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **marker**                                                                                                                                                                                                                                                                                                                                                                        | <p>输出与日志请求相关的标签。<br>一旦标签包含子标签，那么转换器将会根据下面的格式展示父标签与子标签。<br><em>parentName \[child1, child2]</em></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **property{key}**                                                                                                                                                                                                                                                                                                                                                                 | <p>输出属性 <em>key</em> 所对应的值。相关定义参见 <a href="https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%8F%98%E9%87%8F%E6%9B%BF%E6%8D%A2">定义变量</a> 以及<a href="https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E4%BD%9C%E7%94%A8%E5%9F%9F">作用域</a>。如果 key 在 logger context 中没有找到，那么将会去系统属性中找。<br><em>key</em> 没有默认值，如果缺失，则会展示 " Property\_HAS\_NO\_KEY" 的错误信息。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**replace(p){r, t}**](#replace)                                                                                                                                                                                                                                                                                                                                                  | <p>在子模式 'p' 产生的字符中，将所有出现正则表达式 'r' 的地方替换为 't'。例如，"%replace(%msg){'\s', ''}" 将会移除事件消息中所有空格。<br>模式 'p' 可以是任意复杂的甚至由多个转换字符组成。例如，"%replace(%logger %msg){'.', '/'}" 将会替换 logger 以及消息中所有的点为斜杆。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **rEx**{*depth*}  **rootException**{*depth*}   **rEx**{depth, evaluator-1, ..., evaluator-n}  **rootException**{depth, evaluator-1, ..., evaluator-n}                                                                                                                                                                                                                             | <p>输出与日志事件相关的堆栈信息，根异常将会首先输出，而是标准的"根异常最后输出"。下面是一个输出例子：<br>%rootException 跟 %xException 类似，也允许一些可选的参数，包括深度以及 evaluator。它也会输出包信息。简单来说，%rootException 跟 %xException 非常的类似，仅仅是异常输出的顺序完全相反。<br>  %rootException 的作者 Tomasz Nurkiewicz 在他的博客说明了他所作的贡献 <a href="http://nurkiewicz.blogspot.com/2011/09/logging-exceptions-root-cause-first.html">"Logging exceptions root cause first"</a>。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

**% 有特殊的含义**

在给定的转换模式上下文中，% 有特殊的含义。如果作为字面量，需要进行转义。例如，"%d %p \\% %m%n"。

**转换字符对字面量的限制**

在大多数的情况下，字面量包括空格或者其它的分隔符，所以它们不会与转换字符混淆。例如，"%level \[%thread] - %message%n" 包含字面量字符 " \[" 与 "] - "。但是，如果一个转换字符后面紧跟着一个字面量，那么 logback 的模式解析器将会错误的认为这个字面量也是转换字符的一部分。例如，"%dat&#x65;**%nHello**" 将会被解析成两个转换字符 %date 与 %nHello，但是 %nHello 不是一个转换字符，所以 logback 将会输出 %PARSER\_ERROR\[nHello]。如果你想要区分 %n 跟 Hello，可以通过给 %n 传递一个空参数。例如，"%dat&#x65;**%n{}**&#x48;ello" 将会被解析为 %date %n 再紧跟着一个字符串 "Hello"。

### 格式修改器

默认情况下，相关信息按照原样输出。但是，在格式修改器的帮助下，可以对每个数据字段进行对齐，以及更改最大最小宽度。

可选的格式修改器放在百分号跟转换字符之间。

第一个可选的格式修改器是*左对齐标志*，也就是减号 (-) 字符。接下来的是*最小字段宽度修改器*，它是一个十进制常量，表示输出至少多少个字符。如果字段包含很少的数据，它会选择填充左边或者右边，直到满足最小宽度。默认是填充左边 (右对齐)，但是你可以通过左对齐标志来对右边进行填充。填充字符为空格。如果字段的数据大于最小字段的宽度，会自动扩容去容纳所有的数据。字段的数据永远不会被截断。

这个行为可以通过使用*最大字段宽度修改器*来改变，它通过一个点后面跟着一个十进制常量来指定。如果字段的数据长度大于最大字段的宽度，那么会从数据字段的开头移除多余的字符。举个🌰，如果最大字段的宽度是 8，数据长度是十个字符的长度，那么开头的两个字符将会被丢弃。这个行为跟 C 语言中 printf 函数从后面开始截断的行为相违背。

如果想从后面开始截断，可以在点后面增加一个减号。如果是这样的话，最大字段宽度是 8，数据长度是十个字符的长度，那么最后两个字符将会被丢弃。

下面是各种格式修改器的例子：

| 格式修改器         | 左对齐   | 最小宽度 | 最大宽度 | 备注                                                                       |
| ------------- | ----- | ---- | ---- | ------------------------------------------------------------------------ |
| %20logger     | false | 20   | none | 如果 logger 的名字小于 20 个字符的长度，那么会在左边填充空格                                     |
| %-20logger    | true  | 20   | none | 如果 logger 的名字小于 20 个字符的长度，那么会在右边填充空格                                     |
| %.30logger    | NA    | none | 30   | 如果 logger 的名字大于 30 个字符的长度，那么从前面开始截断                                      |
| %20.30logger  | false | 20   | 30   | 如果 logger 的名字大于 20 个字符的长度，那么会从左边填充空格。但是如果 logger 的名字大于 30 字符，将会从前面开始截断   |
| %-20.30logger | true  | 20   | 30   | 如果 logger 的名字小于 20 个字符的长度，那么从右边开始填充空格。但是如果 logger 的名字大于 30 个字符，将会从前面开始截断 |
| %.-30logger   | NA    | none | 30   | 如果 logger 的名字大于 30 个字符的长度，那么从后面开始截断                                      |

下面的表格列出了格式修改器截断的例子。但是请注意综括号 "\[]" 不是输出结果的一部分，它只是用来区分输出的长度。

| 格式修改器            | logger 的名字            | 结果                      |
| ---------------- | --------------------- | ----------------------- |
| \[%20.20logger]  | main.Name             | \[           main.Name] |
| \[%-20.20logger] | main.Name             | \[main.Name           ] |
| \[%10.10logger]  | main.foo.foo.bar.Name | \[o.bar.Name]           |
| \[%10.-10logger] | main.foo.foo.bar.Name | \[main.foo.f]           |

#### 只输出日志等级的一个字符

除了可以输出 TRACE, DEBUG, WARN, INFO 或者 ERROR 来表示日志等级之外，还是输出T, D, W, I 与 E 来进行表示。你可以[自定义转换器](https://logback.qos.ch/manual/layouts.html#customConversionSpecifier) 或者利用刚才讨论的格式修改器来缩短日志级别为一个字符。这个转换说明符可能为 "%.-1level"。

### 转换字符的选项

一个转换字符后面可以跟一个选项。它们通过综括号来声明。我们之前已经看到了一些可能的选项。例如之前的 MDC 转换说明符 *%mdc{someKey}*。

一个转换说明符可能有多个可选项。一个转换说明符可以充分利用我们即将介绍到的 evaluator，可以添加多个 evaluator 的名字到可选列表。如下：

```markup
<pattern>%-4relative [%thread] %-5level - %msg%n \
  %caller{2, DISP_CALLER_EVAL, OTHER_EVAL_NAME, THIRD_EVAL_NAME}</pattern>
```

如果这些选项中包含了一些特殊字符，例如花括号，空格，逗号。你可以使用单引号或者双引号来包裹它们。例如：

```markup
<pattern>%-5level - %replace(%msg){'\d{14,16}', 'XXXX'}%n</pattern>
```

我们传递 `\d{16}` 与 `XXXX` 给 `replace` 转换字符。它将消息中 14，15 或者 16 位的数字替换为 XXXX，用来混淆信用卡号码。在正则表达式中，"\d" 表示一个数字的简写。"{14,16}" 会被解析成 "{14,16}"，也就是说前一个项将会被重复至少 14 次，至多 16 次。

### 特殊的圆括号

在 logback 里，模式字符串中的圆括号被看作为分组标记。因此，它能够对子模式进行分组，并且直接对子模式进行格式化。在 0.9.27 版本，logback 开始支持综合转换字符，例如 [%replace](https://github.com/Volong/logback-chinese-manual/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ALayout.md#replace) 可以对子模式进行转换。

例如一下模式：

```
%-30(%d{HH:mm:ss.SSS} [%thread]) %-5level %logger{32} - %msg%n
```

将会对子模式 "%d{HH:mm:ss.SSS} \[%thread]" 进行分组输出，为了在少于 30 个字符时进行右填充。

如果没有进行分组将会输出：

```java
13:09:30 [main] DEBUG c.q.logback.demo.ContextListener - Classload hashcode is 13995234
13:09:30 [main] DEBUG c.q.logback.demo.ContextListener - Initializing for ServletContext
13:09:30 [main] DEBUG c.q.logback.demo.ContextListener - Trying platform Mbean server
13:09:30 [pool-1-thread-1] INFO  ch.qos.logback.demo.LoggingTask - Howdydy-diddly-ho - 0
13:09:38 [btpool0-7] INFO c.q.l.demo.lottery.LotteryAction - Number: 50 was tried.
13:09:40 [btpool0-7] INFO c.q.l.d.prime.NumberCruncherImpl - Beginning to factor.
13:09:40 [btpool0-7] DEBUG c.q.l.d.prime.NumberCruncherImpl - Trying 2 as a factor.
13:09:40 [btpool0-7] INFO c.q.l.d.prime.NumberCruncherImpl - Found factor 2
```

如果对 "%-30()" 进行分组将会输出：

```java
13:09:30 [main]            DEBUG c.q.logback.demo.ContextListener - Classload hashcode is 13995234
13:09:30 [main]            DEBUG c.q.logback.demo.ContextListener - Initializing for ServletContext
13:09:30 [main]            DEBUG c.q.logback.demo.ContextListener - Trying platform Mbean server
13:09:30 [pool-1-thread-1] INFO  ch.qos.logback.demo.LoggingTask - Howdydy-diddly-ho - 0
13:09:38 [btpool0-7]       INFO  c.q.l.demo.lottery.LotteryAction - Number: 50 was tried.
13:09:40 [btpool0-7]       INFO  c.q.l.d.prime.NumberCruncherImpl - Beginning to factor.
13:09:40 [btpool0-7]       DEBUG c.q.l.d.prime.NumberCruncherImpl - Trying 2 as a factor.
13:09:40 [btpool0-7]       INFO  c.q.l.d.prime.NumberCruncherImpl - Found factor 2
```

后者的格式更加容易阅读。

如果你想将圆括号当作字面量输出，那么你需要对每个圆括号用反斜杠进行转义。就像 **(**%d{HH:mm:ss.SSS} \[%thread]**)** 一样。

### 着色

如上所述的[圆括号](https://github.com/Volong/logback-chinese-manual/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ALayout.md#%E7%89%B9%E6%AE%8A%E7%9A%84%E5%9C%86%E6%8B%AC%E5%8F%B7)分组，允许对子模式进行着色。在 1.0.5 版本，`PatternLayout` 可以识别 "%black"，"%red"，"%green"，"%yellow"，"%blue"，"%magenta","%cyan", "%white", "%gray", "%boldRed","%boldGreen", "%boldYellow", "%boldBlue", "%boldMagenta""%boldCyan", "%boldWhite" 以及 "%highlight" 作为转换字符。这些转换字符都还可以包含一个子模式。任何被颜色转换字符包裹的子模式都会通过指定的颜色输出。

下面是关于着色的配置文件。

```markup
<configuration debug="true">
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
<!--               在 Windows 平台下，设置 withJansi = true 来开启 ANSI 颜色代码需要 Jansi 类库 -->
<!--               需要在 classpath 引入 org.fusesource.jansi:jansi:1.8 包 -->
<!--               在基于 Unix 操作系统，像 Linux 以及 Mac OS X 系统默认支持 ANSI 颜色代码 -->
        <withJansi>true</withJansi>
        <encoder>
            <pattern>[%thread] %highlight(%-5level) %cyan(%logger{15}) - %msg %n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

下面是相关的输出：

```java
[main] WARN  c.l.TrivialMain - a warning message 0
[main] DEBUG c.l.TrivialMain - hello world number1
[main] DEBUG c.l.TrivialMain - hello world number2
[main] INFO  c.l.TrivialMain - hello world number3
[main] DEBUG c.l.TrivialMain - hello world number4
[main] WARN  c.l.TrivialMain - a warning message 5
[main] ERROR c.l.TrivialMain - Finish off with fireworks
```

> 其实是有颜色的，但是 md 不支持直接对字体颜色进行操作，而我懒得去折腾 HTML

只需要几行代码就可以创建一个着色转换字符。在自定义转换说明符部分，我们将讨论怎样在配置文件中注册一个转换字符。

### Evaluators

像之前提到的，当一个转换字符需要基于一个或者多个 [`EventEvaluator`](https://logback.qos.ch/xref/ch/qos/logback/core/boolex/EventEvaluator.html) 对象动态表现时，`EventEvaluator` 对象根据规则可以决定给定的日志事件是否匹配。

让我们来回顾一下包含 `EventEvaluator` 的例子。下一个配置文件输出日志事件到控制台，显示日期，线程，日志级别，消息，以及调用者数据。获取日志事件调用者的信息成本比较高，只有当日志请求来源特定的 logger，或者消息包含特定的字符串时，我们才会这样做。换句话说，在调用者信息是多余的情况下，我们不应该去影响应用的性能。

Evaluator 与 *评价表达式 (evaluation expressions)* 都会在[第七章](https://logback.qos.ch/manual/filters.html#evalutatorFilter) 详细介绍。如果你想利用 evaluator 去做一些有意思的事情，你必须看一下对这个的详细介绍。下面的例子基于 `JaninoEventEvaluator`，所以需要 [Janino 类库](http://docs.codehaus.org/display/JANINO/Home)。查看[相关文档](https://logback.qos.ch/setup.html#janino)进行设置。

> Example: *callerEvaluatorConfig.xml*

```markup
<configuration>
  <evaluator name="DISP_CALLER_EVAL">
    <expression>logger.contains("chapters.layouts") &amp;&amp; \
      message.contains("who calls thee")</expression>
  </evaluator>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> 
    <encoder>
      <pattern>
        %-4relative [%thread] %-5level - %msg%n%caller{2, DISP_CALLER_EVAL}
      </pattern>
    </encoder>
  </appender>

  <root level="DEBUG"> 
    <appender-ref ref="STDOUT" /> 
  </root>
</configuration>
```

上面的评价表达式用来匹配从名为 "chapters.layouts" logger 发出，并且消息中包含字符串 "who calls thee" 的日志事件。由于 XML 的编码规则，`&` 符号需要被转义为 `&amp;`。

下面的类利用了配置文件中所提到的特性。

> Example: CallerEvaluatorExample.java

```java
package chapters.layouts;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.classic.joran.JoranConfigurator;
import ch.qos.logback.core.joran.spi.JoranException;
import ch.qos.logback.core.util.StatusPrinter;

public class CallerEvaluatorExample {

  public static void main(String[] args)  {
    Logger logger = LoggerFactory.getLogger(CallerEvaluatorExample.class);
    LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();

    try {
      JoranConfigurator configurator = new JoranConfigurator();
      configurator.setContext(lc);
      configurator.doConfigure(args[0]);
    } catch (JoranException je) {
      // StatusPrinter will handle this
    }
    StatusPrinter.printInCaseOfErrorsOrWarnings(lc);

    for (int i = 0; i < 5; i++) {
      if (i == 3) {
        logger.debug("who calls thee?");
      } else {
        logger.debug("I know me " + i);
      }
    }
  }
}
```

上面的应用没有什么特别的地方。发出五条日志请求，第三条的的请求信息为 "who calls thee?"。

通过命令：

```bash
java chapters.layouts.CallerEvaluatorExample src/main/java/chapters/layouts/callerEvaluatorConfig.xml
```

将会输出：

```java
0    [main] DEBUG - I know me 0 
0    [main] DEBUG - I know me 1 
0    [main] DEBUG - I know me 2 
0    [main] DEBUG - who calls thee? 
Caller+0   at chapters.layouts.CallerEvaluatorExample.main(CallerEvaluatorExample.java:28)
0    [main] DEBUG - I know me 4
```

当发出日志请求时，会评价相应的日志事件。仅仅只有第三个日志事件会匹配到评价规则，所以它的调用者信息会被展示出来。对于其它的日志事件，由于没有匹配到评价规则，调用者信息不会被打印。

可以通过更改表达式来应对真实的应用场景。举个🌰，你可以结合 logger 名与日志级别，日志级别在 *WARN* 以上的日志请求被当作一个敏感的部分，在金融业务模块中，我们可以这样做来获取调用者的信息。

**重要：**&#x5F53;*评价表达式*为 **true** 时，通过 *caller* 转换字符，可以输出调用者的信息。

考虑这么一种情况，当日志请求中包含异常信息时，它们的堆栈信息也会输出。但是，对于某些特定的异常信息，可能需要禁止输出堆栈信息。

下面的代码创建了三条日志请求，每一条都包含一个异常信息。第二条的异常信息跟其它的不一样，它包含 "do not display this" 字符串，并且它的异常信息类型为 `chapters.layouts.TestException`。现在让我们来阻止第二条日志的打印。

> Example: *ExceptionEvaluatorExample.java*

```java
package chapters.layouts;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.classic.joran.JoranConfigurator;
import ch.qos.logback.core.joran.spi.JoranException;
import ch.qos.logback.core.util.StatusPrinter;

public class ExceptionEvaluatorExample {

  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(ExceptionEvaluatorExample.class);
    LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();

    try {
      JoranConfigurator configurator = new JoranConfigurator();
      configurator.setContext(lc);
      lc.reset();
      configurator.doConfigure(args[0]);
    } catch (JoranException je) {
       // StatusPrinter will handle this
    }
    StatusPrinter.printInCaseOfErrorsOrWarnings(lc);

    for (int i = 0; i < 3; i++) {
      if (i == 1) {
        logger.debug("logging statement " + i, new TestException(
            "do not display this"));
      } else {
        logger.debug("logging statement " + i, new Exception("display"));
      }
    }
  }
}
```

下面的配置文件通过评价表达式来匹配包含 `chapters.layouts.TextException` 类型的日志事件，也就是我们之前说要禁止的异常类型。

> Example: *exceptionEvaluatorConfig.xml*

```markup
<configuration>
  <!-- evaluator 需要在 appender 前面定义 -->
  <evaluator name="DISPLAY_EX_EVAL">
    <expression>throwable != null &amp;&amp; throwable instanceof  \
      chapters.layouts.TestException</expression>
  </evaluator>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%msg%n%xEx{full, DISPLAY_EX_EVAL}</pattern>
    </encoder>
  </appender>

  <root level="debug">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

> 作者原文里面是 %ex，应该是笔误

通过这个配置文件，每当日志请求中包含一个 *chapters.layouts.TestException* 时，堆栈信息不会被输出。

通过如下命令启动：

```bash
java chapters.layouts.ExceptionEvaluatorExample src/main/java/chapters/layouts/exceptionEvaluatorConfig.xml
```

将会输出：

```java
logging statement 0
java.lang.Exception: display
    at chapters.layouts.ExceptionEvaluatorExample.main(ExceptionEvaluatorExample.java:16)
logging statement 1
logging statement 2
java.lang.Exception: display
    at chapters.layouts.ExceptionEvaluatorExample.main(ExceptionEvaluatorExample.java:16)
```

> 作者原文还输出了 jar 包的信息，是因为打包后通过命令行执行的 (I think 😂)

第二条日志没有堆栈信息，因为我们禁止 `TextException` 类型的堆栈信息。每条堆栈信息的最后用综括号包裹起来的是具体的[包信息](https://github.com/Volong/logback-chinese-manual/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ALayout.md#xThrowable)。

**`注意：`** 当 **%ex** 转换说明符中的评价表达式为 **false** 时，堆栈信息才会输出。

### 自定义转换说明符

我们可以在 `PatternLayout` 中使用内置的转换字符。我们也可以使用自己新建的转换字符。

新建一个自定义的转换字符需要两步。

**第一步**

首先，你必须继承 `ClassicConverter` 类。[`ClassicConverter`](https://logback.qos.ch/xref/ch/qos/logback/classic/pattern/ClassicConverter.html) 对象负责从 `ILoggingEvent` 实例中抽取信息并输出字符串。例如，%logger 对应的转换器 [`LoggerConverter`](https://logback.qos.ch/xref/ch/qos/logback/classic/pattern/LoggerConverter.html)，可以从 `ILoggingEvent` 从抽取 logger 的名字，返回一个字符串。它可以缩写 logger 的名字。

下面是一个自定义的转换器，返回从创建开始经过的时间，单位为纳秒。

> Example: MySampleConverter

```java
public class MySampleConverter extends ClassicConverter {

  long start = System.nanoTime();

  @Override
  public String convert(ILoggingEvent event) {
    long nowInNanos = System.nanoTime();
    return Long.toString(nowInNanos-start);
  }
}
```

这个实现非常简单。`MySampleConverter` 继承了 `ClassicConverter` 并实现了 `convert` 方法，返回从创建开始经过多少纳秒。

**第二步**

第二步，我们必须让 logback 知道这个新建的 `Converter`。所以我们需要在配置文件中进行声明，如下：

> Example: *mySampleConverterConfig.xml*

```markup
<configuration>

  <conversionRule conversionWord="nanos" 
                  converterClass="chapters.layouts.MySampleConverter" />

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%-6nanos [%thread] - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

执行命令如下：

```bash
java chapters.layouts.SampleLogging src/main/java/chapters/layouts/mySampleConverterConfig.xml
```

输出信息如下：

```java
26113953 [main] - Everything's going well
26672034 [main] - maybe not quite...
```

可以看一下其它 `Converter` 的实现，例如 [`MDCConverter`](https://logback.qos.ch/xref/ch/qos/logback/classic/pattern/MDCConverter.html) ，去定制更加复杂的功能，如可选处理。想创建自己的颜色主题，可以看一下 [`HighlightingCompositeConverter`](https://logback.qos.ch/xref/ch/qos/logback/classic/pattern/color/HighlightingCompositeConverter.html)。

### HTMLLayout

[`HTMLLayout`](https://logback.qos.ch/xref/ch/qos/logback/classic/html/HTMLLayout.html) (包含在 logback-classic 中) 以 HTML 格式生成日志。`HTMLLayout` 通过 HTML 表格输出日志，每一行对应一条日志事件。

下面是 `HTMLLayout` 通过默认的 CSS 样式生成的。

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbX4Ya1T5s07Xi4D%2FhtmlLayout0.gif?generation=1568702660863641\&alt=media)

表格的列是通过转换模式指定的。关于转换模式的文档请查看 [PatternLayout](https://github.com/Volong/logback-chinese-manual/blob/34f5a61965088f0fa6d0d2a7e0e7085160e95201/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ALayouts.md#patternlayout)。所以，你可以完全控制表格的内容以及格式。你可以选择并且展示任何跟 `PatternLayout` 组合的转换器。

一个值得注意的问题是使用 `PatternLayout` 中的 `HTMLLayout` 时，不要使用空格或者其它的字面量来分隔转换说明符。转换模式中的每个说明符都会被当做一个单独的列。同样的转换模式中的每个文本块也会被当作一个单独的列，这会占用屏幕的空间。

下面的 `HTMLLayout` 相关的配置：

> Example: *htmlLayoutConfig1.xml*

```markup
<configuration debug="true">
  <appender name="FILE" class="ch.qos.logback.core.FileAppender">
    <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
      <layout class="ch.qos.logback.classic.html.HTMLLayout">
        <pattern>%relative%thread%mdc%level%logger%msg</pattern>
      </layout>
    </encoder>
    <file>test.html</file>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="FILE" />
  </root>
</configuration>
```

[TrivialMain](https://logback.qos.ch/xref/chapters/layouts/TrivialMain.html) 包含一些消息以及一个结束异常。执行以下命令：

```bash
java chapters.layouts.TrivialMain src/main/java/chapters/layouts/htmlLayoutConfig1.xml
```

将会当前文件夹创建一个 *test.html* 文件。*test.html* 文件的内容与下面类似：

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbX6xTak01sW3eCB%2FhtmlLayout1.png?generation=1568702660939297\&alt=media)

#### 堆栈信息

如果你使用 *%ex* 转换字符去展示堆栈信息，那么将会创建一个列来展示堆栈信息。在大多数的情况下，列会为空，那么就会浪费屏幕的空间。而且，在单独的列打印堆栈信息，输出的结果阅读起来有难度。但是，*%ex* 转换字符不是唯一一个用来展示堆栈信息的。

> 原文第一个 %ex 为 %em

一个更好的解决办法是通过实现 `IThrowableRenderer` 接口。实现的接口可以分配给 `HTMLLayout` 来管理相关的异常数据。默认情况下，会给每个 `HTMLLayout` 实例分配一个 [`DefaultThrowableRenderer`](https://logback.qos.ch/xref/ch/qos/logback/classic/html/DefaultThrowableRenderer.html)。它将异常的堆栈信息写入到表格新的一行，并且非常易读，就跟上面展示的表格一样。

如果在某些情况下，你仍然想要使用 *%ex*，那么你可以在配置文件中指定 [`NOPThrowableRenderer`](https://logback.qos.ch/xref/ch/qos/logback/core/html/NOPThrowableRenderer.html) 来禁止在单独一行展示堆栈信息。我们不理解为什么你要这样做，但是你开心就好。

#### CSS

`HTMLLayout` 创建的 HTML 是通过 CSS 来控制样式的。在缺少指定命令的情况下，`HTMLLayout` 会使用内部默认的样式。但是，你可以告诉 `HTMLLayout` 去使用外部的 CSS 文件。通过在 `<layout>` 元素内置 `<cssBuilder>` 元素可以做到。如下所示：

```markup
<layout class="ch.qos.logback.classic.html.HTMLLayout">
  <pattern>%relative...%msg</pattern>
  <cssBuilder class="ch.qos.logback.classic.html.UrlCssBuilder">
    <!-- css 文件的路径 -->
    <url>http://...</url>
  </cssBuilder> 
</layout>
```

`HTMLLayout` 通常与 `SMTPAppender` 配合使用，所以邮件可以被格式化成 HTML。

### Log4j XMLLayout

[XMLLayout](https://logback.qos.ch/xref/ch/qos/logback/classic/log4j/XMLLayout.html) (logback-classic 的一部分) 生成一个 log4j.dtd 格式的文件，用来与类似 [Chainsaw](http://logging.apache.org/chainsaw/index.html) 以及 [Vigilog](http://vigilog.sourceforge.net/) 这样的工具进行交互操作，这些工具可以处理由 [log4j XMLLayout](http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/xml/XMLLayout.html) 生成的文件。

跟 log4j 1.2.15 版本的 XMLLayout 一样，logback-classic 中的 XMLLayout 接收两个 boolean 属性：`locationInfo` 与 `properties`。设置 `locationInfo` 的值为 true，可以在每个事件中开启包含位置信息 (调用者的数据)。设置 `properties` 为 true，可以开启包含 MDC 信息。默认情况下，两个属性都设置为 false。

下面是一个示例：

> Example: *log4jXMLLayout.xml*

```markup
<configuration>
  <appender name="FILE" class="ch.qos.logback.core.FileAppender">
    <file>test.xml</file>
    <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
      <layout class="ch.qos.logback.classic.log4j.XMLLayout">
        <locationInfo>true</locationInfo>
      </layout>
    </encoder> 
  </appender> 

  <root level="DEBUG">
    <appender-ref ref="FILE" />
  </root>
</configuration>
```

## Logback access

大多数 logback-access 的 layout 仅仅只是 logback-classic 的 layout 的改编。logback-classic 与 logback-access 模块定位不同的需求，但是都提供了类似的功能。

### 写你自己的 layout

在 logback-access 中写一个定制的 `Layout` 与在 logback-classic 的 `Layout` 中几乎一致。

#### PatternLayout

配置 logback-access 中的 [`PatternLayout`](https://logback.qos.ch/xref/ch/qos/logback/access/PatternLayout.html)，与在 logback-classic 中配置相同。但是它添加了一些额外的转换说明符来适应 HTTP 请求以及 HTTP 响应中特定信息位的记录。

下表是 logback-access 中 `PatternLayout` 的相关转换说明符。

| 转换字符                            | 效果                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **a / remoteIP**                | 远程 IP 地址                                                                                                                                                                                                                                                                                                                                             |
| **A / localIP**                 | 本地 IP 地址                                                                                                                                                                                                                                                                                                                                             |
| **b / B / bytesSent**           | 响应内容的长度                                                                                                                                                                                                                                                                                                                                              |
| **h / clientHost**              | 远程 host                                                                                                                                                                                                                                                                                                                                              |
| **H / protocol**                | 请求协议                                                                                                                                                                                                                                                                                                                                                 |
| **l**                           | 远程日志名，在 logback-access 中，转换器总是返回 "-"                                                                                                                                                                                                                                                                                                                 |
| **reqParameter{paramName}**     | <p>响应参数。<br>这个转换字符在花括号中接受一个参数，在请求中寻找相应的参数。<br> <strong>%reqParameter{input\_data}</strong> 展示相应的参数。</p>                                                                                                                                                                                                                                              |
| **i{header} / header{header}**  | <p>请求头。<br> <strong>%header{Referer}</strong> 显示请求的来源。<br>如果没有指定选项，将会展示所有可用的请求头</p>                                                                                                                                                                                                                                                                  |
| **m / requestMethod**           | 请求方法                                                                                                                                                                                                                                                                                                                                                 |
| **r / requestURL**              | 请求 URL                                                                                                                                                                                                                                                                                                                                               |
| **s / statusCode**              | 请求状态码                                                                                                                                                                                                                                                                                                                                                |
| **D / elapsedTime**             | 请求所耗费的时间，单位为毫秒                                                                                                                                                                                                                                                                                                                                       |
| **T / elapsedSeconds**          | 请求所耗费的时间，单位为秒                                                                                                                                                                                                                                                                                                                                        |
| **t / date**                    | <p>输出日志事件的日期。日期说明符需要用花括号指定。日期格式来源 <code>java.text.SimpleDateFormat</code>。<em>ISO8601</em> 也是一个有效的值。<br>例如，<strong>%t{HH:mm:ss,SSS}</strong> 或者 <strong>%t{dd MMM yyyy ;HH:mm:ss,SSS}</strong>。如果没有指定日期格式字符，那么会默认指定为 <strong>%t{dd/MMM/yyyy:HH:mm:ss Z}</strong></p>                                                                                 |
| **u / user**                    | 远程用户                                                                                                                                                                                                                                                                                                                                                 |
| **q / queryString**             | 请求查询字符串，前缀为 '?'                                                                                                                                                                                                                                                                                                                                      |
| **U / requestURI**              | 请求 URI                                                                                                                                                                                                                                                                                                                                               |
| **S / sessionID**               | Session ID.                                                                                                                                                                                                                                                                                                                                          |
| **v / server**                  | 服务器名                                                                                                                                                                                                                                                                                                                                                 |
| **I / threadName**              | 处理该条请求的线程                                                                                                                                                                                                                                                                                                                                            |
| **localPort**                   | 本地端口                                                                                                                                                                                                                                                                                                                                                 |
| **reqAttribute{attributeName}** | <p>请求的属性。<br><strong>%reqAttribute{SOME\_ATTRIBUTE}</strong> 展示相应的属性。</p>                                                                                                                                                                                                                                                                            |
| **reqCookie{cookie}**           | <p>请求 cookie。<br><strong>%cookie{COOKIE\_NAME}</strong> 展示相应的 cookie。</p>                                                                                                                                                                                                                                                                            |
| **responseHeader{header}**      | <p>响应头。<br><strong>%header{Referer}</strong> 展示响应的来源。</p>                                                                                                                                                                                                                                                                                            |
| **requestContent**              | 展示请求的内容，即请求的 `InputStream`。它与 [`TeeFilter`](https://logback.qos.ch/xref/ch/qos/logback/access/servlet/TeeFilter.html) 结合使用。一个使用  [`TeeHttpServletRequest`](https://logback.qos.ch/xref/ch/qos/logback/access/servlet/TeeHttpServletRequest.html) 替代  `HttpServletRequest` 的  javax.servlet.Filter。前者可以多次访问请求的 `InputStream` 而不会丢失内容。                 |
| **fullRequest**                 | 请求的数据。包括所有的请求头以及请求内容。                                                                                                                                                                                                                                                                                                                                |
| **responseContent**             | 展示响应的内容，也就是响应的 `InputStream`。 它与 [`TeeFilter`](https://logback.qos.ch/xref/ch/qos/logback/access/servlet/TeeFilter.html) 结合使用。一个使用  [`TeeHttpServletResponse`](https://logback.qos.ch/xref/ch/qos/logback/access/servlet/TeeHttpServletResponse.html) 替代 `HttpServletResponse` 的  `javax.servlet.Filter`。前者可以多次访问响应 (原文为请求) 的 `InputStream` 而不会丢失内容。 |
| **fullResponse**                | 获取响应所有可用的数据，包括所有的响应头以及响应内容。                                                                                                                                                                                                                                                                                                                          |

logback-access 的 `PatternLayout` 能够识别三个关键字，有点类似快捷键。

| 关键字               | 相等的转换模式                                                    |
| ----------------- | ---------------------------------------------------------- |
| *common* or *CLF* | *%h %l %u \[%t] "%r" %s %b*                                |
| *combined*        | *%h %l %u \[%t] "%r" %s %b "%i{Referer}" "%i{User-Agent}"* |

关键字 *common* 对应 *'%h %l %u \[%t] "%r" %s %b'*，分别展示客户端主机，远程日志名，用户，日期，请求 URL，状态码，以及响应内容的长度。

关键字 *combined* 对应 *'%h %l %u \[%t] "%r" %s %b "%i{Referer}" "%i{User-Agent}"'*。跟 *common* 有点类似，但是它还会再显示两个请求头，referer 以及 user-agent。

#### HTMLLayout

logback-access 中的 [`HTMLLayout`](https://logback.qos.ch/xref/ch/qos/logback/access/html/HTMLLayout.html) 与 logback-classic 中的 [`HTMLLayout`](https://logback.qos.ch/manual/layouts.html#ClassicHTMLLayout) 有点类似。

默认情况下，它会创建一个包含如下数据的表格：

* 请求 IP (Remote IP)
* 日期 (Date)
* 请求 URL (Request URL)
* 状态码 (Status code)
* 内容长度 (Content Length)

下面是 logback-access 中的 `HTMLLayout` 输出的一个例子：

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbX8DdkQcVHgQy65%2FhtmlLayoutAccess.gif?generation=1568702661130741\&alt=media)

还有比真实的例子更好的例子吗？我们自己的 log4j.properties 用于 logback [翻译器](http://logback.qos.ch/translator/)，充分的利用了 logback-access 在线演示 `RollingFileAppender` 与 `HTMLLayout` 的输出。

每一个新的用户请求 [翻译器](http://logback.qos.ch/translator/) 这个网站，一个新的条目就会添加到访问日志，你可以通过[这个链接](https://logback.qos.ch/translator/logs/access.html) 查看。

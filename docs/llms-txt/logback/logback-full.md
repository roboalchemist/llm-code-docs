# Logback Documentation

Source: https://logbackcn.gitbook.io/llms-full.txt

---

# README

logback 中文手册

> 翻译自 [The logback manual](https://logback.qos.ch/manual/index.html)

[在线地址](https://logbackcn.gitbook.io/logback/)

## 简介

Logback 继承自 log4j。

Logback 的架构非常的通用，适用不同的使用场景。Logback 被分成三个不同的模块：logback-core，logback-classic，logback-access。

logback-core 是其它两个模块的基础。logback-classic 模块可以看作是 log4j 的一个优化版本，它天然的支持 SLF4J，所以你可以随意的从其它日志框架（例如：log4j 或者 java.util.logging）切回到 logack。

logback-access 可以与 Servlet 容器进行整合，例如：Tomcat、Jetty。它提供了 http 访问日志的功能。

## The logback manual

手册包括了最新版本的 logback，总共有 150 多页，以及许多具体的例子，主要包含以下基本的和高级的特性：

* logback 的整体架构
* 讨论 logback 最好的实践以及反模式
* logback 的 xml 配置方式
* appender
* encoder
* layout
* filter
* 上下文诊断
* Joran - logback 的配置系统

logback 手册尽可能详细的描述了 logback API，包括它的特性以及设计原理。logback 手册适用于那些使用 Java 但是是 logback 新手的人，也适合那些对 logback 有一定经验的人。在手册的帮助下，新手可以快速上手。

* [第一章：logback 介绍](https://github.com/Volong/logback-chinese-manual/blob/master/01%E7%AC%AC%E4%B8%80%E7%AB%A0%EF%BC%9Alogback%20%E4%BB%8B%E7%BB%8D.md)
* [第二章：架构](https://github.com/Volong/logback-chinese-manual/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md)
* [第三章：logback 的配置](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md)
* [第四章：Appenders](https://github.com/Volong/logback-chinese-manual/blob/master/04%E7%AC%AC%E5%9B%9B%E7%AB%A0%EF%BC%9AAppenders.md)
* [第五章：Encoder](https://github.com/Volong/logback-chinese-manual/blob/master/05%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9AEncoder.md)
* [第六章：Layouts](https://github.com/Volong/logback-chinese-manual/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ALayouts.md)
* [第七章：Filters](https://github.com/Volong/logback-chinese-manual/blob/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AFilters.md)
* [第八章：MDC](https://github.com/Volong/logback-chinese-manual/blob/master/08%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9AMDC.md)
* [第九章：日志隔离](https://github.com/Volong/logback-chinese-manual/blob/master/09%E7%AC%AC%E4%B9%9D%E7%AB%A0%EF%BC%9A%E6%97%A5%E5%BF%97%E9%9A%94%E7%A6%BB.md)
* [第十章：JMX 配置器](https://github.com/Volong/logback-chinese-manual/blob/master/10%E7%AC%AC%E5%8D%81%E7%AB%A0%EF%BC%9AJMX%20%E9%85%8D%E7%BD%AE%E5%99%A8.md)
* [第十一章：Joran](https://github.com/Volong/logback-chinese-manual/blob/master/11%E7%AC%AC%E5%8D%81%E4%B8%80%E7%AB%A0%EF%BC%9AJoran.md)
* [第十二章：Groovy 配置](https://github.com/Volong/logback-chinese-manual/blob/master/12%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%EF%BC%9AGroovy%20%E9%85%8D%E7%BD%AE.md)
* [第十三章：从 log4j 迁移](https://github.com/Volong/logback-chinese-manual/blob/master/13%E7%AC%AC%E5%8D%81%E4%B8%89%E7%AB%A0%EF%BC%9A%E4%BB%8E%20log4j%20%E8%BF%81%E7%A7%BB.md)
* [第十四章：Receivers](https://github.com/Volong/logback-chinese-manual/blob/master/14%E7%AC%AC%E5%8D%81%E5%9B%9B%E7%AB%A0%EF%BC%9AReceivers.md)
* [第十五章：使用 SSL](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md)

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbMBuqn6JZuuhwH9%2Flog.png?generation=1568702626297053\&alt=media)

> 图片来源：[1](#note1)

推荐阅读：

1. [一个著名的日志系统是怎么设计出来的？](https://mp.weixin.qq.com/s/XiCky-Z8-n4vqItJVHjDIg)
2. [架构师必备，带你弄清混乱的JAVA日志体系！](https://mp.weixin.qq.com/s/8VvBdRH_Yc-Dt4HFGbC5rg)


# 第一章：logback 介绍

## 什么是 logback

logback 继承自 log4j，它建立在有十年工业经验的日志系统之上。它比其它所有的日志系统更快并且更小，包含了许多独特并且有用的特性。

## 天才第一步

### 要求

logback-classic 模块需要在 classpath 添加 slf4j-api.jar、logback-core.jar 以及 logback-classic.jar。

*Example 1.1: Basic template for logging*

```java
package chapters.introduction;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class HelloWorld1 {

    public static void main(String[] args) {
        Logger logger = LoggerFactory.getLogger("chapters.introduction.HelloWorld1");
        logger.debug("hello world");
    }
}
```

类 `HelloWorld1` 定义在包 `chapters.introduction` 中，它导入了两个类 `Logger`、`LoggerFactory`，这两个类定义在 SLF4J API 中，在 org.slf4j 包中。

在这个例子中，`main()` 包含了一个 DEBUG 级别的日志语句，输出信息为 "hello world"

运行 `HelloWord1` 将会在控制台看到一行日志。由于 logback 默认的配置策略：当没有默认的配置时，logback 将会在 root logger 中新增一个 `ConsoleAppender`

```
11:58:56.662 [main] DEBUG chapters.introduction.HelloWorld1 - hello world
```

Logback 通过一个内部的状态系统来报告它本身的状态信息。发生在 logback 生命周期中的事件可以通过 `StatusManager` 来获取。

*Example: Printing Logger Status*

```java
package chapters.introduction;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.core.util.StatusPrinter;

public class HelloWorld2 {

    public static void main(String[] args) {
        Logger logger = LoggerFactory.getLogger("chapters.introduction.HelloWorld2");
        logger.debug("Hello world");

        // 打印内部的状态
        LoggerContext lc = (LoggerContext)LoggerFactory.getILoggerFactory();
        StatusPrinter.print(lc);
    }
}
```

运行结果如下：

```java
12:23:49.324 [main] DEBUG chapters.introduction.HelloWorld2 - Hello world
12:23:49,258 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback-test.xml]
12:23:49,258 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback.groovy]
12:23:49,258 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback.xml]
12:23:49,262 |-INFO in ch.qos.logback.classic.BasicConfigurator@2e5d6d97 - Setting up default configuration.
```

Logback 没有找到 *logback-test.xml* 和 *logback.xml* 配置文件，所以通过默认的配置策略-添加一个基本的 `ConsoleAppender` 来进行配置。`Appender` 类被看作为输出的目的地。Appenders 包括 console，files，Syslog，TCP Sockets，JMS 等等其它的日志输出目的地。用户可以根据自己的情况轻松的创建自己的 Appender。

如果发生了错误，logback 会自动在控制台打印自己内部的状态信息。

前面给的例子相对简单。实际上在大型的应用中，日志记录不会有太大的区别。日志记录的一般形式不会有改变，只是配置方式会有不同。可能你想要根据自己的需求来配置 logback，接下来的章节中将会介绍如何进行配置。

在上面的例子中，我们通过 `StatusPrinter.print()` 打印了 logback 自身的内部状态。logback 的内部状态对查找 logback 相关的问题非常的有用。

通过如下的三个步骤可以启用 logback 来记录日志：

1. 配置 logback 环境。你可以通过简单或者复杂的方式来做，这个在后面会叙述到。
2. 如果你想在每个类中打印日志，那么你需要将当前类的全称或者当前类当作参数，调用  `org.slf4j.LoggerFactory.getLogger()` 方法。
3. 使用实例 logger 来调用不同的方法来打印日志。例：debug()，info()，warn()，error()。通过这些方法将会在配置好的 appender 中输出日志。

## 构建 logback

logback 使用 Maven 作为构建工具。

如果你安装了 Maven，你可以在 logback 的解压文件夹中运行 `mvn install` 来构建 logback 以及它所包含的模块。Maven 会自动下载 logback 需要的其它类库。

Logback 的压缩包包含了完整的源码，所以你可以根据自己的需要随意更改。而且只要你使用 LGPL 跟 EPL 协议，你甚至可以发布你更改后的版本。


# 第二章：架构

## logback 的架构

跟[简介](https://github.com/Volong/logback-chinese-manual#%E7%AE%80%E4%BB%8B)类似

## Logger, Appender 和 Layouts

Logback 构建在三个主要的类上：Logger，Appender 和 Layouts。这三个不同类型的组件一起作用能够让开发者根据消息的类型以及日志的级别来打印日志。

`Logger` 类作为 logback-classic 模块的一部分。`Appender` 与 `Layouts` 接口作为 logback-core 的一部分。作为一个通用的模块，logback-core 没有 logger 的概念。

### Logger 上下文

任何日志 API 的优势在于它能够禁止某些日志的输出，但是又不会妨碍另一些日志的输出。通过假定一个日志空间，这个空间包含所有可能的日志语句，这些日志语句根据开发人员设定的标准来进行分类。在 logback-classic 中，分类是 logger 的一部分，每一个 logger 都依附在 `LoggerContext` 上，它负责产生 logger，并且通过一个树状的层级结构来进行管理。

一个 Logger 被当作为一个实体，它们的命名是大小写敏感的，并且遵循以下规则：

> 命名层次结构
>
> 如果一个 logger 的名字加上一个 `.` 作为另一个 logger 名字的前缀，那么该 logger 就是另一个 logger 的祖先。如果一个 logger 与另一个 logger 之间没有其它的 logger ，则该 logger 就是另一个 logger 的父级。

例如：名为 `com.foo` 的 logger 是名为 `com.foo.Bar` 的 logger 的父级。名为 `java` 的 logger 是名为 `java.util` 的父级，是名为 `java.util.Vector` 的祖先。

root logger 作为 logger 层次结构的最高层。它是一个特殊的 logger，因为它是每一个层次结构的一部分。每一个 logger 都可以通过它的名字去获取。例：

```java
Logger rootLogger = LoggerFactory.getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME)
```

所有其它的 logger 通过 `org.slf4j.LoggerFactory` 类的静态方法 `getLogger` 去获取，这个方法需要传入一个 logger 的名字。下面是 `Logger` 接口一些基本的方法：

```java
package org.slf4j; 
public interface Logger { 
  public void trace(String message);
  public void debug(String message);
  public void info(String message); 
  public void warn(String message); 
  public void error(String message); 
}
```

### 有效等级又称为等级继承

Logger 能够被分成不同的等级。不同的等级（TRACE, DEBUG, INFO, WARN, ERROR）定义在 `ch.qos.logback.classic.Level` 类中。在 logback 中，类 `Level` 使用 final 修饰的，所以它不能用来被继承。一种更灵活的方式是使用 `Marker` 对象。

如果一个给定的 logger 没有指定一个层级，那么它就会继承离它最近的一个祖先的层级。更正式的说法是：

> 对于一个给定的名为 *L* 的 logger，它的有效层级为从自身一直回溯到 root logger，直到找到第一个不为空的层级作为自己的层级。

为了确保所有的 logger 都有一个层级，root logger 会有一个默认层级 --- DEBUG

以下四个例子指定不同的层级，以及根据继承规则得到的最终有效层级

*Example 1*

| logger 的名字 | 指定的层级 |  有效层级 |
| :--------: | :---: | :---: |
|    root    | DEBUG | DEBUG |
|      X     |  none | DEBUG |
|     X.Y    |  none | DEBUG |
|    X.Y.Z   |  none | DEBUG |

在这个例子中，只有 root logger 被指定了层级，所以 logger **X**，**X.Y**，**X.Y.Z** 的有效层级都是 DEBUG。

*Example 2*

| logger 的名字 | 指定的层级 |  有效层级 |
| :--------: | :---: | :---: |
|    root    | ERROR | ERROR |
|      X     |  INFO |  INFO |
|     X.Y    | DEBUG | DEBUG |
|    X.Y.Z   |  WARN |  WARN |

在这个例子中，每个 logger 都分配了层级，所以有效层级就是指定的层级。

*Example 3*

| logger 的名字 | 指定的层级 |  有效层级 |
| :--------: | :---: | :---: |
|    root    | DEBUG | DEBUG |
|      X     |  INFO |  INFO |
|     X.Y    |  none |  INFO |
|    X.Y.Z   | ERROR | ERROR |

在这个例子中，logger **root**，**X**，**X.Y.Z** 都分别分配了层级。logger **X.Y** 继承它的父级 logger **X**。

*Example 4*

| logger 的名字 | 指定的层级 |  有效层级 |
| :--------: | :---: | :---: |
|    root    | DEBUG | DEBUG |
|      X     |  INFO |  INFO |
|     X.Y    |  none |  INFO |
|    X.Y.Z   |  none |  INFO |

在这个例子中，logger **root**，**X** 都分配了层级。logger **X.Y**，**X.Y.Z** 的层级继承它们最近的父级 **X**。

### 方法打印以及基本选择规则

根据定义，打印的方法决定的日志的级别。例如：**L** 是一个 logger 实例，`L.info("...")` 的日志级别就是 INFO。

如果一条的日志的打印级别大于 logger 的有效级别，该条日志才可以被打印出来。这条规则总结如下：

> **基本选择规则**
>
> 日志的打印级别为 *p*，Logger 实例的级别为 *q*，如果 *p* >= *q*，则该条日志可以打印出来。

这条规则是 logbakc 的核心。各级别的排序为：**TRACE** < **DEBUG** < **INFO** < **WARN** < **ERROR**。

在下面的表格中，第一列表示的是日志的打印级别，用 *p* 表示。第一行表示的是 logger 的有效级别，用 *q* 表示。行列交叉处的结果表示由**基本选择规则**得出的结果。

![basic selection rule](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbRNXxcOJop4Vcdl%2Fbasic-selection-rule..png?generation=1568702631088864\&alt=media)

例子：

```java
package chapters.architecture;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.Level;

public class SelectionRule {

    public static void main(String[] args) {

        // ch.qos.logback.classic.Logger 可以设置日志的级别
        // 获取一个名为 "com.foo" 的 logger 实例
        ch.qos.logback.classic.Logger logger = 
                (ch.qos.logback.classic.Logger)LoggerFactory.getLogger("com.foo");
        // 设置 logger 的级别为 INFO
        logger.setLevel(Level.INFO);

        // 这条日志可以打印，因为 WARN >= INFO
        logger.warn("警告信息");
        // 这条日志不会打印，因为 DEBUG < INFO
        logger.debug("调试信息");

        // "com.foo.bar" 会继承 "com.foo" 的有效级别
        Logger barLogger = LoggerFactory.getLogger("com.foo.bar");
        // 这条日志会打印，因为 INFO >= INFO
        barLogger.info("子级信息");
        // 这条日志不会打印，因为 DEBUG < INFO
        barLogger.debug("子级调试信息");
    }
}
```

### 获取 Logger

通过 `LoggerFactory.getLogger()` 可以获取到具体的 logger 实例，名字相同则返回的 logger 实例也相同。

```java
Logger x = LoggerFactory.getLogger("wombat");
Logger y = LoggerFactory.getLogger("wombat");
```

**x**，**y** 是同一个 logger 对象。

可以通过配置一个 logger，然后在其它地方获取，而不需要传递引用。父级 logger 总是优于子级 logger，并且父级 logger 会自动寻找并关联子级 logger，即使父级 logger 在子级 logger 之后实例化。

logback 环境的配置会在应用初始化的时候完成。最优的方式是通过读取配置文件。

在每个类里面通过指定全限定类名为 logger 的名字来实例化一个 logger 是最好也是最简单的方式。因为日志能够输出这个 logger 的名字，所以这个命名策略能够看出日志的来源是哪里。虽然这是命名 logger 常见的策略，但是 logback 不会严格限制 logger 的命名，你完全可以根据自己的喜好来，你开心就好。

但是，根据类的全限定名来对 logger 进行命名，是目前最好的方式，没有之一。

### Appender 与 Layout

有选择的启用或者禁用日志的输出只是 logger 的一部分功能。logback 允许日志在多个地方进行输出。站在 logback 的角度来说，输出目的地叫做 appender。appender 包括console、file、remote socket server、MySQL、PostgreSQL、Oracle 或者其它的数据库、JMS、remote UNIX Syslog daemons 中。

一个 logger 可以有多个 appender。

logger 通过 `addAppender` 方法来新增一个 appender。对于给定的 logger，每一个允许输出的日志都会被转发到该 logger 的所有 appender 中去。换句话说，appender 从 logger 的层级结构中去继承叠加性。例如：如果 root logger 添加了一个 console appender，所有允许输出的日志至少会在控制台打印出来。如果再给一个叫做 ***L*** 的 logger 添加了一个 file appender，那么 ***L*** 以及 ***L*** 的子级 logger 都可以在文件和控制台打印日志。可以通过设置 additivity = false 来改写默认的设置，这样 appender 将不再具有叠加性。

appender 的叠加性规则如下：

> appender 的叠加性
>
> logger *L* 的日志输出语句会遍历 *L* 和它的父级中所有的 appender。这就是所谓的 appender 叠加性（appender additivity）
>
> 如果 *L* 的某个上级 logger 为 *P*，且 *P* 设置了 additivity = false，那么 *L* 的日志会在层级在 *L* 到 *P* 之间的所有 logger 的 appender，包括 *P* 本身的 appender 中输出，但是不会在 *P* 的上级 appender 中输出。
>
> logger 默认设置 additivity = true。

|      Logger     |  Appender  | Additivity  标识 |          输出目的地         |                                   说明                                  |
| :-------------: | :--------: | :------------: | :--------------------: | :-------------------------------------------------------------------: |
|       root      |     A1     |       不适用      |           A1           |             root logger 为 logger 层级中的最高层，additivity 对它不适用             |
|        x        | A-x1, A-x2 |      True      |     A1, A-x1, A-x2     |                          x 与 root 的 appender                          |
|       x.y       |      无     |      true      |     A1, A-x1, A-x2     |                          x 与 root 的 appender                          |
|      x.y.z      |   A-xyz1   |      true      | A1, A-x1, A-x2, A-xyz1 |                       x 与 x.y 与 root 的 appender                       |
|     security    |    A-sec   |    **false**   |          A-sec         |              因为 additivity = false，所以只有 A-sec 这个 appender             |
| security.access |      无     |      true      |          A-sec         | 因为它的父级 logger security 设置了 additivity = false，所以只有 A-sec 这一个 appender |

通常，用户既想自定义日志的输出地，也想自定义日志的输出格式。通过给 appender 添加一个 *layout* 可以做到。layout 的作用是将日志格式化，而 appender 的作用是将格式化后的日志输出到指定的目的地。**PatternLayout** 能够根据用户指定的格式来格式化日志，类似于 C 语言的 printf 函数。

例：PatternLayout 通过格式化串 "%-4relative \[%thread] %-5level %logger{32} - %msg%n" 会将日志格式化成如下结果：

```java
176  [main] DEBUG manual.architecture.HelloWorld2 - Hello world.
```

第一个参数表示程序启动以来的耗时，单位为毫秒。第二个参数表示当前的线程号。第三个参数表示当前日志的级别。第四个参数是 logger 的名字。“-” 之后是具体的日志信息。

### 参数化日志

考虑到 logback-classic 实现了 SLF4J 的 Logger 接口，一些打印方法可以接收多个传参。这些打印方法的变体主要是为了提高性能以及减少对代码可读性的影响。

对于一些 Logger 如下输出日志：

```java
logger.debug("Entry number: " + i + " is " + String.valueOf(entry[i]));
```

会产生构建消息参数的成本，是因为需要将整数转为字符串，然后再将字符串拼接起来。但是我们是不需要关心 debug 信息是否被记录（强行曲解作者的意思）。

为了避免构建参数带来的损耗，可以在日志记录之前做一个判断，如下：

```java
if(logger.isDebugEnabled()) { 
  logger.debug("Entry number: " + i + " is " + String.valueOf(entry[i]));
}
```

在这种情况下，如果 **logger**没有开启 debug 模式，不会有构建参数带来的性能损耗。换句话说，如果 logger 在 debug 级别，将会有两次性能的损耗，一次是判断是否启用了 debug 模式，一次是打印 debug 日志。在实际应用当中，这种性能上的损耗是可以忽略不计的，因为它所花费的时间小于打印一条日志的时间的 1%。

#### 更好的选择

有一种更好的方式去格式化日志信息。假设 **entry** 是一个 Object 对象：

```java
Object entry = new SomeObject();
logger.debug("The entry is {}", entry);
```

只有在需要打印 debug 信息的时候，才会去格式化日志信息，将 '{}' 替换成 entry 的字符串形式。也就是说在这种情况下，如果禁止了日志的打印，也不会有构建参数上的性能消耗。

下面两行输出的结果是一样的，但是一旦禁止日志打印，第二个变量的性能至少比第一个变量好上 30 倍。

```java
logger.debug("The new entry is " + entry + ".");
logger.debug("The new entry is {}", entry);
```

使用两个参数的例子如下：

```java
logger.debug("The new entry is {}, It replaces {}.", entry, oldEntry);
```

如果需要使用三个或三个以上的参数，可以采用如下的形式：

```java
Object[] paramArray = {newVal, below, above};
logger.debug("Value {} was inserted between {} and {}.", paramArray);
```

### 底层实现初探

在介绍了基本的 logback 组件之后，我们准备介绍一下，当用户调用日志的打印方法时，logback 所执行的步骤。现在我们来分析一下当用户通过一个名为 *com.wombat* 的 logger 调用了 **info()** 方法时，logback 执行了哪些步骤。

**第一步：获取过滤器链**

如果存在，则 **TurboFilter** 过滤器会被调用，Turbo 过滤器会设置一个上下文的阀值，或者根据每一条相关的日志请求信息，例如：**Marker**, **Level**， **Logger**， 消息，**Throwable** 来过滤某些事件。如果过滤器链的响应是 *FilterReply.DENY*，那么这条日志请求将会被丢弃。如果是 *FilterReply.NEUTRAL*，则会继续执行下一步，例如：第二步。如果响应是 *FilterRerply.ACCEPT*，则会直接跳到第三步。

**第二步：应用**[**基本选择规则**](#方法打印以及基本选择规则)

在这步，logback 会比较有效级别与日志请求的级别，如果日志请求被禁止，那么 logback 将会丢弃调这条日志请求，并不会再做进一步的处理，否则的话，则进行下一步的处理。

**第三步：创建一个 LoggingEvent 对象**&#x20;

如果日志请求通过了之前的过滤器，logback 将会创建一个 ch.qos.logback.classic.LoggingEvent 对象，这个对象包含了日志请求所有相关的参数，请求的 logger，日志请求的级别，日志信息，与日志一同传递的异常信息，当前时间，当前线程，以及当前类的各种信息和 MDC。MDC 将会在后续章节进行讨论。

**第四步：调用 appender**

在创建了 LoggingEvent 对象之后，logback 会调用所有可用 appender 的 doAppend() 方法。这些 appender 继承自 logger 上下文。

所有的 appender 都继承了 AppenderBase 这个抽象类，并实现了 doAppend() 这个方法，该方法是线程安全的。AppenderBase 的 doAppend() 也会调用附加到 appender 上的自定义过滤器。自定义过滤器能动态的动态的添加到 appender 上，在过滤器章节会详细讨论。

**第五步：格式化输出**

被调用的 Appender 负责格式化 Logging Event。但是，有些 Appender 将格式化 Logging Event 的任务委托给一个 Layout。Layout 将 LoggingEvent 实例格式化为一个字符串并返回。但需要注意的是，某些 Appender（例如 SocketAppender） 并不会把 Logging Event 转化为一个字符串，而是进行序列化。因此，它们没有并且也不需要 Layout。

**第六步：发送 LoggingEvent**

当日志事件被完全格式化之后将会通过每个 appender 发送到具体的目的地。

下图是 logback 执行步骤的 UML 图：

![点击查看大图](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbRUgZemuDk0Akq-%2FunderTheHoodSequence2.gif?generation=1568702631193314\&alt=media)

### 性能

记录日志经常被提到的一个点是它的计算代价。这是一个合理的考虑，因为一个中等大小的应用都可以产生成千上万的日志。我们的大部分努力都花在了测量以及调整 logback 的性能。但是用户还是应该知道以下有关性能的问题。

1. **当日志记录被关闭时记录日志的性能**

通过设置 root logger 的日志级别为 Level.OFF 来完全关闭日志的打印。当日志完全关闭的时候，日志请求的成本为方法的调用以及整数的比较。在 3.2Ghz 奔腾D 的电脑上的耗时大约为 20 纳秒。

任何方法的调用都有参数构建这个隐含的成本在里面。例如下面这个例子：

```java
x.debug("Entry number: " + i + "is " + entry[i]);
```

把整数 i、entry\[i] 转变为字符串，并且连接在一起，而不管这条日志是否会被打印。

构建参数的成本取决于参数的大小，为了避免不必要的性能损耗，可以使用 SLF4J's 的参数化构建：

```java
x.debug("Entry number: {} is {}", i, entry[i]);
```

这种形式不会有构建参数的成本在里面。与上一个例子做比较，这个的速度会更快。只有当日志信息传递给了附加的 appender 时才会被格式化，而且格式化日志信息的组件也是被优化过的。

1. **当日记记录被打开时是否记录日志的性能**

在 logback 中，不需要遍历 logger 的层次结构。logger 在创建的时候就知道自己的有效级别。如果父级 logger 的级别被更改，则会通知所有子级 logger 注意这个更改。因此，在基于有效级别的基础上，logger 能够准实时的做出决定是否接受或者拒绝日志请求，而不需要考虑它的祖先的级别。

1. **日记记录的实际情况（格式化输出到指定设备）**

这是指格式化日志输出以及发送指定的目的地所需要的成本。我们尽可能快的让 layout（格式化）以及 appender 执行。在本地机器上，将日志输出到文件大概耗费 9-12 微秒的时间。当把日志输出到数据库或者远程服务器上时会上升到几毫秒。

尽管 logback 功能丰富，但是它最重要的目标之一是处理速度，这是仅次于可靠性的要求。为了提高性能，一些 logback 的组件被重写了几次。


# 第三章：logback 的配置

我们开始通过多种配置 logback，以及许多示例的配置脚本。logback 依赖的配置框架 - [Joran](#Joran) 将会在之后的章节介绍

### 配置 logback

在应用程序当中使用日志语句需要耗费大量的精力。根据调查，大约有百分之四的代码用于打印日志。即使在一个中型应用的代码当中也有成千上万条日志的打印语句。考虑到这种情况，我们需要使用工具来管理这些日志语句。

可以通过编程或者配置 XML 脚本或者 Groovy 格式的方式来配置 logback。对于已经使用 log4j 的用户可以通过这个[工具](https://logback.qos.ch/translator/)来把 log4j.properties 转换为 logback.xml。

以下是 logback 的初始化步骤：

1. logback 会在类路径下寻找名为 logback-test.xml 的文件。
2. 如果没有找到，logback 会继续寻找名为 logback.groovy 的文件。
3. 如果没有找到，logback 会继续寻找名为 logback.xml 的文件。
4. 如果没有找到，将会通过 JDK 提供的 [ServiceLoader](https://docs.oracle.com/javase/6/docs/api/java/util/ServiceLoader.html) 工具在类路径下寻找文件 *META-INFO/services/ch.qos.logback.classic.spi.Configurator*，该文件的内容为实现了 [`Configurator`](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/Configurator.html) 接口的实现类的全限定类名。
5. 如果以上都没有成功，logback 会通过 [BasicConfigurator](https://logback.qos.ch/xref/ch/qos/logback/classic/BasicConfigurator.html) 为自己进行配置，并且日志将会全部在控制台打印出来。

最后一步的目的是为了保证在所有的配置文件都没有被找到的情况下，提供一个默认的（但是是非常基础的）配置。

如果你使用的是 maven，你可以在 *src/test/resources* 下新建 logback-test.xml。maven 会确保它不会被生成。所以你可以在测试环境中给配置文件命名为 *logback-test.xml*，在生产环境中命名为 *logback.xml*。

`FAST START-UP` Joran 解析给定的配置文件大概需要耗费 100 毫秒。为了减少启动的时间，你可以使用 [ServiceLoader](https://docs.oracle.com/javase/6/docs/api/java/util/ServiceLoader.html) 来加载自定义的 `Configurator`，并使用 [BasicConfigurator](https://logback.qos.ch/xref/ch/qos/logback/classic/BasicConfigurator.html) 作为一个好的起点（个人的理解是通过继承这个类）。

#### 自动配置 logback

最简单的方式配置 logback 是让它去加载默认的配置。例：

```java
package chapters.configuration;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyApp1 {

    public static final Logger LOGGER = LoggerFactory.getLogger(MyApp1.class);
    
    public static void main(String[] args) {
        LOGGER.info("Entering application.");
        
        Foo foo = new Foo();
        foo.doIt();
        LOGGER.info("Exiting application.");
    }   
}
```

`Foo` 的代码如下：

```jav
package chapters.configuration;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Foo {
    
    public static final Logger LOGGER = LoggerFactory.getLogger(Foo.class);

    public void doIt() {
        LOGGER.debug("Did it again!");
    }
}
```

假设配置文件 *logback-test.xml* 或者 *logback.xml* 不存在，logback 会调用 [BasicConfigurator](https://logback.qos.ch/xref/ch/qos/logback/classic/BasicConfigurator.html) 进行最小的配置。最小的配置包含一个附加到 root logger 上的 `ConsoleAppender`，格式化输出使用 `PatternLayoutEncoder` 对模版 *%d{HH:mm:ss.SSS} \[%thread] %-5level %logger{36} - %msg%n* 进行格式化。root logger 默认的日志级别为 `DEBUG`。

所以，*MyApp1* 的输出信息如下：

```java
16:59:20.161 [main] INFO chapters.configuration.MyApp1 - Entering application.
16:59:20.164 [main] DEBUG chapters.configuration.Foo - Did it again!
16:59:20.164 [main] INFO chapters.configuration.MyApp1 - Exiting application.
```

`MyApp1` 通过调用 `org.slf4j.LoggerFactory` 与 `org.slf4j.Logger` 这两个类与 logback 相关联，并检索会用到的 logger。除了配置 logback 的代码，客户端的代码不需要依赖 logback，因为 SLF4J 允许在它的抽象层下使用任何日志框架，所以非常容易将大量代码从一个框架迁移到另一个框架。

#### 使用 *logback-test.xml* 或 *logback.xml* 自动配置

下面的配置等同于通过 `BasicConfigurator` 进行配置。

```xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> 
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

> 你需要将上面的配置文件命名为 logback.xml 或 logback-test.xml

运行 *MyApp1*，你将会看到相同的结果（你要是不相信，你可以更改模版，看是否生效）。

**在警告或错误的情况下自动打印状态信息**

如果在解析配置文件的过程当中发生了错误，logback 会在控制台打印出它的内部状态数据。如果用户明确的定义了状态监听器，为了避免重复，logback 将不会自动打印状态信息。

在没有警告或错误的情况下，如果你想查看 logback 内部的状态信息，可以通过 `StatusPrinter` 类来调用 `print()` 方法查看具体的信息。

> 在 *MyApp1* 的基础上添加两行代码，并命名为 *MyApp2*

```java
package chapters.configuration;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.core.util.StatusPrinter;

public class MyApp2 {

    public static final Logger LOGGER = LoggerFactory.getLogger(MyApp2.class);
    
    public static void main(String[] args) {
        
        LoggerContext lc = (LoggerContext)LoggerFactory.getILoggerFactory();
        StatusPrinter.print(lc);
        
        LOGGER.info("Entering application.");
        
        Foo foo = new Foo();
        foo.doIt();
        LOGGER.info("Exiting application.");
    }
}
```

输出信息如下：

```java
17:56:47,130 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback-test.xml]
17:56:47,130 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback.groovy]
17:56:47,131 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Found resource [logback.xml] at [file:/D:/E/project/logback-examples/target/classes/logback.xml]
17:56:47,224 |-INFO in ch.qos.logback.classic.joran.action.ConfigurationAction - debug attribute not set
17:56:47,225 |-INFO in ch.qos.logback.core.joran.action.AppenderAction - About to instantiate appender of type [ch.qos.logback.core.ConsoleAppender]
17:56:47,238 |-INFO in ch.qos.logback.core.joran.action.AppenderAction - Naming appender as [STDOUT]
17:56:47,251 |-INFO in ch.qos.logback.core.joran.action.NestedComplexPropertyIA - Assuming default type [ch.qos.logback.classic.encoder.PatternLayoutEncoder] for [encoder] property
17:56:47,328 |-INFO in ch.qos.logback.classic.joran.action.RootLoggerAction - Setting level of ROOT logger to DEBUG
17:56:47,329 |-INFO in ch.qos.logback.core.joran.action.AppenderRefAction - Attaching appender named [STDOUT] to Logger[ROOT]
17:56:47,329 |-INFO in ch.qos.logback.classic.joran.action.ConfigurationAction - End of configuration.
17:56:47,332 |-INFO in ch.qos.logback.classic.joran.JoranConfigurator@7d4793a8 - Registering current configuration as safe fallback point

17:56:47.340 [main] INFO  chapters.configuration.MyApp2 - Entering application.
17:56:47.342 [main] DEBUG chapters.configuration.Foo - Did it again!
17:56:47.342 [main] INFO  chapters.configuration.MyApp2 - Exiting application.

```

在输出信息中，可以清楚的看到内部的状态信息，又称之为 `Status` 对象，可以很方便的获取 logback 的内部状态。

**状态数据**

你可以通过构造一个配置文件来打印状态信息，而不需要通过编码的方式调用 `StatusPrinter` 去实现。只需要在 *configuration* 元素上添加 *debug* 属性。配置文件如下所示。

> 注意：debug 属性只跟状态信息有关，并不会影响 logback 的配置文件，也不会影响 logger 的日志级别。

*Example: sample1.xml*

```xml
<configuration debug="true">
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

> 需要将 sample1.xml 改名为 logback.xml 或 logback-test.xml，不然 logbak 找不到配置文件。以后这种情况不再重复申明。

如果配置文件的配置有问题，logback 会检测到这个错误并且在控制台打印它的内部状态。但是，如果配置文件没有被找到，logback 不会打印它的内部状态信息，因为没有检测到错误。通过编码方式调用 `StatusPrinter.print()` 方法会在任何情况下都打印状态信息。

`强制输出状态信息`：在缺乏状态信息的情况下，要找一个有问题的配置文件很难，特别是在生产环境下。为了能够更好的定位到有问题的配置文件，可以通过系统属性 "\[logback.statusListenerClass]\(#"logback.statusListenerClass" system property)" 来设置 `StatusListener` 强制输出状态信息。系统属性 "logback.statusListenerClass" 也可以用来在遇到错误的情况下进行输出。

设置 `debug="true"` 完全等同于配置一个 `OnConsoleStatusListener` 。具体示例如下：

*Example: onConsoleStatusListener.xml*

```xml
<configuration>

    <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />
    <!-- 剩下的配置跟之前的相同 -->
</configuration>
```

设置 `debug="true"` 与配置 `OnConsoleStatusListener` 的效果完全一样。

#### 通过系统属性指定默认的配置文件

通过系统属性 `logback.configurationFile` 可以指定默认的配置文件的路径。它的值可以是 URL，类路径下的文件或者是应用外部的文件。

```java
java -Dlogback.configurationFile=/path/to/config.xml chapters.configuration.MyApp1
```

> 注意：文件类型只能是 ".xml" 或者 ".groovy"，其它的拓展文件将会被忽略。

因为 `logback.configureFile` 是一个系统属性，所以也可以在应用内进行设置。但是必须在 logger 实例创建前进行设置。

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.classic.util.ContextInitializer;

public class ServerMain {

    static {
        System.setProperty(ContextInitializer.CONFIG_FILE_PROPERTY, "configurationFile.xml");
    }
    
    private static final Logger LOGGER = LoggerFactory.getLogger(ServerMain.class);
    
    public static void main(String[] args) {
        LOGGER.info("xxxxxxxx");
    }
}
```

#### 当配置文件更改时，自动加载

为了让 logback 能够在配置文件改变的时候自动去扫描，需要在 `<configuration>` 标签上添加 `scan=true` 属性。

*Example*

```xml
<configuration scan="true">
    ...
</configuration>
```

默认情况下，一分钟扫描一次配置文件，看是否有更改。通过 `<configuration>` 标签上的 `scanPeriod` 属性可以指定扫描周期。扫描周期的时间单位可以是毫秒、秒、分钟或者小时。

*Example*：

```xml
<configuration scan="true" scanPeriod="30 seconds"
   ...
</configuration>
```

> 注意：如果没有指定时间单位，则默认为毫秒。

当设置了 `scan="true"`，会新建一个 [ReconfigureOnChangeTask](#https://logback.qos.ch/xref/ch/qos/logback/classic/joran/ReconfigureOnChangeTask.html) 任务用于监视配置文件是否变化。`ReconfigureOnChangeTask` 也会自动监视外部文件的变化。

如果更改后的配置文件有语法错误，则会回退到之前的配置文件。

**在堆栈中展示包数据**

> 注意：在 1.1.4 版本中，展示包数据是默认被禁用的。

如果启用了展示包数据，logback 会在堆栈的每一行显示 jar 包的名字以及 jar 的版本号。展示包数据可以很好的解决 jar 版本冲突的问题。但是，这个的代价比较高，特别是在频繁报错的情况下。

`Example`：

```txt
14:28:48.835 [btpool0-7] INFO  c.q.l.demo.prime.PrimeAction - 99 is not a valid value
java.lang.Exception: 99 is invalid
  at ch.qos.logback.demo.prime.PrimeAction.execute(PrimeAction.java:28) [classes/:na]
  at org.apache.struts.action.RequestProcessor.processActionPerform(RequestProcessor.java:431) [struts-1.2.9.jar:1.2.9]
  at org.apache.struts.action.RequestProcessor.process(RequestProcessor.java:236) [struts-1.2.9.jar:1.2.9]
  at org.apache.struts.action.ActionServlet.doPost(ActionServlet.java:432) [struts-1.2.9.jar:1.2.9]
  at javax.servlet.http.HttpServlet.service(HttpServlet.java:820) [servlet-api-2.5-6.1.12.jar:6.1.12]
  at org.mortbay.jetty.servlet.ServletHolder.handle(ServletHolder.java:502) [jetty-6.1.12.jar:6.1.12]
  at ch.qos.logback.demo.UserServletFilter.doFilter(UserServletFilter.java:44) [classes/:na]
  at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1115) [jetty-6.1.12.jar:6.1.12]
  at org.mortbay.jetty.servlet.ServletHandler.handle(ServletHandler.java:361) [jetty-6.1.12.jar:6.1.12]
  at org.mortbay.jetty.webapp.WebAppContext.handle(WebAppContext.java:417) [jetty-6.1.12.jar:6.1.12]
  at org.mortbay.jetty.handler.ContextHandlerCollection.handle(ContextHandlerCollection.java:230) [jetty-6.1.12.jar:6.1.12]
```

启用展示包数据：

```xml
<configuration packagingData="true">
    ...
</configuration>
```

#### 直接调用 `JoranConfigurator`

Logback 依赖的配置文件库为 Joran，是 logback-core 的一部分。logback 的默认配置机制为：通过 `JoranConfigurator` 在类路径上寻找默认的配置文件。你可以通过直接调用 `JoranConfigurator` 的方式来重写 logback 的默认配置机制。

`Example`：直接调用 `JoranConfigurator`

```java
package chapters.configuration;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.qos.logback.access.joran.JoranConfigurator;
import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.core.joran.spi.JoranException;
import ch.qos.logback.core.util.StatusPrinter;

public class MyApp3 {

	private static final Logger LOGGER = LoggerFactory.getLogger(MyApp3.class);
	
	public static void main(String[] args) {
		
		LoggerContext context = (LoggerContext)LoggerFactory.getILoggerFactory();
		JoranConfigurator joranConfigurator = new JoranConfigurator();
		joranConfigurator.setContext(context);
		context.reset();
		try {
			joranConfigurator.doConfigure(args[0]);
		} catch (JoranException e) {
			e.printStackTrace();
		}
		
		StatusPrinter.printInCaseOfErrorsOrWarnings(context);
		
		LOGGER.info("Entering application");
		
		Foo foo = new Foo();
		foo.doIt();
		LOGGER.info("Exiting application");
	}
}

```

> 注意：对于多个步骤的配置，`context.reset()` 不需要调用（不是很理解这句话的意思）。

#### 查看内部状态信息

logback 通过 [StatusManager](https://logback.qos.ch/xref/ch/qos/logback/core/status/StatusManager.html) 的对象来收集内部的状态信息，这个对象可以通过 `LoggerContext` 来获取。

对于一个给定的 `StatusManager`，你可以获取 logback 上下文所有的状态信息。为了保持内存的使用在一个合理的水平，`StatusManager` 的默认实现包含两个部分：头部与尾部。头部存储第一个 *H* 状态的消息，尾部存储最后一个 *T* 状态的消息。目前 *H=T=150*，这个值在以后可能会改变。

logback-classic 包含一个名叫 ViewStatusMessagesServlet 的 servlet。这个 servlet 打印当前 LoggerContext 的 StatusManager 的内容，通过 html 进行输出。

*Example*：

![statusMessages](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbX8BJwZS6gmxmHJ%2FstatusMessages.png?generation=1568702658310871\&alt=media)

在 *WEB-INF/web.xml* 中添加如下代码：

```xml
<servlet>
    <servlet-name>ViewStatusMessages</servlet-name>
	<servlet-class>ch.qos.logback.classic.ViewStatusMessagesServlet</servlet-class>
</servlet>

<servlet-mapping>
    <servlet-name>ViewStatusMessages</servlet-name>
	<url-pattern>/lbClassicStatus</url-pattern>
</servlet-mapping>
```

然后可以通过 `http://host/yourWebapp/lbClassicStatus` 进行访问。

#### 监听状态信息

通过给 `StatusManager` 附加一个 `StatusListener`，可以对状态信息进行获取。特别是在配置好 logback 之后。注册一个状态监听器可以很方便的监听 logback 的内部状态，并且不需要人工的干预。

`StatusListener` 有一个名为 `OnConsoleStatusListener` 的实现类，可以将状态信息在控制台打印出来。

*Example*：

```java
public class AddStatusListenerApp {

	public static void main(String[] args) {

		LoggerContext lc = (LoggerContext)LoggerFactory.getILoggerFactory();
		StatusManager statusManager = lc.getStatusManager();
		OnConsoleStatusListener onConsoleStatusListener = new OnConsoleStatusListener();
		statusManager.add(onConsoleStatusListener);
		
		Logger logger = LoggerFactory.getLogger("myApp");
		logger.info("Entering application");
		
		Foo foo = new Foo();
		foo.doIt();
		logger.info("Exiting application");
		
		StatusPrinter.print(statusManager);
	}
}
```

> 注意：注册的状态监听器只会获取注册之后产生的状态消息，而不会获取注册之前产生的消息。所以建议在最开始的时候直接进行配置。

可以在配置文件中配置多个状态监听器。

*Example*：

```xml
<configuration>
  <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />  

  ... the rest of the configuration file  
</configuration>
```

#### 系统属性 "logback.statusListenerClass"

通过设置 java 的系统属性来配置状态监听器。

*Example*：

```bash
java -Dlogback.statusListenerClass=ch.qos.logback.core.status.OnConsoleStatusListener
```

logback 子级实现了几个监听器。[OnConsoleStatusListener](https://logback.qos.ch/xref/ch/qos/logback/core/status/OnConsoleStatusListener.html) 用于在控制台打印状态消息。[OnErrorConsoleStatusListener](https://logback.qos.ch/xref/ch/qos/logback/core/status/OnErrorConsoleStatusListener.html) 用于在控制台打印显示错误的状态信息。[NopStatusListener](https://logback.qos.ch/xref/ch/qos/logback/core/status/NopStatusListener.html) 会丢弃掉状态信息。

> 注意：在配置期间，任何的状态监听器被注册，或者通过 java 系统变量指定 `logback.statusListenerClass` 的值，[在警告或错误的情况下自动打印状态信息](#在警告或错误的情况下自动打印状态信息) 将会被禁用。

可以通过设置 java 系统变量 `logback.statusListenerClass` 的值来禁用一切状态信息的打印。

```bash
java -Dlogback.statusListenerClass=ch.qos.logback.core.status.NopStatusListener
```

### 停止 logback-classic

为了释放 logback-classic 所使用的资源，停止使用 logger context 是一个好注意。停止 context 将会关闭所有在 logger 上定义的 appender，并且有序的停止正在活动的线程。

```java
import org.sflf4j.LoggerFactory;
import ch.qos.logback.classic.LoggerContext;
...

LoggerContext loggerContext = (LoggerContext) LoggerFactory.getILoggerFactory();
loggerContext.stop();
```

在 web 应用中，为了停止 logback-classic 并释放相关资源，上面的代码可以在 `ServletContextListener` 类的 [contextDestroyed](https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContextListener.html#contextDestroyed\(javax.servlet.ServletContextEvent\)) 方法中被调用。从版本 1.1.10 开始，相应的 `ServletContextListener` 会被自动安装。

**通过 shutdown hook 停止 logback-classic**

> 个人觉得 hook 可以理解为钩子或者开关，但是还是觉得照写会更好理解一点。

指定一个 JVM shutdown hook 可以非常方便的关闭 logback 并释放资源。

```xml
<configuration debug="true">
    <!-- 如果缺失 class 属性，则会默认加载 ch.qos.logback.core.hook.DefaultShutdownHook -->
    <shutdownHook/>
</configuration>
```

> 注意：可以通过 *class* 属性指定一个 shutdown hook 的名字。

默认的 shutdown hook 为 [DefaultShutdownHook](https://logback.qos.ch/apidocs/ch/qos/logback/core/hook/DefaultShutdownHook.html)，在一个指定的时间后（默认是 0）会停掉 context。但是允许 context 在 30s 内完成日志文件的打包。在独立的 java 应用程序中，在配置文件中添加 `<shutdownHook/>` 可以确保任何日志打包任务完成之后，JVM 才会退出。在 web 应用程序中，[webShutdownHook](https://logback.qos.ch/manual/configuration.html#webShutdownHook) 会自动安装，`<shutdownHook/>` 将会变的多余且没有必要。

**在 web 应用中使用 WebShutdownHook 停止 logback-classic**

`SINCE 1.1.10` logback-classic 会自动要求 web 服务安装 [LogbackServletContainerInitializer](https://logback.qos.ch/apidocs/ch/qos/logback/classic/servlet/LogbackServletContainerInitializer.html)（实现了 `ServletContainerInitializer` 接口，在 servlet-api 3.x 或以后的版本才有效）。这个初始化程序将会依次实例化 [LogbackServletContextListener](https://logback.qos.ch/apidocs/ch/qos/logback/classic/servlet/LogbackServletContextListener.html) 的实例。在 web 应用停止或者重载的时候会停掉当前 logback-classic 的 context。

> 我表示不是很懂这种做法有何意义，难道应用都停止了，context 还会在运行？这就是作者说的非常多余跟没有必要吗？

可以在 web.xml 中禁止 `LogbackServletContextListener` 的实例化。

*Example*：

```xml
<web-app>
	<context-param>
    	<param-name>logbackDisableServletContainerInitializer</param-name>
        <param-value>true</param-value>
    </context-param>
    ...
</web-app>
```

`logbackDisableServletContainerInitializer` 也可以通过 java 系统属性或者系统的环境变量来设置。优先级为：web 应用 > java 系统属性 > 系统环境变量

### 配置文件的语法

logback 允许你重新定义日志的行为而不需要重新编译代码，你可以轻易的禁用调应用中某些部分的日志，或者将日志输出到任何地方。

logback 的配置文件非常的灵活，不需要指定 DTD 或者 xml 文件需要的语法。但是，最基本的结构为 `<configuration>` 元素，包含 0 或多个 `<appender>` 元素，其后跟 0 或多个 `<logger>` 元素，其后再跟最多只能存在一个的 `<root>` 元素。基本结构图如下：

![basicSyntax](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbXBvhb68uut2e7r%2FbasicSyntax.png?generation=1568702658354270\&alt=media)

**标签名大小写敏感**

在 logback 版本 0.9.17 之后，显示规定的标签名不区分大小写。例如：`<logger>`、`<Logger`、`<LOGGER>` 这些都是有效的标签名。xml 风格的规则仍然适用。如果你有一个开始标签为 \<xyz>，那么必须要有一个结束标签 \</xyz>。\</XyZ> 则是错误的。根据[默认规则](#默认规则)，标签名字是大小写敏感的，除了第一个字母。所以，\<xyz> 与 \<Xyz> 是一样的，但是 \<xYz> 是错误的。默认规则遵循驼峰命名法。很难说清楚一个标签遵循什么规则，如果你不知道给定的标签遵循哪种规则，那么使用驼峰命名法总是正确的。

**配置 logger**

现在你至少应该对[等级继承规则](https://github.com/Volong/logback-chinese-manual/blob/0197a2d5a3820d9c1756c680c2e21e934904c6a6/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%9C%89%E6%95%88%E7%AD%89%E7%BA%A7%E5%8F%88%E7%A7%B0%E4%B8%BA%E7%AD%89%E7%BA%A7%E7%BB%A7%E6%89%BF)与[基本规则](https://github.com/Volong/logback-chinese-manual/blob/0197a2d5a3820d9c1756c680c2e21e934904c6a6/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%96%B9%E6%B3%95%E6%89%93%E5%8D%B0%E4%BB%A5%E5%8F%8A%E5%9F%BA%E6%9C%AC%E9%80%89%E6%8B%A9%E8%A7%84%E5%88%99)有所了解.。

通过 `<logger>` 标签来过 logger 进行配置，一个 `<logger>` 标签必须包含一个 *name* 属性，一个可选的 *level* 属性，一个可选 *additivity* 属性。`additivity` 的值为 *true* 或 *false*。`level` 的值为 TRACE，DEBUG，INFO，WARN，ERROR，ALL，OFF，INHERITED，NULL。当 `level` 的值为 INHERITED 或 NULL 时，将会强制 logger 继承上一层的级别。

`<logger>` 元素至少包含 0 或多个 `<appender-ref>` 元素。每一个 appender 通过这种方式被添加到 logger 上。与 log4j 不同的是，logbakc-classic 不会关闭或移除任何之前在 logger 上定义好的的 appender。

**配置 root logger**

root logger 通过 `<root>` 元素来进行配置。它只支持一个属性——`level`。它不允许设置其它任何的属性，因为 additivity 并不适用 root logger。而且，root logger 的名字已经被命名为 "ROOT"，也就是说也不支持 name 属性。level 属性的值可以为：TRACE、DEBUG、INFO、WARN、ERROR、ALL、OFF，但是不能设置为 INHERITED 或 NULL。

跟 `<logger` 元素类似，`<root>` 元素可以包含 0 或多个 `<appender-ref>` 元素。

**例子**

如果我们不想看到属于 "chapters.configuration" 组件中任何的 DEBUG 信息。

*Example*：sample2.xml

```xml
<configuration>
	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
		</encoder>
	</appender>
	
	<logger name="chapters.configuration" level="INFO" />

	<root level="DEBUG">
		<appender-ref ref="STDOUT" />
	</root>
</configuration>
```

运行 *MyApp3*，可以看到如下的输出信息：

```java
21:52:48.726 [main] INFO  chapters.configuration.MyApp3 - Entering application
21:52:48.728 [main] INFO  chapters.configuration.MyApp3 - Exiting application
```

可以看到，["chapters.configuration.Foo"](https://logback.qos.ch/xref/chapters/configuration/Foo.html) 类中的 debug 信息没有被输出。

你可以配置任何 logger 的日志级别。在下一个例子中，我们设置 *chapters.configurations* 的 logger 日志级别为 INFO，同时设置 *chapters.configuration.Foo* 的 logger 日志级别为 DEBUG。

*Example*：sample3.xml

```xml
<configuration>
	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>
				%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
			</pattern>
		</encoder>
	</appender>
	
	<logger name="chapters.configuration" level="INFO" />
	
	<logger name="chapters.configuration.Foo" level="DEBUG" />
	
	<root level="DEBUG">
		<appender-ref ref="STDOUT" />
	</root>
</configuration>
```

运行 *MyApp3* 可以看到如下的输出信息：

```java
22:06:43.500 [main] INFO  chapters.configuration.MyApp3 - Entering application
22:06:43.502 [main] DEBUG chapters.configuration.Foo - Did it again!
22:06:43.502 [main] INFO  chapters.configuration.MyApp3 - Exiting application
```

下面的表格列出了 `JoranConfigurator` 通过 *sample3.xml* 配置 logback 后，logger 以及其对应的日志级别。

| Logger name                   |  指定级别 |  有效级别 |
| ----------------------------- | :---: | :---: |
| root                          | DEBUG | DEBUG |
| chapters.configuration        |  INFO |  INFO |
| chapters.configuration.MyApp3 |  null |  INFO |
| chapters.configuration.Foo    | DEBUG | DEBUG |

`MyApp3` 类中的两条日志消息的级别都为 INFO，Foo.doIt() 中的 DEBUG 信息也能够进行输出。

> 注意：root logger 的日志级别永远不会设置成一个非空的值，默认是 DEBUG。

[基本选择法](https://github.com/Volong/logback-chinese-manual/blob/0197a2d5a3820d9c1756c680c2e21e934904c6a6/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%96%B9%E6%B3%95%E6%89%93%E5%8D%B0%E4%BB%A5%E5%8F%8A%E5%9F%BA%E6%9C%AC%E9%80%89%E6%8B%A9%E8%A7%84%E5%88%99) 取决于被调用 logger 的有效日志级别，而不是 appender 所依附的 logger 的日志级别。logback 会首先判断日志语句是否可以被打印，如果可以，则会调用在 logger 层级结构中找到的 appender，且不考虑 appender 所依附的 logger 的日志级别是什么。下面的例子说明了这一点。

*Example*：sample4.xml

```xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <logger name="chapters.configuration" level="INFO" />
    
    <root level="OFF">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

如下表格展示了应用 sample4.xml 之后的各 logger 的日志级别。

| logger name                   | 分配级别 | 有效级别 |
| ----------------------------- | ---- | ---- |
| root                          | OFF  | OFF  |
| chapters.configuration        | INFO | INFO |
| chapters.configuration.MyApp3 | null | INFO |
| chapters.configuration.Foo    | null | INFO |

ConsoleAppender 的名字为 *STDOUT*， *sample4.xml* 中唯一的 appender，它所依附的 root logger 的 level = OFF。但是，运行 *MyApp3* 还是得到日志输出：

```java
10:47:34.310 [main] INFO  chapters.configuration.MyApp3 - Entering application
10:47:34.313 [main] INFO  chapters.configuration.MyApp3 - Exiting application
```

很明显，root logger 没有影响到其他的 logger，因为 `chapters.configuration.MyApp3` 与 `chapters.configuration.Foo` 类的日志级别为 INFO。即使在 java 代码中没有直接引用 *chapters.configuration* 这个 logger，但是它是存在，因为它在配置文件中声明了。

**配置 appender**

appender 通过 `<appender>` 元素进行配置，需要两个强制的属性 *name* 与 *class*。*name* 属性用来指定 appender 的名字，*class* 属性指定类的全限定名用于实例化。`<appender>` 元素可以包含 0 或一个 `<layout>` 元素，0 或多个 `<encoder>` 元素，0 或多个 `<filter>` 元素。除了这三个公共的元素之外，`<appender>` 元素可以包含任意与 appender 类的 JavaBean 属性相一致的元素。无缝地支持一个给定的 logback 组件的任意属性是 Joran 的主要优势之一，这将在后面的章节中讨论。下图展示了公共结构。注意：下图没有显示对 JavaBean 属性的支持。

![appenderSyntax](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbXHAcSA20y3Msfs%2FappenderSyntax.png?generation=1568702658529638\&alt=media)

`<layout>` 元素需要一个强制的 class 属性去指定一个类的全限定名，用于实例化。与 `<appender>` 元素一样，`<layout>` 元素也可以包含与 layout 实例相关的属性。一个常见的使用场景是：layout 的 class 属性被设置为 `PatternLayout`，如果是这种场景的话，class 属性可以省略（参考：[默认类映射](#默认类映射)）。

`<encoder>` 元素需要一个强制的 class 属性去指定一个类的全限定名，用于实例化。一个常见的使用场景是：encoder 的 class 属性被设置为 `PatternLayoutEncoder`，如果是这种场景的话，class 属性可以省略（参考：[默认类映射](#默认类映射)）。

通过多个 appender 输出日志就像定义多个 appender 以及将它们关联到 logger 上一样简单。

*Example*：multiple.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>myApp.log</file>
		<encoder>
			<pattern>
				%date %level [%thread] %logger{10} [%file:%line] %msg%n
			</pattern>
		</encoder>
	</appender>
	
	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>
				%msg%n
			</pattern>
		</encoder>
	</appender>
	
	<root level="debug">
		<appender-ref ref="FILE" />
		<appender-ref ref="STDOUT" />
	</root>
</configuration>
```

这个配置文件定义了两个 appender：*FILE* 和 *STDOUT*。*FILE* appender 将日志输出到 *myApp.log* 文件。encoder 通过 `PatternLayoutEncoder` 输出日期、日志等级、线程名、logger 的名字、可以定位日志来源的文件以及所在行、具体的日志信息以及行分隔符。第二个 appender 是 `STDOUT`，将日志输出到控制台。它的 encoder 仅仅输出日志信息以及行分隔符。

appender 通过 *appender-ref* 元素附加到 root logger 上。每一个 appender 都有自己 encoder。encoder 通常不会设计成给所有的 appender 共享。对于 layout 也是如此。因此，logback 不会提供任何共享 encoder 和 layout 的语法。

**重复使用 appender**

在默认的情况下，appender 是可以重复使用的：logger 可以通过附加到本身的 appender 输出日志，同样的也可以附加到起祖先的身上，并输出日志。因此，如果同一个 appender 附加到多个 logger 身上，那么就导致日志重复打印。

*Example*：duplicate.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
		</encoder>
	</appender>
	
	<logger name="chapters.configuration">
		<appender-ref ref="STDOUT" />
	</logger>
	
	<root level="debug">
		<appender-ref ref="STDOUT" />
	</root>
</configuration>
```

运行 *MyApp3*，将会输出如下结果：

```java
22:43:35.469 [main] INFO  chapters.configuration.MyApp3 - Entering application
22:43:35.469 [main] INFO  chapters.configuration.MyApp3 - Entering application
22:43:35.471 [main] DEBUG chapters.configuration.Foo - Did it again!
22:43:35.471 [main] DEBUG chapters.configuration.Foo - Did it again!
22:43:35.472 [main] INFO  chapters.configuration.MyApp3 - Exiting application
22:43:35.472 [main] INFO  chapters.configuration.MyApp3 - Exiting application
```

注意日志重复输出了，因为 appender *STDOUT* 附加到了两个 logger 身上：root 以及 *chapters.configuration*。因为 root logger 是所有 logger 的祖先，*chapters.configuration* 是 *chapters.configuration.MyApp3* 以及 *chapters.configuraion.Foo* 的父级。每一次日志请求都会被打印两次，一次是通过 *STDOUT*，一次是通过 *root*。

appender 的叠加性并不是为新用户设置的陷阱。它是 logback 非常方便的一个特性。例如，你可以让系统中所有的日志输出到控制台上，而其它特定的日志输出到特定的 appender 中。

*Example*： restricted.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>myApp.log</file>
		<encoder>
			<pattern>%date %level [%thread] %logger{10} [%file:%line] %msg%n</pattern>
		</encoder>
	</appender>
	
	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>%msg%n</pattern>
		</encoder>
	</appender>
	
	<logger name="chapters.configuration">
		<appender-ref ref="FILE" />
	</logger>
	
	<root level="debug">
		<appender-ref ref="STDOUT" />
	</root>
</configuration>
```

在这个例子中，控制台会打印所有的日志，而只有属于 *chapters.configuration* 的 logger 以及它的子级 logger 的日志才会输出到 *myApp.log* 文件。

**重写默认的累加行为**

如果默认的累积行为对你来说不适合，你可以设置 additivity = false。

*Example*：additivityFlag.xml

```xml
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <file>foo.log</file>
        <encoder>
            <pattern>%date %level [%thread] %logger{10} [%file : %line] %msg%n</pattern>
        </encoder>
    </appender>
    
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%msg%n</pattern>
        </encoder>
    </appender>
    
    <logger name="chapters.configuration.Foo" additivity="false">
        <appender-ref ref="FILE" />
    </logger>
    
    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

在这个例子中，*FILE* appender 附加到了名为 *chaoters.configuration.Foo* 的 logger 上。而且，*chapters.configuration.Foo* 设置了 additivity = false，那么这个 logger 的日志将会通过 *FILE* 这个 appender 输出，但是它的父级 logger 将不会输出属于这个 logger 的日志。运行 *MyApp3*，属于 *chapters.configuration.MyApp3* 这个 logger 的日志将会在控制台输出，但是属于 *chapters.configuration.Foo* 这个 logger 的日志只会在 *foo.log* 这个文件看到。

#### 设置 context 的名字

在之前的\[章节]\(#Logger 上下文)中提到，每一个 logger 都会附加到一个 logger context 上去。默认这个 logger context 的名字为 "default"。但是你可以通过 `<contextName>` 设置其它的名字。但是如果设置过一次就不能[再设置](#https://logback.qos.ch/apidocs/ch/qos/logback/core/ContextBase.html#setName\(java.lang.String\))。当多个应用输出日志到同一个目的地，设置 logger context 的名字可以更好的区分。

*Example*：contextName.xml

```xml
<configuration>
    <contextName>myAppName</contextName>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d %contextName [%t] %level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

#### 变量替换

**`注意`**：早期版本使用的是属性替换而不是变量替换

**变量的定义**

logback 支持变量的定义以及替换，变量有它的作用域。而且，变量可以在配置文件中，外部文件中，外部资源文件中，甚至动态定义。

*Example*：variableSubstitution1.xml

```xml
<configuration>
	<property name="USER_NAME" value="/data/logs" />

	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>${USER_NAME}/myApp.log</file>
		<encoder>
			<pattern>%msg%n</pattern>
		</encoder>
	</appender>
	
	<root level="debug">
		<appender-ref ref="FILE" />
	</root>	
</configuration>
```

这个例子中，在配置文件的开始定义了一个变量，之后通过引用这个变量指定了日志文件的路径。

*Example*：variableSubstitution2.xml

```xml
<configuration>
	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>${USER_HOME}/myApp.log</file>
		<encoder>
			<pattern>%msg%n</pattern>
		</encoder>
	</appender>
	
	<root level="debug">
		<appender-ref ref="FILE" />
	</root>	
</configuration>
```

这个例子中，在 java 的系统变量中定义一个同样的变量名，达到的效果是一样的。可以通过如下的方式去运行：

```
java -DUSER_HOME="/data/logs" MyApp3

```

当需要定义多个变量时，可以将这些变量放到一个单独的文件中。

*Example*：variableSubstitution3.xml

```xml
<configuration>
	<property file="F:\project\logback-examples\src\main\resources\variables1.properties"/>
	
	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>${USER_HOME}/myApp.log</file>
		<encoder>
			<pattern>%msg%n</pattern>
		</encoder>
	</appender>
	
	<root level="debug">
		<appender-ref ref="FILE" />
	</root>
</configuration>
```

这个配置文件包含了一个对外部文件的引用：*variables1.properties*。这个外部文件包含一个变量：

*Example*：variables1.properties

```properties
USER_HOME=/data/logs
```

也可以引用 classpath 下的资源文件：

```xml
<configuration>
	<property resource="resource1.properties" />
	
	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>${USER_HOME}/myApp.log</file>
		<encoder>
			<pattern>%msg%n</pattern>
		</encoder>
	</appender>
	
	<root level="debug">
		<appender-ref ref="FILE" />
	</root>
</configuration>
```

**作用域**

属性的作用域分别为本地（local scope）、上下文（context scope）、系统（system scope）。默认为本地作用域。

`本地（local scope）`：本地范围内的属性存在配置文件的加载过程中。配置文件每加载一次，变量就会被重新定义一次。

`上下文（context scope）`：上下文范围内的属性会一直存在上下文被清除。

`系统（system scope）`：系统范围内的属性，会插入到 JVM 的系统属性中，跟随 JVM 一同消亡。

在进行变量替换的时候，会先从本地范围去找，再从上下文去找，再从系统属性中去找，最后会去系统的环境变量中去找。

可以通过 `<property>`、`<define>`、`<insertFromJNDI>` 元素的 *scope* 属性来设置变量的作用范围。*scope* 属性可能的值为：local，context，system。如果没有指定，则默认为 local。

*Example*：contextScopedVariable.xml

```xml
<configuration>
    <property scope="context" name="nodeId" value="firstNode"/>
    
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <file>/data/${nodeId}/myApp.log</file>
        <encoder>
            <pattern>%msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

在这个例子中，*nodeId* 这个变量被定义在上下文范围，它在每个日志事件，甚至通过序列化发送到远程服务器上都有效。

#### 变量的默认值

在某些情况下，如果某个变量没有被声明，或者为空，默认值则非常有用。在 bash shell 中，默认值可以通过 **":-"** 来指定。例如：假设变量 *aName* 没有被定义，*"${aNme:-golden}"* 会被解释成 "golden" 。

#### 变量的嵌套

变量的名字、默认值、以及值都可以引用其它的变量。

**嵌套值**

一个变量的值可以包含对其它变量的引用。

*Example*：variables2.properties

```properties
USER_HOME=/data/logs
fileName=myApp.log
destination=${USER_HOME}/${fileName}
```

*Example*：variableSubsitution4.xml

```xml
<configuration>
    <!-- 注: 官网的例子不是 resource 而是 file -->
    <property resource="variables2.properties" />
    
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <file>${destination}</file>
        <encoder>
            <pattern>%msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

**名字嵌套**

变量的名字可以包含对其它变量的引用。例如：如果变量 *userid=alice*，那么 "${${userid}.password}" 就是对变量名为 "alice.passowrd" 的引用。

**默认值嵌套**

一个变量的默认值可以引用另一个变量。例如：假设变量 "id" 没有被定义，变量 "userid" 的值为 "alice"，那么表达式 "${id:-${userid}}" 的值为 "alice"。

#### HOSTNAME 属性

`HOSTNAME` 在配置期间会被自动定义为上下文范围内。

*Example*：

```xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>${HOSTNAME} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

#### CONTEXT\_NAME 属性

通过名字可以看出来，`CONTEXT_NAME` 属性对应当前上下文的名字。

```xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>${CONTEXT_NAME} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

#### 动态定义属性

可以通过 `<define>` 元素动态的定义变量。这个元素需要两个强制的属性：*name*、*class*。*name* 属性用来定义变量的名字，*classs* 属性用来引用实现了 [PropertyDefiner](https://logback.qos.ch/xref/ch/qos/logback/core/spi/PropertyDefiner.html) 接口的类。`PropertyDefiner` 实例的 `getPropertyValue()` 的返回值就是变量的值。还可以通过 *scope* 属性指定变量的[作用域](#作用域)。

```xml
<configuration>

  <define name="rootLevel" class="chapters.configuration.PropertyDefiner1">
    <shape>round</shape>
    <color>brown</color>
    <size>24</size>
  </define>
 
  <root level="${rootLevel}"/>
</configuration>
```

shape，color，size 都是 "chapters.configuration.PropertyDefiner1" 的属性。只要在实现类里面，各属性有对应的 set 方法，logback 就可以通过配置文件给各属性注入对应的值。

目前，logback 已经有了几个简单的实现类：

|                                                                    类名                                                                   | 描述                                                            |
| :-------------------------------------------------------------------------------------------------------------------------------------: | ------------------------------------------------------------- |
| [`CanonicalHostNamePropertyDefiner`](https://logback.qos.ch/apidocs/ch/qos/logback/core/property/CanonicalHostNamePropertyDefiner.html) | 将变量的值设置为本地的主机名。注意：获取主机名可能需要花费几秒的时间。                           |
|        [`FileExistsPropertyDefiner`](https://logback.qos.ch/apidocs/ch/qos/logback/core/property/FileExistsPropertyDefiner.html)        | 如果通过 `path` 属性指定的文件存在，则设置变量为 "true"，否则设置为 "false"。            |
|      [`ResourceExistsPropertyDefiner`](https://logback.qos.ch/apidocs/ch/qos/logback/core/property/FileExistsPropertyDefiner.html)      | 如果通过 `resource` 属性指定的资源文件在类路径中存在，则设置变量为 "true"，否则设置为 "false"。 |

#### 配置文件中的条件处理

开发者通常需要在多个环境中切换配置文件，例如：开发，测试和生产。这些配置文件有大量相同的地方，只有少数地方不同。为了避免重复，logback 在配置文件中支持通过 `<if>`、`<then>`、`<else>` 元素作为条件语句来区分不同的环境。条件处理需要 [Janino](https://logback.qos.ch/setup.html#janino) 环境的支持。

*Example*：

```xml
    <if condition="条件表达式">
        <then>
            ...
        </then>
	</if>
	
	<if condition="条件表达式">
        <then>
            ...
        </then>
        <else>
            ...
        </else>
	</if>
```

条件表达式只能是上下文变量或者系统变量。因为值是通过参数传递的，`property()` 方法或者其等价的 `p()` 方法属性的值。例如：如果要获取变量 "k" 的值，可以通过 `property("k")` 或者 `p("k")` 来获取。如果 "k" 没有定义，那么方法将会返回空字符串。所以不需要去判断是否为 null。

`isDefined()` 方法可以用来判断变量是否已经被定义。例如：可以通过 `isDefined("k")` 来判断 k 是否已经定义。还可以通过 `isNull()` 方法来判断变量是否为 null。例如：`isNull("k")`。

```xml
<configuration debug="true">
	<if condition='property("HOSTNAME").contains("volong")'>
		<then>
			<appender name="CON" class="ch.qos.logback.core.ConsoleAppender">
				<encoder>
					<pattern>%d %-5level %logger{35} - %msg %n</pattern>
				</encoder>
			</appender>
			<root>
				<appender-ref ref="CON" />
			</root>
		</then>
	</if>
	
	<appender name="FILE" class="ch.qos.logback.core.FileAppender">
		<file>${randomOutputDir}/conditional.log</file>
		<encoder>
			<pattern>${HOSTNAME} %d %-5level %logger{35} - %msg %n</pattern>
		</encoder>
	</appender>
	
	<root level="ERROR">
		<appender-ref ref="FILE" />
	</root>
</configuration>
```

条件处理语句与嵌套的 if-else 语句在 `<configuration>` 元素内都是可以使用的。但是 xml 的语法非常的繁琐，不适合作为通用变成语言的基础。因此，不建议使用过多的条件语句，因为别人看了难以理解，对你自己也是如此。

#### 从 JNDI 中获取变量

在某些情况下，如果从 JNDI 中获取变量的值。`<insertFromJNDI>` 元素能够获取存储在 JNDI 中的元素并插入到本地的上下文中，然后通过 `as` 属性获取具体的值。还可以通过[作用域](#作用域)将变量插入到不同的作用域中。

*Example*：insertFromJNDI.xml

```xml
<!-- appName 的配置在 web.xml 中 
	使用的是 eclipse 的 jetty 插件运行的
	运行时候的配置：右键点击项目 -> Run Configurations -> Jetty 选项卡下选择 Show Advanced Options -> 选中 JNDI Support -> 在运行就可以了
-->
<configuration>
	<insertFromJNDI env-entry-name="java:comp/env/appName" as="appName" />
	<contextName>${appName}</contextName>

	<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>%d %contextName %level %msg %logger{50}%n</pattern>
		</encoder>
	</appender>

	<root level="DEBUG">
		<appender-ref ref="CONSOLE" />
	</root>
</configuration>
```

#### 引入文件

通过 `<include>` 元素可以引入外部的配置文件。

*Example*：containingConfig.xml

```xml
<configuration>
    <include file="src/main/resources/includedConfig.xml" />
    
    <root level="DEBUG">
        <appender-ref ref="includedConsole" />
    </root>
</configuration>
```

目标文件必须是由 `<included>` 元素包裹的。

*Example*：includedConfig.xml

```xml
<included>
    <appender name="includedConsole" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d - %m%n</pattern>
        </encoder>
    </appender>
</included>
```

可以通过如下几个属性引入文件：

* **通过文件引入**：

  可以通过 `file` 属性引入外部文件。可以通过相对路径或者绝对路径来引入。相对路径是指相对应用程序的路径。
* **通过资源文件引入**

  可以通过 `resource` 属性来引入位于 classpath 路径下的资源文件。

  ```xml
  <include resource="includedConfig.xml"/>
  ```
* **通过 url 引入文件**

  可以通过 `url` 属性来引入外部文件。

  ```xml
  <include url="http://some.host.com/includedConfig.xml"/>
  ```

如果 logback 没有通过 `include` 元素找到指定的配置文件，会在控制台打印出内部状态信息。如果引入的外部配置文件是可选的，可以设置 `optional=true`。

```xml
<include optional="true" ..../>
```

### 添加上下文监听器

[LoggerContextListener](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/LoggerContextListener.html) 接口的实例监听上下文生命周期内的事件。

`JMXConfigurator` 是 `LoggerContextListener` 接口的一个实现。

#### 更改传播级别

在 0.9.25 版本，logback-classic 通过 `LoggerContextListener` 的实现类 [LevelChangePropagator](https://logback.qos.ch/xref/ch/qos/logback/classic/jul/LevelChangePropagator.html) 来更改 logback-classic 中的 logger 传播到 java.util.logging 中的日志级别。这些传播消除了禁止打印日志时的性能损耗。[LogRecord](http://download.oracle.com/javase/1.5.0/docs/api/java/util/logging/LogRecord.html?is-external=true) 实例仅仅会在允许打印日志的情况下通过 SFL4J 传播到 logback。

配置 `LevelChangePropagator`：

```xml
<configuration debug="true">
  <contextListener class="ch.qos.logback.classic.jul.LevelChangePropagator"/>
  .... 
</configuration>
```

`resetJUL` 属性会重置 j.u.l 中的所有 logger 的等级配置。但是之前配置的将不会受到影响。

```xml
<configuration debug="true">
  <contextListener class="ch.qos.logback.classic.jul.LevelChangePropagator">
    <resetJUL>true</resetJUL>
  </contextListener>
  ....
</configuration>
```


# 第四章：Appenders

## 第四章：Appenders

### 什么是 Appender

logback 将写入日志事件的任务委托给一个名为 appender 的组件。Appender 必须实现 [`ch.qos.logback.core.Appender`](https://logback.qos.ch/xref/ch/qos/logback/core/Appender.html) 接口。该接口的方法如下：

```java
package ch.qos.logback.core;

import ch.qos.logback.core.spi.ContextAware;
import ch.qos.logback.core.spi.FilterAttachable;
import ch.qos.logback.core.spi.LifeCycle;


public interface Appender<E> extends LifeCycle, ContextAware, FilterAttachable {

    public String getName();
      public void setName(String name);
      void doAppend(E event);
}
```

`doAppender()` 方法接收一个泛型参数 *E* 作为唯一的参数。*E* 的实际参数类型取决于 logback 模块。在 logback-classic 模块里面，*E* 的类型是 [ILoggingEvent](https://logback.qos.ch/apidocs/ch/qos/logback/classic/spi/ILoggingEvent.html) 。在 logback-access 模块里面，*E* 的类型是 [AccessEvent](https://logback.qos.ch/apidocs/ch/qos/logback/access/spi/AccessEvent.html)。`doAppend()` 是 logback 框架里面最重要的模块。它的责任是将日志事件进行格式化，然后输出到对应的设备上。

Appender 都是实体类，这样可以确保它们通过名字被引用。`Appender` 接口继承了 `FilterAttachable` 接口。使得一个或多个过滤器可以附加到 appender 实例上。

Appender 最基本的责任是将日志事件进行输出。然而，它们可以委托 `Layout` 或者 `Encoder` 对象来对日志事件进行格式化。每一个 layout/encoder 有且只与一个 appender 相关联。例如，`SocketAppender` 仅仅序列化日志事件，然后再通过线路传输。

### AppenderBase

[`ch.qos.logback.core.AppenderBase`](https://logback.qos.ch/xref/ch/qos/logback/core/AppenderBase.html) 是一个抽象类，实现了 `Appender` 接口。它提供了基本方法供所有 appender 使用。例如：获取或设置名称的方法、激活状态、布局以及过滤器。它是 logback 中所有 appender 的父类。尽管是一个抽象类，但是 `AppenderBase` 还实现了 `Append` 接口中 `doAppend()` 方法。可能附上源码的摘要来讨论 `AppenderBase` 是最清楚的方式。

```java
public synchronized void doAppend(E eventObject) {

  // prevent re-entry.
  if (guard) {
    return;
  }

  try {
    guard = true;

    if (!this.started) {
      if (statusRepeatCount++ < ALLOWED_REPEATS) {
        addStatus(new WarnStatus(
            "Attempted to append to non started appender [" + name + "].",this));
      }
      return;
    }

    if (getFilterChainDecision(eventObject) == FilterReply.DENY) {
      return;
    }

    // ok, we now invoke the derived class's implementation of append
    this.append(eventObject);

  } finally {
    guard = false;
  }
}
```

`doAppend()` 的实现是 synchronized 的。不同的线程通过同一个 appender 打印日志是线程安全的。当一个线程 *T* 正在执行 `doAppend()` 方法，接下来其它的线程调用将会被阻塞直到线程 *T* 离开 `doAppend()` 方法，这样可以确保 *T* 对 appender 的访问具有独占性。

因为这种同步并不总是适合的，所以 logback 提供了 [`ch.qos.logback.core.UnsynchronizedAppenderBase`](https://logback.qos.ch/xref/ch/qos/logback/core/UnsynchronizedAppenderBase.html) 类，0跟 [AppenderBase](https://logback.qos.ch/xref/ch/qos/logback/core/AppenderBase.html) 类十分的相似。为了简单起见，接下来的内容我们只讨论 `UnsynchronizedAppenderBase`。

首先，`doAppend()` 方法会去检查 `guard` 是不是为 true。如果是，它会立即退出。如果 `guard` 不是为 true，下一步将它设置为 true。`guard` 会确保 `doAppend()` 方法不会被自身递归调用。想象一下这样的一个组件，被在 `append()` 方法之外的地方被调用，用于打印日志。它的调用可能被直接指向一个完全相同的刚刚调用过它的一个 appender，导致无限循环和堆栈溢出。

> 注：`` `UnsynchronizedAppenderBase `` 类中有一个 `guard` 变量
>
> `private ThreadLocal<Boolean> guard = new ThreadLocal<Boolean>();`

接下来，我们会检查 `started` 是否为 true。如果不是，`doAppend()` 会发出一个警告并返回。换句话说，一旦 appender 被关闭，就不能对它进行写入。`Appender` 对象实现了 `LifeCycle` 接口，也就是说它实现了 `start()`、`stop()`、`isStarted` 方法。在设置完一个 appender 的所有属性之后，logback 的配置框架 - Joran，将会给 appender 发一个信号去激活它的属性。根据它的类型，一个 appender 可能会启动失败，如果某些特定的属性丢失或者由于各种属性之间的冲突。例如，创建文件依赖截断模式，`FileAppender` 不能对 `File` 选项的值起作用，直到这个值确定下来。明确的激活步骤可以确保一个 appender 在知道它们的值之后再作用于其属性。

如果 appender 不能被被启动或者被停止，logback 内部状态管理系统将会发出一条警告信息。在几次尝试之后，为了避免被同一条警告信息淹没内部状态系统，`doAppend()` 会停止发出这些警告。

接下来 `if` 语句检查过滤器的结果，根据过滤器链的结果，事件可以被拒绝或者被接受。如果缺少过滤器链，事件默认会被接受。

接下来 `doAppend()` 调用 `append()` 的实现方法。这个方法是实际的执行者，用来将事件附加到合适的设备上。

最后，`guard` 被释放，后续对 `append()` 的调用得以执行。

在手册的其余部分，我们保留 `option` 与 `property`，用于 JavaBean 通过 get 和 set 方法动态推断出来的任何属性。

## Logback-core

Logback-core 为 logback 其他模块的构建奠定了基础。一般来说，logback-core 的组件需要一些定制，尽管很少。但是，在接下来的几个部分，我们描述了一种可以开箱即用的 appender。

### OutputStreamAppender

[`OutputStreamAppender`](https://logback.qos.ch/xref/ch/qos/logback/core/OutputStreamAppender.html) 将事件附加到 `java.io.OutputStream` 上。这个类提供了其它 appender 构建的基础服务。用户通常不会直接实例一个 OutputStreamAppender 实例。因为一般来说 `java.io.OutputStream` 类型不能方便的转为 String。因为在配置文件中没有方法去直接指定一个 `OutputStream` 目标对象。简单来说，你不能通过配置文件配置一个 `OutputStreamAppender`。但是这并不意味着 `OutputStreamAppender` 缺少配置属性。这些属性描述如下：

|       属性名      |                                        属性值                                        |                                                                                               描述                                                                                              |
| :------------: | :-------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     ecoder     | [`Encoder`](https://logback.qos.ch/xref/ch/qos/logback/core/encoder/Encoder.html) |                                                                    决定通过哪种方式将事件写入 `OutputStreamAppender`，Encoder 将会在单独的章节介绍                                                                    |
| immediateFlush |                                      boolean                                      | `immediateFlush` 的默认值为 true。立即刷新输出流可以确保日志事件被立即写入，并且可以保证一旦你的应用没有正确关闭 appender，日志事件也不会丢失。从另一方面来说，设置这个属性为 false，有可能会使日志的吞吐量翻两番(视情况而定)。但是，设置为 false，当应用退出的时候没有正确关闭 appender，会导致日志事件没有被写入磁盘，可能会丢失。 |

`OutputStreamAppender` 是其他三个 appender 的父类，分别是 `ConsoleAppender`、`FileAppender` 以及 `RollingFileAppender`。`FileAppender` 又是 `RollingFileAppender` 的父类。下面的类图展示 `OutputStreamAppender` 与子类之间的关系：

![appenderClassDiagram](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-Loxxbn0cNogPNXHZY4C%2FappenderClassDiagram.jpg?generation=1568702960658816\&alt=media)

### ConsoleAppender

[`ConsoleAppender`](https://logback.qos.ch/xref/ch/qos/logback/core/ConsoleAppender.html) 就跟名字显示的一样，是将日志事件附加到控制台，跟进一步说就是通过 *System.out* 或者 *System.err* 来进行输出。默认通过前者。`ConsoleAppender` 通过用户指定的 encoder，格式化日志事件。Encoder 会在接下来的章节讨论。*System.out* 与 *System.err* 两者都是 `java.io.PrintStream` 类型。因此，它们被包装在可以进行 I/O 缓存操作的 `OutputStreamWriter` 中。

|    属性名    |                                         类型                                        |                                                                                                                             描述                                                                                                                            |
| :-------: | :-------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  encoder  | [`Encoder`](https://logback.qos.ch/xref/ch/qos/logback/core/encoder/Encoder.html) |                                                                                                                见  `OutputStreamAppender` 属性                                                                                                               |
|   target  |                                       String                                      |                                                                                                        *System.out* 或 *System.err*。默认为 *System.out*                                                                                                       |
| withJansi |                                      boolean                                      | `withJansi` 的默认值为 `false`。设置 `withJansi` 为 `true` 可以激活 [Jansi](http://jansi.fusesource.org/) 在 windows 使用 ANSI 彩色代码。在 windows 上如果设置为 true，你应该将 `org.fusesource.jansi:jansi:1.9` 这个 jar 包放到 classpath 下。基于 Unix 实现的操作系统，像 Linux、Max OS X 都默认支持 ANSI 才彩色代码。 |

*Example: ConsoleAppender configuraion (logback-Console.xml)*

```markup
<configuration>

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender" >
        <!-- encoder 默认使用 ch.qos.logback.classic.encoder.PatternLayoutEncoder -->
        <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg %n</pattern>
        </encoder>    
    </appender>

    <root level="DEBUG">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

通过以下命令执行上面的配置文件：

```
java chapters.appenders.ConfigurationTester logback-Console.xml
```

### FileAppender

[`FileAppender`](https://logback.qos.ch/xref/ch/qos/logback/core/FileAppender.html) 是 `OutputStreamAppender` 的子类，将日志事件输出到文件中。通过 `file` 来指定目标文件。如果该文件存在，根据 `append` 的值，要么将日志追加到文件中，要么该文件被截断。

|   属性名   |                                         类型                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                 描述                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-----: | :-------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  append |                                      boolean                                      |                                                                                                                                                                                                                                                                                                                                                                                                           如果为 `true`，日志事件会被追加到文件中，否则的话，文件会被截断。默认为 `true`                                                                                                                                                                                                                                                                                                                                                                                                           |
| encoder | [`Encoder`](https://logback.qos.ch/xref/ch/qos/logback/core/encoder/Encoder.html) |                                                                                                                                                                                                                                                                                                                                                                                                                   参见  `OutputStreamAppender` 的属性                                                                                                                                                                                                                                                                                                                                                                                                                   |
|   file  |                                       String                                      |                                                                                                                                                                                                                                                                                                                                       要写入文件的名称。如果文件不存在，则新建。在 windows 平台上，用户经常忘记对反斜杠进行转义。例如，*c:\temp\test.log* 不会被正确解析，因为 *'\t'* 是一个转义字符，会被解析为一个 *tab* 字符 (\u0009)。正确的值应该像：*c:/temp/test.log* 或者 *c:\\\temp\\\test.log*。没有默认值。                                                                                                                                                                                                                                                                                                                                      |
| prudent |                                      boolean                                      | <p>在严格模式下，<code>FileAppender</code> 会将日志安全的写入指定文件。即使在不同的 JVM 或者不同的主机上运行 <code>FileAppender</code> 实例。默认的值为 <code>false</code>。<br>严格模式可以与 <code>RollingFileAppender</code> 结合使用。<br>严格模式也意味着 <code>append</code> 属性被自动设置为 <code>true</code>。<br>严格模式依赖排他文件锁。实验证明，文件锁大概是写入日志事件成本的 3 倍。在严格模式关闭的情况下，往一台"普通"电脑的硬盘上将一个日志事件写入文件，大概需要耗费 10 微秒。但是在开启的情况下，大概需要 30 微秒。也就是说在关闭的情况下可以一秒钟写入 100'000 个日志事件，但是在开启的情况下，一秒钟只能写入33'000 个日志事件。<br>严格模式可以在所有 JVM 写入同一个文件时，有效的序列化 I/O 操作。因此，随着竞相访问同一个文件的 JVM 数量上升，将会延迟每一个 I/O 操作。只要总共的 I/O 操作大约为每秒 20 个日志请求，对性能的影响可以被忽略。但是，如果应用每秒产生了 100 个以上的 I/O 操作，性能会受到明显的影响，应该避免使用严格模式。<br><code>网络文件锁</code> 当日志文件位于网络文件系统上时，严谨模式的成本会更高。同样重要的是，网络文件系统的文件锁带有很强的偏向性，当前获得锁的进程在释放锁之后会立马又重新获得。因此，当一个进程独占日志文件，将会导致其它进程饥饿死锁。<br>严格模式的影响严重依赖网速以及操作系统实现的细节。我们提供了一个小型应用  <a href="https://gist.github.com/2794241">FileLockSimulator</a> 用于在你的环境中模拟严格模式。</p> |

`立即刷新` 默认情况下，每一个日志事件都会被立即刷新到底层的输出流。默认方法更加的安全，因为日志事件在你的应用没有正确关闭 appender 的情况下不会丢失。但是，要想显著的增加日志的吞吐率，你可以将 `immediateFlush` 设置为 `false`。

下面是 `FileAppender` 的配置示例：

> Example: logback-fileAppender.xml

```markup
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <file>testFile.log</file>
<!--         将 immediateFlush 设置为 false 可以获得更高的日志吞吐量 -->
        <immediateFlush>true</immediateFlush>
<!--         默认为 ch.qos.logback.classic.encoder.PatternLayoutEncoder -->
        <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

在 *logback-examples* 的文件夹下，运行以下命令：

```bash
java chapters.appenders.ConfigurationTester logback-fileAppender.xml
```

> 要指定配置文件的具体路径
>
> 也可以直接在 eclipse 里面 Run Application 时设置 Arguments

#### 文件唯一命名 (使用时间戳)

在应用的开发阶段或者短期应用中，例如：批处理程序，在每个应用启动的时候创建一个新的日志文件。通过 `<timestamp>` 元素可以轻易做到这点。

> Example: logback-timestamp.xml

```markup
<configuration>
<!--     通过 "bySecond" 将时间格式化成 "yyyyMMdd'T'HHmmss" 的形式插入到 logger 的上下文中 
        这个值对后续的配置也适用
-->
    <timestamp key="bySecond" datePattern="yyyyMMdd'T'HHmmss" />

    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
<!--         利用之前创建的 timestamp 来创建唯一的文件 -->
        <file>log-${bySecond}.txt</file>
        <encoder>
            <pattern>%logger{35} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

`timestamp` 元素需要两个强制的属性 *key* 跟 *datePattern* 以及可选的属性 *timeReference*。*key* 属性的值是来区分哪个 timestamp 元素，并且在后续的配置中可以通过[TODO 变量替换](https://github.com/Volong/logback-chinese-manual/tree/5d098f38903c9d10311cc9a7f3a39463c28ca522/%E5%8F%98%E9%87%8F%E6%9B%BF%E6%8D%A2/README.md)来使用。*datePattern* 属性用于将当前时间格式化成字符串。日期格式必须遵循 [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) 中的规范。*timeReference* 表示时间戳引用哪个时间。默认为解析配置文件的时间，也就是当前时间。但是，在一些特定的情况下，可以设置为上下文初始化的时间。通过 设置 *timeReference* 的值为 `contextBirth`。

通过一下命令来测试 `<timestamp>` 元素：

```bash
java chapters.appenders.ConfigurationTester logback-timestamp.xml
```

> 译者注：需要指定具体配置文件的具体路径，也可以通过 eclipse 来运行。后续不再重复此注意事项。

设置 *timeReference* 的值为 "contextBirth" 的例子如下：

> Example: logback-timestamp-contextBirth.xml

```markup
<configuration>
    <timestamp key="bySecond" datePattern="yyyyMMdd'T'HHmmss" timeReference="contextBirth"/>
    ...
</configuration>
```

### RollingFileAppender

[`RollingFileAppender`](https://logback.qos.ch/xref/ch/qos/logback/core/rolling/RollingFileAppender.html) 继承自`FileAppender`，具有轮转日志文件的功能。例如，`RollingFileAppender` 将日志输出到 *log.txt* 文件，在满足了特定的条件之后，将日志输出到另外一个文件。

与 `RollingFileAppender` 进行交互的有两个重要的子组件。第一个是 `RollingPolicy`，它负责日志轮转的功能。另一个是 `TriggeringPolicy`，它负责日志轮转的时机。所以 `RollingPolicy` 负责发生什么，`TriggeringPolicy` 负责什么时候发生。

为了让 `RollingFileAppender` 生效，必须同时设置 `RollingPolicy` 与 `TriggeringPolicy`。但是，如果 `RollingPolicy` 也实现了 `TriggeringPolicy` 接口，那么只需要设置前一个就好了。

`RollingFileAppender` 的属性如下所示：

|        属性名       |                                         类型                                        |                                                                                                                                                                                                             描述                                                                                                                                                                                                             |
| :--------------: | :-------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|       file       |                                       String                                      |                                                                                                                                                                                                      参见 `FileAppender`                                                                                                                                                                                                     |
|      append      |                                      boolean                                      |                                                                                                                                                                                                      参见 `FileAppender`                                                                                                                                                                                                     |
|      encoder     | [`Encoder`](https://logback.qos.ch/xref/ch/qos/logback/core/encoder/Encoder.html) |                                                                                                                                                                                                 参见  `OutputStreamAppender`                                                                                                                                                                                                 |
|   rollingPolicy  |                                   RollingPolicy                                   |                                                                                                                                                                                        当轮转发生时，指定 `RollingFileAppender` 的行为。下面将会详细说明                                                                                                                                                                                        |
| triggeringPolicy |                                  TriggeringPolicy                                 |                                                                                                                                                                                        告诉 `RollingFileAppender` 什么时候发生轮转行为。下面将会详细说明                                                                                                                                                                                        |
|      prudent     |                                      boolean                                      | <p><a href="#FixedWindowRollingPolicy"><code>FixedWindowRollingPolicy</code></a> 不支持该属性。<br><code>RollingFileAppender</code> 在使用严格模式时要与  <a href="#TimeBasedRollingPolicy">\`TimeBasedRollingPolicy</a> 结合使用，但是有两个限制：<br>1. 在严格模式下，也不支持也不允许文件压缩（我们不能让一个 JVM 在写入文件时，另一个 JVM 在压缩该文件）<br>2. 不能对 <code>FileAppender</code> 的 <code>file</code> 属性进行设置。实际上，大多数的操作系统不允许在有进程操作文件的情况下对文件改名。<br>其它的参考 <code>FileAppender</code></p> |

#### Rolling policy 简介

[`RollingPolicy`](https://logback.qos.ch/xref/ch/qos/logback/core/rolling/RollingPolicy.html) 负责轮转的方式为：移动文件以及对文件改名。

`RollingPolicy` 接口如下：

```java
package ch.qos.logback.core.rolling;  

import ch.qos.logback.core.FileAppender;
import ch.qos.logback.core.spi.LifeCycle;

public interface RollingPolicy extends LifeCycle {

    public void rollover() throws RolloverFailure;
    public String getActiveFileName();
    public CompressionMode getCompressionMode();
    public void setParent(FileAppender appender);
}
```

`rollover` 方法负责对日志文件进行归档。`getActiveFileName()` 方法负责获取当前日志文件的名字。`getCompressionMode` 方法决定采取哪种压缩模式。通过 `setParent` 方法引用父类。

**TimeBasedRollingPolicy**

[`TimeBasedRollingPolicy`](https://logback.qos.ch/xref/ch/qos/logback/core/rolling/TimeBasedRollingPolicy.html) 是最常用的轮转策略。它是基于时间来定义轮转策略。例如按天或者按月。`TimeBasedRollingPolicy` 既负责轮转的行为，也负责触发轮转。实际上，`TimeBasedRollingPolicy` 同时实现了 `RollingPolicy` 与 `TriggeringPolicy` 接口。

`TimeBasedRollingPolicy` 的配置需要一个强制的属性 `fileNamePattern` 以及其它的可选属性。

|         属性名         |    类型   | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-----------------: | :-----: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   fileNamePattern   |  String | <p>该属性定义了轮转时的属性名。它的值应该由文件名加上一个 <em>%d</em> 的占位符。<em>%d</em> 应该包含  java.text.SimpleDateFormat 中规定的日期格式。如果省略掉这个日期格式，那么就默认为 <em>yyyy-MM-dd</em>。轮转周期是通过  <strong>fileNamePattern</strong> 推断出来的。<br> <br>注意：可以选择对 <code>RollingFileAppender</code>（<code>TimeBasedRollingPolicy</code> 的父类）中的 <code>file</code> 属性进行设置，也可以忽略。通过设置 <code>FileAppender</code> 的 <code>file</code> 属性，你可以将当前活动日志的路径与归档日志的路径分隔开来。当前日志永远会是通过 <code>file</code> 指定的文件。它的名字不会随着时间的推移而发生变化。但是，如果你选择忽略 <code>file</code> 属性，当前活动日志在每个周期内将会根据 <code>fileNamePattern</code> 的值变化。稍后的例子将会说明这一点。<br><em>%d{}</em> 中的日期格式将会遵循  java.text.SimpleDateFormat 中的约定。斜杆 '/' 或者反斜杠 '' 都会被解析成目录分隔符。<br><br><strong>指定多个 %d</strong><br><br>可以指定多个 %d，但是只能有一个是主要的，用于推断轮转周期。其它的 %d 占位符必须通过 'aux' 标记为辅助的。见下面的示例：<br>多个 %d 占位符允许你在文件夹中去管理归档文件，这个跟轮转周期不同。如下所示：通过年月来管理日志文件夹，但是轮转周期是在每天晚上零点。<br>/var/log/%d{yyyy/MM, aux}/myapplication.%d{yyyy-MM-dd}.log<br><br><strong>TimeZone</strong><br><br>在某些情况下，你可能想要根据时区而不是主机的时钟来轮转日志。你可以通过如下方式来指定一个时区，例如：<br>aFloder/test.%d{yyyy-MM-dd-HH, UTC}.log<br>如果指定的 timezone 不能被识别或者拼写错误，将会根据  \[TimeZone.getTimeZone(String)]\(<a href="http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html#getTimeZone(java.lang.String"><http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html#getTimeZone(java.lang.String></a>)) 方法指定为 GMT。</p> |
|      maxHistory     |   int   | 这个可选的属性用来控制最多保留多少数量的归档文件，将会异步删除旧的文件。比如，你指定按月轮转，指定 maxHistory = 6，那么 6 个月内的归档文件将会保留在文件夹内，大于 6 个月的将会被删除。注意：当旧的归档文件被移除时，当初用来保存这些日志归档文件的文件夹也会在适当的时候被移除。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     totalSizeCap    |   int   | 这个可选属性用来控制所有归档文件总的大小。当达到这个大小后，旧的归档文件将会被异步的删除。使用这个属性时还需要设置 maxHistory 属性。而且，maxHistory 将会被作为第一条件，该属性作为第二条件。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| cleanHistoryOnStart | boolean | <p>如果设置为 true，那么在 appender 启动的时候，归档文件将会被删除。默认的值为 false。<br>归档文件的删除通常在轮转期间执行。但是，有些应用的存活时间可能等不到轮转触发。对于这种短期应用，可以通过设置该属性为 true，在 appender 启动的时候执行删除操作。</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

下面是关于 `fileNamePattern` 的介绍。

| fileNamePattern                             | 轮转周期                                           | 示例                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| */wombat/foo.%d*                            | 每天轮转（晚上零点）。由于省略了指定 %d 的日期格式，所以默认为 *yyyy-MM-dd* | <p>没有设置 <code>file</code> 属性：在 2006.11.23 这一天的日志都会输出到 <em>/wombat/foo.2006-11-23</em> 这个文件。晚上零点以后，日志将会输出到 <em>wombat/foo.2016-11-24</em> 这个文件。<br>设置 <code>file</code> 的值为 <em>/wombat/foo.txt</em>：在 2016.11.23 这一天的日志将会输出到 <em>/wombat/foo.txt</em> 这个文件。在晚上零点的时候，<em>foo.txt</em> 将会被改名为 <em>/wombat/foo.2016-11-23</em>。然后将创建一个新的 <em>foo.txt</em>，11.24 号这一天的日志将会输出到这个新的文件中。</p>                         |
| */wombat/%d{yyyy/MM}/foo.txt*               | 每个月开始的时候轮转                                     | <p>没有设置 <code>file</code> 属性：在 2016.10 这一个月中的日志将会输出到 <em>/wombat/2006/10/foo.txt</em>。在 10.31 晚上凌晨以后，11 月份的日志将会被输出到 <em>/wombat/2006/11/foo.txt</em>。<br>设置 <code>file</code> 的值为 <em>/wombat/foo.txt</em>：在 2016.10，这个月份的日志都会输出到 <em>/wombat/foo.txt</em>。在 10.31 晚上零点的时候，<em>/wombat/foo.txt</em> 将会被重命名为 <em>/wombat/2006/10/foo.txt</em>，并会创建一个新的文件 <em>/wombat/foo.txt</em> ，11 月份的日志将会输出到这个文件。依此类推。</p> |
| */wombat/foo.%d{yyyy-ww}.log*               | 每周的第一天（取决于时区）                                  | 每次轮转发生在每周的第一天，其它的跟上一个例子类似                                                                                                                                                                                                                                                                                                                                                                                     |
| */wombat/foo%d{yyyy-MM-dd\_HH}.log*         | 每小时轮转                                          | 跟之前的例子类似                                                                                                                                                                                                                                                                                                                                                                                                      |
| */wombat/foo%d{yyyy-MM-dd\_HH-mm}.log*      | 每分钟轮转                                          | 跟之前的例子类似                                                                                                                                                                                                                                                                                                                                                                                                      |
| */wombat/foo%d{yyyy-MM-dd\_HH-mm, UTC}.log* | 每分钟轮转                                          | 跟之前的例子类似，不过时间格式是 UTC                                                                                                                                                                                                                                                                                                                                                                                          |
| */foo/%d{yyyy-MM, aux}/%d.log*              | 每天轮转。归档文件在包含年月的文件夹下                            | 第一个 %d 被辅助标记。第二个 %d 为主要标记，但是日期格式省略了。因此，轮转周期为每天（由第二个 %d 控制），文件夹的名字依赖年与月。例如，在 2016.11 的时候，所有的归档文件都会在 */foo/2006-11/* 文件夹下，如：*/foo/2006-11/2006-11-14.log*                                                                                                                                                                                                                                                       |

任何斜杆或者反斜杠够会被当作文件夹分隔符。任何必要的文件夹都会在有需要的时候创建。你可以轻松的将日志文件放在单独的文件夹中。

`TimeBasedRollingPolicy` 支持文件自动压缩。如果 `fileNamePattern` 以 *.gz* 或者 *.zip* 结尾，将会启动这个特性。

| fileNamePattern     | 轮转周期                          | 示例                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| */wombat/foo.%d.gz* | 每天轮转（晚上零点），自动将归档文件压缩成 GZIP 格式 | <p><code>file</code> 属性没有设置：在 2009.11.23，日志将会被输出到 <em>/wombat/foo.2009-11-23</em> 这个文件。但是，在晚上零点的时候，文件将会被压缩成 <em>/wombat/foo.2009-11-23.gz</em>。在 11.24，这一天的日志将会被直接输出到 <em>/wombat/folder/foo.2009-11-24</em> 这个文件。<br><code>file</code> 属性的值设置为 <em>/wombat/foo.txt</em>：在 2009.11.23，日志将会被输出到 <em>/wombat/foo.txt</em> 这个文件。在晚上零点的时候，该文件会被压缩成 <em>/wombat/foo.2009-11-23.gz</em>。并会创建一个新的 <em>/wombat/foo.txt</em> 文件，11.24 这一天的日志将会被输出到该文件。依此类推。</p> |

`fileNamePattern` 有两个目的。logback 通过该属性可以进行周期性的轮转并且得到每个归档文件的名字。注意，两种跟不同的 pattern 可能会有相同的轮转周期。*yyyy-MM* 与 *yyyy\@MM* 同样都是按月轮转，但是归档文件最终的名字不一样。

通过设置 `file` 属性，你可以将活动日志文件的路径与归档文件的路径分隔开来。日志将会一直输出到通过 `file` 属性指定的文件中，并且不会随着时间而改变。但是，如果你选择忽略 `file` 属性，活动日志的名字将会根据 `fileNamePattern` 的值在每个周期内变化。不设置 `file` 属性的时候，如果在轮转期间存在外部文件句柄引用日志文件，将会避免[命名错误](https://logback.qos.ch/codes.html#renamingError)。

`maxHistory` 控制归档文件保留的最大数目，并删除旧的文件。例如，如果你指定按月轮转，并设定 `maxHistory` 的值为 6，那么 6 个月之内的归档文件都会被保留，大于 6 个月的文件将会被删除。注意，当旧的文件被移除时，为文件归档而创建的文件夹在适当的时候也会被移除。

由于各种技术原因，轮转并不是时间驱动的，而是依赖日志事件。例如，在 2002.03.08，假设 `fileNamePattern` 的值为 *yyyy-MM-dd*（按天轮转），在晚上零点之后，没有日志事件到来，假设在 23 分 47 秒之后，第一个到达的日志事件将会触发轮转。也就是说轮转实际发生在 03.09 00:23'47 AM 而不是 0:00 AM。因此，依赖日志事件的到达速度，所以轮转可能会有延迟。但是，不管延迟的情况是什么样，一定周期内生成的日志事件将会被输出到指定的文件中，从这个角度来看，轮转算法始终都会是正确的。

下面是 `RollingFileAppender` 与 `TimeBaseRollingPolicy` 结合使用的例子：

> *Example: logback-RollingTimeBased.xml*

```markup
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logFile.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
<!--             按天轮转 -->
            <fileNamePattern>logFile.%d{yyyy-MM-dd}.log</fileNamePattern>
<!--             保存 30 天的历史记录，最大大小为 30GB -->
            <maxHistory>30</maxHistory>
            <totalSizeCap>3GB</totalSizeCap>
        </rollingPolicy>

        <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

下面是在 `prudent` 模式下（严格模式）`RollingFileAppender` 与 `TimeBasedRollingPolicy` 的结合使用的例子：

> Example: logback-PrudentTimeBasedRolling.xml

```markup
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 支持多个 JVM 同时写一个文件 -->
        <prudent>true</prudent>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logFile.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
            <totalSizeCap>3GB</totalSizeCap>
        </rollingPolicy>

        <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

#### 基于大小以及时间的轮转策略

有时你希望按时轮转，但同时又想限制每个日志文件的大小。特别是如果后期处理工具需要对日志进行大小限制。为了满足这个需求，logback 配备了 `SizeAndTimeBasedRollingPolicy`。

注意，`TimeBasedRollingPolicy` 可以限制归档文件总的大小。所以如果你想要这个限制，你可以通过设置 `totalSizeCap` 来达到这个目的。

下面的示例展示了基于时间及大小的配置：

> *Example: logback-sizeAndTime.xml*

```markup
<configuration debug="true">
    <appender name="ROLLING" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>mylog.txt</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
<!--             按天轮转 -->
            <fileNamePattern>mylog-%d{yyyy-MM-dd}.%i.txt</fileNamePattern>
            <maxFileSize>100MB</maxFileSize>
            <maxHistory>60</maxHistory>
            <totalSizeCap>20GB</totalSizeCap>
        </rollingPolicy>

        <encoder>
            <pattern>%msg%n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="ROLLING" />
    </root>
</configuration>
```

注意，除了 %d 之外还有 %i。这两个占位符都是强制要求的。在当前时间还没有到达周期轮转之前，日志文件达到了 `maxFileSize` 指定的大小，会进行归档，递增索引从 0 开始。

基于大小与时间的文件归档支持删除旧的归档文件。你需要指定 `maxHistory` 属性的值来保存几个周期的日志。当你的应用停止或者启动的时候，日志将会继续向正确的位置输出。即当前周期内索引最大的。

在 1.17 版本前，这个文档会提及一个叫 `SizeAndTimeBasedFNATP` 的组件。但是 `SizeAndTimeBasedFNATP` 组件只提供一个最简单的配置。我们不再提供关于 `SizeAndTimeBasedFNATP` 的文档。尽管这样，早期的配置文件使用 `SizeAndTimeBasedFNATP` 依然会运行的很好。 实际上，`SizeAndTimeBasedRollingPolicy` 是使用 `SizeAndTimeBasedFNATP` 实现的。

**FixedWindowRollingPolicy**

在轮转时，[`FixedWindowRollingPolicy`](https://logback.qos.ch/xref/ch/qos/logback/core/rolling/FixedWindowRollingPolicy.html) 根据固定窗口算法重命名文件，具体描述如下：

`filaNamePattern` 表示归档文件的名字。这个属性是必须的，而且必须包含一个表示整形的占位符 *i%*。

`FixedWindowRollingPolicy` 的可用属性如下：

| 属性名             | 类型     | 描述                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| minIndex        | int    | 表示窗口索引的下界                                                                                                                                                                                                                                                                                                                                                                                                  |
| maxIndex        | int    | 表示窗口索引的上界                                                                                                                                                                                                                                                                                                                                                                                                  |
| fileNamePattern | String | <p><code>FixedWindowRollingPolicy</code> 在重命名日志文件时将会根据这个属性来命名。它必须包含一个 <em>i%</em> 的占位符，该占位符指明了窗口索引的值应该插入的位置。<br><br>例如，当该属性的值为 <em>MyLogFile%i.log</em>，最小与最大的值分别为 <em>1</em> 和 <em>3</em>。将会产生的归档文件为 <em>MyLogFile1.log</em>，<em>MyLogFile2.log</em>，<em>MyLogFile3.log</em>。<br><br>文件压缩的方式也是通过该属性来指定。例如，设置该属性的值为 <em>MyLogFile%i.log.zip</em>，那么归档文件将会被压缩成 <em>zip</em> 格式。也可以选择压缩成 <em>gz</em> 格式。</p> |

由于窗口固定算法需要跟窗口大小一样的的重命名次数，因此强烈不推荐太大的窗口大小。当用户指定一个较大值时，当前的实现会将窗口大小自动减少为 20。

让我们通过一个例子来了解下固定窗口算法。假设 `minIndex` 的值为 *1*，`maxIndex` 的值为 *3*。`fileNamePattern` 的值为 *foo%i.log*，`file` 属性的值为 *foo.log*。

| 轮转数目 | 当前输出文件  | 归档日志文件                     | 描述                                                                                                                  |
| ---- | ------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 0    | foo.log | -                          | 还没有到轮转周期，logbak 将日志输出初始文件                                                                                           |
| 1    | foo.log | foo1.log                   | 第一次轮转，*foo.log* 被重命名为 *foo1.log*。一个新的 *foo.log* 文件将会被创建并成为当前输出文件                                                    |
| 2    | foo.log | foo1.log，foo2.log          | 第二次轮转，*foo1.log* 被重命名为 *foo2.log*。*foo.log* 被重命名为 *foo1.log*。一个新的 *foo.log* 被创建并成为当前输出文件                            |
| 3    | foo.log | foo1.log，foo2.log，foo3.log | 第三次轮转，*foo2.log* 被重命名为 *foo3.log*。*foo1.log* 被命名为 *foo2.log*。*foo.log* 被重命名为 *foo1.log*。一个新的 *foo.log* 被创建并成为当前输出文件 |
| 4    | foo.log | foo1.log，foo2.log，foo3.log | 在这次以及后续的轮转中，将会删除 *foo3.log* 文件，其它文件的重命名操作跟之前的步骤一样。在本次以及以后的轮转中，将会一直只有三个归档文件以及一个活跃的日志文件                               |

下面的给出了 `RollingFileAppender` 配合 `FixedWindowRollingPolicy` 使用的例子。注意，`file` 属性是强制的，即使它包含了一些跟 `fileNamePattern` 属性相同的信息。

> Example：logback-RollingFixedWindow\.xml

```markup
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>test.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
            <fileNamePattern>tests.%i.log.zip</fileNamePattern>
            <minIndex>1</minIndex>
            <maxIndex>3</maxIndex>
        </rollingPolicy>

        <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <maxFileSize>5MB</maxFileSize>
        </triggeringPolicy>

        <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

### 触发策略简介

[`TriggeringPolicy`](https://logback.qos.ch/xref/ch/qos/logback/core/rolling/TriggeringPolicy.html) 的实现用于通知 `RollingFileAppender` 何时轮转。

`TriggeringPolicy` 接口仅仅只包含了一个方法。

```java
package ch.qos.logback.core.rolling;

import java.io.File;
import ch.qos.logback.core.spi.LifeCycle;

public interface TriggeringPolicy<E> extends LifeCycle {

  public boolean isTriggeringEvent(final File activeFile, final <E> event);
}
```

`isTriggeringEvent()` 方法接收当前活动的文件以及当前的日志事件作为参数。基于这些参数，通过具体的实现来决定轮转是不是应该发生。

`TimeBasedRollingPolicy` 是使用最广泛的触发策略。也可以用作轮转策略来使用。

**SizeBasedTriggeringPolicy**

[`SizeBasedTriggeringPolicy`](https://logback.qos.ch/xref/ch/qos/logback/core/rolling/SizeBasedTriggeringPolicy.html) 观察当前活动文件的大小，如果已经大于了指定的值，它会给 `RollingFileAppender` 发一个信号触发对当前活动文件的轮转。

`SizeBasedTriggeringPolicy` 只接收 `maxFileSize` 这一个参数，它的默认值是 10 MB。

`maxFileSize` 可以为字节，千字节，兆字节，千兆字节，通过在数值后面指定一个后缀 *KB*，*MB* 或者 *GB*。例如，*5000000*，*5000KB*，*5MB* 以及 *2GB* 都是有效的，前三个是一样的。

```markup
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>test.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
            <fileNamePattern>test.%i.log.zip</fileNamePattern>
            <minIndex>1</minIndex>
            <maxIndex>3</maxIndex>
        </rollingPolicy>

        <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <maxFileSize>5MB</maxFileSize>
        </triggeringPolicy>
        <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n
            </pattern>
        </encoder>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

### Logback Classic

虽然日志事件在 logback-core 是通用的，但是在 logback-classic 中，它们永远是 `ILoggingEvent` 的实例。logback-classic 只不过是用来处理 `ILoggingEvent` 实例的专门处理管道。

#### SocketAppender and SSLSocketAppender

到目前为止，所介绍的 appender 只能将日志输出到本地资源。相反的是，[`SocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/SocketAppender.html) 被设计成可以将 `ILoggingEvent` 实例序列化再传输到远端机器。当使用 `SocketAppender` 时，日志事件将以明文发送，使用 [`SSLSocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/SSLSocketAppender.html) 时，日志事件将通过安全的通道传输。

序列化事件的实际类型为 [`LoggingEventVO`](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/LoggingEventVO.html)，它实现了 `ILoggingEvent` 接口。就日志事件而言，远程日志是非侵入式的。在接收到日志事件并反序列化之后，日记事件就像在本地生成的一样。多个 `SocketAppender` 实例运行在不同的机器上，直接将它们的日志通过固定的格式输出到中央日志服务器上。`SocketAppender` 不会关联 layout，因为它是序列化日志事件到远程服务器上。`SocketAppender` 在 *Transmission Control Protocol (TCP)* 层上运行，该层提供了可靠，有序，流式控制以及段对端的八位字节流。所以，如果远程服务器是可以到达的，那么日志事件最终都会到达那里。相反，如果远程服务器挂掉或者不可达到，那么日志事件会被丢弃。如果服务器重新恢复，那么日志事件的传输将会继续进行。这种重连是通过一个连接线程池周期性的尝试连接来进行的。

日志事件由本地 TCP 实现自动缓冲。也就是说如果连接到服务器的速度很慢，但是比客户端产生日志事件的速度要快，那么客户端不会受到网速的影响。但是，如果网络连接速度比日志产生速度要慢，那么客户端只能以网络速度进行处理。特别在极端情况下，连接到服务器的网络挂掉了，客户端最终会被阻塞。如果网络连接恢复了，但是服务器挂掉了，客户端不会阻塞，尽管因为服务器挂掉了，日志事件丢失。

尽管 `SocketAppender` 不再依赖任何的 logger，在当前线程的连接下也不会被垃圾收集。但是连接线程只有在服务器挂掉的情况下才存在，为了避免出现垃圾收集问题，你需要明确的关闭 `SocketAppender`。生命周期长的应用会创建/销毁许多 `SocketAppender` 实例，应该注意到这个垃圾回收问题。大部分的应用可以忽略这个问题。如果 JVM 在 `SocketAppender` 关闭之前退出，无论是显式的退出或者是通过后续的垃圾回收，都可能会导致未传输的数据在管道中被丢失。这是基于 windows 系统常见的问题。为了避免数据丢失，通常的做法是调用 `close()` 方法去关闭 `SocketAppender`，或者在应用退出之前调用 `LoggerContext` 的 `stop()` 方法。

远程服务器通过 `remoteHost` 与 `port` 属性来标识。`SocketAppender` 属性罗列在下表当中。`SSLSocketAppender` 支持额外的一些属性，将在[第十五章](https://logback.qos.ch/manual/usingSSL.html)进行讨论。

| 属性名               | 类型                                                                                | 描述                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| includeCallerData | boolean                                                                           | 如果为 true，那么调用者的信息也会被发送到服务端。默认为 false。                                                                                                                                  |
| port              | int                                                                               | 远程服务器的端口号                                                                                                                                                              |
| reconnectionDelay | [Duration](https://logback.qos.ch/apidocs/ch/qos/logback/core/util/Duration.html) | 接受一个表示持续时间的字符串，例如 "10 seconds" 代表每次重连的间隔时间。默认值为 30 秒。将这个值设置为 0，将会关闭重连机制。注意，如果连接服务器成功，则不会出现连接线程池。                                                                       |
| queueSize         | int                                                                               | <p>接受一个整数（大于0）代表有多少个日志事件传输到服务端。当这个值为 1 时，会同步传输日志事件到远端。当这个值大于 1 时，将设队列中还有剩余的空间，那么一个新的事件将会入队。队列的长度大于 1 可以提高性能，消除网络引起的延时。<br><br>参见 <code>eventDelayLimist</code> 属性。</p> |
| eventDelayLimit   | [Duration](https://logback.qos.ch/apidocs/ch/qos/logback/core/util/Duration.html) | 接受一个表示持续时间的字符串，例如："10 seconds"。它表示一旦当前队列已满（例如已经包含了 `queueSieze` 个事件），在丢弃事件之前的等待时间。在远端服务器一直缓慢接收事件时，这种情况就会发生。默认值为 100 毫秒。                                                |
| remoteHost        | String                                                                            | 服务器的主机名                                                                                                                                                                |
| ssl               | SSLConfiguration                                                                  | 只支持 `SSLSocketAppender`，这个属性提供了 SSL 配置供 appender 使用，将在[第十五章](https://logback.qos.ch/manual/usingSSL.html)进行讨论                                                          |

**日志服务器的选择**

logback classic 给服务器提供了两个选择接收来自 `SocketAppender` 与 `SSLSocketAppender` 的日志事件。

* `ServerSocketReceiver` 与跟它相对应的具有 SSL 功能的 `SSLServerSocketReceiver` 都是接收组件。可以通过配置应用中的 *logback.xml* 文件来接收远程 socket appender 的日志事件。查看[第十四章](https://logback.qos.ch/manual/receivers.html)获取更多的信息。
* `SimpleSocketServer` 与具有 SSL 功能的 `SimpleSSLSocketServer` 都提供了一个简单的 java 应用程序，该应用程序被设计成可配置，并且可以在命令行界面运行。这些应用仅仅等待来自 `SocketAppender` 或 `SSLSocketAppender` 的日志事件，每个被接收的日志事件按照本地服务器策略进行打印。下面给出一个简单的例子。

**使用 SimpleSocketServer**

`SimpleSocketServer` 应用接收两个命令行参数：*port* 与 *configFile*。*port* 监听的端口，*configFile* 表示 XML 格式的配置文件。

在 *logback-examples/* 文件夹下，通过一下命令来启动 `SimpleSocketServer`：

```bash
java ch.qos.logback.classic.net.SimpleSocketServer 6000 \
  src/main/java/chapters/appenders/socket/server1.xml
```

6000 为监听的端口，在 *server1.xml* 中，`ConsoleAppender` 与 `RollingFileAppender` 被添加到 root logger 上。

在启动了 `SimpleSocketServer` 之后，你可以在多个客户端上使用 *SocketAppender* 来发送日志事件。这个手册中相关的示例包含了两个这样的客户端：*chapters.appenders.SocketClient1* 与 *chapters.appenders.SocketClient2*。两个客户端都会等待用户在控制台输入字符。输入的字符会被包裹在 debug 级别的日志事件中，然后发送到远程服务器。这个两个客户端不同的地方在于 `SocketAppender` 的配置。`SocketClient1` 通过编码来配置，`SocketClient2` 需要获取一个配置文件。

`SimpleSocketServer` 在本地机器上启动之后，通过以下命令去连接：

```bash
java chapters.appenders.socket.SocketClient1 localhost 6000
```

你输入的每一行字符都会出现在之前启动 `SimpleSocketServer` 的控制台上。如果你停止或者重启 `SimpleSocketServer`，客户端会重连新的服务实例，但是在断开连接时的日志时间会丢失（不能取消）。

与 `SocketClient1` 不同的是，`SocketClient2` 需要获取一个 XML 格式的配置文件来进行配置。配置文件 *client1.xml* 如下所示，它创建了一个 `SocketAppender` 附加到 root logger 上。

> Example: client1.xml

```markup
<configuration>

  <appender name="SOCKET" class="ch.qos.logback.classic.net.SocketAppender">
    <remoteHost>${host}</remoteHost>
    <port>${port}</port>
    <reconnectionDelay>10000</reconnectionDelay>
    <includeCallerData>${includeCallerData}</includeCallerData>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="SOCKET" />
  </root>  

</configuration>
```

注意配置文件中的 `remoteHost`，`port`，`includeCallerData` 属性的值并没有直接给出，而是通过占位符来代替。这些值可以通过系统属性来指定：

```bash
java -Dhost=localhost -Dport=6000 -DincludeCallerData=false \
  chapters.appenders.socket.SocketClient2 src/main/java/chapters/appenders/socket/client1.xml
```

这个命令应该会得到跟之前 `SocketClient1` 这个例子类似的结果。

让我再重复强调一遍，日志事件的序列化没有侵入性。反序列化出来的日志事件像其它的日志事件一样携带同样的信息。可以像操作本地日志事件一样操作它，除了序列化日志事件默认不会包含调用者的信息。下面通过一个例子来说明，首先通过一下命令启动 `SimpleSocketServer` ：

```bash
 java ch.qos.logback.classic.net.SimpleSocketServer 6000 \
  src/main/java/chapters/appenders/socket/server2.xml
```

配置文件 server2.xml 创建了一个可以输出调用者文件名以及行号的 `ConsoleAppender`。如果你像之前通过配置文件 *client1.xml* 来运行 `SocketClient2`，你将会在两个括号之间看到两个问号，而不是调用者的文件名以及行号：

```java
2006-11-06 17:37:30,968 DEBUG [Thread-0] [?:?] chapters.appenders.socket.SocketClient2 - Hi
```

可以通过设置 `includeCallerData` 的值为 true，来改变 `SocketAppender` 的输出信息。使用如下命令：

```bash
java -Dhost=localhost -Dport=6000 -DincludeCallerData=true \
  chapters.appenders.socket.SocketClient2 src/main/java/chapters/appenders/socket/client1.xml
```

因为反序列化出来的事件可以像本地日志时间一样被处理，所以它们甚至可以被传送到第二个服务器做进一步的处理。在练习的时候，你可以设置两台服务器，第一台服务器接受客户端的日志事件，然后转发到第二台服务器。

**使用 SimpleSSLSocketServer**

`SimpleSSLSocketServer` 跟之前使用的 `SimpleSocketServer` 一样，在命令行接收两个参数：*port*，*configFile*。此外，你必须为日志服务器的 X.509 认证通过系统属性提供位置与密码信息。

在 *logback-examples/* 文件夹下，通过如下命令来启动 `SimpleSSLSocketServer`：

```
java -Djavax.net.ssl.keyStore=src/main/java/chapters/appenders/socket/ssl/keystore.jks \
    -Djavax.net.ssl.keyStorePassword=changeit \
    ch.qos.logback.classic.net.SimpleSSLSocketServer 6000 \
    src/main/java/chapters/appenders/socket/ssl/server.xml
```

`SimpleSSLSocketServer` 示例使用 X.509 认证，非常适合测试以及实验。**在生产环境使用 `SimpleSSLSocketServer` 之前，你应该为你的日志服务器获取一个 X.509 认证来标识你的服务器**。详情请参考[第十五章](https://logback.qos.ch/manual/usingSSL.html)。

因为服务器的配置文件在根元素上指定了 `debug="true"`，所以你将会在服务器启动的过程中看到 SSL 的配置信息。这在验证本地安全策略是否被正确实现时非常有效。

`SimpleSSLSocketServer` 启动的时候，你可以使用 `SSLSocketAppender` 来连接服务器。下面这个例子展示所需要的配置信息：

```markup
<configuration debug="true">

  <appender name="SOCKET" class="ch.qos.logback.classic.net.SSLSocketAppender">
    <remoteHost>${host}</remoteHost>
    <port>${port}</port>
    <reconnectionDelay>10000</reconnectionDelay>
    <ssl>
      <trustStore>
        <location>${truststore}</location>
        <password>${password}</password>
      </trustStore>
    </ssl>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="SOCKET" />
  </root>  

</configuration>
```

注意，跟之前一样，`remoteHost`、`port` 的值通过占位符来指定。另外，注意一下 `ssl` 属性，它包含了一个内置属性 `trustStore`，通过这个属性来指定信用商店的位置以及密码。这个配置非常的必要，因为我们使用自签名的证书。见[第十五章](https://logback.qos.ch/manual/usingSSL.html)来查看更多使用 `SSLSocketAppender` 关于 SSL 的配置信息。

我们使用这个配置来运行一个客户端实例，在命令行通过系统属性指定占位符的值：

```bash
java -Dhost=localhost -Dport=6000 \
    -Dtruststore=file:src/main/java/chapters/appenders/socket/ssl/truststore.jks \
    -Dpassword=changeit \
    chapters.appenders.socket.SocketClient2 src/main/java/chapters/appenders/socket/ssl/client.xml
```

跟之前的示例一样，在客户端提示的时候输入一些信息，然后这些信息将会传送到服务端（使用安全的通道），并展示在控制台。

注意， *truststore* 的值是通过在命令行使用系统属性指定了一个标识信用商店的文件路径。你也可以使用 classpath 路径，具体参考[第十五章](https://logback.qos.ch/manual/usingSSL.html)。

我们可以看到跟服务器启动时类似的信息，因为我们在客户端的配置文件的根元素中添加了 `debug="true"`，客户端启动的时候，详细打印了 SSL 的配置信息来帮助我们验证本地策略的一致性。

#### ServerSocketAppender and SSLServerSocketAppender

我们之前讨论过的 `SocketAppender` 组件（以及具有 SSL 能力的副本）被设计成允许应用程序通过网络连接远程日志服务器，以便传输日志事件。在某些情况下，通过应用程序初始化一个对日志服务器的连接可能不方便或者不可行。在这些情况下，logback 提供了 [`ServerSocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/server/ServerSocketAppender)。

`ServerSocketAppender` 不会初始化一个到日志服务器的连接，而是被动的监听 TCP 端口，等待客户端的连接。日志事件被传输给这个 appender，然后再分发给每个连接的客户端。如果没有客户端连接，日志事件会被马上丢弃。

除了基本的 `ServerSocketAppender` 之外，logback 还提供了 [`SSLServerSocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/server/SSLServerSocketAppender)，它通过一个安全，加密的通道传输日志事件到每个连接的客户端。而且，具有 SSL 功能的 appender 完全支持基于证书的双向认证，只有认证通过的客户端才可以连接到这个 appender 去接收日志事件。

对日志事件进行编码再传输的方法与 `SocketAppender` 完全一致，每个日志事件都是 `ILoggingEvent` 的实例。只不过连接的起始方向是相反的。虽然 `SocketAppender` 充当了一个主动的角色去连接日志服务器，`ServerSocketAppender` 是被动的监听即将到来的日志事件。

`ServerSocketAppender` 的子类型只提供给 logback 的接收组件。关于接收组件的信息，请查看[第十四章](https://logback.qos.ch/manual/receivers.html)。

`ServerSocketAppender` 支持如下的配置属性：

| 属性名               | 类型               | 描述                                                                                     |
| ----------------- | ---------------- | -------------------------------------------------------------------------------------- |
| address           | String           | appender 监听的本地网络接口地址。如果没有指定，则监听所有的网络接口                                                 |
| includeCallerData | boolean          | 如果为 true，调用者的信息将会发送给远程服务器。为 false，则不发送。                                                |
| port              | int              | appender 监听的端口                                                                         |
| ssl               | SSLConfiguration | 仅仅支持 `SSLServerSocketAppender`。具体参见[第十五章](https://logback.qos.ch/manual/usingSSL.html) |

以下是关于 `ServerSocketAppender` 的配置：

```markup
<configuration debug="true">
    <appender name="SERVER" class="ch.qos.logback.classic.net.server.ServerSocketAppender">
        <port>${port}</port>
        <includeCallerData>${includeCallerData}</includeCallerData>
    </appender>

    <root level="debug">
        <appender-ref ref="SERVER" />
    </root>
</configuration>
```

注意这个配置跟之前 `SocketAppender` 的配置只有 *class* 这个属性不同。`remoteHost` 缺失表示 appender 被动的等待远程主机的连接，而不是新开一个到远程日志服务器的连接。

以下是关于 `SSLServerSocketAppender` 的配置：

```markup
<configuration debug="true">
  <appender name="SERVER" 
    class="ch.qos.logback.classic.net.server.SSLServerSocketAppender">
    <port>${port}</port>
    <includeCallerData>${includeCallerData}</includeCallerData>
    <ssl>
      <keyStore>
        <location>${keystore}</location>
        <password>${password}</password>
      </keyStore>
    </ssl>
  </appender>

  <root level="debug">
    <appender-ref ref="SERVER" />
  </root>  

</configuration>
```

这个配置跟上一个配置主要的不同在于 appender 的 *class* 属性为 `SSLServerSocketAppender` 类型，包含一个嵌套的 `ssl` 元素。在这个例子中，为 appender 配置了 X.509 认证的 keyStore。

> 具体的 SSL 配置参见第十五章，这句话翻的我想吐了

因为 `ServerSocketAppender` 的子类是专门为接收组件设计的，所以我们将对这个的阐述推迟到 [第十四章](https://logback.qos.ch/manual/receivers.html) 介绍。

#### SMTPAppender

[`SMTPAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/SMTPAppender.html) 收集日志事件到一个或多个固定大小的缓冲区，当用户指定的事件发生时，将从缓冲区中取出适当的内容进行发送。SMTP 邮件是异步发送的。默认情况下，当日志的级别为 ERROR 时，邮件发送将会被触发。而且默认的情况下，所有事件都使用同一个缓冲区。

`SMTPAppender` 的属性如下表所示：

| 属性名                 | 类型                                                                                                    | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| smtpHost            | String                                                                                                | SMTP 服务器的主机名。强制性的。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| smtpPort            | int                                                                                                   | SMPT 服务监听的端口。默认为 25.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| to                  | String                                                                                                | 接收者的邮件地址。触发事件发送给接收者。多个收件人可以使用逗号(,)分隔，或者使用多个 `<to>` 元素来指定。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| from                | String                                                                                                | `SMTPAppender` 使用的发件人，格式遵循[邮件通用格式](http://en.wikipedia.org/wiki/Email_address)，如果你想要包含发送者的名字，使用这种格式 " Adam Smith <<smith@moral.org>>"，那么邮件将会显示收件人为 " Adam Smith \\<smith@moral.org\\>"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| subject             | String                                                                                                | <p>邮件的主题。它可以是通过 <a href="https://logback.qos.ch/manual/layouts.html#ClassicPatternLayout">PatternLayout</a> 转换后的有效值。关于 Layout 将在接下来的章节讨论。<br>邮件应该有一个主题行，对应触发的邮件信息。<br>假设 <code>subject</code> 的值为："Log: %Logger - %msg"，触发事件的 logger 名为 "com.foo.Bar"，并且日志信息为 "Hello world"。那么发出的邮件信息将会有一个名为 "Log: com.foo.Bar - Hello World" 的主题行。<br>默认情况下，这个属性的值为 "%logger{20} - %m"</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| discriminator       | [Discriminator](https://logback.qos.ch/xref/ch/qos/logback/core/sift/Discriminator.html)              | 在 Discriminator 的帮助下，`SMTPAppender` 根据 discriminator 返回的值可以将不同日志事件分散到不同的缓冲区中。默认的  discriminator 将返回同一个值，所以所有的事件都使用同一个缓冲区。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| evaluator           | [IEvaluator](https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/IEvaluator.html)               | <p>通过创建一个新的   元素来声明此选项。通过 <code>class</code> 属性指定 class 的名字表示用户希望通过哪个类来满足 <code>SMTPAppender</code> 的 <code>Evaluator</code> 的需要。<br>如果没有指定此选项，当触发一个大于等于 <em>ERROR</em> 级别的事件时，<code>SMTPAppender</code> 将会被分配一个 <a href="https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/OnErrorEvaluator.html">OnErrorEvaluator</a> 的实例。<br>logback 配备了几个其它的  evaluator，分别叫  <a href="https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/OnMarkerEvaluator.html"><code>OnMarkerEvaluator</code></a> （将在下面讨论），一个相对强大的 evaluator 叫  <a href="https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/JaninoEventEvaluator.html"><code>JaninoEventEvaluator</code></a>（在<a href="https://logback.qos.ch/manual/filters.html#evalutatorFilter">其它章节</a>讨论） 以及最近版本才有的一个更加强大的 evaluator 叫  <a href="https://logback.qos.ch/manual/filters.html#GEventEvaluator"><code>GEventEvaluator</code></a>。</p> |
| cyclicBufferTracker | [`CyclicBufferTracker`](https://logback.qos.ch/xref/ch/qos/logback/core/spi/CyclicBufferTracker.html) | <p>从名字可以看出，是一个  <code>CyclicBufferTracker</code> 的实例追踪循环缓冲区。它基于 discriminator 返回的 key （见上）。<br>如果你不想指定一个  cyclicBufferTracker，那么将会自动创建一个 <a href="https://logback.qos.ch/xref/ch/qos/logback/core/spi/CyclicBufferTracker.html">CyclicBufferTracker</a> 的实例。默认的，这个实例用来保留事件的循环缓冲区的大小为 256。你需要改变 <code>bufferSize</code> 选项的大小（见下面）</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| username            | String                                                                                                | 默认为 null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| password            | String                                                                                                | 默认为 null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| STARTTLS            | boolean                                                                                               | 如果为 true，那么 appender 将会发送 STARTTLS 命令（如果服务器支持）将连接变成 SSL 连接。注意，连接初始的时候是为加密的。默认为 false。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SSL                 | boolean                                                                                               | 如果为 true，将通过 SSL 连接服务器。默认为 false。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| charsetEncoding     | String                                                                                                | 邮件信息将会通过 \[charset]\((<https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html)]https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html>) 进行编码。默认编码为 "UTF-8"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| localhost           | String                                                                                                | 一旦  SMTP 客户端的主机名没有配置正确，例如客户端的 hostname 不是全限定的，那么服务端会拒绝客户端发送的 HELO/EHLO 命令。为了解决这个问题，你可以将 `localhost` 的值设置为客户端主机的全限定名。详情见  [com.sun.mail.smtp](http://javamail.kenai.com/nonav/javadocs/com/sun/mail/smtp/package-summary.html) 包文档中的 "mail.smtp.localhost" 属性。(这个网站已经关闭了...)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| asynchronousSending | boolean                                                                                               | 决定邮件传输是否是异步进行。默认为 'true'。但是，在某些特定的情况下，异步发送不怎么合适。例如，当发生一个严重错误时，你的应用使用 `SMTPAppender` 去发送一个警告，然后退出。但是相关线程可能没有时间去发送警告邮件。在这种情况下，你可以设置该属性的值为 'false'。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| includeCallerData   | boolean                                                                                               | 默认为 false。如果 `asynchronousSending` 的值为 true，并且你希望在日志中看到调用者的信息，你可以设置该属性的值为 true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| sessionViaJNDI      | boolean                                                                                               | <p><code>SMTPAppender</code> 基于 <code>javax.mail.Session</code> 来发送邮件信息。默认情况下，该属性的值为 false，所以需要用户指定相关属性通过 <code>SMTPAppender</code> 来构建 <code>javax.mail.Session</code> 实例。如果设置为 true，<code>javax.mail.Session</code> 实例将会通过 JNDI 来获取。参见 <code>jndiLocation</code> 属性。<br>通过 JNDI 获取 <code>Session</code> 实例可以减少需要配置的数量，使你的应用减少重复(\[dryer]\(<a href="http://en.wikipedia.org/wiki/Don&#x27;t_repeat_yourself))%E7%9A%84%E5%B7%A5%E4%BD%9C%E3%80%82%E6%9B%B4%E5%A4%9A%E5%85%B3%E4%BA%8E%E5%9C%A8"><http://en.wikipedia.org/wiki/Don't_repeat_yourself))的工作。更多关于在></a> Tomcat 配置 JNDI 的信息请参考  <a href="http://tomcat.apache.org/tomcat-6.0-doc/jndi-resources-howto.html#JavaMail_Sessions">JNDI Resources How-to</a>。<br><code>注意</code>：通过 JNDI 获取 <code>Session</code> 的时候请移除 web 应用下  <em>WEB-INF/lib</em> 文件夹下的 <em>mail.jar</em> 与 <em>activation.jar</em>。</p>                                  |
| jndiLocation        | String                                                                                                | JNDI 中放置  javax.mail.Session 的地方。默认为：" java:comp/env/mail/Session "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

SMTPAppender 仅仅只在它的循环缓存区中保留最后 256 个日志事件，当缓存区快要满的时候丢掉旧的日志事件。因此，通过 SMTPAppender 发送任何邮件包含的日志事件都不会超过 256 个。这在保留内存需求的限制，还提供了数量可观的应用上下文。

`SMTPAppender` 基于 JavaMail API。在 JavaMail 1.4 版本做过测试。JavaMail 需要 JavaBeans Activation Framework 包。你可以去它们各自的网站下载 [JavaMail API](http://java.sun.com/products/javamail/) 与 [JavaBeans Activation Framework](http://java.sun.com/beans/glasgow/jaf.html)。在运行下面的示例之前先确保将这两个 jar 包放在 classpath 下。

[`chapters.appenders.mail.EMail`](https://logback.qos.ch/xref/chapters/appenders/mail/EMail.html) 应用会生成多个日志信息，随后再生成一个错误日志信息。它接收两个参数，第一参数是整形，表示需要生成多少个日志事件。第二个参数表示 logback 的配置文件。*Email* 最后生成一个错误日志，将会触发发送邮件信息。

下面是一个 `Email` 应用的简单配置信息：

> Example: mail1

```markup
<configuration>
    <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
        <smtpHost>SMTP 服务器的地址</smtpHost>
        <to>收件人1</to>
        <to>收件人2</to>
        <from>发件人</from>
        <subject>TESTING: %logger{20} - %m</subject>
        <layout class="ch.qos.logback.classic.PatternLayout">
            <pattern>%date %-5level %logger{35} - %message%n</pattern>
        </layout>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="EMAIL" />
    </root>
</configuration>
```

在使用以上配置测试 `chapters.appenders.mail.Email` 之前，你需要设置 `smtpHost`，`to`，`from` 的值。一旦你正确设置了配置文件的值，你可以通过一下命令来执行：

```bash
java chapters.appenders.mail.EMail 100 src/main/java/chapters/appenders/mail/mail1.xml
```

收件者收到的邮件是经过 `PatternLayout` 格式化后的 100 条日志。下图展示的就是 Mozilla Thunderbird 邮件客户端接收到的邮件。

![smtpAppender1](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbrrhcpbpK6Es0vy%2FsmtpAppender1.jpg?generation=1568702960727312\&alt=media)

下个例子配置文件 *mail2.xml* 中的 `smtpHost`，`to`，`from` 属性的值通过占位符来代替。下面是 `mail2.xml` 配置中的一部分：

```markup
<appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
  <smtpHost>${smtpHost}</smtpHost>
  <to>${to}</to>
  <from>${from}</from>
  <layout class="ch.qos.logback.classic.html.HTMLLayout"/>
</appender>
```

你可以通过命令行来传递参数：

```bash
java -Dfrom=source@xyz.com -Dto=recipient@xyz.com -DsmtpHost=some_smtp_host \
  chapters.appenders.mail.EMail 10000 src/main/java/chapters/appenders/mail/mail2.xml
```

根据你的环境替换合适的值。

注意在新的例子中，`PatternLayout` 被 `HTMLLayout` 替代，将日志格式化为 HTML 表格。你可以更改行与列的顺序，以及表格的 CSS 样式。查看 [HTMLLayout](https://logback.qos.ch/manual/layouts.html#ClassicHTMLLayout) 文档更详细的信息。

由于给定的循环缓冲区的大小为 256，收件人可以看到经过 256 条经过格式化的日志显示在 HTML 表格中。注意，`chapters.appenders.mail.Email` 应用生成了 10'000 条日志，但是只有最新的 256 条日志会显示在邮件中。

![smtpAppender2](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbrxfpkE8Rlu5q_t%2FsmtpAppender2.jpg?generation=1568702960734482\&alt=media)

像 Mozilla Thunderbird, Eudora or MS Outlook 这些邮件客户端，提供了非常好的 CSS 样式来支持 HTML 邮件。但是，有时候会自动将 HTML 格式变成文本格式。如果想在 Thunderbird 查看 HTML 格式的邮件，需要通过 "View→Message Body As→Original HTML" 选项来进行设置。Yahoo 邮箱对 HTML 邮件有非常好的 CSS 样式支持。另一方面对 Gmail 来说，虽然它支持基本 HTML 表结构，但是它会忽略内部的 CSS 样式。Gmail 支持内联的 CSS 样式，但是由于内联的 CSS 会使输出结果变得庞大，所以 `HTMLLayout` 不会使用内联的 CSS 样式。

#### 定制缓冲区大小

默认情况下，`SMTPAppender` 会输出最新的 256 条日志信息。下面一个例子设置了不同缓冲区大小。

> Example: customBufferSize.xml

```markup
<configuration>
    <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
        <smtpHost>${smtpHost}</smtpHost>
        <to>${to}</to>
        <from>${from}</from>
        <subject>%logger{20} - %m</subject>
        <layout class="ch.qos.logback.classic.html.HTMLLayout" />

        <cyclicBufferTracker
            class="ch.qos.logback.core.spi.CyclicBufferTracker">
            <!-- 每封邮件只包含一条日志 -->
            <bufferSize>1</bufferSize>
        </cyclicBufferTracker>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="EMAIL" />
    </root>
</configuration>
```

#### 触发事件

如果 **evaluator** 属性没有设置，当日志事件的级别为 ERROR 时，`SMTPAppender` 会创建一个 [OnErrorEvaluator](https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/OnErrorEvaluator.html) 实例来触发发送邮件。发送错误时发送邮件是比较合理的，`EventEvaluator` 提供了不同的实现来重写默认的方法。

`SMTPAppender` 提交的每一个日志事件通过 evaluator 都会调用 `evaluate()` 方法来决定这个事件是否需要发送邮件，或者仅仅是替换缓冲区中的内容。当 evaluator 给了一个确定的答案，那么将会发送邮件。`SMTPAppender` 有且只有一个 evaluator 实例。这个实例能够管理它自己的内部状态。为了对这个进行说明，`CounterBasedEvaluator` 实现了一个 evaluator，当第 1024 个日志事件到来时才会触发邮件发送。

> Example: [CounterBasedEvaluator.java](https://logback.qos.ch/xref/chapters/appenders/mail/CounterBasedEvaluator.html)

```java
package chapters.appenders.mail;

import ch.qos.logback.core.boolex.EvaluationException;
import ch.qos.logback.core.boolex.EventEvaluator;
import ch.qos.logback.core.spi.ContextAwareBase;

public class CounterBasedEvaluator extends ContextAwareBase implements EventEvaluator {

  static int LIMIT = 1024;
  int counter = 0;
  String name;

  public boolean evaluate(Object event) throws NullPointerException,
      EvaluationException {
    counter++;

    if (counter == LIMIT) {
      counter = 0;

      return true;
    } else {
      return false;
    }
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }
}
```

这个类继承了 `ContextAwareBase` 以及实现了 `EventEvaluator` 接口。这可以让用户专注在 `EventEvaluator` 的核心功能上，让基类提供基础的功能。

设置 `SMTPAppender` 的 `evaluator` 选项来指定用户自定义的 evaluator。下面的例子将 `SMTPAppender` 附加在 root logger 上，并使用 `CounterBasedEvaluator` 作为它事件的 evaluator。

> Example: mail3.xml

```markup
<configuration>
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <evaluator class="chapters.appenders.mail.CounterBasedEvaluator" />
    <smtpHost>${smtpHost}</smtpHost>
    <to>${to}</to>
    <from>${from}</from>
    <subject>%logger{20} - %m</subject>

    <layout class="ch.qos.logback.classic.html.HTMLLayout"/>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="EMAIL" />
  </root>  
</configuration>
```

#### 基于标记(Marker)触发

虽然通过默认通过错误级别的日志来触发邮件的发送是合理的，但是可能会导致太多的邮件充斥用户的邮箱。logback 自带了另外一个触发策略，叫做 [OnMarkerEvaluator](https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/OnMarkerEvaluator.html)。它基于标记来触发。其实就是通过用户指定的标记来触发。下面这个例子说明这个一点：

[Marked\_EMail](https://logback.qos.ch/xref/chapters/appenders/mail/Marked_EMail.html) 应用包含了几个日志语句，都是 ERROR 级别的。但是只有其中的一条被标记。下面的是相关的代码：

```java
Marker notifyAdmin = MarkerFactory.getMarker("NOTIFY_ADMIN");
logger.error(notifyAdmin,
  "This is a serious an error requiring the admin's attention",
   new Exception("Just testing"));
```

下面的配置文件，表示当存在日志事件被标记为 NOTIFY\_ADMIN 或者 TRANSACTION\_FAILURE 将会触发邮件发送。

> Example: mailWithMarker.xml

```markup
<configuration>
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <evaluator class="ch.qos.logback.classic.boolex.OnMarkerEvaluator">
      <marker>NOTIFY_ADMIN</marker>
      <!-- 你可以指定多个标记 -->
      <marker>TRANSACTION_FAILURE</marker>
    </evaluator>
    <smtpHost>${smtpHost}</smtpHost>
    <to>${to}</to>
    <from>${from}</from>
    <layout class="ch.qos.logback.classic.html.HTMLLayout"/>
  </appender>

  <root>
    <level value ="debug"/>
    <appender-ref ref="EMAIL" />
  </root>  
</configuration>
```

通过以下命令执行：

```bash
java -Dfrom=source@xyz.com -Dto=recipient@xyz.com -DsmtpHost=some_smtp_host \
  chapters.appenders.mail.Marked_EMail src/main/java/chapters/appenders/mail/mailWithMarker.xml
```

**基于标记触发的 JaninoEventEvaluator**

除了使用核心的 `OnMarkerEvaluator`，我们还可以是使用更加通用的 [`JaninoEventEvaluator`](https://logback.qos.ch/manual/filters.html#JaninoEventEvaluator)，甚至更加强大的 [`GEventEvaluator`](https://logback.qos.ch/manual/filters.html#GEventEvaluator)。例如，下面的配置文件使用 `JaninoEventEvaluator` 而不是 `OnMarkerEvaluator`，但是它们的含义是一样的。

> Example: mailWithMarker\_Janino.xml

```markup
<configuration>
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <evaluator class="ch.qos.logback.classic.boolex.JaninoEventEvaluator">
      <expression>
        (marker != null) &&
        (marker.contains("NOTIFY_ADMIN") || marker.contains("TRANSACTION_FAILURE"))
      </expression>
    </evaluator>    
    ... 跟之前一样
  </appender>
</configuration>
```

**基于标记触发的 GEventEvaluator**

通过使用 [GEventEvaluator](https://logback.qos.ch/manual/filters.html#GEventEvaluator) 来实现一个相同的 evaluator。

> Example: mailWithMarker\_GEvent.xml

```markup
<configuration>
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <evaluator class="ch.qos.logback.classic.boolex.GEventEvaluator">
      <expression>
        e.marker?.contains("NOTIFY_ADMIN") || e.marker?.contains("TRANSACTION_FAILURE")
      </expression>
    </evaluator>    
    ... 跟之前一样
  </appender>
</configuration>
```

因为日志事件可能没有 marker，所以 marke 的值可能为 null。可以使用 Groovy 的安全解引用操作符，也就是 . ? 操作符。

#### STARTTLS/SSL 认证

`SMTPAppender` 支持通过用户名/密码以及 STARTTLS，SSL 协议进行认证。STARTTLS 跟 SSL 的不同之处在于，STARTTLS 初始化连接不是加密的，仅仅只有在客户端发出 STARTTLS 命令的时候将连接变为 SSL。在 SSL 模式下，连接在一开始就是被加密的。

#### Gmail 的 SMTPAppender 配置 (SSL)

下面的例子是 Gmail SSL 协议的 `SMTPAppender` 配置：

> Example: gmailSSL.xml

```markup
<configuration>
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <smtpHost>smtp.gmail.com</smtpHost>
    <smtpPort>465</smtpPort>
    <SSL>true</SSL>
    <username>YOUR_USERNAME@gmail.com</username>
    <password>YOUR_GMAIL_PASSWORD</password>

    <to>EMAIL-DESTINATION</to>
    <to>ANOTHER_EMAIL_DESTINATION</to> <!-- additional destinations are possible -->
    <from>YOUR_USERNAME@gmail.com</from>
    <subject>TESTING: %logger{20} - %m</subject>
    <layout class="ch.qos.logback.classic.PatternLayout">
      <pattern>%date %-5level %logger{35} - %message%n</pattern>
    </layout>       
  </appender>

  <root level="DEBUG">
    <appender-ref ref="EMAIL" />
  </root>  
</configuration>
```

> 译者注：Gmail 的配置我没有测试成功，一直发送不了邮件。最后还是配置的 163 邮箱

#### Gmail 的 SMTPAppender 配置 (STARTTLS)

下面的例子是 Gmail STARTTLS 协议的 `SMTPAppender` 配置：

> Example: gmailSTARTTLS.xml

```markup
<configuration>   
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <smtpHost>smtp.gmail.com</smtpHost>
    <smtpPort>587</smtpPort>
    <STARTTLS>true</STARTTLS>
    <username>YOUR_USERNAME@gmail.com</username>
    <password>YOUR_GMAIL_xPASSWORD</password>

    <to>EMAIL-DESTINATION</to>
    <to>ANOTHER_EMAIL_DESTINATION</to> <!-- additional destinations are possible -->
    <from>YOUR_USERNAME@gmail.com</from>
    <subject>TESTING: %logger{20} - %m</subject>
    <layout class="ch.qos.logback.classic.PatternLayout">
      <pattern>%date %-5level %logger - %message%n</pattern>
    </layout>       
  </appender>

  <root level="DEBUG">
    <appender-ref ref="EMAIL" />
  </root>  
</configuration>
```

#### SMTPAppender 与 MDCDiscriminator

之前提到过，指定一个 discriminator 而不是使用默认的。根据指定的 discriminator，`SMTPAppender` 会生成关于特定用户，用户 session，客户端 IP 地址的邮件信息。

下面是 [MDCBasedDiscriminator](https://logback.qos.ch/xref/ch/qos/logback/classic/sift/MDCBasedDiscriminator.html) 与一个名叫 req.remoteHost 的 MDC key 结合使用的一个例子。假定该 key 已经包含了远程主机的 IP 地址。在 web 应用中，你可以使用 [MDCInsertingServletFilter](https://logback.qos.ch/manual/mdc.html#mis) 去填充 MDC 的值。

> Example: mailWithMDCBasedDiscriminator.xml

```markup
<configuration>   
  <appender name="EMAIL" class="ch.qos.logback.classic.net.SMTPAppender">
    <smtpHost>ADDRESS-OF-YOUR-SMTP-HOST</smtpHost>
    <to>EMAIL-DESTINATION</to>
    <from>SENDER-EMAIL</from>

    <discriminator class="ch.qos.logback.classic.sift.MDCBasedDiscriminator">
      <key>req.remoteHost</key>
      <defaultValue>default</defaultValue>
    </discriminator>

    <subject>${HOSTNAME} -- %X{req.remoteHost} %msg"</subject>
    <layout class="ch.qos.logback.classic.html.HTMLLayout">
      <pattern>%date%level%thread%X{req.remoteHost}%X{req.requestURL}%logger%msg</pattern>
    </layout>
  </appender>

  <root>
    <level level="DEBUG"/>
    <appender-ref ref="EMAIL" />
  </root>  
</configuration>
```

所以，`SMTPAppender` 发送的每一封邮件都有一个独特的远程主机，这非常利于定位问题。

**在繁忙的应用中进行缓冲区管理**

在内部，discriminator 返回每个不同的值都会创建一个新的循环缓冲区。但是，会维护一个 `maxNumberOfBuffers` 变量 (默认为 64)。当缓冲区的数量超过 `maxNumberOfBuffers` 时，最近最少更新的缓冲区会被丢弃。第二个安全策略是，最近 30 分钟没有被更新的缓冲区会被丢弃。

在每分钟有大量事务的机器上，设置一个较小值的 `maxNumberOfBuffers`，将会导致邮件中的日志数量变得特别小。实际上，在存在大量事务的情况下，连续生成同一个 discriminator 值会导致多个缓冲区会与同一个事务相关联，因为缓冲区会被 kill 掉再重建。即使在繁忙的系统中，循环缓冲区的最大数量也会被 `maxNumberOfBuffers` 所限制。

为了避免这种悠悠球效应(摇摆不定)，当日志时间被标记为 "FINALIZE\_SESSION " 时， `SMTPAppender` 会释放与给定 discriminator 值相关联的缓冲区。这将会导致在每个事务快要结束的时候，将会丢弃适当的缓冲区。你可以在避免 OOM 的前提下，增加 `maxNumberOfBuffers` 的值到 512 或 1024。

这里有三个完全不同但是又互补的机制一起管理循环缓冲区。它们可以确保即使在繁忙的系统中，也会让相关的缓冲区存活。

#### DBAppender

[`DBAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/db/DBAppender.html) 以一种独立于 JAVA 语言的方式将日志事件插入到三张数据库表中。

这三张表分别为：*logging\_event*, *logging\_event\_property* 与 *logging\_event\_exception*。在使用 DBAppender 之前，它们必须存在。logback 自带 SQL 脚本来创建表。这些脚本在 *logback-classic/src/main/java/ch/qos/logback/classic/db/script* 文件夹下。每一种最流行的数据库都有一个对应的脚本。如果没有你指定的数据库脚本，参考已经存在的例子，可以很简单的写一个。如果你把他们发给我们，我们很乐意在将来的版本中发布这些脚本。

如果你的 JDBC 驱动支持 JDBC 3.0 specification 规范中的 `getGeneratedKeys` 方法，并且你也创建了上述所需要色数据库表，那么不再需要额外的步骤。否则的话，你必须选择一个适合你数据库的 `SQLDialect`。目前 logback 支持的数据库方言有 H2, HSQL, MS SQL Server, MySQL, Oracle, PostgreSQL, SQLLite and Sybase。

下面的表格总结了数据库类型，以及它们是否支持 `getGeneratedKeys()` 方法：

| RDBMS                | 测试版本     | JDBC 驱动的测试版本                | 是否支持 `getGeneratedKeys()` | logback 是否提供对应的方言 |
| -------------------- | -------- | --------------------------- | ------------------------- | ----------------- |
| DB2                  | untested | untested                    | unknown                   | NO                |
| H2                   | 1.2.132  | -                           | unknown                   | YES               |
| HSQL                 | 1.8.0.7  | -                           | NO                        | YES               |
| Microsoft SQL Server | 2005     | 2.0.1008.2 (sqljdbc.jar)    | YES                       | YES               |
| MySQL                | 5.0.22   | 5.0.8 (mysql-connector.jar) | YES                       | YES               |
| PostgreSQL           | 8.x      | 8.4-701.jdbc4               | NO                        | YES               |
| Oracle               | 10g      | 10.2.0.1 (ojdbc14.jar)      | YES                       | YES               |
| SQLLite              | 3.7.4    | -                           | unknown                   | YES               |
| Sybase SQLAnywhere   | 10.0.1   | -                           | unknown                   | YES               |

在 "标准的" PC 电脑上，经过测试，将单个的日志事件写入数据库需要花费大约 10 毫秒。如果使用线程池，大约只需要花费大约 1 毫秒。大部分的 JDBC 驱动都支持连接池。

> 不是很懂这个 "标准的" PC 电脑，到底是台什么电脑

根据连接数据库的工具以及数据库自身，配置 logback 去使用 `DBAppender` 可以通过几种不同的方式去实现。我们很快就会发现，配置 `DBAppender` 的主要问题在于如何设置 `ConnectionSource` 实例。

一旦为数据库配置了 `DBAppender`，日志事件就会被发送到指定的数据库中。根据之前说的，logback 使用三张表来存储日志数据。

*logging\_event* 表包含了以下字段：

| Field                  | Type       | Description                                                                                                                              |
| ---------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **timestamp**          | `big int`  | 日志事件的创建时间                                                                                                                                |
| **formatted\_message** | `text`     | 经过 `org.slf4j.impl.MessageFormatter` 格式化后的消息                                                                                             |
| **logger\_name**       | `varchar`  | 发出日志的 logger 名                                                                                                                           |
| **level\_string**      | `varchar`  | 日志事件的级别                                                                                                                                  |
| **reference\_flag**    | `smallint` | 用来表示是否是异常或者与 MDC 属性相关联。它的值通过 `ch.qos.logback.classic.db.DBHelper` 计算得到。日志时间包含 `MDC` 或者 `Context` 时，它的值为 *1*。包含异常时，它的值为 *2*。包含两者，则值为 *3*。 |
| **caller\_filename**   | `varchar`  | 发出日志请求的文件名                                                                                                                               |
| **caller\_class**      | `varchar`  | 发出日志请求的类                                                                                                                                 |
| **caller\_method**     | `varchar`  | 发出日志请求的方法                                                                                                                                |
| **caller\_line**       | `char`     | 发出日志请求所在的行                                                                                                                               |
| **event\_id**          | `int`      | 日志事件在数据库的 id                                                                                                                             |

*logging\_event\_property* 表用于存储 `MDC` 或者 `Context` 中的 key 与 value。它包含如下字段：

| Field             | Type      | Description     |
| ----------------- | --------- | --------------- |
| **event\_id**     | `int`     | 日志事件的数据库 id     |
| **mapped\_key**   | `varchar` | `MDC` 属性的 key   |
| **mapped\_value** | `text`    | `MDC` 属性的 value |

*logging\_event\_exception* 表包含如下字段：

| Field           | Type       | Description |
| --------------- | ---------- | ----------- |
| **event\_id**   | `int`      | 日志事件的数据库 id |
| **i**           | `smallint` | 堆栈所在的行      |
| **trace\_line** | `varchar`  | 相对应的堆栈信息    |

下面给出一个更加直观的示例，截图上面的信息是 MySQL 数据中 `DBAppender` 提供的内容。

表 *logging\_event*：

![dbAppenderLE](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbsCQL-bkFUxw_VT%2FdbAppenderLE.gif?generation=1568702960611874\&alt=media)

表 *logging\_event\_exception*：

![dbAppenderLEException](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbsEvmWl6eLCZWEL%2FdbAppenderLEException.gif?generation=1568702960440596\&alt=media)

表 *logging\_event\_property*：

![dbAppenderLEProperty](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbsGIVDj9i16JIOn%2FdbAppenderLEProperty.gif?generation=1568702960509325\&alt=media)

**ConnectionSource**

`ConnectionSource` 接口提供了一种可插拔式的方式为需要使用 `java.sql.Connection` 的 logback 类获取 JDBC 连接。`ConnectionSource` 目前有三种实现，分别为：`DataSourceConnectionSource，` `DriverManagerConnectionSource` 与 `JNDIConnectionSource`。

第一个例子我们使用 `DriverManagerConnectionSource` 与 MySQL database，如下所示：

> Example: append-toMySQL-with-driverManager.xml

```markup
<configuration>

  <appender name="DB" class="ch.qos.logback.classic.db.DBAppender">
    <connectionSource class="ch.qos.logback.core.db.DriverManagerConnectionSource">
      <driverClass>com.mysql.jdbc.Driver</driverClass>
      <url>jdbc:mysql://host_name:3306/datebase_name</url>
      <user>username</user>
      <password>password</password>
    </connectionSource>
  </appender>

  <root level="DEBUG" >
    <appender-ref ref="DB" />
  </root>
</configuration>
```

必须正确配置 JDBC 驱动，这里使用 `com.mysql.jdbc.Driver`。`url` 必须以 *jdbc:mysql://* 开头。

[`DriverManagerConnectionSource`](https://logback.qos.ch/xref/ch/qos/logback/core/db/DriverManagerConnectionSource.html) 实现了 `ConnectionSource` 接口，通过基于 URL 的传统 JDBC 方式来获取连接。

这个类为每一个调用 `getConnection()` 的方法都新建一个 `Connection` 连接。推荐你使用本地支持的连接池的 JDBC 驱动，或者创建你自己实现的 `ConnectionSource`，基于你已经使用的任何连接池机制。如果你可以使用支持 `javax.sql.DataSource` 的 JNDI 实现，例如，在 J2EE 应用服务中，参见下面的 [`JNDIConnectionSource`](https://logback.qos.ch/manual/appenders.html#JNDIConnectionSource)。

> Example: append-with-datasource.xml

```markup
<configuration  debug="true">

  <appender name="DB" class="ch.qos.logback.classic.db.DBAppender">
     <connectionSource class="ch.qos.logback.core.db.DataSourceConnectionSource">

       <dataSource class="${dataSourceClass}">
         <!-- Joran 不能替换不是属性的变量。因此我们不能像其它变量一样声明接下来的变量
         -->
         <param name="${url-key:-url}" value="${url_value}"/>
         <serverName>${serverName}</serverName>
         <databaseName>${databaseName}</databaseName>
       </dataSource>

       <user>${user}</user>
       <password>${password}</password>
     </connectionSource>
  </appender>

  <root level="INFO">
    <appender-ref ref="DB" />
  </root>  
</configuration>
```

在这个例子中，我们大量使用了变量替换。当需要把一些连接的细节集中在一个配置文件中，并且通过 logback 与其它框架共享时非常方便。

**JNDIConnectionSource**

[`JNDIConnectionSource`](https://logback.qos.ch/xref/ch/qos/logback/core/db/JNDIConnectionSource.html) 是 logback 自带的，`ConnectionSource` 的另一种实现。从名字可以看出来，它通过 JNDI 获取 `javax.sql.DataSource`，然后再获取 `java.sql.Connection` 实例。`JNDIConnectionSource` 主要设计用在 J2EE 应用服务器以及应用服务器客户端中，这里假设应用服务器支持远程获取 `javax.sql.DataSource`。因为可以利用连接池或者其它应用服务器所提供的好处。更加重要的是，你的应用不需要做重复的工作，因为不需要在 *logback.xml* 中定义一个 `DataSource`。

例如，下面的是关于 Tomcat 的一个配置片段，它是基于 PostgreSQL。当然，上面提到其它数据也可以。

```markup
<Context docBase="/path/to/app.war" path="/myapp">
  ...
  <Resource name="jdbc/logging"
               auth="Container"
               type="javax.sql.DataSource"
               username="..."
               password="..."
               driverClassName="org.postgresql.Driver"
               url="jdbc:postgresql://localhost/..."
               maxActive="8"
               maxIdle="4"/>
  ...
</Context>
```

一旦 `DataSource` 在你的 J2EE 服务中定义了，你可以轻松的在 logback 配置文件中引用。如下所示：

> Example: append-via-jndi.xml

```markup
<configuration debug="true">
  <appender name="DB" class="ch.qos.logback.classic.db.DBAppender">
    <connectionSource class="ch.qos.logback.core.db.JNDIConnectionSource">
      <!-- please note the "java:comp/env/" prefix -->
      <jndiLocation>java:comp/env/jdbc/logging</jndiLocation>
    </connectionSource>
  </appender>
  <root level="INFO">
    <appender-ref ref="DB" />
  </root>  
</configuration>
```

这个类通过午餐构造函数获取一个 `javax.naming.InitialContext`。在 J2EE 环境通常可以行得通。但是在 J2EE 环境之外，你需要根据 JNDI 提供者的文档提供一个 *jndi.properties* 属性文件。

**连接池**

日志事件可以很快的被创建。为了让日志事件都能被插入到数据库，推荐 `DBAppender` 使用连接池配置。

经过实验发现，使用连接池，可以让 `DBAppender` 有大幅的性能提升。下面的配置文件，将日志事件发送给 MySQL，没有使用连接池。

> Example: append-toMySQL-with-datasource.xml

```markup
<configuration>

  <appender name="DB" class="ch.qos.logback.classic.db.DBAppender">
    <connectionSource class="ch.qos.logback.core.db.DataSourceConnectionSource">
      <dataSource class="com.mysql.jdbc.jdbc2.optional.MysqlDataSource">
        <serverName>${serverName}</serverName>
        <port>${port$</port>
        <databaseName>${dbName}</databaseName>
        <user>${user}</user>
        <password>${pass}</password>
      </dataSource>
    </connectionSource>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="DB" />
  </root>
</configuration>
```

在这个配置文件中，发送 500 个日志事件到 MySQL 数据库，需要高达 5 秒的时间，相当每条请求需要 10 毫秒。在大型的应用中，这个数字是不能够被接受的。

`DBAppender` 连接池需要使用一个专业的外部库。下一个例子中使用 [c3p0](http://sourceforge.net/projects/c3p0)。为了使用 c2p0，你需要下载并将 *c3p0-VERSION.jar* 放在类路径下。

> Example: append-toMySQL-with-datasource-and-pooling.xml

```markup
<configuration>

  <appender name="DB" class="ch.qos.logback.classic.db.DBAppender">
    <connectionSource
      class="ch.qos.logback.core.db.DataSourceConnectionSource">
      <dataSource
        class="com.mchange.v2.c3p0.ComboPooledDataSource">
        <driverClass>com.mysql.jdbc.Driver</driverClass>
        <jdbcUrl>jdbc:mysql://${serverName}:${port}/${dbName}</jdbcUrl>
        <user>${user}</user>
        <password>${password}</password>
      </dataSource>
    </connectionSource>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="DB" />
  </root>
</configuration>
```

使用这个新的配置，发送 500 条日志事件到 MySQL 数据库大约需要 0.5 秒，大约 1 毫秒一条请求，性能提升了十倍。

#### SyslogAppender

syslog 协议非常的简单：syslog 发送者将信息发送给 syslog 接收者。接收者通常叫做 *syslog 守护线程* 或者 *syslog 服务器*。logback 可以把消息发送给远程的 syslog 守护线程。通过 [`SyslogAppender`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/SyslogAppender.html) 可以实现。

下面是 SyslogAppender 的属性：

| 属性名                   | 类型        | 描述                                                                                                                                                                                                                      |
| --------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **syslogHost**        | `String`  | syslog 服务器的主机名                                                                                                                                                                                                          |
| **port**              | `String`  | 用来 syslog 服务器的端口号。默认端口为 514，这个情况下，不需要修改。                                                                                                                                                                                |
| **facility**          | `String`  | <p>用来确定消息的来源。<br>它的值必须为 <em>KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP, NTP, AUDIT, ALERT, CLOCK, LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7</em> 其中之一。大小写不敏感</p> |
| **suffixPattern**     | `String`  | 该属性指定发送到 syslog 服务器的消息非标准部分的格式。默认情况下，它的值为 *\[%thread] %logger %msg*。`PatternLayout` 可以使用的任何值都是正确的 suffixPattern 值。                                                                                                      |
| **stackTracePattern** | `String`  | 该属性允许定制出现在每个堆栈行前面的字符。默认的值为 "\t"，即制表符。`PatternLayout` 可以使用的任何值都是正确的  stackTracePattern 值。                                                                                                                                |
| **throwableExcluded** | `boolean` | 设置该属性的值为 `true`，会导致堆栈信息被忽略。默认为 `false`，所以堆栈信息可以被发送给 syslog 服务器。                                                                                                                                                         |

日志事件的 syslog 严重程度是根据日志事件的级别转换来的。*DEBUG* 被转换为 *7*，*INFO* 被转换为 *6*，*WARN* 被转换为 *4*，*ERROR* 被转换为 *3*。

因为 syslog 请求的格式非常严格，所以 `SyslogAppender` 没有任何 layout。但是使用 `suffixPattern` 可以让用户展示他想展示的信息。

下面为 `SyslogAppender` 的配置示例：

> Example: logback-syslog.xml

```markup
<configuration>

  <appender name="SYSLOG" class="ch.qos.logback.classic.net.SyslogAppender">
    <syslogHost>remote_home</syslogHost>
    <facility>AUTH</facility>
    <suffixPattern>[%thread] %logger %msg</suffixPattern>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="SYSLOG" />
  </root>
</configuration>
```

在对这个配置进行测试的时候，应该先验证远程 syslog 守护线程是否能够接收外部的资源。根据以往的经验，syslog 守护进程通常会拒绝来自网络的请求。

#### SiftingAppender

如名字所示，`SiftingAppender` 根据给定的运行时属性分离或者过滤日志。例如，`SiftingAppender` 可以根据用户的 session 分离日志，因此不同的用户的日志会有不同的日志文件，一个用户一个日志文件。

| 属性名                  | 类型                                                                                | 描述                                                                                                         |
| -------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **timeout**          | [Duration](https://logback.qos.ch/apidocs/ch/qos/logback/core/util/Duration.html) | 一个内置的 appender 如果在指定 `timeout` 时间内没有被访问，则被认为是过时的。一个过时的 appender 会被关闭，并且不会被 `SiftingAppende` 所引用。默认值为 30 分钟 |
| **maxAppenderCount** | `integer`                                                                         | `SiftingAppender` 可以创建并且跟踪内置 appender 的最大数量。默认值为 Integer.MAX\_VALUE                                        |

`SiftingAppender` 通过动态创建来实现这个。`SiftingAppender` 通过配置文件中指定的模板 (通过闭合的 `<sift>` 元素，见下面的例子) 来创建内置的 appender。`SiftingAppender` 负责管理子 appender 的生命周期。例如，`SiftingAppender` 会自动关闭并移除任何过时的 appender。在指定的 `timeout` 时间内没有被访问过的内置 appender，被认为是过时的。

在处理一个日志事件时，`SiftingAppender` 会委托一个子 appender 去进行处理。选择的标准是通过 discriminator 在运行时计算。用户也可以通过 [Discriminator](https://logback.qos.ch/xref/ch/qos/logback/core/sift/Discriminator.html) 来指定一个选择标准。让我们通过一个示例来学习一下。

**示例**

[SiftExample](https://logback.qos.ch/xref/chapters/appenders/sift/SiftExample.html) 应用通过打印日志来表明应用已经启动。通过 MDC 设置键 "userid" 对应的值为 "Alice"，并打印了一条日志信息。下面是主要的代码：

```java
logger.debug("Application started");
MDC.put("userid", "Alice");
logger.debug("Alice says hello");
```

`SiftingAppender` 在配置文件中使用模板的示例如下：

> Example: byUserid.xml

```markup
<configuration>

    <property name="FILE_NAME" value="FILE" />

    <appender name="SIFT"
        class="ch.qos.logback.classic.sift.SiftingAppender">
        <!-- 在缺少 class 属性的情况下，默认的 discriminator 类型为                                          ch.qos.logback.classic.sift.MDCBasedDiscriminator -->
        <discriminator>
            <key>userid</key>
            <defaultValue>unknown</defaultValue>
        </discriminator>
        <sift>
            <appender name="FILE-${userid}"
                class="ch.qos.logback.core.FileAppender">
                <file>${userid}_${FILE_NAME}.log</file>
                <append>false</append>
                <layout class="ch.qos.logback.classic.PatternLayout">
                    <pattern>%d [%thread] %level %mdc %logger{35} - %msg%n</pattern>
                </layout>
            </appender>
        </sift>
    </appender>

    <root level="DEBUG">
        <appender-ref ref="SIFT" />
    </root>
</configuration>
```

在没有 class 属性的情况下，默认的 discriminator 类型为 [MDCBasedDiscriminator](https://logback.qos.ch/xref/ch/qos/logback/classic/sift/MDCBasedDiscriminator.html)。discriminator 的的值为 MDC 的 key 所对应的值。但是，如果 MDC 的值为 null，那么 `defaultValue` 的将为 discriminator 的值。

`SiftingAppender` 的独特之处在于它有能力去引用以及配置子 appender。在上面的例子中，`SiftingAppender` 会创建多个 `FileAppender` 实例。每个 `FileAppender` 实例通过 MDC 的 key 所对应的值来标识。每当 MDC 的 key "userid" 被分配一个新值时，一个新的 `FileAppender` 将会被构建。`SiftingAppender` 可以追踪它所创建的 appender。appender 在 30 分钟之内没有被使用将会被自动关闭并丢弃。

`导出变量` 有不同 appender 实例是不够的。每一个实例都必须输出到一个唯一的资源中。为了做到这种区分，在 appender 模板中，key 被传递给 discriminator。在上面的例子中是 "userid"，它将被导出并变成一个[变量](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%8F%98%E9%87%8F%E6%9B%BF%E6%8D%A2)。因此，该变量可以通过给定的子 appender 来区分具体的资源。

在上面的示例中，使用 "byUserid.xml" 来运行 `SiftExample`，将会创建两个不同的日志文件，"unknown.log" 与 "Alice.log"。

`本地变量` 在版本 1.0.12 中，配置文件中局部变量的属性也可以应用到内置的 appender 中。而且，你可以在 `<sift>` 元素中[定义变量](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%8F%98%E9%87%8F%E7%9A%84%E5%AE%9A%E4%B9%89)以及[动态定义属性](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%8A%A8%E6%80%81%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7)。或者在 `<sift>` 元素之外定义变量，在里面使用也是支持的。

**获取正确的 timeout**

对于特定类型的应用，正确的获取 `timeout` 参数非常困难。如果 `timeout` 过小，一个新的内置 appender 在创建几秒钟之后就被移除了。这种现象被称为 "制造垃圾"。如果 `timeout` 的值过大，那么 appender 会快速接连的被创建，可能会耗尽资源。同理，设置 `maxAppenderCount` 的值太低会产生垃圾。

在大多数情况下，在代码中显示的指出不需要再创建内置的 appender。需要在代码中标记日志事件为 [FINALIZE\_SESSION](https://logback.qos.ch/apidocs/ch/qos/logback/classic/ClassicConstants.html#FINALIZE_SESSION_MARKER)。无论什么时候 SiftingAppender 看到日志事件标记为 `FINALIZE_SESSION`，它将会终结相关的子 appender。在生命周期快结束时，内置的 appender 将会留存几秒钟来处理之后到来的日志事件，然后再关闭。

```java
import org.slf4j.Logger;
import static ch.qos.logback.classic.ClassicConstants.FINALIZE_SESSION_MARKER;

  void job(String jobId) {

    MDC.put("jobId", jobId);
    logger.info("Starting job.");

    ... do whather the job needs to do

    // 将导致内置 appender 结束生命周期。但是会留存几秒钟
    logger.info(FINALIZE_SESSION_MARKER, "About to end the job");

    try {
      .. perform clean up
    } catch(Exception e);  
      // 被留存的 appender 处理，但是不会再创建新的 appender
      logger.error("unexpected error while cleaning up", e);
    }
  }
```

#### AsyncAppender

AsyncAppender 异步的打印 [ILoggingEvent](https://logback.qos.ch/apidocs/ch/qos/logback/classic/spi/ILoggingEvent.html)。它仅仅是作为一个事件调度器的存在，因此必须调用其它的 appender 来完成操作。

`默认满了 80% 会丢弃数据` AsyncAppender 使用 [BlockingQueue](http://docs.oracle.com/javase/1.5.0/docs/api/java/util/concurrent/BlockingQueue.html) 来缓存日志时间。AsyncAppender 会创建一个工作线程去队列的头部获取数据，并将日志事件调度给附加再 AsyncAppender 上的 appender。在默认的情况下，在队列被占用了 80% 的情况下，AsyncAppender 会丢弃掉级别为 TRACE，DEBUG，INFO 的日志事件。这个策略虽然会丢失掉日志，但是对性能有利。

`停止/重新部署应用` 当停止或者重新部署应用时，`AsyncAppender` 必须被终止，为了停止并召回工作线程，以及刷新队列中的日志事件。通过[终止上下文](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%81%9C%E6%AD%A2-logback-classic)可以达到这个目标，并会关闭所有的 appender，包含所有 `AsyncAppender` 实例。`AsyncAppender` 将等待工作线程指定的 `maxFlushTime` 时间来刷新队列。如果你发现在关闭 `LoggerContext` 期间，队列中的日志事件被丢弃了，那么你需要去增加 `maxFlushTime`。指定 `maxFlushTime` 的值为 0 将会强制 `AsyncAppender` 等待所有日志事件被刷新才会从 stop() 方法中返回。

`停止后再清理` 取决于 JVM 的停止模式，工作线程在处理队列中的事件时被打断会导致日志事件在队列中被阻塞。一般发生在 `LoggerContext` 没有被完全停止，或者 JVM 在典型控制流之外终止。为了避免工作队列在这些情况下被打断。将一个 shutdown hook 在 JVM 运行时插入，在 JVM 开始准备停止的时候可以[正确的关闭 LoggerContext](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%81%9C%E6%AD%A2-logback-classic)。当其它的 shutdown hook 尝试记录事件时，shutdown hook 可以作为首选的方法来完全关闭 logback。

> 最后一句话没有搞懂是什么意思

如下是 AsyncAppender 的一些属性：

| 属性名                 | 类型        | 描述                                                                                                                                                                                                                                                                                             |
| ------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queueSize           | `int`     | 队列的最大容量，默认为 256                                                                                                                                                                                                                                                                                |
| discardingThreshold | `int`     | 默认，当队列还剩余 20% 的容量时，会丢弃级别为 TRACE, DEBUG 与 INFO 的日志，仅仅只保留 WARN 与 ERROR 级别的日志。想要保留所有的事件，可以设置为 0                                                                                                                                                                                                   |
| includeCallerData   | `boolean` | 获取调用者的数据相对来说比较昂贵。为了提高性能，默认情况下不会获取调用者的信息。默认情况下，只有像线程名或者 [MDC](https://logback.qos.ch/manual/mdc.html) 这种"便宜"的数据会被复制。设置为 true 时，appender 会包含调用者的信息                                                                                                                                               |
| maxFlushTime        | `int`     | 根据所引用 appender 队列的深度以及延迟， `AsyncAppender` 可能会耗费长时间去刷新队列。当 `LoggerContext` 被停止时， `AsyncAppender stop` 方法会等待工作线程指定的时间来完成。使用 maxFlushTime 来指定最大的刷新时间，单位为毫秒。在指定时间内没有被处理完的事件将会被丢弃。这个属性的值的含义与  \[Thread.join(long)]\(<http://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html#join(long>)) 相同 |
| neverBlock          | `boolean` | 默认为 false，在队列满的时候 appender 会阻塞而不是丢弃信息。设置为 true，appender 不会阻塞你的应用而会将消息丢弃                                                                                                                                                                                                                        |

默认情况下，事件队列的最大 容量为 256。如果队列被填满，那么新的日志事件将被阻塞，直到工作线程有机会去调度日志事件。当队列的容量没有处在最大容量的时候，应用线程能够再次开始记录日志。所以，在 AsyncAppender 在缓冲区的容量满了或者快满的情况下，异步日志记录变成了伪异步。但这也不是什么坏的事。虽然在 appender 缓冲区的压力减少之前，会稍微花点时间去处理日志事件，但是这个设计可以让应用继续保持运行。

为应用的最大吞吐量优化 appender 的事件队列依赖以下几个因素。以下的任何一个因素都有可能导致伪同步的发生：

* 大量的应用线程
* 每个应用调用大量的日志事件
* 每个日志事件有大量的数据
* 高延迟的子 appender

为了保持事物继续下去，增加队列的大小通常有用，但是是以应用可用的堆为代价。

`丢弃行为` 根据之前的讨论，为了减少阻塞。默认情况下，当剩余容量少于 20% 的时候，`AsyncAppender` 会丢掉 TRACE, DEBUG 以及 INFO 级别的日志，保留 WARN 与 ERROR 级别的日志。该策略可以确保非阻塞的处理日志事件 (因此具有高性能)。通过设置 `discardingThreshold` 的值为 0 可以阻止丢弃日志事件。

> Example: logback-async.xml

```markup
<configuration>
  <appender name="FILE" class="ch.qos.logback.core.FileAppender">
    <file>myapp.log</file>
    <encoder>
      <pattern>%logger{35} - %msg%n</pattern>
    </encoder>
  </appender>

  <appender name="ASYNC" class="ch.qos.logback.classic.AsyncAppender">
    <appender-ref ref="FILE" />
  </appender>

  <root level="DEBUG">
    <appender-ref ref="ASYNC" />
  </root>
</configuration>
```

#### 编写你自己的 Appender

通过继承 AppenderBase 可以编写你自己的 appender。它支持处理过滤器，状态信息，以及其它大多数 appender 共享的功能。子类仅仅只需要实现 `append(Object eventObject)` 方法。

接下来列出来的 `CountingConsoleAppender`，限制了输出到控制台的日志事件的数量。当日志事件的数量达到上限时，它会退出。它使用 `PatternLayoutEncoder` 来格式化日志事件，还可以接收一个 `limit` 的参数。因此，除了 `append(Object eventObject)` 方法之后，还需要一些其它的方法。正如下面展示的，这些参数都是通过 logback 多种配置机制来自动处理的。

> Example: *CountingConsoleAppender.java*

```java
package chapters.appenders;

import java.io.IOException;

import ch.qos.logback.classic.encoder.PatternLayoutEncoder;
import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.AppenderBase;


public class CountingConsoleAppender extends AppenderBase<ILoggingEvent> {
  static int DEFAULT_LIMIT = 10;
  int counter = 0;
  int limit = DEFAULT_LIMIT;

  PatternLayoutEncoder encoder;

  public void setLimit(int limit) {
    this.limit = limit;
  }

  public int getLimit() {
    return limit;
  }

  @Override
  public void start() {
    if (this.encoder == null) {
      addError("No encoder set for the appender named ["+ name +"].");
      return;
    }

    try {
      encoder.init(System.out);
    } catch (IOException e) {
    }
    super.start();
  }

  public void append(ILoggingEvent event) {
    if (counter >= limit) {
      return;
    }
    // 通过我们自己的 layout 来格式化日志事件
    try {
      this.encoder.doEncode(event);
    } catch (IOException e) {
    }

    // 准备下一个事件
    counter++;
  }

  public PatternLayoutEncoder getEncoder() {
    return encoder;
  }

  public void setEncoder(PatternLayoutEncoder encoder) {
    this.encoder = encoder;
  }
}
```

`start()` 方法会检查是否有 `PatternLayoutEncoder` 存在，如果不存在，appender 将会启动失败并会发出错误信息。

这个定制的 appender 说明了两点：

* 所有的属性遵循 JavaBean 的 setter/getter 转换，由 logback 透明的处理。在 logback 配置期间，`start()` 方法会被自动调用，用来验证 appender 的各种属性是否设置与一致
* `AppenderBase.doAppend()` 方法会调用它子类的所有 append() 方法。实际上输出操作发生在 `append()` 方法中。而且，在这个方法中，appender 通过调用它们的 layout 来格式日志事件。

[`CountingConsoleAppender`](https://logback.qos.ch/xref/chapters/appenders/CountingConsoleAppender.html) 可以像其它的 appender 一样配置。详情见 *countingConsole.xml*。

### Logback Access

大部分的 appender 都可以在 logback-classic 中找到，同样的在 logback-access 中也可以找到。它们的工作本质上与在 logback-classic 中表现的是一样的。在接下来的部分，我们将讨论它们的用法。

#### SocketAppender 与 SSLSocketAppender

[`SocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/access/net/SocketAppender.html) 被委托将序列化的 `AccessEvent` 对象记录到远程实体上去。远程日志事件对 access event 来说是非侵入式的。在接收到并序列化之后，日志事件就像在本地被生成一样。

[`SSLSocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/access/net/SSLSocketAppender.html) 扩展了 `SocketAppender`，通过 SSL 传输日志到远程实体上。

access 的 `SocketAppender` 属性跟 classic 中的 `SocketAppender` 属性一样。

#### ServerSocketAppender 与 SSLServerSocketAppender

跟 `SocketAppender` 一样，[`ServerSocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/access/net/server/ServerSocketAppender.html) 被委托传输序列化后的 `AccessEvent` 对象到远程实体上。但是，使用 `ServerSocketAppender` 时，appender 充当一个服务器的角色，被动的监听 TCP 端口，等待客户端的连接。传送到 appender 的日志事件将被分发给所有连接的客户端。

[`SSLServerSocketAppender`](https://logback.qos.ch/xref/ch/qos/logback/access/net/server/SSLServerSocketAppender.html) 拓展了 `ServerSocketAppender`，通过 SSL 传输日志到远程实体上。

access 的 `ServerSocketAppender` 属性跟 classic 中的 `ServerSocketAppender` 属性一样。

#### SMTPAppender

access 中的 [`SMTPAppender`](https://logback.qos.ch/xref/ch/qos/logback/access/net/SMTPAppender.html) 工作的机制跟 classic 中的一样。但是 `evaluator` 属性完全不同。默认情况下，`SMTPAppender` 使用一个 `URLEvaluator` 对象。这个 evaluator 包含了一个 url 列表，用来检查当前请求的 url。当其中一个页面给 `URLEvaluator` 进行请求时，`SMTPAppender` 会发送一封邮件。

下面是在 access 环境下的一个例子：

> Example: logback-smtp.xml

```markup
<appender name="SMTP"
  class="ch.qos.logback.access.net.SMTPAppender">
  <layout class="ch.qos.logback.access.html.HTMLLayout">
    <pattern>%h%l%u%t%r%s%b</pattern>
  </layout>

  <Evaluator class="ch.qos.logback.access.net.URLEvaluator">
    <URL>url1.jsp</URL>
    <URL>directory/url2.html</URL>
  </Evaluator>
  <from>sender_email@host.com</from>
  <smtpHost>mail.domain.com</smtpHost>
  <to>recipient_email@host.com</to>
</appender>
```

在某些特定的流程中，用户选择的页面是一个重要的步骤，那么将会触发邮件的发送。例如，当一个这样的页面被访问时，之前被访问过的页面会包含在邮件中被发送，还会包含任何用户想要的信息。

#### DBAppender

[`DBAppender`](https://logback.qos.ch/xref/ch/qos/logback/access/db/DBAppender.html) 用来将 access 事件插入到数据库。

`DBAppender` 用到两张表：*access\_event* 以及 *access\_event\_header*。在使用 `DBAppender` 之前，它们必须存在。logback 内置了 SQL 脚本用来创建表格。它们在 *logback-access/src/main/java/ch/qos/logback/access/db/script* 文件夹中。大部分流行的数据库都有一个对应的脚本。如果你使用的数据库不存在一个这样的脚本，那么你可以根据已经存在例子，很轻易的就可以写一个。我们鼓励你将一个这样的脚本提交到这个项目中。

表 *access\_event* 包含的字段如下：

| 字段             | 类型        | 描述                            |
| -------------- | --------- | ----------------------------- |
| **timestamp**  | `big int` | access 时间创建的时间                |
| **requestURI** | `varchar` | 请求的 URI                       |
| **requestURL** | `varchar` | 请求的 URL。由请求方法，请求 URI 以及请求协议组成 |
| **remoteHost** | `varchar` | 远程主机的名字                       |
| **remoteUser** | `varchar` | 远程用户的名字                       |
| **remoteAddr** | `varchar` | 远程 IP 地址                      |
| **protocol**   | `varchar` | 请求协议。例如 *HTTP* 或 *HTTPS*      |
| **method**     | `varchar` | 请求方法。通常为 *GET* 或 *POST*       |
| **serverName** | `varchar` | 发出请求的服务器的名字                   |
| **event\_id**  | `int`     | access 事件的数据库 id              |

表 *access\_event\_header* 包含了每个请求头。字段如下：

| 字段                | 类型      | 描述                                                                                            |
| ----------------- | ------- | --------------------------------------------------------------------------------------------- |
| **event\_id**     | int     | 相对应 access 事件的数据库 id                                                                          |
| **header\_key**   | varchar | 请求头的名字，例如 *User-Agent*                                                                        |
| **header\_value** | varchar | 请求头的值，例如  *Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) Gecko/20061010 Firefox/2.0* |

classic 中的 `DBAppender` 属性在 access 的 `DBAppender` 中一样有效。后者提供了另一个选项，如下：

| 属性名               | 类型      | 描述                              |
| ----------------- | ------- | ------------------------------- |
| **insertHeaders** | boolean | 告诉 `DBAppender` 用所有请求的请求头来填充数据库 |

下面是一个使用 `DBAppender` 的例子：

> Example: *logback-DB.xml*

```markup
<configuration>

  <appender name="DB" class="ch.qos.logback.access.db.DBAppender">
    <connectionSource class="ch.qos.logback.core.db.DriverManagerConnectionSource">
      <driverClass>com.mysql.jdbc.Driver</driverClass>
      <url>jdbc:mysql://localhost:3306/logbackdb</url>
      <user>logback</user>
      <password>logback</password>
    </connectionSource>
    <insertHeaders>true</insertHeaders>
  </appender>

  <appender-ref ref="DB" />
</configuration>
```

#### SiftingAppender

logback-access 中的 SiftingAppender 跟 logback-classic 中的 SiftingAppender 非常相似。主要的不同在于 logback-access 默认的 discriminator 名字叫 [AccessEventDiscriminator](https://logback.qos.ch/xref/ch/qos/logback/access/sift/AccessEventDiscriminator.html)，而不是基于 MDC。从名字可以看出，AccessEventDiscriminator 在 AccessEvent 中使用一个指定的字段来选择一个内置的 appender。如果它的值为 null，那么将使用 `defaultValue` 指定的值。

指定的 AccessEvent 可以是 COOKIE, REQUEST\_ATTRIBUTE, SESSION\_ATTRIBUTE, REMOTE\_ADDRESS, LOCAL\_PORT, REQUEST\_URI 其中的一种。注意，前三个字段中必须指定 `AdditionalKey`。

下面是配置示例：

> Example: access-siftingFile.xml

```markup
<configuration>
  <appender name="SIFTING" class="ch.qos.logback.access.sift.SiftingAppender">
    <Discriminator class="ch.qos.logback.access.sift.AccessEventDiscriminator">
      <Key>id</Key>
      <FieldName>SESSION_ATTRIBUTE</FieldName>
      <AdditionalKey>username</AdditionalKey>
      <defaultValue>NA</defaultValue>
    </Discriminator>
    <sift>
       <appender name="ch.qos.logback:logback-site:jar:1.3.0-alpha4" class="ch.qos.logback.core.FileAppender">
        <file>byUser/ch.qos.logback:logback-site:jar:1.3.0-alpha4.log</file>
        <layout class="ch.qos.logback.access.PatternLayout">
          <pattern>%h %l %u %t \"%r\" %s %b</pattern>
        </layout>
      </appender>
    </sift>
  </appender>
  <appender-ref ref="SIFTING" />
</configuration>
```

在上面的配置文件中，`SiftingAppender` 内置了一个 `FileAppender` 实例。名为 "id" 的键被作为一个变量用于内置的 `FileAppender` 实例。默认的 discriminator，名叫 AccessEventDiscriminator，会在每个 `AccessEvent` 中查找一个 "username" 的 session 属性。如果没有，那么将使用默认值 "NA"。因此，如果一个名叫 "username" 的 session 属性包含了用户每条日志的用户名，那么以用户名命名的日志文件将会在 *byUser/* 文件夹下，日志文件包含了该用户产生的所有 access 日志。


# 第五章：Encoder

## 什么是 encoder

encoder 将日志事件转换为字节数组，同时将字节数组写入到一个 `OutputStream` 中。encoder 在 logback 0.9.19 版本引进。在之前的版本中，大多数的 appender 依赖 layout 将日志事件转换为 string，然后再通过 `java.io.Writer` 写出。在之前的版本中，用户需要在 `FileAppender` 中内置一个 `PatternLayout`。在 0.9.19 之后的版本中，`FileAppender` 以及子类[需要一个 encoder 而不是 layout](https://logback.qos.ch/codes.html#layoutInsteadOfEncoder)。

为什么会有这个改变？

layout 将会在下一章节讨论，它只能将日志事件转换为成 string。而且，考虑到 layout 在日志事件写出时不能控制日志事件，不能将日志事件批量聚合。与之相反的是，encoder 不但可以完全控制字节写出时的格式，而且还可以控制这些字节什么时候被写出。

`PatternLayoutEncoder` 是目前真正唯一有用的 encoder。它仅仅包裹了一个 `PatternLayout` 就完成了大部分的工作。因此，除了不必要的复杂性，encoder 似乎不会有太多的用处。但是，我们希望一个全新的更加强大的 encoder 来改变这种印象。

## Encoder 接口

encoder 负责将日志事件转换为字节数组，并将字节数组写入到合适的 `OutputStream` 中。所以，encoder 可以完全控制将什么样的字节以及什么时候将字节写入到由 appender 维护的 `OutputStream` 中。下面是 [Encoder 接口:](https://logback.qos.ch/xref/ch/qos/logback/core/encoder/Encoder.html)

```java
package ch.qos.logback.core.encoder;

public interface Encoder<E> extends ContextAware, LifeCycle {

   /**
   * This method is called when the owning appender starts or whenever output
   * needs to be directed to a new OutputStream, for instance as a result of a
   * rollover.
   */
  void init(OutputStream os) throws IOException;

  /**
   * Encode and write an event to the appropriate {@link OutputStream}.
   * Implementations are free to defer writing out of the encoded event and
   * instead write in batches.
   */
  void doEncode(E event) throws IOException;


  /**
   * This method is called prior to the closing of the underling
   * {@link OutputStream}. Implementations MUST not close the underlying
   * {@link OutputStream} which is the responsibility of the owning appender.
   */
  void close() throws IOException;
}
```

正如你所看见的，`Encoder` 接口仅仅包含几个方法，但是令人惊讶的是这些方法可以完成许多有用的事情。

## LayoutWrappingEncoder

直到 logback 的 0.9.19 版本，许多 appender 依赖 layout 实例去控制日志的格式化输出。因为基于 layout 接口存在了大量的代码，所以我们需要一种方式容 encoder 与 layout 进行交互。[LayoutWrappingEncoder](https://logback.qos.ch/xref/ch/qos/logback/core/encoder/LayoutWrappingEncoder.html) 就是 encoder 与 layout 之间的桥梁。它实现了 encoder 接口并且包裹了一个 layout，通过委托该 layout 将日志事件转换为字符串。

下面是 `LayoutWrappingEncoder` 的部分代码，说明了如何委托包裹的 layout 实例去完成工作。

```java
package ch.qos.logback.core.encoder;

public class LayoutWrappingEncoder<E> extends EncoderBase<E> {

  protected Layout<E> layout;
  private Charset charset;

   // encode a given event as a byte[]
   public byte[] encode(E event) {
     String txt = layout.doLayout(event);
     return convertToBytes(txt);
  }

  private byte[] convertToBytes(String s) {
    if (charset == null) {
      return s.getBytes();
    } else {
      return s.getBytes(charset);
    }
  } 
}
```

`doLayout()` 方法首先通过包裹的 layout 将日志事件转换为字符串。返回的字符串结果根据用户设定的字符编码 (charset) 再转换为字节数组。

## PatternLayoutEncoder

由于 `PatternLayout` 是最常用的 layout，logback 使用 `PatternLayoutEncoder` 来满足这种用法。它扩展了 `LayoutWrappingEncoder`，被限制用来包裹 `PatternLayout` 实例。

在 logback 0.9.19 版本，无论 `FileAppender` 还是其子类通过 `PatternLayout` 来进行配置，都必须使用 `PatternLayoutEncoder` 来代替。具体的解释参见：[layoutInsteadOfEncoder](https://logback.qos.ch/codes.html#layoutInsteadOfEncoder)。

### immediateFlush 属性

在 `LOGBACK 1.2.0` 中, `immediateFlush` 属性是 appender 的一部分。

### 用格式化字符串作为开头

为了帮助解析日志文件，logback 可以将格式化字符串插入到日志文件的顶部。这个功能默认是**关闭**的。可以为相关的 `PatternLayoutEncoder` 设置 `outputPatternAsHeader` 属性的值为 `true` 来开启这个功能。下面是示例：

```java
<appender name="FILE" class="ch.qos.logback.core.FileAppender"> 
  <file>foo.log</file>
  <encoder>
    <pattern>%d %-5level [%thread] %logger{0}: %msg%n</pattern>
    <outputPatternAsHeader>true</outputPatternAsHeader>
  </encoder> 
</appender>
```

将会在日志文件中输出类似下面的日志：

```java
#logback.classic pattern: %d [%thread] %-5level %logger{36} - %msg%n
2012-04-26 14:54:38,461 [main] DEBUG com.foo.App - Hello world
2012-04-26 14:54:38,461 [main] DEBUG com.foo.App - Hi again
...
```

以 "#logback.classic pattern" 开头的行就是新插入的行。


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


# 第七章：Filters

在之前的章节中介绍的[方法打印以及基本选择规则](https://github.com/Volong/logback-chinese-manual/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%96%B9%E6%B3%95%E6%89%93%E5%8D%B0%E4%BB%A5%E5%8F%8A%E5%9F%BA%E6%9C%AC%E9%80%89%E6%8B%A9%E8%A7%84%E5%88%99)是 logback-classic 的核心。在这章中，将介绍其它的过滤方法。

logback 过滤器基于三元逻辑，允许它们组装或者链接在一起组成一个任意复杂的过滤策略。它们在很大程度上受到 Linux iptables 的启发。

### 在 logback-classic 中

在 logback-classic 中，有两种类型的过滤器，regular 过滤器以及 turbo 过滤器。

#### Regular 过滤器

reqular 过滤器继承自 [`Filter`](https://logback.qos.ch/xref/ch/qos/logback/core/filter/Filter.html) 这个抽象类。本质上它由一个单一的 `decide()` 方法组成，接收一个 `ILoggingEvent` 实例作为参数。

过滤器通过一个有序列表进行管理，并且基于三元逻辑。每个过滤器的 `decide(ILoggingEvent event)` 被依次调用。这个方法返回 [`FilterReply`](https://logback.qos.ch/xref/ch/qos/logback/core/spi/FilterReply.html) 枚举值中的一个， `DENY`, `NEUTRAL` 或者 `ACCEPT`。如果 `decide()` 方法返回 `DENY`，那么日志事件会被丢弃掉，并且不会考虑后续的过滤器。如果返回的值是 `NEUTRAL`，那么才会考虑后续的过滤器。如果没有其它的过滤器了，那么日志事件会被正常处理。如果返回值是 `ACCEPT`，那么会跳过剩下的过滤器而直接被处理。

在 logback-classic 中，过滤器可以被直接添加到 `Appender` 实例上。通过将一个或者多个过滤器添加到 appender 上，你可以通过任意标准来过滤日志事件。例如，日志消息的内容，MDC 的内容，时间，或者日志事件的其它部分。

#### 实现你自己的过滤器

创建一个自己的过滤器非常的简单。只需要继承 `Filter` 并且实现 `decide()` 方法就可以了。

如下所示的 SampleFilter 就是一个简单的例子。如果日志事件包含字符 "sample"， `decide` 方法返回 ACCEPT。对于其他的日志事件，则返回 NEUTRAL。

下面是关于将 `SampleFilter` 添加到 `ConsoleAppender` 上的配置示例：

> Example: *SampleFilterConfig.xml*

```markup
<configuration>
  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">

    <filter class="chapters.filters.SampleFilter" />

    <encoder>
      <pattern>
        %-4relative [%thread] %-5level %logger - %msg%n
      </pattern>
    </encoder>
  </appender>

  <root>
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

在 logback 配置框架 Joran 的帮助下，为过滤器指定属性或者子组件也变得更加的简单。在过滤器类中添加相应的 set 方法，通过 `<filter>` 元素嵌套一个以属性命名的 xml 元素中指定属性的值。

通常情况下，过滤器的逻辑由两个正交的部分组成，match/mismatch 的检验以及基于 match/mismatch 的返回值。例如，对于给定的检验，消息等于 "foobar"，一个过滤器在 match 的情况下返回 ACCEPT，在 mismatch 的情况下返回 NEUTRAL。另一个过滤可能在 match 的情况下返回 NEUTRAL，在 mismatch 的情况下返回 DENY。

注意这种正交，logback 附带了一个 [`AbstractMatcherFilter`](https://logback.qos.ch/xref/ch/qos/logback/core/filter/AbstractMatcherFilter.html) 类，提供了一个有用的骨架用来指定在 match 与 mismatch 情况下的返回值，这两个属性名分别叫做 *OnMatch* 与 *OnMismatch*。logback 中大部分的 regular 过滤器都源于 `AbstractMatcherFilter`。

#### LevelFilter

[`LevelFilter`](https://logback.qos.ch/xref/ch/qos/logback/classic/filter/LevelFilter.html) 基于级别来过滤日志事件。如果事件的级别与配置的级别相等，过滤器会根据配置的 `onMatch` 与 `onMismatch` 属性，接受或者拒绝事件。如下是一个简单的示例：

> Example: *levelFilterConfig.xml*

```markup
<configuration>
  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.classic.filter.LevelFilter">
      <level>INFO</level>
      <onMatch>ACCEPT</onMatch>
      <onMismatch>DENY</onMismatch>
    </filter>
    <encoder>
      <pattern>
        %-4relative [%thread] %-5level %logger{30} - %msg%n
      </pattern>
    </encoder>
  </appender>
  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>
</configuration>
```

#### ThresholdFilter

[`ThresholdFilter`](https://logback.qos.ch/xref/ch/qos/logback/classic/filter/ThresholdFilter.html) 基于给定的临界值来过滤事件。如果事件的级别等于或高于给定的临界值，当调用 `decide()` 时，`ThresholdFilter` 将会返回 NEUTRAL。但是事件的级别低于临界值将会被拒绝。下面是一个简单的例子：

> Example: *thresholdFilterConfig.xml*

```markup
<configuration>
  <appender name="CONSOLE"
    class="ch.qos.logback.core.ConsoleAppender">
    <!-- deny all events with a level below INFO, that is TRACE and DEBUG -->
    <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
      <level>INFO</level>
    </filter>
    <encoder>
      <pattern>
        %-4relative [%thread] %-5level %logger{30} - %msg%n
      </pattern>
    </encoder>
  </appender>
  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>
</configuration>
```

### EvaluatorFilter

[`EvaluatorFilter`](https://logback.qos.ch/xref/ch/qos/logback/core/filter/EvaluatorFilter.html) 是一个通用的过滤器，它封装了一个 `EventEvaluator`。顾名思义，[`EventEvaluator`](https://logback.qos.ch/xref/ch/qos/logback/core/boolex/EventEvaluator.html) 根据给定的标准来评估给定的事件是否符合标准。在 match 和 mismatch 的情况下，`EvaluatorFilter` 将会返回 `onMatch` 或 `onMismatch` 指定的值。

注意 `EventEvaluator` 是一个抽象类。你可以通过继承 `EventEvaluator` 来实现自己事件评估逻辑。

#### GEventEvaluator

[GEventEvaluator](https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/GEventEvaluator.html) 是 [`EventEvaluator`](https://logback.qos.ch/xref/ch/qos/logback/core/boolex/EventEvaluator.html) 具体的实现，它采用 Groovy 表达式作为评估的标准。我们把 Groovy 表达式称为 "Groovy 评估表达式"。Groogy 评估表达式是目前为止进行事件过滤最灵活的方式。`GEventEvaluator` 需要 Groovy 运行环境。参考[相关部分](https://logback.qos.ch/setup.html#groovy)在类路径下添加 Groovy 运行环境。

评估表达式在解析配置文件期间被动态编译。作为用户，不需要考虑实际的情况。但是，你需要确保你的 Groovy 表达式是有效的。

评估表达式作用于当前的日志事件。logback 会自动将 [ILoggingEvent](https://logback.qos.ch/apidocs/ch/qos/logback/classic/spi/ILoggingEvent.html) 类型的日志事件作为变量插入，引用到 'event' 或者它的简称 'e'。TRACE, DEBUG, INFO, WARN 以及 ERROR 也能够被导入到表达式的范围中。所以，"event.level == DEBUG" 与 "e.level == DEBUG" 是等价的。只有当当前日志事件的级别为 DEBUG 时，Groovy 表达式才会返回 `true`。对于其它的级别比较操作，应该通过 `toInt()` 操作将 level 字段转变为整型。

下面是一个比较复杂的例子：

```markup
<configuration>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.core.filter.EvaluatorFilter">      
      <evaluator class="ch.qos.logback.classic.boolex.GEventEvaluator"> 
        <expression>
           e.level.toInt() >= WARN.toInt() &amp;&amp;  <!-- 在 XML 中替代 && -->
           !(e.mdc?.get("req.userAgent") =~ /Googlebot|msnbot|Yahoo/ )
        </expression>
      </evaluator>
      <OnMismatch>DENY</OnMismatch>
      <OnMatch>NEUTRAL</OnMatch>
    </filter>
    <encoder>
      <pattern>
        %-4relative [%thread] %-5level %logger - %msg%n
      </pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

上面的过滤器会让级别在 WARN 及以上的日志事件在控制台显示，除非是由于来自 Google，MSN，Yahoo 的网络爬虫导致的错误。它通过检查与事件相关的 MDC 包含 "req.userAgent" 的值是否匹配 `/Googlebot|msbbot|Yahoo/` 正则表达式。因为 MDC 的映射可能为 null，所以我们使用 Groovy 的[安全解引用操作符](http://groovy.codehaus.org/Null+Object+Pattern)，也就是 `?.` 操作符。这个相等的逻辑在 Java 中的表达式更长。

如果你好奇 user agent 标识符作为值怎样被插入到 key 为 "req.userAgent " 的 MDC 中，那么就会涉及到 logback 为了这个目的附带了一个名为 [`MDCInsertingServletFilter`](https://logback.qos.ch/manual/mdc.html#mis) 的 servlet 过滤器。它将会在接下来的章节中描述。

#### JaninoEventEvaluator

logback-classic 附带的另外一个 `EventEvaluator` 的具体实现名为 [JaninoEventEvaluator](https://logback.qos.ch/xref/ch/qos/logback/classic/boolex/JaninoEventEvaluator.html)，它接受任意返回布尔值的 Java 代码块作为评判标准。我们把这种 Java 布尔表达式称为 "*评估表达式*"。评估表达式在事件过滤中可以更加的灵活。`JaninoEventEvaluator` 需要 [Janino 类库](http://docs.codehaus.org/display/JANINO/Home)。请参见[相关章节](https://logback.qos.ch/setup.html#janino)进行设置。跟 `JaninoEventEvaluator` 相比，`GEventEvaluator` 使用 Groovy 语言，使用起来非常方便。但是 `JaninoEventEvaluator` 将使用运行更快的等效表达式。

评估表达式在解析配置文件期间被动态编译。作为用户，不需要考虑实际的情况。但是，你需要确保你的 Java 表达式是有效的，保证它的评估结果为 true 或 false。

评估表达式对当前日志事件进行评估。logback-classic 自动导出日志事件的各种字段作为变量，为了可以从评估表达式访问。这些导出的变量是大小写敏感的，如下表所示：

| 名字               | 类型                                                                                               | 描述                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| event            | `LoggingEvent`                                                                                   | 日志请求的原始日志事件。下面所有的变量都来自这个日志事件。例如，`event.getMessage()` 返回的字符串跟下面的 `message` 变量返回的字符串一样。                                                                                                                                                                                                                                                                        |
| message          | `String`                                                                                         | 日志请求的原始信息。例如，对于 logger *I*，当你写的是 I.info("Hello {}", name); 时，name 的值被指定为 "Alice"，消息就为 "Hello {}"。                                                                                                                                                                                                                                                            |
| formattedMessage | `String`                                                                                         | 日志请求中格式化后的消息。例如，对于 logger *I*，当你写的是 I.info("Hello {}", name); 时，name 的值被指定为 "Alice"，格式化后的消息就为 "Hello Alice"。                                                                                                                                                                                                                                                 |
| logger           | `String`                                                                                         | logger 的名字                                                                                                                                                                                                                                                                                                                                                   |
| loggerContext    | [`LoggerContextVO`](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/LoggerContextVO.html) | 日志事件属于 logger 上下文中哪个受限的视图 (值对象)                                                                                                                                                                                                                                                                                                                              |
| level            | `int`                                                                                            | 事件级别对应的 int 值。用来创建包含级别的表达式。默认值是 DEBUG，INFO，WARN 以及 ERROR 也是有效的。所以 *level > INFO* 是有效的表达式。                                                                                                                                                                                                                                                                    |
| timeStamp        | `long`                                                                                           | 日志事件创建的时间                                                                                                                                                                                                                                                                                                                                                    |
| marker           | `Marker`                                                                                         | 与日志请求相关的 `Marker` 对象。注意，marker 可能会为 null，因此你需要对这种情况进行检查，进而避免  `NullPointerException`。                                                                                                                                                                                                                                                                        |
| mdc              | `Map`                                                                                            | <p>创建日志事件时包含的所有的 MDC 值的一个映射。可以通过 <em>mdc.get("myKey")</em> 来获取 MDC 中对应的值。在 0.9.30 版本的 logback-classic，mdc 变量永远不会为 null。<br><code>java.util.Map</code> 类型是非参数化的，因为 Janino 不支持泛型。因此，<code>mdc.get()</code> 返回值的类型是 <code>Object</code> 而不是 <code>String</code>。但是可以将返回值强制转换为 <code>String</code>。例如， <code>((String) mdc.get("k")).contains("val")</code>。</p> |
| throwable        | java.lang.Throwable                                                                              | 如果日志事件没有相关的异常，那么变量 "throwable" 的值为 null。"throwable" 不可以被序列化。所以在远程服务器上，这个值永远为 null。想要使用与位置无关的表达式，可以使用下面的 `throwableProxy`。                                                                                                                                                                                                                                    |
| throwableProxy   | [`IThrowableProxy`](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/IThrowableProxy.html) | 日志事件的异常代理。如果日志事件没有相关的异常，那么 `throwableProxy` 的值为 null。与 "throwable" 相反，即使在远程服务器上序列化之后，日志事件相关的异常也不会为 null。                                                                                                                                                                                                                                                     |

下面是具体的例子。

> Example: *basicEventEvaluator.xml*

```markup
<configuration>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.core.filter.EvaluatorFilter">      
      <evaluator> <!-- defaults to type ch.qos.logback.classic.boolex.JaninoEventEvaluator -->
        <expression>return message.contains("billing");</expression>
      </evaluator>
      <OnMismatch>NEUTRAL</OnMismatch>
      <OnMatch>DENY</OnMatch>
    </filter>
    <encoder>
      <pattern>
        %-4relative [%thread] %-5level %logger - %msg%n
      </pattern>
    </encoder>
  </appender>

  <root level="INFO">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

上面的配置将 `EvaluatorFilter` 添加到 `ConsoleAppender`。一个类型为 `JaninoEventEvaluator` 的 evaluator 之后被注入到 `EvaluatorFilter` 中。`<evaluator` 在缺少 *class* 属性的情况下，Joran 会指定 evaluator 的默认类型为 `JaninoEventEvaluator`。这是[少数几个](https://logback.qos.ch/manual/onJoran.html#defaultClassMapping)需要 Joran 默认指定类型的组件。

*expression* 元素对应刚才讨论过的评估表达式。表达式 `return message.contains("billing");` 返回一个布尔值。*message* 变量会被 `JaninoEventEvaluator` 自动导出。

由于 `OnMismatch` 属性的值为 NEUTRAL 以及 `OnMatch` 属性的值为 DENY，所以评估过滤器会丢掉消息包含 "billing" 的日志事件。

[FilterEvents](https://logback.qos.ch/xref/chapters/filters/FilterEvents.html) 发出十条日志请求，编号为 0 到 9。首先在没有过滤器的情况下运行 `FilterEvents`：

```
java chapters.filters.FilterEvents src/main/java/chapters/filters/basicConfiguration.xml
```

输出如下：

```java
0    [main] INFO  chapters.filters.FilterEvents - logging statement 0
0    [main] INFO  chapters.filters.FilterEvents - logging statement 1
0    [main] INFO  chapters.filters.FilterEvents - logging statement 2
0    [main] DEBUG chapters.filters.FilterEvents - logging statement 3
0    [main] INFO  chapters.filters.FilterEvents - logging statement 4
0    [main] INFO  chapters.filters.FilterEvents - logging statement 5
0    [main] ERROR chapters.filters.FilterEvents - billing statement 6
0    [main] INFO  chapters.filters.FilterEvents - logging statement 7
0    [main] INFO  chapters.filters.FilterEvents - logging statement 8
0    [main] INFO  chapters.filters.FilterEvents - logging statement 9
```

假设我们想要丢弃 "billing statement"。*basicEventEvaluator.xml* 中配置的过滤器恰好可以满足这个需求。

通过 *basicEventEvaluator.xml* 运行：

```bash
java chapters.filters.FilterEvents src/main/java/chapters/filters/basicEventEvaluator.xml
```

将会得到：

```java
0    [main] INFO  chapters.filters.FilterEvents - logging statement 0
0    [main] INFO  chapters.filters.FilterEvents - logging statement 1
0    [main] INFO  chapters.filters.FilterEvents - logging statement 2
0    [main] DEBUG chapters.filters.FilterEvents - logging statement 3
0    [main] INFO  chapters.filters.FilterEvents - logging statement 4
0    [main] INFO  chapters.filters.FilterEvents - logging statement 5
0    [main] INFO  chapters.filters.FilterEvents - logging statement 7
0    [main] INFO  chapters.filters.FilterEvents - logging statement 8
0    [main] INFO  chapters.filters.FilterEvents - logging statement 9
```

评估表达式可以是一个 Java 代码块。如下，便是一个有效的表达式。

```markup
<evaluator>
  <expression>
    if(logger.startsWith("org.apache.http"))
      return true;

    if(mdc == null || mdc.get("entity") == null)
      return false;

    String payee = (String) mdc.get("entity");

    if(logger.equals("org.apache.http.wire") &amp;&amp;
        payee.contains("someSpecialValue") &amp;&amp;
        !message.contains("someSecret")) {
      return true;
    }

    return false;
  </expression>
</evaluator>
```

### Matchers

虽然可以通过调用 `String` 类的 [matches()](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html#matches%28java.lang.String%29) 方法来进行模式匹配，但是每次调用 filter 都需要耗费时间重新编译一个新的 `Pattern` 对象。为了消除这种影响，你可以预先定义一个或者多个 [Matcher](https://logback.qos.ch/xref/ch/qos/logback/core/boolex/Matcher.html) 对象。一旦定义了一个 matcher，就可以在评估表达式中重复使用了。

通过一个简单的例子来说明这一点：

> Example: *evaluatorWithMatcher.xml*

```markup
<configuration debug="true">

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.core.filter.EvaluatorFilter">
      <evaluator>        
        <matcher>
          <Name>odd</Name>
          <!-- filter out odd numbered statements -->
          <regex>statement [13579]</regex>
        </matcher>

        <expression>odd.matches(formattedMessage)</expression>
      </evaluator>
      <OnMismatch>NEUTRAL</OnMismatch>
      <OnMatch>DENY</OnMatch>
    </filter>
    <encoder>
      <pattern>%-4relative [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

通过 *evaluatorWithMatcher.xml* 运行：

```bash
java chapters.filters.FilterEvents src/main/java/chapters/filters/evaluatorWithMatcher.xml
```

将会得到：

```java
260  [main] INFO  chapters.filters.FilterEvents - logging statement 0
264  [main] INFO  chapters.filters.FilterEvents - logging statement 2
264  [main] INFO  chapters.filters.FilterEvents - logging statement 4
266  [main] ERROR chapters.filters.FilterEvents - billing statement 6
266  [main] INFO  chapters.filters.FilterEvents - logging statement 8
```

如果你想定义其它的 matcher，可以继续增加 `<matcher>` 元素。

### TurboFilters

`TurboFilter` 对象都继承 [`TurboFilter`](https://logback.qos.ch/xref/ch/qos/logback/classic/turbo/TurboFilter.html) 抽象类。对于 regular 过滤器，它们使用三元逻辑来返回对日志事件的评估。

总之，它们跟之前提到的过滤工作原理差不多。主要的不同点在于 `Filter` 与 `TurboFilter` 对象。

`TurboFilter` 对象被绑定刚在 logger 上下文中。因此，在使用给定的 appender 以及每次发出的日志请求都会调用 `TurboFilter` 对象。因此，turbo 过滤器可以为日志事件提供高性能的过滤，即使是在事件被创建之前。

#### 实现自己的 TurboFilter

想要创建自己的 `TurboFilter` 组件，只需要继承 `TurboFilter` 这个抽象类就可以了。跟之前的一样，想要实现定制的过滤器对象，开发自定义的 `TurboFilter`，只需要实现 `decide()` 方法就可以了。下一个例子，我们会创建一个稍微复杂一点的过滤器：

> Example: *SampleTurboFilter.java*

```java
package chapters.filters;

import org.slf4j.Marker;
import org.slf4j.MarkerFactory;

import ch.qos.logback.classic.Level;
import ch.qos.logback.classic.Logger;
import ch.qos.logback.classic.turbo.TurboFilter;
import ch.qos.logback.core.spi.FilterReply;

public class SampleTurboFilter extends TurboFilter {

  String marker;
  Marker markerToAccept;

  @Override
  public FilterReply decide(Marker marker, Logger logger, Level level,
      String format, Object[] params, Throwable t) {

    if (!isStarted()) {
      return FilterReply.NEUTRAL;
    }

    if ((markerToAccept.equals(marker))) {
      return FilterReply.ACCEPT;
    } else {
      return FilterReply.NEUTRAL;
    }
  }

  public String getMarker() {
    return marker;
  }

  public void setMarker(String markerStr) {
    this.marker = markerStr;
  }

  @Override
  public void start() {
    if (marker != null && marker.trim().length() > 0) {
      markerToAccept = MarkerFactory.getMarker(marker);
      super.start(); 
    }
  }
}
```

`TurboFilter` 接受一个指定的 marker，如果 marker 没有被找到，那么过滤器会将日志事件传递给过滤器链中的下一个过滤器。

为了更加灵活，允许在配置文件指定 marker 用于检测，因此可以使用 get 和 set 方法。我们还可以通过实现 `start()` 方法来检查在配置过程中，指定的选项是否满足。

下面的配置充分利用了我们新创建的 `TurboFilter`。

> Example: *sampleTurboFilterConfig.xml*

```markup
<configuration>
  <turboFilter class="chapters.filters.SampleTurboFilter">
    <Marker>sample</Marker>
  </turboFilter>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>
        %-4relative [%thread] %-5level %logger - %msg%n
      </pattern>
    </encoder>
  </appender>

  <root>
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

loback-classic 附带了几个 `TurboFilter` 类可以开箱即用。[`MDCFilter`](https://logback.qos.ch/xref/ch/qos/logback/classic/turbo/MDCFilter.html) 用来检查给定的值在 MDC 中是否存在。[`DynamicThresholdFilter`](https://logback.qos.ch/apidocs/ch/qos/logback/classic/turbo/DynamicThresholdFilter.html) 根据 MDC key/level 相关的阀值来进行过滤。[`MarkerFilter`](https://logback.qos.ch/xref/ch/qos/logback/classic/turbo/MarkerFilter.html) 用来检查日志请求中指定的 marker 是否存在。

下面的例子使用了 `MDCFilter` 与 `MarkerFilter`。

> Example: *turboFilters.xml*

```markup
<configuration>

  <turboFilter class="ch.qos.logback.classic.turbo.MDCFilter">
    <MDCKey>username</MDCKey>
    <Value>sebastien</Value>
    <OnMatch>ACCEPT</OnMatch>
  </turboFilter>

  <turboFilter class="ch.qos.logback.classic.turbo.MarkerFilter">
    <Marker>billing</Marker>
    <OnMatch>DENY</OnMatch>
  </turboFilter>

  <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%date [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="INFO">
    <appender-ref ref="console" />
  </root>  
</configuration>
```

执行以下命令：

```bash
java chapters.filters.FilterEvents src/main/java/chapters/filters/turboFilters.xml
```

在之前我们看到 [`FilterEvents`](https://logback.qos.ch/xref/chapters/filters/FilterEvents.html) 输出了 10 条日志请求，编号 0 到 9。除了第 3 条与第 6 条，所有的请求都是 INFO 级别的，与 root logger 的级别一致。第 3 条日志请求是 `DEBUG` 级别的，在有效级别之下。但是，因为 MDC 的 key "username" 在第三条请求之前设置为 "sebastien"，之后才被移除，所以 `MDCFilter` 接受这条请求 (仅仅只有这条请求)。第 6 条请求的级别为 `ERROR`，被标记为 "billing"。因此，它会被 `MarkerFilter` (配置文件中第二个 turbo 过滤器) 拒绝。

因此，`FilterEvents` 通过 *turboFilters.xml* 输出的信息如下：

```java
2018-08-20 23:19:28,807 [main] INFO  chapters.filters.FilterEvents - logging statement 0
2018-08-20 23:19:28,810 [main] INFO  chapters.filters.FilterEvents - logging statement 1
2018-08-20 23:19:28,810 [main] INFO  chapters.filters.FilterEvents - logging statement 2
2018-08-20 23:19:28,810 [main] DEBUG chapters.filters.FilterEvents - logging statement 3
2018-08-20 23:19:28,810 [main] INFO  chapters.filters.FilterEvents - logging statement 4
2018-08-20 23:19:28,810 [main] INFO  chapters.filters.FilterEvents - logging statement 5
2018-08-20 23:19:28,810 [main] INFO  chapters.filters.FilterEvents - logging statement 7
2018-08-20 23:19:28,811 [main] INFO  chapters.filters.FilterEvents - logging statement 8
2018-08-20 23:19:28,811 [main] INFO  chapters.filters.FilterEvents - logging statement 9
```

可以看到，第 3 条日志请求，本来不应该被展示出来，因为我们仅仅只关注 *INFO* 级别的请求，但是它匹配了第一个 `TurboFilter`，所以被接受了。

第 6 条日志请求，它是 *ERROR* 级别的日志，应该被显示。但是因为满足第二个 `TurboFilter`，它的 `OnMatch` 设置为 *DENY*，所以第 6 条请求不会被展示。

#### DuplicateMessageFilter

`DuplicateMessageFilter` 可以拿出来单独阐述。这个过滤器检测重复的消息，在重复了一定次数之后，丢弃掉重复的消息。

这个过滤器使用字符串是否相等来检查是否重复。不会检查非常相似，仅仅只差几个字符的字符串。例如：

```java
logger.debug("Hello "+name0);
logger.debug("Hello "+name1);
```

如果 `name0` 与 `name1` 有不同的值，那么两个 "Hello" 消息会被认为不相关。根据用户的需要，将会可能会支持相似字符串的检查，限制相似字符串的重复，而不是完全相同的。

但是在参数化日志请求中，只考虑原始消息。例如，下面两条日志请求，原始消息为 "Hello {}"，它们被认为是想相等的，因此被认为是重复出现。

```javascript
logger.debug("Hello {}.", name0);
logger.debug("Hello {}.", name1);
```

可以通过 `AllowedRepetitions` 属性来指定允许重复的次数。如果这个属性被设置为 1，那么第二条以及后续的日志消息都会被丢弃掉。类似的，如果被设置为 2，那么第三条及后续的日志消息会被丢弃掉。这个值默认设置为 5。

为了检测重复，过滤器需要在内部的缓存中保留对旧消息的引用。通过 `CacheSize` 来控制缓存的大小。默认情况下，这个值为 100。

> Example: *duplicateMessage.xml*

```markup
<configuration>

  <turboFilter class="ch.qos.logback.classic.turbo.DuplicateMessageFilter"/>

  <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%date [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="INFO">
    <appender-ref ref="console" />
  </root>  
</configuration>
```

`FilterEvents` 通过 `duplicateMessage.xml` 配置后输出如下：

```java
2018-08-21 09:09:22,036 [main] INFO  chapters.filters.FilterEvents - logging statement 0
2018-08-21 09:09:22,041 [main] INFO  chapters.filters.FilterEvents - logging statement 1
2018-08-21 09:09:22,041 [main] INFO  chapters.filters.FilterEvents - logging statement 2
2018-08-21 09:09:22,041 [main] INFO  chapters.filters.FilterEvents - logging statement 4
2018-08-21 09:09:22,041 [main] INFO  chapters.filters.FilterEvents - logging statement 5
2018-08-21 09:09:22,050 [main] ERROR chapters.filters.FilterEvents - billing statement 6
```

"logging statement 0" 是消息 "logging statement {}"j 第一次出现。"logging statement 1" 是第一次重复。"logging statement 2" 是第二次重复。有趣的是，虽然 "logging statement 3" 的级别为 *DEBUG*，为第三次重复。但是根据[方法打印以及基本选择规则](https://github.com/Volong/logback-chinese-manual/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%96%B9%E6%B3%95%E6%89%93%E5%8D%B0%E4%BB%A5%E5%8F%8A%E5%9F%BA%E6%9C%AC%E9%80%89%E6%8B%A9%E8%A7%84%E5%88%99)，它被丢弃了。这也说明了 turbo 过滤器会在其它过滤器之前调用，包括在基本选择规则之前。因此 `DuplicateMessageFilter` 认为 "logging statement 3" 是第三次重复，而不会管它是否会在之后过滤器链的处理中被丢弃掉。"logging statement 4" 是第四次重复。"logging statement 5" 是第五次。因此默认的重复次数是 5，所以之后的语句都会被丢弃掉。(注：指的是 "logging statement {}")。

## 在 logback-access 中

logback-access 提供了 logback-classic 提供的大部分功能。特别地，`Filter` 对象同样是有效的，并且以同样的方式工作，就像 logback-classic 的副本一样，但是有一个显著的区别。logback-access 过滤器对 [`AccessEvent`](https://logback.qos.ch/xref/ch/qos/logback/access/spi/AccessEvent.html) 实例起作用，而不是 `LoggingEvent` 实例。目前，logback-access 只提供了以下有限的过滤器。如果你想建议添加额外的过滤器，请通过 logback-dev 邮件列表进行联系。

### CountingFilter

在 [`CountingFilter`](https://logback.qos.ch/manual/xref/ch/qos/logback/access/filter/CountingFilter.html) 类的帮助下，logback-access 可以提供对服务器访问数据的统计。在初始化的死后，`CountingFilter` 将自己作为一个 MBean 注册到平台的 JMX 服务上。你可以通过轮询 MBean 来进行数据统计。例如，平均每分钟，每小时，每天，每周，或者每月。其它的统计，例如周计，天计，小时计，月计或者总计也是可以获取的。

下面的 *logback-access.xml* 配置文件声明了一个 `CountingFilter`。

```markup
<configuration>
  <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />

  <filter class="ch.qos.logback.access.filter.CountingFilter">
    <name>countingFilter</name>
  </filter>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%h %l %u %t \"%r\" %s %b</pattern>
    </encoder>
  </appender>

  <appender-ref ref="STDOUT" />
</configuration>
```

你可以通过 `jconsole` 查看有 `CountingFilte` 在你平台的 JMX 服务上维护的各种统计信息。

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbSsYf2FRldaze_Y%2FcountingFilter.png?generation=1568702636191151\&alt=media)

#### EvaluatorFilter

[`EvaluatorFilter`](https://logback.qos.ch/xref/ch/qos/logback/core/filter/EvaluatorFilter.html) 是一个通用的过滤器，维护了一个 `EventEvaluator`。顾名思义，[`EventEvaluator`](https://logback.qos.ch/xref/ch/qos/logback/core/boolex/EventEvaluator.html) 根据给定的标准判断给定的日志事件是否满足，`EvaluatorFilter` 将会根据 match 与 mismatch 的情况，返回由 `onMatch` 或 `onMismatch` 属性指定的值。`EvaluatorFilter` 在之前的 logback-classic 中已经讨论过了 ([见上面](https://github.com/Volong/logback-chinese-manual/blob/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AFilters.md#evaluatorfilter))。现在大部分都是对之前讨论的重复。

注意 `EventEvaluator` 是一个抽象类。你可以通过继承 `EventEvaluator` 来实现你自己的评估逻辑。logback-access 附带了一个名为 [JaninoEventEvaluator](https://logback.qos.ch/xref/ch/qos/logback/access/boolex/JaninoEventEvaluator.html) 的具体实现。它可以接收任意的 Java 表达式作为评估标准。我们把这种 Java 代码块称为 "*评估表达式*"。评估表达式在事件过滤中有较大的灵活性。`JaninoEventEvaluator` 需要 [Janino 类库](http://docs.codehaus.org/display/JANINO/Home)。请查看[相应的文档](https://logback.qos.ch/setup.html#janino)进行设置。

评估表达式在解析配置文件的过程中被动态编译。作为用户，你不需要知道实际的细节。但是，你需要保证 Java 表达式返回一个布尔值，能够计算为 true 或者 false。

评估表达式可以对当前访问的事件进行评估。logback-access 会自动导出当前 `AccessEvent` 实例到变量 **event** 下。你可以通过 `event` 变量读取 HTTP 请求中以及 HTTP 响应中的各种数据。查看 [AccessEvent 类的源码](https://logback.qos.ch/xref/ch/qos/logback/access/spi/AccessEvent.html)来查看具体的列表。

下个配置文件基于 HTTP 响应码 [404 (Not Found)](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) 来进行过滤。每一个 404 的请求都会在控制台打印出来。

> Example: *accessEventEvaluator.xml*

```markup
<configuration>
  <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.core.filter.EvaluatorFilter">
      <evaluator>
        <expression>event.getStatusCode() == 404</expression>
      </evaluator>
      <onMismatch>DENY</onMismatch>
    </filter>
   <encoder><pattern>%h %l %u %t %r %s %b</pattern></encoder>
  </appender>

  <appender-ref ref="STDOUT" />
</configuration>
```

下面的例子，打印 404 错误，但是排除了请求 CSS 文件的请求。

> Example: *accessEventEvaluator2.xml*

```markup
<configuration>
  <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />
  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.core.filter.EvaluatorFilter">
      <evaluator name="Eval404">
        <expression>
         (event.getStatusCode() == 404)
           &amp;&amp;  <!-- & 符号需要被转义 -->
         !(event.getRequestURI().contains(".css"))
        </expression>
      </evaluator>
      <onMismatch>DENY</onMismatch>
    </filter>

   <encoder><pattern>%h %l %u %t %r %s %b</pattern></encoder>
  </appender>

  <appender-ref ref="STDOUT" />
</configuration>
```


# 第八章：MDC

logback 设计的目标之一是审计与调试复杂的分布式应用。大部分的分布式系统需要同时处理多个客户端。在一个系统典型的多线程实现中，不同的线程处理不同的客户端。一种可能但是不建议的方式是在每个客户端实例化一个新的且独立的 logger，来区分一个客户端与另一个客户端的日志输出。这种方式会导致 logger 急剧增加并且会增加维护成本。

一种轻量级的技术是给每个为客户端服务的 logger 打一个标记。Neil Harrison 在 *Patterns for Logging Diagnostic Messages* in Pattern Languages of Program Design 3, edited by R. Martin, D. Riehle, and F. Buschmann (Addison-Wesley, 1997) 这本书中描述了这种方法。logback 在 SLF4J API 利用了这种技术的变体：诊断上下文映射 (MDC)。

为了给每个请求打上唯一的标记，用户需要将上下文信息放到 `MDC` (Mapped Diagnostic Context 的缩写) 中。下面列出了 MDC 类中主要的部分。完成的方法列表请查看 [MDC javadocs](http://www.slf4j.org/api/org/slf4j/MDC.html)。

```java
package org.slf4j;

public class MDC {
  // 将上下文的值作为 MDC 的 key 放到线程上下的 map 中
  public static void put(String key, String val);

  // 通过 key 获取上下文标识
  public static String get(String key);

  // 通过 key 移除上下文标识
  public static void remove(String key);

  // 清除 MDC 中所有的 entry
  public static void clear();
}
```

`MDC` 类中只包含静态方法。它让开发人员可以在 *诊断上下文* 中放置信息，而后通过特定的 logback 组件去获取。`MDC` 在 *每个线程的基础上* 管理上下文信息。通常，当为一个新客户端启动服务时，开发人员会将特定的上文信息插入到 MDC 中。例如，客户端 id，客户端 IP 地址，请求参数等。如果 logback 组件配置得当的话，会自动在每个日志条目中包含这些信息。

请注意，logback-classic 实现的 MDC，假设值以适当的频率放置。还需注意的一点是，子线程不会自动继承父线程的 MDC。

下面的 [SimpleMDC](https://logback.qos.ch/xref/chapters/mdc/SimpleMDC.html) 说明了这点。

> Example: [*SimpleMDC.java*](https://logback.qos.ch/xref/chapters/mdc/SimpleMDC.html)

```java
package chapters.mdc;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

import ch.qos.logback.classic.PatternLayout;
import ch.qos.logback.core.ConsoleAppender;

public class SimpleMDC {
  static public void main(String[] args) throws Exception {

    // 你可以选择在任何时候将值放入 MDC 中    
    MDC.put("first", "Dorothy");

    [ SNIP ]

    Logger logger = LoggerFactory.getLogger(SimpleMDC.class);

    MDC.put("last", "Parker");

    logger.info("Check enclosed.");
    logger.debug("The most beautiful two words in English.");

    MDC.put("first", "Richard");
    MDC.put("last", "Nixon");
    logger.info("I am not a crook.");
    logger.info("Attributed to the former US president. 17 Nov 1973.");
  }

  [ SNIP ]

}
```

main 方法在启动的时候在 `MDC` 中将 *Dorothy* 关联到 *first* 上。你可以在 `MDC` 放置尽可能多的键值对，反正你开心就好。多次插入同一个 key，新值会覆盖旧值。然后代码继续配置 logback。

为了简洁，我们隐藏了配置文件 [simpleMDC.xml](http://github.com/qos-ch/logback/blob/master/logback-examples/src/main/java/chapters/mdc/simpleMDC.xml) 中的其它配置。下面的一些相关的配置。

```markup
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender"> 
  <layout>
    <Pattern>%X{first} %X{last} - %m%n</Pattern>
  </layout> 
</appender>
```

注意 *X%* 转换符在 `PatternLayout` 中的用法。*X%* 转换符使用了两次，一次用于 key 为 *first*，一次用于 key 为 *last*。在获得了 `SimpleMDC.class` 中的 logger 之后，通过代码将 *Parker* 关联到 *last* 上。然后通过 logger 打印了两条不同的信息。最后，通过代码重新设置了 `MDC` 为不同的值，并打印了几条日志请求。运行 SimpleMDC 将会输出：

```java
Dorothy Parker - Check enclosed.
Dorothy Parker - The most beautiful two words in English.
Richard Nixon - I am not a crook.
Richard Nixon - Attributed to the former US president. 17 Nov 1973.
```

`SimpleMDC` 展示了正确配置 logback layout 就可以自动输出 `MDC` 的信息。而且，`MDC` 中信息可以被多个 logger 使用。

## 高级用法

MDC 在客户端服务器架构中最为重要。通常，服务器上的多个线程为多个客户端提供服务。尽管 MDC 中的方法是静态的，但是是以每个线程为基础来进行管理的，允许每个服务线程都打上一个 `MDC` 标记。`MDC` 中的 `put()` 与 `get()` 操作仅仅只影响当前线程中的 `MDC`。其它线程中 `MDC` 不会受到影响。给定的 `MDC` 信息在每个线程的基础上进行管理。每个线程都有一份 `MDC` 的拷贝。因此，在对 `MDC` 进行编程时，开发人员没有必要去考虑线程安全或者同步问题。它自己会安全的处理这些问题。

下面有一个稍微高级一点的例子。它显示了如何在客户端-服务端上设置 `MDC`。例 7.2 展示的是服务端实现 `NumberCruncher` 接口。`NumberCruncher` 接口仅仅只包含一个方法 `factor()`。客户端使用 RMI 技术，调用服务器应用程序上的 `factor()` 方法来获取一个整数的不同因子。

> Example 7.2 *NumberCruncher.java*

```java
package chapters.mdc;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface NumberCruncher extends Remote {
  int[] factor(int number) throws RemoteException;
}
```

例 7.3 展示了 `NumberCruncherServer` 实现了 `NumberCruncher` 接口。它的主要方法是在本地主机上导出一个 RMI 注册表，并在一个众所周知的端口号上接受请求 (反正我是不知道😓)。

> *Example 7.3* *NumberCruncherServer.java*

```java
package chapters.mdc;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Vector;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.classic.joran.JoranConfigurator;
import ch.qos.logback.core.joran.spi.JoranException;


/**
 * A simple NumberCruncher implementation that logs its progress when
 * factoring numbers. The purpose of the whole exercise is to show the
 * use of mapped diagnostic contexts in order to distinguish the log
 * output from different client requests.
 * */
public class NumberCruncherServer extends UnicastRemoteObject
  implements NumberCruncher {

  private static final long serialVersionUID = 1L;

  static Logger logger = LoggerFactory.getLogger(NumberCruncherServer.class);

  public NumberCruncherServer() throws RemoteException {
  }

  public int[] factor(int number) throws RemoteException {
    // The client's host is an important source of information.
    try {
      MDC.put("client", NumberCruncherServer.getClientHost());
    } catch (java.rmi.server.ServerNotActiveException e) {
      logger.warn("Caught unexpected ServerNotActiveException.", e);
    }

    // The information contained within the request is another source
    // of distinctive information. It might reveal the users name,
    // date of request, request ID etc. In servlet type environments,
    // useful information is contained in the HttpRequest or in the  
    // HttpSession.
    MDC.put("number", String.valueOf(number));

    logger.info("Beginning to factor.");

    if (number <= 0) {
      throw new IllegalArgumentException(number +
        " is not a positive integer.");
    } else if (number == 1) {
      return new int[] { 1 };
    }

    Vector<Integer> factors = new Vector<Integer>();
    int n = number;

    for (int i = 2; (i <= n) && ((i * i) <= number); i++) {
      // It is bad practice to place log requests within tight loops.
      // It is done here to show interleaved log output from
      // different requests. 
      logger.debug("Trying " + i + " as a factor.");

      if ((n % i) == 0) {
        logger.info("Found factor " + i);
        factors.addElement(new Integer(i));

        do {
          n /= i;
        } while ((n % i) == 0);
      }

      // Placing artificial delays in tight loops will also lead to
      // sub-optimal results. :-)
      delay(100);
    }

    if (n != 1) {
      logger.info("Found factor " + n);
      factors.addElement(new Integer(n));
    }

    int len = factors.size();

    int[] result = new int[len];

    for (int i = 0; i < len; i++) {
      result[i] = ((Integer) factors.elementAt(i)).intValue();
    }

    // clean up
    MDC.remove("client");
    MDC.remove("number");

    return result;
  }

  static void usage(String msg) {
    System.err.println(msg);
    System.err.println("Usage: java chapters.mdc.NumberCruncherServer configFile\n" +
      "   where configFile is a logback configuration file.");
    System.exit(1);
  }

  public static void delay(int millis) {
    try {
      Thread.sleep(millis);
    } catch (InterruptedException e) {
    }
  }

  public static void main(String[] args) {
    if (args.length != 1) {
      usage("Wrong number of arguments.");
    }

    String configFile = args[0];

    if (configFile.endsWith(".xml")) {
      try {
        LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();
        JoranConfigurator configurator = new JoranConfigurator();
        configurator.setContext(lc);
        lc.reset();
        configurator.doConfigure(args[0]);
      } catch (JoranException je) {
        je.printStackTrace();
      }
    }

    NumberCruncherServer ncs;

    try {
      ncs = new NumberCruncherServer();
      logger.info("Creating registry.");

      Registry registry = LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
      registry.rebind("Factor", ncs);
      logger.info("NumberCruncherServer bound and ready.");
    } catch (Exception e) {
      logger.error("Could not bind NumberCruncherServer.", e);

      return;
    }
  }
}
```

`factor(int number)` 的实现特别的相关。它在启动的时候将客户端的名字通过 key *client* 放到 `MDC` 中。客户端通过请求将整数放到 `MDC` 中的 *number* 这个 key 下。在计算出整数的不同因子之后，然后将结果返回给客户端。在返回结果之前，通过调用 `MDC.remove()` 清除 *client* 与 *number* 的值。通常，`put()` 操作应该由 `remove()` 操作来平衡。否则的话，`MDC` 将会保留旧值。我们推荐无论何时，在 finally 代码块中调用 `remove` 操作，用来确保该操作的执行，而不用关心代码的具体执行路径。

在解释完理论之后，我们准备运行这个例子。通过一下命令运行这个服务：

```bash
java chapters.mdc.NumberCruncherServer src/main/java/chapters/mdc/mdc1.xml
```

*mdc1.xml* 的内容如下：

> Example: *mdc1.xml*

```markup
<configuration>
  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <layout>
      <Pattern>%-4r [%thread] %-5level C:%X{client} N:%X{number} - %msg%n</Pattern>
    </layout>       
  </appender>

  <root level="debug">
    <appender-ref ref="CONSOLE"/>
  </root>  
</configuration>
```

注意 *%X* 转换符在 `Pattern` 选项中使用。

通过以下命令执行 `NumberCruncherClient` 应用：

```bash
java chapters.mdc.NumberCruncherClient hostname
```

*hostname* 是 `NumberCruncherServer` 运行的主机名。

在客户端执行多个实例，第一个客户端请求服务器对 129 进行因数分解，随后，第二个客户端请求服务器对 71 进行因数分解。服务器的输出如下：

```java
70984 [RMI TCP Connection(4)-192.168.1.6] INFO  C:orion N:129 - Beginning to factor.
70984 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 2 as a factor.
71093 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 3 as a factor.
71093 [RMI TCP Connection(4)-192.168.1.6] INFO  C:orion N:129 - Found factor 3
71187 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 4 as a factor.
71297 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 5 as a factor.
71390 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 6 as a factor.
71453 [RMI TCP Connection(5)-192.168.1.6] INFO  C:orion N:71 - Beginning to factor.
71453 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 2 as a factor.
71484 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 7 as a factor.
71547 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 3 as a factor.
71593 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 8 as a factor.
71656 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 4 as a factor.
71687 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 9 as a factor.
71750 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 5 as a factor.
71797 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 10 as a factor.
71859 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 6 as a factor.
71890 [RMI TCP Connection(4)-192.168.1.6] DEBUG C:orion N:129 - Trying 11 as a factor.
71953 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 7 as a factor.
72000 [RMI TCP Connection(4)-192.168.1.6] INFO  C:orion N:129 - Found factor 43
72062 [RMI TCP Connection(5)-192.168.1.6] DEBUG C:orion N:71 - Trying 8 as a factor.
72156 [RMI TCP Connection(5)-192.168.1.6] INFO  C:orion N:71 - Found factor 71
```

从上面的输出可以看出客户端运行在一个叫做 *orion* 的主机上。尽管服务器在独立的线程中几乎同时处理客户端的请求，但是可以通过 `MDC` 来区分每个客户端的日志输出。示例中的是通过 *number* 来进行标识。

细心的读者可能已经注意到，可以通过线程名来区分每个请求。如果服务端重复使用线程，那么使用线程名可能会导致一下误解。也就是一个给定线程在服务完请求之后，接着去服务下一个请求，在这种情况下，很难去区分每个请求。因为 `MDC` 是受应用开发人员的控制，所以不会受这个影响。(是吗？开发人员就这么可靠吗？)

## 自动获取 `MDC`

正如我们之前看到的，对多个客户端进行请求时，`MDC` 非常有用。在 web 应用中管理用户认证，一个简单的处理方式是在 `MDC` 中设置用户名，在用户退出时进行移除。不幸的是，使用这个技术并不总是可靠的。因为 `MDC` 是在单线程的基础进行管理，服务器重复使用线程可能会导致 `MDC` 包含错误的信息。

为了在处理请求时，`MDC` 中包含的信息一直都是正确的。一种可能的处理方式是在开始处理之前存储用户名，结束时进行移除。[`Filter`](http://java.sun.com/javaee/5/docs/api/javax/servlet/Filter.html) 可以用来处理这种情况。

在 servlet 过滤器 `doFilter` 方法中，我们可以通过 request (或者 cookie) 获取用户的相关信息，并存到 `MDC` 中。其它过滤器或者 servlet 后续的处理会从 `MDC` 中受益。最后，当我们的 servlet 过滤器再次获得控制时，就有机会去清除 MDC 中的数据。

下面是一个过滤器的实现：

> Example: *UserServletFilter.java*

```java
package chapters.mdc;

import java.io.IOException;
import java.security.Principal;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.slf4j.MDC;

public class UserServletFilter implements Filter {

  private final String USER_KEY = "username";

  public void destroy() {
  }

  public void doFilter(ServletRequest request, ServletResponse response,
    FilterChain chain) throws IOException, ServletException {

    boolean successfulRegistration = false;

    HttpServletRequest req = (HttpServletRequest) request;    
    Principal principal = req.getUserPrincipal();
    // Please note that we could have also used a cookie to 
    // retrieve the user name

    if (principal != null) {
      String username = principal.getName();
      successfulRegistration = registerUsername(username);
    } 

    try {
      chain.doFilter(request, response);
    } finally {
      if (successfulRegistration) {
        MDC.remove(USER_KEY);
      }
    }
  }

  public void init(FilterConfig arg0) throws ServletException {
  }


  /**
   * Register the user in the MDC under USER_KEY.
   * 
   * @param username
   * @return true id the user can be successfully registered
   */
  private boolean registerUsername(String username) {
    if (username != null && username.trim().length() > 0) {
      MDC.put(USER_KEY, username);
      return true;
    }
    return false;
  }
}
```

当过滤器的 `doFilter` 被调用时，它首先会在 request 中去寻找 `java.security.Principal` 对象。这个对象包含了当前认证用户的名字。如果找到了用户的信息，会将它注册到 `MDC` 中。

一个过滤器链执行完成，那么这个过滤器会从 `MDC` 中移除用户信息。

刚才我们描述的方法只是在请求期间，或者线程处理中才去设置 MDC 的值。其它的线程不会受到影响。而且，任何给定的线程在任何时候都会包含正确的 MDC 数据。

## MDC 与线程管理

MDC 的副本不能总是由工作线程从初始化线程继承。当使用 `java.util.concurrent.Executors` 进行线程管理时就是这种情况。例如，`newCachedThreadPool` 方法会创建一个 `ThreadPoolExecutor`，跟其它线程池代码一样，有着复杂的线程创建逻辑。

在这些情况下，推荐在提交任务去执行之前，在源线程上调用 `MDC.getCopyOfContextMap()`。当任务运行的时候，它的第一个动作，应该是调用 `MDC.setContextMapValues()` 将原始 MDC 值的存储副本与新的 `Executor` 管理线程关联起来。

## MDCInsertingServletFilter

在 web 应用中，获取给定 HTTP 请求的主机名，请求 URI 以及 user-agent 是十分有用的。[`MDCInsertingServletFilter`](https://logback.qos.ch/xref/ch/qos/logback/classic/helpers/MDCInsertingServletFilter.html) 通过如下的 key，将数据插入到 MDC 中。

| MDC key             | MDC value                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `req.remoteHost`    | 由 [getRemoteHost()](http://java.sun.com/j2ee/sdk_1.3/techdocs/api/javax/servlet/ServletRequest.html#getRemoteHost%28%29) 返回            |
| `req.xForwardedFor` | 请求头 ["X-Forwarded-For"](http://en.wikipedia.org/wiki/X-Forwarded-For) 的值                                                               |
| `req.method`        | 由 [getMethod()](http://java.sun.com/j2ee/sdk_1.3/techdocs/api/javax/servlet/http/HttpServletRequest.html#getMethod%28%29) 返回           |
| `req.requestURI`    | 由 [getRequestURI()](http://java.sun.com/j2ee/sdk_1.3/techdocs/api/javax/servlet/http/HttpServletRequest.html#getRequestURI%28%29) 返回   |
| `req.requestURL`    | 由 [getRequestURL()](http://java.sun.com/j2ee/sdk_1.3/techdocs/api/javax/servlet/http/HttpServletRequest.html#getRequestURL%28%29) 返回   |
| `req.queryString`   | 由 [getQueryString()](http://java.sun.com/j2ee/sdk_1.3/techdocs/api/javax/servlet/http/HttpServletRequest.html#getQueryString%28%29) 返回 |
| `req.userAgent`     | 请求头 "User-Agent" 的值                                                                                                                    |

想要使用 `MDCInsertingServletFilter`，需要在 *web.xml* 中添加以下行：

```markup
<filter>
  <filter-name>MDCInsertingServletFilter</filter-name>
  <filter-class>
    ch.qos.logback.classic.helpers.MDCInsertingServletFilter
  </filter-class>
</filter>
<filter-mapping>
  <filter-name>MDCInsertingServletFilter</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

**如果你的 web 应用有多个过滤器，请确保 `MDCInsertingServletFilter` 在其它过滤器之前声明** 。例如，假设 web 应用的主要处理是在过滤器 'F' 中完成，那么如果 `MDCInsertingServletFilter` 在 'F' 之后被调用，那么在 'F' 中被调用的代码将看不到 `MDCInsertingServletFilter` 设置的 MDC 的值。(这不是废话吗......)

一旦使用了该过滤器，通过 %X 可以输出相对应的 MDC 的值。例如，想要在一行上打印远程主机，后面跟着请求的 URI，令一行打印日志，后面跟着日志消息。那么你应该如下设置 `PatternLayout`：

```markup
%X{req.remoteHost} %X{req.requestURI}%n%d - %m%n
```


# 第九章：日志隔离

## 问题：日志隔离

这个章节处理一个相对困难的问题，为在同一个 web 或 EJB 容器运行的多个客户端提供一个隔离的日志环境。在接下来的章节中，"应用" 一词用来表示 web 应用以及 J2EE 应用。在隔离的日志环境中，每个应用将会看到一个不同的 logback 环境。所以一个应用的 logback 配置不会影响到另一个。从技术角度看，每个 web 应用都会保存一份 `LoggerContext` 的独立拷贝。在 logback 中，`LoggerContext` 产生的每个 logger 对象只要在内存中存活，都会被保留。这个问题的一个变体是隔离应用的日志与容器本身的日志。

## 最简单的方法

假设你的容器支持子级优先加载，那么日志隔离可以通过在每个应用中内置一份 slf4j 与 logback 的 jar 包完成。对于 web 应用，将 slf4j 与 logback 的 jar 包放在 *WEB-INF/lib* 文件夹下，这种方式可以有效的赋予每个 web 应用隔离的日志环境。*logback.xml* 文件放在 *WEB-INF/classes* 下，当 logback 被加载进内存时，该配置会被加载。

由于容器提供了类加载器隔离，每个 web 应用将会加载自己拷贝的 `LoggerContext` 以及自己拷贝的 *logback.xml*。

其实，也不全是。有时候你会被迫将 SLF4J 与 logback 的 jar 包放在同一个地方供所有的应用访问。通常，这是因为共享库需要使用 SLF4J。在这种情况下，所有的应用将会共享同一个日志环境。有许多其它的应用场景需要将 SLF4J 与 logback 的 jar 包放在同一个地方，那么所有的应用都会看到，这样就不能通过类加载隔离来对日志环境进行隔离了。但是并不是没有其它的办法，请继续往下阅读。

## 上下文选择器

logback 提供了一种机制为每个单独 SLF4J 实例以及 logback 类加载进内存提供了多个 logger context。当你写下：

```java
Logger logger = LoggerFactory.getLogger("foo");
```

`LoggerFactory` 类中的 `getLogger()` 方法会要求 SLF4J 绑定 `ILoggerFactory`。当 SLF4J 绑定到 logback，会委托 [ContextSelector](https://logback.qos.ch/apidocs/ch/qos/logback/classic/selector/ContextSelector.html) 实例去返回 `ILoggerFactory`。`ContextSelector` 的实现一直都会返回同一个 `LoggerContext` 实例，也就是默认的 logger context。

你可以通过 *logback.ContextSelector* 这个系统属性指定不同的上下文选择器。假设你想指定 `myPackage.myContextSelector` 这个类的实例为上下文选择器，那么你可以通过如下方式添加一个系统属性：

```java
-Dlogback.ContextSelector=myPackage.myContextSelector
```

这个上下文选择器需要实现 `ContextSelector` 这个接口，并且有一个构造方法，该构造方法仅仅只接收 `LoggerContext` 实例作为参数。

### ContextJNDISelector

logback-classic 附带了一个名为 `ContextJNDISelector` 的选择器，它基于 JNDI 查找的有效数据去选择一个 logger 上下文。这个方法利用 J2EE 规范强制 JNDI 数据分离。因此，同样的环境变量在不同的应用中能够设置不同的值。换句话说，在不同的应用中调用 `LoggerFactory.getLogger()` 不同 logger 上下文中的 logger。即使所有的应用都共享内存中同一个 LoggerFactory 类。这样就能够对你的日志进行隔离。

要开启 `ContextJNDISelector`，需要设置系统属性 *logback.ContextSelector* 为 "JNDI"。如下：

```java
-Dlogback.ContextSelector=JNDI
```

注意，`JNDI` 是 `ch.qos.logback.classic.selector.ContextJNDISelector` 的缩写形式。

### 在应用中设置 JNDI

在你的每个应用中，你需要为应用命名 logger 上下文。对于 web 应用，通过 *web.xml* 指定 JNDI 环境条目。如果你应用的名字为 "kenobi"，那么你可以添加如下的 XML 元素到你的 web.xml 文件中：

```markup
<env-entry>
  <env-entry-name>logback/context-name</env-entry-name>
  <env-entry-type>java.lang.String</env-entry-type>
  <env-entry-value>kenobi</env-entry-value>
</env-entry>
```

假设你已经开启了 `ContextJNDISelector`，那么将使用一个名为 "kenobi" 的 logger 上下文来为 Kenobi 打印日志。而且，logger 上下文 "kenobi" 会按照约定使用线程上下文类加载器去寻找一个名为 *logback-kenobi.xml* 的配置文件进行初始化。因此，对于例子中 "kenobi" web 应用，应该将 *logback-kenobi.xml* 放在 *WEB-INF/classes* 文件夹下。

只要你喜欢，通过设置 "logback/configuration-resource" JNDI 变量，你可以不按照约定，而是指定一个不同的配置文件。例如，对于 "kenobi" web 应用，如果你想指定配置文件为 *aFolder/my\_config.xml* 而不是约定的 *logback-kenobi.xml*，你可以在 web.xml 中添加如下的 xml 元素：

```markup
<env-entry>
  <env-entry-name>logback/configuration-resource</env-entry-name>
  <env-entry-type>java.lang.String</env-entry-type>
  <env-entry-value>aFolder/my_config.xml</env-entry-value>
</env-entry>
```

*my\_config.xml* 文件需要放在 *WEB-INF/classes/aFolder/* 下。需要记住的一点是，使用当前线程的上下文类加载来查找配置文件作为 Java 资源。

### 通过 Tomcat 配置 ContextJNDISelector

首先，将 logback 的 jar 包 (logback-classic-1.3.0-alpha4.jar, logback-core-1.3.0-alpha4.jar and slf4j-api-1.8.0-beta1.jar) 放在 Tomcat 全局的类文件夹下。在 Tomcat 6.x 中，这个文件夹是 *$TOMCAT\_HOME/lib/*。

系统属性 *logback.ContextSelector* 可以在 *catalina.sh* 脚本中添加如下的行来进行设置。Windows 下为 *catalina.bat*。在 *$TOMCAT\_HOME/bin* 文件夹下。

```java
JAVA_OPTS="$JAVA_OPTS -Dlogback.ContextSelector=JNDI"
```

### 应用热部署

当 web 应用被回收或者关闭时，我们强烈推荐关闭现有的 `LoggerContext`，以便正确的进行垃圾回收。logback 附带了一个名为 [`ContextDetachingSCL`](https://logback.qos.ch/xref/ch/qos/logback/classic/selector/servlet/ContextDetachingSCL.html) 的 `ServletContextListener`，用来分离旧 web 应用中的 `ContextSelector` 实例。可以在 *web.xml* 中添加如下的行来指定：

```markup
<listener>
  <listener-class>ch.qos.logback.classic.selector.servlet.ContextDetachingSCL</listener-class>
</listener>
```

**`NOTE`** 大部分的容器会按照声明的顺序调用 `contextInitialized()` 方法，但是按照相反的顺序调用 `contextDestroyed()` 方法。也就是说，如果你在 *web.xml* 中声明了多个 `ServletContextListener`，那么 `ContextDetachingSCL` 应该*第一个*声明，那么在应用关闭的时候，它的 `contextDestroyed()` 方法将会在 *最后* 被调用。

### 更好的性能

当 `ContextJNDISelector` 处于活动状态，每次查找一个 logger，JNDI 查找必须被执行。这样对性能会有影响，特别是当你使用一个非静态的 logger 时。logback 附带了一个名为 [LoggerContextFilter](https://logback.qos.ch/xref/ch/qos/logback/classic/selector/servlet/LoggerContextFilter.html) 的过滤器，为了避免 JNDI 查找的消耗而特意设计。可以通过在 web.xml 中添加如下的行来指定：

```markup
<filter>
  <filter-name>LoggerContextFilter</filter-name>
  <filter-class>ch.qos.logback.classic.selector.servlet.LoggerContextFilter</filter-class>
</filter>
<filter-mapping>
  <filter-name>LoggerContextFilter</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

在每个 http 请求开始的时候，`LoggerContextFilter` 会获取应用相关的 logger 上下文，然后把它放在 `ThreadLocal` 变量中。`ContextJNDISelector` 会看 `ThreadLocal` 变量是否已经被设置，如果是，那么 JNDI 查找将会跳过。在每个 http 请求结束的时候，`ThreadLocal` 变量就会为 null。使用 `LoggerContextFilter` 会大幅度的提高 logger 检索性能。

使 `ThreadLocal` 为 null，可以让 web 应用在停止或者回收时对它进行垃圾回收。

## 在共享库中改进静态引用

当 SLF4J 与 logback 组件被所有应用共享时，`ContextJNDISelector` 可以很好的创建日志隔离。当 `ContextJNDISelector` 处于活动状态时，每次对 `LoggerFactory.getLogger()` 的调用将会返回一个属于正在被调用/当前应用的一个 logger 上下文中的 logger。

通常是通过静态引用来引用一个 logger。(你们前面的例子全部是通过实例变量来引用😓)例如：

```java
public class Foo {
  static Logger logger = LoggerFactory.getLogger(Foo.class);
  ...
}
```

静态 logger 引用在内存以及在 CPU 中都是有效率的。使用一个 logger 引用用于该类的所有实例。而且，当加载类到内存中时，这个 logger 实例只会被查找一次。如果宿主类属于某个应用程序，比如 kenobi，那么这个静态的 logger 将通过抽象的 `ContextJNDISelector` 附加到 kenobi 的 logger 上下文中。类似的，如果宿主类属于其它的应用，比如 yoda，那么它的静态 logger 引用将会再一次通过抽象的 `ContextJNDISelector` 附加到 logger 的上下文中。

如果一个名为 `Mustafar` 的类，属于某个类库，被 *kenobi* 与 *yoda* 共享。只要 `Mustafar` 没有使用静态引用，那么每次对 `LoggerFactory.getLogger()` 的调用将会返回一个属于正在被调用/当前的应用的 logger 上下文中的 logger。但是如果 `Mustafar` 有一个静态的引用，那么当应用第一次调用它时，这个 logger 将会被附加到 logger 上下文中。因此，一旦共享类使用静态的 logger 引用， `ContextJNDISelector` 不会提供日志隔离。这个问题很长时间都没有得到解决。

透明且完美的解决这个问题的唯一方法是引入另一个间接级别的内部 logger，这样每个 logger 以某种方式将工作委托给一个附加在合适上下文的内部 logger 上。这个方法实现起来非常困难，并且会产生大量的计算开销。这个并不是我们追求的方式。(无语了😶，前面说完美，然后马上说不行)

不言而喻，一个非常简单方式去解决 "共享类的静态 logger" 问题的方式是将共享类移到 web 应用的内部。(也就是不进行共享) (废话一大堆，罗里吧嗦)。如果不共享不可能实现，我们可以使用 [`SiftingAppender`](https://logback.qos.ch/manual/appenders.html#SiftingAppender) 使用 JNDI 数据作为隔离标准去进行日志隔离。

> 这段话翻译的我真的是蛋疼的很。外国人不是思维特别严谨的吗？我怎么觉得反复无常，飘忽不定呢。还是我根本就没理解作者想要说的是什么？

logback 内置了一个名为 [JNDIBasedContextDiscriminator](https://logback.qos.ch/xref/ch/qos/logback/classic/sift/JNDIBasedContextDiscriminator.html) 的鉴别器。它可以返回由 `ContextJNDISelector` 计算得来的当前 logger 上下文的名字。`SiftingAppender` 与 `JNDIBasedContextDiscriminator` 结合使用将会为每个 web 应用创建一个单独的 appender。

```markup
<configuration>

  <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />  

  <appender name="SIFT" class="ch.qos.logback.classic.sift.SiftingAppender">
    <discriminator class="ch.qos.logback.classic.sift.JNDIBasedContextDiscriminator">
      <defaultValue>unknown</defaultValue>
    </discriminator>
    <sift>
      <appender name="FILE-${contextName}" class="ch.qos.logback.core.FileAppender">
        <file>${contextName}.log</file>
        <encoder>
          <pattern>%-50(%level %logger{35}) cn=%contextName - %msg%n</pattern>
         </encoder>
      </appender>
     </sift>
    </appender>

  <root level="DEBUG">
    <appender-ref ref="SIFT" />
  </root>
</configuration>
```

如果 kenobi 与 yoda 都是 web 应用，那么上面的配置将会把 yoda 的日志输出到 *yoda.log*，kenobi 的日志输出到 *kenobi.log* 中。这甚至适用共享类中静态 logger 生成的日志。

你可以通过 [logback-starwars](http://github.com/ceki/logback-starwars) 这个项目来对这项技术进行尝试。

上面这个方法解决了日志隔离的问题，但是相对比较复杂。它需要合理的使用 `ContextJNDISelector` 以及通过 `SiftingAppender` 包裹 appender 进行托管。`SiftingAppender` 本身就不是一个平凡的东西。

每个日志上下文都可以通过同个文件或者不同的文件进行配置。选择权在于你。让所有的上下文使用同一份配置文件会更加简单，因为只有一份文件需要去维护。为每个应用维护一个配置文件会更难维护，但是会更加的灵活。

我们已经完成了吗？可以宣布胜利，然后回家了吗？不全是。

假设 web 应用 `yoda` 已经在 `kenobi` 之前被初始化。为了初始化 `yoda`，访问 `http://localhost:port/yoda/servlet` 将会调用 `YodaServlet`。这个 servlet 仅仅只会说 hello，以及在调用 `Mustafar` 中的 `foo` 方法之前打印消息，不必感到奇怪，它只是简单的打印消息，然后返回。

在 `YodaServlet` 被调用后，*yoda.log* 会包含如下内容：

```java
DEBUG ch.qos.starwars.yoda.YodaServlet             cn=yoda - in doGet()
DEBUG ch.qos.starwars.shared.Mustafar              cn=yoda - in foo()
```

注意两个日志条目是如何与 "yoda" 上下文的名字相关联的。logger `ch.qos.starwars.shared.Mustafar` 会一直附加在 'yoda' 上下文中，直到服务被停止。

访问 `http://localhost:port/kenobi/servlet` 将会在 *kenobi.log* 中输出：

```java
DEBUG ch.qos.starwars.kenobi.KenobiServlet          cn=kenobi - in doGet()
DEBUG ch.qos.starwars.shared.Mustafar               cn=yoda - in foo()
```

尽管 logger `ch.qos.starwars.shared.Mustafar` 输出日志到 *kenobi.log* 中，但是它仍然是附加在 'yoda' 上。因此，我们有两个日志上下文输出日志到同一个文件。虽然日志隔离可以按照我们的意愿进行，但是 FileAppender 实例并不能安全写入到同一个文件中，除非它们开启 `prudent` 模式。否则的话，目标文件将会被毁坏。

下面是在 `prudent` 模式下的配置文件：

```markup
<configuration>

  <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />  

  <appender name="SIFT" class="ch.qos.logback.classic.sift.SiftingAppender">
    <discriminator class="ch.qos.logback.classic.sift.JNDIBasedContextDiscriminator">
      <defaultValue>unknown</defaultValue>
    </discriminator>
    <sift>
      <appender name="FILE-${contextName}" class="ch.qos.logback.core.FileAppender">
        <file>${contextName}.log</file>
        <prudent>true</prudent>
        <encoder>
          <pattern>%-50(%level %logger{35}) cn=%contextName - %msg%n</pattern>
         </encoder>
      </appender>
     </sift>
    </appender>

  <root level="DEBUG">
    <appender-ref ref="SIFT" />
  </root>
</configuration>
```

如果你可以跟上我们目前的讨论，并且你已经尝试过 logback-starwars 这个示例。那么你现在一定是沉迷于日志记录。那么你应该考虑 [专业帮助](http://www.qos.ch/shop/products/professionalSupport)。


# 第十章：JMX 配置器

顾名思义，`JMXConfigurator` 允许通过 JMX 来配置 logback。简单来说就是，它允许你从默认配置文件，指定的文件或者 URL 重新配置 logback，列出 logger 以及修改 logger 级别。

### 使用 JMX 配置器

如果你的运行在 JDK 1.6 或者更高的版本，那么你仅仅需要在命令行调用 `jconsole`，然后连接到你服务器上的 MBeanServer。如果你运行在老版本的 JVM 上，那么你需要查看[在服务上使用 JMX](https://logback.qos.ch/manual/jmxConfig.html#jmxEnablingServer)。

在配置文件中开启 `JMXConfigurator` 只需要一行。如下：

```markup
<configuration>
  <jmxConfigurator />

  <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
    <layout class="ch.qos.logback.classic.PatternLayout">
      <Pattern>%date [%thread] %-5level %logger{25} - %msg%n</Pattern>
    </layout>
  </appender>

  <root level="debug">
    <appender-ref ref="console" />
  </root>  
</configuration>
```

在你通过 *jconsole* 连接到服务器上之后，在 MBeans 面板上，在 "ch.qos.logback.classic.jmx.Configurator" 文件夹下你可以看到几个选项。如下图所示：

### 在 `jconsole` 中查看 `JMXConfigurator` 的截图

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbO7nrnTaWUv9b9G%2FjmxConfigurator.gif?generation=1568702627520451\&alt=media)

所以，你可以

* 使用默认配置文件重新加载 logback 的配置
* 通过指定的 URL 重新加载配置
* 通过指定的文件重新加载配置
* 设置指定的 logger 的级别。想要设置为 null，传递 "null" 字符串就可以
* 获取指定 logger 的级别。返回值可以为 null
* 或者指定 logger 的[有效级别](https://github.com/Volong/logback-chinese-manual/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%9C%89%E6%95%88%E7%AD%89%E7%BA%A7%E5%8F%88%E7%A7%B0%E4%B8%BA%E7%AD%89%E7%BA%A7%E7%BB%A7%E6%89%BF)

`JMXConfigurator` 将已经存在的 logger 以及状态当作属性进行展示。

这个状态列表可以帮助你诊断 logger 的内部状态。

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbO91dF36LmItCrh%2FstatusList.gif?generation=1568702627530845\&alt=media)

### 避免内存泄漏

如果你的应用部署在 web 服务器或者应用服务器上，注册的 `JMXConfigurator` 实例会从系统类加载器创建一个引用到你的应用中。在应用停止或者重新部署事，它会阻止垃圾回收，那么将会导致内存泄漏。

因此，除非你的应用是单机的 Java 应用，否则的话，你必须从 JVM 的 Mbeans 服务上注销 `JMXConfigurator` 实例。通过 `LoggerContext` 调用 `reset()` 方法将会自动注销任何 JMXConfigurator 实例。一个好的方法去重置 logger 上下文是通过 `javax.servlet.ServletContextListener` 中的 `contextDestroyed()` 方法。示例代码如下：

```java
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

import org.slf4j.LoggerFactory;
import ch.qos.logback.classic.LoggerContext;

public class MyContextListener implements ServletContextListener {

  public void contextDestroyed(ServletContextEvent sce) {
    LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();
    lc.stop();
  }

  public void contextInitialized(ServletContextEvent sce) {
  }
}
```

## `JMXConfigurator` 与多个 web 应用

如果你在同一个服务器上部署了多个 web 应用，并且你没有重写默认的[上下文选择器](https://github.com/Volong/logback-chinese-manual/blob/master/09%E7%AC%AC%E4%B9%9D%E7%AB%A0%EF%BC%9A%E6%97%A5%E5%BF%97%E9%9A%94%E7%A6%BB.md#%E4%B8%8A%E4%B8%8B%E6%96%87%E9%80%89%E6%8B%A9%E5%99%A8)，以及你把 *logback-\\*.jar *与* slf4j-api.jar *放到了每个 web 应用的* WEB-INF/lib\* 文件夹下。之后默认每个 `JMXConfigurator` 实例将会注册在同一个名字下。也就是 "ch.qos.logback.classic:Name=default,Type=ch.qos.logback.classic.jmx.JMXConfigurator" 。换句话说，在你每个 web 应用中，默认各种 `JMXConfigurator` 实例关联的 logger 上下文将会冲突。

为了避免这种不必要的冲突，你仅仅需要[设置应用的日志上下文](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E8%AE%BE%E7%BD%AE-context-%E7%9A%84%E5%90%8D%E5%AD%97)，`JMXConfigurator` 将会自动使用你设置好的名字。

例如，如果部署两个名为 "Koala" 与 "Wombat" 的 web 应用，那么你可以在 Koala 的配置文件中这样写：

```markup
<configuration>
  <contextName>Koala</contextName>
  <jmxConfigurator/>
  ...
<configuration>
```

在 Wombat 的配置文件中，你可以这样写：

```markup
<configuration>
  <contextName>Wombat</contextName>x
  <jmxConfigurator/>
  ...
<configuration>
```

在 jconsole 的 MBeans 面板中，你可以看到两个不同的 `JMXConfigurator` 实例：

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbOB2zYOWchHmUDT%2Fmultiple.gif?generation=1568702627486662\&alt=media)

通过  元素的 "objectName" 属性，你可以完全控制注册到 MBeans 服务中 JMXConfigurator 的名字。

### 在服务器中开启 JMX

如果你的服务器运行在 JDK 1.6 或者更高版本，那么 JMX 默认开启。

对于旧版的 JVM，我们建议你参考你所使用的 web 服务器上 JMX 相关的文档。这些文档在 [Tomcat](http://tomcat.apache.org/tomcat-6.0-doc/monitoring.html) 以及 [Jetty](http://docs.codehaus.org/display/JETTY/JMX) 中都可以获得。在这个文档中，我们将会详细叙述 Tomcat 与 Jetty 相关的配置步骤。

#### 在 Jetty 中开启 JMX (在 JDK 1.5 以及 JDK 1.6 测试过)

接下来的已经在 JDK 1.5 及 1.6 中测试过。在 JDK 1.6 以及以后的版本中，你的服务器是默认开启 JMX 的，你可以但是不需要遵循下面所讨论的。在 JDK 1.5 下，添加 JMX 支持，只需要在 *$JETTY\_HOME/etc/jetty.xml* 配置文件中添加一个额外的支持。下面是需要被添加的元素：

```markup
<Call id="MBeanServer" class="java.lang.management.ManagementFactory" 
      name="getPlatformMBeanServer"/>

<Get id="Container" name="container">
  <Call name="addEventListener">
    <Arg>
      <New class="org.mortbay.management.MBeanContainer">
        <Arg><Ref id="MBeanServer"/></Arg>
        <Call name="start" />
      </New>
    </Arg>
  </Call>
</Get>
```

如果你想通过 `jconsole` 访问 Jetty 中的 MBeans，那么你需要在启动 Jetty 前设置系统属性 "com.sun.management.jmxremote"。

对于单机版本的 Jetty，通过：

```java
java -Dcom.sun.management.jmxremote -jar start.jar [config files]
```

如果你想将 Jetty 作为 Maven 插件启动，那么你需要通过 `MAVEN_OPTS` shell 变量设置系统属性 "com.sun.management.jmxremote"：

```java
MAVEN_OPTS="-Dcom.sun.management.jmxremote"
mvn jetty:run
```

你可以通过 `jconsole` 访问 Jetty 的 MBeans 以及 logback 的 `JMXConfigurator`。

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbODBGN3iT-8S2gg%2Fjconsole15_jetty.gif?generation=1568702627474506\&alt=media)

在你连接上以后，你可以访问 `JMXConfigurator`，就像上面的[截图](https://github.com/Volong/logback-chinese-manual/blob/master/10%E7%AC%AC%E5%8D%81%E7%AB%A0%EF%BC%9AJMX%20%E9%85%8D%E7%BD%AE%E5%99%A8.md#%E5%9C%A8-jconsole-%E4%B8%AD%E6%9F%A5%E7%9C%8B-jmxconfigurator-%E7%9A%84%E6%88%AA%E5%9B%BE)一样。

#### MX4j 与 Jetty (在 JDK 1.5 以及 1.6 测试过)

假设你已经下载了 [MX4J](http://mx4j.sourceforge.net/)，你想要通过 MX4J 的 HTTP 接口访问 `JMXConfigurator`，你需要添加之前讨论过的配置，并且设置 managementPort。

```markup
<Call id="MBeanServer"
    class="java.lang.management.ManagementFactory"
    name="getPlatformMBeanServer"/>

<Get id="Container" name="container">
  <Call name="addEventListener">
    <Arg>
      <New class="org.mortbay.management.MBeanContainer">
        <Arg><Ref id="MBeanServer"/></Arg>
        <Set name="managementPort">8082</Set>
        <Call name="start" />
      </New>
    </Arg>
  </Call>
</Get>
```

而且，*mx4j-tools.jar* 需要添加到 Jetty 的类路径下。

如果你想将 Jetty 作为 Maven 的插件运行，那么你需要添加 *mx4j-tools* 作为依赖。

```markup
<plugin>
  <groupId>org.mortbay.jetty</groupId>
  <artifactId>maven-jetty-plugin</artifactId>
  <configuration>
    <jettyConfig>path/to/jetty.xml</jettyConfig>
    ...
  </configuration>
  <dependencies>
    <dependency>
      <groupId>mx4j</groupId>
      <artifactId>mx4j-tools</artifactId>
      <version>3.0.1</version>
    </dependency>
  </dependencies>
</plugin>
```

在通过以上配置启动了 Jetty 之后，可以通过如下的 URL 访问 `JMXConfigurator` (查找 "ch.qos.logback.classic")：

```http
http://localhost:8082/
```

下面是通过 MX4J 接口访问的截图信息：

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbOFFaiaeWZV4YPO%2Fmx4j_jetty.gif?generation=1568702627480901\&alt=media)

#### 在 Tomcat 配置 JMX (在 JDK 1.5 以及 1.6 测试过)

如果你使用 JDK 1.6 以及以后的版本，你的服务器是默认开启 JMX 的，你可以但是不需要遵循下面所讨论的。在 JDK 1.5 下，需要在 Tomcat 的 *$TOMCAT\_HOME/bin/catalina.bat/sh* shell 脚本中添加如下的行：

```
CATALINA_OPTS="-Dcom.sun.management.jmxremote"
```

一旦通过这些配置启动后，可以通过在命令行输入如下命令来获取 Tomcat 的 MBeans 以及 logback 的 `JMXConfigurator`：

```
jconsole
```

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbOHQTA7H1dVUwwq%2Fjconsole15_tomcat.gif?generation=1568702627456748\&alt=media)

在你连接上以后，你可以访问 `JMXConfigurator`，就像上面的[截图](https://github.com/Volong/logback-chinese-manual/blob/master/10%E7%AC%AC%E5%8D%81%E7%AB%A0%EF%BC%9AJMX%20%E9%85%8D%E7%BD%AE%E5%99%A8.md#%E5%9C%A8-jconsole-%E4%B8%AD%E6%9F%A5%E7%9C%8B-jmxconfigurator-%E7%9A%84%E6%88%AA%E5%9B%BE)一样。

#### MX4J 与 Tomcat (在 JDK 1.5 以及 1.6 测试过)

你可能想要通过 MX4J 提供的 web 接口访问 JMX 组件。在这种情况下，下面是必须的步骤：

假设你已经下载了 [MX4J](http://mx4j.sourceforge.net/)，将 *mx4j-tools.jar* 文件放到了 *$TOMCAT\_HOME/bin/* 文件夹下。那么，添加如下的行到 *$TOMCAT\_HOME/bin/catalina.sh* 配置文件中：

```
<!-- at the beginning of the file -->
CATALINA_OPTS="-Dcom.sun.management.jmxremote"

<!-- in the "Add on extra jar files to CLASSPATH" section -->
CLASSPATH="$CLASSPATH":"$CATALINA_HOME"/bin/mx4j-tools.jar
```

最后，在 *$TOMCAT\_HOME/conf/server.xml* 文件中声明一个新的 `Connector`：

```markup
<Connector port="0" 
  handler.list="mx"
  mx.enabled="true" 
  mx.httpHost="localhost" 
  mx.httpPort="8082" 
  protocol="AJP/1.3" />
```

一旦 Tomcat 启动后，你可以通过访问如下的 URL 找到 JMXConfigurator (查找 "ch.qos.logback.classic")：

下面是通过 MX4J 接口访问得到的截图：

![](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbOJLuEgs5P4aXvg%2Fmx4j_tomcat.gif?generation=1568702627522814\&alt=media)


# 第十一章：Joran

Joran 代表寒冷的西北风，常常猛烈的吹在日列瓦湖上。位于西欧中部的日列瓦湖，表面上看起来比其它许多欧洲的湖泊都要小。但是它的平均深度有 153 米，异常的深。并且，它是西欧最大的淡水湖。

正如前几章所示，logback 基于 Joran，一个成熟的，灵活的并且强大的配置框架。logback 提供的许多的功能，只能基于 Joran 来实现。这章将专注于 Joran 的基本设计以及一些明显的特征。

Joran 实际上是一个通用的配置系统，能够被独立用于日志记录。为了强调这一点，我们需要说明的是 logback-core 模块没有 logger 的概念。所以，本章的大多数示例与 logger，appender，layout 无关。

本章节中的示例可以在 *LOGBACK\_HOME/logback-examples/src/main/java/chapters/onJoran/* 文件夹下被找到。

要安装 Joran，只需要[下载](https://logback.qos.ch/download.html)，然后将 *logback-core-1.3.0-alpha4.jar* 放到类路径下。

## 历史回顾

反射是 Java 语言一个强大的特性，使得声明式的配置软件系统变成可能。例如，EJB 许多重要的属性都被配置在 *ejb.xml* 文件中。尽管 EJB 是用 Java 编写的，但是它们的许多属性都是通过 *ejb.xml* 来指定的。类似的，logback 也可以通过指定的 XML 格式的配置文件来进行设置。JDK 1.5 中的注解在 EJB 3.0 被大量使用用来替换之前 XML 文件中的许多指令。Joran 也会充分利用注解，但是使用的范围少的多。由于 logback 配置的动态特性 (相比 EJB)，Joran 使用注解相当有限。

在 logback 它爹 log4j 中， `DOMConfigurator` 类是 log4j 1.2.x 以及以后的版本的一部分。也能够解析 XML 的配置文件。`DOMConfigurator` 的编写方式强迫开发人员在配置文件的结构每次发生改变时，需要重新调整代码。调整的代码需要重新编译并重新部署。同样重要的是，`DOMConfigurator` 的代码由循环组成，用于解析子元素，包含了许多 if/else 语句。这样的代码散发着冗余以及重复的味道。 [commons-digester](http://jakarta.apache.org/commons/digester/) 告诉我们可以通过模式匹配规则来解析 XML 文件。在解析的时候，解析器会应用匹配了指定模式的规则。规则类通常比较小，并且具有专业性。因此，理解与维护相对简单。

有了 `DOMConfigurator` 的经验，我们开始开发 `Joran`，一个在 logback 中使用的、强大的配置框架。Joran 受到了 commons-digester 项目很大的启发。但是，它使用了一个稍微不同术语。在 commons-digester 中，规则可以看做由模式和规则组成，如同 `Digester.addRule(String pattern, Rule rule)` 方法展示的一样。我们发现一个不必要的困惑是规则包含自身，但是不是递归，而是有不同的含义。在 Joran 中，规则由模式以及动作组成。当相应的模式被匹配时，会调用一个动作。模式与动作的这种关系是 Joran 的核心。值得注意的是，可以使用简单的模式来处理复杂的匹配，或者更确切的是说是使用精确匹配以及通配符匹配。

### SAX 还是 DOM ?

由于 SAX API 是基于事件的结构，所以基于 SAX 的工具不能很好的处理前向引用，也就是引用元素被定义晚于当前元素被处理。循环引用元素也有同样的问题。通常，DOM API 允许用户在所有的元素上进行搜索，并且可以向前跳转。

这种额外的灵活性导致我们在开始的时候选择 DOM API 作为 Joran 的解析器。在经过了一些实验之后，我们发现当解析规则通过模式以及动作表达时，在解析 DOM 树时处理相隔较远的元素没有意义。*Joran 只需要 XML 文档中连续且深度优先顺序的元素。*

而且，在发生错误时，SAX API 提供元素的位置信息可以让 Joran 去展示精确的行号与列号。位置信息在识别解析问题时非常方便。

### 非目标

考虑到它的高度动态特性，Joran API 没有打算去解析包含几千个元素的 XML 文档。

### 模式 (Pattern)

Joran 的模式本质上就是一个字符串。有两种形式的模式：*exact* 与 *wildcard*。模式 "a/b" 可以用来匹配嵌套在 `<a>` 元素中的 `<b>` 元素。因为 *exact* 匹配的设置，"a/b" 模式不会匹配其它的元素。

wildcard 可以用来进行后缀与前缀匹配。例如，"\*/a" 可以用来匹配任何以 "a" 结尾的后缀，也就是 XML 文档中任何 `<a>` 元素，但是不包含任何嵌套在 `<a>` 中的元素。"a/\*" 将会匹配任何 `<a>` 开头的元素，即任何嵌套在 `<a>` 中的元素。

### 动作

正如之前提到的，Joran 解析规则由相关联的模式组成。动作继承了 [`Action`](https://logback.qos.ch/xref/ch/qos/logback/core/joran/action/Action.html) 类，包含了如下的抽象方法。为了简单起见，其它的方法被隐藏了。

```java
package ch.qos.logback.core.joran.action;

import org.xml.sax.Attributes;
import org.xml.sax.Locator;
import ch.qos.logback.core.joran.spi.InterpretationContext;

public abstract class Action extends ContextAwareBase {
  /**
   * 当解析器遇到一个元素匹配
   * {@link ch.qos.logback.core.joran.spi.Pattern Pattern}.
   */
  public abstract void begin(InterpretationContext ic, String name,
      Attributes attributes) throws ActionException;

  /**
   * 传递包含元素的 body (作为字符串) 参数
   */
  public void body(InterpretationContext ic, String body)
      throws ActionException {
    // NOP
  }

  /*
   * 当解析器遇到最后一个元素匹配
   * {@link ch.qos.logback.core.joran.spi.Pattern Pattern}.
   */
  public abstract void end(InterpretationContext ic, String name)
      throws ActionException;
}
```

所以，每个动作必须实现 `begin()` 与 `end()` 方法。`body()` 方法的实现是可选的，因为 `Action` 提供了一个空的实现。

### 规则存储

如前面提到的，根据匹配模式调用动作是 Joran 的核心概念。规则跟模式与动作相关联。规则被存储在 [RuleStore](https://logback.qos.ch/xref/ch/qos/logback/core/joran/spi/RuleStore.html) 中。

根据之前提到的，Joran 建立在 SAX API 上。当 XML 文档被解析时，每个元素会生成对应 start、body、end 的事件。当 Joran 的配置器接收到这些事件时，它会根据*当前模式*去规则存储中查找对应的动作。例如，元素 *B* 的 start、body、end 事件的当前模式为 "A/B"，内嵌在一个顶级元素 *A* 中。当 Joran 接收并处理 SAX 事件时，它会自动维护当前模式的数据结构。

当有几个规则匹配到当前模式时，精确匹配会比后缀匹配优先，后缀匹配会比前缀匹配优先。对于详细的实现细节，请查看 [SimpleRuleStore](https://logback.qos.ch/xref/ch/qos/logback/core/joran/spi/SimpleRuleStore.html) 类。

### 解析上下文

为了允许多个动作相互协作，在调用 begin 与 end 方法时会包含解析上下文，作为第一个参数传递。解析上下文包含对象栈，对象映射，错误列表以及 Joran 调用动作时的一个引用。请查看 [`InterpretationContext`](https://logback.qos.ch/xref/ch/qos/logback/core/joran/spi/InterpretationContext.html) 类中详细的字段列表。

动作可以通过对象栈获取，入栈，出栈操作，或者通过对象映射来放置、获取 key 来进行协作。动作可以在解析上下文的 `StatusManager` 上通过添加错误项来报告任何错误条件。

### Hello world

这个章节中的第一个例子将会展示使用 Joran 所需要最小条件。这个例子由一个名为 [`HelloWorldAction`](https://logback.qos.ch/xref/chapters/onJoran/helloWorld/HelloWorldAction.html) 的动作组成。在调用它的 `begin()` 方法时会在控制台打印 "Hello World"。配置文件由解析器负责解析。为了实现本章的目的，我们实现了一个非常的简单的配置器 [`SimpleConfigurator`](https://logback.qos.ch/xref/chapters/onJoran/SimpleConfigurator.html)。[`HelloWorld`](https://logback.qos.ch/xref/chapters/onJoran/helloWorld/HelloWorld.html) 应用会将下面这些结合在一起：

* 创建一个规则与 `Context` 的映射
* 创建一个与 *hello-world* 模式相关的解析规则，以及对应的 `HelloWorldAction` 实例
* 创建一个 `SimpleConfigutator`，解析之前提到的规则映射。
* 调用配置器的 `doConfigure` 方法，解析 XML 文件
* 最后，将会收集上下文中的所有转态信息。如果有的话，将会打印

*hello.xml* 包含一个 \ 元素，没有任何其它的内置元素。详细的内容请查看 *logback-examples/src/main/java/chapters/onJoran/helloWorld/* 文件夹中的内容。

通过 *hello.xml* 运行 HelloWorld 应用将会在控制台输出 "Hello World"。

```java
java chapters.onJoran.helloWorld.HelloWorld src/main/java/chapters/onJoran/helloWorld/hello.xml
```

强烈推荐你在规则存储中添加新的规则，更改 XML 配置 (hello.xml)，以及添加新的动作。

### 动作相互合作

*logback-examples/src/main/java/joran/calculator/* 文件夹包含了几个动作，为了完成简单的计算，它们通过共同的对象栈相互合作。

*calculator1.xml* 文件包含一个 `computation` 元素，内嵌了一个 `literal` 元素。如下：

> Example: calculator1.xml

```markup
<computation name="total">
  <literal value="3"/>
</computation>
```

在应用 [`Calculator1`](https://logback.qos.ch/xref/chapters/onJoran/calculator/Calculator1.html) 中，我们声明了各种解析规则 (模式与动作) 基于 XML 文档的内容一起合作来计算一个结果。

通过 *calculator1.xml* 运行 `Calculator`：

```
java chapters.onJoran.calculator.Calculator1 src/main/java/chapters/onJoran/calculator/calculator1.xml
```

将会输出：

```java
The computation named [total] resulted in the value 3
```

解析 *calculator1.xml* 文档包含如下的步骤：

* 开始事件对应的 \  元素转换为当前模式 "/computation"。因为在  [`Calculator1`](https://logback.qos.ch/xref/chapters/onJoran/calculator/Calculator1.html) 中我们为 "/computation" 模式关联了一个 [`ComputationAction1`](https://logback.qos.ch/xref/chapters/onJoran/calculator/ComputationAction1.html) 实例。`ComputationAction1` 实例中的 `begin()` 方法将会被调用
* 开始事件对应的 \ 元素转换为当前模式 "/computation/literal"。为 "/computation/literal" 关联了一个 [`LiteralAction`](https://logback.qos.ch/xref/chapters/onJoran/calculator/LiteralAction.html) 实例。`LiteralAction` 实例中的 `begin()` 方法将会被调用。
* 同样的，结束事件对应的 \ 元素将会触发 `ComputationAction1` 实例中的 `end()` 方法的调用。

有意思的是动作相互合作的方式。`LiteralAction` 读取到一个字面值，并将其放到对象栈中，由 `InterpretationContext` 来维护。一旦完成，其它的动作可以获取该值或者对其进行更改。`ComputationAction1` 类的 `end()` 方法从栈中获取值，并打印。

下一个例子中， *calculator2.xml* 有点复杂，但是更加有趣。

> 有趣个鸡儿
>
> Example：*calculator2.xml*

```markup
<computation name="toto">
  <literal value="7"/>
  <literal value="3"/>
  <add/>
  <literal value="3"/>
  <multiply/>
</computation>
```

在之前的例子中，为了响应 \ 元素，[`LiteralAction`](https://logback.qos.ch/xref/chapters/onJoran/calculator/LiteralAction.html) 实例会将 value 属性对应的整数放到解析上下文中的栈顶。在这个例子中，也就是 *calculator2.xml*，这个值是 7 与 3。为了响应 \ 元素。[`AddAction`](https://logback.qos.ch/xref/chapters/onJoran/calculator/AddAction.html) 实例将会获取之前放进去的两个整数，计算它们的和，然后再放进去。如，在解析上下文栈顶的就是 10 (= 7 + 3)。下个 literal 元素将会让 LiteralAction 将会将整数 3 放入栈顶。为了响应 \ 元素，[`MultiplyAction`](https://logback.qos.ch/xref/chapters/onJoran/calculator/MultiplyAction.html) 将会获取之前放入的两个整数 10 与 3，然后计算它们的乘积。它会将结果 30 放入栈顶。最后，为了响应结束事件对应的 \\\</computation> 标签，ComputationAction1 将会打印堆栈顶部的结果，因此，运行：

```java
java chapters.onJoran.calculator.Calculator1 src/main/java/chapters/onJoran/calculator/calculator2.xml
```

将会输出：

```java
The computation named [toto] resulted in the value 30
```

### 默认动作

目前定义的队则都是被显示的动作调用。因为当前元素相关的模式/动作能够在规则存储中被找到。但是，在高度可以扩展的系统中，组件的数量跟类型都会非常多，因此对所有的模式都关联一个具体的动作将会变得十分的蛋疼。

同时，甚至在高扩展的系统中，可以看到重复的规则关联了不同的部分。如果我们可以识别这些规则，那么我们就可以在编译时处理由子组件组成的未知组件。例如，Apache Ant 有能力在编译时处理包含未知标签的任务，仅仅通过检查组件中的方法名是不是以 *add* 开头，像 `addFile` 或者 `addClassPath` 之类的。当 Ant 在任务内遇到一个内置的标签，它仅仅实例化一个匹配了任务类 add 方法的签名的对象，并且将结果对象附加到父级上。

Joran 通过默认动作的形式来提供类似的功能。Joran 保留了一系列的默认动作，如果当前模式没有具体的模式可以匹配时，它们将会被应用。但是，应用默认的动作可能并不总是合适的。在执行默认的动作之前，Joran 会询问指定的动作当前的情况是否合适。只有动作返回肯定的回答，Joran 的配置器才会调用默认的动作。注意，这个额外的步骤可能支持多个默认的动作，如果在给定的情况下，没有合适的默认动作，也可能一个都不支持。

你可以创建并注册一个自定义的默认动作。见下一个示例。该示例位于 *logback-examples/src/main/java/chapters/onJoran/implicit* 文件夹下。

[`PrintMe`](https://logback.qos.ch/xref/chapters/onJoran/implicit/PrintMe.html) 应用将一个 [`NOPAction`](https://logback.qos.ch/xref/chapters/onJoran/implicit/NOPAction.html) 实例与 "\*/foo" 模式相关联，也就是与名字叫做 "foo" 的任何元素。正如它的名字所示， `NOPAction` 的 `begin()` 与 `end()` 方法都为空。`PrintMe` 应用仍然会在它的默认动作列表注册一个 [PrintMeImplicitAction](https://logback.qos.ch/xref/chapters/onJoran/implicit/PrintMeImplicitAction.html) 的实例。`PrintMeImplicitAction` 对任何 *printme* 属性为 true 的元素有效。参见 `PrintMeImplicitAction` 的 `isApplicable()` 方法。`PrintMeImplicitAction` 的 `begin()` 方法会在控制台打印当前元素的名字。

*implicit1.xml* XML 文档说明了默认动作是如何起作用的。

> Example: *implicit1.xml*

```markup
<foo>
  <xyz printme="true">
    <abc printme="true"/>
  </xyz>

  <xyz/>

  <foo printme="true"/>

</foo>
```

运行：

```java
java chapters.onJoran.implicit.PrintMe src/main/java/chapters/onJoran/implicit/implicit1.xml
```

输出：

```java
Element [xyz] asked to be printed.
Element [abc] asked to be printed.
20:33:43,750 |-ERROR in c.q.l.c.joran.spi.Interpreter@10:9 - no applicable action for [xyz], current pattern is [[foo][xyz]]
```

给定一个 `NOPAction` 实例与 "*\\/foo*" 实例相关联，`NOPAction` 的 `begin()` 与 `end()` 方法在 \ 元素上被调用。`PrintMeImplicitAction` 不会在任何 \ 元素上触发。对于其它的元素，因为没有明确的动作可以匹配，所以 `PrintMeImplicitAction` 的 `isApplicable()` 方法被调用。它只有在 *printme* 属性设置为 true 的时候才会返回 true。也就是第一个 \ 元素 (不是第二个) 与 \ 元素。第十行的第二个 \ 元素，没有可用的动作，所以生成了一个内部的错误信息。这个信息通过 `PrintMe` 的最后一行代码 `StatusPrinter.print` 来进行输出。这也解释了上面的输出。

### 在实践中使用默认动作

logback-classic 与 logback-access 各自的 Joran 配置器只包含两个默认的动作，叫做 [`NestedBasicPropertyIA`](https://logback.qos.ch/xref/ch/qos/logback/core/joran/action/NestedBasicPropertyIA.html) 与 [`NestedComplexPropertyIA`](https://logback.qos.ch/xref/ch/qos/logback/core/joran/action/NestedComplexPropertyIA.html)。

`NestedBasicPropertyIA` 适用于任何属性的类型为原始类型 (或者 equivalent object type in the `java.lang` 包中的对象类型 )，枚举类，或者其它遵循 "valuesOf" 约定的类型。这些属性被称之为*基本* 或者*简单* 属性。如果一个类它包含一个名为 `valueOf()` 的静态方法，接受一个 `java.lang.String` 作为参数并且返回相关类型的实例，那么就说这个类遵循 "valueOf" 约定。目前，[`Level`](https://logback.qos.ch/xref/ch/qos/logback/classic/Level.html)，[`Duration`](https://logback.qos.ch/xref/ch/qos/logback/core/util/Duration.html)，以及 [`FileSize`](https://logback.qos.ch/xref/ch/qos/logback/core/util/FileSize.html) 类遵循这个约定。

`NestedComplexPropertyIA` 适用于 `NestedBasicPropertyIA` 不适用的情况，并且如果对象栈顶部的对象具有当前属性名的 set 与 add 方法，那么该属性名相当于当前元素的名称。这些属性可以反过来包含其它的组件。因此，这些属性可以说是有点*复杂*。由于复杂属性的存在，[`NestedComplexPropertyIA`](https://logback.qos.ch/xref/ch/qos/logback/core/joran/action/NestedComplexPropertyIA.html) 将会为内部组件实例化一个合适的类，并且通过使用父组件以及内部元素名的 set/add 方法将其附加到父组件上 (在对象栈的顶部)。相应的类通过当前 (内置) 元素的 *class* 属性来指定。但是，如果没有指定 *class* 属性，那么将会根据是否满足以下其中之一的条件来使用默认的类名。

1. 父对象属性指定的类有内部的规则相关联
2. set 方法包含一个指定类的 @DefaultClass 属性
3. set 方法的参数类型是一个含有共有构造方法的实体类

#### 默认类映射

在 logback-classic，有一些内部的规则将父 类/属性 名映射为默认的类。这些规则如下表所示：

| 父类                                             | 属性名       | 默认类                                                 |
| ---------------------------------------------- | --------- | --------------------------------------------------- |
| ch.qos.logback.core.AppenderBase               | encoder   | ch.qos.logback.classic.encoder.PatternLayoutEncoder |
| ch.qos.logback.core.UnsynchronizedAppenderBase | encoder   | ch.qos.logback.classic.encoder.PatternLayoutEncoder |
| ch.qos.logback.core.AppenderBase               | layout    | ch.qos.logback.classic.PatternLayout                |
| ch.qos.logback.core.UnsynchronizedAppenderBase | layout    | ch.qos.logback.classic.PatternLayout                |
| ch.qos.logback.core.filter.EvaluatorFilter     | evaluator | ch.qos.logback.classic.boolex.JaninoEventEvaluator  |

在以后的版本中，这个列表可能会发生改变。最新的规则，请查看 logback-classic 中 [JoranConfigurator](https://logback.qos.ch/xref/ch/qos/logback/classic/joran/JoranConfigurator.html) 中的 `addDefaultNestedComponentRegistryRules` 方法。

#### 属性集

除了单个简单属性以及单个复杂属性外，logback 的默认动作支持属性集，它们可以是简单的或者复杂的。指定的属性通过 "add" 方法，而不是 set 方法。

### 动态添加新规则

Joran 包含一个允许 Joran 在解析 XML 文档的过程中，动态解析新规则的动作。示例代码，查看 *logback-examples/src/main/java/chapters/onJoran/newRule/* 文件夹。在这个包中，[`NewRuleCalculator`](https://logback.qos.ch/xref/chapters/onJoran/newRule/NewRuleCalculator.html) 仅仅设置两个规则，一个用来处理最顶层的元素，一个用来学习新规则。下面是 `NewRuleCalculator` 中相关的代码：

```java
ruleMap.put(new Pattern("*/computation"), new ComputationAction1());
ruleStore.addRule(new Pattern("/computation/newRule"), new NewRuleAction());
```

[`NewRuleAction`](https://logback.qos.ch/xref/ch/qos/logback/core/joran/action/NewRuleAction.html) 是 logback-core 的一部分，跟其它的动作非常的类似。它有 `begin()` 与 `end()` 方法，在每次解析器找到一个 *newRule* 元素时被调用。当被调用时，`begin()` 方法会去寻找 *pattern* 与 *actionClass* 属性。然后实例化相应的动作类，并将模式/动作作为一条新规则添加到 Joran 的规则存储中。

下面是如何在 xml 文件添加一条新规则：

```markup
<newRule pattern="*/computation/literal"
          actionClass="chapters.onJoran.calculator.LiteralAction"/>
```

使用 newRule 声明，我们可以看到 `NewRuleCalculator` 表现出跟之前看到的 `Calculator1` 同样的结果。包括计算在内，我们可以按照如下的方式进行表示：

> Example: *newRule.xml*

```markup
<computation name="toto">
  <newRule pattern="*/computation/literal" 
            actionClass="chapters.onJoran.calculator.LiteralAction"/>
  <newRule pattern="*/computation/add" 
            actionClass="chapters.onJoran.calculator.AddAction"/>
  <newRule pattern="*/computation/multiply" 
            actionClass="chapters.onJoran.calculator.MultiplyAction"/>

  <computation>
    <literal value="7"/>
    <literal value="3"/>
    <add/>
  </computation>   

  <literal value="3"/>
  <multiply/>
</computation>
```

```java
java chapters.onJoran.newRule.NewRuleCalculator src/main/java/chapters/onJoran/newRule/newRule.xml
```

> 作者原文中的命令写了两个 java

输出：

```java
The computation named [toto] resulted in the value 30
```

跟[之前](https://github.com/Volong/logback-chinese-manual/blob/master/11%E7%AC%AC%E5%8D%81%E4%B8%80%E7%AB%A0%EF%BC%9AJoran.md#%E5%8A%A8%E4%BD%9C%E7%9B%B8%E4%BA%92%E5%90%88%E4%BD%9C)的结果一致。

> 运行原文中的示例并不会输出坐着所说的结果，需要去掉 \ 中的 \ 标签才可以


# 第十二章：Groovy 配置

领域特定语言或者 DSL 更加普遍。logback 基于 XML 的配置可以看做 DSL 的实例。由于 XML 的本质，基于 XML 的配置文件变得非常的啰嗦以及臃肿。另外，logback 中的 Joran 有一个相对庞大的代码，用来专门处理基于 XML 的配置文件。Joran 支持一些非常好的特性，例如变量替换，条件处理，以及动态扩展。但是，不但 Joran 非常复杂，而且给用户的体验非常的不好，或者至少不直观。

本章叙述基于 Groovy 的 DSL 致力于一致性，直观性，以及非常强大。任何你可以使用 XML 配置的文件，你都可以用更加简短的符号使用 Groovy 来实现。为了帮助你迁移到 Groovy 风格的配置，我们开发了一个[工具](https://logback.qos.ch/translator/asGroovy.html)。

## 常规建议

一般来说，*logback.groovy* 文件是 Groovy 程序。因为 Groovy 是 Java 的超集，所以无论你在 Java 执行什么配置操作，你都可以在 *logback.groovy* 文件中做同样的事情。但是，在 Java 中，使用变成的方式配置 logback 有点笨重，所以我们增加了一些 logback 特有的扩展来减轻你的负担。我们尝试限制 logback 特有的拓展符号尽量的少。如果你已经熟悉了 Groovy，那么你应该更加容易去读，去理解甚至去写你自己的 *logback.groovy* 文件。那么不熟悉 Groovy 的人依然会发现 *logback.groovy* 中的语法比 *logback.xml* 中的语法更加容易使用。

*logback.groovy* 文件是 Groovy 程序，具有最小的 logback 特定的拓展。所有常用的 groovy 结构，例如类的导入，变量定义，字符串 (GString) 中包含 ${..} 评估表达式，以及 if-else 语句在 *logback.grooby* 文件中都是可用的。

## 自动导入

**`1.0.10 版本以后`** 为了减少不必要的引用，一些共同的类以及包会被自动导入。因此，只要你只是配置了内置的 appender，layout 等等，你不需要在你的脚本中添加相对应的导入语句。当然，对于默认导入不会涉及到类，你需要自己导入。

下面是默认导入的列表：

* import ch.qos.logback.core.\*;
* import ch.qos.logback.core.encoder.\*;
* import ch.qos.logback.core.read.\*;
* import ch.qos.logback.core.rolling.\*;
* import ch.qos.logback.core.status.\*;
* import ch.qos.logback.classic.net.\*;
* import ch.qos.logback.classic.encoder.PatternLayoutEncoder;

另外，`ch.qos.logback.classic.Level` 中的所有常量 (大写) 都会被静态导入，以及小写的别名。也就是说在你的脚本中可以引用 *INFO* 以及 *info*，而不需要使用静态导入语句。

## 不再支持 SiftingAppender

**`1.0.12 版本以后`** 在 groovy 配置文件中不再支持 `SiftingAppender`。但是，如果有需要，可以重新引进。

## *logback.groovy* 特定的拓展

**本质上，*****logback.groovy*****&#x20;语法包含以下所说的六个方法；按照它们习惯上相反的顺序出现。**&#x4E25;格来说，这些方法的调用顺序并**不**重要，但是有一个例外：appender 附加到 logger 之前**必须**被定义。

* **root(Level level, List\ appenderNames = \[])**

`root` 方法可以用来设置 root logger 的日志级别。第二个可选参数的类型为 `List<String>`，可以用来添加之前定义的 appender 的名字。如果你不想指定 appenderNames，那么就是一个空 (empty) 的列表。在 Groovy 中，用 `[]` 表示一个空的列表。

设置 root logger 的级别为 WARN，你可以这样写：

```groovy
root(WARN)
```

设置 root logger 的级别为 INFO，并且将名为 "CONSOLE" 与 "FILE" 的 appender 附加到 root 上，你可以这样写：

```groovy
root(INFO, ["CONSOLE", "FILE"])
```

在前面的例子中，假设名为 "CONSOLE" 与 "FILE" 的 appender 已经被定义好了。很快将会讨论有关 appender 的定义。

* **logger(String name, Level level, List\ appenderNames = \[], Boolean additivity = null)**

`logger()` 方法接收四个参数，最后两个是可选的。第一个参数表示配置 logger 的名字。第二参数表示指定 logger 的级别。设置 logger 的级别为 `null` 将强制它从它最近的祖先那里[继承](https://github.com/Volong/logback-chinese-manual/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#%E6%9C%89%E6%95%88%E7%AD%89%E7%BA%A7%E5%8F%88%E7%A7%B0%E4%B8%BA%E7%AD%89%E7%BA%A7%E7%BB%A7%E6%89%BF)级别。第三个参数的类型为 `List<String>`，是可选的，默认为空列表。列表中 appender 会被附加到指定的 logger 上去。第四个参数的类型为 `Boolean`，也是可选的，用来控制[叠加性](https://github.com/Volong/logback-chinese-manual/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%9E%B6%E6%9E%84.md#appender-%E4%B8%8E-layout)。如果忽略，默认值为 `null`。

例如，下面这个脚本设置 "com.foo" 这个 logger 的级别为 INFO：

```groovy
logger("com.foo", INFO)
```

下个脚本设置 "com.foo" 这个 logger 的级别为 DEBUG，并且将名为 "CONSOLE" 的 appender 附加到其上：

```groovy
logger("com.foo", DEBUG, ["CONSOLE"])
```

下个脚本跟上一个类似，只是这个还设置了 "com.foo" 这个 logger 的叠加性为 false：

```groovy
logger("com.foo", DEBUG, ["CONSOLE"]，false)
```

* **appender(String name, Class clazz, Closure closure = null)**

appender 方法的第一个参数接收 appender 的名字进行配置。第二个参数是强制的，表示 appender 实例化的类。第三个参数包含更多的配置信息。如果忽略，默认为 null。

大部分 appender 都需要设置属性，并且注入子组件才能正常工作。属性通过 '=' 进行设置。子组件的注入通过调用以属性命名的方法，并且将实例化的类作为参数传递给该方法。这个约定可以被递归的应用到配置的属性以及任何 appender 子组件的子组件中。这个方法是 *logback.groovy* 的核心，可能是唯一需要去学习的约定。

例如，接下来的脚本实例化一个 `FileAppender` 命名为 "FILE"，设置它的 `file` 属性为 "testFile.log"，以及它的 `append` 属性设置为 false。类型为 `PatternLayoutEncoder` 的 encoder 被注入到这个 appender 中。encoder 的模式属性设置为 "%level %logger - %msg%n"。然后将这个 appender 附加到 root logger 上。

```groovy
appender("FILE", FileAppender) {
    file = "testFile.log"
    append = false
    encoder(PatternLayoutEncoder) {
        pattern = "%level %logger - %msg%n"
    }
}

root(DEBUG, ["FILE"])
```

* **timestamp(String datePattern, long timeReference = -1)**

`timestamp()` 方法根据 `datePattern` 将 `timeReference` 参数格式化，返回一个对应的字符串。`datePattern` 参数应该尊村 [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) 中定义的约定。如果 `timeReference` 没有指定，那么默认为 -1。在这种情况下，当解析配置文件时，当前时间作为 `timeReference` 参数的值。

在下个例子中，`bySecond` 变量表示被 "yyyyMMdd'T'HHmmss" 格式化之后的当前时间。之后，"bySecond" 变量被用于 `file` 属性的定义中。

```groovy
def bySecond = timestamp("yyyyMMdd'T'HHmmss")

appender("FILE", FileAppender) {
    file = "log-${bySecond}.txt"
    encoder(PatternLayoutEncoder) {
        pattern = "%logger{35} - %msg%n"
    }
}

root(DEBUG, ["FILE"])
```

* **conversionRule(String conversionWord, Class converterClass)**

在创建了你自己的[转换说明符](https://github.com/Volong/logback-chinese-manual/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ALayouts.md#%E8%87%AA%E5%AE%9A%E4%B9%89%E8%BD%AC%E6%8D%A2%E8%AF%B4%E6%98%8E%E7%AC%A6)之后，你需要通知 logback 它的存在。下面这个简单的 logback.groovy 文件告诉 logback 在遇到 `%sample` 转换字符时使用 MySampleConverter。

```groovy
import chapters.layouts.MySampleConverter

conversionRule("sample", MySampleConverter)
appender("STDOUT", ConsoleAppender) {
    encoder(PatternLayoutEncoder) {
        pattern = "%-4relative [%thread] %sample - %msg%n"
    }
}

root(DEBUG, ["STDOUT"])
```

* **scan(String scanPeriod = null)**

调用 scan() 方法告诉 logback 周期性的扫描 logback.groovy 文件的变化。当检测到变化时，*logback.groovy* 文件会被重新加载。

```groovy
scan()
```

默认情况下，一分钟扫描一次配置文件。你可以通过 "scanPeriod" 来指定一个不同的扫描周期。它的值可以被指定以 milliseconds, seconds, minutes 或者 hours 位单位。例如：

```groovy
scan("30 seconds")
```

如果没有指定时间单位，那么默认的时间单位为 milliseconds，但是通常来说是不合适的 (既然不合适，为什么默认还是毫秒，费解🤔)。如果你更改了默认的扫描周期，记得要指定时间单位。更多关于扫描工作的细节，请查看[自动加载](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E5%BD%93%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E6%9B%B4%E6%94%B9%E6%97%B6%E8%87%AA%E5%8A%A8%E5%8A%A0%E8%BD%BD)部分。

* **statusListener(Class listenerClass)**

你可以通过调用 `statusListener` 方法，并给该方法传递一个监听器类，来添加一个状态监听器。例：

```groovy
import chapters.layouts.MySampleConverter

// 强烈建议在最后一个导入语句之后，其它所有语句之前添加状态监听器
statusListener(OnConsoleStatusListener)
```

关于[状态监听器](https://github.com/Volong/logback-chinese-manual/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alogback%20%E7%9A%84%E9%85%8D%E7%BD%AE.md#%E7%9B%91%E5%90%AC%E7%8A%B6%E6%80%81%E4%BF%A1%E6%81%AF)请查看之前的章节。

* **jmxConfigurator(String name)**

你可以通过该方法注册一个 [`JMXConfigurator`](https://logback.qos.ch/manual/jmxConfig.html) MBean。无参调用将会使用 logback 默认的对象名 (`ch.qos.logback.classic:Name=default,Type=ch.qos.logback.classic.jmx.JMXConfigurator`) 去注册 MBean。

```groovy
jmxConfigurator()
```

要改变 `Name` 键的值，而不是 "default"，仅仅只需要给 `jmxConfigurator` 方法传递一个不同的名字参数就可以了。

```groovy
jmxConfigurator('MyName')
```

如果你想要完整的定义对象名，可以使用同样的语法，但是需要传递一个有效的对象名字符串作为参数：

```groovy
jmxConfigurator('myApp:type=LoggerManager')
```

该方法首先会去尝试将该参数作为对象名，如果它不表示一个有效的对象名，则会把它当作 "Name" 键的值。

## 内置 DSL

*logback.groovy* 是一个内置 DSL 的意思是，它的内容可以作为 Groovy 脚本执行。因此，所有常用的 Groovy 指令，例如类的导入，GString，变量的定义，包含字符串 (GString) 的 ${..} 评估表达式，if-else 语句这些在 logback.groovy 文件中都是可用的。在接下来的讨论中，我们将会展示 Groovy 指令在 *logback.groovy* 文件中的典型用法。

### 变量定义与 GString

你可以在 *logback.groovy* 文件中的任何地方定义变量，然后在 GString 中使用该变量。例如：

```groovy
def USER_HOME = System.getProperty("user.home")

appender("FILE", FileAppender) {
    // 使用 USER_HOME 变量
    file = "${USER_HOME}/myApp.log"
    encoder(PatternLayoutEncoder) {
        pattern = "%msg%n"
    }
}
root(DEBUG, ["FILE"])
```

### 在控制台打印

通过调用 Groovy 的 `println` 方法在控制台进行打印。例如：

```groovy
def USER_HOME = System.getProperty("user.home");
println "USER_HOME=${USER_HOME}"

appender("FILE", FileAppender) {
    println "Setting [file] property to [${USER_HOME}/myApp.log]"
    file = "${USER_HOME}/myApp.log"
    encoder(PatternLayoutEncoder) {
        pattern = "%msg%n"
    }
}
root(DEBUG, ["FILE"])
```

### 自动输出字段

#### 'hostname' 变量

'hostname' 变量包含当前 host 的名字。但是由于作用域规则，所以作者不能完全解释清楚 (😓)。'hostname' 变量只在最上层的作用域中有效，但是在内部的作用域中无效。下面的例子应该可以解释这一点：

```groovy
// 如果当前 host 的名字为 x，那么将会输出 "hostname is x"
println "hostname is ${hostname}"

appender("STDOUT", ConsoleAppender) {
    // 将会输出 "hostname is null"
    println "hostname is ${hostname}"
}
```

如果你想要在所有的作用域中使用 hostname 变量。那么你需要定义一个变量，并将 'hostname' 的值赋给它。如下：

```groovy
// 将 hostname 的值赋给 HOSTNAME
def HOSTNAME = hostname

// 如果当前 host 的名字为 x，那么将会输出 "hostname is x"
println "hostname is ${HOSTNAME}"

appender("STDOUT", ConsoleAppender) {
    // 如果当前 host 的名字为 x，那么将会输出 "hostname is x"
    println "hostname is ${HOSTNAME}"
}
```

### 任何对于当前上下文的引用都是上下文感知的

*logback.groovy* 脚本是在 [ContextAware](https://logback.qos.ch/xref/ch/qos/logback/core/spi/ContextAware.html) 对象的范围内执行完成的。因此，在当前上下文的范围内，你可以使用 '`context`'，并且可以通过 `addInfo()`、`addWarn()`、与 `addError()` 方法将状态信息发送给上下文的 `StatusManager`。

```groovy
// 添加一个控制台转态监听器总是没错的
statusListener(OnConsoleStatusListener)

// 设置上下文的名字为 wombat
context.name = 'wombat'

// 添加一个关于上下文名字的状态信息
addInfo("Context name has been set to ${context_name}")

def USER_HOME = System.getProperty("user.home")

// 添加关于 USRE_HOME 的状态信息
addInfo("USER_HOME=${USER_HOME}")

appender("FILE", FileAppender) {
    addInfo("Setting [file] property to [${USER_NAME}/myApp.log]")
    file = "${USER_HOME}/myApp.log"
    encoder(PatternLayoutEncoder) {
        pattern = "%msg%n"
    }
}
root(DEBUG, ["FILE"])
```

### 条件配置

由于 Groovy 是一种完全成熟的编程语言，条件语句允许单一的 *logback.groovy* 文件用来适用不同的环境，例如开发，测试以及生产。

在下个脚本中，console appender 根据 host 来激活，而不是我们的生产环境 pixie 或 orion。rolling file appender 的输出目录也是根据 host 来确定。

```groovy
statusListener(OnConsoleStatusListener)

def appenderList = ["ROLLING"]
def WEBAPP_DIR = "."
def consoleAppender = true;

// hostname 是否匹配 pixie 或 orion
if (hostname =~ /pixie|orion/) {
    WEBAPP_DIR = "/opt/myapp"
    consoleAppender = false
} else {
    appenderList.add("CONSOLE")
}

if (consoleAppender) {
    appender("CONSOLE", ConsoleAppender) {
        encoder(PatternLayoutEncoder) {
            pattern = "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"
        }
    }
}

appender("ROLLING", RollingFileAppender) {
    encoder(PatternLayoutEncoder) {
        Pattern = "%d %level %thread %mdc %logger - %m%n"
    }
    rollingPolicy(TimeBasedRollingPolicy) {
        FileNamePattern = "${WEBAPP_DIR}/log/translator-%d{yyyy-MM}.zip"
    }
}

root(INFO, appenderList)
```


# 第十三章：从 log4j 迁移

本章涉及到的内容为将 log4j 的组件，例如 appender 或者 layout 迁移到 logback-classic。

仅仅调用 log4j 客户端 API 的软件，也就是 `org.apache.log4j` 包中 `Logger` 或者 `Category` 类，可以通过 [SLF4J 迁移工具](https://www.slf4j.org/migrator.html)使用 SLF4J 来进行自动迁移。为了将 *log4j.property* 文件转换为同等的 logback 配置，你可以使用 [log4j.properties 转换器](https://logback.qos.ch/translator/)。

在某种程度上来说，log4j 与 logback-classic 密切相关。核心组件，logger，appender 以及 layout 在两个框架中都存在，并且目的一致。类似的，最重要的内部数据结构，叫做 `LoggingEvent`，在两个框架中非常相似，但是实现完全不同。最主要的是，在 logback-classic 中，`LoggingEvent` 实现了 `ILoggingEvent` 接口。迁移 log4j 组件到 logback-classic 最大的改变在于 `LoggingEvent` 类相关的实现不同。但是，请放心，这些变化是有限的。如果你尽了最大的努力仍然不能将 log4j 组件迁移到 logback-classic，你可以通过 [logback 开发邮件列表](https://logback.qos.ch/mailinglist.html)来进行提问。logback 的开发者应该可以提供指导。

## 迁移 log4j 的 layout

假设我们现在要迁移一个简单的，名叫 [TrivialLog4jLayout](https://logback.qos.ch/xref/chapters/migrationFromLog4j/TrivialLog4jLayout.html) 的 log4j layout，它将日志事件中的消息作为格式化消息返回。代码如下：

```java
package chapters.migrationFromLog4j;

import org.apache.log4j.Layout;
import org.apache.log4j.spi.LoggingEvent;

public class TrivialLog4jLayout extends Layout {

  public void activateOptions() {

  }

  public String format(LoggingEvent loggingEvent) {
    return loggingEvent.getRenderedMessage();
  }

  public boolean ignoresThrowable() {
    return true;
  }
}
```

等价的 logback-classic [TrivialLogbackLayout](https://logback.qos.ch/xref/chapters/migrationFromLog4j/TrivialLogbackLayout.html) 如下：

```java
package chapters.migrationFromLog4j;

import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.LayoutBase;

public class TrivialLogbackLayout extends LayoutBase<ILoggingEvent> {

  public String doLayout(ILoggingEvent loggingEvent) {
    return loggingEvent.getMessage();
  }
}
```

正如你所见，在 logback-classic layout 中，格式化的方法叫做 `doLayout`，而在 log4j 中叫 `format()`。因为在 logback-classic 中没有等价的方法，所以 `ignoresThrowable()` 方法则不需要。logback-classic layout 必须继承 `LayoutBase<ILoggingEvent>` 类。

`activateOptions()` 方法的优点值得进一步讨论。在 log4j 中，一个 layout 有它自己的 `activateOptions()` 方法，通过 log4j 的配置程序，也就是 `PropertyConfigurator` 与 `DOMConfigurator`，会在 layout 所有的选项都设置完之后调用。因此，layout 有机会去检查它的所有的选项是否一致，如果是，那么开始进行初始化。

在 logback-classic 中，layout 必须实现 [LifeCycle](https://logback.qos.ch/xref/ch/qos/logback/core/spi/LifeCycle.html) 接口，该接口包含了一个 `start()` 方法。这个 `start()` 方法相当 log4j 中的 `activateOptions()` 方法。

## 迁移 log4j 的 appender

迁移 appender 与迁移 layout 相当的类似。下面是有一个名为 [TrivialLog4jAppender](https://logback.qos.ch/xref/chapters/migrationFromLog4j/TrivialLog4jAppender.html) 的简单 appender，它会在控制台输出由它的 layout 返回的字符串。

```java
package chapters.migrationFromLog4j;

import org.apache.log4j.AppenderSkeleton;
import org.apache.log4j.spi.LoggingEvent;


public class TrivialLog4jAppender extends AppenderSkeleton {

  protected void append(LoggingEvent loggingevent) {
    String s = this.layout.format(loggingevent);
    System.out.println(s);
  }

  public void close() {
    // nothing to do
  }

  public boolean requiresLayout() {
    return true;
  }
}
```

在 logback-classic 中等价的写法为 [TrivialLogbackAppender](https://logback.qos.ch/xref/chapters/migrationFromLog4j/TrivialLogbackAppender.html)，如下：

```java
package chapters.migrationFromLog4j;

import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.AppenderBase;

public class TrivialLogbackAppender extends AppenderBase<ILoggingEvent> {

  @Override
  public void start() {
    if (this.layout == null) {
      addError("No layout set for the appender named [" + name + "].");
      return;
    }
    super.start();
  }

  @Override
  protected void append(ILoggingEvent loggingevent) {
    // AppenderBase.doAppend 只会在这个 appender 成功启动之后调用这个方法
    String s = this.layout.doLayout(loggingevent);
    System.out.println(s);
  }
}
```

比较这两个类，你会发现 `append()` 方法的内容没有改变。`requiresLayout` 方法在 logback 中没有用到，所以它可以被移除。在 logback 中，`stop()` 方法与 log4j 中的 `close()` 方法等价。然而，logback-classic 中的 `AppenderBase` 包含一个没有实现的 `stop` 方法，但是在这个简单的 appender 已经足够了。


# 第十四章：Receivers

## 什么是 Receiver

*receiver* 是 logback 的一个组件，用于接收远程 appender 的日志事件，根据本地策略打印接收到的日志事件。结合使用基于套接字的 appender 与 receiver，可以构建复杂的拓扑图，通过网络分发应用程序的日志事件。

一个 receiver 继承 [`ch.qos.logback.classic.net.ReceiverBase`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/ReceiverBase.html) 类。由于 receiver 继承了这个类，所以它也是 logback 组件 [LifeCycle](https://logback.qos.ch/xref/ch/qos/logback/core/spi/LifeCycle.html) 的一部分，而且它也是一个 [ContextAware](https://logback.qos.ch/xref/ch/qos/logback/core/spi/ContextAware.html)。

过去为了支持日志事件通过网络传输，logback 提供了 `SocketAppender` 与 `SimpleSocketServer`。appender 充当一个客户端，初始化到服务器应用程序的网络连接，再通过网络传输日志事件。receiver 组件以及相应的 appender 提供了很大的灵活性。在 *logback.xml* 中配置一个 receiver 组件，跟配置其它的组件一样。这允许配置 receiver 组件利用 [Joran](https://logback.qos.ch/manual/onJoran.html) 所有的功能。而且，任何应用都可以通过简单的配置一个或多个 receiver 组件从远程 appender 接收日志事件。

连接开始可以发生在 appender 与 recevier 之间的任何一方。一个 receiver 可以充当服务器的角色，被动的监听远程 appender 客户端的连接。或者，receiver 充当客户端的角色，初始化与远程 appender 服务器的连接。不管 appender 与 receiver 的角色是什么，*日志事件总是从 appender 流向 receiver。*

允许 receiver 初始化到 appender 的连接的灵活性在特定的情况下特别的有用：

* 由于安全的原因，中心日志服务器位于网络防火墙的后面，不允许即将到来的连接。使用 receiver 组件充当客户端的角色，中心日志服务器 (防火墙内) 可以初始化对应用程序 (防火墙外) 的连接。
* 开发者工具与企业管理应用可以获取正在运行中的程序的日志事件流。通常，logback 通过要求接收方应用程序 (例如，IDE 中正在运行的开发者工具) 去充当服务器的角色，被动的监听来自远程 appender 的连接来支持这个 (例如在 logback Beagle 中)。这提高了管理的困难，特别是当工具运行在开发者的工作站中的时候，有可能是通过移动设备。但是，可以使用 logback receiver 组件充当客户端角色来实现这些工具。初始化一个到远程 appender 的连接，接收日志事件用于本地显示，过滤以及报警。

一个 logback 的配置可以包含任何数量的 receiver 组件，充当任意组合的服务器或者客户端的角色。唯一的限制是每个充当服务器角色的 receiver 必须监听在不同的端口，每个充当客户端角色的 receiver 将会准备的连接到一个远程的 appender 上。

## Receivers 充当服务器角色

一个 receiver 可以被配置为充当服务器的绝对，被动的监听远程 appender 即将到来的连接。这个功能类似于使用独立的 `SimpleSocketServer` 应用，特别是在使用 receiver 组件时，*任何* 应用仅仅只需要在 *logback.xml* 中配置 receiver 就可以使用 logback-classic 接收来自远程 appender 的日志事件。

![serverSocketReceiver.png](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbNliV60PlEtvMTj%2FserverSocketReceiver.png?generation=1568702627880959\&alt=media)

logback 包含两个 receiver 组件用于充当服务器角色。[`ServerSocketReceiver`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/server/ServerSocketReceiver.html) 以及它支持 SSL 的子类型 [`SSLServerSocketReceiver`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/server/SSLServerSocketReceiver.html)。这两个 receiver 组件都被设计成用来接收来自于 `SocketAppender` (或者 `SSLSocketAppender`) 客户端的连接。

`ServerSocketReceiver` 组件提供以下配置属性：

| 属性名         | 类型                 | 描述                                                                                                                  |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **address** | `String`           | receiver 监听的本地网络接口。如果没有指定这个属性，那么将监听所有的网络接口。                                                                         |
| **port**    | `int`              | receiver 监听的 TCP 端口。如果这个属性没有被指定，将会使用一个默认的值。(译者注：默认的端口为 4560)                                                        |
| **ssl**     | `SSLConfiguration` | 仅仅支持 `SSLServerSocketReceiver`。这个属性提供了 receiver 使用的 SSL 配置。详情请见 [第十五章](https://logback.qos.ch/manual/usingSSL.html) |

### 使用 ServerSocketReceiver

下面的配置使用 `ServerSocketReceiver` 组件，它使用最小的本地 appender 以及 logger 配置。接收来自远程 appender 的日志事件，将会匹配到 root logger，并输出到本地的 console appender。

> Example: receiver1.xml

```markup
<configuration debug="true">

  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>

  <receiver class="ch.qos.logback.classic.net.server.ServerSocketReceiver">
    <port>${port}</port>
  </receiver>

</configuration>
```

receiver 组件的 *class* 属性表明了我们想要使用的 receiver 子类型。在这个例子中，我们使用 `ServerSocketReceiver`。

我们示例中的服务器应用在功能与设计上与 `SimpleSocketServer` 非常的类似。它仅仅接收 logback 配置文件的路径作为命令行的参数，并运行给定的配置。虽然我们的示例程序很简单，但是请记住，你可以在*任何*应用中配置 logback 的 `ServerSocketReceiver` (或者 `SSLServerSocketReceiver`) 组件。

我们可以在 *logback-examples* 文件夹中通过以下方式运行示例中服务器应用：

```
java -Dport=6000 chapters.receivers.socket.ReceiverExample \ 
      src/main/java/chapters/receivers/socket/receiver1.xml
```

我们可以使用配置了 `SocketAppender` 的客户端应用来连接运行中的 receiver。我们示例当中的客户端应用仅仅加载了 logback 配置，就可以连接我们示例中 receiver 的 socket appender。然后，它会等待用户的数据，以消息的形式转发给 receiver。我们可以通过如下的方式来运行客户端应用示例：

```
java -Dhost=localhost -Dport=6000 \
      chapters.receivers.socket.AppenderExample \
      src/main/java/chapters/receivers/socket/appender1.xml
```

### 使用 SSLServerSocketReceiver

下面的配置重复使用了最小的 appender 以及 logger 配置，但是使用了支持 SSL 的 receiver 组件，用于充当服务器角色。

> Example: receiver2.xml

```markup
<configuration debug="true">

  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>

  <receiver class="ch.qos.logback.classic.net.server.SSLServerSocketReceiver">
    <port>${port}</port>
    <ssl>
      <keyStore>
        <location>${keystore}</location>
        <password>${password}</password>
      </keyStore>
    </ssl>
  </receiver>

</configuration>
```

这个配置与之前使用 `ServerSocketReceiver` 的示例本质的区别是通过 *class* 属性指定了 `SSLServerSocketReceiver` 以及内嵌的 `ssl` 属性，使用变量替换来指定 key store 中包含 receiver 的私钥以及证书的位置以及密码。关于 logback 组件配置 SSL 属性的详细信息请查看[第十五章](https://logback.qos.ch/manual/usingSSL.html)。

我们可以使用相同的示例服务器配置来运行这个配置，仅仅添加几个额外的配置属性：

```
java -Dport=6001 \
      -Dkeystore=file:src/main/java/chapters/appenders/socket/ssl/keystore.jks \
      -Dpassword=changeit \
      chapters.receivers.socket.ReceiverExample \
      src/main/java/chapters/receivers/socket/receiver2.xml
```

*keystore* 属性被用来在命令行指定文件 URL 来标识 key store 的位置。你也可以使用[第十五章](https://logback.qos.ch/manual/usingSSL.html)所说的类路径 URL。

我们可以使用配置了 `SSLSocketAppender` 的客户端应用来连接运行中的 receiver。我们使用在之前示例中使用过的简单示例客户端应用，通过一个开启了 SSL appender 的配置文件，以如下方式运行：

```
java -Dhost=localhost -Dport=6001 \
      -Dtruststore=file:src/main/java/chapters/appenders/socket/ssl/truststore.jks \
      -Dpassword=changeit \
      chapters.receivers.socket.AppenderExample \
      src/main/java/chapters/receivers/socket/appender2.xml
```

注意，在我们的示例中，使用了自签名的 X.509 证书，这仅仅适用于测试。**在生产环境中的设置中，你应用获取一个合适的 X.509 证书，用于标识你的开启了 SSL 支持的 logback 组件。**&#x67E5;看[第十五章](https://logback.qos.ch/manual/usingSSL.html)获取更多的信息。

## Receivers 充当客户端角色

配置 receiver 充当客户端角色，初始化一个到远程 appender 的连接。远程 appender 必须是服务器类型，例如 `ServerSocketAppender`。

![socketReceiver](https://2058138220-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LoxxS4AhO6NhYkiZ1VB%2F-LoxxabEHVaYXifMZ1VN%2F-LoxxbNoJLDEoAPS3Mrw%2FsocketReceiver.png?generation=1568702627826169\&alt=media)

logback 包含两个 receiver 组件用于充当客户端角色：[`SocketReceiver`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/SocketReceiver.html) 以及它的支持 SSL 子类型的 [`SSLSocketReceiver`](https://logback.qos.ch/xref/ch/qos/logback/classic/net/SSLSocketReceiver.html)。这两个组件都被设计成初始化一个连接到远程 appender，也就是 `ServerSocketAppender` (或者 `SSLServerSocketAppender`)。

`SocketReceiver` 子类型支持如下的配置属性：

| 属性名                   | 类型                 | 描述                                                                                                                 |
| --------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **remoteHost**        | `String`           | 远程服务器 socket appender 的 hostname 或者地址                                                                              |
| **port**              | `int`              | 远程服务器 socket appender 的端口号                                                                                         |
| **reconnectionDelay** | `int`              | 在某次连接失败之后，在尝试重连时的等待时间。默认值为 3000 (30 秒)。                                                                            |
| **ssl**               | `SSLConfiguration` | 仅仅支持 `SSLSocketReceiver`，这个属性提供了用于这个  receiver 的 SSL 配置。如[第十五章](https://logback.qos.ch/manual/usingSSL.html)描述的那样。 |

### 使用 SocketReceiver

用于 `SocketReceiver` 的配置跟之前使用 `ServerSocketReceiver` 的示例非常的相似。不同的地方在于客户端与服务端的角色反转了。`SocketReceiver` 类型的 receiver 为客户端，远程 appender 充当服务器的角色。

> Example: receiver3.xml

```markup
<configuration debug="true">

  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">    
    <encoder>
      <pattern>%date %-5level [%thread] %logger - %message%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>  

  <receiver class="ch.qos.logback.classic.net.SocketReceiver">
    <remoteHost>${host}</remoteHost>
    <port>${port}</port>
    <reconnectionDelay>10000</reconnectionDelay>
  </receiver>

</configuration>
```

这个配置将会使 logback 连接通过 *host* 与 *port* 变量替换指定的主机与端口上的 `ServerSocketAppender`。将会通过 console appender 本地输出 (根据这里的配置文件) 从远程 appender 接收到的日志事件。

你可以在 *logback-examples/* 文件夹下，通过以下命令运行示例中的配置文件：

这个示例仅仅加载配置文件，然后仅仅等待来自远程 appender 的日志事件。如果你在远程 appender 没有运行的情况下运行这个示例，那么你将会周期性的看到*连接被拒绝*的日志消息输出。receiver 将会周期性的尝试重新连接远程 appender，直到连接成功或者 logger 上下文关闭。尝试的延迟间隔是可以通过 `reconnectionDelay` 属性来配置的，如示例配置中展示的一样。

```
java -Dhost=localhost -Dport=6000 \
      chapters.receivers.socket.ReceiverExample \
      src/main/java/chapters/receivers/socket/receiver3.xml
```

我们示例中的 receiver 连接之前使用过的同一个远程 apennder。这个示例加载一个包含 `ServerSocketAppender` 的配置，然后等待用户的输入，输入的消息将会被传递给已经连接上的 receiver。我们可以通过如下方式运行示例 appender 应用：

```
java -Dport=6000 \
      chapters.receivers.socket.AppenderExample \
      src/main/java/chapters/receivers/socket/appender3.xml
```

如果在 receiver 没有连接上的情况下输入消息，那么消息将会被丢弃。

### 使用 SocketSSLReceiver

`SSLSocketReceiver` 需要的配置跟使用 `SocketReceiver` 非常的类似。本质的区别在于通过 class 指定的 receiver，以及通过内嵌的 `ssl` 属性去指定 SSL 配置属性。下面是一个基础的示例：

> Example: receiver4.xml

```markup
<configuration debug="true">

  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">    
    <encoder>
      <pattern>%date %-5level [%thread] %logger - %message%n</pattern>
    </encoder>         
  </appender>

  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>  

  <receiver class="ch.qos.logback.classic.net.SSLSocketReceiver">
    <remoteHost>${host}</remoteHost>
    <port>${port}</port>
    <reconnectionDelay>10000</reconnectionDelay>
    <ssl>
      <trustStore>
        <location>${truststore}</location>
        <password>${password}</password>
      </trustStore>
    </ssl>
  </receiver>

</configuration>
```

除了在上一个例子中展示的配置属性之外，*class* 属性现在指定了 `SSLSocketReceiver`。配置文件中包含了指定 trust strore 的位置与密码的 SSL 配置。用于验证远程 appender 是可以受信任的。查看[第十五章](https://logback.qos.ch/manual/usingSSL.html)获取更多关于配置 SSL 属性的信息。

通过如下命令来运行示例配置：

```
java -Dhost=localhost -Dport=6001 \
      -Dtruststore=file:src/main/java/chapters/appenders/socket/ssl/truststore.jks \
      -Dpassword=changeit \
      chapters.receivers.socket.ReceiverExample \
      src/main/java/chapters/receivers/socket/receiver4.xml
```

一旦启动，receiver 尝试去连接指定的远程 appender。如果 appender 没有运行，那么你将会在日志输出中周期性的看到 "连接被拒" 的信息。在延迟了通过 `reconnectionDelay` 指定的周期时间后，receiver 将会周期性的重试到远程 appender 的连接。

我们示例中的 receiver 会连接之前使用过的远程 appender。这个示例加载包含了 `SSLServerSocketAppender` 的配置，然后等待用户的输入，输入的信息将会被传递给连接上的 receiver。通过如下方式运行示例 appender 应用：

```
java -Dport=6001 \
      -Dkeystore=file:src/main/java/chapters/appenders/socket/ssl/keystore.jks \
      -Dpassword=changeit \
      chapters.receivers.socket.AppenderExample \
      src/main/java/chapters/receivers/socket/appender4.xml
```

如果在 receiver 没有连接上的时候输入信息，那么信息将会被丢弃。

需要再次注意的是，我们的示例使用的是仅适用于测试的自签名 X.509 证书。**在生产环境中，你应该获取适当的 X.509 证书来标识你的支持 SSL 的 logback 组件。**&#x66F4;多细节请查看[第十五章](https://logback.qos.ch/manual/usingSSL.html)。


# 第十五章：使用 SSL

在从以 socket 为基础的 appender 到远程 receiver 传递日志事件时，logback 支持使用安全套接字层。当使用支持 SSL 的 appender 以及响应的 receiver 时，通过安全通道来传递日志事件。

## SSL 与组件的角色

logback 的组件，例如 appender 以及 receiver 在网络连接初始化时可能承当服务器的角色或者客户端的角色。当充当服务器角色时，logback 组件被动的监听来自远程客户端组件的连接。相反地，充当客户端角色的 logback 组件会初始化一个连接到远程服务器组件。例如，一个充当客户端角色的 appender 连接充当服务端角色的 receiver。或者一个充当客户端角色的 receiver 连接充当服务端角色的 appender。

组件的角色通常由组件的类型决定。例如，`SSLServerSocketAppender` 是一个充当服务端角色的 appender 组件，但是 `SSLSocketAppender` 是一个充当客户端角色的 appender 组件。因此开发者或者应用管理人员可以配置 logback 组件来支持想要的网络连接初始化方向。

网络连接初始化方法在 SSL 上下文中非常重要，因为在 SSL 中，服务端组件连接客户端必须具有 X.509 证书来标识自身。客户端组件，在连接服务端时，使用服务端的证书来验证服务端是否可信。开发人员或者应用管理者必须清楚的知道 logback 组件的角色，才能正确配置服务器的 keystore (包含服务器 X.509 证书) 以及客户端的 truststore (包含用于验证服务器信任时的自签名根证书)。

当为 **相互认证** 配置 SSL，服务器组件与客户端组件必须拥有有效的 X.509 证书，它们的信任由它们各自对等的声明。相互认证配置在服务器组件中，因此开发人员或者应用管理者必须知道哪一个组件充当的是服务器的角色。

在本章，我们使用术语 *服务器组件* 或者简单的 *服务器* 来表示 logback 中充当服务器角色的 appender 或者 receiver。使用 *客户端组件* 或者建的 *客户端* 来表示充当客户端角色的组件。

## SSL 以及 X.509 证书

为了是用支持 SSL 的 logback 组件，你需要一个 X.509 的证书 (一个私钥，相应的证书，以及 CA 认证链) 去标识你的组件充当了一个 SSL 服务器。如果你想要使用双向认证，那么充当 SSL 客户端的组件还需要一个证书。

虽然你可以使用由商业认证机构 (CA) 颁发的证书，但是你也可以使用内部 CA 颁发的证书，甚至是自签名的证书。下面是必须满足的条件：

1. 服务端组件必须配置一个 key store，包含服务器私钥，相应的证书，以及 CA 认证链 (如果没有使用自签名证书)
2. 客户端组件必须配置一个 trust store，包含可信任的根 CA 证书，或者服务器自签名根证书

## 为 SSL 配置 logback 组件

Java 安全套接字拓展 (JSSE) 以及 Java 加密体系 (JCA) 用来实现 logback 的 SSL，支持诸多的配置选项。可插拔的提供框架允许替换或增强内置的 SSL 以及平台的加密功能。为了满足你的对安全的需要，支持 SSL 的 logback 组件提供完全指定 SSL 引擎以及密码提供者配置方面的能力。

### 使用 JSSE 系统属性的基本 SSL 配置

幸运的是，支持 SSL 的 logback 组件几乎所有的 SSL 属性的配置都有合理的默认值。在多数的情况下，只需要配置一些 JSSE 的系统属性。

本节剩余的部分将讲述在大多数的环境中都需要被指定的 JSSE 属性。查看[定制 JSSE](https://docs.oracle.com/javase/1.5.0/docs/guide/security/jsse/JSSERefGuide.html#InstallationAndCustomization)来获取更多关于设置 JSSE 系统属性的信息来定制 JSSE。

如果你使用任何 logback 中支持 SSL 的 appender 或者 receiver 组件充当服务端角色 (例如，`SSLServerSocketReceiver`，`SSLServerSocketAppender`，`SimpleSSLSocketServer`)。你需要提供 key store 包含的密钥以及证书的 location，type 以及 password 来配置 JSEE 系统属性。

#### 服务端 key store 配置的系统属性

| 属性名                              | 描述                                  |
| -------------------------------- | ----------------------------------- |
| `javax.net.ssl.keyStore`         | 指定包含服务端组件的密钥以及证书的文件的文件系统的路径         |
| `javax.net.ssl.keyStoreType`     | 指定 key store 类型。如果这个属性没有指定，将默认为 JKS |
| `javax.net.ssl.keyStorePassword` | 指定访问 key store 的密码                  |

查看下面 \[Examples]\([Examples](https://logback.qos.ch/manual/usingSSL.html#Examples)) 部分，在应用启动的时候通过利用 logback 支持 SSL 的服务端组件来设置这些系统属性。

如果你的服务端组件使用的证书是商业认证机构 (CA) 认证，**你可能不需要在你应用的客户端组件中提供任何 SSL 配置。**&#x5F53;在你的服务端组件使用商业签名证书，仅仅只需要在运行服务端组件的 JVM 上设置系统的 key store 属性。

如果你使用自签名的服务器证书或者你服务器证书是认证机构 (CA) 签名但是它们的根证书不再 Java 平台默认的 trust store 中 (例如，你的组织有自己的内部签名机构)。你需要配置 JSSE 系统属性，以提供包含你服务器证书的 trust store 或者认证机构 (CA) 颁发的受信任根证书签名的服务器证书的 location，type，以及 password。**这些属性需要在每个利用支持 SSL 的客户端组件中的应用中设置。**

#### 客户端 trust store 配置的系统属性

| 属性名                                | 描述                                     |
| ---------------------------------- | -------------------------------------- |
| `javax.net.ssl.trustStore`         | 指定包含服务端组件的证书或者受信任根证书的文件的文件系统的路径        |
| `javax.net.ssl.trustStoreType`     | 指定 trust store 类型。如果这个属性没有被指定，则默认为 JKS |
| `javax.net.ssl.trustStorePassword` | 指定访问 trust store 的密码                   |

查看下面 \[Examples]\([Examples](https://logback.qos.ch/manual/usingSSL.html#Examples)) 部分，在应用启动的时候通过利用 logback 支持 SSL 的客户端组件来设置这些系统属性。

### 高级 SSL 配置

在特定的情况下，使用 JSEE 系统属性的基本 SSL 配置是不恰当的。比如，你想要在 web 应用中使用 `SSLServerSocketReceiver` 组件，你可能想要使用不同的证书为你的远程日志客户端标识你的日志服务器，而不是 web 服务器为了 web 客户端使用证书来标识自身。你可能想要在日志服务器上验证 SSL 客户端，确保只有真正授权的远程 logger 才可以连接。或者你的组织对于在组织所在的网络上使用 SSL 协议以及密码套件有严格的策略。为了满足这些需求，你需要使用 logback SSL 高级配置选项。

在配置 logback 组件支持 SSL 时，你需要在组件的配置中指定 `ssl` 属性来指定 SSL 的配置。

例如，如果你想要使用 `SSLServerSocketReceiver` 以及为日志服务器认证配置 key store 属性，你可以使用类似如下的配置：

```markup
<configuration>

  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="debug">
    <appender-ref ref="CONSOLE" />
  </root>

  <receiver class="ch.qos.logback.classic.net.server.SSLServerSocketReceiver">
    <ssl>
      <keyStore>
        <location>classpath:/logging-server-keystore.jks</location>
        <password>changeit</password>
      </keyStore>
    </ssl>
  </receiver> 

</configuration>
```

该配置将 key store 的位置指定为位于应用类路径下的 *logging-server-keystore.jks*。你也可以通过 `file:` URL 来指定 key store 的位置。

如果你想要在你的应用中使用 `SSLSocketAppender`，但是不想要改变默认 trust store 使用的 JSSE `javax.net.ssl.trustStore` 属性。你可以通过如下的方式进行配置：

```markup
<configuration>
  <appender name="SOCKET" class="ch.qos.logback.classic.net.SSLSocketAppender">
    <ssl>
      <trustStore>
        <location>classpath:/logging-server-truststore.jks</location>
        <password>changeit</password>
      </trustStore>
    </ssl>
  </appender>

  <root level="debug">
    <appender-ref ref="SOCKET" />
  </root>

</configuration>
```

该配置将 key store 的位置指定为位于应用类路径下的 *logging-server-keystore.jks*。你也可以通过 `file:` URL 来指定 key store 的位置。

#### SSL 配置属性

JSSE 公开 了大量的可配置选项。logback 的 SSL 支持几乎所有这些可用的选项在支持 SSL 组件的配置中指定。在使用 XML 配置时，在组件的配置中，SSL 属性被嵌套在 `<ssl>` 元素中引入。这个配置元素对应 [`SSLConfiguration`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/SSLConfiguration.html) 类。

当为你的组件配置 SSL 时，你仅仅只需要配置那些默认值不适合的 SSL 属性。过度指定 SSL 配置经常会导致一些难以诊断的问题。

下面的表格展示了顶层的 SSL 配置属性。许多顶层的属性还有额外的子属性，这些子属性将会顶层属性之后描述。

| 属性名                     | 类型                                                                                                                              | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **keyManagerFactory**   | [`KeyManagerFactoryFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/KeyManagerFactoryFactoryBean.html)     | 指定用于创建 [`KeyManagerFactory`](http://docs.oracle.com/javase/1.5.0/docs/api/javax/net/ssl/KeyManagerFactory.html) 的配置。如果这个属性没有配置，那么将会使用 Java 平台默认的 factory。见 [Key Manager Factory 配置](https://logback.qos.ch/manual/usingSSL.html#KeyManagerFactoryFactoryBean)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **keyStore**            | [`KeyStoreFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/KeyStoreFactoryBean.html)                       | <p>指定用于创建 <a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/security/KeyStore.html"><code>KeyStore</code></a> 的配置。通过这个属性创建的 KeyStore 必须包含唯一的 X.509 证书 (包含密钥，相应的证书以及 CA 认证链)。这个证书由本地 SSL 提供给远程的 SSL。<br>当配置一个 SSL 客户端时 (例如，<code>SSLSocketAppender</code>)，仅仅只有在远程配置需要验证客户端身份时才需要该属性。<br>当配置一个 SSL 服务端时 (例如，<code>SimpleSSLSocketServer</code>)，该属性指定的 key store 包含了服务端证书。如果没有配置这个属性，JSSE 的 <code>javax.net.ssl.keyStore</code> 系统属性必须配置用于提供服务端 key store 的位置。查看 <a href="https://docs.oracle.com/javase/1.5.0/docs/guide/security/jsse/JSSERefGuide.html#InstallationAndCustomization">定制 JSEE</a> 来获取更多关于 JSEE 系统属性的信息。<br>更多的信息查看 <a href="https://logback.qos.ch/manual/usingSSL.html#KeyStoreFactoryBean">Key Store 配置</a>。</p> |
| **parameters**          | [`SSLParametersConfiguration`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/SSLParametersConfiguration.html)         | 在 SSL 会话中，指定各种参数。见下面的 [SSL 参数配置](https://logback.qos.ch/manual/usingSSL.html#SSLParametersConfiguration)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **protocol**            | `String`                                                                                                                        | 指定创建 [`SSLContext`](http://docs.oracle.com/javase/1.5.0/docs/api/javax/net/ssl/SSLContext.html) 的 SSL 协议。见[命名规范](https://docs.oracle.com/javase/1.5.0/docs/guide/security/jsse/JSSERefGuide.html#AppA)。如果没有配置该参数，那么将使用 Java 平台默认的协议。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **provider**            | `String`                                                                                                                        | 指定创建 [`SSLContext`](http://docs.oracle.com/javase/1.5.0/docs/api/javax/net/ssl/SSLContext.html) 的 JSSE 提供者。如果没有配置该参数，那么将使用 Java 平台默认的 JSSE 提供者。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **secureRandom**        | [`SecureRandomFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/SecureRandomFactoryBean.html)               | 指定创建 [`SecureRandom`](http://docs.oracle.com/javase/1.5.0/docs/api/java/security/SecureRandom.html) (安全的随机数生成器) 的配置。如果没有配置该参数，那么将使用 Java 平台默认的生成器。见下面的 [安全随机数生成配置](https://logback.qos.ch/manual/usingSSL.html#SecureRandomFactoryBean)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **trustManagerFactory** | [`TrustManagerFactoryFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/TrustManagerFactoryFactoryBean.html) | 指定创建 [`TrustManagerFactory`](http://docs.oracle.com/javase/1.5.0/docs/api/javax/net/ssl/TrustManagerFactory.html) 的配置。如果没有指定该参数，那么将使用 Java 平台默认的 factory。见下面的 [受信任的管理工厂](https://logback.qos.ch/manual/usingSSL.html#TrustManagerFactoryFactoryBean)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **trustStore**          | [`KeyStoreFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/KeyStoreFactoryBean.html)                       | <p>指定创建 <a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/security/KeyStore.html"><code>KeyStore</code></a> 的配置，用于验证远程 SSL 的身份。通过这个属性创建的 KeyStore 应该包含一个或多个<em>信任锚 (trust anchors)</em> — keystore 中被标记为受信任的自签名证书。通常，trust store 包含自签名的 CA 证书。<br>通过该属性指定的 trust store 会覆盖任何通过 JSSE 的 <code>javax.net.ssl.trustStore</code> 以及平台默认的 trust store。</p>                                                                                                                                                                                                                                                                                                                                                                                |

#### Key Store 配置

[`KeyStoreFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/KeyStoreFactoryBean.html) 指定创建包含 X.509 证书的 [`KeyStore`](http://docs.oracle.com/javase/1.5.0/docs/api/java/security/KeyStore.html) 所需要的配置。这个 factory bean 的属性能够用于 [SSL 配置](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#%E9%AB%98%E7%BA%A7-ssl-%E9%85%8D%E7%BD%AE) 中的 [keyStore](https://logback.qos.ch/manual/usingSSL.html#ssl.keyStore) 以及 [trustStore](https://logback.qos.ch/manual/usingSSL.html#ssl.trustStore) 属性。

| 属性名          | 类型       | 描述                                                                                                                                               |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **location** | `String` | 指定 key store 的位置 URL。使用 `file:` 指定 keystore 在文件系统中的位置。使用 `classpath:` 指定 keystore 在类路径下的位置。如果 URL 没有指定具体的策略，那么将使用 `classpath:`。                  |
| **password** | `String` | 指定访问 keystore 的密码                                                                                                                                |
| **provider** | `String` | 指定用于创建 `KeyStore` 的 JCA 提供者的名字。如果没有指定该属性，那么将使用 Java 平台默认的 keystore 提供者。                                                                          |
| **type**     | `String` | 指定 `KeyStore` 的类型。见 [命名规范](http://docs.oracle.com/javase/1.5.0/docs/guide/security/CryptoSpec.html#AppA)。如果没有指定该属性，那么将使用 Java 平台默认的 keystore 类型。 |

#### Key Manager Factory 配置

[`KeyManagerFactoryFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/KeyManagerFactoryFactoryBean.html) 指定创建 [`KeyManagerFactory`](http://docs.oracle.com/javase/1.5.0/docs/api/javax/net/ssl/KeyManagerFactory.html) 需要的配置。通常，没有必要详细的配置 key manager factory，因为平台默认的 factory 就可以满足大部分的需求。

| 属性名           | 类型       | 描述                                                                                                                                                              |
| ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **algorithm** | `String` | 指定 `KeyManagerFactory` 算法的名字。见 [命名规范](http://docs.oracle.com/javase/1.5.0/docs/guide/security/CryptoSpec.html#AppA)。如果没有指定该属性，那么将会使用 Java 平台默认的 key manager 算法。 |
| **provider**  | `String` | 指定生成 `SecureRandom` 生成器的 JCA 提供者的名字。如果没有指定该属性，那么将会使用 Java 平台默认的 JSSE 提供者。                                                                                       |

#### Secure Random Generator 配置

[`SecureRandomFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/SecureRandomFactoryBean.html) 指定创建 [`SecureRandom`](http://docs.oracle.com/javase/1.5.0/docs/api/java/security/SecureRandom.html) 生成器所需要的配置。通常，没有必要详细的配置 secure random 生成器，因为平台默认的生成器就可以满足大部分的需求。

| 属性名           | 类型       | 描述                                                                                                                                                                              |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **algorithm** | `String` | 指定 `SecureRandom` 算法的名字。见 [命名规范](http://docs.oracle.com/javase/1.5.0/docs/guide/security/CryptoSpec.html#AppA)。如果没有指定该属性，那么将会使用 Java 平台默认的随机数生成器 (random number generation) 算法。 |
| **provider**  | `String` | 指定用于创建 `SecureRandom` 生成器的 JCA 提供者。如果没有指定该属性，那么将会使用 Java 平台默认的 JSSE 提供者。                                                                                                        |

#### SSL 参数配置

[`SSLParametersConfiguration`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/SSLParametersConfiguration.html) 允许定制受允许的 SSL 协议，密码套件，以及客户端认证选项。

| Property Name            | Type      | Description                                                                                                                                                                                                                          |
| ------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **excludedCipherSuites** | `String`  | <p>指定以逗号分隔的 SSL 密码套件的名字或者模式列表，用来在会话期间进行禁用。这个属性通过 SSL 引擎过滤密码套件。任何被该属性匹配到的密码套件都会被禁用。<br>以逗号分割的各个字段可以是字符串或者正则表达式。<br>查看密码套件的<a href="https://docs.oracle.com/javase/1.5.0/docs/guide/security/jsse/JSSERefGuide.html#AppA">命名规则</a></p> |
| **includedCipherSuites** | `String`  | 与上一个属性除了作用相反，其它都是一样 (懒得翻译了)。                                                                                                                                                                                                         |
| **excludedProtocols**    | `String`  | 这个是表示需要排除的 SSL 协议。与上一个属性，除了作用不同，其它都一样。                                                                                                                                                                                               |
| **includedProtocols**    | `String`  | 与上一个协议作用相反，其它一致。                                                                                                                                                                                                                     |
| **needClientAuth**       | `boolean` | 设置属性为 `true` 表示，服务端需要一个有效的客户端证书。当客户端组件为 `SSLSocketAppender` 时，该属性会被忽略。                                                                                                                                                               |
| **wantClientAuth**       | `boolean` | 设置属性为 `true` 表示，服务端想要一个有效的客户端证书。当客户端组件为 `SSLSocketAppender` 时，该属性会被忽略。(与上一个属性的差异，需要自己动手去实践。因为我也不清楚😂)                                                                                                                                |

#### Trust Manager Factory 配置

[`TrustManagerFactoryFactoryBean`](https://logback.qos.ch/xref/ch/qos/logback/core/net/ssl/TrustManagerFactoryFactoryBean.html) 指定创建 [`TrustManagerFactory`](http://docs.oracle.com/javase/1.5.0/docs/api/javax/net/ssl/TrustManagerFactory.html) 所需要的配置。通常，没有必要明确的配置 trust manager factory，平台默认的 factory 就可以满足大部分的需要。

| 属性名           | 类型       | 描述                                                                                                                                                                        |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **algorithm** | `String` | 指定 `TrustManagerFactory` 算法的名字。见 [命名标准](https://docs.oracle.com/javase/1.5.0/docs/guide/security/jsse/JSSERefGuide.html#AppA)。如果没有指定该属性，那么将使用 Java  平台默认的 key manager 算法。 |
| **provider**  | `String` | 指定创建 `SecureRandom` 生成器的 JCA 提供者的名字。如果没有指定该属性，那么将使用 Java 平台默认的 JSSE 提供者。                                                                                                  |

## 示例

### 使用 JSSE 系统属性

JSEE 系统属性可以用来指定包含服务端 X.509 证书的 keystore 的位置以及密码。或者包含客户端组件验证服务端信任的自签名根 CA 证书的 truststore 的位置以及密码。

#### 指定服务端 keystore

在运行服务端组件时，需要指定包含服务端证书的 keystore 的位置以及密码。一种方法是使用 JSSE 系统属性。下面的例子通过命令行的方式启动 `SimpleSSLSocketServer`：

```
java -DkeyStore=/etc/logback-server-keystore.jks \
     -DkeyStorePassword=changeit -DkeyStoreType=JKS \
     ch.qos.logback.net.SimpleSSLSocketServer 6000 /etc/logback-server-config.xml
```

注意，在使用 JSSE *keyStore* 系统属性时，指定了 keystore 的路径。在指定了 *logback.xml* 的路径时，keystore 的 URL 被指定。

虽然这个示例启动了一个提供 logback 的单机服务端应用，但是同样的系统属性可以在任何使用支持 SSL 的 logback 服务端组件上指定并启动。

#### 指定客户端 truststore

当使用客户端组件时，需要指定包含根 CA 证书的 truststore 的位置与密码，用于验证服务端的信任。一种方式是通过使用 JSSE 系统属性。下面的示例通过命令行启动一个名为 `com.example.MyLoggingApplication` 的应用，该应用使用一个或多个支持 SSL 的 logback 客户端组件。

```
java -DtrustStore=/etc/logback-client-truststore.jks \
     -DtrustStorePassword=changeit -DtrustStoreType=JKS \
     com.example.MyLoggingApplication
```

注意，在使用 JSSE *trustStore* 系统属性时，指定了 truststore 的路径。在指定了 *logback.xml* 的路径时，truststore 的 URL 被指定。

### 创建以及使用自签名的服务端组件证书

为了生成自签名的证书，可以使用 JRE 自带的 *keytool* 工具。下面的指令在服务端组件的 keystore 中创建一个自签名的 X.509 证书。以及创建在客户端组件中使用的 truststore。

#### 创建服务端组件证书

下面的命令在一个名为 *server.keystore* 的文件中生成自签名客户端证书。

```
keytool -genkey -alias server -dname "CN=my-logging-server" \
    -keyalg RSA -validity 365 -keystore server.keystore
Enter keystore password: <Enter password of your choosing>
Re-enter new password: <Re-enter same password>
Enter key password for <my-logging-server>
    (RETURN if same as keystore password):  <Press RETURN>
```

在 *dname* 中使用的名字 *my-logging-server* 可以是任何你选择的有效的名字。你可能想要使用服务端主机上的全限定名。*validity* 参数可以指定从当前日期开始直到证书过期的天数。

在实际的设置中，为包含服务端证书的 keystore 选择一个强密码是非常重要的。密码用来保护服务端的密码，防止被已授权方使用。记下刚才设置的密码，因为在接下来配置服务端的时候需要使用。

#### 为客户端组件创建 truststore

由于要配置客户端组件，在前一个步骤中创建的服务端证书需要从 keystore 中导出，并且导入到 truststore 中。下面的命令将会导出证书并且导入到名为 *server.truststore* 的 truststore。

```
keytool -export -rfc -alias server -keystore server.keystore \
    -file server.crt
Enter keystore password: <Enter password you chose for in previous step>

keytool -import -alias server -file server.crt -keystore server.truststore
Enter keystore password: <Enter password of your choosing>
Re-enter new password: <Re-enter same password>
Owner: CN=my-logging-server
Issuer: CN=my-logging-server
Serial number: 6e7eea40
Valid from: Sun Mar 31 07:57:29 EDT 2013 until: Mon Mar 31 07:57:29 EDT 2014

   ...

Trust this certificate? [no]:  <Enter "yes">
```

第一个命令从 keystore 中导出服务端证书 (但是不是服务端密钥) 到一个名为 *server.crt* 的文件。第二个步骤创建一个名为 *server.truststore*，包含服务端证书的新的 truststore。

在实际的设置中，为 truststore 选择一个不同于服务端 keystore 的强密码非常的重要。记住这个密码，因为在配置客户端 appender 时需要使用。

#### 配置服务端组件

拷贝 *server.keystore* 到你的服务端应用的配置中。keystore 可以放在应用的类路径下，或者放在服务器主机文件系统的某个位置。在配置文件中指定 keystore 位置 URL 时，可以使用 `classpath:` 或者 `file:`。一个示例的服务端配置如下：

```markup
<configuration debug="true">
  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="CONSOLE" />
  </root>

  <server class="ch.qos.logback.classic.net.server.SSLServerSocketReceiver">
    <ssl>
      <keyStore>
        <location>classpath:server.keystore</location>
        <password>${server.keystore.password}</password>
      </keyStore>
    </ssl>
  </server>
</configuration>
```

示例假设 keystore 放在应用类路径的根路径下。

配置文件中使用 *server.keystore.password* 替换符指定 keystore 的密码。这种方式可以避免将密码直接存储在配置文件中。例如，在启动的时候，你的应用可能会在控制台提示密码，之后在配置日志系统之前使用输入的密码将 *server.keystore.password* 设置为系统属性。

#### 配置客户端组件

你需要将 *server.truststore* 文件拷贝到使用支持 SSL 组件充当客户端角色的每个应用的配置中。truststore 可以放置在应用的类路径下，或者文件系统的某个地方。可以通过 `classpath:` 或者 `file:` 来指定 truststore 位置的 URL。客户端 appender 的配置示例如下：

> Example:

```markup
<configuration debug="true">
  <appender name="SOCKET" class="ch.qos.logback.classic.net.SSLSocketAppender">
    <remoteHost>${host}</remoteHost>
    <ssl>
      <trustStore>
        <location>classpath:server.truststore</location>
        <password>${server.truststore.password}</password>
      </trustStore>
    </ssl>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="SOCKET" />
  </root>
</configuration>
```

示例中假设 truststore 位于应用类路径的根路径下。

配置中使用 *server.truststore.password* 替换符来指定 truststore 的密码。这种方式可以避免直接将密码存储在配置文件中。例如，应用启动时会在控制台提示密码，之后可以在配置日志系统之前通过输入密码将 *server.truststore.password* 设置为系统属性。

## 审核 SSL 配置

在需要安全通行的设置中，经常需要审核组件的 SSL 配置，验证与本地策略的一致性。在 logback 初始化时，logback 中的 SSL 通过提供 SSL 配置的详细日志来满足这一需求。可以在配置中使用 `debug` 属性来开启这个功能。

```markup
<configuration debug="true">

  ...

</configuration>
```

当使用了 debug 属性，在日志系统初始化时，所有与 SSL 配置产生的相关信息都会被打印出来。一个典型的示例如下：

> Example:

```java
06:46:31,941 |-INFO in SSLServerSocketReceiver@4ef18d37 - SSL protocol 'SSL' provider 'SunJSSE version 1.6'
06:46:31,967 |-INFO in SSLServerSocketReceiver@4ef18d37 - key store of type 'JKS' provider 'SUN version 1.6': file:src/main/java/chapters/appenders/socket/ssl/keystore.jks
06:46:31,967 |-INFO in SSLServerSocketReceiver@4ef18d37 - key manager algorithm 'SunX509' provider 'SunJSSE version 1.6'
06:46:31,973 |-INFO in SSLServerSocketReceiver@4ef18d37 - secure random algorithm 'SHA1PRNG' provider 'SUN version 1.6'
06:46:32,755 |-INFO in SSLParametersConfiguration@4a6f19d5 - enabled protocol: SSLv2Hello
06:46:32,755 |-INFO in SSLParametersConfiguration@4a6f19d5 - enabled protocol: SSLv3
06:46:32,755 |-INFO in SSLParametersConfiguration@4a6f19d5 - enabled protocol: TLSv1
06:46:32,756 |-INFO in SSLParametersConfiguration@4a6f19d5 - enabled cipher suite: SSL_RSA_WITH_RC4_128_MD5
06:46:32,756 |-INFO in SSLParametersConfiguration@4a6f19d5 - enabled cipher suite: SSL_RSA_WITH_RC4_128_SHA
06:46:32,756 |-INFO in SSLParametersConfiguration@4a6f19d5 - enabled cipher suite: TLS_RSA_WITH_AES_256_CBC_SHA
```

为了简便起见，这里的输出被截断了一部分。但是包含了协议、提供者、算法、密码套件以及在配置中所使用的 keystore 与 truststore 位置。

虽然没有一个审核日志是敏感的，但是为了安全，在实际的设置中，在配置被验证之后，日志信息不应该被启用。将 `debug` 属性移除，或者设置为 `false`，将禁用日志审核。

## 解决 SSL 异常

当 SSL 配置错误时，普遍的结果是客户端与服务端组件不能正常的通常。当客户端尝试连接服务端时，这个问题通常会被双方抛出的异常表现出来。

异常消息内容的不容取决于你查看的是客户端的日志还是服务端的日志。最主要的原因是在会话期间，错误报告受限制于内部的协议。由于这种情况，为了定位会话问题，需要查看客户端与服务端的日志。

### Server's Certificate is Not Available

当启动服务端组件时，你会在日志中看到如下的异常：

*javax.net.ssl.SSLException: No available certificate or key corresponds to the SSL cipher suites which are enabled*

大部分情况下表示你没有配置包含服务端密钥的 keystore 以及相应的证书。

#### 解决办法

使用 [keystore 系统属性](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#%E6%9C%8D%E5%8A%A1%E7%AB%AF-key-store-%E9%85%8D%E7%BD%AE%E7%9A%84%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7) 或者服务端组件 `ssl` 属性中的 [keyStore](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7) 属性。你必须指定包含服务端密钥以及证书的 keystore 的路径以及密码。

### Client Does Not Trust the Server

当客户端尝试连接服务端时，在日志中看到如下的异常：

*javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed*

这个问题表示服务端展示的证书，客户端不相信。大部分情况下是使用自签名的证书 (或者服务端证书由你组织内部的认证机构所签名) 并且你还没有配置客户端，导致它引用了包含服务端自签名证书 (或者你的服务器证书是由 CA 签名的受信任的根证书) 的 truststore。

这个问题还会发生在服务端证书过期或者被取消的情况下。在客户端每次尝试进行连接时，你在服务端的日志中会看到如下的异常信息：

*javax.net.ssl.SSLHandshakeException: Received fatal alert: ...*

异常信息的余下部分通常会提供一个代码来表明为什么客户端拒绝服务端证书：

| 代码                    | 描述                          |
| --------------------- | --------------------------- |
| `certificate_unknown` | 通常表示客户端 truststore 没有被正确的配置 |
| `certificate_expired` | 表示服务端证书已过期，需要更换             |
| `certificate_revoked` | 表示颁发的 CA 已经撤销了服务端证书，需要更换    |

#### 解决办法

如果服务端日志显示 `certificate_unknown`，那么使用 [truststore 系统属性](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#%E5%AE%A2%E6%88%B7%E7%AB%AF-trust-store-%E9%85%8D%E7%BD%AE%E7%9A%84%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7) 或者 appender 组件 `ssl` 属性中的 [trustStore](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7) 属性，指定包含服务端自签名证书或者颁发的 CA 根证书的 truststore 的路径以及密码。

如果服务端日志显示 `certificate_expired` 或者 `certificate_revoked`，表示服务端需要一个新的证书。新的证书以及相关的密钥需要在服务端配置的 keystore 中更换。并且，如果使用自签名服务端证书，那么还需要更换在客户端 appender 中配置的 truststore 服务端证书。

### Server Does Not Trust the Client

注意：**这个问题仅仅发生在你明确的配置服务端请求客户端证书时。(使用** [**needClientAuth**](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) **或者** [**wantClientAuth**](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) **属性)。**

当客户端尝试连接日志服务器时，可以在客户端日志中看到如下的异常信息：

*javax.net.ssl.SSLHandshakeException: Received fatal alert: ...*

异常信息的其余部分会提供一个代码表明为什么服务端拒绝客户端证书。

| 代码                    | 描述                         |
| --------------------- | -------------------------- |
| `certificate_unknown` | 通常表示服务端 truststore 没有正确的配置 |
| `certificate_expired` | 表示客户端证书已经过期，需要更换           |
| `certificate_revoked` | 表示颁发的 CA 已经撤销了客户端证书，需要更换   |

#### 解决办法

如果客户端日志信息显示 `bad_certificate`，那么使用 [truststore 系统属性](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#%E5%AE%A2%E6%88%B7%E7%AB%AF-trust-store-%E9%85%8D%E7%BD%AE%E7%9A%84%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7) 或者服务端组件 `ssl` 属性中的 [trustStore](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7) 属性，指定包含客户端自签名证书或者颁发的 CA 根证书的 truststore 的路径以及密码。

如果服务端日志信息显示 `certificate_expired` 或者 `certificate_revoked`，表示客户端需要一个新的证书。需要更换在客户端配置中指定的 keystore 的新证书以及相应的密钥。

### Client and Server Cannot Agree on a Protocol

注意：**这个问题仅仅只在你的配置中明确的配置了** [**excludedProtocols**](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) **或者** [**includedProtocols**](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) **SSL 协议时。**

当客户端尝试连接服务端时，你会在日志中看到如下异常信息：

*javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake\_failure*

服务端的日志信息通常更加详细，例如：

*javax.net.ssl.SSLHandshakeException: SSLv2Hello is disabled*

通常，表示你已经排除其中的一个协议。

#### 解决办法

检查服务端与客户端指定的 [excludedProtocols](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) 以及 [includedProtocols](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) 属性的值。

### Client and Server Cannot Agree on a Cipher Suite

注意：**通常这个问题只发生在你明确的在配置文件中指定了** [**excludedCipherSuites**](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) **或者** [**includedCipherSuites**](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) **SSL 密码套件时。**

当客户端尝试去连接服务端时，你会在日志中看到如下的异常信息：

*javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake\_failure*

服务端的日志信息通常会更加详细：

*javax.net.ssl.SSLHandshakeException: no cipher suites in common*

这意味着你已经在服务端与客户端配置了密码套件，但是它们各自密码套件的交集为空。

#### 解决办法

检查服务端与客户端指定的 [excludedCipherSuites](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) 以及 [includedCipherSuites](https://github.com/Volong/logback-chinese-manual/blob/master/15%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E4%BD%BF%E7%94%A8%20SSL.md#ssl-%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE) 属性的值。



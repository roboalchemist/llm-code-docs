# Source: https://docs.vespa.ai/en/reference/rag/chunking.html.md

# Chunking Reference

 

Reference configuration for _chunkers_: Components that splits text into pieces in[chunk indexing expressions](../writing/indexing-language.html#chunk), as in

```
indexing: input myTextField | chunk fixed-length 500 | index
```

See also the [guide to working with chunks](../../rag/working-with-chunks.html).

## Built-in chunkers

Vespa provides these built-in chunkers:

| Chunker id | Arguments | Description |
| --- | --- | --- |
| sentence | - | Splits the text into chunks at sentence boundaries. |
| fixed-length | target chunk length in characters | Splits the text into chunks with roughly equal length. This will prefer to make chunks of similar length, and to split at reasonable locations over matching the target length exactly. |

## Chunker components

Chunkers are [components](../../applications/components.html), so you can also add your own:

```
```
<container version="1.0">
    <component id="myChunker"
      class="com.example.MyChunker"
      bundle="the name in artifactId in pom.xml">
        <config name='com.example.my-chunker'>
            <myValue>foo</myValue>
        </config>
    </component>
</container>
```
```

You create a chunker component by implementing the[com.yahoo.language.process.Chunker](https://github.com/vespa-engine/vespa/blob/master/linguistics/src/main/java/com/yahoo/language/process/Chunker.java)interface, see [these examples](https://github.com/vespa-engine/vespa/tree/master/linguistics/src/main/java/ai/vespa/language/chunker).

 Copyright © 2026 - [Cookie Preferences](#)


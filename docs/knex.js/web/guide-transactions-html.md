# Source: https://knexjs.org/guide/transactions.html

Title: Transactions | Knex.js

URL Source: https://knexjs.org/guide/transactions.html

Markdown Content:
Transactions | Knex.js
===============

[Skip to content](https://knexjs.org/guide/transactions.html#VPContent)

[![Image 1](https://knexjs.org/knex-logo.svg)Knex.js](https://knexjs.org/)

Search K

 Main Navigation [Guide](https://knexjs.org/guide/)[F.A.Q.](https://knexjs.org/faq/)[Changelog](https://knexjs.org/changelog.html)

[](https://github.com/knex/knex)

Appearance

[](https://github.com/knex/knex)

Menu

Return to top

 Sidebar Navigation

[Installation ------------](https://knexjs.org/guide/)

[Node.js](https://knexjs.org/guide/#node-js)

[Browser](https://knexjs.org/guide/#browser)

[### Configuration Options](https://knexjs.org/guide/#configuration-options)

[withUserParams](https://knexjs.org/guide/#withuserparams)

[debug](https://knexjs.org/guide/#debug)

[asyncStackTraces](https://knexjs.org/guide/#asyncstacktraces)

[pool](https://knexjs.org/guide/#pool)

[afterCreate](https://knexjs.org/guide/#aftercreate)

[acquireConnectionTimeout](https://knexjs.org/guide/#acquireconnectiontimeout)

[fetchAsString](https://knexjs.org/guide/#fetchasstring)

[defaultDateTimePrecision](https://knexjs.org/guide/#defaultdatetimeprecision)

[migrations](https://knexjs.org/guide/#migrations)

[postProcessResponse](https://knexjs.org/guide/#postprocessresponse)

[wrapIdentifier](https://knexjs.org/guide/#wrapidentifier)

[log](https://knexjs.org/guide/#log)

[compileSqlOnError](https://knexjs.org/guide/#compilesqlonerror)

[TypeScript](https://knexjs.org/guide/#typescript)

[Query Builder -------------](https://knexjs.org/guide/query-builder.html)

[Identifier Syntax](https://knexjs.org/guide/query-builder.html#identifier-syntax)

[### Common](https://knexjs.org/guide/query-builder.html#common)

[knex](https://knexjs.org/guide/query-builder.html#knex)

[only (knex/from option) PG only](https://knexjs.org/guide/query-builder.html#only-knex-from-option)

[timeout PG+MY only](https://knexjs.org/guide/query-builder.html#timeout)

[select](https://knexjs.org/guide/query-builder.html#select)

[as](https://knexjs.org/guide/query-builder.html#as)

[column](https://knexjs.org/guide/query-builder.html#column)

[from](https://knexjs.org/guide/query-builder.html#from)

[fromRaw](https://knexjs.org/guide/query-builder.html#fromraw)

[with MY CR RS](https://knexjs.org/guide/query-builder.html#with)

[withRecursive MY CR RS](https://knexjs.org/guide/query-builder.html#withrecursive)

[withMaterialized PG+SQ only](https://knexjs.org/guide/query-builder.html#withmaterialized)

[withNotMaterialized PG+SQ only](https://knexjs.org/guide/query-builder.html#withnotmaterialized)

[withSchema](https://knexjs.org/guide/query-builder.html#withschema)

[jsonExtract](https://knexjs.org/guide/query-builder.html#jsonextract)

[jsonSet RS](https://knexjs.org/guide/query-builder.html#jsonset)

[jsonInsert RS](https://knexjs.org/guide/query-builder.html#jsoninsert)

[jsonRemove RS](https://knexjs.org/guide/query-builder.html#jsonremove)

[offset](https://knexjs.org/guide/query-builder.html#offset)

[limit](https://knexjs.org/guide/query-builder.html#limit)

[union](https://knexjs.org/guide/query-builder.html#union)

[unionAll](https://knexjs.org/guide/query-builder.html#unionall)

[intersect](https://knexjs.org/guide/query-builder.html#intersect)

[except](https://knexjs.org/guide/query-builder.html#except)

[insert](https://knexjs.org/guide/query-builder.html#insert)

[onConflict MS OR CR RS](https://knexjs.org/guide/query-builder.html#onconflict)

[upsert MY+CR only](https://knexjs.org/guide/query-builder.html#upsert)

[update](https://knexjs.org/guide/query-builder.html#update)

[updateFrom PG only](https://knexjs.org/guide/query-builder.html#updatefrom)

[del / delete](https://knexjs.org/guide/query-builder.html#del-delete)

[using PG only](https://knexjs.org/guide/query-builder.html#using)

[returning MY CR RS](https://knexjs.org/guide/query-builder.html#returning)

[transacting](https://knexjs.org/guide/query-builder.html#transacting)

[forUpdate PG+MY only](https://knexjs.org/guide/query-builder.html#forupdate)

[forShare PG+MY only](https://knexjs.org/guide/query-builder.html#forshare)

[forNoKeyUpdate PG only](https://knexjs.org/guide/query-builder.html#fornokeyupdate)

[forKeyShare PG only](https://knexjs.org/guide/query-builder.html#forkeyshare)

[skipLocked PG+MY only](https://knexjs.org/guide/query-builder.html#skiplocked)

[noWait PG+MY only](https://knexjs.org/guide/query-builder.html#nowait)

[count](https://knexjs.org/guide/query-builder.html#count)

[min](https://knexjs.org/guide/query-builder.html#min)

[max](https://knexjs.org/guide/query-builder.html#max)

[sum](https://knexjs.org/guide/query-builder.html#sum)

[avg](https://knexjs.org/guide/query-builder.html#avg)

[increment](https://knexjs.org/guide/query-builder.html#increment)

[decrement](https://knexjs.org/guide/query-builder.html#decrement)

[truncate](https://knexjs.org/guide/query-builder.html#truncate)

[pluck](https://knexjs.org/guide/query-builder.html#pluck)

[first](https://knexjs.org/guide/query-builder.html#first)

[hintComment MY+OR only](https://knexjs.org/guide/query-builder.html#hintcomment)

[comment](https://knexjs.org/guide/query-builder.html#comment)

[clone](https://knexjs.org/guide/query-builder.html#clone)

[denseRank](https://knexjs.org/guide/query-builder.html#denserank)

[rank](https://knexjs.org/guide/query-builder.html#rank)

[rowNumber](https://knexjs.org/guide/query-builder.html#rownumber)

[partitionBy](https://knexjs.org/guide/query-builder.html#partitionby)

[modify](https://knexjs.org/guide/query-builder.html#modify)

[columnInfo](https://knexjs.org/guide/query-builder.html#columninfo)

[debug](https://knexjs.org/guide/query-builder.html#debug)

[connection](https://knexjs.org/guide/query-builder.html#connection)

[options](https://knexjs.org/guide/query-builder.html#options)

[queryContext](https://knexjs.org/guide/query-builder.html#querycontext)

[Extending Query Builder](https://knexjs.org/guide/query-builder.html#extending-query-builder)

[### Where Clauses](https://knexjs.org/guide/query-builder.html#where-clauses)

[where](https://knexjs.org/guide/query-builder.html#where)

[whereNot](https://knexjs.org/guide/query-builder.html#wherenot)

[whereIn](https://knexjs.org/guide/query-builder.html#wherein)

[whereNotIn](https://knexjs.org/guide/query-builder.html#wherenotin)

[whereNull](https://knexjs.org/guide/query-builder.html#wherenull)

[whereNotNull](https://knexjs.org/guide/query-builder.html#wherenotnull)

[whereExists](https://knexjs.org/guide/query-builder.html#whereexists)

[whereNotExists](https://knexjs.org/guide/query-builder.html#wherenotexists)

[whereBetween](https://knexjs.org/guide/query-builder.html#wherebetween)

[whereNotBetween](https://knexjs.org/guide/query-builder.html#wherenotbetween)

[whereRaw](https://knexjs.org/guide/query-builder.html#whereraw)

[whereLike](https://knexjs.org/guide/query-builder.html#wherelike)

[whereILike](https://knexjs.org/guide/query-builder.html#whereilike)

[whereJsonObject](https://knexjs.org/guide/query-builder.html#wherejsonobject)

[whereJsonPath](https://knexjs.org/guide/query-builder.html#wherejsonpath)

[whereJsonSupersetOf SQ MS OR RS](https://knexjs.org/guide/query-builder.html#wherejsonsupersetof)

[whereJsonSubsetOf SQ MS OR RS](https://knexjs.org/guide/query-builder.html#wherejsonsubsetof)

[### Join Methods](https://knexjs.org/guide/query-builder.html#join-methods)

[join](https://knexjs.org/guide/query-builder.html#join)

[innerJoin](https://knexjs.org/guide/query-builder.html#innerjoin)

[leftJoin](https://knexjs.org/guide/query-builder.html#leftjoin)

[leftOuterJoin](https://knexjs.org/guide/query-builder.html#leftouterjoin)

[rightJoin](https://knexjs.org/guide/query-builder.html#rightjoin)

[rightOuterJoin](https://knexjs.org/guide/query-builder.html#rightouterjoin)

[fullOuterJoin](https://knexjs.org/guide/query-builder.html#fullouterjoin)

[crossJoin](https://knexjs.org/guide/query-builder.html#crossjoin)

[crossJoin conditions MY+SQ only](https://knexjs.org/guide/query-builder.html#crossjoin-conditions)

[joinRaw](https://knexjs.org/guide/query-builder.html#joinraw)

[### OnClauses](https://knexjs.org/guide/query-builder.html#onclauses)

[onIn](https://knexjs.org/guide/query-builder.html#onin)

[onNotIn](https://knexjs.org/guide/query-builder.html#onnotin)

[onNull](https://knexjs.org/guide/query-builder.html#onnull)

[onNotNull](https://knexjs.org/guide/query-builder.html#onnotnull)

[onExists](https://knexjs.org/guide/query-builder.html#onexists)

[onNotExists](https://knexjs.org/guide/query-builder.html#onnotexists)

[onBetween](https://knexjs.org/guide/query-builder.html#onbetween)

[onNotBetween](https://knexjs.org/guide/query-builder.html#onnotbetween)

[onJsonPathEquals](https://knexjs.org/guide/query-builder.html#onjsonpathequals)

[### ClearClauses](https://knexjs.org/guide/query-builder.html#clearclauses)

[clear](https://knexjs.org/guide/query-builder.html#clear)

[clearSelect](https://knexjs.org/guide/query-builder.html#clearselect)

[clearWhere](https://knexjs.org/guide/query-builder.html#clearwhere)

[clearGroup](https://knexjs.org/guide/query-builder.html#cleargroup)

[clearOrder](https://knexjs.org/guide/query-builder.html#clearorder)

[clearHaving](https://knexjs.org/guide/query-builder.html#clearhaving)

[clearCounters](https://knexjs.org/guide/query-builder.html#clearcounters)

[distinct](https://knexjs.org/guide/query-builder.html#distinct)

[distinctOn PG only](https://knexjs.org/guide/query-builder.html#distincton)

[groupBy](https://knexjs.org/guide/query-builder.html#groupby)

[groupByRaw](https://knexjs.org/guide/query-builder.html#groupbyraw)

[orderBy](https://knexjs.org/guide/query-builder.html#orderby)

[orderByRaw](https://knexjs.org/guide/query-builder.html#orderbyraw)

[### Having Clauses](https://knexjs.org/guide/query-builder.html#having-clauses)

[having](https://knexjs.org/guide/query-builder.html#having)

[havingIn](https://knexjs.org/guide/query-builder.html#havingin)

[havingNotIn](https://knexjs.org/guide/query-builder.html#havingnotin)

[havingNull](https://knexjs.org/guide/query-builder.html#havingnull)

[havingNotNull](https://knexjs.org/guide/query-builder.html#havingnotnull)

[havingExists](https://knexjs.org/guide/query-builder.html#havingexists)

[havingNotExists](https://knexjs.org/guide/query-builder.html#havingnotexists)

[havingBetween](https://knexjs.org/guide/query-builder.html#havingbetween)

[havingNotBetween](https://knexjs.org/guide/query-builder.html#havingnotbetween)

[havingRaw](https://knexjs.org/guide/query-builder.html#havingraw)

[Transactions ------------](https://knexjs.org/guide/transactions.html)

[Transaction Modes](https://knexjs.org/guide/transactions.html#transaction-modes)

[Schema Builder --------------](https://knexjs.org/guide/schema-builder.html)

[### Essentials](https://knexjs.org/guide/schema-builder.html#essentials)

[withSchema](https://knexjs.org/guide/schema-builder.html#withschema)

[createTable](https://knexjs.org/guide/schema-builder.html#createtable)

[createTableLike](https://knexjs.org/guide/schema-builder.html#createtablelike)

[dropTable](https://knexjs.org/guide/schema-builder.html#droptable)

[dropTableIfExists](https://knexjs.org/guide/schema-builder.html#droptableifexists)

[renameTable](https://knexjs.org/guide/schema-builder.html#renametable)

[hasTable](https://knexjs.org/guide/schema-builder.html#hastable)

[hasColumn](https://knexjs.org/guide/schema-builder.html#hascolumn)

[table](https://knexjs.org/guide/schema-builder.html#table)

[alterTable](https://knexjs.org/guide/schema-builder.html#altertable)

[createView](https://knexjs.org/guide/schema-builder.html#createview)

[createViewOrReplace ~SQ](https://knexjs.org/guide/schema-builder.html#createvieworreplace)

[createMaterializedView MY SQ MS](https://knexjs.org/guide/schema-builder.html#creatematerializedview)

[refreshMaterializedView MY SQ MS](https://knexjs.org/guide/schema-builder.html#refreshmaterializedview)

[dropView](https://knexjs.org/guide/schema-builder.html#dropview)

[dropViewIfExists](https://knexjs.org/guide/schema-builder.html#dropviewifexists)

[dropMaterializedView MY SQ MS](https://knexjs.org/guide/schema-builder.html#dropmaterializedview)

[dropMaterializedViewIfExists MY SQ MS](https://knexjs.org/guide/schema-builder.html#dropmaterializedviewifexists)

[renameView OR SQ](https://knexjs.org/guide/schema-builder.html#renameview)

[alterView MY SQ OR CR](https://knexjs.org/guide/schema-builder.html#alterview)

[generateDdlCommands](https://knexjs.org/guide/schema-builder.html#generateddlcommands)

[raw](https://knexjs.org/guide/schema-builder.html#raw)

[queryContext](https://knexjs.org/guide/schema-builder.html#querycontext)

[createSchema PG only](https://knexjs.org/guide/schema-builder.html#createschema)

[createSchemaIfNotExists PG only](https://knexjs.org/guide/schema-builder.html#createschemaifnotexists)

[dropSchema PG only](https://knexjs.org/guide/schema-builder.html#dropschema)

[dropSchemaIfExists PG only](https://knexjs.org/guide/schema-builder.html#dropschemaifexists)

[### Schema Building](https://knexjs.org/guide/schema-builder.html#schema-building)

[dropColumn ~SQ](https://knexjs.org/guide/schema-builder.html#dropcolumn)

[dropColumns ~SQ](https://knexjs.org/guide/schema-builder.html#dropcolumns)

[renameColumn](https://knexjs.org/guide/schema-builder.html#renamecolumn)

[increments](https://knexjs.org/guide/schema-builder.html#increments)

[integer](https://knexjs.org/guide/schema-builder.html#integer)

[bigInteger](https://knexjs.org/guide/schema-builder.html#biginteger)

[tinyint](https://knexjs.org/guide/schema-builder.html#tinyint)

[smallint](https://knexjs.org/guide/schema-builder.html#smallint)

[mediumint](https://knexjs.org/guide/schema-builder.html#mediumint)

[bigint](https://knexjs.org/guide/schema-builder.html#bigint)

[text](https://knexjs.org/guide/schema-builder.html#text)

[string](https://knexjs.org/guide/schema-builder.html#string)

[float](https://knexjs.org/guide/schema-builder.html#float)

[double](https://knexjs.org/guide/schema-builder.html#double)

[decimal](https://knexjs.org/guide/schema-builder.html#decimal)

[boolean](https://knexjs.org/guide/schema-builder.html#boolean)

[date](https://knexjs.org/guide/schema-builder.html#date)

[datetime](https://knexjs.org/guide/schema-builder.html#datetime)

[time RS](https://knexjs.org/guide/schema-builder.html#time)

[timestamp](https://knexjs.org/guide/schema-builder.html#timestamp)

[timestamps](https://knexjs.org/guide/schema-builder.html#timestamps)

[dropTimestamps](https://knexjs.org/guide/schema-builder.html#droptimestamps)

[binary](https://knexjs.org/guide/schema-builder.html#binary)

[enum / enu](https://knexjs.org/guide/schema-builder.html#enum-enu)

[json](https://knexjs.org/guide/schema-builder.html#json)

[jsonb](https://knexjs.org/guide/schema-builder.html#jsonb)

[uuid RS](https://knexjs.org/guide/schema-builder.html#uuid)

[geometry MY OR CR RS](https://knexjs.org/guide/schema-builder.html#geometry)

[geography MY OR CR RS](https://knexjs.org/guide/schema-builder.html#geography)

[point CR MS](https://knexjs.org/guide/schema-builder.html#point)

[comment](https://knexjs.org/guide/schema-builder.html#comment)

[engine MY only](https://knexjs.org/guide/schema-builder.html#engine)

[charset MY only](https://knexjs.org/guide/schema-builder.html#charset)

[collate MY only](https://knexjs.org/guide/schema-builder.html#collate)

[inherits PG only](https://knexjs.org/guide/schema-builder.html#inherits)

[specificType](https://knexjs.org/guide/schema-builder.html#specifictype)

[index RS](https://knexjs.org/guide/schema-builder.html#index)

[dropIndex RS](https://knexjs.org/guide/schema-builder.html#dropindex)

[setNullable ~SQ](https://knexjs.org/guide/schema-builder.html#setnullable)

[dropNullable ~SQ](https://knexjs.org/guide/schema-builder.html#dropnullable)

[primary ~SQ](https://knexjs.org/guide/schema-builder.html#primary)

[unique](https://knexjs.org/guide/schema-builder.html#unique)

[foreign ~SQ](https://knexjs.org/guide/schema-builder.html#foreign)

[dropForeign ~SQ](https://knexjs.org/guide/schema-builder.html#dropforeign)

[dropForeignIfExists](https://knexjs.org/guide/schema-builder.html#dropforeignifexists)

[dropUnique](https://knexjs.org/guide/schema-builder.html#dropunique)

[dropUniqueIfExists](https://knexjs.org/guide/schema-builder.html#dropuniqueifexists)

[dropPrimary ~SQ](https://knexjs.org/guide/schema-builder.html#dropprimary)

[dropPrimaryIfExists](https://knexjs.org/guide/schema-builder.html#dropprimaryifexists)

[queryContext](https://knexjs.org/guide/schema-builder.html#querycontext-1)

[### Chainable Methods](https://knexjs.org/guide/schema-builder.html#chainable-methods)

[alter ~SQ RS](https://knexjs.org/guide/schema-builder.html#alter)

[index](https://knexjs.org/guide/schema-builder.html#index-1)

[primary](https://knexjs.org/guide/schema-builder.html#primary-1)

[unique](https://knexjs.org/guide/schema-builder.html#unique-1)

[references](https://knexjs.org/guide/schema-builder.html#references)

[inTable](https://knexjs.org/guide/schema-builder.html#intable)

[onDelete](https://knexjs.org/guide/schema-builder.html#ondelete)

[onUpdate](https://knexjs.org/guide/schema-builder.html#onupdate)

[defaultTo](https://knexjs.org/guide/schema-builder.html#defaultto)

[unsigned](https://knexjs.org/guide/schema-builder.html#unsigned)

[notNullable](https://knexjs.org/guide/schema-builder.html#notnullable)

[nullable](https://knexjs.org/guide/schema-builder.html#nullable)

[first](https://knexjs.org/guide/schema-builder.html#first)

[after](https://knexjs.org/guide/schema-builder.html#after)

[comment](https://knexjs.org/guide/schema-builder.html#comment-1)

[collate](https://knexjs.org/guide/schema-builder.html#collate-1)

[### View](https://knexjs.org/guide/schema-builder.html#view)

[columns](https://knexjs.org/guide/schema-builder.html#columns)

[as](https://knexjs.org/guide/schema-builder.html#as)

[checkOption SQ MS CR](https://knexjs.org/guide/schema-builder.html#checkoption)

[localCheckOption SQ MS OR CR](https://knexjs.org/guide/schema-builder.html#localcheckoption)

[cascadedCheckOption SQ MS OR CR](https://knexjs.org/guide/schema-builder.html#cascadedcheckoption)

[### Checks](https://knexjs.org/guide/schema-builder.html#checks)

[check](https://knexjs.org/guide/schema-builder.html#check)

[checkPositive](https://knexjs.org/guide/schema-builder.html#checkpositive)

[checkNegative](https://knexjs.org/guide/schema-builder.html#checknegative)

[checkIn](https://knexjs.org/guide/schema-builder.html#checkin)

[checkNotIn](https://knexjs.org/guide/schema-builder.html#checknotin)

[checkBetween](https://knexjs.org/guide/schema-builder.html#checkbetween)

[checkLength](https://knexjs.org/guide/schema-builder.html#checklength)

[checkRegex](https://knexjs.org/guide/schema-builder.html#checkregex)

[dropChecks](https://knexjs.org/guide/schema-builder.html#dropchecks)

[Raw ---](https://knexjs.org/guide/raw.html)

[### Raw Parameter Binding](https://knexjs.org/guide/raw.html#raw-parameter-binding)

[Named bindings with array values](https://knexjs.org/guide/raw.html#named-bindings-with-array-values)

[Raw Expressions](https://knexjs.org/guide/raw.html#raw-expressions)

[Raw Queries](https://knexjs.org/guide/raw.html#raw-queries)

[Wrapped Queries](https://knexjs.org/guide/raw.html#wrapped-queries)

[Ref ---](https://knexjs.org/guide/ref.html)

[### Usage](https://knexjs.org/guide/ref.html#usage)

[withSchema](https://knexjs.org/guide/ref.html#withschema)

[alias](https://knexjs.org/guide/ref.html#alias)

[Utility -------](https://knexjs.org/guide/utility.html)

[batchInsert](https://knexjs.org/guide/utility.html#batchinsert)

[now](https://knexjs.org/guide/utility.html#now)

[uuid](https://knexjs.org/guide/utility.html#uuid)

[uuidToBin](https://knexjs.org/guide/utility.html#uuidtobin)

[binToUuid](https://knexjs.org/guide/utility.html#bintouuid)

[Interfaces ----------](https://knexjs.org/guide/interfaces.html)

[### Promises](https://knexjs.org/guide/interfaces.html#promises)

[then](https://knexjs.org/guide/interfaces.html#then)

[catch](https://knexjs.org/guide/interfaces.html#catch)

[### Callbacks](https://knexjs.org/guide/interfaces.html#callbacks)

[asCallback](https://knexjs.org/guide/interfaces.html#ascallback)

[### Streams](https://knexjs.org/guide/interfaces.html#streams)

[stream](https://knexjs.org/guide/interfaces.html#stream)

[pipe](https://knexjs.org/guide/interfaces.html#pipe)

[### Events](https://knexjs.org/guide/interfaces.html#events)

[query](https://knexjs.org/guide/interfaces.html#query)

[query-error](https://knexjs.org/guide/interfaces.html#query-error)

[query-response](https://knexjs.org/guide/interfaces.html#query-response)

[start](https://knexjs.org/guide/interfaces.html#start)

[### Other](https://knexjs.org/guide/interfaces.html#other)

[toString](https://knexjs.org/guide/interfaces.html#tostring)

[toSQL](https://knexjs.org/guide/interfaces.html#tosql)

[Migrations ----------](https://knexjs.org/guide/migrations.html)

[Migration CLI](https://knexjs.org/guide/migrations.html#migration-cli)

[### Seed files](https://knexjs.org/guide/migrations.html#seed-files)

[Seed CLI](https://knexjs.org/guide/migrations.html#seed-cli)

[### knexfile.js](https://knexjs.org/guide/migrations.html#knexfile-js)

[Basic configuration](https://knexjs.org/guide/migrations.html#basic-configuration)

[Environment configuration](https://knexjs.org/guide/migrations.html#environment-configuration)

[Custom migration](https://knexjs.org/guide/migrations.html#custom-migration)

[Custom migration name](https://knexjs.org/guide/migrations.html#custom-migration-name)

[Generated migration extension](https://knexjs.org/guide/migrations.html#generated-migration-extension)

[Knexfile in other languages](https://knexjs.org/guide/migrations.html#knexfile-in-other-languages)

[### Migration API](https://knexjs.org/guide/migrations.html#migration-api)

[Transactions in migrations](https://knexjs.org/guide/migrations.html#transactions-in-migrations)

[make](https://knexjs.org/guide/migrations.html#make)

[latest](https://knexjs.org/guide/migrations.html#latest)

[rollback](https://knexjs.org/guide/migrations.html#rollback)

[up](https://knexjs.org/guide/migrations.html#up)

[down](https://knexjs.org/guide/migrations.html#down)

[currentVersion](https://knexjs.org/guide/migrations.html#currentversion)

[list](https://knexjs.org/guide/migrations.html#list)

[unlock](https://knexjs.org/guide/migrations.html#unlock)

[Notes about locks](https://knexjs.org/guide/migrations.html#notes-about-locks)

[### Custom migration sources](https://knexjs.org/guide/migrations.html#custom-migration-sources)

[Webpack migration source example](https://knexjs.org/guide/migrations.html#webpack-migration-source-example)

[ECMAScript modules (ESM) Interoperability](https://knexjs.org/guide/migrations.html#ecmascript-modules-esm-interoperability)

[### Seed API](https://knexjs.org/guide/migrations.html#seed-api)

[make](https://knexjs.org/guide/migrations.html#make-1)

[run](https://knexjs.org/guide/migrations.html#run)

[Custom seed sources](https://knexjs.org/guide/migrations.html#custom-seed-sources)

[Extending](https://knexjs.org/guide/extending.html)

On this page

Transactions [​](https://knexjs.org/guide/transactions.html#transactions)
=========================================================================

Transactions are an important feature of relational databases, as they allow correct recovery from failures and keep a database consistent even in cases of system failure. All queries within a transaction are executed on the same database connection, and run the entire set of queries as a single unit of work. Any failure will mean the database will rollback any queries executed on that connection to the pre-transaction state.

Transactions are handled by passing a handler function into `knex.transaction`. The handler function accepts a single argument, an object which may be used in two ways:

1. As the "promise aware" knex connection
2. As an object passed into a query with [transacting](https://knexjs.org/guide/query-builder.html#transacting) and eventually call commit or rollback.

Consider these two examples:

js

```
// Using trx as a query builder:
knex
  .transaction(function (trx) {
    const books = [
      { title: 'Canterbury Tales' },
      { title: 'Moby Dick' },
      { title: 'Hamlet' },
    ];

    return trx
      .insert({ name: 'Old Books' }, 'id')
      .into('catalogues')
      .then(function (ids) {
        books.forEach((book) => (book.catalogue_id = ids[0]));
        return trx('books').insert(books);
      });
  })
  .then(function (inserts) {
    console.log(inserts.length + ' new books saved.');
  })
  .catch(function (error) {
    // If we get here, that means that
    // neither the 'Old Books' catalogues insert,
    // nor any of the books inserts will have taken place.
    console.error(error);
  });
```

And then this example:

js

```
// Using trx as a transaction object:
knex
  .transaction(function (trx) {
    const books = [
      { title: 'Canterbury Tales' },
      { title: 'Moby Dick' },
      { title: 'Hamlet' },
    ];

    knex
      .insert({ name: 'Old Books' }, 'id')
      .into('catalogues')
      .transacting(trx)
      .then(function (ids) {
        books.forEach((book) => (book.catalogue_id = ids[0]));
        return knex('books').insert(books).transacting(trx);
      })
      .then(trx.commit)
      .catch(trx.rollback);
  })
  .then(function (inserts) {
    console.log(inserts.length + ' new books saved.');
  })
  .catch(function (error) {
    // If we get here, that means that
    // neither the 'Old Books' catalogues insert,
    // nor any of the books inserts will have taken place.
    console.error(error);
  });
```

Same example as above using await/async:

ts

```
try {
  await knex.transaction(async (trx) => {
    const books = [
      { title: 'Canterbury Tales' },
      { title: 'Moby Dick' },
      { title: 'Hamlet' },
    ];

    const ids = await trx('catalogues').insert(
      {
        name: 'Old Books',
      },
      'id'
    );

    books.forEach((book) => (book.catalogue_id = ids[0]));
    const inserts = await trx('books').insert(books);

    console.log(inserts.length + ' new books saved.');
  });
} catch (error) {
  // If we get here, that means that neither the 'Old Books' catalogues insert,
  // nor any of the books inserts will have taken place.
  console.error(error);
}
```

Same example as above using another await/async approach:

ts

```
try {
  await knex.transaction(async (trx) => {
    const books = [
      { title: 'Canterbury Tales' },
      { title: 'Moby Dick' },
      { title: 'Hamlet' },
    ];

    const ids = await knex('catalogues')
      .insert(
        {
          name: 'Old Books',
        },
        'id'
      )
      .transacting(trx);

    books.forEach((book) => (book.catalogue_id = ids[0]));
    await knex('books').insert(books).transacting(trx);

    console.log(inserts.length + ' new books saved.');
  });
} catch (error) {
  console.error(error);
}
```

Throwing an error directly from the transaction handler function automatically rolls back the transaction, same as returning a rejected promise.

Notice that if the handler does not return a promise, it is up to you to ensure `trx.commit`, or `trx.rollback` are called, otherwise the transaction connection will hang. If the handler does not return a promise, `knex.transaction` will return the transaction `trx`.

Calling `trx.rollback` will return a rejected Promise. If you don't pass any argument to `trx.rollback`, a generic `Error` object will be created and passed in to ensure the Promise always rejects with something.

Note that Amazon Redshift does not support savepoints in transactions.

In some cases you may prefer to create transaction but only execute statements in it later. In such case call method `transaction` without a handler function:

ts

```
// Using trx as a transaction object:
const trx = await knex.transaction();

const books = [
  { title: 'Canterbury Tales' },
  { title: 'Moby Dick' },
  { title: 'Hamlet' },
];

trx('catalogues')
  .insert({ name: 'Old Books' }, 'id')
  .then(function (ids) {
    books.forEach((book) => (book.catalogue_id = ids[0]));
    return trx('books').insert(books);
  })
  .then(trx.commit)
  .catch(trx.rollback);
```

If you want to create a reusable transaction instance, but do not want to actually start it until it is used, you can create a transaction provider instance. It will start transaction after being called for the first time, and return same transaction on subsequent calls:

ts

```
// Does not start a transaction yet
const trxProvider = knex.transactionProvider();

const books = [
  { title: 'Canterbury Tales' },
  { title: 'Moby Dick' },
  { title: 'Hamlet' },
];

// Starts a transaction
const trx = await trxProvider();
const ids = await trx('catalogues').insert({ name: 'Old Books' }, 'id');
books.forEach((book) => (book.catalogue_id = ids[0]));
await trx('books').insert(books);

// Reuses same transaction
const sameTrx = await trxProvider();
const ids2 = await sameTrx('catalogues').insert({ name: 'New Books' }, 'id');
books.forEach((book) => (book.catalogue_id = ids2[0]));
await sameTrx('books').insert(books);
```

You can access the promise that gets resolved after transaction is rolled back explicitly by user or committed, or rejected if it gets rolled back by DB itself, when using either way of creating transaction, from field `executionPromise`:

ts

```
const trxProvider = knex.transactionProvider();
const trx = await trxProvider();
const trxPromise = trx.executionPromise;

const trx2 = await knex.transaction();
const trx2Promise = trx2.executionPromise;

const trxInitPromise = new Promise(async (resolve, reject) => {
  knex.transaction((transaction) => {
    resolve(transaction);
  });
});
const trx3 = await trxInitPromise;
const trx3Promise = trx3.executionPromise;
```

You can check if a transaction has been committed or rolled back with the method `isCompleted`:

ts

```
const trx = await knex.transaction();
trx.isCompleted(); // false
await trx.commit();
trx.isCompleted(); // true

const trx2 = knex.transactionProvider();
await trx2.rollback();
trx2.isCompleted(); // true
```

You can check the property `knex.isTransaction` to see if the current knex instance you are working with is a transaction.

Transaction Modes [​](https://knexjs.org/guide/transactions.html#transaction-modes)
-----------------------------------------------------------------------------------

In case you need to specify an isolation level for your transaction, you can use a config parameter `isolationLevel`. Not supported by oracle and sqlite, options are `read uncommitted`, `read committed`, `repeatable read`, `snapshot` (mssql only), `serializable`.

ts

```
// Simple read skew example
const isolationLevel = 'read committed';
const trx = await knex.transaction({ isolationLevel });
const result1 = await trx(tableName).select();
await knex(tableName).insert({ id: 1, value: 1 });
const result2 = await trx(tableName).select();
await trx.commit();
// result1 may or may not deep equal result2 depending on isolation level
```

You may also set the transaction mode as `read only` using the `readOnly` config parameter. It is currently only supported on mysql, postgres, and redshift.

ts

```
const trx = await knex.transaction({ readOnly: true });
// 💥 Cannot `INSERT` while inside a `READ ONLY` transaction
const result = await trx(tableName).insert({ id: 1, foo: 'bar' });
```

[Edit this page on GitHub](https://github.com/knex/knex/edit/master/docs/src/guide/transactions.md)

Last Updated:

Pager

[Previous page Query Builder](https://knexjs.org/guide/query-builder.html)

[Next page Schema Builder](https://knexjs.org/guide/schema-builder.html)

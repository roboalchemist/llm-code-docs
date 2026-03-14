# Source: https://knexjs.org/guide/interfaces.html

Title: Interfaces | Knex.js

URL Source: https://knexjs.org/guide/interfaces.html

Markdown Content:
Interfaces | Knex.js
===============

[Skip to content](https://knexjs.org/guide/interfaces.html#VPContent)

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

Interfaces [​](https://knexjs.org/guide/interfaces.html#interfaces)
===================================================================

Knex.js provides several options to deal with query output. The following methods are present on the query builder, schema builder, and the raw builder:

Promises [​](https://knexjs.org/guide/interfaces.html#promises)
---------------------------------------------------------------

[Promises](https://github.com/petkaantonov/bluebird#what-are-promises-and-why-should-i-use-them) are the preferred way of dealing with queries in knex, as they allow you to return values from a fulfillment handler, which in turn become the value of the promise. The main benefit of promises are the ability to catch thrown errors without crashing the node app, making your code behave like a **.try / .catch / .finally** in synchronous code.

js

```
knex
  .select('name')
  .from('users')
  .where('id', '>', 20)
  .andWhere('id', '<', 200)
  .limit(10)
  .offset(x)
  .then(function (rows) {
    return _.pluck(rows, 'name');
  })
  .then(function (names) {
    return knex.select('id').from('nicknames').whereIn('nickname', names);
  })
  .then(function (rows) {
    console.log(rows);
  })
  .catch(function (error) {
    console.error(error);
  });
```

### then [​](https://knexjs.org/guide/interfaces.html#then)

**.then(onFulfilled, [onRejected])**

Coerces the current query builder chain into a promise state, accepting the resolve and reject handlers as specified by the Promises/A+ spec. As stated in the spec, more than one call to the then method for the current query chain will resolve with the same value, in the order they were called; the query will not be executed multiple times.

js

```
knex
  .select('*')
  .from('users')
  .where({ name: 'Tim' })
  .then(function (rows) {
    return knex
      .insert({ user_id: rows[0].id, name: 'Test' }, 'id')
      .into('accounts');
  })
  .then(function (id) {
    console.log('Inserted Account ' + id);
  })
  .catch(function (error) {
    console.error(error);
  });
```

### catch [​](https://knexjs.org/guide/interfaces.html#catch)

**.catch(onRejected)**

Coerces the current query builder into a promise state, catching any error thrown by the query, the same as calling .then(null, onRejected).

js

```
return knex
  .insert({ id: 1, name: 'Test' }, 'id')
  .into('accounts')
  .catch(function (error) {
    console.error(error);
  })
  .then(function () {
    return knex.select('*').from('accounts').where('id', 1);
  })
  .then(function (rows) {
    console.log(rows[0]);
  })
  .catch(function (error) {
    console.error(error);
  });
```

Callbacks [​](https://knexjs.org/guide/interfaces.html#callbacks)
-----------------------------------------------------------------

### asCallback [​](https://knexjs.org/guide/interfaces.html#ascallback)

**.asCallback(callback)**

If you'd prefer a callback interface over promises, the asCallback function accepts a standard node style callback for executing the query chain. Note that as with the then method, subsequent calls to the same query chain will return the same result.

js

```
knex
  .select('name')
  .from('users')
  .where('id', '>', 20)
  .andWhere('id', '<', 200)
  .limit(10)
  .offset(x)
  .asCallback(function (err, rows) {
    if (err) return console.error(err);
    knex
      .select('id')
      .from('nicknames')
      .whereIn('nickname', _.pluck(rows, 'name'))
      .asCallback(function (err, rows) {
        if (err) return console.error(err);
        console.log(rows);
      });
  });
```

Streams [​](https://knexjs.org/guide/interfaces.html#streams)
-------------------------------------------------------------

Streams are a powerful way of piping data through as it comes in, rather than all at once. You can read more about streams [here at substack's stream handbook](https://github.com/substack/stream-handbook). See the following for example uses of stream & pipe. If you wish to use streams with PostgreSQL, you must also install the [pg-query-stream](https://github.com/brianc/node-postgres/tree/master/packages/pg-query-stream) module. If you wish to use streams with the `pgnative` dialect, please be aware that the results will not be streamed as they are received, but rather streamed after the entire result set has returned. On an HTTP server, make sure to [manually close your streams](https://github.com/knex/knex/wiki/Manually-Closing-Streams) if a request is aborted.

### stream [​](https://knexjs.org/guide/interfaces.html#stream)

**.stream([options], [callback])**

If called with a callback, the callback is passed the stream and a promise is returned. Otherwise, the readable stream is returned.

 When the stream is consumed as an [iterator](https://nodejs.org/api/stream.html#readablesymbolasynciterator), if the loop terminates with a `break`, `return`, or a `throw`, the stream will be destroyed. In other terms, iterating over a stream will consume the stream fully.

js

```
// Retrieve the stream:
const stream = knex.select('*').from('users').stream();
stream.pipe(writableStream);
```

js

```
// With options:
const stream = knex.select('*').from('users').stream({ highWaterMark: 5 });
stream.pipe(writableStream);
```

js

```
// Use as an iterator
const stream = knex.select('*').from('users').stream();

for await (const row of stream) {
  /* ... */
}
```

js

```
// Use as a promise:
const stream = knex
  .select('*')
  .from('users')
  .where(knex.raw('id = ?', [1]))
  .stream(function (stream) {
    stream.pipe(writableStream);
  })
  .then(function () {
    /* ... */
  })
  .catch(function (e) {
    console.error(e);
  });
```

### pipe [​](https://knexjs.org/guide/interfaces.html#pipe)

**.pipe(writableStream)**

Pipe a stream for the current query to a writableStream.

js`const stream = knex.select('*').from('users').pipe(writableStream);`

Events [​](https://knexjs.org/guide/interfaces.html#events)
-----------------------------------------------------------

### query [​](https://knexjs.org/guide/interfaces.html#query)

A query event is fired just before a query takes place, providing data about the query, including the connection's `__knexUid` / `__knexTxId` properties and any other information about the query as described in toSQL. Useful for logging all queries throughout your application.

js

```
knex
  .select('*')
  .from('users')
  .on('query', function (data) {
    app.log(data);
  })
  .then(function () {
    // ...
  });
```

### query-error [​](https://knexjs.org/guide/interfaces.html#query-error)

A query-error event is fired when an error occurs when running a query, providing the error object and data about the query, including the connection's `__knexUid` / `__knexTxId` properties and any other information about the query as described in toSQL. Useful for logging all query errors throughout your application.

js

```
knex
  .select(['NonExistentColumn'])
  .from('users')
  .on('query-error', function (error, obj) {
    app.log(error);
  })
  .then(function () {
    /* ... */
  })
  .catch(function (error) {
    // Same error object as the query-error event provides.
  });
```

### query-response [​](https://knexjs.org/guide/interfaces.html#query-response)

A query-response event is fired when a successful query has been run, providing the response of the query and data about the query, including the connection's `__knexUid` / `__knexTxId` properties and any other information about the query as described in toSQL, and finally the query builder used for the query.

js

```
knex
  .select('*')
  .from('users')
  .on('query-response', function (response, obj, builder) {
    // ...
  })
  .then(function (response) {
    // Same response as the emitted event
  })
  .catch(function (error) {});
```

### start [​](https://knexjs.org/guide/interfaces.html#start)

A `start` event is fired right before a query-builder is compiled.

INFO

While this event can be used to alter a builders state prior to compilation it is not to be recommended. Future goals include ways of doing this in a different manner such as hooks.

js

```
knex
  .select('*')
  .from('users')
  .on('start', function (builder) {
    builder.where('IsPrivate', 0);
  })
  .then(function (Rows) {
    //Only contains Rows where IsPrivate = 0
  })
  .catch(function (error) {});
```

Other [​](https://knexjs.org/guide/interfaces.html#other)
---------------------------------------------------------

### toString [​](https://knexjs.org/guide/interfaces.html#tostring)

**.toString()**

Returns an array of query strings filled out with the correct values based on bindings, etc. Useful for debugging, but should not be used to create queries for running them against DB.

js

```
const toStringQuery = knex.select('*').from('users').where('id', 1).toString();

// Outputs: console.log(toStringQuery);
// select * from "users" where "id" = 1
```

### toSQL [​](https://knexjs.org/guide/interfaces.html#tosql)

**.toSQL()**

**.toSQL().toNative()**

Returns an array of query strings filled out with the correct values based on bindings, etc. Useful for debugging and building queries for running them manually with DB driver. `.toSQL().toNative()` outputs object with sql string and bindings in a dialects format in the same way that knex internally sends them to underlying DB driver.

js

```
knex
  .select('*')
  .from('users')
  .where(knex.raw('id = ?', [1]))
  .toSQL();
// Outputs:
// {
//   bindings: [1],
//   method: 'select',
//   sql: 'select * from "users" where id = ?',
//   options: undefined,
//   toNative: function () {}
// }

knex
  .select('*')
  .from('users')
  .where(knex.raw('id = ?', [1]))
  .toSQL()
  .toNative();
// Outputs for postgresql dialect:
// {
//   bindings: [1],
//   sql: 'select * from "users" where id = $1',
// }
```

[Edit this page on GitHub](https://github.com/knex/knex/edit/master/docs/src/guide/interfaces.md)

Last Updated:

Pager

[Previous page Utility](https://knexjs.org/guide/utility.html)

[Next page Migrations](https://knexjs.org/guide/migrations.html)

# Source: https://pub.dev/documentation/isar/latest/

Title: isar - Dart API docs

URL Source: https://pub.dev/documentation/isar/latest/

Markdown Content:
[![Image 1](https://raw.githubusercontent.com/isar/isar/main/.github/assets/isar.svg?sanitize=true)](https://isar.dev/)

Isar Database
-------------

[![Image 2](https://img.shields.io/pub/v/isar?label=pub.dev&labelColor=333940&logo=dart)](https://pub.dev/packages/isar)[![Image 3](https://img.shields.io/github/actions/workflow/status/isar/isar/test.yaml?branch=main&label=tests&labelColor=333940&logo=github)](https://github.com/isar/isar/actions/workflows/test.yaml)[![Image 4](https://img.shields.io/codecov/c/github/isar/isar?logo=codecov&logoColor=fff&labelColor=333940)](https://app.codecov.io/gh/isar/isar)[![Image 5](https://img.shields.io/static/v1?label=join&message=isardb&labelColor=333940&logo=telegram&logoColor=white&color=229ED9)](https://t.me/isardb)[![Image 6](https://img.shields.io/twitter/follow/simcdev?style=social)](https://twitter.com/simonleier)

[Quickstart](https://isar.dev/) • [Documentation](https://isar.dev/schema) • [Sample Apps](https://github.com/isar/isar/tree/main/examples/) • [Support & Ideas](https://github.com/isar/isar/discussions) • [Pub.dev](https://pub.dev/packages/isar)

> #### Isar `ee-zahr`:
> 
> 
> 1.   River in Bavaria, Germany.
> 2.   [Crazy fast](https://pub.dev/documentation/isar/latest/#benchmarks) NoSQL database that is a joy to use.

Features
--------

*   💙 **Made for Flutter**. Easy to use, no config, no boilerplate
*   🚀 **Highly scalable** The sky is the limit (pun intended)
*   🍭 **Feature rich**. Composite & multi-entry indexes, query modifiers, JSON support etc.
*   ⏱ **Asynchronous**. Parallel query operations & multi-isolate support by default
*   🦄 **Open source**. Everything is open source and free forever!

Isar database can do much more (and we are just getting started)

*   🕵️ **Full-text search**. Make searching fast and fun
*   📱 **Multiplatform**. iOS, Android, Desktop
*   🧪 **ACID semantics**. Rely on database consistency
*   💃 **Static typing**. Compile-time checked and autocompleted queries
*   ✨ **Beautiful documentation**. Readable, easy to understand and ever-improving

Join the [Telegram group](https://t.me/isardb) for discussion and sneak peeks of new versions of the DB.

If you want to say thank you, star us on GitHub and like us on pub.dev 🙌💙

Quickstart
----------

Holy smokes you're here! Let's get started on using the coolest Flutter database out there...

### 1. Add to pubspec.yaml

```
isar_version: &isar_version 3.1.0 # define the version to be used

dependencies:
  isar: *isar_version
  isar_flutter_libs: *isar_version # contains Isar Core

dev_dependencies:
  isar_generator: *isar_version
  build_runner: any
```

### 2. Annotate a Collection

```
part 'email.g.dart';

@collection
class Email {
  Id id = Isar.autoIncrement; // you can also use id = null to auto increment

  @Index(type: IndexType.value)
  String? title;

  List<Recipient>? recipients;

  @enumerated
  Status status = Status.pending;
}

@embedded
class Recipient {
  String? name;

  String? address;
}

enum Status {
  draft,
  pending,
  sent,
}
```

### 3. Open a database instance

```
final dir = await getApplicationDocumentsDirectory();
final isar = await Isar.open(
  [EmailSchema],
  directory: dir.path,
);
```

### 4. Query the database

```
final emails = await isar.emails.filter()
  .titleContains('awesome', caseSensitive: false)
  .sortByStatusDesc()
  .limit(10)
  .findAll();
```

Isar Database Inspector
-----------------------

The Isar Inspector allows you to inspect the Isar instances & collections of your app in real-time. You can execute queries, edit properties, switch between instances and sort the data.

![Image 7](https://raw.githubusercontent.com/isar/isar/main/.github/assets/inspector.gif)

To launch the inspector, just run your Isar app in debug mode and open the Inspector link in the logs.

CRUD operations
---------------

All basic crud operations are available via the `IsarCollection`.

```
final newEmail = Email()..title = 'Amazing new database';

await isar.writeTxn(() {
  await isar.emails.put(newEmail); // insert & update
});

final existingEmail = await isar.emails.get(newEmail.id!); // get

await isar.writeTxn(() {
  await isar.emails.delete(existingEmail.id!); // delete
});
```

Database Queries
----------------

Isar database has a powerful query language that allows you to make use of your indexes, filter distinct objects, use complex `and()`, `or()` and `.xor()` groups, query links and sort the results.

```
final importantEmails = isar.emails
  .where()
  .titleStartsWith('Important') // use index
  .limit(10)
  .findAll()

final specificEmails = isar.emails
  .filter()
  .recipient((q) => q.nameEqualTo('David')) // query embedded objects
  .or()
  .titleMatches('*university*', caseSensitive: false) // title containing 'university' (case insensitive)
  .findAll()
```

Database Watchers
-----------------

With Isar database, you can watch collections, objects, or queries. A watcher is notified after a transaction commits successfully and the target actually changes. Watchers can be lazy and not reload the data or they can be non-lazy and fetch new results in the background.

```
Stream<void> collectionStream = isar.emails.watchLazy();

Stream<List<Post>> queryStream = importantEmails.watch();

queryStream.listen((newResult) {
  // do UI updates
})
```

Benchmarks
----------

Benchmarks only give a rough idea of the performance of a database but as you can see, Isar NoSQL database is quite fast 😇

| ![Image 8](https://raw.githubusercontent.com/isar/isar/main/.github/assets/benchmarks/insert.png) | ![Image 9](https://raw.githubusercontent.com/isar/isar/main/.github/assets/benchmarks/query.png) |
| --- | --- |
| ![Image 10](https://raw.githubusercontent.com/isar/isar/main/.github/assets/benchmarks/delete.png) | ![Image 11](https://raw.githubusercontent.com/isar/isar/main/.github/assets/benchmarks/size.png) |

If you are interested in more benchmarks or want to check how Isar performs on your device you can run the [benchmarks](https://github.com/isar/isar_benchmark) yourself.

Unit tests
----------

If you want to use Isar database in unit tests or Dart code, call `await Isar.initializeIsarCore(download: true)` before using Isar in your tests.

Isar NoSQL database will automatically download the correct binary for your platform. You can also pass a `libraries` map to adjust the download location for each platform.

Make sure to use `flutter test -j 1` to avoid tests running in parallel. This would break the automatic download.

Contributors ✨
--------------

Big thanks go to these wonderful people:

[![Image 12](https://avatars.githubusercontent.com/u/30233189?v=4) **Alexis**](https://github.com/AlexisL61)[![Image 13](https://avatars.githubusercontent.com/u/49204989?v=4) **Burak**](https://github.com/buraktabn)[![Image 14](https://avatars.githubusercontent.com/u/13763473?v=4) **Carlo Loguercio**](https://github.com/CarloDotLog)[![Image 15](https://avatars.githubusercontent.com/u/84601232?v=4) **Frostedfox**](https://github.com/Frostedfox)[![Image 16](https://avatars.githubusercontent.com/u/87476445?v=4) **Hafeez Rana**](https://github.com/hafeezrana)[![Image 17](https://avatars.githubusercontent.com/u/3498335?v=4) **Hamed H.**](https://github.com/h1376h)[![Image 18](https://avatars.githubusercontent.com/u/32107801?v=4) **JT**](https://github.com/Jtplouffe)
[![Image 19](https://avatars.githubusercontent.com/u/111809?v=4) **Jack Rivers**](https://github.com/ritksm)[![Image 20](https://avatars.githubusercontent.com/u/43643339?v=4) **Joachim Nohl**](https://github.com/nohli)[![Image 21](https://avatars.githubusercontent.com/u/20894472?v=4) **Johnson**](https://github.com/vothvovo)[![Image 22](https://avatars.githubusercontent.com/u/55886143?v=4) **LaLucid**](https://github.com/VoidxHoshi)[![Image 23](https://avatars.githubusercontent.com/u/16468579?v=4) **Lety**](https://github.com/letyletylety)[![Image 24](https://avatars.githubusercontent.com/u/8101584?v=4) **Michael**](https://github.com/lodisy)[![Image 25](https://avatars.githubusercontent.com/u/10720298?v=4) **Moseco**](https://github.com/Moseco)
[![Image 26](https://avatars.githubusercontent.com/u/57417802?v=4) **Nelson Mutane**](https://github.com/inkomomutane)[![Image 27](https://avatars.githubusercontent.com/u/24822764?v=4) **Peyman**](https://github.com/Viper-Bit)[![Image 28](https://avatars.githubusercontent.com/u/13610195?v=4) **Simon Leier**](https://github.com/leisim)[![Image 29](https://avatars.githubusercontent.com/u/42883378?v=4) **Ura**](https://github.com/ika020202)[![Image 30](https://avatars.githubusercontent.com/u/32213113?v=4) **blendthink**](https://github.com/blendthink)[![Image 31](https://avatars.githubusercontent.com/u/41247357?v=4) **mnkeis**](https://github.com/mnkeis)[![Image 32](https://avatars.githubusercontent.com/u/44443899?v=4) **nobkd**](https://github.com/nobkd)

### License

```
Copyright 2022 Simon Leier

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

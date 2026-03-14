# Source: https://pub.dev/documentation/fluent_design_system/latest/

Title: fluent_design_system - Dart API docs

URL Source: https://pub.dev/documentation/fluent_design_system/latest/

Markdown Content:
Fluent Design System for Flutter
--------------------------------

A design system for Flutter, inspired by Fluent Design. This package provides a collection of reusable widgets, color schemes, typography, and styles that follow the Fluent Design guidelines. It aims to make it easier for developers to create beautiful and consistent user interfaces that feel native to the platform.

Getting started
---------------

To use this package, add `fluent_design_system` as a dependency in your `pubspec.yaml` file. For example:

```
dependencies:
  fluent_design_system: ^1.0.0
```

Then, run flutter packages get to install the package.

Usage To use the widgets, colors, typography, or styles provided by this package, import the package in your Dart code. For example:

```
import 'package:fluent_design_system/fluent.dart';
import 'package:flutter/material.dart';
import 'package:fluent_design_system/design_system.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: FluentDesignSystem.themeData,
      home: const MyHomePage(title: 'Flutter Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: kHeadingTextStyle,
            ),
          ],
        ),
      ),
      floatingActionButton: PrimaryButton(
        onPressed: _incrementCounter,
        tooltip: 'Click increment button',
        label: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
```

For more information on how to use this package, please refer to the API documentation and examples.

API documentation The API documentation for this package can be found at pub.dev.

Examples The example folder in this package contains a sample app that demonstrates how to use the widgets and styles provided by this package. You can run the app using flutter run in the root of the package.

Contributions Contributions to this package are welcome! If you find a bug or want to suggest a new feature, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and submit a pull request

License This package is licensed under the MIT License. See the LICENSE file for more information.

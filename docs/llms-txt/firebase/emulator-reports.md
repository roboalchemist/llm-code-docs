# Source: https://firebase.google.com/docs/rules/emulator-reports.md.txt

<br />

Cloud FirestoreandRealtime Databaseboth rely on powerful, concise rules languages specifically created to govern information security and access control. However, as rules get longer and more complex, you might need some help debugging errors in their behavior.

The Firebase Emulators include the ability to generate rule coverage reports, so you can see see exactly what each subexpression evaluated to when you reproduce an error. The reports also provide information about how frequently each test case used a rule, like traditional "line coverage" techniques.

## Generate a report

After running a suite of tests, you can access test coverage reports that show how each of your security rules was evaluated.

To get the reports, query an exposed endpoint on the emulator while it's running. For a browser-friendly version, use the following URL:  

### Cloud Firestore

```scdoc
http://localhost:8080/emulator/v1/projects/<database_name>:ruleCoverage.html
 
```

### Realtime Database

```scdoc
http://localhost:9000/.inspect/coverage?ns=<database_name>
 
```

This breaks your rules into expressions and subexpressions that you can mouseover for more information, including number of evaluations and values returned. For the raw JSON version of this data, include the following URL in your query:  

### Cloud Firestore

```scdoc
http://localhost:8080/emulator/v1/projects/<database_name>:ruleCoverage
 
```

### Realtime Database

```scdoc
http://localhost:9000/.inspect/coverage.json?ns=<database_name>
 
```

## Debugging example rules

To easily generate a test report, use the emulator quickstarts available on GitHub for[Cloud Firestore](https://github.com/firebase/quickstart-testing/)and[Realtime Database](https://github.com/firebase/quickstart-testing/). These quickstarts guide you through properly installing and initializing the emulators, then generating sample tests from an example set of rules.

Consider an example app usingCloud Firestorethat counts how many times users click a button. The app employs the following rules:  

### Cloud Firestore

```css+lasso
 service cloud.firestore {
   match /databases/{database}/documents {
     match /counters/{counter} {
       allow read;
       allow write: if request.resource.data.value == resource.data.value +1;
     }
   }
 }
 
```

To debug the errors in the rules shown above, use the following sample JavaScript test:  

    const counter0 = db.collection("counters").doc("0");
    await firebase.assertSucceeds(counter0.set({value: 0}));

The emulator generates a report available at the URL noted above:  

```scdoc
http://localhost:8080/emulator/v1/projects/<database_name>:ruleCoverage.html
```

The report shows the following undefined and null-value errors:

![](https://firebase.google.com/static/docs/rules/images/rules-report-broken.png)

The problem with this specific example is that the rules don't differentiate between creating the document and updating the document. Consequently, the write isn't allowed if the document doesn't exist, and the document can't be created because it doesn't exist. Differentiating the "write" into two more specific operations --- "create" and "update" --- solves the problem.  

### Cloud Firestore

```css+lasso
 service cloud.firestore {
   match /databases/{database}/documents {
     match /counters/{counter} {
       allow read;
       allow create: if request.resource.data.value == 0;
       allow update: if request.resource.data.value == resource.data.value +1;
     }
   }
 }
 
```

The generated report shows how frequently each rule was used and what was returned.

![](https://firebase.google.com/static/docs/rules/images/rules-report-fixed.png)
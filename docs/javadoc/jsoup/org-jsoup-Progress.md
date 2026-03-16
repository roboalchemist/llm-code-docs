Package org.jsoup

# Interface Progress<ProgressContext>

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

@FunctionalInterface
public interface Progress<ProgressContext>

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`onProgress(int processed,
 int total,
 float percent,
 ProgressContext context)`

Called to report progress.

- 

## Method Details

  - 

### onProgress

void onProgress(int processed,
 int total,
 float percent,
 ProgressContext context)
Called to report progress. Note that this will be executed by the same thread that is doing the work, so either
     don't take to long, or hand it off to another thread.

Parameters:
`processed` - the number of bytes processed so far.
`total` - the total number of expected bytes, or -1 if unknown.
`percent` - the percentage of completion, 0.0..100.0. If the expected total is unknown, % will remain at zero
     until complete.
`context` - the object that progress was made on.
Since:
1.18.1
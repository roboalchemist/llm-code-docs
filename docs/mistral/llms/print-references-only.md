# Print references only
if refs_used:
    print("\n\nSources:")
    for i, ref in enumerate(set(refs_used), 1):
        reference = json.loads(result)[str(ref)]
        print(f"\n{i}. {reference['title']}: {reference['url']}")
```

Output:
```
The Nobel Peace Prize for 2024 was awarded to the Japan Confederation of A- and H-Bomb Sufferers Organizations (Nihon Hidankyo) for their activism against nuclear weapons, including efforts by survivors of the atomic bombings of Hiroshima and Nagasaki.

Sources:

1. 2024 Nobel Peace Prize: https://en.wikipedia.org/wiki/2024_Nobel_Peace_Prize
```
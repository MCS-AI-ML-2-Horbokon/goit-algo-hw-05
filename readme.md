## Порівняння алгоритмів пошуку підстроки

Цей проєкт порівнює швидкодію деяких алгоритмів пошуку.

Для порівняння використовувалися наступні алгоритми:
- `knuth_search` алгоритм Кнута-Морріса-Пратта
- `boyer_search` алгоритм Боєра-Мура
- `rabin_search` алгоритм Рабіна-Карпа:
   - `rabin_search_polynomial` зі стандартною поліноміальною функцією з конспекту
   - `rabin_search_naive` зі наївною функцією, просто сума всіх кодів
   
### Результати виконання програми

```py
========== Article 1 ==========

===== GOOD =====
knuth_search completed search in 1318.00 ms, result: 11002
boyer_search completed search in 88.60 ms, result: 11002
rabin_search_polynomial completed search in 28544.50 ms, result: 11002
rabin_search_naive completed search in 1792.20 ms, result: 11002

===== BAD ======
knuth_search completed search in 831.20 ms, result: None
boyer_search completed search in 60.90 ms, result: None
rabin_search_polynomial completed search in 32675.40 ms, result: None
rabin_search_naive completed search in 1392.50 ms, result: None

========== Article 2 ==========

===== GOOD =====
knuth_search completed search in 1091.70 ms, result: 16791
boyer_search completed search in 41.40 ms, result: 16791
rabin_search_polynomial completed search in 7783.40 ms, result: 16791
rabin_search_naive completed search in 1927.00 ms, result: 16791

===== BAD ======
knuth_search completed search in 884.30 ms, result: None
boyer_search completed search in 42.40 ms, result: None
rabin_search_polynomial completed search in 6796.40 ms, result: None
rabin_search_naive completed search in 1885.90 ms, result: None
```

### Висновки

Як можна бачити на даних тестах алгоритм Боєра-Мура виявився найшвидшим в 10-20 разів швидше за алгоритм Кнута-Морріса-Пратта. \
Найповільнішим виявився алгоритм Рабіна-Карпа. \
Спробувавши замінити хеш-функцію на більш просту, можна виявити, що він стає значно швидше, в 3-15 разів, не дивлячись на зрозстаючу кількість коллізій!

Для простих ітеративних алгоритмів алгоритм Боєра-Мура є найшвидшим. \
Для алгоритму Рабіна-Карпа не має сенсу використувавати повільну реалізацію хеш-функції на Python, \
має сенс у майбутньому перевірити це на мові програмування, де математичні операції виконуються значно швидше.

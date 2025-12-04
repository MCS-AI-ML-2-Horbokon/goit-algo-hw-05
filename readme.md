## Порівняння алгоритмів пошуку підстроки

Цей проєкт порівнює швидкодію деяких алгоритмів пошуку.

Для порівняння використовувалися наступні алгоритми:
- `knuth_search` алгоритм Кнута-Морріса-Пратта
- `boyer_search` алгоритм Боєра-Мура
- `rabin_search` алгоритм Рабіна-Карпа

### Результати виконання програми

```py
========== Article 1 ==========

===== GOOD =====
knuth_search completed search in 1058.90 ms, result: 11002
boyer_search completed search in 96.90 ms, result: 11002
rabin_search completed search in 1105.20 ms, result: 11002

===== BAD ======
knuth_search completed search in 855.20 ms, result: None
boyer_search completed search in 60.70 ms, result: None
rabin_search completed search in 1192.50 ms, result: None # 3 collisions

========== Article 2 ==========

===== GOOD =====
knuth_search completed search in 877.90 ms, result: 16791
boyer_search completed search in 45.60 ms, result: 16791
rabin_search completed search in 1701.30 ms, result: 16791

===== BAD ======
knuth_search completed search in 915.90 ms, result: None
boyer_search completed search in 43.20 ms, result: None
rabin_search completed search in 1776.00 ms, result: None # 1 collision
```

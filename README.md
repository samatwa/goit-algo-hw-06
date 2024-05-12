# goit-algo-hw-06

## Висновки до Завдання 3:

# Порівняння алгоритмів DFS та BFS для пошуку шляхів в графі

1. **DFS** (Depth-First Search) та **BFS** (Breadth-First Search) - це два основних алгоритми пошуку в графах. 
2. Обидва алгоритми відвідали всі вершини графа. Однак їх порядок відвідування різний:
   - DFS: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
   - BFS: ['A', 'B', 'D', 'C', 'E', 'G', 'F']\
   Слід зазначити, що при ітеративній реалізації алгоритму BFS виведення може трошки відрізнятися, на своїх рівнях вузли можуть мінятися місцями, це B із C та E,D,F між собою. Це відбувається, оскільки в нашому графі є цикл, і ми використовуємо вираз $set(graph[vertex]) - visited$ для визначення множини невідвіданих сусідніх вершин. Порядок елементів у вбудованих множинах у Python не гарантований, і це може вплинути на порядок, у якому вершини додаються до черги.
3. Різниця в отриманих шляхах полягає в способі обходу графа: 
   - DFS шукає шлях, спускаючись глибше в граф, перед тим як повернутись і перевірити інші можливі шляхи. Це може призвести до того, що DFS знаходить один з можливих шляхів між двома вершинами, але не завжди знаходить найкоротший шлях. 
   - BFS починає з перевірки всіх сусідніх вершин першої вершини, потім переходить до сусідів цих вершин і так далі. Він знаходить найкоротший шлях між двома вершинами, оскільки обходить всі можливі шляхи за одну ітерацію. 
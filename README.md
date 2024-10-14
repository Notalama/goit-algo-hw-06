# goit-algo-hw-06

# Різниця в отриманих шляхах:

# Алгоритм DFS знаходить шлях: ['Zaliznychnyy', 'Halytskyy', 'Shevchenkivskyy', 'Lychakivskyy', 'Sykhivskyy']

# Алгоритм BFS знаходить шлях: ['Zaliznychnyy', 'Lychakivskyy', 'Sykhivskyy']

# Пояснення:

# DFS (пошук у глибину):  DFS досліджує граф, йдучи "вглиб" по кожній гілці, доки не досягне кінця або цільового вузла. У нашому випадку, DFS спочатку йде від "Zaliznychnyy" до "Halytskyy", потім до "Shevchenkivskyy" і так далі, доки не знайде "Sykhivskyy".

# BFS (пошук у ширину): BFS досліджує граф рівень за рівнем. Спочатку він переглядає всі сусідні вузли від початкового, потім сусідів цих сусідів і так далі.  BFS знаходить найкоротший шлях (за кількістю ребер) від "Zaliznychnyy" до "Sykhivskyy", який проходить через "Lychakivskyy".

# Висновок:

# DFS і BFS - це два різні алгоритми пошуку в графі, які можуть давати різні результати. DFS, як правило, знаходить перший доступний шлях, тоді як BFS знаходить найкоротший шлях.

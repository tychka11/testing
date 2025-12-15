# Звіт до роботи
## Тема: Тестування
### Мета роботи: ознайомитися з тестуванням Python-коду, реалізувати юніт-тести з використанням unittest та PyTest, перевірити покриття коду тестами за допомогою coverage і pytest-cov.

---
## Виконання роботи

## Перевірка assert

1. assert - це перевірка певних тверджень та встановлення працездатності коду. Твердження дозволяють перевірити правильність коду, перевіряючи, чи виконуються певні умови. 
```Python
number = 1
assert number > 0, "число має бути більшим за нуль!"
```
2. Створіть власний крок assert та зробіть тестові превірки при введенні даних з клавіатури. Для цього використайте метод input як показано нижче: 
```Python
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")
```
3. В ООП методи assert найкраще виконувати для перевірки (валідації) правильності вводу аргументів. Для прикладу маємо простий клас в якому здійснюємо валідацію даних перед тим як створювати обєкт. Умовою валідації може бути будь-який вираз Python який повертає значення True/False. 
```Python
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

#a = Figure("трапеція", 12)
#b = Figure("квадрат", 0)
c = Figure("квадрат", 1)
```
4. Виконайте код наведений вище для різних обєктів. Вставте у звіт результат виконання роботи для різної комбінації введених значень при створенні обєкта.
```Python
number = -1
assert number > 0, "число має бути більшим за нуль!"

---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[1], line 2
      1 number = -1
----> 2 assert number > 0, "число має бути більшим за нуль!"

AssertionError: число має бути більшим за нуль!



a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")

---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[4], line 2
      1 a = input("Введіть число: ")
----> 2 assert a.isdigit(), "Потрібно ввести число!"
      3 print(f"введене число: {a}")

AssertionError: Потрібно ввести число!



a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")

введене число: 5

class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

#a = Figure("трапеція", 12)
#b = Figure("квадрат", 0)
a = Figure("трапеція", 12)

---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[11], line 10
      6         self.length = length
      8 #a = Figure("трапеція", 12)
      9 #b = Figure("квадрат", 0)
---> 10 a = Figure("трапеція", 12)

Cell In[11], line 4
      2 def __init__(self, type, length) -> None:
      3     assert length > 0, "Довжина має бути більшою за 0!"
----> 4     assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
      5     self.type = type
      6     self.length = length

AssertionError: Дозволені фігури: квадрат, прямокутник, трикутник
```
5. Перевірки можна організовувати і іншими способами, наприклад з використанням умовного розгалуження. Якщо дані введені невірно, можна викликати клас помилки. 
```Python
class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Анонім"]:
            raise ValueError("Дозволені імена: Богдан, Анонім")
        self.name = name

a = Name("Бодько")
```
6.  Додайте власне імя в перевірку, та спробуйте створити такий обєкт. Додайте ще один аргумент в клас, наприклад хоббі, та здійсніть валідацію чи хоббі є введено (поле не пусте).
```Python
class Name:
    def __init__(self, name, hobby) -> None:
        allowed_names = ["Дмитро", "Анонім"]
        if name not in allowed_names:
            raise ValueError(f"Дозволені імена: {', '.join(allowed_names)}")
        if not hobby:
            raise ValueError("Поле хоббі не може бути порожнім")
        self.name = name
        self.hobby = hobby

a = Name("Дмитро", "Програмування")
print(f"Об'єкт створено: ім'я = {a.name}, хоббі = {a.hobby}")
```

## Юніт тести

1. Створимо простий клас з двома пропертями, та навмисно зробимо помилку в ньому. Для коректної роботи з тестами назвіть файл app.py. Це буди потрібно для імпорту бібліотек (класів). 
```Python
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type # робимо помилку
```
2. Спробуйте застосувати цей клас та створити декілька обєктів, викликати методи пропертіс.
```Python
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type

fig1 = Figure("квадрат", 5)
fig2 = Figure("трикутник", 10)
fig3 = Figure("прямокутник", 7)

print(fig1.get_figure_type, fig1.get_figure_length)
print(fig2.get_figure_type, fig2.get_figure_length)
print(fig3.get_figure_type, fig3.get_figure_length)
```
3. Створимо юніт тести та спробуємо перевірити тестовий клас щоб все працювало правильно. Для цьго у методі setUp з допомогою бібліотеки random створимо обєкт та перевіримо чи правильно працюють методи: 
```Python
import unittest
from random import choice, randint

from app import Figure # назва файлу з нашим класом повинна бути app.py

class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass
    
    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")
    
    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1) # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError


if __name__ == '__main__':
    unittest.main() # unittest.main(verbosity=2) щоб був більш детальний вивід
```
4. Попрактикуйтесь викликати тести з консолі та з Visual Studio Code. Вкажіть які тести виконуються а які провалюються.
```
- test_figure_type - Виконується успішно (змінна figure і get_figure_type збігаються)
- test_figure_lengh - Провалюється через помилку в класі (get_figure_length повертає type замість length)
- test_obj - Виконується успішно (створення об’єкта з недозволеним типом викликає AssertionError)
```
5. Розширте функціонал класу який тестується та створіть юніт тест для перевірки правильності роботи доданого функціоналу.
```Python
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length

    def area(self):
        if self.type == "квадрат":
            return self.length ** 2
        elif self.type == "прямокутник":
            return self.length * (self.length * 2)
        elif self.type == "трикутник":
            return (self.length ** 2) / 2

import unittest
from random import choice, randint

class TestFigureExtended(unittest.TestCase):
    def setUp(self):
        self.figure_type = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure_type, self.length)

    def test_area(self):
        if self.obj.get_figure_type == "квадрат":
            self.assertEqual(self.obj.area(), self.length ** 2)
        elif self.obj.get_figure_type == "прямокутник":
            self.assertEqual(self.obj.area(), self.length * (self.length * 2))
        elif self.obj.get_figure_type == "трикутник":
            self.assertEqual(self.obj.area(), (self.length ** 2) / 2)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
```

## Юніт тести з використання бібліотеки PyTest
1. створюємо простий тест у файл app.py
```Python
def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"
```

2. вкажіть у звіті що вивела програма та чи виконалась функція test_app_triangle.

```
collected 5 items

app.py::TestFigure::test_figure_lengh PASSED      [ 20%] 
app.py::TestFigure::test_figure_type PASSED       [ 40%] 
app.py::TestFigure::test_obj PASSED               [ 60%] 
app.py::test_app_triangle PASSED                  [ 80%] 
app.py::test_get_angles PASSED                    [100%] 

================= 5 passed in 0.04s =================
```

## Візуалізація результатів та покриття коду Coverage (pytest-cov)

1. Для візуалізації результаів не в консолі а через браузер - згенеруйте звіт у форматі html. Відкрийте файл index.html у веб-браузері та дослідіть отриману інформацію. Отриманий файл повинен бути у звіті. 

![Інформація з html файлу](/1.png))

2. За замовчеванням звіт буде показувати всі файли проекту (навіть пусті, і навіть самі тести). Щоб обмежити звіт лише тими файлами які ви хочете, створіть файл .coveragerc з наступним вмістом: 

```Python
[run]
source = app.py

[report]
omit =
    */__init__.py
    */tests/*
    */venv/*
```   

# Висновок:

    ❓ Що зроблено в роботі:
    - Створено класи з валідацією даних та юніт-тести для перевірки їхньої роботи.
    ❓ Чи досягнуто мети роботи:
    - Так, усі тести виконалися успішно і функціонал перевірено.
    ❓ Які нові знання отримано:
    - Навички створення юніт-тестів, використання assert та аналізу покриття коду.
    ❓ Чи вдалось відповісти на всі питання задані в ході роботи:
    - Так, усі питання, що виникали під час виконання завдання, були розібрані та опрацьовані.
    ❓ Чи вдалося виконати всі завдання:
    - Так, всі завдання були виконані повністю.
    ❓ Чи виникли складності у виконанні завдання:
    - Ні, труднощів під час виконання завдання не виникло.
    ❓ Чи подобається такий формат здачі роботи (Feedback):
    - Так, формат зручний, зрозумілий та практичний.
    ❓ Побажання для покращення (Suggestions):
    - Все влаштовує, побажань щодо покращення немає.

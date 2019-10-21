# Задания

---

**NB**: предполагается, что вы умеете работать с Git.

В своей рабочей папке создайте файл `lesson17.py` и в нём создавайте функции согласно заданию.

---

## Уровень 1

_Алиса и Боб участвуют в конкурсе.
Их работу оценивают по трём номинациям: красота, оригинальность и сложность._

Оценка — это три числа: `r = (x, y, z)`.

Три любых объекта ещё называются — "триплет".

Оценка Алисы — это триплет A, оценка Боба — триплет B.

Общий счёт определяется количеством поинтов, по принципу:
- если `A[i]` > `B[i]`, то один поинт зарабатывает А,
- если `B[i]` > `A[i]`, то один поинт зарабатывает B,
- если `B[i]` = `A[i]`, то никто не зарабатывает ничего.

### Задача:

Написать функцию `compare_triplets`.
Её аргументы — два триплета.
Функция считает общий счёт для каждого оппонента.
Возвращает результат: счёт для первого и для второго участника.

### Пример:

```python
A = (1, 1, 0)
B = (1, 0, 1)

compare_triplets(A, B)
# (1, 1)
``` 

```python
A = (10, 100, 1000)
B = (100, 1000, 10)

compare_triplets(A, B)
# (1, 2)
```
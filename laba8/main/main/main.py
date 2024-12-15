# Завдання 1: Реалізація класу з алгоритмічними методами

class Algorithms:
    @staticmethod
    def find_min_positive(numbers):
        """Пошук мінімального елементу масиву позитивних чисел."""
        positives = [num for num in numbers if num > 0]
        return min(positives) if positives else None

    @staticmethod
    def sum_negative(numbers):
        """Розрахунок суми елементів масиву, який може складатися лише з від’ємних чисел."""
        negatives = [num for num in numbers if num < 0]
        return sum(negatives)

    @staticmethod
    def fibonacci(n):
        """Алгоритм розрахунку N-го елементу послідовності Фібоначчі."""
        if n < 0:
            raise ValueError("N має бути невід'ємним цілим числом.")
        if n in [0, 1]:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def current(voltage, resistance):
        """Алгоритм розрахунку сили струму на ділянці кола за законом Ома."""
        if resistance <= 0:
            raise ValueError("Опір має бути більшим за нуль.")
        return voltage / resistance

# Завдання 2: Реалізація модульних тестів
import unittest

class TestAlgorithms(unittest.TestCase):
    # Тести для find_min_positive
    def test_find_min_positive(self):
        self.assertEqual(Algorithms.find_min_positive([3, -1, 7, 5, 0]), 3)
        self.assertEqual(Algorithms.find_min_positive([10, 5, 2, 8]), 2)
        self.assertIsNone(Algorithms.find_min_positive([-3, -7, -1]))

    def test_find_min_positive_invalid(self):
        self.assertIsNone(Algorithms.find_min_positive([]))

    # Тести для sum_negative
    def test_sum_negative(self):
        self.assertEqual(Algorithms.sum_negative([-1, -3, -5]), -9)
        self.assertEqual(Algorithms.sum_negative([0, 2, -4, -6]), -10)
        self.assertEqual(Algorithms.sum_negative([1, 2, 3]), 0)

    def test_sum_negative_invalid(self):
        self.assertEqual(Algorithms.sum_negative([]), 0)

    # Тести для fibonacci
    def test_fibonacci(self):
        self.assertEqual(Algorithms.fibonacci(0), 0)
        self.assertEqual(Algorithms.fibonacci(1), 1)
        self.assertEqual(Algorithms.fibonacci(5), 5)
        self.assertEqual(Algorithms.fibonacci(10), 55)

    def test_fibonacci_invalid(self):
        with self.assertRaises(ValueError):
            Algorithms.fibonacci(-1)

    # Тести для current
    def test_current(self):
        self.assertEqual(Algorithms.current(10, 2), 5)
        self.assertEqual(Algorithms.current(0, 5), 0)

    def test_current_invalid(self):
        with self.assertRaises(ValueError):
            Algorithms.current(10, 0)
        with self.assertRaises(ValueError):
            Algorithms.current(10, -1)

# Завдання 3: Запуск тестів та підрахунок покриття
if __name__ == "__main__":
    unittest.main()

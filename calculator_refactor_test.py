from calculator_refactor import Eval
import unittest

class EvalTest(unittest.TestCase):
    def test_expression_string_to_list(self):
        new_eval = Eval()
        assert new_eval.expression_string_to_list("1+2+3+4") == [1, '+', 2, '+', 3, '+', 4]
        assert new_eval.expression_string_to_list("12+23+34+45") == [12, '+', 23, '+', 34, '+', 45]
        assert new_eval.expression_string_to_list("12*23/34^45-8") == [12, '*', 23, '/', 34, '^', 45, '-', 8]
    
    def test_exponents(self):
        new_eval = Eval()
        assert new_eval.exponents([1, '*', 2, '^', 3, '+', 4]) == [1,'*',8,'+',4]

    def test_multiplication_or_division(self):
        new_eval = Eval()
        assert new_eval.multiplication_or_division([1, '*', 2, '-', 3, '+', 4]) == [2, '-', 3, '+', 4]
        assert new_eval.multiplication_or_division([1, '/', 2, '-', 3, '+', 4]) == [0.5, '-', 3, '+', 4]

    def test_addition_or_subtraction(self):
        new_eval = Eval()
        assert new_eval.addition_or_subtraction([1, '+', 2, '-', 3, '+', 4]) == [3, '-', 3, '+', 4]
        assert new_eval.addition_or_subtraction([1, '-', 2, '-', 3, '+', 4]) == [-1, '-', 3, '+', 4]

    def test_order_emdas(self):
        new_eval = Eval()
        assert new_eval.order_emdas([1, '+', 2, '-', 3, '+', 4]) == 4
        assert new_eval.order_emdas([12, '*', 23, '/', 34, '^', 45, '-', 8]) == -8.0

if __name__ == '__main__':
    unittest.main()

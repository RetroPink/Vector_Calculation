from Math_part import product_vectors_vector
from Math_part import vectors_difference
from Math_part import vector_multiplication_scalar
from Math_part import product_vectors_scalar
from Math_part import vector_modulus
from Math_part import vectors_sum
from Math_part import vector_division_scalar

return_error = {
    3: 'you cannot divide a number by a vector',
    4: 'dividing a vector by a vector is not possible',
    5: '_0 impossible for a number and a vector',
    6: 'The modulus of a vector is impossible for a number',
    7: 'Several in a row _0',
    8: 'Check _0',
    9: 'We have input characters that this program cannot work with.',
    10: '_0 in the wrong order'
}


class VectorCalculator:
    """
The class responsible for operations with vectors
    """

    def __init__(self, opr_vector):
        """
Converts the input data into a vector.
        :param opr_vector:Vector
        """
        self.value = opr_vector

    def __add__(self, other):  # + только с вектора
        """
Vector sum
        :param other:second value
        :return:vector sum
        """
        if type(self) == int or type(self) == float or type(other) == int or type(other) == float:
            print(return_error[5].replace('_0', 'Addition'))  # можно только для векторов
            raise SystemExit
        return VectorCalculator(vectors_sum(self.value, other.value))

    def __sub__(self, other):
        """
vector difference
        :param other:second value
        :return:vector difference
        """
        if type(self) == int or type(self) == float or type(other) == int or type(other) == float:
            print(return_error[5].replace('_0', 'Subtraction'))  # можно только для векторов
            raise SystemExit
        return VectorCalculator(vectors_difference(self.value, other.value))

    def __mul__(self, other):
        """
scalar product or scalar on a vector
        :param other:second value
        :return:a number that is a scalar product or scalar on a vector
        """
        if type(self) == int or type(self) == float:
            return VectorCalculator(vector_multiplication_scalar(self, other.value))
        elif type(other) == int or type(other) == float:
            return VectorCalculator(vector_multiplication_scalar(self.value, other))
        else:
            return VectorCalculator(product_vectors_scalar(self.value, other.value))

    def __rmul__(self, other):
        """
scalar product or scalar on a vector
        :param other:first value
        :return:a number that is a scalar product or scalar on a vector
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
scalar product or scalar on a vector
        :param other:second value
        :return:a number that is a scalar product or scalar on a vector
        """
        if type(self) == int or type(self) == float:
            return VectorCalculator(vector_division_scalar(self, other.value))
        elif type(other) == int or type(other) == float:
            return VectorCalculator(vector_division_scalar(self.value, other))
        else:
            print(return_error[4])
            raise SystemExit

    def __rtruediv__(self, other):
        """
scalar product or scalar on a vector
        :param other:first value
        :return:a number that is a scalar product or scalar on a vector
        """
        print(return_error[3])
        raise SystemExit

    def __pow__(self, other):
        """
vector product
        :param other:second value
        :return: a vector product or, if it is impossible to find it, a scalar product
        """
        if type(self) == int or type(self) == float or type(other) == int or type(other) == float:
            print(return_error[5].replace('_0', 'Vector product'))  # можно только для векторов
            raise SystemExit
        q = product_vectors_vector(self.value, other.value)
        if type(q) == int or type(q) == float:
            return q
        else:
            return VectorCalculator(q)

    def __abs__(self):
        """
vector modulus
        :return:the number that is the modulus of the vector
        """
        if type(self) == int or type(self) == float:
            print(return_error[6])  # можно только для векторов
            raise SystemExit
        return vector_modulus(self.value)


dictionary_elements = '1234567890,.[({})]+-*/'


def check_input(oper):
    """
Responsible for verifying the correctness of the entered data.
Is it possible to overflow them using eval(). Closing brackets. Comma point operators are no longer repeated
    :param oper: accepted data
    :return:The source line itself or is interrupted if the data is incorrect, the data is entered incorrectly.
    """
    c_1 = 0
    c_2 = 0
    c_3 = 0
    p = 0
    ps = '_'
    oper = oper.replace(' ', '')
    if oper.count('(') != oper.count(')'):
        print(return_error[8].replace('_0', '()'))
        raise SystemExit
    if oper.count('[') != oper.count(']'):
        print(return_error[8].replace('_0', '()'))
        raise SystemExit
    if oper.count('{') != oper.count('}'):
        print(return_error[8].replace('_0', '()'))
        raise SystemExit
    if ',,' in oper:
        print(return_error[7].replace('_0', ','))
        raise SystemExit
    if '..' in oper:
        print(return_error[7].replace('_0', '.'))
        raise SystemExit
    if '***' in oper or '++' in oper or '--' in oper:
        print(return_error[7].replace('_0', 'operators'))
        raise SystemExit
    if '[[' in oper or ']]' in oper or '[]' in oper or '][' in oper:
        print(return_error[8].replace('_0', '[]'))
        raise SystemExit
    if '{{' in oper or '}}' in oper or '{}' in oper or '}{' in oper:
        print(return_error[8].replace('_0', '{}'))
        raise SystemExit
    if ')(' in oper or '()' in oper:
        print(return_error[8].replace('_0', '()'))
        raise SystemExit

    for i in oper:
        if not (i in dictionary_elements):  # (i in dictionary_elements) == False
            print(return_error[9])
            raise SystemExit
        if i in dictionary_elements[:10]:  # 1234567890
            if ps == "e_c":
                print('error"Num"')
                raise SystemExit
            ps = 'n'
        elif i in dictionary_elements[12:15]:  # ([{
            if ps == 'n' or ps == 'p' or ps == 'e_c':  # e_c p n
                print('error"start (')
                raise SystemExit
            ps = 's_c'
        elif i in dictionary_elements[15:18]:  # ]})
            if ps == 'o' or ps == 'p' or ps == 's_c':  # s_c p o
                print('error"end )"')
                raise SystemExit
            ps = 'e_c'
        elif i in dictionary_elements[10:12]:  # .,
            if ps == 's_c' or ps == 'e_c' or ps == 'o':  # s_c e_c o
                print('error"Point"')
                raise SystemExit
        elif i in dictionary_elements[18:]:  # +-*
            if ps == 's_c' or ps == 'p':  # s_c p
                print('error"Operation"')
                raise SystemExit
            ps = 'o'

        if i == '(':
            if c_2 == 1 or c_3 == 1:
                print(return_error[10].replace('_0', '()'))
                raise SystemExit
            c_1 = 1
            p = 0
        elif i == '[':
            if c_2 == 1:
                print(return_error[10].replace('_0', '[]'))
                raise SystemExit
            c_2 = 1
            p = 0
        elif i == '{':
            if c_3 == 1 or c_2 == 1:
                print(return_error[10].replace('_0', '{}'))
                raise SystemExit
            c_3 = 1
            p = 0

        elif i == ')':
            if c_2 == 1 or c_3 == 1:
                print(return_error[10].replace('_0', '()'))
                raise SystemExit
            if c_1 == 0:
                print(return_error[10].replace('_0', '()'))
                raise SystemExit
            c_1 = 0
            p = 0
        elif i == ']':
            if c_2 == 0:
                print(return_error[10].replace('_0', '[]'))
                raise SystemExit
            c_2 = 0
            p = 0
        elif i == '}':
            if c_3 == 0:
                print(return_error[10].replace('_0', '{}'))
                raise SystemExit
            if c_2 == 1:
                print(return_error[10].replace('_0', '{}'))
                raise SystemExit
            c_3 = 0
            p = 0
        elif i == ',':
            p = 0
        elif i == '.':
            if p == 1:
                print('error"two point in one num"')
                raise SystemExit
            ps = 'p'
            p = 1
    return oper


def log_oper(inp):
    """
Converts a string to an expression via eval().
    :param inp: entered data
    :return:the result of a mathematical operation
    """
    inp = check_input(inp)
    outp = eval(inp.replace('[', 'VectorCalculator([').replace(']', '])').replace('{', 'abs(').replace('}', ')'))
    if type(outp) == int or type(outp) == float or type(outp) == list:
        return outp
    else:
        return outp.value


HELP = '''HELP:\n
Vector by coordinates a,b,c:...........................................[a,b,c]\n
Number a:....................................................................a\n
Modulus vector by coordinates a,b:.....................................{[a,b]}\n
Sum of vectors by coordinates a,b,c and x,y,z:.................[a,b,c]+[x,y,z]\n
The difference of vectors in coordinates a,b,c and x,y,z:......[a,b,c]-[x,y,z]\n
Vector product of vectors by coordinates a,b,c and x,y,z:.....[a,b,c]**[x,y,z]\n
Scalar product of vectors in coordinates a,b,c and x,y,z:......[a,b,c]*[x,y,z]\n
The product of the number a by the vector at the coordinates x,y,z:..a*[x,y,z]\n
If you want to stop the program, enter "Esc"'''

while True:
    enter = input('\nEnter a vector expression: (if you need help, enter "HELP")\n')
    if enter == 'HELP':
        print(HELP)
    elif enter == 'Esc':
        print('Good bye!')
        break
    else:
        print(log_oper(enter))

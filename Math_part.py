"""
The program block responsible for performing mathematical operations with vectors.
He is mainly engaged only in calculations. The correctness of the data is checked in main.
"""

return_error = {
    0: 'One of the values inside the _0 vector is not a number.',
    1: 'It is impossible to perform such an operation with vectors of different space measures.',
    2: 'The entered data value is not an integer',
    3: 'The entered data _0 and _1 are not a vector and a scalar',
    4: 'It is possible to find a vector product only for vectors of Euclidean space.',
    5: '_0 impossible for a number and a vector',
    6: 'The modulus of a vector is impossible for a number',
    7: 'Several in a row _0',
    8: 'Check _0',
    9: 'We have input characters that this program cannot work with.',
    10: '_0 in the wrong order'
}

accuracy = 10


def appending_vector(vector_smaller, vector_larger):
    """
reduces vectors to a single space
    :param vector_smaller:the vector whose space needs to be enlarged
    :param vector_larger:the vector space to which you need to increase
    :return:corrected vector
    """
    while len(vector_smaller) != len(vector_larger):
        vector_smaller.append(0)
    return vector_smaller


def question_about_appending(vector_first, vector_second):
    """
calls the function of increasing the vector space
    :param vector_first:the first argument is a vector
    :param vector_second:the second argument is a vector
    :return:calls the function of increasing the vector space
    """
    return appending_vector(vector_first, vector_second)


def check_space_vectors(vector_left, vector_right):
    """
checks the difference of the vector space
    :param vector_left:the left argument of the operation
    :param vector_right:the right argument of the operation
    :return:calls the function of increasing the vector space or it says that everything is fine
    """
    if len(vector_left) < len(vector_right):
        question_about_appending(vector_left, vector_right)
    elif len(vector_left) > len(vector_right):
        question_about_appending(vector_right, vector_left)
    return '_'


def check4three(vector):
    """
checks whether the vector of vectors is a three-dimensional space
    :param vector:the introduced vector
    :return:a vector brought to three-dimensional space or says that everything is fine
    """
    if len(vector) > 3:
        return appending_vector(vector, ['_', '_', '_'])
    return '_'


def correction_float_data(final_vector):
    """
corrects fractional data, solves the problem 3.3+6.6=9.899999999999999
    :param final_vector:data that needs to be checked for the correctness of fractional numbers
    :return:data with corrected fractional numbers
    """
    global accuracy
    post_final_vector = []
    for i in range(len(final_vector)):
        if type(final_vector[i]) == float:
            post_final_vector.append(round(final_vector[i], accuracy))
        else:
            post_final_vector.append(final_vector[i])
    return post_final_vector


def vectors_sum(vector_left, vector_right):
    """
find the vector sum
    :param vector_left:the left argument of the operation
    :param vector_right:the right argument of the operation
    :return:vector sum
    """
    check_space_vectors(vector_left, vector_right)
    resulting_vector = []
    for i in range(len(vector_left)):
        resulting_vector.append(vector_left[i] + vector_right[i])
    return correction_float_data(resulting_vector)


def vector_multiplication_scalar(vector, scalar):
    """
multiplies the modulus by a scalar
    :param vector:accepted vector
    :param scalar:accepted scalar
    :return:vector multiplied by a scalar
    """
    if (type(vector) == list and (type(scalar) == int or type(scalar) == float)) or ((type(vector) == int or type(vector) == float) and type(scalar) == list):
        if (type(vector) == int or type(vector) == float) and type(scalar) == list:
            vector, scalar = scalar, vector
    return correction_float_data([i * scalar for i in vector])


def vector_division_scalar(vector, scalar):
    """
division the modulus by a scalar
    :param vector:accepted vector
    :param scalar:accepted scalar
    :return:vector divides by a scalar
    """
    if (type(vector) == list and (type(scalar) == int or type(scalar) == float)) or ((type(vector) == int or type(vector) == float) and type(scalar) == list):
        if (type(vector) == int or type(vector) == float) and type(scalar) == list:
            vector, scalar = scalar, vector
    return vector_multiplication_scalar(vector, scalar**(-1))


def vectors_difference(vector_left, vector_right):
    """
finds the difference of vectors
    :param vector_left:the left argument of the operation
    :param vector_right:the right argument of the operation
    :return:vector difference
    """
    vector_right = vector_multiplication_scalar(vector_right, -1)
    return vectors_sum(vector_left, vector_right)


def vector_modulus(vector):
    """
find the modulus of the vector, that is, its length
    :param vector:accepted vector
    :return:vector length
    """
    return (correction_float_data([sum([i * i for i in vector]) ** 0.5]))[0]


def product_vectors_scalar(vector_left, vector_right):
    """
finds the scalar product of vectors
    :param vector_left:the left argument of the operation
    :param vector_right:the right argument of the operation
    :return:a number that is a scalar product of vectors
    """
    check_space_vectors(vector_left, vector_right)
    return sum(correction_float_data([vector_left[i] * vector_right[i] for i in range(len(vector_left))]))


def question_about_change_operator(vector_left, vector_right):
    """
changes the operation from a vector product to a scalar
    :param vector_left:the left argument of the operation
    :param vector_right:the right argument of the operation
    :return:calling the scalar product
    """
    return product_vectors_scalar(vector_left, vector_right)


def product_vectors_vector(vector_left, vector_right):
    """
finds the vector product of vectors
    :param vector_left:the left argument of the operation
    :param vector_right:the right argument of the operation
    :return:a vector that is a vector product of the introduced vectors
    """
    if not (len(vector_left) == 3 and len(vector_right) == 3):
        if len(vector_left) > 3 or len(vector_right) > 3:
            return question_about_change_operator(vector_left, vector_right)
        else:
            if check4three(vector_left) == 'error':
                pass
            if check4three(vector_right) == 'error':
                pass
    check_space_vectors(vector_left, vector_right)
    resulting_vector = [vector_left[1] * vector_right[2] - vector_left[2] * vector_right[1],
                        (vector_left[0] * vector_right[2] - vector_left[2] * vector_right[0]) * (-1),
                        vector_left[0] * vector_right[1] - vector_left[1] * vector_right[0]]
    return correction_float_data(resulting_vector)

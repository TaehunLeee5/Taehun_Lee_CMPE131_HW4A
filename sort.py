def sort_dictionary(dictionary1):
    def get_age(item):
        return item[1][1]

    sorted_dict = sorted(dictionary1.items(), key = get_age)

    result = []

    for name, (phone, age) in sorted_dict:
        result.append((name, phone))

    return result

"""
dictionary11 = {"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}
print(sort_dictionary(dictionary11))

Output: 
[('Mary', 1557896), ('Tom', 5464512), ('Sara', 5446987)]
"""
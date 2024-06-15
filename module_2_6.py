# def single_root_words(root_word, *other_words):
#     same_words = []
#     for word in other_words:
#         if root_word.lower() in word.lower() or word.lower() in root_word.lower():
#             same_words.append(word)
#     return same_words
#
# # root_word1 = "cat"
# # other_words1 = ["caterpillar", "dog", "catalog", "bat", "catch"]
# result1 = single_root_words("cat", "caterpillar", "dog", "catalog", "bat", "catch")
# print(result1)
#
# # root_word2 = "Disablement"
# # other_words2 = ["Able", "Mable", "Disable", "Bagel"]
# result2 = single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel")
# print(result2)

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])

list_ = [1, 3, 4]
dict_= {'a': 4, 'b': 10, 'c': True}
print_params(*list_)
print_params(**dict_)

values_list_2 = [2, True]
print_params(*values_list_2, 42)



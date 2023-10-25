def sorting_time(words:list) -> list:
    words = sorted(words, key=lambda x: x[:2])
    return words

if(__name__ == "__main__"):
    number_of_words = 1
    word_list_list = [0][0]
    list_list_index = 0
    while(number_of_words != 0):
        
        number_of_words = input()
        for i in range(1,int(number_of_words)):
            new_word = input()
            word_list_list[list_list_index].append(new_word)
        list_list_index += 1
    for i in word_list_list:
        for x in i:
            print(x)
        print("\n") 
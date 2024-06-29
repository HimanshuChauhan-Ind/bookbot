def main():
    file_path = "./books/frankenstein.txt"
    text = read_file(file_path)
    word_count = word_counter(text)
    letter_count = letter_counter(text)

    letter_list = letter_dict_list(letter_count)
    report_generator(word_count,letter_list)
    # print(letter_list)

def word_counter(str):
    words = str.split()
    return len(words)   

def letter_counter(str):
    lowrcase_str = str.lower()
    letter_record = {}
    for letter in lowrcase_str:
        if letter in letter_record:
            letter_record[letter] += 1
        else:
            letter_record[letter] = 1
    return letter_record

def letter_dict_list(dict):
    letter_list = []
    for letter in dict:
        if letter.isalpha():
            new_dict = {"letter":letter,"count":dict[letter]}
            letter_list.append(new_dict)
    return letter_list
            
def report_generator(count,letter_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{count} words found in the document\n\n')    
    def sort_on(dict):
        return dict["count"]

    letter_list.sort(reverse=True,key=sort_on)

    for letter in letter_list:
        print(f'The {letter["letter"]} character was found {letter["count"]} times')
    print("--- End report ---")
    



def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents




main()
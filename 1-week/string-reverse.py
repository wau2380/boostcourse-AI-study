sentence = "way is a there will a is there where"

def reverse_sentence(sentence):
    s_reverse = ''
    for i in sentence:
        print(i)
        s_reverse = i + s_reverse
    return s_reverse
        
        

print(reverse_sentence(sentence))
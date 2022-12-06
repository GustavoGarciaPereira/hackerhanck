def count_substring(string, sub_string):

    cont = 0
    for i in range(len(string)):
        if string[i:len(sub_string)+i] == sub_string:
            cont += 1

    return cont

if __name__ == '__main__':
    string = 'ABCDCDC'#input().strip()
    sub_string = 'CDC'#input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
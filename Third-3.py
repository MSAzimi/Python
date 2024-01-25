import re
text=input()
def edit_text_first(text):
    b=list(text)
    counter=0
    for i in range(len(b)):
        if b[i] == '@':
            counter += 1
        elif b[i] == '#':
            if counter > 0:
                counter -= 1
                b[i] = ''
            else:
                pass
    first =''.join(b)
    second = ' '.join(first.split())
    final = re.sub(r'\\n', '\n', second)
    return f"Formatted Text: {final}"

a=edit_text_first(text)
print(a)

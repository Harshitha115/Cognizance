assigned_string = input('Enter a string: ')
even_chars = []

for i in range(len(assigned_string)):
    if i % 2 == 0:
        even_chars.append(assigned_string[i])

print('Even characters: {}'.format(even_chars))

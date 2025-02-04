# Write a function that receives the number n as a parameter. 
# If n is odd, produce and return a rug with dimensions n*n. 
# If n is even, the appropriate message will be returned.
# Creat Concentric Rugs 
# num: rugs'dimensions, have to odd number (1,3,5,...)
# type: 'emoji' for default, number for another values
def concentric_rugs(num, type_cr='emoji'):
    emoji = ['😀','😍','😎','👀','🎈','🍗','🍕','😆']
    center = (num-1) / 2
    if not center.is_integer() or center < 0:
        raise ValueError('input number have to odd and positive number (1,3,5,...) !!')
    CR_matrix = []
    for row in range(num):
        Temp_array = []
        for com in range(num):
            result = int(max(abs(com - center), abs(row - center)))
            if type_cr == 'emoji':
                Temp_array.append(emoji[result%(len(emoji))])
            else:
                Temp_array.append(result)
        CR_matrix.append(Temp_array)
    return CR_matrix

def print_concentric_rugs(CR_matrix):
    for row in CR_matrix:
        for char in row:
            print(char, end=' ')
        print()

number = int(input('Enter your nubmer to creat concentric rugs: '))
print_concentric_rugs(concentric_rugs(number))
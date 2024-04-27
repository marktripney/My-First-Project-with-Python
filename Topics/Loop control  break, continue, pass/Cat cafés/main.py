cafe_name = ''
cafes = []


def find_cafe_with_max_cats(cafe_list):
    destination, most_cats = cafe_list[0][0], int(cafe_list[0][1])
    for cafe in cafe_list:
        if int(cafe[1]) > most_cats:
            destination, most_cats = cafe[0], int(cafe[1])
    return destination


while cafe_name != 'MEOW':
    cafe_name = input()
    if cafe_name == 'MEOW':
        break
    else:
        cafes.append(cafe_name.split(' '))


print(find_cafe_with_max_cats(cafes))
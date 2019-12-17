colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
with open('C:/Users/Djush/PycharmProjects/untitled/text.txt', 'w') as raibow_colors:
    for color in colors_list:
        print(color, file=raibow_colors)


#1. Create a tuple of colors
colors_tuple = ('V - VIOLET','I-INDIGO','B-BLUE','G-GREEN','Y-YELLOW','O-ORANGE','R-RED')
print(colors_tuple)

#2. Try to add 1 more color
#colors_tuple.append('WHITE') #can't do it
colors_tuple_ext = colors_tuple + ('WHITE',)
print(colors_tuple_ext)


#3. Print all colors 1 by 1 on 1 line with "color" as prefix
# print('Color: ',colors_tuple[0])
# print('Color: ',colors_tuple[1])
# print('Color: ',colors_tuple[2])
# print('Color: ',colors_tuple[3])
# print('Color: ',colors_tuple[4])
# print('Color: ',colors_tuple[5])
# print('Color: ',colors_tuple[6])

#TODO: Can kiem tra lai doan code nay
print('#3a Print all use WHILE loop!!')
count = 0
while (count < 7):
   print('Color: ',colors_tuple[count])
   count = count + 1

print('#3b Print all use FOR loop!!')



#4. Check how many colors we have?
print('Count Color Tuples:', len(colors_tuple))

#5. Print colors from 3 - 7
print(colors_tuple[2:6])


def bubbleSort(liste):
    k = 0
    is_swap = True
    while k < len(liste) - 1 and is_swap:
        k = k+1 
        for i in range(0, len(liste)-1):
            if liste[i] > liste[i+1]:
                is_swap = True
                tmp = liste[i] 
                liste[i] = liste[i+1]
                liste[i+1]=tmp
    return liste

if __name__ == '__main__':
    liste = [5,8,6,9,7,4,2,5,3,6,1,45,25,5,2,5,3,6,5]
    sorted_list = bubbleSort(liste)
    print(sorted_list)

"""
Bubble Sort:

her elemanını bir sonraki eleman ile karşılaştır  
liste sıralanana kadar bu işlemi devam ettir.

[5,8,6,9,7,4,2<,5] - 5 > 8 değişikliğe gerek yok
[5,8,6,9,7,4,2,5] - 8 > 6 değiştir
[5,6,8,9,7,4,2,5] - 8 > 9 
[5,6,8,9,7,4,2,5] - 9 > 7 değiştir
[5,6,8,7,9,4,2,5] - 9 > 4 değiştir
[5,6,8,7,4,9,2,5] - 9 > 2 değiştir
[5,6,8,7,4,2,9,5] - 9 > 5 değiştir
[5,6,8,7,4,2,5,9] - 9 > 5 değiştir
...
[2,4,5,5,6,7,8,9]
 
"""
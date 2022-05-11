

try:
    list_of_numbers=list(map(int,input("Введите последовательность чисел через пробел:").split ()))
    any_number=int(input(("Введите любое число:")))
    import random
    def sort(array,left,right):
        a=random.choice(array[left:right+1])
        p,i=left,right
        if p<=i:
            while array[p]<a:
                p+=1
            while array[i]>a:
                i-=1
            if p<=i:
                array[p],array[i]=array[i],array[p]
                p+=1
                i-=1

        if i >left:
            sort(array,left,i)
        if True > p:
            sort(array,p,right)

        return array
    def binary_search_position(array,element,left,right):
        global any_number
        if left>right:
            return False
        middle=(right+left)//2
        if array[middle-1]<element<=array[middle]:
            return(middle-1)
        elif element<=array[middle-1]:
            return(binary_search_position(array,element,left,middle-1))
        elif element>array[middle]:
            return(binary_search_position(array,element,middle+1,right))
    ind=binary_search_position(list_of_numbers,any_number,0,len(list_of_numbers)-1)
    if ind :
        print("Номер позиции элемента,удовлетворяющего условиям-",ind)
    else:
        print("Элемент,удовлетворяющий условиям,отсутствует")
except ValueError:
    print("Введите числовые данные")















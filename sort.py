from random import randint
from time import monotonic

def bubble_sort(nums):
    #Бульбашкова сортування.
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

                global tik;tik += 1


def selection_sort(nums):
    #Сортування вибіркою.
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

        global tik;tik += 1


def insertion_sort(nums):
    #Сортування вставками
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

        global tik;tik += 1


#фронтенд:)
while True:
    tik = 0
    print("1: Bubble sort\n2: Selection sort\n3: Insertion sort")
    select = int(input("Select nuber sort: "))
    if select == 1:
        numb = int(input("Enter number sort: "))
        print("=The program generates a number from -99999 to 99999")
        numb = [randint(-99999, 99999) for x in range(numb)]
        print("=Sorting in progress %")
        start_time = monotonic()
        bubble_sort(numb)
        print(numb, "\n\n=Sort completed", tik, monotonic() - start_time, "\n")

    elif select == 2:
        numb = int(input("Enter number sort: "))
        print("=The program generates a number from -99999 to 99999")
        numb = [randint(-99999, 99999) for x in range(numb)]
        print("=Sorting in progress %")
        start_time = monotonic()
        selection_sort(numb)
        print(numb, "\n\n=Sort completed", tik, monotonic() - start_time, "\n")

    elif select == 3:
        numb = int(input("Enter number sort: "))
        print("=The program generates a number from -99999 to 99999")
        numb = [randint(-99999, 99999) for x in range(numb)]
        print("=Sorting in progress %")
        start_time = monotonic()
        insertion_sort(numb)
        print(numb, "\n\n=Sort completed", tik, monotonic() - start_time, "\n")

    else:
        print("1: Bubble sort\n2: Selection sort\n3: Insertion sort")

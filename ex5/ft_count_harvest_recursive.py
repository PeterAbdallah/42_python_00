def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def checkpoint(days: int):
        if (days < 1):
            return
        checkpoint(days - 1)
        print("Day ", days)
    checkpoint(days)

# def ft_count_harvest_recursive():
#     days = int(input("Days until harvest: ")) + 1

#     def checkpoint():
#         nonlocal days
#         days -= 1
#         result = days
#         if (days < 1):
#             return
#         checkpoint()
#         print(result)
#     checkpoint()

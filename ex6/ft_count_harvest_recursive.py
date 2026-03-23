def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def checkpoint(days: int):
        if (days < 1):
            return
        checkpoint(days - 1)
        print("Day ", days)
    checkpoint(days)
    print("Harvest time!")

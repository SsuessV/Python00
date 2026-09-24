def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_day(day):
        print("Day", day)
        if day == days:
            print("Harvest time!")
            return
        count_day(day + 1)
    count_day(1)

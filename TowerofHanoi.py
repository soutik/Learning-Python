def hanoi(disk, start, inter, end):
    if disk >=1:
        hanoi(disk-1, start, inter, end)
        print("Disk", disk ," From ",start, " to " , end)
        hanoi(disk-1, inter, start, end)

hanoi(3, 'A','B','C')
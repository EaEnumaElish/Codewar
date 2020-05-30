def queue_time(customers, n):
    tills = [0]*n
    print(tills, "do")
    for i in customers:
      tills[0] += i
      tills.sort()
    print(tills, "posle")
    return max(tills)




print(queue_time([5], 1))
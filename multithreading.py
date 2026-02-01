import threading as t
import time


def func(s):
    print(f"Sleep for {s} s")
    time.sleep(s)



# t1 = time.perf_counter()
# func(4)
# func(5)
# func(7)
# func(2)
# t2 = time.perf_counter()

# print("Time diff is ",(t2-t1))


t1 = time.perf_counter()

th1 = t.Thread(target=func, args=[4])
th2 = t.Thread(target=func, args=[5])
th3 = t.Thread(target=func, args=[3])
th4 = t.Thread(target=func, args=[2])

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()


t2 = time.perf_counter()

print("Time diff is ",(t2-t1))
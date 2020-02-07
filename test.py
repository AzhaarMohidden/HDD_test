import time
def load_ind(x):
    switcher = {
        1: "/",
        2: "-",
        3: r"\ ",
        4: "|",
        5: "/",
    }
    print switcher.get(x, "Invalid month")
n=1
while(1):
    if (n>5):
        n = 1
    load_ind(n)
    time.sleep(1)
    n=n+1

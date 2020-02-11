import time
def load_ind(x, ad):
    switcher = {
        0: ad + " * -> 1",
        1: ad + " / -> 2",
        2: ad + " - -> 3",
        3: ad + r"\ -> 4 ",
        4: ad + " | -> 5",
    }
    print switcher.get(x, "Invalid month")
def mn_ld(load_word):
    for i in range(5):
        load_ind(i, load_word)
        time.sleep(1)
    print("Done")

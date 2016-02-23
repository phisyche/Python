def bubble_sort(items):
    """Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j] #swap!

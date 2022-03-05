def top_n(items,n):
    '''
    return the top n items 
    in an array in a decending order

    args:
        items(array): list or arrays-like object
        n(int): num of items to return
    Eg.:
        >>> top_n([8,5,4,1,5,2],3)
        [8,5,5]
    '''
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j]>items[j+1]: #if this item is bigger than the next item
                items[j],items[j+1]=items[j+1],items[j] #swap the two
    #get last two items
    top_n=items[-n:]
    #return in descending order
    return top_n[::-1]
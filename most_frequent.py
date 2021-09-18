import operator

w = input("Please enter a string: ")
def most_frequent(w):
    d=dict()
    for key in w:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    for key, value in sorted_d.items():
        print(f'{key}=0{value}')

most_frequent(w)

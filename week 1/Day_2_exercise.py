# def multiplyall(*args):
#     print(args)
#     ans=1
#     for i in range(len(args)):
#         print(f"{args[i]} *"," ")
#         ans*=args[i]
        
#     return ans

# print(multiplyall(1,2,3,4,5))


def makesentence(**kwargs):
    words=kwargs.values()
    return ' '.join(words)
        
print(makesentence(w1='hey', w2='chaitanya',w3='shimpi',w4='How',w5='Are',w6='You'))
from big_o import BigO
if __name__=='__main__':
    matrix= [
                ['a','b','c','d'],
                ['q','i','n','m'],
                ['f','e','h','j'],
                ['p','o','l','g'],
            ]
    a=BigO(matrix)
    a.run_bo()
    a.run()

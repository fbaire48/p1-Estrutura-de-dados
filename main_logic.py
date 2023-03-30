class SubArrIdxPos:
    def __init__(self,matrix):
        self.matrix=matrix
        self.item_pos={} #k=key v=value
        self.items=[]
        self.pos=[]
    def get_item_pos(self,lim,dict_dest,key_dest):
        for row_idx in range(0,lim):
            for column_idx in range(0,lim):
                key=self.matrix[row_idx][column_idx]
                pos=f'{row_idx}:{column_idx}'
                dict_dest[key]=pos
                key_dest+=[key]
    def sort_items(self):
        for focus in range(0,len(self.items)):
            for list_item in range(0,len(self.items)):
                if self.items[focus]<self.items[list_item]:
                    bigger=self.items[list_item]
                    smaller=self.items[focus]
                    self.items[focus]=bigger
                    self.items[list_item]=smaller
    def mapper(self):
        for item in self.items:
            value=self.item_pos[item]
            self.pos+=[value]
    def run(self):  
        self.get_item_pos(len(self.matrix),self.item_pos,self.items)  
        self.sort_items()  
        self.mapper()  
        print(self.items)  
        print(self.pos)  
# matrix=[  #
#             ['a','b','c','d'],  #
#             ['q','i','n','m'],  #
#             ['f','e','h','j'],  #
#             ['p','o','l','g'],  #
#         ]  #
# a=SubArrIdxPos(matrix)   #
# a.run()   #

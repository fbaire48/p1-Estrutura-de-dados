class SortedSubarrIdxPosMapper:
    def __init__(self,matrix):
        self.matrix=matrix
        self.kv_before_pos={} #k=key v=value
        self.sub_arrs_items=[]
        self.pos_mapper=[]
    def fill_dict_list(self,lim,matrix,dict_dest,key_dest):
        for row_idx in range(0,lim):
            for column_idx in range(0,lim):
                key=matrix[row_idx][column_idx]
                pos=f'{row_idx}:{column_idx}'
                dict_dest[key]=pos
                key_dest+=[key]
    def sort_list(self):
        for focus in range(0,len(self.sub_arrs_items)):
            for list_item in range(0,len(self.sub_arrs_items)):
                if self.sub_arrs_items[focus]<self.sub_arrs_items[list_item]:
                    bigger=self.sub_arrs_items[list_item]
                    smaller=self.sub_arrs_items[focus]
                    self.sub_arrs_items[focus]=bigger
                    self.sub_arrs_items[list_item]=smaller
    def mapper_val_key(self):
        for item in self.sub_arrs_items:
            value=self.kv_before_pos[item]
            self.pos_mapper+=[value]
    def run(self):  
        self.fill_dict_list(len(self.matrix),self.matrix,self.kv_before_pos,self.sub_arrs_items)  
        self.sort_list()  
        self.mapper_val_key()  
        print(self.sub_arrs_items)  
        print(self.pos_mapper)  
# matrix= [ #
#             ['a','b','c','d'], #
#             ['q','i','n','m'], #
#             ['f','e','h','j'], #
#             ['p','o','l','g'], #
#         ] #
# a=SortedSubarrIdxPosMapper(matrix)  #
# a.run()  #

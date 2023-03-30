from main_logic import SortedSubarrIdxPosMapper

import time as timer
import matplotlib.pyplot as graph
class BigO(SortedSubarrIdxPosMapper): #Hybridclass
    def __init__(self,matrix):
        super().__init__(matrix)
        self.input_sizes=[input_size for input_size in range(0,len(self.matrix)+1)]
        self.time=[]
        self.k_v_pos_bo={}
        self.sub_arr_items_bo=[]
    def fill_dict_list_complexity(self,input_size):
        start_time = timer.time()
        self.fill_dict_list(input_size,self.matrix,self.k_v_pos_bo,self.sub_arr_items_bo)
        end_time = timer.time()
        full_time=(end_time-start_time)*10**6 #second to microsecond
        self.time+=[full_time]
    def fill_time(self):
        for input_size in self.input_sizes: 
            self.fill_dict_list_complexity(input_size)
    def render_graph(self):
        create_graph=graph.plot(self.input_sizes,self.time)
        render=graph.show()
    def run_bo(self):
        self.fill_time()
        self.render_graph()
# matrix= [ #
#             ['a','b','c','d'], #
#             ['q','i','n','m'], #
#             ['f','e','h','j'], #
#             ['p','o','l','g'], #
#         ] #
# # a=SortedSubarrIdxPosMapper(matrix) # #
# # a.run() # #
# a=BigO(matrix) #
# a.run_bo() #
# a.run() #

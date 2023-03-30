from main_logic import SubArrIdxPos

import time as timer
import matplotlib.pyplot as graph
class BigO(SubArrIdxPos): #Hybridclass
    def __init__(self,matrix):
        super().__init__(matrix)
        self.input_sizes=[input_size for input_size in range(0,len(self.matrix)+1)]
        self.time=[]
        self.item_pos_bo={}
        self.items_bo=[]
    def get_item_pos_complexity(self,input_size):
        start_time = timer.time()
        self.get_item_pos(input_size,self.item_pos_bo,self.items_bo)
        end_time = timer.time()
        full_time=(end_time-start_time)*10**6 #second to microsecond
        self.time+=[full_time]
    def get_time(self):
        for input_size in self.input_sizes: 
            self.get_item_pos_complexity(input_size)
    def render_graph(self):
        create_graph=graph.plot(self.input_sizes,self.time)
        render=graph.show()
    def run_bo(self):
        self.get_time()
        self.render_graph()
# matrix= [ #
#             ['a','b','c','d'], #
#             ['q','i','n','m'], #
#             ['f','e','h','j'], #
#             ['p','o','l','g'], #
#         ] #
# # a=SubArrIdxPos(matrix) # #
# # a.run() # #
# a=BigO(matrix) #
# a.run_bo() #
# a.run() #

import csv
import sys

#Storing all the Node in aList
Node=[]

#Storing the whole Network in a dictionary
Network={}

#Opening the csv file in a dictionary mode 
with open(str(sys.argv[1]), newline='') as csvfile:
     reader = csv.DictReader(csvfile)

#Read each line of csv file to store the node and whole network
     for row in reader:
        Row=dict(row)
        #Adding the Node in the Node List
        Node+=[Row['']] 
        del Row['']
        #Updating the network dictionary in the dictionary where the keys are the nodes
        Network[Node[-1]]=Row

#Taking the input as a source node
source= input("Please, provide the node’s name:")

#If source not in list
while source not in Node:
   print("Please memorize the topolgy and come back!!!")
   source= input("Please, provide the node’s name:")

#For comparing create a set for total node
set_Node=set(Node)
#For comparing create a compare set node
compare_set={source}
#Starting point of each link and Initialization
start=source
#Creating a dictionary to update the trace table it will containg the least cost and previous node in the link for each node as tuple
Trace_Table={}
#Compare two set of Node for updating the trace table
while set_Node & compare_set!=set_Node:
   Compare_min=(9999,'u') #dummy comparing tuple
   #Iterating all the nodes for updating the trace table
   for node in Node:
      #Updating the trace table
      if Trace_Table.get(node)==None:
         Trace_Table[node]=int(Network[start][node]),start
      else:
         #Updating the neighbour node
         Trace_Table[node]=min(Trace_Table[node],(Trace_Table[start][0]+int(Network[start][node]),start))
      Compare_min=min(Compare_min,(Trace_Table[node][0],node)) #For adding the next staring pont of link iteration
   start=Compare_min[1] #Starting Node for the next link iteration
   compare_set.add(start) #Adding the next starting node
   Node.remove(start) #Removing the staring node from the list

#Creating path tree dictionary for generating path tree from the trace table
path_tree={}

#Searching for the source node for each path which will give us the path
for key in Trace_Table:
   key1=Trace_Table[key][1]
   #Searching for source node
   while key1[0]!=source:
      key1=Trace_Table[key1[0]][1]+key1
   #When source node is found add with the destination
   path_tree[key]=key1+key

#Remove the source Node from the path tree
del path_tree[source]

#Printing the result
print ('Shortest path tree for node {}:'.format(source))
print (', '.join('%s' % (path_tree[k]) for k in path_tree.keys()))

print ('Costs of least-cost paths for node {}:'.format(source))
print (', '.join('%s : %s' % (k,Trace_Table[k][0]) for k in Trace_Table.keys()))

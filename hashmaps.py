"""
hash tables and hash algorithms
"""

big_dict = {'Employees' : {'Dave' : {'Age': 23, 'Salary': 2000, 'Position': 'Junior'},
                          'Ana': {'Age': 35, 'Salary': 3000,'Position': 'Senior'}}
                          }
#print(big_dict)
#print(big_dict['Employees']['Dave'])
#print(big_dict.keys())
data_array = ['Bob','Bill','Jane','Leon','Vincent','Andy','Fritz','Daniel']
class Node:
    def __init__(self, dataval=None): #initalise with dataval as None as default
        self.dataval = dataval 
        self.nextval = None

def hash_func(i):
    total = 0
    for letter in i:
        total += ord(letter)
    return total%10

class LinkedList: 
    def __init__(self):
        self.headval = None

    def printList(self): #print the list
        printval = self.headval 
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval #referencing next node in the list, if None->ends

    def insertBeginning(self,newdata):
        newNode = Node(newdata)
        newNode.nextval = self.headval  #udpating old node to new node's next value
        self.headval = newNode #change first node to new node

    def insertEnd(self,newdata):
        newNode = Node(newdata)
        if self.headval ==  None: #in case where no nodes are currently in the list
            self.headval = newNode
            return
        lastNode = self.headval
        while lastNode.nextval !=  None: #goes down the list until the end (nextval = None)
            lastNode = lastNode.nextval 
        lastNode.nextval = newNode #appends new node after last node

    def insertBetween(self,insertAfterThisNode,newdata):
        newNode = Node(newdata)
        if self.headval == None:
            self.headval = newNode
            return
        lastNode = self.headval
        newNode.nextval = insertAfterThisNode.nextval #assigns the original nextval to the new node
        insertAfterThisNode.nextval = newNode #assigns the new node as next val to the given node

    def removeNode(self,DataToBeRemoved):
        headval = self.headval
        if headval != None: 
            if headval.dataval == DataToBeRemoved: #case where first node has to be removed
                self.headval = self.headval.nextval #assigns 2nd node to 1st node's place (1st node removed)
                return
        while headval != None: #go down the list to find last node
            if headval.dataval == DataToBeRemoved: #this will never trigger on the first node, as the code above catches that 
                break
            prev = headval
            headval = headval.nextval
            if headval ==  None: #no such node can be found
                print("The node to be removed cannot be found")
                return
        prev.nextval = headval.nextval #assigns previous node's nextval to skip the removed node, essentially removing the node



def hashing(data_array):
    big_dict = {}
    for data in data_array:
        index = hash_func(data['Name'])
        newNode = Node(data)
        if str(index) in big_dict.keys():
            #print("conflict!",name)
            big_dict[str(index)].insertEnd(data)
        else:
            big_dict[str(index)] = LinkedList()
            big_dict[str(index)].headval = newNode
    return big_dict

def access(table,key): #not functional
    index = hash_func(key)
    i = table[str(index)].headval
    while i.dataval['Name']!= key:
        i = i.nextval
    return i.dataval['Age']
        

dict3 =  [{'Name':"Able",'Age':'15'},
          {'Name': 'Beta', 'Age': '17'}
          ]
big_dict2 = hashing(data_array)
hashed = hashing(dict3)
print(access(hashed,'Able'))
#print(big_dict2['7'].printList())
#for index in big_dict2:
#  print(index, big_dict2[index].printList())
#print(access(big_dict2,"Vincent"))
        
list1 = LinkedList()
list1.headval = Node("Mon") #first node (head)
node1 = Node("Tues")
node2 = Node("Weds")
node3 = Node("Thurs")

list1.headval.nextval = node1 #second node
node1.nextval = node2 #3rd node
node2.nextval = node3 #4th node

list1.insertBeginning('Sun')
list1.insertEnd('Fri')
list1.insertBetween(node2,'bruh')
list1.removeNode('Thurs')

#list1.printList()



    

    

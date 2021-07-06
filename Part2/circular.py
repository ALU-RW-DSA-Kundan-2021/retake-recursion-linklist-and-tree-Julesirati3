class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
   
class list:  
    #Here we a are declaring head and tail pointer as null.  
    def __init__(self):  
        self.count = 0;  
        self.t = Node(None);
        self.head = Node(None);  
        self.head.next = self.t;  
        self.t.next = self.head;  
      
    #function to add new node at the end of the list.  
    def addNode(self,data):  
        newNode = Node(data);  
       
        if self.head.data is None:  
            
            self.head = newNode;  
            self.t= newNode;  
            newNode.next = self.head;  
        else:  
           
            self.t.next = newNode;  
            # the New node will become new tail.  
            self.t = newNode;  
             
            self.t.next = self.head;  
              
    #This is a function to count the nodes of list  
    def CountNode(self):  
        TNode = self.head;  
        self.count=self.count+1;  
        while(TNode.next != self.head):  
            self.count=self.count+1;  
            TNode  = TNode.next;  
        print("number of nodes found in this are : ") 
        print(self.count)
      
   
class CircularSinglyLinkedList:
    r = list() 
    #Add data 
    r.addNode(17);  
    r.addNode(23);  
    r.addNode(69);  
    r.addNode(7);  
    r.addNode(2);
    r.addNode(11);
     
    r.CountNode(); 

class Node:
    def __init__(self, v):
        self.value = v
        self.child = []
    
    def ins(self, val):
        self.child.append(val)


#-------------------------------------------------------------------
#Recursive Solution------------------------------------------------------------
def MIS_(root, bit):
    exclude = 0
    include = 1
    for i in range(len(root.child)):
        include += MIS_(root.child[i], 0)
        exclude += max(MIS_(root.child[i], 0), MIS_(root.child[i], 1))
    
    if bit == 1:
        return include
    else:
        return exclude

def MIS(root):
    return max(MIS_(root, 0), MIS_(root, 1))

#Dynamic Programmin ------------------------------------------------------------- # The DP solution isn't complete
def DP_(root, mem, index, adj):
    for i in range(len(root.child)):
        DP_(root.child[i], mem, index+adj+i, len(root.child))
    
        if(len(root.child) == 0):
            mem[index][0] = 0
            mem[index][1] = 1
        else:
            for i in range(len(root.child)):
                mem[index][0] += max(mem[index+i][0], mem[index+i][1])
        

def DP(root):
    temp = [root]
    n = 0
    while(len(temp)>0):
        r = temp.pop(0)
        n += 1
        for i in range(len(r.child)):
            temp.append(r.child[0])
    
    mem = [[0]*n for i in range(2)]

    DP_(root, mem, 0, 1)
    return(mem[0][0], mem[0][1])

root = Node(1)
root.ins(Node(2))
root.ins(Node(2))
root.ins(Node(2))
for i in range(3):
    for j in range(3):
        root.child[i].ins(Node(3))

#print(MIS(root))

print(DP(root)) # The DP solution isn't complete
import time
start_time = time.time()

datafile = 'data/day18.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

from collections import deque
def infixToPostfix1(infixexpr):
    prec = {}
    prec["+"] = 2
    prec["*"] = 2
    prec["("] = 1
    opStack = deque()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (len(opStack)>0) and \
               (prec[opStack[-1]] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while len(opStack)>0:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def infixToPostfix2(infixexpr):
    prec = {}
    prec["+"] = 3
    prec["*"] = 2
    prec["("] = 1
    opStack = deque()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (len(opStack)>0) and \
               (prec[opStack[-1]] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while len(opStack)>0:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)



class Evaluate: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
  
    # The main function that converts given infix expression 
    # to postfix expression 
    def evaluatePostfix(self, exp): 
          
        # Iterate over the expression for conversion 
        for i in exp: 
              
            # If the scanned character is an operand 
            # (number here) push it to the stack 
            if i.isdigit(): 
                self.push(i) 
  
            # If the scanned character is an operator, 
            # pop two elements from stack and apply it. 
            else: 
                val1 = self.pop() 
                val2 = self.pop() 
                self.push(str(eval(val2 + i + val1))) 
  
        return int(self.pop()) 
                  
  
              

def part1Math(problem):
    postfix1 = infixToPostfix1(problem)
    postfix1 = postfix1.replace(" ","")
    obj = Evaluate(len(postfix1)) 
    return obj.evaluatePostfix(postfix1) 

def part2Math(problem):
    postfix2 = infixToPostfix2(problem)
    postfix2 = postfix2.replace(" ","")
    obj = Evaluate(len(postfix2)) 
    return obj.evaluatePostfix(postfix2) 

part1 = 0
part2 = 0  
for x in data:
    x = x.replace("(","( ")
    x = x.replace(")"," )")
    part1 += part1Math(x)
    part2 += part2Math(x)
  

print("Part 1: %s" % part1)
print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))
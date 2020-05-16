import Knight
import variable
import copy
import constraint
import notEqualConstraint
import simpleInference
import forwardCheckingInference
import time
import backtrackingSearch
import consoleListener
import numpy as np
class CSP():
 
    def __init__(self, variables = [], domains = [], constraints = []):
        self._variables = variables
        self._domain = domains
        self._constraints = constraints
        self._domainOfVariable = {}
        self._contraintsOfVariable = {}
        self.setUpVariableDomains()
        self.setUpConstraints()
        self.list1=[]
    def setUpVariableDomains(self):
        for var in self._variables:
            self.addVariableDomain(var, self._domain)
        
    def setUpConstraints(self):
        for constraint in self._constraints:
            self.addConstraint(constraint)
            
    def addVariableDomain(self,var,domain):
        self._domainOfVariable[var] = copy.deepcopy(domain)
        
    def addConstraint(self,constraint):
        for var in constraint.getScope():
            if var not in self._contraintsOfVariable:
                self._contraintsOfVariable[var] = []
                self._contraintsOfVariable[var].append(constraint)
                
    def addSingleConstraint(self,constraint):
        self._constraints.append(constraint)
        for var in constraint.getScope():
            if var not in self._contraintsOfVariable:
                self._contraintsOfVariable[var] = []
                self._contraintsOfVariable[var].append(constraint)
                
    def addVariable(self,variable):
        self._variables.append(variable)
        self.addVariableDomain(variable,self._domain)
        
    def getVariables(self):
        return self._variables
    
    def getDomainValues(self,var):
        return self._domainOfVariable[var]

    def getConstraints(self,var):
        if var not in self._contraintsOfVariable:
            return []
        return self._contraintsOfVariable[var]
    
    def getVariableDomains(self):
        return self._domainOfVariable
    
    def setVariableDomains(self,domainOfVariable):
        self._domainOfVariable = domainOfVariable
        
    def copy(self):
        variables = copy.deepcopy(self._variables)
        domains = copy.deepcopy(self._variables)
        constraints = copy.deepcopy(self._variables)
        csp = CSP(variables, domains, constraints)
        return csp
    
    def getNeighbour(self,variable,constraints):
        neigh = []
        for va in constraint.getScope():
            if va != variable and (va not in neigh):
                neigh.append(va)
                return neigh
        
    def removeValueFromDomain(self,variable,value):
        values = []
        for val in self.getDomainValues(variable):
            if val != value:
                values.append(val)
                self._domainOfVariable[variable] = values

    def printboard(self,n,values,list1):
        
        values=[]
        print("Initial Board:")
        for i in range(n*n):
            list1.append('A')
        for j in range(len(domains)):
            values.append(domains[j])
            list1[int(str(values[j]))]='K'
        
        print(np.reshape(list1,(n,n)))
        
    def knighttour(K,k_index,movex,movey,list1,n):
        nm=n*2
        for j in range(len(list1)):
            
            if K=='K':
               
                if list1[j]==list1[k_index]:
                    print("Moving ",list1[k_index],"at at index ",k_index)
                    
                    
                    if movex==2:
                        list1[k_index]='A'
                        
                    if movey==1:
                        list1[j-n+2]="K"
                        break
                    
                    if movey==-1:
                        list1[j+2+n]="K"
                        break
                    
                        
                    elif movex==-2:
                        list1[j]='A'
                      
                    if movey==1:    
                        list1[j+n-2]="K"
                            
                    if movey==-1:    
                        list1[j-2-n]="K"
                        break
                        
                    elif movey==-2:
                        list1[k_index]="A"
                     
                    if movex==1:
                        list1[j+nm-1]="K"
                        break
                    
                    elif movey==2:
                        list1[k_index]="A"
                        
                    if movex==1:
                        list1[j-nm+1]="K"
                        break
                       
                    if movex==-1:
                        list1[j-nm-1]="K"
                        break  
        print(np.reshape(list1,(n,n)))
         
if __name__ == '__main__':
    
    
    
    
    K1 = variable.Variable("K1")
    K2 = variable.Variable("K2")
    K3 = variable.Variable("K3")
    K4 = variable.Variable("K4")
    K5 = variable.Variable("K5")
    variables = [K1,K2,K3,K4,K5]
    domains = [1,3,5,8,11]
    n=6
    list1=[]
    CSP.printboard(n,n,domains,list1)
    
      
       
    
    CSP.knighttour('K',1, 1, -2,list1,n)    
    CSP.knighttour('K',3, 2, 1,list1,n)
    CSP.knighttour('K',5, -1, 2,list1,n)
    CSP.knighttour('K',8, 2, -1,list1,n)
    CSP.knighttour('K',11, 1, 2,list1,n)
    CSP.knighttour('K',1, -2, 1,list1,n)
    CSP.knighttour('K',3, -2, 1,list1,n)
    CSP.knighttour('K',5, 1, -2,list1,n)
    CSP.knighttour('K',8, 1, -2,list1,n)
    CSP.knighttour('K',11, -1, 2,list1,n)
    CSP.knighttour('K',11, -1, -2,list1,n)
   
    
    '''

    CSP.knighttour('K',1, 1, -2,list1,n)    
    CSP.knighttour('K',3, 2, 1,list1,n)
    CSP.knighttour('K',5, -1, 2,list1,n)
    CSP.knighttour('K',8, 2, -1,list1,n)
    CSP.knighttour('K',11, 1, 2,list1,n)
    CSP.knighttour('K',1, -2, 1,list1,n)
    CSP.knighttour('K',3, -2, 1,list1,n)
    CSP.knighttour('K',8, 1, -2,list1,n)
    CSP.knighttour('K',11, -1, 2,list1,n)
    CSP.knighttour('K',11, -1, -2,list1,n)
    
'''
        
    
   
   
    Csp = CSP(variables,domains,constraints)
    inPro = forwardCheckingInference.ForwardCheckingInference()
    bts = backtrackingSearch.BactrackingSearch(inPro,[consoleListener.ConsoleListener()],variableOrdering = False)
    start = time.time()
   
    end = time.time()
    print("%.2f ‐ %.2f" % (start,end))
    
   
   
    

        
'''
Created on Mar 6, 2019

@author: dr.aarij
'''
class Variable(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        
        self._name = name
    
    def getName(self):
        return self._name
    
    def __eq__(self, other):
        return self.getName() == other.getName()
    
    def __hash__(self):
        return hash(self._name)
    
    def __str__(self):
        return self._name
    
    
    '''
                         if movey==1:
                            list1[j+2+n]="K"+str(j)
                        
                        if movey==-1:
                             list1[j+2-n]="K"+str(j)    
                            
                        if movex==-2:
                            list1[j]='A'
                        
                      .  if movey==1:    
                            list1[j+n-2]="K"+str(j)
                            
                       .. if movey==-1:    
                            list1[j-2-n]="K"+str(j) 
                        
                        if movey==-2:
                            list1[j+2+n]="K"+str(j)
                        
                     
                        if movex==-2:
                               list1[j]='A'
                               list1[j+6-1]="K"+str(j)
                        
                        if movey==2:
                              list1[j-2+n]="k"+str(j)
                        
                        if movey==-2:
                              list1[j+2+n]="k"+str(j)
                        
                        if movey==-2:
                            list1[j]='A'
                            list1[j-12]="K1v"    
        print(np.reshape(list1,(n,n)))
         
        
    CSP.knighttour('K1',2,-1,list1,n)
    CSP.knighttour('K2',2,1,list1,n)
    CSP.knighttour('K5',1,2,list1,n)
    CSP.knighttour('K3',-2,1,list1,n)
    CSP.knighttour('K2',2,-1,list1,n)
    CSP.knighttour('K4',1,-2,list1,n)

        
    
    
    
    
    
    '''
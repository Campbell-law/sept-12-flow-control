# Sept 19 Flow Control

## [Chapter 2 Flow Control](https://automatetheboringstuff.com/chapter2/)

# Fork this Repo clone it to your drive and do the exercises at:  [sept-19.py](https://github.com/Campbell-law/sept-19-flow-control/blob/master/sept-19.py)

# If Then Else Flowcharts

![XKCD](https://github.com/Campbell-law/sept-19-flow-control/blob/master/flowcharts.png)

## A basic If statement

![if](https://github.com/Campbell-law/sept-19-flow-control/blob/master/if_Python.jpg)

```
n = 10
if (n > 15): 
   print ("10 is less than 15") 
print ("I am Not in if") 
```
## If with an Else
![if_else](https://github.com/Campbell-law/sept-19-flow-control/blob/master/if_else.jpg)

```
n = 20; 
if (n < 15): 
    print ("n is smaller than 15") 
    print ("n is in if Block") 
else: 
    print ("n is greater than 15") 
    print ("n in else Block") 
print ("n not in if and not in else Block") 
```
## If Else Elif

![ladder](https://github.com/Campbell-law/sept-19-flow-control/blob/master/if-elseif-ladder.jpg)
```
n = 20
if (n == 10): 
    print ("i is 10") 
elif (n == 15): 
    print ("i is 15") 
elif (n == 20): 
    print ("n is 20") 
else: 
    print ("n is not present") 
```
## Nested Ifs

![nested](https://github.com/Campbell-law/sept-19-flow-control/blob/master/nested-if.jpg)
```
n = 10
if (n == 10): 
    #  First if statement 
    if (n < 15): 
        print ("n is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (n < 12): 
        print ("n is smaller than 12 too") 
    else: 
        print ("n is greater than 15")  
```
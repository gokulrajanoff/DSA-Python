
names = ['test','orange','apple']

print(names[::1])

defaultBool = bool()
print(defaultBool)

zeroNumber = 0
negactiveNumber = -5
positivenumber = 10

if not zeroNumber:
    print('its zero number')

if negactiveNumber:
    print('its a negactive number')
    
if positivenumber:
    print('positive number')

emptyString = ""
print ( type(emptyString))
if not emptyString:
    print('its empty string')

emptyList = []
print ( type(emptyList))
if not emptyList:
    print('its empty list')

emptySet = set();
print ( type(emptySet))
if not emptySet:
    print('its empty set')

emptyTuple = ();
print ( type(emptyTuple))
if not emptyTuple:
    print('its empty tuple')

emptyDict = {}
print ( type(emptyDict))
if not emptyDict:
    print('its empty dict')

basicInteger = int()
print(basicInteger) # 0
basicBinary = 0b0011
print(basicBinary) # 3
basicOcta = 0o52 # 42
print(basicOcta)
basicHexa = 0x7f # 127
print(basicHexa)

floatToInt = int(3.99)
print('floored values ',floatToInt)

stringToInt = int('134')
print(stringToInt)

#wrongStringToInt = int('hello')
#print(wrongStringToInt)  ValueError: invalid literal for int() with base 10: 'hello'

baseConversion = int('f',16)
print(baseConversion) # 15


expoFlot = 6.022e23
print(expoFlot)

emptyFloat = float()
print(emptyFloat)

stringFloat = float('3.14')
print(stringFloat)


# list

basicList = []
basicList.append(1)
basicList.append(2)
print(basicList)

basicTuple = (4,5,6);
#basicTuple[0]=6; Error : TypeError: 'tuple' object does not support item assignment
print('basicTuple',basicTuple)
print(basicTuple[0]);

singleTuple = (1); # even though error is not comming , dont use this
# print(' singleTuple length',len(singleTuple)) TypeError: object of type 'int' has no len() 
singleTupleWithComma = (1,)
print('singleTupleWithComma length',len(singleTupleWithComma) )
print('singleTuple',singleTuple)

wordHellow = "hello"
stringToList = list(wordHellow)
backupReferenceList = stringToList
backupList = list(stringToList)
stringToList[-1] = 'W'
print('stringToList',stringToList) #['h', 'e', 'l', 'l', 'W']
print('backupReferenceList',backupReferenceList) # ['h', 'e', 'l', 'l', 'W']
print('backupList',backupList) # ['h', 'e', 'l', 'l', 'o']

singleQuoteString = 'test'
doubleQuoteString = "test 's"
tripleQuoteString = ''' this is a
    multiple line string'''

for x in "banana":
  print(x)

a = "Hello, World!"
print('length of a is ',len(a))

txt = "The best things in life are free!"
print('is free present in \'',txt,'\' string ? = ',("free" in txt))

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
# slicing
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!" 
print(b[2:5]) #llo
print(b[:5])  #Hello
print(b[2:])  #llo, World!
print(b[-5:-2]) #orl


print(singleQuoteString)
print(doubleQuoteString)
print(tripleQuoteString)

basicSet = {1,3,3,4,4,5,5,6}
print(basicSet)
basicSet = {wordHellow,'hello','world '}
print(basicSet) # {'world ', 'hello'}
stringToSet = set(wordHellow)  # {'h', 'e', 'o', 'l'}
print(stringToSet)

basicDict = {"ga":'irish','en':"english"}
print(basicDict)
keyVal1 = ('in','india')
keyVal2 = ('np','nepal')
countryDict = dict([keyVal1,keyVal2])
print('countryDict',countryDict)

numberA = 5
numberB = int('5')
numberC = None
numberD = None
numberAAlias = numberA
if(numberA is numberB):
    print('its equal to 5') # if executes

if(numberA is not numberC):
    print('not equal') # if executes
    
if((numberA <= 6 and numberB >= 1) or numberC != numberD):
    print('if execute ')


Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Name = 'Azie Melasari'
>>> NIM = 174
>>> High = 1.63
>>> Weight = 50
>>> YearOfBirth = 2000
>>> I = (YearOfBirth, Weight, High, NIM, Name)
>>> Data = [YearOfBirth, Weight, High, NIM, Name]
>>> type(I)
<class 'tuple'>
>>> ## because variable 'I' is a string data that has a row of objects with different data types so its including class 'tuple' but cannot be changed
>>> I[0]
2000
>>> ## because the index 0 from the variable 'I' is 2000
>>> a = NIM % 4; I[a]
1.63
>>> ##Because the variable 'a' is remaining results from the variable 'NIM' is 174 divided 4 with the remaining results is 2, then the program will print the value of variable 'I' on the index to variable 'a', which means the 2nd, which is 1.63
>>> type(I[a])
<class 'float'>
>>> ## because I[a] is 1.63, where this is including class'float'(decimal number)
>>> I[a:4]
(1.63, 174)
>>> ## because the variable 'I' starting from 2nd index that is 1.63 until to the limit which is 3rd index that is 174
>>> type(I[4])s
<class 'str'>
>>> ## because I[4] is the data type of the value of variable 'I' in the 4th index that is Name, and including class'str' or string.
>>> I[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    I[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ##I[0] = 'ok' cannot be executed because variable 'I' including class'tuple' because tuple is a type that cannot be changed (immutable)
>>> type(Data)
<class 'list'>
>>> ## because the variable 'Data' is a string data that has a row obeject with different data types but class'list' can be changed
>>> type(Data[4])
<class 'str'>
>>> ## because Data[4] is the data type of the value variable 'Data' in the 4th index that is 'Name', so that including class'str' or string
>>> Data[4][5]
'M'
>>> ## because Data[4][5] is 5th index value in the variabe'Data' at the 4th index, which is 'M'
>>> Data[4][a:6]
'ie M'
>>> ##because Data[4][a:6] is the value from index to 'a' (which means 2nd index) until to the limit 5th index in the variable 'Data' at the 4th index, which is 'ie M'
>>> Data[0] = 'ok'; Data
['ok', 50, 1.63, 174, 'Azie Melasari']
>>> ##because to change index 0 of the list of 'Data' that is 'YearOfBirth' to be 'ok'
>>> Data[-a]
174
>>> ##because Data[-a] giving output the variable'Data' on index 2nd but counts from right that is 174
>>> range(a)
range(0, 2)
>>> ##because giving output the range from 'start'(0) until 'a'(2)

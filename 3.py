Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Name = 'Azie Melasari'
>>> NIM = 'L200183174'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Name)
>>> type(a)
<class 'int'>
>>> ##because the variable 'X' is a string has been converted into an integer using a variable int()
>>> type(b)
<class 'int'>
>>> ##because variable 'b' calculate the number of all members the variable 'Name' and including in the type integer
>>> a / b
90.3076923076923
>>> ##because the variable 'a' is 1174 and the variable 'b' is 13, so that 1174 devided 13 is equal to 90.307....
>>> a // b
90
>>> ##because the variable 'a' divide the variable 'b', after that the result changed from float(decimal number) to integer, so 90.30769... is rounded 90
>>> 10 * (a-999)
1750
>>> ##because the variable 'a' is 1174, after that reduced by 999 so the result is 175 and multiplied by 10 with the result 1750.
>>> b ** 2
169
>>> ##because the variable 'b' power of 2, so that 13 power of 2 is 169.
>>> a % b
4
>>> ##because % function to count the divide remainder after dividing the variable of a and b.
>>> c = 12.5
>>> ##variable 'c' is rated 12.5
>>> type(c)
<class 'float'>
>>> ##because 12.5 is including the decimal number, so that named class 'float'
>>> a / c
93.92
>>> ##because the variable 'a' is 1174 devide the variable 'c' is 12.5, so that 1174 devided 12.5 is equal to 93.92.
>>> a // c
93.0
>>> ##because the result from the variable 'a' divide the variable 'b' changed from float(decimal number) to integer, so 93.92 is rounded 93
>>> a % c
11.5
>>> ##because % function to count the devide remainder after dividing the variable of a and c.
>>> c >  b
False
>>> ##because the variable 'c' is 12.5 and variable 'b' is 13, so statement 'c' is greater then 'b' is False.
>>> type(c > b)
<class 'bool'>
>>> ##because c > b is a comparison that determines the result is True or False, so including class 'bool'
>>> a > b and b > c
True
>>> ##because the variable 'a' is 1174, variable 'b' is 13 and the variable 'c' is 12.5, then the statement 'a' is greater than 'b' and 'b' is greater than 'c'. So that the result is True.
>>> a > 1100 or b < 10
True
>>> ##because the variable 'a' is 1174 which is greater than 1100, so the statement a > 1100 is True while the variable 'b' is 13 which is greater than 10. So the statement b < 10 is False. 

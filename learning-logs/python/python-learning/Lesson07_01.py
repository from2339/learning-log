##①数値型
num01 = 123 #整数 int型
num02 = 1.23 #小数点 float型

print(type(num01)) #pythonのデータ型は、typeを使用して確認することができる
print(type(num02))



##②文字列型
string_a = "Hello,World!" #文字列型 string(str)型

print(string_a)
print(type(string_a))



##③ブール型
a = 10 #aという変数に10を代入
b = 1 #bという変数に1を代入

bool01 = (a > b) #a>bは正しい。結果をbool01に反映

print(bool01) #正しいのでTrueが表示される
print(type(bool01)) #ブール型であるboolが表示される

#逆にしてみる
a = 10 #aという変数に10を代入
b = 1 #bという変数に1を代入

bool01 = (a < b) #a<bは正しくない。結果をbool01に反映

print(bool01) #正しくないのでFalseが表示される
print(type(bool01)) #ブール型であるboolが表示される

name = "ada lovelace"
print(name)
print(name.title())
# name.title() 是对name这个变量进行title（）这个函数操作，首字母大写

print(name.upper())
#name.upper() 全部大写
print(name.lower())
#name.lower() 全部小写

name = "   a b c   "
print(name)
print(name.rstrip().lstrip())
#lstrip()删除字符串前面的空格
#rstrip()删除字符串后面的空格

#合并字符串
first_name="ada"
last_name="lovelace"
full_name=first_name+ " " +last_name
print(first_name)
print(last_name)
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.title())


#制表符 \t  换行符 \n

print("Languages:\nPython\nC\nJava")
print("Languages:\tPython\tC\tJava")
print("Languages:\n\t\tPython\n\t\tC\n\t\tJava")

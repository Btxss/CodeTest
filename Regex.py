# -*- coding: utf-8 -*-
from __future__ import unicode_literals
正则表达式

动机
1、文本处理已近成为计算机常见工作之一
2、对文本的搜索，定位，提取的逻辑往往比较复杂
3、为了快速解决上述问题，产生了正则表达式技术

定义：正则表达式即文本的高级匹配模式，提供搜索，替代，获取等功能。本质是由一系列特殊符号和字符构成的字串，这个字串就是正则表达式

特点：
1、方便进行检索和修改等文本操作
2、支持语言众多
3、灵活多样

目标：
1、能熟练掌握所有正则表达式符号
2、能够编写简单的正则表达式，读懂较复杂的正则表达式
3、能够用python re模块操作正则表达式

正则表达式匹配手段
通过设定有特殊意义的符号，描述符号和字符的重复行为及位置特征来表示一类特定规则的字符串

python - --> re模块    处理正则表达式

re.findall(pattern, string)
pattern：以字符串的形式传入一个正则表达式
string：要匹配的目标字符串
返回值：得到列表，将目标字串中能用正则表达式匹配的内容放入列表

正则表达式元字符
1、普通字符匹配（除了后续讲解的特殊字符全是普通字符）
    元字符：   a   b   c   &   #
    匹配规则 ： 匹配字符本身
        re.findall("abc", "abcsgfsdfab")
        ['abc']
        re.findall("ab", "abcsgfsdfab")
        ['ab', 'ab']
2、或
    元字符：|
    匹配规则：匹配符号两侧的任意一个正则表达式
        re.findall("ab|cd", "abcdefghabi")
        ['ab', 'cd', 'ab']
        re.findall("ab | bc", "abcdefghijk")
        []
3、匹配单个字符
    元字符： .
    匹配除 \n 外任意一个字符
    f.o - --> foo fao f@o
        re.findall("f.o", "foo,fao is not fbo")
        ['foo', 'fao', 'fbo']
4、匹配开始位置
    元字符：^
    匹配规则：匹配字符串的开头位置
        re.findall("^Jame", "hi,Jame")
        []
        re.findall("^Jame", "Jame,how are you")
        ['Jame']
5、匹配结束位置
    元字符：$
    匹配规则：匹配目标字符串的结束位置
        re.findall("py$", "hello.py")
        ['py']
        re.findall(".+py$", "hello.py")
        ['hello.py']
6、匹配重复
    元字符：*
    匹配规则：匹配前面出现的字符0次或多次
    fo * ---> f fo fooooooooooooooooo
        re.findall("fo*", "f,ff,foo,fffff")
        ['f', 'f', 'f', 'foo', 'f', 'f', 'f', 'f', 'f']
7、匹配重复
    元字符：+
    匹配前面出现的正则表达式一次或多次
    ab + ---> ab  abbbb
        re.findall("ab+", "ababababab")
        ['ab', 'ab', 'ab', 'ab', 'ab']
8、匹配重复
    元字符：?
    匹配前面出现的正则表达式零次或一次
    ab? - -> a ab
        re.findall("ab?", "abce,asdabbbb")
        ['ab', 'a', 'ab']
9、匹配重复
    元字符：{n}
    匹配规则：匹配前面的正则出现n次
    ab{3} - --> abbb
10、匹配重复
    元字符：{m，n}
    匹配规则：匹配前面的正则 m - n 次
    ab{3, 5} - --> abbb  abbbb  abbbbb
        re.findall("ab{3,5}", "ab,abbb,abbbbb,abbbbbbbbbb")
        ['abbb', 'abbbbb', 'abbbbb']
        re.findall(".{1,3}..{1,3}..{1,3}..{1,3}", "192.168.1.2")
        ['192.168.1.2']
11、匹配字符集合
    元字符：[字符集]
    匹配规则：匹配字符集中任意一个字符
    [a, b, c] - --> a b c
        re.findall("[a,b,c]", "abcashghgcvcb")
        ['a', 'b', 'c', 'a', 'c', 'c', 'b']
    [0 - 9] [a - z] [A - Z] [0 - 9a - z] [_abc0 - 9]
    	re.findall("^[A-Z][a-z]*", "Hello world")
    	['Hello']
12、匹配字符集
    元字符：[^ ...]
    匹配规则：匹配除了中括号中字符集字符之外的任意一个字符
    	re.findall("[^0-9]+", "hello1")
    	['hello']
13、匹配任意（非）数字字符
    元字符：\d   \D
    匹配规则：\d 匹配任意一个数字字符      [0 - 9]
              \D 匹配任意一个非数字字符    [^ 0-9]
14、匹配任意（非）普通字符
    元字符：\w   \W
    匹配规则：\w  匹配一个普通字符
	      \W  匹配一个非普通字符
	re.findall("\w+","hello$1")
	['hello', '1']
15、匹配（非）空字符
    （空格 \r   \n   \t   \v   \f）
    元字符： \s   \S
    匹配规则：\s  匹配任意空字符
	      \S  匹配任意非空字符
	re.findall("\w+\s+\w+","hello   world")
	['hello   world']
        re.findall("\S+","hi#%$  ash*&(")
        ['hi#%$', 'ash*&(']
16、匹配起始位置
    元字符：\A    \Z
    匹配规则：\A  匹配字符串开头位置
	      \Z   匹配字符串结尾位置
	re.findall("\Ahi","hi.hello")
	['hi']
	re.findall("hi\Z","working.hi")
	['hi']
	完全匹配：使用一个正则表达式可以匹配目标字符串的全部内容
	re.findall("\A\w{5}\d{3}\Z","abcde123")
17、匹配（非）单词边界 (前面加r)
    （普通字符和非普通字符交界处称单词边界）
    元字符：\b    \B
    匹配规则：\b  匹配单词边界位置
	      \B  匹配非单词边界位置
	re.findall(r"\bis\b","this is a test")
	['is']  #第二个is
	re.findall(r"\Bis\b","this is a test")
	['is']  #第一个is
	re.findall(r"htc01\b","htc01@1996")
	['htc01']
元字符总结：
	匹配单个字符的：a . [...] [^...] \d  \D  \w  \W  \s  \S
	匹配重复的：* + ？ {n} {m,n}
	匹配位置：^  $  \A  \Z  \b  \B
	其他： |  （）  \	
 
正则表达式的转义
正则表达式特殊字符
. * $ ? ^ [] {} () \
在正则表达式中如果要匹配这些特殊字符需要进行转义
	re.findall("\[\d+\]","abc[123]")
	['[123]']

raw字符串 ---> 原始字符串
特点：对字符串中的内容不进行转义，即表达原始含义
r"\b" ---> \b
"\\b" ---> \b
	re.findall(r"\w+@\w+\.cn","lves@tedu.cn")
	['lves@tedu.cn']

贪婪和非贪婪
贪婪模式：正则表达式的重复匹配，总是尽可能多的向后匹配内容
*    +   ？   {m.n}
贪婪 ---> 非贪婪（懒惰）
*?  +?  ??  {m，n}?

正则表达式分组
使用（）可以为正则表达式建立子组，子组不会影响正则表达式整体的匹配内容，可以被看做是一个内部单元。
abcdef  --->  abcdef
(ab)cd(ef) --->  abcdef
(ab)cd(ef)+ --->  abcdefefefefefef
ab+ --->  abbbbb
(ab)+ ---> ababababab

子组内部作用
1、形成内部整体，改变某些元素符的行为
	re.search(r"\w+@\w+\.com|cn","xixi@haha.cn").group()
	'cn'
	re.search(r"\w+@\w+\.(com|cn)","xixi@haha.cn").group()
	'xixi@haha.cn'
	re.search(r"(ab)+","ababababab").group()
	'ababababab'
	re.search(r"\w+@\w+\.com","xixi@haha.com").group()
	'xixi@haha.com'
2、子组匹配内容可以被单独获取
	re.search(r"\w+@\w+\.(com|cn)","xixi@haha.cn").group(1)
	'cn'
	re.search(r"\w+@\w+\.(com|cn)","xixi@haha.com").group(1)
	'com'

子组注意事项
*一个正则表达式中可以有多个子组，区分第一，第二...子组
*子组不要出现重叠的情况，尽量简单（ab(c）de)f

捕获组和非捕获组（命名组，未命名组）
命名格式：（?P<name>pattern）
	re.search(r"(?P<dog>ab)+","ababab").group()
	'ababab'
	re.search(r"(?P<dog>ab)+","ababab").groupdict()
	{'dog': 'ab'}

作用：
1、方便通过名字区分每个子组
2、捕获组可以重复调用  格式：（?P=name）
e.g.  (?P<dog>ab)cd(?P=dog)  ===>  abcdab
正则表达式的匹配原则、
1、正确性   能够正确匹配目标字符串
2、唯一性   除了匹配的内容尽可能不会有不需要的内容
3、全面性   对目标字符串可能的情况要考虑全面不遗漏
	re.search(r"\d{18}","888888888888888888").group()
	'888888888888888888'
	re.search(r"\d{17}(\d|x)","888888888888888888").group()
	'888888888888888888'

re模块的使用
regex = compile(pattern, flags = 0)
功能：生成正则表达式对象
参数：pattern 正则表达式
      flags 功能标志位，丰富正则表达式的匹配
返回值：返回一个正则表达式对象   
    
re.findall(pattern, string, flags=0)
功能：根据正则表达式匹配目标字串内容
参数：pattern 正则表达式
      string 目标字符串
返回 ： 返回一个列表，内部为匹配到的内容
* 如果正则表达式有分组则只显示子组内容

regex.findall(string,pos,endpos)
功能：根据正则表达式匹配目标字串内容
参数:string 目标字符串
     pos，endpos 截取目标字符串的起止位置进行匹配，默认是整个字符串
返回：返回一个列表，内部为匹配到的内容
* 如果正则表达式有分组则只显示子组内容

re.split(pattern, string, maxsplit=0, flags=0)
功能：通过正则表达式切割目标字符串
参数：pattern 正则表达式
      string 目标字串
返回值：以列表形式返回切割后的内容

re.sub(pattern, replace, string, count=0, flags=0)
功能：替换正则表达式匹配内容
参数：pattern  正则表达式
      replace  要替换的参数
      string   目标字符串
      count    设定最多替换几处
返回值：替换后的字符串

re.subn(pattern, repl, string, count=0, flags=0)
功能和参数同sub
返回值多一个实际替换了几处

re.finditer(pattern, string, flags=0)
功能：使用正则匹配目标字串
参数：pattern  正则表达式
      string   目标字串
返回值：迭代对象 --->  迭代内容为match对象（match object）

re.fullmatch(pattern, string, flags=0)
功能：完全匹配一个字符串
参数：pattern  正则表达式
      string   目标字串
返回值：match对象，匹配到内容（match object）

re.match(pattern, string, flags=0)
功能:匹配一个字符串的起始内容
参数：pattern  正则表达式
      string   目标字符
返回值：match对象，匹配到的内容（match object）
  
re.search(pattern, string, flags=0)
功能：匹配第一个符合条件的字符串
参数：pattern  正则表达式
      string   目标字符
返回值：match对象，匹配到的内容（match object）

    template(pattern, flags=0)
        Compile a template pattern, returning a pattern object


compile生成的正则对象regex属性

pattern     正则对象对应的正则表达式
flags       获取标志位值
groupindex  获取捕获组形成的字典 组名为键，第几组为值
	regex = re.compile(r"(?P<dog>ab)cd(?P<pig>ef)")
groups      子组个数


作业：
1. 读取一个文本，
	将文本中所有以大写字母开头的单词匹配出来，
	将文本中数字匹配出来 数字类型：234 -12 1.23 1/2
2. 熟练掌握元字符的匹配规则
3. 将findall  finditer  match  search  sub  split fullmatch  使用compile方法进行调用
4. 看一下之前的项目


***********************************regex1.py******************************
match object 属性函数
属性变量
pos		目标字符串的起始位置
endpos		目标字符串的结束位置
re		生成正则表达式
string		生成目标字符串
lastgroup	最后一组的名称
lastindex	最后一组是第几组
属性方法
span()		匹配内容的起止位置
start()		匹配内容的开始位置
end()		匹配内容的结束位置
group(n=0)
功能：获取match对象对应的匹配内容
参数：默认为0，表示获取整体的匹配内容。如果赋值1,2,3...表示获取第n个子组匹返回：返回获取到的内容字串

groupdict()获取左右捕获组匹配内容，形成一个字典
groups()获取所有子组匹配到的内容

flags参数
compile   re.findall   re.search  re.match
re.finditer   re.fullmatch  re.sub   re.subn  re.split
作用：辅助正则表达式，扩展丰富匹配内容
I == IGNORECASE  忽略大小写
S == DOTALL      元字符 .能够让点匹配\n
M == MULTILINE   元字符^ $可以匹配每行的开头结尾
X == VERBOSE     可以给正则添加注释

多个标志位可以用 | 隔开
flags = re.X | re.I

要求
编写一个程序接口，通过传入端口名称可以获取地址信息
文档特征：每个端口占一段，每段之间有空行，端口






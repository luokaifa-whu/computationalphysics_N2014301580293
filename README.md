#**2016武汉大学计算物理作业**

###[课程要求](https://github.com/caihao/computational_physics_whu/blob/master/README.md)

--------------------

###**作业列表**
**一、[2月24日第一次作业](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md)**

1. 安装linux系统（已安装双系统——Ubuntu 14.04)<br/>
2. 安装python 2.7 运行环境（已安装）<br/>
3. 注册github 账号，关注caihao（已Marked并star)<br/>
4. 按照markdown语法书写自己的第一个README.md(完成)<br/>
   附：<br/>
   [How to think like a computer scientist](http://www.openbookproject.net/thinkcs/python/english2e/)<br/>
   [Markdown语法说明](http://www.appinn.com/markdown/#p)<br/>
   [git使用简易指南](http://www.bootcss.com/p/git-guide/)<br/>
   [Python2.7 教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)<br/>

--------------------

**二、3月2日第二次作业**

1. 下载某大神学长的  [插件](https://github.com/Ron89/thesaurus_query.vim)<br/>
2. 用Github生成图片外链——(Markdown控制不了图片尺寸，一不小心占地面积过大)
   ![迷の卷福](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/QQ.20160308141916.png)
3. 使用[Learning with Python](http://interactivepython.org/runestone/static/thinkcspy/index.html)练习Python

--------------------

**三、3月9日第三次作业**

1. 使用字符在显示屏幕上组合并显示出名字的正序、倒序、乱序
2. 制作由字符形成的动态图形——即原始的显示屏扫描

##计算物理2016.03.09第三次作业##
----------------
###1.在屏幕上显示由符号排列组合形成的字母或其它符号
    原理是利用Python中的字典功能将所要显示的字母以分行阵列的形式储存，后用print命令输出即可。
    如果储存26个字母的对应字典，则可实现任意字母以任意顺序输出。
    例图：<br/>
    ![正序](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/%E6%AD%A3%E5%BA%8F.png)<br/>
    ![逆序](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/%E9%80%86%E5%BA%8F.png)<br/>
    ![乱序](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/%E9%80%86%E5%BA%8F.png)
    ![心形](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/%E5%BF%83%E5%BD%A2.png)<br/>
    *代码如下：*
line1={'L':' #          ','K':' #       # ','A':'        #        ','F':' #########  ','I':'  #####   ','U':'  #         #','O':'    #####    ','m':'   ##          ##   ',' ':'           '}
line2={'L':' #          ','K':' #     #   ','A':'       # #       ','F':' #          ','I':'    #     ','U':'  #         #','O':'  #       #  ','m':' #     #     #    # ',' ':'           '}
line3={'L':' #          ','K':' #   #     ','A':'      #   #      ','F':' #          ','I':'    #     ','U':'  #         #','O':' #         # ','m':'#         #        #',' ':'           '}
line4={'L':' #          ','K':' # #       ','A':'     #     #     ','F':' #########  ','I':'    #     ','U':'  #         #','O':' #         # ','m':'#                  #',' ':'           '}
line5={'L':' #          ','K':' # #       ','A':'    #########    ','F':' #          ','I':'    #     ','U':'  #         #','O':' #         # ','m':' #                # ',' ':'           '}
line6={'L':' #          ','K':' #   #     ','A':'   #         #   ','F':' #          ','I':'    #     ','U':'  #         #','O':' #         # ','m':'   #            #   ',' ':'           '}
line7={'L':' #          ','K':' #     #   ','A':'  #           #  ','F':' #          ','I':'    #     ','U':'   #       # ','O':'  #       #  ','m':'      #       #     ',' ':'           '}
line8={'L':' ########## ','K':' #       # ','A':' #             # ','F':' #          ','I':'  #####   ','U':'     #####   ','O':'    #####    ','m':'          #         ',' ':'           '}
line=[line1,line2,line3,line4,line5,line6,line7,line8]
name=raw_input('What do you want to type?')    # let the user to input characters
i,j=1,1          #set the loop variables
while i<=9 :     #this loop can display the charaters or some marks
    line_print = ''
    while j<=len(name) :
        line_print=line_print+line[i-1][name[j-1]]
        j=j+1
    print line_print
    j=1          
    i=i+1       #reset the loop variables
    
------------------------------
###2.在屏幕上显示由字符组合而成的特定动图

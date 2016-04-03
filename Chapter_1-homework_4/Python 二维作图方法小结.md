###Python 二维作图方法小结
    first of all:
     %pylab     #导入matplotlib和numpy

####1.1 plot二维图    
    %matplotlib qt5
    x = linspace(0, 2 * pi, 50)    #设置x轴的起止点及计算步长
    plot(sin(x))             #作出sinx在笛卡尔坐标系中的函数图像
    plot(x, sin(x), 'b-o', x, sin(2 * x), 'r-^')    #作出sinx和sin2x的图像
####1.1.1 
   函数：linspace(x1,x2,N)
   功能：linspace是Matlab中的均分计算指令，用于产生x1,x2之间的N点行线性的矢量。
  其中x1、x2、N分别为起始值、终止值、元素个数。若默认N，默认点数为100。
 类似的函数还有 logspace。
####1.1.2 （python)plot画图的颜色线型
<table>
        <tr>
                <td>
                        y         黄色            --           长虚线
                </td>
        </tr>
        <tr>
                <td>
                        m        粉红             ○            圈线   
                </td>
        </tr>
        <tr>
                <td>
                        c         亮蓝             ×            ×线    
                </td>
        </tr>
        <tr>
                <td>
                        r          大红            ＋          ＋字线 
                </td>
        </tr>
        <tr>
                <td>
                        g         绿色             －           实线    
                </td>
        </tr>
        <tr>
                <td>
                        b         蓝色             *            星形线
                </td>
        </tr>
        <tr>
                <td>
                        w         白色             ：           虚线    
                </td>
        </tr>
        <tr>
                <td>
                        k         黑色            －.          点划线
                </td>
        </tr>
</table>
####1.1.3 作多张图
       e.g.
       t = linspace(0, 2*pi, 50)
       x = sin(t)
       y = cos(t)
       figure()     #产生一张空图1
       plot(x)      #在空图1上作出x的图像
       figure()     #产生一张空图2
       plot(y)      #在空图2上作出y的图像

####1.1.4 在一张图上作出多个图像
       语法：
       subplot(row, column, index)
       e.g.（其中x,y均由上例定义）
       subplot(1, 2, 1)    #将一张图纸分为水平两半，弹出空图框1
       plot(x)             #在空图框1上作出x的图像
       subplot(1, 2, 2)    #弹出空图框2
       plot(y)             #在空图框2上作出x的图像
![多图](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/Chapter_1-homework_4/%E5%A4%9A%E5%9B%BE.png)


#### 1.1.5 在原图上加新图&新图将原图覆盖
        语法：
        plot(x)
        hold(False)     #接下来作的图将覆盖x的图，注意F需大写
        plot(y)         
        hold(True)      #取消覆盖，接下来作的图将叠加在y的图上，注意T需大写   

####1.1.6 在图上添加坐标轴标签、标题、图例、网格
 #####坐标轴标签：
         xlabel('name')    #可以设置标签名和字体大小
         ylabel('name', fontsize='small/large/...')
#####标题：
    title('Sin(x)')
#####图例：         
     legend(['sin', 'cos'])
#####网格：
     grid()

####1.2 scatter散点图
     语法：
     scatter(x, y)
     scatter(x, y, size)
     scatter(x, y, size, color)
     e.g.
     x = rand(200)
     y = rand(200)
     size = rand(200) * 30
     color = rand(200)
     scatter(x, y, size, color)     # 显示颜色条
     colorbar()
     out:
![散点图](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/Chapter_1-homework_4/%E6%95%A3%E7%82%B9%E5%9B%BE.png)

####1.3 直方图
     语法：hist(array())
     e.g.<br/>
     hist(randn(1000))   #从高斯分布随机生成1000个点得到的直方图
![直方图](https://raw.githubusercontent.com/luokaifa-whu/computationalphysics_N2014301580293/master/Chapter_1-homework_4/%E7%9B%B4%E6%96%B9%E5%9B%BE.png)
   

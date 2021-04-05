'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-04-05 23:35:43
LastEditors: TianyuYuan
LastEditTime: 2021-04-06 00:06:02
'''
from tykit import rlog

rlog.start('欢迎使用tykit :toolbox:，tykit目前含有丰富的进度条打印方法，以及五颜六色的记录打印方法。\
帮您更好的了解任务进度、使用多进程、展示任务日志等',title='欢迎使用👏',align='center',padding=1)
rlog.say("您可以这样来展示一个任务或状态的开始：rlog.start('Task one start!',align='center)")
rlog.start('Task one start!',align='center')
rlog.say("您也可以打印一条横线，来展示某一阶段的结束: rlog.stage('Stage 1 ended, Stage 2 start!')")
rlog.stage('Stage 1 ended, Stage 2 start!')
rlog.caution('您可以用`rlog.caution()`函数输出一些需要注意的消息，提示将以蓝色表示')
rlog.error('或是用红色来输出一些错误和警告:skull:')
rlog.stage()
rlog.say("当然，还包括如何输出这样一段简单的话：rlog.say('当然，还包括如何输出这样一段简单的话：...')")
rlog.say("又或是调用rlog.saynum来展示文本+变量的提示：")
rlog.caution("var a = 1;\nrlog.saynum('var a is :',a)",title="rlog.saynum()的用法")
a = 1
rlog.saynum('var a is :',a)
rlog.done("Thanks for reading, hope you enjoy it! :smile:",title="感谢🙏",align='center',padding=1)

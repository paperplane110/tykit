<!--
 * @Description: 
 * @version: 
 * @Author: TianyuYuan
 * @Date: 2021-04-02 15:42:10
 * @LastEditors: TianyuYuan
 * @LastEditTime: 2021-04-02 17:59:20
-->
# tykit (Tell You kit)👀

![Alt Text](./image/Kapture%202021-04-02%20at%2017.18.06.gif)

## 📜 Description
'Tell You kit' is a toolkit to monitor your scripts' status easily, which haves rich and pretty output for progress bar and console logs.
The tykit may support more decent output in the future

## 🌟 Features
### 🚀 ProgressBar 
for ***loop,range,multi-threading and multi-threading with multi-params***

> ___pb_range(*args)___
> ```python3
> from tykit import pb_range
> from time import sleep
> 
> # use pb_range just like range()
> for i in pb_range(50):
>    sleep(0.001)
> ```


<!--
 * @Description: 
 * @version: 
 * @Author: TianyuYuan
 * @Date: 2021-04-15 00:11:23
 * @LastEditors: TianyuYuan
 * @LastEditTime: 2021-04-15 01:02:33
-->
# 💻 FaceXClient API
`class FacexClient(builtins.object)`
   
***针对facex的客户端，可以发送请求返回应答，不用考虑请求格式***
   
## Methods defined here:
   
### __init__(self, ip, port, group_id='FacexClient-tyyuan')
       初始化一个facex的客户端
       - ip: 服务器的ip地址(ip可直接选择输入gpu204/gpu205/gpu206)
       - port: facex的服务端口
       - group_id: 注册照片的组名
   
### add(self, img_address, user_id, check=False) -> dict
       注册服务
       - img_address: abs path of the img
       - check: the swith of quality check
       - user_id
       - return: response
   
### add_dataset(self, dataset, to_register='register_images', to_id='name', check=False, orker=10)
       注册整个数据集，适用于注册一个n_samples.json or p_samples.json
       - dataset: 数据集的字典
       - to_register: 注册request_images or register_images
       - to_id: 以什么为user_id: img_name(without .jpg) or group_name
       - check: the swith of quality check
       - worker: 多线程的大小
       - return log_list: 返回注册记录列表
   
### add_samples(self, sample: dict, to_register: str, to_id: str, check: bool) -> dict
       注册sample
       - sample: 样本字典
       - to_register: 注册request_images or register_images
       - to_id: 以什么为user_id: img_name(without .jpg) or group_name
       - check: the swith of quality check
       - return: the response dict
   
### compare_1v1(self, img1_address, img2_address, threshold=80, check=False) -> bool
       比对1v1
       - img1_address,img2_address: abs path of the imgs
       - threshold: 阈值，大于此阈值则返回True
       - check: the switch of quality check
       - return: True: the same person
   
### compare_1vn(self, img_address, top_n=1, check=False, op=31) -> dict
       比对1vn
       - img_address: abs path of the img
       - top_n: 返回的最相似的个数
       - check: the swith of quality check
       - return: response
   
### compare_1vn_dataset(self, dataset: dict, to_compare='register_images', top_n=1, check=False, orker=10) -> list
       比对1vn 输入维度为sample
       - dataset:数据集
       - to_compare: 拿样本里的什么进行比对：register_images/request_images
       - top_n: 返回前n个结果
       - check: the switch of quality check
       - worker: 多线程的大小
       - return: 结果列表[{img_name1:r1},{img_name2:r2}.....]
   
### compare_1vn_samples(self, sample, to_compare, top_n, check) -> dict
       比对1vn 输入维度为sample
       - sample: 样本
       - to_compare: 拿样本里的什么进行比对：register_images/request_images
       - top_n: 返回前n个结果
       - check: the swith of quality check
       - return: {图片名：对比结果字典}
   
### get_box(self, img_address: str, check=True) -> dict
       从img_process的response中提取检测框的信息
       - img_address: abs path of the img
       - return: a dict contains the info of the box
   
### get_box_txt(self, txt_address: str, img_type=1) -> dict
       以txt为单位的提取图片检测框信息
       - txt_address: the abs address of txt: line: rgb (d) (ir)
       - return: ans = {txt_name:{img:box,img:box,...},txt_name:{...},...}
   
### get_feature(self, img_address) -> numpy.ndarray
       抽取图片的特征向量
   
### img_process(self, img_address: str, op=31) -> dict
       处理图片，获取face_info信息
       - img_address: abs path of the img
       - op: 返回那些信息
       - return: response
   
   ----------------------------------------------------------------------
## Static methods defined here:
   
### base64tondarray(feature)
       将64编码的特征转换成512维的特征向量
   
### img2base64(img_address: str) -> str
       读取图片地址，并将图片编码为base64
   
### open_dataset(dataset) -> dict
       打开数据集
   
### write_log(log_list: list, log_name='log')
       保存log记录，可用于
       compare_1vn_dataset
       add_dataset之后

# 🔍ParseNP API
`class ParseNP(builtins.object)`

解析标注结果(np_samples.json)工具包
   
## Static methods defined here:
   
### get_ids2index(data: dict) -> dict
       从data中获得ids和index的关系，方便后续用index直接修改p_data
   
### get_ids2sample(data) -> dict
        描述：获取以ids为key，所对应sample为val的dict
        - data: 由json导入后的np_samples.json
        - return: ids2sample{'ids':sample}
        - ⚠️注意：key是ids，与图片名不通用
   
### get_register2index(data) -> dict
       从data中获得register和index的关系，方便后续用index直接修改p_data
   
### get_register2sample(data) -> dict
       描述：获取以register为key，所对应sample为val的dict
       - data: 由json导入后的np_samples.json
       - return: register2sample{'register':sample}
       - ⚠️注意：key是图片名，带.jpg后缀
   
### get_request2index(data: dict) -> dict
       描述：获取以request为key，所对应index为val的dict
       - data: 由json导入后的np_samples.json
       - return: request2index={'request':sample_index}
       - ⚠️注意：key是图片名，带.jpg后缀
   
### get_request2sample(data) -> dict
       描述：获取以request为key，所对应sample为val的dict
       - data: 由json导入后的np_samples.json
       - return: request2sample={'request':sample}
       - ⚠️注意：key是图片名，带.jpg后缀
   
### read_json(json_path) -> dict
       读取json文件
   
### show_info(self, data, np='')
       展示np_samples的主要信息
   
### total_registers(self, data) -> int
       描述：统计data中有多少的register_images
       - data: 由json导入后的np_samples.json
       - return: register_images的总数
   
### total_requests(self, data) -> int
       描述：统计data中有多少的request_images
       - data: 由json导入后的np_samples.json
       - return: request_images的总数
   
### total_samples(self, data) -> int
       统计data中有多少个sample
   


# 🥑 NPsamples API
`class NPsamples(builtins.object)`

***对象化np_samples.json***

对标注结果np_samples的进一步抽象，以samples.son作为对象，集成删除，融合，显示信息等方法
   
## Methods defined here:
   
### __init__(self, jsonfile, np: str)
       对象化np_samples.json
       @params: jsonfile 可以是json的地址，或解析后的dict
       @params: np 是n_samples.json就填”n“，反之填”p“
   
### check_empty_sample(self) -> list
       检查是否有空注册照的情况，返回空注册照的sample_list
   
###   delete_registers(self, registers: list)
       将register列表中的register_image从data中删除
       @params: registers:list 需要删除的register图片的列表，注意列表中的每一项必须是egister_path（because list.remove）
       @return: void 副作用，改变了self.data
   
###   delete_requests(self, requests: list)
       将requests列表中的request_image从data中删除
       @params: requests 需要删除的request图片的列表，注意列表中的每一项必须是request_path
       @return: void 副作用，改变了self.data
   
###   delete_samples(self, samples: list)
       将samples列表中的sample从data中删除
       @params: samples:list 需要删除的samples列表
       @return: void Side-effect: self.data
   
###   delete_samples_by_registers(self, registers: list)
       将包含registers的sample从data中删除
       @params: registers:list 需要删除的register图片的列表，注意列表中的每一项必须是egister_path（because list.remove）
       @return: void 副作用，改变了self.data

###   merge_samples(self, sample1, sample2)
       融合两个sample
       @params sample1
       @params sample2
       @return: void
   
###   save_json(self, name='new_p_samples.json')
       以name为名保持json，name需要json后缀

> ## reference: ParseNP  
> ids2index(self) -> dict
> 
> ids2sample(self) -> dict
>   
> register2index(self) -> dict
>   
> register2sample(self) -> dict
>   
> request2index(self) -> dict
>   
> request2sample(self) -> dict
>   
> show_info(self) -> dict
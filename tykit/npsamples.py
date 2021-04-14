'''
Description: 对标注结果np——samples的进一步抽象，以samples.json作为对象，集成删除，显示信息等方法
version: 
Author: TianyuYuan
Date: 2021-04-14 23:00:45
LastEditors: TianyuYuan
LastEditTime: 2021-04-14 23:47:25
'''
from .parse_np import ParseNP
import json
import os.path as osp

class NPsamples():
    """
    ## 对象化np_samples.json
    对标注结果np_samples的进一步抽象，以samples.json作为对象，集成删除，显示信息等方法
    """

    def __init__(self, jsonfile, np:str):
        """
        对象化np_samples.json
        @params: jsonfile 可以是json的地址，或解析后的dict
        @params: np 是n_samples.json就填”n“，反之填”p“
        """
        if isinstance(jsonfile,str):
            self.data = ParseNP.read_json(jsonfile)
        elif isinstance(jsonfile,dict):
            self.data = jsonfile
        else:
            print("Unsupported sample file type: ",jsonfile)
        self.np = np
        self.total_samples = ParseNP.total_samples(self.data)
        self.total_requests = ParseNP.total_requests(self.data)
        self.total_registers = ParseNP.total_registers(self.data)

    def request2sample(self) -> dict:
        return ParseNP.get_request2sample(self.data)
    
    def request2index(self) -> dict:
        return ParseNP.get_request2index(self.data)

    def register2sample(self) -> dict:
        return ParseNP.get_register2sample(self.data)

    def register2index(self) -> dict:
        return ParseNP.get_register2index(self.data)
    
    def ids2sample(self) -> dict:
        return ParseNP.ids2sample(self.data)

    def ids2index(self) -> dict:
        return ParseNP.get_ids2index(self.data)

    def show_info(self) -> dict:
        ParseNP.show_info(self.data,np=self.np)

    def check_empty_sample(self) -> list:
        """检查是否有空注册照的情况，返回空注册照的sample_list"""
        empty_sample = []
        for sample in self.data['images']:
            register_list = sample['register_images']
            # request_list = sample['request_images']
            # ids = sample['ids'][0]
            # if not request_list:
            #     print(f"{ids} don't have any requests")
            if not register_list:
                empty_sample.append(sample)
        print("Find empty 'register' samples: ", len(empty_sample))
        return empty_sample

    def save_json(self,name="new_p_samples.json"):
        """以name为名保持json，name需要json后缀"""
        # p_samples.json 应该在保持之前检查是否有空注册照的情况
        if self.np == "p":
            empty_sample = self.check_empty_sample()
            if empty_sample:
                self.delete_samples(empty_sample)
        with open(name,"w") as fp:
            json.dump(self.data, fp, indent=4)
        print(f"The {name} has been saved!")
        self.show_info()

    def delete_requests(self, requests:list):
        """
        将requests列表中的request_image从data中删除
        @params: requests 需要删除的request图片的列表，注意列表中的每一项必须是request_path（because list.remove）
        @return: void 副作用，改变了self.data
        """
        print(f"Before deleting, {self.np}_data has requests: {self.total_requests}")
        print("There are {} requests should be deleted.".format(len(requests)))
        request2index = self.request2index()
        for request_path in requests:
            request_name = osp.basename(request_path)
            index = request2index[request_name]
            self.data['images'][index]["request_images"].remove(request_path)
        self.total_requests = ParseNP.total_requests(self.data)
        print(f"After deleting, {self.np}_data has requests: {self.total_requests}")

    def delete_registers(self, registers:list):
        """
        将register列表中的register_image从data中删除
        @params: registers:list 需要删除的register图片的列表，注意列表中的每一项必须是register_path（because list.remove）
        @return: void 副作用，改变了self.data
        """
        print(f"Before deleting, {self.np}_data has registers: {self.total_registers}")
        print("There are {} registers should be deleted.".format(len(registers)))
        register2index = self.request2index()
        for register_path in registers:
            register_name = osp.basename(register_path)
            index = register2index[register_name]
            self.data["images"][index]["register_images"].remove(register_path)
        self.total_registers = ParseNP.total_registers(self.data)
        print(f"After deleting, {self.np}_data has registers: {self.total_registers}")

    def delete_samples_by_registers(self,registers:list):
        """
        将包含registers的sample从data中删除
        @params: registers:list 需要删除的register图片的列表，注意列表中的每一项必须是register_path（because list.remove）
        @return: void 副作用，改变了self.data
        """
        print(f"Before deleting, {self.np}_data has samples: {self.total_samples}")
        register2sample = self.request2sample()
        dele_sample_list = []
        for register_path in registers:
            register_name = osp.basename(register_path)
            sample = register2sample[register_name]
            dele_sample_list.append(sample)
        dele_set = set(dele_sample_list)
        print("There are {} samples should be deleted".format(len(dele_set)))
        for sample in dele_set:
            self.data["images"].remove(sample)
        self.total_samples = ParseNP.total_samples(self.data)
        print(f"After deleting, {self.np}_data has samples: {self.total_samples}")

    def delete_samples(self, samples:list):
        """
        将samples列表中的sample从data中删除
        @params: samples:list 需要删除的samples列表
        @return: void Side-effect: self.data
        """
        print(f"Before deleting, {self.np}_data has samples: {self.total_samples}")
        dele_set = set(samples)
        print("There are {} samples should be deleted".format(len(dele_set)))
        for sample in dele_set:
            self.data["images"].remove(sample)
        self.total_samples = ParseNP.total_samples(self.data)
        print(f"After deleting, {self.np}_data has samples: {self.total_samples}")

    def merge_samples(self,sample1,sample2):
        """
        融合两个sample
        @params sample1
        @params sample2
        @return: void
        """
        
        return 0
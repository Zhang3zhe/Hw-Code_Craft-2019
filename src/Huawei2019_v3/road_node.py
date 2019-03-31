import channel_node


class road_node(object):
    # 初始化道路节点
    def __init__(self, data):
        # 原始的道路信息
        self.id = data[0]               # 道路的id
        self.length = data[1]           # 道路的长度
        self.limit_speed = data[2]      # 道路的最高限速
        self.channel_num = data[3]      # 道路的车道数
        self.from_cross_id = data[4]    # 道路的起始路口id
        self.to_cross_id = data[5]      # 道路的终止路口id
        self.is_duplex = data[6]        # 0表示单向车道,1表示双向车道

        # 引用
        self.road_next = None
        self.channel_ptr = None         # lane表示road_node的左右车道之一

    # 判断线路指针是否为空
    def is_channel_empty(self):
        return self.channel_ptr == None

    # 向道路节点中添加线路节点
    def append_channel(self):
        if self.is_channel_empty():
            for index in range(self.channel_num):
                channel = channel_node.channel_node(index + 1, self.length)
                if self.channel_ptr == None:
                    self.channel_ptr = channel
                else:
                    cur = self.channel_ptr
                    while cur.channel_next:
                        cur = cur.channel_next
                    cur.channel_next = channel


class road_list(object):
    # 初始化道路list
    def __init__(self):
        self.head = None

    # 判断是否为空
    def is_empty(self):
        return self.head == None

    # 计算road_list的长度
    def length(self):
        count = 0

        cur = self.head
        while cur:
            count += 1
            cur = cur.road_next

        return count

    # 添加原始数据放到road_list中
    def append_raw(self, item):
        index = 0
        while (index <= item[6]):
            node = road_node(item)
            node.append_channel()
            if index == 1:
                node.from_cross_id = item[5]
                node.to_cross_id = item[4]
            if self.is_empty():
                self.head = node
            else:
                cur = self.head
                while cur.road_next != None:
                    cur = cur.road_next
                cur.road_next = node
            index += 1

    # 根据指定的id和道路起始路口id寻找道路
    def search_from(self, road_id, from_cross_id):
        cur = self.head

        while cur != None:
            if ((cur.id == road_id) and (cur.from_cross_id == from_cross_id)):
                return cur
            cur = cur.road_next

        return False

    # 根据指定的id和道路终止路口id寻找道路
    def search_to(self, road_id, to_cross_id):
        cur = self.head

        while cur != None:
            if ((cur.id == road_id) and (cur.to_cross_id == to_cross_id)):
                return cur
            cur = cur.road_next

        return False

    # 根据道路起始路口id和终止路口id寻找道路
    def search_from_to(self,from_cross_id,to_cross_id):
        cur=self.head

        while cur!=None:
            if((cur.from_cross_id==from_cross_id)and(cur.to_cross_id==to_cross_id)):
                return cur
            cur=cur.road_next

        return False
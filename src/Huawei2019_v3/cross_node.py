import sys
import numpy


class cross_node(object):
    def __init__(self, data):
        # 原始的路口信息
        self.id = data[0]
        self.north = data[1] if data[1] >= 0 else 0     # 路口北的道路id
        self.east = data[2] if data[2] >= 0 else 0      # 路口东的道路id
        self.south = data[3] if data[3] >= 0 else 0     # 路口南的道路id
        self.west = data[4] if data[4] >= 0 else 0      # 路口西的道路id
        self.index = -1                                 # 将路口编号从0开始编号，以便匹配数组的下标从0开始

        # 引用
        self.cross_next = None
        self.road_north_from = None
        self.road_east_from = None
        self.road_south_from = None
        self.road_west_from = None

        self.road_north_to = None
        self.road_east_to = None
        self.road_south_to = None
        self.road_west_to = None

    # 连接路口的东南西北四个方向的道路，包括以该路口为起始点的和以该路口为终止点
    def link(self, road_list):
        self.road_north_from = road_list.search_from(self.north, self.id)
        self.road_east_from = road_list.search_from(self.east, self.id)
        self.road_south_from = road_list.search_from(self.south, self.id)
        self.road_west_from = road_list.search_from(self.west, self.id)

        self.road_north_to = road_list.search_to(self.north, self.id)
        self.road_east_to = road_list.search_to(self.east, self.id)
        self.road_south_to = road_list.search_to(self.south, self.id)
        self.road_west_to = road_list.search_to(self.west, self.id)


class cross_list(object):
    # 初始化
    def __init__(self):
        self.head = None

    # 判断cross_list是否为空
    def is_empty(self):
        return self.head == None

    # 计算长度
    def length(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.cross_next
        return count

    # 添加原始数据放到cross_list中
    def append_raw(self, item):
        node = cross_node(item)
        if self.is_empty():
            node.index = 0
            self.head = node
        else:
            cur = self.head
            index = 0
            while cur.cross_next != None:
                cur = cur.cross_next
                index += 1
            node.index = index + 1
            cur.cross_next = node

    # 用于连接每个cross_node的北东南西四个方向的道路，包括道路的起始和终止信息
    def link_road(self, road_list):
        cur = self.head

        while cur != None:
            cur.link(road_list)
            cur = cur.cross_next

    # 根据cross的id搜索节点
    def search(self, id):
        cur = self.head
        while cur != None:
            if cur.id == id:
                return cur
            cur = cur.cross_next
        return False

    # 根据道路和路口信息返回graph矩阵
    def init_graph(self, road_list):
        size = self.length()
        graph = numpy.zeros([size, size])

        for i in range(size):
            for j in range(size):
                graph[i][j] = sys.maxsize

        cur = road_list.head
        while cur != None:
            graph[self.search(cur.from_cross_id).index][self.search(cur.to_cross_id).index] = cur.length
            cur = cur.road_next

        return graph

    # 根据index返回路口的id
    ###############################################
    def search_by_index(self, index):
        cur = self.head
        while cur != None:
            if cur.index == index:
                return cur
            cur = cur.cross_next
        return False
    ###############################################

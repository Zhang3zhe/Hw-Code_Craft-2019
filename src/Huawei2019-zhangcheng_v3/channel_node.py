class channel_node(object):
    def __init__(self, id, max_entries):
        # 一个方向的一个小车道的信息
        self.id = id if id > 0 else 0           # 该方向的车道的id
        self.max_entries = max_entries

        # 引用
        self.channel_next = None

# class channel_list(object):
#     # 初始化一条道路的一个方向的所有车道
#     def __init__(self):
#         self.head=None
#         self.channel_list_next
#
#     #判断channel_list是否为空
#     def is_empty__(self):
#         return self.head==None
#
#     # 计算channel_list的长度
#     def length(self):
#         count=0
#
#         cur=self.head
#         while cur:
#             count+=1
#             cur=cur.road_next
#
#         return count

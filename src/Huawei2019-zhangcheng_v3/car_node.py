import Dijkstra


class car_node(object):
    def __init__(self, data):
        # 原始的车辆信息
        self.id = data[0]               # 车辆id
        self.leave = data[1]            # 车辆的始发路口id
        self.arrive = data[2]           # 车辆的终点路口id
        self.max_speed = data[3]        # 车辆的最高速度
        self.set_time = data[4]         # 车辆的计划出发时间

        # 需要的信息
        # self.dis_before_switch = 0      # 在车移动之前所在的位置
        # self.dis_after_switch = 0       # 车移动后的位置
        self.position = 0               # 车在当前车道的位置，从from_cross处记为0，车本身的长度为1
        self.actual_speed = -1          # 车的实际速度
        self.leave_time = -1            # 车的实际出发时间
        self.arrive_time = -1           # 车的实际到达时间
        self.run_time = -1              # 每辆车的实际运行时间

        # 引用
        self.car_next = None            # 指向下一个car_node
        self.from_road_ptr = None       # 指向车当前所在道路
        self.to_road_ptr = None         # 指向车将要行驶的道路
        self.last_cross_ptr = None      # 指向车上一个路口
        self.current_cross_ptr = None   # 指向车将要到达的路口
        self.next_cross_ptr = None      # 指向车将要到达的路口的再下一个路口，用于寻找to_road_ptr
        self.shortest_cross = []        # 指向车的最短路径

    #
    def link_cross(self, cross_list, car_cross_id):
        if (len(car_cross_id) == 3):
            self.last_cross_ptr = cross_list.search(car_cross_id[0])
            self.current_cross_ptr = cross_list.search(car_cross_id[1])
            self.next_cross_ptr = cross_list.search(car_cross_id[2])
        else:
            self.last_cross_ptr = cross_list.search(car_cross_id[0])
            self.current_cross_ptr = cross_list.search(car_cross_id[1])
            self.next_cross_ptr = None

    def link_road(self, road_list):
        if self.last_cross_ptr and self.current_cross_ptr:
            self.from_road_ptr = road_list.search_from_to(self.last_cross_ptr.id, self.current_cross_ptr.id)
        elif self.current_cross_ptr and self.next_cross_ptr:
            self.to_road_ptr = road_list.search_from_to(self.current_cross_ptr.id, self.next_cross_ptr.id)
        else:
            self.from_road_ptr = None
            self.to_road_ptr = None

    # 判断车的下一个路口是否已经到达目的路口
    def is_on_dest_road(self):
        cur_cross = self.current_cross_ptr
        while (cur_cross):
            if cur_cross.id == self.arrive:
                return 1
            else:
                return 0


class car_list(object):
    # 初始化
    def __init__(self):
        self.head = None

    # 判断list是否为空
    def is_empty(self):
        return self.head == None

    # 计算list的长度
    def length(self):
        count = 0
        current_node = self.head

        while current_node != None:
            count += 1
            current_node = current_node.car_next

        return count

    # 添加原始数据放到car_list中
    def append_raw(self, item):
        node = car_node(item)

        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.car_next:
                cur = cur.car_next
            cur.car_next = node

    # 连接车和道路
    def link_road(self, road_list):
        cur = self.head
        while cur != None:
            cur.link_road(road_list)
            cur = cur.car_next

    # 连接车和路口
    def link_cross(self, cross_list, car_cross_id):
        cur = self.head
        while cur != None:
            cur.link_cross(cross_list, car_cross_id)
            cur = cur.car_next

    def short_list(self, cross_list, P,D):
        cur = self.head

        while cur != None:
            shortest_cross = []  # 车最短路径所经过的路口节点
           #path, distance = Dijkstra.dijkstra(graph, cross_list.search(cur.leave).index,
                                              # cross_list.search(cur.arrive).index)

            distance = D[cross_list.search(cur.leave).index][cross_list.search(cur.arrive).index]
            path = [cross_list.search(cur.arrive).index,]
            k = cross_list.search(cur.arrive).index
            while k != cross_list.search(cur.leave).index:
                k = int(P[cross_list.search(cur.leave).index][k])
                path.append(k)
            path.reverse()
            #print(path)
            #print(distance)
            for index in range(len(path)):
                shortest_cross.append(cross_list.search_by_index(path[index]).id)
            print(shortest_cross)
            print(distance)
            cur.shortest_cross = shortest_cross
            cur = cur.car_next

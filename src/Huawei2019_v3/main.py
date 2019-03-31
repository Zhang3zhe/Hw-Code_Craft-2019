import data_io
import car_node
import road_node
import cross_node
import schedule


def main():
    # # 导入数据  测试数据
    # car_data=data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/car.txt')
    # road_data=data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/road.txt')
    # cross_data=data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/cross.txt')

    # 导入数据 config_1数据
    car_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config_1/car.txt')
    road_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config_1/road.txt')
    cross_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config_1/cross.txt')

    # 导入1-map-training-1数据
    # car_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/1-map-training-1/car.txt')
    # road_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/1-map-training-1/road.txt')
    # cross_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/1-map-training-1/cross.txt')

    # 1 初始化车辆、道路、路口的信息
    print('Start initialing ...')
    car_run_list = car_node.car_list()      # 开始运行的车辆，动态添加
    car_wait_list = car_node.car_list()
    for item in car_data:
        car_wait_list.append_raw(item)
    road_list = road_node.road_list()
    for item in road_data:
        road_list.append_raw(item)
    cross_list = cross_node.cross_list()
    for item in cross_data:
        cross_list.append_raw(item)
    print('initialization complete!')

    # 2 将整个地图的拓扑进行关联，包括道路与路口的连接，道路与车的连接，路口与车的连接
    cross_list.link_road(road_list)

    # 3 求所有车的最短路径
    graph = cross_list.init_graph(road_list)
    car_wait_list.short_list(cross_list, graph)

    # 4 开始调度 一辆车一辆车跑
    set_time = 0
    cur = car_wait_list.head
    answer=[]
    while cur != None:
        route,set_time = schedule.schedule_one_car(cur, road_list, cross_list, set_time)
        answer.append(route)
        cur = cur.car_next

    data_io.data_output_to_file("SDK/SDK/SDK/SDK_python/CodeCraft-2019/config_1/answer.txt",answer)
    print(set_time)


if __name__ == '__main__':
    main()

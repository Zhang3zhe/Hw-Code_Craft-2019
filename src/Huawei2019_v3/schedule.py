def schedule_one_car(car, road_list, cross_list, set_time):
    route = [car.id]
    while (car.set_time > set_time):  # 该车是否上路
        set_time += 1
    car.leave_time = set_time
    route.append(car.leave_time)

    complete_cross_count = 0
    item = car.shortest_cross[complete_cross_count:complete_cross_count + 3]
    car.link_cross(cross_list, item)
    car.link_road(road_list)
    car.actual_speed = min(car.max_speed, car.from_road_ptr.limit_speed)
    route.append(car.from_road_ptr.id)

    while (1):
        # 如果车的下一个路口就是目的路口
        if car.is_on_dest_road():
            # 如果可以移动的距离超过道路长度，认为车已经如果
            if car.position + car.actual_speed > car.from_road_ptr.length:
                set_time += 1
                car.arrive_time = set_time
                car.run_time = car.arrive_time - car.leave_time
                break
            else:  # 正常行驶
                car.position = car.position + car.actual_speed
                set_time += 1
        else:  # 下一个路口不时目的路口
            virtual_position = car.position + car.actual_speed
            if virtual_position <= car.from_road_ptr.length:
                car.position = virtual_position
                set_time += 1
            else:  # 通过路口
                remain_distance = car.from_road_ptr.length - car.position
                complete_cross_count += 1
                if car.next_cross_ptr.id != car.arrive:
                    item = car.shortest_cross[complete_cross_count:complete_cross_count + 3]
                else:
                    item = car.shortest_cross[complete_cross_count:complete_cross_count + 2]
                car.link_cross(cross_list, item)
                car.link_road(road_list)
                car.actual_speed = min(car.max_speed, car.from_road_ptr.limit_speed)
                car.position = car.actual_speed - remain_distance
                set_time += 1
                route.append(car.from_road_ptr.id)

    print(route)

    return route,set_time

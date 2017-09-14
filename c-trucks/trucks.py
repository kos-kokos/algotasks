str_input = input()

boxes = int(str_input.split(" ")[0])
truck_limit = int(str_input.split(" ")[1])

boxes_list = []
for i in range(0,boxes):
    boxes_list.append(1)

to_trucks = [boxes]
trucks = []

while len(to_trucks) > 0 :
    boxes_batch = to_trucks.pop()
    batch_part_1 = int(boxes_batch/2)
    batch_part_2 = boxes_batch - batch_part_1
    if batch_part_1 <= truck_limit:
        trucks.append(1)
    else:
        to_trucks.append(batch_part_1)
    if batch_part_2 <= truck_limit:
        trucks.append(1)
    else: to_trucks.append(batch_part_2)

print(len(trucks))

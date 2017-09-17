def process_queue(current_time: int, queue: [], last_exit_time: int, results: []):
    if (len(queue) == 0):
        return last_exit_time
    client = queue[0]
    if (last_exit_time > client[0]):
        actual_start_time = last_exit_time
    else:
        actual_start_time = client[0]
    if current_time - actual_start_time >= 20:
        last_exit_time = actual_start_time + 20  # записываем время когда он закончил стрижку
        queue.pop(0)  # удаляем клиента т.к. он уже постригся
        results[client[2]] = (str(last_exit_time // 60) + " " + str(last_exit_time % 60))
    return last_exit_time


n = int(input())
queue = []  # очередь к парикмахеру
last_exit_time = 0
results = [None] * n

for i in range(n):
    str_client = input()
    client_array = str_client.split(" ")
    hours = int(client_array[0])
    minutes = int(client_array[1])
    max_queue = int(client_array[2])
    client = (hours * 60 + minutes, max_queue, i)
    # вызываем обработку очереди, запоминаем время ухода поледнего на данный момент клиента
    last_exit_time = process_queue(client[0], queue, last_exit_time, results)
    if (len(queue) <= max_queue):
        queue.append(client)
    else:
        results[i] = (str(hours) + " " + str(minutes))

while (len(queue) > 0):
    last_exit_time = process_queue(24 * 60, queue, last_exit_time, results)
for result in results:
    print(result)

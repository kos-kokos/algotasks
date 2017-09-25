class MQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def put(self, elem: int):
        current_min = None
        if(len(self.stack_in) > 0):
            current_min = self.stack_in[len(self.stack_in) - 1][1]
        if None == current_min or elem < current_min:
            self.stack_in.append((elem, elem))
        else:
            self.stack_in.append((elem, current_min))

    def remove(self):
        if(len(self.stack_out) == 0):
            while (len(self.stack_in) > 0):
                curr_min = None
                if(len(self.stack_out)> 0):
                    curr_min = self.stack_out[len(self.stack_out) - 1][1]
                elem = self.stack_in.pop()[0]
                if(None == curr_min or elem < curr_min):
                    self.stack_out.append((elem, elem))
                else:
                    self.stack_out.append((elem, curr_min))
        return self.stack_out.pop()[0]

    def getMin(self):
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return None
        if len(self.stack_in) == 0:
            return self.stack_out[len(self.stack_out) - 1][1]
        if len(self.stack_out) == 0:
            return self.stack_in[len(self.stack_in) - 1][1]

        in_stack_min = self.stack_in[len(self.stack_in) - 1][1]
        out_stack_min = self.stack_out[len(self.stack_out) - 1][1]
        if (out_stack_min < in_stack_min):
            return out_stack_min
        else:
            return in_stack_min


str_n_k = input()
n = int(str_n_k.split(" ")[0])
k = int(str_n_k.split(" ")[1])
str_in = input()
input_data = []
output_data = []
for s in str_in.split(" "):
    input_data.append(int(s))
q = MQueue()

for i in range(k):
    q.put(input_data[i])
for i in range(k, n):
    output_data.append(q.getMin())
    q.remove()
    q.put(input_data[i])
output_data.append(q.getMin())

for val in output_data:
    print(val)

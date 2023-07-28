from tqdm import tqdm
from time import sleep
from Process import Process

class FCFS:
    def __init__(self, p_list):
        self.processes_list = []
        self.process_queue = p_list
        self.burst_queue = []
        self.amount = len(p_list)
        self.create_processes(self.process_queue)
        self.fill_queue()
        self.average_wait_time = 0

    def create_processes(self, p):
        p.sort(key=lambda words: words[1])

        for x in p:
            self.processes_list.append(Process(x[0], x[2], x[1], x[3]))

    def fill_queue(self):
        for p in self.processes_list:
            self.burst_queue.append(p.burst())


    def run(self):
        t_t=0
        sleep(1)
        for x in range(self.amount):
            actual_pname = str(self.processes_list[x].name)
            for i2 in range(self.burst_queue[x]):
                # self.log.pending(actual_pname)
                self.processes_list[x].e_time+=1
                t_t+=1
                sleep(1)
                tqdm.write('\nTime Unit: {} PID {} executes. {} instructions left'.format(t_t, str(self.processes_list[x].name),int(self.processes_list[x].burst_time)-self.processes_list[x].e_time))
                for p in self.processes_list:
                    if str(p.name) != actual_pname:
                        if int(p.arrival_time) == int(t_t):
                            p.w_time+=1
                            tqdm.write('PID {} wait = {}'.format(p.name,p.w_time))                            
                        if int(p.arrival_time) < int(t_t) and p.e_time == 0:
                            p.w_time+=1
                            tqdm.write('PID {} wait = {}'.format(p.name,p.w_time))
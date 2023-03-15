from object import Queue
from random import randrange


class Printer:
    def __init__(self, ppm):
        self.pages_per_minute: int = ppm
        self.current_task = None
        self.task_list = Queue()

    def necessary_time(self) -> float:
        return self.current_task.number_of_pages / self.pages_per_minute * 60

    def is_idle(self) -> bool:
        return False if self.current_task else True

    def print_task(self):
        self.current_task = self.task_list.dequeue()

    def finish_printing(self):
        self.current_task = None


class Task:
    def __init__(self, current_second):
        self.number_of_pages: int = randrange(1, 21)
        self.start_time: int = current_second


def simulation(simulation_time: int, ppm: int) -> None:
    printer = Printer(ppm)
    average_wait = list()
    for second in range(simulation_time):
        if randrange(1, 181) == 180:
            printer.task_list.enqueue(Task(second))
        if printer.is_idle():
            if not printer.task_list.is_empty():
                printer.print_task()
                average_wait.append(printer.necessary_time())
        elif second - printer.current_task.start_time >= printer.necessary_time():
            printer.finish_printing()
    average_wait_time = sum(average_wait) / len(average_wait)
    print(f"Average waiting time: {average_wait_time:0>5.2f} s. {len(printer.task_list)} tasks remaining.")


for c in range(10):
    simulation(3600, 1)






class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def __str__(self):
        return f'cpu: {self.cpu}, memory: {self.memory}'

    def __gt__(self, other):
        return self.memory > self.cpu

    def __ge__(self, other):
        return self.memory > self.cpu

    def __eq__(self, other):
        return self.memory > self.cpu

    def make_computations(self, __cpu, __memory):
        return self.__cpu + self.__memory


class Phone:

    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        self.__sim_card_number = sim_card_number
        self.__call_to_number = call_to_number

        while True:
            sim_card_list = input('Введите номер абонета: ')
            print(f'Идет звонок на номер: {sim_card_list}')

    def __str__(self):
        super(Phone, self).__str__(f'sim_card: {self.sim_cards_list}')


class SmartPhone(Computer, Phone):

    def __init__(self, cpu, location, memory):
        super().__init__(cpu, memory)
        self.location = location

    def use_gps(self, location):
        self.location = location
        location = input('Введите адрес: ')
        print(f'Ваш маршрут проложен: {location}')

    def __str__(self):
        return Computer.__str__(self) + f'cpu: {self.cpu}' \
                                        f'location: {self.location}' \
                                        f'memory: {self.memory}' \
                                        f'sim_card: {self.sim_cards_list}'

ч
my_cump = Computer(6, 16192)
my_phone = Phone("Beelin")
my_smartphon = SmartPhone(6, location="Bishkek", memory=32)
my_smartphon_2 = SmartPhone(4, location="Jalal-abad", memory=16)
my_smartphon.use_gps("Bishkek")
my_phone.call("Beelin", 0)

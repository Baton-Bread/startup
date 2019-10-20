# Подходы Программирования
# Императивный 
# Декларативный
# Структурный 
# Функиональный
# ООП (объектно ориентированный подход)


# Котик Класс
# Св-ва: размер, цвет, атрибуты Атрибуты
# Действия: ходить, есть, спать, мяукать Методы
# Кот Вася - экземпляр класса

class Tank:
    def __init__(self, model, health, armor, damage):
        self.model = model
        self.health = health
        self.armor = armor
        self.damage = damage
        self.alive = True

    def print_info(self):
        print('Модель: ' + self.model)
        print('Здоровье: ' + str(self.health))
        print('Броня: ' + str(self.armor))
        print('Урон: ' + str(self.damage))

        if self.alive == True:
            print('ВСЕ СИСТЕМЫ В НОРМЕ. ПРОДОЛЖАЙТЕ ДВИЖЕНИЕ')
        else:
            print('ТАНК ЛИКВИДИРОВАН. БОЕВЫЕ ДЕЙСТВИЯ НЕВОЗМОЖНЫ.')
    
    def shoot(self, enemy):
        enemy.health = enemy.health - self.damage
        if enemy.health <= 0:
            enemy.health = 0
            enemy.alive = False
        

tank_1 = Tank('T-34', 1000, 100, 160)
tank_2 = Tank('ИМБА', 1, 500, 20000)
tank_3 = Tank('БОРЕЦ САМБО', 200, 10000, 50)
tank_1.print_info()
#print(tank_2.model)
#tanl_2.health = 1500
tank_2.print_info()

tank_1.shoot(tank_2)

tank_2.print_info()

class SuperTank(Tank):
    def __init__(self, model, health, armor, damage, dop_health):
        super().__init__(model, health, armor, damage)
        self.dop_health = dop_health

    def repair(self):
        print('починка завершена (work in progress)')

super_tank = SuperTank('T-34', 1000, 100, 160,50)
super_tank.print_info()
super_tank.repair()
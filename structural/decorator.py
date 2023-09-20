from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def hit(self):
        pass

class BaseWeapon(Weapon):

    def hit(self):
        print("Weapon hitted the enemy!")

class WeaponDecorator(Weapon):
    
    def __init__(self, base_weapon):
        self._base_weapon = base_weapon

    def hit(self):
        self._base_weapon.hit()

class EnchantedWeapon(WeaponDecorator):

    def hit(self):
        super().hit()
        print("Enchantment caused more damage to the enemy!")

class PoisonedWeapon(WeaponDecorator):

    def hit(self):
        super().hit()
        print("Poisoned weapon caused more damage to the enemy!")

if __name__ == "__main__":

    weapon = BaseWeapon()
    weapon.hit()

    print("---------------------------")

    p_weapon = PoisonedWeapon(weapon)
    p_weapon.hit()

    print("---------------------------")

    e_weapon = EnchantedWeapon(p_weapon)
    e_weapon.hit()

    print("---------------------------")

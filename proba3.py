from pprint import pprint
import inspect
class BankAccount():
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
    def deposit(self, amount):
        self.account += amount
        print(f'Пополнение {amount}, новый баланс {self.account}')
object = BankAccount(100,50)
data = {}
attr_name = 'account'
def introspection_info(obj):
    data['тип'] = type(obj)
    data['атрибуты'] = dir(obj)
    data['account'] = hasattr(obj, attr_name)
    data['значение account'] = getattr(obj, attr_name, None)
    data['вызывемый объект deposit?'] = callable(obj.deposit)
    data['объект класс?'] = isinstance(obj, BankAccount)
    return data

number_info = introspection_info(object)
pprint(number_info)
print('Используем inspect:')
print(inspect.ismodule(object))
print(inspect.isclass(object))
print(inspect.getmodule(object.deposit))
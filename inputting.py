#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
import re
from constants import CONST


# Функция запроса у пользователя стартового числа поиска
def inputStartNumber():

  # Запрос повторяется до тех пор пока не будет введено число
  # или пустое значение
  while 1:

    # Получаем ввод от пользователя
    inputMessage = 'Введите начальный номер (или Enter, чтобы начать с 1)'
    startNum = input(inputMessage)
    startNum = startNum.strip()

    try:

      # Если ничего не введено то начинаем с 1
      if(startNum == ''):
        return 1

      # Если введено число, то возвращаем его значение
      startNum = int(startNum)
      return startNum

    except ValueError:

      # Если число не распознано, уточняем что вводить необходимо число
      print('Вводите число')


# Распознавание строки обозначения
def parseClassificator(classificator):
  # патерн для разбора строк, подходит как для полной (например 5ЭТ.384),
  # так и для сокращённной формы (например 5.384)
  # точка в конце не имеет значения
  pattern = '(?P<firstRange>\d)(ЭТ)?\.(?P<secondRange>\d{3,3})'

  expr = re.compile(pattern, re.IGNORECASE)
  m = expr.match(classificator)

  if not m:
    raise Exception('Не удалось распознать классификатор: %s'%classificator)

  # Первый разряд, например 5 в 5.384
  firstRange = m.group('firstRange')
  # Второй разряд, например 384 в 5.384
  secondRange = m.group('secondRange')

  return (firstRange, secondRange)


# Функция запроса у пользователя искомой группы обозначений
def inputClassificator():

  checkingClassificator = ''

  # Запрос повторяется до тех пор пока не будет введено обозначение
  while 1:

    # Получаем ввод от пользователя
    inputMessage = 'Введите классификатор для поиска (например 5.384)'
    checkingClassificator = input(inputMessage)
    checkingClassificator = checkingClassificator.strip()

    try:

      # Распознавание ввода
      firstRange, secondRange = parseClassificator(checkingClassificator)

      # Ввоссоздание стандартной формы записи
      classificator = firstRange + CONST.COMPANY_ID_INFIX + '.' + secondRange + '.'
      return classificator

    except Exception:
      print('Не удалось распознать обозначение %s'%checkingClassificator)


# Запрос всех необходимых данных у пользователя
def inputData():

  startNum = inputStartNumber()
  checkingClassificator = inputClassificator()

  return (startNum, checkingClassificator)

# Запуск модуля по умолчанию
def main():
  pass

if __name__ == '__main__':
  main()

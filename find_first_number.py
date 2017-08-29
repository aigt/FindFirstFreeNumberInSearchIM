#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
import re

from search import getPreparedSearch
from inputting import inputData
from constants import CONST


# Проверяет есть ли в наименовании метка что документ свободен
def isDocMarkedAsFree(inventoryDocId):

  # Выбираем документ в Search
  CONST.search.OpenDocument(inventoryDocId)
  # Получаем его наименование
  fldName = CONST.search.GetFieldValue('Наименование')

  # Проверяем есть ли в наименовании метка что документ свободен
  if fldName.find('свободн') >= 0:
    print('    - marked as free: ' + fldName)
    return True
  else:
    print('    - without special marks')
    return False


# Проверяет свободен ли документ с указанным обозначением
def checkDoc(docId):

  docMarkedAsFree = False
  existed = False

  print(docId)
  print('    Checking is being started:')

  # Запрашивает инвентарный номер по обозначению
  inventoryId = CONST.search.GetDocID_ByDesignation(docId)

  # Инвентарный номер больше нуля обозначает
  # что такой документ существует
  if inventoryId > 0:

    print('    - existed, no.: ' + str(inventoryId))

    existed = True

    # Проверяем помечен ли документ пометкой, что он свободен
    docMarkedAsFree = isDocMarkedAsFree(inventoryId)

  else:
    print('    - not existed')

  return (not existed) or docMarkedAsFree


# Проверяет документы с указанным Id,
# в т.ч. спецификации если если есть
def checkId(id):

  idIsFree = checkDoc(id)

  idWithSBIsFree = True

  if int(id[0]) in CONST.RANGES_WITH_SB_DRAWS:
    idWithSB = id + ' СБ'
    idWithSBIsFree = checkDoc(idWithSB)


  if idIsFree and idWithSBIsFree:

    print()
    print('  Free id: ' + id)

    return True

  print()
  print('  Result: Id ' + id + ' is not free')
  print()
  print()

  return False


def checkRangeOfClassificator(startNum, classificator):
  i=startNum

  while i < 1000:

    checking_i = ''
    if i < 10:
      checking_i = '00' + str(i)
    elif i < 100:
      checking_i = '0' + str(i)
    else:
      checking_i = str(i)

    checking_id = classificator + checking_i
    isFree = checkId(checking_id)

    if isFree:
      return checking_id

    i = i + 1

  return ''


def freeIdSearch():

  # Получаем com-объект Search'а
  try:
    CONST.search = getPreparedSearch()
  except Exception as error:
    print('Caught this error while logged: ' + repr(error))
    return

  # Запрашиваем критерии поиска у пользователя
  startNum, checking_classificator = inputData()

  freeId = checkRangeOfClassificator(startNum, checking_classificator)

  if freeId == '':
    print('There is not free id')


# Запуск модуля по умолчанию
def main():
  freeIdSearch()

if __name__ == '__main__':
  main()

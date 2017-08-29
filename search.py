#-------------------------------------------------------------------------------
# Name:        Search
# Purpose:
#
# Author:      Krugov Alexey
#
# Created:     21.08.2017
# Copyright:   (c) Krugov Alexey 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from win32com.client import Dispatch
from constants import CONST


# Создание com-объекта Search
def createSearch():
  search = Dispatch(CONST.SEARCH_APP_TOKEN)
  return search


# Залогинивание в Search
def LogInSearch(search):

  # Попытка залогиниться
  search.Login()

  # Проверка залогинился ли пользователь в сёрч Search
  if search.IsLoggedIn == 0:

    print('can\'t login')
    raise Exception('can\'t login search')

  else:

    print('Seach is logged in.')
    print()


# Возвращает залогиненый com-объект Search
def getPreparedSearch():

  # создание com-объекта
  search = createSearch()

  # log in
  LogInSearch(search)

  return search


# Запуск модуля по умолчанию
def main():
  pass

if __name__ == '__main__':
  main()

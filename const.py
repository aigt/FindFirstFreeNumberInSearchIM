#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------


# Оболочка для констант
class _const:
  class ConstError(TypeError): pass

  def __setattr__(self, name, value):
    if name in self.__dict__:
      raise self.ConstError("Can't rebind const (%s)"%name)
    self.__dict__[name] = value


# Экземпляр оболочки для констант
CONST = _const()


# Запуск модуля по умолчанию
def main():
  return CONST

if __name__ == '__main__':
  main()

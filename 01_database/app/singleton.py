class MetaSingleton(type):
    """
    всякий раз, когда мы будем создавать экземпляр класса, использующий
    этот метакласс, то метод __call__ будет возвращать существующий экзмепляр из словаря
    если же экзмепляр отсутствует, то он создает его и добавляет в словарь
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

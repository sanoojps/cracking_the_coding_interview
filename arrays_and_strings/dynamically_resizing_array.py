# make_a_dynamically_resizing_array():

class ArrayList(object):
    def __init__(self):
        self._internal_list = []
        self.__capacity = 10
        
    def capacity(self):
        return len(self._internal_list)

    def add(self,obj):
        if self.capacity >= self.__capacity:
            # create a new array of the size 2 * (self.__capacity) and add it to the current array
            # this is only a symbolic representation
            # so we simply increment the capacity
            self.__capacity = 2 * self.__capacity
            self._internal_list.append(obj)





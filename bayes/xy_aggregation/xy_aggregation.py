from typing import Union



class table_aggregation:
    "Creates table and returns divided on X_train, Y_train, X_test."

    def __init__(self, table: list[list], x: Union[int, bool] = False, y: Union[int, bool] = False):
        "Creates table and returns if directed X_train, Y_train, X_test."

        # main table
        self.__row_table = table

        # for one aggregation
        self.__X_train  = []
        self.__Y_train  = []
        self.__X_test   = []

        # if data for division already given
        if isinstance(x, int) and isinstance(y, int): self.__call__(x, y)


    def __call__(self,  x: Union[int, bool] = False, y: Union[int, bool] = False):
        "Returns divided X_train, Y_train, X_test if division done."

        # if data for division given
        if isinstance(x, int) and isinstance(y, int):
            self.divide(x, y)
            return self.__X_train, self.__Y_train, self.__X_test

        # just returns existing data
        elif self.__X_train!=[] and self.__Y_train!=[] and self.__X_test!=[]:
            return self.__X_train, self.__Y_train, self.__X_test

        # results do not exist
        else:
            message = "Results do not exist (division was not done)."
            print(message)
            return [False, message]


    def divide(self,  x: int, y: int):
        "Gives X_train, Y_train, X_test."

        if y < 0 or y >= len(self.__row_table):
            message = "Invalid row index"
            print(message)
            return [False, message]
        if x < 0 or x >= len(self.__row_table[0]):
            message = "Invalid column index"
            print(message)
            return [False, message]

        self.__X_train  = [row[:x] + row[x+1:] for i, row in enumerate(self.__row_table) if i != y]
        self.__Y_train  = [row[x] for i, row in enumerate(self.__row_table) if i != y]
        self.__X_test   = self.__row_table[y][:x] + self.__row_table[y][x+1:]

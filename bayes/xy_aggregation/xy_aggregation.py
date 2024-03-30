



class table_aggregation:
    "Creates table and returns divided on X_train, Y_train, X_test."

    def __init__(self, table: list[list], Y_train_col: int|bool = False, X_test_row: int|bool = False):
        "Creates table and returns if directed X_train, Y_train, X_test."

        # main table
        self.__row_table = table

        # for one aggregation
        self.__X_train  = []
        self.__Y_train  = []
        self.__X_test   = []

        # if data for division already given
        if Y_train_col and X_test_row: self.__call__(Y_train_col, X_test_row)


    def __call__(self, Y_train_col: int|bool = False, X_test_row: int|bool = False):
        "Returns divided X_train, Y_train, X_test if division done."

        # if data for division given
        if Y_train_col and X_test_row:
            self.divide(Y_train_col, X_test_row)
            return self.__X_train, self.__Y_train, self.__X_test

        # just returns existing data
        elif self.__X_train!=[] and self.__Y_train!=[] and self.__X_test!=[]:
            return self.__X_train, self.__Y_train, self.__X_test

        # results do not exist
        else:
            message = "Results do not exist (division was not done)."
            print(message)
            return [False, message]


    def divide(self, Y_train_col: int, X_test_row: int):
        "Gives X_train, Y_train, X_test."

        # temporary variables
        temp_rows = []

        # saving X_test
        self.__X_test = self.__row_table[X_test_row]

        # excluding X_test row
        if   X_test_row!=0 and X_test_row!=len(self.__row_table):

            temp_rows+=self.__row_table[:X_test_row]
            temp_rows+=self.__row_table[X_test_row+1:]

        elif X_test_row!=0: temp_rows = self.__row_table[:-1]
        else: temp_rows = self.__row_table[1:]

        # creating Y_train_col and excluding Y_train_col for X_train table
        # reset
        self.__X_train = []
        self.__Y_train = []

        for x in temp_rows:

            # temporary row
            temp_row = []

            if   Y_train_col!=0 and Y_train_col!=len(x):

                temp_row+=x[:Y_train_col]
                temp_row+=x[Y_train_col+1:]

            elif Y_train_col!=0: temp_row = x[:-1]
            else: temp_row = x[1:]

            # append to class lists
            self.__X_train.append(temp_row)
            self.__Y_train.append(x[Y_train_col])

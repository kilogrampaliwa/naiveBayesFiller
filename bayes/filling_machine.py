from xy_aggregation.xy_aggregation import table_aggregation
from stat_helpers import stat_helpers
from simpleNaiveBayes import snb
from typing import Union


class by_strategy:

    def __init__(self, strategy_dict: dict, table: Union[list[list[str]], bool]=False, empty_symbol: Union[str, bool]=False):
        """
        initiates filling machine. Attributes:
        strategy_dict - dicitionary made by strategies.py

        """
        #raw data
        self.__raw_table = False

        # empty symbol
        self.__emptySymb = False

        # temp sets
        self.__temp_X_train  =   []
        self.__temp_Y_train  =   []
        self.__temp_X_test   =   []

        # strategy settings
        self.changeStrategy(strategy_dict)
        if empty_symbol: self.changeEmptySymmbol(empty_symbol)
        if table: self.changeTable(table)


    def changeStrategy(self, strategy_dict: dict):
        "Changes approach to table filling."

        output = self.__unpack_dict(strategy_dict)
        if output[0]: return [True]
        else: return output


    def changeEmptySymmbol(self, eempty_symbol: str):
        "Replaces symbol of empty element."

        self.__emptySymb = eempty_symbol


    def changeTable(self, table: list[list[str]]):
        "Changes input table."

        self.__raw_table = table
        self.__output_table = self.__raw_table.copy()


    def __unpack_dict(self, dictionary: dict):
            "Unpacking dictionary from strategies.py."

            # inside function
            def row_schedule(how: str|list[int]):
                "Creates list with number of rows as schedule or checks if schedule is correct."

                if isinstance(how, str):
                    if    how=="up_to_down":     return [True, range(0, len(self.__table))]
                    elif  how=="down_to_up":     return [True, range(len(self.__table)-1, -1)]
                    else: self.__error_output("Wrong schedeule.")
                elif isinstance(how, list[int]):
                    if how.copy().sort() == range(0, len(self.__table)): return [True, how]
                    else: self.__error_output("Wrong length of schedeule.")
                else:
                    self.__error_output()

            # inside function
            def column_schedule(how: str|list[int]):
                "Creates list with number of columns as schedule or checks if schedule is correct."

                if isinstance(how, str):
                    if    how=="left_to_right":     return [True, range(0, len(self.__table[0]))]
                    elif  how=="right_to_left":     return [True, range(len(self.__table[0])-1, -1)]
                    else: self.__error_output("Wrong schedeule.")
                elif isinstance(how, list[int]):
                    if how.copy().sort() == range(0, len(self.__table[0])): return [True, how]
                    else: self.__error_output("Wrong length of schedeule.")
                else:
                    self.__error_output()

            # function
            #

            self.__percent      =   dictionary["percent"]
            self.__replacement  =   dictionary["replacement"]
            self.__results      =   dictionary["results"]

            rows = row_schedule(dictionary["rows"])
            columns = column_schedule(dictionary["columns"])

            if rows[0]:
                self.__rows = rows[1]
                if columns[0]: self.__columns = columns[1]
                else: return columns
            else: return rows

            return [True]


    def __error_output(self, message:Union[str, bool] = False):
        "Returns message with error."
        if message: return [False, message]
        else: return [False, False]


    def __solve_single_Bayes(self, coordinates: list[int]):
        "Solves Bayes for single coordinate."

        # temporary buff table to pick all X sets that has result in Y_test
        X_train_temp = []
        Y_train_temp = []

        # division od big table into smaller groups
        X_train_temp, Y_train_temp, self.__temp_X_test = table_aggregation(self.__raw_table, coordinates[1], coordinates[0])

        # adding lists to training groups if there is a solution in Y_train
        for i in range(len(Y_train_temp)):
            if Y_train_temp[i]!=self.__emptySymb:
                self.__temp_X_train.append(X_train_temp[i])
                self.__temp_Y_train.append(Y_train_temp[i])

        # filling X_train list
        for i in range(len(self.__temp_X_train)):
            self.__temp_X_train[i] = stat_helpers.fill_array(self.__temp_X_train[i], self.__emptySymb, self.__replacement)
        
        # filling X_test list
        self.__temp_X_test = stat_helpers.fill_array(self.__temp_X_test, self.__emptySymb, self.__replacement)

        # result
        return snb.sklearnBasis(self.__temp_X_train, self.__temp_Y_train, self.__temp_X_test)
    
    
    def __solve_column(self, column_no: int, table: Union[list[list[int]], bool] = False):
        "Solves empty spaces with naive Bayes for selected column."

        # buff list
        new_values = []

        # table to work on
        if table: table = table
        else: table = self.__raw_table.copy()

        for i in range(len(table)):

            if table[i]==self.__emptySymb:   new_values.append([i, self.__solve_single_Bayes([i,column_no])])
            else:                            new_values.append([i, table[i]])

        for x in new_values:    self.__output_table[x[0]][column_no] = x[1]
    

    def __solve_table(self):
        "Solves full table."

        for i in range(len(self.__raw_table)):
            if self.__results: self.__solve_column(i, self.__output_table)
            else:              self.__solve_column(i, self.__raw_table)


# 1 solve bayes
# 2 every row in column
# 3 every column


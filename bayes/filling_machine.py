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

        self.__strategy_dict = strategy_dict

        # empty symbol
        self.__emptySymb = empty_symbol

        # raw data
        self.__raw_table = self.__remove_ns(table)

        # temp sets
        self.__temp_X_train  =   []
        self.__temp_Y_train  =   []
        self.__temp_X_test   =   []

        # out table
        self.__out_table = False


    def __call__(self):
        "Runs the program anyway."

        if   self.__strategy_dict["strategy"] == "one":     self.__runOne()
        elif self.__strategy_dict["strategy"] == "column":  self.__runColumn()
        elif self.__strategy_dict["strategy"] == "table":   self.__runTable()

        return self.__out_table


    def __solve_single_Bayes(self,x: int, y: int):
        "Solves Bayes for single coordinate."

        # temporary buff table to pick all X sets that has result in Y_test
        X_train_temp = []
        Y_train_temp = []

        aggregator =  table_aggregation(self.__raw_table)

        # division od big table into smaller groups
        X_train_temp, Y_train_temp, self.__temp_X_test = aggregator(x, y)

        # adding lists to training groups if there is a solution in Y_train
        for i in range(len(Y_train_temp)):
            if Y_train_temp[i]!=self.__emptySymb:
                self.__temp_X_train.append(X_train_temp[i])
                self.__temp_Y_train.append(Y_train_temp[i])

        # filling X_train list
        for i, n in enumerate(self.__temp_X_train):
            self.__temp_X_train[i] = stat_helpers.fill_array(n, self.__emptySymb, self.__strategy_dict["replacement"])

        # filling X_test list
        self.__temp_X_test = stat_helpers.fill_array(self.__temp_X_test, self.__emptySymb, self.__strategy_dict["replacement"])

        # result
        bayes = snb.sklearnBasis(self.__temp_X_train, self.__temp_Y_train, self.__temp_X_test)
        return bayes()


    def __remove_ns(self, table):
        "Removing \n from table."
        out_table = []
        for n in table:
            new_line = []
            for m in n:
                if '\n' not in m:   new_line.append(m)
                else:               new_line.append(m[0])
            out_table.append(new_line)
        return out_table


    def __runOne(self, x: Union[int, bool] = False, y: Union[int, bool] = False, new_table: Union[list[list], bool] = False):
        "Runs Naive Bayes for only one element."

        outTable = []
        if new_table:   outTable = new_table
        else:           outTable = self.__raw_table.copy()
        
        result = []
        if isinstance(x, int) and isinstance(y, int):
            result = self.__solve_single_Bayes(x, y)[0]
        else:
            result = self.__solve_single_Bayes(self.__strategy_dict["columns"], self.__strategy_dict["rows"])[0]

        if isinstance(x, bool): x = self.__strategy_dict["rows"]
        if isinstance(y, bool): y = self.__strategy_dict["columns"]

        outTable[y][x] =  result

        self.__out_table =  outTable


    def __runColumn(self, x: Union[int, bool] = False, new_table: Union[list[list], bool] = False):
        "Runs Naive Bayes for selected column."

        inTable = []
        if new_table:       inTable = new_table
        else:               inTable = self.__raw_table.copy()

        if   self.__strategy_dict["rows"] == "up_to_down": self.__strategy_dict["rows"] = [i for i in range(len(inTable))          ]
        elif self.__strategy_dict["rows"] == "down_to_up": self.__strategy_dict["rows"] = [i for i in range(len(inTable)-1, -1, -1)]

        for y in self.__strategy_dict["rows"]:
            if self.__strategy_dict["results"]:     inTable = self.__out_table.copy()
            else:                                   inTable = self.__raw_table.copy()

            if self.__raw_table[y][x]==self.__emptySymb:
                self.__runOne(x, y, inTable)


    def __runTable(self):
        "Runs Naive Bayes for whole table."

        inTable = []
        inTable = self.__raw_table.copy()

        if   self.__strategy_dict["columns"] == "left_to_right": self.__strategy_dict["columns"] = [i for i in range(len(inTable[0]))          ]
        elif self.__strategy_dict["columns"] == "right_to_left": self.__strategy_dict["columns"] = [i for i in range(len(inTable[0])-1, -1, -1)]

        for x in self.__strategy_dict["columns"]:
            if self.__strategy_dict["results"]:     inTable = self.__out_table.copy()
            else:                                   inTable = self.__raw_table.copy()
            self.__runColumn(x, inTable)


from typing import Union


class one_element:

    def __init__(self, coordinates: Union[list[int, int], bool] = False, test_percent_existing: int = 0, replacement_type: str = "mean"):
        """
        Choose proper strategy parameters.

        test_percent_existing:  give int in range 0-100.
        replacement_type:       give one of following:    "mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"
        """

        # default attributes (false if not given)
        self.__test_percent_existing = False
        self.__replacement_type      = False
        self.__coordinates           = False

        # using public functions to save attributes
        print( test_percent_existing)
        self.change_test_percent_existing(test_percent_existing)
        self.change_test_replace_type(replacement_type)
        if coordinates: self.change_coordinates(coordinates)


    def change_coordinates(self, coordinates: list[int, int]):
        "Change coordinates."
        self.__coordinates = [True, coordinates]


    def change_test_percent_existing(self, test_percent_existing: int):
        "Changing class parameter, give int in range 0-100."
        print( test_percent_existing)
        # if given input is corresponding
        if test_percent_existing >= 0 and test_percent_existing <= 100:
            self.__test_percent_existing = test_percent_existing
            return [True]

        # if given value is not considerable
        else:
            message = "Wrong percent ranage (not in [0-100])."
            print(message)
            return [False, message]


    def change_test_replace_type(self, replacement_type: str):
        """
        Changing replacement type, give one of below:
        "mean", "median" , "zero", "ones", "maximal", "minimal"
        "dynamic_mean"
        """

        # if given input is corresponding
        if replacement_type in ["mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"]:
            self.__replacement_type = replacement_type
            return [True]

        # if given value is not considerable
        else:
            message = "Wrong attribute given, choose one of mentioned. [one_elemenet, change_test_replace_type, not] "+str(replacement_type)
            print(message)
            return [False, message]


    def give_coordinates(self):
        "Gives coordinates of unknown item."

        # returns value if attribute defined
        if self.__coordinates:
            return [True, self.__coordinates]
        else:
            message = "Attribute yet not given."
            print(message)
            return [False, message]


    def give_test_percent_existing(self):
        "Gives attirbute: test_percent_existing"
        
        # returns value if attribute defined
        if self.__test_percent_existing: 
            return [True, self.__test_percent_existing]
        else:
            message = "Attribute yet not given."
            print(message)
            return [False, message]


    def give_replacement_type(self):
        "Gives attirbute: replacement_type"
        
        # returns value if attribute defined
        if self.__replacement_type: 
            return [True, self.__replacement_type]
        else:
            message = "Attribute yet not given."
            print(message)
            return [False, message]


    def give_dict(self):
        "Gives dictionary ready to use by a filling machine."

        # take and check data
        tempList = [self.give_test_percent_existing(), self.give_replacement_type(), self.give_coordinates()]
        if tempList[0][0] and tempList[1][0] and tempList[2][0]:

            # output dictionary:
            return {
                "strategy":     "one",
                "percent":      tempList[0][1],
                "replacement":  tempList[1][1],
                "columns":      tempList[2][1][0],
                "rows":         tempList[2][1][1],
                "results":      False
            }
        
        # error output
        else:
            message = "Error with data in strategy."
            print(message)
            return [False, message]




class series_column(one_element):

    def __init__(self, which_column: Union[int, bool] = False, test_percent_existing: int = 0, replacement_type: str = "mean", row_order: Union[str, list[int]] = "up_to_down"):
        """
        Choose proper strategy parameters.

        test_percent_existing:  give int in range 0-100.
        replacement_type:       give one of following:    "mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"
        row_order:              give one of following: "up_to_down", "down_to_up"
                                or list of int where every given number means column to be considered
        """

        # executing init function from parent class
        super().__init__(False, test_percent_existing=test_percent_existing, replacement_type=replacement_type)
        #super().__init__(test_percent_existing, replacement_type)

        # default attributes (false if not given)
        self.__row_order       = False
        self.__column             = False

        # using public functions to save attributes
        self.change_row_order(row_order)
        if which_column: self.change_column(which_column)


    def change_column(self, which_column: int):
        "Change row."
        self.__column = which_column


    def change_row_order(self, row_order: Union[str, list[int]]):
        """
        Changing execute order, type, give one of below:
        "up_to_down", "down_to_up"
        or list of int where every given number means column to be considered
        """

        # if given input is str
        if isinstance(row_order, str):

            # if given input is corresponding
            if row_order in ["up_to_down", "down_to_up"]:
                self.__row_order = row_order
                return [True]

            # if given input is not considerable
            else:
                message = "Wrong attribute given, choose one of mentioned. [series_column, change_row_order, str] " + str(row_order)
                print(message)
                return [False, message]

        # if given input is list
        elif isinstance(row_order, list):

            # if given elements are unique
            if len(row_order) > len(set(row_order)):
                self.__row_order = row_order
                return [True]

            # if given values are not unique
            else:
                message = "Elements in list are not unique."
                print(message)
                return [False, message]

        # if given value is not considerable
        else:
            message = "Wrong attribute given, choose one of mentioned. [series_column, change_row_order, not] " + str(row_order)
            print(message)
            return [False, message]


    def give_row_order(self):
        "Gives attirbute: in_column_order"
        
        # returns value if attribute defined
        if self.__in_column_order: 
            return [True, self.__in_column_order]
        else:
            message = "Attribute yet not given."
            print(message)
            return [False, message]


    def give_dict(self):
        "Gives dictionary ready to use by a filling machine."

        # take and check data
        tempList = [self.give_test_percent_existing(), self.give_replacement_type(), self.give_row_order(), self.give_column()]
        if tempList[0][0] and tempList[1][0] and tempList[2][0] and tempList[3][0]:

            # output dictionary:
            return {
                "strategy":     "column",
                "percent":      tempList[0][1],
                "replacement":  tempList[1][1],
                "columns":      tempList[2][1],
                "rows":         tempList[3][1],
                "results":      False
            }
        
        # error output
        else:
            message = "Error with data in strategy."
            print(message)
            return [False, message]


    def give_column(self):
        "Gives row."
        # returns value if attribute defined
        if self.__row_order:
            return [True, self.__row_order]
        else:
            message = "Attribute yet not given."
            print(message)
            return [False, message]



class series_table(series_column):

    def __init__(self, test_percent_existing: int = 0, replacement_type: str = "mean", include_results: bool = False, in_row_order: Union[str, list[int]] = "up_to_down", in_column_order: Union[str, list[int]] = "left_to_right"):#in_row_order: Union[str, list[int]] = "left_to_right", in_column_order: Union[str, list[int]] = "up_to_down")
        """
        Choose proper strategy parameters.

        test_percent_existing:  give int in range 0-100.
        replacement_type:       give one of following:    "mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"
        in_column_order:        give one of following: "up_to_down", "down_to_up"
                                or list of int where every given number means column to be considered
        in_row_order:           give one of following: "left_to_right", "right_to_left"
                                or list of int where every given number means column to be considered
        """

        # executing init function from parent class
        super().__init__(False, test_percent_existing=test_percent_existing, replacement_type=replacement_type, row_order=in_row_order)

        # default attributes (false if not given)
        self.__in_row_order         = False
        self.__include_results      = False

        # using public functions to save attributes
        self.change_row_order(in_row_order)
        self.change_include_results(include_results)


    def change_row_order(self, in_row_order: Union[str, list[int]]):
        """
        Changing execute order, type, give one of below:
        "up_to_down", "down_to_up"
        or list of int where every given number means column to be considered
        """

        # if given input is str
        if isinstance(in_row_order, str):

            # if given input is corresponding
            if in_row_order in ["up_to_down", "down_to_up"]:
                self.__in_row_order = in_row_order
                return [True]

            # if given input is not considerable
            else:
                message = "Wrong attribute given, choose one of mentioned. [series_table, change_row_order, str] " + str(in_row_order)
                print(message)
                return [False, message]

        # if given input is list
        elif isinstance(in_row_order, list):

            # if given elements are unique
            if len(in_row_order) > len(set(in_row_order)):
                self.__in_column_order = in_row_order
                return [True]

            # if given values are not unique
            else:
                message = "Elements in list are not unique."
                print(message)
                return [False, message]

        # if given value is not considerable
        else:
            message = "Wrong attribute given, choose one of mentioned. [series_table, change_row_order, not] " + str(in_row_order)
            print(message)
            return [False, message]


    def give_in_row_order(self):
        "Gives attirbute: in_row_order"
        
        # returns value if attribute defined
        if self.__in_row_order: 
            return [True, self.__in_row_order]
        else:
            message = "Attribute yet not given."
            print(message)
            return [False, message]


    def change_include_results(self, include_results: bool):
        "Changing class parameter, give int in range 0-100."

        self.__include_results = include_results
        return [True]


    def give_include_results(self):
        "Gives attirbute: include_results"
        return [True, self.__include_results]


    def give_dict(self):
        "Gives dictionary ready to use by a filling machine."

        # take and check data
        tempList = [self.give_test_percent_existing(), self.give_replacement_type(), self.give_in_column_order(), self.give_in_row_order(), self.give_include_results()]
        if tempList[0][0] and tempList[1][0] and tempList[2][0] and tempList[3][0] and tempList[4][0]:

            # output dictionary:
            return {
                "strategy":     "table",
                "percent":      tempList[0][1],
                "replacement":  tempList[1][1],
                "columns":      tempList[2][1],
                "rows":         tempList[3][1],
                "results":      tempList[4][1]
            }
        
        # error output
        else:
            message = "Error with data in strategy."
            print(message)
            return [False, message]
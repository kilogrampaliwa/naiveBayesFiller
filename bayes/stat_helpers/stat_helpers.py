


def fill_array(array: list, symbol: str, fill_type: str): # ["median", "mean", "zero", "ones", "maximal", "minimal", "dynamic_mean"]
    "Returns float array with filled empty spaces, symbolized by specified character."

    # list without empties
    clear_list = []
    to_be_filled = 0

    # output
    out_list = []

    # filling without array
    for x in array:
        if   x != symbol:   clear_list.append(float(x))

    # if filltype is dynamic (fillers are various)
    if fill_type[:4]=="dyna":

        # if clear list is 1
        if len(clear_list)==1:
            for x in array: out_list.append(clear_list[0])
            return out_list
        
        # dymanic mean
        elif "dynamic_mean":
            
            # with additional means between
            with_mids = []
            for i in range(1, len(array)):
                with_mids.append(array[i-1])
                with_mids.append((array[i-1] + array[i])/2)
            
            # counter and flag
            j = 0
            flag_next = False

            # filling loop
            for x in array:
                if flag_next and with_mids!=x:
                    j+=1
                    flag_next = False
                out_list.append(with_mids[j])
                if with_mids==x: flag_next = True
            
            # output
            return out_list


    # if filltype is static (fillers are all the same)
    else:
        # sets to-be-filled value
        if   fill_type=="mean"    :     to_be_filled = meanFromList(clear_list)
        elif fill_type=="median"  :     to_be_filled = medianFromList(clear_list)
        elif fill_type=="zero"    :     to_be_filled = 0
        elif fill_type=="ones"    :     to_be_filled = 1
        elif fill_type=="maximal" :     to_be_filled = max(clear_list)
        elif fill_type=="minimal" :     to_be_filled = min(clear_list)

        # filling output list
        for x in array:
            if   x == symbol:   out_list.append(to_be_filled)
            else:               out_list.append(float(x))

        # output
        return out_list


def meanFromList(array: list[float]):
    "Returns mean from list."
    
    # sum of all elements
    sum = 0
    for x in array: sum+=x

    # return result
    return sum/len(array)


def medianFromList(array: list[float]):
    "Returns median from list"

    # array length
    lngt = len(array)

    # returns middle one from odd
    if  lngt & 1:   return array[(lngt+1)/2]

    # returns average of two in even
    else:           return (array[lngt/2]+array[(lngt/2)+1])/2




class List(object):
#     def __init__(self,)
    
    def count_spec_digits(self, integers_list, digits_list):
        result = []
        integers = "".join(str(i) for i in integers_list)
        for number in digits_list:
            tmp = (number, integers.count(str(number)))
            result.append(tmp)
        return result 
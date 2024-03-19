def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,3,42]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop(-1)
    return l

def remove_element_from_start_of_list(l):
    del l[0]
    # l.pop(0)     or this one
    return l

def retrieve_first_element_from_list(l):
    list_item = l[0]
    return list_item

def retrieve_element_from_index(l, index):
    list_item = l[index]
    return list_item

def retrieve_last_element_from_list(l):
    list_item = l[-1]
    return list_item

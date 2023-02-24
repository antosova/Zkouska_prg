
import file_handler as fh

class Sorter:
    def __init__(self):
        correct_input = False
        while not correct_input:
            print('Sort in ascending (a) or descending (d) order?')
            order = input()
            if order == 'a':
                self.ascending = True
                correct_input = True
            elif order == 'd':
                self.ascending = False
                correct_input = True
            else:
                print('Incorrect input')
            self.done = False
    
    def set_array_to_sort(self, array):
        self.unsorted = array
        self.sorted = array
        self.done = False

    def sort_using_insertion_sort(self):
        for i in range(1, len(self.unsorted)):
            j = i
            if self.ascending:
                while self.sorted[j] < self.sorted[j-1] and j != 0:
                    self.sorted[j], self.sorted[j-1] = self.sorted[j-1], self.sorted[j]
                    j -= 1
            else:
                while self.sorted[j] > self.sorted[j-1] and j != 0:
                    self.sorted[j], self.sorted[j-1] = self.sorted[j-1], self.sorted[j]
                    j -= 1
        self.done = True
    
    def print_sorted_array(self):
        if self.done == False:
            print('Array hasn\'t been sorted yet.')
        else:
            print(str(self.sorted))

input_file_name = 'numbers.txt'
output_file_name = 'sorted.txt'

f_handler = fh.FileHandler()
array = f_handler.load_as_numbers_list(input_file_name)

sorter = Sorter()
sorter.set_array_to_sort(array)
sorter.sort_using_insertion_sort()
sorter.print_sorted_array()

f_handler.write_array_to_file(output_file_name, sorter.sorted)
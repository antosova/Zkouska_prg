import file_handler as fh

class WordsFinder:
    def __init__(self):
        self.input_set = False
        self.shortest = ''
        self.longest = ''
        self.done = False
        
    def set_input_data(self, file_name):
        self.f_handler = fh.FileHandler()
        self.words = self.f_handler.load_as_words_list(file_name)
        self.input_set = True
        self.done = False
        self.shortest = ''
        self.longest = ''

    def find_longest_and_shortest(self):
        if not self.input_set:
            print('Input data has not been set yet')
            return

        self.shortest = min(self.words[::-1], key = len)
        self.longest = max(self.words[::-1], key = len)
        
        self.done = True

        return self.shortest, self.longest

    def write_longest_shortest_to_file(self, file_name):
        if not self.done:
            print('The words have not been found yet.')
            return
        out_text = 'shortest: ' + self.shortest + '\n' + 'longest: ' + self.longest
        self.f_handler.write_string_to_file(file_name, out_text)
        


input_file_name = 'text.txt'
output_file_name = 'shortest_longest.txt'

w_finder = WordsFinder()
w_finder.set_input_data(input_file_name)

shortest, longest = w_finder.find_longest_and_shortest()

w_finder.write_longest_shortest_to_file(output_file_name)

print("longest = " + str(longest))
print("shortest = " + str(shortest))
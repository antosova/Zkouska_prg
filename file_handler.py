class FileHandler:
    def load_as_string(self, file_name):
        f = open(file_name, 'r', encoding='utf-8')
        text = f.read()
        f.close()
        return text
        
    def load_as_words_list(self, file_name):
        text = self.load_as_string(file_name)
        tmp_text = ''
        for char in text:
            if char.isalpha() or char.isnumeric() or char == ' ':
                tmp_text += char
        words = tmp_text.split(' ')
        return words

    def load_as_numbers_list(self, file_name):
        text = self.load_as_string(file_name)
        return list(map(float, text.split(',')))

    def write_array_to_file(self, file_name, array):
        f = open(file_name, 'w')
        f.write(str(array))
        f.close()

    def write_string_to_file(self, file_name, text):
        f = open(file_name, 'w')
        f.write(text)
        f.close()

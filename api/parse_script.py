class ParseScript:

    def import_from_txt(self, file_name):

        with open(f"../MovieScripts/{file_name}.txt", 'r') as f:
            for line in f:
                print(f"--> {line}")


ParseScript().import_from_txt("dances_with_wolves")

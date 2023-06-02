import random
def Password_Generator(length,type):
    password = ""
    if type == "char":
        possible_characters = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        length_possible_characters = len(possible_characters)
        for pos in range(length):
            rand_int = random.randint(0,length_possible_characters-1)
            password = password+possible_characters[rand_int]
        return password
    if type == "char_num":
        possible_characters = ["1","2","3","4","5","6","7","8","9","0","A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i",
                               "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r",
                               "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
        length_possible_characters = len(possible_characters)
        for pos in range(length):
            rand_int = random.randint(0, length_possible_characters - 1)
            password = password + possible_characters[rand_int]
        return password
    if type == "char_num_special-char":
        possible_characters = ["+","*","%","&","/","(",")","=","?","^","!","$"",",".","-",";",":","_","1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "a", "B", "b", "C", "c", "D", "d",
                               "E", "e", "F", "f", "G", "g", "H", "h", "I", "i",
                               "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r",
                               "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
        length_possible_characters = len(possible_characters)
        for pos in range(length):
            rand_int = random.randint(0, length_possible_characters - 1)
            password = password + possible_characters[rand_int]
        return password
def configure():
    # the length defines, how long the password will be
    length = 16
    # type defines, what types of character is the password made of:
    # "char" = only characters (e.g. "EfhweHEFsaH")
    # "char_num" = characters and numbers (e.g. "A73jI39hP")
    # "char_num_special-char" = characters, numbers and special characters (e.g. "U!48jl.(jd")
    # the special characters are: +*%&/()=?^!$,.-;:_
    type = "char_num_special-char"
    print("length of password:")
    print(length)
    print("type of password:")
    print(type)
    print("Generated password:")
    print(Password_Generator(length,type))

if __name__ == '__main__':
    configure()

#translate any word or sentence from Tuzmifdenki to english language.
english = input()
eng_result = ""
for i in english:
	if i == " ":
		eng_result += " "
	if i == "a":
		eng_result += "mif"
	if i == "A":
		eng_result += "Mif"
	if i == "b":
		eng_result += "qar"
	if i == "B":
		eng_result += "Qar"
	if i == "c":
		eng_result += "ui"
	if i == "C":
		eng_result += "Ui"
	if i == "d":
		eng_result += "ped"
	if i == "D":
		eng_result += "Ped"
	if i == "e":
		eng_result += "si"
	if i == "E":
		eng_result += "Si"
	if i == "f":
		eng_result += "wel"
	if i == "F":
		eng_result += "Wel"
	if i == "g":
		eng_result += "ki"
	if i == "G":
		eng_result += "Ki"
	if i == "h":
		eng_result += "bon"
	if i == "H":
		eng_result += "Bon"
	if i == "i":
		eng_result += "ku"
	if i == "I":
		eng_result += "Ku"
	if i == "j":
		eng_result += "ur"
	if i == "J":
		eng_result += "Ur"
	if i == "k":
		eng_result += "art"
	if i == "K":
		eng_result += "Art"
	if i == "l":
		eng_result += "tuz"
	if i == "L":
		eng_result += "Tuz"
	if i == "m":
		eng_result += "vox"
	if i == "M":
		eng_result += "Vox"
	if i == "n":
		eng_result += "den"
	if i == "N":
		eng_result += "Den"
	if i == "o":
		eng_result += "o"
	if i == "O":
		eng_result += "O"
	if i == "p":
		eng_result += "ya"
	if i == "P":
		eng_result += "Ya"
	if i == "q":
		eng_result += "ik"
	if i == "Q":
		eng_result += "Ik"
	if i == "r":
		eng_result += "pit"
	if i == "R":
		eng_result += "Pit"
	if i == "s":
		eng_result += "yo"
	if i == "S":
		eng_result += "Yo"
	if i == "t":
		eng_result += "ev"
	if i == "T":
		eng_result += "Ev"
	if i == "u":
		eng_result += "feq"
	if i == "U":
		eng_result += "Feq"
	if i == "v":
		eng_result += "ji"
	if i == "V":
		eng_result += "Ji"
	if i == "w":
		eng_result += "sez"
	if i == "W":
		eng_result += "Sez"
	if i == "x":
		eng_result += "guy"
	if i == "X":
		eng_result += "Guy"
	if i == "y":
		eng_result += "rov"
	if i == "Y":
		eng_result += "Rov"
	if i == "z":
		eng_result += "lya"
	if i == "Z":
		eng_result += "Lya"
	if i == ".":
		eng_result += "me"
	if i == ",":
		eng_result += "do"
	if i == "?":
		eng_result += "hon"
	if i == "!":
		eng_result += "apr"
	if i == ";":
		eng_result += "bro"
	if i == ":":
		eng_result += "ci"
if eng_result != "":
    print(eng_result)
#text = input("What is your text? ")
text = eng_result
result = ""
word = text
for i in range(len(word)):
    if word[i] == " ":
        result += " "
    if word[i] == "t":
        if word[i + 1] == "u":
            if word[i + 2] == "z":
                result += "l"
    if word[i] == "T":
    	if word[i + 1] == "u":
    		if word[i + 2] == "z":
    			result += "L"
    if word[i] == "b":
    	if word[i + 1] == "o":
    		if word[i + 2] == "n":
			    result += "h"
    if word[i] == "B":
    	if word[i + 1] == "o":
		    if word[i + 2] == "n":
		    	result += "H"
    if word[i] == "a":
    	if word[i + 1] == "r":
    		if word[i + 2] == "t":
    			result += "k"
    if word[i] == "A":
    	if word[i + 1] == "r":
		    if word[i + 2] == "t":
		    	result += "k"
    if word[i] == "m":
	    if word[i + 1] == "i":
	    	if word[i + 2] == "f":
			    result += "a"
    if word[i] == "M":
	    if word[i + 1] == "i":
		    if word[i + 2] == "f":
			    result += "A"
    if word[i] == "d":
    	if word[i + 1] == "e":
	    	if word[i + 2] == "n":
		    	result += "n"
    if word[i] == "D":
    	if word[i + 1] == "e":
	    	if word[i + 2] == "n":
		    	result += "N"
    if word[i] == "k":
        if i + 1 < len(word):
	        if word[i + 1] == "i":
	            result += "g"
	        if word[i + 1] == "u":
	    	    result += "i"
    if word[i] == "K":
	    if word[i + 1] == "i":
		    result += "G"
    if word [i] == "K":
        if word[i + 1] == "u":
        	result += "I"
    if word[i] == "w":
    	if word[i + 1] == "e":
	    	if word[i + 2] == "l":
		    	result += "f"
    if word[i] == "W":
    	if word[i + 1] == "e":
	    	if word[i + 2] == "l":
		    	result += "F"
    if word[i] == "p":
    	if word[i + 1] == "e":
	    	if word[i + 2] == "d":
		    	result += "d"
    if word[i] == "P":
	    if word[i + 1] == "e":
	    	if word[i + 2] == "d":
		    	result += "D"
    if word[i] == "q":
    	if i + 2 < len(word):
    	    if word[i + 1] == "a":
	    	    if word[i + 2] == "r":
			        result += "b"
    if word[i] == "Q":
	    if word[i + 1] == "a":
	    	if word[i + 2] == "r":
			    result += "B"
    if word[i] == "u":
	    if word[i + 1] == "i":
	    	result += "c"
	    if word[i + 1] == "r":
	    	result += "j"
    if word[i] == "U":
    	if word[i + 1] == "i":
	    	result += "C"
    	if word[i + 1] == "r":
	    	result += "J"
    if word[i] == "s":
	    if word[i + 1] == "i":
	    	result += "e"
    if word[i] == "S":
	    if word[i + 1] == "i":
	    	result += "E"
    if word[i] == "v":
	    if word[i + 1] == "o":
		    if word[i + 2] == "x":
			    result += "m"
    if word[i] == "V":
    	if word[i + 1] == "o":
	    	if word[i + 2] == "x":
			    result += "M"
    if word[i] == "o":
    	if i - 3 >= 0:
    		if word[i - 1] == "r":
    			if word[i - 2] == "a":
    				if word[i - 3] == "q":
    					result += "o"
    	if i + 1 < len(word):
        	if word[i + 1] != "n" and word[i + 1] != "x" and word[i + 1] != "N" and word[i + 1] != "X":
	        	if word[i - 1] != "r" and word[i - 1] != "R" and word[i - 1] != "b" and word[i - 1] != "B" and word[i - 1] != "y" and word[i - 1] != "h" and word[i - 1] != "d" and word[i - 1] != "Y" and word[i - 1] != "H" and word[i - 1] != "D":
			        result += "o"
    if word[i] == "O":
	    result += "O"
    if word[i] == "y":
    	if i - 1 >= 0:
    	    if word[i - 1] != "l":
                if word[i + 1] == "a":
	                result += "p"
    if word[i] == "Y":
    	if i + 1 <= len(word):
        	if word[i - 1] == "l" or word[i - 1] == "L":
        	    if word[i + 1] == "a":
                	result += "P"
    if word[i] == "i":
    	if i + 1 < len(word):
    	    if word[i + 1] == "k":
		        if word[i - 1] != "m" and word[i - 1] != "u" and word[i - 1] != "s" and word[i - 1] != "k" and word[i - 1] != "j" and word[i - 1] != "c" and word[i - 1] != "M" and word[i - 1] != "U" and word[i - 1] != "S" and word[i - 1] != "K" and word[i - 1] != "J":
			        result += "q"
    if word[i] == "I":
    	if word[i + 1] == "k":
	        result += "Q"
    if word[i] == "y":
	    if word[i + 1] == "o":
		    result += "s"
    if word[i] == "Y":
    	if word[i + 1] == "o":
		    result += "S"
    if word[i] == "p":
	    if word[i + 1] == "i":
	    	if word[i + 2] == "t":
			    result += "r"
    if word[i] == "P":
    	if word[i + 1] == "i":
	    	if word[i + 2] == "t":
		    	result += "R"
    if word[i] == "e":
	    if word[i + 1] == "v":
	    	result += "t"
    if word[i] == "E":
	    if word[i + 1] == "v":
		    result += "T"
    if word[i] == "f":
	    if word[i + 1] == "e":
		    if word[i + 2] == "q":
			    result += "u"
    if word[i] == "F":
	    if word[i + 1] == "e":
	        if word[i + 2] == "q":
	        	result += "U"
    if word[i] == "j":
    	if word[i + 1] == "i":
		    result += "v"
    if word[i] == "J":
	    if word[i + 1] == "i":
		    result += "V"
    if word[i] == "h" or word[i] == "H":
        if word[i + 1] == "o":
        	if word[i + 2] == "n":
        		result += "?"
    if word[i] == "s":
    	if word[i + 1] == "e":
		    if word[i + 2] == "z":
		    	result += "w"
    if word[i] == "S":
    	if word[i + 1] == "e":
	    	if word[i + 2] == "z":
		    	result += "W"
    if word[i] == "s" or word[i] == "S":
	    if word[i + 1] == "o":
		    if word[i + 2] == "x":
			    result += "."
    if word[i] == "g":
	    if word[i + 1] == "u":
	    	if word[i + 2] == "y":
		    	result += "x"
    if word[i] == "G":
	    if word[i + 1] == "u":
	    	if word[i + 2] == "y":
		    	result += "X"
    if word[i] == "r":
    	if i + 1 < len(word):
    	    if word[i + 1] == "o":
	    	    if word[i + 2] == "v":
		        	result += "y"
    if word[i] == "R":
    	if i + 2 < len(word):
    	    if word[i + 1] == "o":
	        	if word[i + 2] == "v":
	        		result += "Y"
    if word[i] == "l":
	    if word[i + 1] == "y":
		    if word[i + 2] == "a":
			    result += "z"
    if word[i] == "L":
	    if word[i + 1] == "y":
		    if word[i + 2] == "a":
		    	result += "Z"
    if word[i] == "d" or word[i] == "D":
	    if word[i + 1] == "o":
		    result += ","
    if word[i] == "b" or word[i] == "B":
    	if word[i + 1] == "r":
	    	if word[i + 2] == "o":
		    	result += ";"
    if word[i] == "a" or word[i] == "A":
	    if word[i + 1] == "p":
	    	if word[i + 2] == "r":
		    	result += "!"
    if word[i] == "c" or word[i] == "C":
	    if word[i + 1] == "i":
	    	result += ":"
    if word[i] == "m" or word[i] == "M":
	    if word[i + 1] == "e":
		    result += "."
if result == "":
	print("Your text is empty or it is not characters of Tuzmifdenki language.")
else:
	print(result)
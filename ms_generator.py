import os
import sys

def generate_dic_file():
    dic_file = ""
    for root, dirs, files in os.walk("."):
        for file in files:
            if not file.endswith(".dic") and not file.endswith(".md") and (file.endswith(".yaml") or file.endswith(".yml" or file.endswith(".json"))):
                file_name = os.path.join(root, file)
                file = open(file_name, "r")
                all_lines = file.read()
                # remove all special characters
                #all_lines = all_lines.replace(":","")
                all_lines = all_lines.replace(";","")
                all_lines = all_lines.replace(",","")
                #all_lines = all_lines.replace(".","")
                all_lines = all_lines.replace("(","")
                all_lines = all_lines.replace(")","")
                all_lines = all_lines.replace("[","")
                all_lines = all_lines.replace("]","")
                all_lines = all_lines.replace("{","")
                all_lines = all_lines.replace("}","")
                all_lines = all_lines.replace("“","")
                all_lines = all_lines.replace("”","")
                all_lines = all_lines.replace("‘","")
                all_lines = all_lines.replace("’","")
                all_lines = all_lines.replace("…","")
                all_lines = all_lines.replace("=","")
                all_lines = all_lines.replace("+","")
                all_lines = all_lines.replace("*","")
                #all_lines = all_lines.replace("/","")
                #all_lines = all_lines.replace("\\","")
                all_lines = all_lines.replace("|","")
                all_lines = all_lines.replace("\"","")
                all_lines = all_lines.replace("'","")
                all_lines = all_lines.replace("#","")
                all_lines = all_lines.replace("`","")
                #print(all_lines)
                all_lines = all_lines.split("\n")
                for line in all_lines:
                    # get all words from line
                    words = line.split(" ")
                    #print(words)
                    for word in words:
                        dic_file += word + "\n"
    # reomve duplicates
    dic_file = set(dic_file.split("\n"))
    dic_file = "\n".join(dic_file)
    # remove empty lines
    dic_file = dic_file.replace("::","\n")
    dic_file = dic_file.replace("/","\n")
    dic_file = dic_file.replace("\n\n","\n")

    #print(dic_file)
    print("Writing to file...")
    # write to file
    file = open("out.dic", "w")
    file.write(dic_file)

    return True


                

def main():
    print("===========================")
    print("= Hello I am Mohamed Sherby l0x0ffy :) =")
    print("=   Twitter: @l0x0ffy   =")
    print("===========================")
    
    print("Starting...")
    generate_dic_file()
main()

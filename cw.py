import itertools
import argparse
import time
import math

parser = argparse.ArgumentParser(description="Otomatic password creator")
parser.add_argument("-f",'--way',required=True,help="Save files for this passwords")
parser.add_argument("-s","--length",type=int,required=True,help="max password length")
args = parser.parse_args()

def banner():
    print("""
    🐍
    CREATOR BY DAĞIZTANLI08 
        Twitter:
            08Ztanl
    🐍
    """)

def sifreolustur(sifre_uzunluk,sayac=0):
    try:
        name = str(input("[+]Name of focus:"))
        surname = str(input("[+]Surname of focus:")) 
        number = input("[+]what is the favorite number of focus:")
        animal = str(input("[+]What is the favorite animal of focus:"))
        memleket = str(input("[+]What is the favorite city of focus:"))
        born_date = input("[+]What is the date of birth of focus:")
        color = str(input("[+]What is the favorite color of focus:"))
                           
        dosya_1 = open(args.way,"w")
        for l in range(1,sifre_uzunluk):
            c = itertools.permutations(str(name+surname+str(number)+animal+memleket+str(born_date)+color),l+1)
            for i in c:
                line = "".join(str(m) for m in i)
                dosya_1.write(line + '\n')
                sayac += 1
        if sayac == 0:
            print("You are EMPTY man because all the question are empty")
        
        print("{} tane şifre oluşturuldu".format(sayac))
        dosya_1.close()

    except ValueError:
            print("only number please so type(integer)")
            exit()
    except KeyboardInterrupt:
            print("\n"+"When you used CTRL+C python gives this error message :) or when you used unsupported character")
            exit()
    except:
            print("something went wrong")
            exit()
                                                                                                             
if __name__ == '__main__':
    banner()
    time.sleep(0.3)
    sifreolustur(args.length)

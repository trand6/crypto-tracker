import pandas as pd
from pycoingecko import CoinGeckoAPI

# https://github.com/man-c/pycoingecko
cg = CoinGeckoAPI()

##### ------------- FUNCTIONS ------------- #####
def get_price():
    '''id of token, a single str or a list'''
    id = input("Enter cryptocurrency: ")
    output = cg.get_price(ids=id, vs_currencies=['usd','vnd'])
    print(f"{id.title()}\n{output['bitcoin']}\n")

def list_exchanges():
    '''display top 25 exchanges'''
    count = int(input("Display how many top exchanges? "))
    data =cg.get_exchanges_list()
    df = pd.DataFrame(data, columns=['name', 'trust_score','trust_score_rank'])
    df.set_index('name',inplace=True)

    #add user input for how many
    ranking = df.head(count)
    print(f"{ranking}\n")

def trending():
    trending = cg.get_search_trending()

    #add dataframe here
    #add user input for how many

    print(f"{trending}\n")

def list_currencies():
    '''display supported currencies'''
    currencies = cg.get_supported_vs_currencies()
    print(f"{currencies}\n")

##### ------------- MAIN ------------- #####
# edit as needed to print whatever you need

def main():
    options = ["Enter 0 to exit", "Price", "Exchanges", "Trending", "Currencies"]

    loop = True
    while loop:
        
        for i in range(len(options)):
            print(str(i) + ":", options[i])
        choice = int(input("------------------------------------\nHi, what do you need? type 0 to exit: \n"))
        if choice in range(0, len(options)+1):
            if choice == 0:
                loop = False
                print("\n>> powering off ...\n")
                break
            if choice == 1:
                get_price()
            elif choice == 2:
                list_exchanges()
            elif choice == 3:
                trending()
            elif choice == 4:
                list_currencies()
        else:
            print("Invalid input!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: # ctrl + c to end program
        print("\n>> powering off ...\n")
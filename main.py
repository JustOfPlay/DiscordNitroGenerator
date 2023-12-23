import requests


def make_discord_request():
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)'
    }
    data = {
        'partnerUserId': '991a09958b886ab0d3bd2e14593449225bc69a8358dc8390c59d7278b8978f70'
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            json_response = response.json()
            if 'token' in json_response:
                token_value = json_response['token']
                #print("Token: ", token_value) # Debug
                link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}\n"
                f = open("links.dc", "a")
                f.write(link)
                input(f"Your Link >>> {link}")

            else:
                print("Token not found.")
        else:
            print("Cannot call server | Code:", response.status_code)
    except requests.RequestException as e:
        print("Response error:", e)


print("""
 _______   __                                                __        __    __  __    __                         
/       \ /  |                                              /  |      /  \  /  |/  |  /  |                        
$$$$$$$  |$$/   _______   _______   ______    ______    ____$$ |      $$  \ $$ |$$/  _$$ |_     ______    ______  
$$ |  $$ |/  | /       | /       | /      \  /      \  /    $$ |      $$$  \$$ |/  |/ $$   |   /      \  /      \ 
$$ |  $$ |$$ |/$$$$$$$/ /$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$$ |      $$$$  $$ |$$ |$$$$$$/   /$$$$$$  |/$$$$$$  |
$$ |  $$ |$$ |$$      \ $$ |      $$ |  $$ |$$ |  $$/ $$ |  $$ |      $$ $$ $$ |$$ |  $$ | __ $$ |  $$/ $$ |  $$ |
$$ |__$$ |$$ | $$$$$$  |$$ \_____ $$ \__$$ |$$ |      $$ \__$$ |      $$ |$$$$ |$$ |  $$ |/  |$$ |      $$ \__$$ |
$$    $$/ $$ |/     $$/ $$       |$$    $$/ $$ |      $$    $$ |      $$ | $$$ |$$ |  $$  $$/ $$ |      $$    $$/ 
$$$$$$$/  $$/ $$$$$$$/   $$$$$$$/  $$$$$$/  $$/        $$$$$$$/       $$/   $$/ $$/    $$$$/  $$/        $$$$$$/  
                                                                                                                  
                                                                                                                  
                                                                                                                  
  ______                                                      __                                                  
 /      \                                                    /  |                                                 
/$$$$$$  |  ______   _______    ______    ______   ______   _$$ |_     ______    ______                           
$$ | _$$/  /      \ /       \  /      \  /      \ /      \ / $$   |   /      \  /      \                          
$$ |/    |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |                         
$$ |$$$$ |$$    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/                          
$$ \__$$ |$$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |                               
$$    $$/ $$       |$$ |  $$ |$$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |                               
 $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/                                
                                                                                                                  

  _                  _           _    ____   __ _____  _             
 | |                | |         | |  / __ \ / _|  __ \| |            
 | |__  _   _       | |_   _ ___| |_| |  | | |_| |__) | | __ _ _   _ 
 | '_ \| | | |  _   | | | | / __| __| |  | |  _|  ___/| |/ _` | | | |
 | |_) | |_| | | |__| | |_| \__ \ |_| |__| | | | |    | | (_| | |_| |
 |_.__/ \__, |  \____/ \__,_|___/\__|\____/|_| |_|    |_|\__,_|\__, |
         __/ |                                                  __/ |
        |___/                                                  |___/                                                      

""")

make_discord_request()



# 🎫 DiscordNitroGenerator
 Generate nitro Links for free (30 days only)



# 😨 Disclaimer
1. Its only a proof of concept. I am not responsible for anyone who gets in trouble.
---
2. It works **only** for a limited time




# 🤔 How it works
It sends a payload to https://api.discord.gx.games/v1/direct-fulfillment. \
It's an exploit for https://www.opera.com/gx/discord-nitro

### Payload:
headers = {
        'authority': 'api.discord.gx.games',\
        'accept': '*/*',\
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',\
        'content-type': 'application/json',\
        'origin': 'https://www.opera.com',\
        'referer': 'https://www.opera.com/',\
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',\
        'sec-ch-ua-mobile': '?0',\
        'sec-ch-ua-platform': '"Windows"',\
        'sec-fetch-dest': 'empty',\
        'sec-fetch-mode': 'cors',\
        'sec-fetch-site': 'cross-site',\
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)'\
    }\
    data = {\
        'partnerUserId': '991a09958b886ab0d3bd2e14593449225bc69a8358dc8390c59d7278b8978f70'\
    }

# 👀 Instructions
1. Install python interpreter (https://www.python.org/downloads/).
---
2. Install all used libraries (Windows: setup.bat | Linux: setup.sh).
---
3. Execute main.py with **python main.py**.
---
4. Open the links.dc file in your text editor (the file is in the same folder as main.py).
---
5. Open the link in the links.dc file.
---
6. **Enjoy 30 Days Discord Nitro 💜**

# 💰 Donation

If you find DeltaModLoader helpful and wish to support its development, you can donate via Bitcoin:

Bitcoin Address: bc1qyvc8gyplf3nd8plpz0fw3chf3vs499cxcywypd

<img src=".readme-src/btc.webp" alt="Bitcoin Donation" width="50%">


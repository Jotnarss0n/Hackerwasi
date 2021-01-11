import random

header1 = """
 _    _    __    ___  ____ 
( \/\/ )  /__\  / __)(_  _)
 )    (  /(__)\ \__ \ _)(_ 
(__/\__)(__)(__)(___/(____)
"""

header2 = """
 _  _   __   ____  __  
/ )( \ / _\ / ___)(  ) 
\ /\ //    \\___ \ )(  
(_/\_)\_/\_/(____/(__) 
"""

header5 = """
 __      __               .__ 
/  \    /  \_____    _____|__|
\   \/\/   /\__  \  /  ___/  |
 \        /  / __ \_\___ \|  |
  \__/\  /  (____  /____  >__|
       \/        \/     \/    
"""

header6 = """
 __    __          _ 
/ / /\ \ \__ _ ___(_)
\ \/  \/ / _` / __| |
 \  /\  / (_| \__ \ |
  \/  \/ \__,_|___/_|
"""

header7 = """
  _      __         _ 
 | | /| / /__ ____ (_)
 | |/ |/ / _ `(_-</ / 
 |__/|__/\_,_/___/_/  
"""

header8 = """
,--.   ,--.               ,--. 
|  |   |  | ,--,--. ,---. `--' 
|  |.'.|  |' ,-.  |(  .-' ,--. 
|   ,'.   |\ '-'  |.-'  `)|  | 
'--'   '--' `--`--'`----' `--' 
"""

header9 = """
 __        __        _ 
 \ \      / /_ _ ___(_)
  \ \ /\ / / _` / __| |
   \ V  V / (_| \__ \ |
    \_/\_/ \__,_|___/_|
"""

header11 = """
 ,--.   ,--.               ,--. 
 |  |   |  | ,--,--. ,---. `--' 
 |  |.'.|  |' ,-.  |(  .-' ,--. 
 |   ,'.   |\ '-'  |.-'  `)|  | 
 '--'   '--' `--`--'`----' `--' 
"""

header12 = """
,--.   ,--.               ,--. 
|  |   |  | ,--,--. ,---. `--' 
|  |.'.|  |' ,-.  |(  .-' ,--. 
|   ,'.   |\ '-'  |.-'  `)|  | 
'--'   '--' `--`--'`----' `--' 
"""

header13 = """
   __     __     ______     ______     __    
  /\ \  _ \ \   /\  __ \   /\  ___\   /\ \   
  \ \ \/ ".\ \  \ \  __ \  \ \___  \  \ \ \  
   \ \__/".~\_\  \ \_\ \_\  \/\_____\  \ \_\ 
    \/_/   \/_/   \/_/\/_/   \/_____/   \/_/ 
"""

header14 = """
 __ __ __   ________   ______    ________     
/_//_//_/\ /_______/\ /_____/\  /_______/\    
\:\\:\\:\ \\::: _  \ \\::::_\/_ \__.::._\/    
 \:\\:\\:\ \\::(_)  \ \\:\/___/\   \::\ \     
  \:\\:\\:\ \\:: __  \ \\_::._\:\  _\::\ \__  
   \:\\:\\:\ \\:.\ \  \ \ /____\:\/__\::\__/\ 
    \_______\/ \__\/\__\/ \_____\/\________\/ 
"""

header15 = """
.-.  .-.  .--.     .---. ,-. 
| |/\| | / /\ \   ( .-._)|(| 
| /  \ |/ /__\ \ (_) \   (_) 
|  /\  ||  __  | _  \ \  | | 
|(/  \ || |  |)|( `-'  ) | | 
(_)   \||_|  (_) `----'  `-' 
"""

header16 = """
 ____      ____              _   
|_  _|    |_  _|            (_)  
  \ \  /\  / /,--.   .--.   __   
   \ \/  \/ /`'_\ : ( (`\] [  |  
    \  /\  / // | |, `'.'.  | |  
     \/  \/  \'-;__/[\__) )[___] 
"""

header17 = """

 ___       __   ________  ________  ___     
|\  \     |\  \|\   __  \|\   ____\|\  \    
\ \  \    \ \  \ \  \|\  \ \  \___|\ \  \   
 \ \  \  __\ \  \ \   __  \ \_____  \ \  \  
  \ \  \|\__\_\  \ \  \ \  \|____|\  \ \  \ 
   \ \____________\ \__\ \__\____\_\  \ \__\
    \|____________|\|__|\|__|\_________\|__|
                            \|_________| 
"""

header18 = """
██╗    ██╗ █████╗ ███████╗██╗
██║    ██║██╔══██╗██╔════╝██║
██║ █╗ ██║███████║███████╗██║
██║███╗██║██╔══██║╚════██║██║
╚███╔███╔╝██║  ██║███████║██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝
"""

def lb_header():
    headers = [header1, header2, header5, header6, header7, header8, header9,
        header11, header12, header13, header14, header15, header16, header17, header18]
    return(random.choice(headers))

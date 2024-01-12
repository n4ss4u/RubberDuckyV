import colorama

colorama.init(autoreset=True)

cyan = colorama.Fore.CYAN
yellow = colorama.Fore.YELLOW

def map_keyboard():
        print(f"""    {yellow}MAPA DE EVENTOS DE PULSACIONES
{cyan}──────────────────────────────────────
{yellow}'0'{cyan}, {yellow}'1'{cyan}, {yellow}'2'{cyan}, {yellow}'4'{cyan}, {yellow}'5'{cyan}, {yellow}'6'{cyan}, {yellow}'7'{cyan}, {yellow}'8'{cyan},
{yellow}'9'{cyan}, {yellow}'='{cyan}, {yellow}'+'{cyan}, {yellow}'-'{cyan}, {yellow}'f1'{cyan}, {yellow}'f2'{cyan}, {yellow}'f3',{cyan} 
{yellow}'f4'{cyan}, {yellow}'f5'{cyan}, {yellow}'f6'{cyan}, {yellow}'f7'{cyan}, {yellow}'f8'{cyan}, {yellow}'f9'{cyan}, 
{yellow}'f10'{cyan}, {yellow}'f11'{cyan}, {yellow}'f12'{cyan}, {yellow}'a'{cyan}, {yellow}'b'{cyan}, {yellow}'c'{cyan}, {yellow}'d'{cyan}, 
{yellow}'e'{cyan}, {yellow}'f'{cyan}, {yellow}'g'{cyan}, {yellow}'h'{cyan}, {yellow}'i'{cyan}, {yellow}'j'{cyan}, {yellow}'k'{cyan}, {yellow}'l'{cyan},  
{yellow}'m'{cyan}, {yellow}'n'{cyan}, {yellow}'o'{cyan}, {yellow}'p'{cyan}, {yellow}'q'{cyan}, {yellow}'r'{cyan}, {yellow}'s'{cyan}, {yellow}'t'{cyan}, 
{yellow}'u'{cyan}, {yellow}'v'{cyan}, {yellow}'w'{cyan}, {yellow}'x'{cyan}, {yellow}'y'{cyan}, {yellow}'z'
{cyan}────────────────────────────────────── 
{yellow}Control inzquierdo  {cyan}= {cyan}'{yellow}ctrlleft{cyan}'
{yellow}Control derecho     {cyan}= {cyan}'{yellow}ctrlright{cyan}'
{yellow}Delete              {cyan}= {cyan}'{yellow}del{cyan}'
{yellow}Flecha arriba       {cyan}= {cyan}'{yellow}arrowup{cyan}'
{yellow}Flecha abajo        {cyan}= {cyan}'{yellow}arrowdown{cyan}'  
{yellow}Flecha derecha      {cyan}= {cyan}'{yellow}arrowright{cyan}'  
{yellow}Flecha izquierda    {cyan}= {cyan}'{yellow}arrowleft{cyan}'
{yellow}Enter               {cyan}= {cyan}'{yellow}enter{cyan}'
{yellow}Escape              {cyan}= {cyan}'{yellow}esc{cyan}'
{yellow}Captura de pantalla {cyan}= {cyan}'{yellow}printscreen{cyan}'
{yellow}Shift izquierdo     {cyan}= {cyan}'{yellow}shiftleft{cyan}'
{yellow}Shift derecho       {cyan}= {cyan}'{yellow}shiftright{cyan}'
{yellow}Espaciadora         {cyan}= {cyan}'{yellow}space{cyan}'
{yellow}Tabulación          {cyan}= {cyan}'{yellow}tab{cyan}'
{yellow}Windows izquierdo   {cyan}= {cyan}'{yellow}winleft{cyan}'
{yellow}Windows derecho     {cyan}= {cyan}'{yellow}winright{cyan}'
{yellow}Alt izquierdo       {cyan}= {cyan}'{yellow}altleft{cyan}'
{yellow}Alt derecho         {cyan}= {cyan}'{yellow}altright{cyan}'
{yellow}Backspace           {cyan}= {cyan}'{yellow}backspace{cyan}'
{cyan}──────────────────────────────────────""")
        

def map_icons(icon_file):
        if icon_file == "1" or icon_file == "01":
            icon_file = "whatsapp"
        elif icon_file == "2" or icon_file == "02":
            icon_file = "facebook"
        elif icon_file == "3" or icon_file == "03":
            icon_file = "telegram"
        elif icon_file == "4" or icon_file == "04":
            icon_file = "netflix"
        elif icon_file == "5" or icon_file == "05":
            icon_file = "youtube"
        elif icon_file == "6" or icon_file == "06":
            icon_file = "snapchat"
        elif icon_file == "7" or icon_file == "07":
            icon_file = "udemy"
        elif icon_file == "8" or icon_file == "08":
            icon_file = "tiktok"
        elif icon_file == "9" or icon_file == "09":
            icon_file = "instagram"
        elif icon_file == "10":
            icon_file = "twitch"
        elif icon_file == "11":
            icon_file = "reddit"
        elif icon_file == "12":
            icon_file = "paypal"
        elif icon_file == "13":
            icon_file = "pinterest"
        elif icon_file == "14":
            icon_file = "htbo"
        elif icon_file == "15":
            icon_file = "discord"
        elif icon_file == "16":
            icon_file = "gmail"
        elif icon_file == "17":
            icon_file = "spotify"
        elif icon_file == "18":
            icon_file = "chrome"
        elif icon_file == "19":
            icon_file = "edge"
        elif icon_file == "20":
            icon_file = "firefox"
        elif icon_file == "21":
            icon_file = "opera"
        elif icon_file == "22":
            icon_file = "tor"
        elif icon_file == "23":
            icon_file = "photoshop"
        elif icon_file == "24":
            icon_file = "adobexd"
        elif icon_file == "25":
            icon_file = "steam"
        elif icon_file == "26":
            icon_file = "alert"
        elif icon_file == "27":
            icon_file = "flstudio"
        elif icon_file == "28":
            icon_file = "folder1"
        elif icon_file == "29":
            icon_file = "folder2"
        elif icon_file == "30":
            icon_file = "folder3"
        elif icon_file == "31":
            icon_file = "folder4"
        elif icon_file == "32":
            icon_file = "traductor"
        elif icon_file == "33":
            icon_file = "photo"
        elif icon_file == "34":
            icon_file = "maps"
        elif icon_file == "35":
            icon_file = "drive"
        elif icon_file == "36":
            icon_file = "photo1"
        elif icon_file == "37":
            icon_file = "photo2"
        elif icon_file == "38":
            icon_file = "pdf1"
        elif icon_file == "39":
            icon_file = "media"
        elif icon_file == "40":
            icon_file = "xxx"
        elif icon_file == "41":
            icon_file = "meet"
        elif icon_file == "42":
            icon_file = "word"
        elif icon_file == "43":
            icon_file = "minecraft"
        elif icon_file == "44":
            icon_file = "roblox"
        elif icon_file == "45":
            icon_file = "gtav"
        elif icon_file == "46":
            icon_file = "sims"
        elif icon_file == "47":
            icon_file = "private"
        elif icon_file == "48":
            icon_file = "IMGxxx1"
        elif icon_file == "49":
            icon_file = "IMGxxx2"
        elif icon_file == "50":
            icon_file = "IMGxxx3"

        return icon_file

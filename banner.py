import os
import colorama
import time

colorama.init(autoreset=True)

red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN

def config_project():
     config = """<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <ApplicationIcon>XXXXXX</ApplicationIcon>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="InputSimulator" Version="1.0.4" />
  </ItemGroup>

</Project>
"""
     return config


def banner_main_move():
     os.system("clear")
     list_fisrt_line = ["c", "r", "i", "p", "t", ":", " ", f"{yellow}R", "o", "b", "b", "e", "r", "D", "u", "c", "k", "y", "-", "V"]
     list_senc_line = ["r", "e", "a", "d", "o", "r", ":", " ", f"{yellow}n", "4", "s", "s", "4", "u"]
     list_thre_line = [":", " ", f"{yellow}h", "t", "t", "p", "s", ":", "/", "/", "a", "g", "o", "r", "a", "l", "a", "t", "a", "m"]
     list_four_line = [":", " ", f"{yellow}v", "0", ".", "1", " ", "©", " ", "2", "0", "2", "4"]

     space_dynamic = " "
     water_dynamic = "`~"
     first_line = "  S"
     s_line = "  C"
     t_line = "  T"
     f_line = "  V"

     counter_senc_line = 0

     for i in range(0, 22):
        os.system("clear")
        print(cyan + f"\r{space_dynamic}" + yellow + "         ,~~.")
        print(cyan + f"\r{first_line}" + yellow + "      (  6 )-_,")
        print(cyan + f"\r{s_line}" + yellow + " (\___ )=='-'")
        print(cyan + f"\r{t_line}" + yellow + "  \ .   ) )")
        print(cyan + f"\r{f_line}" + yellow + "   \ `-' /    ")
        print(cyan + f"\r{water_dynamic}")
        space_dynamic += " "

        if i < 12:
             water_dynamic += "'`~"
        else:
             water_dynamic += " "

        if counter_senc_line <= 19:
             first_line += list_fisrt_line[i]
        else:
             first_line += " "

        if counter_senc_line <= 13:
             s_line += list_senc_line[i]
        else:
             s_line += " "
             
        if counter_senc_line <= 19:
             t_line += list_thre_line[i]
        else:
             t_line += " "

        if counter_senc_line <= 12:
             f_line += list_four_line[i]
        else:
             f_line += " "

        counter_senc_line += 1
    
        time.sleep(0.05)
        
     print(f"{cyan}──────────────────────────────────────")



def banner_main():
     os.system("clear")

     print(f"                              {yellow},~~.")
     print(f"{cyan}  Script: {yellow}RobberDucky-V      (  6 )-_,")
     print(f"{cyan}  Creador: {yellow}n4ss4u       (\___ )=='-'")
     print(f"{cyan}  T: {yellow}https://agoralatam  \ .   ) )")
     print(f"{cyan}  V: {yellow}v0.1 © 2024          \ `-' /")
     print(f"{cyan}`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~")

     print(f"{cyan}──────────────────────────────────────")




        


def main_code_c():
      main_code = """using System;
using WindowsInput;
using WindowsInput.Native;
using System.Threading;

namespace PressKey{

    class PressKey{

        static void Main(string[] args){
        
        InputSimulator simulator = new InputSimulator();



        }

    }
}
"""
      return main_code


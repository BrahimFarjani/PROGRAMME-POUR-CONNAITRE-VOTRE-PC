import socket
import platform
import psutil
import subprocess


class bcolors:
    BLUE = '\033[94m'
    AQUI = '\033[34m'
    AQ = '\033[36m'
    CI = '\033[46m'
    END = '\033[0m'

def banner():
    print(bcolors.AQUI + '''                                                                                   
          K   K   N   N    OOO    W   W      Y   Y    OOO    U   U    RRRR       PPPPP CCCCC  
          K  K    NN  N   O   O   W   W       Y Y    O   O   U   U    R   R      P   P C       
          KKK     N N N   O   O   W W W        Y     O   O   U   U    RRRR       PPPP  C                
          K  K    N  NN   O   O   WW WW        Y     O   O   U   U    R  R       P     C     
          K   K   N   N    OOO    W   W        Y      OOO     UUU     R   R      P     CCCCC   
          ''' + bcolors.END) 
    print("\033[44m Cet outil t'aidera à connaître ton PC!    ||    This tool will helpyou to know your PC!     ||      هذه الأداة ستساعدك على معرفة جهاز الكمبيوتر الخاص بك !\033[0m")
    print("\033[36m # Taper un nombre pour voir plus d'informations")
    print("1->Le nom de GPU")
    print("2->La capacité de DISK et son type (SSD/HDD)")
    print("3->La capacité de RAM")
    print("4->Systéme version")
    print("5->Systéme type (84-bit/64-bit/34-bit)")
    print("6->La capacité de CPU")
    print("7->Le nom de Processeur")
    print("8->Le nom de l'appareil")
    print("9->IP adresse")
    print("10->Les informations de configuration complètes (IPconfig / All)\033[0m")


if __name__=='__main__':
    banner()
    

NomHost = socket.gethostname()

inp = int(input("\033[34m #Taper le nombre ici => \033[0m"))

match inp:
    case 1:
        gpu_info = subprocess.check_output("wmic path win32_videocontroller get caption,deviceid", shell=True).decode("utf-8")
        print(f"# Le nom de GPU est: {gpu_info}")

    case 2:
        partitions = psutil.disk_partitions()
        for partition in partitions:    
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"# Total space: {usage.total / (1024**3):.2f} GB")
            print(f"# Espace utilisé: {usage.used / (1024**3):.2f} GB")
            print(f"# Espace libre: {usage.free / (1024**3):.2f} GB")

        try:
            if "ssd" in partition.device.lower():
                 print("# Disk est SSD")

            else:
                 print("# Disk est HDD")

        except Exception as e:
            print(f"Type de Disk non detecté: {e}")

    case 3:
        ram = psutil.virtual_memory().total
        print(f"# RAM est: {ram / (1024**3):.2f} GB")

    case 4:
        system_v = platform.version()[:2]
        print(f"# Version de systéme est Windows {system_v}")

    case 5:
         system_type = platform.architecture()[0]
         print(f"# Type de systéme: {system_type}")

    case 6:
        physical_cores = psutil.cpu_count(logical=False) 
        logical_cores = psutil.cpu_count(logical=True)

        print(f"# CPU les cores physique: {physical_cores}")
        print(f"# CPU les cores local: {logical_cores}")

    case 7:
        processor_info = subprocess.check_output("wmic cpu get name").decode().split("\n")[1].strip()
        print(f"# Le processeur est: {processor_info}")

    case 8:
        print(f"# Le nom de l'appareil est: {NomHost}")
    case 9:
        ip_address = socket.gethostbyname(NomHost)
        print("# IP address est:", ip_address)
    case 10:
        ipconfig_result = subprocess.check_output("ipconfig /all", encoding='cp850')
        print(f"# Les informations de configuration complètes (IPconfig / All): {ipconfig_result}")

import time
import threading

espacio_celda = 5  # Variable global para simular el espacio en la celda de miel
look=threading.Lock()  # Lock para sincronizar el acceso a la celda de miel

def depositar_miel(abeja, cantidad):
    global espacio_celda
    
    
    with look:
        print(f"{abeja} está intentando depositar {cantidad} de miel en la celda.")
        time.sleep(1)  # Simula el tiempo de depósito
        
        if espacio_celda >= cantidad:
            espacio_celda -= cantidad
            print(f"{abeja} ha depositado {cantidad} de miel. Espacio restante en la celda: {espacio_celda}.")
        else:
            print(f"{abeja} no puede depositar {cantidad} de miel. Espacio insuficiente en la celda: {espacio_celda}.")

if __name__ == "__main__":
    ab1="Abeja Obrera #1"
    ab2="Abeja Obrera #2"
    ab3="Abeja Obrera #3"
    
    t1 = threading.Thread(target=depositar_miel, args=(ab1, 3))
    t2 = threading.Thread(target=depositar_miel, args=(ab2, 4))
    t3 = threading.Thread(target=depositar_miel, args=(ab3, 2))
    
    print("Iniciando la deposición de miel en la celda...")
    inicio=time.time()
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    fin=time.time()
    print(f"Tiempo total de recolección: {fin - inicio:.2f} segundos.")
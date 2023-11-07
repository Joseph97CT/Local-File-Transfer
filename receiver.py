import paramiko
import os

def receive_file():
    # Chiedi all'utente l'indirizzo IP del sender
    sender_ip = input("Inserisci l'indirizzo IP del sender (predefinito: 192.168.1.100): ") or '192.168.1.100'

    # Chiedi all'utente la porta SSH (predefinito: 22)
    ssh_port = int(input("Inserisci la porta SSH (predefinito: 22): ") or '22')

    # Chiedi all'utente il nome utente per l'autenticazione SSH
    username = input("Inserisci il nome utente SSH (predefinito: your_username): ") or 'your_username'

    # Crea una connessione SFTP
    transport = paramiko.Transport((sender_ip, ssh_port))

    try:
        transport.connect(username=username, password=None)  # Puoi utilizzare chiavi SSH per l'autenticazione
        sftp = transport.open_sftp()

        # Chiedi all'utente il percorso remoto del file da ricevere
        remote_path = input("Inserisci il percorso remoto del file da ricevere: ")

        # Chiedi all'utente il percorso locale in cui desideri salvare il file
        local_path = input("Inserisci il percorso locale dove desideri salvare il file: ")

        # Verifica se il file locale esiste
        if os.path.exists(local_path):
            choice = input("Il file locale esiste già. Sovrascrivere? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Operazione annullata.")
                return

        # Chiedi all'utente l'autorizzazione per iniziare il download
        download_choice = input("Vuoi iniziare il download? (yes/no): ").strip().lower()
        if download_choice != 'yes':
            print("Download annullato.")
            return

        sftp.get(remote_path, local_path)
        print(f"File '{remote_path}' ricevuto e salvato in '{local_path}'.")
    except paramiko.AuthenticationException:
        print("Errore di autenticazione SSH. Verifica le credenziali.")
    except paramiko.SSHException as e:
        print(f"Errore SSH: {str(e)}")
    except FileNotFoundError:
        print("Il file specificato non esiste.")
    except Exception as e:
        print(f"Errore durante la ricezione del file: {str(e)}")
    finally:
        if 'sftp' in locals():
            sftp.close()
        transport.close()

if __name__ == "__main__":
    receive_file()

import paramiko
import os

def send_file():
    # Chiedi all'utente il percorso del file da inviare
    file_path = input("Inserisci il percorso del file da inviare: ")

    # Verifica se il file specificato esiste
    if not os.path.exists(file_path):
        print(f"Il file '{file_path}' non esiste.")
        return

    # Chiedi all'utente l'indirizzo IP del receiver
    receiver_ip = input("Inserisci l'indirizzo IP del receiver (predefinito: 192.168.1.100): ") or '127.0.0.1'

    # Chiedi all'utente il nome utente per l'autenticazione SSH
    username = input("Inserisci il nome utente SSH (predefinito: your_username): ") or 'your_username'

    # Chiedi all'utente la porta SSH (predefinito: 22)
    ssh_port = int(input("Inserisci la porta SSH (predefinito: 22): ") or '22')

    # Crea una connessione SFTP
    transport = paramiko.Transport((receiver_ip, ssh_port))

    try:
        transport.connect(username=username, password=None)  # Puoi utilizzare chiavi SSH per l'autenticazione
        sftp = transport.open_sftp()
        sftp.put(file_path, os.path.join(remote_path, os.path.basename(file_path)))

        print(f"File '{file_path}' inviato con successo a '{receiver_ip}:{remote_path}'.")
    except paramiko.AuthenticationException:
        print("Errore di autenticazione SSH. Verifica le credenziali.")
    except paramiko.SSHException as e:
        print(f"Errore SSH: {str(e)}")
    except FileNotFoundError:
        print("Il file specificato non esiste.")
    except Exception as e:
        print(f"Errore durante l'invio del file: {str(e)}")
    finally:
        if 'sftp' in locals():
            sftp.close()
        transport.close()

if __name__ == "__main__":
    send_file()

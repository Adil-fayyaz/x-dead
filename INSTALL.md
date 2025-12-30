# 📥 Guida Installazione X DEAD

## 🎯 Installazione per Principianti

Questa guida ti aiuterà passo-passo ad installare X DEAD anche se non hai mai usato il terminale!

---

## 📱 INSTALLAZIONE SU TERMUX (Android)

### ⚡ Metodo Veloce (Copia e Incolla)

Apri Termux e incolla questo comando:

```bash
pkg update && pkg upgrade -y && pkg install python3 nmap arp-scan -y && python3 x_dead.py
```

**Fatto!** Il tool si avvierà automaticamente.

---

### 📝 Metodo Dettagliato (Passo-Passo)

#### Passo 1: Apri Termux
- Apri l'app **Termux** sul tuo telefono Android

#### Passo 2: Aggiorna Termux
Copia e incolla questo comando, poi premi **Invio**:
```bash
pkg update && pkg upgrade -y
```
Aspetta che finisca (potrebbe richiedere 1-2 minuti)

#### Passo 3: Installa Python
Copia e incolla:
```bash
pkg install python3 -y
```
Premi **Invio** e aspetta

#### Passo 4: Installa nmap
Copia e incolla:
```bash
pkg install nmap -y
```
Premi **Invio** e aspetta

#### Passo 5: Installa arp-scan
Copia e incolla:
```bash
pkg install arp-scan -y
```
Premi **Invio** e aspetta

#### Passo 6: Vai nella cartella del tool
Se hai scaricato `x_dead.py` nella cartella Download:
```bash
cd ~/storage/downloads
```

Se è nella home:
```bash
cd ~
```

#### Passo 7: Avvia X DEAD
```bash
python3 x_dead.py
```

**🎉 Fatto! Il tool è avviato!**

---

## 🐧 INSTALLAZIONE SU KALI LINUX

### ⚡ Metodo Veloce (Copia e Incolla)

Apri il terminale e incolla questo comando:

```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip nmap arp-scan && sudo python3 x_dead.py
```

**Fatto!** Il tool si avvierà automaticamente.

---

### 📝 Metodo Dettagliato (Passo-Passo)

#### Passo 1: Apri il Terminale
- Premi `Ctrl + Alt + T` oppure cerca "Terminal" nel menu

#### Passo 2: Aggiorna il Sistema
Copia e incolla:
```bash
sudo apt-get update
```
Premi **Invio** e inserisci la password quando richiesto

#### Passo 3: Installa Python
Copia e incolla:
```bash
sudo apt-get install -y python3 python3-pip
```
Premi **Invio** e aspetta

#### Passo 4: Installa nmap
Copia e incolla:
```bash
sudo apt-get install -y nmap
```
Premi **Invio** e aspetta

#### Passo 5: Installa arp-scan
Copia e incolla:
```bash
sudo apt-get install -y arp-scan
```
Premi **Invio** e aspetta

#### Passo 6: Vai nella cartella del tool
Se hai salvato `x_dead.py` sul Desktop:
```bash
cd ~/Desktop/kali\ linux\ tool
```

Oppure se è in un'altra cartella, vai lì:
```bash
cd /percorso/della/cartella
```

#### Passo 7: Rendi eseguibile (Opzionale)
```bash
chmod +x x_dead.py
```

#### Passo 8: Avvia X DEAD
```bash
sudo python3 x_dead.py
```

**🎉 Fatto! Il tool è avviato!**

---

## ❓ Domande Frequenti

### Q: Cosa significa "sudo"?
**A:** `sudo` significa "Super User Do" - ti dà i permessi di amministratore. Su Kali Linux è necessario per alcune funzionalità.

### Q: Perché devo inserire la password?
**A:** Quando usi `sudo`, il sistema ti chiede la password per sicurezza. È normale!

### Q: Cosa faccio se vedo "Command not found"?
**A:** Significa che il programma non è installato. Segui i passi di installazione delle dipendenze.

### Q: Posso usare il tool senza root/sudo?
**A:** Sì, ma alcune funzionalità potrebbero non funzionare. Prova prima senza sudo, se non funziona usa sudo.

### Q: Come trovo la mia rete?
**A:** Esegui questo comando:
```bash
ip route show
```
Cerca una riga che inizia con un indirizzo IP tipo `192.168.x.x` o `10.0.x.x`

---

## 🆘 Problemi Comuni

### ❌ "Permission denied"
**Soluzione:** Usa `sudo` prima del comando:
```bash
sudo python3 x_dead.py
```

### ❌ "nmap: command not found"
**Soluzione:** Installa nmap:
- Termux: `pkg install nmap -y`
- Kali: `sudo apt-get install nmap -y`

### ❌ "No devices found"
**Soluzione:** 
1. Verifica di essere connesso al WiFi
2. Prova a inserire manualmente la rete quando richiesto

### ❌ "Network not detected"
**Soluzione:** Inserisci manualmente:
- Network: `192.168.1.0/24` (sostituisci con la tua)
- Interface: `wlan0` (per WiFi) o `eth0` (per cavo)

---

## ✅ Verifica Installazione

Dopo l'installazione, verifica che tutto funzioni:

```bash
# Controlla Python
python3 --version

# Controlla nmap
nmap --version

# Controlla arp-scan
arp-scan --version
```

Se tutti i comandi funzionano, sei pronto! 🚀

---

## 📞 Supporto

Se hai ancora problemi:
1. Rileggi questa guida
2. Controlla di aver seguito tutti i passi
3. Verifica di avere una connessione internet attiva

---

**Buon Hacking! 🎯**

*Created by: Infinity X Team White Devel*


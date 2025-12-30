# 🐧 Guida Completa: Installare e Usare X DEAD su Kali Linux

## 🎯 Guida da Zero per Principianti

Questa guida ti spiega TUTTO passo-passo, anche se non hai mai usato Kali Linux!

---

## 📋 Prerequisiti

Prima di iniziare, assicurati di avere:
- ✅ Kali Linux installato (o live USB)
- ✅ Connessione internet attiva
- ✅ Account con permessi sudo (o root)
- ✅ File `x_dead.py` scaricato

---

## 📥 Passo 1: Scarica X DEAD

### Metodo A: Scarica da GitHub (Consigliato)

1. **Apri il browser** su Kali Linux
2. Vai su: **https://github.com/Adil-fayyaz/x-dead**
3. Clicca sul pulsante verde **"Code"**
4. Clicca su **"Download ZIP"**
5. Estrai il file ZIP
6. Trova il file `x_dead.py`

### Metodo B: Clona con Git

Apri il terminale e scrivi:

```bash
cd ~/Desktop
git clone https://github.com/Adil-fayyaz/x-dead.git
cd x-dead
```

**✅ Test:** Verifica che il file esista:
```bash
ls x_dead.py
```
**Dovresti vedere:** `x_dead.py`

---

## 🔧 Passo 2: Apri il Terminale

### Come aprire il terminale:

**Metodo 1:**
- Premi `Ctrl + Alt + T` (tasti insieme)

**Metodo 2:**
- Clicca sull'icona del terminale nella barra laterale

**Metodo 3:**
- Cerca "Terminal" nel menu applicazioni

**✅ Test:** Vedrai una finestra nera con testo - è normale!

---

## 🔄 Passo 3: Aggiorna il Sistema

**IMPORTANTE:** Prima di installare qualsiasi cosa, aggiorna sempre il sistema!

Copia e incolla questo comando:

```bash
sudo apt-get update
```

**Cosa succede:**
- Ti chiederà la password
- **Scrivi la password** (non la vedrai mentre scrivi - è normale!)
- Premi **Invio**
- Aspetta che finisca (2-5 minuti)
- Vedrai molte righe di testo - è normale!

**✅ Test:** Quando vedi di nuovo il prompt `$` o `#`, è finito!

**Cosa aspettarsi:**
```
Reading package lists... Done
```

---

## 🐍 Passo 4: Installa Python (Se Non C'è)

Kali Linux di solito ha già Python, ma verifichiamo:

```bash
python3 --version
```

**Se vedi:** `Python 3.x.x` → ✅ Python è installato! Vai al passo 5.

**Se vedi:** `command not found` → Installa Python:

```bash
sudo apt-get install -y python3 python3-pip
```

**Cosa succede:**
- Ti chiederà la password
- Aspetta che finisca (1-2 minuti)

**✅ Test:** Dopo l'installazione, verifica:
```bash
python3 --version
```
**Dovresti vedere:** `Python 3.x.x`

---

## 🔍 Passo 5: Installa nmap

nmap è lo scanner di porte che X DEAD usa.

```bash
sudo apt-get install -y nmap
```

**Cosa succede:**
- Ti chiederà la password
- Ti chiederà conferma: `Do you want to continue? [Y/n]`
- Scrivi `Y` e premi **Invio**
- Aspetta che finisca (1-2 minuti)

**✅ Test:** Verifica che nmap funzioni:
```bash
nmap --version
```
**Dovresti vedere:** `Nmap version x.x.x`

---

## 📡 Passo 6: Installa arp-scan (Opzionale ma Consigliato)

arp-scan rende la scansione più veloce.

```bash
sudo apt-get install -y arp-scan
```

**Cosa succede:**
- Ti chiederà la password
- Scrivi `Y` quando chiede conferma
- Aspetta che finisca (1 minuto)

**✅ Test:** Verifica:
```bash
arp-scan --version
```
**Dovresti vedere:** `arp-scan x.x.x`

**Nota:** Se arp-scan non si installa, va bene! Il tool funziona lo stesso con ping scan.

---

## 📁 Passo 7: Vai nella Cartella di X DEAD

### Se hai scaricato nella cartella Download:

```bash
cd ~/Downloads/x-dead
```

### Se hai scaricato sul Desktop:

```bash
cd ~/Desktop/x-dead
```

### Se hai clonato con Git:

```bash
cd ~/Desktop/x-dead
```

**✅ Test:** Verifica che sei nella cartella giusta:
```bash
pwd
```
**Dovresti vedere:** `/home/tuonome/Desktop/x-dead` (o simile)

**✅ Test:** Verifica che il file esista:
```bash
ls x_dead.py
```
**Dovresti vedere:** `x_dead.py`

---

## 🔐 Passo 8: Rendi Eseguibile (Opzionale)

Questo passo non è obbligatorio, ma è utile:

```bash
chmod +x x_dead.py
```

**Cosa fa:** Rende il file eseguibile (puoi avviarlo direttamente)

**✅ Test:** Verifica i permessi:
```bash
ls -l x_dead.py
```
**Dovresti vedere:** `-rwxr-xr-x` (la `x` significa eseguibile)

---

## 🚀 Passo 9: Avvia X DEAD!

Ora puoi avviare il tool!

```bash
sudo python3 x_dead.py
```

**IMPORTANTE:** Usa `sudo` per avere tutti i permessi necessari!

**Cosa succede:**
- Ti chiederà la password
- Vedrai il banner colorato di X DEAD
- Vedrai il menu principale

**✅ Test:** Se vedi il banner e il menu, FUNZIONA! 🎉

---

## 🎯 Passo 10: Usa X DEAD

### Cosa vedrai:

```
██████╗     ██████╗ ███████╗ █████╗ ██████╗ 
╚════██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗
 █████╔╝    ██║  ██║█████╗  ███████║██║  ██║
██╔═══╝     ██║  ██║██╔══╝  ██╔══██║██║  ██║
███████╗    ██████╔╝███████╗██║  ██║██████╔╝
╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ 

     X DEAD v1.0 - Network Control System
    Created by: Infinity X Team White Devel
        Ethical Hackers & Security Experts
═══════════════════════════════════════════════════════════════

[+] X DEAD v1.0 CAPABILITIES:
  ✓ Network Discovery & Mapping
  ✓ Device Enumeration
  ✓ Port Scanning & Service Detection
  ✓ MAC Address & Vendor Identification
  ✓ Hostname Resolution
  ✓ Works on ANY Network
  ⚡ More features coming soon...

═══════════════════════════════════════════════════════════════
  X DEAD - MAIN MENU
═══════════════════════════════════════════════════════════════
1. Scan Network (Auto Discovery)
2. Deep Scan Device
3. View Discovered Devices
4. Network Information
5. Advanced Options
6. Exit
═══════════════════════════════════════════════════════════════

[X DEAD]> 
```

---

## 📖 Come Usare il Menu

### Opzione 1: Scan Network (Scansione Rete)

**Cosa fa:** Trova tutti i dispositivi sulla tua rete

**Come usare:**
1. Premi `1` e premi **Invio**
2. Il tool cerca automaticamente la tua rete
3. Se non la trova, ti chiederà:
   - **Network:** Inserisci `192.168.1.0/24` (sostituisci con la tua rete)
   - **Interface:** Inserisci `wlan0` (WiFi) o `eth0` (Ethernet)
4. Aspetta che scansiona (1-3 minuti)
5. Vedrai la lista dei dispositivi!

**Cosa vedrai:**
```
═══════════════════════════════════════════════════════════════════════════════
  DISCOVERED DEVICES ON NETWORK
═══════════════════════════════════════════════════════════════════════════════

#    IP Address        MAC Address         Hostname                  Vendor
───────────────────────────────────────────────────────────────────────────────
1.   192.168.1.1       aa:bb:cc:dd:ee:ff   router.local              Unknown
2.   192.168.1.100     aa:bb:cc:dd:ee:ff   laptop.local              Unknown

[+] Total devices found: 2
```

---

### Opzione 2: Deep Scan Device (Scansione Approfondita)

**Cosa fa:** Analizza un dispositivo specifico in dettaglio

**Come usare:**
1. Prima fai una scansione rete (Opzione 1)
2. Premi `2` e premi **Invio**
3. Scegli il numero del dispositivo (es: `1`)
4. Aspetta che scansiona le porte (2-5 minuti)
5. Vedrai le porte aperte e i servizi!

**Cosa vedrai:**
```
═══════════════════════════════════════════════════════════════════════════════
  DEEP SCAN RESULTS - 192.168.1.1
═══════════════════════════════════════════════════════════════════════════════

OPEN PORTS & SERVICES:

Port        State      Service
──────────────────────────────────────────────────
  22/tcp    open       ssh
  80/tcp    open       http
  443/tcp   open       https
```

---

### Opzione 3: View Discovered Devices (Vedi Dispositivi)

**Cosa fa:** Mostra i dispositivi trovati nell'ultima scansione

**Come usare:**
1. Premi `3` e premi **Invio**
2. Vedrai la lista dei dispositivi trovati

**Nota:** Devi aver fatto almeno una scansione prima!

---

### Opzione 4: Network Information (Informazioni Rete)

**Cosa fa:** Mostra informazioni sulla tua rete

**Come usare:**
1. Premi `4` e premi **Invio**
2. Vedrai:
   - Network (rete)
   - Gateway (router)
   - Interface (interfaccia di rete)
   - Scan Time (ora della scansione)

**Cosa vedrai:**
```
═══════════════════════════════════════════════════════════════
  NETWORK INFORMATION
═══════════════════════════════════════════════════════════════

Network:     192.168.1.0/24
Gateway:    192.168.1.1
Interface:  wlan0
Scan Time:  2024-01-15 14:30:00
```

---

### Opzione 5: Advanced Options (Opzioni Avanzate)

**Cosa fa:** Mostra le funzionalità future (v2.0)

**Come usare:**
1. Premi `5` e premi **Invio**
2. Vedrai le funzionalità che arriveranno nella v2.0

---

### Opzione 6: Exit (Esci)

**Cosa fa:** Chiude il tool

**Come usare:**
1. Premi `6` e premi **Invio**
2. Il tool si chiude
3. Torni al terminale normale

---

## 🔍 Trovare la Tua Rete

Se il tool non trova automaticamente la rete, devi inserirla manualmente.

### Metodo 1: Comando ip

```bash
ip route show
```

**Cosa vedrai:**
```
default via 192.168.1.1 dev wlan0
192.168.1.0/24 dev wlan0 proto kernel scope link src 192.168.1.100
```

**Cosa prendere:**
- **Network:** `192.168.1.0/24` (la parte con `/24`)
- **Interface:** `wlan0` (dopo `dev`)

### Metodo 2: Comando ifconfig

```bash
ifconfig
```

**Cosa vedrai:**
```
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255
```

**Cosa prendere:**
- **IP:** `192.168.1.100` (dopo `inet`)
- **Network:** `192.168.1.0/24` (primi 3 numeri dell'IP + `/24`)
- **Interface:** `wlan0` (nome dell'interfaccia)

---

## ❓ Problemi Comuni

### Problema: "Permission denied"

**Soluzione:**
Usa `sudo`:
```bash
sudo python3 x_dead.py
```

---

### Problema: "Command not found: nmap"

**Soluzione:**
Installa nmap:
```bash
sudo apt-get install -y nmap
```

---

### Problema: "No devices found"

**Soluzioni:**
1. Verifica di essere connesso al WiFi/Ethernet
2. Controlla l'interfaccia: `ip addr show`
3. Inserisci manualmente la rete quando chiede
4. Prova con un'altra interfaccia (wlan0, eth0, etc.)

---

### Problema: "Network not detected"

**Soluzione:**
Inserisci manualmente:
- Network: `192.168.1.0/24` (sostituisci con la tua)
- Interface: `wlan0` (WiFi) o `eth0` (Ethernet)

Per trovare la tua rete:
```bash
ip route show
```

---

### Problema: "Python not found"

**Soluzione:**
Installa Python:
```bash
sudo apt-get install -y python3
```

---

## ✅ Checklist Installazione

Dopo l'installazione, verifica:

- [ ] Python installato: `python3 --version`
- [ ] nmap installato: `nmap --version`
- [ ] arp-scan installato: `arp-scan --version` (opzionale)
- [ ] File x_dead.py presente: `ls x_dead.py`
- [ ] Tool si avvia: `sudo python3 x_dead.py`

**Se tutti i check sono ✅, sei pronto!**

---

## 🚀 Comandi Rapidi (Tutto in Uno)

Se vuoi fare tutto velocemente:

```bash
# 1. Aggiorna sistema
sudo apt-get update

# 2. Installa dipendenze
sudo apt-get install -y python3 python3-pip nmap arp-scan

# 3. Vai nella cartella
cd ~/Desktop/x-dead

# 4. Avvia X DEAD
sudo python3 x_dead.py
```

---

## 🎯 Esempio Completo di Uso

### Scenario: Scansionare la rete di casa

1. **Avvia il tool:**
   ```bash
   sudo python3 x_dead.py
   ```

2. **Scansiona la rete:**
   - Premi `1`
   - Se chiede la rete, inserisci: `192.168.1.0/24`
   - Se chiede l'interfaccia, inserisci: `wlan0`
   - Aspetta...

3. **Vedi i dispositivi:**
   - Vedrai tutti i dispositivi connessi
   - Router, telefoni, computer, etc.

4. **Analizza un dispositivo:**
   - Premi `2`
   - Scegli un dispositivo (es: `1` per il router)
   - Vedrai le porte aperte

5. **Esci:**
   - Premi `6`

---

## 📚 Risorse Utili

- **Repository GitHub:** https://github.com/Adil-fayyaz/x-dead
- **Documentazione:** Vedi README.md
- **Guida Installazione:** Vedi INSTALL.md
- **Guida Test:** Vedi TEST_GUIDE.md

---

**Buon uso di X DEAD! 🎉**

*Created by: Infinity X Team White Devel*


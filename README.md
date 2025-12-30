# 🔴 X DEAD v1.0 - Network Control System

<div align="center">

**Created by: Infinity X Team White Devel**  
**Ethical Hackers & Security Experts**

[![Version](https://img.shields.io/badge/version-1.0-red.svg)](https://github.com)
[![Platform](https://img.shields.io/badge/platform-Kali%20Linux%20%7C%20Termux-blue.svg)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.6+-green.svg)](https://python.org)

</div>

---

## 📖 Descrizione

**X DEAD** è un potente tool di network discovery e controllo progettato per **Kali Linux** e **Termux**. Fornisce scansione completa della rete, enumerazione dei dispositivi e analisi avanzata della rete.

### ⚡ Caratteristiche Principali

- ✅ **Network Discovery**: Rilevamento automatico e mappatura della rete
- ✅ **Device Enumeration**: Scoperta completa dei dispositivi con IP, MAC, hostname e vendor
- ✅ **Port Scanning**: Scansione avanzata delle porte con rilevamento servizi
- ✅ **Multi-Platform**: Funziona su Kali Linux e Termux
- ✅ **Interfaccia Interattiva**: Bellissima interfaccia CLI colorata
- ✅ **Scansione Real-time**: Scansione veloce della rete basata su ARP e ping

---

## 🚀 Installazione Rapida

### 📱 Su Termux (Android)

#### Metodo 1: Installazione Automatica (Consigliato)

```bash
# Copia e incolla tutto questo comando:
pkg update && pkg upgrade -y && pkg install python3 nmap arp-scan -y && python3 x_dead.py
```

#### Metodo 2: Installazione Manuale

**Passo 1:** Apri Termux e aggiorna:
```bash
pkg update && pkg upgrade -y
```

**Passo 2:** Installa le dipendenze:
```bash
pkg install python3 nmap arp-scan -y
```

**Passo 3:** Vai nella cartella del tool:
```bash
cd ~/storage/downloads  # se hai scaricato qui
# oppure
cd ~  # se è nella home
```

**Passo 4:** Avvia X DEAD:
```bash
python3 x_dead.py
```

---

### 🐧 Su Kali Linux

#### Metodo 1: Installazione Automatica (Consigliato)

```bash
# Copia e incolla tutto questo comando:
sudo apt-get update && sudo apt-get install -y python3 python3-pip nmap arp-scan && sudo python3 x_dead.py
```

#### Metodo 2: Installazione Manuale

**Passo 1:** Apri il terminale e aggiorna il sistema:
```bash
sudo apt-get update
```

**Passo 2:** Installa le dipendenze:
```bash
sudo apt-get install -y python3 python3-pip nmap arp-scan
```

**Passo 3:** Vai nella cartella del tool:
```bash
cd ~/Desktop/kali\ linux\ tool  # o dove hai salvato il file
```

**Passo 4:** Rendi eseguibile lo script:
```bash
chmod +x x_dead.py
```

**Passo 5:** Avvia X DEAD (con sudo per funzionalità avanzate):
```bash
sudo python3 x_dead.py
```

---

## 🎯 Come Usare X DEAD

### 1️⃣ Avvio del Tool

Dopo l'installazione, avvia semplicemente:
```bash
python3 x_dead.py
# oppure su Kali Linux:
sudo python3 x_dead.py
```

### 2️⃣ Menu Principale

Vedrai un menu con queste opzioni:

```
1. Scan Network (Auto Discovery)    - Scansiona automaticamente la rete
2. Deep Scan Device                 - Analisi approfondita di un dispositivo
3. View Discovered Devices          - Visualizza i dispositivi trovati
4. Network Information               - Mostra informazioni sulla rete
5. Advanced Options                  - Opzioni avanzate (v2.0)
6. Exit                              - Esci dal programma
```

### 3️⃣ Scansione della Rete

1. Seleziona l'opzione **1** dal menu
2. Il tool rileverà automaticamente la tua rete
3. Se non riesce, ti chiederà di inserire:
   - **Network**: Esempio `192.168.1.0/24` (sostituisci con la tua rete)
   - **Interface**: Esempio `wlan0` o `eth0`

### 4️⃣ Visualizzare i Dispositivi

Dopo la scansione, vedrai tutti i dispositivi connessi con:
- 📍 Indirizzo IP
- 🔢 Indirizzo MAC
- 🏷️ Hostname
- 🏭 Vendor/Produttore

### 5️⃣ Deep Scan

1. Seleziona l'opzione **2** dal menu
2. Scegli il numero del dispositivo da analizzare
3. Il tool eseguirà una scansione approfondita delle porte

---

## 📋 Requisiti di Sistema

### Dipendenze Software:
- **Python 3.6+** (già incluso in Kali/Termux)
- **nmap** (scanner di porte)
- **arp-scan** (scansione ARP)

### Permessi:
- **Root/Sudo** (consigliato per funzionalità complete)
- **Permessi di rete** (per scansione)

---

## 🔧 Risoluzione Problemi

### ❌ Problema: "Command not found: nmap"

**Soluzione:**
```bash
# Su Termux:
pkg install nmap -y

# Su Kali Linux:
sudo apt-get install nmap -y
```

### ❌ Problema: "Permission denied"

**Soluzione:**
```bash
# Su Kali Linux, usa sudo:
sudo python3 x_dead.py

# Su Termux, se necessario:
su
python3 x_dead.py
```

### ❌ Problema: "No devices found"

**Soluzioni:**
1. Verifica di essere connesso alla rete WiFi
2. Controlla l'interfaccia di rete:
   ```bash
   ip addr show
   ```
3. Inserisci manualmente la rete quando richiesto

### ❌ Problema: "Network not detected"

**Soluzione:**
Inserisci manualmente:
- **Network**: `192.168.1.0/24` (sostituisci `192.168.1` con la tua rete)
- **Interface**: `wlan0` (WiFi) o `eth0` (Ethernet)

Per trovare la tua rete:
```bash
ip route show
```

---

## 📸 Screenshots

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
```

---

## 🔮 Prossime Funzionalità (v2.0)

- 🔍 Network Traffic Analysis
- 🛡️ Vulnerability Assessment
- ⚔️ Exploit Framework Integration
- 🤖 Automated Attack Vectors
- 📊 Advanced Reporting

---

## ⚠️ Disclaimer Legale

**IMPORTANTE:** Questo tool è destinato **SOLO a scopi educativi e di testing autorizzato**. 

- ✅ Usa solo su reti di tua proprietà
- ✅ Usa solo con autorizzazione esplicita
- ❌ Non usare su reti senza permesso
- ❌ L'accesso non autorizzato è illegale

Gli sviluppatori **non sono responsabili** per l'uso improprio di questo strumento.

---

## 👥 Crediti

**Infinity X Team White Devel**  
*Ethical Hackers & Security Experts*

---

## 📝 Licenza

Questo progetto è rilasciato per scopi educativi. Usa responsabilmente.

---

## 🆘 Supporto

Se hai problemi o domande:
1. Controlla la sezione "Risoluzione Problemi" sopra
2. Verifica di aver installato tutte le dipendenze
3. Assicurati di avere i permessi necessari

---

<div align="center">

**⭐ Se questo tool ti è stato utile, lascia una stella su GitHub! ⭐**

Made with ❤️ by **Infinity X Team White Devel**

</div>

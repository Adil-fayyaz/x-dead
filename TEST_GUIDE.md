# 🧪 Guida Completa per Testare X DEAD su Termux

## ✅ Checklist Pre-Test

Prima di testare, assicurati di avere:

- [ ] Termux installato e aggiornato
- [ ] Python 3 installato
- [ ] nmap installato
- [ ] File `x_dead.py` nella cartella corretta
- [ ] Connessione WiFi attiva
- [ ] Permessi di rete (se necessario)

---

## 📋 Installazione Completa (Passo-Passo)

### Passo 1: Aggiorna Termux

```bash
pkg update && pkg upgrade -y
```

**Cosa aspettarsi:**
- Vedrai molte righe di testo
- Aspetta che finisca (1-3 minuti)
- Quando vedi `$` di nuovo, è finito

**✅ Test:** Se vedi `$` senza errori, PASS!

---

### Passo 2: Installa Python

```bash
pkg install python3 -y
```

**Cosa aspettarsi:**
- Ti chiederà: `Do you want to continue? [Y/n]`
- Scrivi `Y` e premi Invio
- Aspetta che finisca (1-2 minuti)

**✅ Test:** Verifica che Python funzioni:
```bash
python3 --version
```
**Dovresti vedere:** `Python 3.x.x`

**✅ Se vedi la versione, PASS!**

---

### Passo 3: Installa nmap

```bash
pkg install nmap -y
```

**Cosa aspettarsi:**
- Ti chiederà conferma
- Scrivi `Y` e premi Invio
- Aspetta che finisca (1-2 minuti)

**✅ Test:** Verifica che nmap funzioni:
```bash
nmap --version
```
**Dovresti vedere:** `Nmap version x.x.x`

**✅ Se vedi la versione, PASS!**

---

### Passo 4: Vai nella Cartella

```bash
cd ~/tools/x-dead
```

**✅ Test:** Verifica che sei nella cartella giusta:
```bash
pwd
```
**Dovresti vedere:** `/data/data/com.termux/files/home/tools/x-dead`

**✅ Test:** Verifica che il file esista:
```bash
ls
```
**Dovresti vedere:** `x_dead.py` nella lista

**✅ Se vedi x_dead.py, PASS!**

---

### Passo 5: Avvia X DEAD

```bash
python3 x_dead.py
```

**Cosa aspettarsi:**
- Vedrai il banner colorato di X DEAD
- Vedrai il menu principale
- Il tool è avviato!

**✅ Test:** Se vedi il banner e il menu, PASS!

---

## 🧪 Test Completo del Tool

### Test 1: Verifica Banner

**Cosa vedere:**
```
██████╗     ██████╗ ███████╗ █████╗ ██████╗ 
╚════██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗
 █████╔╝    ██║  ██║█████╗  ███████║██║  ██║
██╔═══╝     ██║  ██║██╔══╝  ██╔══██║██║  ██║
███████╗    ██████╔╝███████╗██║  ██║██████╔╝
╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ 

     X DEAD v1.0 - Network Control System
```

**✅ Se vedi il banner colorato, PASS!**

---

### Test 2: Verifica Menu

**Cosa vedere:**
```
============================================================
  X DEAD - MAIN MENU
============================================================
1. Scan Network (Auto Discovery)
2. Deep Scan Device
3. View Discovered Devices
4. Network Information
5. Advanced Options
6. Exit
============================================================
```

**✅ Se vedi il menu, PASS!**

---

### Test 3: Test Scansione Rete

1. **Premi `1`** e premi Invio
2. **Cosa aspettarsi:**
   - Il tool cerca di rilevare la rete automaticamente
   - Se non riesce, ti chiederà di inserire:
     - Network (es: `192.168.1.0/24`)
     - Interface (es: `wlan0`)

**Se la rete viene rilevata automaticamente:**
- ✅ Vedrai: `[*] Discovering network...`
- ✅ Vedrai: `[*] Scanning network...`
- ✅ PASS!

**Se ti chiede di inserire manualmente:**
- Inserisci la tua rete (es: `192.168.1.0/24`)
- Inserisci l'interfaccia (es: `wlan0`)
- ✅ Il tool inizierà a scansionare
- ✅ PASS!

---

### Test 4: Verifica Dispositivi Trovati

**Dopo la scansione, dovresti vedere:**

```
═══════════════════════════════════════════════════════════════════════════════
  DISCOVERED DEVICES ON NETWORK
═══════════════════════════════════════════════════════════════════════════════

#    IP Address        MAC Address         Hostname                  Vendor
───────────────────────────────────────────────────────────────────────────────
1.   192.168.1.1       aa:bb:cc:dd:ee:ff   router.local              Unknown
2.   192.168.1.100     aa:bb:cc:dd:ee:ff   phone.local               Unknown

[+] Total devices found: 2
```

**✅ Se vedi almeno 1 dispositivo (anche solo il router), PASS!**

**❌ Se vedi "No devices found":**
- Verifica di essere connesso al WiFi
- Prova a inserire manualmente la rete
- Controlla l'interfaccia di rete: `ip addr show`

---

### Test 5: Test Deep Scan

1. **Premi `2`** e premi Invio
2. **Scegli un dispositivo** (scrivi il numero, es: `1`)
3. **Cosa aspettarsi:**
   - Vedrai: `[*] Deep scanning 192.168.1.1...`
   - Il tool scansionerà le porte
   - Vedrai i risultati

**✅ Se vedi i risultati della scansione, PASS!**

---

### Test 6: Test Network Information

1. **Premi `4`** e premi Invio
2. **Cosa aspettarsi:**
   - Vedrai informazioni sulla rete
   - Network, Gateway, Interface, Scan Time

**✅ Se vedi le informazioni, PASS!**

---

### Test 7: Test Exit

1. **Premi `6`** e premi Invio
2. **Cosa aspettarsi:**
   - Il tool si chiude
   - Torni al prompt `$`

**✅ Se il tool si chiude correttamente, PASS!**

---

## 🔍 Test Avanzati

### Test A: Verifica Dipendenze

```bash
# Test Python
python3 --version
# ✅ Dovrebbe mostrare: Python 3.x.x

# Test nmap
nmap --version
# ✅ Dovrebbe mostrare: Nmap version x.x.x

# Test se arp-scan esiste (opzionale)
which arp-scan
# ❌ Se non esiste, va bene! Il tool funziona lo stesso
```

---

### Test B: Verifica Permessi

```bash
# Verifica permessi di rete
ip addr show
# ✅ Dovresti vedere le interfacce di rete (wlan0, etc.)

# Verifica connessione
ping -c 1 8.8.8.8
# ✅ Dovresti vedere risposta (se hai internet)
```

---

### Test C: Test con Rete Manuale

Se la scansione automatica non funziona:

1. Avvia il tool: `python3 x_dead.py`
2. Premi `1`
3. Quando chiede la rete, inserisci: `192.168.1.0/24` (sostituisci con la tua)
4. Quando chiede l'interfaccia, inserisci: `wlan0`
5. ✅ Il tool dovrebbe scansionare

---

## ❌ Problemi Comuni e Soluzioni

### Problema: "Command not found: python3"

**Soluzione:**
```bash
pkg install python3 -y
```

---

### Problema: "Command not found: nmap"

**Soluzione:**
```bash
pkg install nmap -y
```

---

### Problema: "No devices found"

**Soluzioni:**
1. Verifica connessione WiFi: `ip addr show`
2. Prova rete manuale: inserisci `192.168.1.0/24` quando chiede
3. Verifica interfaccia: usa `wlan0` o quella che vedi con `ip addr show`

---

### Problema: "Permission denied"

**Soluzione:**
- Su Termux di solito non serve root
- Se persiste, prova: `su` (ma di solito non serve)

---

### Problema: "Network not detected"

**Soluzione:**
- Inserisci manualmente quando chiede:
  - Network: `192.168.1.0/24` (sostituisci con la tua rete)
  - Interface: `wlan0` (WiFi) o `eth0` (Ethernet)

---

## ✅ Checklist Finale

Dopo tutti i test, verifica:

- [ ] ✅ Tool si avvia correttamente
- [ ] ✅ Banner e menu appaiono
- [ ] ✅ Scansione rete funziona (automatica o manuale)
- [ ] ✅ Dispositivi vengono trovati
- [ ] ✅ Deep scan funziona
- [ ] ✅ Network information funziona
- [ ] ✅ Exit funziona

**Se tutti i test sono PASS, il tool funziona perfettamente! 🎉**

---

## 🎯 Comandi Rapidi per Test

```bash
# 1. Verifica installazione
python3 --version && nmap --version

# 2. Vai nella cartella
cd ~/tools/x-dead

# 3. Verifica file
ls x_dead.py

# 4. Avvia tool
python3 x_dead.py

# 5. Test scansione (premi 1 nel menu)
# 6. Test deep scan (premi 2 nel menu)
# 7. Test info (premi 4 nel menu)
# 8. Esci (premi 6 nel menu)
```

---

**Buon testing! 🧪**

*Created by: Infinity X Team White Devel*


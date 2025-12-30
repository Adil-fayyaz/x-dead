# 📱 Come Installare X DEAD su Termux - Guida Completa per Principianti

## 🎯 Guida Passo-Passo (Prima Volta)

Questa guida ti aiuterà passo-passo anche se non hai mai usato Termux!

---

## 📥 Passo 1: Scarica X DEAD

### Opzione A: Scarica da GitHub

1. Apri il browser sul telefono
2. Vai su: **https://github.com/Adil-fayyaz/x-dead**
3. Clicca sul pulsante verde **"Code"**
4. Clicca su **"Download ZIP"**
5. Estrai il file ZIP (di solito si estrae automaticamente)
6. Trova il file `x_dead.py` nella cartella scaricata

### Opzione B: Clona con Git (se sai usarlo)

```bash
cd ~
git clone https://github.com/Adil-fayyaz/x-dead.git
cd x-dead
```

---

## 📱 Passo 2: Apri Termux

1. Apri l'app **Termux** sul telefono
2. Vedrai una schermata nera con testo - **è normale!**
3. Aspetta che appaia il simbolo `$` - significa che è pronto

---

## 🔧 Passo 3: Aggiorna Termux

Copia e incolla questo comando (tutto insieme):

```bash
pkg update && pkg upgrade -y
```

**Cosa fare:**
1. Tocca e tieni premuto nella schermata di Termux
2. Seleziona "Paste" (Incolla)
3. Premi **Invio** (il tasto con la freccia)

**Cosa succede:**
- Termux scarica gli aggiornamenti
- Aspetta 1-3 minuti (dipende dalla connessione)
- Vedrai molte righe di testo - **è normale!**
- Quando vedi di nuovo `$`, è finito!

---

## 🐍 Passo 4: Installa Python

Copia e incolla questo comando:

```bash
pkg install python3 -y
```

**Cosa fare:**
1. Incolla il comando
2. Premi **Invio**
3. Ti chiederà: `Do you want to continue? [Y/n]`
4. Scrivi `Y` e premi **Invio**

**Cosa succede:**
- Python viene installato
- Aspetta 1-2 minuti
- Quando vedi `$` di nuovo, è finito!

---

## 🔍 Passo 5: Installa nmap

Copia e incolla:

```bash
pkg install nmap -y
```

**Cosa fare:**
1. Incolla
2. Premi **Invio**
3. Scrivi `Y` quando chiede conferma
4. Aspetta che finisca

---

## 🌐 Passo 6: Installa arp-scan

Copia e incolla:

```bash
pkg install arp-scan -y
```

**Cosa fare:**
1. Incolla
2. Premi **Invio**
3. Scrivi `Y` quando chiede conferma
4. Aspetta che finisca

---

## 📁 Passo 7: Vai alla Cartella del File

### Se hai scaricato il file nella cartella Download:

```bash
cd ~/storage/downloads
```

### Se hai scaricato nella cartella x-dead:

```bash
cd ~/storage/downloads/x-dead
```

### Se non sai dove è il file:

1. Apri il file manager del telefono
2. Cerca `x_dead.py`
3. Ricorda il percorso (es: Download/x-dead/)
4. Usa: `cd ~/storage/downloads/NOME_CARTELLA`

---

## ✅ Passo 8: Verifica che il File Esista

Scrivi:

```bash
ls
```

**Cosa vedrai:**
- Una lista di file
- Dovresti vedere `x_dead.py` nella lista
- Se non lo vedi, sei nella cartella sbagliata!

---

## 🚀 Passo 9: Avvia X DEAD!

Scrivi:

```bash
python3 x_dead.py
```

**Cosa succede:**
- Vedrai il banner colorato di X DEAD
- Vedrai il menu principale
- **Sei dentro!** 🎉

---

## ⚡ METODO VELOCE (Tutto in Uno)

Se vuoi fare tutto velocemente, copia e incolla questo comando:

```bash
pkg update && pkg upgrade -y && pkg install python3 nmap arp-scan -y && cd ~/storage/downloads && python3 x_dead.py
```

**Attenzione:** Assicurati che `x_dead.py` sia nella cartella Downloads!

---

## ❓ Problemi Comuni

### Problema: "No such file or directory"

**Soluzione:**
- Il file `x_dead.py` non è nella cartella corrente
- Usa `cd` per andare nella cartella giusta
- Usa `ls` per vedere i file

### Problema: "Command not found: python3"

**Soluzione:**
- Python non è installato
- Esegui: `pkg install python3 -y`

### Problema: "Permission denied"

**Soluzione:**
- Su Termux di solito non serve root
- Se persiste, prova: `su` (ma di solito non serve)

### Problema: "No devices found" quando usi il tool

**Soluzione:**
1. Assicurati di essere connesso al WiFi
2. Quando chiede la rete, inserisci manualmente:
   - Network: `192.168.1.0/24` (sostituisci con la tua rete)
   - Interface: `wlan0`

---

## 🎯 Come Usare X DEAD (Dopo l'Installazione)

1. **Avvia il tool:** `python3 x_dead.py`
2. **Premi `1`** per scansionare la rete
3. **Aspetta** che trovi i dispositivi
4. **Guarda** la lista dei dispositivi
5. **Premi `2`** per analizzare un dispositivo specifico

---

## ✅ Verifica Installazione

Per verificare che tutto sia installato correttamente:

```bash
# Verifica Python
python3 --version
# Dovrebbe mostrare: Python 3.x.x

# Verifica nmap
nmap --version
# Dovrebbe mostrare: Nmap version x.x.x

# Verifica arp-scan
arp-scan --version
# Dovrebbe mostrare: arp-scan version x.x.x
```

Se tutti i comandi funzionano, sei pronto! 🚀

---

## 📞 Serve Aiuto?

1. Rileggi questa guida passo-passo
2. Verifica di aver seguito tutti i passi
3. Assicurati di avere una connessione internet attiva
4. Controlla che il file `x_dead.py` sia nella cartella giusta

---

**Buona installazione! 🎉**

*Created by: Infinity X Team White Devel*


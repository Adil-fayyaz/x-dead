# 🔧 Fix Problemi Termux - Guida Rapida

## ❌ Problemi che hai incontrato:

1. ❌ `arp-scan` non disponibile su Termux
2. ❌ Cartella `~/storage/downloads` non esiste
3. ❌ File `x_dead.py` non trovato

## ✅ Soluzioni:

### Problema 1: arp-scan non disponibile

**Soluzione:** Ho modificato il tool! Ora funziona SENZA arp-scan!

Il tool ora:
- ✅ Usa `ping` scan se arp-scan non è disponibile
- ✅ Funziona perfettamente su Termux
- ✅ Non richiede arp-scan

**Non devi installare arp-scan!** Il tool funziona lo stesso.

---

### Problema 2: Cartella storage non esiste

**Soluzione:** Dai i permessi a Termux

1. Apri Termux
2. Scrivi:
```bash
termux-setup-storage
```
3. Ti chiederà i permessi - clicca **"Consenti"** o **"Allow"**
4. Ora la cartella esisterà!

---

### Problema 3: File x_dead.py non trovato

**Hai detto che vedi:**
```
~/tools $ ls
x-dead  zphisher
```

Il file è dentro la cartella `x-dead`!

**Soluzione:**

```bash
cd x-dead
ls
```

Dovresti vedere `x_dead.py`!

Poi avvia:
```bash
python3 x_dead.py
```

---

## 🚀 Comandi Completi (Copia e Incolla)

### Passo 1: Dai i permessi storage
```bash
termux-setup-storage
```
(Clicca "Consenti" quando chiede)

### Passo 2: Vai nella cartella x-dead
```bash
cd ~/tools/x-dead
```

### Passo 3: Verifica che il file ci sia
```bash
ls
```
(Dovresti vedere `x_dead.py`)

### Passo 4: Installa solo nmap (arp-scan NON serve!)
```bash
pkg install nmap -y
```

### Passo 5: Avvia X DEAD
```bash
python3 x_dead.py
```

---

## ✅ Installazione Completa Termux (Senza arp-scan)

```bash
# 1. Dai permessi storage
termux-setup-storage

# 2. Aggiorna Termux
pkg update && pkg upgrade -y

# 3. Installa Python (se non ce l'hai)
pkg install python3 -y

# 4. Installa SOLO nmap (arp-scan NON serve!)
pkg install nmap -y

# 5. Vai nella cartella x-dead
cd ~/tools/x-dead

# 6. Avvia X DEAD
python3 x_dead.py
```

---

## 🎯 Ora Funziona!

Il tool è stato aggiornato per funzionare su Termux SENZA arp-scan!

Usa solo:
- ✅ Python 3
- ✅ nmap

**arp-scan NON è necessario!**

---

*Created by: Infinity X Team White Devel*


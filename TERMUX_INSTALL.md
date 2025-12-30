# 🚀 Come Avviare X DEAD su Termux

## 📋 Passo 1: Aggiorna Termux
```bash
pkg update && pkg upgrade -y
```

## 📦 Passo 2: Installa le Dipendenze
```bash
pkg install python3 nmap arp-scan -y
```

## 📁 Passo 3: Vai nella Cartella del Tool
```bash
cd "/sdcard/Download"  # o dove hai salvato x_dead.py
# oppure se è nella home:
cd ~
```

## 🔐 Passo 4: Dai i Permessi (Opzionale ma Consigliato)
Per funzionalità avanzate, Termux potrebbe richiedere permessi root. Per ora prova senza root:
```bash
# Se hai root access:
su
```

## ▶️ Passo 5: Avvia X DEAD
```bash
python3 x_dead.py
```

## ⚠️ Note Importanti:

1. **Permessi di Storage**: Se il tool non trova la rete, potresti dover dare permessi:
   ```bash
   termux-setup-storage
   ```

2. **Permessi di Root**: Alcune funzionalità richiedono root. Se non funziona, prova:
   ```bash
   su
   python3 x_dead.py
   ```

3. **Interfaccia di Rete**: Su Termux, l'interfaccia potrebbe essere `wlan0` o `rmnet0`. Se la scansione automatica non funziona, inserisci manualmente:
   - Network: `192.168.1.0/24` (sostituisci con la tua rete)
   - Interface: `wlan0` (o quella che vedi con `ip addr`)

## 🔍 Verifica la Tua Interfaccia di Rete:
```bash
ip addr show
```
Cerca l'interfaccia con un indirizzo IP (non 127.0.0.1)

## ✅ Comandi Rapidi (Copia e Incolla):
```bash
pkg update && pkg upgrade -y && pkg install python3 nmap arp-scan -y && python3 x_dead.py
```

---

**Buon Hacking! 🎯**
*Created by: Infinity X Team White Devel*


# 📤 Come Pubblicare X DEAD su GitHub

## 🎯 Guida Completa per Pubblicare il Repository

### Passo 1: Crea un Account GitHub (se non ce l'hai)

1. Vai su [github.com](https://github.com)
2. Clicca su "Sign up"
3. Crea il tuo account

### Passo 2: Crea un Nuovo Repository

1. Clicca sul pulsante **"+"** in alto a destra
2. Seleziona **"New repository"**
3. Inserisci:
   - **Repository name**: `X-DEAD` (o come preferisci)
   - **Description**: `Powerful Network Control System for Kali Linux and Termux`
   - **Visibility**: Pubblica (Public) o Privata (Private)
   - **NON** spuntare "Initialize with README" (abbiamo già il nostro)
4. Clicca **"Create repository"**

### Passo 3: Installa Git (se non ce l'hai)

#### Su Kali Linux:
```bash
sudo apt-get install git -y
```

#### Su Windows:
Scarica da: https://git-scm.com/download/win

### Passo 4: Configura Git (Prima Volta)

```bash
git config --global user.name "Il Tuo Nome"
git config --global user.email "tua.email@example.com"
```

### Passo 5: Inizializza il Repository Locale

Apri il terminale nella cartella del progetto e esegui:

```bash
# Inizializza git
git init

# Aggiungi tutti i file
git add .

# Fai il primo commit
git commit -m "Initial commit: X DEAD v1.0 - Network Control System"
```

### Passo 6: Collega al Repository GitHub

GitHub ti mostrerà i comandi. Sostituisci `TUO_USERNAME` con il tuo username:

```bash
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git
git branch -M main
git push -u origin main
```

### Passo 7: Carica i File

```bash
git push -u origin main
```

Ti chiederà username e password di GitHub.

---

## 📁 File da Includere nel Repository

Assicurati di avere questi file:

- ✅ `x_dead.py` - Il tool principale
- ✅ `README.md` - Documentazione principale
- ✅ `INSTALL.md` - Guida installazione dettagliata
- ✅ `QUICKSTART.md` - Guida rapida
- ✅ `LICENSE` - Licenza
- ✅ `.gitignore` - File da ignorare
- ✅ `start_termux.sh` - Script per Termux (opzionale)
- ✅ `install.sh` - Script per Kali (opzionale)

---

## 🎨 Migliora il Repository

### Aggiungi Badge (Opzionale)

Nel README.md ho già aggiunto alcuni badge. Puoi personalizzarli.

### Aggiungi Screenshots

1. Fai screenshot del tool in azione
2. Salvali nella cartella `screenshots/`
3. Aggiungi i link nel README.md

### Aggiungi Topics/Tags

Quando pubblichi, aggiungi questi topics:
- `network-scanner`
- `kali-linux`
- `termux`
- `python`
- `cybersecurity`
- `ethical-hacking`
- `network-discovery`

---

## 🔄 Aggiornare il Repository (Dopo Modifiche)

Quando modifichi i file:

```bash
# Aggiungi i file modificati
git add .

# Fai commit
git commit -m "Descrizione delle modifiche"

# Carica su GitHub
git push
```

---

## 📝 Esempio di Comandi Completi

```bash
# 1. Vai nella cartella del progetto
cd "C:\Users\adil\Desktop\kali linux tool"

# 2. Inizializza git
git init

# 3. Aggiungi tutti i file
git add .

# 4. Fai il primo commit
git commit -m "Initial commit: X DEAD v1.0"

# 5. Collega a GitHub (sostituisci TUO_USERNAME)
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git

# 6. Carica su GitHub
git push -u origin main
```

---

## ✅ Checklist Pre-Pubblicazione

- [ ] Tutti i file sono presenti
- [ ] README.md è completo e chiaro
- [ ] INSTALL.md ha istruzioni dettagliate
- [ ] Il codice funziona su Kali Linux
- [ ] Il codice funziona su Termux
- [ ] LICENSE è incluso
- [ ] .gitignore è configurato
- [ ] Hai testato l'installazione

---

## 🆘 Problemi Comuni

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TUO_USERNAME/X-DEAD.git
```

### "Authentication failed"
Usa un Personal Access Token invece della password:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Genera un nuovo token
3. Usalo come password

### "Permission denied"
Verifica di avere i permessi sul repository GitHub.

---

**Buona pubblicazione! 🚀**

*Created by: Infinity X Team White Devel*


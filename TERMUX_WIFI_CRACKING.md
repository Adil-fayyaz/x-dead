# 📱 WiFi Password Cracking su Termux - Guida Completa

## ⚠️ IMPORTANTE: Limitazioni di Termux

WiFi password cracking su Termux ha **limitazioni significative** rispetto a Kali Linux:

### ❌ Cosa NON funziona su Termux:
- ❌ **Monitor mode** (richiede root e hardware supportato)
- ❌ **Cattura handshake in tempo reale** (limitazioni Android)
- ❌ **WPS PIN Attack** (reaver non sempre disponibile)
- ❌ **Full aircrack-ng suite** (non sempre installabile)

### ✅ Cosa FUNZIONA su Termux:
- ✅ **Dictionary Attack** (se hai un file .cap già catturato)
- ✅ **WiFi Network Scanning** (vedere le reti)
- ✅ **Password cracking su handshake già catturato**

---

## 🔧 Come Funziona su Termux

### Metodo 1: Dictionary Attack (FUNZIONA!)

Questo metodo **funziona** su Termux se hai già un file handshake (.cap):

1. **Avvia X DEAD:**
   ```bash
   python3 x_dead.py
   ```

2. **Vai in Advanced Options:**
   - Premi `5`
   - Premi `2` (WiFi Password Cracking)

3. **Scegli Dictionary Attack:**
   - Premi `1`

4. **Inserisci i file:**
   - Handshake file: percorso del file `.cap`
   - Wordlist: percorso del file wordlist (es: `rockyou.txt`)

5. **Il tool proverà a crackare la password!**

---

## 📥 Installazione Tool per Termux

### Opzione 1: Prova a installare aircrack-ng

```bash
pkg install aircrack-ng
```

**Nota:** Potrebbe non essere disponibile su Termux. Se non funziona, usa l'opzione 2.

### Opzione 2: Usa hashcat (Alternativa)

```bash
pkg install hashcat
```

Hashcat può crackare handshake WPA/WPA2 se convertiti nel formato giusto.

### Opzione 3: Usa wordlist online

Se non hai una wordlist:

```bash
# Scarica rockyou.txt
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

---

## 🎯 Workflow Completo su Termux

### Passo 1: Ottieni un Handshake

**SU TERMUX NON PUOI CATTURARE HANDSHAKE!**

Devi:
- Catturare l'handshake su Kali Linux
- Oppure scaricare un file .cap già catturato (per test)
- Trasferire il file .cap su Termux

### Passo 2: Prepara la Wordlist

```bash
# Scarica una wordlist
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# O crea una piccola wordlist di test
echo -e "password123\nadmin123\nwifi123" > wordlist.txt
```

### Passo 3: Usa X DEAD per Crackare

1. Avvia X DEAD
2. Advanced Options → WiFi Password Cracking
3. Dictionary Attack
4. Inserisci percorso file .cap
5. Inserisci percorso wordlist
6. Aspetta il risultato!

---

## 🔍 Alternative su Termux

### Se aircrack-ng non funziona:

#### Metodo 1: Usa hashcat

```bash
# Converti .cap in .hccapx (formato hashcat)
cap2hccapx capture.cap output.hccapx

# Cracka con hashcat
hashcat -m 2500 output.hccapx wordlist.txt
```

#### Metodo 2: Usa John the Ripper

```bash
pkg install john
# Converti e cracka (metodo più complesso)
```

---

## ⚠️ Limitazioni Hardware Android

Anche con root, Android ha limitazioni:

1. **Driver WiFi:** Molti dispositivi Android non supportano monitor mode
2. **Restrizioni Kernel:** Android limita l'accesso alle interfacce wireless
3. **Chipset WiFi:** Solo alcuni chipset supportano monitor mode

---

## 💡 Suggerimenti

### Per Test Completi:
1. **Usa Kali Linux** per catturare handshake
2. **Trasferisci il file .cap** su Termux
3. **Usa Termux** per il dictionary attack (più portabile)

### Per Cattura Handshake:
- **Kali Linux** (consigliato)
- **Dispositivo con chipset compatibile** (es: alcune USB WiFi adapter)

---

## ✅ Checklist Termux WiFi Cracking

- [ ] File .cap (handshake già catturato)
- [ ] Wordlist file (rockyou.txt o altro)
- [ ] aircrack-ng o hashcat installato
- [ ] X DEAD avviato
- [ ] Dictionary Attack selezionato

---

## 🆘 Problemi Comuni

### "aircrack-ng not found"
**Soluzione:**
- Prova: `pkg install aircrack-ng`
- Se non disponibile, usa hashcat
- Oppure usa Kali Linux

### "Cannot open handshake file"
**Soluzione:**
- Verifica il percorso del file
- Assicurati che il file .cap sia valido
- Controlla i permessi del file

### "Monitor mode not supported"
**Soluzione:**
- Su Termux, monitor mode spesso non funziona
- Usa Kali Linux per catturare handshake
- Termux è utile solo per il dictionary attack

---

## 📚 Risorse

- **Wordlist:** https://github.com/brannondorsey/naive-hashcat
- **Handshake Samples:** Cerca su internet per file .cap di test
- **Hashcat:** https://hashcat.net/hashcat/

---

## 🎓 Conclusione

**Termux è limitato per WiFi cracking completo**, ma può essere usato per:
- ✅ Dictionary attacks su handshake già catturati
- ✅ Testing e apprendimento
- ✅ Password cracking portatile

**Per funzionalità complete, usa Kali Linux!**

---

*Created by: Infinity X Team White Devel*


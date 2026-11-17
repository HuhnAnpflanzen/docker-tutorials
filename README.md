# Git & GitHub – Befehle für VS Code

Diese README enthält die wichtigsten Git-Befehle für die Arbeit mit GitHub über das integrierte Terminal von Visual Studio Code.

## 1. Repository-Informationen anzeigen

| Befehl | Beschreibung |
|---|---|
| `git status` | Zeigt den aktuellen Status und geänderte Dateien |
| `git branch` | Zeigt alle lokalen Branches |
| `git branch --show-current` | Zeigt den aktuell verwendeten Branch |
| `git branch -a` | Zeigt alle lokalen und Remote-Branches |
| `git log --oneline` | Zeigt die bisherigen Commits in Kurzform |
| `git log --oneline --graph --all` | Zeigt die Commit-Historie als Graph |
| `git remote -v` | Zeigt die verbundenen Remote-Repositories |
| `git rev-parse --show-toplevel` | Zeigt das Stammverzeichnis des Repositories |

## 2. Änderungen überprüfen

| Befehl | Beschreibung |
|---|---|
| `git diff` | Zeigt Änderungen an noch nicht vorgemerkten Dateien |
| `git diff --staged` | Zeigt Änderungen, die bereits für einen Commit vorgemerkt sind |
| `git status` | Zeigt, welche Dateien geändert, neu oder gelöscht wurden |

## 3. Änderungen committen (lokal speichern)

Ein Commit speichert einen bestimmten Stand deiner Änderungen in der lokalen Git-Historie.

```bash
# Alle Änderungen vormerken
git add .

# Nur eine bestimmte Datei vormerken
git add datei.py

# Commit erstellen
git commit -m "Beschreibung der Änderungen"
```

Beispiel:

```bash
git add .
git commit -m "Implementierung der Datenbankverbindung"
```

## 4. Änderungen zu GitHub hochladen (Push)

Mit Push überträgst du deine lokalen Commits zu GitHub.

```bash
# Aktuellen Branch zu GitHub pushen
git push
```

Beim ersten Push eines neuen Branches:

```bash
git push -u origin mein-branch
```

`origin` bezeichnet normalerweise das verbundene Remote-Repository.

`-u` verknüpft deinen lokalen Branch mit dem Remote-Branch. Bei zukünftigen Pushes reicht dann `git push`.

## 5. Änderungen von GitHub herunterladen (Pull)

Mit Pull holst du Änderungen vom Remote-Repository und integrierst sie in deinen aktuellen Branch.

```bash
# Änderungen des verbundenen Remote-Branches herunterladen
git pull
```

Alternativ kannst du den Branch explizit angeben:

```bash
git pull origin main
```

## 6. Änderungen vom Remote-Repository abrufen (Fetch)

Fetch lädt Informationen über neue Commits und Branches von GitHub herunter, ohne deine lokalen Dateien zu verändern.

```bash
git fetch
```

Unterschied:
- `git fetch`: Ruft neue Informationen ab, integriert sie aber nicht.
- `git pull`: Ruft neue Informationen ab und integriert die Änderungen in deinen aktuellen Branch.

## 7. Mit Branches arbeiten

Branches ermöglichen es, unabhängig vom Hauptentwicklungszweig an neuen Funktionen zu arbeiten.

```bash
# Neuen Branch erstellen
git branch mein-branch

# Zu einem anderen Branch wechseln
git switch main

# Neuen Branch erstellen und direkt wechseln
git switch -c mein-branch

# Branch löschen (lokal)
git branch -d mein-branch
```

Beispiel:

```bash
git switch -c feature/database
```

## 8. Änderungen rückgängig machen

```bash
# Änderungen einer Datei verwerfen (nicht vorgemerkte Änderungen)
git restore datei.py

# Vormerkung einer Datei aufheben
git restore --staged datei.py

# Letzten Commit rückgängig machen, Änderungen aber behalten
git reset --soft HEAD~1
```

**Achtung:** `git restore` verwirft lokale Änderungen unwiderruflich. Vorher gegebenenfalls eine Sicherung erstellen.

## 9. Repository einrichten

Falls noch kein Git-Repository existiert:

```bash
# Git-Repository initialisieren
git init

# GitHub-Repository als Remote hinzufügen
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Git-Benutzerinformationen einmalig konfigurieren:

```bash
git config --global user.name "Dein Name"
git config --global user.email "deine-email@example.com"
```

Bereits vorhandenes Remote-Repository anzeigen:

```bash
git remote -v
```

## 10. Typischer Git-Workflow in VS Code

Das ist der Ablauf, den du im Alltag wahrscheinlich am häufigsten verwenden wirst:

**Schritt 1 – Aktuellen Status überprüfen**

```bash
git status
```

**Schritt 2 – Aktuellen Branch überprüfen**

```bash
git branch --show-current
```

**Schritt 3 – Änderungen von GitHub holen**

```bash
git pull
```

**Schritt 4 – Code bearbeiten**

Änderungen in VS Code durchführen.

**Schritt 5 – Änderungen vormerken**

```bash
git add .
```

**Schritt 6 – Commit erstellen**

```bash
git commit -m "Beschreibung der Änderungen"
```

**Schritt 7 – Änderungen zu GitHub hochladen**

```bash
git push
```

---

## Merkhilfe

| Begriff | Bedeutung |
|---|---|
| Repository | Projekt, das mit Git versioniert wird |
| Branch | Separater Entwicklungszweig |
| Commit | Lokale Speicherung eines bestimmten Entwicklungsstands |
| Push | Lokale Commits zu GitHub hochladen |
| Pull | Änderungen von GitHub abrufen und integrieren |
| Fetch | Änderungen von GitHub abrufen, ohne sie zu integrieren |
| Merge | Zwei Entwicklungszweige zusammenführen |
| Remote | Verknüpftes Repository auf GitHub |

**Wichtig:** Git speichert Commits zunächst lokal auf deinem Computer. Erst durch `git push` werden sie zu GitHub übertragen.

# Docker Cheat Sheet (Tutorials 01–06)

## 1. Dockerfile vs. Docker Compose

Kurz gesagt: Das **Dockerfile** baut *einen einzelnen* Baustein, **Docker Compose** setzt *alle Bausteine* zu einer funktionierenden Anwendung zusammen.

| Merkmal | `Dockerfile` | `compose.yaml` (Docker Compose) |
|---|---|---|
| **Zweck** | Bauplan für **ein einzelnes Image** | Orchestrierung von **mehreren Containern** |
| **Inhalt** | Basis-Image (`FROM`), Code kopieren (`COPY`), Pakete installieren (`RUN`), Startbefehl (`CMD`) | Services, Ports (`ports`), Umgebungsvariablen (`environment`), Netzwerke, Volumes, `depends_on` |
| **Zeitpunkt** | **Build-Zeit** (`docker build`) | **Laufzeit** (`docker compose up`) |
| **Analogie** | Das Rezept für *ein* Gericht | Der Menüplan für ein ganzes Abendessen |

---

## 2. Die wichtigsten Flags (Schalter)

| Flag | Langform | Bedeutung |
|---|---|---|
| `-d` | `--detach` | Startet den Container im Hintergrund (Terminal bleibt frei). |
| `-p` | `--publish` | Verbindet Ports nach dem Schema `Host:Container` (z. B. `-p 8080:8000`). |
| `--rm` | – | Löscht den Container automatisch, sobald er beendet wird. |
| `--name` | – | Vergibt einen festen Namen für den Container. |
| `-t` | `--tag` | Vergibt Namen und Version beim Bauen (z. B. `-t shopping-api:v1`). |
| `-it` | `--interactive --tty` | Öffnet eine interaktive Terminal-Sitzung im Container. |
| `-e` | `--env` | Übergibt eine Umgebungsvariable (z. B. `-e BACKEND_URL=...`). |
| `-f` | `--force` / `--file` | Erzwingt Aktionen (z. B. `rm -f`) oder wählt bei Compose eine andere Datei. |
| `-a` | `--all` | Zeigt alle Einträge (z. B. auch gestoppte Container) oder löscht alles Ungenutzte. |
| `-q` | `--quiet` | Gibt nur die reinen IDs aus (praktisch für Skripte). |

---

## 3. Container-Grundlagen & Lebenszyklus

| Befehl | Beschreibung |
|---|---|
| `docker run -d --name <name> -p 8080:80 <image>` | Startet einen Container im Hintergrund mit Namen und Port-Weiterleitung. |
| `docker run -it --rm <image> sh` | Startet einen Wegwerf-Container mit interaktiver Shell. |
| `docker ps` | Zeigt alle aktuell **laufenden** Container. |
| `docker ps -a` | Zeigt **alle** Container (auch gestoppte). |
| `docker stop <container>` | Stoppt einen laufenden Container sauber. |
| `docker rm <container>` | Löscht einen gestoppten Container. |
| `docker rm -f <container>` | Stoppt und löscht einen laufenden Container sofort. |
| `docker logs <container>` | Zeigt die Ausgaben/Logs eines Containers an. |

---

## 4. Images & Bauen

| Befehl | Beschreibung |
|---|---|
| `docker build -t <name>:<tag> <ordner>` | Baut ein Image aus dem `Dockerfile` im angegebenen Ordner (`.` für aktuellen Ordner). |
| `docker images` | Listet alle lokal gespeicherten Images auf. |
| `docker tag <alt> <neu>:<tag>` | Vergibt einen weiteren Namen/Tag für ein bestehendes Image. |
| `docker rmi <image>` | Löscht ein Image (nur möglich, wenn kein Container mehr darauf verweist). |
| `docker history <image>` | Zeigt alle Layer eines Images und wie sie entstanden sind. |

---

## 5. In Container hineinschauen (Debugging)

| Befehl | Beschreibung |
|---|---|
| `docker exec <container> <befehl>` | Führt einen einzelnen Befehl in einem laufenden Container aus. |
| `docker exec -it <container> sh` | Öffnet eine interaktive Shell in einem laufenden Container. |
| `docker diff <container>` | Zeigt alle Datei-Änderungen (`C` changed, `A` added, `D` deleted) im Container. |
| `docker container inspect <container>` | Zeigt detaillierte Metadaten (z. B. IP-Adressen, Netzwerke) eines Containers. |

---

## 6. Netzwerke

| Befehl | Beschreibung |
|---|---|
| `docker network create <name>` | Erstellt ein eigenes Netzwerk (inkl. automatischem DNS über Container-Namen). |
| `docker network ls` | Listet alle Docker-Netzwerke auf. |
| `docker network connect <netz> <container>` | Verbindet einen laufenden Container mit einem Netzwerk. |
| `docker run --network <netz> ...` | Startet einen neuen Container direkt im angegebenen Netzwerk. |
| `docker network inspect <netz>` | Zeigt Details zum Netzwerk und alle verbundenen Container inkl. IP. |
| `docker network rm <netz>` | Löscht ein ungenutztes Netzwerk. |

---

## 7. Aufräumen & Speicherplatz

| Befehl | Beschreibung |
|---|---|
| `docker system df` | Zeigt den Speicherverbrauch von Images, Containern, Volumes und Build Cache. |
| `docker rm -f $(docker ps -aq)` | Stoppt und löscht **alle** Container auf einmal. |
| `docker container prune` | Löscht alle gestoppten Container. |
| `docker image prune` / `docker image prune -a` | Löscht unbenannte (*dangling*) Images / alle ungenutzten Images. |
| `docker network prune` | Löscht alle ungenutzten Netzwerke. |
| `docker volume prune` / `docker volume prune -a` | Löscht ungenutzte anonyme Volumes / auch benannte Volumes. |
| `docker builder prune` | Löscht den Build Cache. |
| `docker system prune` | Löscht gestoppte Container, ungenutzte Netzwerke, *dangling* Images und Cache. |
| `docker system prune -a --volumes` | Radikaler Reset: löscht alles, was aktuell nicht in Benutzung ist. |

---

## 8. Docker Compose

| Befehl | Beschreibung |
|---|---|
| `docker compose up -d` | Erstellt Netzwerk, baut/pullt fehlende Images und startet alle Services im Hintergrund. |
| `docker compose up -d --build` | Erzwingt vor dem Start ein Neubauen der Images (wichtig nach Code-Änderungen). |
| `docker compose down` | Stoppt und löscht Container sowie das Netzwerk (Images und Volumes bleiben erhalten). |
| `docker compose down -v` | Wie `down`, löscht aber zusätzlich die zugehörigen **Volumes**. |
| `docker compose ps` | Listet die Container des aktuellen Compose-Projekts auf. |
| `docker compose logs <service>` | Zeigt die Logs eines bestimmten Services. |
| `docker compose exec <service> <befehl>` | Führt einen Befehl in einem laufenden Compose-Service aus. |
| `docker compose -f <datei> ...` | Nutzt eine bestimmte Datei statt der standardmäßigen `compose.yaml`. |

### `build:` vs. `image:` in der `compose.yaml`
* **Nur `build:`** – baut das Image lokal aus dem Dockerfile (ideal für Entwicklung & PVL).
* **Nur `image:`** – nutzt ein lokales Image oder pullt es aus einer Registry; baut **nie** selbst.
* **`build:` + `image:`** – versucht erst zu pullen; falls nicht vorhanden, wird gebaut und mit dem `image:`-Namen getaggt.
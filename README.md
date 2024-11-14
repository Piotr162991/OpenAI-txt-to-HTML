# OpenAI-txt-to-HTML
## Opis Projektu
Ten skrypt w Pythonie korzysta z modelu GPT od OpenAI do generowania fragmentu HTML na podstawie opisu tekstowego zawartego w zewnętrznym pliku **tresc.txt**. Wygenerowany kod HTML jest zbudowany poprzez użycie tagów HTML, bez umieszczania znaczników \<html>, \<head> i \<body>. Wynikowy HTML zapisywany jest w pliku **artykul.html** w głównym katalogu projektu.
### Zadanie dodtkowe "szablon dla artykułu"
Dodatkowo w repozytorium znajduje się przykładowy szablon postu na bloga **blog-post.html**, który pokazuje zastosowanie wygenerowanego kodu HTML. Szablon zawiera plik CSS i JavaScript, znajdujące się w folderze assets, które odpowiadają za stylizację i funkcjonalność.

## Wymagania
1. Python 3.6+: Upewnij się, że Python jest zainstalowany.
2. Pakiet OpenAI dla Pythona: Skrypt używa SDK OpenAI do komunikacji z API.
3. Pakiet Dotenv: Wymagany do bezpiecznego zarządzania kluczem API.

Możesz zainstalować niezbędne pakiety, korzystając z poniższych komend:

```
pip install openai
pip install python-dotenv
```
## Konfiguracja
Klucz API: Uzyskaj klucz API OpenAI i zapisz go w pliku **.env** w katalogu głównym projektu:
```
OPENAI_API_KEY=twój_klucz_api
```
## Struktura Skryptu
- Wczytywanie Klucza API: Skrypt używa load_dotenv() do bezpiecznego przechowywania klucza API z pliku **.env**.
- Wczytywanie Tekstu: Skrypt czyta tekst z pliku **tresc.txt**, który służy jako "content" dla prompt'a do wygenerowania HTML.
- Opis Promptu: Skrypt definiuje szczegółową strukturę dla generowania HTML, w tym instrukcje formatowania oraz przykłady użycia tagów HTML, z miejscem na obrazy w formie placeholderów.
- Zapytanie do OpenAI API: Skrypt wysyła prompt do API OpenAI, wykorzystując chat.completions.create, aby wygenerować odpowiedź w formie HTML.
- Zapis Wyniku: Odpowiedź API jest zapisywana w pliku **artykul.html**, tworząc nowy plik lub nadpisując istniejący.
## Uruchamianie Skryptu
Aby uruchomić skrypt, wpisz poniższe polecenie:

```
python main.py
```
Upewnij się, że tresc.txt zawiera poprawny tekst promptu przed uruchomieniem skryptu. Po wykonaniu skryptu sprawdź plik **artykul.html** w katalogu projektu, aby zobaczyć wygenerowany kod HTML.

## Notatki
Skrypt jest skonfigurowany z temperaturą 0.7, co zapewnia zbalansowany poziom kreatywności.
Znaczniki obrazów (\<img>) w wygenerowanym HTML zawierają placeholder src="image_placeholder.jpg" oraz opisowy atrybut alt oparty na kontekście zawartym w tresc.txt.

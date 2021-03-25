# Panlex Scrape

## Panlex
The mission of PanLex, a project of The Long Now Foundation, is to overcome language barriers to human rights, information, and opportunities. After ten years of pooling together different sources from across the world, PanLex’s database covers over 2,500 dictionaries, 5,700 languages, 25 million words, and 1.3 billion translations. 

PanLex is a panlingual database (built to contain every language), and lexical (focused on words, not sentences).

## What this script does
Extract word dictionary from two language code available in panlex database <https://vocab.panlex.org/>

## Requirements
- beautifulsoup4
- requests
- tqdm

## How To Use
```
python scrape.py <language-code-1> <language-code-2>
```


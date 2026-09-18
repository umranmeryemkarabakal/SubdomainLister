# SubdomainLister

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Requests-2B5B84?style=for-the-badge" alt="Requests" />
</p>

## Overview

A wordlist-based subdomain finder: it tries each name in `subdomain.txt` against a target domain over HTTP and prints the ones that respond. Written as a networking exercise.

**Quick start:** `pip install -r requirements.txt && python main.py`

## Proje hakkında

`subdomain.txt` içindeki kelimeleri hedef alan adının önüne ekleyip HTTP isteği atan ve yanıt veren alt alan adlarını listeleyen bir alıştırma betiği.

## Özellikler

- Kelime listesiyle alt alan adı deneme
- Bağlantı hatalarını sessizce atlama
- Hedef alan adı `target_input` değişkeninden değiştirilebilir

## Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```bash
python main.py
```

## Dosya yapısı

```text
SubdomainLister/
├── main.py
└── subdomain.txt
```

## Notlar

- Yalnızca size ait ya da test izniniz olan alan adlarında kullanın.
